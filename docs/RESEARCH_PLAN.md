# Orbital Foundry — research and execution plan

Working scope, 24 October 2026. Build an evidence system around a modular orbital materials foundry. The website explains the concept; the research workspace tracks what supports it and what remains untested.

## Three claims and the evidence required

| Pillar | Claim to test | Required evidence | Current state |
|---|---|---|---|
| Materials | Some processes deliver a valuable advantage in microgravity. | Matched Earth controls; independent replicates; uncertainty; application-specific performance. | One published comparison recalculated; NASA raw-image QC pilot. No new causal result. |
| Foundry design | Multiple processes can share infrastructure while retaining specialized equipment. | Stage-level requirements, compatibility map, resource budget and interference tests. | Published infrastructure precedent and power-budget bound; screening model with placeholder loads. No qualified capsule design. |
| Fleet operations | Coordinating production improves delivery, utilization or cost. | Same-workload comparisons against simple policies, sensitivity analysis and calibrated logistics. | Reproducible synthetic benchmark. Initial coordination heuristic loses to dedicated operation. |

## Lead product decision

Choose one lead material/process/application before expanding all six programs. Protein suspensions offer a published comparison; DSI offers accessible morphology data; neither automatically supplies the other's evidence. Keep the other materials as architecture use cases until their measurements support stronger claims.

For each candidate record the customer problem, product specification, best Earth route, minimum useful effect, return stability, required qualification, accessible data and estimated experimental cost. Set a minimum useful effect before comparing results. Do not pool unrelated materials into one “space benefit” score.

## Materials measurements

| Program | Structural proxy | Functional endpoint | Critical control |
|---|---|---|---|
| Protein crystals | Size distribution, aggregation | Viscosity at matched concentration; retained biological function | Optimized Earth mixing and thermal schedule |
| Small molecules | Form and crystal morphology | Dissolution, stability, reproducibility | Same compound, form-identification protocol and storage history |
| Cooling materials | Phase distribution, front morphology | Caloric response, hysteresis, lifetime after cycling | Matched composition and preconditioning; analogue images are not a refrigerant test |
| MOF membranes | Coverage, orientation, defect density | Selectivity, flux, adhesion, fouling and lifetime | Optimized ground synthesis, same substrate and feed |
| Bijel structures | Connectivity and coarsening | Reaction/transport performance and pressure drop | Matched chemistry and fixation; test survival after return |
| Photonic colloids | Order, domain size, defects | Optical loss/band response after stabilization | Same particle formulation, measurement geometry and Earth assembly route |

Use a provenance record for accession, DOI, file key/version, checksum, sample, independent experiment block, run, gravity condition, hardware, composition, temperature history, calibration and measurement method. Mark missing values explicitly.

Adjacent frames are correlated. Split train/validation/test by complete runs or flights; keep the final test set untouched while developing features. Blind manual annotation to treatment where possible. Report inclusion/exclusion counts, missingness, annotation agreement and calibration uncertainty.

`analysis/compare_runs.py` computes matched differences from reviewed run-level CSV rows. It weights independent blocks equally and bootstraps those blocks. With fewer than three blocks it reports no interval; even larger small samples require caution. It cannot correct unmeasured confounding. Use a hierarchical model only when actual replication supports it.

## What the foundry can parallelize

1. **Across research workstreams:** protocol extraction, evidence curation, requirements mapping and simulation can progress independently; freeze shared schemas before combining results.
2. **Across independent cartridges:** growth stages may coexist if electrical, thermal, contamination, pressure, field and vibration constraints permit. Keep wetted paths and product containment separate.
3. **Across time windows:** share cameras and metrology only when observation schedules tolerate it; sequence mixing, high-heat stages or field operations around sensitive growth.
4. **Across capsules:** specialize incompatible process families and coordinate assignments, completion dates and return logistics. Shared software does not imply physically shared power or thermal resources across spacecraft.

The common platform can supply time synchronization, power interfaces, telemetry, provenance, command envelopes and logistics. Specialized hardware retains chemistry-specific handling, furnaces, fields, mixers, fixation and acceptance logic. The compatibility screen uses illustrative power/heat assumptions and a simple disturbance rule. Replace each with sourced envelopes and transient measurements before design decisions.

NASA's [EXPRESS resource table](https://www.nasa.gov/wp-content/uploads/2023/08/np-2022-06-009-jsc-iss-tech-demo-mini-book-proof-3.pdf), printed page 13, provides a concrete precedent: ten payload positions, 500 W individual limits and a 2,000 W rack budget. A simple power-only bound allows four simultaneous 500 W loads; further cooling/integration limits still apply. These station-supported values are not specifications for our capsule. NASA also describes [MSRR interchangeable furnace inserts](https://ntrs.nasa.gov/citations/20140011639), supporting the separation of common services from specialized process hardware.

Produce an interface-control document and failure-mode table: resource, units, operating range, transient peak, allowed disturbance, contamination boundary, hazard response, evidence source, confidence and test owner. Compare dedicated, sequential shared and concurrently shared designs on useful throughput, mass, heat margin and failure isolation.

## Fleet experiments

Baseline policies: FIFO, earliest due date, dedicated family per capsule, and coordinated v0 (urgency plus predicted return among capable idle capsules). Use identical workloads and hidden actual durations/outcomes for each policy. Count every submitted job, including failures and undelivered jobs.

Primary endpoint: on-time deliveries / all submitted jobs. Secondary endpoints: delivered count, restricted waiting time, occupancy including setup, setup burden and normalized cost per delivered batch. Compare paired seed differences. Publish individual scenarios; avoid reporting only favorable averages.

The predeclared sensitivity grid varies job count (36/72/108), changeover (0/2 h), return cadence (12/24 h), and failure probability (0/0.1): 24 scenarios, 100 paired seeds each, using evaluation seeds 10000–10099. Keep these distinct from the initial seeds 0–99. Future heuristic development needs a new held-out evaluation set.

Add realistic downmass, power, launch/return windows, capsule reuse, maintenance and disruptions only with explicit sources and assumptions. The current periodic-return abstraction is not a flight dynamics or full lifecycle model.

## Data and compute strategy

NASA's [PSI public-data registry](https://registry.opendata.aws/nasa-psi/) identifies a public S3 mirror for DSI and OASIS. The local pilot inventories only the first 1,000 objects beneath one DSI prefix; it preserves the pagination token and does not claim a complete catalogue. Twelve lexicographically selected bitmaps are a convenience sample, not a randomized experiment.

Scale in stages: metadata → complete-run pilot → validated feature extraction → all eligible runs → independent-block comparisons. Store large immutable raw data in cluster scratch, manifests and compact results in version control, and reproducible feature tables in Parquet partitioned by investigation/run. Use CPU arrays for independent runs and simulations. Introduce a GPU only after a model has beaten a simpler validated measurement method.

## Team handoff and completion gates

Science owns valid comparisons and application outcomes; systems owns interfaces and constraints; operations owns simulation fairness and logistics; the teammate owns the video. These are workstream roles, not assigned personal commitments. Site content files contain task status, dependencies and deliverables. Browser notes are local only.

For the video, label every quantitative statement **published result**, **our computation**, **simulation**, or **hypothesis**. The pitch can use the architecture and the research opportunity; it must retain the negative scheduler result and the gap between morphology and useful performance.

The next research increment is complete when one lead product is selected, its control and independent units are established, its requirements replace the illustrative loads, and a calibrated experiment or simulation produces a reviewable decision. A polished website alone does not meet that gate.
