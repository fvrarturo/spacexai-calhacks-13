"""Create a compact research handoff directly from the saved result files."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]

def run():
    read=lambda name:json.loads((ROOT/'data/results'/name).read_text())
    material=read('materials.json');hardware=read('foundry.json');fleet=read('fleet.json');sweep=read('sensitivity.json');pilot=read('dsi-qc.json')
    m=material['rows'][0];delta=fleet['paired_on_time_delta']['dedicated'];low=sweep['rows'][0]
    difference=low['paired_on_time_delta']['dedicated']
    report=f'''# Current results — Orbital Foundry

Generated from saved analysis outputs. The results have different evidence levels and should be presented separately.

| Pillar | Result | What it supports | What it does not establish |
|---|---|---|---|
| Materials | Published 50 mg/ml suspension: {m['earth']:.2f} → {m['flight']:.2f} cP; {m['relative_reduction_pct']:.1f}% lower mean viscosity. | A specific flight/Earth formulation comparison. | Our own independent replication, clinical benefit or persistent advantage over optimized Earth processing. |
| Foundry | {hardware['positions']} EXPRESS positions × {hardware['position_power_w']} W = {hardware['all_positions_max_w']} W; published rack budget {hardware['rack_power_w']} W. | Shared facilities require resource budgeting; at most {hardware['simultaneous_full_power_upper_bound']} maximum-power positions in this power-only bound. | Our capsule's resource capacity, thermal feasibility or qualified simultaneous operation. |
| Fleet | Initial coordinated v0 minus dedicated on-time rate: {delta['mean']*100:.2f} percentage points; paired 95% CI [{delta['low']*100:.2f}, {delta['high']*100:.2f}]. | An unfavorable benchmark that exposes the cost of changeovers in this model. | Real mission losses, an optimal scheduler, or proof coordination can never help. |

Materials source: [Reichert et al., Table 1](https://www.nature.com/articles/s41526-019-0090-3.pdf). Reported spreads are preserved in `materials.json`; no effect confidence interval is inferred from pooled technical repeats. The source's prose/table discrepancy is recorded with the extraction.

Foundry source: [NASA resource table, printed page 13]({hardware['source']}). This is station-supported hardware, not an autonomous capsule specification. [MSRR]({hardware['specialized_precedent']['source']}) provides a further precedent for specialized furnace inserts supplied by common services.

## The sensitivity result changes the discussion

At 36 jobs, zero changeover, 12-hour return cadence and no failures, coordinated v0 minus dedicated is {difference['mean']*100:.2f} percentage points (paired 95% CI [{difference['low']*100:.2f}, {difference['high']*100:.2f}]). This contrasts with the initial high-changeover scenario. All 24 predeclared scenarios are exposed in the workspace; these examples are not a universal ranking.

The next scheduler experiment should test family batching and selective sharing, with fresh held-out seeds. The design question is where flexibility earns more than its setup and interference costs.

## Raw-data readiness

{pilot['count']} NASA DSI bitmaps, {pilot['bytes']/1e6:.1f} MB, passed checksum/dimension and descriptive image-QC processing. They form a convenience sample within one run segment. No calibrated morphology, matched Earth controls, material advantage or independent-flight statistics were produced.

## Immediate next decision

Select one lead material × process × application. Define a useful performance threshold and the best Earth comparator, identify independent experimental units, and replace the corresponding illustrative cartridge loads with sourced or measured requirements. Keep the remaining material families as architecture cases until their evidence is sufficient.
'''
    (ROOT/'docs/RESULTS.md').write_text(report)
    print('Updated docs/RESULTS.md from saved results.')

if __name__=='__main__':run()
