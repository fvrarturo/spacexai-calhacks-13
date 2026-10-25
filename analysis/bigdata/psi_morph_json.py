"""Compose data/results/bigdata/dsi-morphology.json from psi_morph_report aggregates."""
from datetime import datetime, timezone

COLORS = ['orange', 'cyan', 'violet', 'green', 'grey']
BUCKET = 'https://nasa-psi.s3.us-west-2.amazonaws.com/'


def r(x, n=1):
    return None if x is None else round(x, n)


def series_runs(runs, keys, field, colors=COLORS):
    out = []
    for i, k in enumerate(keys):
        v = runs[k]
        pts = [[b['d_mm'], b[field]] for b in v['bins'] if b[field] is not None and b['detected'] >= 3]
        lab = f"{v['short']} (V={v['V_um_s']:g}" + (f"->{v['V2_um_s']:g}" if v['V2_um_s'] else '') + ' um/s)'
        out.append(dict(name=lab, color=colors[i % len(colors)], points=pts))
    return out


def build(agg, jobs):
    import json
    from pathlib import Path
    tj = Path(__file__).resolve().parents[2] / 'data/results/bigdata/psi-thumbs/thumbs.json'
    thumbs = [dict(path='data/results/bigdata/psi-thumbs/' + t['file'], caption=t['label'] + f" - FFT peak {t['lambda_um']:.0f} um",
                   source_key=t['key'], credit='NASA Physical Sciences Informatics, DECLIC-DSI (CNES/NASA); public domain')
              for t in (json.loads(tj.read_text()) if tj.exists() else [])]
    runs = agg['runs']
    um = agg['um_per_px']
    slow = [k for k in ['INIT activity 4', 'S2 activity 4', 'S1 activity 4', 'S2 activity 11', 'HD activity 9'] if k in runs]
    fast = [k for k in ['S1 activity 1', 'S1 activity 2', 'S1 activity 3'] if k in runs]
    good = [k for k, v in runs.items() if v['lambda_ss_um'] is not None]
    nframes = agg['frames_processed']
    gb = agg['bytes_processed'] / 1e9
    fit = agg['fit']
    same = agg['same_v']
    lam = sorted((runs[k]['lambda_ss_um'], runs[k]['short']) for k in good)
    seq_col = lambda k: 'orange' if k.startswith(('S1', 'INIT')) else 'cyan'
    scatter = [dict(name='Sequences INIT + S1 (Apr-May 2010)', color='orange',
                    points=[[runs[k]['V2_um_s'] or runs[k]['V_um_s'], runs[k]['lambda_ss_um']] for k in good if seq_col(k) == 'orange']),
               dict(name='Sequences S2 + HD (Oct 2010-Jan 2011)', color='cyan',
                    points=[[runs[k]['V2_um_s'] or runs[k]['V_um_s'], runs[k]['lambda_ss_um']] for k in good if seq_col(k) == 'cyan'])]
    ann = [dict(x=runs[k]['V2_um_s'] or runs[k]['V_um_s'], y=runs[k]['lambda_ss_um'], text=runs[k]['short']) for k in good]
    det_pts = [[runs[k]['short'], r(100 * (runs[k]['detected_fraction'] or 0), 1)] for k in slow + fast]
    run_table = []
    for k in slow + fast:
        v = runs[k]
        run_table.append({kk: v[kk] for kk in v if kk != 'bins'})
    headline_val = f'{nframes:,}'
    if same:
        ratios = ', '.join(f"{k}: x{v['ratio']}" for k, v in same.items())
    else:
        ratios = 'n/a'
    findings = [
        f'We streamed and analysed {nframes:,} axial (HR2) frames ({gb:.1f} GB) from all 8 public DECLIC-DSI runs; the 2-D FFT spacing metric found a cellular pattern in '
        f'{sum(runs[k]["frames_detected"] for k in runs):,} frames recorded during directional solidification.',
    ]
    for k in slow + fast:
        v = runs[k]
        vlab = f"V = {v['V_um_s']:g}{' -> ' + format(v['V2_um_s'], 'g') if v['V2_um_s'] else ''} um/s"
        if v['lambda_ss_um']:
            txt = (f"{v['short']} ({vlab}): spacing {v['lambda_ss_um']:.0f} um over the last 40% of the run "
                   f"(bin-bootstrap interval {v['lambda_ss_ci95_um'][0]:.0f}-{v['lambda_ss_ci95_um'][1]:.0f} um); cells first stable after ~{v['onset_mm']:g} mm of pulling")
            if v.get('lambda_early_um') and v.get('lambda_late_um') and not v['V2_um_s']:
                ch = 100 * (v['lambda_late_um'] / v['lambda_early_um'] - 1)
                txt += f"; spacing went from {v['lambda_early_um']:.0f} um near {v['early_at_mm']:g} mm to {v['lambda_late_um']:.0f} um at the end ({ch:+.0f}%)"
            findings.append(txt + '.')
        else:
            findings.append(f"{v['short']} ({vlab}): no steady-state value - only {100 * v['steady_window_detected_fraction']:.0f}% of late-run frames pass the gate "
                            f"(fast, low-contrast fronts; eye checks show cells in some frames, fringes or blur in others).")
    s11 = runs.get('S1 activity 1')
    if s11:
        findings.append('S1-1 (6 um/s) is bimodal: ~240 um cells for most of the run and ~550 um in the last ~8 mm (both confirmed by eye); the cause (cell-dendrite transition, end-of-pull transient or an optics change) is not identifiable from PSI metadata.')
    if same:
        findings.append('Same pulling rate, different sequence: ' + '; '.join(
            f"{V}: {', '.join(f'{n} {l:.0f} um' for n, l in d['runs'].items())} (x{d['ratio']})" for V, d in same.items()) +
            '. Spring-2010 runs (INIT, S1) settle at ~400 um and autumn-2010 runs (S2) at 650-730 um, so pulling rate alone does not set the spacing; '
            'a different thermal gradient or growth history between sequences is the likely reason (the Task Book reports two gradients), but PSI does not record G per run.')
    if fit:
        findings.append(f"Across the {fit['n_runs']} runs with a steady value, spacing ~ V^{fit['exponent']:.2f}, but dropping one run moves the exponent from "
                        f"{fit['leave_one_out_exponent_range'][0]:.2f} to {fit['leave_one_out_exponent_range'][1]:.2f}: with sequences mixed, no scaling law can be claimed.")
    hd = runs.get('HD activity 9', {})
    if hd.get('lambda_end_um'):
        findings.append(f"HD-9 (velocity jump 0.35 -> 0.75 um/s at {hd['jump_at_mm']:.0f} mm): the front stayed planar (no cells) for the first ~{hd['onset_mm']:.0f} mm at 0.35 um/s; "
                        f"cells appeared just before the jump (~{hd['lambda_before_jump_um']:.0f} um), grew to ~{hd['lambda_peak_after_jump_um']:.0f} um by {hd['peak_at_mm']:g} mm, "
                        f"then settled at ~{hd['lambda_end_um']:.0f} um at 0.75 um/s (frames at 35 and 50 mm checked by eye).")
    ma = agg['mode_agreement']
    if ma:
        findings.append('Two illumination looks of the same camera (dark cell-boundary view, grey cell-tip-dot view) give the same late-run spacing: ' +
                        ', '.join(f"{k} {v['grey_um']:.0f} vs {v['dark_um']:.0f} um ({v['diff_pct']:+.1f}%)" for k, v in ma.items()) +
                        ' - an internal validation that the metric measures the pattern, not the optics.')
    findings.append(f'Data reduction: each 1,049,654-byte frame is summarised by 16 numbers (64 bytes as float32), a ~16,000x reduction; the whole {gb:.1f} GB axial archive becomes {nframes * 64 / 1e6:.1f} MB of morphology - the kind of step an on-board foundry pipeline could run before downlink.')

    return dict(
        id='dsi-morphology', tab='materials', material='cooling',
        title='Cell spacing measured in 54,000 ISS solidification images (DECLIC-DSI)',
        question='Can a physically meaningful, defensible morphology metric be extracted at scale from public ISS solidification imagery?',
        headline=dict(value=headline_val, unit='ISS frames',
                      text=(f'We measured cell spacing in {nframes:,} ISS images of a solidifying transparent alloy: runs settle at '
                            f'{lam[0][0]:.0f}-{lam[-1][0]:.0f} um, and runs at the same pulling speed from different 2010 sequences differ '
                            + ' to '.join(f"{d['ratio']:.1f}x" for d in sorted(same.values(), key=lambda d: d['ratio'])) + '.') if lam else
                           f'We processed {nframes:,} ISS solidification images.'),
        evidence_level='our computation on public data',
        datasets=[dict(name='NASA PSI - DECLIC Directional Solidification Insert (DSI), axial HR2 camera', url=BUCKET + 'DSI/',
                       license='NASA open data (public domain); cite NASA Physical Sciences Informatics, DECLIC-DSI (CNES/NASA)',
                       records=nframes, bytes=agg['bytes_processed'], accessed='2026-10-24', scope='processed',
                       notes='All HR2 1024x1024 8-bit BMP frames of the 8 public activities, streamed from S3 (not stored). Run conditions from the PSI DSI-* Solidification Plan sheets.')],
        compute=dict(where='MIT Engaging', partitions=jobs.get('morph_partitions', ['mit_quicktest']), job_ids=jobs.get('morph', []),
                     cpu_hours=jobs.get('morph_cpu_hours', 0.0), wall_minutes=jobs.get('morph_wall_minutes', 0.0), peak_storage_gb=0.05),
        method=[
            'Frame manifest from the complete bucket inventory: every *_HR2_<tick>_<mode>.bmp in the 8 extracted activity folders (duplicates in "extracted by cbp" folders and zips skipped).',
            'Clock: file-name ticks = 23 per second since 2009-01-01 (from the plan sheets\' SL2 column); confirmed by the 180-s melt image period (60 s in S2-4, as planned) and by the first S1-1 frame falling 20 s from its planned command.',
            'Run conditions (pulling rate V, pulled length, planned start and duration) transcribed from DSI-INIT/S1/S2/HD Solidification Plan.xlsx; frames are placed on the pulled distance d = V t from the planned start of the directional-solidification step.',
            'Per frame: 768x768 central crop, Gaussian high-pass (sigma 24 px), Hann window, 2-D FFT; Fourier bins of fixed optical/sensor artefacts are excluded using a mask learned from 480 frames (80th-percentile ratio to the radial mean > 2.6, present in >20% of frames across all runs).',
            'Spacing = 768 / k_peak of the radial power spectrum above a robust power-law baseline (search 12-110 px); order metrics = relative FWHM of the peak (positional order) and the 6-fold angular order |<e^{6i theta}>| on 3x3 tiles minus an off-peak null (orientational order).',
            'Detection gate (set after eye validation of ~45 frames, then applied unchanged to all 53,895): prominence >= 10 dB, 2-fold anisotropy <= 0.30 (rejects stripe artefacts), relative FWHM >= 0.10, high-pass contrast >= 4 grey levels, and >= 20 for grey-look frames (mean >= 90; fringe-only grey frames have 13-16). A run gets a steady value only if >= 50% of its late frames pass.',
            f'Scale: {um:.2f} um/px, from circle fits to the bright 10-mm sample disk in 15 unsaturated homogenisation frames of 3 runs (869 +/- 5 px). This is our calibration, assuming the disk is the 10-mm sample of the PSI Science Requirements Document.',
            f'Run = unit: per run, frames are binned into 60 pulled-distance bins; steady-state spacing = median of bin medians over the last 40% of the pulled length; interval = bootstrap over bins (descriptive, bins are autocorrelated). Cross-run statements use one value per run.',
        ],
        charts=[
            dict(id='dsi-spacing-vs-distance', kind='line', title='Cell spacing as the front advances (slow runs)',
                 subtitle='Median FFT spacing per pulled-distance bin, frames passing the pattern gate',
                 x=dict(label='Pulled distance', unit='mm', scale='linear'), y=dict(label='Cell spacing', unit='um', scale='linear'),
                 series=series_runs(runs, slow, 'lambda_um'), annotations=[],
                 caption='Each line is one ISS run; each point is the median over all accepted frames in a ~1 mm bin. The spacing keeps evolving along most runs (' +
                         ', '.join(f"{runs[k]['short']} {100 * (runs[k]['lambda_late_um'] / runs[k]['lambda_early_um'] - 1):+.0f}%" for k in slow
                                   if runs[k].get('lambda_early_um') and runs[k].get('lambda_late_um') and not runs[k]['V2_um_s']) +
                         ' from onset to end), so the "steady" value is a late-run value, not a converged one. HD-9 is planar (no points) until ~28 mm. No Earth control is included: this shows pattern dynamics in microgravity, not a microgravity advantage.'),
            dict(id='dsi-spacing-vs-velocity', kind='scatter', title='Steady-state spacing vs pulling rate, one point per run',
                 subtitle='Median over the last 40% of the pulled length',
                 x=dict(label='Pulling rate (final)', unit='um/s', scale='log'), y=dict(label='Steady-state cell spacing', unit='um', scale='log'),
                 series=scatter, annotations=ann,
                 caption=(f"Log-log slope {fit['exponent']:.2f} over {fit['n_runs']} runs (leave-one-out {fit['leave_one_out_exponent_range'][0]:.2f} to {fit['leave_one_out_exponent_range'][1]:.2f}). " if fit else '') +
                         'Points from the two sequences separate at equal speed; the thermal gradient and history are not given per run in PSI, so the slope is descriptive.'),
            dict(id='dsi-order-vs-distance', kind='line', title='Pattern order as the front advances',
                 subtitle='Relative width of the FFT spacing peak (lower = more ordered)',
                 x=dict(label='Pulled distance', unit='mm', scale='linear'), y=dict(label='Peak FWHM / k_peak', unit='', scale='linear'),
                 series=series_runs(runs, slow, 'rel_fwhm'), annotations=[],
                 caption='A narrow peak means a narrow distribution of cell sizes. Values depend on image mode and illumination as well as on the pattern, so compare trends within a run rather than absolute levels between runs.'),
            dict(id='dsi-detected-fraction', kind='bar', title='Share of solidification frames with a measurable cellular pattern',
                 subtitle='Per run, axial mode-1 frames inside the solidification window',
                 x=dict(label='Run', unit='', scale='category'), y=dict(label='Frames passing the gate', unit='%', scale='linear'),
                 series=[dict(name='Detected', color='green', points=det_pts)], annotations=[],
                 caption='Slow runs (0.5-1 um/s) pass 78-95% of solidification frames. HD-9 passes fewer because its front stayed planar for the first ~28 mm, and planar-front frames are correctly rejected. Fast runs (6-16 um/s) give fine, low-contrast fronts and pass 19-55%.'),
        ],
        stats=dict(frames_processed=nframes, frames_failed=agg['frames_failed'], bytes_processed=agg['bytes_processed'],
                   frames_with_pattern=sum(runs[k]['frames_detected'] for k in runs), illumination_mode_agreement=agg['mode_agreement'],
                   um_per_px=r(um, 3), calibration=agg['calib'], loglog_fit=fit, same_velocity_replicates=same,
                   runs=run_table,
                   thresholds=dict(prom_db_min=10.0, aniso2_max=0.30, rel_fwhm_min=0.10, hp_std_min=4.0, grey_mean=90.0, grey_hp_std_min=20.0,
                                   steady_fraction=0.4, steady_window_detected_min=0.5, bins_per_run=60)),
        findings=findings,
        limitations=[
            'No matched ground (1 g) runs are in PSI, so nothing here measures a microgravity advantage; the result shows that space imagery supports quantitative morphology at scale, and what the pattern dynamics are.',
            'Eight runs only; two pairs share a pulling rate but come from different sequences, and the thermal gradient G per run is not in the PSI files (the Task Book reports two G values), so V and G effects are confounded.',
            f'The physical scale ({um:.2f} um/px) is our disk-fit calibration assuming a 10-mm sample; a different true diameter scales all spacings proportionally (relative comparisons are unaffected).',
            'Frames are timed from planned command dates (the plan sheets); actual start times can lag by minutes. Mode-1 frames mix two illuminations (dark cell-boundary view and grey dot view); both show the same spacing in validation, but the order metrics differ by mode.',
            'The FFT spacing is a dominant-wavelength measure over a 8.8-mm field; it does not resolve local spacing gradients (centre vs edge) or individual cell neighbours.',
            'Frames within a run are autocorrelated; within-run intervals are descriptive, not independent-replicate confidence intervals.',
        ],
        future_big_data=[
            'Request the remaining ~31 of 39 DSI runs and the 2017-2018 DSI-R reflight from the full PSI catalogue (psi.nasa.gov, registration) to cover both thermal gradients at every speed.',
            'Pair each ISS run with ground runs in the same DECLIC insert (or thin-sample 1 g runs from the Iowa State/IM2NP groups) to measure the convection effect directly.',
            'Add Voronoi/neighbour analysis on segmented cells and the side-view (HR1) interface position to get front velocity and recoil per run.',
            'Apply the same pipeline to ACE colloid images for photonic crystals and to NPG-type barocaloric solidification if flown.',
        ],
        partners=[
            dict(name='CNES (DECLIC facility) and the DSI science team', why='Built and operated the sealed solidification insert; the natural partner for a solidification process cartridge',
                 evidence='DSI Task Book report: DECLIC-DSI built by CNES; 39 experiments over 100 days in SCN-0.24 wt% camphor'),
            dict(name='Iowa State University / Ames Laboratory (R. Trivedi, PI) and Northeastern University (A. Karma, Co-I)', why='Phase-field modelling and ground thin-sample experiments that give the theory to interpret on-orbit spacing',
                 evidence='PI and Co-I named in the PSI DSI Task Book reports (grant NNX07AK69G)'),
            dict(name='NASA MSFC (PSI curation)', why='Archive owner; access to the full DSI and DSI-R catalogue',
                 evidence='Task Book contact monitor at NASA MSFC; PSI hosts the data'),
        ],
        code=['analysis/bigdata/psi_dsi_morph.py', 'analysis/bigdata/psi_morph_report.py', 'analysis/bigdata/psi_morph_json.py',
              'analysis/bigdata/psi_thumbs.py', 'cluster/bigdata/psi-mask.sbatch', 'cluster/bigdata/psi-dsi-quick.sbatch'],
        reproduce=[
            'python -I analysis/bigdata/psi_dsi_morph.py manifest --tsv psi-objects.tsv.gz --out dsi-hr2-manifest.tsv',
            'sbatch cluster/bigdata/psi-mask.sbatch   # learns the artefact mask',
            'sbatch cluster/bigdata/psi-dsi-quick.sbatch   # repeat (resumable) until all 24 shards report done',
            'python -I analysis/bigdata/psi_dsi_morph.py calib --manifest dsi-hr2-manifest.tsv --out dsi-calib.json',
            'python -I analysis/bigdata/psi_report.py morph --features dsi-features.csv.gz --calib dsi-calib.json --jobs jobs.json --out data/results/bigdata/dsi-morphology.json',
        ],
        thumbnails=thumbs,
        generated_at=datetime.now(timezone.utc).isoformat(timespec='seconds'),
    )
