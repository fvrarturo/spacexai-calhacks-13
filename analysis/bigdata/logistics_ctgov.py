#!/usr/bin/env python3
"""ClinicalTrials.gov full registry: subcutaneous vs intravenous antibody / biologic trials per start year.

Runs on MIT Engaging (cluster/bigdata/logistics-ctgov.sbatch). Standard library only.

Input : the bulk download ctg-studies.json.zip (one JSON document per study), streamed member by
        member with zipfile, never extracted to disk.
Also counted: antibody interventions co-formulated with a hyaluronidase or named by a subcutaneous
brand/code (Faspro, Hybreza, Qvantig, Qlex, Zunovo, Phesgo, Hycela, MK-3475A, Herceptin SC, MabThera SC),
a high-precision marker of IV-to-SC reformulation programmes.

Output: a compact JSON table (per start year, per definition), per-antibody first-SC/first-IV years,
        lead sponsors of SC antibody trials, and a deterministic sample of matched snippets used for
        the hand precision check.

Unit of analysis: one registered study (NCT ID). A study is counted once per year whatever its
number of arms or interventions.

Antibody intervention: an intervention whose name or other names contain an INN monoclonal-antibody
stem word (r"\b[a-z]{3,}mab\b"), the phrase "monoclonal antibod", or the token "mAb".
Biologic intervention: interventionType == BIOLOGICAL, or an antibody intervention.

Route text is gathered two ways:
  linked     : the antibody/biologic intervention's own name and other names; its own description
               (whole, if it names no other intervention; otherwise only windows around the antibody
               name); windows around the antibody name in descriptions of arms that include it (the
               whole arm description when the arm has only that intervention); and windows around the
               antibody name in the titles. A window runs 60 characters before to 160 after each
               mention and is cut at the nearest mention of another intervention, so that the route
               of a co-administered drug (IV chemotherapy, an SC vaccine) is not attributed to the
               antibody.
  trial-wide : every intervention and arm text plus the titles (crude sensitivity check: picks up
               routes of co-administered drugs such as IV chemotherapy).
Route definitions:
  strict : full words only (subcutaneous[ly] / sub-cutaneous ; intravenous[ly] / intra-venous).
  loose  : strict plus abbreviations in a dosing context (s.c., s.q., subQ, "SC"/"IV" after a dose
           unit or before injection/infusion/dose/administration/every/q2w..., "(SC)", "(IV)", i.v.),
           plus the word "infusion" for IV unless it is a subcutaneous infusion.
"""
import argparse
import hashlib
import json
import multiprocessing as mp
import re
import sys
import time
import zipfile
from collections import Counter, defaultdict

MAB_RE = re.compile(r"\b([a-z]{3,}mab)\b", re.I)
MAB_GENERIC_RE = re.compile(r"monoclonal\s+antibod|\bmAbs?\b")

SC_STRICT = re.compile(r"\bsub[\s-]?cutaneous(?:ly)?\b", re.I)
IV_STRICT = re.compile(r"\bintra[\s-]?venous(?:ly)?\b", re.I)

UNIT = r"(?<![A-Za-z])(?i:mg/kg|mg/m2|mg/m²|mg|mcg|µg|ug|ml|g|iu|units?|u)\b\.?"
FOLLOW = (r"(?i:injections?|inj\b|administration|administered|admin\b|doses?|dosing|formulation|route|every|"
          r"once|twice|q\d+w?|qw|qd|weekly|biweekly|monthly|daily|on\s+days?|at\s+weeks?|bolus|push|"
          r"infusions?|drip|over|use|delivery|given|loading|maintenance)")
# "SC"/"SQ"/"IV" are matched upper-case only and only in a dosing context; dotted forms and subQ anywhere.
PRE = r"(?i:given|administered|delivered|infused|injected|dosed|by|via)\s+(?:\w+\s+)?"
SC_ABBR = re.compile(
    rf"{UNIT}\s*(?:\w+\s+)?S[CQ]\b|{PRE}S[CQ]\b|\(S[CQ]\)|\bS[CQ]\b\s*(?:\)\s*)?(?:\w+\s+){{0,2}}{FOLLOW}\b"
    r"|(?i:\bs\.\s?[cq]\.)(?=\W|$)|(?i:\bsub-?q\b)")
