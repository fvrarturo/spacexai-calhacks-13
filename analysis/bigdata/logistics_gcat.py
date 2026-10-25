#!/usr/bin/env python3
"""Logistics workstream, questions 1 and 2: launch scale and return cadence from GCAT.

Data: Jonathan McDowell's General Catalog of Artificial Space Objects (GCAT),
https://planet4589.org/space/gcat/ (CC-BY). Standard library only.

    python3 -I analysis/bigdata/logistics_gcat.py --raw RAW_DIR --download \
        --out-dir data/results/bigdata

Writes launch-scale.json and return-cadence.json (schema: docs/appendix/AGENT_BRIEF.md).
Every number in the outputs is computed here from the downloaded TSV files.
"""
import argparse
import collections
import csv
import datetime as dt
import hashlib
import json
import math
import os
import re
import statistics
import sys
import urllib.request

GCAT = 'https://planet4589.org/space/gcat/tsv/'
FILES = {
    'launch.tsv': 'launch/launch.tsv',          # every launch (orbital and suborbital)
    'launchlog.tsv': 'derived/launchlog.tsv',   # derived: one row per payload on orbital launches
    'satcat.tsv': 'cat/satcat.tsv',             # main object catalog, first phase of each object
    'satcat070k.tsv': 'cat/satcat070k.tsv',
    'satcat100k.tsv': 'cat/satcat100k.tsv',
    'satcat270k.tsv': 'cat/satcat270k.tsv',
    'satcat700M.tsv': 'cat/satcat700M.tsv',
    'auxcat.tsv': 'cat/auxcat.tsv',             # auxiliary objects (capsules, cargo, ...)
    'ecat.tsv': 'cat/ecat.tsv',                 # extra phases: undock, landing, ...
    'lprcat.tsv': 'cat/lprcat.tsv',             # lunar/planetary objects (sample-return capsules)
    'ftocat.tsv': 'cat/ftocat.tsv',             # failed-to-orbit objects
    'tmpcat.tsv': 'cat/tmpcat.tsv',
    'csocat.tsv': 'cat/csocat.tsv',
    'psatcat.tsv': 'cat/psatcat.tsv',           # payload details (mission end dates, programs)
}
OBJECT_CATS = ['satcat.tsv', 'satcat070k.tsv', 'satcat100k.tsv', 'satcat270k.tsv', 'satcat700M.tsv',
               'auxcat.tsv', 'lprcat.tsv', 'tmpcat.tsv', 'csocat.tsv']
PHASE_CATS = OBJECT_CATS + ['ecat.tsv']
MONTHS = {m: i + 1 for i, m in enumerate('Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec'.split())}
SYNTHETIC_CADENCE_HOURS = [12, 24]   # analysis/fleet.py assumption (default 24 h, sensitivity 12 h)


# ---------------------------------------------------------------- loading
def download(raw):
    os.makedirs(raw, exist_ok=True)
    for name, path in FILES.items():
        dest = os.path.join(raw, name)
        if os.path.exists(dest) and os.path.getsize(dest) > 0:
            continue
        req = urllib.request.Request(GCAT + path, headers={'User-Agent': 'orbital-foundry-hackathon/1.0'})
        with urllib.request.urlopen(req, timeout=300) as r, open(dest + '.part', 'wb') as f:
            f.write(r.read())
        os.replace(dest + '.part', dest)


def load(raw, name):
    """Return (rows, meta) for a GCAT TSV; rows are dicts with stripped values."""
    path = os.path.join(raw, name)
    updated = None
    rows = []
    with open(path, encoding='utf-8', newline='') as f:
        reader = csv.reader(f, delimiter='\t')
        header = [c.lstrip('#').strip() for c in next(reader)]
        for r in reader:
            if not r:
                continue
            if r[0].startswith('#'):
                if 'Updated' in r[0]:
                    updated = r[0].lstrip('# ').strip()
                continue
            d = dict(zip(header, (x.strip() for x in r)))
            d['_file'] = name
            rows.append(d)
    with open(path, 'rb') as f:
        sha = hashlib.sha256(f.read()).hexdigest()
    return rows, {'file': name, 'url': GCAT + FILES[name], 'records': len(rows),
                  'bytes': os.path.getsize(path), 'sha256': sha, 'updated': updated}


def parse_vague(s):
    """GCAT 'vague date' -> (datetime, precision) or (None, None). '2026 Feb 27 0744?' etc."""
    if not s or s == '-':
        return None, None
    s = s.replace('?', ' ').strip()
    m = re.match(r'^(\d{4})(?:\s+([A-Z][a-z]{2}))?(?:\s+(\d{1,2}))?(?:\s+(\d{2})(\d{2})(?::(\d{2}))?)?', s)
    if not m:
        return None, None
    y, mon, day, hh, mm, ss = m.groups()
    if not mon:
        return dt.datetime(int(y), 7, 1), 'year'
    if not day:
        return dt.datetime(int(y), MONTHS[mon], 15), 'month'
    if hh is None:
        return dt.datetime(int(y), MONTHS[mon], int(day), 12), 'day'
    return dt.datetime(int(y), MONTHS[mon], int(day), int(hh), int(mm), int(ss or 0)), 'minute'


def num(s):
    try:
        return float(s)
    except (TypeError, ValueError):
        return None


def pct(values, q):
    """Linear-interpolated percentile (q in [0, 100]) of a non-empty list."""
    v = sorted(values)
    if len(v) == 1:
        return v[0]
    k = (len(v) - 1) * q / 100.0
    lo, hi = math.floor(k), math.ceil(k)
    return v[lo] + (v[hi] - v[lo]) * (k - lo)


def r1(x, nd=1):
    return None if x is None else round(x, nd)


# ---------------------------------------------------------------- Q1: launch scale
def is_orbital_attempt(code):
    """GCAT LaunchCode: first letter O (orbital) or D (deep space); second S (success) or F (failure).
    OE (failed before ignition) and OA (abort, no launch) are not launches."""
    return len(code) >= 2 and code[0] in 'OD' and code[1] in 'SF'


