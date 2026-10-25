#!/usr/bin/env python
"""Orbit workstream, analysis 4: sunlight fraction, beta angle and eclipse cycling for
candidate foundry orbits over one year (2027).

Geometry (standard analytic treatment, e.g. Vallado, Fundamentals of Astrodynamics):
  * Sun direction: low-precision solar ephemeris of the Astronomical Almanac (~0.01 deg).
  * Orbit plane: circular orbit, node regression by J2,
        dOmega/dt = -1.5 n J2 (Re/a)^2 cos i.
    The sun-synchronous inclination is solved so that dOmega/dt = 360 deg / 365.2422 d.
  * Beta angle: beta = asin(h_hat . s_hat), h_hat the orbit normal.
  * Eclipse (cylindrical shadow): beta* = asin(Re/(Re+h)); for |beta| < beta*
        f_ecl = (1/pi) acos( sqrt(h^2 + 2 Re h) / ((Re+h) cos beta) ).
The analytic eclipse fraction is cross-checked by brute-force propagation of the circular
orbit at 10 s steps with the same cylindrical shadow test (a numerical simulation).

Output: a JSON fragment with charts and stats, merged by orbit_build.py.
Usage: python orbit_power.py OUT.json
"""
import json
import sys

import numpy as np

RE = 6378.137e3
MU = 3.986004418e14
J2 = 1.08262668e-3
DEG = np.pi / 180
YEAR_D = 365.2422
J2000_2027 = 9861.5        # days from J2000.0 (2000-01-01 12:00 TT) to 2027-01-01 00:00


def sun_unit(d):
    """Unit vector to the Sun in an equatorial inertial frame; d = days since J2000."""
    L = (280.460 + 0.9856474 * d) * DEG
    g = (357.528 + 0.9856003 * d) * DEG
    lam = L + (1.915 * np.sin(g) + 0.020 * np.sin(2 * g)) * DEG
    eps = (23.439 - 4e-7 * d) * DEG
    return np.stack([np.cos(lam), np.cos(eps) * np.sin(lam), np.sin(eps) * np.sin(lam)], -1)


def node_rate(a, inc):
    n = np.sqrt(MU / a ** 3)
    return -1.5 * n * J2 * (RE / a) ** 2 * np.cos(inc)        # rad/s


def sso_inclination(a):
    target = 2 * np.pi / (YEAR_D * 86400)
    cosi = target / (-1.5 * np.sqrt(MU / a ** 3) * J2 * (RE / a) ** 2)
    return np.arccos(cosi)


def orbit_normal(inc, raan):
    return np.stack([np.sin(inc) * np.sin(raan), -np.sin(inc) * np.cos(raan),
                     np.cos(inc) * np.ones_like(raan)], -1)


def eclipse_fraction(h, beta):
    bstar = np.arcsin(RE / (RE + h))
    x = np.sqrt(h ** 2 + 2 * RE * h) / ((RE + h) * np.cos(beta))
    f = np.where(np.abs(beta) < bstar, np.arccos(np.clip(x, -1, 1)) / np.pi, 0.0)
    return f


def run_orbit(h_km, inc_deg, raan0_deg, days, sso_ltan=None):
    a = RE + h_km * 1e3
    inc = sso_inclination(a) if inc_deg is None else inc_deg * DEG
    d = J2000_2027 + days
    s = sun_unit(d)
    if sso_ltan is not None:
        # node placed so that local time of ascending node = sso_ltan hours at t0
        ra_sun0 = np.arctan2(s[0, 1], s[0, 0])
        raan0 = ra_sun0 + (sso_ltan - 12.0) * 15 * DEG
    else:
        raan0 = raan0_deg * DEG
    raan = raan0 + node_rate(a, inc) * days * 86400
    hhat = orbit_normal(inc, raan)
    beta = np.arcsin(np.clip(np.sum(hhat * s, -1), -1, 1))
    fe = eclipse_fraction(h_km * 1e3, beta)
    period_min = 2 * np.pi * np.sqrt(a ** 3 / MU) / 60
    return dict(a=a, inc=inc, raan0=raan0, beta=beta, fe=fe, period_min=period_min)


def brute_force_check(h_km, inc, raan0, day0, ndays=3, step=10.0):
    """Propagate a circular orbit numerically and test the cylindrical shadow directly."""
    a = RE + h_km * 1e3
    n = np.sqrt(MU / a ** 3)
    t = np.arange(0, ndays * 86400, step)
    raan = raan0 + node_rate(a, inc) * (t + day0 * 86400)
    u = n * t
    # position in ECI for a circular orbit with argument of latitude u
    r = a * np.stack([np.cos(raan) * np.cos(u) - np.sin(raan) * np.sin(u) * np.cos(inc),
                      np.sin(raan) * np.cos(u) + np.cos(raan) * np.sin(u) * np.cos(inc),
                      np.sin(u) * np.sin(inc)], -1)
    s = sun_unit(J2000_2027 + day0 + t / 86400)
    rs = np.sum(r * s, -1)
    perp = np.linalg.norm(r - rs[:, None] * s, axis=1)
    shadow = (rs < 0) & (perp < RE)
    return shadow.mean()


