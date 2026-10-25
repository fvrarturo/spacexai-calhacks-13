"""Recall cross-check: compare our hand-checked space-grown list with RCSB full-text search.

Usage:
    python3 analysis/bigdata/pdb_rcsb_check.py --entries data/results/bigdata/pdb-microgravity-entries.csv \
        --labels-csv WORK/analysis/candidates.csv --out WORK/results/rcsb_fulltext_check.json

Runs RCSB Search API full-text queries for a few space terms, then reports how many of the RCSB hits
are in our space-grown set, how many we classified otherwise (and why), and how many of ours RCSB misses.
"""
from __future__ import annotations

import argparse
import csv
import json
import urllib.request

QUERIES = ["microgravity", "space shuttle", "international space station", "JAXA", "Kibo"]
# ("space-grown" was tried too, but RCSB tokenises it into 'space' + 'grown' and returns 182 mostly
#  'space group' entries, so it is not used.)

# Hand-read verdicts for RCSB hits that were outside our candidate pool (2026-10-24).
OUTSIDE_POOL_VERDICTS = {
    "2DEB": "title 'in space group C2221'", "2FYO": "title 'in space group P43212'",
    "3S3M": "citation author Jaxa-Chamiec", "3S3N": "citation author Jaxa-Chamiec", "3S3O": "citation author Jaxa-Chamiec",
    "4PJ1": "E. coli-Thermus shuttle vector", "5XP6": "E. coli-Pichia shuttle vector", "5XP9": "E. coli-Pichia shuttle vector",
    "5Y3B": "JAXA listed as funder; crystals grown by hanging drop", "5Y3C": "JAXA listed as funder",
}


def search(q: str) -> list[str]:
    body = {"query": {"type": "terminal", "service": "full_text", "parameters": {"value": q}},
            "return_type": "entry", "request_options": {"return_all_hits": True}}
    req = urllib.request.Request("https://search.rcsb.org/rcsbsearch/v2/query", data=json.dumps(body).encode(),
                                 headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            txt = r.read().decode()
    except Exception as exc:  # network errors are reported, not fatal
        return [f"ERROR:{exc!r}"]
    if not txt.strip():
        return []  # RCSB returns an empty body (HTTP 204) when nothing matches
    return [x["identifier"] for x in json.loads(txt).get("result_set", [])]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--entries", required=True)
    ap.add_argument("--labels-csv", default=None, help="candidates.csv with final labels (optional)")
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    ours = {r["entry_id"] for r in csv.DictReader(open(a.entries))}
    hits = {q: search(q) for q in QUERIES}
    union = sorted({i for v in hits.values() for i in v if not i.startswith("ERROR")})
    in_ours = sorted(set(union) & ours)
    not_ours = sorted(set(union) - ours)
    missed_by_rcsb = sorted(ours - set(union))
    out = {"queries": {q: len(v) for q, v in hits.items()}, "n_ids": len(union),
           "rcsb_ids_in_our_set": len(in_ours), "rcsb_ids_not_in_our_set": not_ours,
           "n_our_set": len(ours), "our_ids_not_found_by_rcsb_fulltext": len(missed_by_rcsb),
           "missed_by_rcsb_examples": missed_by_rcsb[:15],
           "note": "RCSB full-text search queried 2026-10-24 for: " + ", ".join(QUERIES)}
    lab = {}
    if a.labels_csv:
        lab = {r["entry_id"]: r.get("final_label") or r.get("auto_label") for r in csv.DictReader(open(a.labels_csv))}
    out["rcsb_not_ours_labels"] = {i: lab.get(i, "outside pool: " + OUTSIDE_POOL_VERDICTS.get(i, "NOT READ"))
                                   for i in not_ours}
    n_unread = sum(1 for v in out["rcsb_not_ours_labels"].values() if v.startswith("outside pool"))
    n_not_read = sum(1 for v in out["rcsb_not_ours_labels"].values() if v.endswith("NOT READ"))
    out["finding"] = (f"Cross-check: RCSB's own full-text search for {len(QUERIES)} space terms returns {len(union)} entries; "
                      f"{len(in_ours)} are in our list, {len(not_ours) - n_unread} others were in our reviewed candidate pool "
                      f"and judged not space-grown (Earth controls, unclear cases, other entries' mentions), and "
                      f"{n_unread} were outside our pool and, read by hand, are false hits ('space group', shuttle "
                      f"vectors, an author named Jaxa-Chamiec, JAXA as funder){' (' + str(n_not_read) + ' not yet read)' if n_not_read else ''}. "
                      f"Our archive scan finds {len(missed_by_rcsb)} of our "
                      f"{len(ours)} space-grown entries that this full-text search does not return.")
    json.dump(out, open(a.out, "w"), indent=1)
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
