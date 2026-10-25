#!/usr/bin/env python
"""Orbit workstream, stage 2: turn the per-year reductions into aggregate results.

Inputs (cluster scratch): work/reduced/{drag,crowd,cross,stats}_<year>.*, the CelesTrak SATCAT and
the GFZ Potsdam Kp/Ap/SN/F10.7 file. Output: one JSON of aggregates (no raw TLEs), merged into the
site result files by orbit_build.py on the laptop.

Analyses
 1. Residual drag acceleration of passive objects (debris, rocket bodies, non-operational payloads)
    on near-circular orbits: a_d = -(da/dt) v/(2a), by 25 km altitude band and solar-activity tercile
    (81-day centred F10.7 over 1990-2026). Unit of replication = calendar month (all objects in a
    month share one atmosphere): we take the median over objects within each month, then the median
    over months, with a month-cluster bootstrap CI.
 2. Scaling to a foundry ballistic coefficient BC_f = m/(Cd A). Two independent density routes:
    (a) TLE route: rho_eff = 2 a_d / (v^2 B_obj), B_obj = 12.741621 * B* (m^2/kg), with B* the
        object's lifetime-median value (a per-month B* would absorb the solar cycle and make the
        estimate circular);
    (b) model route: NRLMSIS 2.1 (pymsis) at the same altitude and F10.7, orbit-averaged.
    Foundry a_d = 0.5 rho v^2 / BC_f.
    OUTCOME (2026-10-24 run): route (a) was REJECTED. Median B* of the same population swings ~30x
    with the solar cycle, so B* is not a physical ballistic coefficient; route (a) density came out
    3-35x NRLMSIS. orbit_build.py uses route (b), checked on the Starshine 3 sphere (orbit_calib.py)
    and on the measured solar-activity response. Route (a) is still computed here for the record.
 3. Lifetime: integrate da/dt = -a rho v / BC_f from each start altitude down to 180 km through the
    real daily F10.7 history (start dates every month 1990-2014; series wrapped after 2026), with
    rho(h, F10.7) fitted to route (a); MSIS route as a check. Plus a Kaplan-Meier of the actual
    residence time of passive objects below each threshold altitude until their catalogued decay.
 4. Crowding: catalogued objects per 25 km mean-altitude band and category, 1 July each year and the
    latest 30 days.
"""
import glob
import json
import os
import sys

import numpy as np
import pandas as pd

MU = 3.986004418e14
RE = 6378.137e3
G0 = 9.80665
BSTAR_TO_B = 12.741621          # B (m^2/kg) = 2 B*/rho0, rho0 = 0.15696615 kg/m^2/ER (Hoots & Roehrich 1980)
rng = np.random.default_rng(20261024)

ROOT = sys.argv[1]
OUT = sys.argv[2]
RED = os.path.join(ROOT, "work", "reduced")


# ---------------------------------------------------------------- solar activity
def load_solar():
    cols = ["Y", "M", "D", "days", "days_m", "Bsr", "dB"] + [f"Kp{i}" for i in range(8)] + \
           [f"ap{i}" for i in range(8)] + ["Ap", "SN", "F107obs", "F107adj", "Dflag"]
    sw = pd.read_csv(os.path.join(ROOT, "raw/solar/Kp_ap_Ap_SN_F107_since_1932.txt"), comment="#",
                     sep=r"\s+", names=cols)
    sw["date"] = pd.to_datetime(dict(year=sw.Y, month=sw.M, day=sw.D))
    sw = sw.set_index("date")
    f = sw["F107obs"].where(sw["F107obs"] > 0)
    sw["F107a"] = f.rolling(81, center=True, min_periods=40).mean()
    sw["Ap"] = sw["Ap"].where(sw["Ap"] >= 0)
    return sw[["F107obs", "F107a", "Ap"]]


sw = load_solar()
sw_ref = sw.loc["1990-01-01":"2026-10-24"]
T1, T2 = np.nanquantile(sw_ref["F107a"], [1 / 3, 2 / 3])
monthly = sw.resample("MS").mean()                      # month-start index


# ---------------------------------------------------------------- drag object-months
files = sorted(glob.glob(os.path.join(RED, "drag_*.parquet")))
drag = pd.concat([pd.read_parquet(f) for f in files], ignore_index=True)
n_om_all = len(drag)
stats_files = sorted(glob.glob(os.path.join(RED, "stats_*.json")))
ystats = [json.load(open(f)) for f in stats_files]