IV_ABBR = re.compile(
    rf"{UNIT}\s*(?:\w+\s+)?IV\b|{PRE}IV\b|\(IV\)|\bIV\b\s*(?:\)\s*)?(?:\w+\s+){{0,2}}{FOLLOW}\b|(?i:\bi\.\s?v\.)(?=\W|$)")
INFUSION = re.compile(r"\binfus(?:ion|ions|ed)\b(?![\s-]*(?:related|reactions?|site))", re.I)
SC_INFUSION = re.compile(r"\b(?:sub[\s-]?cutaneous(?:ly)?|SC|s\.c\.|subq)\s+(?:\w+\s+){0,2}infus", re.I)
IV_ABBR_STAGE = re.compile(r"\b(?:stage|grade|phase|type|class|level|part|cohort|arm|factor|nyha|step|group|tier)\s*\(?\s*(?:I{1,3}[/-])?IV\b", re.I)

SENT_SPLIT = re.compile(r"(?<=[.;])\s+|\n+")
DEFS = ("linked_strict", "linked_loose", "trial_strict", "trial_loose")


def classify(text):
    """Return dict with booleans for strict/loose SC and IV, plus the first loose snippet for each."""
    out = {"sc_strict": False, "iv_strict": False, "sc_loose": False, "iv_loose": False,
           "sc_snip": None, "iv_snip": None, "sc_kind": None, "iv_kind": None}
    if not text:
        return out
    m = SC_STRICT.search(text)
    if m:
        out["sc_strict"] = out["sc_loose"] = True
        out["sc_snip"], out["sc_kind"] = snippet(text, m), "word"
    m = IV_STRICT.search(text)
    if m:
        out["iv_strict"] = out["iv_loose"] = True
        out["iv_snip"], out["iv_kind"] = snippet(text, m), "word"
    if not out["sc_loose"]:
        m = SC_ABBR.search(text)
        if m:
            out["sc_loose"] = True
            out["sc_snip"], out["sc_kind"] = snippet(text, m), "abbr"
    if not out["iv_loose"]:
        for m in IV_ABBR.finditer(text):
            # drop "stage IV"-type hits that slipped through the dosing context
            pre = text[max(0, m.start() - 12):m.end()]
            if IV_ABBR_STAGE.search(pre):
                continue
            out["iv_loose"] = True
            out["iv_snip"], out["iv_kind"] = snippet(text, m), "abbr"
            break
    if not out["iv_loose"]:
        for m in INFUSION.finditer(text):
            pre = text[max(0, m.start() - 40):m.end()]
            if SC_INFUSION.search(pre):
                continue
            out["iv_loose"] = True
            out["iv_snip"], out["iv_kind"] = snippet(text, m), "infusion"
            break
    return out


def snippet(text, m, w=90):
    a, b = max(0, m.start() - w), min(len(text), m.end() + w)
    return text[a:b].replace("\n", " ")


def start_year(ps):
    d = (ps.get("statusModule", {}).get("startDateStruct") or {}).get("date")
    if not d or len(d) < 4 or not d[:4].isdigit():
        return None
    return int(d[:4])


def mab_tokens(iv):
    names = [iv.get("name") or ""] + list(iv.get("otherNames") or [])
    toks = set()
    for n in names:
        toks.update(t.lower() for t in MAB_RE.findall(n))
    generic = any(MAB_GENERIC_RE.search(n) for n in names)
    return toks, generic


STOP = {"placebo", "drug", "drugs", "standard", "control", "treatment", "therapy", "best", "matching",
        "biological", "other", "procedure", "device", "dose", "doses", "high", "high-dose", "low", "active",
        "combination", "investigator", "physician", "intravenous", "subcutaneous", "injection", "infusion"}