def main(out):
    days = np.arange(0, 365, 1.0)
    cands = [
        ("Dawn-dusk SSO 500 km", 500, None, None, 18.0),
        ("Dawn-dusk SSO 550 km", 550, None, None, 18.0),
        ("Dawn-dusk SSO 600 km", 600, None, None, 18.0),
        ("ISS-like 51.6 deg, 420 km", 420, 51.6, 0.0, None),
        ("Starlink-like 53 deg, 550 km", 550, 53.0, 0.0, None),
    ]
    stats, series_sun, series_beta, cyc_bars, ecl_bars = {}, [], [], [], []
    colors = ["orange", "grey", "violet", "cyan", "green"]
    for (name, h, inc, raan0, ltan), col in zip(cands, colors):
        r = run_orbit(h, inc, raan0, days, ltan)
        sun = 1 - r["fe"]
        orbits_per_day = 1440 / r["period_min"]
        ecl_days = int((r["fe"] > 0).sum())
        cycles = float((orbits_per_day * (r["fe"] > 0)).sum())
        # spread over the starting node for non-SSO orbits (annual statistics)
        spread = None
        if ltan is None:
            means, cyc = [], []
            for o in range(0, 360, 15):
                rr = run_orbit(h, inc, float(o), days, None)
                means.append(float((1 - rr["fe"]).mean()))
                cyc.append(float((orbits_per_day * (rr["fe"] > 0)).sum()))
            spread = {"annual_mean_sun_min": round(min(means), 4), "annual_mean_sun_max": round(max(means), 4),
                      "cycles_min": round(min(cyc)), "cycles_max": round(max(cyc))}
        # brute-force check on a day with eclipse (or day 0)
        dchk = int(np.argmax(r["fe"])) if r["fe"].max() > 0 else 0
        bf = brute_force_check(h, r["inc"], r["raan0"], float(dchk), ndays=2)
        stats[name] = {
            "altitude_km": h, "inclination_deg": round(float(r["inc"] / DEG), 2),
            "period_min": round(float(r["period_min"]), 2),
            "sunlight_fraction_annual_mean": round(float(sun.mean()), 4),
            "sunlight_fraction_min": round(float(sun.min()), 4),
            "beta_deg_min": round(float(r["beta"].min() / DEG), 1),
            "beta_deg_max": round(float(r["beta"].max() / DEG), 1),
            "days_with_eclipse": ecl_days,
            "eclipse_cycles_per_year": round(cycles),
            "max_eclipse_min": round(float(r["fe"].max() * r["period_min"]), 1),
            "check_day": dchk,
            "check_eclipse_fraction_analytic": round(float(r["fe"][dchk]), 4),
            "check_eclipse_fraction_bruteforce_2d": round(float(bf), 4),
            "node_spread": spread,
        }
        series_sun.append({"name": name, "points": [[int(d), round(float(v), 4)] for d, v in zip(days, sun)], "color": col})
        series_beta.append({"name": name, "points": [[int(d), round(float(v / DEG), 2)] for d, v in zip(days, r["beta"])], "color": col})
        cyc_bars.append([name, round(cycles)])
        ecl_bars.append([name, round(float(r["fe"].max() * r["period_min"]), 1)])
    charts = [
        {"id": "sunlight-fraction", "kind": "line", "title": "Fraction of each orbit spent in sunlight, through 2027",
         "subtitle": "Circular orbits, cylindrical Earth shadow, J2 node regression",
         "x": {"label": "Day of 2027", "unit": "day", "scale": "linear"},
         "y": {"label": "Sunlight fraction", "unit": "", "scale": "linear"},
         "series": series_sun,
         "caption": "Analytic geometry (simulation, not tracking data). Dawn-dusk sun-synchronous orbits stay in "
                    "sunlight except for a short eclipse season around the June solstice; 51.6 deg and 53 deg orbits "
                    "enter Earth's shadow on most orbits. Non-SSO curves use a starting node of 0 deg; their annual "
                    "statistics barely depend on it (stats.node_spread). Penumbra and atmospheric refraction are ignored."},
        {"id": "beta-angle", "kind": "line", "title": "Sun angle to the orbit plane (beta) through 2027",
         "subtitle": "Eclipse disappears when |beta| exceeds about 66-68 deg at these altitudes",
         "x": {"label": "Day of 2027", "unit": "day", "scale": "linear"},
         "y": {"label": "Beta angle", "unit": "deg", "scale": "linear"},
         "series": series_beta,
         "caption": "Analytic geometry (simulation). The beta angle sets both power (array illumination) and thermal "
                    "environment; it swings quickly for 51.6 deg and 53 deg orbits and stays high for dawn-dusk SSO."},
        {"id": "thermal-cycles", "kind": "hbar", "title": "Sun-to-shadow thermal cycles per year",
         "subtitle": "One cycle per orbit that crosses Earth's shadow",
         "x": {"label": "Orbit", "unit": "", "scale": "category"},
         "y": {"label": "Eclipse cycles per year", "unit": "cycles/yr", "scale": "linear"},
         "series": [{"name": "Eclipse cycles in 2027", "points": cyc_bars, "color": "orange"}],
         "caption": "Analytic geometry (simulation). Each eclipse is a thermal cycle for radiators, batteries and any "
                    "process that needs steady heat rejection."},
    ]
    json.dump({"charts": charts, "stats": stats, "max_eclipse_minutes": ecl_bars}, open(out, "w"), indent=1)
    for k, v in stats.items():
        print(k, v)


if __name__ == "__main__":
    main(sys.argv[1])
