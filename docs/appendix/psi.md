# Appendix — NASA PSI: open ISS physical-science data (workstream `psi`)

**Result files:** `data/results/bigdata/psi-inventory.json` (Foundry tab) and `data/results/bigdata/dsi-morphology.json` (Materials tab, material `cooling`). Validation thumbnails are in `data/results/bigdata/psi-thumbs/`.
**Evidence level:** our computation on public data. Conditions transcribed from PSI documents are labelled as such.
**Data credit:** NASA Physical Sciences Informatics (PSI), <https://registry.opendata.aws/nasa-psi/>, bucket `s3://nasa-psi` (us-west-2, anonymous access). The data are NASA open data (public domain). DECLIC was built by CNES and DSI is a CNES/NASA investigation; cite "NASA PSI, DECLIC-DSI (CNES/NASA)" with any image.

## 1. What is openly available (complete inventory)

### Data and method
- `analysis/bigdata/psi_inventory.py` runs as Slurm job **26813006** (`mit_normal`, 2 CPUs, 1 min 59 s). It makes anonymous S3 `ListObjectsV2` calls:
  - delimiter listings at depth 0 and 1 enumerate 17 second-level prefixes;
  - each prefix is then listed to exhaustion through continuation tokens (12 threads).
- 399 list pages returned **388,602 objects, 30,269,667,094,536 bytes (30.27 TB)**.
- Key uniqueness is asserted, and the listing is complete by construction: every key either has fewer than two `/` or lies under one of the 17 prefixes.
- `analysis/bigdata/psi_inventory_summary.py` summarises the 10 MB gzipped listing (light, run off-cluster).
  - *Exact duplicate* means the same ETag and size; 345,940 objects are content-distinct.
  - Zip archives are reported separately.
- `analysis/bigdata/psi_report.py inventory` writes the site JSON.

| Investigation | Objects | Stored | Notes |
|---|---:|---:|---|
| PK-4 (complex plasma, ESA/Roscosmos, ISS Columbus, campaigns C00–C08, 2014–2019) | 61,592 | 21.03 TB | 20.46 TB is on-board `.avi` camera video; 31 runs (C00_R1 … C08_R4) |
| OASIS (smectic liquid-crystal bubbles/islands, 2015–2016) | 205,198 | 9.07 TB | 7.23 TB is `_Originals.zip` archives of original frames; extracted `.jpg` are gallery previews; 13 hard-drive folders + 1.71 TB streaming video |
| DECLIC-DSI (directional solidification, 2010–2011) | 121,811 | 165 GB | Only 70 GB after removing zip copies and a second extracted copy; 8 activities |

File types across the whole bucket, by bytes: `.avi` 20.46 TB (1,578 files), `.zip` 7.46 TB (5,280), `.ts` 1.70 TB (718), `.log` 0.24 TB, `.dat` 0.11 TB, `.raw` 73 GB (67,084), `.bmp` 66 GB (63,328), `.tiff` 54 GB, `.jpg` 20 GB (169,608 files, the most numerous type).

### Data volume per experiment-day
- **DSI.** Raw 1024×1024 8-bit BMP bytes divided by the span between the first and last frame of each activity.
  - Frame times come from the clock tick in each file name (see §2.2).
  - Range **2.2–13.0 GB/day**; INIT-4 is highest because it ran 20,725 frames in 1.7 days.
- **OASIS.** De-duplicated bytes per hard-drive folder divided by the calendar days in the folder name (e.g. "HD01 – SN001 Jul 1 to Jul 6 2015").
  - Range **25–146 GB per calendar day**.
  - This is a lower bound on the rate while operating, because the date ranges include idle days.
- **PK-4.** On-board camera video (`VMx-AVI` files) per calendar date, from the `YYMMDD-HHMMSS` stamps in file names. 98.6% of PK-4 bytes carry a date stamp.
  - The daily distribution is bimodal: 296–786 GB "science days" against 2–7 GB check-out days.
  - Over the **31 science days (≥ 100 GB)** the median is **702 GB/day**; campaign means are 537–766 GB per science day.
- **Takeaway for the Foundry tab.** One ISS facility day ranges from a few GB (a camera-based solidification insert) to about 0.7 TB (a multi-camera plasma lab). That is more than two orders of magnitude. It is the quantitative case for shared on-board data services: buffering, onboard reduction and downlink scheduling.

