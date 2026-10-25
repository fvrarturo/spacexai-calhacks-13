#!/usr/bin/env python
"""Orbit workstream: calibrate the NRLMSIS 2.1 density route against a passive object whose
ballistic coefficient is known from its build: the Starshine 3 sphere (NORAD 26929, launched
2001-09-30, reentered 2003-01-21; 91 kg, 0.94 m diameter, published by ILRS / eoPortal / NASA).

For each pair of element sets 3-8 days apart: measured a_d = -(da/dt) v / 2a, versus the model
a_d = 0.5 rho_MSIS v_rel^2 / BC with rho averaged over the orbit (latitudes within the 67 deg
inclination, all longitudes) at the pair's mid-epoch, using that day's F10.7 (previous day), the
81-day centred F10.7 and the daily Ap. The ratio measured/model tests the absolute level of the
model route used for the foundry curves.
Usage: python orbit_calib.py ROOT OUT.json
"""
import json
import os
import sys

import numpy as np
import pandas as pd
import pyarrow.parquet as pq
import pyarrow.compute as pc
import pymsis

ROOT, OUT = sys.argv[1], sys.argv[2]
MU, RE, G0, OMEGA_E = 3.986004418e14, 6378.137e3, 9.80665, 7.2921159e-5
OBJ = {"name": "STARSHINE 3", "norad": 26929, "mass_kg": 91.0, "mass_range": [88.0, 91.0],
       "diam_m": 0.94, "diam_range": [0.94, 1.0], "cd": 2.2, "cd_range": [2.1, 2.3]}

cols = ["Y", "M", "D", "days", "days_m", "Bsr", "dB"] + [f"Kp{i}" for i in range(8)] + \
       [f"ap{i}" for i in range(8)] + ["Ap", "SN", "F107obs", "F107adj", "Dflag"]
sw = pd.read_csv(os.path.join(ROOT, "raw/solar/Kp_ap_Ap_SN_F107_since_1932.txt"), comment="#", sep=r"\s+", names=cols)
sw["date"] = pd.to_datetime(dict(year=sw.Y, month=sw.M, day=sw.D))
sw = sw.set_index("date")
sw["F107a"] = sw.F107obs.where(sw.F107obs > 0).rolling(81, center=True, min_periods=40).mean()

parts = []
for y in (2001, 2002, 2003):
    t = pq.read_table(os.path.join(ROOT, f"raw/tle/tle_{y}.parquet"),
                      columns=["norad_id", "epoch", "mean_motion", "eccentricity", "inclination", "bstar"],
                      filters=[("norad_id", "=", OBJ["norad"])])
    parts.append(t.to_pandas())
