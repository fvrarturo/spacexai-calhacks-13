"""Merge parsed shards and flag PDB entries whose crystals were grown in microgravity.

Usage:
    python -I analysis/bigdata/pdb_classify.py --parsed WORK/parsed --out WORK/analysis

Steps
  1. Merge entries_*.parquet / hits_*.parquet from the parse array.
  2. Build one text field from the crystal-growth categories (method, details, apparatus,
     crystal description) and one from context fields (titles, keywords, citation titles,
     refinement / diffraction details), and test both against space vocabulary.
  3. Apply automatic rules -> auto_label in {space, ground_control, simulated, none}
     plus platform (Shuttle / Mir / ISS / Other / Unknown) and programs/organisations.
  4. Write candidates.csv (every entry with any space vocabulary anywhere in its header),
     so a human can review them; manual verdicts live in pdb_review_labels.py.
"""
from __future__ import annotations

import argparse
import glob
import json
import re
from pathlib import Path

import pandas as pd

I = re.IGNORECASE

# --- vocabulary ---------------------------------------------------------------------------
P = {
    "microgravity": r"micro[\s-]?gravit|\bu[\s-]?g\s+environment|zero[\s-]?gravit|weightless",
    "shuttle": (r"space[\s-]?shuttle|\bshuttle\b(?![\s-]*(vector|plasmid|protein|domain|system|mechanism))"
                r"|\bSTS[\s-]?\d{1,3}\b|\bspacehab\b|\bspace[\s-]?lab\b|\bIML[\s-]?[12]\b|\bUSML[\s-]?[12]\b"
                r"|\bLMS\b|\bMSL[\s-]?1\b|\b(columbia|endeavou?r|atlantis|discovery)\s+(mission|flight|orbiter)"),
    "iss": (r"international[\s-]+space[\s-]+station|space[\s-]+station|\bISS\b|\bKIBO\b|\bJEM\b"
            r"|japanese\s+experiment\s+module|\bzvezda\b"),
    "mir": r"\bMIR\b(?![\s-]*\d)|\bmir[\s-]+(space|station|orbital)",
    "jaxa": r"\bJAXA\b|\bNASDA\b|japan\s+aerospace",
    "hardware": (r"\bAPCF\b|\bHDPCG\b|\bCPCG\b|\bPCAM\b|\bDCAM\b|\bPCDF\b|\bGCB\b|\bGCF\b|\bJCB\b|\bPCF\b"
                 r"|\bVDA\b|\bPCG\b|advanced\s+protein\s+crystalli[sz]ation\s+facility"
                 r"|granada\s+crystalli[sz]ation|protein\s+crystal\s+growth\s+(experiment|facility|program)"
                 r"|crystalli[sz]ation\s+(facility|apparatus)\s+for\s+microgravity|\bPIL[\s-]?BOX"),
    "orbit": (r"\bin[\s-]+space\b(?![\s_-]*group)|\bon[\s-]+orbit\b|\bin[\s-]+orbit\b|\borbit(al|er|ing)?\b|space[\s-]?grown"
              r"|grown\s+(in|on)\s+(the\s+)?space|space[\s-]?flight|spaceflight|\bflight\s+(crystal|sample|experiment)"
              r"|\bin\s+flight\b|\bflown\b"),
    "free_flyer": r"\bEURECA\b|\bFOTON\b|\bBION\b|\bTEXUS\b|\bMASER\b|\bsounding\s+rocket|\bfree[\s-]?flyer",
    "commercial": (r"\bCASIS\b|ISS\s+national\s+lab|\bSpaceX\b|\bspace\s?tango\b|\bredwire\b|\bCRS[\s-]?\d+"
                   r"|\bdragon\s+(capsule|spacecraft)|\bcygnus\b|\bprogress\s+(m|ms|spacecraft)\b|\bsoyuz\b"),
    "agency": (r"\bNASA\b|\bMSFC\b|marshall\s+space|european\s+space\s+agency|\bESA\b|\bCNES\b|\bDLR\b"
               r"|roscosmos|\benergia\b|russian\s+space|\bCSA\b|chinese\s+space|\bCMSA\b|\bshenzhou\b|\btiangong\b"),
}
RX = {k: re.compile(v, I) for k, v in P.items()}
SIM = re.compile(r"simulat\w*\s+(micro[\s-]?gravit|weightless)|magnetic(ally)?[\s-]+levitat|diamagnetic|clinostat"
                 r"|random\s+positioning|mimic\w*\s+(a\s+)?micro[\s-]?gravit|micro[\s-]?gravity[\s-]+(like|mimetic)"
                 r"|(gel|agarose)\s+to\s+(mimic|simulate)|high[\s-]+magnetic\s+field", I)
