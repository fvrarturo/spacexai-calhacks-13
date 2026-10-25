#!/usr/bin/env python3
"""Demand signals for orbit-made materials (logistics workstream, Network tab).

Builds data/results/bigdata/demand-signals.json from real public files:
  1. ClinicalTrials.gov full registry (608k studies), parsed on MIT Engaging by
     analysis/bigdata/logistics_ctgov.py -> ctgov-routes.json (+ route samples).
  2. FDA Purple Book monthly data download (every licensed biologic, with route and approval date).
  3. openFDA Drugs@FDA bulk file (cross-check of antibody BLA approval dates).
  4. USGS lithium: Data Series 140 historical statistics (to 2021) + Mineral Commodity Summaries
     2022/2023/2024 lithium world tables + MCS 2026 commodities table (2024-2025).

Standard library only. Downloads go into --raw (one sub-folder per source); nothing is written to the repo
except --out.

    python3 -I analysis/bigdata/logistics_demand.py --raw <raw dir> \
        --ctgov <work>/ctgov-routes.json --samples <work>/ctgov-route-samples.json \
        --sacct <work>/sacct.txt --out data/results/bigdata/demand-signals.json
"""
import argparse
import csv
import datetime as dt
import hashlib
import io
import json
import math
import os
import re
import sys
import urllib.request
import xml.etree.ElementTree as ET
import zipfile
from collections import Counter, defaultdict

UA = "Mozilla/5.0 (compatible; orbital-foundry-research/1.0)"
ACCESSED = "2026-10-24"
SOURCES = {
    "purplebook": ("purplebook", "purplebook-search-September-data-download.csv",
                   "https://www.accessdata.fda.gov/drugsatfda_docs/PurpleBook/2026/purplebook-search-September-data-download.csv"),
    "drugsfda": ("openfda", "drug-drugsfda-0001-of-0001.json.zip",
                 "https://download.open.fda.gov/drug/drugsfda/drug-drugsfda-0001-of-0001.json.zip"),
    "ds140": ("usgs", "ds140-lithium-2021.xlsx",
              "https://d9-wret.s3.us-west-2.amazonaws.com/assets/palladium/production/s3fs-public/media/files/ds140-lithium-2021.xlsx"),
    "mcs2022": ("usgs", "mcs2022-lithi_world.csv",
                "https://www.sciencebase.gov/catalog/file/get/61ead34ad34e8b818ad9f3d3?f=__disk__29%2F43%2Ffe%2F2943fe1b4a84d571b20f9812aeefaf301bb1030b"),
    "mcs2023": ("usgs", "mcs2023-lithi_world.csv",
                "https://www.sciencebase.gov/catalog/file/get/63d1a467d34e06fef150071d?f=__disk__05%2F9e%2F04%2F059e04e0c5fbf232f947e9a06da1f5ef770ba73a"),
    "mcs2024": ("usgs", "mcs2024-lithi_world.csv",
                "https://www.sciencebase.gov/catalog/file/get/65b7d7ffd34e36a39045b4e8?f=__disk__17%2Fd7%2F94%2F17d7941de79f0eb78f7ff5516394886dc17934b0"),
    "mcs2026": ("usgs", "MCS2026_Commodities_Data.csv",
                "https://www.sciencebase.gov/catalog/file/get/696a75d5d4be0228872d3bf8?f=__disk__eb%2F4d%2Fd1%2Feb4dd129d4f08cfba010a8b11cbbd2d88bbefdcb"),
}

MAB_RE = re.compile(r"\b([a-z]{3,}mab)(?:-[a-z]{4})?\b", re.I)
# Immune-checkpoint antibodies (PD-1, PD-L1, CTLA-4, LAG-3 and PD-1 bispecifics) by INN, used only to explain
# the SC-share trend; mention-level counts (a study with two such antibodies counts twice).
CHECKPOINT = {"pembrolizumab", "nivolumab", "atezolizumab", "durvalumab", "avelumab", "cemiplimab", "dostarlimab",
              "tislelizumab", "sintilimab", "camrelizumab", "toripalimab", "serplulimab", "penpulimab", "retifanlimab",
              "zimberelimab", "prolgolimab", "balstilimab", "spartalizumab", "envafolimab", "sugemalimab", "adebrelimab",
              "socazolimab", "pucotenlimab", "cadonilimab", "ivonescimab", "ipilimumab", "tremelimumab", "relatlimab",
              "cosibelimab", "finotonlimab", "enlonstobart", "tebotelimab", "botensilimab", "balstilimab", "pidilizumab"}


