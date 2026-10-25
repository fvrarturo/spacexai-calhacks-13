#!/usr/bin/env python3
"""matdb C: why gravity ruins large colloidal crystals (physics computation).

For hard spheres of silica, PMMA and polystyrene in water at 25 C, compute versus
diameter d = 100 nm .. 5 um:
  - Stokes sedimentation velocity     v   = 2 a^2 drho g / (9 eta)
  - gravitational Peclet number        Pe  = (4/3) pi a^4 drho g / (kB T)  (= v a / D)
  - gravitational (barometric) length  l_g = kB T / (m_b g) = a / Pe
  - time to sediment 1 mm              t   = 1 mm / v
at 1 g, at the ISS quasi-steady level (1e-6 g) and at a free-flyer drag level
(1e-7 g, a PLACEHOLDER until the orbit workstream measures it from tracking data).

Nothing here is measured. Stdlib only. Usage: python3 matdb_colloid.py OUT_JSON
"""
import datetime as dt
import json
import math
import sys

KB = 1.380649e-23          # J/K, exact (SI 2019)
T = 298.15                 # K
G0 = 9.80665               # m/s^2, standard gravity
RHO_W = 997.05             # kg/m^3, water at 25 C
ETA_W = 0.8900e-3          # Pa s, water at 25 C
MATERIALS = {              # particle density, kg/m^3 (typical values; see notes)
    "silica (Stober, 2.0 g/cm3)": 2000.0,
    "PMMA (1.19 g/cm3)": 1190.0,
    "polystyrene (1.05 g/cm3)": 1050.0,
}
ENVS = {"1 g (ground)": 1.0, "ISS quasi-steady (1e-6 g)": 1e-6,
        "free flyer (1e-7 g, placeholder)": 1e-7}
COLORS = {"silica (Stober, 2.0 g/cm3)": "orange", "PMMA (1.19 g/cm3)": "cyan",
          "polystyrene (1.05 g/cm3)": "violet"}
ENV_COLORS = {"1 g (ground)": "orange", "ISS quasi-steady (1e-6 g)": "cyan",
              "free flyer (1e-7 g, placeholder)": "green"}


def props(d, rho_p, glev):
    a = d / 2
    drho = rho_p - RHO_W
    g = glev * G0
    v = 2 * a * a * drho * g / (9 * ETA_W)
    pe = 4 / 3 * math.pi * a ** 4 * drho * g / (KB * T)
    lg = a / pe
    return v, pe, lg, 1e-3 / v


def d_crit(rho_p, glev):
    """Diameter at which Pe = 1."""
    return 2 * (3 * KB * T / (4 * math.pi * (rho_p - RHO_W) * glev * G0)) ** 0.25


def fmt_t(s):
    for unit, k in (("years", 3.156e7), ("days", 86400), ("hours", 3600), ("minutes", 60)):
        if s >= k:
            return f"{s / k:.3g} {unit}"
    return f"{s:.3g} s"


