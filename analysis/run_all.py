"""Recompute offline results. Raw NASA retrieval is an explicit separate step."""
import json
from pathlib import Path
from .materials import run
from .foundry import run as run_foundry
from .fleet import benchmark
ROOT=Path(__file__).resolve().parents[1]
run()
run_foundry()
(ROOT/'data/results/fleet.json').write_text(json.dumps(benchmark(),indent=2)+'\n')
print('Recomputed published comparison and 100-seed synthetic fleet benchmark.')