WORD_RE = re.compile(r"[a-z][a-z0-9-]{3,}")


def other_keys(ivs, this, toks):
    """First significant word (and -mab words) of every *other* intervention, used to cut windows."""
    keys = set()
    for o in ivs:
        if o is this:
            continue
        nm = (o.get("name") or "").lower()
        ws = [w for w in WORD_RE.findall(nm) if w not in STOP]
        if ws:
            keys.add(ws[0])
        keys.update(t.lower() for t in MAB_RE.findall(nm))
    return {k for k in keys if k not in toks and not any(k in t or t in k for t in toks)}


def windows(text, keys, others, back=60, fwd=160):
    """Text windows around each mention of the antibody, cut at the nearest other intervention name."""
    tl = text.lower()
    out = []
    for k in keys:
        if not k:
            continue
        start_at = 0
        while True:
            p = tl.find(k, start_at)
            if p == -1:
                break
            a, b = max(0, p - back), min(len(tl), p + len(k) + fwd)
            for o in others:
                q = tl.find(o, p + len(k), b)
                if q != -1:
                    b = q
                r = tl.rfind(o, a, p)
                if r != -1:
                    a = max(a, r + len(o))
            out.append(text[a:b])
            start_at = p + len(k)
    return out


def linked_text(iv, arms, titles, toks, others=frozenset()):
    """Route-bearing text attributable to this intervention (see module docstring, 'linked')."""
    name = (iv.get("name") or "").strip()
    nl = name.lower()
    keys = set(toks)
    if not keys:
        ws = [w for w in WORD_RE.findall(nl) if w not in STOP]
        keys = {ws[0]} if ws else set()
    parts = [name, " ".join(iv.get("otherNames") or [])]
    desc = iv.get("description") or ""
    dl = desc.lower()
    if any(k in dl for k in keys):
        parts.extend(windows(desc, keys, others))
    elif not any(o in dl for o in others):
        parts.append(desc)  # own description that names no other intervention
    for arm in arms:
        inames = [x.split(":", 1)[-1].strip().lower() for x in (arm.get("interventionNames") or [])]
        if nl and nl in inames:
            ad = arm.get("description") or ""
            if len(inames) == 1:
                parts.append(ad)
            else:
                parts.extend(windows(ad, keys, others))
    for t in titles:
        parts.extend(windows(t, keys, others))
    return "\n".join(x for x in parts if x)


HYAL_RE = re.compile(r"hyaluronidase|rhuph20|\bph20\b|enhanze|faspro|hybreza|qvantig|qlex|zunovo|phesgo|hycela|"
                     r"\bmk-?3475a\b|herceptin\s+sc\b|mabthera\s+sc\b", re.I)


def sample_key(nct):
    return int(hashlib.sha1(nct.encode()).hexdigest()[:8], 16) / 0xFFFFFFFF


def empty_year():
    return {d: Counter() for d in DEFS}


def tally(counter, sc, iv):
    if sc and iv:
        counter["both"] += 1
    elif sc:
        counter["sc_only"] += 1
    elif iv:
        counter["iv_only"] += 1
    else:
        counter["none"] += 1
    counter["total"] += 1