GROUND = re.compile(r"ground[\s-]+(based\s+)?control|ground[\s-]+(grown|crystal|experiment|reference)"
                    r"|earth[\s-]+(grown|control|based)|grown\s+on\s+(the\s+)?(earth|ground)"
                    r"|terrestrial(ly)?[\s-]+grown|\b1\s?-?g\s+control|on[\s-]+(the\s+)?ground\b|\bearth\b", I)
# programs / organisations mentioned in text (for the partner list)
ORGS = {
    "JAXA": r"\bJAXA\b|japan\s+aerospace", "NASDA": r"\bNASDA\b", "NASA": r"\bNASA\b",
    "NASA MSFC": r"\bMSFC\b|marshall\s+space", "ESA": r"european\s+space\s+agency|\bESA\b",
    "CNES": r"\bCNES\b", "DLR": r"\bDLR\b", "Roscosmos / RSC Energia": r"roscosmos|\benergia\b|russian\s+space",
    "CASIS / ISS National Lab": r"\bCASIS\b|ISS\s+national\s+lab", "SpaceX": r"\bSpaceX\b",
    "Space Tango": r"space\s?tango", "Redwire": r"\bredwire\b", "Merck": r"\bmerck\b",
    "UAB CBSE": r"\bUAB\b|alabama\s+at\s+birmingham|\bCBSE\b",
    "Hauptman-Woodward": r"hauptman|woodward", "Granada (LEC)": r"granada|\bLEC\b",
    "Kirin / Japanese industry": r"\bkirin\b", "CSA (China)": r"\bCMSA\b|chinese\s+space|shenzhou|tiangong",
}
ORGRX = {k: re.compile(v, I) for k, v in ORGS.items()}
PROGRAMS = {
    "JAXA PCG / Kibo": r"\bJAXA\b.*\bPCG\b|\bPCG\b.*\bJAXA\b|\bKIBO\b|high[\s-]quality\s+protein\s+crystal",
    "APCF (ESA)": r"\bAPCF\b|advanced\s+protein\s+crystalli[sz]ation\s+facility",
    "PCF": r"\bPCF\b|protein\s+crystalli[sz]ation\s+facility",
    "HDPCG": r"\bHDPCG\b|high[\s-]density\s+protein\s+crystal", "CPCG": r"\bCPCG\b|commercial\s+protein\s+crystal",
    "PCAM / DCAM": r"\bPCAM\b|\bDCAM\b", "VDA": r"\bVDA\b|vapou?r\s+diffusion\s+apparatus",
    "GCB / GCF (Granada)": r"\bGCB\b|\bGCF\b|granada\s+crystalli[sz]ation", "JCB": r"\bJCB\b",
    "PCDF (ESA)": r"\bPCDF\b", "IML / USML / LMS Spacelab": r"\bIML[\s-]?\d|\bUSML[\s-]?\d|\bLMS\b|spacelab|space\s+lab",
    "Spacehab": r"spacehab",
}
PROGRX = {k: re.compile(v, I) for k, v in PROGRAMS.items()}

GROW_COLS = ["grow_method", "grow_details", "grow_details2", "grow_apparatus", "grow_atmosphere",
             "crystal_description", "crystal_preparation"]
CTX_COLS = ["title", "keywords_text", "all_citation_titles", "refine_details", "diffrn_details"]


def textcat(row, cols):
    return " | ".join(str(row[c]) for c in cols if isinstance(row.get(c), str) and row.get(c))


def terms(text: str) -> list[str]:
    return [k for k, rx in RX.items() if rx.search(text)]


