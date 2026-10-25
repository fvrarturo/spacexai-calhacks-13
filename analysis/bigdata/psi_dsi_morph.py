"""DECLIC-DSI (ISS, 2010-2011) axial-view cellular-pattern morphology at scale.

Data: NASA Physical Sciences Informatics (PSI) public bucket, DSI/Data/<activity>/.
Camera folders: *_HR2_k = axial view (looking down the growth axis onto the
solid-liquid front, cellular pattern visible); *_HR1 = side view. File names carry
a clock tick; ticks = 23 per second since 2009-01-01, derived from the PSI
'Solidification Plan' sheets (column SL2 = (Excel date - 39814) * 86400 * 23) and
checked against (a) the 3-min melt image period (4140 ticks) and (b) the first
S1 activity 1 frame (within 20 s of the planned step 1-1 command).

Per frame (streamed from S3, never stored):
  * 768x768 central crop, Gaussian high-pass (sigma 32 px), Hann window, 2-D FFT
  * radial power spectrum; robust power-law baseline; dominant peak in
    lambda = 12..160 px -> spacing lambda = N / k_peak (px)
  * prominence (dB above baseline), relative FWHM of the excess peak (positional order),
    2-fold angular anisotropy at the peak ring (stripe/artefact detector),
    6-fold orientational order |<e^{6i theta}>| on 3x3 tiles at k_peak vs an off-peak null.

    python -I psi_dsi_morph.py manifest --tsv psi-objects.tsv.gz --out dsi-hr2-manifest.tsv
    python -I psi_dsi_morph.py process --manifest dsi-hr2-manifest.tsv --shard 0 --nshards 24 --out shard-00.csv
"""
import argparse
import csv
import gzip
import io
import os
import re
import sys
import time
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor

BASE = 'https://nasa-psi.s3.us-west-2.amazonaws.com/'
TICKS_PER_S = 23.0
HP_SIGMA = 24          # px, Gaussian high-pass (removes illumination, keeps lambda <~ 110 px)
LAM_MIN, LAM_MAX = 12.0, 110.0   # px, search band for the cell-spacing peak
EXCEL_2009 = 39814.0          # Excel serial of 2009-01-01 (tick epoch)

# Experimental conditions per activity, transcribed from the PSI 'DSI-* Solidification Plan.xlsx'
# sheets (DSI/Data/). V = pulling rate; z = sample-holder position (mm) at start/end of the
# directional solidification step; sol_start = planned command date (Excel serial, same clock as
# the image ticks); sol_dur = planned duration (days).  Alloy: succinonitrile-0.24 wt% camphor
# (NASA Task Book FY2013 report, in DSI/Taskbook Downloads/).
RUNS = {
    'INIT activity 4': dict(plan='DSI-INIT step 4-3 DSI1_SOL', V=1.0, z0=69, z1=9, sol_start=40295.576249999998, sol_dur=0.69097222222222221),
    'S1 activity 1': dict(plan='DSI-S1 step 1-3 DSI1_SOL', V=6.0, z0=69, z1=9, sol_start=40324.420138888869, sol_dur=0.11574074074074074),
    'S1 activity 2': dict(plan='DSI-S1 step 2-3 DSI1_SOL', V=12.0, z0=69, z1=9, sol_start=40325.516435185164, sol_dur=0.057870370370370371),
    'S1 activity 3': dict(plan='DSI-S1 step 3-3 DSI1_SOL', V=16.0, z0=69, z1=9, sol_start=40326.577777777755, sol_dur=0.043402777777777783),
    'S1 activity 4': dict(plan='DSI-S1 step 4-3 DSI1_SOL', V=0.5, z0=69, z1=29, sol_start=40327.590624999975, sol_dur=0.92592592592592593),
    'S2 activity 4': dict(plan='DSI-S2 step 4-3 DSI1_SOL', V=1.0, z0=72, z1=30, sol_start=40461.042824074066, sol_dur=0.4861111111111111),
    'S2 activity 11': dict(plan='DSI-S2 step 11-3 DSI1_SOL', V=0.5, z0=72, z1=12.5, sol_start=40467.891203703693, sol_dur=1.3773148148148149),
    'HD activity 9': dict(plan='DSI-HD step 9-7 DSI1_SOL_VV', V=0.35, V2=0.75, z_jump=43, t_jump=40562.333074294511,
                          z0=73, z1=13, sol_start=40561.341010802447, sol_dur=1.4550264550264549),
}


