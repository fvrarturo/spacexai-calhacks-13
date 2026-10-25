"""Summarise the complete PSI bucket listing (output of psi_inventory.py).

Counts and bytes per investigation, per run/activity/drive, per file type, with
exact-duplicate removal (same ETag + size) and archive (.zip) bytes split out,
plus data volume per experiment-day where timestamps allow:
  * DSI   : image-name tick stamps (23 ticks/s since 2009-01-01, derived from the
            PSI 'Solidification Plan' sheets; checked against the 3-min melt image period)
  * OASIS : calendar date range in each hard-drive folder name (HD01 ... HD13)
  * PK-4  : YYMMDD_HHMMSS stamps in on-board video/log file names

    python -I analysis/bigdata/psi_inventory_summary.py --tsv work/psi-objects.tsv.gz --out work/psi-inventory-summary.json
"""
import argparse
import collections
import gzip
import json
import re
from datetime import date, datetime, timedelta

TICKS_PER_S = 23.0
TICK_EPOCH = datetime(2009, 1, 1)
MONTHS = {m: i + 1 for i, m in enumerate(['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec'])}


def read(tsv):
    with gzip.open(tsv, 'rt') as f:
        for line in f:
            k, s, e, m = line.rstrip('\n').split('\t')
            yield k, int(s), e, m


def ftype(key):
    if key.endswith('/'):
        return 'folder marker'
    name = key.rsplit('/', 1)[-1]
    if name.lower().endswith('.md5') or '.md5' in name.lower():
        return 'md5 checksum'
    if '.' not in name:
        return '(no extension)'
    return name.rsplit('.', 1)[-1].lower()


def unit_of(key):
    """Run / activity / drive level unit inside each investigation."""
    p = key.split('/')
    inv = p[0]
    if inv == 'DSI':
        if len(p) >= 3 and p[1] == 'Data' and len(p) > 3:
            return inv, p[2]                       # e.g. 'S1 activity 1'
        if len(p) >= 3 and p[1] == 'Data' and p[2].endswith('.zip'):
            return inv, p[2][:-4] + ' (whole-activity zip)'
        return inv, 'documentation'
    if inv == 'OASIS':
        if len(p) > 3 and p[1] == 'Data':
            return inv, p[2]
        return inv, 'documentation'
    if inv == 'pk4':
        m = re.match(r'(C\d\d_R\d)_', p[2]) if len(p) > 3 else None
        if m:
            return inv, m.group(1)
        return inv, 'documentation'
    return 'bucket root', key


