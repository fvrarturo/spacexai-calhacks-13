# Appendix: orbit selection and the free-flyer environment (workstream `orbit`)

**Question.** A free-flying orbital foundry has to pick an orbit. How quiet is each candidate band, i.e. how much residual drag acceleration does it feel? How long does it stay up if it dies? How sunlit is it, and how crowded?

**Result files**
- `data/results/bigdata/orbit-environment.json` (tab `foundry`): g-level vs altitude, lifetime vs altitude, sunlight fraction, beta angle, thermal cycles, trade table.
- `data/results/bigdata/orbit-crowding.json` (tab `network`, also relevant to `foundry`): objects per shell over time and today's profile.

**Evidence levels used**
- **Our computation on public data:** measured drag and g-levels, Kaplan–Meier lifetimes, crowding.
- **Simulation:** NRLMSIS-driven foundry curves and lifetimes, with the model checked on our data; power and eclipse geometry.
- **Published result:** ISS requirements and characterisations, and the FCC 5-year rule.
- **Our assumption:** the foundry ballistic coefficient.

No ISS acceleration data were computed by us; see §7.

---

## 1. Data

| Dataset | Source | Licence / terms | Size actually processed |
|---|---|---|---|
| Space-Track TLE history, Hugging Face mirror `juliensimon/space-track-tle-history` | https://huggingface.co/datasets/juliensimon/space-track-tle-history | CC-BY-4.0 per the mirror card. The data originate from Space-Track.org (US Space Force 18th/19th SDS), whose user agreement restricts redistribution. **We publish aggregates only and never re-host raw TLEs.** | All 68 yearly parquet files, 1959–2026, **12,506,451,615 bytes** and **252,632,016 element sets** (the card says ~238 M; the files now hold more). Latest epoch 2026-10-23. |
| CelesTrak SATCAT | https://celestrak.org/pub/satcat.csv (T.S. Kelso) | public; cite CelesTrak | 71,139 objects, 6.8 MB |
| GFZ Potsdam Kp/ap/Ap/SN/F10.7 since 1932 | https://kp.gfz-potsdam.de/app/files/Kp_ap_Ap_SN_F107_since_1932.txt | CC BY 4.0 (Matzka et al. 2021, *Space Weather* 19, e2020SW002641); F10.7 is measured by NRCan/DRAO Penticton | 34,630 daily rows, 5.5 MB |
| NRLMSIS 2.1 via `pymsis` 0.13 | https://github.com/SWxTREC/pymsis (Emmert et al., NRLMSIS 2.0/2.1) | open source | model, driven by the GFZ F10.7/Ap |
| Starshine 3 build data (91 kg, 0.94 m sphere; NORAD 26929) | ILRS mission page, eoPortal, Wikipedia (sources give 88–91 kg and 0.94–1.0 m) | published | used only to compute its ballistic coefficient |
| ISS microgravity requirements and characterisation | Del Basso et al., AIAA 2003-1002 (NTRS 20100042410); McPherson, Hrovat, Kelly, Keller, *ISS Researcher's Guide: Acceleration Environment*, NASA NP-2015-11-040-JSC | published | quoted, labelled published |

Raw and intermediate data live only on Engaging under `~/orcd/scratch/orbital-foundry-20261024-01a170b7/bigdata/orbit/{raw,work}`. Peak footprint is about 14 GB.

## 2. Pipeline

| Stage | Code | Where | What |
|---|---|---|---|
| Download | `cluster/bigdata/orbit-download.sbatch` | `mit_data_transfer`, job 26813071 (4 CPU, 42 s) | 68 parquet files, 4 parallel curl streams; SATCAT; GFZ; CelesTrak SW-All (backup, unused) |
| Reduce | `analysis/bigdata/orbit_process.py`, `cluster/bigdata/orbit-process.sbatch` | `mit_quicktest`, job 26813726 (16 CPU, 8 workers, 41 s, MaxRSS 37 GB); test job 26813259 on 2003 only | Per year: drag object-months, crowding snapshots, threshold crossings |
| Aggregate | `analysis/bigdata/orbit_analyze.py`, `cluster/bigdata/orbit-analyze.sbatch` | `mit_quicktest`, job 26813879 (4 CPU, 81 s) | Band × solar-tercile statistics, NRLMSIS, lifetime integration, Kaplan–Meier, crowding tables. Writes `work/orbit_agg.json` (aggregates only) |
| Calibrate | `analysis/bigdata/orbit_calib.py`, `cluster/bigdata/orbit-calib.sbatch` | `mit_quicktest`, job 26814237 (2 CPU, 3 s) | Starshine 3 measured decay vs NRLMSIS |
| Diagnostic | inline script | `mit_quicktest`, job 26814098 (2 CPU, 4 s) | B* by year (led to rejecting the B* route) |
| Power | `analysis/bigdata/orbit_power.py` | laptop | Analytic beta and eclipse geometry, brute-force check |
| Build | `analysis/bigdata/orbit_build.py` | laptop | Writes the two result JSONs |