def platform(text: str, dep_year: float | None) -> str:
    t = text
    if RX["iss"].search(t) or re.search(r"\bKIBO\b|\bJEM\b", t, I):
        return "ISS"
    if RX["mir"].search(t):
        return "Mir"
    if RX["shuttle"].search(t) or re.search(r"\bAPCF\b|\bPCF\b|\bHDPCG\b|\bCPCG\b|\bVDA\b|\bPCAM\b|\bDCAM\b", t, I):
        return "Shuttle"
    if RX["free_flyer"].search(t) or RX["commercial"].search(t):
        return "Other"
    if RX["jaxa"].search(t) and dep_year and dep_year >= 2009:
        return "ISS"  # JAXA PCG flew on Kibo from 2009 onward; stated as inferred in the CSV
    return "Unknown"


def auto_label(grow: str, ctx: str) -> tuple[str, str]:
    """Automatic rule. Returns (label, reason)."""
    gt, ct = terms(grow), terms(ctx)
    strong = {"microgravity", "shuttle", "iss", "mir", "jaxa", "orbit", "free_flyer", "commercial"}
    if SIM.search(grow) or (SIM.search(ctx) and not gt):
        return "simulated", "simulated-microgravity vocabulary"
    g_strong = strong.intersection(gt)
    if g_strong:
        if GROUND.search(grow) and not re.search(r"grown\s+(in|on|aboard)|crystals?\s+(were\s+)?grown\s+.*(space|orbit|microgravity|shuttle|station)", grow, I):
            return "ground_control", "growth text mentions space but also ground/earth control"
        return "space", "growth fields: " + ",".join(sorted(g_strong))
    if "microgravity" in ct or ({"shuttle", "iss", "mir"} & set(ct) and "orbit" in ct):
        return "context_only", "space vocabulary only in titles/citations: " + ",".join(ct)
    return "none", ""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--parsed", required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    out = Path(a.out)
    out.mkdir(parents=True, exist_ok=True)

    ent = pd.concat([pd.read_parquet(f) for f in sorted(glob.glob(f"{a.parsed}/entries_*.parquet"))],
                    ignore_index=True)
    hits = pd.concat([pd.read_parquet(f) for f in sorted(glob.glob(f"{a.parsed}/hits_*.parquet"))],
                     ignore_index=True)
    stats = [json.load(open(f)) for f in sorted(glob.glob(f"{a.parsed}/stats_*.json"))]
    prov = {"files": sum(s["files"] for s in stats), "parsed": sum(s["parsed"] for s in stats),
            "errors": sum(s["errors"] for s in stats), "bytes_gz": sum(s["bytes_gz"] for s in stats),
            "bytes_unz": sum(s["bytes_unz"] for s in stats), "task_seconds": sum(s["seconds"] for s in stats),
            "error_samples": [e for s in stats for e in s["error_samples"]][:30]}
    ent.to_parquet(out / "entries.parquet", index=False)
    hits.to_parquet(out / "hits.parquet", index=False)

    # entries with any non-trivial hit anywhere in the header (raw scan) -> candidate pool
    weak_only = {"space", "flight", "nasa", "esa", "dlr", "cnes", "orbital", "energia"}
    hits["t"] = hits.term.str.lower().str.replace(r"[\s-]+", " ", regex=True)
    # known false-positive contexts, dropped before building the review pool
    win = hits.snippet.str.slice(130, 215)
    fp = (
        (hits.t.isin(["space", "in space"]) & win.str.contains(r"space[\s_-]*group", case=False, regex=True))
        | ((hits.t == "mir") & hits.category.str.match(r"refine|pdbx_phasing|phasing|pdbx_refine"))
        | hits.category.str.match(r"em_|pdbx_nmr|software|pdbx_struct_ref_seq_dif|struct_ref_seq_dif")
        | (hits.t.isin(["space", "in space", "mir", "iss", "jem", "lms", "pcg", "pcf", "vda", "gcb", "gcf", "jcb"])
           & hits.category.str.match(r"pdbx_database_related|struct_ref|entity|entity_name_com|struct_conn|pdbx_entity"))
    )
    # journal DOIs (10.1083/jcb..., 10.1084/jem...) are not hardware names
    fp |= hits.t.isin(["jcb", "jem"]) & hits.category.str.match(r"citation")
    hits["fp_context"] = fp
    # only categories that hold free text written by depositors or annotators can describe growth;
    # sequence schemes, chem_comp atoms, assemblies etc. produce token collisions (IML, MIR, ISS ligands)
    text_cat = hits.category.str.match(
        r"exptl|pdbx_exptl|struct$|struct_keywords|citation$|pdbx_database_related|diffrn|refine$|reflns$"
        r"|pdbx_entry_details|pdbx_database_remark|database_PDB_remark|struct_biol")
    hits["text_category"] = text_cat
    strong_hits = hits[~hits.t.isin(weak_only) & ~fp & text_cat]
    pool = set(strong_hits.entry_id)
    grow_hit_ids = set(hits[hits.category.isin(["exptl_crystal_grow", "exptl_crystal"])].entry_id)
    pool |= grow_hit_ids  # also review weak words when they sit inside crystal-growth text

    ent["grow_text"] = ent.apply(lambda r: textcat(r, GROW_COLS), axis=1)
    ent["ctx_text"] = ent.apply(lambda r: textcat(r, CTX_COLS), axis=1)
    ent["dep_year"] = pd.to_datetime(ent.deposit_date, errors="coerce").dt.year
    lab = ent.apply(lambda r: auto_label(r.grow_text, r.ctx_text), axis=1)
    ent["auto_label"] = [x[0] for x in lab]
    ent["auto_reason"] = [x[1] for x in lab]
    pool |= set(ent.loc[ent.auto_label != "none", "entry_id"])

    cand = ent[ent.entry_id.isin(pool)].copy()
    h_by = strong_hits.groupby("entry_id").apply(
        lambda g: " ## ".join(f"[{c}] {s}" for c, s in zip(g.category.head(4), g.snippet.head(4))),
        include_groups=False)
    cand["hit_categories"] = cand.entry_id.map(
        hits.groupby("entry_id").category.apply(lambda s: ",".join(sorted(set(s)))))
    cand["hit_terms"] = cand.entry_id.map(hits.groupby("entry_id").t.apply(lambda s: ",".join(sorted(set(s)))))
    cand["hit_snippets"] = cand.entry_id.map(h_by)
    alltxt = cand.grow_text + " | " + cand.ctx_text
    cand["platform_auto"] = [platform(t, y) for t, y in zip(alltxt, cand.dep_year)]
    cand["orgs"] = [",".join(k for k, rx in ORGRX.items() if rx.search(t)) for t in alltxt]
    cand["programs"] = [",".join(k for k, rx in PROGRX.items() if rx.search(t)) for t in alltxt]
    keep = ["entry_id", "methods", "deposit_date", "dep_year", "auto_label", "auto_reason", "platform_auto",
            "programs", "orgs", "res_refine", "res_reflns", "grow_text", "ctx_text", "hit_terms",
            "hit_categories", "hit_snippets", "cit_doi", "cit_pubmed", "authors", "polymer_entities"]
    cand[keep].sort_values(["auto_label", "entry_id"]).to_csv(out / "candidates.csv", index=False)

    # funding records naming space agencies (partner evidence only; funding is not growth location)
    fund = hits[hits.category.str.startswith("pdbx_audit_support")]
    fund_ids = {k: sorted(set(fund[fund.snippet.str.contains(v, case=False, regex=True)].entry_id))
                for k, v in {"NASA": r"NASA|Aeronautics and Space", "JAXA": r"JAXA|Aerospace Exploration",
                             "ESA": r"European Space Agency|\(ESA", "CASIS": r"CASIS|ISS National"}.items()}
    (out / "funding_space_agencies.json").write_text(json.dumps(fund_ids))
    summary = {"provenance": prov, "n_entries": int(len(ent)),
               "funding_entries": {k: len(v) for k, v in fund_ids.items()},
               "n_xray": int((ent.methods == "X-RAY DIFFRACTION").sum()),
               "n_candidates": int(len(cand)),
               "auto_label_counts": cand.auto_label.value_counts().to_dict(),
               "hit_term_counts": hits.t.value_counts().head(60).to_dict(),
               "hit_category_counts_strong": strong_hits.category.value_counts().head(30).to_dict()}
    (out / "classify_summary.json").write_text(json.dumps(summary, indent=1, default=str))
    print(json.dumps({k: v for k, v in summary.items() if k != "provenance"}, indent=1, default=str)[:4000])
    print(json.dumps({k: v for k, v in prov.items() if k != "error_samples"}))


if __name__ == "__main__":
    main()
