#!/usr/bin/env python3
"""matdb A: how common is polymorphism in molecular crystals, and among FDA drugs?

Inputs (all built on MIT Engaging by the other matdb steps):
  work/cif_shards/*.parquet   our own parse of every COD CIF (matdb_cod_parse.py)
  work/cod_sql.parquet        COD's MySQL `data` table (flags + cross-check)
  work/cod_inchikeys.parquet  RDKit InChIKeys of COD's SMILES (matdb_cod_inchi.py)
  work/fda_ingredients.parquet  Orange Book ingredients -> PubChem (matdb_fda_pubchem.py)

Identity ("same compound"), as requested, conservative:
  normalised sum formula (Hill order, divided by the GCD of the counts) AND a shared
  normalised name (common or systematic; polymorph descriptors such as 'form II',
  'beta-polymorph', 'monoclinic', 'at 100 K' stripped). Entries are linked by union-find
  within a formula when they share any normalised name. Entries with no usable name stay
  singletons (cannot be matched, so cannot count as polymorphs).
Cross-check identity: InChIKey connectivity block of single-component COD SMILES.

Form ("same solid form"): two entries of one compound are the same form if their space
groups are equal (or a commonly mis-assigned pair, e.g. Cc/C2/c, P1/P-1) AND their volumes
per non-H atom, corrected to 293 K, agree within TOL (3%). Forms are connected components.
A compound is polymorphic if it has >= 2 forms. Volume thermal expansion is estimated
from the data (same compound, same space group, measured at different temperatures).

Usage: python -I matdb_cod_polymorph.py WORK_DIR OUT_JSON
"""
import datetime as dt
import glob
import json
import math
import os
import re
import sys
import unicodedata
from collections import Counter, defaultdict

import numpy as np
import pandas as pd

TOL = 0.03                 # 3% in volume per non-H atom after T correction
T_REF = 293.0
ORGANIC_EL = {"C", "H", "D", "N", "O", "S", "P", "F", "Cl", "Br", "I", "B", "Si", "Se"}
# commonly mis-assigned (missed-symmetry) pairs, plus the 11 enantiomorphic pairs (same structure,
# opposite hand, e.g. P3_121 / P3_221), are treated as the same space-group class
CONFUSABLE = {frozenset(p) for p in [(1, 2), (4, 11), (4, 14), (5, 12), (5, 15), (7, 13), (7, 14),
                                     (9, 15), (29, 57), (33, 62), (36, 63),
                                     (76, 78), (91, 95), (92, 96), (144, 145), (151, 153), (152, 154),
                                     (169, 170), (171, 172), (178, 179), (180, 181), (212, 213)]}
DTOL_PER_K = 0.5e-4        # extra tolerance per K of temperature gap (uncertainty in alpha_V)
SOHNCKE = set([1] + list(range(3, 6)) + list(range(16, 25)) + list(range(75, 81)) + list(range(89, 99))
              + list(range(143, 147)) + list(range(149, 156)) + list(range(168, 174))
              + list(range(177, 183)) + list(range(195, 200)) + list(range(207, 215)))
GREEK = {"α": "alpha", "β": "beta", "γ": "gamma", "δ": "delta", "ε": "epsilon", "ζ": "zeta",
         "η": "eta", "θ": "theta", "κ": "kappa", "λ": "lambda", "μ": "mu", "ω": "omega"}
GR = r"(?:alpha|beta|gamma|delta|epsilon|zeta|eta|theta)"
DESIG = r"(?:[ivx]{1,5}|\d{1,2}|[a-h]|" + GR + r")"
FORMW = r"(?:polymorphs?|forms?|modifications?|phases?|mod\.)"
PATS = [
    re.compile(r"\b" + FORMW + r"\s*[-(]?\s*" + DESIG + r"\b\)?"),
    re.compile(r"\b" + DESIG + r"[\s-]*" + FORMW + r"\b"),
    re.compile(r"\b(?:triclinic|monoclinic|orthorhombic|tetragonal|trigonal|hexagonal|rhombohedral|cubic)\b"),
    re.compile(r"\b(?:low|high|room|ambient|variable)[\s-]*(?:temperature|pressure)\b"),
    re.compile(r"\b(?:at\s+)?\d+(?:\.\d+)?\s*k\b"),
    re.compile(r"[,;(\s]+" + DESIG + r"\)?\s*$"),
    re.compile(r"\b(?:polymorphs?|polymorphic|forms?|phases?|modifications?|new|novel|metastable|"
               r"stable|redetermination|redetermined|crystal|structure|of|the|at|a)\b"),
]
BAD_NAMES = re.compile(r"^(?:unknown|none|na|titlecompound|compound\d*[a-z]?|complex\d*[a-z]?|"
                       r"ligand\d*|product\d*|\d+[a-z]?)$")


def norm_name(s):
    if not isinstance(s, str) or not s.strip():
        return None
    s = s.lower()
    for g, w in GREEK.items():
        s = s.replace(g, w)
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()
    s = s.replace("~", "")             # CIF sub/superscript markers
    for _ in range(2):
        for p in PATS:
            s = p.sub(" ", s)
    s = re.sub(r"[^a-z0-9]", "", s)
    if len(s) < 4 or BAD_NAMES.match(s):
        return None
    return s


_tok = re.compile(r"^([A-Z][a-z]?)(\d+(?:\.\d+)?)?$")


def parse_formula(s):
    if not isinstance(s, str):
        return None
    s = s.strip().strip("-").strip().strip("'\"")
    if not s:
        return None
    el = Counter()
    for t in s.split():
        m = _tok.match(t)
        if not m:
            return None
        el[m.group(1)] += float(m.group(2)) if m.group(2) else 1.0
    return dict(el) if el else None


