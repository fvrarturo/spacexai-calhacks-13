"""Parse header metadata from the mirrored PDB mmCIF archive (one Slurm array task per shard group).

Usage (one array task):
    python -I analysis/bigdata/pdb_parse.py --mirror RAW/mmCIF --out WORK/parsed \
        --task $SLURM_ARRAY_TASK_ID --ntasks $SLURM_ARRAY_TASK_COUNT

For every *.cif.gz in the task's two-letter shard directories it:
  1. decompresses the file and cuts out the coordinate loops (_atom_site, _atom_site_anisotrop),
  2. parses the remaining header with gemmi,
  3. writes one row per entry (dates, methods, crystal-growth text, resolution, R-free, Wilson B,
     beamline, citation, polymer entities with UniProt refs and sequence hashes),
  4. scans the whole header text for space/microgravity vocabulary and records each hit with
     the category it sits in, so recall does not depend on depositors using one specific field.

Output: <out>/entries_<task>.parquet and <out>/hits_<task>.parquet, plus a small JSON with
bytes and record counts for provenance.
"""
from __future__ import annotations

import argparse
import gzip
import hashlib
import json
import os
import re
import sys
import time
from pathlib import Path

import gemmi
import pandas as pd

# Vocabulary scanned over the full header text (case-insensitive). Broad on purpose: the
# classifier in pdb_analyze.py decides what counts; here we only keep candidate snippets.
SCAN = re.compile(
    r"micro[\s-]?gravit|zero[\s-]?gravit|weightless|low[\s-]gravity|reduced[\s-]gravity"
    r"|space[\s-]?shuttle|\bshuttle\b|\bSTS[\s-]?\d{1,3}\b|spacehab|spacelab|space[\s-]?lab\b"
    r"|international[\s-]space[\s-]station|space[\s-]station|\bISS\b|\bKIBO\b|\bJEM\b|\bJAXA\b|\bNASDA\b"
    r"|\bMIR\b|\bAPCF\b|\bHDPCG\b|\bCPCG\b|\bPCAM\b|\bDCAM\b|\bPCDF\b|\bGCB\b|\bGCF\b|\bJCB\b|\bIML[\s-]?\d\b"
    r"|\bUSML[\s-]?\d\b|\bLMS\b|\bEURECA\b|\bFOTON\b|\bBION\b|\bTEXUS\b|\bMASER\b|\bCASIS\b|\bSpaceX\b"
    r"|\bNASA\b|\bMSFC\b|marshall space|european space|\bESA\b|\bCNES\b|\bDLR\b|roscosmos|energia"
    r"|in[\s-]space\b|on[\s-]orbit|in[\s-]orbit|\borbital\b|space[\s-]?grown|space[\s-]?flight|spaceflight"
    r"|\bflight\b|\bPCG\b|\bPCF\b|\bVDA\b|\bclinostat|magnetic[\s-]levitation|diamagnetic"
    r"|\bspace\b",
    re.IGNORECASE,
)

COORD_LOOPS = ("_atom_site.", "_atom_site_anisotrop.")

# Fast pre-filter: SCAN is only run on small windows around these word tokens (identical hits,
# ~30x faster than running the long alternation over every character of the header).
TRIGGERS = {
    "micro", "gravity", "weightless", "weightlessness", "shuttle", "sts", "spacehab", "spacelab", "space",
    "station", "iss", "kibo", "jem", "jaxa", "nasda", "mir", "apcf", "hdpcg", "cpcg", "pcam", "dcam", "pcdf",
    "gcb", "gcf", "jcb", "iml", "usml", "lms", "eureca", "foton", "bion", "texus", "maser", "casis", "spacex",
    "nasa", "msfc", "marshall", "esa", "cnes", "dlr", "roscosmos", "energia", "orbit", "orbital", "flight",
    "spaceflight", "pcg", "pcf", "vda", "clinostat", "magnetic", "diamagnetic", "international", "european",
    "zero", "low", "reduced", "in", "on", "levitation",
}
TOKEN = re.compile(r"[A-Za-z]+")