def main(out, lit_path=None):
    n = 120
    ds = [1e-7 * (50 ** (i / (n - 1))) for i in range(n)]   # 100 nm .. 5 um, log spaced
    um = lambda d: round(d * 1e6, 5)                          # noqa: E731
    charts = []

    # Chart 1: Pe vs d, three materials at 1 g
    charts.append({
        "id": "pe-ground", "kind": "line",
        "title": "On the ground, gravity beats Brownian motion above about 1 um",
        "subtitle": "Gravitational Peclet number Pe = (4/3) pi a^4 drho g / kT, spheres in water, 25 C, 1 g",
        "x": {"label": "Particle diameter", "unit": "um", "scale": "log"},
        "y": {"label": "Peclet number Pe", "unit": "", "scale": "log"},
        "series": [{"name": m, "color": COLORS[m],
                    "points": [[um(d), float(f"{props(d, r, 1.0)[1]:.4g}")] for d in ds]}
                   for m, r in MATERIALS.items()],
        "hlines": [{"y": 1, "text": "Pe = 1: settling and diffusion balance"}],
        "caption": "Physics computation, not a measurement. Pe < 1 means thermal motion can still "
                   "rearrange particles faster than they settle by one radius. It does not by itself "
                   "guarantee a good crystal: polydispersity, interactions and drying also matter.",
    })
    # Chart 2: silica Pe vs d in three environments
    rs = MATERIALS["silica (Stober, 2.0 g/cm3)"]
    charts.append({
        "id": "pe-environments", "kind": "line",
        "title": "Silica spheres: Peclet number at 1 g, ISS level and free-flyer level",
        "subtitle": "Pe scales linearly with g, so the Pe = 1 crossover diameter scales as g^(-1/4)",
        "x": {"label": "Particle diameter", "unit": "um", "scale": "log"},
        "y": {"label": "Peclet number Pe", "unit": "", "scale": "log"},
        "series": [{"name": e, "color": ENV_COLORS[e],
                    "points": [[um(d), float(f"{props(d, rs, gl)[1]:.4g}")] for d in ds]}
                   for e, gl in ENVS.items()],
        "hlines": [{"y": 1, "text": "Pe = 1"}],
        "caption": "Physics computation. The 1e-7 g level is a placeholder until the orbit workstream "
                   "measures the free-flyer drag acceleration from tracking data. ISS measured "
                   "quasi-steady levels are typically a few micro-g, not exactly 1e-6 g.",
    })
    # Chart 3: time to sediment 1 mm, silica, three environments
    charts.append({
        "id": "t-sediment-1mm", "kind": "line",
        "title": "Time for silica spheres to sink 1 mm",
        "subtitle": "Stokes velocity v = 2 a^2 drho g / (9 eta); t = 1 mm / v",
        "x": {"label": "Particle diameter", "unit": "um", "scale": "log"},
        "y": {"label": "Time to sediment 1 mm", "unit": "hours", "scale": "log"},
        "series": [{"name": e, "color": ENV_COLORS[e],
                    "points": [[um(d), float(f"{props(d, rs, gl)[3] / 3600:.4g}")] for d in ds]}
                   for e, gl in ENVS.items()],
        "hlines": [{"y": 24 * 7, "text": "1 week"}, {"y": 24 * 365, "text": "1 year"}],
        "caption": "Physics computation for a single sphere in an unbounded fluid (dilute limit). Real "
                   "concentrated suspensions settle more slowly (hindered settling, roughly (1-phi)^5), "
                   "so these times are lower bounds for dense samples.",
    })
    # Chart 4: gravitational length vs d, silica
    charts.append({
        "id": "grav-length", "kind": "line",
        "title": "Gravitational length vs sample height (silica)",
        "subtitle": "l_g = kT / (m_b g): the height over which the equilibrium concentration falls by e",
        "x": {"label": "Particle diameter", "unit": "um", "scale": "log"},
        "y": {"label": "Gravitational length l_g", "unit": "mm", "scale": "log"},
        "series": [{"name": e, "color": ENV_COLORS[e],
                    "points": [[um(d), float(f"{props(d, rs, gl)[2] * 1e3:.4g}")] for d in ds]}
                   for e, gl in ENVS.items()],
        "hlines": [{"y": 1, "text": "1 mm sample height"}, {"y": 10, "text": "1 cm sample height"}],
        "caption": "Physics computation. A sample much taller than l_g ends up as a dense sediment with a "
                   "concentration gradient, which compresses and strains crystals. On the ground, l_g "
                   "of 300 nm silica is ~0.03 mm, far below a 1 cm sample; at 1e-6 g it is ~30 m.",
    })
    # Chart 5: crossover diameters
    short = {"1 g (ground)": "1 g", "ISS quasi-steady (1e-6 g)": "ISS 1e-6 g",
             "free flyer (1e-7 g, placeholder)": "free flyer 1e-7 g (placeholder)"}
    charts.append({
        "id": "d-crit", "kind": "hbar",
        "title": "Largest sphere diameter that Brownian motion can still organise (Pe = 1)",
        "subtitle": "Crossover diameter d* = 2 (3 kT / (4 pi drho g))^(1/4)",
        "x": {"label": "Crossover diameter d*", "unit": "um", "scale": "log"},
        "y": {"label": "Particle material", "unit": "um", "scale": "category"},
        "series": [{"name": short[e], "color": ENV_COLORS[e],
                    "points": [[m.split(" (")[0], round(d_crit(r, gl) * 1e6, 3)]
                               for m, r in MATERIALS.items()]} for e, gl in ENVS.items()],
        "caption": "Physics computation. Below d* thermal motion dominates; above it, settling does. "
                   "The 1e-7 g row uses a placeholder acceleration.",
    })

    # optional: sphere sizes used in published colloidal-crystal papers (OpenAlex abstracts)
    lit = json.load(open(lit_path)) if lit_path else None
    lit_stats = None
    if lit:
        dsil, dps = d_crit(MATERIALS["silica (Stober, 2.0 g/cm3)"], 1.0) * 1e6, d_crit(MATERIALS["polystyrene (1.05 g/cm3)"], 1.0) * 1e6
        edges = [0.0, 0.2, 0.3, 0.5, dsil, dps, 1e9]
        labs = ["< 0.2 um", "0.2-0.3 um", "0.3-0.5 um", f"0.5-{dsil:.1f} um", f"{dsil:.1f}-{dps:.1f} um", f"> {dps:.1f} um"]
        ds = sorted(p["d_um"] for p in lit["papers"])
        mats = ["silica", "polystyrene", "PMMA", "unspecified"]
        series = []
        for mname, col in zip(mats, ["orange", "violet", "cyan", "grey"]):
            pts = []
            for lo, hi, lb in zip(edges[:-1], edges[1:], labs):
                pts.append([lb, sum(1 for p in lit["papers"] if p["material"] == mname and lo <= p["d_um"] < hi)])
            series.append({"name": mname, "color": col, "points": pts})
        n_above = sum(d > dsil for d in ds)
        med = ds[len(ds) // 2] if len(ds) % 2 else 0.5 * (ds[len(ds) // 2 - 1] + ds[len(ds) // 2])
        lit_stats = {"n_sampled_works": lit["n_sampled"], "n_with_diameter": len(ds), "median_d_um": round(med, 3),
                     "n_above_silica_1g_crossover": n_above, "share_above_pct": round(100 * n_above / len(ds), 1),
                     "query": lit["query"], "per_paper": [[p["id"].rsplit("/", 1)[-1], p.get("year"),
                                                           round(p["d_um"], 4), p["material"]] for p in lit["papers"]],
                     "extraction_examples": lit["examples"][:10]}
        charts.append({
            "id": "lit-sphere-sizes", "kind": "stacked",
            "title": "Sphere sizes used in published colloidal-crystal papers",
            "subtitle": f"Sphere diameters stated in {len(ds)} of {lit['n_sampled']:,} randomly sampled OpenAlex abstracts "
                        "(one median value per paper)",
            "x": {"label": "Sphere diameter", "unit": "", "scale": "category"},
            "y": {"label": "Papers", "unit": "", "scale": "linear"},
            "series": series,
            "caption": "This chart alone is our computation on public data (OpenAlex abstracts, regex extraction), not "
                       "physics. Bin edges at the 1 g crossover diameters of silica and polystyrene. Only ~3% of "
                       "abstracts state a sphere size, so this is a small, abstract-only sample."})

    # stats
    table = {}
    for m, r in MATERIALS.items():
        table[m] = {}
        for e, gl in ENVS.items():
            ent = {"d_crit_um": round(d_crit(r, gl) * 1e6, 3)}
            for dsz in (0.2, 0.3, 1.0, 5.0):
                v, pe, lg, t = props(dsz * 1e-6, r, gl)
                ent[f"d{dsz}um"] = {"v_m_per_s": float(f"{v:.4g}"), "Pe": float(f"{pe:.4g}"),
                                     "l_g_mm": float(f"{lg * 1e3:.4g}"),
                                     "t_1mm_s": float(f"{t:.4g}"), "t_1mm_human": fmt_t(t)}
            table[m][e] = ent
    s = table["silica (Stober, 2.0 g/cm3)"]
    dc1, dciss, dcff = (s[e]["d_crit_um"] for e in ENVS)
    res = {
        "id": "colloid-sedimentation",
        "tab": "materials",
        "material": "photonic",
        "title": "Why gravity ruins large colloidal crystals",
        "question": "At what particle size does sedimentation beat Brownian self-assembly, on the "
                    "ground and in orbit?",
        "headline": {"value": f"{dc1:.1f}", "unit": "um",
                     "text": f"On the ground, silica spheres larger than about {dc1:.1f} um sink faster "
                             f"than Brownian motion can arrange them (Pe > 1). At an ISS-like 1e-6 g "
                             f"that limit moves to about {dciss:.0f} um, and at 1e-7 g to about "
                             f"{dcff:.0f} um. Physics computation, not a measurement."},
        "evidence_level": "physics computation (not a measurement)",
        "evidence_note": "physics computation from textbook formulas (Stokes drag, Peclet number); "
                         "no data were measured",
        "datasets": [
            {"name": "Physical constants and fluid properties", "url": "https://physics.nist.gov/cuu/Constants/",
             "license": "public", "records": 0, "bytes": 0, "accessed": "2026-10-24",
             "notes": "kB exact (SI 2019); water at 25 C: density 997.05 kg/m3, viscosity 0.890 mPa s "
                      "(standard reference values, e.g. CRC Handbook). Particle densities: Stober silica "
                      "~2.0 g/cm3 (fused silica is 2.2), PMMA 1.19, polystyrene 1.05 g/cm3."},
            {"name": "ISS quasi-steady acceleration level", "url":
             "https://www.nasa.gov/wp-content/uploads/2016/06/acceleration-environment-iss-mini-book_detail-508c.pdf",
             "license": "public (NASA)", "records": 0, "bytes": 0, "accessed": "2026-10-24",
             "notes": "ISS design requirement of about 1 micro-g at payload locations; PIMS reports "
                      "measured quasi-steady levels typically a few micro-g (<= ~5 ug). See also NASA "
                      "NTRS 20100042410 (Assembly Complete microgravity verification)."},
        ] + ([{"name": "OpenAlex works (random sample, seed 42)", "url": "https://openalex.org/", "license": "CC0",
               "records": lit_stats["n_sampled_works"], "bytes": 0, "accessed": "2026-10-24",
               "notes": "title_and_abstract.search: " + lit_stats["query"] + "; type article; has abstract."}] if lit_stats else []),
        "compute": {"where": "local (stdlib Python; physics < 1 s; OpenAlex sample 20 API pages)", "partitions": [], "job_ids": [],
                    "cpu_hours": 0.0, "wall_minutes": 0.0, "peak_storage_gb": 0.0},
        "method": [
            "Hard spheres of diameter 100 nm to 5 um (120 log-spaced sizes) in water at 25 C.",
            "Stokes velocity v = 2 a^2 drho g / (9 eta); Peclet number Pe = (4/3) pi a^4 drho g / kT "
            "(equivalently v a / D with D = kT / (6 pi eta a)); gravitational length l_g = a / Pe; "
            "time to sink 1 mm = 1 mm / v.",
            "Three gravity levels: 1 g; 1e-6 g (ISS quasi-steady design level); 1e-7 g (free-flyer "
            "drag level, a placeholder until the orbit workstream measures it).",
            "Crossover diameter where Pe = 1: d* = 2 (3 kT / (4 pi drho g))^(1/4), so d* scales as g^(-1/4).",
        ],
        "charts": charts,
        "stats": {"table": table, "gravity_levels_g": ENVS, "literature_sizes": lit_stats,
                  "constants": {"kB": KB, "T_K": T, "g0": G0, "rho_water": RHO_W, "eta_water": ETA_W}},
        "findings": [
            f"At 1 g the Pe = 1 crossover is at d* = {dc1:.2f} um for silica, "
            f"{table['PMMA (1.19 g/cm3)']['1 g (ground)']['d_crit_um']:.2f} um for PMMA and "
            f"{table['polystyrene (1.05 g/cm3)']['1 g (ground)']['d_crit_um']:.2f} um for polystyrene "
            "(density-matched particles settle less).",
            f"At 1e-6 g the silica crossover moves to {dciss:.1f} um and at 1e-7 g to {dcff:.1f} um, so "
            "every size from 100 nm to 5 um has Pe < 1 in orbit.",
            "300 nm silica spheres, the size used for visible-light photonic crystals, sink 1 mm in "
            f"{s['1 g (ground)']['d0.3um']['t_1mm_human']} on the ground and in "
            f"{s['ISS quasi-steady (1e-6 g)']['d0.3um']['t_1mm_human']} at 1e-6 g.",
            "For visible-range spheres (~200-300 nm) Pe is already below 1 on the ground, so the gravity "
            "problem for them is not single-particle settling but the dense sediment: the gravitational "
            f"length ({s['1 g (ground)']['d0.3um']['l_g_mm'] * 1000:.0f} um for 300 nm silica) is far "
            "smaller than a mm-cm sample, giving concentration gradients and self-compression. Larger "
            "(IR, 1-5 um) spheres have Pe >> 1 on the ground.",
            "Published context (not our result): hard-sphere colloids that stayed glassy on Earth "
            "crystallised in microgravity on Space Shuttle STS-73 (Zhu et al., Nature 387, 883, 1997).",
        ] + ([f"Literature sample (our computation on OpenAlex abstracts): of {lit_stats['n_with_diameter']} papers that state a "
              f"sphere size, the median is {lit_stats['median_d_um'] * 1000:.0f} nm and {lit_stats['n_above_silica_1g_crossover']} "
              f"({lit_stats['share_above_pct']}%) use spheres above silica's 1 g crossover of {dc1:.1f} um. Most "
              "experiments sit in the sub-micron range that visible-light photonics needs, where Pe < 1 even on the "
              "ground; the gravity-limited regime (> ~1 um, infrared photonics, large-sphere model systems) is the "
              "under-explored part. Why authors choose sizes is not in the data."] if lit_stats else []),
        "limitations": [
            "Physics computation, not a measurement or simulation of crystal growth.",
            "Dilute single-sphere Stokes settling; dense suspensions settle more slowly (hindered "
            "settling), and walls, convection, charge and polydispersity are ignored.",
            "Pe < 1 is a necessary condition for gravity not to dominate, not a sufficient condition "
            "for a large defect-free crystal.",
            "1e-7 g is a placeholder; the real free-flyer level comes from the orbit workstream. ISS "
            "measured quasi-steady levels are typically a few micro-g (d* then shrinks by ~5^(1/4) = 1.5x).",
            "Particle densities are typical values; Stober silica density varies (~1.9-2.2 g/cm3).",
        ] + (["Literature sizes: abstract-only regex extraction from a seeded random sample of OpenAlex works; only "
              "papers that state a size in the abstract are counted, a few matches may be pore or film sizes rather "
              "than sphere diameters, and the sample was run from a laptop because OpenAlex's anonymous budget is "
              "per IP."] if lit_stats else []),
        "future_big_data": [
            "Mine the literature (e.g. OpenAlex/Crossref full text) for particle diameters, materials and "
            "crystal sizes reported in colloidal photonic-crystal papers, and place them on these curves.",
            "Use the measured free-flyer acceleration spectrum (orbit workstream) instead of the 1e-7 g "
            "placeholder, including its time variation.",
            "Pair with Brownian-dynamics simulations of sedimenting crystallisation at each g level.",
        ],
        "partners": [
            {"name": "Colloid / photonic-crystal research groups",
             "why": "They make and characterise the sphere suspensions and opals that this pillar needs.",
             "evidence": "Generic: the computation shows which sizes (>~1 um on Earth) are gravity-limited; "
                         "no specific organisation is named because this analysis has no data pointing "
                         "to one."},
        ],
        "code": ["analysis/bigdata/matdb_colloid.py", "analysis/bigdata/matdb_colloid_lit.py"],
        "reproduce": ["python3 analysis/bigdata/matdb_colloid_lit.py RAW_DIR colloid_lit.json --n 4000  # OpenAlex sample, seed 42",
                      "python3 analysis/bigdata/matdb_colloid.py data/results/bigdata/colloid-sedimentation.json colloid_lit.json"],
        "generated_at": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"),
    }
    json.dump(res, open(out, "w"), indent=1)
    print(json.dumps(res["headline"], indent=1))
    print("silica d*:", dc1, dciss, dcff)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else None)
