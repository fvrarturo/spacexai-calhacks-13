"""24 predeclared sensitivity scenarios; each Slurm array task is independent."""
import argparse
import itertools
import json
from pathlib import Path
from .fleet import benchmark

SCENARIOS=[dict(jobs=jobs,setup_hours=setup,cadence=cadence,failure_rate=failure)
           for jobs,setup,cadence,failure in itertools.product([36,72,108],[0,2],[12,24],[0,.1])]

def run(index, output, seeds=100):
    if not 0<=index<len(SCENARIOS):raise ValueError('Scenario index out of range')
    # Separate seed range from the initial scenario to avoid tuning to it.
    result=benchmark(seeds=seeds,start_seed=10000,**SCENARIOS[index])
    result['scenario_index']=index
    output.mkdir(parents=True,exist_ok=True)
    target=output/f'scenario-{index:02d}.json';temporary=target.with_suffix('.tmp')
    temporary.write_text(json.dumps(result,indent=2)+'\n');temporary.replace(target)
    print(f'Completed scenario {index}: {SCENARIOS[index]}',flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--index',type=int);p.add_argument('--seeds',type=int,default=100)
    p.add_argument('--output',type=Path,default=Path('data/results/sweep'))
    a=p.parse_args()
    for index in [a.index] if a.index is not None else range(len(SCENARIOS)):run(index,a.output,a.seeds)