def scan_hits(head: str):
    """Yield SCAN matches, evaluating the regex only near trigger tokens."""
    seen = set()
    for t in TOKEN.finditer(head):
        w = t.group(0).lower()
        if w not in TRIGGERS and not w.startswith(("microgravit", "gravit", "spaceflight", "orbit")):
            continue
        if w in ("in", "on", "low", "zero", "reduced", "international", "european", "magnetic", "micro"):
            continue  # these only start phrases whose second word is itself a trigger
        lo, hi = max(0, t.start() - 30), min(len(head), t.end() + 40)
        for m in SCAN.finditer(head, lo, hi):
            if m.start() not in seen and m.start() <= t.end() and m.end() >= t.start():
                seen.add(m.start())
                yield m


def strip_coordinates(text: str) -> str:
    """Remove the big coordinate loops so gemmi parses only the header categories."""
    for tag in COORD_LOOPS:
        i = text.find("\n" + tag)
        if i < 0:
            continue
        start = text.rfind("\nloop_", 0, i + 1)
        if start < 0 or i - start > 20:
            start = i
        end = text.find("\n#", i + 1)
        if end < 0:
            end = len(text)
        text = text[:start] + "\n" + text[end:]
    return text


def table(block, cat: str, cols: list[str]) -> list[dict]:
    """Return a category as a list of row dicts (works for loops and key-value pairs)."""
    t = block.find_mmcif_category(cat)
    if not t:
        return []
    idx = {tg[len(cat):].lower(): i for i, tg in enumerate(t.tags)}
    want = [(c, idx[c.lower()]) for c in cols if c.lower() in idx]
    out = []
    for row in t:
        d = {}
        for c, j in want:
            v = row[j]
            if v not in ("?", "."):
                d[c] = gemmi.cif.as_string(v)
        out.append(d)
    return out


def first(block, tag: str):
    v = block.find_value(tag)
    if v is None or v in ("?", "."):
        return None
    return gemmi.cif.as_string(v)


