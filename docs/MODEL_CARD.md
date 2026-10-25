# Fleet model v0

This is a synthetic operations experiment, not measured spacecraft performance or a financial forecast.

## Mechanism

Three capsules each support two of three families: (solution, thermal), (thermal, assembly), and (assembly, solution). Each has one chamber. Jobs arrive online over 72 hours; the evaluation ends at 120 hours. Actual duration and success are sampled once per job and reused across all policies. Scheduling uses nominal durations; the realized completion time becomes observable when processing ends.

Setup consumes chamber time when switching families. Each capsule has a fixed periodic return offset. A job counts as delivered only if it succeeds and reaches a modeled return opportunity before the horizon. Failed jobs are not retried. This is a transport-service abstraction: the model does not deorbit, relaunch or remove a capsule at a return event.

## Policies and fairness

- FIFO: oldest feasible waiting job, deterministic capsule tie-break.
- Earliest due: earliest deadline among feasible waiting jobs.
- Dedicated: same hardware, but each capsule accepts only its designated family.
- Coordinated v0: smallest nominal deadline slack, then earliest predicted delivery among idle capable capsules, then smallest setup burden.

The v0 coordinator is a simple heuristic, not an optimal solver. Tie-breaking differences are part of the policies; counterfactual workloads are otherwise identical. It does not intentionally batch families or anticipate future arrivals. The dedicated policy's lower flexibility can reduce changeovers.

## Metrics

On-time rate uses all submitted jobs as its denominator. Delivered count includes late deliveries. Occupancy includes setup and processing clipped to the horizon; high occupancy does not establish productivity. Restricted waiting time includes all jobs and censors failures/pending jobs at the horizon, so it is not the mean delivery time among successes.

Normalized cost = (capsules × horizon hours + 0.25 × setup hours) / delivered count. The numerical cost weights are assumptions, not prices. Zero-delivery seeds produce null cost, retained in raw outputs and excluded from conditional mean cost.

Bootstrap 1,000 resamples over independent workload seeds for 95% percentile intervals. Policy differences are paired by seed. No interval quantifies uncertainty in the structural assumptions or future real operations. Different metrics do not identify a unique best policy; the workspace highlights the highest on-time rate only.

## Reproducibility and limits

`python3 -m analysis.fleet` writes configurations, code/input hashes, seed-level metrics, intervals and one example schedule. `analysis/sweep.py` runs 24 predeclared scenarios on separate seeds. `tests/test_analysis.py` checks capability constraints, no overlapping jobs, delivery timing, conservation and edge cases.

Missing: measured demand, demand mix shifts, multi-stage jobs, mass, per-stage power/heat, shelf life, replenishment, capsule failure, ground turnaround, launch/return windows, orbital mechanics, monetary costs and optimality bounds. These omissions limit any operational conclusion.

Initial finding: under 72 jobs, 2-hour changeovers, 24-hour return cadence and 5% failures, dedicated operation beats coordinated v0 on on-time delivery. Preserve this result when designing a batching policy; assess revisions on untouched seeds and scenarios.