### What this does not show
- These are volumes PSI publishes after downlink and curation, not raw sensor rates.
- PSI's own notes say some OASIS drives were only partly loaded and some PK-4 runs lack sensor data.
- We did not open the OASIS zips, which may partly duplicate extracted raw/tiff files.
- Three investigations are not a sample of all ISS science.

## 2. DECLIC-DSI: cellular spacing at scale

### 2.1 What the DSI folder contains (from PSI files)
- **Alloy and campaign.** Succinonitrile–0.24 wt% camphor. The NASA Task Book FY2013 report in `DSI/Taskbook Downloads/` says 39 experiments ran over 100 days at two thermal gradients (PI R. Trivedi, Iowa State; Co-I A. Karma, Northeastern; grant NNX07AK69G; facility built by CNES). PSI hosts 8 of them.
- **Camera folders.**
  - `DA_TC_DSI_SEQx_ACTIVITEyy_HR1`: side view, perpendicular to growth. The interface appears as a vertical line between solid and liquid.
  - `…_HR2_k`: axial view, looking down the growth axis onto the front. Cellular patterns are directly visible.
  - `…_SCIENCE`: `.dat` telemetry.
  - Each folder has `filelist.txt` and, for HD-9, `import.xlsx` (PSI gallery records). Zips of the same folders and a duplicate "extracted by cbp" copy also exist.
- **File-name suffix.** `_1` or `_2`, with 3,164 frames suffixed `_2`. Its meaning is not documented. `_2` frames show a bright central illumination spot, so we analyse `_1` frames for the time series (features were computed for both).
- **Run conditions.** From `DSI/Data/DSI-{INIT,S1,S2,HD} Solidification Plan.xlsx` (French and English sheets):

| Run | Plan step | Pulling rate V (µm/s) | Pulled length (mm) | Planned duration (h) | Planned start (UTC, plan clock) |
|---|---|---:|---:|---:|---|
| INIT-4 | DSI-INIT 4-3 | 1.0 | 60 (z 69→9) | 16.6 | 2010-04-26 13:50 |
| S1-1 | DSI-S1 1-3 | 6 | 60 | 2.8 | 2010-05-26 10:05 |
| S1-2 | DSI-S1 2-3 | 12 | 60 | 1.4 | 2010-05-27 12:24 |
| S1-3 | DSI-S1 3-3 | 16 | 60 | 1.0 | 2010-05-28 13:52 |
| S1-4 | DSI-S1 4-3 | 0.5 | 40 (z 69→29) | 22.2 | 2010-05-29 14:10 |
| S2-4 | DSI-S2 4-3 | 1.0 | 42 (z 72→30) | 11.7 | 2010-10-10 01:02 |
| S2-11 | DSI-S2 11-3 | 0.5 | 59.5 (z 72→12.5) | 33.1 | 2010-10-16 21:23 |
| HD-9 | DSI-HD 9-7 (`SOL_VV`) | 0.35 → 0.75 at z = 43 mm | 60 (z 73→13) | 34.9 | 2011-01-19 08:11 |

The thermal gradient per run is **not** given in these files. Only the INIT and S1 plans list heater set-points: HZ3 at 93 °C for INIT and 90 °C for S1.

### 2.2 Clock and timing (verified)
- The plan sheets' `SL2` column equals (Excel date − 39814) × 86400 × 23. The image file names use the same counter: **23 ticks per second since 2009-01-01**. We checked this three ways:
  1. the melt-phase image period is 4,140 ticks = 180 s, the planned `P_img = 3 min`;
  2. in S2-4 the period is 60 s, as its plan says (`P_img = 1 min`);
  3. the first S1-1 frame is 20 s from the planned step 1-1 command.
- Frames are placed on the pulled distance d = V·t from the planned start of the solidification step. Commands may have executed minutes late.

### 2.3 Metric: dominant cell spacing from the 2-D FFT, plus pattern order
The code is in `analysis/bigdata/psi_dsi_morph.py`.
- **Frame manifest.** Every `*_HR2_<tick>_<mode>.bmp` in the 8 extracted activity folders, taken from the complete inventory: **53,895 frames, 56.57 GB**.
- **Streaming.** Frames are streamed from S3 on compute nodes and never written to disk; each is decoded in memory and reduced to 16 numbers.
- **Per frame:**
  1. take the 768×768 central crop (8.8 mm);
  2. apply a Gaussian high-pass (σ = 24 px) and a Hann window;
  3. compute the 2-D FFT;
  4. exclude the Fourier bins of fixed artifacts;
  5. average the power radially and fit a robust lower-envelope power-law baseline;
  6. take the peak of the excess in λ = 12–110 px, giving **spacing λ = 768 / k_peak**, refined by parabolic interpolation.