Job 26813495 (`mit_normal`, 16 CPU) never left the queue. We cancelled it ourselves and resubmitted the same work as 26813726. Total ≈ 0.33 CPU-hours. Every job used ≤ 16 CPUs and was named `of-orbit-*`.

## 3. Residual drag acceleration (the headline)

**Physics.** For a near-circular orbit the specific energy is E = −μ/2a and dE/dt = −a_d·v, so

a_d = −(da/dt) · v / (2a), with v = √(μ/a) and a = (μ/n²)^(1/3) from the TLE mean motion n.

**Selection.**
- Object types (CelesTrak SATCAT): debris (DEB) and rocket bodies (R/B). These are non-manoeuvring by nature.
- Payloads flagged non-operational ("−") were processed separately as `PAY-` and are **not** in the headline, because they may have manoeuvred earlier in life.
- Orbits: e < 0.01, mean altitude 150–1000 km.
- The first 30 days after launch are skipped, to avoid deorbit and passivation burns.

**Estimating da/dt.**
1. Each element set is paired with the first set of the same object at least 4 days later, keeping gaps of 3–8 days.
2. Pairs with |Δa| > 30 km are dropped as cross-tags or bad sets.
3. We take the median da/dt per object and calendar month, requiring ≥ 3 pairs and an altitude spread < 40 km.

This gives 58.9 M valid pairs and 1,836,464 object-months, of which 1,575,278 are from 1990–2026. The headline uses 15,573 DEB/R/B objects over 442 months.

**Cross-check.** Our differenced da/dt agrees with the TLE mean-motion-derivative field. The field holds ṅ/2, so da/dt = −(2/3)(a/n)(2·field). The median ratio is **0.95** (IQR 0.84–1.03) over 1.44 M object-months.

**Solar activity.** We use the 81-day centred mean of observed F10.7 from GFZ. Terciles over 1990-01-01 to 2026-10-24 are:
- low: < 83.1 sfu (median 73)
- mid: 83.1–131.4 sfu (median 108)
- high: ≥ 131.4 sfu (median 166)

**Statistic and independence.** All objects in a month share one atmosphere, so the month is the independent unit, not the object or the element set. Each cell value is the median over months of the within-month median across objects. The 95% CI comes from bootstrapping months (300 resamples). The object-month spread is reported separately (p10–p90).

### Measured g-levels (our computation on public data) and the foundry rescale (simulation, checked on data)

