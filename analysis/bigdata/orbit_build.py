#!/usr/bin/env python
"""Orbit workstream, stage 3 (laptop): build the site result files from the cluster aggregates.

Inputs : orbit_agg.json (from orbit_analyze.py on Engaging; aggregates only, no raw TLEs)
         power.json     (from orbit_power.py)
         jobs.json      (sacct records collected by hand from the cluster)
Outputs: data/results/bigdata/orbit-environment.json  (tab foundry)
         data/results/bigdata/orbit-crowding.json     (tabs network / foundry)
Usage  : python analysis/bigdata/orbit_build.py AGG.json POWER.json JOBS.json
"""
import datetime
import json
import sys

import numpy as np
import pandas as pd

AGG, POWER, JOBS = sys.argv[1:4]
CALIB = sys.argv[4] if len(sys.argv) > 4 else None
agg = json.load(open(AGG))
power = json.load(open(POWER))
jobs = json.load(open(JOBS))
OUTDIR = "data/results/bigdata"
NOW = datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds")
MU, RE, G0 = 3.986004418e14, 6378.137e3, 9.80665
BC_LO, BC_MID, BC_HI = 50.0, 150.0, 400.0

ys = pd.DataFrame(agg["year_stats"])
ROWS, BYTES = int(ys.rows_read.sum()), int(ys.bytes.sum())
g_all = pd.DataFrame(agg["g_all"]); g_rb = pd.DataFrame(agg["g_rb"]); g_deb = pd.DataFrame(agg["g_deb"])
g_pay = pd.DataFrame(agg["g_pay"])
rho = pd.DataFrame(agg["rho_tle"]); msis = pd.DataFrame(agg["msis"])
life = pd.DataFrame(agg["lifetime"]); km = pd.DataFrame(agg["km"])
sol = agg["solar"]
T1, T2 = sol["T1"], sol["T2"]


def sig(x, n=2):
    return float(f"{x:.{n}g}")


def hc(b):
    return b + 12.5


def v_of(h_km):
    return np.sqrt(MU / (RE + h_km * 1e3))


# ------------------------------------------------------------------ foundry-scaled g-levels
# Route used: NRLMSIS 2.1 orbit-averaged density at the tercile-median F10.7 / Ap, validated against
# (i) the Starshine 3 sphere of known ballistic coefficient (absolute level) and (ii) the measured
# population decay (solar-activity response). The B*-based route was rejected (see stats).
def foundry_g(rho_v, h_km, BC):
    return 0.5 * rho_v * v_of(h_km) ** 2 / BC / G0


rows = []
for s in ("low", "mid", "high"):
    gt = g_all[g_all.sol == s].set_index("band")
    mt = msis[msis.sol == s].set_index("band")
    rt = rho[rho.sol == s].set_index("band")
    for b in sorted(set(gt.index) & set(mt.index)):
        h = hc(b)
        rm = mt.loc[b, "rho_msis"]
        gb1 = foundry_g(rm, h, 1.0)                       # g per unit B (B = 1 m2/kg)
        rows.append(dict(band=b, sol=s, h=h, rho_msis=rm, g_f=foundry_g(rm, h, BC_MID),
                         g_f_lo=foundry_g(rm, h, BC_HI), g_f_hi=foundry_g(rm, h, BC_LO),
                         g_pop=gt.loc[b, "med"], bc_pop=gb1 / gt.loc[b, "med"],
                         n_obj=int(gt.loc[b, "n_objects"]),
                         rho_bstar_ratio=(rt.loc[b, "med"] / rm) if b in rt.index else np.nan))
fs = pd.DataFrame(rows)
cal = json.load(open(CALIB)) if CALIB else None
cal_ratio = cal["ratio_measured_over_msis_median"] if cal else None


def pts(df, x, y, scale=1.0, nd=3):
    return [[float(a), sig(float(c) * scale, nd)] for a, c in zip(df[x], df[y]) if np.isfinite(c) and c > 0]


def gtab(df, s, hmin=300, hmax=800):
    d = df[df.sol == s].sort_values("band").copy()
    d["h"] = d.band + 12.5
    return d[(d.h >= hmin) & (d.h < hmax)]


low, high, mid = gtab(g_all, "low"), gtab(g_all, "high"), gtab(g_all, "mid")
fsv = fs[(fs.h >= 300) & (fs.h < 800)]
series_g = [
    {"name": "Measured: passive objects, solar high tercile (median month)", "points": pts(high, "h", "med"), "color": "orange"},
    {"name": "Measured: passive objects, solar low tercile (median month)", "points": pts(low, "h", "med"), "color": "cyan"},
    {"name": "Measured: solar high, 90th percentile object-month", "points": pts(high, "h", "p90"), "color": "orange"},
    {"name": "Measured: solar low, 10th percentile object-month", "points": pts(low, "h", "p10"), "color": "cyan"},
    {"name": f"Foundry BC {BC_MID:.0f} kg/m2, solar high (MSIS, checked on data)", "points": pts(fsv[fsv.sol == "high"], "h", "g_f"), "color": "violet"},
    {"name": f"Foundry BC {BC_MID:.0f} kg/m2, solar low (MSIS, checked on data)", "points": pts(fsv[fsv.sol == "low"], "h", "g_f"), "color": "green"},
    {"name": "ISS quasi-steady requirement, 1 micro-g (published)", "points": [[300, 1e-6], [775, 1e-6]], "color": "grey"},
    {"name": "ISS perpendicular-component requirement, 0.2 micro-g (published)", "points": [[300, 2e-7], [775, 2e-7]], "color": "grey"},
]


def at(df, h, col="med"):
    r = df[df.band + 12.5 == h]
    return float(r[col].iloc[0]) if len(r) else float("nan")


head = {}
for h in (300.0, 350.0, 400.0, 450.0, 500.0, 550.0, 600.0, 650.0, 700.0):
    for s in ("low", "mid", "high"):
        r = fs[(fs.band == h) & (fs.sol == s)]
        if not len(r):
            continue
        r = r.iloc[0]
        gs = g_all[g_all.sol == s].set_index("band").loc[h]
        head[f"{int(h)}-{int(h) + 25}km_{s}"] = {
            "foundry_g_BC150": sig(r.g_f),
            "foundry_g_range_BC400_to_BC50": [sig(r.g_f_lo), sig(r.g_f_hi)],
            "passive_objects_median_g": sig(gs["med"]),
            "passive_objects_median_g_95ci_month_bootstrap": [sig(gs["lo"]), sig(gs["hi"])],
            "passive_objects_p10_p90_g": [sig(gs["p10"]), sig(gs["p90"])],
            "rocket_bodies_median_g": sig(at(g_rb[g_rb.sol == s], h + 12.5)) if len(g_rb) else None,
            "debris_median_g": sig(at(g_deb[g_deb.sol == s], h + 12.5)) if len(g_deb) else None,
            "implied_population_BC_kg_m2": sig(r.bc_pop),
            "F107a_tercile_median_sfu": sig(sol["ref"][s]["F107a"], 3),
            "n_object_months": int(gs["n_object_months"]), "n_objects": int(gs["n_objects"]), "n_months": int(gs["n_months"]),
        }

