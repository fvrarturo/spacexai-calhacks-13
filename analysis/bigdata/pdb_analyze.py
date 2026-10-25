"""Matched comparison of space-grown vs Earth-grown PDB crystals of the same protein.

Usage:
    python -I analysis/bigdata/pdb_analyze.py --work WORK/analysis \
        --sifts RAW/sifts/pdb_chain_uniprot.tsv.gz --out-json data/results/bigdata/pdb-microgravity.json \
        --out-csv data/results/bigdata/pdb-microgravity-entries.csv [--provenance provenance.json]

Inputs come from pdb_classify.py (entries.parquet, candidates.csv) and the manual verdicts in
pdb_review_labels.py. The unit of independence is the protein = the set of UniProt accessions of an
entry (SIFTS), falling back to the set of polymer sequence hashes when an entry has no UniProt mapping.

Per protein with >= 1 space-grown and >= 1 Earth-grown X-ray entry:
  (a) delta_all = best space resolution - best ground resolution (A; negative = space better)
  (b) delta_era = same, ground restricted to depositions within +/-3 years of the best space entry
  (c) space_best = the protein's best-resolution entry is space-grown
Medians and the share in (c) get 95% bootstrap CIs over proteins (10,000 resamples), deltas a
Wilcoxon signed-rank test, and all three a within-protein label-permutation null: entries are
exchangeable under "no microgravity effect", so we shuffle which n_s entries of each protein are
called "space" and recompute. That null corrects for "best of many ground entries" automatically.
"""
from __future__ import annotations

import argparse
import datetime as dt
import importlib.util
import json
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats as st

RNG = np.random.default_rng(20261024)
ERA_DAYS = 3 * 365.25
PLATFORMS = ["Shuttle", "Mir", "ISS", "Other", "Unknown"]
PCOLOR = {"Shuttle": "orange", "Mir": "violet", "ISS": "cyan", "Other": "green", "Unknown": "grey"}