| Band | Solar tercile | Measured passive median g (95% CI) | p10–p90 | Rocket bodies | Debris | Implied pop. BC (kg/m²) | Foundry BC 150 g | Foundry BC 400–50 | objects / months |
|---|---|---|---|---|---|---|---|---|---|
| 300-325 km | low | 3.80e-07 (3.0e-07–4.7e-07) | 1.3e-07–3.3e-06 | 1.9e-07 | 6.2e-07 | 45 | 1.1e-07 | 4e-08–3e-07 | 318 / 124 |
| 300-325 km | high | 9.40e-07 (7.6e-07–1.7e-06) | 4.4e-07–3.7e-06 | 7.8e-07 | 2.2e-06 | 67 | 4.2e-07 | 2e-07–1e-06 | 249 / 101 |
| 400-425 km | low | 6.40e-08 (5.7e-08–7.0e-08) | 1.4e-08–4.2e-07 | 1.7e-08 | 8.5e-08 | 26 | 1.1e-08 | 4e-09–3e-08 | 442 / 147 |
| 400-425 km | high | 2.60e-07 (2.4e-07–2.9e-07) | 9.4e-08–1.6e-06 | 1.6e-07 | 4.9e-07 | 43 | 7.4e-08 | 3e-08–2e-07 | 1,027 / 143 |
| 450-475 km | low | 1.40e-08 (1.3e-08–1.5e-08) | 3.5e-09–1.5e-07 | 5.7e-09 | 3.1e-08 | 43 | 3.9e-09 | 1e-09–1e-08 | 462 / 147 |
| 450-475 km | high | 1.50e-07 (1.2e-07–1.6e-07) | 4.1e-08–7.7e-07 | 7.2e-08 | 2.9e-07 | 35 | 3.4e-08 | 1e-08–1e-07 | 1,410 / 145 |
| 500-525 km | low | 8.90e-09 (8.2e-09–1.0e-08) | 1.9e-09–8.5e-08 | 2.7e-09 | 1.7e-08 | 25 | 1.5e-09 | 6e-10–4e-09 | 543 / 147 |
| 500-525 km | mid | 3.90e-08 (3.1e-08–4.5e-08) | 7.5e-09–3.3e-07 | 1.1e-08 | 6.4e-08 | 19 | 4.8e-09 | 2e-09–1e-08 | 1,499 / 150 |
| 500-525 km | high | 1.00e-07 (9.0e-08–1.2e-07) | 2.3e-08–6.2e-07 | 3.5e-08 | 2.0e-07 | 24 | 1.6e-08 | 6e-09–5e-08 | 1,798 / 145 |
| 550-575 km | low | 6.70e-09 (5.1e-09–1.0e-08) | 7.5e-10–4.5e-08 | 1.2e-09 | 1.1e-08 | 14 | 6.3e-10 | 2e-10–2e-09 | 636 / 147 |
| 550-575 km | high | 7.10e-08 (6.8e-08–8.5e-08) | 1.3e-08–4.4e-07 | 1.8e-08 | 1.4e-07 | 17 | 7.9e-09 | 3e-09–2e-08 | 2,407 / 145 |
| 600-625 km | low | 2.10e-09 (1.7e-09–2.6e-09) | 1.9e-10–2.2e-08 | 2.4e-10 | 6.5e-09 | 22 | 3.0e-10 | 1e-10–9e-10 | 783 / 147 |
| 600-625 km | high | 3.10e-08 (2.8e-08–3.3e-08) | 2.7e-09–2.5e-07 | 4.6e-09 | 7.5e-08 | 19 | 4.0e-09 | 1e-09–1e-08 | 2,616 / 145 |
| 650-675 km | low | 2.40e-09 (2.0e-09–2.8e-09) | 5.3e-10–1.6e-08 | 4.9e-10 | 3.6e-09 | 10 | 1.7e-10 | 6e-11–5e-10 | 609 / 147 |
| 650-675 km | high | 4.70e-08 (3.9e-08–5.3e-08) | 7.6e-09–1.8e-07 | 6.6e-09 | 5.4e-08 | 7 | 2.1e-09 | 8e-10–6e-09 | 2,747 / 145 |

The full table, including all 25 km bands and the mid tercile, is in `stats.headline_by_altitude_and_solar_tercile`.

### Scaling to a foundry

**Ballistic coefficient (our assumption).** We use BC = m/(Cd·A):
- **150 kg/m² central:** a ~10 t free-flyer with ~30 m² mean projected area including arrays, Cd 2.2.
- **50 kg/m²:** a light body with large face-on arrays.
- **400 kg/m²:** a compact, dense module.

Drag acceleration scales exactly as 1/BC, so any other design is a linear rescale. The measured population itself behaves like BC ≈ 10–70 kg/m², lower at higher altitude where high area-to-mass debris dominates. So a foundry feels several times less drag than the median tracked object.

**Density route used:** NRLMSIS 2.1. We take the orbit-averaged density (latitudes ±50°, all longitudes, four seasons) at the band centre and the tercile-median F10.7 and Ap, then compute a_d = ½ρv²/BC. We checked it on our data in three ways:
1. **Absolute level, known-BC sphere.** Starshine 3 (NORAD 26929; 91 kg, 0.94 m, Cd 2.2, so BC ≈ 60 kg/m²) was tracked from 2001-09 to 2003-01. We compared its measured a_d pair by pair with NRLMSIS, using that day's F10.7 and Ap, latitudes weighted for the 67° inclination, and atmospheric co-rotation.
   - Median measured/model ratio is **0.87**, IQR 0.81–0.92, over 48 ten-day windows.
   - It is flat with altitude: 0.87 at 400–480 km, 0.86 at 300–400 km, 0.87 at 200–300 km.
   - So the model is about 13% high at solar maximum, and the foundry curves are, if anything, slightly conservative.
   - This is a single object at solar maximum only.
