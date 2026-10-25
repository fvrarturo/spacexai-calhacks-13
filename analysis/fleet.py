"""Event-based benchmark with identical workloads and non-clairvoyant policies.

One process chamber per capsule. Jobs arrive online. Setup consumes chamber time;
finished batches wait for a capsule's periodic return opportunity. Return events
are an abstract transport service, not a modeled capsule deorbit/relaunch.
"""
import argparse
import hashlib
import json
import math
import random
import statistics
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
POLICIES = ['fifo', 'earliest_due', 'dedicated', 'coordinated']
FAMILIES = ['solution', 'thermal', 'assembly']
CAPABILITIES = [('solution', 'thermal'), ('thermal', 'assembly'), ('assembly', 'solution')]

def workload(seed, jobs=72, horizon=120, failure_rate=0.05, arrival_window=72):
    rng = random.Random(seed)
    rows = []
    for i in range(jobs):
        family = rng.choice(FAMILIES)
        arrival = rng.uniform(0, arrival_window)
        nominal = {'solution': 3, 'thermal': 5, 'assembly': 4}[family] * rng.uniform(.7, 1.3)
        rows.append(dict(id=i, family=family, arrival=arrival, due=arrival+rng.uniform(16, 44),
                         nominal=nominal, actual=nominal*rng.uniform(.8, 1.25), succeeds=rng.random() >= failure_rate))
    return sorted(rows, key=lambda j: (j['arrival'], j['id']))

def return_time(finish, capsule, cadence):
    offset = capsule * cadence / len(CAPABILITIES)
    return offset + math.ceil((finish - offset) / cadence - 1e-10) * cadence

def simulate(jobs, policy, horizon=120, cadence=24, setup_hours=2):
    if policy not in POLICIES or horizon <= 0 or cadence <= 0 or setup_hours < 0:
        raise ValueError('Invalid simulation settings')
    if any(j['actual'] <= 0 or j['nominal'] <= 0 or j['arrival'] < 0 or j['arrival'] > horizon or j['family'] not in FAMILIES for j in jobs):
        raise ValueError('Invalid workload')
    pending, events = [], []
    future = sorted(jobs, key=lambda j: (j['arrival'], j['id']))
    caps = [dict(busy_until=0, family=None) for _ in CAPABILITIES]
    now, cursor, occupied, setup_total = 0., 0, 0., 0.
    while now < horizon:
        while cursor < len(future) and future[cursor]['arrival'] <= now + 1e-9:
            pending.append(future[cursor]); cursor += 1
        idle = [c for c in range(len(caps)) if caps[c]['busy_until'] <= now + 1e-9]
        while idle and pending:
            candidates = []
            for c in idle:
                for j in pending:
                    if j['family'] not in CAPABILITIES[c]: continue
                    if policy == 'dedicated' and j['family'] != FAMILIES[c]: continue
                    setup = setup_hours if caps[c]['family'] not in (None, j['family']) else 0
                    predicted = return_time(now + setup + j['nominal'], c, cadence)
                    if policy in ('fifo', 'dedicated'): score = (j['arrival'], j['id'], c)
                    elif policy == 'earliest_due': score = (j['due'], j['arrival'], c)
                    else:
                        # Urgency uses only disclosed due dates, nominal durations and current state.
                        # Select the most urgent job, then the capsule with earliest predicted delivery.
                        slack = j['due'] - now - j['nominal']
                        score = (slack, predicted, setup, j['id'], c)
                    candidates.append((score, c, j, setup))
            if not candidates: break
            _, c, job, setup = min(candidates, key=lambda x: x[0])
            finish = now + setup + job['actual']
            delivery = return_time(finish, c, cadence)
            events.append(dict(**job, capsule=c, start=now, setup=setup, finish=finish,
                               delivery=delivery, delivered=job['succeeds'] and delivery <= horizon))
            occupied += min(horizon-now, setup+job['actual'])
            setup_total += min(horizon-now, setup)
            caps[c] = dict(busy_until=finish, family=job['family'])
            pending.remove(job); idle.remove(c)
        next_times = [c['busy_until'] for c in caps if c['busy_until'] > now + 1e-9]
        if cursor < len(future): next_times.append(future[cursor]['arrival'])
        if not next_times: break
        now = min(next_times)
    delivered = [e for e in events if e['delivered']]
    by_id = {e['id']: e for e in events}
    # All submitted jobs contribute, including pending and failed jobs (censored at horizon).
    restricted_wait = [min(by_id[j['id']]['delivery'], horizon)-j['arrival']
                       if j['id'] in by_id and by_id[j['id']]['delivered'] else horizon-j['arrival'] for j in jobs]
    return dict(policy=policy, submitted=len(jobs), delivered=len(delivered),
                on_time=sum(e['delivery'] <= e['due'] for e in delivered),
                on_time_rate=sum(e['delivery'] <= e['due'] for e in delivered)/max(1,len(jobs)),
                delivery_wait=statistics.mean(restricted_wait) if restricted_wait else 0,
                utilization=occupied/(len(caps)*horizon), setup_hours=setup_total,
                cost_per_delivered=(len(caps)*horizon + setup_total*.25)/len(delivered) if delivered else None,
                events=events)