def oasis_days(folder):
    """'HD04 - SN003 Jul 31 to Aug 13 2015' -> (start, end) dates (inclusive)."""
    m = re.search(r'([A-Z][a-z]{2})[a-z]* (\d{1,2})(?: (\d{4}))? to ([A-Z][a-z]{2})[a-z]* (\d{1,2}) (\d{4})', folder)
    if not m:
        return None
    m1, d1, y1, m2, d2, y2 = m.groups()
    y2 = int(y2)
    y1 = int(y1) if y1 else y2
    a = date(y1, MONTHS[m1.lower()], int(d1))
    b = date(y2, MONTHS[m2.lower()], int(d2))
    return a, b


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--tsv', required=True)
    ap.add_argument('--out', required=True)
    a = ap.parse_args()

    inv = collections.defaultdict(lambda: dict(objects=0, bytes=0, zip_bytes=0, unique_objects=0, unique_bytes=0,
                                                unique_nonzip_bytes=0))
    units = collections.defaultdict(lambda: dict(objects=0, bytes=0, unique_bytes=0, unique_nonzip_bytes=0))
    types = collections.defaultdict(lambda: dict(objects=0, bytes=0))
    types_by_inv = collections.defaultdict(lambda: collections.defaultdict(lambda: [0, 0]))
    seen = set()
    dsi_ticks = collections.defaultdict(list)   # activity -> tick stamps of canonical image frames
    dsi_img_bytes = collections.defaultdict(int)
    dsi_cam = collections.defaultdict(collections.Counter)  # activity -> {HR1, HR2 mode 1, HR2 mode 2}
    dsi_day = collections.defaultdict(int)                   # calendar date (frame clock) -> raw BMP bytes
    pk4_day = collections.defaultdict(int)
    pk4_vid_day = collections.defaultdict(int)       # on-board VM camera video (VMx-AVI / VMx_AVI) per date
    pk4_vid_day_run = collections.defaultdict(int)   # (run, date) -> video bytes
    pk4_run_days = collections.defaultdict(set)
    pk4_dated = pk4_total = 0
    n = tot = 0
    for k, s, e, _ in read(a.tsv):
        n += 1
        tot += s
        i, u = unit_of(k)
        t = ftype(k)
        is_zip = t == 'zip'
        dup = (e, s) in seen
        seen.add((e, s))
        d = inv[i]
        d['objects'] += 1
        d['bytes'] += s
        d['zip_bytes'] += s if is_zip else 0
        uu = units[(i, u)]
        uu['objects'] += 1
        uu['bytes'] += s
        if not dup:
            d['unique_objects'] += 1
            d['unique_bytes'] += s
            uu['unique_bytes'] += s
            if not is_zip:
                d['unique_nonzip_bytes'] += s
                uu['unique_nonzip_bytes'] += s
        types[t]['objects'] += 1
        types[t]['bytes'] += s
        types_by_inv[i][t][0] += 1
        types_by_inv[i][t][1] += s
        if i == 'DSI' and t in ('bmp', 'jpg') and 'extracted by cbp' not in k:
            m = re.search(r'_(\d{9,10})_(\d)\.(bmp|jpg)$', k)
            if m:
                if t == 'bmp':
                    dsi_ticks[u].append(int(m.group(1)))
                    dsi_img_bytes[u] += s
                    dsi_day[(TICK_EPOCH + timedelta(seconds=int(m.group(1)) / TICKS_PER_S)).date().isoformat()] += s
                    cam = 'HR1' if '_HR1_' in k.rsplit('/', 1)[-1] else 'HR2'
                    dsi_cam[u][cam + ' mode ' + m.group(2)] += 1
        if i == 'pk4':
            pk4_total += s
            m = re.search(r'[-_](\d{6})[-_](\d{6})', k.rsplit('/', 1)[-1])
            if m:
                try:
                    dd = datetime.strptime(m.group(1), '%y%m%d').date()
                except ValueError:
                    dd = None
                if dd and 2014 <= dd.year <= 2023:
                    pk4_day[dd.isoformat()] += s
                    if re.match(r'VM\d[-_]AVI', k.rsplit('/', 1)[-1]) and 'Ground_DATA' not in k:
                        pk4_vid_day[dd.isoformat()] += s
                        pk4_vid_day_run[(u, dd.isoformat())] += s
                    pk4_run_days[u].add(dd.isoformat())
                    pk4_dated += s

    # DSI per activity: frames, span, GB/day
    dsi = []
    for u, ticks in sorted(dsi_ticks.items()):
        ticks.sort()
        t0 = TICK_EPOCH + timedelta(seconds=ticks[0] / TICKS_PER_S)
        t1 = TICK_EPOCH + timedelta(seconds=ticks[-1] / TICKS_PER_S)
        span_d = (ticks[-1] - ticks[0]) / TICKS_PER_S / 86400
        ub = units[('DSI', u)]['unique_nonzip_bytes']
        bb = dsi_img_bytes[u]
        dsi.append(dict(activity=u, bmp_frames=len(ticks), cameras=dict(sorted(dsi_cam[u].items())),
                        first=t0.isoformat(timespec='minutes'),
                        last=t1.isoformat(timespec='minutes'), span_days=round(span_d, 3),
                        raw_bmp_bytes=bb, unique_nonzip_bytes=ub,
                        gb_per_day=round(bb / 1e9 / span_d, 2) if span_d > 0 else None))
    # OASIS per drive: GB per calendar day of operations named in the folder
    oasis = []
    for (i, u), v in sorted(units.items()):
        if i != 'OASIS' or not u.startswith('HD'):
            continue
        r = oasis_days(u)
        if not r:
            continue
        days = (r[1] - r[0]).days + 1
        oasis.append(dict(drive=u, start=r[0].isoformat(), end=r[1].isoformat(), days=days,
                          unique_bytes=v['unique_bytes'], unique_nonzip_bytes=v['unique_nonzip_bytes'],
                          gb_per_day=round(v['unique_bytes'] / 1e9 / days, 1),
                          gb_per_day_nonzip_lower=round(v['unique_nonzip_bytes'] / 1e9 / days, 2)))
    pk4_runs = []
    for (i, u), v in sorted(units.items()):
        if i == 'pk4' and u.startswith('C'):
            nd = len(pk4_run_days[u])
            pk4_runs.append(dict(run=u, bytes=v['bytes'], unique_bytes=v['unique_bytes'],
                                 dated_days=nd, days=sorted(pk4_run_days[u]),
                                 gb_per_active_day=round(v['unique_bytes'] / 1e9 / nd, 1) if nd else None))
    out = dict(
        objects=n, bytes=tot,
        unique_objects=len(seen),
        investigations={k: v for k, v in sorted(inv.items())},
        units=[dict(investigation=i, unit=u, **v) for (i, u), v in sorted(units.items())],
        file_types=sorted(([t, v['objects'], v['bytes']] for t, v in types.items()), key=lambda x: -x[2]),
        file_types_by_investigation={i: sorted(([t, c, b] for t, (c, b) in d.items()), key=lambda x: -x[2])
                                     for i, d in types_by_inv.items()},
        dsi_activities=dsi, oasis_drives=oasis, pk4_runs=pk4_runs, dsi_bytes_per_day=sorted(dsi_day.items()),
        pk4_bytes_per_day=sorted(pk4_day.items()), pk4_video_bytes_per_day=sorted(pk4_vid_day.items()),
        pk4_video_bytes_per_run_day=sorted([r, d, b] for (r, d), b in pk4_vid_day_run.items()), pk4_dated_fraction=pk4_dated / pk4_total if pk4_total else None,
    )
    with open(a.out, 'w') as f:
        json.dump(out, f, indent=1)
    print(json.dumps({k: out[k] for k in ('objects', 'bytes', 'unique_objects')}))
    for i, v in sorted(inv.items()):
        print(i, v)


if __name__ == '__main__':
    main()
