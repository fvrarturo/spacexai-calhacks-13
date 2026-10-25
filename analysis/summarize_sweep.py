"""Summarize complete scenario outputs without selecting favorable cases."""
import hashlib
import json
from pathlib import Path
from .sweep import SCENARIOS
ROOT=Path(__file__).resolve().parents[1]

def summarize(folder):
    rows=[]
    for i,config in enumerate(SCENARIOS):
        p=folder/f'scenario-{i:02d}.json'
        if not p.exists():raise ValueError(f'Missing scenario {i}; refusing a partial summary')
        data=json.loads(p.read_text())
        for key,value in config.items():
            mapped={'cadence':'return_cadence_hours','setup_hours':'changeover_hours'}.get(key,key)
            if data['config'][mapped]!=value:raise ValueError('Scenario configuration mismatch')
        rows.append(dict(index=i,config=config,policies={k:v['on_time_rate'] for k,v in data['policies'].items()},
                         paired_on_time_delta=data['paired_on_time_delta'],sha256=hashlib.sha256(p.read_bytes()).hexdigest()))
    hashes={json.loads((folder/f'scenario-{i:02d}.json').read_text())['code_hash'] for i in range(len(SCENARIOS))}
    if len(hashes)!=1:raise ValueError('Mixed analysis code versions')
    return dict(kind='synthetic sensitivity sweep',scenario_count=len(rows),rows=rows,
                code_hash=next(iter(hashes)),note='Each scenario uses the same 100 evaluation seeds, 10000–10099. No pooled significance claim across scenarios.')

if __name__=='__main__':
    result=summarize(ROOT/'data/results/sweep')
    (ROOT/'data/results/sensitivity.json').write_text(json.dumps(result,indent=2)+'\n')
    print('Summarized all 24 scenarios.')
