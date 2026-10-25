"""Annotated validation thumbnails (<= 8 PNG, <= 80 KB each) for the DSI FFT spacing metric.

Left: the axial frame (central 768x768 crop analysed, 1-mm scale bar). Right: radial power spectrum
(masked), robust baseline and detected peak. Image credit: NASA Physical Sciences Informatics,
DECLIC-DSI (CNES/NASA), public domain.

    python -I analysis/bigdata/psi_thumbs.py --picks picks.json --mask dsi-artefact-mask.npz --um-px 11.51 --outdir data/results/bigdata/psi-thumbs
"""
import argparse
import io
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import psi_dsi_morph as M  # noqa: E402
import psi_morph_report as R  # noqa: E402  (same detection gate as the analysis)


def render(key, size, label, um_px, out):
    import numpy as np
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    from PIL import Image
    from scipy.ndimage import gaussian_filter
    img = M.decode(M.fetch(key, size))
    f = M.frame_features(img)
    N = 768
    c0 = (img.shape[0] - N) // 2
    x = img[c0:c0 + N, c0:c0 + N].astype(np.float32)
    y = x - gaussian_filter(x, M.HP_SIGMA)
    P, K, TH = M.spectrum(y / y.std())
    k, pr = M.radial(P, K, N / 10)
    sel = (k >= 3) & np.isfinite(pr) & (pr > 0)
    lam_um = N / k[sel] * um_px
    fig = plt.figure(figsize=(5.2, 2.6), dpi=100)
    a1 = fig.add_axes([0.0, 0.0, 0.5, 1.0])
    a1.imshow(x, cmap='gray', vmin=np.percentile(x, 1), vmax=np.percentile(x, 99.5))
    bar = 1000 / um_px
    a1.plot([30, 30 + bar], [N - 40, N - 40], color='yellow', lw=3)
    a1.text(30, N - 60, '1 mm', color='yellow', fontsize=7)
    a1.text(10, 30, label, color='yellow', fontsize=6.5, va='top')
    a1.set_axis_off()
    a2 = fig.add_axes([0.6, 0.2, 0.37, 0.68])
    a2.loglog(lam_um, pr[sel], color='#555555', lw=1)
    if 'lambda_px' in f:
        a2.axvline(f['lambda_px'] * um_px, color='#e8590c', lw=1.2)
        det = R.detected(f)
        a2.set_title(f"peak {f['lambda_px'] * um_px:.0f} um, {f['prom_db']:.0f} dB\n"
                     f"FWHM/k {f['rel_fwhm']:.2f}, aniso {f['aniso2']:.2f} -> {'cells' if det else 'rejected'}", fontsize=6.5)
    a2.set_xlabel('wavelength (um)', fontsize=6.5)
    a2.set_ylabel('radial power', fontsize=6.5)
    a2.invert_xaxis()
    a2.tick_params(labelsize=5.5)
    fig.text(0.52, 0.02, 'NASA PSI / DECLIC-DSI (CNES/NASA), public domain', fontsize=5)
    buf = io.BytesIO()
    fig.savefig(buf, format='png')
    plt.close(fig)
    im = Image.open(buf).convert('RGB').quantize(colors=48)
    im.save(out, optimize=True)
    return f, Path(out).stat().st_size


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--picks', required=True)   # [{"key":..,"size":..,"label":..,"name":..}]
    ap.add_argument('--mask', required=True)
    ap.add_argument('--um-px', type=float, required=True)
    ap.add_argument('--outdir', required=True)
    a = ap.parse_args()
    M.load_mask(a.mask)
    Path(a.outdir).mkdir(parents=True, exist_ok=True)
    meta = []
    for p in json.load(open(a.picks))[:8]:
        out = str(Path(a.outdir) / p['name'])
        f, sz = render(p['key'], int(p['size']), p['label'], a.um_px, out)
        assert sz <= 80_000, (out, sz)
        meta.append(dict(file=p['name'], key=p['key'], label=p['label'], bytes=sz,
                         lambda_um=round(f.get('lambda_px', 0) * a.um_px, 1), prom_db=round(f.get('prom_db', 0), 1),
                         rel_fwhm=round(f.get('rel_fwhm', 0), 3), aniso2=round(f.get('aniso2', 0), 3)))
        print(meta[-1])
    json.dump(meta, open(Path(a.outdir) / 'thumbs.json', 'w'), indent=1)


if __name__ == '__main__':
    main()