- **Order metrics.**
  - *Positional order:* the relative FWHM of the peak.
  - *Orientational order:* the 6-fold order |⟨e^{6iθ}⟩| on 3×3 tiles at k_peak, minus the same quantity at 1.7·k_peak (a null).
  - *Artifact detector:* the 2-fold anisotropy at the peak ring.
- **Artifact mask.** This was learned from data in job **26814504**: 480 mode-1 frames, 60 per run.
  - Each frame's spectrum is divided by its own radial mean.
  - Bins whose 80th-percentile ratio exceeds 2.6 are dilated by one bin and excluded.
  - Fixed fringes recur in more than 20% of frames across all runs, so they pass this threshold. The strongest is at (k_y, k_x) = (9, 3) cycles per 768 px, λ ≈ 81 px, and appears in every run. Structure confined to one run (at most 12.5% of the sample) cannot reach it.
  - Before masking, that fringe dominated the spectrum of every "grey-look" frame and returned a spurious 81 px "spacing".
- **Scale: 11.51 µm/px.** `calib` fits circles to the bright sample disk in unsaturated homogenization frames: 869 ± 5 px over 15 frames from HD-9, S1-4 and S2-11.
  - This assumes the disk is the 10-mm sample of the SRD. It is **our calibration, not a PSI value**.
  - Saturated frames bloom to about 980–999 px and are excluded.
  - The disk size is the same in 2010 and 2011 runs, so magnification did not change between sequences.
- **Detection gate.** It was set after eye validation of about 45 frames, then applied unchanged to all frames:
  - prominence ≥ 10 dB;
  - anisotropy ≤ 0.30;
  - relative FWHM ≥ 0.10;
  - high-pass contrast ≥ 4 grey levels, and ≥ 20 for grey-look frames (mean ≥ 90).
  - The last condition was added after the eye check found grey fringe-only frames from the planar front, e.g. S1-1, giving false "cells". Their contrast is 13–16; grey dot lattices sit at 27–43.
- **Run as the unit.**
  - Mode-1 frames in the solidification window are binned into 60 pulled-distance bins per run.
  - The late-run ("steady") spacing is the median of bin medians over the last 40% of the pulled length, reported only if at least 50% of late frames pass the gate.
  - Intervals come from a bootstrap over bins and are descriptive, because bins are autocorrelated.
  - Cross-run statements use one value per run.

### 2.4 Results (our computation on public data)
- Job **26814839** (`mit_quicktest`, 24 CPUs, 6 min 10 s, 2.47 CPU-h) processed all **53,895** frames, 56.57 GB streamed, with zero failures.
- **36,366** solidification frames passed the pattern gate.

| Run | V (µm/s) | Mode-1 frames in window | Pass gate | Cells stable after (mm) | Late-run spacing (µm) [bin bootstrap] | Onset → end (µm) | Peak FWHM/k |
|---|---:|---:|---:|---:|---|---|---:|
| INIT-4 | 1.0 | 18,976 | 94.5% | 6.5 | **410** [393–411] | 353 → 431 (+22%) | 0.29 |
| S2-4 | 1.0 | 4,038 | 80.0% | 4.6 | **731** [704–757] | 505 → 751 (+49%) | 0.34 |
| S1-4 | 0.5 | 3,535 | 77.9% | 7.7 | **401** [384–416] | 474 → 411 (−13%) | 0.33 |
| S2-11 | 0.5 | 5,353 | 84.8% | 8.4 | **646** [616–669] | 491 → 720 (+47%) | 0.40 |
| HD-9 | 0.35 → 0.75 | 7,084 | 42.9% | 29.5 | **422** [404–428] | 339 (onset, ~28 mm) → 593 (35.5 mm, after jump) → 431 (end) | 0.20 |
| S1-1 | 6 | 4,377 | 50.6% | 3.5 | none (only 48% of late frames pass) | bimodal ~240 / ~550 | — |
| S1-2 | 12 | 3,661 | 55.4% | 21.5 | **223** [218–226] | 246 → 217 (−12%) | 0.25 |
| S1-3 | 16 | 3,411 | 18.5% | 43.5 | none (35%) | — | — |

