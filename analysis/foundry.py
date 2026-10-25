"""A power-only arithmetic bound from a published infrastructure table."""
import hashlib
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]

def run():
    source=ROOT/'data/published-foundry.json';data=json.loads(source.read_text())
    data['positions']=data['lockers']+data['drawers']
    data['simultaneous_full_power_upper_bound']=min(data['positions'],data['rack_power_w']//data['position_power_w'])
    data['all_positions_max_w']=data['positions']*data['position_power_w']
    data['input_sha256']=hashlib.sha256(source.read_bytes()).hexdigest()
    (ROOT/'data/results/foundry.json').write_text(json.dumps(data,indent=2)+'\n')
    return data

if __name__=='__main__':run()
