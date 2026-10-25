# Big-data analysis brief (shared by all analysis workstreams)

Read this before starting. It sets the conventions that let five parallel workstreams land in one website without collisions.

## The project in one paragraph

**Orbital Foundry** is our Cal Hacks 13.0 entry for the SpaceXSI/SpaceXAI "Make it Legendary" challenge. The brief reads: "Space gives you more to work with than almost any other field… enormous public datasets, decades of missions, and a literature no human can read all of. Real space data goes in and a legendary project comes out." Projects must be built with Cursor; Grok Bot gives bonus points.

The concept is a shared orbital materials foundry. Specialized sealed process cartridges share power, thermal, observation and data services, and the foundry returns materials to Earth. It starts with five candidates:
1. protein crystals (therapeutic suspensions; pembrolizumab is the published anchor)
2. small-molecule drug crystals (solid forms; Varda's ritonavir Form III)
3. cooling materials (barocaloric NPG-type solidification)
4. MOF membranes (lithium-selective ion separation)
5. photonic colloidal crystals

The website has three main tabs:
- **Materials:** the science of orbit-made materials and the top 5.
- **Foundry:** the design, the shareable processes, the challenges, and where SpaceX/xAI come in.
- **Network:** scale and a fleet of foundries.

A new **Appendix** tab will hold methods.

Your job is to produce **real big-data evidence** for one of those tabs: download a lot of public data on MIT Engaging, analyse it carefully, and write compact, honest result files the site can render.

## Ethos: non-negotiable

The existing site is careful about evidence levels. Keep it that way.
- Every number must come from data you actually downloaded and code you ran. **Never invent, round up, or "illustrate" a result.**
- Label each result with one of: **our computation on public data**, **published result**, **simulation**, **hypothesis**.
- State what a result does *not* show. A correlation in a public archive is not a causal microgravity effect. Selection bias, era, confounders and matching quality all need to be stated.
- Independent units matter. Do not treat correlated frames or records as independent replicates.
- If the data you planned on is unavailable, say so, and pivot to the next-best real dataset.

## MIT Engaging cluster rules

- SSH alias `engaging`. A master connection is already running; use `ssh engaging '...'`.
- **No heavy work on the login node.** Use Slurm.
- Account `mit_general`. Partitions:
  - `mit_quicktest`: ≤15 min.
  - `mit_normal`: ≤12 h, 96 CPU per user *shared by all five workstreams*.
  - `mit_data_transfer`: for big downloads, ≤3 days.
- **Respect the CPU cap given in your prompt.** The user has other jobs running. Do not touch them, cancel them, or `scancel` anything you did not submit.
- Prefix your job names with `of-<your-id>-` so they can be identified.
- Project root on the cluster: `~/orcd/scratch/orbital-foundry-20261024-01a170b7/`. Use **your own subfolder** `bigdata/<your-id>/`, holding `raw/`, `work/`, `env/` and `logs/`.
  - Scratch has about 760 GB free in total. Respect the storage cap in your prompt.
  - Never traverse `/orcd/scratch` or `/orcd/pool` broadly.
- Python: `module load miniforge`, then create *your own* venv at `bigdata/<your-id>/env` (`python -m venv`). Set `PIP_CACHE_DIR=~/orcd/scratch/pip_cache`. Never `conda init` and never `pip --user`. Login and compute nodes have internet (PyPI, HF, most sites).
- Read `/etc/claude-code/CLAUDE.md` on the cluster once. Bound all outputs (`head`, `tail -n`), and never `du` big trees (use `~/orcd/.quota`).
- Record every job: ID, partition, CPUs, wall time and state (`sacct -j ID -o jobid,state,elapsed,ncpus,maxrss`). These go into your result file.

## The local repo (the user's Mac)

The repo is at `/Users/arturofavara/Desktop/SpaceXAI_CalHacks_13`. You own only these paths:
- `analysis/bigdata/<your-id>*.py` (your analysis code; keep it readable and reproducible)
- `cluster/bigdata/<your-id>-*.sbatch`
- `data/results/bigdata/<your-id>*.json` (the compact results the site renders; schema below)
- `docs/appendix/<your-id>.md` (a full methods appendix: data, sizes, steps, job IDs, limitations, reproduce commands)

Rules for the repo:
- Do **not** edit `site/`, `scripts/`, other workstreams' files, `README.md` or existing analysis files.
- Large data never goes in the repo. `data/raw/` is gitignored; keep raw and intermediate data on the cluster.
- Do not `git commit` or `git push`. The main session integrates and commits.
- Sync code with `rsync -azR analysis/bigdata cluster/bigdata engaging:~/orcd/scratch/orbital-foundry-20261024-01a170b7/` (`-R` keeps the relative paths) and never use `--delete`. Pull results back with `rsync`.
- Never put secrets in files.

## Result file schema: `data/results/bigdata/<id>.json`

One file per analysis. Keep it under ~300 KB and at most ~400 points per chart series.

```json
{
  "id": "pdb-microgravity",
  "tab": "materials",                       // materials | foundry | network
  "material": "protein",                    // optional: protein | small | cooling | mof | photonic
  "title": "Every space-grown protein crystal in the PDB",
  "question": "Do protein crystals grown in orbit diffract better than the best Earth crystals of the same protein?",
  "headline": {"value": "38", "unit": "%", "text": "One plain-language sentence a judge understands in 5 seconds."},
  "evidence_level": "our computation on public data",
  "datasets": [{"name": "...", "url": "...", "license": "...", "records": 0, "bytes": 0, "accessed": "2026-10-24", "notes": "..."}],
  "compute": {"where": "MIT Engaging", "partitions": ["mit_normal"], "job_ids": ["..."], "cpu_hours": 0.0, "wall_minutes": 0.0, "peak_storage_gb": 0.0},
  "method": ["Step 1 ...", "Step 2 ..."],
  "charts": [{
    "id": "res-delta", "kind": "hist",      // bar | hbar | line | hist | scatter | stacked
    "title": "...", "subtitle": "...",
    "x": {"label": "...", "unit": "...", "scale": "linear"},   // linear | log | time | category
    "y": {"label": "...", "unit": "...", "scale": "linear"},
    "series": [{"name": "...", "points": [[0, 1], [1, 3]], "color": "orange"}],   // orange | cyan | violet | green | grey
    "annotations": [{"x": 0, "y": 0, "text": "..."}],
    "caption": "What the chart shows, and what it does not."
  }],
  "stats": {"any": "key numbers with CIs"},
  "findings": ["Plain sentences, each true and sourced to this analysis."],
  "limitations": ["..."],
  "future_big_data": ["How we would extend this with more or better data after the hackathon."],
  "partners": [{"name": "Org or company", "why": "Why they matter for this pillar", "evidence": "What in the data points to them"}],
  "code": ["analysis/bigdata/....py", "cluster/bigdata/....sbatch"],
  "reproduce": ["command 1", "command 2"],
  "generated_at": "ISO timestamp"
}
```

For category charts, use strings as `x` (e.g. `[["Protein", 12], ...]`). For time charts, use years as numbers or ISO dates.

## Pace and handoff

It is Saturday evening. Results are needed in about 3 hours of wall time, and judging is Sunday.
- Write results **incrementally**: a first valid JSON early, then refine it. The usage limit or a timeout can kill a session, and saved files survive.
- Prefer a smaller analysis that is right over a huge one that is unfinished. "Big data" still matters, though: download and process at real scale where it adds credibility.
- When done, reply with:
  - the headline numbers
  - the dataset sizes actually processed
  - the job IDs
  - the paths written
  - anything the website should say or avoid saying
