#!/usr/bin/env python3
"""matdb B: geometric pre-screen of known MOFs for lithium-sieving pore windows.

Data (CC-BY-4.0, Zenodo):
  CoRE MOF 2024 public (SI) release, record 15055758: computation-ready ASR / FSR / ION
    descriptor tables (Zeo++ PLD, LCD, density, ASA, ...).
  CoRE MOF 2019, record 7691378: ASR descriptor table for 14,142 structures (CSD-derived
    + SI); descriptors are public even where the CIF needs a CSD licence.

Independent units: CoRE 2019 lists the same MOF under several CSD refcodes
(e.g. RUBTAK, RUBTAK01..09 = UiO-66). We collapse to the 6-letter CSD refcode family
and use the family median PLD. CoRE 2024 lists one structure in up to three solvent
treatments (ASR/FSR/ION); we collapse on the MOFid-v1 string (one record per MOFid,
ASR preferred).

This is a GEOMETRIC pre-screen. A pore-limiting diameter in a window says nothing
about selectivity, flux, water stability under brine, membrane growth or defects.

Usage: python -I matdb_mof.py RAW_MOF_DIR OUT_JSON
"""
import datetime as dt
import json
import os
import sys

import numpy as np
import pandas as pd

# Ion and molecule sizes (diameters, Angstrom)
HYD = {"Li+": 7.64, "Na+": 7.16, "K+": 6.62, "Mg2+": 8.56, "Ca2+": 8.24}  # Nightingale 1959 (2 x hydrated radius)
BARE = {"Li+": 1.52, "Na+": 2.04, "K+": 2.76, "Mg2+": 1.44, "Ca2+": 2.00}  # Shannon 1976, CN 6 (2 x ionic radius)
WATER = 2.65  # kinetic diameter of water, Breck 1974
BANDS = [
    ("PLD < 2.65 A (below water kinetic diameter)", 0, WATER),
    ("2.65-7.64 A (water passes; hydrated Li+ must partly dehydrate)", WATER, HYD["Li+"]),
    ("7.64-8.56 A (between hydrated Li+ and hydrated Mg2+)", HYD["Li+"], HYD["Mg2+"]),
    ("PLD >= 8.56 A (both hydrated ions fit)", HYD["Mg2+"], 1e9),
]
SHORT = ["< 2.65 A", "2.65-7.64 A", "7.64-8.56 A", ">= 8.56 A"]


def band_counts(pld):
    pld = np.asarray(pld, float)
    out = []
    for (name, lo, hi), sh in zip(BANDS, SHORT):
        n = int(((pld >= lo) & (pld < hi)).sum())
        out.append({"band": name, "short": sh, "lo_A": lo, "hi_A": None if hi > 1e8 else hi,
                    "n": n, "pct": round(100 * n / len(pld), 2)})
    return out


def wilson(k, n, z=1.96):
    if n == 0:
        return [None, None]
    p = k / n
    den = 1 + z * z / n
    c = (p + z * z / (2 * n)) / den
    h = z * np.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / den
    return [round(100 * (c - h), 2), round(100 * (c + h), 2)]