# consistency of the model's solar response with the measured decay: implied population BC per tercile
cons = {}
for h in (300.0, 350.0, 400.0, 450.0, 500.0, 550.0, 600.0):
    d = fs[fs.band == h].set_index("sol")
    if {"low", "high"} <= set(d.index):
        meas = d.loc["high", "g_pop"] / d.loc["low", "g_pop"]
        mod = d.loc["high", "rho_msis"] / d.loc["low", "rho_msis"]
        cons[f"{int(h)}-{int(h) + 25}km"] = {"measured_high_over_low": sig(meas, 3), "msis_high_over_low": sig(mod, 3),
                               "measured_over_model": sig(meas / mod, 3)}

# ------------------------------------------------------------------ lifetime chart
def lpts(route, BC, col="med"):
    d = life[(life.route == route) & (life.BC == BC)].sort_values("h0")
    return [[float(h), sig(float(v), 3)] for h, v in zip(d.h0, d[col]) if v is not None and np.isfinite(v)]


series_life = [
    {"name": f"Foundry BC {BC_MID:.0f} kg/m2, median start date", "points": lpts("msis", BC_MID), "color": "orange"},
    {"name": f"Foundry BC {BC_MID:.0f}: start near solar max (10th pct)", "points": lpts("msis", BC_MID, "p10"), "color": "orange"},
    {"name": f"Foundry BC {BC_MID:.0f}: start near solar min (90th pct)", "points": lpts("msis", BC_MID, "p90"), "color": "orange"},
    {"name": f"Foundry BC {BC_LO:.0f} kg/m2 (light, big arrays), median", "points": lpts("msis", BC_LO), "color": "cyan"},
    {"name": f"Foundry BC {BC_HI:.0f} kg/m2 (compact, dense), median", "points": lpts("msis", BC_HI), "color": "violet"},
]
km_series = []
for typ, col in (("R/B", "green"), ("DEB", "grey")):
    d = km[(km.type == typ) & (km.n >= 50)].sort_values("h")
    km_series.append({"name": f"Measured: real {'rocket bodies' if typ == 'R/B' else 'debris'}, Kaplan-Meier median years to reentry after crossing altitude",
                      "points": [[float(h), sig(float(q), 3)] for h, q in zip(d.h, d.q50) if q is not None and np.isfinite(q)],
                      "color": col})

life_stats = {}
for h0 in (300, 350, 400, 450, 500, 550, 600, 650, 700):
    rr = {}
    for BC in (BC_LO, BC_MID, BC_HI):
        d = life[(life.route == "msis") & (life.BC == BC) & (life.h0 == h0)]
        if len(d):
            r = d.iloc[0]
            f = lambda x: None if x is None or not np.isfinite(x) else sig(x, 3)
            rr[f"BC{int(BC)}"] = {"median_yr": f(r.med), "p10_yr": f(r.p10), "p90_yr": f(r.p90),
                                  "frac_beyond_300yr": sig(r.frac_over_max, 3)}
    life_stats[f"{h0}km"] = rr

# ------------------------------------------------------------------ power
pw = power["stats"]

# ------------------------------------------------------------------ crowding
cr = pd.DataFrame(agg["crowd"])
cmap = {"Starlink": "Starlink", "OneWeb": "Other megaconstellations", "Other megaconstellation": "Other megaconstellations",
        "Other payload": "Other payloads", "Rocket body": "Rocket bodies", "Debris": "Debris and unknown",
        "Unknown": "Debris and unknown"}
cr["cat"] = cr.category.map(cmap).fillna("Debris and unknown")
CATS = [("Starlink", "orange"), ("Other megaconstellations", "violet"), ("Other payloads", "cyan"),
        ("Rocket bodies", "green"), ("Debris and unknown", "grey")]
jul = cr[cr.snapshot.str.endswith("-07-01") & (cr.year >= 1990)]
latest_lab = sorted(cr[cr.snapshot.str.startswith("latest:")].snapshot.unique())[-1]
latest = cr[cr.snapshot == latest_lab]
latest_date = latest_lab.split(":")[1]

leo = jul[jul.band < 2000].groupby(["year", "cat"]).n.sum().unstack(fill_value=0)
series_year = [{"name": c, "points": [[int(y), int(leo.loc[y, c]) if c in leo else 0] for y in leo.index], "color": col}
               for c, col in CATS]
# add the latest snapshot as the final point labelled by fractional year
fy = 2026 + (pd.Timestamp(latest_date).dayofyear - 1) / 365.25
lat_tot = latest.groupby("cat").n.sum()
for s in series_year:
    s["points"].append([round(fy, 2), int(lat_tot.get(s["name"], 0))])

prof = latest[(latest.band >= 200) & (latest.band < 2000)].groupby(["band", "cat"]).n.sum().unstack(fill_value=0)
series_prof = [{"name": c, "points": [[int(b) + 12.5, int(prof.loc[b, c]) if c in prof else 0] for b in prof.index], "color": col}
               for c, col in CATS]
tot_band = prof.sum(axis=1).sort_values(ascending=False)
top = [[f"{int(b)}-{int(b) + 25} km", int(n)] for b, n in tot_band.head(12).items()]

# growth of selected shells (all categories), July snapshots + latest
shells = [(400, "400-425 km (ISS shell)", "cyan"), (500, "500-525 km", "green"), (525, "525-550 km", "violet"),
          (550, "550-575 km", "orange"), (775, "775-800 km (debris belt)", "grey")]
series_shell = []
for b, nm, col in shells:
    d = jul[jul.band == b].groupby("year").n.sum()
    p = [[int(y), int(d.get(y, 0))] for y in range(1990, 2027)]
    p.append([round(fy, 2), int(latest[latest.band == b].n.sum())])
    series_shell.append({"name": nm, "points": p, "color": col})

# foundry candidate bands today
def band_count(lo, hi, df=latest):
    return int(df[(df.band >= lo) & (df.band < hi)].n.sum())


cand_counts = {"400-450 km": band_count(400, 450), "450-500 km": band_count(450, 500), "500-550 km": band_count(500, 550),
               "550-600 km": band_count(550, 600), "600-650 km": band_count(600, 650), "650-700 km": band_count(650, 700)}
star_share = {}
for lo, hi in ((500, 600), (525, 575), (300, 2000)):
    sub = latest[(latest.band >= lo) & (latest.band < hi)]
    star_share[f"{lo}-{hi}"] = sig(sub[sub.cat == "Starlink"].n.sum() / max(sub.n.sum(), 1), 3)
