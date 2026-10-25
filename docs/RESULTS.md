# Current results — Orbital Foundry

The twelve big-data analyses (PDB, COD, CoRE MOF, NASA PSI, satellite tracking, launch/return, demand, literature) are summarised in [BIGDATA_RESULTS.md](BIGDATA_RESULTS.md). This page keeps the original three-pillar results.

Generated from saved analysis outputs. The results have different evidence levels and should be presented separately.

| Pillar | Result | What it supports | What it does not establish |
|---|---|---|---|
| Materials | Published 50 mg/ml suspension: 5.48 → 3.66 cP; 33.2% lower mean viscosity. | A specific flight/Earth formulation comparison. | Our own independent replication, clinical benefit or persistent advantage over optimized Earth processing. |
| Foundry | 10 EXPRESS positions × 500 W = 5000 W; published rack budget 2000 W. | Shared facilities require resource budgeting; at most 4 maximum-power positions in this power-only bound. | Our capsule's resource capacity, thermal feasibility or qualified simultaneous operation. |
| Fleet | Initial coordinated v0 minus dedicated on-time rate: -19.67 percentage points; paired 95% CI [-20.83, -18.46]. | An unfavorable benchmark that exposes the cost of changeovers in this model. | Real mission losses, an optimal scheduler, or proof coordination can never help. |

Materials source: [Reichert et al., Table 1](https://www.nature.com/articles/s41526-019-0090-3.pdf). Reported spreads are preserved in `materials.json`; no effect confidence interval is inferred from pooled technical repeats. The source's prose/table discrepancy is recorded with the extraction.

Foundry source: [NASA resource table, printed page 13](https://www.nasa.gov/wp-content/uploads/2023/08/np-2022-06-009-jsc-iss-tech-demo-mini-book-proof-3.pdf). This is station-supported hardware, not an autonomous capsule specification. [MSRR](https://ntrs.nasa.gov/citations/20140011639) provides a further precedent for specialized furnace inserts supplied by common services.

## The sensitivity result changes the discussion

At 36 jobs, zero changeover, 12-hour return cadence and no failures, coordinated v0 minus dedicated is 6.42 percentage points (paired 95% CI [5.06, 7.83]). This contrasts with the initial high-changeover scenario. All 24 predeclared scenarios are exposed in the workspace; these examples are not a universal ranking.

The next scheduler experiment should test family batching and selective sharing, with fresh held-out seeds. The design question is where flexibility earns more than its setup and interference costs.

## Raw-data readiness

12 NASA DSI bitmaps, 12.6 MB, passed checksum/dimension and descriptive image-QC processing. They form a convenience sample within one run segment. No calibrated morphology, matched Earth controls, material advantage or independent-flight statistics were produced.

## Immediate next decision

Select one lead material × process × application. Define a useful performance threshold and the best Earth comparator, identify independent experimental units, and replace the corresponding illustrative cartridge loads with sourced or measured requirements. Keep the remaining material families as architecture cases until their evidence is sufficient.