# lifetime-median B* per object (all its months)
bl = drag.groupby("norad_id")["bstar_med"].median().rename("bstar_life")
drag = drag.join(bl, on="norad_id")
drag["mdate"] = pd.to_datetime(dict(year=drag.year, month=drag.month, day=1))
drag = drag.join(monthly[["F107a", "F107obs", "Ap"]], on="mdate")
q = (drag.year >= 1990) & (drag.n_pairs >= 3) & ((drag.alt_max - drag.alt_min) < 40) & drag.rate_med.notna()
drag = drag[q].copy()
a = RE + drag["alt_med"].to_numpy() * 1e3
v = np.sqrt(MU / a)
drag["ad"] = -(drag["rate_med"].to_numpy() / 86400.0) * v / (2 * a)          # m/s^2
drag["g"] = drag["ad"] / G0
drag["v"] = v
B = BSTAR_TO_B * drag["bstar_life"].to_numpy()
drag["rho_eff"] = np.where(B > 0, 2 * drag["ad"].to_numpy() / (v ** 2 * np.where(B > 0, B, 1)), np.nan)
drag["BC_obj"] = np.where(B > 0, 1 / np.where(B > 0, B, 1), np.nan)            # m/(Cd A), kg/m^2
drag["sol"] = np.select([drag.F107a < T1, drag.F107a < T2], ["low", "mid"], "high")
drag["band"] = (np.floor(drag.alt_med / 25) * 25).astype(int)
drag["ym"] = drag.year * 100 + drag.month
drag["grp"] = np.where(drag.passive == "PAY-", "PAY-", np.where(drag.passive == "R/B", "R/B", "DEB"))

BANDS = list(range(200, 800, 25))


def month_cluster_stat(sub, col, nboot=300):
    """Median over months of the within-month median; bootstrap over months."""
    mm = sub.groupby("ym")[col].median().dropna().to_numpy()
    if len(mm) < 3:
        return None
    med = float(np.median(mm))
    bs = np.median(rng.choice(mm, size=(nboot, len(mm)), replace=True), axis=1)
    lo, hi = np.quantile(bs, [0.025, 0.975])
    return med, float(lo), float(hi), len(mm)


def cell_table(df, groups=("DEB", "R/B"), col="g"):
    rows = []
    sub0 = df[df.grp.isin(groups)]
    for b in BANDS:
        for s in ("low", "mid", "high", "all"):
            sub = sub0[(sub0.band == b) & ((sub0.sol == s) if s != "all" else True)]
            if len(sub) < 30:
                continue
            r = month_cluster_stat(sub, col)
            if r is None:
                continue
            x = sub[col].dropna().to_numpy()
            p10, p25, p50, p75, p90 = np.quantile(x, [0.1, 0.25, 0.5, 0.75, 0.9])
            rows.append(dict(band=b, sol=s, med=r[0], lo=r[1], hi=r[2], n_months=r[3],
                             n_object_months=int(len(sub)), n_objects=int(sub.norad_id.nunique()),
                             p10=p10, p25=p25, p50=p50, p75=p75, p90=p90,
                             F107a_med=float(sub.F107a.median()), Ap_med=float(sub.Ap.median()),
                             frac_pos=float((sub.rate_med > 0).mean())))
    return pd.DataFrame(rows)


g_all = cell_table(drag, ("DEB", "R/B"), "g")
g_rb = cell_table(drag, ("R/B",), "g")
g_deb = cell_table(drag, ("DEB",), "g")
g_pay = cell_table(drag, ("PAY-",), "g")
rho_tab = cell_table(drag[drag.rho_eff > 0], ("DEB", "R/B"), "rho_eff")
bc_tab = drag[drag.grp.isin(["DEB", "R/B"]) & (drag.BC_obj > 0)].groupby("grp")["BC_obj"].quantile([0.1, 0.25, 0.5, 0.75, 0.9]).unstack()

# n-dot cross-check (TLE field = n-dot/2): ratio of the two decay-rate estimates
cc = drag[drag.grp.isin(["DEB", "R/B"]) & (drag.rate_med < 0)]
ndot_ratio = (cc.rate_ndot_med / cc.rate_med)
ndot_check = {"median_ratio": float(ndot_ratio.median()),
              "iqr": [float(ndot_ratio.quantile(0.25)), float(ndot_ratio.quantile(0.75))],
              "n_object_months": int(len(cc))}