def formula_key(el):
    cnt = {k: round(v, 3) for k, v in el.items()}
    if all(abs(v - round(v)) < 1e-3 for v in cnt.values()):
        iv = {k: int(round(v)) for k, v in cnt.items()}
        g = 0
        for v in iv.values():
            g = math.gcd(g, v)
        g = max(g, 1)
        cnt = {k: v // g for k, v in iv.items()}
    order = (["C", "H", "D"] if "C" in cnt else []) + sorted(k for k in cnt if not ("C" in cnt and k in "CHD"))
    return "".join(f"{k}{'' if cnt[k] == 1 else cnt[k]}" for k in order if k in cnt)


class DSU:
    def __init__(self, n):
        self.p = list(range(n))

    def find(self, x):
        while self.p[x] != x:
            self.p[x] = self.p[self.p[x]]
            x = self.p[x]
        return x

    def union(self, a, b):
        a, b = self.find(a), self.find(b)
        if a != b:
            self.p[max(a, b)] = min(a, b)


def wilson(k, n, z=1.96):
    if n == 0:
        return [None, None]
    p = k / n
    den = 1 + z * z / n
    c = (p + z * z / (2 * n)) / den
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / den
    return [round(100 * (c - h), 1), round(100 * (c + h), 1)]


# ---------------------------------------------------------------- load
def load(work):
    sql = pd.read_parquet(f"{work}/cod_sql.parquet")
    shards = sorted(glob.glob(f"{work}/cif_shards/cod_cif_*.parquet"))
    if shards:
        cif = pd.concat([pd.read_parquet(f) for f in shards], ignore_index=True)
        src = "cif"
    else:
        cif = None
        src = "sql"
    return sql, cif, src, len(shards)


def build_entries(sql, cif):
    s = sql.rename(columns={"sgNumber": "sql_sg", "vol": "sql_vol", "Z": "sql_Z", "formula": "sql_formula",
                            "commonname": "sql_common", "chemname": "sql_systematic",
                            "celltemp": "sql_cellT", "diffrtemp": "sql_diffrT"})
    s = s.rename(columns={k: f"sql_{k}" for k in ("a", "b", "c", "alpha", "beta", "gamma")})
    keep = ["file", "sql_sg", "sql_vol", "sql_Z", "sql_formula", "sql_common", "sql_systematic", "sql_cellT",
            "sql_diffrT", "cellpressure", "diffrpressure", "method", "status", "duplicateof", "onhold", "doi",
            "title", "year", "flags", "sg", "sql_a", "sql_b", "sql_c", "sql_alpha", "sql_beta", "sql_gamma"]
    s = s[keep]
    if cif is not None:
        e = cif.merge(s, on="file", how="left")
        e["in_sql"] = e["sql_sg"].notna() | e["sql_formula"].notna()
    else:
        e = s.copy()
        e["formula_sum"] = e["sql_formula"]
        e["name_common"] = e["sql_common"]
        e["name_systematic"] = e["sql_systematic"]
        e["sg_number"] = e["sql_sg"]
        e["vol"] = e["sql_vol"]
        e["Z"] = e["sql_Z"]
        e["cell_T"] = e["sql_cellT"]
        e["diffrn_T"] = e["sql_diffrT"]
        e["cell_P"] = np.nan
        e["diffrn_P"] = np.nan
        e["sg_hm"] = e["sg"]
        for k in ("a", "b", "c", "alpha", "beta", "gamma"):
            e[k] = e[f"sql_{k}"]
        e["in_sql"] = True
    # fall back to SQL values where our CIF parse is missing
    e["sg_number"] = e["sg_number"].fillna(e["sql_sg"])
    e["vol"] = e["vol"].fillna(e["sql_vol"])
    e["Z"] = e["Z"].fillna(e["sql_Z"])
    e["formula_sum"] = e["formula_sum"].fillna(e["sql_formula"])
    e["sg_hm"] = e["sg_hm"].fillna(e["sg"])
    for k in ("a", "b", "c", "alpha", "beta", "gamma"):
        e[k] = e[k].fillna(e[f"sql_{k}"])
    return e


def reduced_cells(e):
    """Niggli-reduced primitive cell (gemmi) -> sorted lengths and |cos| of angles, for the cell-shape rule."""
    import gemmi
    out = np.full((len(e), 6), np.nan)
    for n, (a, b, c, al, be, ga, hm) in enumerate(zip(e["a"], e["b"], e["c"], e["alpha"], e["beta"], e["gamma"],
                                                      e["sg_hm"])):
        try:
            if not (a > 0 and b > 0 and c > 0 and al > 0 and be > 0 and ga > 0):
                continue
            cen = str(hm).strip()[:1].upper() if isinstance(hm, str) and hm.strip() else "P"
            if cen not in "PABCIFR":
                cen = "P"
            if cen == "R" and abs(a - c) < 1e-3 and abs(al - 90) > 1e-3:
                cen = "P"          # rhombohedral axes are already primitive
            gv = gemmi.GruberVector(gemmi.UnitCell(a, b, c, al, be, ga), cen, True)
            gv.niggli_reduce()
            p = gv.cell_parameters()
            out[n] = [p[0], p[1], p[2], abs(math.cos(math.radians(p[3]))),
                      abs(math.cos(math.radians(p[4]))), abs(math.cos(math.radians(p[5])))]
        except Exception:  # noqa: BLE001
            continue
    for i, k in enumerate(["rl1", "rl2", "rl3", "rc1", "rc2", "rc3"]):
        e[k] = out[:, i]
    return e


def annotate(e):
    el = e["formula_sum"].map(parse_formula)
    e["el"] = el
    e["fkey"] = el.map(lambda d: formula_key(d) if d else None)
    e["n_nonH"] = el.map(lambda d: sum(v for k, v in d.items() if k not in ("H", "D")) if d else np.nan)
    e["organic"] = el.map(lambda d: bool(d) and "C" in d and ("H" in d or "D" in d) and set(d) <= ORGANIC_EL)
    e["int_formula"] = el.map(lambda d: bool(d) and all(abs(v - round(v)) < 1e-3 for v in d.values()))
    txt = (e["title"].fillna("") + " " + e["name_common"].fillna("").astype(str) + " "
           + e["name_systematic"].fillna("").astype(str))
    e["pressure_study"] = txt.str.contains(r"pressure|\bGPa\b|\bkbar\b|compressi|piezo", case=False, regex=True)
    T = e["cell_T"].where((e["cell_T"] > 1) & (e["cell_T"] < 1000))
    T = T.fillna(e["diffrn_T"].where((e["diffrn_T"] > 1) & (e["diffrn_T"] < 1000)))
    T = T.fillna(e["sql_cellT"].where((e["sql_cellT"] > 1) & (e["sql_cellT"] < 1000)))
    e["T_known"] = T.notna()
    e["T"] = T.fillna(T_REF)
    P = pd.concat([e.get("cell_P"), e.get("diffrn_P"), e["cellpressure"], e["diffrpressure"]], axis=1).max(axis=1)
    # CIF pressure is in kPa, but some depositors put GPa values in that field (e.g. 0.25-1.9 for a
    # compression series). Any recorded pressure outside 80-120 kPa is treated as non-ambient.
    e["high_pressure"] = P.notna() & ~P.between(80.0, 120.0)
    e["v_atom"] = e["vol"] / (e["Z"] * e["n_nonH"])
    e["vol_ok"] = e["v_atom"].between(10.0, 30.0)   # organic crystals: ~18 A^3 per non-H atom
    e["sg_number"] = pd.to_numeric(e["sg_number"], errors="coerce")
    nc = e["name_common"].map(norm_name)
    ns = e["name_systematic"].map(norm_name)
    sc = e["sql_common"].map(norm_name)
    ss = e["sql_systematic"].map(norm_name)
    e["names"] = [sorted({x for x in t if isinstance(x, str)}) for t in zip(nc, ns, sc, ss)]
    return e


def base_filter(e):
    reasons = Counter()
    m = pd.Series(True, index=e.index)
    for name, cond in [
        ("retracted or COD 'errors' status", e["status"].isin(["retracted", "errors"])),
        ("theoretical (computed) structure", e["method"].eq("theoretical")),
        ("flagged duplicate of another COD entry", e["duplicateof"].notna()),
        ("on hold (prepublication)", e["onhold"].notna()),
        ("no parsable sum formula", e["fkey"].isna()),
        ("no valid space group number", ~e["sg_number"].between(1, 230)),
        ("non-ambient pressure recorded (outside 80-120 kPa)", e["high_pressure"]),
        ("pressure study (title/name mentions pressure, GPa, kbar)", e["pressure_study"]),
        ("non-integer formula (partial occupancy / disorder)", ~e["int_formula"]),
    ]:
        reasons[name] = int((m & cond).sum())
        m &= ~cond
    return m, reasons


# ---------------------------------------------------------------- identity + forms
def compounds_by_name(e):
    idx = e.index.to_numpy()
    pos = {k: i for i, k in enumerate(idx)}
    d = DSU(len(idx))
    first = {}
    for k, fk, names in zip(idx, e["fkey"], e["names"]):
        for nm in names:
            key = (fk, nm)
            if key in first:
                d.union(pos[k], pos[first[key]])
            else:
                first[key] = k
    return pd.Series([d.find(pos[k]) for k in idx], index=idx)


def same_sg_class(a, b):
    return a == b or frozenset((int(a), int(b))) in CONFUSABLE


def forms_of(sub, alpha, tol=TOL, use_volume=True, use_cell=False):
    """sub: DataFrame of one compound's entries -> list of form labels."""
    if use_cell:
        RL = np.log(sub[["rl1", "rl2", "rl3"]].to_numpy()) + (alpha / 3) * (T_REF - sub["T"].to_numpy())[:, None]
        RC = sub[["rc1", "rc2", "rc3"]].to_numpy()
    n = len(sub)
    sg = sub["sg_number"].to_numpy()
    Tv = sub["T"].to_numpy()
    lv = np.log(sub["v_atom"].to_numpy()) + alpha * (T_REF - Tv)
    vok = (sub["vol_ok"] & sub["T_known"]).to_numpy()   # volume splits only if T is known
    d = DSU(n)
    for i in range(n):
        for j in range(i + 1, n):
            if not same_sg_class(sg[i], sg[j]):
                continue
            if use_volume and vok[i] and vok[j] and abs(lv[i] - lv[j]) > tol + DTOL_PER_K * abs(Tv[i] - Tv[j]):
                r = math.exp(abs(lv[i] - lv[j]))
                if not any(abs(r - k) < tol * k for k in (2, 3, 4, 1.5)):   # integer ratio = Z/formula error
                    continue
            if use_cell and vok[i] and vok[j] and np.isfinite(RL[i]).all() and np.isfinite(RL[j]).all():
                if (np.abs(RL[i] - RL[j]).max() > tol + DTOL_PER_K / 3 * abs(Tv[i] - Tv[j])
                        or np.abs(RC[i] - RC[j]).max() > 0.035):
                    continue
            d.union(i, j)
    return [d.find(i) for i in range(n)]


def call_compound(sub, alpha, tol=TOL, use_cell=False):
    lab = forms_of(sub, alpha, tol, use_cell=use_cell)
    nforms = len(set(lab))
    sgs = sub["sg_number"].astype(int).to_numpy()
    T = sub["T"].to_numpy()
    form_sg = defaultdict(set)
    form_T = defaultdict(list)
    for l, s, t in zip(lab, sgs, T):
        form_sg[l].add(s)
        form_T[l].append(t)
    by_sg = len({min(v) for v in form_sg.values()}) >= 2
    chir = {l: any(s in SOHNCKE for s in v) for l, v in form_sg.items()}
    only_chiral_split = nforms >= 2 and len(set(chir.values())) == 2 and all(
        sum(1 for l in chir if chir[l] == c) == 1 for c in (True, False))
    close_T = False
    ls = list(form_T)
    for i in range(len(ls)):
        for j in range(i + 1, len(ls)):
            if min(abs(a - b) for a in form_T[ls[i]] for b in form_T[ls[j]]) <= 50:
                close_T = True
    return {"n_entries": len(sub), "n_forms": nforms, "n_forms_eff": 1 if only_chiral_split else nforms,
            "split_by_sg": by_sg,
            "chirality_only": bool(only_chiral_split), "forms_at_similar_T": close_T,
            "sgs": sorted(set(sgs.tolist())),
            "n_pubs": int(sub["doi"].fillna(sub["title"]).fillna(sub["file"].astype(str)).nunique())}


def estimate_alpha(e, comp):
    """Median volumetric expansion from same-compound, same-space-group pairs at different T."""
    slopes = []
    g = e[e["vol_ok"] & e["T_known"]].groupby(comp)
    for _, sub in g:
        if len(sub) < 2 or len(sub) > 60:
            continue
        best = None
        sg = sub["sg_number"].to_numpy()
        lv = np.log(sub["v_atom"].to_numpy())
        T = sub["T"].to_numpy()
        for i in range(len(sub)):
            for j in range(i + 1, len(sub)):
                if sg[i] != sg[j] or abs(T[i] - T[j]) < 40 or abs(lv[i] - lv[j]) > 0.06:
                    continue
                s = (lv[i] - lv[j]) / (T[i] - T[j])
                if best is None or abs(T[i] - T[j]) > best[0]:
                    best = (abs(T[i] - T[j]), s)
        if best:
            slopes.append(best[1])        # one pair per compound (independent units)
    s = np.array(slopes)
    return float(np.median(s)), [float(np.percentile(s, 25)), float(np.percentile(s, 75))], len(s)


def summarise(calls, label):
    c = pd.DataFrame(calls)
    multi = c[c.n_entries >= 2]
    multi_pub = c[c.n_pubs >= 2]
    k = int((multi.n_forms_eff >= 2).sum())
    k_all = int((c.n_forms_eff >= 2).sum())
    kp = int((multi_pub.n_forms_eff >= 2).sum())
    return {
        "label": label, "compounds": int(len(c)), "compounds_with_2plus_entries": int(len(multi)),
        "polymorphic": k_all,
        "share_of_all_compounds_pct": round(100 * k_all / max(1, len(c)), 2),
        "share_of_multi_entry_compounds_pct": round(100 * k / max(1, len(multi)), 1),
        "ci95_multi_entry_pct": wilson(k, len(multi)),
        "compounds_with_2plus_publications": int(len(multi_pub)),
        "share_of_multi_publication_compounds_pct": round(100 * kp / max(1, len(multi_pub)), 1),
        "ci95_multi_publication_pct": wilson(kp, len(multi_pub)),
        "split_by_space_group": int(((c.n_forms_eff >= 2) & c.split_by_sg).sum()),
        "excluded_racemate_vs_enantiopure_only": int(((c.n_forms >= 2) & c.chirality_only).sum()),
        "share_incl_racemate_splits_pct": round(100 * int((multi.n_forms >= 2).sum()) / max(1, len(multi)), 1),
        "forms_seen_at_similar_T": int(((c.n_forms_eff >= 2) & c.forms_at_similar_T).sum()),
        "n_forms_hist_multi_entry": {str(kk): int(v) for kk, v in
                                     multi.n_forms_eff.clip(upper=5).value_counts().sort_index().items()},
    }


# ---------------------------------------------------------------- main
def main(work, out):
    t0 = dt.datetime.now(dt.timezone.utc)
    sql, cif, src, nshards = load(work)
    e = build_entries(sql, cif)
    n_total = len(e)
    e = annotate(e)
    qc = {}
    if src == "cif":
        both = e[e["in_sql"]]
        qc = {
            "cif_parsed": int(n_total), "matched_to_sql": int(len(both)),
            "uncompressed_cif_bytes": int(cif["bytes"].sum()),
            "parse_modes": {k: int(v) for k, v in cif["parse_mode"].value_counts().items()},
            "sg_number_agree_pct": round(100 * float((both["sg_number"] == both["sql_sg"]).mean()), 2),
            "volume_agree_0p1pct_pct": round(100 * float(((both["vol"] - both["sql_vol"]).abs()
                                                         <= 1e-3 * both["sql_vol"]).mean()), 2),
            "formula_agree_pct": round(100 * float((both["formula_sum"].map(parse_formula).map(
                lambda d: formula_key(d) if d else None) == both["sql_formula"].map(parse_formula).map(
                lambda d: formula_key(d) if d else None)).mean()), 2),
        }
    keep, reasons = base_filter(e)
    allk = e[keep].copy()
    org = reduced_cells(allk[allk["organic"]].copy())
    # generic / class names (same normalised name on >= 3 different formulas) are not identities
    nf = defaultdict(set)
    for fk, names in zip(org["fkey"], org["names"]):
        for nm in names:
            nf[nm].add(fk)
    generic = {nm for nm, fs in nf.items() if len(fs) >= 3}
    org["names"] = org["names"].map(lambda ns: [x for x in ns if x not in generic])
    # identity (primary: formula + name)
    org["cmp_name"] = compounds_by_name(org)
    # cross-check identity (structure): InChIKey connectivity, single-component only
    ik_path = f"{work}/cod_inchikeys.parquet"
    ik = pd.read_parquet(ik_path) if os.path.exists(ik_path) else None
    if ik is not None:
        org = org.merge(ik[["file", "n_comp", "main_key", "comp_keys", "ok"]], on="file", how="left")
        org.index = range(len(org))
        org["cmp_struct"] = np.where((org["ok"] == True) & (org["n_comp"] == 1),  # noqa: E712
                                     org["main_key"].str[:14] + "|" + org["fkey"].astype(str), None)
    named = org["names"].map(len) > 0
    alpha, alpha_iqr, alpha_n = estimate_alpha(org, org["cmp_name"])

    def run(groupcol, frame, tol=TOL, use_cell=False):
        calls = {}
        for key, sub in frame.groupby(groupcol):
            if len(sub) == 1:
                calls[key] = {"n_entries": 1, "n_forms": 1, "n_forms_eff": 1, "split_by_sg": False, "chirality_only": False,
                              "forms_at_similar_T": False, "sgs": [int(sub["sg_number"].iloc[0])], "n_pubs": 1}
            else:
                calls[key] = call_compound(sub, alpha, tol, use_cell)
        return calls

    calls_name = run("cmp_name", org)
    s_name = summarise(list(calls_name.values()), "formula + name (primary)")
    s_name_named = summarise([calls_name[k] for k in org.loc[named, "cmp_name"].unique()],
                             "formula + name, named entries only")
    sens = {}
    for tol in (0.02, 0.05):
        sens[f"tol_{int(tol * 100)}pct"] = summarise(list(run("cmp_name", org, tol).values()),
                                                     f"formula + name, tol {int(tol * 100)}%")
    sens["cell_shape_rule"] = summarise(list(run("cmp_name", org, use_cell=True).values()),
                                        "formula + name, + Niggli reduced-cell shape")
    # strict: space group only (ignore volume)
    strict = {}
    for key, sub in org.groupby("cmp_name"):
        lab = forms_of(sub, alpha, use_volume=False) if len(sub) > 1 else [0]
        strict[key] = len(set(lab))
    st = pd.Series(strict)
    multi_keys = [k for k, v in calls_name.items() if v["n_entries"] >= 2]
    sens["space_group_only"] = {
        "polymorphic": int((st >= 2).sum()),
        "share_of_multi_entry_compounds_pct": round(100 * float((st[multi_keys] >= 2).mean()), 1)}
    s_struct = None
    calls_struct = {}
    if ik is not None:
        sf = org[org["cmp_struct"].notna()]
        calls_struct = run("cmp_struct", sf)
        s_struct = summarise(list(calls_struct.values()), "InChIKey connectivity (cross-check)")
    # liberal upper bound: formula only
    calls_formula = run("fkey", org)
    s_formula = summarise(list(calls_formula.values()), "formula only (liberal upper bound; merges isomers)")

    # ------------------------------------------------ FDA
    fda_path = f"{work}/fda_ingredients.parquet"
    fda_res, famous, strat = None, [], {}
    if os.path.exists(fda_path) and ik is not None:
        fda = pd.read_parquet(fda_path)
        fda["k14"] = fda["moiety_key"].str[:14]
        fda["n_ing"] = fda["ingredient"].map(norm_name)
        fda["n_moi"] = fda["moiety_name"].map(norm_name)
        # metal complexes (e.g. copper histidinate, Gd contrast agents, Pt drugs) would map onto their organic
        # ligand's crystals, which are not the drug's solid form -> excluded. Simple Na/K/Ca/Mg/Li salts are kept
        # and matched through the neutral active moiety.
        ok_el = ORGANIC_EL | {"Na", "K", "Ca", "Mg", "Li"}
        fda["metal_complex"] = fda["formula"].fillna("").map(
            lambda f: bool(set(re.findall(r"[A-Z][a-z]?", f)) - ok_el))
        n_metal = int((fda["types"].notna() & fda["metal_complex"]).sum())
        drugs = fda[fda["types"].notna() & fda["k14"].notna() & ~fda["metal_complex"]]   # in the Orange Book
        drug_k14 = set(drugs["k14"])
        org["k14"] = org["main_key"].str[:14]
        neat = org[(org["n_comp"] == 1) & org["k14"].isin(drug_k14)]
        # name-based backup for entries without a usable SMILES
        name_to_k14 = {}
        for _, r in drugs.iterrows():
            for nm in (r["n_ing"], r["n_moi"]):
                if nm:
                    name_to_k14.setdefault(nm, r["k14"])
        nosmi = org[org["ok"] != True]  # noqa: E712
        hits = []
        for i, names in zip(nosmi.index, nosmi["names"]):
            for nm in names:
                if nm in name_to_k14:
                    hits.append((i, name_to_k14[nm]))
                    break
        org["drug_k14"] = None
        org.loc[neat.index, "drug_k14"] = neat["k14"]
        for i, k in hits:
            org.at[i, "drug_k14"] = k
        # formula consistency for name-matched entries: must equal the formula of other matched entries
        dm = org[org["drug_k14"].notna()]
        mode_f = dm.groupby("drug_k14")["fkey"].agg(lambda s: s.value_counts().index[0])
        bad = dm["fkey"] != dm["drug_k14"].map(mode_f)
        org.loc[dm.index[bad.values], "drug_k14"] = None
        dm = org[org["drug_k14"].notna()]
        dcalls = {k: (call_compound(sub, alpha) if len(sub) > 1 else
                      {"n_entries": 1, "n_forms": 1, "n_forms_eff": 1, "split_by_sg": False, "chirality_only": False,
                       "forms_at_similar_T": False, "sgs": [int(sub["sg_number"].iloc[0])], "n_pubs": 1})
                  for k, sub in dm.groupby("drug_k14")}
        s_drug = summarise(list(dcalls.values()), "FDA active moieties (structure match)")
        s_drug_cell = summarise([call_compound(sub, alpha, use_cell=True) if len(sub) > 1 else dcalls[k]
                                 for k, sub in dm.groupby("drug_k14")], "FDA active moieties, + cell-shape rule")
        multicomp = org[(org["n_comp"] > 1) & org["comp_keys"].notna()]
        mc_k = Counter()
        for ck in multicomp["comp_keys"]:
            for k in {x[:14] for x in ck.split(";")} & drug_k14:
                mc_k[k] += 1
        n_drug_moieties = len(drug_k14)
        k2name = {}
        dn = drugs.assign(_self=(drugs["inchikey"].str[:14] != drugs["k14"]).astype(int),
                          _len=drugs["ingredient"].str.len())
        for _, r in dn.sort_values(["_self", "_len"]).iterrows():   # prefer the neutral moiety's own entry
            k2name.setdefault(r["k14"], (r["title"] or r["moiety_name"] or r["ingredient"]))
        top = sorted(((k2name.get(k, k), v) for k, v in dcalls.items()),
                     key=lambda kv: (-kv[1]["n_forms_eff"], -kv[1]["n_entries"]))[:20]
        fda_top = [{"drug": str(n).lower(), "forms_in_cod": v["n_forms_eff"], "cod_entries": v["n_entries"],
                    "space_groups": v["sgs"]} for n, v in top]
        fda_res = {
            "orange_book_ingredient_strings": int(fda["types"].notna().sum()),
            "with_pubchem_structure": int(drugs["ingredient"].nunique()),
            "excluded_metal_complex_ingredients": n_metal,
            "unique_active_moieties": n_drug_moieties,
            "moieties_with_neat_cod_structure": int(len(dcalls)),
            "moieties_with_salt_solvate_or_cocrystal_in_cod": int(len(mc_k)),
            "name_matched_entries_without_smiles": int(len(hits)),
            "summary": s_drug, "summary_cell_shape_rule": s_drug_cell, "most_forms_in_cod": fda_top,
        }
        # stratified comparison by number of entries (controls for study intensity)
        others = {k: v for k, v in calls_struct.items() if k.split("|")[0] not in drug_k14}
        bins = [(2, 2, "2"), (3, 4, "3-4"), (5, 9, "5-9"), (10, 10 ** 6, "10+")]
        for lo, hi, lab in bins:
            dd = [v for v in dcalls.values() if lo <= v["n_entries"] <= hi]
            oo = [v for v in others.values() if lo <= v["n_entries"] <= hi]
            strat[lab] = {
                "drugs_n": len(dd), "drugs_pct": round(100 * sum(v["n_forms_eff"] >= 2 for v in dd) / max(1, len(dd)), 1),
                "drugs_ci": wilson(sum(v["n_forms_eff"] >= 2 for v in dd), len(dd)),
                "others_n": len(oo), "others_pct": round(100 * sum(v["n_forms_eff"] >= 2 for v in oo) / max(1, len(oo)), 1),
                "others_ci": wilson(sum(v["n_forms_eff"] >= 2 for v in oo), len(oo))}
        # famous cases (validation)
        val = fda[fda["is_validation"]]
        lit = {"RITONAVIR": (2, "Forms I and II; Bauer et al., Pharm. Res. 18, 859 (2001)"),
               "CARBAMAZEPINE": (5, "anhydrous forms I-V; Form V: Arlin et al., Chem. Commun. 47, 7074 (2011)"),
               "ACETAMINOPHEN": (3, "forms I-III at ambient pressure (paracetamol)"),
               "SULFATHIAZOLE": (5, "forms I-V"),
               "ROY": (10, ">= 10 forms; Yu, Acc. Chem. Res. 43, 1257 (2010); more reported since")}
        for _, r in val.iterrows():
            k14 = r["k14"]
            sub_s = org[(org["k14"] == k14) & (org["n_comp"] == 1)] if isinstance(k14, str) else org.iloc[0:0]
            extra_names = {"ACETAMINOPHEN": ["paracetamol", "N-(4-hydroxyphenyl)acetamide", "4-acetamidophenol"],
                           "ROY": ["5-methyl-2-[(2-nitrophenyl)amino]thiophene-3-carbonitrile",
                                   "5-methyl-2-[(2-nitrophenyl)amino]-3-thiophenecarbonitrile"]}
            nmset = ({r["n_ing"], r["n_moi"]} | {norm_name(x) for x in extra_names.get(r["ingredient"], [])}) - {None}
            sub_n = org[org["names"].map(lambda ns: bool(set(ns) & nmset))]
            cn = sub_n["cmp_name"].value_counts()
            res_s = call_compound(sub_s, alpha) if len(sub_s) > 1 else {"n_entries": len(sub_s), "n_forms": len(sub_s)}
            res_c = call_compound(sub_s, alpha, use_cell=True) if len(sub_s) > 1 else {"n_forms": len(sub_s)}
            # name-based: the compound group(s) matched by name
            grp = org[org["cmp_name"].isin(cn.index)] if len(cn) else org.iloc[0:0]
            res_n = call_compound(grp, alpha) if len(grp) > 1 else {"n_entries": len(grp), "n_forms": len(grp)}
            ent = sub_s if len(sub_s) else grp
            famous.append({
                "name": {"ACETAMINOPHEN": "paracetamol", "ROY": "ROY"}.get(r["ingredient"], r["ingredient"].lower()),
                "inchikey": r["moiety_key"], "known_forms_literature": lit[r["ingredient"]][0],
                "literature_note": lit[r["ingredient"]][1],
                "cod_entries_structure_match": int(len(sub_s)), "forms_structure_match": int(res_s.get("n_forms_eff", res_s.get("n_forms", 0))),
                "forms_structure_match_cell_rule": int(res_c.get("n_forms_eff", res_c.get("n_forms", 0))),
                "cod_entries_name_match": int(len(grp)), "forms_name_match": int(res_n.get("n_forms_eff", res_n.get("n_forms", 0))),
                "space_groups": sorted({int(x) for x in ent["sg_number"]}),
                "cod_ids": sorted(int(x) for x in ent["file"])[:40],
                "temperatures_K": sorted({round(float(x)) for x in ent["T"]}),
            })

    # ------------------------------------------------ charts
    def hist_pct(s):
        h = s["n_forms_hist_multi_entry"]
        tot = sum(h.values())
        return [[("5+" if k == "5" else k), round(100 * v / tot, 2)] for k, v in sorted(h.items())]

    charts = [{
        "id": "forms-per-compound", "kind": "bar",
        "title": "How many distinct solid forms each compound has",
        "subtitle": "Organic molecular crystals in COD with at least two crystal-structure entries",
        "x": {"label": "Distinct forms found", "unit": "", "scale": "category"},
        "y": {"label": "Share of compounds", "unit": "%", "scale": "linear"},
        "series": [{"name": f"All organic compounds (n = {s_name['compounds_with_2plus_entries']:,})",
                    "color": "cyan", "points": hist_pct(s_name)}]
        + ([{"name": f"FDA active ingredients (n = {fda_res['summary']['compounds_with_2plus_entries']:,})",
             "color": "orange", "points": hist_pct(fda_res["summary"])}] if fda_res else []),
        "caption": "Our computation on public data. A form = same space group (allowing commonly mis-assigned "
                   "pairs) and volume per non-H atom within 3% after correcting to 293 K. Forms seen in COD are a "
                   "lower bound on forms that exist: most compounds are only crystallised once or twice."}]
    bars = [["All organic, formula+name", s_name["share_of_multi_entry_compounds_pct"]]]
    if s_struct:
        bars.append(["All organic, structure key", s_struct["share_of_multi_entry_compounds_pct"]])
    if fda_res:
        bars.append(["FDA active ingredients", fda_res["summary"]["share_of_multi_entry_compounds_pct"]])
    charts.append({
        "id": "polymorph-share", "kind": "bar",
        "title": "Share of compounds with two or more solid forms",
        "subtitle": "Among compounds with at least two COD entries",
        "x": {"label": "Population", "unit": "", "scale": "category"},
        "y": {"label": "Polymorphic", "unit": "%", "scale": "linear"},
        "series": [{"name": "Polymorphic (>= 2 forms)", "color": "orange", "points": bars}],
        "caption": "Our computation on public data. Drugs are studied far more intensively than typical "
                   "compounds (polymorph screens, regulatory filings), so the gap reflects attention as well as "
                   "chemistry; see the stratified chart."})
    if strat:
        charts.append({
            "id": "polymorph-share-by-entries", "kind": "bar",
            "title": "Polymorph share rises with how often a compound has been crystallised",
            "subtitle": "Compounds stratified by number of COD entries; structure-key identity",
            "x": {"label": "COD entries per compound", "unit": "", "scale": "category"},
            "y": {"label": "Polymorphic", "unit": "%", "scale": "linear"},
            "series": [{"name": "FDA active ingredients", "color": "orange",
                        "points": [[k, v["drugs_pct"]] for k, v in strat.items()]},
                       {"name": "Other organic compounds", "color": "cyan",
                        "points": [[k, v["others_pct"]] for k, v in strat.items()]}],
            "caption": "Our computation on public data. Comparing like with like (same number of determinations) "
                       "separates 'drugs are more polymorphic' from 'drugs are studied more'. Sample sizes and "
                       "95% intervals are in stats.stratified."})
    if famous:
        charts.append({
            "id": "famous-cases", "kind": "hbar",
            "title": "Famous polymorphic compounds: forms in COD vs forms known",
            "subtitle": "Validation of the heuristic on textbook cases",
            "x": {"label": "Number of forms", "unit": "", "scale": "linear"},
            "y": {"label": "Compound", "unit": "forms", "scale": "category"},
            "series": [{"name": "Forms found by our heuristic in COD", "color": "orange",
                        "points": [[f["name"], max(f["forms_structure_match"], f["forms_name_match"])] for f in famous]},
                       {"name": "Forms known in the literature", "color": "grey",
                        "points": [[f["name"], f["known_forms_literature"]] for f in famous]}],
            "caption": "COD is an open subset of all published structures (the CSD has far more), so missing forms "
                       "are expected. Literature counts are approximate and grow over time."})

    # ------------------------------------------------ assemble
    headline_drug = fda_res["summary"] if fda_res else None
    if headline_drug:
        hv = headline_drug["share_of_multi_entry_compounds_pct"]
        htxt = (f"Of the {headline_drug['compounds_with_2plus_entries']} FDA-approved drugs crystallised at least twice "
                f"in the open Crystallography Open Database, {headline_drug['polymorphic']} ({hv:.0f}%) show two or more "
                f"distinct solid forms, vs {s_name['share_of_multi_entry_compounds_pct']:.0f}% for organic compounds in "
                f"general. A lower bound: the open database misses many known forms.")
    else:
        hv = s_name["share_of_multi_entry_compounds_pct"]
        htxt = (f"{hv:.0f}% of organic compounds crystallised at least twice in COD show two or more distinct "
                f"solid forms.")
    findings = [
        (f"COD archive: {n_total:,} CIFs parsed by our job array" if src == "cif" else
         f"COD MySQL data table (COD's own parse of each CIF; our CIF parse not yet merged): {n_total:,} entries")
        + f"; {len(allk):,} pass the quality filters, of which {len(org):,} are organic molecular crystals.",
        f"Formula + name identity groups these into {s_name['compounds']:,} compounds; "
        f"{s_name['compounds_with_2plus_entries']:,} have >= 2 entries and {s_name['polymorphic']:,} of those are "
        f"polymorphic ({s_name['share_of_multi_entry_compounds_pct']}%, 95% CI {s_name['ci95_multi_entry_pct'][0]}-"
        f"{s_name['ci95_multi_entry_pct'][1]}%).",
        f"Volumetric thermal expansion estimated from {alpha_n:,} same-compound same-space-group pairs: median "
        f"{alpha * 1e4:.2f}e-4 per K (IQR {alpha_iqr[0] * 1e4:.2f}-{alpha_iqr[1] * 1e4:.2f}e-4).",
    ]
    if s_struct:
        findings.append(f"Structure-key cross-check (InChIKey connectivity, single-component entries): "
                        f"{s_struct['share_of_multi_entry_compounds_pct']}% of {s_struct['compounds_with_2plus_entries']:,} "
                        f"multiply-crystallised compounds are polymorphic.")
    findings.append(f"Liberal upper bound (formula only, which merges isomers): "
                    f"{s_formula['share_of_multi_entry_compounds_pct']}% - shows why name or structure matching matters.")
    if fda_res:
        sd = fda_res["summary"]
        findings.append(f"FDA Orange Book: {fda_res['unique_active_moieties']:,} unique active moieties with a PubChem "
                        f"structure; {fda_res['moieties_with_neat_cod_structure']:,} have a neat (single-component) "
                        f"crystal structure in COD; {sd['compounds_with_2plus_entries']} have >= 2 entries and "
                        f"{sd['polymorphic']} of those show >= 2 forms ({sd['share_of_multi_entry_compounds_pct']}%, 95% CI "
                        f"{sd['ci95_multi_entry_pct'][0]}-{sd['ci95_multi_entry_pct'][1]}%).")
        findings.append(f"{fda_res['moieties_with_salt_solvate_or_cocrystal_in_cod']:,} FDA moieties also appear in COD as "
                        "salts, solvates, hydrates or cocrystals - further solid forms not counted as polymorphs here.")
    for f in famous:
        findings.append(f"{f['name']}: {f['cod_entries_structure_match']} neat COD entries by structure "
                        f"({f['forms_structure_match']} forms), {f['cod_entries_name_match']} by name "
                        f"({f['forms_name_match']} forms); literature: {f['known_forms_literature']} ({f['literature_note']}).")

    res = {
        "id": "cod-polymorphs", "tab": "materials", "material": "small",
        "title": "How common is polymorphism? Every crystal in the Crystallography Open Database",
        "question": "How often does the same molecule crystallise in more than one solid form, and is that common "
                    "among FDA-approved drugs?",
        "headline": {"value": f"{hv:.0f}", "unit": "%", "text": htxt},
        "evidence_level": "our computation on public data",
        "datasets": [
            {"name": "Crystallography Open Database (COD), bulk archive cod-cifs-mysql.zip",
             "url": "https://www.crystallography.net/archives/", "license": "CC0 (COD data are public domain)",
             "records": int(n_total), "bytes": 27107247440, "accessed": "2026-10-24",
             "notes": "Release of 2025-02-09 (SVN r297631), md5-verified. All CIFs parsed by our job array"
                      + (f" ({qc['uncompressed_cif_bytes'] / 1e9:.1f} GB uncompressed)" if qc else "")
                      + "; COD's MySQL data table from the same archive used for duplicate/retraction flags and "
                        "cross-checks. The live COD has grown since this release; we used the latest bulk archive."},
            {"name": "FDA Orange Book (products.txt)", "url": "https://www.fda.gov/media/76860/download",
             "license": "public domain (US government)", "records": 48864,
             "bytes": 1099838, "accessed": "2026-10-24",
             "notes": "Monthly data file (Oct 2026 edition); RX, OTC and discontinued products; ingredients split on ';'."},
            {"name": "PubChem PUG-REST (name -> structure)", "url": "https://pubchem.ncbi.nlm.nih.gov/",
             "license": "public", "records": int(fda_res["with_pubchem_structure"]) if fda_res else 0, "bytes": 0,
             "accessed": "2026-10-24", "notes": "Used only to get a structure (InChIKey) for each Orange Book ingredient."},
        ],
        "compute": {"where": "MIT Engaging", "partitions": ["mit_data_transfer", "mit_normal", "mit_quicktest"],
                    "job_ids": [], "cpu_hours": 0.0, "wall_minutes": 0.0, "peak_storage_gb": 28.0},
        "method": [
            "Downloaded COD's single-file bulk archive (27.1 GB zip, 521,901 CIFs + MySQL dump) on mit_data_transfer; "
            "md5 verified. Chosen over the per-file rsync tree to avoid putting ~520k files on shared scratch.",
            ("Parsed every CIF straight from the zip with a 32-task job array (gemmi CIF parser, regex fallback): "
             "formula, names, space group, cell, Z, temperatures, pressures, COD id; COD's SQL table fills gaps and "
             "is used as a cross-check (agreement rates in stats.parse_qc)." if src == "cif" else
             "PRELIMINARY: fields taken from COD's MySQL data table (COD's own CIF parse) while our CIF job array runs."),
            "Filtered out retracted / error-flagged, theoretical, duplicate and on-hold entries, entries with a "
            "recorded non-ambient pressure or a pressure study in the title, and non-integer (partial-occupancy) "
            "formulas; kept organic molecular crystals (C and H plus N, O, S, P, halogens, B, Si, Se only).",
            "Same compound = same GCD-reduced Hill formula AND a shared normalised name (polymorph descriptors stripped); "
            "union-find within each formula. Cross-check: RDKit InChIKey connectivity block of COD's SMILES "
            "(single-component entries).",
            f"Same form = same space group (or a commonly mis-assigned or enantiomorphic pair such as Cc/C2/c or "
            f"P3121/P3221) AND volume per non-H atom within {int(TOL * 100)}% (+0.005% per K of temperature gap) "
            f"after correcting to 293 K with the data-derived expansion coefficient ({alpha * 1e4:.2f}e-4 /K); volume "
            f"splits need recorded temperatures and are ignored at ~integer volume ratios (Z errors). Polymorphic = "
            f">= 2 forms, excluding cases whose only split is racemate vs enantiopure (one Sohncke, one non-Sohncke "
            f"form).",
            "FDA: Orange Book ingredients -> PubChem structure -> InChIKey of the active moiety; matched to neat COD "
            "entries by InChIKey connectivity (and by name + formula for entries without SMILES).",
            "Validated on ritonavir, carbamazepine, paracetamol, sulfathiazole and ROY; sensitivity to tolerance, "
            "space-group-only rule and identity definition reported in stats.",
        ],
        "charts": charts,
        "stats": {
            "entries_total": int(n_total), "entries_after_filters": int(len(allk)), "organic_entries": int(len(org)),
            "organic_entries_with_name": int(named.sum()), "generic_names_dropped": len(generic), "filter_removed": dict(reasons),
            "parse_qc": qc, "alpha_V_per_K": {"median": alpha, "iqr": alpha_iqr, "n_compounds": alpha_n},
            "tolerance": TOL, "primary": s_name, "primary_named_only": s_name_named,
            "structure_crosscheck": s_struct, "formula_only_upper_bound": s_formula, "sensitivity": sens,
            "fda": fda_res, "stratified_by_entries": strat, "famous_cases": famous,
        },
        "findings": findings,
        "limitations": [
            "COD is open but incomplete: the CSD holds ~1.3M+ structures vs COD's ~0.5M, and most pharmaceutical "
            "polymorph data sit in the CSD or in company files. Counts here are lower bounds.",
            "Most compounds were crystallised only once, so 'no second form seen' is not evidence of no polymorphism.",
            "Solvates, hydrates and salts have different formulas and are deliberately NOT counted as polymorphs; "
            "a mis-entered formula (e.g. solvent omitted) can still create a false polymorph.",
            "Name normalisation can fail both ways: different authors' systematic names for one compound do not "
            "merge (undercount), and an over-generic name could merge isomers (guarded by requiring the same formula).",
            "Racemate vs enantiopure crystals of one constitution can look like two forms (flagged in stats as "
            "chirality_only); temperature-induced phase transitions count as distinct forms (flagged as forms not "
            "seen at similar temperatures).",
            "Space-group mis-assignment and pseudo-symmetry (Z' > 1 superstructures) can split or merge forms.",
            "The FDA comparison is confounded by attention: drugs are screened for polymorphs on purpose. The "
            "stratified chart compares compounds with the same number of determinations, which helps but does not "
            "remove that bias.",
            "The Orange Book also lists amino acids, sugars and polyols (e.g. glycine, dextrose, mannitol) as active "
            "ingredients; they are included. Salts are matched through their largest organic component, so a metal "
            "salt maps to its organic ligand.",
            "Repeat determinations of a compound are often published because something new (a new form) was found, "
            "which inflates polymorph shares among multiply-crystallised compounds; compare with deliberate screens: "
            "Stahly, Cryst. Growth Des. 7, 1007 (2007) reports roughly half of ~245 industrially screened compounds as "
            "polymorphic (published result).",
            "This is about solid forms on Earth; it says nothing direct about microgravity crystallisation.",
        ],
        "future_big_data": [
            "Repeat with the CSD (licensed, ~1.3M structures) and its curated polymorph and refcode-family fields.",
            "Use full structure comparison (COMPACK / PXRD similarity) instead of cell volume to separate forms.",
            "Join with FDA labels / DailyMed and patent data to find drugs whose approved form is metastable.",
            "Mine the literature for polymorph screens and solid-form patents to estimate true form counts.",
        ],
        "partners": [
            {"name": "CCDC (Cambridge Structural Database)",
             "why": "Holds the most complete record of drug crystal forms; would turn these lower bounds into "
                    "near-complete counts.",
             "evidence": "COD (open) covers well under half of published organic structures; several famous forms are "
                         "missing from COD (see famous_cases)."},
            {"name": "Pharmaceutical solid-form teams (polymorph screening groups at drug makers and CROs)",
             "why": "They decide which form is developed and would be the users of a form-controlled orbital process.",
             "evidence": "Polymorphism is common among multiply-crystallised FDA active ingredients in this analysis."},
        ],
        "code": ["analysis/bigdata/matdb_fetch.py", "analysis/bigdata/matdb_cod_sql.py",
                 "analysis/bigdata/matdb_cod_parse.py", "analysis/bigdata/matdb_cod_inchi.py",
                 "analysis/bigdata/matdb_fda_pubchem.py", "analysis/bigdata/matdb_cod_polymorph.py",
                 "cluster/bigdata/matdb-fetch.sbatch", "cluster/bigdata/matdb-prep.sbatch",
                 "cluster/bigdata/matdb-cod-parse.sbatch", "cluster/bigdata/matdb-fda.sbatch",
                 "cluster/bigdata/matdb-analyse.sbatch"],
        "reproduce": [
            "sbatch cluster/bigdata/matdb-fetch.sbatch      # COD zip + Orange Book",
            "sbatch cluster/bigdata/matdb-prep.sbatch       # SQL table -> parquet, SMILES -> InChIKeys",
            "sbatch cluster/bigdata/matdb-fda.sbatch        # Orange Book -> PubChem",
            "sbatch cluster/bigdata/matdb-cod-parse.sbatch  # 32-task CIF parse array",
            "sbatch cluster/bigdata/matdb-analyse.sbatch    # this analysis",
        ],
        "generated_at": t0.isoformat(timespec="seconds"),
    }
    os.makedirs(os.path.dirname(out) or ".", exist_ok=True)
    json.dump(res, open(out, "w"), indent=1, default=lambda o: o.item() if hasattr(o, "item") else str(o))
    # inspection tables (stay on the cluster)
    cn = pd.DataFrame([{"cmp": k, **v} for k, v in calls_name.items()])
    cn.to_parquet(f"{work}/compounds_name.parquet", index=False)
    org.drop(columns=["el"]).to_parquet(f"{work}/organic_entries.parquet", index=False)
    print(json.dumps(res["headline"], indent=1))
    for f in findings:
        print("-", f)
    print(json.dumps({"sens": sens, "qc": qc, "filters": dict(reasons)}, indent=1))


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