def launch_scale(raw, metas, cutoff):
    launches, _ = load(raw, 'launch.tsv'), None
    launches = launches[0]
    log = load(raw, 'launchlog.tsv')[0]
    first_year, last_year = 1957, cutoff.year

    orb = [r for r in launches if is_orbital_attempt(r['LaunchCode'])]
    for r in orb:
        r['_dt'] = parse_vague(r['Launch_Date'])[0]
    tags = {r['Launch_Tag']: r for r in orb}

    # mass lookup: first-phase row of every object (kg)
    mass = {}
    mflag = {}
    for name in OBJECT_CATS:
        for r in load(raw, name)[0]:
            j = r.get('JCAT')
            if j and j not in mass:
                mass[j] = num(r.get('Mass'))
                mflag[j] = r.get('MassFlag', '')

    years = list(range(first_year, last_year + 1))
    Y = {y: collections.Counter() for y in years}
    for r in orb:
        y = r['_dt'].year
        spx = r['Agency'] == 'SPX'
        Y[y]['attempts'] += 1
        Y[y]['spx_attempts'] += spx
        if r['LaunchCode'][1] == 'S':
            Y[y]['successes'] += 1
            Y[y]['spx_successes'] += spx
        else:
            Y[y]['failures'] += 1
        Y[y]['orbpay_t'] += num(r['OrbPay']) or 0.0
        Y[y]['spx_orbpay_t'] += (num(r['OrbPay']) or 0.0) if spx else 0.0

    # payloads per year (payloads on successful orbital/deep-space launches; launchlog is payloads only)
    rideshare = collections.defaultdict(list)
    n_payload_rows = 0
    for p in log:
        code = p['Launch_Code']
        if not is_orbital_attempt(code):
            continue
        n_payload_rows += 1
        y = int(p['Launch_Date'][:4])
        ok = code[1] == 'S'
        spx = p['Agency'] == 'SPX'
        starlink = p['Name'].startswith('Starlink') or p['PLName'].startswith('Starlink')
        m = mass.get(p['JCAT'])
        key = 'pl' if ok else 'pl_lost'
        Y[y][key] += 1
        if not ok:
            continue
        Y[y]['spx_pl'] += spx
        Y[y]['starlink_pl'] += starlink
        if m and m > 0:
            Y[y]['pl_with_mass'] += 1
            Y[y]['mass_kg'] += m
            Y[y]['spx_mass_kg'] += m if spx else 0
            Y[y]['starlink_mass_kg'] += m if starlink else 0
            Y[y]['mass_flagged_kg'] += m if '?' in mflag.get(p['JCAT'], '') else 0
        lr = tags.get(p['Launch_Tag'])
        if lr and re.search(r'\b(Transporter|Bandwagon)-\d+', lr['Flight'] + ' ' + lr['Mission']):
            rideshare[p['Launch_Tag']].append((p, m))

    # rideshare missions (every Transporter/Bandwagon launch, even if a payload count is 0)
    rs = []
    for r in orb:
        mm = re.search(r'\b((Transporter|Bandwagon)-\d+)', r['Flight'] + ' ' + r['Mission'])
        if not mm:
            continue
        pls = rideshare.get(r['Launch_Tag'], [])
        masses = [m for _, m in pls if m and m > 0]
        owners = {p['SatOwner'] for p, _ in pls}
        rs.append(dict(mission=mm.group(1), launch_tag=r['Launch_Tag'], date=r['_dt'].date().isoformat(),
                       outcome=r['LaunchCode'], payloads=len(pls), payloads_with_mass=len(masses),
                       mass_kg=round(sum(masses), 1), distinct_owners=len(owners)))
    rs.sort(key=lambda x: x['date'])

    # Starship: every launch of the Starship vehicle in launch.tsv (any category), integrated flights separately
    ss = []
    for r in launches:
        if not r['LV_Type'].startswith('Starship'):
            continue
        code = r['LaunchCode']
        ss.append(dict(launch_tag=r['Launch_Tag'], date=parse_vague(r['Launch_Date'])[0].date().isoformat(),
                       vehicle=r['LV_Type'], variant=r['Variant'], flight=r['Flight'] if r['Flight'] != '-' else r['Mission'], ship=r['Mission'],
                       launch_code=code, category={'O': 'orbital', 'N': 'near-orbital', 'A': 'atmospheric hop'}.get(code[0], code[0]),
                       success=len(code) > 1 and code[1] == 'S', apogee_km=num(r['Apogee']), perigee_km=num(r['Perigee'])))
    integrated = [s for s in ss if s['category'] != 'atmospheric hop']
    # payloads carried on Starship flights (launchlog rows with LV_Type Starship)
    ss_payloads = collections.Counter(p['Launch_Tag'] for p in log if p['LV_Type'].startswith('Starship'))
    for s in integrated:
        s['payloads_catalogued'] = ss_payloads.get(s['launch_tag'], 0)

    # year-to-date comparison (same calendar window as the data cutoff)
    def ytd(y):
        end = dt.datetime(y, cutoff.month, cutoff.day, 23, 59)
        sel = [r for r in orb if r['_dt'].year == y and r['_dt'] <= end]
        return dict(year=y, attempts=len(sel), spx=sum(r['Agency'] == 'SPX' for r in sel))
    ytds = [ytd(y) for y in (2023, 2024, 2025, 2026)]

    table = []
    for y in years:
        c = Y[y]
        table.append(dict(year=y, partial=(y == cutoff.year), attempts=c['attempts'], successes=c['successes'],
                          failures=c['failures'], spacex_attempts=c['spx_attempts'],
                          spacex_share_attempts=r1(100 * c['spx_attempts'] / c['attempts'], 1) if c['attempts'] else None,
                          payloads=c['pl'], payloads_lost_on_failures=c['pl_lost'], spacex_payloads=c['spx_pl'],
                          starlink_payloads=c['starlink_pl'],
                          spacex_share_payloads=r1(100 * c['spx_pl'] / c['pl'], 1) if c['pl'] else None,
                          mass_t=r1(c['mass_kg'] / 1000, 1), spacex_mass_t=r1(c['spx_mass_kg'] / 1000, 1),
                          starlink_mass_t=r1(c['starlink_mass_kg'] / 1000, 1),
                          spacex_share_mass=r1(100 * c['spx_mass_kg'] / c['mass_kg'], 1) if c['mass_kg'] else None,
                          mass_coverage_pct=r1(100 * c['pl_with_mass'] / c['pl'], 1) if c['pl'] else None,
                          mass_flagged_estimate_pct=r1(100 * c['mass_flagged_kg'] / c['mass_kg'], 1) if c['mass_kg'] else None,
                          orbpay_t=r1(c['orbpay_t'], 1), spacex_orbpay_t=r1(c['spx_orbpay_t'], 1)))
    T = {t['year']: t for t in table}
    last_full = cutoff.year - 1
    tot_attempts = sum(t['attempts'] for t in table)
    tot_payloads = sum(t['payloads'] for t in table)

    def window_sum(k, y0, y1):
        return sum(T[y][k] for y in range(y0, y1 + 1))

    stats = dict(
        data_cutoff=cutoff.date().isoformat(),
        orbital_launch_attempts_all_time=tot_attempts,
        payloads_on_successful_orbital_launches_all_time=tot_payloads,
        last_full_year=last_full,
        last_full_year_attempts=T[last_full]['attempts'],
        last_full_year_spacex_attempts=T[last_full]['spacex_attempts'],
        last_full_year_spacex_share_attempts_pct=T[last_full]['spacex_share_attempts'],
        last_full_year_payloads=T[last_full]['payloads'],
        last_full_year_spacex_share_payloads_pct=T[last_full]['spacex_share_payloads'],
        last_full_year_starlink_payloads=T[last_full]['starlink_payloads'],
        last_full_year_mass_t=T[last_full]['mass_t'],
        last_full_year_spacex_share_mass_pct=T[last_full]['spacex_share_mass'],
        last_full_year_mass_coverage_pct=T[last_full]['mass_coverage_pct'],
        attempts_2015=T[2015]['attempts'], payloads_2015=T[2015]['payloads'], mass_t_2015=T[2015]['mass_t'],
        growth_attempts_2015_to_last_full=r1(T[last_full]['attempts'] / T[2015]['attempts'], 2),
        growth_payloads_2015_to_last_full=r1(T[last_full]['payloads'] / T[2015]['payloads'], 2),
        growth_mass_2015_to_last_full=r1(T[last_full]['mass_t'] / T[2015]['mass_t'], 2),
        payloads_2016_2025_spacex_share_pct=r1(100 * window_sum('spacex_payloads', 2016, 2025) / window_sum('payloads', 2016, 2025), 1),
        year_to_date=ytds,
        rideshare_missions=len(rs),
        rideshare_payloads_total=sum(x['payloads'] for x in rs),
        rideshare_payloads_per_mission_median=statistics.median([x['payloads'] for x in rs]) if rs else None,
        rideshare_payloads_per_mission_max=max((x['payloads'] for x in rs), default=None),
        rideshare_payloads_per_mission_min=min((x['payloads'] for x in rs), default=None),
        starship_integrated_flights=len(integrated),
        starship_integrated_flights_coded_orbital=sum(s['category'] == 'orbital' for s in integrated),
        starship_integrated_successes=sum(s['success'] for s in integrated),
        starship_hops=len(ss) - len(integrated),
    )
    return table, rs, integrated, ss, stats, n_payload_rows, len(mass)