def excel_to_tick(x):
    return (x - EXCEL_2009) * 86400 * TICKS_PER_S


def manifest(tsv, out):
    rows = []
    rx = re.compile(r'_HR2_(\d{9,10})_([12])\.bmp$')
    with gzip.open(tsv, 'rt') as f:
        for line in f:
            k, s, e, m = line.rstrip('\n').split('\t')
            if not k.startswith('DSI/Data/') or 'extracted by cbp' in k:
                continue
            mm = rx.search(k)
            if not mm:
                continue
            run = k.split('/')[2]
            rows.append((run, int(mm.group(1)), int(mm.group(2)), int(s), k))
    rows.sort()
    with open(out, 'w') as f:
        f.write('run\ttick\tmode\tsize\tkey\n')
        for r in rows:
            f.write('\t'.join(map(str, r)) + '\n')
    print(f'{len(rows)} HR2 frames, {sum(r[3] for r in rows)/1e9:.2f} GB')


# ---------------------------------------------------------------- per-frame features
_cache = {}


# Fixed-pattern artefacts (optical fringes, sensor pattern) recur at identical Fourier positions in
# frames of every run, e.g. a sharp spot at (ky, kx) = (9, 3) cycles per 768 px (lambda ~ 81 px).
# 'mask' learns them from data: per frame, P(k) / <P>_|k| (spectrum divided by its own radial mean);
# the 80th percentile of that ratio over frames sampled evenly from all 8 runs is ~1.6 for isotropic
# noise (exponential law) and stays low for structure confined to one run (<= 12.5 % of the sample),
# but is >> 1 at artefacts present in > 20 % of frames. Bins with q80 ratio > MASK_THR (dilated by
# one bin) are excluded (not zeroed) from every radial / angular statistic.
MASK_THR = 2.6
MASK_Q = 80
_MASK = {}


def load_mask(path):
    import numpy as np
    if path and os.path.exists(path):
        z = np.load(path)
        for key in z.files:
            _MASK[int(key.split('_')[1])] = z[key]
        _cache.clear()


def _geom(N):
    import numpy as np
    if N not in _cache:
        ky = np.fft.fftfreq(N) * N
        kx = np.fft.rfftfreq(N) * N
        KX, KY = np.meshgrid(kx, ky)
        K = np.hypot(KX, KY)
        TH = np.arctan2(KY, KX)          # (-pi/2, pi/2] on the rfft half plane
        w1 = np.hanning(N)
        ok = ~_MASK[N] if N in _MASK else np.ones(K.shape, bool)
        _cache[N] = (K, TH, np.outer(w1, w1).astype(np.float32), ok)
    return _cache[N]


def raw_power(y):
    import numpy as np
    N = y.shape[0]
    w1 = np.hanning(N)
    z = (y - y.mean()) * np.outer(w1, w1)
    return np.abs(np.fft.rfft2(z)) ** 2


def ratio_to_radial(P):
    import numpy as np
    N = P.shape[0]
    ky = np.fft.fftfreq(N) * N
    kx = np.fft.rfftfreq(N) * N
    KX, KY = np.meshgrid(kx, ky)
    idx = np.floor(np.hypot(KX, KY) + 0.5).astype(np.int32)
    s = np.bincount(idx.ravel(), weights=P.ravel())
    c = np.bincount(idx.ravel())
    with np.errstate(invalid='ignore', divide='ignore'):
        return P / (s / np.maximum(c, 1))[idx]