2. **Solar response.** The measured high/low-tercile drag ratio of the passive population divided by the model's ratio is 0.60–1.22 across the 300–625 km bands, and 1.07 at 500–525 km.
3. **Lifetimes.** Real rocket bodies' Kaplan–Meier lifetimes match the model at BC ≈ 50 (§4).

**Rejected route: B* as ballistic coefficient.** Our first attempt converted B* to a ballistic coefficient with the nominal B = 12.741621·B* m²/kg (Hoots & Roehrich 1980) and inferred density as 2a_d/(v²B).
- The median B* of the same population at 500–550 km swings about 30× with the solar cycle: 6.6e-5 in 2009 versus 2.8e-3 in 2002.
- So B* absorbs density-model error and is not a physical ballistic coefficient.
- The resulting density was 3–35× NRLMSIS, and it predicted lifetimes far shorter than real rocket bodies show.

We report it in `stats.rejected_route_bstar` and do not use it.

**Context (published).** The ISS quasi-steady requirement is **1 µg** magnitude and **0.2 µg** perpendicular component, below 0.01 Hz:
- It applies in ≥ 50% of payload rack locations, for 180 days a year in 30-day increments.
- Transient limits are 1000 µg peak and 10 µg·s per 10 s.
- In the assembly-complete verification, 14 of 32 rack locations complied; the 15th and 16th were at 1.11 and 1.17 µg.

Source: Del Basso et al., AIAA 2003-1002, from SSP 41000.

NASA's guide characterises the measured environment this way:
- Quasi-steady accelerations are "on the order of less than a micro-g".
- The unisolated vibratory spectrum reaches "well over 10 milli-g" at the high-frequency end.
- Isolation reduces it by up to 100×.
- Structural modes are quieter during crew sleep.

**Gravity gradient (our analytic computation).** The radial term is 3n²r, about **0.39–0.40 µg per metre** of offset from the centre of mass at 400–600 km. Above about 450 km, drag on a BC-150 foundry is smaller, even in active-Sun years, than the gravity gradient 10 cm from the centre of mass. At 400–425 km in active-Sun years, it equals the gradient about 19 cm away. Cartridge placement, and the absence of crew, exercise and pumps, matter more for "quiet growth" than the choice of altitude.

## 4. Orbital lifetime

**Model (simulation driven by real solar data).** We integrate da/dt = −aρv/BC day by day with NRLMSIS 2.1 density, interpolated on a grid of altitude and F10.7, with Ap = 12.
- Solar input: the observed daily 81-day F10.7 sequence of 1990–2026, wrapped after its end.
- Start dates: every month from 1990 to 2014, so the spread reflects where in the solar cycle the foundry dies.
- Reentry is taken as 180 km, with a 300-year cap.

| Start altitude | BC 50: median yr (p10–p90) | BC 150: median yr (p10–p90) | BC 400: median yr (p10–p90) |
|---|---|---|---|
| 300 km | 0.082 (0.047–0.13) | 0.24 (0.13–0.39) | 0.61 (0.35–1.0) |
| 350 km | 0.26 (0.12–0.50) | 0.73 (0.36–1.45) | 2.0 (0.98–3.6) |
| 400 km | 0.70 (0.30–1.6) | 2.1 (0.91–4.1) | 5.8 (2.7–8.4) |
| 450 km | 1.9 (0.69–4.1) | 5.6 (2.2–8.6) | 13 (9.8–19) |
| 500 km | 4.5 (1.6–7.9) | 12 (7.0–19) | 30 (26–33) |
| 550 km | 10.5 (4.0–15.6) | 26 (23–30) | 65 (61–68) |
| 600 km | 19 (15–23) | 51 (47–57) | 135 (130–137) |
| 650 km | 33 (28–36) | 102 (98–105) | 268 (263–273) |
| 700 km | 66 (62–70) | 194 (189–200) | > 300 |

The highest altitude at which a dead foundry still meets the **5-year post-mission disposal rule** (FCC 2022, published) without propulsion is:
- **≈ 443 km** for BC 150;
- ≈ 506 km for BC 50;
- ≈ 392 km for BC 400.