sl_band = latest[latest.cat == "Starlink"].groupby("band").n.sum().sort_values(ascending=False)
tot_all = latest.groupby("band").n.sum()
sl_top = [[f"{int(b)}-{int(b) + 25} km", int(n), sig(n / tot_all[b], 3)] for b, n in sl_band.head(6).items()]
sl_dom = [f"{int(b)}-{int(b) + 25}" for b in sorted(sl_band.index) if sl_band[b] / tot_all[b] > 0.5 and tot_all[b] >= 100]
for lo, hi in ((450, 500), (400, 450), (500, 550), (550, 600), (600, 650)):
    sub = latest[(latest.band >= lo) & (latest.band < hi)]
    star_share[f"{lo}-{hi}"] = sig(sub[sub.cat == "Starlink"].n.sum() / max(sub.n.sum(), 1), 3)
leo_1990 = int(leo.loc[1990].sum()); leo_2020 = int(leo.loc[2020].sum()); leo_now = int(lat_tot.sum())
ecc_frac = float(latest.n_ecc_gt_0p01.sum() / latest.n.sum())

# ------------------------------------------------------------------ assemble environment JSON
dc = agg["drag_counts"]
n_pass = int(sum(g["obj"] for g in dc["by_group"] if g["grp"] in ("DEB", "R/B")))
jobs_ids = [j["id"] for j in jobs["jobs"]]
cpu_h = sum(j["ncpus"] * j["elapsed_s"] for j in jobs["jobs"]) / 3600
wall_min = sum(j["elapsed_s"] for j in jobs["jobs"]) / 60
H500 = head.get("500-525km_high", {}); L500 = head.get("500-525km_low", {})
H400 = head.get("400-425km_high", {}); L400 = head.get("400-425km_low", {})
H600 = head.get("600-625km_high", {}); L600 = head.get("600-625km_low", {})
ls = {k: life_stats.get(f"{k}km", {}).get("BC150", {}) for k in (400, 450, 500, 550, 600, 650)}
ls50 = {k: life_stats.get(f"{k}km", {}).get("BC50", {}) for k in (400, 450, 500, 550, 600)}
h5 = {}
for BC in (BC_LO, BC_MID, BC_HI):
    d = life[(life.route == "msis") & (life.BC == BC)].sort_values("h0")
    d = d[d.med.notna()]
    h5[int(BC)] = float(np.interp(np.log(5.0), np.log(d.med.to_numpy(float)), d.h0.to_numpy(float)))
km_rb = {int(r.h): r.q50 for r in km[km.type == "R/B"].itertuples() if r.q50 is not None}

datasets = [
    {"name": "Space-Track TLE history, Hugging Face mirror juliensimon/space-track-tle-history",
     "url": "https://huggingface.co/datasets/juliensimon/space-track-tle-history",
     "license": "CC-BY-4.0 per the mirror card; data originate from Space-Track.org (18th/19th Space Defense Squadron), whose user agreement restricts redistribution, so we publish aggregates only",
     "records": ROWS, "bytes": BYTES, "accessed": "2026-10-24",
     "notes": f"All 68 yearly parquet files 1959-2026 (latest epoch {ys.tmax_date.max()[:10]}); {ROWS:,} element sets read in full."},
    {"name": "CelesTrak SATCAT", "url": "https://celestrak.org/pub/satcat.csv", "license": "CelesTrak public data (T.S. Kelso); cite CelesTrak",
     "records": 71139, "bytes": 6781690, "accessed": "2026-10-24", "notes": "Object type (PAY/R/B/DEB/UNK), operational status, owner, launch and decay dates, names (Starlink, OneWeb, Kuiper, Qianfan, Guowang = HULIANWANG DIGUI)."},
    {"name": "GFZ Potsdam Kp, ap, Ap, SN, F10.7 since 1932", "url": "https://kp.gfz-potsdam.de/app/files/Kp_ap_Ap_SN_F107_since_1932.txt",
     "license": "CC BY 4.0 (GFZ; Matzka et al. 2021, Space Weather 19, e2020SW002641); F10.7 from NRCan / DRAO Penticton", "records": 34630, "bytes": 5509921,
     "accessed": "2026-10-24", "notes": "Daily observed F10.7; we use an 81-day centred mean (F10.7a) and the daily Ap."},
    {"name": "NRLMSIS 2.1 empirical atmosphere (pymsis 0.13)", "url": "https://github.com/SWxTREC/pymsis", "license": "open source (pymsis, MIT-style; NRLMSIS distribution terms)",
     "records": 0, "bytes": 0, "accessed": "2026-10-24", "notes": "Empirical model driven by the observed F10.7/Ap; used for the foundry rescaling and lifetimes after checking it on the measured decay (Starshine 3, population solar response)."},
]

charts_env = [
    {"id": "g-vs-altitude", "kind": "line", "title": "Drag-induced quasi-steady acceleration vs altitude",
     "subtitle": f"Measured from the orbital decay of {n_pass:,} debris objects and rocket bodies, 1990-2026, split by solar activity",
     "x": {"label": "Mean altitude", "unit": "km", "scale": "linear"},
     "y": {"label": "Along-track drag deceleration", "unit": "g (9.80665 m/s2)", "scale": "log"},
     "series": series_g,
     "annotations": [{"x": 600, "y": 1e-6, "text": "ISS requirement 1 micro-g (published)"},
                     {"x": 600, "y": 2e-7, "text": "0.2 micro-g perpendicular (published)"}],
     "caption": ("Our computation on public data. Each point is the median over calendar months of the within-month median "
                 "a_d = -(da/dt) v / 2a for debris and rocket bodies on near-circular orbits (e < 0.01) in that 25 km band. "
                 f"Solar terciles use the 81-day F10.7: low < {T1:.0f} sfu, high >= {T2:.0f} sfu. Thin lines show the 10th "
                 "(low activity) and 90th (high activity) percentile object-months: debris fragments with large area-to-mass ratios "
                 "feel far more drag than compact bodies. The foundry curves are 0.5 rho v^2 / BC with NRLMSIS 2.1 density (model, checked "
                 f"against the measured decay of the Starshine 3 sphere and the population's solar response) for m/(Cd A) = {BC_MID:.0f} kg/m2 "
                 f"(our assumption; scale by {BC_MID:.0f}/BC for other designs). Drag is only one part of the quasi-steady "
                 "budget: gravity gradient adds about 0.39 micro-g per metre of radial offset from the centre of mass at these altitudes, "
                 "and the ISS requirement lines are for the ISS, not a demonstrated free-flyer environment.")},
    {"id": "lifetime-vs-altitude", "kind": "line", "title": "How long a passive foundry stays up",
     "subtitle": "Decay integrated through the real 1990-2026 solar record, from start dates every month 1990-2014",
     "x": {"label": "Starting altitude (circular)", "unit": "km", "scale": "linear"},
     "y": {"label": "Years until reentry (below 180 km)", "unit": "yr", "scale": "log"},
     "series": series_life + km_series,
     "caption": ("Simulation driven by real solar data, checked on measured decays. The foundry curves integrate da/dt = -a rho v / BC "
                 "with NRLMSIS 2.1 density and the observed daily 81-day F10.7 of 1990-2026 (wrapped after 2026); the spread is the start date "
                 "in the solar cycle. The green and grey lines are measured: Kaplan-Meier medians of how long real rocket bodies and debris "
                 "that crossed each altitude after 1990 took to reenter (censored at 1 Oct 2026). They carry those objects' own ballistic "
                 "coefficients (rocket bodies behave like BC ~ 50, debris lower), not a foundry's.")},
] + power["charts"]