def fetch(key, raw):
    sub, name, url = SOURCES[key]
    d = os.path.join(raw, sub)
    os.makedirs(d, exist_ok=True)
    path = os.path.join(d, name)
    if not os.path.exists(path):
        req = urllib.request.Request(url, headers={"User-Agent": UA})
        with urllib.request.urlopen(req, timeout=120) as r, open(path + ".part", "wb") as f:
            f.write(r.read())
        os.replace(path + ".part", path)
    data = open(path, "rb").read()
    return path, data, {"url": url, "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()}


def wilson(k, n, z=1.96):
    if n == 0:
        return None, None
    p = k / n
    den = 1 + z * z / n
    c = (p + z * z / (2 * n)) / den
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / den
    return round(c - h, 4), round(c + h, 4)


# ----------------------------------------------------------------------------- ClinicalTrials.gov
def ctgov_section(path, samples_path, first=2005, last_full=2025, partial=2026):
    d = json.load(open(path))
    years = list(range(first, partial + 1))

    def row(src, y, defn):
        c = src.get(str(y), {}).get(defn, {})
        sc = c.get("sc_only", 0) + c.get("both", 0)
        cl = sc + c.get("iv_only", 0)
        lo, hi = wilson(sc, cl)
        return {"year": y, "total": c.get("total", 0), "sc_only": c.get("sc_only", 0), "iv_only": c.get("iv_only", 0),
                "both": c.get("both", 0), "unclassified": c.get("none", 0), "sc_any": sc, "classified": cl,
                "sc_share": round(sc / cl, 4) if cl else None, "sc_share_ci95": [lo, hi], "partial_year": y == partial}

    tables = {}
    for grp, key in (("antibody", "mab_by_year"), ("biologic", "biologic_by_year")):
        tables[grp] = {defn: [row(d[key], y, defn) for y in years]
                       for defn in ("linked_loose", "linked_strict", "trial_loose", "trial_strict")}

    def pooled(grp, defn, y0, y1):
        rs = [r for r in tables[grp][defn] if y0 <= r["year"] <= y1]
        sc, cl, tot = sum(r["sc_any"] for r in rs), sum(r["classified"] for r in rs), sum(r["total"] for r in rs)
        lo, hi = wilson(sc, cl)
        return {"years": [y0, y1], "trials": tot, "classified": cl, "sc_any": sc, "iv_only": cl - sc,
                "sc_share": round(sc / cl, 4) if cl else None, "ci95": [lo, hi],
                "sc_any_per_year": round(sc / (y1 - y0 + 1), 1)}

    periods = [(2005, 2009), (2010, 2014), (2015, 2019), (2020, 2025)]
    pooled_tab = {grp: {defn: [pooled(grp, defn, a, b) for a, b in periods]
                        for defn in ("linked_loose", "linked_strict", "trial_loose")} for grp in ("antibody", "biologic")}
    hy = d.get("hyaluronidase_or_sc_brand_mab_by_year", {})
    hy_rows = [[y, hy.get(str(y), 0)] for y in years]
    samples = json.load(open(samples_path)) if samples_path and os.path.exists(samples_path) else []
    peak = max((r for r in tables["antibody"]["linked_loose"] if not r["partial_year"]), key=lambda r: r["sc_share"])
    cpi = []
    for y in years:
        c_iv = sum(v.get("iv_years", {}).get(str(y), 0) for k, v in d["per_mab"].items() if k in CHECKPOINT)
        a_iv = sum(v.get("iv_years", {}).get(str(y), 0) for v in d["per_mab"].values())
        c_sc = sum(v.get("sc_years", {}).get(str(y), 0) for k, v in d["per_mab"].items() if k in CHECKPOINT)
        a_sc = sum(v.get("sc_years", {}).get(str(y), 0) for v in d["per_mab"].values())
        cpi.append({"year": y, "checkpoint_iv_mentions": c_iv, "all_iv_mentions": a_iv,
                    "checkpoint_share_of_iv": round(c_iv / a_iv, 3) if a_iv else None,
                    "sc_share_excluding_checkpoint": round((a_sc - c_sc) / ((a_sc - c_sc) + (a_iv - c_iv)), 3) if (a_sc - c_sc + a_iv - c_iv) else None})
    return {"raw": d, "tables": tables, "pooled": pooled_tab, "hy_rows": hy_rows, "samples": samples, "peak": peak, "cpi": cpi,
            "years": years, "partial": partial, "last_full": last_full}


# ----------------------------------------------------------------------------- FDA Purple Book
def parse_date(s):
    s = (s or "").strip()
    for fmt in ("%B %d, %Y", "%b %d, %Y", "%m/%d/%Y"):
        try:
            return dt.datetime.strptime(s, fmt).date()
        except ValueError:
            pass
    return None


def route_set(r):
    r = (r or "").lower()
    out = set()
    if "subcutaneous" in r:
        out.add("SC")
    if "intravenous" in r:
        out.add("IV")
    if not out and r.strip():
        out.add("other")
    return out


def purplebook_section(data):
    text = data.decode("utf-8-sig", errors="replace")
    rows = list(csv.reader(io.StringIO(text)))
    hdr_idx = [i for i, r in enumerate(rows) if r and r[0] == "N/R/U"]
    h = rows[hdr_idx[-1]]
    prods = [dict(zip(h, r)) for r in rows[hdr_idx[-1] + 1:] if len(r) > 5 and r[2].strip()]
    mab = []
    for p in prods:
        m = MAB_RE.search(p["Proper Name"])
        if not m:
            continue
        p["_inn"] = m.group(1).lower()
        p["_date"] = parse_date(p["Approval Date"])
        p["_routes"] = route_set(p["Route of Administration"])
        p["_orig"] = p["License Type"].strip().startswith("351(a)")
        p["_hyal"] = "hyaluronidase" in p["Proper Name"].lower()
        mab.append(p)
    # BLA level: route(s) at first licensure
    bla = defaultdict(list)
    for p in mab:
        bla[p["BLA Number"].strip()].append(p)
    bla_first = {}
    for b, ps in bla.items():
        dated = [p for p in ps if p["_date"]]
        if not dated:
            continue
        d0 = min(p["_date"] for p in dated)
        r0 = set().union(*[p["_routes"] for p in dated if p["_date"] == d0])
        bla_first[b] = {"date": d0, "routes": r0, "orig": any(p["_orig"] for p in ps), "inn": ps[0]["_inn"],
                        "name": ps[0]["Proprietary Name"], "applicant": ps[0]["Applicant"], "center": ps[0]["Center"]}

    def cat(rs):
        if "SC" in rs and "IV" in rs:
            return "SC and IV"
        if "SC" in rs:
            return "SC"
        if "IV" in rs:
            return "IV"
        return "other"

    per_year = defaultdict(Counter)
    for b, v in bla_first.items():
        per_year[(v["date"].year, "orig" if v["orig"] else "biosimilar")][cat(v["routes"])] += 1
    # INN level, originator (351(a)) products only: first IV and first SC licensure
    inn = defaultdict(lambda: {"iv": None, "sc": None, "sc_name": None, "sc_applicant": None, "iv_name": None})
    for p in mab:
        if not p["_orig"] or not p["_date"]:
            continue
        v = inn[p["_inn"]]
        if "IV" in p["_routes"] and (v["iv"] is None or p["_date"] < v["iv"]):
            v["iv"], v["iv_name"] = p["_date"], p["Proprietary Name"]
        if "SC" in p["_routes"] and (v["sc"] is None or p["_date"] < v["sc"]):
            v["sc"], v["sc_name"], v["sc_applicant"] = p["_date"], p["Proprietary Name"], p["Applicant"]
    switches = sorted([{"inn": k, "first_iv": v["iv"].isoformat(), "iv_product": v["iv_name"],
                        "first_sc": v["sc"].isoformat(), "sc_product": v["sc_name"], "sc_applicant": v["sc_applicant"],
                        "lag_years": round((v["sc"] - v["iv"]).days / 365.25, 1)}
                       for k, v in inn.items() if v["iv"] and v["sc"] and v["sc"] > v["iv"]],
                      key=lambda r: r["first_sc"])
    hyal = sorted({(p["Proprietary Name"], p["Proper Name"], p["Applicant"], p["_date"].isoformat() if p["_date"] else "")
                   for p in mab if p["_hyal"]}, key=lambda r: r[3])
    # first-hyal date per product name (dedupe presentations)
    hyal_first = {}
    for nm, proper, app, d in hyal:
        if nm not in hyal_first or (d and d < hyal_first[nm][2]):
            hyal_first[nm] = (proper, app, d)
    return {"n_products": len(prods), "n_mab_rows": len(mab), "n_mab_bla": len(bla_first), "bla_first": bla_first,
            "per_year": per_year, "switches": switches,
            "hyal_products": sorted([[k, v[0], v[1], v[2]] for k, v in hyal_first.items()], key=lambda r: r[3])}


def drugsfda_crosscheck(data, pb):
    z = zipfile.ZipFile(io.BytesIO(data))
    res = json.loads(z.read(z.namelist()[0]))
    recs = res["results"]
    found, same_date, n = 0, 0, 0
    d_mab = {}
    for x in recs:
        an = x.get("application_number", "")
        if not an.startswith("BLA"):
            continue
        if not any(re.search(r"MAB\b", ai.get("name", ""), re.I) for p in x.get("products", []) for ai in p.get("active_ingredients", [])):
            continue
        orig = [s.get("submission_status_date") for s in x.get("submissions", [])
                if s.get("submission_type") == "ORIG" and s.get("submission_status") == "AP" and s.get("submission_status_date")]
        d_mab[an[3:]] = min(orig) if orig else None
    for b, v in pb["bla_first"].items():
        if v["center"] != "CDER":
            continue
        n += 1
        if b in d_mab:
            found += 1
            if d_mab[b] and d_mab[b] == v["date"].strftime("%Y%m%d"):
                same_date += 1
    return {"drugsfda_records": len(recs), "drugsfda_mab_bla": len(d_mab), "purplebook_cder_mab_bla": n,
            "found_in_drugsfda": found, "same_first_approval_date": same_date,
            "keytruda_qlex_BLA761467": d_mab.get("761467"), "last_updated": res["meta"].get("last_updated")}


# ----------------------------------------------------------------------------- USGS lithium
NS = {"m": "http://schemas.openxmlformats.org/spreadsheetml/2006/main"}


def xlsx_rows(data):
    z = zipfile.ZipFile(io.BytesIO(data))
    ss = []
    if "xl/sharedStrings.xml" in z.namelist():
        for si in ET.fromstring(z.read("xl/sharedStrings.xml")).findall("m:si", NS):
            ss.append("".join(t.text or "" for t in si.iter("{%s}t" % NS["m"])))
    root = ET.fromstring(z.read("xl/worksheets/sheet1.xml"))
    out = []
    for row in root.iter("{%s}row" % NS["m"]):
        vals = {}
        for c in row.findall("m:c", NS):
            v = c.find("m:v", NS)
            x = (ss[int(v.text)] if c.get("t") == "s" else v.text) if v is not None else ""
            vals[re.sub(r"\d+", "", c.get("r"))] = x
        out.append(vals)
    return out


def num(s):
    s = (s or "").replace(",", "").strip()
    try:
        return float(s)
    except ValueError:
        return None


def lithium_section(ds140, mcs22, mcs23, mcs24, mcs26):
    rows = xlsx_rows(ds140)
    hdr = next(r for r in rows if r.get("A") == "Year")
    col = {v: k for k, v in hdr.items()}
    world, us_cons = {}, {}
    for r in rows:
        y = r.get("A", "")
        if not y.isdigit():
            continue
        y = int(y)
        w = num(r.get(col["World production (lithium content)"]))
        if w is not None:
            world[y] = {"t": w, "source": "USGS DS140 (2021 ed., modified 2023-08-02)", "estimated": False}
        c = num(r.get(col["Estimated consumption"]))
        if c is not None:
            us_cons[y] = c

    def mcs_world(data, tag):
        txt = data.decode("utf-8-sig", errors="replace")
        for r in csv.DictReader(io.StringIO(txt)):
            if r.get("Country", "").startswith("World total"):
                out = {}
                for k, v in r.items():
                    m = re.match(r"Prod_t_(est_|Est_)?(\d{4})", k or "")
                    if m and num(v) is not None:
                        out[int(m.group(2))] = {"t": num(v), "source": tag, "estimated": bool(m.group(1))}
                return out
        return {}

    for data, tag in ((mcs22, "USGS MCS 2022"), (mcs23, "USGS MCS 2023"), (mcs24, "USGS MCS 2024")):
        for y, v in mcs_world(data, tag).items():
            if y not in world or world[y]["source"].startswith("USGS MCS"):
                world[y] = v  # later editions overwrite earlier estimates; DS140 kept to 2021
    price = {}
    for r in csv.DictReader(io.StringIO(mcs26.decode("latin-1"))):
        if r["MCS chapter"].strip().upper() != "LITHIUM":
            continue
        if r["Section"].startswith("World Mine") and r["Country"] == "World total" and r["Statistics"] == "Production":
            world[int(r["Year"])] = {"t": num(r["Value"]), "source": "USGS MCS 2026",
                                     "estimated": "Estimated" in r["Notes"]}
        if r["Statistics"] == "Price":
            price[int(r["Year"])] = {"value": r["Value"], "unit": r["Unit"], "detail": r["Statistics_detail"]}
    return {"world": dict(sorted(world.items())), "us_consumption_est": dict(sorted(us_cons.items())), "price": price}


# ----------------------------------------------------------------------------- accounting
def parse_sacct(path):
    jobs = []
    if not path or not os.path.exists(path):
        return jobs
    main, rss = {}, {}
    for line in open(path):
        f = line.split()
        if not f:
            continue
        if f[0].endswith(".batch") and len(f) >= 5:
            rss[f[0].split(".")[0]] = f[-1]
        elif f[0].isdigit() and len(f) >= 7 and f[1].startswith("of-"):
            main[f[0]] = {"job_id": f[0], "name": f[1], "partition": f[2].replace("mit_quick+", "mit_quicktest"),
                          "state": f[3], "elapsed": f[4], "cpus": int(f[5])}
    for j, v in main.items():
        v["max_rss"] = rss.get(j)
        jobs.append(v)
    return sorted(jobs, key=lambda v: v["job_id"])


def hms(s):
    h, m, sec = (int(x) for x in s.split(":"))
    return h * 3600 + m * 60 + sec


# ----------------------------------------------------------------------------- assemble
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--raw", required=True)
    ap.add_argument("--ctgov", required=True)
    ap.add_argument("--samples", default="")
    ap.add_argument("--sacct", default="")
    ap.add_argument("--ctgov-meta", default="", help="json with zip bytes/sha256/accessed from the cluster")
    ap.add_argument("--out", required=True)
    a = ap.parse_args()

    _, pb_data, pb_meta = fetch("purplebook", a.raw)
    _, fda_data, fda_meta = fetch("drugsfda", a.raw)
    li_files = {k: fetch(k, a.raw) for k in ("ds140", "mcs2022", "mcs2023", "mcs2024", "mcs2026")}
    pb = purplebook_section(pb_data)
    xchk = drugsfda_crosscheck(fda_data, pb)
    li = lithium_section(*(li_files[k][1] for k in ("ds140", "mcs2022", "mcs2023", "mcs2024", "mcs2026")))
    ct = ctgov_section(a.ctgov, a.samples)
    ctmeta = json.load(open(a.ctgov_meta)) if a.ctgov_meta and os.path.exists(a.ctgov_meta) else {}
    jobs = parse_sacct(a.sacct)

    raw = ct["raw"]
    LL = ct["tables"]["antibody"]["linked_loose"]
    LS = ct["tables"]["antibody"]["linked_strict"]
    TL = ct["tables"]["antibody"]["trial_loose"]
    BL = ct["tables"]["biologic"]["linked_loose"]
    pooled = ct["pooled"]["antibody"]["linked_loose"]
    p_first, p_last = pooled[0], pooled[-1]
    y05 = next(r for r in LL if r["year"] == 2005)
    full = [r for r in LL if not r["partial_year"]]
    last5 = [r for r in full if r["year"] >= 2021]
    sc_last5 = round(sum(r["sc_any"] for r in last5) / len(last5), 1)
    sw = pb["switches"]
    sw_recent = [s for s in sw if s["first_sc"] >= "2020-01-01"]
    hy_tot = sum(v for _, v in ct["hy_rows"])

    # ---------------- charts
    pct = lambda v: None if v is None else round(100 * v, 1)
    charts = [
        {"id": "ct-sc-share", "kind": "line",
         "title": "Share of antibody trials that give the antibody subcutaneously",
         "subtitle": "ClinicalTrials.gov, interventional studies with an INN '-mab' antibody, by start year; share of trials whose text states a route",
         "x": {"label": "Study start year", "unit": "year", "scale": "time"},
         "y": {"label": "Subcutaneous share", "unit": "%", "scale": "linear"},
         "series": [
             {"name": "Route linked to the antibody, words + abbreviations (primary)", "color": "orange",
              "points": [[r["year"], pct(r["sc_share"])] for r in LL]},
             {"name": "Route linked to the antibody, full words only", "color": "cyan",
              "points": [[r["year"], pct(r["sc_share"])] for r in LS]},
             {"name": "Any route word anywhere in the trial (crude)", "color": "grey",
              "points": [[r["year"], pct(r["sc_share"])] for r in TL]}],
         "annotations": [{"x": ct["peak"]["year"], "y": pct(ct["peak"]["sc_share"]), "text": f"peak {pct(ct['peak']['sc_share'])}% ({ct['peak']['year']})"},
                         {"x": ct["partial"], "y": pct(LL[-1]["sc_share"]), "text": f"{ct['partial']} partial (registry of 24 Oct 2026; includes planned start dates)"}],
         "caption": "Share = trials whose antibody-linked text says subcutaneous / trials that state any SC or IV route. "
                    "The SC share rose until the mid-2010s, then fell as IV checkpoint-inhibitor oncology trials multiplied. "
                    "It is a registry proxy for formulation demand, not a market share, and 30-40% of trials state no route."},
        {"id": "ct-route-counts", "kind": "stacked",
         "title": "Antibody trials per start year, by stated route of the antibody",
         "subtitle": "ClinicalTrials.gov full registry (608,415 studies parsed); primary definition",
         "x": {"label": "Study start year", "unit": "year", "scale": "time"},
         "y": {"label": "Interventional trials", "unit": "trials", "scale": "linear"},
         "series": [
             {"name": "Subcutaneous only", "color": "orange", "points": [[r["year"], r["sc_only"]] for r in LL]},
             {"name": "Both SC and IV", "color": "violet", "points": [[r["year"], r["both"]] for r in LL]},
             {"name": "Intravenous only", "color": "cyan", "points": [[r["year"], r["iv_only"]] for r in LL]},
             {"name": "No route stated", "color": "grey", "points": [[r["year"], r["unclassified"]] for r in LL]}],
         "annotations": [{"x": ct["partial"], "y": LL[-1]["total"], "text": "partial year"}],
         "caption": f"Trials with an SC antibody arm grew from {y05['sc_any']} (2005 start) to {sc_last5} per year on average in 2021-2025. "
                    "Counts are registered studies, not patients or doses; one study counts once."},
        {"id": "ct-hyaluronidase", "kind": "bar",
         "title": "Trials of antibodies reformulated for subcutaneous injection",
         "subtitle": "ClinicalTrials.gov: antibody interventions co-formulated with a hyaluronidase or named by an SC brand/code",
         "x": {"label": "Study start year", "unit": "year", "scale": "time"},
         "y": {"label": "Trials", "unit": "trials", "scale": "linear"},
         "series": [{"name": "Hyaluronidase / SC-brand antibody trials", "color": "violet", "points": ct["hy_rows"]}],
         "annotations": [],
         "caption": "A high-precision but incomplete marker of IV-to-SC reformulation programmes (e.g. daratumumab Faspro, "
                    "pembrolizumab MK-3475A). Programmes that reach high concentration without an enzyme are not captured."},
        {"id": "fda-new-antibodies", "kind": "stacked",
         "title": "New FDA antibody licences by route at first approval",
         "subtitle": "FDA Purple Book (Sep 2026 download): originator (351(a)) BLAs whose proper name carries an INN '-mab' stem",
         "x": {"label": "Year of first licensure", "unit": "year", "scale": "time"},
         "y": {"label": "New originator antibody BLAs", "unit": "BLAs", "scale": "linear"},
         "series": [], "annotations": [],
         "caption": "Route of the products licensed on the BLA's first approval date. Biosimilars (351(k)) are excluded here "
                    "and reported in stats. A count of licences, not of sales or doses."},
        {"id": "fda-iv-to-sc", "kind": "hbar",
         "title": "Antibodies first licensed IV that later gained an FDA-licensed SC product",
         "subtitle": "FDA Purple Book, originator products; years from first IV licence to first SC licence",
         "x": {"label": "Antibody (first SC licence)", "unit": "", "scale": "category"},
         "y": {"label": "Years from first IV to first SC licence", "unit": "years", "scale": "linear"},
         "series": [{"name": "IV-to-SC lag", "color": "orange",
                     "points": [[f"{s['inn']} ({s['first_sc'][:4]}, {s['sc_product']})", s["lag_years"]] for s in sw]}],
         "annotations": [],
         "caption": "Each bar is one antibody (INN) licensed IV first that later gained a subcutaneous product under a 351(a) licence "
                    "(biosimilars excluded); usually the same company, but SC infliximab (Zymfentra) is Celltrion's and daclizumab/ofatumumab "
                    "changed indication. "
                    "Most recent SC versions are co-formulated with a hyaluronidase, an existing competitor route to "
                    "high-dose SC delivery; crystalline suspensions are an alternative, not yet a licensed one for antibodies."},
        {"id": "lithium-world", "kind": "line",
         "title": "World lithium mine production",
         "subtitle": "USGS, metric tons of contained lithium, excluding US production (withheld)",
         "x": {"label": "Year", "unit": "year", "scale": "time"},
         "y": {"label": "Mine production", "unit": "t Li", "scale": "linear"},
         "series": [{"name": "World mine production (Li content)", "color": "green",
                     "points": [[y, v["t"]] for y, v in li["world"].items()]}],
         "annotations": [{"x": y, "y": v["t"], "text": "USGS estimate"} for y, v in li["world"].items() if v["estimated"]],
         "caption": "Demand context for lithium-selective separation (MOF membranes). It shows supply growth of the "
                    "commodity, not demand for membranes and not any role for orbit-made MOFs."},
    ]
    yrs = sorted({y for (y, kind) in pb["per_year"] if kind == "orig"})
    yrs = list(range(min(yrs), max(yrs) + 1))
    cols = {"SC": ("SC only", "orange"), "SC and IV": ("SC and IV", "violet"), "IV": ("IV only", "cyan"), "other": ("Other route", "grey")}
    charts[3]["series"] = [{"name": nm, "color": c, "points": [[y, pb["per_year"].get((y, "orig"), Counter()).get(k, 0)] for y in yrs]}
                           for k, (nm, c) in cols.items()]
    y_first = yrs[0]

    # Purple Book stats
    def pb_period(y0, y1, kind="orig"):
        c = Counter()
        for y in range(y0, y1 + 1):
            c.update(pb["per_year"].get((y, kind), Counter()))
        n = sum(c.values())
        sc = c["SC"] + c["SC and IV"]
        return {"years": [y0, y1], "new_bla": n, "sc_or_both": sc, "iv_only": c["IV"], "other": c["other"],
                "sc_share": round(sc / n, 3) if n else None}

    pb_stats = {"products_rows": pb["n_products"], "antibody_product_rows": pb["n_mab_rows"], "antibody_bla": pb["n_mab_bla"],
                "originator_by_period": [pb_period(a, b) for a, b in ((y_first, 2004), (2005, 2014), (2015, 2019), (2020, 2026))],
                "biosimilar_by_period": [pb_period(a, b, "biosimilar") for a, b in ((2015, 2019), (2020, 2026))],
                "iv_to_sc_switches": sw, "hyaluronidase_coformulated_products": pb["hyal_products"]}

    ct_tot = raw["totals"]
    n_mab_trials = sum(v["linked_loose"].get("total", 0) for v in raw["mab_by_year"].values())
    n_bio_trials = sum(v["linked_loose"].get("total", 0) for v in raw["biologic_by_year"].values())

    hc = HAND_CHECK_RESULTS
    zip_bytes = ctmeta.get("zip_bytes", 2772470590)
    cpu_s = sum(hms(j["elapsed"]) * j["cpus"] for j in jobs)
    wall_s = sum(hms(j["elapsed"]) for j in jobs)

    headline_val = len(sw_recent)
    out = {
        "id": "demand-signals",
        "tab": "network",
        "material": "protein",
        "title": "Who needs high-concentration protein formulations, and how fast is that growing?",
        "question": "Is there real, growing demand for the formulations orbit-grown protein crystals could serve "
                    "(subcutaneous high-dose antibodies), and for the commodities our other candidates touch (lithium)?",
        "headline": {"value": str(headline_val), "unit": "antibodies",
                     "text": f"Since 2020 the FDA has licensed subcutaneous versions of {headline_val} antibodies first licensed as IV "
                             f"infusions (Keytruda Qlex in Sep 2025), and registered SC antibody trials grew from {y05['sc_any']} "
                             f"starting in 2005 to about {round(sc_last5)} a year in 2021-2025."},
        "evidence_level": "our computation on public data",
        "datasets": [
            {"name": "ClinicalTrials.gov full registry, bulk JSON (API v2 download)",
             "url": "https://clinicaltrials.gov/api/v2/studies/download?format=json.zip",
             "license": "U.S. National Library of Medicine; public registry data (clinicaltrials.gov terms and conditions)",
             "records": ct_tot["n_parsed"], "bytes": zip_bytes, "accessed": ACCESSED,
             "notes": f"{ct_tot['n_members']} study files, {raw['uncompressed_bytes']} bytes uncompressed, {ct_tot['n_errors']} parse errors; "
                      f"{ct_tot['n_interventional']} interventional; {n_mab_trials} interventional studies with an INN '-mab' antibody; "
                      f"{n_bio_trials} with any biologic. Streamed inside the zip on MIT Engaging; sha256 {ctmeta.get('zip_sha256', 'see appendix')}."},
            {"name": "FDA Purple Book, monthly data download (September 2026)", "url": pb_meta["url"],
             "license": "U.S. Government work (public domain)", "records": pb["n_products"], "bytes": pb_meta["bytes"], "accessed": ACCESSED,
             "notes": f"All licensed biologics (CDER and CBER) with route and approval date; {pb['n_mab_rows']} antibody product rows in {pb['n_mab_bla']} BLAs. sha256 {pb_meta['sha256']}."},
            {"name": "openFDA Drugs@FDA bulk file", "url": fda_meta["url"], "license": "openFDA, CC0 / public domain",
             "records": xchk["drugsfda_records"], "bytes": fda_meta["bytes"], "accessed": ACCESSED,
             "notes": f"Cross-check of antibody BLA first-approval dates (openFDA last_updated {xchk['last_updated']}). sha256 {fda_meta['sha256']}."},
            {"name": "USGS Data Series 140, lithium historical statistics (2021 edition)", "url": li_files["ds140"][2]["url"],
             "license": "U.S. Government work (public domain)", "records": len(li["world"]), "bytes": li_files["ds140"][2]["bytes"], "accessed": ACCESSED,
             "notes": "World production, lithium content, 2000-2021; US estimated consumption to 2021."},
            {"name": "USGS Mineral Commodity Summaries lithium data releases 2022-2024 and MCS 2026 commodities table",
             "url": "https://www.sciencebase.gov/catalog/item/696a75d5d4be0228872d3bf8",
             "license": "U.S. Government work (public domain)", "records": 8886,
             "bytes": sum(li_files[k][2]["bytes"] for k in ("mcs2022", "mcs2023", "mcs2024", "mcs2026")), "accessed": ACCESSED,
             "notes": "World mine production 2022-2025 (2023 from the MCS 2024 estimate; the MCS 2025 lithium release has no world table). US consumption is withheld (W) in MCS 2026."},
        ],
        "compute": {"where": "MIT Engaging (ClinicalTrials.gov download and parse); laptop (FDA, USGS, assembly)",
                    "partitions": sorted({j["partition"] for j in jobs if j["state"] == "COMPLETED"}),
                    "job_ids": [j["job_id"] for j in jobs], "jobs": jobs,
                    "cpu_hours": round(cpu_s / 3600, 3), "wall_minutes": round(wall_s / 60, 1),
                    "peak_storage_gb": round(zip_bytes / 1e9, 2)},
        "method": [
            "Downloaded the full ClinicalTrials.gov registry as one bulk JSON zip on MIT Engaging and streamed all study files inside the zip with 6 worker processes (no extraction).",
            "Kept interventional studies. An antibody intervention is one whose name or other names contain an INN monoclonal-antibody stem word (-mab), 'monoclonal antibody' or 'mAb'; a biologic is interventionType BIOLOGICAL or an antibody.",
            "Route text is attributed to the antibody itself: its own name, other names and description, and text windows around its name in arm descriptions and titles, cut at the nearest mention of any other intervention so the route of co-administered chemotherapy or vaccines is not counted.",
            "Primary route definition: full words (subcutaneous, intravenous) plus abbreviations in a dosing context (SC/IV after a dose unit or before injection/infusion/dose/every/q3w..., s.c., i.v., subQ) plus 'infusion' for IV (not subcutaneous infusion or infusion reactions). Sensitivity: full words only, and a crude trial-wide match.",
            "Counted one study once per start year (startDateStruct); SC share = studies with an SC antibody route / studies with any stated SC or IV antibody route, with Wilson 95% intervals. 2026 is partial and includes planned start dates.",
            "Hand-checked the classifier on a deterministic 2% hash sample of antibody studies (20 SC-positive, 20 IV-positive).",
            "Counted antibody interventions co-formulated with a hyaluronidase or named by an SC brand/code (Faspro, Hybreza, Qvantig, Qlex, Zunovo, Phesgo, MK-3475A...) as a high-precision marker of IV-to-SC reformulation programmes.",
            "From the FDA Purple Book (every licensed biologic), took antibody BLAs (INN -mab in the proper name), dated each by its first approval date and its route then; for originator products found each antibody's first IV and first SC licence and listed those that went IV first, SC later. Cross-checked first-approval dates against openFDA Drugs@FDA.",
            "Joined USGS DS140 world lithium-content production (2000-2021) with MCS 2022, 2024 and 2026 world totals (2020-2025), latest edition winning.",
        ],
        "charts": charts,
        "stats": {
            "ctgov_totals": {**ct_tot, "uncompressed_bytes": raw["uncompressed_bytes"], "antibody_interventional_trials": n_mab_trials,
                             "biologic_interventional_trials": n_bio_trials, "parse_elapsed_s": raw["elapsed_s"], "workers": raw["workers"]},
            "antibody_sc_share_pooled_primary": ct["pooled"]["antibody"]["linked_loose"],
            "antibody_sc_share_pooled_strict": ct["pooled"]["antibody"]["linked_strict"],
            "antibody_sc_share_pooled_trialwide": ct["pooled"]["antibody"]["trial_loose"],
            "biologic_sc_share_pooled_primary": ct["pooled"]["biologic"]["linked_loose"],
            "antibody_by_year_primary": LL,
            "biologic_by_year_primary": BL,
            "sc_antibody_trials_2005": y05["sc_any"], "sc_antibody_trials_per_year_2021_2025": sc_last5,
            "growth_multiple_sc_2005_to_2021_25_mean": round(sc_last5 / y05["sc_any"], 1) if y05["sc_any"] else None,
            "peak_sc_share_year": ct["peak"]["year"], "peak_sc_share": ct["peak"]["sc_share"],
            "checkpoint_inhibitor_iv_mentions_by_year": ct["cpi"],
            "hyaluronidase_or_sc_brand_trials_total_2005_2026": hy_tot,
            "hyaluronidase_or_sc_brand_top_sponsors": raw.get("hyaluronidase_or_sc_brand_sponsors", [])[:12],
            "hyaluronidase_or_sc_brand_trials": raw.get("hyaluronidase_or_sc_brand_trials", [])[:120],
            "top_lead_sponsors_sc_antibody_trials": raw["top_sponsors_sc_mab"][:15],
            "sc_antibody_trial_sponsor_class": raw["sc_mab_sponsor_class"],
            "precision_check": hc,
            "purple_book": pb_stats,
            "drugsfda_crosscheck": xchk,
            "lithium_world_production_t": {str(y): v for y, v in li["world"].items()},
            "lithium_us_estimated_consumption_t": {str(y): v for y, v in li["us_consumption_est"].items() if y >= 2000},
            "lithium_price_mcs2026": {str(y): v for y, v in sorted(li["price"].items())},
            "lithium_growth_2015_to_2025": round(li["world"][2025]["t"] / li["world"][2015]["t"], 1),
        },
        "findings": [],
        "limitations": [],
        "future_big_data": [],
        "partners": [],
        "code": ["analysis/bigdata/logistics_ctgov.py", "analysis/bigdata/logistics_demand.py", "cluster/bigdata/logistics-ctgov.sbatch"],
        "reproduce": [
            "rsync -azR analysis/bigdata/logistics_ctgov.py cluster/bigdata/logistics-ctgov.sbatch engaging:~/orcd/scratch/orbital-foundry-20261024-01a170b7/",
            "ssh engaging 'cd ~/orcd/scratch/orbital-foundry-20261024-01a170b7 && sbatch -c 1 --mem=2G -J of-logistics-ctgov-dl cluster/bigdata/logistics-ctgov.sbatch download'",
            "ssh engaging 'cd ~/orcd/scratch/orbital-foundry-20261024-01a170b7 && sbatch -p mit_quicktest -t 00:15:00 -c 6 --mem=12G -J of-logistics-ctgov-parse cluster/bigdata/logistics-ctgov.sbatch parse'",
            "rsync -az engaging:~/orcd/scratch/orbital-foundry-20261024-01a170b7/bigdata/logistics/work/ctgov-route*.json <work>/",
            "python3 -I analysis/bigdata/logistics_demand.py --raw <raw dir> --ctgov <work>/ctgov-routes.json --samples <work>/ctgov-route-samples.json --sacct <work>/sacct.txt --ctgov-meta <work>/ctgov-meta.json --out data/results/bigdata/demand-signals.json",
        ],
        "generated_at": dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat(),
    }
    out["findings"], out["limitations"], out["future_big_data"], out["partners"] = narrative(out, ct, pb, li, sw, sw_recent, xchk, hc, raw)
    s = json.dumps(out, indent=1, ensure_ascii=False, default=str)
    os.makedirs(os.path.dirname(os.path.abspath(a.out)), exist_ok=True)
    with open(a.out, "w") as f:
        f.write(s)
    print(f"wrote {a.out} ({len(s)/1024:.0f} KB)")


# Hand precision check of the route classifier (primary definition), done by reading the matched snippet of
# the deterministic sample written by logistics_ctgov.py (sha1(NCT) < 2% of antibody studies; v3 classifier,
# Engaging job 26814260). First 20 SC-positive studies in NCT order and every 14th IV-positive study.
# Verdict = does the snippet say the *antibody* is given by that route?
HAND_CHECK_RESULTS = {
    "sample": "deterministic hash sample (~2%) of interventional antibody studies; 545 studies",
    "sc_n": 20, "sc_correct": 18,
    "sc_errors": ["NCT01373229: SC refers to co-administered plerixafor", "NCT02089685: SC refers to co-administered PEG-IFN; pembrolizumab is IV"],
    "sc_checked": ["NCT00235833", "NCT00390221", "NCT01059435", "NCT01302795", "NCT01373229", "NCT01448239", "NCT01845740",
                   "NCT01859988", "NCT01882491", "NCT01894360", "NCT01989468", "NCT02017639", "NCT02089685", "NCT02135640",
                   "NCT02272946", "NCT02385110", "NCT02443298", "NCT02497469", "NCT02684370", "NCT02852694"],
    "iv_n": 20, "iv_correct": 19,
    "iv_errors": ["NCT00004143: 'infused' refers to stem cells, not alemtuzumab"],
    "iv_checked": ["NCT00004143", "NCT00583830", "NCT00927615", "NCT01121939", "NCT01763645", "NCT02409355", "NCT02807103",
                   "NCT03077828", "NCT03308396", "NCT03705858", "NCT03971474", "NCT04246086", "NCT04483739", "NCT04782791",
                   "NCT05045716", "NCT05534646", "NCT05897268", "NCT06171178", "NCT06695013", "NCT07069712"],
    "sample_studies": 545, "sample_sc_positive": 58, "sample_iv_positive": 291, "sample_unclassified": 208,
    "unclassified_share_pct": 38.2,
    "note": "All three errors attach a co-administered agent's route to the antibody. Recall was not measured; "
            "38% of sampled antibody studies state no route in the fields read.",
}
HAND_CHECK_RESULTS["sc_precision_ci95"] = list(wilson(HAND_CHECK_RESULTS["sc_correct"], HAND_CHECK_RESULTS["sc_n"]))
HAND_CHECK_RESULTS["iv_precision_ci95"] = list(wilson(HAND_CHECK_RESULTS["iv_correct"], HAND_CHECK_RESULTS["iv_n"]))


def narrative(out, ct, pb, li, sw, sw_recent, xchk, hc, raw):
    st = out["stats"]
    p = st["antibody_sc_share_pooled_primary"]
    ps = st["antibody_sc_share_pooled_strict"]
    cpi = {r["year"]: r for r in st["checkpoint_inhibitor_iv_mentions_by_year"]}
    ob = st["purple_book"]["originator_by_period"]
    f = [
        f"Across the full ClinicalTrials.gov registry ({st['ctgov_totals']['n_parsed']:,} studies), {st['ctgov_totals']['antibody_interventional_trials']:,} interventional studies test an INN '-mab' antibody.",
        f"Studies that give an antibody subcutaneously grew from {st['sc_antibody_trials_2005']} starting in 2005 to {round(st['sc_antibody_trials_per_year_2021_2025'])} a year on average in 2021-2025 (about {st['growth_multiple_sc_2005_to_2021_25_mean']}x).",
        f"The SC share of route-stated antibody studies was {round(100*p[0]['sc_share'])}% in 2005-2009, peaked at {round(100*st['peak_sc_share'])}% in {st['peak_sc_share_year']}, and was {round(100*p[-1]['sc_share'])}% in 2020-2025 (95% CI {round(100*p[-1]['ci95'][0])}-{round(100*p[-1]['ci95'][1])}%).",
        f"Part of that dip is the IV checkpoint-inhibitor boom: PD-1/PD-L1/CTLA-4/LAG-3 antibodies went from {round(100*cpi[2005]['checkpoint_share_of_iv'])}% of antibody-level IV mentions in 2005 to {round(100*cpi[2020]['checkpoint_share_of_iv'])}% in 2020; excluding them the SC share is {round(100*cpi[2020]['sc_share_excluding_checkpoint'])}% in 2020 (vs {round(100*cpi[2014]['sc_share_excluding_checkpoint'])}% in 2014), so it still fell, but less. These IV checkpoint antibodies are the pool now being converted to SC (nivolumab, atezolizumab, pembrolizumab).",
        f"With full words only (no abbreviations) the shares are higher ({round(100*ps[0]['sc_share'])}% in 2005-2009, {round(100*ps[-1]['sc_share'])}% in 2020-2025) because IV is more often abbreviated; the rise-then-plateau shape is the same.",
        f"The FDA Purple Book lists {len(sw)} antibodies licensed IV first that later gained an SC product under a 351(a) (non-biosimilar) licence; {len(sw_recent)} of those SC licences came in 2020 or later: " + ", ".join(f"{s['inn']} ({s['sc_product']}, {s['first_sc'][:7]})" for s in sw_recent) + ".",
        f"New originator antibody licences that include an SC product at first approval: {ob[0]['sc_or_both']}/{ob[0]['new_bla']} in {ob[0]['years'][0]}-2004, {ob[1]['sc_or_both']}/{ob[1]['new_bla']} in 2005-2014, {ob[2]['sc_or_both']}/{ob[2]['new_bla']} in 2015-2019 and {ob[3]['sc_or_both']}/{ob[3]['new_bla']} in 2020-2026 (FDA Purple Book).",
        f"{len(pb['hyal_products'])} licensed antibody products are co-formulated with a hyaluronidase: today's main route to high-dose SC antibodies is enzyme-assisted injection, not crystalline suspensions.",
        f"ClinicalTrials.gov holds {st['hyaluronidase_or_sc_brand_trials_total_2005_2026']} studies (start 2005-2026) of antibodies co-formulated with a hyaluronidase or named by an SC brand/code, a direct count of IV-to-SC reformulation programmes.",
        f"World lithium mine production rose from {int(li['world'][2015]['t']):,} t (2015) to an estimated {int(li['world'][2025]['t']):,} t in 2025 ({st['lithium_growth_2015_to_2025']}x, USGS, lithium content, excluding the US).",
    ]
    if hc:
        f.append(f"Hand check of the route classifier: {hc.get('sc_correct')}/{hc.get('sc_n')} SC calls and {hc.get('iv_correct')}/{hc.get('iv_n')} IV calls were correct on a deterministic sample; {hc.get('unclassified_share_pct')}% of sampled antibody studies state no route at all.")
    lim = [
        "Registered trials are a proxy for formulation demand. They do not measure doses, patients, sales or willingness to pay, and they say nothing yet about demand for orbit-grown crystals specifically.",
        "Route is inferred from free text with regular expressions. Precision is reported from a hand check, recall is lower: 30-40% of antibody studies state no route in the fields we read, and those are excluded from the share.",
        "The '-mab' INN stem misses antibodies known only by code names (e.g. MK-3475 alone) and antibodies named under the 2021+ INN scheme (-tug, -bart, -mig, -ment); 'biologic' (interventionType BIOLOGICAL) also includes vaccines and cell therapies.",
        "Start year is not approval year; 2026 is a partial year and includes planned (estimated) start dates. Registration practice changed over time (ICMJE 2005, FDAAA 2007, the 2017 Final Rule), so early-year counts are not strictly comparable.",
        "One study counts once even if it has many arms; studies are not independent of each other (one sponsor runs many related trials of one molecule).",
        "Purple Book counts are licences by route, not sales; route is read from the product listing, and our IV-to-SC list is restricted to originator (351(a)) products. Drugs@FDA covers only CDER BLAs and its route field is often just 'INJECTION', so it is used only as a date cross-check.",
        "SC demand is being met today mainly by hyaluronidase co-formulation and high-concentration liquids. Crystalline suspensions (Merck's published pembrolizumab work) are one alternative; this analysis does not show they will win.",
        "Lithium: production is a supply series, US consumption is withheld after 2021, the 2023 value is an MCS 2024 estimate, and 2024-2025 are USGS estimates. It does not show demand for MOF membranes.",
        "No solid-state / barocaloric cooling demand series was added: we found no quick, real public market series and did not substitute one.",
    ]
    fut = [
        "Link ClinicalTrials.gov interventions to RxNorm/UNII and to the FDA SPL label corpus (openFDA label bulk, ~1.8 GB zipped) to read the route and concentration (mg/mL) of every antibody product, instead of free-text regex.",
        "Add the EU Clinical Trials Register / CTIS and WHO ICTRP to cover non-US registrations, and the AACT relational snapshot for a dated history of protocol changes (IV-to-SC amendments).",
        "Use IQVIA-type or CMS Part B/Part D spending data to turn trial counts into dollars spent on IV infusion chair-time that SC conversion would remove.",
        "Text-mine patents (USPTO/EPO full text) for 'crystalline suspension' antibody formulations to size the specific crystal-formulation pipeline.",
        "For lithium, add USGS country-level production, IEA battery demand and direct-lithium-extraction project databases to size the separation-membrane market.",
    ]
    hy_sp = dict(raw.get("hyaluronidase_or_sc_brand_sponsors", []))
    merck_trials = [t for t in raw.get("hyaluronidase_or_sc_brand_trials", []) if "Merck Sharp" in t[2]]
    sw_by = {s["inn"]: s for s in sw}
    partners = []
    if "pembrolizumab" in sw_by:
        s = sw_by["pembrolizumab"]
        partners.append({"name": "Merck & Co. (MSD)",
                         "why": "Owns pembrolizumab, the project's published protein-crystal anchor, and has just moved it from IV to SC; a crystalline high-concentration suspension is a direct alternative formulation route.",
                         "evidence": f"FDA Purple Book: {s['sc_product']} licensed {s['first_sc']} ({s['lag_years']} years after IV Keytruda); ClinicalTrials.gov: {len(merck_trials)} Merck-sponsored hyaluronidase/SC-brand antibody studies, e.g. " + ", ".join(t[0] for t in merck_trials[:4]) + ". Merck's ISS pembrolizumab crystallization is a published result (Reichert et al., npj Microgravity 2019)."})
    groups = [("Johnson & Johnson (Janssen)", ["daratumumab", "amivantamab"], "Janssen"),
              ("Roche / Genentech", ["atezolizumab", "ocrelizumab", "trastuzumab", "rituximab", "pertuzumab"], "Roche|Genentech|Hoffmann"),
              ("Bristol Myers Squibb", ["nivolumab"], "Bristol")]
    for name, inns, pat in groups:
        hits = [sw_by[i] for i in inns if i in sw_by]
        nsp = sum(v for k, v in hy_sp.items() if re.search(pat, k))
        if hits or nsp:
            partners.append({"name": name,
                             "why": "Runs IV-to-SC antibody reformulation programmes, i.e. is already paying to make high-dose SC antibody formulations.",
                             "evidence": "FDA Purple Book SC licences: " + "; ".join(f"{h['inn']} ({h['sc_product']}, {h['first_sc']})" for h in hits)
                                         + f". ClinicalTrials.gov: {nsp} hyaluronidase/SC-brand antibody studies with this lead sponsor."})
    top = raw["top_sponsors_sc_mab"][:6]
    partners.append({"name": "Large SC-antibody trial sponsors: " + ", ".join(t[0] for t in top),
                     "why": "The industrial sponsors that register the most studies giving an antibody subcutaneously, i.e. the buyers of high-concentration formulation capacity.",
                     "evidence": "ClinicalTrials.gov lead-sponsor counts of SC antibody studies (primary definition): " + ", ".join(f"{t[0]} {t[1]}" for t in top) + "."})
    return f, lim, fut, partners


if __name__ == "__main__":
    sys.exit(main())