**Kaplan–Meier on real objects (our computation).** For debris and rocket bodies that crossed below each altitude after 1990 (first observed above it, e < 0.01), we take the time from crossing to the SATCAT decay date, censored at 2026-10-01.

| Altitude | Type | n crossed | n decayed | KM median yr (q25–q75) |
|---|---|---|---|---|
| 300 km | R/B | 362 | 354 | 0.072 (0.048–0.10) |
| 400 km | R/B | 271 | 249 | 0.54 (0.35–0.77) |
| 450 km | R/B | 235 | 196 | 1.3 (0.76–2.5) |
| 500 km | R/B | 155 | 107 | 3.7 (2.0–8.3) |
| 550 km | R/B | 94 | 54 | 12 (10–19) |
| 600 km | R/B | 60 | 19 | 32 (23–n/a) |
| 500 km | DEB | 5,295 | 5,178 | 0.13 (0.057–0.33) |
| 700 km | DEB | 3,610 | 2,761 | 2.3 (0.98–7.5) |

From 400 to 550 km, rocket bodies track the model's BC-50 curve within about 30% (0.54 vs 0.70 yr at 400 km, 3.7 vs 4.5 yr at 500 km, 12 vs 10.5 yr at 550 km). At 600 km, only 19 of 60 have decayed, so the median (32 yr vs 19) is poorly constrained. This independently supports the model route. Debris lifetimes are far shorter because the debris that reaches these altitudes is dominated by high area-to-mass fragments. These are real objects' lifetimes with their own BCs, not a foundry's.

## 5. Crowding

**Method.**
1. For each year 1990–2026, take the last element set of each object in the 30 days before 1 July. For "today", take the last 30 days of data, ending 2026-10-23.
2. Assign each object to a 25 km band of mean altitude a − 6378.137 km.
3. Categorise with SATCAT:
   - **Starlink:** PAY named `STARLINK*`;
   - **Other megaconstellations:** `ONEWEB*`, `KUIPER*`, `QIANFAN*`, `HULIANWANG*` (Guowang appears as "HULIANWANG DIGUI");
   - **Other payloads;**
   - **Rocket bodies;**
   - **Debris and unknown.**

**Results.**
- **27,298** catalogued objects are below 2,000 km today, against 4,846 in 1990 and 15,094 in 2020. Today's split: Starlink 10,688; other megaconstellations 1,482; other payloads 4,665; rocket bodies 997; debris and unknown 9,466.
- The most crowded shells are **450–475 km (6,144 objects, 95% Starlink)** and 475–500 km (3,780, 88% Starlink), then the old debris belts at 750–850 km.
- This is consistent with SpaceX's announced 2026 lowering of Starlink shells to about 480 km (an operator statement we did not verify), which appear at 450–475 km in this altitude convention. Our "altitude" is a − R_eq, typically 5–10 km below quoted altitudes.
- Candidate bands today: 400–450 km holds 546 objects; 450–500 km, 9,924; 500–550 km, 985; 550–600 km, 983; 600–650 km, 1,157; 650–700 km, 860.

## 6. Power and thermal (simulation: analytic geometry)

**Method.**
- Sun position: low-precision solar ephemeris.
- Orbits: circular, with J2 node regression. The sun-synchronous inclination is solved from the J2 condition.
- Beta angle: β = asin(ĥ·ŝ).
- Eclipse: cylindrical shadow, f = acos(√(h²+2Rh)/((R+h)cos β))/π when |β| < asin(R/(R+h)).
- The analytic eclipse fraction is checked against a brute-force 10 s propagation; it agrees to < 1.5% on the worst day.
- Year: 2027.

| Orbit | Incl. | Foundry drag g (low–high Sun, BC 150) | Passive life BC150 / BC50 (yr) | Sunlight | Eclipse cycles/yr | Max eclipse | Objects ±25 km today |
|---|---|---|---|---|---|---|---|
| Dawn-dusk SSO, 500 km | 97.4° | 1.9e-09–1.9e-08 | 12 / 4.5 | 94.4% | 1,613 | 22.7 min | 4,330 |
| Dawn-dusk SSO, 550 km | 97.6° | 7.8e-10–9.4e-09 | 26 / 10.5 | 95.0% | 1,521 | 21.7 min | 955 |
| Dawn-dusk SSO, 600 km | 97.8° | 3.6e-10–4.7e-09 | 51 / 19 | 95.5% | 1,430 | 20.7 min | 905 |
| ISS-like 51.6°, 420 km | 51.6° | 9.5e-09–6.6e-08 | 3.3 / 1.0 | 66.1% | 5,514 | 36.0 min | 546 |
| Starlink-like 53°, 550 km | 53.0° | 7.8e-10–9.4e-09 | 26 / 10.5 | 69.2% | 5,119 | 35.6 min | 955 |