# ---------------------------------------------------------------- Q2: return cadence
CLASS_INFO = {
    # class: (label, chart color, downmass for a commercial foundry product, note)
    'dragon_cargo': ('Dragon cargo (CRS)', 'orange', 'yes',
                     'Routine pressurized ISS downmass; GCAT catalogues a "Down Cargo" object landed inside each recent CRS Dragon.'),
    'dragon_crew': ('Crew Dragon (NASA + private)', 'cyan', 'limited',
                    'Returns some research with crew; GCAT catalogues no separate down-cargo object for crew flights.'),
    'varda': ('Varda W-series', 'violet', 'yes (own product)',
              'Commercial free-flyer reentry vehicle that returns its own manufactured product.'),
    'spacex_starfall': ('SpaceX Starfall', 'violet', 'unknown',
                        'SpaceX-owned recoverable capsule catalogued in GCAT from 2026; payload purpose not stated in GCAT.'),
    'starliner': ('Boeing Starliner', 'cyan', 'limited',
                  'Crew vehicle; GCAT records 300 kg of down cargo on the 2024 crewed test flight.'),
    'soyuz': ('Soyuz', 'grey', 'limited',
              'Crew return to Kazakhstan; small downmass, not a routine commercial channel for US payloads.'),
    'shenzhou': ('Shenzhou', 'grey', 'not for US payloads',
                 "China's crew vehicle for the Tiangong station."),
    'china_recoverable_sat': ('China recoverable satellites (SJ-10, SJ-19, FSW)', 'grey', 'not for US payloads',
                              'Chinese free-flying recoverable science satellites.'),
    'military_spaceplane': ('Military spaceplanes (X-37B, CSSHQ)', 'grey', 'no', 'Classified payloads; not a commercial channel.'),
    'other_recoverable': ('Other recoverable capsules and demos', 'green', 'case by case',
                          'Bion-M, Foton, reentry demos (IXV, LOFTID, HSRC, ATMOS Phoenix) and others.'),
    'starship_test': ('Starship test ships', 'orange', 'not yet',
                      'Test ships recorded as landed after (near-)orbital flights; no payload return to date.'),
    'shuttle': ('Space Shuttle', 'grey', 'historical', 'Retired 2011.'),
    'military_film_capsule': ('Russian film-return capsules', 'grey', 'no', 'Reconnaissance film capsules; ended 2015.'),
    'deep_space_return': ('Deep-space returns (Orion, sample capsules)', 'grey', 'no', 'Lunar/planetary missions, not LEO return slots.'),
}
US_ACCESSIBLE = ['dragon_cargo', 'dragon_crew', 'varda', 'spacex_starfall', 'starliner']
LEO_CAPSULE = [c for c in CLASS_INFO if c not in ('deep_space_return', 'starship_test', 'military_film_capsule',
                                                  'military_spaceplane', 'shuttle')]


def classify(r):
    bus, name, pl, f = r.get('Bus', ''), r.get('Name', ''), r.get('PLName', ''), r['_file']
    text = f'{name} {pl}'
    if f == 'lprcat.tsv' or bus in ('Orion', 'Orion CM', 'DASH', 'CE-5', 'CE-6', 'CE5T1', 'Stardust SRC', 'Genesis'):
        return 'deep_space_return'
    if bus.startswith('Dragon'):
        if re.search(r'\bCRS-\d+', text) or (re.search(r'Dragon C1\d\d', pl) and 'Crew' not in name) or name in ('Dragon C1', 'Dragon C2', 'Dragon C2+'):
            return 'dragon_cargo'
        return 'dragon_crew'
    if bus.startswith('Varda'):
        return 'varda'
    if bus.startswith('Starfall'):
        return 'spacex_starfall'
    if bus.startswith('CST-100'):
        return 'starliner'
    if bus.startswith('Starship'):
        return 'starship_test'
    if bus.startswith('Soyuz') or bus.startswith('7K') or name.startswith('Soyuz'):
        return 'soyuz'
    if bus.startswith('Shenzhou') or name.startswith('Shenzhou'):
        return 'shenzhou'
    if bus.startswith('STS'):
        return 'shuttle'
    if bus in ('X-37', 'CSSHQ'):
        return 'military_spaceplane'
    if bus in ('SpK', 'MSpK') or bus.startswith("Yantar") or "Kobal't" in pl:
        return 'military_film_capsule'
    if bus.startswith('FSW') or bus.startswith('SJ'):
        return 'china_recoverable_sat'
    return 'other_recoverable'


def gap_stats(times):
    times = sorted(times)
    gaps = [(b - a).total_seconds() / 3600 for a, b in zip(times, times[1:])]
    if not gaps:
        return dict(n_returns=len(times), n_gaps=0), gaps
    span = (times[-1] - times[0]).total_seconds() / 3600
    # mean wait for a product finished at a uniformly random time between the first and last return
    wait = sum(g * g for g in gaps) / (2 * sum(gaps)) if sum(gaps) else None
    return dict(n_returns=len(times), n_gaps=len(gaps),
                median_gap_hours=r1(statistics.median(gaps)), mean_gap_hours=r1(statistics.mean(gaps)),
                p10_gap_hours=r1(pct(gaps, 10)), p25_gap_hours=r1(pct(gaps, 25)), p75_gap_hours=r1(pct(gaps, 75)),
                p90_gap_hours=r1(pct(gaps, 90)), min_gap_hours=r1(min(gaps)), max_gap_hours=r1(max(gaps)),
                median_gap_days=r1(statistics.median(gaps) / 24, 2), p90_gap_days=r1(pct(gaps, 90) / 24, 2),
                max_gap_days=r1(max(gaps) / 24, 2),
                mean_wait_hours_random_finish=r1(wait), mean_wait_days_random_finish=r1(wait / 24, 2) if wait else None,
                span_days=r1(span / 24, 1)), gaps


