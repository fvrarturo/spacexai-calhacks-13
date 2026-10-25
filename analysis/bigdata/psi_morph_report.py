"""Aggregate per-frame DSI FFT features into per-run time series and run-level results.

Unit of analysis = the run (activity). Frames inside a run are strongly correlated (the same
cells are imaged every few seconds), so within-run statistics are descriptive only; any
cross-run statement uses one number per run.
"""
import csv
import gzip
import json
import math
import random
import statistics
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from psi_dsi_morph import RUNS, TICKS_PER_S, excel_to_tick  # noqa: E402

# Frame accepted as showing a cellular pattern (thresholds fixed after eye validation, see appendix):
PROM_MIN = 10.0      # dB above the power-law baseline
ANISO_MAX = 0.30     # 2-fold anisotropy at the peak ring (stripes / fringes are > 0.4)
FWHM_MIN = 0.10      # relative FWHM; residual fixed artefacts are sharper than this
HP_MIN = 4.0         # high-pass contrast (grey levels); darker frames are blank/unlit
GREY_MEAN = 90.0     # frames with mean grey level >= 90 are the 'grey' illumination look (fringes + bright cell-tip dots)
GREY_HP_MIN = 20.0   # grey frames need this contrast: fringe-only grey frames (planar front) have 13-16, dot lattices 27-43
SS_DET_MIN = 0.5     # a run gets a steady-state spacing only if >= 50 % of its steady-window frames pass the gate
STEADY_FRAC = 0.4    # steady state = last 40 % of the pulled length
NBINS = 60           # distance bins per run for the time series

SHORT = {'INIT activity 4': 'INIT-4', 'S1 activity 1': 'S1-1', 'S1 activity 2': 'S1-2', 'S1 activity 3': 'S1-3',
         'S1 activity 4': 'S1-4', 'S2 activity 4': 'S2-4', 'S2 activity 11': 'S2-11', 'HD activity 9': 'HD-9'}


def fnum(x):
    try:
        v = float(x)
        return v if math.isfinite(v) else None
    except (TypeError, ValueError):
        return None


def pulled_mm(run, t_s):
    c = RUNS[run]
    if 'V2' in c:
        tj = (c['t_jump'] - c['sol_start']) * 86400
        if t_s > tj:
            return (c['V'] * tj + c['V2'] * (t_s - tj)) / 1000
    return c['V'] * t_s / 1000


def load(path):
    op = gzip.open if str(path).endswith('.gz') else open
    with op(path, 'rt') as f:
        return list(csv.DictReader(f))


def detected(r):
    p, a, w, h = fnum(r.get('prom_db')), fnum(r.get('aniso2')), fnum(r.get('rel_fwhm')), fnum(r.get('hp_std'))
    m = fnum(r.get('mean'))
    return (p is not None and a is not None and w is not None and h is not None and
            p >= PROM_MIN and a <= ANISO_MAX and w >= FWHM_MIN and h >= HP_MIN and
            not (m is not None and m >= GREY_MEAN and h < GREY_HP_MIN))


def med(x):
    return statistics.median(x) if x else None


def q(x, p):
    if not x:
        return None
    x = sorted(x)
    k = (len(x) - 1) * p
    i = int(k)
    return x[i] + (x[min(i + 1, len(x) - 1)] - x[i]) * (k - i)