findings = []
cal_txt = (f"NRLMSIS 2.1 reproduces the measured decay of the Starshine 3 sphere (known mass and size, BC {cal['BC_kg_m2']:.0f} kg/m2) "
           f"with a median measured/model ratio of {cal['ratio_measured_over_msis_median']:.2f} (IQR {cal['ratio_iqr'][0]:.2f}-{cal['ratio_iqr'][1]:.2f}, "
           f"{cal['n_10day_windows']} ten-day windows, 2001-2003)") if cal else "the model was not calibrated on a known sphere"
if H500 and L500:
    findings.append(
        f"In the 500-525 km band, drag on a foundry-like free-flyer (ballistic coefficient {BC_MID:.0f} kg/m2, our assumption) is about "
        f"{H500['foundry_g_BC150']:.1e} g in the high solar-activity tercile and {L500['foundry_g_BC150']:.1e} g in the low tercile "
        f"({H500['foundry_g_range_BC400_to_BC50'][0]:.0e}-{H500['foundry_g_range_BC400_to_BC50'][1]:.0e} g at solar high for BC 400-50). "
        f"That is {1e-6 / H500['foundry_g_BC150']:.0f} to {1e-6 / L500['foundry_g_BC150']:.0f} times below the ISS 1 micro-g quasi-steady requirement (published).")
if H400 and L400 and H600:
    findings.append(
        f"Altitude and the Sun matter about equally: the same foundry would feel {H400['foundry_g_BC150']:.1e} g (solar high) and {L400['foundry_g_BC150']:.1e} g (solar low) at 400-425 km, "
        f"and {H600['foundry_g_BC150']:.1e} and {L600['foundry_g_BC150']:.1e} g at 600-625 km. Measured decay of passive objects rises "
        f"{cons['500-525km']['measured_high_over_low']:.0f}x from the low to the high solar tercile at 500-525 km.")
if H500:
    findings.append(
        f"Measured directly from {n_pass:,} passive objects (debris and rocket bodies, with their own ballistic coefficients), the median object in the 500-525 km band decelerates at "
        f"{H500['passive_objects_median_g']:.1e} g in high solar activity (95% CI {H500['passive_objects_median_g_95ci_month_bootstrap'][0]:.1e}-{H500['passive_objects_median_g_95ci_month_bootstrap'][1]:.1e}, "
        f"bootstrap over {H500['n_months']} months) and {L500['passive_objects_median_g']:.1e} g in low activity; those objects behave like a ballistic coefficient of about "
        f"{H500['implied_population_BC_kg_m2']:.0f} kg/m2, so a heavier foundry feels proportionally less.")
findings.append(
    f"The model route used for the foundry curves is checked against our data two ways: {cal_txt}; and its solar-activity response is close to the measured one "
    f"(measured/model ratio of high-to-low drag {min(v['measured_over_model'] for v in cons.values()):.2f}-{max(v['measured_over_model'] for v in cons.values()):.2f} across the 300-625 km bands).")
findings.append(
    "Drag is not the binding microgravity constraint for a free-flyer above about 400 km: gravity gradient alone is about 0.4 micro-g per metre "
    "of radial distance from the centre of mass (3 n^2 r, our analytic computation), so cartridge placement near the centre of mass and the absence "
    "of crew, exercise and pumps (vibratory regime, which on the ISS reaches over 10 milli-g at high frequency without isolation, published) matter more than the altitude.")
if ls.get(500):
    findings.append(
        f"A dead foundry (BC {BC_MID:.0f}) reenters on its own in about {ls[400].get('median_yr')} years from 400 km, {ls[450].get('median_yr')} from 450 km, "
        f"{ls[500].get('median_yr')} from 500 km (range {ls[500].get('p10_yr')}-{ls[500].get('p90_yr')} with solar phase), {ls[550].get('median_yr')} from 550 km and "
        f"{ls[600].get('median_yr')} from 600 km. Only below about {h5[150]:.0f} km does a BC-150 foundry meet the 5-year post-mission disposal rule (FCC 2022, published) without propulsion; "
        f"a light BC-50 design meets it up to about {h5[50]:.0f} km and a dense BC-400 design only below {h5[400]:.0f} km. Real rocket bodies took a median {km_rb.get(500, float('nan')):.1f} years to reenter after crossing 500 km and {km_rb.get(400, float('nan')):.1f} after 400 km (Kaplan-Meier, measured), close to the model's BC-50 values ({ls50[500].get('median_yr')} and {ls50[400].get('median_yr')} yr).")
pw_dd = pw.get("Dawn-dusk SSO 600 km", {}); pw_iss = pw.get("ISS-like 51.6 deg, 420 km", {}); pw_sl = pw.get("Starlink-like 53 deg, 550 km", {})
pw_dd5 = pw.get("Dawn-dusk SSO 500 km", {})
findings.append(
    f"Power and heat: a dawn-dusk sun-synchronous orbit is sunlit {pw_dd5.get('sunlight_fraction_annual_mean', 0) * 100:.0f}% (500 km) to {pw_dd.get('sunlight_fraction_annual_mean', 0) * 100:.0f}% (600 km) of the year with "
    f"{pw_dd.get('days_with_eclipse')}-{pw_dd5.get('days_with_eclipse')} eclipse days and about {pw_dd.get('eclipse_cycles_per_year'):,}-{pw_dd5.get('eclipse_cycles_per_year'):,} thermal cycles per year (eclipses at most {pw_dd5.get('max_eclipse_min')} min, around the June solstice), versus "
    f"{pw_iss.get('sunlight_fraction_annual_mean', 0) * 100:.0f}% sunlight and ~{pw_iss.get('eclipse_cycles_per_year'):,} cycles for an ISS-like 51.6 deg orbit and "
    f"{pw_sl.get('sunlight_fraction_annual_mean', 0) * 100:.0f}% and ~{pw_sl.get('eclipse_cycles_per_year'):,} for a 53 deg Starlink-like orbit, with eclipses up to {pw_iss.get('max_eclipse_min')} min every orbit (analytic geometry, simulation).")