def process(args):
    zpath, names = args
    res = {
        "n_members": 0, "n_parsed": 0, "n_errors": 0, "bytes": 0,
        "n_interventional": 0, "year_all_interventional": Counter(),
        "mab": defaultdict(empty_year), "bio": defaultdict(empty_year),
        "mab_any_status": defaultdict(Counter),
        "per_mab": defaultdict(lambda: {"sc_years": Counter(), "iv_years": Counter(), "sc_nct": [], "n": 0}),
        "sponsors_sc": Counter(), "sponsors_sc_class": Counter(), "sponsors_iv": Counter(),
        "samples": [], "phase_sc": Counter(), "phase_iv": Counter(),
        "hyal_year": Counter(), "hyal_sponsors": Counter(), "hyal_trials": [],
    }
    with zipfile.ZipFile(zpath) as z:
        for n in names:
            res["n_members"] += 1
            try:
                raw = z.read(n)
                res["bytes"] += len(raw)
                doc = json.loads(raw)
            except Exception:
                res["n_errors"] += 1
                continue
            studies = doc if isinstance(doc, list) else [doc]
            for st in studies:
                handle_study(st, res)
    # convert defaultdicts for pickling
    res["mab"] = {k: {d: dict(c) for d, c in v.items()} for k, v in res["mab"].items()}
    res["bio"] = {k: {d: dict(c) for d, c in v.items()} for k, v in res["bio"].items()}
    res["per_mab"] = {k: {"sc_years": dict(v["sc_years"]), "iv_years": dict(v["iv_years"]),
                          "sc_nct": v["sc_nct"], "n": v["n"]} for k, v in res["per_mab"].items()}
    res["mab_any_status"] = {k: dict(v) for k, v in res["mab_any_status"].items()}
    return res


def handle_study(st, res):
    ps = st.get("protocolSection") or {}
    res["n_parsed"] += 1
    ident = ps.get("identificationModule", {})
    nct = ident.get("nctId", "")
    stype = ps.get("designModule", {}).get("studyType")
    if stype != "INTERVENTIONAL":
        return
    res["n_interventional"] += 1
    yr = start_year(ps)
    res["year_all_interventional"][yr] += 1
    aim = ps.get("armsInterventionsModule", {}) or {}
    ivs = aim.get("interventions") or []
    arms = aim.get("armGroups") or []
    titles = [ident.get("briefTitle") or "", ident.get("officialTitle") or ""]
    status = ps.get("statusModule", {}).get("overallStatus")
    phases = tuple(ps.get("designModule", {}).get("phases") or ["NA"])
    sponsor = (ps.get("sponsorCollaboratorsModule", {}).get("leadSponsor") or {})

    mab_ivs, bio_ivs, all_toks = [], [], set()
    for iv in ivs:
        toks, generic = mab_tokens(iv)
        is_mab = bool(toks) or generic
        if is_mab:
            mab_ivs.append((iv, toks))
            all_toks |= toks
        if is_mab or iv.get("type") == "BIOLOGICAL":
            bio_ivs.append((iv, toks))
    if not bio_ivs:
        return

    trial_text = "\n".join(
        [" ".join([iv.get("name") or "", iv.get("description") or "", " ".join(iv.get("otherNames") or [])]) for iv in ivs]
        + [" ".join([a.get("label") or "", a.get("description") or ""]) for a in arms] + titles)
    tw = classify(trial_text)

    def linked_class(group):
        agg = {"sc_strict": False, "iv_strict": False, "sc_loose": False, "iv_loose": False,
               "sc_snip": None, "iv_snip": None, "sc_kind": None, "iv_kind": None}
        per = []
        for iv, toks in group:
            c = classify(linked_text(iv, arms, titles, toks, other_keys(ivs, iv, toks)))
            per.append((toks, c))
            for k in ("sc_strict", "iv_strict", "sc_loose", "iv_loose"):
                agg[k] = agg[k] or c[k]
            for k in ("sc", "iv"):
                if agg[k + "_snip"] is None and c[k + "_snip"]:
                    agg[k + "_snip"], agg[k + "_kind"] = c[k + "_snip"], c[k + "_kind"]
        return agg, per

    for label, group in (("mab", mab_ivs), ("bio", bio_ivs)):
        if not group:
            continue
        lk, per = linked_class(group)
        yrec = res[label][yr]
        tally(yrec["linked_strict"], lk["sc_strict"], lk["iv_strict"])
        tally(yrec["linked_loose"], lk["sc_loose"], lk["iv_loose"])
        tally(yrec["trial_strict"], tw["sc_strict"], tw["iv_strict"])
        tally(yrec["trial_loose"], tw["sc_loose"], tw["iv_loose"])
        if label == "mab":
            hy = [iv for iv, _ in group if HYAL_RE.search(" ".join([iv.get("name") or "", iv.get("description") or "",
                                                                     " ".join(iv.get("otherNames") or [])]))]
            if hy:
                res["hyal_year"][yr] += 1
                res["hyal_sponsors"][sponsor.get("name", "?")] += 1
                res["hyal_trials"].append([nct, yr, sponsor.get("name", "?"), sorted(all_toks)[:4],
                                           (hy[0].get("name") or "")[:120]])
            res["mab_any_status"][status]["total"] += 1
            if lk["sc_loose"]:
                res["mab_any_status"][status]["sc"] += 1
                res["sponsors_sc"][sponsor.get("name", "?")] += 1
                res["sponsors_sc_class"][sponsor.get("class", "?")] += 1
                for p in phases:
                    res["phase_sc"][p] += 1
            if lk["iv_loose"]:
                res["sponsors_iv"][sponsor.get("name", "?")] += 1
                for p in phases:
                    res["phase_iv"][p] += 1
            for toks, c in per:
                for t in toks:
                    pm = res["per_mab"][t]
                    pm["n"] += 1
                    if c["sc_loose"]:
                        pm["sc_years"][yr] += 1
                        if len(pm["sc_nct"]) < 40:
                            pm["sc_nct"].append([nct, yr, sponsor.get("name", "?"), c["sc_kind"]])
                    if c["iv_loose"]:
                        pm["iv_years"][yr] += 1
            u = sample_key(nct)
            if u < 0.02:  # ~2% deterministic sample of antibody trials for hand checking
                res["samples"].append({
                    "nct": nct, "year": yr, "mabs": sorted(all_toks),
                    "sc_loose": lk["sc_loose"], "sc_strict": lk["sc_strict"], "sc_kind": lk["sc_kind"], "sc_snip": lk["sc_snip"],
                    "iv_loose": lk["iv_loose"], "iv_strict": lk["iv_strict"], "iv_kind": lk["iv_kind"], "iv_snip": lk["iv_snip"],
                    "title": titles[0][:200]})


