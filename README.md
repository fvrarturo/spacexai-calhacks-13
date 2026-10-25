# Orbital Foundry

A maintainable research site and reproducible analysis workspace for the SpaceXAI × Cal Hacks 13.0 project.

**Live site: [zerogspot.us](https://zerogspot.us)** (published from `dist/` to the `fvrarturo/zero-g-spot` Pages repo with `scripts/publish_pages.sh`).

## Run locally

Python 3.10+ is required. No JavaScript package installation is needed.

```bash
npm run dev
```

Open `http://127.0.0.1:4173` for the cinematic site. Its chapters are `/index.html`, `/materials.html`, `/foundry.html`, `/network.html` and the methods page `/appendix.html`. The prior `/workspace.html` bookmark now opens the new vision page. The detailed research workspace is at `/research.html`, and the original modular story remains at `/story.html`. Source changes rebuild automatically; refresh the browser to see them. `python3 scripts/dev.py` works without npm.

```bash
npm run analyze   # published arithmetic + 100-seed synthetic fleet benchmark
npm test         # analysis invariants
npm run analyze:sweep  # 24 synthetic scenarios × 100 paired seeds
npm run report   # refresh the results handoff
npm run build    # static output in dist/
python3 -m analysis.bigdata_report   # regenerate docs/BIGDATA_RESULTS.md from the result files
python3 -m analysis.grok_review      # optional: Grok reviews every result file (needs XAI_API_KEY)
```

## Where to work

| Path | Purpose |
|---|---|
| `initial-work/` | Unchanged original HTML, README and broad exploratory research |
| `site/sections/` | The original story split into 13 independent sections |
| `site/pages/` | Four independently editable chapters: vision, materials, foundry and network |
| `site/content/` | Programs, sources, datasets, requirements, claims and task plan as JSON |
| `site/templates/` | Shared mission header/footer, original story chrome and research workspace layout |
| `site/static/js/mission/` | Canvas visuals, material dossiers, foundry explorer and fleet results |
| `site/static/js/workspace/` | Separate materials, compatibility, fleet and task-plan components |
| `site/static/css/`, `site/static/assets/` | Styles and extracted original image |
| `analysis/` | Reproducible Python analyses and bounded NASA ingestion |
| `analysis/bigdata/` | Big-data workstreams (PDB, COD/MOF/colloids, NASA PSI, satellite tracking, launch/return/demand/literature) |
| `cluster/bigdata/` | Slurm scripts actually run on MIT Engaging for those workstreams |
| `data/results/bigdata/` | Compact result files the site renders (one JSON per analysis, plus NASA thumbnails) |
| `docs/appendix/` | Methods note per workstream, shared brief and pitch guidance |
| `data/` | Published inputs, manifests and generated results; raw files ignored |
| `cluster/` | Small CPU smoke job, scenario array and NASA pilot |
| `docs/` | Research plan, model card, Engaging runbook and starter pack |
| `tests/` | Simulation invariants and independent-unit checks |

Edit task status and dependencies in `site/content/workspace.json`. Edit process loads in `site/content/compatibility.json`; they are illustrative assumptions until sourced and measured. Result cards load generated JSON; never hand-edit a result to improve the story. Browser working notes are local, with export for sharing.

The five featured candidates are protein crystals, small-molecule drug crystals, cooling materials, MOF membranes and photonic crystals. Their narrative lives in `site/content/material-dossiers.json`; the broader six-program research catalogue is preserved. The site uses native SVG/canvas and a locally saved generated hero image, with no runtime CDN dependencies. A persistent motion toggle and the system reduced-motion preference control decorative animation. See `docs/SITE_DESIGN.md` for visual provenance and verification.

The website serves from `dist/`, which is disposable. Keep durable edits in `site/`. It can be hosted by any static host; no deployment is configured by this change.

## Big-data evidence

Twelve analyses on public space and materials archives, run on MIT Engaging: 192 GB processed, about 256 million records, 36 datasets and 64 Slurm jobs. A further 30.3 TB of NASA archive was catalogued object by object. Each tab shows its evidence, its plan for using more data and the partners the data points to; the Appendix tab lists data, jobs, methods and limits for every result. Summary: [docs/BIGDATA_RESULTS.md](docs/BIGDATA_RESULTS.md). Methods: [docs/appendix/](docs/appendix/README.md). What each result lets us say: [docs/appendix/PITCH_GUIDANCE.md](docs/appendix/PITCH_GUIDANCE.md).

Tab display choices (which charts and series, short captions) live in `site/content/evidence-display.json`; curated partners in `site/content/partners.json`. Never edit numbers in result files: re-run the analysis.

## Evidence boundaries

Materials: one published comparison is recalculated, with reported spread and extraction discrepancies. Twelve NASA DSI bitmaps verify access and image QC, not a materials advantage. Foundry design: published NASA EXPRESS/MSRR infrastructure precedents, a power-budget calculation and a transparent compatibility screen; not flight qualification. Fleet: synthetic seeded comparisons; the initial coordinator loses to dedicated operation under the current assumptions.

Read [the current results](docs/RESULTS.md), [the research plan](docs/RESEARCH_PLAN.md), [model card](docs/MODEL_CARD.md), and [Engaging runbook](docs/ENGAGING.md) before extending claims or scaling compute. The full prior concept and original source catalogue remain available in the story and archive.

## Project context

Team: Arturo Favara and Emma Sampietro. The teammate is developing the video. The challenge asks for a clear problem and credible idea using space data; see the starter-pack PDF in `docs/` and the preserved initial README for the original brief.