# ------------------------------------------------------------------ candidate-orbit trade table and recommendation
def objs_near(h, half=25):
    return int(latest[(latest.band >= h - half) & (latest.band < h + half)].n.sum())


def life_at(h, BC=BC_MID):
    d = life[(life.route == "msis") & (life.BC == BC)].sort_values("h0")
    d = d[d.med.notna()]
    return sig(float(np.exp(np.interp(h, d.h0.to_numpy(float), np.log(d.med.to_numpy(float))))), 3)


def g_at(h, s):
    d = fs[fs.sol == s].sort_values("h")
    return sig(float(np.exp(np.interp(h, d.h.to_numpy(float), np.log(d.g_f.to_numpy(float))))), 2)


trade = []
for name, h, key in (("Dawn-dusk SSO, 500 km", 500, "Dawn-dusk SSO 500 km"), ("Dawn-dusk SSO, 550 km", 550, "Dawn-dusk SSO 550 km"),
                     ("Dawn-dusk SSO, 600 km", 600, "Dawn-dusk SSO 600 km"),
                     ("ISS-like 51.6 deg, 420 km", 420, "ISS-like 51.6 deg, 420 km"), ("Starlink-like 53 deg, 550 km", 550, "Starlink-like 53 deg, 550 km")):
    p_ = pw[key]
    trade.append({"orbit": name, "altitude_km": h, "inclination_deg": p_["inclination_deg"],
                  "foundry_drag_g_solar_high": g_at(h, "high"), "foundry_drag_g_solar_low": g_at(h, "low"),
                  "passive_lifetime_yr_BC150_median": life_at(h), "passive_lifetime_yr_BC50_median": life_at(h, BC_LO),
                  "sunlight_fraction": p_["sunlight_fraction_annual_mean"], "eclipse_cycles_per_year": p_["eclipse_cycles_per_year"],
                  "max_eclipse_min": p_["max_eclipse_min"], "catalogued_objects_within_25km_now": objs_near(h)})
tt = {t["orbit"]: t for t in trade}
dd5, dd55, dd6, iss_, slk = (tt["Dawn-dusk SSO, 500 km"], tt["Dawn-dusk SSO, 550 km"], tt["Dawn-dusk SSO, 600 km"],
                              tt["ISS-like 51.6 deg, 420 km"], tt["Starlink-like 53 deg, 550 km"])
findings.append(
    "Candidate band, as our computation and not a design decision: on these numbers a dawn-dusk sun-synchronous orbit at about 525-575 km balances the four constraints best "
    f"if the foundry carries a deorbit capability. At 550 km, drag on a BC-150 foundry is {dd55['foundry_drag_g_solar_low']:.0e}-{dd55['foundry_drag_g_solar_high']:.0e} g, sunlight {dd55['sunlight_fraction'] * 100:.0f}% "
    f"with ~{dd55['eclipse_cycles_per_year']:,} thermal cycles a year (vs ~{iss_['eclipse_cycles_per_year']:,} at 51.6 deg), and {dd55['catalogued_objects_within_25km_now']:,} catalogued objects sit within 25 km "
    f"(vs {cand_counts['450-500 km']:,} in Starlink's 450-500 km region just below). Trade-offs: a dead BC-150 foundry would stay up ~{dd55['passive_lifetime_yr_BC150_median']:.0f} years there "
    f"(~{dd55['passive_lifetime_yr_BC50_median']:.0f} for BC 50), far beyond the 5-year rule, so disposal must be propulsive. The alternative, an ISS-like ~420 km orbit, self-disposes in ~{iss_['passive_lifetime_yr_BC150_median']:.0f} years "
    f"and has only {iss_['catalogued_objects_within_25km_now']:,} neighbours, but drag is ~{iss_['foundry_drag_g_solar_high'] / dd55['foundry_drag_g_solar_high']:.0f}x higher (still < 0.1 micro-g), it needs reboosts, and it sees "
    f"{iss_['sunlight_fraction'] * 100:.0f}% sunlight and ~{iss_['eclipse_cycles_per_year']:,} eclipses a year. "
    "SSO launch costs more delta-v than 51.6 deg and has no crew-station access; and the result rests on public TLE crowding, an assumed BC and a model atmosphere checked on one sphere.")