def bootstrap_mean(values, seed=827, samples=1000):
    rng=random.Random(seed)
    means=sorted(statistics.mean(rng.choices(values, k=len(values))) for _ in range(samples))
    return dict(mean=statistics.mean(values), low=means[int(.025*samples)], high=means[int(.975*samples)])

def benchmark(seeds=100, start_seed=0, jobs=72, cadence=24, setup_hours=2, failure_rate=.05, arrival_window=72):
    if seeds < 2 or jobs < 1 or not 0 <= failure_rate <= 1 or not 0 < arrival_window <= 120:
        raise ValueError('Need >=2 seeds, positive jobs, valid failure rate and arrival window')
    results = {p: [] for p in POLICIES}
    metrics = ['on_time_rate','delivered','delivery_wait','utilization','setup_hours','cost_per_delivered']
    example = None
    for seed in range(start_seed, start_seed+seeds):
        work = workload(seed, jobs, failure_rate=failure_rate, arrival_window=arrival_window)
        for policy in POLICIES:
            result=simulate(work, policy, cadence=cadence, setup_hours=setup_hours)
            if seed == start_seed and policy == 'coordinated': example = result['events']
            results[policy].append({k:result[k] for k in metrics})
    summaries={p:{m:bootstrap_mean([r[m] for r in rows if r[m] is not None])
                  if any(r[m] is not None for r in rows) else None for m in metrics} for p,rows in results.items()}
    paired={p:bootstrap_mean([a['on_time_rate']-b['on_time_rate'] for a,b in zip(results['coordinated'],results[p])]) for p in POLICIES if p != 'coordinated'}
    config=dict(seeds=seeds,start_seed=start_seed,jobs=jobs,horizon_hours=120,capsules=3,return_cadence_hours=cadence,
                changeover_hours=setup_hours,failure_rate=failure_rate,arrival_window_hours=arrival_window)
    return dict(schema_version=1,kind='synthetic simulation',config=config,
                input_hash=hashlib.sha256(json.dumps(config,sort_keys=True).encode()).hexdigest(),
                code_hash=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                uncertainty='95% percentile bootstrap across seeds; paired policy differences use the same workload seeds. Intervals describe this model only.',
                assumptions=['Synthetic arrivals, durations, failures, capacity and costs; not measured flight operations.',
                             'One chamber per capsule; fixed capability sets; switching families incurs setup time.',
                             'Periodic return is an abstract transport service; no deorbit, relaunch, launch-window, mass, power or orbital dynamics model.',
                             'No retries; all failed or undelivered jobs remain in the denominator. Cost uses normalized units, not dollars.',
                             'Policies know arrivals only when they occur and use nominal duration; actual duration and success are hidden until completion.',
                             'Dedicated baseline uses the same hardware but reserves one family per capsule. No optimality claim.'],
                policies=summaries,paired_on_time_delta=paired,replicates=results,example=example)

def main():
    p=argparse.ArgumentParser()
    p.add_argument('--seeds',type=int,default=100);p.add_argument('--start-seed',type=int,default=0)
    p.add_argument('--jobs',type=int,default=72);p.add_argument('--cadence',type=float,default=24)
    p.add_argument('--setup-hours',type=float,default=2);p.add_argument('--failure-rate',type=float,default=.05)
    p.add_argument('--arrival-window',type=float,default=72)
    p.add_argument('--output',type=Path,default=ROOT/'data/results/fleet.json')
    a=p.parse_args();out=a.output; delattr(a,'output')
    result=benchmark(**vars(a));out.parent.mkdir(parents=True,exist_ok=True)
    temp=out.with_suffix('.tmp');temp.write_text(json.dumps(result,indent=2)+'\n');temp.replace(out)
    print(json.dumps({p:{k:round(v['mean'],4) if v else None for k,v in m.items()} for p,m in result['policies'].items()},indent=2))

if __name__ == '__main__':main()