def per_run(rows, um_px):
    out = {}
    for run in RUNS:
        c = RUNS[run]
        t0 = excel_to_tick(c['sol_start'])
        dur = c['sol_dur'] * 86400
        length = c['z0'] - c['z1']
        fr = [r for r in rows if r['run'] == run and r['mode'] == '1' and not r.get('error')]
        allm = [r for r in rows if r['run'] == run]
        sol = []
        for r in fr:
            t = (int(r['tick']) - t0) / TICKS_PER_S
            if -600 <= t <= dur + 1800:
                r['_t'] = t
                r['_d'] = pulled_mm(run, max(t, 0))
                sol.append(r)
        det = [r for r in sol if detected(r)]
        # distance bins
        bins = []
        edges = [length * i / NBINS for i in range(NBINS + 1)]
        for i in range(NBINS):
            inb = [r for r in sol if edges[i] <= r['_d'] < edges[i + 1] or (i == NBINS - 1 and r['_d'] >= edges[i])]
            dd = [r for r in inb if detected(r)]
            lam = [fnum(r['lambda_px']) * um_px for r in dd]
            fw = [fnum(r['rel_fwhm']) for r in dd]
            q6 = [fnum(r['q6_tiles']) - fnum(r['q6_tiles_null']) for r in dd
                  if fnum(r['q6_tiles']) is not None and fnum(r['q6_tiles_null']) is not None]
            bins.append(dict(d_mm=round((edges[i] + edges[i + 1]) / 2, 2),
                             t_h=round(med([r['_t'] for r in inb]) / 3600, 3) if inb else None,
                             frames=len(inb), detected=len(dd),
                             lambda_um=round(med(lam), 1) if lam else None,
                             lambda_q25=round(q(lam, .25), 1) if lam else None, lambda_q75=round(q(lam, .75), 1) if lam else None,
                             rel_fwhm=round(med(fw), 3) if fw else None, q6_excess=round(med(q6), 3) if q6 else None))
        # onset: first bin from which >= 50 % of frames are detected for 3 consecutive non-empty bins
        onset = None
        ne = [b for b in bins if b['frames'] >= 3]
        for i in range(len(ne) - 2):
            if all(b['detected'] / b['frames'] >= 0.5 for b in ne[i:i + 3]):
                onset = ne[i]['d_mm']
                break
        ss_from = length * (1 - STEADY_FRAC)
        ss_frames = [r for r in sol if r['_d'] >= ss_from]
        ss_det = sum(1 for r in ss_frames if detected(r)) / len(ss_frames) if ss_frames else 0
        ssb = [b for b in bins if b['d_mm'] >= ss_from and b['lambda_um'] is not None and b['detected'] >= 3]
        if ss_det < SS_DET_MIN:
            ssb = []
        lam_ss = [b['lambda_um'] for b in ssb]
        fw_ss = [b['rel_fwhm'] for b in ssb if b['rel_fwhm'] is not None]
        q6_ss = [b['q6_excess'] for b in ssb if b['q6_excess'] is not None]
        # within-run bootstrap over distance bins (descriptive: bins are still autocorrelated)
        rnd = random.Random(7)
        boot = sorted(med([rnd.choice(lam_ss) for _ in lam_ss]) for _ in range(2000)) if len(lam_ss) >= 3 else []
        hd = {}
        if 'V2' in c:
            dj = c['z0'] - c['z_jump']
            pre = [b['lambda_um'] for b in bins if b['lambda_um'] and dj * 0.6 <= b['d_mm'] < dj and b['detected'] >= 3]
            post = [b['lambda_um'] for b in bins if b['lambda_um'] and b['d_mm'] >= length * 0.8 and b['detected'] >= 3]
            peak = [(b['lambda_um'], b['d_mm']) for b in bins if b['lambda_um'] and dj <= b['d_mm'] <= dj + 10 and b['detected'] >= 3]
            hd = dict(jump_at_mm=dj, lambda_before_jump_um=round(med(pre), 1) if pre else None,
                      lambda_peak_after_jump_um=max(peak)[0] if peak else None, peak_at_mm=max(peak)[1] if peak else None,
                      lambda_end_um=round(med(post), 1) if post else None)
        # within-run drift: first stable bins after onset vs last 10 % of the pulled length
        st_bins = [b for b in bins if b['lambda_um'] is not None and b['detected'] >= 3 and (onset is None or b['d_mm'] >= onset)]
        early = [b['lambda_um'] for b in st_bins[:5]]
        late = [b['lambda_um'] for b in st_bins if b['d_mm'] >= length * 0.9]
        drift = dict(lambda_early_um=round(med(early), 1) if early else None,
                     early_at_mm=round(med([b['d_mm'] for b in st_bins[:5]]), 1) if early else None,
                     lambda_late_um=round(med(late), 1) if late else None)
        out[run] = dict(
            short=SHORT[run], plan=c['plan'], V_um_s=c['V'], V2_um_s=c.get('V2'), pulled_length_mm=length,
            planned_duration_h=round(dur / 3600, 2), frames_hr2_all=len(allm), frames_mode1_in_window=len(sol),
            frames_detected=len(det), detected_fraction=round(len(det) / len(sol), 3) if sol else None,
            onset_mm=onset, steady_bins=len(ssb), steady_window_detected_fraction=round(ss_det, 3),
            lambda_ss_um=round(med(lam_ss), 1) if lam_ss else None,
            lambda_ss_ci95_um=[round(boot[50], 1), round(boot[1949], 1)] if boot else None,
            lambda_ss_iqr_um=[round(q(lam_ss, .25), 1), round(q(lam_ss, .75), 1)] if lam_ss else None,
            lambda_ss_cv=round(statistics.pstdev(lam_ss) / statistics.mean(lam_ss), 3) if len(lam_ss) >= 2 else None,
            rel_fwhm_ss=round(med(fw_ss), 3) if fw_ss else None, q6_excess_ss=round(med(q6_ss), 3) if q6_ss else None,
            **hd, **drift, bins=bins)
    return out