# ---------------------------------------------------------------- MSIS model route
msis_ok = True
try:
    import pymsis

    def msis_orbit_avg(alt_km, f107, f107a, ap):
        lats = np.arange(-50, 51, 10.0)
        lons = np.arange(0, 360, 30.0)
        dates = np.array([np.datetime64("2003-03-20T12:00"), np.datetime64("2003-06-21T12:00"),
                          np.datetime64("2003-09-22T12:00"), np.datetime64("2003-12-21T12:00")])
        out = []
        for d in dates:
            LA, LO = np.meshgrid(lats, lons, indexing="ij")
            n = LA.size
            res = pymsis.calculate(np.repeat(d, n), LO.ravel(), LA.ravel(), np.full(n, alt_km),
                                   f107s=np.full(n, f107), f107as=np.full(n, f107a),
                                   aps=np.full((n, 7), ap), version=2.1)
            out.append(np.nanmean(res[..., 0]))
        return float(np.mean(out))
except Exception as e:      # pragma: no cover
    msis_ok = False
    msis_err = repr(e)

# solar-activity reference levels (medians of the tercile, 1990-2026)
sol_ref = {}
for s, m in (("low", sw_ref.F107a < T1), ("mid", (sw_ref.F107a >= T1) & (sw_ref.F107a < T2)),
             ("high", sw_ref.F107a >= T2)):
    sol_ref[s] = dict(F107a=float(sw_ref.F107a[m].median()), Ap=float(sw_ref.Ap[m].median()))

msis_rows = []
if msis_ok:
    for b in BANDS:
        for s in ("low", "mid", "high"):
            h = b + 12.5
            F = sol_ref[s]["F107a"]
            rho = msis_orbit_avg(h, F, F, sol_ref[s]["Ap"])
            msis_rows.append(dict(band=b, sol=s, rho_msis=rho, F107a=F, Ap=sol_ref[s]["Ap"]))
msis_tab = pd.DataFrame(msis_rows)

# ---------------------------------------------------------------- density model rho(h, F) for lifetime
# Fit, per band, log10(rho_eff) = c0 + c1 (F107a - 120) on month-level medians (DEB + R/B).
mon = drag[drag.grp.isin(["DEB", "R/B"]) & (drag.rho_eff > 0)].groupby(["band", "ym"]).agg(
    rho=("rho_eff", "median"), F=("F107a", "median"), n=("rho_eff", "size")).reset_index()
fit = {}
for b, gb in mon.groupby("band"):
    gb = gb[(gb.n >= 3) & gb.F.notna()]
    if len(gb) < 24:
        continue
    X = np.c_[np.ones(len(gb)), gb.F - 120]
    yv = np.log10(gb.rho.to_numpy())
    coef, *_ = np.linalg.lstsq(X, yv, rcond=None)
    resid = yv - X @ coef
    fit[int(b)] = dict(c0=float(coef[0]), c1=float(coef[1]), resid_sd=float(resid.std()), n_months=int(len(gb)))
fit_bands = np.array(sorted(fit))
c0 = np.array([fit[b]["c0"] for b in fit_bands])
c1 = np.array([fit[b]["c1"] for b in fit_bands])
hc = fit_bands + 12.5


def rho_model(h_km, F):
    """log-linear interpolation in altitude of the per-band fit; linear extrapolation at the ends."""
    l0 = np.interp(h_km, hc, c0, left=np.nan, right=np.nan)
    l1 = np.interp(h_km, hc, c1, left=np.nan, right=np.nan)
    lo = h_km < hc[0]
    hi = h_km > hc[-1]
    if np.any(lo):
        s0 = (c0[1] - c0[0]) / (hc[1] - hc[0]); s1 = (c1[1] - c1[0]) / (hc[1] - hc[0])
        l0 = np.where(lo, c0[0] + s0 * (h_km - hc[0]), l0); l1 = np.where(lo, c1[0] + s1 * (h_km - hc[0]), l1)
    if np.any(hi):
        s0 = (c0[-1] - c0[-3]) / (hc[-1] - hc[-3]); s1 = (c1[-1] - c1[-3]) / (hc[-1] - hc[-3])
        l0 = np.where(hi, c0[-1] + s0 * (h_km - hc[-1]), l0); l1 = np.where(hi, c1[-1] + s1 * (h_km - hc[-1]), l1)
    return 10 ** (l0 + l1 * (F - 120))


