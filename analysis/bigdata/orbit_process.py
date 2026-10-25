#!/usr/bin/env python
"""Orbit workstream, stage 1: per-year reduction of the Space-Track TLE history mirror.

For every yearly parquet file of juliensimon/space-track-tle-history this script writes three
small aggregate tables (raw TLEs never leave the cluster; Space-Track terms forbid
redistribution):

  drag_<year>.parquet     one row per (object, calendar month) for passive objects on
                          near-circular orbits: robust median of da/dt from element-set pairs
                          3-8 days apart, median altitude, median B*, n-dot cross-check.
  crowd_<year>.parquet    catalogued objects per 25 km mean-altitude band and category, from a
                          snapshot (last element set of each object in the 30 days before
                          1 July; for the latest year also the last 30 days of data, "today").
  cross_<year>.parquet    first epoch at which each passive near-circular object is seen below
                          each threshold altitude (for the Kaplan-Meier residence-time check).
  stats_<year>.json       rows read, bytes, rows kept.

Physics. Mean motion n (rev/day) -> semi-major axis a = (mu / n_rad^2)^(1/3). For a near-
circular orbit E = -mu/(2a), dE/dt = -a_d v, so the along-track drag deceleration is
a_d = -(da/dt) v / (2a), v = sqrt(mu/a). This script stores da/dt; stage 2 converts it.

Usage: python orbit_process.py --raw RAW_DIR --satcat SATCAT_CSV --out OUT_DIR --years 1990-2026 --workers 8
"""
import argparse
import json
import os
import time
from multiprocessing import Pool

import numpy as np
import pandas as pd
import pyarrow.parquet as pq

MU = 3.986004418e14          # m^3/s^2 (WGS-84 / EGM-96 value)
RE_KM = 6378.137             # equatorial radius, km
DAY = 86400.0
THRESH_KM = list(range(250, 751, 50))
BAND_KM = 25.0

SATCAT = None                # filled per worker


def categorise(sat: pd.DataFrame) -> pd.DataFrame:
    """Object category for crowding and the passive flag for the drag analysis."""
    name = sat["OBJECT_NAME"].fillna("").str.upper()
    typ = sat["OBJECT_TYPE"].fillna("UNK")
    cat = np.where(typ == "DEB", "Debris",
          np.where(typ == "R/B", "Rocket body",
          np.where(typ == "PAY", "Other payload", "Unknown")))
    cat = pd.Series(cat, index=sat.index)
    is_pay = typ == "PAY"
    cat[is_pay & name.str.startswith("STARLINK")] = "Starlink"
    cat[is_pay & name.str.startswith("ONEWEB")] = "OneWeb"
    mega = (name.str.startswith("KUIPER") | name.str.startswith("QIANFAN")
            | name.str.contains("GUOWANG") | name.str.startswith("SATNET LEO")
            | name.str.startswith("HULIANWANG"))
    cat[is_pay & mega] = "Other megaconstellation"
    sat = sat.assign(category=cat)
    ops = sat["OPS_STATUS_CODE"].fillna("?")
    # passive class used for drag: DEB, R/B, and payloads flagged non-operational ('-') today.
    passive = np.where(typ == "DEB", "DEB", np.where(typ == "R/B", "R/B",
              np.where(is_pay & (ops == "-") & (cat == "Other payload"), "PAY-", "")))
    sat = sat.assign(passive=passive)
    return sat


def load_satcat(path: str) -> pd.DataFrame:
    sat = pd.read_csv(path, dtype=str)
    sat["norad_id"] = pd.to_numeric(sat["NORAD_CAT_ID"], errors="coerce")
    sat = sat.dropna(subset=["norad_id"]).copy()
    sat["norad_id"] = sat["norad_id"].astype(np.int64)
    for c in ("LAUNCH_DATE", "DECAY_DATE"):
        sat[c] = pd.to_datetime(sat[c], errors="coerce")
    sat = categorise(sat)
    return sat.set_index("norad_id")[["OBJECT_NAME", "OBJECT_TYPE", "OPS_STATUS_CODE", "OWNER",
                                      "LAUNCH_DATE", "DECAY_DATE", "category", "passive"]]