def return_cadence(raw, cutoff):
    phases = []
    for name in PHASE_CATS:
        phases += load(raw, name)[0]
    # Earth landings ('L', 'L?') of orbital objects: payload-type entries only (cargo inside capsules is separate)
    events, seen = [], set()
    for r in phases:
        st = r.get('Status', '').split(' ')[0]
        if st not in ('L', 'L?') or r.get('Primary') != 'Earth':
            continue
        if not r.get('Type', '').startswith('P'):
            continue
        t, prec = parse_vague(r.get('DDate'))
        if t is None:
            continue
        key = (r['JCAT'], t.date())
        if key in seen:
            continue
        seen.add(key)
        events.append(dict(jcat=r['JCAT'], name=r['Name'], plname=r['PLName'], bus=r['Bus'], owner=r['Owner'],
                           file=r['_file'], t=t, precision=prec, dest=r.get('Dest', ''), mass_kg=num(r.get('Mass')),
                           cls=classify(r), uncertain=('?' in r.get('DDate', '') or st == 'L?')))
    events.sort(key=lambda e: e['t'])

    # reentries of commercial return capsules that are NOT recorded as landed (status R/D): honesty list
    not_landed = []
    for r in phases:
        st = r.get('Status', '').split(' ')[0]
        if st in ('R', 'D') and r.get('Primary') == 'Earth' and re.search(r'Reentry Vehicle|Mission Possible|Starfall', r.get('Name', '')) \
                and not r.get('Type', '').startswith('C'):
            t, _ = parse_vague(r.get('DDate'))
            not_landed.append(dict(jcat=r['JCAT'], name=r['Name'], owner=r['Owner'], status=st,
                                   date=t.date().isoformat() if t else None, file=r['_file']))
    not_landed.sort(key=lambda x: x['date'] or '')

    # down cargo: GCAT 'Down Cargo' objects; final phase status AL* = landed inside a capsule, AR* = burned with the vehicle
    dc_final = {}
    for r in phases:
        if 'Down Cargo' not in r.get('Name', ''):
            continue
        t, _ = parse_vague(r.get('DDate'))
        if t is None:
            continue
        j = r['JCAT']
        if j not in dc_final or t > dc_final[j][0]:
            dc_final[j] = (t, r)
    downcargo = collections.defaultdict(lambda: collections.Counter())
    dc_rows = []
    for j, (t, r) in dc_final.items():
        st = r.get('Status', '')
        fate = 'returned' if st.startswith('AL') else ('burned' if st.startswith('AR') else 'other')
        m = num(r.get('Mass')) or 0.0
        vehicle = re.sub(r'\s*Down Cargo.*$', '', r['Name'])
        fam = ('SpaceX Dragon' if vehicle.startswith('SpX') else 'Progress' if vehicle.startswith('Progress') else
               'Cygnus (NG)' if 'NG-' in vehicle else 'Tianzhou' if vehicle.startswith('Tianzhou') else
               'Space Shuttle' if vehicle.startswith('STS') else 'Starliner' if 'Boe' in vehicle else
               'HTV/HTV-X' if vehicle.startswith('HTV') else 'other')
        downcargo[t.year][f'{fate}_kg'] += m
        downcargo[t.year][f'{fate}_n'] += 1
        dc_rows.append(dict(jcat=j, vehicle=vehicle, family=fam, year=t.year, fate=fate, mass_kg=m,
                            mass_flag=r.get('MassFlag', '')))

    # ---- windows
    w_start = dt.datetime(2021, 1, 1)
    w_end = cutoff
    def sel(classes, a=w_start, b=w_end):
        return [e['t'] for e in events if e['cls'] in classes and a <= e['t'] <= b]
    groups = collections.OrderedDict([
        ('all_leo_capsules', LEO_CAPSULE),
        ('us_accessible', US_ACCESSIBLE),
        ('dragon_all', ['dragon_cargo', 'dragon_crew']),
        ('dragon_cargo', ['dragon_cargo']),
        ('dragon_crew', ['dragon_crew']),
        ('varda', ['varda']),
        ('soyuz', ['soyuz']),
        ('shenzhou', ['shenzhou']),
        ('commercial_downmass_yes', ['dragon_cargo', 'varda']),
    ])
    yrs = (w_end - w_start).total_seconds() / (365.25 * 86400)
    calib = collections.OrderedDict()
    all_gaps = {}
    for g, classes in groups.items():
        s, gaps = gap_stats(sel(classes))
        s['returns_per_year'] = r1(s['n_returns'] / yrs, 2)
        s['classes'] = classes
        s['ratio_median_gap_to_24h'] = r1(s['median_gap_hours'] / 24, 1) if s.get('median_gap_hours') else None
        s['gaps_hours'] = [round(x, 1) for x in gaps]
        calib[g] = s
        all_gaps[g] = gaps
    # earlier era, for context
    era_prev = collections.OrderedDict()
    for g in ('all_leo_capsules', 'us_accessible', 'dragon_cargo'):
        s, _ = gap_stats(sel(groups[g], dt.datetime(2012, 1, 1), dt.datetime(2020, 12, 31, 23, 59)))
        era_prev[g] = s

    # per-year counts by class
    first_year = 2000
    years = list(range(first_year, cutoff.year + 1))
    per_year = {c: collections.Counter() for c in CLASS_INFO}
    for e in events:
        if e['t'].year >= first_year:
            per_year[e['cls']][e['t'].year] += 1

    return events, not_landed, downcargo, dc_rows, calib, era_prev, per_year, years, all_gaps, (w_start, w_end, yrs)