**What the data show**
1. **The metric works at scale.** Two illumination looks of the same camera, dark cell boundaries and grey cell-tip dots, give the same late-run spacing: INIT-4 +0.1%, S1-4 +3.1%, S2-4 +3.6%, HD-9 +2.1%. Planar-front frames are correctly rejected (HD-9 stays planar for about 28 mm at 0.35 µm/s). Eight annotated frames are in `psi-thumbs/`.
2. **The pattern evolves.** Spacing coarsens through most slow runs: +22% in INIT-4, about +49% in S2-4 and +47% in S2-11. HD-9 shows a transient after the velocity jump, rising to about 590 µm and then settling near 430 µm; we checked frames at 35 and 50 mm by eye.
3. **Same speed, different sequence.** At 0.5 µm/s, S1-4 is 401 µm and S2-11 is 646 µm (×1.61). At 1 µm/s, INIT-4 is 410 µm and S2-4 is 731 µm (×1.78).
   - The spring-2010 sequences (INIT, S1) settle near 400 µm; the autumn sequence (S2) settles at 650–730 µm.
   - The magnification is unchanged (same disk diameter), so this is not an optics artifact.
   - A different thermal gradient or growth history is the likely cause, since the Task Book reports two G values, but PSI does not record G per run.
4. **No scaling law can be claimed.** A log-log fit over the 6 runs gives λ ∝ V^−0.26, but leaving one run out moves the exponent from −0.31 to +0.08.
5. **Data reduction.** 16 numbers per 1 MB frame is about 16,000×. The 56.6 GB axial archive becomes 3.4 MB of morphology, which is the kind of on-board reduction a foundry data service would run.

**What this does not show**
- **No microgravity advantage.** There are no matched 1 g controls in PSI.
- **G and V are confounded** across sequences.
- **Physical scale rests on our 10-mm-disk calibration.** All µm values scale with it; ratios do not.
- **Timing uses planned command times.**
- **The FFT gives a dominant field-averaged wavelength.** It does not give local spacing or neighbour statistics.
- **S1-1's late ~550 µm mode and S1-3 are unexplained.** Possible causes are a cell-to-dendrite transition, an end-of-pull transient or an optics change; PSI metadata cannot tell them apart.

### 2.5 Thumbnails (`data/results/bigdata/psi-thumbs/`, PNG, 42–54 KB each)
Each thumbnail shows the analysed 8.8-mm crop with a 1-mm bar and its masked radial spectrum with the detected peak. Credit: NASA Physical Sciences Informatics, DECLIC-DSI (CNES/NASA), public domain.
- `dsi-init4-cells-dark.png` and `dsi-init4-cells-grey.png`: the same run in both looks, both 411 µm.
- `dsi-s1-2-fast.png`: 223 µm.
- `dsi-s2-4-cells.png`: 760 µm.
- `dsi-s2-11-cells.png`: 658 µm.
- `dsi-hd9-after-jump.png`: 409 µm.
- `dsi-hd9-planar-rejected.png`: planar front, rejected.
- `dsi-s1-1-fringe-rejected.png`: fringe-only grey frame, rejected.
- `thumbs.json`: the source keys.

## 3. OASIS and PK-4: inventory only
- **OASIS** (Observation and Analysis of Smectic Islands In Space). Freely suspended smectic liquid-crystal films and bubbles on the ISS, 2015–2016. The tests cover island coarsening, Marangoni flow, electric field and more, on 4 samples (SN001–SN004), in 39 sample/test-type records (PSI OASIS DoD). Storage is 9.07 TB in 205,198 objects across 13 hard-drive folders plus a 1.71 TB "SCIENCE VIDEOS Streaming" folder.
- **PK-4** (Plasma Kristall-4). Complex (dusty) plasma in a DC discharge tube in ISS Columbus (ESA/Roscosmos), 9 campaigns (C00–C08, 2014–2019) and 31 runs. Data are on-board videos, sensor logs and ground data, curated for PSI by the University of Memphis team. Storage is 21.03 TB in 61,592 objects.