stats_env = {
    "candidate_orbit_trade_table": trade,
    "passive_5yr_disposal_max_altitude_km_by_BC": {str(k): round(v) for k, v in h5.items()},
    "headline_by_altitude_and_solar_tercile": head,
    "solar_terciles_F107a_sfu": {"low_below": round(T1, 1), "high_at_or_above": round(T2, 1),
                                 "reference_period": "1990-01-01 to 2026-10-24, 81-day centred mean of observed F10.7",
                                 "tercile_medians": sol["ref"]},
    "drag_sample": dc,
    "ndot_cross_check": agg["ndot_check"],
    "solar_response_check_measured_vs_msis": cons,
    "starshine3_calibration": ({k: v for k, v in cal.items() if k != "series"} if cal else None),
    "rejected_route_bstar": {
        "what": "Effective density from rho = 2 a_d / (v^2 B), B = 12.741621 B* (Hoots & Roehrich 1980 nominal conversion), object lifetime-median B*.",
        "why_rejected": "Median B* of the same population at 500-550 km swings ~30x with the solar cycle (e.g. 6.6e-5 in 2009 vs 2.8e-3 in 2002), i.e. B* absorbs atmospheric-density error and is not a physical ballistic coefficient. "
                        "The resulting density was 3-35x NRLMSIS (ratio growing with altitude) and gave lifetimes far shorter than real rocket bodies show, so it is not used.",
        "ratio_bstar_route_over_msis": {f"{int(r.band)}-{int(r.band) + 25}km_{r.sol}": sig(r.rho_bstar_ratio, 3) for r in fs.itertuples() if r.band in (300, 400, 500, 600, 700) and np.isfinite(r.rho_bstar_ratio)},
        "BC_from_Bstar_quantiles_kg_m2": agg["bc_obj_quantiles"]},
    "foundry_ballistic_coefficient_assumption": {
        "BC_kg_m2": {"low": BC_LO, "central": BC_MID, "high": BC_HI},
        "definition": "BC = m / (Cd A), Cd ~ 2.2",
        "rationale": "Central: a ~10 t free-flyer with ~30 m2 mean projected area including arrays (10000/(2.2*30) ~ 150 kg/m2). "
                     "Low: lighter body with large face-on arrays. High: compact dense module with arrays edge-on. "
                     "Drag acceleration scales exactly as 1/BC, so any other design is a linear rescale."},
    "gravity_gradient_micro_g_per_m": {"400km": sig(3 * MU / (RE + 400e3) ** 3 / G0 * 1e6, 3), "500km": sig(3 * MU / (RE + 500e3) ** 3 / G0 * 1e6, 3),
                                       "600km": sig(3 * MU / (RE + 600e3) ** 3 / G0 * 1e6, 3),
                                       "note": "radial gravity-gradient term 3 n^2 r per metre offset from the centre of mass (our analytic computation)"},
    "lifetime_years": life_stats,
    "kaplan_meier_real_objects": agg["km"],
    "power_thermal": pw,
    "iss_reference_published": {
        "quasi_steady_requirement": "1 micro-g magnitude and 0.2 micro-g perpendicular component, below 0.01 Hz, in at least 50% of payload rack locations, "
                                    "for 180 days/yr in 30-day increments; transient limits 1000 micro-g peak and 10 micro-g-s per 10 s per axis "
                                    "(Del Basso et al., AIAA 2003-1002, NASA NTRS 20100042410; ISS SSP 41000).",
        "assembly_complete_verification": "14 of 32 payload rack locations met the quasi-steady requirement in analysis; the 15th and 16th were at 1.11 and 1.17 micro-g (same source).",
        "measured_environment": "Quasi-steady accelerations below 0.01 Hz are 'on the order of less than a micro-g'; the unisolated vibratory spectrum reaches 'well over 10 milli-g' at the high-frequency end, "
                                "isolation reduces it by up to 100x; structural modes are quieter during crew sleep (McPherson, Hrovat, Kelly, Keller, NASA ISS Researcher's Guide: Acceleration Environment, NP-2015-11-040-JSC).",
        "sources": ["https://ntrs.nasa.gov/citations/20100042410",
                    "https://www.nasa.gov/wp-content/uploads/2016/06/acceleration-environment-iss-mini-book_detail-508c.pdf"]},
    "iss_acceleration_data_probe": {
        "result": "not openly downloadable from our environment on 2026-10-24",
        "detail": "PIMS documents its PAD archive at http://pims.grc.nasa.gov/ftp/pad (SAMS, MAMS, MMA). The pims.grc.nasa.gov host did not resolve from MIT Engaging or from a home network; "
                  "the gipoc.grc.nasa.gov/pims/ftp/pad mirror returned HTTP 403 for the root and dated paths; the 'pub/pad' link resolves to a documents page. "
                  "No crew-sleep vs awake contrast was computed; we cite the PIMS published characterisation instead.",
        "pages": ["https://gipoc.grc.nasa.gov/wp/pims/acceleration-archives/"]},
}