def mode_agreement(rows, um_px):
    """Steady-window spacing from the grey vs dark illumination looks, per run with >= 50 frames of each."""
    out = {}
    for run in RUNS:
        L = RUNS[run]['z0'] - RUNS[run]['z1']
        fr = [r for r in rows if r['run'] == run and r['mode'] == '1' and '_d' in r and r['_d'] >= (1 - STEADY_FRAC) * L and detected(r)]
        g = [fnum(r['lambda_px']) * um_px for r in fr if fnum(r['mean']) >= GREY_MEAN]
        d = [fnum(r['lambda_px']) * um_px for r in fr if fnum(r['mean']) < GREY_MEAN]
        if len(g) >= 50 and len(d) >= 50:
            out[SHORT[run]] = dict(grey_frames=len(g), grey_um=round(med(g), 1), dark_frames=len(d), dark_um=round(med(d), 1),
                                   diff_pct=round(100 * (med(g) / med(d) - 1), 1))
    return out


def loglog_fit(xs, ys):
    lx = [math.log(x) for x in xs]
    ly = [math.log(y) for y in ys]
    n = len(lx)
    mx, my = sum(lx) / n, sum(ly) / n
    sxx = sum((a - mx) ** 2 for a in lx)
    b = sum((a - mx) * (c - my) for a, c in zip(lx, ly)) / sxx
    return b, math.exp(my - b * mx)


def morph(a):
    rows = load(a.features)
    calib = json.load(open(a.calib)) if a.calib else {}
    jobs = json.load(open(a.jobs)) if a.jobs else {}
    um_px = calib.get('_global', {}).get('um_per_px')
    if um_px is None:
        raise SystemExit('need calibration')
    runs = per_run(rows, um_px)
    nproc = sum(1 for r in rows if not r.get('error'))
    nerr = sum(1 for r in rows if r.get('error'))
    bproc = sum(int(r['bytes']) for r in rows if r.get('bytes'))
    good = {k: v for k, v in runs.items() if v['lambda_ss_um'] is not None}
    # cross-run: spacing vs pulling rate (final V for HD-9), one point per run
    pts = [(v['V2_um_s'] or v['V_um_s'], v['lambda_ss_um'], k) for k, v in good.items()]
    fit = None
    if len(pts) >= 3:
        b, c0 = loglog_fit([p[0] for p in pts], [p[1] for p in pts])
        loo = []
        for i in range(len(pts)):
            sub = pts[:i] + pts[i + 1:]
            if len({p[0] for p in sub}) >= 2:
                loo.append(loglog_fit([p[0] for p in sub], [p[1] for p in sub])[0])
        fit = dict(exponent=round(b, 3), prefactor_um=round(c0, 1), n_runs=len(pts),
                   leave_one_out_exponent_range=[round(min(loo), 3), round(max(loo), 3)] if loo else None)
    same_v = {}
    for V in (0.5, 1.0):
        pair = {v['short']: v['lambda_ss_um'] for k, v in good.items() if v['V_um_s'] == V and not v['V2_um_s']}
        if len(pair) == 2:
            (n1, l1), (n2, l2) = sorted(pair.items())
            same_v[f'{V} um/s'] = dict(runs=pair, ratio=round(max(l1, l2) / min(l1, l2), 2))
    out = dict(runs=runs, fit=fit, same_v=same_v, mode_agreement=mode_agreement(rows, um_px), frames_processed=nproc, frames_failed=nerr, bytes_processed=bproc,
               um_per_px=um_px, calib=calib.get('_global'))
    import psi_morph_json
    res = psi_morph_json.build(out, jobs)
    json.dump(res, open(a.out, 'w'), indent=1)
    print('wrote', a.out, len(json.dumps(res)) // 1024, 'KB')
    for k, v in runs.items():
        print(v['short'], {kk: v[kk] for kk in ('V_um_s', 'frames_mode1_in_window', 'detected_fraction', 'onset_mm',
                                                'lambda_ss_um', 'lambda_ss_ci95_um', 'lambda_ss_cv', 'rel_fwhm_ss', 'q6_excess_ss')})
    print('fit', fit, 'same_v', same_v)
    return out
