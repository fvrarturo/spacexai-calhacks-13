"""Paired differences, clustered at the independent experiment/flight block.

Input rows must already represent validated, matched run-level measurements.
This tool cannot resolve confounding or make independent units from images.
"""
import argparse
import csv
import hashlib
import json
import math
import statistics
from collections import defaultdict
from pathlib import Path
from .fleet import bootstrap_mean

def compare(rows):
    if not rows: raise ValueError('No measurements')
    if len({(r['metric'],r['unit']) for r in rows}) != 1: raise ValueError('Compare one metric and unit at a time')
    if len({r['pair_id'] for r in rows}) != len(rows): raise ValueError('Duplicate pair ID')
    blocks=defaultdict(list)
    for row in rows:
        if not row['pair_id'].strip() or not row['block_id'].strip(): raise ValueError('Pair and independent block IDs are required')
        flight,earth=float(row['flight_value']),float(row['earth_value'])
        if not math.isfinite(flight) or not math.isfinite(earth):raise ValueError('Non-finite measurement')
        blocks[row['block_id']].append(flight-earth)
    effects=[statistics.mean(values) for values in blocks.values()]
    return dict(kind='paired run-level comparison',metric=rows[0]['metric'],unit=rows[0]['unit'],
                pairs=len(rows),independent_blocks=len(blocks),effect_flight_minus_earth=statistics.mean(effects),
                effect_ci=bootstrap_mean(effects,samples=5000) if len(blocks)>=3 else None,
                weighting='Equal weight per independent block; mean paired difference within block.',
                limitations=['Independent block labels and matching require scientific review.',
                             'Fewer than three independent blocks: no bootstrap interval reported. Small block counts remain unstable.',
                             'A paired difference does not isolate gravity when hardware, chemistry or thermal history differ.'])

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('input',type=Path);p.add_argument('--output',type=Path,required=True)
    a=p.parse_args()
    with a.input.open(newline='') as handle:result=compare(list(csv.DictReader(handle)))
    result['input_sha256']=hashlib.sha256(a.input.read_bytes()).hexdigest()
    a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(result,indent=2)+'\n')