def load_labels(path: Path) -> dict:
    spec = importlib.util.spec_from_file_location("pdb_review_labels", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.LABELS, getattr(mod, "PLATFORM", {}), getattr(mod, "NOTES", {}), getattr(mod, "KEYWORD_TIER", set())


def sifts_keys(path: str) -> dict:
    s = pd.read_csv(path, sep="\t", comment="#", usecols=["PDB", "SP_PRIMARY"], dtype=str)
    s["PDB"] = s.PDB.str.upper()
    return s.groupby("PDB").SP_PRIMARY.apply(lambda x: "|".join(sorted(set(x)))).to_dict()


def boot_median(x, n=10000):
    x = np.asarray(x, float)
    if len(x) == 0:
        return [None, None]
    idx = RNG.integers(0, len(x), (n, len(x)))
    m = np.median(x[idx], axis=1)
    return [float(np.percentile(m, 2.5)), float(np.percentile(m, 97.5))]


def boot_mean(x, n=10000):
    x = np.asarray(x, float)
    if len(x) == 0:
        return [None, None]
    idx = RNG.integers(0, len(x), (n, len(x)))
    m = x[idx].mean(axis=1)
    return [float(np.percentile(m, 2.5)), float(np.percentile(m, 97.5))]


def r3(x):
    return None if x is None or (isinstance(x, float) and np.isnan(x)) else round(float(x), 3)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--work", required=True)
    ap.add_argument("--sifts", required=True)
    ap.add_argument("--labels", default=str(Path(__file__).with_name("pdb_review_labels.py")))
    ap.add_argument("--out-json", required=True)
    ap.add_argument("--out-csv", required=True)
    ap.add_argument("--meta", default=None, help="JSON with provenance/compute info to merge into result")
    ap.add_argument("--nperm", type=int, default=2000)
    ap.add_argument("--strict", action="store_true", help="drop keyword-tier space entries (sensitivity)")
    a = ap.parse_args()
    work = Path(a.work)

    ent = pd.read_parquet(work / "entries.parquet")
    cand = pd.read_csv(work / "candidates.csv", dtype={"entry_id": str})
    labels, plat_over, notes, kw_tier = load_labels(Path(a.labels))

    # ---- final labels -------------------------------------------------------------------
    cand["label"] = cand.auto_label
    cand.loc[cand.entry_id.isin(labels), "label"] = cand.entry_id.map(labels)
    cand["platform"] = cand.platform_auto
    cand.loc[cand.entry_id.isin(plat_over), "platform"] = cand.entry_id.map(plat_over)
    reviewed = set(cand.entry_id)  # every candidate was read (see pdb_review_labels.py docstring)
    cand.assign(final_label=cand.label, note=cand.entry_id.map(notes).fillna("")).drop(
        columns=["polymer_entities"]).to_csv(work / "candidates_final.csv", index=False)
    lab = dict(zip(cand.entry_id, cand.label))
    ent["label"] = ent.entry_id.map(lab).fillna("none")
    ent["platform"] = ent.entry_id.map(dict(zip(cand.entry_id, cand.platform)))
    ent["keyword_tier"] = ent.entry_id.isin(kw_tier)
    ent["in_census"] = ent.label.isin(["space", "mixed"])
    strict = a.strict
    ent["is_space"] = (ent.label == "space") & ~(strict & ent.keyword_tier)
    # anything that might be space-grown is kept out of the Earth pool; explicit ground controls stay in
    ent["excluded_from_ground"] = ent.label.isin(["space", "mixed", "context_only", "unclear", "simulated", "noncrystal"])

    # ---- precision / recall of the automatic rule against the hand-checked verdicts ----------
    truth = cand.label.isin(["space", "mixed"])
    auto = cand.auto_label == "space"
    rs = np.random.default_rng(40)
    samp = cand[auto].iloc[rs.choice(int(auto.sum()), size=min(40, int(auto.sum())), replace=False)]
    prec = {"n_candidates_any_vocabulary": int(len(cand)), "n_true_in_candidates": int(truth.sum()),
            "precision_any_vocabulary_hit": r3(truth.mean()),
            "auto_rule_flagged": int(auto.sum()), "auto_rule_correct": int((auto & truth).sum()),
            "auto_rule_precision": r3((auto & truth).sum() / max(auto.sum(), 1)),
            "auto_rule_recall_vs_final": r3((auto & truth).sum() / max(truth.sum(), 1)),
            "n_sample": int(len(samp)), "n_correct": int(samp.label.isin(["space", "mixed"]).sum()),
            "sample_ids": " ".join(sorted(samp.entry_id)),
            "false_positive_causes": "MIR = multiple isomorphous replacement phasing (17 of the auto rule's errors), "
                                     "LMS = sulfamoyl-adenosine ligand, 'orbital mixing plate', crystal size 'in space'",
            "missed_by_auto_rule": "space-grown entries saying so only in the title/keywords/citation, a typo "
                                   "('microgavity'), or flight labels without the word microgravity"}

    ent["xray"] = ent.methods.eq("X-RAY DIFFRACTION")
    ent["res"] = ent.res_refine.where(ent.res_refine.notna() & (ent.res_refine > 0), ent.res_reflns)
    ent["dep"] = pd.to_datetime(ent.deposit_date, errors="coerce")

    # ---- protein keys -----------------------------------------------------------------------
    sk = sifts_keys(a.sifts)
    pe = ent.polymer_entities.map(json.loads)
    unp_cif = pe.map(lambda L: "|".join(sorted({u for e in L for u in e["unp"]})))
    seqk = pe.map(lambda L: "SEQ:" + "|".join(sorted({e["seq_md5"] for e in L if e["seq_md5"]})))
    ent["key_sifts"] = ent.entry_id.map(sk)
    ent["key"] = ent.key_sifts.where(ent.key_sifts.notna() & (ent.key_sifts != ""), unp_cif)
    ent["key_type"] = np.where(ent.key_sifts.notna(), "uniprot_sifts", np.where(unp_cif != "", "uniprot_cif", "sequence"))
    ent.loc[ent.key == "", "key"] = seqk[ent.key == ""]
    ent["n_acc"] = ent.key.map(lambda k: 0 if k.startswith("SEQ:") else len(k.split("|")))
    ent["single_entity"] = (ent.n_polymer_entities == 1) & (ent.n_acc == 1)
    ent["name"] = pe.map(lambda L: "; ".join(sorted({(e["description"] or "?")[:60] for e in L}))[:120])
    ent["organism"] = pe.map(lambda L: next((e["organism"] for e in L if e.get("organism")), None))

    xr = ent[ent.xray & ent.res.notna() & (ent.res > 0) & (ent.res < 10)].copy()
    space = ent[ent.is_space]
    space_x = xr[xr.is_space]
    ground = xr[~xr.excluded_from_ground]
    gby = {k: g for k, g in ground.groupby("key")}

    # ---- per-protein comparison --------------------------------------------------------------
    rows = []
    for key, S in space_x.groupby("key"):
        G = gby.get(key)
        best_s = S.loc[S.res.idxmin()]
        r = {"key": key, "key_type": best_s.key_type, "single_entity": bool(S.single_entity.all()),
             "name": best_s["name"], "organism": best_s.organism, "n_space": len(S),
             "space_entries": " ".join(sorted(S.entry_id)), "best_space_entry": best_s.entry_id,
             "best_space_res": float(best_s.res), "best_space_dep": best_s.deposit_date,
             "platforms": ",".join(sorted(set(S.platform.fillna("Unknown")))),
             "space_rfree": best_s.r_free, "space_wilson": best_s.wilson_b, "n_ground": 0}
        if G is not None and len(G):
            bg = G.loc[G.res.idxmin()]
            r.update(n_ground=len(G), best_ground_entry=bg.entry_id, best_ground_res=float(bg.res),
                     best_ground_dep=bg.deposit_date, delta_all=float(best_s.res - bg.res),
                     space_best=bool(best_s.res < bg.res), tie=bool(best_s.res == bg.res),
                     ground_rfree=bg.r_free, ground_wilson=bg.wilson_b,
                     ground_median_res=float(G.res.median()))
            Ge = G[(G.dep - best_s.dep).abs().dt.days <= ERA_DAYS]
            if len(Ge):
                be = Ge.loc[Ge.res.idxmin()]
                r.update(n_ground_era=len(Ge), best_ground_era_entry=be.entry_id, best_ground_era_res=float(be.res),
                         delta_era=float(best_s.res - be.res), space_best_era=bool(best_s.res < be.res))
            # same-study pairs: space and ground entries sharing a primary citation (DOI, else PubMed id,
            # else citation title). One difference per study (best vs best), then the median over the
            # protein's studies, so the protein stays the unit.
            def ckey(df):
                return df.cit_doi.fillna(df.cit_pubmed).fillna(df.cit_title.str.lower().str.strip())
            sk, gk = ckey(S), ckey(G)
            studies = sorted(set(sk.dropna()) & set(gk.dropna()))
            ds, pairs = [], []
            for c in studies:
                Ss, Gs = S[sk == c], G[gk == c]
                bs2, bg2 = Ss.loc[Ss.res.idxmin()], Gs.loc[Gs.res.idxmin()]
                ds.append(float(bs2.res - bg2.res))
                pairs.append(f"{bs2.entry_id}-{bg2.entry_id}")
            if ds:
                r.update(n_same_studies=len(ds), same_study_pairs=" ".join(pairs),
                         delta_same_study=float(np.median(ds)))
            r["_G"] = G.res.to_numpy()
            r["_Gdep"] = G.dep.to_numpy()
        r["_S"] = S.res.to_numpy()
        r["_Sdep"] = S.dep.to_numpy()
        rows.append(r)
    P = pd.DataFrame(rows)
    M = P[P.n_ground > 0].copy()

    def summarize(D, col):
        x = D[col].dropna().to_numpy()
        if len(x) == 0:
            return {"n_proteins": 0}
        out = {"n_proteins": int(len(x)), "median": r3(np.median(x)), "median_ci95": [r3(v) for v in boot_median(x)],
               "mean": r3(x.mean()), "share_space_better": r3((x < 0).mean()), "share_equal": r3((x == 0).mean())}
        if len(x) >= 6 and np.any(x != 0):
            w = st.wilcoxon(x, zero_method="wilcox")
            out["wilcoxon_p_two_sided"] = float(w.pvalue)
        return out

    # permutation null: within each protein shuffle which entries are "space"
    def perm_null(D, era=False, nperm=a.nperm):
        meds, shares = [], []
        items = []
        for _, r in D.iterrows():
            if not isinstance(r.get("_G"), np.ndarray):
                continue
            allres = np.concatenate([r._S, r._G])
            alldep = np.concatenate([r._Sdep, r._Gdep])
            items.append((allres, alldep, len(r._S)))
        for _ in range(nperm):
            d, sb = [], []
            for allres, alldep, ns in items:
                perm = RNG.permutation(len(allres))
                si, gi = perm[:ns], perm[ns:]
                s_best = si[np.argmin(allres[si])]
                g = gi
                if era:
                    g = gi[np.abs((alldep[gi] - alldep[s_best]).astype("timedelta64[D]").astype(float)) <= ERA_DAYS]
                    if len(g) == 0:
                        continue
                dd = allres[s_best] - allres[g].min()
                d.append(dd)
                sb.append(dd < 0)
            meds.append(np.median(d))
            shares.append(np.mean(sb))
        return np.array(meds), np.array(shares)

    res_stats = {}
    for name, D in [("all_proteins", M), ("single_entity_uniprot", M[M.single_entity & (M.key_type != "sequence")])]:
        block = {"delta_all_time": summarize(D, "delta_all"), "delta_era_pm3y": summarize(D, "delta_era")}
        for col in ["space_best", "space_best_era"]:
            x = D[col].dropna().astype(float).to_numpy()
            block[col] = {"n_proteins": int(len(x)), "share": r3(x.mean()) if len(x) else None,
                          "share_ci95": [r3(v) for v in boot_mean(x)] if len(x) else None}
        nm, ns_ = perm_null(D)
        em, es_ = perm_null(D, era=True)
        obs_m, obs_s = np.median(D.delta_all.dropna()), D.space_best.dropna().mean()
        obs_em = np.median(D.delta_era.dropna()) if D.delta_era.notna().any() else np.nan
        obs_es = D.space_best_era.dropna().astype(float).mean() if D.space_best_era.notna().any() else np.nan
        block["permutation_null"] = {
            "n_perm": int(len(nm)),
            "null_median_delta_all": r3(np.median(nm)), "null_median_delta_all_95": [r3(np.percentile(nm, 2.5)), r3(np.percentile(nm, 97.5))],
            "p_delta_all_lower": float((np.sum(nm <= obs_m) + 1) / (len(nm) + 1)),
            "null_share_space_best": r3(np.mean(ns_)), "null_share_space_best_95": [r3(np.percentile(ns_, 2.5)), r3(np.percentile(ns_, 97.5))],
            "p_share_space_best_higher": float((np.sum(ns_ >= obs_s) + 1) / (len(ns_) + 1)),
            "null_median_delta_era": r3(np.median(em)), "null_median_delta_era_95": [r3(np.percentile(em, 2.5)), r3(np.percentile(em, 97.5))],
            "p_delta_era_lower": float((np.sum(em <= obs_em) + 1) / (len(em) + 1)),
            "null_share_space_best_era": r3(np.mean(es_)),
            "p_share_space_best_era_higher": float((np.sum(es_ >= obs_es) + 1) / (len(es_) + 1)),
        }
        block["same_study_delta"] = summarize(D, "delta_same_study")
        res_stats[name] = block

    # secondary metrics (paired best-space vs best-ground entries)
    sec = {}
    for m_, sc, gc in [("r_free", "space_rfree", "ground_rfree"), ("wilson_b", "space_wilson", "ground_wilson")]:
        d = (M[sc] - M[gc]).dropna().to_numpy()
        sec[m_] = {"n_proteins": int(len(d)), "coverage": r3(len(d) / max(len(M), 1)), "median_space_minus_ground": r3(np.median(d)) if len(d) else None,
                   "median_ci95": [r3(v) for v in boot_median(d)] if len(d) else None}

    # ---- census ------------------------------------------------------------------------------
    sp = ent[ent.in_census].copy()
    sp["year"] = sp.dep.dt.year
    sp["platform"] = sp.platform.fillna("Unknown")
    census_year = sp.groupby(["year", "platform"]).size().unstack(fill_value=0)
    years = list(range(int(sp.year.min()), int(sp.year.max()) + 1)) if len(sp) else []
    census_year = census_year.reindex(years, fill_value=0)
    cand_by_id = cand.set_index("entry_id")
    sp_c = cand_by_id.loc[sp.entry_id]
    orgs = pd.Series([o for s in sp_c.orgs.fillna("") for o in s.split(",") if o]).value_counts()
    progs = pd.Series([o for s in sp_c.programs.fillna("") for o in s.split(",") if o]).value_counts()
    # first authors and synchrotrons as partner evidence
    first_auth = sp.authors.fillna("").map(lambda s: s.split(";")[0].strip()).value_counts()
    all_auth = pd.Series([x.strip() for s in sp.authors.fillna("") for x in s.split(";") if x.strip()]).value_counts()
    synch = sp.synchrotron_site.dropna().str.split(r" \|\| ").explode().value_counts()

    # partner evidence: entries (not mentions) whose own text names each organisation / its hardware
    txt = (sp_c.grow_text.fillna("") + " | " + sp_c.ctx_text.fillna("")).str.upper()
    pm_rx = {"JAXA / NASDA / Kibo / JEM / JCB": r"JAXA|NASDA|KIBO|\bJEM\b|JAPANESE EXPERIMENT MODULE|\bJCB\b",
             "NASA / Shuttle mission named": r"NASA|SHUTTLE|\bSTS-?\d|SPACEHAB|IML|USML|\bLMS\b|MSFC",
             "ESA / APCF / PCDF": r"\bESA\b|EUROPEAN SPACE|APCF|PCDF",
             "Granada GCB / GCF": r"GRANADA|\bGCB\b|\bGCF\b", "ISS named": r"\bISS|SPACE STATION|KIBO|PCDF"}
    partner_mentions = {k: int(txt.str.contains(v, regex=True).sum()) for k, v in pm_rx.items()}
    gm = sp.grow_method.fillna("").str.upper() + " " + sp.grow_details.fillna("").str.upper()
    cd = gm.str.contains(r"COUNTER|LIQUID DIFFUSION|CAPILLAR|GEL-TUBE|DIALYSIS|FREE.INTERFACE", regex=True)
    recent = sp.year >= 2010
    method_mix = {"n_since_2010": int(recent.sum()), "n_counter_or_liquid_diffusion_since_2010": int((cd & recent).sum()),
                  "n_before_2010": int((~recent).sum()), "n_counter_or_liquid_diffusion_before_2010": int((cd & ~recent).sum())}
    fpath = work / "funding_space_agencies.json"
    fund = json.load(open(fpath)) if fpath.exists() else {}
    census_ids = set(sp.entry_id)
    space_fund = {k: sorted(set(v) & census_ids) for k, v in fund.items()}

    # ---- entries table -----------------------------------------------------------------------
    keymap = P.set_index("key")
    rows = []
    for _, e in sp.sort_values("dep").iterrows():
        k = keymap.loc[e.key] if e.key in keymap.index else None
        c = cand_by_id.loc[e.entry_id]
        rows.append({
            "entry_id": e.entry_id, "deposit_date": e.deposit_date, "platform": e.platform,
            "programs": c.programs if isinstance(c.programs, str) else "",
            "orgs": c.orgs if isinstance(c.orgs, str) else "",
            "method": e.methods, "resolution_A": r3(e.res), "r_free": r3(e.r_free), "wilson_b": r3(e.wilson_b),
            "protein": e["name"], "organism": e.organism, "match_key": e.key, "key_type": e.key_type,
            "single_entity": bool(e.single_entity),
            "n_ground_xray_same_protein": int(k.n_ground) if k is not None else 0,
            "best_ground_entry": k.get("best_ground_entry") if k is not None else None,
            "best_ground_res_A": r3(k.get("best_ground_res")) if k is not None else None,
            "delta_vs_best_ground_A": r3(e.res - k.best_ground_res) if (k is not None and pd.notna(k.get("best_ground_res")) and pd.notna(e.res)) else None,
            "best_ground_pm3y_res_A": r3(k.get("best_ground_era_res")) if k is not None else None,
            "is_protein_best_space_entry": bool(k is not None and k.best_space_entry == e.entry_id),
            "label": e.label, "evidence_tier": "keyword/citation" if e.keyword_tier else "growth text or title",
            "note": notes.get(e.entry_id, ""),
            "label_source": "manual review" if e.entry_id in reviewed else "automatic rule",
            "evidence": ((c.grow_text if isinstance(c.grow_text, str) else "")[:220] + " || title: "
                         + (e.title if isinstance(e.title, str) else ""))[:360],
        })
    E = pd.DataFrame(rows)
    Path(a.out_csv).parent.mkdir(parents=True, exist_ok=True)
    E.to_csv(a.out_csv, index=False)
    P.drop(columns=[c for c in P.columns if c.startswith("_")]).to_csv(work / "proteins.csv", index=False)

    # ---- result JSON -------------------------------------------------------------------------
    meta = json.load(open(a.meta)) if a.meta else {}
    A = res_stats["all_proteins"]
    hist_bins = np.round(np.arange(-2.0, 2.01, 0.2), 2)

    def hist(x):
        x = np.clip(np.asarray(x, float), -1.999, 1.999)
        c, _ = np.histogram(x, bins=hist_bins)
        return [[r3((hist_bins[i] + hist_bins[i + 1]) / 2), int(c[i])] for i in range(len(c))]

    sc_pts = [[r3(r.best_ground_res), r3(r.best_space_res)] for _, r in M.iterrows()][:400]
    ref = [[r3(v), r3(v)] for v in np.arange(0.6, 4.01, 0.1)]
    stack_series = [{"name": p, "color": PCOLOR[p],
                     "points": [[int(y), int(census_year.loc[y, p]) if p in census_year.columns else 0] for y in years]}
                    for p in PLATFORMS if p in census_year.columns]
    n_space = int(len(sp))
    n_space_x = int(sp.xray.sum())
    nprot = int(sp.key.nunique())
    meta_ds = meta.get("datasets", [])
    out = {
        "id": "pdb-microgravity", "tab": "materials", "material": "protein",
        "title": "Every space-grown protein crystal in the PDB",
        "question": "Across the whole Protein Data Bank, do protein crystals grown in microgravity give better diffraction "
                    "data than Earth-grown crystals of the same protein?",
        "headline": {"value": str(n_space), "unit": "entries",
                     "text": meta.get("headline_text", f"{n_space} PDB entries say their crystals were grown in space.")},
        "evidence_level": "our computation on public data",
        "datasets": meta_ds,
        "compute": meta.get("compute", {}),
        "method": meta.get("method", []),
        "charts": [
            {"id": "census", "kind": "stacked", "title": "Space-grown PDB depositions per year",
             "subtitle": f"{n_space} entries whose own deposited text says the crystal grew in orbit (incl. "
                         f"{int((sp.label == 'mixed').sum())} merged space+Earth data sets), by the platform the text names",
             "x": {"label": "Deposition year", "unit": "", "scale": "time"},
             "y": {"label": "Entries", "unit": "count", "scale": "linear"},
             "series": stack_series,
             "caption": "Counts entries, not proteins (several entries can come from one flight). Platform comes from the "
                        "deposited text; 'Unknown' means the text says microgravity or space without naming the vehicle. No entry "
                        "names Mir. Depositors are not required to report where crystals grew, so this is a lower bound, and the "
                        "deposition year lags the flight by months to years."},
            {"id": "res-delta", "kind": "hist", "title": "Space best minus Earth best, per protein",
             "subtitle": f"{A['delta_all_time']['n_proteins']} proteins with both space- and Earth-grown X-ray entries; negative = space better",
             "x": {"label": "Resolution difference (space - Earth)", "unit": "Å", "scale": "linear"},
             "y": {"label": "Proteins", "unit": "count", "scale": "linear"},
             "series": [{"name": "vs best Earth entry, any year", "color": "orange", "points": hist(M.delta_all.dropna())},
                        {"name": "vs best Earth entry within ±3 years", "color": "cyan", "points": hist(M.delta_era.dropna())}],
             "annotations": [{"x": 0, "y": 0, "text": "no difference"}],
             "caption": "Each protein (UniProt accession set) counts once. Values beyond ±2 Å are put in the end bins. The Earth "
                        "side is the best of often many entries, so even with no microgravity effect the difference skews positive; "
                        "the permutation null in the stats corrects for that."},
            {"id": "space-vs-ground", "kind": "scatter", "title": "Best space vs best Earth resolution",
             "subtitle": "One point per protein; below the line = the space crystal set the record",
             "x": {"label": "Best Earth-grown resolution", "unit": "Å", "scale": "linear"},
             "y": {"label": "Best space-grown resolution", "unit": "Å", "scale": "linear"},
             "series": [{"name": "proteins", "color": "orange", "points": sc_pts},
                        {"name": "y = x", "color": "grey", "points": ref}],
             "caption": "Lower is better. Points are not independent of era, construct, ligand or beamline."},
            {"id": "space-best-share", "kind": "bar", "title": "How often is the space crystal the protein's best?",
             "subtitle": "Observed share of proteins vs the share expected if growth site made no difference",
             "x": {"label": "", "unit": "", "scale": "category"},
             "y": {"label": "Proteins where a space entry is the best", "unit": "%", "scale": "linear"},
             "series": [{"name": "observed", "color": "orange",
                         "points": [["Any year", r3(100 * (A["space_best"]["share"] or 0))],
                                    ["Earth entries within ±3 y", r3(100 * (A["space_best_era"]["share"] or 0))]]},
                        {"name": "expected with no effect (label permutation)", "color": "grey",
                         "points": [["Any year", r3(100 * A["permutation_null"]["null_share_space_best"])],
                                    ["Earth entries within ±3 y", r3(100 * A["permutation_null"]["null_share_space_best_era"])]]}],
             "caption": "Expected shares come from shuffling which entries of each protein are called 'space' (2,000 times). "
                        "Exceeding it means space entries rank better than a random entry of the same protein; it does not prove "
                        "microgravity caused it."},
        ],
        "stats": {
            "n_entries_scanned": int(len(ent)), "n_xray_entries": int(ent.xray.sum()),
            "n_candidates_reviewed_pool": int(len(cand)), "n_manually_reviewed": int(len(reviewed)),
            "n_space_entries": n_space, "n_space_label_space": int((sp.label == "space").sum()),
            "n_mixed_entries": int((sp.label == "mixed").sum()), "n_keyword_tier": int(sp.keyword_tier.sum()),
            "n_ground_control_entries": int((ent.label == "ground_control").sum()),
            "n_unclear_entries": int((ent.label == "unclear").sum()),
            "n_noncrystal_microgravity_entries": int((ent.label == "noncrystal").sum()),
            "methods_space_entries": sp.methods.value_counts().to_dict(),
            "precision_audit": prec, "strict_mode": bool(strict),
            "partner_mentions_entries": partner_mentions, "growth_method_mix": method_mix,
            "space_entries_by_funder": space_fund, "pdb_entries_by_space_agency_funder": {k: len(v) for k, v in fund.items()},
            "n_space_nasa_funded": len(space_fund.get("NASA", [])), "n_space_casis": len(space_fund.get("CASIS", [])),
            "n_space_xray_with_resolution": int(len(space_x)),
            "n_space_xray": n_space_x, "n_space_proteins": nprot,
            "n_proteins_with_ground_match": int(len(M)),
            "label_counts": cand.label.value_counts().to_dict(),
            "platform_counts": sp.platform.value_counts().to_dict(),
            "key_type_counts_space": sp.key_type.value_counts().to_dict(),
            "resolution": res_stats, "secondary_metrics": sec,
            "programs_mentioned": progs.to_dict(), "orgs_mentioned": orgs.to_dict(),
            "top_authors_space_entries": all_auth.head(15).to_dict(),
            "synchrotron_sites_space_entries": synch.head(10).to_dict(),
            **meta.get("extra_stats", {}),
        },
        "findings": meta.get("findings", []),
        "limitations": meta.get("limitations", []),
        "future_big_data": meta.get("future_big_data", []),
        "partners": meta.get("partners", []),
        "code": ["analysis/bigdata/pdb_parse.py", "analysis/bigdata/pdb_classify.py", "analysis/bigdata/pdb_review_labels.py",
                 "analysis/bigdata/pdb_analyze.py", "cluster/bigdata/pdb-mirror.sbatch", "cluster/bigdata/pdb-parse.sbatch",
                 "cluster/bigdata/pdb-analyze.sbatch"],
        "reproduce": meta.get("reproduce", []),
        "generated_at": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"),
    }
    Path(a.out_json).write_text(json.dumps(out, indent=1, default=lambda o: o.item() if hasattr(o, "item") else str(o)))
    print(json.dumps(out["stats"], indent=1, default=str)[:6000])


if __name__ == "__main__":
    main()
