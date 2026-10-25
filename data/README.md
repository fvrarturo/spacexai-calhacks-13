# Data contract

`published-materials.json` and `published-foundry.json` contain manually checked source-table inputs, source locations, and interpretation limits. Generated cards are in `results/`; recompute them from `analysis/`, rather than editing result numbers.

`manifests/dsi-pilot.json` records a bounded NASA object listing, pagination state, selected object keys, sizes, ETags and SHA-256 hashes. `raw/` is ignored. To reproduce the pilot:

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r analysis/requirements.txt
python3 -m analysis.psi inventory
python3 -m analysis.psi fetch --count 12 --max-bytes 20000000
python3 -m analysis.psi qc
```

The selection is the first eligible images in a lexicographic object listing. All twelve are from one directory/run segment. They are not twelve independent experiments. Image QC has no physical calibration and does not estimate gravity effects.

`paired-runs-template.csv` is intentionally empty. Fill it only with scientifically reviewed run-level measurements: one unique `pair_id`, its independent `block_id`, one metric/unit per file, and matched flight/Earth values. Samples sharing a flight can share a block. Never populate it with invented replicates or individual frames and call them independent flights.

```bash
python3 -m analysis.compare_runs data/reviewed-runs.csv --output data/results/run-comparison.json
```

`results/fleet.json` preserves seed-level outputs and one schedule. `results/sweep/` contains all 24 scenario outputs; `results/sensitivity.json` is their validated summary. Initial scenario seeds are 0–99. Sensitivity seeds are 10000–10099, shared across scenarios for reproducibility. All workloads and cost weights are synthetic. See the model card for missing physics and operations.

Large future features should be stored outside Git, partitioned by investigation/run, with compact manifests and quality summaries committed. Retain source versions, processing configuration, environment versions and code hashes. Distinguish source-table extraction, raw-data measurement, simulation and hypothesis in every exported record.