d = pd.concat(parts).sort_values("epoch").drop_duplicates("epoch")
d["t"] = (d.epoch - d.epoch.iloc[0]).dt.total_seconds() / 86400
n = d.mean_motion.to_numpy() * 2 * np.pi / 86400
d["a"] = (MU / n ** 2) ** (1 / 3)
d["alt"] = d.a / 1e3 - RE / 1e3
t = d.t.to_numpy(); a = d.a.to_numpy()
j = np.searchsorted(t, t + 4.0)
ok = j < len(d)
jj = np.where(ok, j, 0)
dt = t[jj] - t
ok &= (dt >= 3) & (dt <= 8)
rows = []
inc = np.deg2rad(float(d.inclination.median()))
BC = OBJ["mass_kg"] / (OBJ["cd"] * np.pi * OBJ["diam_m"] ** 2 / 4)
for i in np.where(ok)[0]:
    k = jj[i]
    amid = 0.5 * (a[i] + a[k]); hmid = amid / 1e3 - RE / 1e3
    if hmid < 200:
        continue
    v = np.sqrt(MU / amid)
    dadt = (a[k] - a[i]) / (dt[i] * 86400)
    ad = -dadt * v / (2 * amid)
    tmid = d.epoch.iloc[i] + (d.epoch.iloc[k] - d.epoch.iloc[i]) / 2
    day = tmid.tz_convert(None).normalize() if tmid.tzinfo else tmid.normalize()
    F = float(sw.F107obs.get(day - pd.Timedelta(days=1), np.nan)); Fa = float(sw.F107a.get(day, np.nan))
    Ap = float(sw.Ap.get(day, np.nan))
    lats = np.arange(-60, 61, 10.0); lons = np.arange(0, 360, 30.0)
    LA, LO = np.meshgrid(lats, lons, indexing="ij")
    # weight latitudes by time spent there on an inclined circular orbit
    w = 1 / np.sqrt(np.clip(np.sin(inc) ** 2 - np.sin(np.deg2rad(LA)) ** 2, 1e-3, None))
    N = LA.size
    res = pymsis.calculate(np.repeat(np.datetime64(tmid.tz_convert(None) if tmid.tzinfo else tmid, "s"), N),
                           LO.ravel(), LA.ravel(), np.full(N, hmid), f107s=np.full(N, F), f107as=np.full(N, Fa),
                           aps=np.full((N, 7), Ap), version=2.1)
    rho = float(np.sum(res[..., 0].ravel() * w.ravel()) / np.sum(w))
    vrel2 = v ** 2 * (1 - OMEGA_E * amid * np.cos(inc) / v) ** 2
    ad_model = 0.5 * rho * vrel2 / BC
    ad_model_norot = 0.5 * rho * v ** 2 / BC
    rows.append(dict(t=str(tmid)[:19], h=hmid, F107=F, F107a=Fa, Ap=Ap, ad=ad, ad_model=ad_model,
                     ratio=ad / ad_model, ratio_norot=ad / ad_model_norot))
r = pd.DataFrame(rows)
# one value per 10-day window to limit overlap between pairs
r["win"] = (pd.to_datetime(r.t) - pd.to_datetime(r.t).min()).dt.days // 10
w10 = r.groupby("win").agg(h=("h", "median"), ratio=("ratio", "median"), ratio_norot=("ratio_norot", "median"),
                           F107a=("F107a", "median"), g=("ad", lambda x: np.median(x) / G0)).reset_index()
bands = []
for lo, hi in ((400, 480), (300, 400), (200, 300)):
    s = w10[(w10.h >= lo) & (w10.h < hi)]
    if len(s):
        bands.append(dict(band=f"{lo}-{hi} km", n_windows=int(len(s)), ratio_median=float(s.ratio.median()),
                          ratio_iqr=[float(s.ratio.quantile(.25)), float(s.ratio.quantile(.75))],
                          F107a_median=float(s.F107a.median())))
# BC uncertainty envelope from published mass/diameter/Cd ranges
bc_lo = OBJ["mass_range"][0] / (OBJ["cd_range"][1] * np.pi * OBJ["diam_range"][1] ** 2 / 4)
bc_hi = OBJ["mass_range"][1] / (OBJ["cd_range"][0] * np.pi * OBJ["diam_range"][0] ** 2 / 4)
out = {"object": OBJ, "BC_kg_m2": BC, "BC_range_kg_m2": [bc_lo, bc_hi], "n_element_sets": int(len(d)),
       "n_pairs": int(len(r)), "n_10day_windows": int(len(w10)),
       "first_epoch": str(d.epoch.iloc[0])[:19], "last_epoch": str(d.epoch.iloc[-1])[:19],
       "alt_first_km": float(d.alt.iloc[0]), "alt_last_km": float(d.alt.iloc[-1]),
       "ratio_measured_over_msis_median": float(w10.ratio.median()),
       "ratio_iqr": [float(w10.ratio.quantile(.25)), float(w10.ratio.quantile(.75))],
       "ratio_no_corotation_median": float(w10.ratio_norot.median()),
       "by_band": bands,
       "series": [[round(float(h), 1), round(float(x), 3)] for h, x in zip(w10.h, w10.ratio)]}
json.dump(out, open(OUT, "w"), indent=1)
print(json.dumps({k: v for k, v in out.items() if k != "series"}, indent=1))