def merge(results):
    tot = {"n_members": 0, "n_parsed": 0, "n_errors": 0, "bytes": 0, "n_interventional": 0}
    year_all = Counter()
    mab = defaultdict(lambda: {d: Counter() for d in DEFS})
    bio = defaultdict(lambda: {d: Counter() for d in DEFS})
    status = defaultdict(Counter)
    per_mab = defaultdict(lambda: {"sc_years": Counter(), "iv_years": Counter(), "sc_nct": [], "n": 0})
    sp_sc, sp_sc_class, sp_iv, ph_sc, ph_iv = Counter(), Counter(), Counter(), Counter(), Counter()
    samples = []
    hy_year, hy_sp, hy_trials = Counter(), Counter(), []
    for r in results:
        hy_year.update(r["hyal_year"]); hy_sp.update(r["hyal_sponsors"]); hy_trials.extend(r["hyal_trials"])
        for k in tot:
            tot[k] += r[k]
        year_all.update(r["year_all_interventional"])
        for tgt, src in ((mab, r["mab"]), (bio, r["bio"])):
            for y, defs in src.items():
                for d, c in defs.items():
                    tgt[y][d].update(c)
        for s, c in r["mab_any_status"].items():
            status[s].update(c)
        for m, v in r["per_mab"].items():
            pm = per_mab[m]
            pm["sc_years"].update(v["sc_years"]); pm["iv_years"].update(v["iv_years"])
            pm["n"] += v["n"]; pm["sc_nct"].extend(v["sc_nct"])
        sp_sc.update(r["sponsors_sc"]); sp_sc_class.update(r["sponsors_sc_class"]); sp_iv.update(r["sponsors_iv"])
        ph_sc.update(r["phase_sc"]); ph_iv.update(r["phase_iv"])
        samples.extend(r["samples"])
    return (tot, year_all, mab, bio, status, per_mab, sp_sc, sp_sc_class, sp_iv, ph_sc, ph_iv, samples,
            hy_year, hy_sp, hy_trials)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--zip", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--samples", required=True)
    ap.add_argument("--workers", type=int, default=6)
    ap.add_argument("--limit", type=int, default=0, help="debug: only the first N members")
    a = ap.parse_args()
    t0 = time.time()
    with zipfile.ZipFile(a.zip) as z:
        infos = [i for i in z.infolist() if not i.is_dir()]
    names = [i.filename for i in infos]
    if a.limit:
        names = names[:a.limit]
    uncompressed = sum(i.file_size for i in infos)
    print(f"members={len(names)} uncompressed_bytes={uncompressed}", flush=True)
    nchunk = max(a.workers * 8, 1)
    chunks = [(a.zip, names[i::nchunk]) for i in range(nchunk)]
    with mp.Pool(a.workers) as pool:
        results = []
        for i, r in enumerate(pool.imap_unordered(process, chunks)):
            results.append(r)
            if (i + 1) % a.workers == 0:
                print(f"chunks {i+1}/{nchunk} elapsed {time.time()-t0:.0f}s", flush=True)
    (tot, year_all, mab, bio, status, per_mab, sp_sc, sp_sc_class, sp_iv, ph_sc, ph_iv, samples,
     hy_year, hy_sp, hy_trials) = merge(results)

    def ytable(src):
        out = {}
        for y in sorted(src, key=lambda v: (v is None, v or 0)):
            out[str(y)] = {d: dict(c) for d, c in src[y].items()}
        return out

    pm_out = {}
    for m, v in per_mab.items():
        scy = {y: c for y, c in v["sc_years"].items() if y is not None}
        ivy = {y: c for y, c in v["iv_years"].items() if y is not None}
        pm_out[m] = {"n_trials": v["n"], "n_sc": sum(v["sc_years"].values()), "n_iv": sum(v["iv_years"].values()),
                     "first_sc_year": min(scy) if scy else None, "first_iv_year": min(ivy) if ivy else None,
                     "sc_years": {str(k): c for k, c in sorted(scy.items())},
                     "iv_years": {str(k): c for k, c in sorted(ivy.items())},
                     "sc_nct_examples": sorted(v["sc_nct"], key=lambda r: (r[1] or 0, r[0]))[:40]}
    out = {
        "source_zip": a.zip, "uncompressed_bytes": uncompressed, "totals": tot,
        "interventional_by_start_year": {str(k): v for k, v in sorted(year_all.items(), key=lambda kv: (kv[0] is None, kv[0] or 0))},
        "mab_by_year": ytable(mab), "biologic_by_year": ytable(bio),
        "mab_by_status": {str(k): dict(v) for k, v in status.items()},
        "per_mab": pm_out,
        "top_sponsors_sc_mab": sp_sc.most_common(40), "sc_mab_sponsor_class": dict(sp_sc_class),
        "top_sponsors_iv_mab": sp_iv.most_common(40),
        "phase_sc_mab": dict(ph_sc), "phase_iv_mab": dict(ph_iv),
        "hyaluronidase_or_sc_brand_mab_by_year": {str(k): v for k, v in sorted(hy_year.items(), key=lambda kv: (kv[0] is None, kv[0] or 0))},
        "hyaluronidase_or_sc_brand_sponsors": hy_sp.most_common(30),
        "hyaluronidase_or_sc_brand_trials": sorted(hy_trials, key=lambda r: ((r[1] or 0), r[0])),
        "definitions": __doc__, "elapsed_s": round(time.time() - t0, 1), "workers": a.workers,
    }
    with open(a.out, "w") as f:
        json.dump(out, f, indent=1)
    samples.sort(key=lambda s: s["nct"])
    with open(a.samples, "w") as f:
        json.dump(samples, f, indent=1)
    print(json.dumps(tot), f"elapsed={time.time()-t0:.0f}s samples={len(samples)}", flush=True)


if __name__ == "__main__":
    sys.exit(main())
