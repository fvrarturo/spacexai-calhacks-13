#!/usr/bin/env python3
"""matdb C (optional): what sphere sizes do published colloidal-crystal experiments use?

Random sample (seeded) of OpenAlex works whose title/abstract mention colloidal crystals or
opals; sphere diameters are pulled from abstracts with conservative regexes that require a
particle word next to the size ("250 nm silica spheres", "spheres with a diameter of
1.2 um"). One value per paper (median of its matches) so that a paper listing many sizes
counts once. Stdlib only.

Usage: python3 matdb_colloid_lit.py RAW_DIR OUT_JSON [--n 4000]
"""
import json
import os
import re
import statistics
import sys
import time
import urllib.parse
import urllib.request

Q = '"colloidal crystal" OR "colloidal crystals" OR "colloidal photonic crystal" OR "artificial opal" OR "inverse opal"'
NUM = r"(\d+(?:\.\d+)?)(?:\s*(?:-|–|to|and)\s*(\d+(?:\.\d+)?))?"
UNIT = r"(nm|µm|μm|um|microns?|micrometers?|micrometres?|nanometers?|nanometres?)"
PARTW = (r"(?:(?:mono-?disperse|uniform|silica|SiO2|SiO 2|polystyrene|PS|PMMA|poly\s*\(methyl methacrylate\)|latex|"
         r"colloidal|core-shell|polymer|carboxylated|hollow|sub-?micron|charged)[\s-]+){0,3}"
         r"(?:nano|micro)?(?:spheres?|particles?|beads?|colloids?|microspheres?|nanospheres?|nanoparticles?|"
         r"microparticles?|latex(?:es)?)\b")
PA = re.compile(NUM + r"\s*" + UNIT + r"[\s-]*(?:(?:diameter|sized?|size)[\s-]*)?" + PARTW, re.I)
PB = re.compile(PARTW + r"[^.;]{0,50}?(?:diameters?|sizes?)\s*(?:of|=|:|~|ranging from|from|between|in the range of)?"
                r"\s*(?:about|approximately|ca\.|~|≈)?\s*" + NUM + r"\s*" + UNIT, re.I)
MAT = [("silica", re.compile(r"silica|SiO\s?2", re.I)), ("polystyrene", re.compile(r"polystyrene|\bPS\b", re.I)),
       ("PMMA", re.compile(r"PMMA|methyl methacrylate", re.I))]


def to_um(v, unit):
    u = unit.lower()
    return v / 1000.0 if u.startswith("n") else v


def abstract(ii):
    if not ii:
        return ""
    n = max(p for v in ii.values() for p in v) + 1
    t = [""] * n
    for k, v in ii.items():
        for p in v:
            t[p] = k
    return " ".join(t)


def fetch(raw_dir, n):
    path = os.path.join(raw_dir, f"openalex_colloid_sample_{n}.jsonl")
    if os.path.exists(path):
        return [json.loads(x) for x in open(path)], path
    out = []
    page = 1
    while len(out) < n:
        url = ("https://api.openalex.org/works?" + urllib.parse.urlencode({
            "filter": f"title_and_abstract.search:{Q},has_abstract:true,type:article",
            "sample": n, "seed": 42, "per-page": 200, "page": page,
            "select": "id,doi,title,publication_year,abstract_inverted_index"}))
        with urllib.request.urlopen(url, timeout=60) as r:
            d = json.load(r)
        res = d.get("results", [])
        if not res:
            break
        out += res
        page += 1
        time.sleep(0.5)
    with open(path, "w") as f:
        for w in out:
            f.write(json.dumps(w) + "\n")
    return out, path


def main():
    raw_dir, out_json = sys.argv[1], sys.argv[2]
    n = int(sys.argv[sys.argv.index("--n") + 1]) if "--n" in sys.argv else 4000
    os.makedirs(raw_dir, exist_ok=True)
    works, path = fetch(raw_dir, n)
    papers = []
    examples = []
    for w in works:
        txt = abstract(w.get("abstract_inverted_index"))
        vals, mats = [], []
        for rx, order in ((PA, "num_first"), (PB, "part_first")):
            for m in rx.finditer(txt):
                g = m.groups()
                if order == "num_first":
                    a, b, unit = g[0], g[1], g[2]
                else:
                    a, b, unit = g[0], g[1], g[2]
                v = float(a) if not b else (float(a) + float(b)) / 2
                d = to_um(v, unit)
                if 0.02 <= d <= 50:
                    vals.append(d)
                    s = m.group(0)
                    mats += [name for name, r in MAT if r.search(s)]
                    if len(examples) < 25:
                        examples.append({"match": s[:120], "d_um": round(d, 4), "work": w["id"]})
        if vals:
            mat = max(set(mats), key=mats.count) if mats else "unspecified"
            papers.append({"id": w["id"], "year": w.get("publication_year"), "d_um": statistics.median(vals),
                           "material": mat, "n_matches": len(vals)})
    json.dump({"query": Q, "n_sampled": len(works), "raw_file": os.path.basename(path), "papers": papers,
               "examples": examples}, open(out_json, "w"), indent=1)
    ds = sorted(p["d_um"] for p in papers)
    print(f"sampled={len(works)} with_diameter={len(papers)} median_um={statistics.median(ds):.3f}")
    print("share > 1.12 um:", round(sum(d > 1.124 for d in ds) / len(ds), 3))
    for e in examples[:12]:
        print(e)


if __name__ == "__main__":
    main()