def init_worker(satcat_path):
    global SATCAT
    SATCAT = load_satcat(satcat_path)


def snapshot_counts(df, t0, t1, label, year):
    """Last element set per object in [t0, t1) -> counts per 25 km band and category."""
    m = (df["t"] >= t0) & (df["t"] < t1)
    snap = df.loc[m, ["norad_id", "t", "alt", "ecc"]].drop_duplicates("norad_id", keep="last")
    snap = snap.join(SATCAT[["category", "DECAY_DATE"]], on="norad_id")
    snap["category"] = snap["category"].fillna("Unknown")
    snap = snap[(snap["alt"] > 100) & (snap["alt"] < 2000)]
    snap["band"] = (np.floor(snap["alt"] / BAND_KM) * BAND_KM).astype(int)
    g = snap.groupby(["band", "category"]).agg(n=("norad_id", "size"),
                                                n_ecc_gt_0p01=("ecc", lambda e: int((e > 0.01).sum())))
    g = g.reset_index()
    g["snapshot"] = label
    g["year"] = year
    return g


def process_year(args):
    year, raw, out = args
    t_start = time.time()
    path = os.path.join(raw, f"tle_{year}.parquet")
    pf = pq.ParquetFile(path)
    nbytes = os.path.getsize(path)
    nrows_read = pf.metadata.num_rows
    tab = pq.read_table(path, columns=["norad_id", "epoch", "eccentricity", "mean_motion",
                                       "mean_motion_dot", "bstar", "inclination"])
    df = tab.to_pandas()
    del tab
    df = df.rename(columns={"eccentricity": "ecc", "mean_motion": "n", "mean_motion_dot": "ndot",
                            "inclination": "inc"})
    df = df[np.isfinite(df["n"]) & (df["n"] > 0.5)]
    ep = pd.to_datetime(df["epoch"], utc=True)
    y0 = pd.Timestamp(f"{year}-01-01", tz="UTC")
    df["t"] = (ep - y0).dt.total_seconds().to_numpy() / DAY          # days since 1 Jan of year
    df["month"] = ep.dt.month.to_numpy().astype(np.int8)
    df = df.drop(columns=["epoch"])
    nrad = df["n"].to_numpy() * 2 * np.pi / DAY
    a_m = (MU / nrad ** 2) ** (1.0 / 3.0)
    df["a"] = a_m
    df["alt"] = a_m / 1000.0 - RE_KM
    df = df.sort_values(["norad_id", "t"], kind="stable").reset_index(drop=True)

    # ---------------- crowding snapshots ----------------
    crowd = []
    jul1 = (pd.Timestamp(f"{year}-07-01", tz="UTC") - y0).total_seconds() / DAY
    tmax = float(df["t"].max())
    if tmax >= jul1:
        crowd.append(snapshot_counts(df, jul1 - 30, jul1, f"{year}-07-01", year))
    if year == 2026 or tmax < jul1:
        lab = (y0 + pd.Timedelta(days=tmax)).strftime("%Y-%m-%d")
        crowd.append(snapshot_counts(df, tmax - 30, tmax + 1e-6, "latest:" + lab, year))
    crowd = pd.concat(crowd, ignore_index=True) if crowd else pd.DataFrame()
    crowd.to_parquet(os.path.join(out, f"crowd_{year}.parquet"), index=False)

    # ---------------- passive near-circular objects ----------------
    sat = SATCAT
    d = df.join(sat[["passive", "LAUNCH_DATE"]], on="norad_id")
    d = d[(d["passive"].fillna("") != "") & (d["ecc"] < 0.01) & (d["alt"] > 150) & (d["alt"] < 1000)]
    launch_t = (d["LAUNCH_DATE"].dt.tz_localize("UTC") - y0).dt.total_seconds() / DAY
    d = d[~(launch_t > d["t"] - 30)]           # skip the first 30 days after launch (deorbit/passivation burns)
    d = d.drop(columns=["LAUNCH_DATE"])
    # drop duplicate epochs (keep the latest-issued element set, which comes last after the stable sort)
    dup = (d["norad_id"].to_numpy()[1:] == d["norad_id"].to_numpy()[:-1]) & \
          (np.abs(np.diff(d["t"].to_numpy())) < 1e-6)
    keep = np.ones(len(d), bool)
    keep[:-1][dup] = False
    d = d[keep].reset_index(drop=True)

    nid = d["norad_id"].to_numpy().astype(np.int64)
    t = d["t"].to_numpy()
    a = d["a"].to_numpy()
    key = nid.astype(np.float64) * 1000.0 + t
    j = np.searchsorted(key, key + 4.0)          # first element set >= 4 days later
    valid = j < len(d)
    jj = np.where(valid, j, 0)
    dt = t[jj] - t
    valid &= (nid[jj] == nid) & (dt >= 3.0) & (dt <= 8.0)
    da = a[jj] - a
    valid &= np.abs(da) < 30e3                   # > 30 km in a few days = cross-tag / bad set
    rate = np.where(valid, da / np.where(valid, dt, 1.0), np.nan)       # m/day
    # n-dot cross-check: the TLE field is (1/2) dn/dt in rev/day^2 -> da/dt = -(2/3) a (2*field)/n
    rate_ndot = -(2.0 / 3.0) * a * (2.0 * d["ndot"].to_numpy()) / d["n"].to_numpy()
    d["rate"] = rate
    d["rate_ndot"] = rate_ndot
    d["pos"] = (rate > 0).astype(float)
    dv = d[valid]
    om = dv.groupby(["norad_id", "month"]).agg(
        rate_med=("rate", "median"), rate_q25=("rate", lambda x: np.quantile(x, 0.25)),
        rate_q75=("rate", lambda x: np.quantile(x, 0.75)), n_pairs=("rate", "size"),
        frac_pos=("pos", "mean"), alt_med=("alt", "median"), alt_min=("alt", "min"),
        alt_max=("alt", "max"), bstar_med=("bstar", "median"), inc_med=("inc", "median"),
        ecc_med=("ecc", "median"), rate_ndot_med=("rate_ndot", "median"), t_med=("t", "median"),
    ).reset_index()
    om["year"] = year
    om = om.join(sat[["passive"]], on="norad_id")
    om.to_parquet(os.path.join(out, f"drag_{year}.parquet"), index=False)

    # ---------------- first crossing below threshold altitudes ----------------
    rows = []
    g_first = d.groupby("norad_id").agg(t_first=("t", "first"), alt_first=("alt", "first"))
    for h in THRESH_KM:
        below = d[d["alt"] < h].groupby("norad_id")["t"].min()
        if len(below):
            rows.append(pd.DataFrame({"norad_id": below.index, "h": h, "t_cross": below.values}))
    cross = pd.concat(rows, ignore_index=True) if rows else pd.DataFrame(columns=["norad_id", "h", "t_cross"])
    cross = cross.join(g_first, on="norad_id")
    cross["year"] = year
    cross.to_parquet(os.path.join(out, f"cross_{year}.parquet"), index=False)

    stats = {"year": year, "bytes": nbytes, "rows_read": int(nrows_read),
             "rows_passive_circular": int(len(d)), "pairs_valid": int(valid.sum()),
             "object_months": int(len(om)), "objects_passive": int(om["norad_id"].nunique()),
             "objects_in_file": int(df["norad_id"].nunique()),
             "tmax_date": (y0 + pd.Timedelta(days=tmax)).isoformat(),
             "seconds": round(time.time() - t_start, 1)}
    with open(os.path.join(out, f"stats_{year}.json"), "w") as f:
        json.dump(stats, f)
    return stats


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--raw", required=True)
    ap.add_argument("--satcat", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--years", default="1990-2026")
    ap.add_argument("--workers", type=int, default=8)
    args = ap.parse_args()
    y0, y1 = (int(x) for x in args.years.split("-"))
    os.makedirs(args.out, exist_ok=True)
    years = list(range(y0, y1 + 1))
    years.sort(key=lambda y: -os.path.getsize(os.path.join(args.raw, f"tle_{y}.parquet")))  # big first
    with Pool(args.workers, initializer=init_worker, initargs=(args.satcat,)) as pool:
        for s in pool.imap_unordered(process_year, [(y, args.raw, args.out) for y in years]):
            print(json.dumps(s), flush=True)


if __name__ == "__main__":
    main()