# ---------------------------------------------------------------- outputs
def dataset_entries(metas, used, accessed):
    out = []
    for n in used:
        m = metas[n]
        out.append(dict(name=f'GCAT {n}', url=m['url'], license='CC-BY (J. McDowell, planet4589.org)',
                        records=m['records'], bytes=m['bytes'], accessed=accessed,
                        notes=f"{m['updated'] or ''}; sha256 {m['sha256'][:16]}"))
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('--raw', required=True, help='directory holding (or receiving) the GCAT TSV files')
    ap.add_argument('--download', action='store_true', help='fetch missing GCAT files first')
    ap.add_argument('--out-dir', default='data/results/bigdata')
    ap.add_argument('--accessed', default=dt.date.today().isoformat())
    ap.add_argument('--compute-json', default=None, help='optional JSON with a compute block to embed')
    a = ap.parse_args()
    if a.download:
        download(a.raw)
    metas = {n: load(a.raw, n)[1] for n in FILES}
    upd = metas['launch.tsv']['updated'] or ''
    m = re.search(r'(\d{4}) (\w{3}) +(\d+)', upd)
    cutoff = dt.datetime(int(m.group(1)), MONTHS[m.group(2)], int(m.group(3)), 23, 59) if m else dt.datetime.now()
    # Varda spacecraft: who built each bus, and which reentry vehicles are still in orbit (first-phase status)
    varda_sats, varda_rv_orbit = [], []
    for n in ('satcat.tsv', 'satcat070k.tsv', 'satcat100k.tsv', 'auxcat.tsv'):
        for r in load(a.raw, n)[0]:
            if r.get('Owner') != 'VARDA' or not r.get('Type', '').startswith('P'):
                continue
            if 'Reentry' in r['Name']:
                if r['Status'] in ('AO', 'O'):
                    varda_rv_orbit.append(r['Name'].replace(' Reentry Vehicle', ''))
            else:
                varda_sats.append((r['Name'], r['Manufacturer'], r['Bus']))
    rl_built = sorted(nm for nm, mf, _ in varda_sats if mf.startswith('RLAB'))
    total_bytes = sum(v['bytes'] for v in metas.values())
    total_records = sum(v['records'] for v in metas.values())
    compute = dict(where='local Mac (stdlib Python); rerun on MIT Engaging for verification', partitions=[], job_ids=[],
                   cpu_hours=0.0, wall_minutes=0.0, peak_storage_gb=round(total_bytes / 1e9, 3))
    if a.compute_json and os.path.exists(a.compute_json):
        compute = json.load(open(a.compute_json))
    now = dt.datetime.now(dt.timezone.utc).isoformat(timespec='seconds')
    code = ['analysis/bigdata/logistics_gcat.py', 'cluster/bigdata/logistics-gcat.sbatch']
    reproduce = ['python3 -I analysis/bigdata/logistics_gcat.py --raw <raw-dir> --download --out-dir data/results/bigdata',
                 'sbatch cluster/bigdata/logistics-gcat.sbatch   # same script on MIT Engaging (mit_quicktest, 1 CPU)']
    os.makedirs(a.out_dir, exist_ok=True)

    # ---------------- Q1
    table, rs, integ, ss_all, st, n_pl_rows, n_mass = launch_scale(a.raw, metas, cutoff)
    T = {t['year']: t for t in table}
    lf = st['last_full_year']
    yrange = [y for y in range(2000, cutoff.year + 1)]
    part = f' ({cutoff.year} YTD = to {cutoff.date().isoformat()})'
    def yl(y):
        return f'{y} YTD' if y == cutoff.year else y
    charts = [
        dict(id='launches-per-year', kind='stacked', title='Orbital launch attempts per year',
             subtitle='SpaceX versus everyone else, 2000 to date' + part,
             x=dict(label='Year', unit='', scale='category'), y=dict(label='Orbital launch attempts', unit='', scale='linear'),
             series=[dict(name='SpaceX', color='orange', points=[[yl(y), T[y]['spacex_attempts']] for y in yrange]),
                     dict(name='Rest of world', color='grey', points=[[yl(y), T[y]['attempts'] - T[y]['spacex_attempts']] for y in yrange])],
             annotations=[dict(x=lf, y=T[lf]['attempts'], text=f"{lf}: {T[lf]['attempts']} attempts, {T[lf]['spacex_share_attempts']}% SpaceX")],
             caption='GCAT launch list, LaunchCode O* or D* (orbital and deep-space attempts, successes and failures). '
                     'Shows launch counts by launch provider (GCAT Agency = SPX), not who owns the payloads.'),
        dict(id='payloads-per-year', kind='stacked', title='Payloads placed in orbit per year',
             subtitle='Starlink, other SpaceX-launched payloads, and payloads launched by others' + part,
             x=dict(label='Year', unit='', scale='category'), y=dict(label='Payloads on successful orbital launches', unit='', scale='linear'),
             series=[dict(name='Starlink', color='orange', points=[[yl(y), T[y]['starlink_payloads']] for y in yrange]),
                     dict(name='Other payloads on SpaceX launches', color='cyan', points=[[yl(y), T[y]['spacex_payloads'] - T[y]['starlink_payloads']] for y in yrange]),
                     dict(name='Payloads on other launchers', color='grey', points=[[yl(y), T[y]['payloads'] - T[y]['spacex_payloads']] for y in yrange])],
             caption='GCAT derived launchlog (one row per payload). Counts payloads, not mass; most are small satellites. '
                     'Payloads lost on failed launches are excluded (they are listed in the stats).'),
        dict(id='mass-per-year', kind='line', title='Payload mass placed in orbit per year',
             subtitle=f'Sum of GCAT payload launch masses, 1957–{lf} (complete years only)',
             x=dict(label='Year', unit='', scale='linear'), y=dict(label='Payload mass', unit='tonnes', scale='linear'),
             series=[dict(name='All launchers', color='grey', points=[[t['year'], t['mass_t']] for t in table if 1957 <= t['year'] <= lf]),
                     dict(name='SpaceX-launched', color='orange', points=[[t['year'], t['spacex_mass_t']] for t in table if 2006 <= t['year'] <= lf])],
             caption=f"Sums the Mass column of every payload with a mass value ({T[lf]['mass_coverage_pct']}% of {lf} payloads have one). "
                     'Many masses are GCAT estimates (flagged ?), and secret payloads are often nominal. Upper stages are excluded.'),
        dict(id='rideshare', kind='bar', title='Payloads per SpaceX rideshare mission',
             subtitle='Transporter and Bandwagon missions, catalogued payloads per launch',
             x=dict(label='Mission', unit='', scale='category'), y=dict(label='Payloads catalogued', unit='', scale='linear'),
             series=[dict(name='Payloads', color='cyan', points=[[x['mission'], x['payloads'], x['date']] for x in rs])],
             caption='Counts GCAT payload entries sharing the mission\'s launch designation. Includes payloads released later by orbital transfer vehicles; '
                     'the newest missions may still be incompletely catalogued.'),
        dict(id='starship-flights', kind='stacked', title='Starship integrated flights',
             subtitle='Apogee of each integrated flight; GCAT codes flights 4 onward as orbital (target perigee > 0)',
             x=dict(label='Flight', unit='', scale='category'), y=dict(label='Apogee', unit='km', scale='linear'),
             series=[dict(name='Success (GCAT code ?S)', color='orange', points=[[s['flight'].replace('Starship ', ''), s['apogee_km'] if s['success'] else 0, s['date'] + ' ' + s['ship']] for s in integ]),
                     dict(name='Failure (GCAT code ?F)', color='grey', points=[[s['flight'].replace('Starship ', ''), 0 if s['success'] else s['apogee_km'], s['date'] + ' ' + s['ship']] for s in integ])],
             caption='All integrated Starship/Super Heavy flights in the GCAT launch list. Apogee only. GCAT notes some orbital codings are borderline. Payloads catalogued per flight (in stats) include the ship itself and Starlink mass simulators.'),
    ]
    ytd = {d['year']: d for d in st['year_to_date']}
    findings = [
        f"GCAT lists {st['orbital_launch_attempts_all_time']:,} orbital launch attempts from 1957 to {cutoff.date().isoformat()}; "
        f"{lf} had {T[lf]['attempts']}, {st['growth_attempts_2015_to_last_full']}x the {st['attempts_2015']} of 2015.",
        f"SpaceX flew {T[lf]['spacex_attempts']} of the {T[lf]['attempts']} orbital launch attempts in {lf} ({T[lf]['spacex_share_attempts']}%).",
        f"{T[lf]['payloads']:,} payloads reached orbit in {lf}; {T[lf]['spacex_share_payloads']}% rode SpaceX rockets and {T[lf]['starlink_payloads']:,} were Starlink.",
        f"Catalogued payload mass placed in orbit in {lf} sums to {T[lf]['mass_t']:,} t ({T[lf]['spacex_share_mass']}% on SpaceX launches), "
        f"{st['growth_mass_2015_to_last_full']}x the {st['mass_t_2015']} t of 2015; {T[lf]['mass_coverage_pct']}% of {lf} payloads have a mass in GCAT.",
        f"Through {cutoff.strftime('%b %d')}: {ytd[cutoff.year]['attempts']} orbital attempts in {cutoff.year} ({ytd[cutoff.year]['spx']} by SpaceX) vs "
        f"{ytd[cutoff.year - 1]['attempts']} ({ytd[cutoff.year - 1]['spx']} by SpaceX) in the same window of {cutoff.year - 1}: growth has paused this year in GCAT's count.",
        f"{st['rideshare_missions']} Transporter/Bandwagon rideshare missions carried {st['rideshare_payloads_total']:,} catalogued payloads "
        f"(median {st['rideshare_payloads_per_mission_median']} per mission, range {st['rideshare_payloads_per_mission_min']}–{st['rideshare_payloads_per_mission_max']}).",
        f"Starship has made {st['starship_integrated_flights']} integrated flights ({st['starship_integrated_successes']} coded successful by GCAT). "
        f"GCAT puts {st['starship_integrated_flights_coded_orbital']} of them (flight 4 onward, including two failures) in its orbital category (target perigee above zero within uncertainties); the successful ones have GCAT perigees of {min(x['perigee_km'] for x in integ if x['category'] == 'orbital' and x['success'] and x['perigee_km'] is not None):.0f} to {max(x['perigee_km'] for x in integ if x['category'] == 'orbital' and x['success'] and x['perigee_km'] is not None):.0f} km, i.e. at the edge of orbit.",
    ]
    ls = dict(
        id='launch-scale', tab='network',
        title='Launch scale and the SpaceX effect',
        question='How much launch capacity exists today, how fast is it growing, and how much of it is SpaceX?',
        headline=dict(value=str(T[lf]['spacex_share_attempts']), unit='%',
                      text=f"In {lf}, SpaceX flew {T[lf]['spacex_share_attempts']}% of the world's {T[lf]['attempts']} orbital launch attempts "
                           f"and carried {T[lf]['spacex_share_payloads']}% of the {T[lf]['payloads']:,} payloads that reached orbit."),
        evidence_level='our computation on public data',
        datasets=dataset_entries(metas, ['launch.tsv', 'launchlog.tsv', 'satcat.tsv', 'satcat070k.tsv', 'satcat100k.tsv',
                                         'satcat270k.tsv', 'satcat700M.tsv', 'auxcat.tsv', 'lprcat.tsv', 'tmpcat.tsv', 'csocat.tsv'], a.accessed),
        compute=compute,
        method=[
            'Download the GCAT launch list (launch.tsv), the derived per-payload orbital launch log (launchlog.tsv) and all object catalogs (satcat*, auxcat, lprcat, tmpcat, csocat).',
            'Orbital launch attempt = LaunchCode starting O (orbital) or D (deep space) with second letter S (success) or F (failure); OE (failed before ignition) and OA (aborted, no launch) are excluded.',
            'SpaceX = launch agency SPX in GCAT (who flew the rocket, not who owns the payload).',
            'Payloads per year = launchlog rows on successful orbital/deep-space launches; Starlink = name or payload name starting "Starlink".',
            'Mass to orbit = sum of the GCAT Mass column (payload launch mass, kg) joined by JCAT from the object catalogs; coverage = share of payloads with a positive mass. The GCAT OrbPay column (autogenerated, flagged by GCAT as "use with caution") is kept only as a cross-check in the table.',
            'Rideshare = launches whose flight or mission name matches Transporter-N or Bandwagon-N; payloads per mission = launchlog payload rows with that launch designation.',
            'Starship = every launch of LV_Type Starship*; integrated flights are those not coded A (atmospheric hop).',
        ],
        charts=charts,
        stats=dict(st, rideshare=rs, starship_flights=integ, yearly=[t for t in table if t['year'] >= 1990],
                   payload_rows_used=n_pl_rows, objects_with_mass_lookup=n_mass),
        findings=findings,
        limitations=[
            f"{cutoff.year} is partial (data to {cutoff.date().isoformat()}); year-to-date comparisons use the same calendar window.",
            'Launch counts follow GCAT definitions (McDowell); other trackers differ by a few launches a year on borderline cases (Starship, failures before orbit).',
            'Mass sums use payload launch masses, many of which are GCAT estimates (flagged ?), and classified payloads with nominal masses. They exclude upper stages, so they understate total mass to orbit. Coverage per year is reported.',
            'SpaceX share counts the launch provider. Payload owners differ: Starlink is SpaceX-owned, while rideshare payloads belong to hundreds of organisations.',
            'Recent rideshare missions may not be fully catalogued yet, so their payload counts are lower bounds.',
            'This is capacity *up*. A foundry also needs capacity *down*, which is far scarcer: see return-cadence.json.',
        ],
        future_big_data=[
            'Join Space-Track TLE histories (all payloads, ~10^8 element sets) to measure orbit-raising and lifetime by operator, to size free-flyer foundry orbits.',
            'Add per-launch price data (public FAA/press filings) to compute $/kg trends next to the mass series.',
            'Track Starship payload deployments once they are catalogued, to calibrate a heavy-lift foundry delivery scenario.',
        ],
        partners=[
            dict(name='SpaceX', why='Flies most of the world\'s launches and rideshare slots; Transporter/Bandwagon is the cheapest route to orbit for a first foundry cartridge.',
                 evidence=f"{T[lf]['spacex_share_attempts']}% of {lf} orbital attempts and {T[lf]['spacex_share_payloads']}% of {lf} payloads in GCAT; "
                          f"{st['rideshare_missions']} rideshare missions with {st['rideshare_payloads_total']:,} payloads."),
            dict(name='Rocket Lab', why='Second most frequent US launcher, and it built the spacecraft buses for Varda\'s W-series capsules.',
                 evidence='filled in below from the launch counts'),
            dict(name='Jonathan McDowell (GCAT)', why='Maintains the open catalog every number here comes from.',
                 evidence='All launch, payload and mass counts in this file are computed from GCAT TSVs (' + (metas['launch.tsv']['updated'] or '') + ').'),
        ],
        code=code, reproduce=reproduce, generated_at=now,
    )
    # top agencies in last full year (for partner evidence)
    launches = load(a.raw, 'launch.tsv')[0]
    agc = collections.Counter(r['Agency'] for r in launches if is_orbital_attempt(r['LaunchCode']) and r['Launch_Date'][:4] == str(lf))
    ls['stats']['top_agencies_last_full_year'] = agc.most_common(10)
    ls['partners'][1]['evidence'] = (f"GCAT launch agency RLABN flew {agc.get('RLABN', 0)} orbital attempts in {lf} "
                                     f"(rank {[k for k, _ in agc.most_common()].index('RLABN') + 1 if 'RLABN' in agc else 'n/a'} by launch agency); "
                                     f"GCAT lists Rocket Lab (RLABLB) as manufacturer of the Varda {', '.join(rl_built)} spacecraft; later W-series buses are Varda-built.")
    with open(os.path.join(a.out_dir, 'launch-scale.json'), 'w') as f:
        json.dump(ls, f, indent=1)

    # ---------------- Q2
    events, not_landed, downcargo, dc_rows, calib, era_prev, per_year, years, all_gaps, (ws, we, wyrs) = return_cadence(a.raw, cutoff)
    ua, dc_, lc = calib['us_accessible'], calib['dragon_cargo'], calib['all_leo_capsules']
    # histogram of gaps (days), 7-day bins, last bin open
    def hist(gaps, w=14, top=294):
        bins = []
        for lo in range(0, top, w):
            hi = lo + w
            n = sum(1 for g in gaps if lo <= g / 24 < hi) if hi < top else sum(1 for g in gaps if g / 24 >= lo)
            bins.append([lo, hi, n])
        return bins
    cls_order = ['dragon_cargo', 'dragon_crew', 'varda', 'spacex_starfall', 'starliner', 'soyuz', 'shenzhou',
                 'china_recoverable_sat', 'other_recoverable', 'military_spaceplane', 'starship_test', 'shuttle',
                 'military_film_capsule', 'deep_space_return']
    chart_groups = [('Dragon cargo (CRS)', 'orange', ['dragon_cargo']),
                    ('Crew Dragon', 'cyan', ['dragon_crew']),
                    ('Starliner, Varda, Starfall', 'violet', ['starliner', 'varda', 'spacex_starfall']),
                    ('Soyuz and Shenzhou', 'green', ['soyuz', 'shenzhou']),
                    ('Everything else (Shuttle to 2011, military, China recoverable sats, sample return, demos, Starship tests)', 'grey',
                     ['shuttle', 'military_spaceplane', 'military_film_capsule', 'china_recoverable_sat', 'other_recoverable',
                      'deep_space_return', 'starship_test'])]
    yl2 = lambda y: f'{y} YTD' if y == cutoff.year else y
    stacked = [dict(name=n, color=col, points=[[yl2(y), sum(per_year[c][y] for c in cs)] for y in years]) for n, col, cs in chart_groups]
    med_bar = [[lab, calib[g]['median_gap_hours'] / 24] for g, lab in
               [('dragon_cargo', 'Dragon cargo (CRS)'), ('varda', 'Varda W-series'), ('dragon_all', 'All Dragon'),
                ('us_accessible', 'US-accessible, any'), ('all_leo_capsules', 'All LEO capsules, world')]
               if calib[g].get('median_gap_hours')]
    model_bar = [['Fleet model: 24 h', 1.0], ['Fleet model: 12 h', 0.5]]
    dc_years = [y for y in range(2017, cutoff.year + 1)]   # GCAT down-cargo coverage is continuous from SpX-10 / Progress MS-05 (2017)
    charts2 = [
        dict(id='returns-per-year', kind='stacked', title='Recoverable vehicles landed on Earth per year',
             subtitle='Capsules, spaceplanes and test ships recorded as landed in GCAT, 2000 to date' + part,
             x=dict(label='Year', unit='', scale='category'), y=dict(label='Landings', unit='', scale='linear'),
             series=stacked,
             caption='One bar segment per landed vehicle (GCAT status L, primary Earth). Cargo carried inside a capsule is not counted separately. '
                     'Excludes suborbital flights and launch aborts.'),
        dict(id='gap-hist-us', kind='hist', title='Days between US-accessible return opportunities',
             subtitle=f'Dragon cargo, Crew Dragon, Starliner, Varda and Starfall landings, {ws.date().isoformat()} to {we.date().isoformat()}',
             x=dict(label='Gap to next landing', unit='days', scale='linear'), y=dict(label='Number of gaps', unit='', scale='linear'),
             series=[dict(name='US-accessible landings', color='orange', points=hist(all_gaps['us_accessible'])),
                     dict(name='Dragon cargo only', color='cyan', points=hist(all_gaps['dragon_cargo']))],
             caption='14-day bins; the last bin collects any longer gaps. A real return slot is weeks away, not hours. '
                     '"US-accessible" is our classification of vehicles a US commercial payload could plausibly ride.'),
        dict(id='median-gap-vs-model', kind='hbar', title='Median gap between returns versus the fleet model',
             subtitle=f'Real median gaps {ws.year}–{cutoff.year} compared with the synthetic return cadence in analysis/fleet.py',
             x=dict(label='Median gap between returns', unit='days', scale='log'), y=dict(label='', unit='', scale='category'),
             series=[dict(name='Real median gap (GCAT)', color='orange', points=[[k, round(v, 2)] for k, v in med_bar]),
                     dict(name='Synthetic fleet-model cadence', color='grey', points=model_bar)],
             caption='Log scale. The fleet model\'s 12 h and 24 h cadences are synthetic assumptions, not observations.'),
        dict(id='downcargo', kind='stacked', title='Station down cargo: returned versus burned',
             subtitle='GCAT "Down Cargo" objects by fate, tonnes per year, 2017 to date (years with continuous GCAT coverage)',
             x=dict(label='Year', unit='', scale='category'), y=dict(label='Down cargo mass', unit='tonnes', scale='linear'),
             series=[dict(name='Returned to Earth (landed inside a capsule)', color='orange',
                          points=[[yl2(y), round(downcargo[y]['returned_kg'] / 1000, 2)] for y in dc_years]),
                     dict(name='Burned on reentry (disposal on Progress, Cygnus, Tianzhou, HTV)', color='grey',
                          points=[[yl2(y), round(downcargo[y]['burned_kg'] / 1000, 2)] for y in dc_years])],
             caption='GCAT down-cargo masses are mostly nominal estimates (often round numbers, flagged ?). The point is the split, not the exact tonnes. '
                     'Before 2017 GCAT catalogues down cargo only for some missions, so earlier years are not shown.'),
    ]
    # integrity check: mission numbers of landed vehicles should be contiguous apart from known losses
    integrity = {}
    for label, rx in [('Dragon CRS', r'\bCRS-(\d+)'), ('Shenzhou', r'^Shenzhou (\d+)$'), ('Soyuz MS', r'^Soyuz MS-(\d+)$')]:
        nums = sorted({int(m.group(1)) for e in events for m in [re.search(rx, e['name'])] if m})
        if nums:
            missing = [n for n in range(nums[0], nums[-1] + 1) if n not in nums]
            integrity[label] = dict(landed=f'{nums[0]}..{nums[-1]}', n=len(nums), missing=missing)
    for label, rx in [('Down cargo SpX-n', r'^SpX-(\d+)$'), ('Down cargo Progress MS-n', r'^Progress MS-(\d+)$'),
                      ('Down cargo Tianzhou-n', r'^Tianzhou-(\d+)$'), ('Down cargo ISS NG-n', r'^ISS NG-(\d+)$')]:
        nums = sorted({int(m.group(1)) for d in dc_rows for m in [re.search(rx, d['vehicle'])] if m})
        if nums:
            integrity[label] = dict(catalogued=f'{nums[0]}..{nums[-1]}', n=len(nums),
                                    missing=[n for n in range(nums[0], nums[-1] + 1) if n not in nums])
    vehicle_rows = []
    for c in cls_order:
        n_all = sum(1 for e in events if e['cls'] == c and e['t'].year >= 2000)
        n_win = sum(1 for e in events if e['cls'] == c and ws <= e['t'] <= we)
        if n_all:
            last = max(e['t'] for e in events if e['cls'] == c)
            vehicle_rows.append(dict(cls=c, label=CLASS_INFO[c][0], landings_since_2000=n_all, landings_in_window=n_win,
                                     last_landing=last.date().isoformat(), commercial_downmass=CLASS_INFO[c][2], note=CLASS_INFO[c][3]))
    dragon_dc = [d for d in dc_rows if d['family'] == 'SpaceX Dragon' and d['fate'] == 'returned']
    dragon_dc_median = statistics.median([d['mass_kg'] for d in dragon_dc]) if dragon_dc else None
    n_starfall = sum(1 for e in events if e['cls'] == 'spacex_starfall')
    dc_window = [d for d in dc_rows if ws.year <= d['year'] <= cutoff.year]
    returned_t = sum(d['mass_kg'] for d in dc_window if d['fate'] == 'returned') / 1000
    burned_t = sum(d['mass_kg'] for d in dc_window if d['fate'] == 'burned') / 1000
    calibration = dict(
        description='Empirical gaps between real Earth landings, for analysis/fleet.py. Replace the synthetic cadence by sampling gaps_hours, or use median/percentiles.',
        window=dict(start=ws.date().isoformat(), end=we.date().isoformat(), years=round(wyrs, 2)),
        synthetic_assumption_hours=SYNTHETIC_CADENCE_HOURS,
        synthetic_model_note='analysis/fleet.py: 3 capsules, each with a return slot every cadence hours, offset by cadence/3, so the system has a slot every cadence/3 hours (8 h at 24 h).',
        classes={g: {k: v for k, v in s.items()} for g, s in calib.items()},
        previous_era_2012_2020={g: s for g, s in era_prev.items()},
        recommended=dict(
            baseline='us_accessible', conservative='dragon_cargo', optimistic='all_leo_capsules',
            note='us_accessible pools all US-accessible landings as if any could carry a foundry cartridge; real manifests are booked months ahead, so this is an upper bound on opportunity.'),
    )
    findings2 = [
        f"From {ws.date().isoformat()} to {we.date().isoformat()} GCAT records {lc['n_returns']} landings of LEO return capsules worldwide; "
        f"{ua['n_returns']} were US-accessible vehicles (Dragon, Starliner, Varda, Starfall).",
        f"The median gap between US-accessible return opportunities was {ua['median_gap_days']} days (90th percentile {ua['p90_gap_days']} days, longest {ua['max_gap_days']} days). "
        f"That is {ua['ratio_median_gap_to_24h']}x the fleet model's synthetic 24 h per-capsule cadence (its 3 staggered capsules give a slot every 8 h system-wide).",
        f"Of those {lc['n_returns']} landings, {calib['commercial_downmass_yes']['n_returns']} ({calib['commercial_downmass_yes']['returns_per_year']} per year) were vehicles whose job includes "
        f"commercial downmass (Dragon cargo, Varda); the rest were crew vehicles with limited downmass, new or demo capsules, or vehicles that are not a routine channel for US commercial payloads (Soyuz, Shenzhou, Chinese satellites).",
        f"Dragon cargo, the only routine pressurized downmass, landed {dc_['n_returns']} times ({dc_['returns_per_year']} per year), with a median gap of {dc_['median_gap_days']} days.",
        f"A product finished at a random moment would wait on average {ua['mean_wait_days_random_finish']} days for the next US-accessible landing "
        f"and {dc_['mean_wait_days_random_finish']} days for the next Dragon cargo landing; the fleet model assumes 12 h on average (half of 24 h).",
        f"Of GCAT down cargo catalogued since {ws.year}, about {returned_t:.1f} t came back to Earth inside capsules and {burned_t:.1f} t was burned on purpose with disposal vehicles.",
        f"Varda's W-series capsules landed {calib['varda']['n_returns']} times in the window; GCAT also lists a W-4 reentry vehicle as reentered without a recorded landing (status R).",
    ]
    rc = dict(
        id='return-cadence', tab='foundry',
        title='How often can anything come back from orbit?',
        question='How often do pressurised or recoverable capsules land on Earth, how long are the gaps, and how does that compare with the fleet model\'s 12–24 h return cadence?',
        headline=dict(value=f"{ua['median_gap_days']:.0f}", unit='days',
                      text=f"Since 2021 a US-accessible capsule (Dragon, Starliner, Varda or Starfall) has landed every {ua['median_gap_days']:.0f} days at the median. "
                           f"The fleet model assumes each of its 3 capsules can return every 12–24 hours."),
        evidence_level='our computation on public data',
        datasets=dataset_entries(metas, ['satcat.tsv', 'ecat.tsv', 'auxcat.tsv', 'lprcat.tsv', 'satcat070k.tsv', 'satcat100k.tsv',
                                         'satcat270k.tsv', 'satcat700M.tsv', 'tmpcat.tsv', 'csocat.tsv'], a.accessed),
        compute=compute,
        method=[
            'Load every phase record of every catalogued object (satcat*, auxcat, lprcat, tmpcat, csocat, plus the extra-phase file ecat).',
            'A return event = a payload-type object (Type P*) whose phase ends with status L (landed) on primary Earth; one event per object per day. Cargo inside capsules (Type C*) is counted separately, as down cargo.',
            'Classify each landed vehicle by GCAT bus and name (Dragon cargo vs crew by CRS naming; Soyuz, Shenzhou, Starliner, Varda RV, Starfall, X-37B/CSSHQ, sample-return capsules, Starship test ships, and so on).',
            '"US-accessible" (our classification) = Dragon cargo, Crew Dragon, Starliner, Varda and SpaceX Starfall: vehicles a US commercial payload could plausibly ride home.',
            f'Gaps = time between consecutive landings within a class, window {ws.date().isoformat()} to {we.date().isoformat()} (Dragon-2 era); 2012–2020 is kept for comparison.',
            'Mean wait for a product finished at a uniformly random time = sum(gap^2) / (2 sum(gap)) (the inspection paradox), compared with the fleet model\'s uniform wait of cadence/2.',
            'Down cargo = GCAT objects named "... Down Cargo". Final status AL* = landed inside a capsule (returned) and AR* = reentered with a disposal vehicle (burned).',
            'Integrity check: mission numbers of landed CRS Dragons, Shenzhous and Soyuz MS must be contiguous; the only gaps are expected losses (stats.integrity_checks).',
        ],
        charts=charts2,
        stats=dict(vehicles=vehicle_rows, integrity_checks=integrity,
                   window_summary={g: {k: v for k, v in s.items() if k != 'gaps_hours'} for g, s in calib.items()},
                   previous_era_2012_2020=era_prev,
                   commercial_capsule_reentries_not_recorded_as_landed=not_landed,
                   downcargo_by_year={y: dict(downcargo[y]) for y in sorted(downcargo) if y >= 2000},
                   dragon_downcargo_returned_objects=len(dragon_dc),
                   dragon_downcargo_returned_median_kg=dragon_dc_median,
                   downcargo_since_window_start_t=dict(returned=round(returned_t, 2), burned=round(burned_t, 2)),
                   events_in_window=[dict(date=e['t'].isoformat(timespec='minutes'), name=e['name'], cls=e['cls'], owner=e['owner'],
                                          file=e['file'], time_uncertain=e['uncertain'])
                                     for e in events if ws <= e['t'] <= we and e['cls'] in LEO_CAPSULE + ['starship_test']]),
        calibration=calibration,
        findings=findings2,
        limitations=[
            'Landing times come from GCAT phase records; some are flagged uncertain (?) and a few are day-precision only. That changes gaps by hours, not the weeks-scale conclusion.',
            '"US-accessible" and "commercial downmass" are our classifications from public vehicle roles, not manifests. A landing is an opportunity only if the payload was booked on that flight, often months ahead, so pooled gaps overstate real access.',
            'Crew Dragon, Soyuz and Starliner carry some downmass, but GCAT does not catalogue it separately for crew flights, so its mass is unknown here.',
            'GCAT down-cargo masses are mostly nominal (round, flagged ?) and should not be read as measured manifests.',
            'Varda and SpaceX Starfall are new; with a handful of flights, their cadence is not yet a stable rate.',
            f'Failed or unrecorded recoveries (for example the Varda W-4 reentry vehicle, status R; The Exploration Company\'s Mission Possible, status D) are listed in stats, not counted as returns.',
            'The window ends at the GCAT update date, so the last gap is right-censored (the next landing has not happened yet).',
            'An external cross-check against Wikipedia mission lists was attempted, but the Wikimedia API rate-limited our IP. Validation here is internal: contiguous mission numbering, CRS-7 (2015 launch failure) and Soyuz MS-10 (2018 abort) are the only gaps.',
        ],
        future_big_data=[
            'Join NASA ISS cargo manifests and ISS National Lab payload lists to turn landings into booked commercial downmass (kg per flight available to customers).',
            'Add Space-Track decay messages and TLE histories for free-flyer capsules, to model deorbit-window availability by orbit rather than by booked flight.',
            'Feed the empirical gaps_hours distribution into analysis/fleet.py and rerun the sweep on Engaging to see how on-time delivery collapses (or how much buffer storage is needed) at real cadence.',
        ],
        partners=[
            dict(name='SpaceX (Dragon, Starfall)', why='Dragon is the only routine pressurized downmass channel for US payloads, and Starfall is a new SpaceX recoverable capsule.',
                 evidence=f"{calib['dragon_all']['n_returns']} of {ua['n_returns']} US-accessible landings since 2021 were Dragons; "
                          f"GCAT records {len(dragon_dc)} returned 'SpX-n Down Cargo' objects (median {dragon_dc_median} kg, nominal) "
                          f"and {n_starfall} Starfall landings."),
            dict(name='Varda Space Industries', why='The only company routinely landing its own free-flying manufacturing capsules.',
                 evidence=f"{sum(1 for e in events if e['cls']=='varda')} W-series reentry vehicles recorded as landed in GCAT ("
                          + '; '.join(f"{e['name'].replace(' Reentry Vehicle', '')} {e['t'].date().isoformat()} at {e['dest'] if e['dest'] not in ('', '-') else 'unrecorded site'}" for e in events if e['cls'] == 'varda')
                          + f"); {', '.join(varda_rv_orbit) or 'none'} still in orbit at the data cutoff."),
            dict(name='NASA / ISS National Lab (CASIS)', why='Book commercial and research downmass on CRS Dragon flights.',
                 evidence='GCAT down-cargo objects for CRS missions are owned by JSC (NASA) and land inside Dragon (status AL IN).'),
            dict(name='Boeing (Starliner)', why='A second US crew vehicle; adds return slots if it flies operationally.',
                 evidence=f"{sum(1 for e in events if e['cls']=='starliner')} Starliner landings in GCAT, with 300 kg of down cargo recorded on the 2024 crewed test flight."),
        ],
        code=code, reproduce=reproduce, generated_at=now,
    )
    with open(os.path.join(a.out_dir, 'return-cadence.json'), 'w') as f:
        json.dump(rc, f, indent=1)
    print(json.dumps(dict(cutoff=cutoff.isoformat(), total_records=total_records, total_bytes=total_bytes,
                          launch_headline=ls['headline'], return_headline=rc['headline']), indent=1))


if __name__ == '__main__':
    sys.exit(main())