def main(raw, out):
    rd = lambda f: pd.read_csv(os.path.join(raw, f), encoding="utf-8-sig", low_memory=False)  # noqa: E731
    # ---------- CoRE MOF 2019 ----------
    c19 = rd("core2019_2019-11-01-ASR-internal_14142.csv")
    c19["family"] = c19["filename"].str.extract(r"^([A-Z]{6})")[0]
    c19["family"] = c19["family"].fillna(c19["filename"])   # non-CSD names keep their own id
    fam19 = c19.groupby("family").agg(PLD=("PLD", "median"), LCD=("LCD", "median"),
                                      n_entries=("PLD", "size"),
                                      pld_min=("PLD", "min"), pld_max=("PLD", "max")).reset_index()
    # ---------- CoRE MOF 2024 (public SI, computation-ready) ----------
    parts = []
    for tag, f in (("ASR", "core2024_ASR_data_SI_20250204.csv"), ("FSR", "core2024_FSR_data_SI_20250204.csv"),
                   ("ION", "core2024_ION_data_SI_20250204.csv")):
        d = rd(f)
        d["treatment"] = tag
        parts.append(d)
    c24 = pd.concat(parts, ignore_index=True)
    c24["PLD"] = pd.to_numeric(c24["PLD (Å)"], errors="coerce")
    c24["LCD"] = pd.to_numeric(c24["LCD (Å)"], errors="coerce")
    c24["mofid_key"] = c24["mofid-v1"].astype(str).str.split(";").str[0].str.strip()
    c24["water_stab"] = pd.to_numeric(c24["Water_stability"], errors="coerce")
    order = {"ASR": 0, "FSR": 1, "ION": 2}
    c24["_o"] = c24["treatment"].map(order)
    u24 = c24.sort_values("_o").drop_duplicates("mofid_key").copy()
    # ---------- reference points ----------
    refs = []
    for fam, label in (("RUBTAK", "UiO-66"), ("WIZMAV", "UiO-67")):
        r = c19[c19.family == fam]
        if len(r):
            refs.append({"name": label, "csd_refcode_family": fam, "n_entries": int(len(r)),
                         "PLD_median_A": round(float(r.PLD.median()), 2),
                         "PLD_range_A": [round(float(r.PLD.min()), 2), round(float(r.PLD.max()), 2)],
                         "LCD_median_A": round(float(r.LCD.median()), 2), "source": "CoRE MOF 2019 ASR"})
    # (a CoRE 2024 SI entry named "MOF-801" has LCD 12.2 A, inconsistent with MOF-801's
    #  published ~5-7 A cages, so it is deliberately NOT used as a reference point)

    b19 = band_counts(fam19.PLD)
    b24 = band_counts(u24.PLD)
    allp = np.concatenate([fam19.PLD.values, u24.PLD.values])
    ball = band_counts(allp)
    win = (u24.PLD >= WATER) & (u24.PLD < HYD["Mg2+"])
    ws = u24.loc[win, "water_stab"]
    n_ws = int((ws >= 0.5).sum())

    # ---------- charts ----------
    edges = np.arange(2.0, 20.01, 0.25)

    def hist(v):
        v = np.clip(np.asarray(v, float), None, 19.99)
        h, _ = np.histogram(v, bins=edges)
        return [[round(float(edges[i] + 0.125), 3), int(h[i])] for i in range(len(h))]

    vl = [{"x": WATER, "text": "water 2.65 A"}, {"x": HYD["Li+"], "text": "hydrated Li+ 7.64 A"},
          {"x": HYD["Mg2+"], "text": "hydrated Mg2+ 8.56 A"}]
    uio = {r["name"]: r for r in refs}
    ann = [{"x": uio[k]["PLD_median_A"], "y": 0, "text": k} for k in ("UiO-66", "UiO-67") if k in uio]
    charts = [
        {"id": "pld-hist", "kind": "hist",
         "title": "Pore-limiting diameter of every known MOF in CoRE MOF",
         "subtitle": f"CoRE MOF 2019 ({len(fam19):,} unique CSD refcode families) and CoRE MOF 2024 public "
                     f"SI set ({len(u24):,} unique MOFids); 0.25 A bins; PLD >= 20 A folded into the last bin",
         "x": {"label": "Pore-limiting diameter (PLD)", "unit": "A", "scale": "linear"},
         "y": {"label": "Number of unique MOFs", "unit": "", "scale": "linear"},
         "series": [{"name": "CoRE MOF 2019 (ASR)", "color": "cyan", "points": hist(fam19.PLD)},
                    {"name": "CoRE MOF 2024 public SI", "color": "orange", "points": hist(u24.PLD)}],
         "vlines": vl, "annotations": ann,
         "caption": "Our computation on public descriptor tables (Zeo++ geometry computed by the CoRE MOF "
                    "authors). CoRE only includes frameworks with PLD >= 2.4 A, so the smallest bins are "
                    "cut by construction. Geometry only: no selectivity, stability or flux is implied."},
        {"id": "pld-bands", "kind": "bar",
         "title": "How many MOFs have windows in each ion-sieving band",
         "subtitle": "Bands set by water (2.65 A) and the hydrated diameters of Li+ (7.64 A) and Mg2+ (8.56 A)",
         "x": {"label": "Pore-limiting diameter band", "unit": "", "scale": "category"},
         "y": {"label": "Share of unique MOFs", "unit": "%", "scale": "linear"},
         "series": [{"name": "CoRE MOF 2019", "color": "cyan", "points": [[b["short"], b["pct"]] for b in b19]},
                    {"name": "CoRE MOF 2024 public SI", "color": "orange",
                     "points": [[b["short"], b["pct"]] for b in b24]}],
         "caption": "Our computation on public data. A window narrower than the hydrated ion means the ion "
                    "must shed water to pass; Mg2+ pays a much larger dehydration penalty than Li+, which is "
                    "the usual rationale for sub-nm MOF windows in Li/Mg separation. This is a hypothesis "
                    "for each MOF, not a prediction."},
    ]
    rng = np.random.default_rng(0)
    samp = fam19.sample(n=min(400, len(fam19)), random_state=0)
    charts.append({
        "id": "pld-lcd", "kind": "scatter",
        "title": "Window vs cavity: PLD against largest cavity diameter",
        "subtitle": "Random sample of 400 CoRE MOF 2019 refcode families, plus UiO-66 and UiO-67",
        "x": {"label": "Pore-limiting diameter (PLD)", "unit": "A", "scale": "linear"},
        "y": {"label": "Largest cavity diameter (LCD)", "unit": "A", "scale": "linear"},
        "series": [{"name": "CoRE MOF 2019 sample", "color": "grey",
                    "points": [[round(float(a), 2), round(float(b), 2)] for a, b in zip(samp.PLD, samp.LCD)]},
                   {"name": "UiO-66 / UiO-67 entries", "color": "orange",
                    "points": [[round(float(a), 2), round(float(b), 2)] for a, b in
                               c19[c19.family.isin(["RUBTAK", "WIZMAV"])][["PLD", "LCD"]].values]}],
        "vlines": vl,
        "caption": "Our computation on public data. Cage-and-window MOFs (LCD >> PLD) such as the UiO family "
                   "have narrow windows into larger cages; the window (PLD) is what sieves."})
    _ = rng

    lo, hi = WATER, HYD["Mg2+"]
    n_win19 = int(((fam19.PLD >= lo) & (fam19.PLD < hi)).sum())
    n_win24 = int(win.sum())
    n_sub_li = int(((fam19.PLD >= lo) & (fam19.PLD < HYD["Li+"])).sum())
    n_between = int(((fam19.PLD >= HYD["Li+"]) & (fam19.PLD < HYD["Mg2+"])).sum())
    pct_win19 = round(100 * n_win19 / len(fam19), 1)

    res = {
        "id": "mof-pore-screen",
        "tab": "materials",
        "material": "mof",
        "title": "Which known MOFs have pore windows sized for lithium sieving?",
        "question": "How many known MOFs have pore-limiting diameters in a range useful for separating "
                    "lithium from magnesium in brine?",
        "headline": {"value": f"{n_win19:,}", "unit": "MOFs",
                     "text": f"{n_win19:,} of {len(fam19):,} distinct known MOFs ({pct_win19:.0f}%) have pore windows "
                             f"wider than a water molecule (2.65 A) but narrower than a hydrated Mg2+ ion "
                             f"(8.56 A), the geometric range for ion sieving; only {n_between:,} sit in the "
                             f"narrow band between hydrated Li+ and Mg2+. Candidate chemistry is plentiful; "
                             f"making oriented, defect-free membranes is the open problem. Geometry only, "
                             f"not selectivity."},
        "evidence_level": "our computation on public data",
        "datasets": [
            {"name": "CoRE MOF 2024 public (SI) dataset v1.1", "url": "https://zenodo.org/records/15055758",
             "license": "CC-BY-4.0", "records": int(len(c24)), "bytes": int(sum(os.path.getsize(os.path.join(raw, f))
                                                                                for f in os.listdir(raw) if f.startswith("core2024_"))),
             "accessed": "2026-10-24",
             "notes": f"Computation-ready descriptor tables ASR ({(c24.treatment == 'ASR').sum()}), FSR "
                      f"({(c24.treatment == 'FSR').sum()}), ION ({(c24.treatment == 'ION').sum()}); "
                      f"{len(u24)} unique MOFid-v1 strings. Public release covers only the SI-derived part of "
                      "CoRE MOF 2024 (CSD-derived structures need a CSD licence). Includes ML-predicted "
                      "water stability by the CoRE authors."},
            {"name": "CoRE MOF 2019 dataset v1.1.4", "url": "https://zenodo.org/records/7691378",
             "license": "CC-BY-4.0", "records": int(len(c19)),
             "bytes": int(os.path.getsize(os.path.join(raw, "core2019_2019-11-01-ASR-internal_14142.csv"))),
             "accessed": "2026-10-24",
             "notes": f"ASR descriptor table, {len(c19):,} structures, collapsed to {len(fam19):,} CSD refcode "
                      "families (independent MOFs)."},
            {"name": "Ion sizes", "url": "https://doi.org/10.1021/j150579a011", "license": "citation",
             "records": 0, "bytes": 0, "accessed": "2026-10-24",
             "notes": "Hydrated diameters (2 x hydrated radius): Nightingale, J. Phys. Chem. 63, 1381 (1959): "
                      "Li+ 7.64, Na+ 7.16, K+ 6.62, Mg2+ 8.56, Ca2+ 8.24 A. Bare diameters (2 x ionic radius, "
                      "CN 6): Shannon, Acta Cryst. A32, 751 (1976), doi:10.1107/S0567739476001551: Li+ 1.52, "
                      "Mg2+ 1.44, Na+ 2.04, K+ 2.76 A. Water kinetic diameter 2.65 A: Breck, Zeolite "
                      "Molecular Sieves (1974)."},
        ],
        "compute": {"where": "MIT Engaging", "partitions": ["mit_quicktest"], "job_ids": [],
                    "cpu_hours": 0.0, "wall_minutes": 0.0, "peak_storage_gb": 0.01},
        "method": [
            "Downloaded the CoRE MOF 2024 public descriptor tables and the CoRE MOF 2019 ASR descriptor table "
            "from Zenodo onto MIT Engaging.",
            "Collapsed duplicates: CoRE 2019 to 6-letter CSD refcode families (median PLD per family); CoRE 2024 "
            "to unique MOFid-v1 strings (ASR record preferred over FSR and ION).",
            "Binned the pore-limiting diameter (PLD, the narrowest window along the best path through the "
            "framework) against water's kinetic diameter (2.65 A) and the hydrated diameters of Li+ (7.64 A) "
            "and Mg2+ (8.56 A).",
            "Located UiO-66 (refcode family RUBTAK) and UiO-67 (WIZMAV) as reference points.",
            "Wilson 95% intervals on shares; these describe the database, not all possible MOFs.",
        ],
        "charts": charts,
        "stats": {
            "core2019_structures": int(len(c19)), "core2019_unique_families": int(len(fam19)),
            "core2024_records": int(len(c24)), "core2024_unique_mofid": int(len(u24)),
            "bands_core2019": b19, "bands_core2024": b24, "bands_combined_possible_overlap": ball,
            "window_2p65_to_8p56": {
                "core2019": {"n": n_win19, "of": int(len(fam19)), "pct": pct_win19,
                             "ci95_pct": wilson(n_win19, len(fam19))},
                "core2024": {"n": n_win24, "of": int(len(u24)), "pct": round(100 * n_win24 / len(u24), 1),
                             "ci95_pct": wilson(n_win24, len(u24))}},
            "core2019_sub_hydrated_Li_2p65_to_7p64": n_sub_li,
            "core2019_between_hydrated_Li_and_Mg_7p64_to_8p56": n_between,
            "core2024_window_and_ml_water_stability_ge_0p5": {
                "n": n_ws, "of_window": n_win24, "with_prediction": int(ws.notna().sum()),
                "note": "Water_stability is an ML prediction published with CoRE MOF 2024, not a measurement."},
            "pld_median_A": {"core2019": round(float(fam19.PLD.median()), 2),
                             "core2024": round(float(u24.PLD.median()), 2)},
            "references": refs,
            "ion_diameters_A": {"hydrated_Nightingale1959": HYD, "bare_Shannon1976_CN6": BARE,
                                "water_kinetic_Breck1974": WATER},
        },
        "findings": [
            f"CoRE MOF 2019: {n_win19:,} of {len(fam19):,} independent MOFs ({pct_win19}%, 95% CI "
            f"{wilson(n_win19, len(fam19))[0]}-{wilson(n_win19, len(fam19))[1]}%) have PLD between 2.65 and 8.56 A.",
            f"{n_sub_li:,} of those have windows narrower than hydrated Li+ (2.65-7.64 A), the partial-"
            f"dehydration regime; only {n_between:,} fall in the narrow 7.64-8.56 A band between the hydrated Li+ "
            "and Mg2+ diameters.",
            f"CoRE MOF 2024 public SI set: {n_win24:,} of {len(u24):,} unique MOFs ({round(100 * n_win24 / len(u24), 1)}%) "
            "are in the same 2.65-8.56 A window.",
        ] + [f"{r['name']}: PLD {r['PLD_median_A']} A (LCD {r['LCD_median_A']} A) in {r['source']}"
             + (f", {r['n_entries']} entries, range {r['PLD_range_A'][0]}-{r['PLD_range_A'][1]} A" if "n_entries" in r else "")
             + "." for r in refs] + [
            f"The CoRE MOF 2024 authors' ML model predicts water stability >= 0.5 for {n_ws} of the {n_win24} "
            "in-window 2024 MOFs; that is a model output, not a measurement.",
        ],
        "limitations": [
            "Geometric pre-screen only. PLD from rigid-framework Zeo++ geometry; real frameworks flex, swell and "
            "breathe in water, and windows shift by tenths of an angstrom.",
            "PLD in a band does not imply Li/Mg selectivity: dehydration energetics, charge, functional groups "
            "and transport path all matter.",
            "Membrane performance is dominated by growth orientation, intergrowth and defects (missing linkers, "
            "grain boundaries), none of which are in these crystal-structure databases. These are exactly what "
            "an orbital process might change, and that is a hypothesis, not a result.",
            "CoRE only contains frameworks with PLD >= 2.4 A, so the 'below water' band is truncated by design.",
            "Refcode-family and MOFid de-duplication is approximate; CoRE 2019 and CoRE 2024 may share some "
            "MOFs, so their counts are reported separately rather than summed.",
            "Hydrated ion sizes are model-dependent (Nightingale's values are one standard set).",
        ],
        "future_big_data": [
            "Add QMOF and the licensed CSD-derived part of CoRE MOF 2024 (~40,800 structures in total) to "
            "widen the screen.",
            "Run molecular-dynamics ion-dehydration / transport screens on the in-window MOFs, then rank by "
            "predicted Li/Mg selectivity and water stability.",
            "Mine the membrane literature (OpenAlex) for reported Li/Mg selectivities of grown MOF membranes and "
            "join them to these descriptors.",
        ],
        "partners": [
            {"name": "CoRE MOF team (Chung group and co-authors)",
             "why": "Maintainers of the descriptor database this screen is built on; the full 2024 set needs "
                    "CSD-licensed structures.",
             "evidence": "Data source of this analysis (Zenodo 15055758, 7691378)."},
            {"name": "CCDC (Cambridge Structural Database)",
             "why": "Owner of most experimental MOF structures; the CSD-derived 32,500 CoRE 2024 entries are "
                    "not in the open release.",
             "evidence": "CoRE MOF 2024 Zenodo record: public release covers the SI subset only."},
            {"name": "NuMat Technologies",
             "why": "Commercial MOF manufacturing at scale, which a space-grown membrane would have to beat or "
                    "complement.",
             "evidence": "Not from this dataset; named as an industry MOF producer in the project brief."},
            {"name": "Lithium direct-lithium-extraction (DLE) companies, e.g. Lilac Solutions",
             "why": "End users of Li/Mg separation from brine.",
             "evidence": "Not from this dataset; the screen targets their separation problem. Lilac's published "
                         "approach is ion exchange, not MOF membranes."},
        ],
        "code": ["analysis/bigdata/matdb_mof.py", "cluster/bigdata/matdb-mof.sbatch"],
        "reproduce": [
            "sbatch cluster/bigdata/matdb-mof.sbatch   # downloads Zenodo CSVs and runs the screen",
            "python -I analysis/bigdata/matdb_mof.py bigdata/matdb/raw/mof data/results/bigdata/mof-pore-screen.json",
        ],
        "generated_at": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"),
    }
    json.dump(res, open(out, "w"), indent=1)
    print(json.dumps(res["headline"], indent=1))
    for f in res["findings"]:
        print("-", f)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