env = {
    "id": "orbit-environment", "tab": "foundry",
    "title": "What a free-flying foundry feels in each orbit: drag, lifetime, sunlight",
    "question": "How quiet (residual drag acceleration), how long-lived and how sunlit is each candidate low-Earth-orbit band for a free-flying foundry, measured from 68 years of tracking data?",
    "headline": {"value": f"{H500.get('foundry_g_BC150', 0) * 1e9:.2g}", "unit": "nano-g at 500-525 km, active Sun",
                 "text": (f"From {ROWS / 1e6:.0f} million tracking records: drag on a foundry-sized free-flyer (our assumed BC {BC_MID:.0f} kg/m2) at 500-525 km is about "
                          f"{H500.get('foundry_g_BC150', 0) * 1e9:.2g} nano-g in active-Sun years and {L500.get('foundry_g_BC150', 0) * 1e9:.2g} nano-g in quiet years, "
                          f"{round(1e-6 / H500.get('foundry_g_BC150', 1), -1):.0f}-{round(1e-6 / L500.get('foundry_g_BC150', 1), -1):.0f} times below the ISS 1 micro-g requirement.") if H500 else ""},
    "evidence_level": "our computation on public data",
    "datasets": datasets,
    "compute": {"where": "MIT Engaging", "partitions": sorted(set(j["partition"] for j in jobs["jobs"])), "job_ids": jobs_ids,
                "cpu_hours": round(cpu_h, 3), "wall_minutes": round(wall_min, 1), "peak_storage_gb": jobs.get("peak_storage_gb", 13.0)},
    "method": [
        "Downloaded all 68 yearly parquet files of the Space-Track TLE mirror (12.5 GB) plus CelesTrak SATCAT and GFZ F10.7 to Engaging scratch (mit_data_transfer).",
        "Per year (16-CPU job): semi-major axis a = (mu/n^2)^(1/3) from each element set's mean motion; kept debris, rocket bodies and payloads flagged non-operational, e < 0.01, mean altitude 150-1000 km, skipping the first 30 days after launch.",
        "For each element set, paired it with the first set of the same object at least 4 days later (3-8 day gap), da/dt = delta a / delta t; dropped pairs with |delta a| > 30 km (cross-tags).",
        "Took the median da/dt per object and calendar month (>= 3 pairs, altitude spread < 40 km); a_d = -(da/dt) v / (2a), v = sqrt(mu/a), g-level = a_d / 9.80665.",
        "Cross-checked against the TLE mean-motion-derivative field (n-dot/2): median ratio of the two decay-rate estimates 0.95, IQR 0.84-1.03 over 1.4 million object-months (stats.ndot_cross_check).",
        "Grouped object-months by 25 km band and by solar-activity tercile of the 81-day F10.7; statistic = median over months of within-month medians, 95% CI by bootstrapping months (months, not objects, are the independent units, since all objects in a month share one atmosphere).",
        "Foundry scaling: a_d = 0.5 rho v^2 / BC for BC = m/(Cd A) = 50, 150 (central), 400 kg/m2, with rho the orbit-averaged NRLMSIS 2.1 density at each band's centre and the tercile-median F10.7 and Ap.",
        "Checked that model route on data: (i) against the measured decay of the Starshine 3 sphere (known 91 kg, 0.94 m; BC ~ 60 kg/m2), pair by pair with that day's F10.7 and Ap; (ii) the measured high/low-tercile drag ratio of the passive population vs the model's ratio, band by band.",
        "Tried and rejected a B*-based density route (B* tracks the solar cycle ~30x, so it is not a ballistic coefficient); details in stats.rejected_route_bstar.",
        "Lifetime: integrated da/dt = -a rho v / BC day by day with NRLMSIS 2.1 driven by the observed daily 81-day F10.7 of 1990-2026 (wrapped), from start dates every month 1990-2014, down to 180 km.",
        "Kaplan-Meier: residence time of real debris and rocket bodies from first crossing below each altitude (after 1990) to the SATCAT decay date, censored at 2026-10-01.",
        "Power: analytic beta angle and cylindrical-shadow eclipse fraction for each candidate orbit through 2027 with J2 node regression, checked by brute-force propagation.",
    ],
    "charts": charts_env,
    "stats": stats_env,
    "findings": findings,
    "limitations": [
        "The measured objects are debris and rocket bodies, not foundries. Their g-levels are real measurements; the foundry curves rescale them through a model atmosphere (NRLMSIS 2.1) and an assumed ballistic coefficient, checked against one known-BC sphere (Starshine 3, solar-maximum years only) and the population's solar response. The absolute level is therefore uncertain by roughly the Starshine spread plus the BC assumption, which dominates (a factor 8 across BC 50-400).",
        "TLE B* could not be used as a ballistic coefficient: it tracks the solar cycle (~30x), so per-object ballistic coefficients of the measured population are not known; we only infer an effective population value through the model.",
        "Co-rotation of the atmosphere lowers the relative speed by ~4% (v^2 by ~8%) for 51.6-53 deg orbits and raises it slightly for sun-synchronous orbits; the foundry curves use the inertial speed.",
        "TLE mean elements smooth over each fit span; the result is an orbit-averaged, quasi-steady (<< 0.01 Hz) along-track drag. It says nothing about vibration, attitude-control, venting or crew disturbances, and does not include the gravity-gradient and rotational terms that depend on where a cartridge sits relative to the centre of mass.",
        "Some 'non-operational' payloads may have manoeuvred earlier in life; debris can be cross-tagged. Medians per object-month and the 30 km jump cut limit, but do not eliminate, these effects. Results for payloads are kept separate (stats are dominated by debris and rocket bodies).",
        "Solar terciles pool three solar cycles (22-25). Cycle-to-cycle differences and geomagnetic storms (e.g. the 2024 May storm) are inside the spread, not modelled separately.",
        "Lifetimes assume a constant BC, no attitude change and the 1990-2026 solar sequence repeated; real decays depend on future cycles. They are a planning estimate, not a disposal analysis.",
        "Power/thermal uses circular orbits and a cylindrical shadow (no penumbra, no atmosphere), which slightly underestimates eclipse length (< 1 min).",
        "ISS acceleration data (PIMS) could not be downloaded today; ISS numbers are published values, not our computation.",
    ],
    "future_big_data": [
        "CelesTrak SupGP: operator-supplied ephemerides for Starlink, OneWeb, Kuiper and others, to measure shell occupancy and manoeuvre rates at higher fidelity than TLEs.",
        "GRACE-FO and Swarm accelerometer Level-1B/ACC data (ESA/NASA/GFZ): direct measurement of non-gravitational acceleration at 400-500 km, to replace the B*-based density route with measured densities and to see orbit-period variations a free-flyer would feel.",
        "Conjunction screening for a foundry fleet: propagate candidate foundry orbits against the full catalogue (or SupGP) for a year to count close approaches per shell, and estimate avoidance manoeuvres (which themselves disturb microgravity).",
        "Space-Track decay and reentry messages (TIP) to calibrate the lifetime model on known-ballistic-coefficient spheres (ANDE, Starshine-class objects).",
        "ISS PIMS SAMS/MAMS PAD archive, if access is restored: crew-sleep vs awake vibratory spectra as the baseline a crew-free foundry would beat.",
        "NOAA SWPC solar-cycle-25/26 forecasts to replace the repeated 1990-2026 F10.7 record in lifetime estimates.",
    ],
    "partners": [
        {"name": "SpaceX (Starlink space-safety and Stargaze)", "why": "Operates most objects in the 500-575 km shells a foundry would share and runs conjunction screening/ephemeris sharing for other operators.",
         "evidence": f"Starlink is {star_share.get('450-500', 0) * 100:.0f}% of the {cand_counts['450-500 km']:,} catalogued objects at 450-500 km and {star_share.get('300-2000', 0) * 100:.0f}% of everything in LEO on {latest_date} (orbit-crowding.json)."},
        {"name": "LeoLabs", "why": "Commercial radar tracking of LEO with higher cadence than public TLEs; conjunction and manoeuvre detection for a foundry fleet.",
         "evidence": "Our drag and crowding numbers come from public TLE averages; independent tracking would tighten both."},
        {"name": "NOAA SWPC", "why": "Solar-cycle and F10.7 forecasts drive both foundry drag (x several between solar min and max) and orbital lifetime.",
         "evidence": f"The measured drag level rises {cons['500-525km']['measured_high_over_low']:.0f}x from the low to the high solar tercile at 500-525 km (stats.solar_response_check_measured_vs_msis)."},
        {"name": "NASA Glenn PIMS / ISS National Lab", "why": "Owners of the ISS acceleration record (SAMS/MAMS) and the microgravity requirements a foundry would be compared with.",
         "evidence": "Published ISS quasi-steady requirement 1 micro-g; the public PAD archive was not reachable today."},
        {"name": "ESA / GFZ (Swarm, GRACE-FO accelerometers)", "why": "Direct non-gravitational acceleration and thermosphere density products at foundry-like altitudes.",
         "evidence": "Our density route relies on TLE B*; accelerometer-derived densities would replace that proxy."},
        {"name": "Space-Track.org / 18th & 19th Space Defense Squadrons; CelesTrak", "why": "Source of the catalogue and element sets used here; redistribution terms govern what we can publish.",
         "evidence": f"{ROWS:,} element sets processed."},
    ],
    "code": ["analysis/bigdata/orbit_process.py", "analysis/bigdata/orbit_analyze.py", "analysis/bigdata/orbit_calib.py",
             "analysis/bigdata/orbit_power.py", "analysis/bigdata/orbit_build.py", "cluster/bigdata/orbit-download.sbatch",
             "cluster/bigdata/orbit-process.sbatch", "cluster/bigdata/orbit-analyze.sbatch", "cluster/bigdata/orbit-calib.sbatch",
             "docs/appendix/orbit.md"],
    "reproduce": [
        "rsync -az analysis/bigdata cluster/bigdata engaging:~/orcd/scratch/orbital-foundry-20261024-01a170b7/",
        "ssh engaging 'cd ~/orcd/scratch/orbital-foundry-20261024-01a170b7/bigdata/orbit && sbatch ../orbit-download.sbatch'",
        "ssh engaging 'cd ~/orcd/scratch/orbital-foundry-20261024-01a170b7/bigdata/orbit && sbatch --export=ALL,YEARS=1959-2026,WORKERS=8 ../orbit-process.sbatch'",
        "ssh engaging 'cd ~/orcd/scratch/orbital-foundry-20261024-01a170b7/bigdata/orbit && sbatch ../orbit-analyze.sbatch && sbatch ../orbit-calib.sbatch'",
        "rsync -az engaging:~/orcd/scratch/orbital-foundry-20261024-01a170b7/bigdata/orbit/work/orbit_{agg,calib}.json <local>/",
        "python analysis/bigdata/orbit_power.py power.json && python analysis/bigdata/orbit_build.py orbit_agg.json power.json jobs.json orbit_calib.json",
    ],
    "generated_at": NOW,
}

