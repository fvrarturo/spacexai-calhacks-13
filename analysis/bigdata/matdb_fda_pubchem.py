#!/usr/bin/env python3
"""matdb: map every active ingredient in the FDA Orange Book to a PubChem structure.

Orange Book `products.txt` (tilde-separated) lists approved drug products (RX, OTC and
discontinued). Its `Ingredient` field is ';'-separated and uses USAN names with the
salt (e.g. 'SERTRALINE HYDROCHLORIDE').

For each unique ingredient string we query PubChem PUG-REST by name (<= 4 req/s, cached,
resumable); if that fails, we retry with salt / hydrate words stripped. From the PubChem
SMILES we derive with RDKit the InChIKey of the largest organic component (the active
moiety), which is how we match COD crystal structures independently of naming.

Usage: python -I matdb_fda_pubchem.py PRODUCTS_TXT CACHE_JSON OUT_PARQUET
"""
import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request

import pandas as pd

SALT_WORDS = r"""hydrochloride dihydrochloride trihydrochloride hydrobromide hydroiodide hcl sodium
 disodium trisodium potassium dipotassium calcium magnesium lithium zinc aluminum ammonium
 mesylate mesilate dimesylate besylate besilate tosylate tosilate esylate edisylate napsylate
 maleate dimaleate fumarate hemifumarate tartrate bitartrate hemitartrate citrate dihydrogen
 phosphate diphosphate sulfate bisulfate hemisulfate acetate diacetate succinate hemisuccinate
 lactate gluconate malate benzoate salicylate stearate palmitate pamoate xinafoate nitrate
 oxalate bromide chloride iodide hyclate hydrate monohydrate dihydrate trihydrate
 tetrahydrate pentahydrate sesquihydrate hemihydrate anhydrous meglumine tromethamine
 olamine erbumine arginine lysine choline trifluoroacetate decanoate enanthate cypionate
 propionate valerate dipropionate furoate cyclodextrin"""
SALT_RE = re.compile(r"\b(" + "|".join(SALT_WORDS.split()) + r")\b", re.I)
PROPS = "SMILES,ConnectivitySMILES,InChIKey,MolecularFormula,Title"


def moiety_name(name):
    s = SALT_RE.sub(" ", name)
    s = re.sub(r"\s+", " ", s).strip(" ,;-")
    return s


def pubchem(name):
    url = ("https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/"
           + urllib.parse.quote(name.lower(), safe="") + f"/property/{PROPS}/JSON")
    for attempt in range(4):
        try:
            with urllib.request.urlopen(url, timeout=30) as r:
                return json.load(r)["PropertyTable"]["Properties"][0]
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return None
            time.sleep(2 * (attempt + 1))
        except Exception:  # noqa: BLE001
            time.sleep(2 * (attempt + 1))
    return None


def main_component_key(smiles):
    from rdkit import Chem, RDLogger
    from rdkit.Chem import inchi
    RDLogger.DisableLog("rdApp.*")
    best = None
    for part in smiles.split("."):
        m = Chem.MolFromSmiles(part)
        if m is None:
            continue
        nc = sum(1 for a in m.GetAtoms() if a.GetSymbol() == "C")
        heavy = m.GetNumHeavyAtoms()
        if nc == 0:
            continue
        if best is None or heavy > best[0]:
            best = (heavy, inchi.MolToInchiKey(m), Chem.MolToSmiles(m))
    return best


def main():
    products, cache_path, out = sys.argv[1:4]
    ob = pd.read_csv(products, sep="~", dtype=str)
    rows = []
    for _, r in ob.iterrows():
        for ing in str(r["Ingredient"]).split(";"):
            rows.append({"ingredient": ing.strip().upper(), "type": r["Type"], "appl_type": r["Appl_Type"]})
    ing = pd.DataFrame(rows)
    agg = ing.groupby("ingredient").agg(types=("type", lambda s: ",".join(sorted(set(s)))),
                                        n_products=("type", "size")).reset_index()
    cache = json.load(open(cache_path)) if os.path.exists(cache_path) else {}
    extra = {  # validation compounds (not all are FDA ingredients)
        "ROY": "Cc1cc(C#N)c(Nc2ccccc2[N+](=O)[O-])s1",
    }
    names = list(agg["ingredient"]) + ["RITONAVIR", "CARBAMAZEPINE", "ACETAMINOPHEN", "SULFATHIAZOLE"]
    t_last = 0.0
    n_new = 0
    for nm in dict.fromkeys(names):
        if nm in cache:
            continue
        hit, used = None, None
        for q in dict.fromkeys([nm, moiety_name(nm)]):
            if not q:
                continue
            dt = time.time() - t_last
            if dt < 0.26:
                time.sleep(0.26 - dt)
            t_last = time.time()
            hit = pubchem(q)
            if hit:
                used = q
                break
        cache[nm] = {"query": used, "hit": hit}
        n_new += 1
        if n_new % 50 == 0:
            json.dump(cache, open(cache_path, "w"))
            print(f"{n_new} queried, {sum(1 for v in cache.values() if v['hit'])} hits", flush=True)
    json.dump(cache, open(cache_path, "w"))
    recs = []
    for nm in dict.fromkeys(names + list(extra)):
        if nm in extra:
            smi, hit, q = extra[nm], {"Title": nm, "CID": None, "MolecularFormula": None}, "SMILES"
        else:
            c = cache.get(nm, {})
            hit, q = c.get("hit"), c.get("query")
            smi = (hit or {}).get("SMILES") or (hit or {}).get("IsomericSMILES") or (hit or {}).get("CanonicalSMILES")
        mc = main_component_key(smi) if smi else None
        recs.append({"ingredient": nm, "moiety_name": moiety_name(nm), "pubchem_query": q,
                     "cid": (hit or {}).get("CID"), "title": (hit or {}).get("Title"),
                     "formula": (hit or {}).get("MolecularFormula"), "smiles": smi,
                     "inchikey": (hit or {}).get("InChIKey"),
                     "moiety_key": mc[1] if mc else None, "moiety_heavy": mc[0] if mc else None,
                     "moiety_smiles": mc[2] if mc else None,
                     "is_validation": nm in ("RITONAVIR", "CARBAMAZEPINE", "ACETAMINOPHEN", "SULFATHIAZOLE", "ROY")})
    df = pd.DataFrame(recs).merge(agg, on="ingredient", how="left")
    df.to_parquet(out, index=False)
    print(f"ingredients={len(agg)} pubchem_hits={int(df.cid.notna().sum())} "
          f"with_moiety_key={int(df.moiety_key.notna().sum())} unique_moieties={df.moiety_key.nunique()}")


if __name__ == "__main__":
    main()