def build_mask(manifest_path, per_run, out):
    """Learn the fixed-artefact Fourier mask from frames sampled evenly across all runs."""
    import numpy as np
    from scipy.ndimage import binary_dilation, gaussian_filter
    rows = list(csv.DictReader(open(manifest_path), delimiter='\t'))
    by = {}
    for r in rows:
        if r['mode'] == '1':
            by.setdefault(r['run'], []).append(r)
    pick = []
    for run, l in sorted(by.items()):
        step = max(1, len(l) // per_run)
        pick += l[::step][:per_run]
    stacks = {768: [], 256: []}
    with ThreadPoolExecutor(8) as ex:
        for b in ex.map(lambda r: fetch(r['key'], int(r['size'])), pick):
            g = decode(b).astype(np.float32)
            c0 = (g.shape[0] - 768) // 2
            x = g[c0:c0 + 768, c0:c0 + 768]
            y = x - gaussian_filter(x, HP_SIGMA)
            if y.std() < 1e-3:
                continue                      # blank frame
            stacks[768].append(ratio_to_radial(raw_power(y)).astype(np.float32))
            for i in range(0, 768, 256):
                for j in range(0, 768, 256):
                    t = y[i:i + 256, j:j + 256]
                    if t.std() > 1e-3:
                        stacks[256].append(ratio_to_radial(raw_power(t)).astype(np.float32))
    res = {}
    for N, st in stacks.items():
        med = np.nanpercentile(np.stack(st), MASK_Q, axis=0)
        ky = np.fft.fftfreq(N) * N
        kx = np.fft.rfftfreq(N) * N
        KX, KY = np.meshgrid(kx, ky)
        m = (med > MASK_THR) & (np.hypot(KX, KY) >= 2)
        m = binary_dilation(m, iterations=1)
        res[f'mask_{N}'] = m
        res[f'median_{N}'] = med
        print(f'N={N}: {len(st)} frames, {int(m.sum())} masked bins; strongest:',
              [(int(KY.ravel()[i]), int(KX.ravel()[i]), round(float(med.ravel()[i]), 1))
               for i in np.argsort(med.ravel())[::-1][:8]], flush=True)
    np.savez_compressed(out, **{k: v for k, v in res.items() if k.startswith('mask')})
    np.savez_compressed(out.replace('.npz', '-median.npz'), **{k: v for k, v in res.items() if k.startswith('median')})
    return len(pick)


def spectrum(y):
    import numpy as np
    N = y.shape[0]
    K, TH, W, ok = _geom(N)
    z = (y - y.mean()) * W
    P = np.abs(np.fft.rfft2(z)) ** 2
    return P[ok], K[ok], TH[ok]


def radial(P, K, kmax):
    import numpy as np
    idx = np.floor(K * 2 + 0.5).astype(np.int32).ravel()   # half-integer annuli
    n = int(kmax * 2) + 1
    m = idx < n
    s = np.bincount(idx[m], weights=P.ravel()[m], minlength=n)
    c = np.bincount(idx[m], minlength=n)
    k = np.arange(n) / 2.0
    with np.errstate(invalid='ignore', divide='ignore'):
        pr = s / c
    return k, pr


def frame_features(img):
    import numpy as np
    from scipy.ndimage import gaussian_filter
    g = img.astype(np.float32)
    out = dict(mean=float(g.mean()), std=float(g.std()), p01=float(np.percentile(g, 1)),
               p99=float(np.percentile(g, 99)), sat=float(np.mean(g >= 254)))
    N = 768
    c0 = (g.shape[0] - N) // 2
    x = g[c0:c0 + N, c0:c0 + N]
    out['crop_std'] = float(x.std())
    y = x - gaussian_filter(x, HP_SIGMA)
    out['hp_std'] = float(y.std())
    if out['hp_std'] < 1e-3:
        return out
    P, K, TH = spectrum(y / out['hp_std'])
    lam_min, lam_max = LAM_MIN, LAM_MAX
    kmin, kmax = N / lam_max, N / lam_min
    k, pr = radial(P, K, kmax * 1.3)
    sel = (k >= kmin * 0.7) & (k <= kmax * 1.25) & np.isfinite(pr) & (pr > 0)
    lk, lp = np.log10(k[sel]), np.log10(pr[sel])
    # robust lower-envelope power-law baseline (iteratively drop points above the fit)
    keep = np.ones(lk.size, bool)
    for _ in range(6):
        a, b = np.polyfit(lk[keep], lp[keep], 1)
        r = lp - (a * lk + b)
        keep = r < np.percentile(r[keep], 70)
    base = a * lk + b
    exc = lp - base                              # log10 excess
    kk = k[sel]
    band = (kk >= kmin) & (kk <= kmax)
    i = int(np.argmax(np.where(band, exc, -np.inf)))
    # parabolic refinement in log k
    if 0 < i < exc.size - 1:
        y0, y1, y2 = exc[i - 1], exc[i], exc[i + 1]
        den = y0 - 2 * y1 + y2
        d = 0.5 * (y0 - y2) / den if den < 0 else 0.0
        d = max(-0.5, min(0.5, d))
        lkp = lk[i] + d * (lk[i + 1] - lk[i - 1]) / 2
    else:
        lkp = lk[i]
    kp = 10 ** lkp
    out['k_peak'] = float(kp)
    out['lambda_px'] = float(N / kp)
    out['prom_db'] = float(10 * exc[i])
    # FWHM of linear excess power (P/base - 1) around the peak
    lin = 10 ** exc - 1
    half = lin[i] / 2
    j0 = i
    while j0 > 0 and lin[j0] > half:
        j0 -= 1
    j1 = i
    while j1 < lin.size - 1 and lin[j1] > half:
        j1 += 1
    out['rel_fwhm'] = float((kk[j1] - kk[j0]) / kp) if lin[i] > 0 else float('nan')
    # excess-power-weighted centroid wavelength over the FWHM window
    wsl = slice(j0, j1 + 1)
    wgt = np.clip(lin[wsl], 0, None)
    out['lambda_centroid_px'] = float(N / (np.sum(kk[wsl] * wgt) / np.sum(wgt))) if wgt.sum() > 0 else float('nan')
    # angular structure at the peak ring
    ring = np.abs(K - kp) < 0.15 * kp
    Pr, Tr = P[ring], TH[ring]
    out['aniso2'] = float(np.abs(np.sum(Pr * np.exp(2j * Tr))) / np.sum(Pr))
    out['q6_global'] = float(np.abs(np.sum(Pr * np.exp(6j * Tr))) / np.sum(Pr))
    # local 6-fold orientational order on 3x3 tiles of 256 px, at k_peak and an off-peak null (1.7 k_peak)
    T = 256
    q6, q6n = [], []
    for r0 in range(0, N, T):
        for s0 in range(0, N, T):
            t = y[r0:r0 + T, s0:s0 + T]
            Pt, Kt, Tt = spectrum(t / (t.std() + 1e-6))
            for kt, acc in ((kp * T / N, q6), (1.7 * kp * T / N, q6n)):
                rg = np.abs(Kt - kt) < 0.2 * kt
                if rg.sum() >= 12:
                    acc.append(float(np.abs(np.sum(Pt[rg] * np.exp(6j * Tt[rg]))) / np.sum(Pt[rg])))
    out['q6_tiles'] = float(np.mean(q6)) if q6 else float('nan')
    out['q6_tiles_null'] = float(np.mean(q6n)) if q6n else float('nan')
    return out


def fetch(key, size, tries=6):
    url = BASE + urllib.parse.quote(key, safe='/')
    for i in range(tries):
        try:
            with urllib.request.urlopen(url, timeout=120) as r:
                b = r.read()
            if len(b) != size:
                raise IOError(f'size mismatch {len(b)} != {size}')
            return b
        except Exception:
            if i == tries - 1:
                raise
            time.sleep(2 ** i)


def decode(b):
    import numpy as np
    from PIL import Image
    with Image.open(io.BytesIO(b)) as im:
        return np.asarray(im.convert('L'))


def disk_fit(img):
    """Circle fit to the bright sample-disk edge (homogenisation frames, liquid sample).
    Otsu-like threshold on the smoothed frame, largest bright component, algebraic (Kasa) least-squares
    circle through its boundary pixels that do not touch the frame border."""
    import numpy as np
    from scipy import ndimage as ndi
    g = ndi.gaussian_filter(img.astype(np.float32), 3)
    h, e = np.histogram(g, 256)
    c = (e[:-1] + e[1:]) / 2
    w0 = np.cumsum(h)
    w1 = w0[-1] - w0
    m0 = np.cumsum(h * c) / np.maximum(w0, 1)
    m1 = (np.sum(h * c) - np.cumsum(h * c)) / np.maximum(w1, 1)
    thr = c[np.argmax(w0 * w1 * (m0 - m1) ** 2)]
    b = g > thr
    lab, n = ndi.label(b)
    if n == 0:
        return None
    big = lab == (np.argmax(np.bincount(lab.ravel())[1:]) + 1)
    big = ndi.binary_fill_holes(big)
    edge = big & ~ndi.binary_erosion(big)
    yy, xx = np.nonzero(edge)
    H, W = img.shape
    k = (yy > 3) & (yy < H - 4) & (xx > 3) & (xx < W - 4)
    yy, xx = yy[k].astype(float), xx[k].astype(float)
    if yy.size < 200:
        return None
    A = np.c_[2 * xx, 2 * yy, np.ones_like(xx)]
    sol, *_ = np.linalg.lstsq(A, xx ** 2 + yy ** 2, rcond=None)
    cx, cy, cc = sol
    R = float(np.sqrt(cc + cx ** 2 + cy ** 2))
    res = np.hypot(xx - cx, yy - cy) - R
    return dict(cx=float(cx), cy=float(cy), diameter_px=2 * R, rms_px=float(res.std()), edge_pts=int(yy.size),
                frac_bright=float(big.mean()), thr=float(thr), saturated=float(np.mean(img >= 254)))


def calib(manifest_path, out, idx=(15, 20, 25, 30, 35)):
    import json
    import numpy as np
    rows = list(csv.DictReader(open(manifest_path), delimiter='\t'))
    by = {}
    for r in rows:
        if r['mode'] == '1':
            by.setdefault(r['run'], []).append(r)
    res = {}
    for run, l in sorted(by.items()):
        l.sort(key=lambda r: int(r['tick']))
        fits = []
        for i in idx:
            f = disk_fit(decode(fetch(l[i]['key'], int(l[i]['size']))))
            if f:
                f['key'] = l[i]['key']
                fits.append(f)
        # saturated frames bloom and inflate the disk; keep unsaturated, well-fitting edges only
        good = [f for f in fits if f['rms_px'] < 15 and 0.3 < f['frac_bright'] < 0.95 and f['saturated'] < 0.005]
        d = [f['diameter_px'] for f in good]
        res[run] = dict(fits=fits, n_good=len(good), diameter_px_median=float(np.median(d)) if d else None,
                        diameter_px_range=[float(min(d)), float(max(d))] if d else None)
        print(run, res[run]['n_good'], res[run]['diameter_px_median'], res[run]['diameter_px_range'], flush=True)
    allg = [f['diameter_px'] for v in res.values() for f in v['fits']
            if f['rms_px'] < 15 and 0.3 < f['frac_bright'] < 0.95 and f['saturated'] < 0.005]
    res['_global'] = dict(n_frames=len(allg), runs=[k for k, v in res.items() if v['n_good']],
                          diameter_px_median=float(np.median(allg)), diameter_px_sd=float(np.std(allg)),
                          assumed_sample_diameter_mm=10.0,
                          um_per_px=10000.0 / float(np.median(allg)),
                          note='Assumes the bright disk seen in homogenisation frames is the 10-mm-diameter sample '
                               '(PSI DSI Science Requirements Document: 10 mm bulk samples). Our calibration, not an official PSI value.')
    print(res['_global'])
    json.dump(res, open(out, 'w'), indent=1)


FIELDS = ['run', 'tick', 'mode', 'key', 'bytes', 'mean', 'std', 'p01', 'p99', 'sat', 'crop_std', 'hp_std', 'k_peak',
          'lambda_px', 'lambda_centroid_px', 'prom_db', 'rel_fwhm', 'aniso2', 'q6_global', 'q6_tiles', 'q6_tiles_null',
          'error']


def process(manifest_path, shard, nshards, out, modes=(1, 2), deadline=None):
    rows = []
    with open(manifest_path) as f:
        rd = csv.DictReader(f, delimiter='\t')
        for j, r in enumerate(rd):
            if j % nshards == shard and int(r['mode']) in modes:
                rows.append(r)
    done = set()
    if os.path.exists(out):                     # resumable
        with open(out) as f:
            done = {r['key'] for r in csv.DictReader(f)}
    todo = [r for r in rows if r['key'] not in done]
    print(f'shard {shard}/{nshards}: {len(rows)} frames, {len(todo)} to do', flush=True)
    t0 = time.time()
    nbytes = 0
    new = not os.path.exists(out)
    with open(out, 'a', newline='') as fo, ThreadPoolExecutor(4) as ex:
        w = csv.DictWriter(fo, fieldnames=FIELDS, extrasaction='ignore')
        if new:
            w.writeheader()
        futs = [ex.submit(fetch, r['key'], int(r['size'])) for r in todo[:8]]
        for n, r in enumerate(todo):
            if deadline and time.time() - t0 > deadline:
                print(f'deadline reached after {n} frames; resubmit to continue', flush=True)
                break
            if n + 8 < len(todo):
                futs.append(ex.submit(fetch, todo[n + 8]['key'], int(todo[n + 8]['size'])))
            rec = dict(run=r['run'], tick=r['tick'], mode=r['mode'], key=r['key'])
            try:
                b = futs[n].result()
                futs[n] = None
                nbytes += len(b)
                rec['bytes'] = len(b)
                rec.update(frame_features(decode(b)))
            except Exception as e:  # keep going; record the failure
                rec['error'] = repr(e)[:200]
            w.writerow({k: (f'{v:.6g}' if isinstance(v, float) else v) for k, v in rec.items()})
            fo.flush()
            if n % 100 == 0:
                el = time.time() - t0
                print(f'{n}/{len(todo)} {nbytes/1e9:.2f} GB {el:.0f}s {n/max(el,1):.2f} fr/s', flush=True)
    print(f'shard {shard} done: {len(todo)} frames, {nbytes} bytes, {time.time()-t0:.0f}s', flush=True)


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest='cmd', required=True)
    m = sub.add_parser('manifest')
    m.add_argument('--tsv', required=True)
    m.add_argument('--out', required=True)
    p = sub.add_parser('process')
    p.add_argument('--manifest', required=True)
    p.add_argument('--shard', type=int, required=True)
    p.add_argument('--nshards', type=int, required=True)
    p.add_argument('--out', required=True)
    p.add_argument('--modes', default='1,2')
    p.add_argument('--deadline', type=float, help='stop cleanly after this many seconds')
    p.add_argument('--mask')
    k = sub.add_parser('mask')
    k.add_argument('--manifest', required=True)
    k.add_argument('--per-run', type=int, default=60)
    k.add_argument('--out', required=True)
    c = sub.add_parser('calib')
    c.add_argument('--manifest', required=True)
    c.add_argument('--out', required=True)
    t = sub.add_parser('test')
    t.add_argument('--mask')
    t.add_argument('files', nargs='+')
    a = ap.parse_args()
    if a.cmd == 'manifest':
        manifest(a.tsv, a.out)
    elif a.cmd == 'calib':
        calib(a.manifest, a.out)
    elif a.cmd == 'mask':
        build_mask(a.manifest, a.per_run, a.out)
    elif a.cmd == 'process':
        load_mask(a.mask)
        process(a.manifest, a.shard, a.nshards, a.out, tuple(int(x) for x in a.modes.split(',')), a.deadline)
        os._exit(0)   # do not wait for in-flight prefetches after a deadline stop
    else:
        from PIL import Image
        import numpy as np
        load_mask(a.mask)
        for fn in a.files:
            t0 = time.time()
            f = frame_features(np.asarray(Image.open(fn).convert('L')))
            print(fn.rsplit('/', 1)[-1], {k: round(v, 3) for k, v in f.items()}, f'{time.time()-t0:.2f}s')


if __name__ == '__main__':
    sys.exit(main())