# daily F10.7a series 1990-01-01 .. 2026-09-30, wrapped
Fd = sw.loc["1990-01-01":"2026-09-30", "F107a"].interpolate().bfill().ffill().to_numpy()
starts = np.arange(0, 25 * 365, 30)          # start every ~month, 1990-2014
H0 = np.arange(300, 726, 25).astype(float)
BC_LIST = [50.0, 150.0, 400.0]
MAX_YEARS = 300


def lifetime_sim(BC, rho_fn, dt_days=1.0):
    S, Hh = np.meshgrid(starts, H0, indexing="ij")
    h = Hh.ravel().copy(); s = S.ravel()
    life = np.full(h.shape, np.nan)
    alive = np.ones(h.shape, bool)
    nsteps = int(MAX_YEARS * 365 / dt_days)
    for k in range(nsteps):
        idx = (s + int(k * dt_days)) % len(Fd)
        F = Fd[idx]
        aa = RE + h * 1e3
        vv = np.sqrt(MU / aa)
        rho = rho_fn(h, F)
        dadt = -aa * rho * vv / BC                       # m/s
        h = h + np.where(alive, dadt * dt_days * 86400 / 1e3, 0)
        dead = alive & (h < 180)
        life[dead] = (k + 1) * dt_days / 365.25
        alive &= ~dead
        if not alive.any():
            break
        if k > 3650 and dt_days == 1.0 and k % 3650 == 0 and (h[alive] > 250).all():
            pass
    return life.reshape(S.shape)


life_rows = []
for BC in BC_LIST:
    L = lifetime_sim(BC, rho_model)
    for j, h0 in enumerate(H0):
        col = L[:, j]
        nd = np.isnan(col)
        life_rows.append(dict(route="tle", BC=BC, h0=h0, med=float(np.nanmedian(col)) if (~nd).any() else None,
                              p10=float(np.nanquantile(col, 0.1)) if (~nd).sum() > 5 else None,
                              p90=float(np.nanquantile(col, 0.9)) if (~nd).sum() > 5 else None,
                              frac_over_max=float(nd.mean())))

# MSIS route: rho from MSIS with F as the daily F10.7a (precomputed grid, interpolate)
msis_life = []
if msis_ok:
    hg = np.arange(175, 801, 25.0)
    Fg = np.array([65, 80, 100, 130, 160, 200, 250.0])
    grid = np.array([[msis_orbit_avg(h, F, F, 12.0) for F in Fg] for h in hg])
    lg = np.log10(grid)

    def rho_msis(h_km, F):
        hh = np.clip(h_km, hg[0], hg[-1]); FF = np.clip(F, Fg[0], Fg[-1])
        i = np.clip(np.searchsorted(hg, hh) - 1, 0, len(hg) - 2)
        jx = np.clip(np.searchsorted(Fg, FF) - 1, 0, len(Fg) - 2)
        th = (hh - hg[i]) / (hg[i + 1] - hg[i]); tf = (FF - Fg[jx]) / (Fg[jx + 1] - Fg[jx])
        v00 = lg[i, jx]; v10 = lg[i + 1, jx]; v01 = lg[i, jx + 1]; v11 = lg[i + 1, jx + 1]
        return 10 ** ((1 - th) * (1 - tf) * v00 + th * (1 - tf) * v10 + (1 - th) * tf * v01 + th * tf * v11)

    for BC in BC_LIST:
        L = lifetime_sim(BC, rho_msis)
        for j, h0 in enumerate(H0):
            col = L[:, j]
            nd = np.isnan(col)
            life_rows.append(dict(route="msis", BC=BC, h0=h0, med=float(np.nanmedian(col)) if (~nd).any() else None,
                                  p10=float(np.nanquantile(col, 0.1)) if (~nd).sum() > 5 else None,
                                  p90=float(np.nanquantile(col, 0.9)) if (~nd).sum() > 5 else None,
                                  frac_over_max=float(nd.mean())))
life_tab = pd.DataFrame(life_rows)