## 4. Compute record (all jobs submitted by this workstream)

| Job | Partition | CPUs | Elapsed | State | Purpose |
|---|---|---:|---|---|---|
| 26813006 | mit_normal | 2 | 00:01:59 | COMPLETED | complete bucket inventory |
| 26814070 | mit_quicktest | 4 | 00:00:52 | COMPLETED | artifact mask v1 (median rule), superseded |
| 26814211 | mit_quicktest | 4 | 00:00:58 | COMPLETED | artifact mask v2 (NaN bug in tile mask), superseded |
| 26814504 | mit_quicktest | 4 | 00:00:56 | COMPLETED | **final artifact mask** |
| 26814212, 26814505 | mit_normal | (24×1) | — | CANCELLED before start | array versions; `mit_normal` had >1,500 pending jobs |
| 26814839 | mit_quicktest | 24 | 00:06:10 | COMPLETED | **all 53,895 frames** |
| 26814840, 26814841 | mit_quicktest | — | — | CANCELLED unused | chained resume jobs, not needed |

- Peak scratch use was under 50 MB: frames were streamed, and only the listing (10 MB), features (3.4 MB) and mask are stored, in `bigdata/psi/work/`.
- The venv is in `bigdata/psi/env`.

## 5. Reproduce
```bash
rsync -azR analysis/bigdata/psi* cluster/bigdata/psi-* engaging:~/orcd/scratch/orbital-foundry-20261024-01a170b7/
ssh engaging 'cd ~/orcd/scratch/orbital-foundry-20261024-01a170b7 && sbatch cluster/bigdata/psi-inventory.sbatch'
# pull bigdata/psi/work/psi-objects.tsv.gz*, then:
python -I analysis/bigdata/psi_inventory_summary.py --tsv psi-objects.tsv.gz --out psi-inventory-summary.json
python -I analysis/bigdata/psi_dsi_morph.py manifest --tsv psi-objects.tsv.gz --out dsi-hr2-manifest.tsv   # copy to bigdata/psi/work/
ssh engaging 'cd ~/orcd/scratch/orbital-foundry-20261024-01a170b7 && M=$(sbatch --parsable cluster/bigdata/psi-mask.sbatch) && sbatch --dependency=afterok:$M cluster/bigdata/psi-dsi-quick.sbatch'
# (alternative for an idle mit_normal: cluster/bigdata/psi-dsi-array.sbatch, 24 x 1 CPU)
# merge: (head -1 shards/dsi-features-00.csv; tail -qn +2 shards/*.csv) | gzip > dsi-features.csv.gz
python -I analysis/bigdata/psi_dsi_morph.py calib --manifest dsi-hr2-manifest.tsv --out dsi-calib.json
python -I analysis/bigdata/psi_report.py inventory --summary psi-inventory-summary.json --meta psi-objects.tsv.gz.meta.json --jobs jobs.json --out data/results/bigdata/psi-inventory.json
python -I analysis/bigdata/psi_thumbs.py --picks picks_final.json --mask dsi-artefact-mask.npz --um-px 11.508 --outdir data/results/bigdata/psi-thumbs
python -I analysis/bigdata/psi_report.py morph --features dsi-features.csv.gz --calib dsi-calib.json --jobs jobs.json --out data/results/bigdata/dsi-morphology.json
```

## 6. What the website should and should not say
- **Say:** "30.3 TB of ISS physical-science data is openly catalogued by NASA PSI (three investigations); we listed every object, and streamed and analysed all 53,895 DSI axial frames (56.6 GB)."
- **Say:** "ISS solidification imagery supports quantitative, reproducible morphology at scale. Cell spacing ranges 220–730 µm across runs, evolves within runs, and differs 1.6–1.8× between 2010 sequences at the same pulling speed."
- **Say:** "One ISS facility day ranges from about 2–13 GB (DSI) to about 0.7 TB (PK-4 video). On-board reduction (about 16,000× for this metric) is the case for shared foundry data services."
- **Do not say:**
  - that microgravity gives better or larger cells, since there is no Earth control;
  - that we found a spacing–velocity law;
  - that DSI samples NPG barocalorics. DSI is a transparent SCN–camphor *analogue* for solidification-processed materials, not a cooling material itself.
- **Do not say** "processed 30 TB". The 30 TB was inventoried; 56.6 GB was processed.