def fnum(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return None


def join(rows: list[dict], key: str, sep: str = " || ") -> str | None:
    vals = [r[key] for r in rows if key in r]
    return sep.join(vals) if vals else None


def category_of_hit(text: str, pos: int) -> str:
    """Name of the mmCIF category a scan hit sits in (last tag line before the hit)."""
    j = pos
    while True:
        j = text.rfind("\n_", 0, j)
        if j < 0:
            return "?"
        line_end = text.find("\n", j + 1)
        tag = text[j + 1:line_end].split()[0]
        return tag.split(".")[0].lstrip("_")


def parse_entry(path: Path):
    raw = path.read_bytes()
    text = gzip.decompress(raw).decode("utf-8", errors="replace")
    nbytes_unz = len(text)
    head = strip_coordinates(text)
    doc = gemmi.cif.read_string(head)
    b = doc.sole_block()
    eid = b.name.upper()

    methods = [r.get("method") for r in table(b, "_exptl.", ["method"]) if r.get("method")]
    grow = table(b, "_exptl_crystal_grow.",
                 ["crystal_id", "method", "pdbx_details", "details", "apparatus", "atmosphere", "temp", "pH",
                  "pdbx_pH_range", "time", "seeding"])
    xtal = table(b, "_exptl_crystal.", ["id", "description", "preparation", "density_percent_sol"])
    refine = table(b, "_refine.", ["pdbx_refine_id", "ls_d_res_high", "ls_R_factor_R_free", "ls_R_factor_R_work",
                                   "B_iso_mean", "details"])
    reflns = table(b, "_reflns.", ["d_resolution_high", "B_iso_Wilson_estimate", "pdbx_Rmerge_I_obs",
                                   "pdbx_netI_over_sigmaI", "percent_possible_obs", "pdbx_redundancy"])
    src = table(b, "_diffrn_source.", ["source", "type", "pdbx_synchrotron_site", "pdbx_synchrotron_beamline"])
    diffrn = table(b, "_diffrn.", ["ambient_temp", "details", "crystal_id"])
    det = table(b, "_diffrn_detector.", ["detector", "type", "pdbx_collection_date"])
    cits = table(b, "_citation.", ["id", "title", "journal_abbrev", "year", "pdbx_database_id_DOI",
                                   "pdbx_database_id_PubMed"])
    prim = next((c for c in cits if c.get("id") == "primary"), cits[0] if cits else {})
    authors = [r.get("name") for r in table(b, "_audit_author.", ["name"]) if r.get("name")]
    revs = table(b, "_pdbx_audit_revision_history.", ["ordinal", "revision_date"])
    rel = min((r["revision_date"] for r in revs if "revision_date" in r), default=None)

    ents = table(b, "_entity.", ["id", "type", "pdbx_description", "pdbx_number_of_molecules"])
    polys = {r.get("entity_id"): r for r in table(b, "_entity_poly.", ["entity_id", "type",
                                                                         "pdbx_seq_one_letter_code_can"])}
    refs = table(b, "_struct_ref.", ["entity_id", "db_name", "pdbx_db_accession"])
    orgs = {}
    for cat in ("_entity_src_gen.", "_entity_src_nat.", "_pdbx_entity_src_syn."):
        col = "pdbx_gene_src_scientific_name" if cat == "_entity_src_gen." else (
            "pdbx_organism_scientific" if cat == "_entity_src_nat." else "organism_scientific")
        for r in table(b, cat, ["entity_id", col]):
            if r.get(col):
                orgs.setdefault(r.get("entity_id"), r[col])
    poly_ents = []
    for e in ents:
        if e.get("type") != "polymer":
            continue
        p = polys.get(e.get("id"), {})
        seq = re.sub(r"\s+", "", p.get("pdbx_seq_one_letter_code_can", ""))
        unp = sorted({r["pdbx_db_accession"] for r in refs
                      if r.get("entity_id") == e.get("id") and r.get("db_name") in ("UNP", "UniProt")
                      and r.get("pdbx_db_accession")})
        poly_ents.append({
            "entity_id": e.get("id"),
            "poly_type": p.get("type"),
            "description": e.get("pdbx_description"),
            "n_copies": e.get("pdbx_number_of_molecules"),
            "seq_len": len(seq),
            "seq_md5": hashlib.md5(seq.encode()).hexdigest() if seq else None,
            "unp": unp,
            "organism": orgs.get(e.get("id")),
        })

    xr = [r for r in refine if "X-RAY" in r.get("pdbx_refine_id", "X-RAY DIFFRACTION")]
    rf = xr[0] if xr else (refine[0] if refine else {})
    rl = reflns[0] if reflns else {}

    row = {
        "entry_id": eid,
        "methods": " | ".join(methods) if methods else None,
        "n_methods": len(methods),
        "deposit_date": first(b, "_pdbx_database_status.recvd_initial_deposition_date"),
        "release_date": rel,
        "title": first(b, "_struct.title"),
        "keywords": first(b, "_struct_keywords.pdbx_keywords"),
        "keywords_text": first(b, "_struct_keywords.text"),
        "grow_method": join(grow, "method"),
        "grow_details": join(grow, "pdbx_details"),
        "grow_details2": join(grow, "details"),
        "grow_apparatus": join(grow, "apparatus"),
        "grow_atmosphere": join(grow, "atmosphere"),
        "grow_temp": join(grow, "temp"),
        "grow_pH": join(grow, "pH"),
        "n_grow_rows": len(grow),
        "crystal_description": join(xtal, "description"),
        "crystal_preparation": join(xtal, "preparation"),
        "solvent_pct": fnum(xtal[0].get("density_percent_sol")) if xtal else None,
        "res_refine": fnum(rf.get("ls_d_res_high")),
        "r_free": fnum(rf.get("ls_R_factor_R_free")),
        "r_work": fnum(rf.get("ls_R_factor_R_work")),
        "b_mean": fnum(rf.get("B_iso_mean")),
        "refine_details": rf.get("details"),
        "res_reflns": fnum(rl.get("d_resolution_high")),
        "wilson_b": fnum(rl.get("B_iso_Wilson_estimate")),
        "rmerge": fnum(rl.get("pdbx_Rmerge_I_obs")),
        "i_over_sigma": fnum(rl.get("pdbx_netI_over_sigmaI")),
        "completeness": fnum(rl.get("percent_possible_obs")),
        "diffrn_temp": join(diffrn, "ambient_temp"),
        "diffrn_details": join(diffrn, "details"),
        "source": join(src, "source"),
        "source_type": join(src, "type"),
        "synchrotron_site": join(src, "pdbx_synchrotron_site"),
        "beamline": join(src, "pdbx_synchrotron_beamline"),
        "detector": join(det, "detector"),
        "collection_date": join(det, "pdbx_collection_date"),
        "cit_title": prim.get("title"),
        "cit_journal": prim.get("journal_abbrev"),
        "cit_year": prim.get("year"),
        "cit_doi": prim.get("pdbx_database_id_DOI"),
        "cit_pubmed": prim.get("pdbx_database_id_PubMed"),
        "all_citation_titles": " || ".join(c["title"] for c in cits if c.get("title")) or None,
        "authors": "; ".join(authors[:8]) if authors else None,
        "n_authors": len(authors),
        "n_polymer_entities": len(poly_ents),
        "polymer_entities": json.dumps(poly_ents),
        "bytes_gz": len(raw),
        "bytes_unz": nbytes_unz,
    }

    hits = []
    for m in scan_hits(head):
        s = m.start()
        word = m.group(0)
        if word.lower() == "space":
            ctx = head[max(0, s - 15): s + 25].lower()
            # drop the overwhelmingly common crystallographic and lab uses up front
            if re.search(r"space[\s_-]*group|head[\s-]?space|space[\s-]?filling|real[\s-]space|reciprocal[\s-]space"
                         r"|k[\s-]?space|q[\s-]?space|vapou?r space|air space|dead space|free space|"
                         r"space[\s_-]*(between|around)|_space|space_", ctx):
                continue
        hits.append({
            "entry_id": eid,
            "term": word,
            "category": category_of_hit(head, s),
            "snippet": head[max(0, s - 160): s + 160].replace("\n", " "),
        })
    return row, hits


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--mirror", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--task", type=int, default=0)
    ap.add_argument("--ntasks", type=int, default=1)
    ap.add_argument("--limit", type=int, default=0, help="debug: stop after N files")
    ap.add_argument("--shards-file", default=None, help="ordered shard list (from the mirror job)")
    ap.add_argument("--first", type=int, default=0, help="use shards[first:last] of the list")
    ap.add_argument("--last", type=int, default=10**6)
    ap.add_argument("--tag", default="", help="output file tag, keeps batches apart")
    ap.add_argument("--skip-parsed", action="store_true",
                    help="fix-up pass: skip entries already present in <out>/entries_*.parquet")
    a = ap.parse_args()
    done = set()
    if a.skip_parsed:
        for f in Path(a.out).glob("entries_*.parquet"):
            done |= set(pd.read_parquet(f, columns=["entry_id"]).entry_id.str.lower())

    mirror = Path(a.mirror)
    if a.shards_file:
        shards = [x.strip() for x in open(a.shards_file) if x.strip()]
    else:
        shards = sorted(p.name for p in mirror.iterdir() if p.is_dir())
    shards = shards[a.first:a.last]
    mine = shards[a.task::a.ntasks]
    out = Path(a.out)
    out.mkdir(parents=True, exist_ok=True)

    rows, hits, errors = [], [], []
    t0 = time.time()
    nfiles = nbytes = nunz = 0
    for sh in mine:
        for f in sorted((mirror / sh).glob("*.cif.gz")):
            if done and f.name.split(".")[0].lower() in done:
                continue
            try:
                row, h = parse_entry(f)
                rows.append(row)
                hits.extend(h)
                nbytes += row["bytes_gz"]
                nunz += row["bytes_unz"]
            except Exception as exc:  # keep going; failures are reported
                errors.append({"file": str(f.name), "error": repr(exc)[:300]})
            nfiles += 1
            if a.limit and nfiles >= a.limit:
                break
        if a.limit and nfiles >= a.limit:
            break

    pd.DataFrame(rows).to_parquet(out / f"entries_{a.tag}{a.task:03d}.parquet", index=False)
    pd.DataFrame(hits, columns=["entry_id", "term", "category", "snippet"]).to_parquet(
        out / f"hits_{a.tag}{a.task:03d}.parquet", index=False)
    stats = {"task": f"{a.tag}{a.task}", "shards": len(mine), "files": nfiles, "parsed": len(rows), "errors": len(errors),
             "bytes_gz": nbytes, "bytes_unz": nunz, "seconds": round(time.time() - t0, 1),
             "error_samples": errors[:20]}
    (out / f"stats_{a.tag}{a.task:03d}.json").write_text(json.dumps(stats, indent=1))
    print(json.dumps({k: v for k, v in stats.items() if k != "error_samples"}))


if __name__ == "__main__":
    sys.exit(main())