**Dawn–dusk SSO.**
- β stays at 59–88°.
- Eclipses come only in a ~96–106-day season around the June solstice (6 pm node), lasting ≤ 22 min.
- So arrays see near-continuous sun, and radiators see about 3.5× fewer thermal cycles than at 51.6–53°.

**51.6–53° orbits.**
- β swings ±73–76° on a roughly two-month cycle.
- The orbit is in eclipse on almost every pass, for up to 36 min.
- The result is about two-thirds sunlight and more than 5,000 thermal cycles a year. This needs a larger array and battery for the same average process power.

## 7. ISS acceleration data probe (≤ 20 min)

PIMS documents a public PAD archive (SAMS, MAMS, MMA) at `http://pims.grc.nasa.gov/ftp/pad`. What we found on 2026-10-24:
- That host did not resolve, either from MIT Engaging or from a home network.
- The `gipoc.grc.nasa.gov/pims/ftp/pad/` mirror returned HTTP 403 for the root and for dated paths.
- The `pims/pub/pad/` link resolves to a documents page.

So **we computed no crew-sleep vs awake contrast**, and `iss-microgravity.json` was not produced. We cite the published characterisation in §3 instead, as `stats.iss_reference_published` and `stats.iss_acceleration_data_probe`.

## 8. Candidate band

This is **our computation, not a design decision.**

On these numbers, a **dawn–dusk sun-synchronous orbit at about 525–575 km** balances the four constraints best, **provided the foundry carries a deorbit capability**. At 550 km:
- **Drag:** 0.8–9 nano-g (BC 150), more than 100× below the ISS 1 µg requirement.
- **Power:** 95% sunlight.
- **Thermal:** about 1,500 thermal cycles a year, against about 5,500 at 51.6°.
- **Crowding:** about 955 catalogued neighbours within ±25 km, against 9,924 in Starlink's 450–500 km region just below.

Trade-offs:
- **Disposal:** a dead BC-150 foundry stays up about 26 years (about 10 at BC 50), so disposal must be propulsive.
- **Alternative:** an ISS-like ~420 km orbit self-disposes in about 3 years and has few neighbours. But drag there is about 7× higher (still < 0.1 µg), it needs reboosts (each one a transient), and it has 66% sunlight with about 5,500 eclipses a year.
- **Launch and access:** SSO costs more launch Δv and offers no crew-station access.
- **Return:** we did not analyse the return-capsule landing geometry.

## 9. Limitations (what this does not show)

- **Not a foundry measurement.** The measured objects are debris and rocket bodies. Their g-levels are real, but the foundry curves rescale them through a model atmosphere and an assumed BC. The BC assumption dominates the uncertainty: a factor of 8 across BC 50–400.
- **Model check is narrow.** NRLMSIS was checked against one known-BC sphere (Starshine 3, solar maximum only) and against the population's solar response, which agrees within 0.6–1.2×.
- **TLE smoothing.** Mean elements average over each fit span, so this is orbit-averaged, quasi-steady (≪ 0.01 Hz) along-track drag.
- **Not in the drag numbers:**
  - vibration, attitude control, venting or crew disturbances;
  - the gravity-gradient and rotational terms, which depend on where a cartridge sits;
  - the ~8% co-rotation effect on v² (the foundry curves use inertial speed).
- **Selection and contamination.**
  - Debris can be cross-tagged.
  - Medians per object-month and the 30 km jump cut limit, but do not remove, these effects.
  - Debris populations differ between solar max and min, which may explain why the measured solar response is weaker than the model's below 425 km.
