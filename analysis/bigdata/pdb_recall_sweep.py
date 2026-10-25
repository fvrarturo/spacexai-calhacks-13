"""Near-miss recall sweep: a deliberately loose regex over the text fields of every parsed entry,
listing matches that are NOT already in the review pool (candidates.csv), for hand reading.

Usage: python -I analysis/bigdata/pdb_recall_sweep.py WORK/analysis
Run on 2026-10-24 (job 26816613): 172 loose hits, 74 outside the pool, all false (flight muscle,
time-of-flight neutron, ORBIT design software, synchrotron "station", gravitropism).
"""
import sys, re, pandas as pd
e = pd.read_parquet(sys.argv[1] + "/entries.parquet").astype(object)
c = set(pd.read_csv(sys.argv[1] + "/candidates.csv", dtype=str).entry_id)
cols = ["grow_method", "grow_details", "grow_details2", "grow_apparatus", "grow_atmosphere", "crystal_description",
        "crystal_preparation", "title", "keywords_text", "all_citation_titles", "diffrn_details", "refine_details"]
txt = e[cols].fillna("").agg(" | ".join, axis=1)
loose = re.compile(r"gr[a-z]?v[a-z]?ty|gravit|space(?![\s_-]*(group|groups|filling))\W+(grown|crystal|experiment|condition|environment|mission|flight|station|shuttle)"
                   r"|\bin\s+space\b(?![\s_-]*group)|\borbit\b|\bkibo\b|\bjaxa\b|\bnasda\b|\bsoyuz\b|\bspacex\b|\bdragon\b|\bstation\b|\bflight\b|\bflown\b|\bspace-grown\b|\bspacegrown\b|\bmicro-g\b|\bμg\b", re.I)
m = txt.map(lambda t: [x.group(0) for x in loose.finditer(t)][:3])
hit = e[m.map(len) > 0].copy()
hit["m"] = m[m.map(len) > 0]
new = hit[~hit.entry_id.isin(c)]
print("loose hits:", len(hit), "not already candidates:", len(new))
for _, r in new.iterrows():
    t = txt[r.name]
    i = loose.search(t).start()
    print(r.entry_id, str(r.deposit_date)[:4], str(r.methods)[:5], r.m, "::", " ".join(t[max(0, i - 120): i + 120].split()))