# ---------------------------------------------------------------- Kaplan-Meier of real residence times
sat = pd.read_csv(os.path.join(ROOT, "raw/satcat/satcat.csv"), dtype=str)
sat["norad_id"] = pd.to_numeric(sat.NORAD_CAT_ID, errors="coerce")
sat = sat.dropna(subset=["norad_id"]).astype({"norad_id": np.int64}).set_index("norad_id")
sat["decay"] = pd.to_datetime(sat.DECAY_DATE, errors="coerce")
cross = pd.concat([pd.read_parquet(f) for f in sorted(glob.glob(os.path.join(RED, "cross_*.parquet")))], ignore_index=True)
cross["abs_t"] = pd.to_datetime(cross.year.astype(str) + "-01-01") + pd.to_timedelta(cross.t_cross, unit="D")
first = cross.sort_values(["norad_id", "year"]).groupby("norad_id").agg(alt_first=("alt_first", "first"), y_first=("year", "first"))
cx = cross.groupby(["norad_id", "h"])["abs_t"].min().reset_index().join(first, on="norad_id")
cx = cx.join(sat[["decay", "OBJECT_TYPE"]], on="norad_id")
cx = cx[(cx.alt_first > cx.h + 10) & (cx.abs_t >= "1990-01-01") & cx.OBJECT_TYPE.isin(["DEB", "R/B"])]
END = pd.Timestamp("2026-10-01")
dur = ((cx.decay.fillna(END) - cx.abs_t).dt.total_seconds() / 86400 / 365.25).to_numpy()
event = cx.decay.notna().to_numpy() & (cx.decay <= END).to_numpy()
cx = cx.assign(dur=np.maximum(dur, 1 / 365.25), event=event)
cx["F_cross"] = monthly.F107a.reindex(cx.abs_t.dt.to_period("M").dt.to_timestamp()).to_numpy()


def km_quantiles(d, e, qs=(0.25, 0.5, 0.75)):
    o = np.argsort(d); d = d[o]; e = e[o]
    n = len(d); at_risk = n - np.arange(n)
    surv = np.cumprod(1 - e / at_risk)
    out = {}
    for qv in qs:
        idx = np.where(surv <= 1 - qv)[0]
        out[qv] = float(d[idx[0]]) if len(idx) else None
    return out


km_rows = []
for (h, typ), gsub in cx.groupby(["h", "OBJECT_TYPE"]):
    if len(gsub) < 20:
        continue
    kq = km_quantiles(gsub.dur.to_numpy(), gsub.event.to_numpy().astype(float))
    km_rows.append(dict(h=int(h), type=typ, n=int(len(gsub)), n_decayed=int(gsub.event.sum()),
                        q25=kq[0.25], q50=kq[0.5], q75=kq[0.75]))
km_tab = pd.DataFrame(km_rows)

# ---------------------------------------------------------------- crowding
crowd = pd.concat([pd.read_parquet(f) for f in sorted(glob.glob(os.path.join(RED, "crowd_*.parquet")))], ignore_index=True)

# ---------------------------------------------------------------- write
res = {
    "solar": {"T1": float(T1), "T2": float(T2), "ref": sol_ref,
              "series_monthly_F107a": [[d.strftime("%Y-%m"), round(float(x), 1)] for d, x in
                                        monthly.loc["1990-01-01":"2026-10-01", "F107a"].dropna().items()]},
    "drag_counts": {"object_months_all_years": int(n_om_all), "object_months_used": int(len(drag)),
                    "objects_used": int(drag.norad_id.nunique()),
                    "by_group": drag.groupby("grp").agg(om=("g", "size"), obj=("norad_id", "nunique")).reset_index().to_dict("records"),
                    "months": int(drag.ym.nunique())},
    "g_all": g_all.to_dict("records"), "g_rb": g_rb.to_dict("records"), "g_deb": g_deb.to_dict("records"),
    "g_pay": g_pay.to_dict("records"), "rho_tle": rho_tab.to_dict("records"),
    "msis": msis_tab.to_dict("records"), "msis_ok": msis_ok,
    "bc_obj_quantiles": {k: {str(q): float(v) for q, v in row.items()} for k, row in bc_tab.iterrows()},
    "ndot_check": ndot_check, "rho_fit": fit,
    "lifetime": life_tab.to_dict("records"), "km": km_tab.to_dict("records"),
    "crowd": crowd.to_dict("records"), "year_stats": ystats,
}
json.dump(res, open(OUT, "w"), default=lambda o: None if (isinstance(o, float) and np.isnan(o)) else float(o))
print("wrote", OUT, os.path.getsize(OUT))
print(g_all[g_all.sol != "all"].pivot(index="band", columns="sol", values="med"))
print(ndot_check)
if msis_ok:
    m = rho_tab.merge(msis_tab, on=["band", "sol"])
    m["ratio"] = m.med / m.rho_msis
    print(m[["band", "sol", "med", "rho_msis", "ratio"]].to_string())
print(life_tab.pivot_table(index="h0", columns=["route", "BC"], values="med"))
print(km_tab.to_string())