# ------------------------------------------------------------------ crowding JSON
crowd = {
    "id": "orbit-crowding", "tab": "network",
    "title": "How crowded each low-Earth-orbit shell is, 1990 to today",
    "question": "Which altitude shells would a foundry fleet share, with whom, and how fast are they filling?",
    "headline": {"value": f"{leo_now:,}", "unit": "catalogued objects below 2,000 km",
                 "text": f"On {latest_date} the public catalogue tracks {leo_now:,} objects in low Earth orbit, up from {leo_1990:,} in 1990 and {leo_2020:,} in 2020; "
                         f"{star_share.get('450-500', 0) * 100:.0f}% of the objects between 450 and 500 km are Starlink satellites."},
    "evidence_level": "our computation on public data",
    "datasets": datasets[:2],
    "compute": env["compute"],
    "method": [
        "For each year 1990-2026, took the last element set of every object in the 30 days before 1 July (and the last 30 days of data for 'today').",
        "Assigned each object to a 25 km band of mean altitude a - 6378.137 km (100-2000 km).",
        "Categorised with CelesTrak SATCAT: Starlink (PAY named STARLINK*), other megaconstellations (ONEWEB*, KUIPER*, QIANFAN*, HULIANWANG*/Guowang), other payloads, rocket bodies, debris and unknown.",
    ],
    "charts": [
        {"id": "leo-by-year", "kind": "stacked", "title": "Catalogued objects below 2,000 km, by type",
         "subtitle": "1 July snapshot each year; last point is today", "x": {"label": "Year", "unit": "", "scale": "linear"},
         "y": {"label": "Objects", "unit": "count", "scale": "linear"}, "series": series_year,
         "caption": "Our computation on public data. Only objects the US catalogue tracks publicly (roughly > 10 cm in LEO); classified objects and untracked debris are missing. "
                    "The 2007 Fengyun-1C test and 2009 Iridium-Cosmos collision show as debris steps; the post-2019 rise is Starlink."},
        {"id": "profile-today", "kind": "stacked", "title": f"Objects per 25 km shell today ({latest_date})",
         "subtitle": "Mean altitude band centre", "x": {"label": "Mean altitude", "unit": "km", "scale": "linear"},
         "y": {"label": "Objects in band", "unit": "count", "scale": "linear"}, "series": series_prof,
         "caption": "Our computation on public data. Eccentric objects are assigned to their mean altitude, so they cross more shells than shown "
                    f"({ecc_frac * 100:.0f}% of today's sample has e > 0.01)."},
        {"id": "shell-growth", "kind": "line", "title": "Growth of selected shells",
         "subtitle": "All object types, 1 July snapshots", "x": {"label": "Year", "unit": "", "scale": "linear"},
         "y": {"label": "Objects in shell", "unit": "count", "scale": "linear"}, "series": series_shell,
         "caption": "Our computation on public data. Counts, not collision probabilities: risk also depends on relative velocity, object size and manoeuvrability."},
        {"id": "top-shells", "kind": "hbar", "title": "The most crowded 25 km shells today", "subtitle": latest_date,
         "x": {"label": "Shell", "unit": "", "scale": "category"}, "y": {"label": "Objects", "unit": "count", "scale": "linear"},
         "series": [{"name": "Objects", "points": top, "color": "orange"}],
         "caption": "Our computation on public data (mean-altitude bands)."},
    ],
    "stats": {"starlink_top_shells_now_count_share": sl_top, "starlink_majority_shells_now": sl_dom,
              "altitude_definition": "mean altitude = semi-major axis from TLE mean motion minus 6378.137 km (equatorial radius); typically 5-10 km below altitudes quoted by operators",
              "latest_snapshot": latest_date, "leo_total_now": leo_now, "leo_total_1990": leo_1990, "leo_total_2020": leo_2020,
              "foundry_candidate_bands_now": cand_counts, "starlink_share": star_share, "top_shells_now": top,
              "fraction_eccentric_gt_0p01_now": round(ecc_frac, 3),
              "by_category_now": {k: int(v) for k, v in lat_tot.items()}},
    "findings": [
        f"The public catalogue holds {leo_now:,} objects below 2,000 km on {latest_date}, {leo_now / leo_1990:.1f}x the 1990 count and {leo_now / leo_2020:.1f}x the 2020 count.",
        f"The most crowded 25 km shell today is {top[0][0]} with {top[0][1]:,} objects, then {top[1][0]} ({top[1][1]:,}); both are mostly Starlink. The next most crowded shells are the old debris belts at 750-850 km.",
        f"Candidate foundry bands today: " + ", ".join(f"{k}: {v:,}" for k, v in cand_counts.items()) + " objects.",
        f"Starlink dominates the 450-500 km region today ({star_share['450-500'] * 100:.0f}% of {cand_counts['450-500 km']:,} objects; its largest shells: "
        + ", ".join(f"{b} ({n:,}, {f * 100:.0f}%)" for b, n, f in sl_top[:3]) + "). The 400-450 km and 500-650 km bands each hold about 500-1,200 objects, so a foundry "
        "placed just above or below the Starlink shells avoids the densest traffic while staying in the drag regime where it would deorbit itself.",
    ],
    "limitations": [
        "Public TLE catalogue only (~10 cm and larger in LEO); classified objects and small debris are missing, and tracking capacity grew over time (1990s counts are lower partly for that reason).",
        "Snapshot uses objects with an element set in the prior 30 days; objects with sparse tracking can drop out of a given year.",
        "Mean-altitude assignment understates how many shells eccentric objects cross, and 'altitude' here is a - 6378.137 km, typically 5-10 km below altitudes quoted by operators (e.g. Starlink shells announced by SpaceX at ~480 km appear at 450-475 km).",
        "Object counts are not collision risk; they ignore relative velocity, size and the fact that active satellites manoeuvre.",
    ],
    "future_big_data": env["future_big_data"][:1] + env["future_big_data"][2:3],
    "partners": env["partners"][:2] + env["partners"][5:],
    "code": env["code"], "reproduce": env["reproduce"], "generated_at": NOW,
}

def clean(o):
    """Recursively replace NaN/inf by None and numpy scalars by Python numbers."""
    if isinstance(o, dict):
        return {str(k): clean(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)):
        return [clean(v) for v in o]
    if isinstance(o, (np.integer,)):
        return int(o)
    if isinstance(o, (float, np.floating)):
        return float(o) if np.isfinite(o) else None
    return o


for obj, name in ((env, "orbit-environment.json"), (crowd, "orbit-crowding.json")):
    s = json.dumps(clean(obj), indent=1, allow_nan=False)
    open(f"{OUTDIR}/{name}", "w").write(s)
    print(name, len(s), "bytes")
print(json.dumps(H500, indent=1))
print(findings)
