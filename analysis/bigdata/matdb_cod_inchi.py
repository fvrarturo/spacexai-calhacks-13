#!/usr/bin/env python3
"""matdb: structure-based identity for COD entries.

COD ships a SMILES for ~240k entries (mysql/smiles.txt, derived by COD from the CIF
coordinates). For each entry we compute, with RDKit:
  - the set of distinct molecular components (split on '.'),
  - one InChIKey per component and its connectivity block (first 14 chars),
  - the number of distinct components (1 = single-component crystal; >1 = salt,
    solvate, hydrate or cocrystal),
  - the main (largest heavy-atom) component's InChIKey.

This is a cross-check on the requested formula + name identity, and the key we use
to match COD entries to FDA active ingredients (via PubChem InChIKeys).

Usage: python -I matdb_cod_inchi.py SMILES_TXT OUT_PARQUET [--procs 8]
"""
import argparse
import multiprocessing as mp

import pandas as pd


def one(args):
    cod_id, smi = args
    from rdkit import Chem, RDLogger
    from rdkit.Chem import inchi
    RDLogger.DisableLog("rdApp.*")
    out = {"file": cod_id, "smiles": smi, "n_comp": None, "comp_keys": None,
           "main_key": None, "main_heavy": None, "ok": False}
    if not smi:
        return out
    comps = {}
    for part in smi.split("."):
        m = Chem.MolFromSmiles(part)
        if m is None:
            m = Chem.MolFromSmiles(part, sanitize=False)
            if m is None:
                return out
        try:
            k = inchi.MolToInchiKey(m) if m is not None else ""
        except Exception:  # noqa: BLE001
            k = ""
        if not k:
            return out
        comps[k] = max(comps.get(k, 0), m.GetNumHeavyAtoms())
    main = max(comps, key=comps.get)
    out.update(n_comp=len(comps), comp_keys=";".join(sorted(comps)), main_key=main,
               main_heavy=comps[main], ok=True)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("smiles_txt")
    ap.add_argument("out")
    ap.add_argument("--procs", type=int, default=8)
    a = ap.parse_args()
    rows = []
    for line in open(a.smiles_txt, encoding="utf-8", errors="replace"):
        f = line.rstrip("\n").split("\t")
        if len(f) >= 3:
            rows.append((int(f[1]), f[2].strip()))
    with mp.Pool(a.procs) as pool:
        res = pool.map(one, rows, chunksize=500)
    df = pd.DataFrame(res)
    df.to_parquet(a.out, index=False)
    print(f"smiles rows={len(rows)} ok={int(df.ok.sum())} single_component={int((df.n_comp == 1).sum())}")


if __name__ == "__main__":
    main()
