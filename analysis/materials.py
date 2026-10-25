"""Transparent arithmetic on published aggregates; never invent raw replicates."""
import hashlib
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]

def run():
    source=ROOT/'data/published-materials.json'
    data=json.loads(source.read_text())
    for row in data['rows']:
        row['absolute_reduction']=round(row['earth']-row['flight'],4)
        row['relative_reduction_pct']=round((1-row['flight']/row['earth'])*100,4)
        row['effect_ci']=None
    data.update(kind='published comparison, independently recalculated',input_sha256=hashlib.sha256(source.read_bytes()).hexdigest())
    (ROOT/'data/results/materials.json').write_text(json.dumps(data,indent=2)+'\n')
    return data

if __name__=='__main__':run()