- **Solar cycles are pooled.** The terciles pool cycles 22–25. Storms such as May 2024 sit inside the spread, not as separate cases.
- **Lifetime assumptions.** Lifetimes assume constant BC and attitude, and that the 1990–2026 F10.7 record repeats. They are planning estimates, not a disposal analysis.
- **Crowding is a count.**
  - It covers the public catalogue only (~10 cm and larger in LEO).
  - Tracking capacity grew over time.
  - Eccentric objects are assigned to their mean altitude.
  - Counts are not collision probabilities.
- **Power geometry is idealised.** No penumbra or atmosphere, and orbits are circular.

## 10. Future big data

- **CelesTrak SupGP** (operator ephemerides for Starlink, OneWeb, Kuiper): higher-fidelity shell occupancy and manoeuvre statistics.
- **GRACE-FO and Swarm accelerometer data** (ESA/NASA/GFZ): direct non-gravitational acceleration at 400–500 km, replacing the model route with measured densities.
- **Conjunction screening for a foundry fleet:** propagate candidate orbits against the full catalogue or SupGP for a year to count close approaches per shell and the avoidance manoeuvres they would require.
- **More known-BC calibration objects:** Space-Track decay and TIP messages, plus spheres such as ANDE and Starshine 1/2.
- **The PIMS PAD archive, if access is restored:** crew-sleep vs awake vibratory spectra as the baseline a crew-free foundry would beat.
- **NOAA SWPC solar-cycle 25/26 forecasts,** in place of the repeated historical F10.7.

## 11. Reproduce

```bash
rsync -az analysis/bigdata cluster/bigdata engaging:~/orcd/scratch/orbital-foundry-20261024-01a170b7/
ssh engaging 'cd ~/orcd/scratch/orbital-foundry-20261024-01a170b7/bigdata/orbit && module load miniforge && python -m venv env && . env/bin/activate && PIP_CACHE_DIR=~/orcd/scratch/pip_cache pip install numpy pandas pyarrow duckdb scipy sgp4 pymsis'
ssh engaging 'cd ~/orcd/scratch/orbital-foundry-20261024-01a170b7/bigdata/orbit && sbatch ../orbit-download.sbatch'
ssh engaging 'cd ~/orcd/scratch/orbital-foundry-20261024-01a170b7/bigdata/orbit && sbatch --partition=mit_quicktest --time=00:15:00 --mem=120G --export=ALL,YEARS=1959-2026,WORKERS=8 ../orbit-process.sbatch'
ssh engaging 'cd ~/orcd/scratch/orbital-foundry-20261024-01a170b7/bigdata/orbit && sbatch ../orbit-analyze.sbatch && sbatch ../orbit-calib.sbatch'
rsync -az engaging:~/orcd/scratch/orbital-foundry-20261024-01a170b7/bigdata/orbit/work/orbit_{agg,calib}.json ./tmp/
python analysis/bigdata/orbit_power.py ./tmp/power.json
python analysis/bigdata/orbit_build.py ./tmp/orbit_agg.json ./tmp/power.json ./tmp/jobs.json ./tmp/orbit_calib.json
```

`jobs.json` holds the `sacct` records (`sacct -j <ids> -X -o jobid,jobname,partition,state,elapsed,ncpus,maxrss`).

## References

- Space-Track.org; Julien Simon, *space-track-tle-history* (Hugging Face, CC-BY-4.0).
- T.S. Kelso, CelesTrak SATCAT.
- Matzka, J. et al. (2021) *Space Weather* 19, e2020SW002641 (GFZ Kp/ap/F10.7).
- Emmert, J.T. et al., NRLMSIS 2.0 (2021, *Earth and Space Science*) and 2.1 (2022); pymsis (SWxTREC).
- Hoots, F.R. & Roehrich, R.L. (1980), *Spacetrack Report No. 3* (B* definition).
- Del Basso, S. et al. (2003), *ISS Microgravity Analytical Model Correlation and Update*, AIAA 2003-1002, NTRS 20100042410.
- McPherson, K., Hrovat, K., Kelly, E., Keller, J., *A Researcher's Guide to: Acceleration Environment*, NASA ISS Program Science Office, NP-2015-11-040-JSC.
- FCC Second Report and Order on orbital debris (5-year rule), FCC 22-74 (2022).
- Kaplan–Meier residence-time approach in the spirit of J. McDowell's satellite-decay statistics (planet4589.org).
- Starshine 3 build data: ILRS mission page (https://ilrs.gsfc.nasa.gov/missions/satellite_missions/past_missions/sta3_general.html) and eoPortal.
