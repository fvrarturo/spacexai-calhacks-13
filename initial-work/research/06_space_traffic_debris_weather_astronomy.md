# Space traffic, orbital debris, SSA, space weather, reentries, and megaconstellation impacts on astronomy and the atmosphere

**Scope:** space traffic management (STM) and space situational awareness (SSA) data and gaps; commercial SSA players; debris removal and servicing; breakups and Kessler-risk metrics; reentries and ground debris; atmospheric pollution from reentry; space weather (Solar Cycle 25, satellite drag, GNSS/aviation/grid); satellite streaks and radio interference in astronomy; policy (FCC 5-year rule, EU Space Act, UN COPUOS, Space Sustainability Rating).

**Researched on 2026-10-24.**

**How to read this file:** sections A–J hold one entry per organisation, resource or problem (fields: what it is, problems, solutions, data, off-the-shelf tech, hackathon angle, credibility, sources). Items marked "search result" were seen in search results but not opened; items marked "not verified" or "unverified" need checking before use.

---

## A. Space environment: headline numbers and metrics

### A1. ESA Space Environment Report 2026 (ESA Space Debris Office)

- **What it is:** ESA's annual report on the state of the orbital environment, published since 2017. The 2026 edition (Issue 10.1, reference GEN-DB-LOG-00288-OPS-SD, dated 8 September 2026, web release 14 September 2026) covers data up to end of 2025. 152 pages.
- **Problems / pain points:**
  - "In 2025, more than 300 launches took place with over 4000 new payloads put into orbit" (ESA web page). About ten payloads launched per day; more than three intact satellites or rocket bodies reenter per day.
  - **1,200 intact objects reentered in 2025** (PDF, executive summary).
  - The Space Environment Health Index jumped "from about 4 to 50 in just one year". In the business-as-usual scenario the environment's risk level is predicted to be 50 times higher than the first sustainability threshold (it was 4 times in the 2025 edition).
  - Projection horizon was cut from 200 to 100 years "reflecting the increasingly rapid evolution of the orbital environment". Even with no further launches, debris-on-debris collisions would grow the LEO population.
  - **Catalogue gap:** "the number of space objects with unidentified object class continues to increase ... This mismatch between detected and catalogued fragments remains a point of attention. Notably, the majority of fragments associated with new events this year are asserted rather than catalogued by the U.S. Space Surveillance Network, and were identified through various alternative space surveillance networks and service providers."
  - **Fragmentation rate:** on average 9.8 non-deliberate fragmentations per year over the last two decades. 2024 added over 3,000 catalogued fragments, mostly from propulsion-related breakups; 2025 added comparatively few.
  - **2025 fragmentation table (Table 3.7):** 2025-01-17 payload, 3,980 kg, MEO, propulsion, 0 catalogued / 67 asserted fragments; 2025-06-01 rocket body, 2,020 kg, eccentric GEO orbit, unknown cause, 2/2; 2025-12-18 payload, 530 kg, LEO, propulsion, 0/10 (date matches the Starlink 35956 anomaly, see A6).
  - **Compliance:** of payloads that reached end of mission in LEO since 2020, 88–99% of those under 1,000 kg are in orbits that naturally meet the 25-year rule, but only 54% of larger payloads. Of payloads that end life in non-compliant orbits, only 5–50% successfully comply with the 25-year limit, and 5–35% with the 5-year limit, over the last decade. Rocket body controlled reentries rose from 10% to over 65% of the decade. "While a common target for successful post-mission disposal is 90%, this practice will not by itself reduce the amount of debris in orbit, and will need to increase to near 100%."
  - **Casualty risk (new in 2026):** aggregate on-ground casualty risk from uncontrolled reentries is growing with reentry counts. Uses a 1-in-10,000 per-reentry threshold and fragments ≥15 J. Secondary press (NewsBytes) claims it "doubled since 2020"; not verified against ESA text.
  - Conjunction hot band: "the need for effective space traffic coordination in altitude ranges with high concentrations of active and manoeuvrable satellites (400 km - 600 km)".
- **How they're trying to solve it:** ESA Zero Debris Approach (limit debris from future missions by 2030); ESA Space Debris Mitigation Standard (2023) cut post-mission lifetime limit from 25 to 5 years plus a cumulative collision probability <10⁻³ for objects >1 cm; calls for active debris removal ("Active debris removal must become part of the solution and soon"), data sharing on planned constellation deployments, design-for-demise and controlled reentries, and research on atmospheric pollution from reentries.
- **Data:** Report built on DISCOS (ESA's object database), USSTRATCOM TLEs, Vimpel (Russian) data, RAE tables, the MASTER model (reference population 1 Feb 2026) and the DELTA-4 long-term evolution model. Conjunction statistics computed with ESA CRASS on GP (TLE) data, Alfriend–Akella collision probability. The PDF figures are images, but tables are extractable.
- **Off-the-shelf tech:** `pdftotext` to pull tables; DISCOSweb API (free account) for object mass/area; `sgp4` / Skyfield to reproduce the conjunction-statistics method on public TLEs.
- **Hackathon angle:** (1) Rebuild a live "orbital health index" dashboard from public Space-Track/CelesTrak GP data plus DISCOS mass, updated daily rather than once a year. (2) "Asserted vs catalogued" tracker: fragments seen by commercial networks but missing from the public catalogue. (3) Compliance auditor: for each payload that has gone quiet, estimate remaining orbital lifetime and flag likely 5-year-rule violators.
- **Credibility:** official (ESA).
- **Sources:**
  - [ESA Space Environment Report 2026, ESA web page (14 Sep 2026)](https://www.esa.int/Space_Safety/Space_Debris/ESA_Space_Environment_Report_2026)
  - [ESA's Annual Space Environment Report, Issue 10.1, PDF (8 Sep 2026)](https://www.sdo.esoc.esa.int/environment_report/Space_Environment_Report_latest.pdf)
  - [ESA Space Environment Report 2025 (1 Apr 2025)](https://www.esa.int/Space_Safety/Space_Debris/ESA_Space_Environment_Report_2025)
  - [NewSpace Economy: What does ESA's new report reveal (17 Sep 2026)](https://newspaceeconomy.ca/2026/09/17/what-does-esas-new-report-reveal-about-the-risks-facing-satellites/) (secondary)
  - [NewsBytes: casualty risk doubled since 2020](https://www.newsbytesapp.com/news/science/esa-warns-earths-orbit-crowding-casualty-risk-doubled-since-2020/tldr) (secondary, unverified)
  - [Space.com / Leonard David: risk of debris falling to Earth is growing](https://www.space.com/space-exploration/satellites/the-risk-of-space-debris-falling-to-earth-and-causing-deaths-and-is-growing-experts-say) (secondary)

### A2. ESA Space Environment Report 2025 (previous edition)

- **What it is:** Issue 9.0 (31 March 2025, released 1 April 2025), data to end of 2024.
- **Problems / pain points:** ~40,000 tracked objects, ~11,000 active payloads; ESA model estimates ~54,000 objects >10 cm and ~1.2 million objects 1–10 cm (per ScienceAlert summary). Density of active payloads approaching that of debris in some altitude bands (MASTER-2024). Environment index projected at 4× sustainable threshold (vs 50× in the 2026 edition).
- **Credibility:** official; numbers via reputable press.
- **Sources:** [ESA Space Environment Report 2025 (1 Apr 2025)](https://www.esa.int/Space_Safety/Space_Debris/ESA_Space_Environment_Report_2025); [ScienceAlert summary](https://www.sciencealert.com/esa-report-says-theres-too-much-junk-in-earth-orbit-trunk); [UN-SPIDER note](https://www.un-spider.org/news-and-events/news/esa-space-environment-report-2025)

### A3. CRASH Clock (Thiele, Heiland, Boley, Lawler; arXiv Dec 2025, Acta Astronautica)

- **What it is:** "An Orbital House of Cards: Frequent Satellite Close Conjunctions", arXiv:2512.09643 (v1 10 Dec 2025, v3 29 June 2026; accepted in *Acta Astronautica*). Proposes the **CRASH Clock = "Collision Realization And Significant Harm" Clock**: expected time until a potentially catastrophic collision if all satellites stopped maneuvering (e.g., after a severe solar storm or loss of SSA).
- **Problems / pain points:**
  - CRASH Clock was **164 days in January 2018**, **5.5 days in June 2025**, and **2.5 days as of May 2026** (v3).
  - 5.5 days ≈ 17% chance of ≥1 potential collision in any 24-hour no-maneuver window.
  - Close approaches within 1 km: about one every 36 s (analytic) / 44 s (simulation) across LEO; Starlink–other object about every 47 s (converted: ~1,800–2,400 per day).
  - Framed as resilience: how much time we have to recover from a widespread disruption such as a geomagnetic storm.
- **How they're trying to solve it:** a single easy-to-communicate metric for regulators; authors stress it is "not a strict limit" and they "are not making any claim about this being a runaway collisional cascade".
- **Data:** Space-Track 3LE catalogue snapshots (1 Jan 2018 and 25 June 2025), 1-km spherical shells, number densities, cross-sections (10-5-10 rule: 10 m sat-sat, 5 m sat-debris, 10 cm debris-debris), mean relative speed = 4/3 circular speed.
- **Off-the-shelf tech:** Python + numpy; Space-Track historical GP (TLE) files to recompute the clock back in time; `sgp4` for full propagation version.
- **Hackathon angle:** "CRASH Clock live": recompute the clock daily from public TLEs, back-fill a 2010–2026 time series, and add a "what-if" slider (a constellation stops maneuvering, a storm knocks out tracking for N hours). Very communicable to judges.
- **Credibility:** peer-reviewed (accepted, Acta Astronautica) plus arXiv preprint; widely covered.
- **Sources:**
  - [arXiv:2512.09643 abstract](https://arxiv.org/abs/2512.09643) and [HTML full text](https://arxiv.org/html/2512.09643) (v3, 29 June 2026)
  - [Scientific American: Satellites used to have months to avoid collisions, now they have days](https://www.scientificamerican.com/article/satellites-used-to-have-months-to-avoid-collisions-now-they-have-days) (reputable press)
  - [IEEE Spectrum: Kessler syndrome CRASH clock](https://spectrum.ieee.org/kessler-syndrome-crash-clock) (reputable press)
  - [TechSpot: CRASH clock reveals how close next satellite collision](https://www.techspot.com/news/111055-crash-clock-reveals-how-close-next-satellite-collision.html) (press)

### A4. Starlink collision-avoidance maneuvers (SpaceX semiannual reports to the FCC)

- **What it is:** SpaceX must file semiannual reports to the FCC on Starlink constellation status, maneuvers, failures and disposals.
- **Problems / pain points:**
  - Dec 2024–May 2025: 144,404 maneuvers. June–Nov 2025: **148,696** (filed 31 Dec 2025, ~70% by Gen2). Dec 2025–May 2026: **207,152** (65,137 Gen1, 142,015 Gen2; filed 1 July 2026). That is >355,000 in 12 months, about one maneuver every ~90 seconds; ~36 maneuvers per Gen1 satellite per year, ~46 per Gen2.
  - SpaceX maneuvers at a probability of collision above **3×10⁻⁷**, much stricter than the common 1×10⁻⁴ threshold, which inflates maneuver counts.
  - Ephemeris sharing problems reported by SpaceX (Dec 2025 filing, as quoted by Altagrove): "prolonged ephemeris outages, where operators of maneuvering satellites fail to upload data" to Space-Track; "Others provide data with insufficient lead time for effective screening"; some "only share ephemerides before planned maneuvers"; "physically implausible trajectories"; ephemerides that "diverge significantly from actual satellite paths"; "Unreliable thrusters or poorly planned maneuvers often contribute to these inaccuracies." Chinese and Russian operators often do not share ephemerides or contacts; UNOOSA has acted as go-between in several conjunctions.
  - Single operator Honghu-2 (Hongqing Technology, China) caused 1,143 Starlink maneuvers (Dec 2025 filing per Altagrove).
  - 260 Starlink satellites disposed by reentry Dec 2025–May 2026 (176 Gen1, 84 Gen2), 349 more decommissioned; 4 satellites with suspected hardware failures that could not deorbit normally (incl. STARLINK-34343, which later broke up, see A6).
  - Plan to lower ~4,400 Starlinks from 550 km to 480 km during 2026.
- **How they're trying to solve it:** autonomous collision avoidance; ephemeris published on Space-Track (public, every ~8 h); advocacy for mandatory ephemeris sharing and status disclosure by all operators; lowering orbits.
- **Data:** FCC IBFS/ICFS filings (public PDFs, SAT-MOD / SAT-LOA dockets); Starlink operator ephemerides on Space-Track (requires account); public TLE/GP history.
- **Off-the-shelf tech:** PDF table extraction; Space-Track API; `sgp4`; maneuver-detection by TLE differencing.
- **Hackathon angle:** "Who makes Starlink dodge?" Join public GP data with CelesTrak SOCRATES to rank which operators/objects drive the most close approaches against Starlink, and flag operators whose published ephemerides diverge from observed TLEs (an "ephemeris quality scorecard").
- **Credibility:** official filings; numbers here are via reputable press and secondary sites (primary filing not opened).
- **Sources:**
  - [Space.com: Every SpaceX Starlink satellite has to dodge a collision almost weekly (July 2026)](https://www.space.com/space-exploration/satellites/every-spacex-starlink-satellite-has-to-dodge-a-collision-almost-weekly-and-experts-fear-the-worst) (reputable press; figures from search snippets)
  - [Gigazine: SpaceX Starlink report, July 2026 (6 Jul 2026)](https://www.gigazine.net/gsc_news/en/20260706-spacex-starlink-satelite) (press)
  - [Altagrove GroveWire: SpaceX 148,696 Starlink collision maneuvers ... operators' slipshod reporting (13 Jan 2026)](https://www.altagrove.com/grovewire-news/spacex-148696-starlink-collision-maneuvers-in-6-months-ending-nov-30-continued-issues-with-operators-slipshod-reporting) (blog/secondary)
  - [FCC ICFS attachment (SpaceX filing)](https://api-prod.fcc.gov/icfs-attachment/exp/api/v1/bff0244acfb947505791bf252f851ce6) (official; appeared in search, not opened)
  - [KeepTrack: Collision avoidance conjunction screening deep dive](https://www.keeptrack.space/deep-dive/collision-avoidance-conjunction-screening) (blog; claims ~300,000 maneuvers in 2025 vs 200,000 in 2024; conflicts with other figures)

### A5. TraCSS (Traffic Coordination System for Space), US Office of Space Commerce

- **What it is:** The civil space traffic coordination system the Department of Commerce is building to take over basic SSA/conjunction services for civil and commercial operators from the US Space Force (Space Policy Directive-3, 2018).
- **Problems / pain points:**
  - The FY2026 President's budget proposed cutting OSC to $10 million and terminating TraCSS. Seven industry associations representing 450+ companies wrote to Congress to save it (July 2025). Appropriators in both chambers restored funding; Senate committee proposed $60 million.
  - FY2026 enacted OSC level: **$52.5 million**. FY2027 request: **$11 million** (about 80% cut), which does not mention TraCSS by name.
  - As of 17 July 2026: TraCSS "still in a pilot phase but is essentially operational", 62 pilot users covering more than 11,000 satellites; OSC is containerizing the code and weighing a contractor-owned model, a data-as-a-service model, or a government system, and possibly a fee-based model.
  - Taylor Jordan (OSC director): "The question is not should we provide [space situational awareness] data, it's how do we do that as a federal government?" "the basic function of the system we're creating is collision avoidance. Are there other capabilities that could be built on top of that? Sure, there could be."
- **How they're trying to solve it:** pilot program with commercial data suppliers (e.g., commercial SSA firms), cloud-native architecture, onboarding operators.
- **Data:** TraCSS is not a public open dataset; operators get CDMs and screening. Public elements still come via Space-Track.
- **Off-the-shelf tech:** CCSDS CDM / OEM / OPM message standards; open-source parsers.
- **Hackathon angle:** "TraCSS-lite for everyone": a free, open conjunction screening service on public GP data with a clear explanation of uncertainty, targeted at universities and small operators who may lose free service if TraCSS is cut or becomes fee-based.
- **Credibility:** reputable press (FedScoop, Breaking Defense, Payload, The Register, Reuters/Yahoo).
- **Sources:**
  - [FedScoop: Space Commerce official says TraCSS continues (17 Jul 2026)](https://fedscoop.com/space-commerce-official-tracss-continues/)
  - [FedScoop: TraCSS continues despite budget uncertainty](https://fedscoop.com/space-commerce-official-tracss-continues-despite-budget-uncertainty/)
  - [Breaking Defense: Appropriators restore funding for Commerce's TraCSS (July 2025)](https://breakingdefense.com/2025/07/appropriators-restore-funding-for-commerces-tracss-spacewatch-effort/)
  - [Payload: NOAA proposes terminating TraCSS program](https://payloadspace.com/noaa-proposes-terminating-tracss-program/)
  - [The Register: Please don't cut funds for space traffic control, industry begs Congress (10 Jul 2025)](https://www.theregister.com/2025/07/10/space_traffic_control_congress/)
  - [Reuters via Yahoo: Space industry urges US Congress not to axe system that prevents satellite collisions](https://www.yahoo.com/news/space-industry-urges-us-congress-093551264.html)

### A6. Breakups and fragmentation events, 2024–2026

- **What it is:** In-orbit fragmentations (explosions of tanks/batteries, collisions, unknown) are the dominant source of debris (ESA).
- **Events:**
  - **Long March 6A upper stage, 6 Aug 2024** (Qianfan / Thousand Sails launch, ~810 km polar): USSPACECOM tracked "over 300 pieces"; LeoLabs said "at least 700 debris fragments and potentially more than 900"; Slingshot saw ≥50 pieces on 7 Aug. Same rocket type broke up in Nov 2022 (533 catalogued fragments by Jan 2023). ESA lists both events (L-15/YF115 stage, 6,000 kg) as top contributors to conjunctions.
  - **Intelsat 33e, 19 Oct 2024 (GEO):** total loss after power loss; Space Force S4S first ~20 then 50+ pieces; ExoAnalytic 57 pieces on 21 Oct and ~500 by late October ("softball-sized to car-door-sized"); KeepTrack says >700 by December (unverified). Not insured. Small GEO fragments are hard to observe consistently.
  - **2025 events (ESA table):** a MEO payload (17 Jan 2025, propulsion, 67 asserted fragments), a rocket body in eccentric GEO orbit (1 June 2025), a LEO payload (18 Dec 2025, propulsion, 10 asserted).
  - **Starlink 35956, 17 Dec 2025:** anomaly at 418 km while raising orbit, propulsion tank venting, ~4 km altitude drop, "small number of trackable debris"; LeoLabs first said "tens" of pieces, later "hundreds", spread over 6,000 km of the orbit within days, from an "internal energetic source rather than a collision". SpaceX deployed software protections.
  - **Russian "inspector" satellite, January 2026, GEO:** disintegrated (per Space.com; details not verified).
  - **Starlink 34343, 29 Mar 2026, ~560 km:** V2 Mini Optimized; LeoLabs saw "tens of objects"; internal cause; McDowell: risk increase "fairly small", maybe ~10% for a few months; "I don't see how the risks can be nil." Ahead of Artemis II.
  - **Long March 6C upper stage, 27 Aug 2026, 02:30 UTC:** LeoLabs on X: "We estimate tens to hundreds of fragments were generated" (NORAD 100472, expected to reenter in a few years).
  - **USA 32, September 2026:** Cold War-era US satellite confirmed to have disintegrated (Space.com; details unverified).
  - **Meteor 2-7, 5 Oct 2026 (~855 km):** Soviet 1981 weather satellite; detected by LeoLabs' Western Australia radar with its "LeoLabs Delta" system; "tens of fragments"; cause unknown (battery/pressure vs untracked debris impact). LeoLabs calls it the latest in a series of debris-generating events in six months; Space.com headline: "a worrying trend".
- **Problems / pain points:** detection latency and attribution (who broke up, why); the US public catalogue lags commercial detections; fragments in long-lived orbits (800+ km) persist for decades; GEO fragments are hard to track.
- **How they're trying to solve it:** commercial radar (LeoLabs), optical (ExoAnalytic, Slingshot), passivation requirements, design fixes (SpaceX software patch).
- **Data:** Space-Track SATCAT and GP history (new objects with same international designator), CelesTrak "breakup" groups, ESA Fragmentation Database (DISCOS), NASA ODQN breakup reports.
- **Off-the-shelf tech:** `sgp4`, NASA Standard Breakup Model implementations (open source), Gabbard diagrams (period vs apogee/perigee) in matplotlib/Plotly.
- **Hackathon angle:** "Breakup detector + Gabbard diagram generator": watch the public GP feed for clusters of new objects sharing a parent designator, auto-generate the Gabbard diagram and a 30-day spread animation, and estimate which operational constellations' shells the cloud crosses.
- **Credibility:** mix of official (USSPACECOM, ESA), company statements (LeoLabs, ExoAnalytic, SpaceX), reputable press.
- **Sources:**
  - [Space.com: Chinese rocket breaks apart after megaconstellation launch (Aug 2024)](https://www.space.com/china-megaconstellation-launch-space-junk)
  - [SpaceNews (Aug 2024)](https://spacenews.com/?p=498436)
  - [Air & Space Forces Magazine (Aug 2024)](https://airandspaceforces.com/?p=229465)
  - [DataCenterDynamics: 500 pieces of debris from Intelsat 33e now being tracked (Oct 2024)](https://www.datacenterdynamics.com/en/news/500-pieces-of-debris-from-intelsat-33e-now-being-tracked)
  - [SpaceNews: Intelsat 33e (Oct 2024)](https://spacenews.com/?p=507754)
  - [KeepTrack: Intelsat 33e breakup deep dive](https://keeptrack.space/deep-dive/intelsat-33e-breakup) (blog)
  - [The Register: Starlink satellite fails, polluting orbit with debris (23 Dec 2025)](https://www.theregister.com/2025/12/23/starlink_satellite_fails_debris/)
  - [Engadget: A Starlink satellite just exploded and left trackable debris (Dec 2025)](https://engadget.com/science/space/a-starlink-satellite-just-exploded-and-left-trackable-debris-120002814.html)
  - [Business Standard / Reuters: Starlink loses contact with satellite (19 Dec 2025)](https://www.business-standard.com/world-news/starlink-satellite-anomaly-debris-loses-contact-low-earth-orbit-125121900826_1.html)
  - [Space Domain substack: Starlink's First Space Debris Event](https://spacedomain.substack.com/p/starlinks-first-space-debris-event) (blog)
  - [EarthSky: Starlink satellite breaks up (31 Mar 2026)](https://earthsky.org/space/starlink-satellite-breaks-up-debris-artemis-risk/)
  - [SatNews: SpaceX loses contact with Starlink satellite (30 Mar 2026)](https://satnews.com/2026/03/30/spacex-loses-contact-with-starlink-satellite/)
  - [FODNews: Long March 6C upper stage fragments into hundreds of pieces](https://fodnews.com/long-march-6c-upper-stage-fragmentation-debris/) (niche news)
  - [Space.com: A dead Soviet satellite just broke apart in orbit (again), "a worrying trend" (Oct 2026)](https://www.space.com/space-exploration/satellites/a-dead-soviet-satellite-just-broke-apart-in-orbit-again-experts-say-its-part-of-a-worrying-trend)
  - [EarthSky: Meteor 2-7 breakup (Oct 2026)](https://earthsky.org/?p=560313)
  - [Universe Magazine: Soviet weather satellite from 1981 broke up](https://universemagazine.com/en/a-soviet-weather-satellite-from-1981-broke-up-into-dozens-of-fragments/)
  - [Spidersweb (PL): Meteor 2-7 (Oct 2026)](https://spidersweb.pl/2026/10/meteor-2-7-satelita-rozpad-odlamki.html)

### A7. LeoLabs / McKnight "Top 50 most concerning objects" (IAC 2025, Sydney)

- **What it is:** Paper led by Darren McKnight (LeoLabs senior technical fellow) at IAC 2025 ranking the 50 derelict objects in LEO most likely to generate new debris via collisions, by mass, altitude and proximity to traffic.
- **Problems / pain points:** 88% of the top 50 are rocket bodies; 76% were left last century; 34 from Russia/USSR (30 are SL-16 and SL-8 stages), 10 from China, 3 US, 1 Japan; #1 a Russian SL-16, #2 ESA's Envisat. Removing these 50 would cut debris-generation risk roughly in half. Earlier LeoLabs work (2021): 65% of the top 200 riskiest conjunctions were debris-on-debris; 35 involved SL-8 stages. Derelict-on-derelict collisions are outside any operator's control (e.g., Cosmos 2361 vs SL-8 stage near-miss of ~6 m at ~984 km, 27 Jan 2023).
- **How they're trying to solve it:** prioritized active debris removal (ADR) target list; "just-in-time collision avoidance" ideas (nudging derelicts).
- **Data:** public GP + LeoLabs radar; DISCOS mass.
- **Hackathon angle:** "ADR target ranker": reproduce a top-50 list from public data with an open, explainable scoring (mass × local traffic density × lifetime), and show how the ranking changes as new constellations fill shells.
- **Credibility:** conference paper (IAC) via reputable press.
- **Sources:**
  - [Ars Technica via syndication: Removing these 50 objects from orbit would cut danger from space junk in half (Oct 2025)](https://threatbeat.com/threats/removing-these-50-objects-from-orbit-would-cut-danger-from-space-junk-in-half/)
  - [heise: Experts identify the 50 most dangerous pieces of space debris (Oct 2025)](https://heise.de/-10728122)
  - [Leonard David: LeoLabs/McKnight](https://www.leonarddavid.com/?p=49259)
  - [Fox Weather: Satellite, rocket body miss collision by only 20 feet (2023)](https://www.foxweather.com/earth-space/space-debris-collision-satellite-rocket-body)

### A8. More 2026 breakups and the battery-passivation gap (NASA ODQN Sept 2026)

- **What it is:** NASA ODQN Vol. 30 Iss. 3 (Sept 2026) lead story: **breakup of China's ZhuQue-2E (ZQ-2E) upper stage** (2026-128C, SSN #69537) at 08:47 GMT on 9 June 2026, shortly after payload deployment, at ~416 × 327 km, 54.53°. "Many fragments were identified initially. As of 16 July 2026, 7 fragments have been added to the U.S. Satellite Catalog and 4 of them have reentered." (A ZQ-2E also exploded minutes after liftoff in Aug 2025.)
- **Problems / pain points (NASA Battery Passivation Workshop, JSC, 11–13 March; the text says 2025, the header says 2026):**
  - "substantial confusion about what qualifies as an acceptable practice, what level of testing is required" for battery passivation in Orbital Debris Assessment Reports (ODARs), especially for commercially built buses.
  - "A recurring challenge noted in the workshop is the lack of a comprehensive NASA database on battery failure modes, debris generation potential, and end-of-life behavior." Commercial Li-ion cells have spontaneous internal short rates of roughly 1 in 1 million to 1 in 10 million; "Thermal runaway propagation, battery ejecta characteristics, and battery debris size distributions remain poorly quantified".
  - A commercial spacecraft in 2023 had arc-induced thermal runaway from a foreign object in the pack.
  - Industry practices vary: relays/MOSFET disconnects, tumbling to limit solar input, relying on natural decay.
  - Fits the 2025–2026 pattern of "internal energetic source" breakups of Starlinks (A6).
- **ES-MCAT (Ascension Island) GEO survey:** ten years of operations; many detections are **uncorrelated targets (UCTs)** not in the public catalogue; UCT magnitudes peak at 18–19 in the 2023–2025 survey; true small-debris population keeps rising following a power law below the detection limit.
- **Hackathon angle:** "Breakup early warning from public data": a model that flags satellites likely to fragment (age, bus type, no passivation, eclipse thermal cycling, history of anomalies) using GCAT + ESA fragmentation history; or an "anomaly-to-breakup" timeline database from news + catalogue.
- **Credibility:** official (NASA).
- **Sources:** [NASA ODQN Vol. 30 Iss. 3, Sept 2026 (PDF)](https://orbitaldebris.jsc.nasa.gov/quarterly-news/pdfs/ODQNv30i3.pdf)

### A9. Russian RPO near a Ukraine-used SAR satellite: KOSMOS 2612 and ICEYE-X36 (Oct 2026)

- **What it is:** Marco Langbroek (SatTrackCam Leiden, TU Delft) analysis, 17–21 Oct 2026. KOSMOS 2612 (2026-083H, launched Plesetsk 16 Apr 2026) maneuvered on 30 Sept, 12, 15 and 16 Oct 2026, "clearly designed" to match ICEYE-X36's (2024-043F) altitude, eccentricity and period; within 1–2 km at 18:15 UTC 17 Oct; predicted approach to "a few meters" (large TLE uncertainty), revised to "a few hundred meters or possibly much closer" around 01:35 UTC 18 Oct; further maneuvers 18 and 19 Oct; ~480 km apart on 21 Oct.
- **Problems / pain points:** "completely non-consensual" rendezvous and proximity operation; possible ASAT rehearsal; attribution is very hard if the target fails. **Detected entirely from public TLEs** by an independent analyst, showing both the power and the limits (uncertainty) of public data for maneuver detection.
- **Hackathon angle:** **"Who is stalking whom?"**: automatic detection of unannounced maneuvers and co-orbital approaches in the full public GP catalogue (pairwise relative-orbit screening, flag objects that change orbit to match another object's plane/period). Ready training data: SPLID (J2).
- **Credibility:** expert blog (well-regarded independent tracker).
- **Sources:** [SatTrackCam Leiden, October 2026 archive ("KOSMOS 2612 and ICEYE-X36: a worrisome cat-and-mouse-game in Space", 17 Oct 2026)](https://sattrackcam.blogspot.com/2026/10/)

### A10. Kessler-risk and orbital-capacity metrics (beyond ESA index and CRASH Clock)

- **What it is:** Competing ways to quantify "how full" LEO is.
  - **ESA Environment/Health Index** (A1): 50× the first sustainability threshold in business-as-usual (2026 edition).
  - **CRASH Clock** (A3): 2.5 days (May 2026).
  - **LeoLabs/McKnight "Top 50" update** (9th European Conference on Space Debris, Bonn, 2025; co-authors from LeoLabs, L3Harris, JAXA, IFAC-CNR, UKSA, Bauman MSTU): ranks derelicts by (1) aggregate collision risk since 1 Jan 2022, (2) fragment persistence, (3) proximity to the highest-risk 100-km bands centred ~675, 840, 1000 and 1450 km, (4) likelihood of spontaneous explosion. Original 2020 list by 19 experts from 13 countries.
  - **MIT ARCLab MOCAT / pySSEM:** open-source (MIT licence) Python source-sink evolutionary model of LEO by species (active, derelict, debris) and altitude shell, with launch, post-mission disposal, collision-avoidance and drag parameters, to estimate orbital capacity. AMOS 2026 papers extend source-sink models (KAIST inclination-aware 2D; Purdue narrow-shell stochasticity; Clemson/Purdue "Stochastic Dynamics of LEO Near Full Capacity"; Embry-Riddle E-MOCAT for policy assessment).
- **Problems / pain points:** metrics disagree and are hard for policymakers to read; results depend on unknown future launch plans (ITU paper filings, I3) and compliance assumptions; ESA warns that "Projections of future traffic remain subject to considerable uncertainty".
- **Hackathon angle:** "Orbit capacity calculator for regulators": a web UI on top of pySSEM where a user picks a new constellation (size, altitude, PMD success) and sees its effect on the CRASH Clock and collision count by 2050. Ties licensing decisions (FCC, EU) to a number.
- **Credibility:** conference papers + open-source academic code.
- **Sources:** [ECSD 2025: "An Update of the Top 50 List" (McKnight et al.)](https://conference.sdo.esoc.esa.int/proceedings/sdc9/paper/4); [GitHub ARCLab-MIT/pyssem](https://github.com/ARCLab-MIT/pyssem); [AMOS 2026 technical papers](https://amostech.space/amos/2026/); [ESA SER 2026 PDF](https://www.sdo.esoc.esa.int/environment_report/Space_Environment_Report_latest.pdf)

### A11. The small-debris tracking gap (<10 cm, "lethal non-trackable")

- **What it is:** The public catalogue covers roughly >10 cm in LEO (SWPC: SSN tracks "over 20,000 objects larger than 10 cm"); ESA estimates ~1.2 million objects 1–10 cm (2025 report summary) that can still disable a satellite.
- **Evidence:**
  - NASA ODPO radar (Manis et al., ECSD 2025): HUSIR detects ~5 mm at 1000 km and ~2–3 cm throughout LEO; Goldstone ~2–3 mm below 1000 km; >500 hours/year combined; tracks NaK coolant droplets near 65° and a persistent cloud near 82°.
  - Digantara EISCAT beam-park (AMOS 2026): >1,000 detections in 24 h around CZ-6A breakup clouds; many uncorrelated with the catalogue.
  - ESA SER 2026: most fragments of 2025 events are "asserted rather than catalogued".
  - NASA ES-MCAT: GEO uncorrelated targets peak at mag 18–19 (A8).
  - Concepts: star-tracker-based detection of ≤10 cm debris (Filho et al., ECSD 2025; simulation, "an initial step toward a future catalogue for objects ≤10 cm"); SpaceX Stargaze sees ~0.5 m routinely, aims at cubesat size.
- **Problems / pain points:** operators cannot avoid what is not catalogued; risk is estimated statistically (ORDEM/MASTER flux) not per-object.
- **Hackathon angle:** "Invisible risk map": combine MASTER/ORDEM-style flux statistics (published curves) with operator shells to show where untracked debris risk dominates tracked risk; or a model of "expected unseen fragments" for each breakup using the NASA Standard Breakup Model vs what was catalogued.
- **Credibility:** official + conference.
- **Sources:** [ECSD 2025: Monitoring the Small Debris Environment with Ground-based Radar 2016–2023 (Manis et al.)](https://conference.sdo.esoc.esa.int/proceedings/sdc9/paper/29); [ECSD 2025: Sub-10 cm space debris detection with a star tracker (Filho et al.)](https://conference.sdo.esoc.esa.int/proceedings/sdc9/paper/14); [AMOS 2026: Digantara EISCAT CZ-6A](https://amostech.space/year/2026/independent-radar-detection-and-characterization-of-the-cz-6a-breakup-debris-cloud-in-leo-insights-from-eiscat-uhf-beam-park-campaigns/); [SWPC satellite drag page](https://www.spaceweather.gov/impacts/satellite-drag); [ECSD proceedings list](https://conference.sdo.esoc.esa.int/proceedings/list)

---

## B. Public SSA data sources and their gaps

### B1. Space-Track.org (US Space Force)

- **What it is:** The official public distribution point for the US public satellite catalogue (SATCAT), general perturbations (GP) element sets (TLE/OMM), decay and TIP (tracking and impact prediction) messages, and, for registered operators, conjunction data messages (CDMs) and operator ephemerides. Free account required.
- **Problems / pain points:**
  - Strict rate limits: "Limit API queries to less than 30 requests per 1 minute(s) and 300 requests per 1 hour(s)"; GP 1/hour; GP_HISTORY "1 / lifetime" (bulk history via yearly zip files); CDM 3/day for all constellation CDMs; TIP 1/hour (10 min allowed within 12 h of reentry).
  - **Catalogue number exhaustion / Alpha-5:** object numbers 100,000–339,999 are written in TLE lines with a letter prefix ("Alpha-5", 100000 → "A0000"); other formats (XML, KVN, JSON, CSV) handle up to 999,999,999. The documentation itself is inconsistent (one FAQ says objects above 99,999 "are not available in TLE/3LE format"). Legacy `tle` classes are to be deprecated; OMM formats recommended for new development.
  - CDMs sit behind operator login; not openly downloadable, so researchers lack real conjunction data (one reason the ESA Kelvins dataset matters, see J1).
  - Public GP/TLE accuracy is limited (km-level errors, no covariance), see B3.
- **How they're trying to solve it:** OMM formats, Alpha-5, cloud bulk files, operator ephemeris hosting (Starlink, OneWeb, Kuiper, Iridium, SES, Telesat, etc.), planned hand-off of civil services to TraCSS.
- **Data:** SATCAT, GP (current), GP_HISTORY (full TLE history since 1957), DECAY, TIP, BOXSCORE, SATCAT_DEBUT, 60-day decay predictions; public files.
- **Off-the-shelf tech:** `spacetrack` Python client, `sgp4`, Skyfield, Orekit, `astropy`; OMM parsers.
- **Hackathon angle:** any project here starts from Space-Track/CelesTrak GP data; the full TLE history (yearly zip files) is a "large dataset" in the sense the challenge wants (tens of millions of element sets).
- **Credibility:** official.
- **Sources:** [Space-Track documentation (accessed 2026-10-24)](https://www.space-track.org/documentation)

### B2. CelesTrak (T.S. Kelso): GP data, SupGP, SOCRATES, and the 5-digit catalogue number cliff

- **What it is:** Free, long-running redistribution and analysis site run by T.S. Kelso: GP data by group (Starlink, OneWeb, Qianfan, Hulianwang Digui (Guowang), Kuiper, GEO, debris clouds of Fengyun-1C, Iridium 33, Cosmos 2251, etc.) in CSV, JSON, OMM XML/KVN, TLE; SATCAT; SupGP (operator-derived GP data); SOCRATES conjunction screening.
- **Problems / pain points:**
  - **"We ran out of 5-digit catalog numbers on 2026-07-11."** "All newly cataloged objects have 6-digit catalog numbers of 100000+", so their GP data is not available in TLE format from CelesTrak; official USSF SATCAT has reached 101150. Any legacy tool, ground station, amateur tracker or student code that parses fixed-width TLEs silently misses new objects (new launches, new debris). Default CelesTrak format became CSV "as of 2026 May 09".
  - **Standard GP accuracy is poor relative to operator data.** SupGP test: GPS average error 7.54 km (Space-Track GP) vs 0.87 km (SupGP), max 32.45 km vs 2.37 km; GLONASS 3.30 km vs 0.20 km. "approximately an order of magnitude improvement in the error". Intelsat post-maneuver sets marked [PM].
  - **SOCRATES Plus** screens active payloads against the full catalogue three times a day for 7 days ahead, reporting conjunctions "within 5 km at time of closest approach"; the minimum-range method ignores covariance and "can exaggerate risk"; maximum probability is "more reasonable (although still conservative)". Excluding intra-fleet conjunctions among fully operational constellation satellites cut the list "from 143,997 to 56,343" (2 Mar 2023). (SOCRATES page last updated 5 Apr 2023; considering switching to SupGP.)
  - Download etiquette: GP data updates every 2 hours; repeated requests on 403/404 errors are blocked.
- **How they're trying to solve it:** OMM/CSV/JSON formats, SupGP from operator ephemerides (SpaceX Starlink, OneWeb, Kuiper, Iridium, SES, Telesat, Orbcomm, AST SpaceMobile, EUMETSAT, Planet, Intelsat, NASA ISS, China's CSS, GPS almanac, GLONASS).
- **Data:** SATCAT, GP by group, SupGP, SOCRATES tables; SATCAT boxscore on 24 Oct 2026: 20,364 payloads on orbit, 15,030 debris on orbit (incl. rocket bodies per CelesTrak boxscore categories), 35,394 total on orbit, 35,738 decayed; US 18,595 on orbit, PRC 6,192, CIS 6,658.
- **Off-the-shelf tech:** `sgp4` (Vallado/Rhodes, matches "Revisiting Spacetrack Report #3"), Skyfield, `satellite.js`, CesiumJS for 3D.
- **Hackathon angle:** (1) "Six-digit migration checker": a linter/test harness that tells amateur and university ground-station software whether it breaks on catalogue numbers ≥100000 and auto-converts TLE pipelines to OMM. (2) "SOCRATES with probabilities": rescreen with SupGP and a simple covariance model, show how many 5-km alerts are false alarms. (3) GP-vs-SupGP error maps by constellation.
- **Credibility:** reputable expert-run resource (long-standing; widely used).
- **Sources:**
  - [CelesTrak GP data formats page, banner "ran out of 5-digit catalog numbers on 2026-07-11" (accessed 2026-10-24)](https://celestrak.org/NORAD/documentation/gp-data-formats.php)
  - [CelesTrak GP element groups](https://celestrak.org/NORAD/elements/)
  - [CelesTrak Supplemental GP data](https://celestrak.org/NORAD/elements/supplemental/)
  - [CelesTrak SOCRATES Plus (last updated 2023-04-05)](https://celestrak.org/SOCRATES/)
  - [CelesTrak SATCAT boxscore (24 Oct 2026)](https://celestrak.org/satcat/boxscore.php)

### B3. Jonathan McDowell: planet4589.org, GCAT, Jonathan's Space Report, Starlink statistics

- **What it is:** Harvard-Smithsonian astrophysicist's independent catalogues and statistics: GCAT (General Catalog of Artificial Space Objects) covering satcat, auxcat, failed-to-orbit, satcat100k (for numbers above 100000), Vimpel catalog, launch logs, reentry catalog; Starlink constellation statistics updated near-daily.
- **Problems / pain points:** Starlink stats on 24 Oct 2026: **13,042 launched, 11,170 in orbit, 11,155 working, 1,852 reentered** (181 early deorbit, 1,519 disposal complete, 152 reentry after failure), 15 "failed and decaying". Gen2 shells now include a 97° shell (1,292) and 70° shells. These numbers back the "several Starlinks reenter per day" problem (E-section).
- **Data:** GCAT TSV/text files, CC-BY 4.0 ("data from GCAT (J. McDowell, planet4589.org/space/gcat)"), Release 1.8.8 (3 Sep 2026), data updated 24 Oct 2026. Stats pages: launches per year, population by height/inclination, active satellites by owner, reentries per year, Starlink reentries per month.
- **Off-the-shelf tech:** pandas (TSV), Plotly.
- **Hackathon angle:** GCAT is the cleanest open, licensed catalogue for history/ownership joins (owner, mission, mass, status); combine with Space-Track GP for "who owns the risk" dashboards.
- **Credibility:** expert/independent but widely cited (de facto reference for journalists and ESA uses comparable sources).
- **Sources:** [GCAT (accessed 2026-10-24)](https://planet4589.org/space/gcat/); [Starlink statistics (data 24 Oct 2026)](https://planet4589.org/space/con/star/stats.html); [planet4589 statistics index](https://planet4589.org/space/stats/)

### B4. NASA Orbital Debris Program Office (ODPO): Orbital Debris Quarterly News (ODQN)

- **What it is:** NASA JSC's debris office; publishes ODQN with breakups, radar measurements (HUSIR, Goldstone) of the sub-10-cm population, models (ORDEM, LEGEND, DAS).
- **Problems / pain points (recent issue headlines):** Sept 2026 (Vol. 30, Iss. 3): "A Decade of Telescope Observations with ES-MCAT", "The NASA Battery Passivation Workshop"; July 2026 (Vol. 30, Iss. 1&2): "HUSIR and Goldstone Measurements of the Orbital Debris Environment: 2024-2025"; Sept 2025: "An Updated Explosion Rate Methodology..." and "Overview of the Cataloged Population over the Past 20 Years"; May 2025: "ISS Maneuvers Twice to Avoid Debris", "Python Scripting API for the Debris Assessment Software", "Recovered SpaceX Dragon Trunk Reentry Fragment Study"; Feb 2025: "Two New On-orbit Fragmentations", "Machine Learning Applications Supporting the ODPO". Battery passivation workshop links to the run of 2025–2026 "internal energetic" breakups (A6).
- **Data:** ODQN PDFs with monthly object counts by type and orbit; ORDEM model (export controlled for some versions); DAS (Debris Assessment Software, now with a Python API).
- **Off-the-shelf tech:** DAS Python API; ORDEM.
- **Hackathon angle:** sub-10-cm radar statistics (HUSIR/Goldstone) show the untracked population that drives "lethal non-trackable" risk; a visual that contrasts tracked vs modeled populations by altitude is a strong pitch slide.
- **Credibility:** official.
- **Sources:** [NASA ODPO ODQN index (accessed 2026-10-24)](https://orbitaldebris.jsc.nasa.gov/quarterly-news/)

---

## C. Commercial SSA and space traffic companies

### C1. LeoLabs (radar SSA, US)

- **What it is:** Commercial phased-array radar network (sites incl. Western Australia, New Zealand, Costa Rica, Texas, Alaska, Azores) tracking LEO objects; products include conjunction screening and "LeoLabs Delta" / Multi-Object Detection for breakup detection.
- **Problems / pain points:** first detector of most 2025–2026 LEO breakups (Starlink 35956, Starlink 34343, Long March 6C, Meteor 2-7); calls out "a series of debris-generating events its network has detected over the past six months". McKnight-led top-50 derelicts list (A7). Won >$50M in 2024 contracts (blog, 16 Jan 2025); MOU with ST Engineering Geo-Insights for Asia-Pacific SSA.
- **How they're trying to solve it:** radar coverage in the southern hemisphere, rapid fragmentation alerts on X, government defense contracts.
- **Data:** Commercial; public outputs are mostly social posts and blog posts. (A free LeoLabs visualization existed historically; not verified as of 2026.)
- **Hackathon angle:** scrape/collect LeoLabs' public fragmentation alerts and cross-check with when (or whether) the objects appear in the public catalogue: "detection-to-catalogue latency".
- **Credibility:** company / reputable press.
- **Sources:** [LeoLabs blog (accessed 2026-10-24)](https://leolabs.space/blog/); see A6 and A7 sources.

### C1b. SpaceX Stargaze and space-safety.com (AMOS 2026)

- **What it is:** SpaceX's own SSA system and free screening platform, described in two AMOS 2026 papers.
  - **Stargaze** (Roa Vicens et al.): star trackers on Starlink satellites detect objects; onboard star removal and tracklet linking; tracklets downlinked through the laser mesh within seconds; Kalman-filter orbit updates; new objects catalogued by initial orbit determination. **>40 million tracklets per day, ~17 million associated with known objects; routinely sees objects ~0.5 m**; next-gen tracker aims at cubesat size; can catalogue tens of new payloads within 24 h of launch; 95% of orbit updates within 5 min; P90 position error <40 m, P90 propagation error 400 m after 3 h. Free for the community to submit ephemerides for screening; CDMs auto-distributed; Starlinks act on them.
  - **space-safety.com** (Hoot, Hymes, Petrov, Ruh, Koenig): free continuous screening (vs legacy "3-6 full-catalog screenings per day"); **>500,000 ephemeris files and >50 million CDMs per day**; Starlink ephemerides hourly, Stargaze-tracked objects every 10–15 min; on-the-fly empirical accuracy and covariance-realism scoring of submitted ephemerides; "hypothetical" trajectories for maneuver planning. From 30,000 satellite-years of data, the main LEO collision risk drivers are: **the launch COLA gap, failed or unannounced maneuvers, geomagnetic storms, and ephemeris quality**.
- **Timeline:** Stargaze announced 29 Jan 2026 as a free conjunction-screening and ephemeris-sharing platform in closed beta with "more than a dozen" operators ("we hope to motivate operators to take similar steps towards ephemeris sharing and safe flight"); now also branded Space-Safety.com; participants receive CDMs, not full database access.
- **SpaceX space-safety briefing, 6 Oct 2026 (IAC Antalya, per press):** in 2026 Starlink had conjunctions with **~650 unique third-party satellites, and only about half of their operators share ephemeris**; **~164,000 conjunctions in the last six months had closest approach within four hours of an unannounced maneuver** ("not all ... high-risk", but SpaceX lacks information to reliably avoid them); Stargaze fed by **~31,000 star trackers across 11,000+ satellites**; stated daily collision probability ~5×10⁻⁵ for a 1 m satellite at Starlink altitude; examples of 57 m, 134 m and 200 m approaches. Reasons operators don't share: fear of revealing proprietary maneuver plans, or no government permission. Michael Nicolls (SVP Starlink): SpaceX has "begun to share data" with some Chinese operators, but "there are many that we do not". Press also reports a late-2025 case where a non-sharing satellite maneuvered 5 h before a predicted ~9,000 m pass, cutting it to ~60 m (search-result summary; not confirmed in the article opened). Figures come from SpaceX's own presentation; no independent verification found.
- **Dec 2025 near miss with a Chinese launch:** Nicolls posted that a satellite from the 9 Dec 2025 Kinetica-1 launch (Jiuquan; 9 payloads incl. UAE, Egyptian and Nepali student satellites) passed ~200 m from STARLINK-6079 at 560 km with no prior coordination; CAS Space replied that launch windows are screened and that the event, "If confirmed", happened "nearly 48 hours after payload separation", and called for re-establishing collaboration.
- **Problems / pain points:** a private company now runs one of the largest SSA catalogues and CDM generators; the 50M CDMs/day figure illustrates the alert-volume problem; dependence on one operator for safety-critical data (governance question); half of third-party operators are dark; unannounced maneuvers are the dominant unmanageable risk.
- **Hackathon angle:** the four risk drivers named by SpaceX are a ready problem list. Each maps to a hackathon-sized tool: COLA-gap identification of new launches (B/C), unannounced-maneuver detector (A9), storm-time uncertainty (G), ephemeris quality scorecard (A4).
- **Credibility:** conference paper abstracts (company authors).
- **Sources:** [AMOS 2026: Stargaze: SpaceX's Space Situational Awareness System](https://amostech.space/year/2026/stargaze-spacexs-space-situational-awareness-system/); [AMOS 2026: SpaceX's Conjunction Screening and Space Traffic Coordination Platform](https://amostech.space/year/2026/spacexs-conjunction-screening-and-space-traffic-coordination-platform/); [SDxCentral: SpaceX's Starlink encourages every satellite operator to share data with Stargaze (16 Oct 2026)](https://www.sdxcentral.com/news/spacexs-starlink-encourages-every-satellite-operator-to-share-data-with-stargaze-platform-for-safety/); [Starlink "Space Safety" update page (JS-rendered, content not readable on fetch)](https://starlink.com/gb/updates/space-safety); [SatNews: SpaceX identifies unshared ephemeris data as primary orbital collision hazard (8 Oct 2026)](https://satnews.com/2026/10/08/spacex-identifies-unshared-ephemeris-data-as-primary-orbital-collision-hazard-in-low-earth-orbit/); [DataCenterDynamics on the same briefing](https://www.datacenterdynamics.com/en/news/spacexs-starlink-encourages-every-satellite-operator-to-share-data-with-stargaze-platform-for-safety/) (search result; 403 on fetch); [Via Satellite: Starlink to launch free SSA platform (30 Jan 2026)](https://www.satellitetoday.com/sustainability/2026/01/30/starlink-to-launch-free-space-situational-awareness-platform/); [TechSpot: SpaceX satellite near miss with China spacecraft (Dec 2025)](https://www.techspot.com/news/110600-spacex-satellite-near-miss-china-spacecraft-highlights-growing.html) (search result); [Yahoo/Space.com: Spacecraft from Chinese launch nearly slammed into Starlink satellite](https://tech.yahoo.com/science/articles/spacecraft-chinese-launch-nearly-slammed-045934216.html) (search result); [IDN Financials: Chinese company denies SpaceX allegation](https://www.idnfinancials.com/news/59795/chinese-company-deny-spacex-allegation-of-nearly-collide-with-starlink) (search result)

### C1c. The launch "COLA gap" (Office of Space Commerce pathfinder, AMOS 2026)

- **What it is:** After a launch deploys many satellites, there are "days to weeks" when new objects cannot be reliably tracked, identified and screened. MITRE (Gruber et al.) reported OSC's eight-month **Commercial COLA Gap Pathfinder** for TraCSS: five cooperative launches at 260–550 km, 51.9–97.5°.
- **Findings:** radar + electro-optical gave catalogue-grade orbits (~1 km mean error at 24 h); with owner/operator data, commercial providers catalogued and identified objects faster than the public catalogue, closing the gap in days (hours once); **without operator data, commercial providers did not substantially shorten the gap**, and identification at rideshare scale was unreliable: "a substantial fraction of separation-state associations were incorrect" (two misidentifications fixed using non-Earth imaging).
- **Hackathon angle:** "Rideshare ID helper": for a new rideshare launch, use deployment sequence + early TLEs + operator-published info to rank object-to-satellite assignments with confidence scores; publish as a public "who is who" board for the first week after launch.
- **Credibility:** conference paper abstract (MITRE/OSC).
- **Sources:** [AMOS 2026: Results and Conclusions from the COLA Gap Pathfinder](https://amostech.space/year/2026/results-and-conclusions-from-the-cola-gap-pathfinder/)

### C1d. AMOS 2026 (Maui, Sept 2026) themes relevant to this slice

- **Best Paper:** Moriba Jah (UT Austin), "The Epistemic Support-Point Filter (ESPF): Possibilistic Space Object State Estimation Under Ignorance". Best Student Paper: Ryan Menges (CU Boulder), cislunar navigation constellation design. AMOS 2025 Best Paper: Roger Hunter (NASA), "NASA's Starling Mission and Space Situational Awareness Implication".
- **CDM/alert load:** NEC (Mori et al.): "strong correlation between the downward trend in TLE altitudes and the frequency of CDM issuance", i.e., decaying debris clouds from past breakups predict future CDM workload at lower altitudes (operators can plan staffing/compute). Iridium (Shepperd): "Operationally Practical Conjunction Metrics for Models"; AMOS 2025 poster "Iridium's Use of Mean Elements in Collision Assessment". Federated conjunction assessment reconciling multiple providers' risk numbers (Omitron/Aerospace/NASA). Tippie, Oltrogge, Vallado, Alfano: "A Critical Assessment of Space Data Message Standards".
- **Maneuver detection (many papers):** MIT (Harris & Linares) "From Detection to Classification: ... Maneuver Characterization in LEO Using TLE Data" (public TLEs only; REACT framework compares a target with the consensus of nearby passive debris; labels scarce, so unsupervised/semi-supervised); LLNL "SSAPy in the Loop: TLE-Driven Orbit Anomaly Detection with Autoencoders and Isolation Forests"; Politecnico di Milano transformer maneuver detection; Digantara adversarial maneuver prediction; KARI ontology + LLM maneuver reasoning; DSTG GEO pattern-of-life anomaly detection; Privateer "Predictive SDA through multi-source OSINT fusion and LLMs".
- **Debris/catalogue gaps:** Digantara (Balakrishnan et al.): EISCAT UHF beam-park campaigns (5, 10, 20 May 2025, 24 h total) made >1,000 detections, many at 650–950 km, and "a significant population of detections failed to correlate with any catalogued RSOs" around the CZ-6A breakup clouds, so catalogues are incomplete for small debris. NorthStar: "Turning Uncorrelated Tracks into Catalogued Objects ... Using Commercial SSA Data". Stanford: "Black-Box" for real-time satellite failure attribution.
- **Drag / reentry:** Leonid Space (Shambaugh): backtest of **878 deorbited satellites**, median one-year lifetime error 3.9 days (1.1%) with perfect knowledge vs **44.9 days (12.3%)** fully predictive; **solar flux forecasts explain 89% of variance**. GMV/CNES/DLR "Storm-proofing LEO Cataloguing": "Conventional noise-only covariances often fail to represent drag-driven error growth". MIT (Tian, Parker, Linares) drag forecasting from DSCOVR L1 solar wind (hours of warning). West Virginia Univ. density uncertainty and reduced-order models; Slingshot global density corrections from sparse trajectories. **Global Meteor Network** (Do, Brown, Vida): 1,600+ cameras, Jan 2019–July 2026, 26 reentry-like events, 20 correlated with Space-Track TLEs, sensitive to ~10 cm objects.
- **Cislunar:** LLNL one million cislunar trajectories classification; low-lunar-orbit optical cataloguing feasibility (Advanced Space); CAPSTONE photometry; cislunar breakup consequences (Padova).
- **Sources:** [AMOS 2026 conference archive (awards, sessions)](https://amostech.com/2026-amos-conference-archive/); [AMOS 2026 technical papers list](https://amostech.space/amos/2026/); [AMOS 2025 conference archive](https://amostech.com/2025-amos-conference-archive/); individual abstracts: [CDM frequency prediction (NEC)](https://amostech.space/year/2026/improving-satellite-operation-efficiency-using-conjunction-data-message-cdm-frequency-prediction/), [MIT TLE maneuver classification](https://amostech.space/year/2026/from-detection-to-classification-a-feature-driven-approach-to-satellite-maneuver-characterization-in-leo-using-tle-data/), [Digantara EISCAT CZ-6A](https://amostech.space/year/2026/independent-radar-detection-and-characterization-of-the-cz-6a-breakup-debris-cloud-in-leo-insights-from-eiscat-uhf-beam-park-campaigns/), [Leonid Space lifetime validation](https://amostech.space/year/2026/large-scale-validation-of-satellite-lifetime-predictions-using-forecasted-space-weather/), [Storm-proofing LEO cataloguing](https://amostech.space/year/2026/storm-proofing-leo-cataloguing-operational-mitigation-of-space-weather-driven-drag-uncertainty/), [MIT solar-wind drag forecasting](https://amostech.space/year/2026/lead-time-forecasting-of-drag-influenced-trajectories-using-solar-wind-data/), [Global Meteor Network reentries](https://amostech.space/year/2026/observation-and-characterization-of-satellite-and-debris-reentries-with-the-global-meteor-network/), [LLNL SSAPy anomaly detection](https://amostech.space/year/2026/ssapy-in-the-loop-two-line-element-tle-driven-orbit-anomaly-detection-with-autoencoders-and-isolation-forests/)
- **Credibility:** conference abstracts (peer-reviewed program, not journal).

### C2. Slingshot Aerospace (US)

- **What it is:** SSA data and software: 200+ sensor "Global Sensor Network", Seradata (satellite reliability/insurance database), Digital Space Twin, TALOS (AI maneuver planning), Beacon (operator coordination), new "Portal" platform; $27M Space Force contract for an AI-driven space warfare training environment; on Fast Company's 2026 most innovative list.
- **Problems / pain points:** tracked early Long March 6A debris (≥50 pieces on 7 Aug 2024).
- **Data:** commercial; claims 50,000+ spacecraft records updated daily; free trial of Portal; developer docs public.
- **Hackathon angle:** Seradata-style "reliability" data is a niche: open reconstruction of satellite failure rates from GCAT status fields + reentry-after-failure counts.
- **Credibility:** company.
- **Sources:** [Slingshot Aerospace homepage (accessed 2026-10-24)](https://slingshot.space/); [Space.com Long March 6A (Aug 2024)](https://www.space.com/china-megaconstellation-launch-space-junk)

### C3. Kayhan Space (US)

- **What it is:** Satcat (free spaceflight intelligence exchange and directory) and Dynamics (astrodynamics/orbit simulation). Selected by the Office of Space Commerce as a data quality monitor in the "Commercial Pathfinder Project for TraCSS".
- **Problems / pain points:** automating conjunction response "removes delays and errors from the critical path of response to high-risk events"; claims ">95%" reduction in response time; aims to minimize unnecessary maneuvers.
- **Hackathon angle:** operator-to-operator coordination (who to call, what each will do) is still email/phone-driven; a structured "maneuver intent" exchange format is a crisp problem.
- **Credibility:** company.
- **Sources:** [Kayhan Space homepage (accessed 2026-10-24)](https://www.kayhan.space/)

### C4. Privateer (Moriba Jah, Alex Fielding; Steve Wozniak co-founder)

- **What it is:** Data fusion company; **Wayfinder** free live satellite tracking; Elements platform (land, sea, air, space, cyber), GNSS interference detection, maritime tracking (Lloyd's List partnership).
- **Problems / pain points:** Moriba Jah (chief scientist) won the **2026 AMOS Best Paper award** for an "Epistemic Support-Point Filter", new thinking on uncertainty, evidence and decision-making in space object state estimation: i.e., current SSA represents uncertainty poorly (overconfident covariances).
- **Hackathon angle:** "honest uncertainty" visualizations: show the same conjunction under different uncertainty models; Wayfinder-style public tracker focused on debris rather than satellites.
- **Credibility:** company page.
- **Sources:** [Privateer homepage](https://www.privateer.com/); [Privateer news (accessed 2026-10-24)](https://www.privateer.com/news)

### C5. Digantara (India; offices Bengaluru, Singapore, Colorado Springs)

- **What it is:** "Space Intelligence, Surveillance & Data Infrastructures": hardware (PRISM, PULSE, SKYGATE), data (LOCUS, IRIS), analytics (STARS, MAP), AIRA. (Known for space-based SSA satellites; details not verified on the homepage fetch.)
- **Credibility:** company page (thin).
- **Sources:** [Digantara homepage (accessed 2026-10-24)](https://www.digantara.co.in/)

### C6. Other SSA players (brief)

- **ExoAnalytic Solutions:** exoanalytic.com now redirects (302) to anduril.com/space, suggesting ExoAnalytic is part of Anduril (acquisition details not verified). ExoAnalytic was the main tracker of the Intelsat 33e GEO debris (A6). Anduril authors appear at AMOS 2026 (tracklet fusion). [exoanalytic.com redirect, checked 2026-10-24](https://exoanalytic.com/)
- **COMSPOC:** SSASuite (commercial catalogue builder, on-prem), SEG, SOTA, ODSSA (Ansys ODTK plugin for maneuvers/closely spaced objects); **Spacebook**, a free visualization and data portal with APIs (details not loaded). [COMSPOC](https://www.comspoc.com/); [Spacebook](https://spacebook.com/)
- **Vyoma (Germany):** commissioning of the Flamingo-1 space-based SSA platform (press release 23 June 2026); contract to fly miniaturised Flamingo SSA sensors under ESA HydRON Element 3 (15 Apr 2026); products Safety, Agility, Efficiency; defence products; "manoeuvre detection and insights". [Vyoma](https://www.vyoma.space/)
- **NorthStar Earth & Space (Canada):** space-based SDA (Detect/Understand/Respond); listed on NYSE (NSTR, closing bell 9 Oct 2026 "Ushering in new financing to expand SDA services"); >CAD 40M with 3 Canadian Space Division; customers DARPA, USSF Joint Commercial Operations, Canada DND. AMOS 2026 papers on early-orbit conjunction risk and UCT-to-catalogue association. [NorthStar](https://www.northstar-data.com/)
- **Look Up Space (France):** the guessed domain lookup.space is parked for sale (checked 2026-10-24); the company likely uses another domain. Company status not verified.
- **Aldoria (France):** website certificate error on fetch; not verified.
- **Credibility:** company pages.

---

## D. Debris removal and servicing

### D1. Astroscale (Japan/UK/France/US)

- **What it is:** On-orbit servicing and debris removal company.
- **Status:** **ADRAS-J** (JAXA CRD2 Phase I) rendezvoused with a Japanese upper stage, reached a 15 m approach, flew around it (July and Nov 2024), and on 25 March 2026 "Completes Operations, Begins Deorbit". **ADRAS-J2** (removal of the stage) will launch on Isar Aerospace (selected 1 Sept 2026). **ELSA-M** (magnetic capture of prepared client satellites; customers Eutelsat, ESA, UKSA) completed Critical Design Review 16 March 2026; launch on Isar Aerospace; "Astroscale UK Strengthens Mission Readiness for World's First Active Debris Removal Mission" (30 Sept 2026). ISSA-J1 multi-orbit inspection mission (Apr 2026; "inspect 2 dead satellites in 2027"). Japan MoD gripping mechanism contract (Jan 2026); Astroscale France + Exotrail deorbit partnership (Jan 2026) and France 2030 sovereign deorbiting demo with Eutelsat (Sept 2026).
- **Problems / pain points:** ADR remains one-object-at-a-time and expensive; most derelicts were not designed for capture (no docking plates).
- **Hackathon angle:** ADR mission planner: given a ranked target list (A7), compute delta-v/time to visit multiple targets in similar planes (a travelling-salesman-in-orbit problem using RAAN drift).
- **Credibility:** company.
- **Sources:** [Astroscale news (accessed 2026-10-24)](https://www.astroscale.com/en/news); [ADRAS-J mission page](https://www.astroscale.com/en/missions/adras-j); [ELSA-M mission page](https://www.astroscale.com/en/missions/elsa-m)

### D2. ClearSpace (Switzerland/UK)

- **What it is:** ADR company. ClearSpace-1 (ESA) targets PROBA-1, €100M, launch 2028; ESA PRELUDE started Jan 2026 targeting 2027 launch; **15 Oct 2026: UK Space Agency selected ClearSpace as prime contractor for the UK national ADR mission to remove two UK-registered satellites**; ESA contract for Phoenix GEO life-extension (Sept 2026) and term sheet with Eutelsat (Oct 2026); co-led UK RPO Sandbox Stage 1 with Astroscale and D-Orbit (Aug 2025).
- **Credibility:** company.
- **Sources:** [ClearSpace homepage (accessed 2026-10-24)](https://clearspace.today/)

### D3. Starfish Space (US)

- **What it is:** Otter servicing vehicle (electric propulsion only, life extension and disposal); Otter Pup 2 RPOD demo aimed at first commercial docking in LEO (summer 2025 launch; outcome not stated on homepage).
- **Credibility:** company.
- **Sources:** [Starfish Space homepage (accessed 2026-10-24)](https://www.starfishspace.com/)

---

## E. Reentries and debris reaching the ground

### E1. Kenya "space ring", Mukuku village, 30 Dec 2024

- **What it is:** A ~2.5 m diameter, ~500 kg metallic ring fell in Mukuku Village, Makueni County. Kenya Space Agency (KSA) assessed it as a launch vehicle separation ring.
- **Problems / pain points:** attribution failure. McDowell and Langbroek pointed to a July 2008 Ariane 5 launch; Arianespace said the part is not from its launcher and the diameter does not fit; Langbroek's second candidate (2004 Atlas) was later seen still in orbit. As of January 2025, no definitive origin. Raises Liability Convention questions with no identified launching state.
- **Data:** Space-Track decay and TIP messages, GCAT reentry catalogue, launch logs; physical evidence photos.
- **Hackathon angle:** "Who dropped this?" forensic tool: given a find location, date window and rough size, back-propagate all decayed objects' last TLEs and ground tracks to rank candidates (Space-Track DECAY + GP_HISTORY).
- **Credibility:** official (KSA) via reputable press; expert analysis.
- **Sources:** [heise: origin of space debris still a mystery (Jan 2025)](https://heise.de/-10236740); [The Star (Kenya), 12 Jan 2025](https://www.the-star.co.ke/news/africa/2025-01-12-is-it-a-bomb-is-it-a-plane-crash-no-its-space-junk-landing); [Indian Defence Review](https://indiandefencereview.com/a-half-ton-metal-ring-fell-from-the-sky-in-kenya-the-countrys-space-agency-confirmed-what-many-suspected-2/); [Leonard David (KSA images)](https://www.leonarddavid.com/?p=44140)

### E2. Falcon 9 upper stage over NW Europe / debris in Poland, 19 Feb 2025

- **What it is:** Upper stage 2025-022Y (#62878) from Starlink Group 11-4 (launched 1 Feb 2025, Vandenberg) failed its deorbit burn (planned Pacific disposal ~00:45 UTC 2 Feb), stayed in orbit almost three weeks, then reentered uncontrolled ~03:43–03:45 UTC on 19 Feb 2025 over the British Isles, Netherlands, Germany and Poland. A composite overwrapped pressure vessel was found at Komorniki near Poznań; another tank later reported in Poland.
- **Note on the brief:** the Poland event was a **Falcon 9 second stage**, not a Crew Dragon trunk. Dragon trunk fragments have landed elsewhere (e.g., ODQN May 2025 "Recovered SpaceX Dragon Trunk Reentry Fragment Study"; Australia 2022, North Carolina and Saskatchewan 2024, not separately verified here).
- **Problems / pain points:** failed deorbit burns turn controlled reentries into uncontrolled ones over populated Europe; COPVs routinely survive.
- **Data:** CSpOC TIP messages (Space-Track), citizen video of the fireball, find locations.
- **Hackathon angle:** reentry-footprint visualizer that turns TIP windows (±minutes) into a ground-track corridor and population-at-risk estimate (WorldPop/GPW population grids).
- **Credibility:** expert blog (Langbroek, SatTrackCam Leiden) + official TIP.
- **Sources:** [Marco Langbroek, SatTrackCam Leiden: "The reentry of a Falcon 9 upper stage over NW Europe on 19 February [UPDATED]" (19 Feb 2025)](https://sattrackcam.blogspot.com/2025/02/); [NASA ODQN May 2025 headlines](https://orbitaldebris.jsc.nasa.gov/quarterly-news/)

### E2b. Repeated failed deorbits of Falcon 9 upper stages, and confusing reentry notices (2024–2026)

- **What it is:** Langbroek counts four failed Falcon 9 upper-stage deorbits in ~1.5 years: July 2024 (Starlink 9-3, failed relight), Sept 2024 (Crew-9 launch, failed deorbit burn), Feb 2025 (Starlink 11-4, Poland debris), and **2 Feb 2026 (Starlink 17-32)**: "the second stage experienced an off-nominal condition during preparation for the deorbit burn" (SpaceX); stage 2026-022AB (#67675) left in 110 × 241 km orbit and reentered uncontrolled ~12 h after launch. CSpOC TIP predicted 3 Feb 02:29 ± 1 h UTC; Langbroek's Tudat model 03:47 ± 1.5 h UTC.
- Other 2026 Langbroek reentry posts: observed reentry of Chinese CZ-2C upper stage 2018-054D over SE Australia (28 Feb 2026); "unusual and confusing double reentry" of a ZQ-3 upper stage (2025-282A) with two "final" reentry notices hours apart (31 Jan 2026); reentry of Starlink-1541 over the northern Netherlands (24 July 2026), watched from Texel.
- **Problems / pain points:** even official TIP windows are ±1 h (≈ ±40,000 km along track); disagreement between models; uncontrolled reentries over Europe/Australia; confusing official notices.
- **Hackathon angle:** "Fireball-to-object matcher": given a citizen video/meteor-camera fireball sighting (time, place, direction), rank candidate reentering objects from TIP + GP data; also crowdsource debris-find reporting. Off-the-shelf: Tudat (open source, TU Delft), `sgp4`, global meteor networks (GMN) data.
- **Credibility:** expert blog citing official TIP and SpaceX statements.
- **Sources:** [SatTrackCam Leiden, Feb 2026 archive ("Another failed deorbit of a Falcon 9 upper stage", 4 Feb 2026)](https://sattrackcam.blogspot.com/2026/02/); [SatTrackCam Leiden homepage, post list (accessed 2026-10-24)](https://sattrackcam.blogspot.com/)

### E2c. Other ground-impact and reentry-identification cases (2025–2026)

- **Jielong-3 upper stage, Western Australia, 18 Oct 2025:** a burning object found near Newman, WA, linked by Langbroek to Chinese Jielong-3 stage 2024-173L that reentered that day.
- **XJY-7, Canary Islands, 16 Oct 2025:** a fireball over Tenerife identified as the reentry of the Chinese satellite XJY-7, "a heavy object that never received a TIP" (no official reentry prediction published).
- **BRIK-II, 12 Nov 2025:** reentry of the Netherlands' first military cubesat, accelerated by geomagnetic storms and suspected attitude loss (link to G4).
- **Starlink-1541 over the Netherlands, 24 July 2026 ~20:26 UTC:** observed fragmenting from Texel; pre-reentry TIP window was 22:51 UTC ± 2 h, post-event TIP 20:26 ± 1 min (likely from DoD fireball detection); vapour trail of "fine aluminium and carbon particles" lingered >10 min.
- **Global Meteor Network** (AMOS 2026): 1,600+ cameras captured 26 reentry-like events (2019–2026), 20 matched to Space-Track TLEs; ~10 cm sensitivity.
- **Hackathon angle:** "Reentry citizen-science hub": ingest TIP + decay + GMN/fireball reports, auto-match sightings to objects, notify the public where to look/where debris might fall. Gaps: objects that never get a TIP (XJY-7).
- **Credibility:** expert blog (Langbroek) + conference.
- **Sources:** [SatTrackCam Leiden 2025 archive (posts of 20 Oct, 17 Oct, 14 Nov 2025)](https://sattrackcam.blogspot.com/2025/); [SatTrackCam Leiden Aug 2026 ("The reentry of Starlink-1541 over the northern Netherlands on 24 July 2026")](https://sattrackcam.blogspot.com/2026/08/); [AMOS 2026 GMN reentries](https://amostech.space/year/2026/observation-and-characterization-of-satellite-and-debris-reentries-with-the-global-meteor-network/)

### E2d. Saskatchewan: Dragon debris on a farm (Feb 2025) and Starlink reentry sightings (Sept 2025); survivability claims

- **What it is:** Debris from a SpaceX spacecraft returning in February 2025 was found on a farm northwest of Regina and collected by SpaceX staff (headlined as Dragon debris); in late Sept 2025 bright sparks over Saskatchewan were Starlink remnants reentering, with "no debris ... confirmed to have reached the ground" (Canadian Space Agency).
- **Problems / pain points:** Samantha Lawler (U. Regina): the southern Prairies lie under the densest satellite band; "anything that survives the re-entry will get to the ground"; odds for any individual are very low but "eventually, someone's going to get hurt". McDowell (Oct 2025): 1–2 Starlinks deorbit per day on average in 2025, heading to ~5/day; "Every few months there's a report of a piece of space hardware that's reentered"; "So far, we've been very lucky but it won't last." SpaceX has said ~5% of a V2 Mini's mass could survive reentry, mainly as very small silicon fragments from solar cells (search result; not opened). SpaceX publicly countered an FAA (2023) report claiming reentering Starlink debris could injure or kill people (search result; FAA PDF returned 403).
- **Data:** decay messages, GCAT, population grids; public reports of finds.
- **Hackathon angle:** "Where will it fall?" public map: daily latitude-weighted ground-risk for reentering objects (inclination bands make some regions, e.g., ~50–53° N, much more exposed), with a debris-find reporting form routed to authorities.
- **Credibility:** reputable press + expert quotes; some items from search results only.
- **Sources:** [Global News: Space junk debris falls to Earth, Saskatchewan (30 Sept 2025)](https://globalnews.ca/news/11456027/space-junk-debris-falls-to-earth-saskatchewan); [American Bazaar: up to two Starlinks reenter every day (9 Oct 2025)](https://americanbazaaronline.com/2025/10/09/starlink-satellites-falling-to-earth-daily-up-to-two-reenter-the-atmosphere-every-day-468559/); [The Globe and Mail: SpaceX staff collect cosmic junk found on farmer's field](https://www.theglobeandmail.com/canada/article-spacex-staff-collect-cosmic-junk-found-on-farmers-field-in) (search result); [Behind the Black: SpaceX retrieves its Dragon debris that fell in Canada in February](https://behindtheblack.com/?p=105883) (search result); [DevX: SpaceX warns retired Starlink satellites might leave debris](https://www.devx.com/daily-news/spacex-warns-retired-starlink-satellites-might-leave-debris/) (search result); [Yahoo: SpaceX counters FAA claims that reentering Starlink satellites could hurt or kill people](https://news.yahoo.com/spacex-counters-faa-claims-reentering-150026535.html) (search result); [Tribune (PH): Poland rained down by SpaceX debris (21 Feb 2025)](https://tribune.net.ph/amp/story/2025/02/21/poland-rained-down-by-spacex-debris) (search result; 1.5 × 1 m chunk found at a warehouse near Poznań)

### E3. Daily intact reentries and Starlink disposal volume

- **What it is:** ESA: 1,200 intact objects reentered in 2025; more than three per day. SpaceX disposed of 260 Starlinks by reentry Dec 2025–May 2026 with 349 more decommissioned awaiting disposal; McDowell counts 1,852 Starlink reentries total by 24 Oct 2026 (152 after failure).
- **Problems / pain points:** casualty risk aggregated over thousands of reentries; atmospheric deposition of aluminium (F-section); uncertainty of reentry time (drag, see G).
- **Data:** Space-Track DECAY, TIP; GCAT reentry catalogue; planet4589 "Starlink reentries per month".
- **Hackathon angle:** "Reentry weather": daily feed of what is coming down where (TIP + 60-day decay), with mass and material estimates feeding an "aluminium load" counter.
- **Credibility:** official + expert.
- **Sources:** [ESA SER 2026 PDF](https://www.sdo.esoc.esa.int/environment_report/Space_Environment_Report_latest.pdf); [Gigazine, July 2026](https://www.gigazine.net/gsc_news/en/20260706-spacex-starlink-satelite); [planet4589 Starlink stats](https://planet4589.org/space/con/star/stats.html)

### E4. Reentry prediction services

- **What it is:** ESA reentry prediction service (registration required; front-end user guide; links to DISCOSweb and the Fragmentation Database); Aerospace Corporation reentry database (403 on fetch; not verified); CSpOC TIP messages.
- **Problems / pain points:** reentry time windows remain wide until the final hours because density (drag) is uncertain; satellite-observed fireballs sometimes set final TIP time (Langbroek).
- **Sources:** [ESA reentry prediction service](https://reentry.esoc.esa.int/home); [Space-Track documentation (TIP)](https://www.space-track.org/documentation)

---

## F. Atmospheric pollution from reentries and launches

### F1. Peer-reviewed studies (chronological)

- **What it is:** A fast-growing literature on metals (aluminium, lithium, copper) and soot injected into the upper atmosphere by burning satellites and rockets.
- **Key findings:**
  - **Ryan et al. 2022, *Earth's Future*:** rocket soot is far more effective at warming the upper atmosphere than other soot sources; space tourism could undercut Montreal Protocol gains. [doi:10.1029/2021EF002612](https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2021EF002612)
  - **Murphy et al. 2023, *PNAS* (observational, NOAA aircraft):** ~10% of stratospheric sulfuric acid particles >120 nm contained aluminium and other reentry metals; planned LEO growth could make that up to half. [doi:10.1073/pnas.2313374120](https://www.pnas.org/doi/epdf/10.1073/pnas.2313374120)
  - **Ferreira et al. 2024, *GRL*:** 2022 reentries raised atmospheric aluminium 29.5% above natural levels, ~17 t of aluminium oxides; megaconstellations could produce >360 t/yr; particles may take up to 30 years to reach the ozone layer. [doi:10.1029/2024GL109280](https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2024GL109280); [Physics World summary](https://physicsworld.com/a/satellites-burning-up-in-the-atmosphere-may-deplete-earths-ozone-layer/)
  - **Maloney, Portmann, Ross, Rosenlof 2025, *JGR Atmospheres* (21 Mar 2025):** simulating 10,000 t/yr alumina (60,000+ LEO satellites by 2040, a reentry every 1–2 days) gives 20–40 Gg accumulated poleward of 30°, up to ~1.5 °C warming in the polar middle atmosphere, ~10% weaker Southern Hemisphere polar vortex; ozone effect unclear. "[This study is a] baby step". [doi:10.1029/2024JD042442](https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2024JD042442); [NOAA CSL news (28 Apr 2025)](https://csl.noaa.gov/news/2025/427_0428.html); [CIRES news](https://cires.colorado.edu/news/within-15-years-plummeting-satellites-could-release-enough-aluminum-alter-winds-temp)
  - **Revell et al. 2025, *npj Climate and Atmospheric Science* (9 June 2025):** launches only; "ambitious" 2,040 launches/yr scenario cuts global ozone ~0.29% by 2030, Antarctic spring ozone 3.9%. [nature.com/articles/s41612-025-01098-6](https://www.nature.com/articles/s41612-025-01098-6)
  - **Wing et al. 2026, *Communications Earth & Environment* (19 Feb 2026):** lidar detected a tenfold lithium enhancement at 96 km traced to a Falcon 9 upper stage reentry: described as first observational evidence of reentry pollution in the mesosphere. (Not opened; via secondary blog. Likely the 19 Feb 2025 stage of E2, unverified.) [nature.com/articles/s43247-025-03154-8](https://www.nature.com/articles/s43247-025-03154-8)
  - **Barker et al. 2026, *Earth's Future*/AGU (14 May 2026):** megaconstellation missions are ~1/10 of stratospheric ozone depletion from all space missions but ~1/2 of the climate effect (mainly soot). (Not opened; via secondary blog.) [doi:10.1029/2025EF007229](https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2025EF007229)
  - **ESA/aircraft reentry observation campaign:** scientists flew a private jet to observe two satellites burning up; aluminium oxide formation during reentry "has never been observed before". [Space.com](https://www.space.com/space-exploration/satellites/2-satellites-just-burned-up-in-earths-atmosphere-and-scientists-were-watching-from-a-private-jet-heres-why)
  - ESA SER 2026 explicitly calls for research on atmospheric pollution from reentries.
  - Spaceweather.com figure of "~5 t Starlink-derived aluminium oxide in 2026 so far" seen only in a forum repost: **unverified**.
- **Problems / pain points:** no operational inventory of how much mass, of what material, reenters where and when; modeling relies on assumed material composition; measurement campaigns are rare.
- **Data:** Space-Track DECAY + GCAT mass + DISCOS mass/material where available; reentry latitude from final TLEs; MERRA-2 / satellite aerosol data for context.
- **Hackathon angle:** **"Reentry emissions ledger"**: daily mass-and-aluminium tally of reentering satellites by latitude band, from public decay data and published spacecraft masses (Starlink V1 ~260–295 kg, V2 Mini ~800 kg), with projections under constellation growth scenarios (Starlink 42,000; Guowang; Qianfan; Kuiper). Very clear problem → solution story.
- **Credibility:** peer-reviewed (mostly modeling) + one observational; blog aggregator for the 2026 papers.
- **Sources:** as listed; aggregator: [DSHR's blog: "Chatbots vs. ozone" (May 2026)](https://blog.dshr.org/2026/05/chatbots-vs-ozone.html) (blog, used to locate 2025–2026 papers)

---

## G. Space weather

### G1. Solar Cycle 25

- **What it is:** Current 11-year cycle. NOAA/NASA panel (Dec 2019) predicted a smoothed peak of 115 ± 10 around July 2025; observed smoothed sunspot number peaked at ~161 in October 2024 (unsmoothed max 216 in Aug 2024): ~40% stronger and ~9 months earlier than forecast. Cycle expected to run to ~2030; SILSO: another maximum "remains a possibility" but unlikely higher.
- **Problems / pain points:** forecasts underpredicted activity; high activity raises drag, shortens orbital lifetimes (helps debris decay, hurts satellites in very low orbits), increases reentries (ESA cites "high levels of solar activity").
- **Data:** SILSO sunspot numbers; NOAA SWPC solar cycle progression JSON; F10.7 (Penticton).
- **Credibility:** official data via Wikipedia aggregation.
- **Sources:** [Wikipedia: Solar cycle 25 (accessed 2026-10-24)](https://en.wikipedia.org/wiki/Solar_cycle_25)

### G2. February 2022 Starlink loss (Group 4-7)

- **What it is:** 38 of 49 Starlink satellites launched 3 Feb 2022 into a low (~210 km) insertion orbit were lost after a minor-to-moderate geomagnetic storm increased drag (SpaceX said up to 50% higher than previous launches). Canonical example that even a modest storm can destroy freshly launched satellites. (Numbers from prior knowledge of SpaceX's 8 Feb 2022 update and Fang et al. 2022, *Space Weather*, doi:10.1029/2022SW003193; the paper page returned 403 and was **not opened**: treat details as unverified.)
- **Sources:** [Fang et al. 2022, Space Weather (not opened)](https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2022SW003193)

### G3. May 2024 "Gannon" G5 storm

- **What it is:** 10–13 May 2024, G5 "Extreme", Kp 9, Ap 271 (2nd highest on record), Dst minimum −412 nT (some readings −518 nT); strongest since 2003 Halloween storms.
- **Problems / pain points:**
  - **Satellites:** About half of ~10,000 LEO payloads (mostly Starlink) maneuvered: "largest satellite migration on record" (Parker & Linares 2024). One Starlink reentry accelerated ~11 days (Oliveira et al. 2025). Starlink service degraded. GOES-16 data outage ~2 h on 13 May; Gaia electrical issues.
  - **Forecasting:** Parker & Linares found the ap index magnitude and duration "poorly predicted, even a day ahead".
  - **GNSS/agriculture:** John Deere RTK GPS degraded; farms suspended planting, ~US$17,000 loss per affected farm (reports).
  - **Grids:** New Zealand Transpower declared a grid emergency and took lines out; Hydro-Québec no outages; NOAA reported grid irregularities.
- **Data:** full NORAD TLE history (drag decay → density), ap/Kp forecasts vs observations, GNSS TEC maps.
- **Hackathon angle:** "Storm replay": use TLE history to show every LEO satellite's altitude drop during May 2024, versus forecasted ap, and compute how conjunction predictions degrade during storms (link to CRASH Clock).
- **Credibility:** peer-reviewed (JSR, Frontiers) + official + press (via Wikipedia).
- **Sources:** [Parker & Linares, "Satellite Drag Analysis During the May 2024 Gannon Geomagnetic Storm", arXiv:2406.08617 (June 2024; JSR 61:5)](https://arxiv.org/abs/2406.08617); [Wikipedia: May 2024 solar storms (accessed 2026-10-24)](https://en.wikipedia.org/wiki/May_2024_solar_storms)

### G4. November 2025 storms

- **What it is:** X5.16 flare on 11 Nov 2025 from AR 4274 (strongest of 2025, 6th largest of Cycle 25), CME ~1,950 km/s, S2 radiation storm, NOAA G4 watch; X4.05 on 14 Nov (G1 listed); X1.8 (4 Nov), X1.7 (9 Nov), X1.21 (10 Nov).
- **Warnings issued (12 Nov 2025):** SWPC classified the event as G4 (severe); NOAA's G4 description: GPS "degraded or inoperable for hours"; local emergency notices warned of "widespread voltage control problems" and protective systems that "may mistakenly trip out key assets from the power grid", mainly poleward of 45° geomagnetic latitude. **Post-event confirmed impacts were not found** in this research (no SWPC event report located).
- **Satellite effect seen:** Dutch military cubesat BRIK-II reentered 12 Nov 2025, sped up by the geomagnetic storms (Langbroek, E2c).
- **Credibility:** official classification via press/local government notices; impacts unverified.
- **Sources:** [Wikipedia: Solar cycle 25 (flare table)](https://en.wikipedia.org/wiki/Solar_cycle_25); [CTIF: Severe geomagnetic storm threatened power grids and communications worldwide Nov 12, 2025](https://ctif.org/news/severe-geomagnetic-storm-threatened-power-grids-and-communications-worldwide-nov-12-2025) (search result); [Greene County MO emergency notice](https://greenecountymo.gov/files/file.php?id=45755) (search result); [SatTrackCam Leiden 2025 archive (BRIK-II)](https://sattrackcam.blogspot.com/2025/)

### G4b. GNSS, aviation and grid impacts: the economic side

- **What it is:** Space weather disrupts GNSS (ionospheric scintillation, TEC gradients), HF radio (polar flights), and power grids (geomagnetically induced currents).
- **Problems / pain points:**
  - **Precision agriculture (Gannon storm, May 2024):** John Deere RTK degraded; initial US estimate **~$500M in agricultural production losses** (Kansas State poster; the figure "has since been repeated widely", early assessment).
  - **Aviation:** Hong Kong PolyU forward-looking simulation of 2025 GNSS failures in the Greater Bay Area: flight cancellations/delays costing "tens of millions of Euros", tied to the equatorial ionization anomaly; earlier PolyU work (*Space Weather*, 2023): HF radio blackout rerouting/cancellation costs €0.21M–€2.20M per day.
  - INGV/URSI review: quantification of socioeconomic impacts "is not yet mature because of a lack of important modeling data".
  - Vendor projection (Mission Space): GNSS-disruption exposure $3.23B in 2026, $6.46B annualized by 2035 (commercial, method unverified).
  - SWPC JSON feed includes an `icao-space-weather-advisories.json` product (ICAO advisories for aviation).
- **Data:** IGS/CDDIS GNSS RINEX + TEC maps (not opened), SWPC JSON (Kp, F10.7, OVATION aurora, ICAO advisories), GFZ Kp/Hpo (CC BY 4.0, Kp since 1932, Hp30/Hp60), GOES XRS (NetCDF via NCEI).
- **Hackathon angle:** **"Is my GPS safe tomorrow?"**: a farmer/drone/aviation-facing forecast that converts Kp/solar-wind forecasts (or Surya outputs) into a regional GNSS-degradation risk map, validated on the May 2024 storm.
- **Credibility:** academic posters/papers + vendor estimate.
- **Sources:** [PolyU: Forward-looking study of solar maximum impact in 2025](https://research.polyu.edu.hk/en/publications/forward-looking-study-of-solar-maximum-impact-in-2025-effects-of-/) (search result); [PolyU: Examining economic costs (PDF)](https://ira.lib.polyu.edu.hk/bitstream/10397/110681/1/Xue_Examining_Economic_Costs.pdf) (search result); [URSI AT-AP-RASC 2024 paper](https://www.ursi.org/proceedings/procAT24/papers/0617.pdf) (search result); [CPAESS/UCAR item](https://cpaess.ucar.edu/print/pdf/node/26431) (search result, contains Kansas State poster per summary); [Location Business News: Mission Space GNSS exposure](https://locationbusinessnews.com/mission-space-highlights-rising-solar-storm-threats-to-gnss-navigation-infrastructure) (search result); [SWPC JSON directory](https://services.swpc.noaa.gov/json/); [GFZ Kp index](https://kp.gfz.de/en/); [NCEI GOES-R XRS](https://www.ncei.noaa.gov/products/goes-r-extreme-ultraviolet-xray-irradiance); [Wikipedia: May 2024 solar storms](https://en.wikipedia.org/wiki/May_2024_solar_storms)

### G5. NOAA SWPC (now spaceweather.gov), SOLAR-1 (ex-SWFO-L1), DSCOVR end

- **What it is:** NOAA's Space Weather Prediction Center; the site now redirects from swpc.noaa.gov to **spaceweather.gov**.
- **Problems / pain points:**
  - **30 June 2026: "DSCOVR data has ended and SOLAR-1 is now the primary instrument"** for real-time solar wind at L1; users must switch to the new solar wind display (operational 21 Aug 2026). SOLAR-1 = NOAA's Space Weather Follow On–L1 spacecraft (renamed after launch). Single-point-of-failure concern for L1 upstream monitoring (ACE ageing; not verified).
  - CCOR-2 coronagraph on SOLAR-1 declared operational June 2026; imagery public from 23 July 2026.
  - SWPC satellite drag page: drag "is the largest source of uncertainty in LEO orbit determination"; after big storms "NORAD must re-identify hundreds of objects"; near solar max, satellites may need orbit maintenance every 2–3 weeks (vs ~4×/yr at quiet Sun); points to WAM-IPE for real-time density.
- **Data:** SWPC JSON/text products (solar wind, Kp, GOES XRS X-ray flux, proton flux, F10.7), WAM-IPE density.
- **Hackathon angle:** "Drag alert for operators": map WAM-IPE/forecast Kp into expected along-track error growth for each Starlink/LEO shell, flagging when public TLEs will go stale.
- **Credibility:** official.
- **Sources:** [spaceweather.gov homepage (announcements, accessed 2026-10-24)](https://www.spaceweather.gov/); [SWPC Satellite Drag impacts page](https://www.spaceweather.gov/impacts/satellite-drag)

### G5b. Starlink as a thermosphere density sensor (Kyoto University, Aug 2026)

- **What it is:** Mamoru Yamamoto (Research Institute for Sustainable Humanosphere, Kyoto University), "Tomography of thermospheric density from Starlink Ephemeris: initial report", *Earth, Planets and Space* 78, 175 (2026), doi:10.1186/s40623-026-02509-5; press release 4 Aug 2026. Used **publicly available orbit data of ~1,200 Starlink satellites at ~482 km**, inferred local density from drag-induced decay, and applied CT-style tomography to build the first 2D latitude–longitude map of thermospheric density near 500 km; highly consistent with ESA Swarm along-track densities. Builds on an earlier study (with Takuya Sori) using Starlink TLEs to track density over time and altitude.
- **Problems / pain points:** density is the largest uncertainty in LEO orbit prediction (SWPC; A-section AMOS papers); dedicated density missions are few; megaconstellations are accidentally a dense sensor network.
- **How they're trying to solve it:** tomography from public ephemerides; aim for near-real-time density monitoring to support collision avoidance and orbit prediction. "This is a multidisciplinary study between space science and space engineering" (Yamamoto).
- **Data:** Starlink public ephemerides (Space-Track operator ephemerides / CelesTrak SupGP), TLEs; ESA Swarm density for validation.
- **Hackathon angle:** **"Constellation-as-sensor density nowcast"**: daily density map from public Starlink/OneWeb/Kuiper element sets (drag fitting per satellite → gridded map), compared with NRLMSIS and STORM-AI data; then use it to correct reentry and conjunction predictions. Very strong "real space data in, legendary product out" story, with a peer-reviewed proof of concept.
- **Credibility:** peer-reviewed + university press release.
- **Sources:** [Kyoto University research news: Mapping the upper atmosphere (4 Aug 2026)](https://www.kyoto-u.ac.jp/en/research-news/2026-08-04); [ScienceDaily (Aug 2026)](https://sciencedaily.com/releases/2026/08/260812015212.htm) (search result); [Science Times (10 Aug 2026)](https://www.sciencetimes.com/articles/62346/20260810/starlink-satellites-help-scientists-map-earths-elusive-thermosphere-300-miles-above-surface.htm) (search result)

### G6. Surya, NASA–IBM heliophysics foundation model (Aug 2025)

- **What it is:** 366M-parameter spatiotemporal transformer pretrained on ~9 years (~218 TB) of SDO data (8 AIA channels + 5 HMI products, 2010–2019); zero-shot solar dynamics and flare forecasting; LoRA fine-tuned for solar wind speed, active region segmentation, flare forecasting, EUV spectra. Paper arXiv:2508.14112 (Roy et al., 18 Aug 2025, CC BY 4.0); weights **Apache-2.0** on Hugging Face (`nasa-ibm-ai4science/Surya-1.0`), code at GitHub NASA-IMPACT/Surya. Downstream heads: `solar_flares_surya`, `solar_wind_surya`, `ar_segmentation_surya`, `euv_spectra_surya`. SuryaBench datasets on HF: `surya-bench-ar-segmentation`, `Surya-bench-solarwind`, `surya-bench-coronal-extrapolation`, `ar_emergence`, `euv-spectra` (updated 16 Dec 2025).
- **Hackathon angle:** chain Surya solar-wind forecasts → Kp → thermospheric density → satellite drag → "which satellites/conjunction predictions are at risk tomorrow". Connects heliophysics AI to an operator decision.
- **Credibility:** preprint + official model release.
- **Sources:** [arXiv:2508.14112](https://arxiv.org/abs/2508.14112); [Hugging Face model card](https://huggingface.co/nasa-ibm-ai4science/Surya-1.0); [nasa-ibm-ai4science HF org](https://huggingface.co/nasa-ibm-ai4science)

---

## H. Astronomy and spectrum

### H1. Satellite brightness vs IAU limits (optical)

- **What it is:** IAU CPS recommends satellites be fainter than ~7th magnitude (altitude-adjusted). Measured reality:
  - **Rayworth et al., arXiv:2610.10834 (7 Oct 2026):** uncued survey late 2024, ~25,000 tracks of 5,118 satellites to mag +9. Starlink exceeded the limit on ~1/4 of possible passes, rocket bodies ~1/5, **Guowang/Hulianwang on more than half**, OneWeb ~1/20 ("effective mitigation is feasible"). Predicts ~1 in 3 thirty-second twilight exposures at Rubin will contain a trail.
  - **Mallama et al., arXiv:2507.00107 (30 June 2025):** nearly all Starlink, BlueBird, Qianfan, Guowang and OneWeb spacecraft exceed the 7+ limit; most exceed mag 6 aesthetic reference.
  - **Amazon Leo (Kuiper):** mean mag 6.28 over 1,938 observations; 92% exceed IAU limit (Mallama, arXiv:2601.07708, Jan 2026).
  - **BlueBird (AST SpaceMobile):** mean 3.44, up to ~mag 0.5 near zenith (Cole, arXiv:2505.05820); BlueBird 6 3.85 vs Block 1 3.30, still all exceed limits (Mallama, arXiv:2608.23668, Aug 2026).
  - **Starlink Direct-to-Cell:** mean 4.62 (2024), 5.16 after brightness mitigation (2025) (arXiv:2407.03092, 2502.03651). Starlink Mini during orbit raising mag 2.68 below 357 km vs 6.46 above (arXiv:2405.12007). Daytime Starlink 3.6 mag (Huntsman, arXiv:2506.11382).
- **Policy context:** at the 2025 COPUOS Scientific and Technical Subcommittee, the IAU spoke under the dark and quiet skies / large constellations agenda item (item 15) and backed Conference Room Paper 22 of the "Group of Friends" reviewing impacts and mitigation effectiveness. Amazon's Kuiper flagged in Jan 2026 for exceeding brightness limits, with IAU and NSF NOIRLab monitoring (SatNews).
- **Problems / pain points:** no enforceable brightness limit; Chinese constellations least mitigated; uncued surveys are small and sporadic.
- **Data:** IAU CPS SatHub SCORE database (not verified), MMT-9, citizen observations; public TLEs for prediction.
- **Hackathon angle:** "Brightness compliance leaderboard": predict which satellites will be above the Rubin field tonight and their modeled magnitude (simple phase-angle model fit to published means), and rank operators by expected streak contamination.
- **Credibility:** arXiv preprints (several peer-reviewed later).
- **Sources:** [arXiv:2610.10834](https://arxiv.org/abs/2610.10834); [arXiv listing query results, accessed 2026-10-24: 2507.00107, 2601.07708, 2608.23668, 2505.05820, 2502.03651, 2407.03092, 2405.12007, 2506.11382](https://arxiv.org/abs/2507.00107); [IAU statement, COPUOS STSC 2025, agenda item 15 (PDF)](https://www.unoosa.org/documents/pdf/copuos/stsc/2025/Statements/15_IAU.pdf) (search result); [SatNews: Astronomers flag Amazon's Kuiper constellation for exceeding brightness limits (28 Jan 2026)](https://satnews.com/2026/01/28/astronomers-flag-amazons-kuiper-constellation-for-exceeding-satellite-brightness-limits) (search result); [COST LONNE: satellite constellations](https://cost-lonne.eu/light-pollution/satellite-constellations/) (search result); [NSF PAR: Mitigating satellite constellation impacts on astronomy](https://par.nsf.gov/biblio/10592067) (search result)

### H2. Vera C. Rubin Observatory / LSST satellite streaks

- **What it is:** LSST (started 2025) is the most streak-sensitive survey.
- **Findings:** Hu et al. 2022 (arXiv:2211.15908): giving up 10% of observing time to avoid ~40,000 Starlink+OneWeb satellites halves the fraction of streaked visits. Lu et al. 2024 (arXiv:2403.11118): 71.6% of trails brighter than best-case crosstalk-correctable limit. Tyson et al. 2024 (arXiv:2403.04942): debris glints affect ~1 in 5 low-sky twilight exposures. Kandula et al. 2025 (arXiv:2506.19092): lowering to 350 km cuts bright-satellite count ~40%. Snyder 2025 (arXiv:2505.06424): streak brightness roughly unchanged moving a large satellite from 550 to 350 km for LSSTCam. Rayworth 2026: ~1 in 3 twilight exposures with a trail. ZTF: 3.6% of science images had glints (Karpov 2022).
- **How they're trying to solve it:** scheduler avoidance, masking pipelines, ML trail removal (STARLINC, arXiv:2608.29145, ECCV 2026, code on GitHub starioKim/STARLINC; DECam streak measurement, arXiv:2603.10790). Rubin's LSST Science Pipelines add a STREAK mask plane in single-frame processing; in data release production CompareWarpAssembleCoadd catches most streaks, and a Hough-transform detector masks the rest, though "some streaks are not caught at this stage and can contaminate the final coadds and detection catalogs" (Rubin tech note DMTN-197). Earlier Rubin-linked warning: up to ~30% of LSST Camera images could include bright streaks if Starlink's 42,000-satellite plan proceeds (search result). Rubin worked with SpaceX on brightness. No 2026 measured fraction found. IAU CPS SatHub paper on quantifying/mitigating interference: arXiv:2408.15223 (search result).
- **Data:** public survey images (ZTF public alerts/images via IRSA, DECam via NOIRLab Astro Data Archive, Rubin Data Preview releases), TLEs for cross-match.
- **Hackathon angle:** "Streak ID": detect streaks in public survey images and identify the culprit satellite by cross-matching with TLE-predicted positions at exposure time (SatChecker API), producing per-operator contamination statistics. Off-the-shelf: astropy, `acstools.satdet`-style Hough detectors, STARLINC.
- **Credibility:** arXiv preprints.
- **Sources:** [Rubin DMTN-197 (streak masking)](https://dmtn-197.lsst.io/) (search result); [Freethink: LSST camera / streak warning](https://www.freethink.com/space/lsst-camera) (search result); [arXiv:2408.15223 SatHub](https://arxiv.org/html/2408.15223v1) (search result); [arXiv:2211.15908](https://arxiv.org/abs/2211.15908); [arXiv:2403.11118](https://arxiv.org/abs/2403.11118); [arXiv:2403.04942](https://arxiv.org/abs/2403.04942); [arXiv:2506.19092](https://arxiv.org/abs/2506.19092); [arXiv:2505.06424](https://arxiv.org/abs/2505.06424); [arXiv:2608.29145](https://arxiv.org/abs/2608.29145); [arXiv:2202.05719](https://arxiv.org/abs/2202.05719)

### H2b. Diffuse night-sky brightness from space objects, and brightness in debris models

- **What it is:** Beyond individual streaks, the sum of unresolved satellites and debris brightens the whole night sky.
  - **Kocifaj et al. 2021 (arXiv:2103.17125):** space objects may add ~20 µcd/m² zenith luminance, roughly a 10% increase over natural night-sky brightness (10% is the level astronomers use to call a site light-polluted; that interpretation is from the paper's framing, not re-checked here).
  - **Barentine et al. 2023 (arXiv:2302.00769):** "Aggregate Effects of Proliferating LEO Objects and Implications for Astronomical Data Lost in the Noise": each log-decade of debris size contributes roughly the same radiance.
  - **Singh, Braun, Kübler (ECSD 2025):** proposal to add brightness to ESA's MASTER debris model (link catalogue IDs to observatory magnitudes; estimate brightness of uncatalogued/modeled objects) and a future **Light Pollution Score (LPS)** for objects and constellations.
- **Hackathon angle:** "Light Pollution Score": compute an LPS per constellation from TLEs + published mean magnitudes (H1), and show the projected sky-brightness increase under filed constellation sizes (I3).
- **Credibility:** peer-reviewed / conference.
- **Sources:** [arXiv:2103.17125](https://arxiv.org/abs/2103.17125); [arXiv:2302.00769](https://arxiv.org/abs/2302.00769); [ECSD 2025: Adding Brightness to ESA's MASTER Model](https://conference.sdo.esoc.esa.int/proceedings/sdc9/paper/21)

### H3. IAU CPS SatChecker

- **What it is:** IAU CPS SatHub API: satellite position prediction for a time/location, satellites crossing a sky region (field-of-view check), metadata and TLE history; TLEs from Space-Track and CelesTrak; planned brightness estimates, pass alerts, covariance-based uncertainties. Open source (GitHub iausathub/satchecker; README says CC BY 4.0, sidebar BSD-3).
- **Hackathon angle:** ready-made backend for any astronomy-facing tool (streak attribution, observing-schedule planner).
- **Credibility:** official (IAU) open source.
- **Sources:** [GitHub iausathub/satchecker](https://github.com/iausathub/satchecker); [SatChecker docs](https://satchecker.readthedocs.io/en/latest/) (not opened); [satchecker.cps.iau.org](https://satchecker.cps.iau.org/) (403 on fetch)

### H4. Radio: unintended electromagnetic radiation (UEMR) from Starlink and others

- **What it is:** Satellites leak broadband radio noise from onboard electronics outside licensed bands.
  - **Di Vruno et al. 2023 (arXiv:2307.02316):** LOFAR observed 68 Starlink satellites and detected emission from 47 at 110–188 MHz; broadband 0.1–10 Jy, narrowband 10–500 Jy at 125, 135, 150 and 175 MHz (143.05 MHz = reflections of the French GRAVES radar); field strength up to 49 dB(µV/m) at 10 m. Limits for intended emissions "do not apply" to unintended radiation.
  - **Bassa et al. 2024 (arXiv:2409.11767):** Gen2 V2-Mini and V2-Mini DTC emit broadband UEMR at 40–70 and 110–188 MHz; 15–1,300 Jy at 56–66 MHz; "up to a factor of 32 stronger compared to the first generation"; field strengths exceed commercial EMC standards and ITU-R thresholds protecting the 150.05–153 MHz radio astronomy band.
  - **Dong et al. 2026 (arXiv:2605.17150):** EDA2 (SKA-Low prototype) at 72–234 MHz: DTC satellites ~1.45× flux of Ku-only satellites, with reversed solar-illumination dependence.
  - **Yang et al. 2026 (arXiv:2603.07631):** 21 Centimeter Array (China): no detectable broadband Starlink UEMR; detected ORBCOMM downlinks; impulsive bursts were local power-line arcing.
  - **Policy:** 23 Jan 2026 meeting at Paris Observatory of observatories/administrations from DE, FR, IT, NL, SE plus CRAF and SKAO on UEMR regulatory paths (ASTRON, 5 Feb 2026).
- **Problems / pain points:** no ITU regulation covers unintended emissions from satellites; SKA-Low (Australia) and LOFAR2.0 at risk.
- **Data:** LOFAR LTA (public after proprietary period), MWA/EDA2 data; TLEs for identification.
- **Hackathon angle:** "RFI attribution": given a radio dynamic spectrum with transient signals and timestamps, identify passing satellites from TLEs (same pipeline as H2, different wavelength).
- **Credibility:** peer-reviewed / preprint; official (ASTRON).
- **Sources:** [arXiv:2409.11767](https://arxiv.org/abs/2409.11767); [arXiv:2307.02316](https://arxiv.org/abs/2307.02316); [arXiv:2605.17150](https://arxiv.org/abs/2605.17150); [arXiv:2603.07631](https://arxiv.org/abs/2603.07631); [ASTRON: European observatories and administrations in dialogue on satellite interference (5 Feb 2026)](https://www.astron.nl/european-observatories-and-administrations-in-dialogue-on-satellite-interference/)

---

## I. Policy, regulation and coordination

### I1. FCC 5-year deorbit rule (FCC 22-74, Second Report and Order, IB Dockets 22-271 and 18-313)

- **What it is:** Adopted 29 Sept 2022, released 30 Sept 2022. Requires space stations "ending their mission in, or passing through, the LEO region below 2000 km altitude and planning disposal through uncontrolled atmospheric re-entry to complete disposal as soon as practicable following end of mission, and no later than five years after the end of the mission." End of mission = when the spacecraft can no longer perform collision avoidance (or, for non-maneuverable craft, completes its primary mission). Applies to US-licensed and US-market-access foreign satellites, small sats (25.122), Part 5 experimental and Part 97 amateur.
- **Transition:** satellites already in orbit exempt; already-authorized satellites launched after **29 Sept 2024** must comply (two-year grandfathering), waivers possible.
- **Problems / pain points:** "we believe it is no longer sustainable to leave satellites in LEO to deorbit over decades"; many commenters said "five years may still be too long for large constellations". FCC mainly checks filings ex ante; there is no public, systematic ex-post verification that satellites actually deorbit within 5 years (ESA estimates only 5–35% of non-naturally-compliant payloads achieve 5-year compliance, A1).
- **Related 2026 FCC actions:** FCC approved 7,500 more Starlink Gen2 satellites (DA-26-36, Jan 2026; total ~19,000 approved; half operational by 1 Dec 2028, rest by 1 Dec 2031; deferred ~15,000 incl. those above 600 km). FCC has proposed exempting satellites from NEPA review as "extraterrestrial activities" (not yet approved per Gigazine, July 2026; unverified).
- **Data:** FCC IBFS/ICFS filings (ODARs, semiannual reports) + GP history.
- **Hackathon angle:** **"Deorbit compliance auditor"**: for every LEO payload that stopped maneuvering (detected from TLE history), start a 5-year clock and forecast reentry date with a drag model; flag likely violators and show per-operator compliance scores. Exactly the gap between rule and enforcement.
- **Credibility:** official.
- **Sources:** [FCC 22-74 Second Report and Order (PDF, adopted 29 Sept 2022)](https://docs.fcc.gov/public/attachments/FCC-22-74A1.pdf); [IEEE ComSoc tech blog on DA-26-36 and China ITU filings (13 Jan 2026)](https://techblog.comsoc.org/2026/01/13/china-itu-filing-to-put-200k-satellites-in-orbit-fcc-authorizes-7-5k-additional-starlink-leo-satellites/); [Gigazine (July 2026)](https://www.gigazine.net/gsc_news/en/20260706-spacex-starlink-satelite)

### I2. EU Space Act (proposed 25 June 2025; under negotiation)

- **What it is:** Commission proposal for an EU regulation on safety, resilience and sustainability of space activities; applies to EU and non-EU operators providing space services in Europe; requirements scaled to size and risk.
- **Debris/traffic provisions (per King & Spalding analysis, 1 July 2025):** mandatory tracking; **subscription to collision avoidance services**; spacecraft "must be trackable and capable of performing collision avoidance maneuvers", special obligations for large constellations; a "right of way" approach between maneuverable spacecraft and standardized procedures for high-interest event alerts; debris mitigation covering "both physical structures and light and radio pollution"; safe end-of-life disposal; lifecycle **environmental footprint** declaration with a common LCA methodology and EUSPA Environmental Footprint Database. Would apply from **1 Jan 2030** (two-year transition; assets launched before 2030 generally exempt).
- **Status:** public consultation 15 July–7 Nov 2025; Cypriot Council Presidency compromise text 30 March 2026 plus Council Legal Service opinion; compromise reportedly replaces "a largely declaratory provision on 'orbital traffic rules' with an operational priority regime for collision avoidance" (Arts. 59–74); EP ITRE rapporteur Elena Donazzan (ECR, IT), shadow Giorgio Gori; US Commerce/State reviewing (US comments submitted 4 Nov 2025). ITRE vote outcome not found.
- **Hackathon angle:** "EU Space Act readiness checker": for a given operator/constellation, use public data to estimate trackability, maneuverability evidence (maneuvers detected in TLEs), brightness, and disposal behaviour against the Act's requirements. Also: an open LCA calculator for a mission's environmental footprint (launch emissions + reentry alumina).
- **Credibility:** official (EC, OSC) + law-firm analysis + niche press.
- **Sources:** [European Commission: EU Space Act](https://defence-industry-space.ec.europa.eu/eu-space-act_en); [King & Spalding: EU Space Act, what in-house counsel need to know (1 July 2025)](https://www.kslaw.com/news-and-insights/eu-space-act-what-in-house-counsel-need-to-know-about-the-potential-regulatory-framework-for-space-activities-in-europe); [Office of Space Commerce: EU Space Act Update (3 Apr 2026)](https://space.commerce.gov/eu-space-act-update-april-2026/); [EP Legislative Observatory document summary](https://oeil.europarl.europa.eu/oeil/en/document-summary?id=1824746) (search result, not opened); [EU Perspectives: harmonization and the Space Act (Nov 2025)](https://euperspectives.eu/2025/11/harmonization-space-act/) (search result, not opened); [Space Intel Report on Commission reassuring industry](https://www.spaceintelreport.com/eu-commission-preparing-law-on-space-safety-sustainability-seeks-to-reassure-private-sector-on-scope-and-cost/) (search result, not opened)

### I3. ITU filings and "paper satellites"

- **What it is:** Operators file NGSO systems with the ITU (via national administrations) to secure spectrum/orbit priority; deployment milestones apply.
- **Problems / pain points:** In the final week of 2025, Chinese entities filed for **~200,000 satellites**, mostly two NGSO systems **CTC-1 and CTC-2** (~193,000 combined, ~96,714–97,000 each) by the Radio Spectrum Development and Technology Innovation Institute (RSDTII); also China Mobile (2,664 in two constellations), Shanghai Yuanxin/Qianfan (1,296 more), GalaxySpace (187), ChinaSat (24 MEO), China Telecom (12). ITU "use it or lose it": first satellite within 7 years, full rollout within 14 years (as reported). Analysts call the number a strategic claim at the conceptual stage, limited by launch capacity. Filings far beyond plausible deployment create spectrum/orbit "warehousing" and make long-term debris projections (like ESA's) highly uncertain. (Rwanda's 2021 "Cinnamon" filing of ~327,000 satellites is a known earlier example, not re-verified this session.)
- **Data:** ITU Space Explorer / SNS (Space Network Systems) database, public ITU BR IFIC circulars (partially public).
- **Hackathon angle:** "Filed vs flown" tracker: join ITU filings (counts/shells) with what is actually in orbit (GCAT/Space-Track) to expose paper constellations and feed realistic numbers into collision-risk projections.
- **Credibility:** reputable press/blog citing ITU documentation.
- **Sources:** [IEEE ComSoc tech blog (13 Jan 2026)](https://techblog.comsoc.org/2026/01/13/china-itu-filing-to-put-200k-satellites-in-orbit-fcc-authorizes-7-5k-additional-starlink-leo-satellites/); [Light Reading: China shows satellite ambitions with big ITU filing](https://www.lightreading.com/satellite/china-shows-satellite-ambitions-with-big-itu-filing) (search result); [Advanced Television: China wants 200,000 satellites (13 Jan 2026)](https://www.advanced-television.com/2026/01/13/china-wants-200000-satellites/) (search result)

### I4. Space Sustainability Rating (SSR)

- **What it is:** Voluntary non-profit rating hosted by eSpace (EPFL Space Center), developed with ESA, MIT, others. Six modules: Mission Index (with ESA), Detectability/Identification/Trackability (with MIT), Collision Avoidance Capabilities, Data Sharing, Application of Design and Operation Standards, External Services. Bronze/silver/gold/platinum badges.
- **2025 news:** OKAPI:Orbits contracted to compute SSR ratings (4 June 2025); SES O3b mPOWER rated **platinum** after analysis of 65+ parameters (4 June 2025); paper "Deploying a practical solution to space debris" (5 June 2025). No 2026 news listed.
- **Problems / pain points:** voluntary; few ratings; no public scoreboard of all operators.
- **Hackathon angle:** "Public SSR-lite": compute a transparent, data-only proxy score for every constellation from public data (maneuver frequency, ephemeris sharing via SupGP availability, disposal behaviour, brightness), a "Yelp for satellite operators".
- **Credibility:** official program page.
- **Sources:** [Space Sustainability Rating (accessed 2026-10-24)](https://spacesustainabilityrating.org/)

### I5. Cislunar and lunar traffic

- **What it is:** 30+ lunar missions planned 2024–2030 (US, China, Japan, India, private).
- **Problems / pain points:**
  - Georgia Tech (Crum, Borowitz, Gunter; *J. Spacecraft and Rockets*, March 2025): for a 50-satellite low lunar orbit fleet, operators "must perform up to four maneuvers annually for each satellite"; "There is significant uncertainty about the exact location of objects around the moon."; "The close approaches were much more common than I would have intuitively anticipated".
  - Gambarotto et al. 2026 (*Acta Astronautica*): "current sensor capabilities are insufficient for large-scale Cislunar Space Situational Awareness"; simulated 11 catastrophic cislunar collisions (NASA Standard Breakup Model, CR3BP, 29 observer orbits); L2 halo family best for debris-cloud monitoring.
  - No mature lunar/cislunar debris mitigation framework (ESA-related 2026 presentation, per search snippet).
  - AFRL Oracle cislunar monitoring satellite expected 2027 (per search snippet; not verified).
  - Langbroek tracked Artemis II with TU Delft's MISO telescope (Apr 2026): amateurs/universities can observe cislunar traffic.
- **Data:** NASA Horizons ephemerides, SPICE kernels (NAIF) for lunar orbiters (LRO, Chandrayaan-2, KPLO/Danuri, CAPSTONE), mission-published OEMs.
- **Off-the-shelf tech:** SPICE (spiceypy), Orekit, poliastro/hapsira (CR3BP), GMAT.
- **Hackathon angle:** "Lunar SOCRATES": conjunction screening among active lunar orbiters from public SPICE/Horizons ephemerides, with a 2030 traffic scenario.
- **Credibility:** peer-reviewed + university press.
- **Sources:** [Georgia Tech news (18 Jul 2025)](https://sustainability.gatech.edu/hg/news/2025/07/18/georgia-tech-study-hopes-prevent-cislunar-collisions-moon-missions-increase); [Georgia Tech SPP news](https://spp.gatech.edu/news/item/686327/with-more-moon-missions-horizon-avoiding-crowding-collisions-will-growing); [Gambarotto et al. 2026, Acta Astronautica (PoliMi repository)](https://re.public.polimi.it/handle/11311/1298592); [ESA-related presentation (indico)](https://indico.esa.int/event/644/contributions/12251/attachments/7555/14510/CSD_LZD_OHB.pdf) (search result); [SatTrackCam Leiden post list](https://sattrackcam.blogspot.com/)

### I6. Expert voices worth following (for quotes and problem framing)

- **Hugh Lewis (Univ. of Southampton):** in 2025 UK parliamentary evidence traced the problem to Kessler's 1978 warning; ~11,500 active satellites vs just under 2,000 about ten years earlier; >40,000 objects in the public catalogue and "probably more than 50,000" trackable (per search summary; committee page 403 on fetch). [UK Parliament oral evidence 15974](https://committees.parliament.uk/oralevidence/15974/html); [oral evidence 16504](https://committees.parliament.uk/oralevidence/16504/html) (search results)
- **Moriba Jah (UT Austin, Privateer):** long-time advocate of debris transparency and "space environmentalism"; 2026 AMOS Best Paper on possibilistic state estimation; AMOS 2026 papers on knowledge-graph SDA fusion and socio-technical threat assessment. A 2020 podcast description says he doubted a Kessler event is inevitable. [UT Austin profile](https://sites.utexas.edu/moriba/?p=579) (search result); [AMOS 2026 archive](https://amostech.com/2026-amos-conference-archive/)
- **Darren McKnight (LeoLabs):** Top-50 derelicts; chairs AMOS 2026 Space Debris session (A7, A10).
- **Marco Langbroek (TU Delft / SatTrackCam Leiden):** independent reentry and military-satellite analysis from public TLEs (A9, E2, E2b, E2c).
- **Jonathan McDowell (CfA):** GCAT and Starlink statistics; quotes on reentry rate and risk (B3, E2d).
- **T.S. Kelso (CelesTrak):** GP/SupGP/SOCRATES; flagged the 5-digit catalogue exhaustion (B2).
- **Samantha Lawler (U. Regina) / Aaron Boley (UBC):** CRASH Clock; reentry risk on the Prairies (A3, E2d).
- **Credibility:** mixed (official testimony, profiles, own outputs).

---

## J. Ready-made benchmark datasets in this slice

### J1. ESA Kelvins Collision Avoidance Challenge (CDM dataset)

- **What it is:** ESA Advanced Concepts Team + Space Debris Office competition (16 Oct–16 Dec 2019). Real CDMs (2015–2019) for ESA missions.
- **Problems / pain points:** "For a typical Low Earth Orbit satellite, hundreds of collision alerts are issued weekly"; after filtering, about two actionable alerts per spacecraft per week remain: the CDM-overload problem in one sentence.
- **Data:** training 162,634 CDMs / 13,154 events (~12 CDMs per event); test 24,484 CDMs / 2,167 events; 103 columns (time_to_tca, miss distance, relative position/velocity, covariances for chaser and target, orbital parameters, space weather F10/AP/F3M/SSN); target = log10 risk at TCA. Still downloadable from the Kelvins data page. Licence not stated ("Copyright © European Space Agency 2021").
- **Off-the-shelf tech:** pandas, LightGBM/XGBoost, sequence models; NASA CARA open-source Pc tools (not opened).
- **Hackathon angle:** **"Alert triage copilot"**: predict, 2+ days out, which CDM events will end up high-risk vs fizzle, and present operators with a ranked inbox plus a plain-language explanation. Real data, clear pain, measurable result.
- **Credibility:** official dataset; competition paper: Uriot et al., arXiv:2008.03069 (2020), *Astrodynamics*.
- **Sources:** [Kelvins Collision Avoidance Challenge](https://kelvins.esa.int/collision-avoidance-challenge/); [Kelvins data page](https://kelvins.esa.int/collision-avoidance-challenge/data/); [Uriot et al., arXiv:2008.03069](https://arxiv.org/abs/2008.03069)

### J2. MIT ARCLab SPLID (Satellite Pattern-of-Life Identification Dataset)

- **What it is:** Dataset and devkit for GEO pattern-of-life: classify station-keeping vs drifting modes and the nodes (maneuvers) between them; challenge on EvalAI (#2164); MIT licence for devkit; data via Dropbox; baseline notebooks.
- **Hackathon angle:** maneuver detection from element-set time series, then transfer the model to real public GEO TLE histories ("which GEO satellites moved this week, and towards whom?").
- **Credibility:** academic (MIT ARCLab).
- **Sources:** [GitHub ARCLab-MIT/splid-devkit](https://github.com/ARCLab-MIT/splid-devkit)

### J3. MIT ARCLab STORM-AI 2025 (satellite drag / thermosphere density)

- **What it is:** Challenge for "nowcasting and forecasting space weather-driven changes in atmospheric density across low earth orbit"; dataset of historical orbital elements, satellite-derived densities, IMF, plasma, indices, particles, X-ray flux (ESA, NASA Goddard, NOAA sources); Codabench submissions; MIT licence for devkit; winners Bimasakti, Millennial-IUP, Cteceliker.
- **Hackathon angle:** ready baseline for a drag forecaster to plug into conjunction-uncertainty or reentry-time products.
- **Credibility:** academic.
- **Sources:** [GitHub ARCLab-MIT/STORM-AI-devkit-2025](https://github.com/ARCLab-MIT/STORM-AI-devkit-2025)

### J4. Off-the-shelf tools (open source unless noted)

- **`sgp4` (Python, MIT):** v2.27 (3 Jul 2026); Alpha-5 support (satnum ≤339999), experimental OMM parsing (CSV/JSON/XML), vectorized `SatrecArray`. [PyPI sgp4](https://pypi.org/project/sgp4/)
- **Skyfield:** positions of stars, planets and Earth satellites (pass prediction etc. via docs). [Skyfield](https://rhodesmill.org/skyfield/)
- **hapsira (MIT):** maintained fork of poliastro (archived Oct 2023): propagation, Lambert, element conversion, plotting. [GitHub hapsira](https://github.com/pleiszenburg/hapsira)
- **Orekit (Java, Python wrapper):** full flight dynamics incl. CCSDS messages; site blocked by an anti-bot page on fetch. [orekit.org](https://www.orekit.org/)
- **NASA CARA Analysis Tools (MATLAB, NASA Open Source Agreement):** collision probability SDK, January 2026 release. [GitHub nasa/CARA_Analysis_Tools](https://github.com/nasa/CARA_Analysis_Tools)
- **pySSEM / MOCAT (MIT licence):** LEO source-sink capacity model. [GitHub ARCLab-MIT/pyssem](https://github.com/ARCLab-MIT/pyssem)
- **IAU SatChecker (API, open source):** satellite positions / FOV crossings / TLE history. [GitHub iausathub/satchecker](https://github.com/iausathub/satchecker)
- **KeepTrack (open source web 3D tracker, 37,000+ objects):** good front-end base; GitHub thkruz/keeptrack.space. [keeptrack.space](https://keeptrack.space/)
- **Tudat (TU Delft):** used by Langbroek for reentry modeling (E2b).
- **Surya (Apache-2.0)** for solar forecasting (G6); **STARLINC** for trail removal (H2).
- **Data APIs:** Space-Track (B1), CelesTrak (B2), GCAT (B3), SWPC JSON, GFZ Kp (CC BY 4.0), NCEI GOES XRS, Hugging Face SuryaBench, Kelvins CDM, SPLID, STORM-AI (J1–J3). OMNIWeb (omniweb.gsfc.nasa.gov) refused connection on 2026-10-24 (temporary or blocked; not verified). Aditya-L1 data via ISSDC PRADAN appears to need login ([PRADAN Aditya-L1](https://pradan.issdc.gov.in/al1/)).

---

## Problem bank

Format: problem → who has it → data that could address it → source.

**Orbital environment and metrics**
1. No live, public, easy-to-read measure of orbital "health" (ESA's index is yearly and jumped from ~4 to ~50) → regulators, public, operators → Space-Track/CelesTrak GP + DISCOS/GCAT → [ESA SER 2026](https://www.esa.int/Space_Safety/Space_Debris/ESA_Space_Environment_Report_2026)
2. Time-to-collision if maneuvers stop (CRASH Clock) fell from 164 days (2018) to 5.5 (2025) to 2.5 days (May 2026), and there is no live tracker of it → policymakers, insurers → Space-Track 3LE snapshots / GP history → [arXiv:2512.09643](https://arxiv.org/html/2512.09643)
3. Competing Kessler/capacity metrics that policymakers cannot compare or play with → regulators (FCC, EU, ITU) → pySSEM/MOCAT + GP → [pyssem](https://github.com/ARCLab-MIT/pyssem)
4. Long-term debris projections depend on fictional future traffic (ITU filings for ~200,000 Chinese satellites) → ESA, modelers, spectrum regulators → ITU filings vs GCAT/Space-Track → [IEEE ComSoc](https://techblog.comsoc.org/2026/01/13/china-itu-filing-to-put-200k-satellites-in-orbit-fcc-authorizes-7-5k-additional-starlink-leo-satellites/)
5. Prioritising which derelicts to remove first (88% of top 50 are rocket bodies) → ADR companies, agencies → GP + DISCOS mass + traffic density → [heise top 50](https://heise.de/-10728122); [ECSD 2025 Top 50 update](https://conference.sdo.esoc.esa.int/proceedings/sdc9/paper/4)
6. Multi-target ADR mission planning (visit several derelicts cheaply) → Astroscale, ClearSpace, UKSA → GP (RAAN drift) → [ClearSpace](https://clearspace.today/)

**Breakups and catalogue gaps**
7. Breakup detection, attribution and debris-cloud spread forecasting (≥6 events in 6 months to Oct 2026) → operators, SSA analysts → GP feed, SATCAT debut, Gabbard diagrams → [Space.com Meteor 2-7](https://www.space.com/space-exploration/satellites/a-dead-soviet-satellite-just-broke-apart-in-orbit-again-experts-say-its-part-of-a-worrying-trend)
8. Fragments detected by commercial networks but missing from the public catalogue ("asserted not catalogued"; ZQ-2E: "many fragments" seen, 7 catalogued) → ESA, NASA, operators → GP feeds, commercial alerts → [ESA SER 2026 PDF](https://www.sdo.esoc.esa.int/environment_report/Space_Environment_Report_latest.pdf); [ODQN Sept 2026](https://orbitaldebris.jsc.nasa.gov/quarterly-news/pdfs/ODQNv30i3.pdf)
9. Lethal non-trackable debris (1–10 cm) cannot be avoided; ~1.2 million objects estimated → all LEO operators → HUSIR/Goldstone statistics, MASTER/ORDEM flux, EISCAT beam-parks → [ECSD 2025 radar paper](https://conference.sdo.esoc.esa.int/proceedings/sdc9/paper/29)
10. Battery-driven explosions with no failure-mode database; inconsistent passivation → NASA, bus makers, regulators → GCAT bus/age + fragmentation history → [ODQN Sept 2026](https://orbitaldebris.jsc.nasa.gov/quarterly-news/pdfs/ODQNv30i3.pdf)
11. "Internal energetic" Starlink breakups (Dec 2025, Mar 2026) → SpaceX, neighbours at 400–560 km → GP, LeoLabs alerts → [The Register](https://www.theregister.com/2025/12/23/starlink_satellite_fails_debris/); [EarthSky](https://earthsky.org/space/starlink-satellite-breaks-up-debris-artemis-risk/)
12. GEO debris (Intelsat 33e) is faint and hard to track; GEO UCTs peak at mag 18–19 → GEO operators → optical surveys, GP → [DCD Intelsat 33e](https://www.datacenterdynamics.com/en/news/500-pieces-of-debris-from-intelsat-33e-now-being-tracked)

**Conjunctions, coordination and data quality**
13. CDM overload: hundreds of alerts per satellite per week, ~2 actionable; SpaceX generates >50M CDMs/day → operators' flight-dynamics teams → Kelvins CDM dataset, SOCRATES → [Kelvins](https://kelvins.esa.int/collision-avoidance-challenge/); [AMOS 2026 SpaceX](https://amostech.space/year/2026/spacexs-conjunction-screening-and-space-traffic-coordination-platform/)
14. SOCRATES-style 5-km screening ignores covariance and exaggerates risk; public GP errors are km-level → universities, small operators → GP vs SupGP → [CelesTrak SOCRATES](https://celestrak.org/SOCRATES/); [SupGP](https://celestrak.org/NORAD/elements/supplemental/)
15. Starlink maneuver volume (~355,000 in 12 months; threshold 3×10⁻⁷) and the opportunity cost of ultra-conservative thresholds → SpaceX, other operators → FCC semiannual reports, GP → [Space.com](https://www.space.com/space-exploration/satellites/every-spacex-starlink-satellite-has-to-dodge-a-collision-almost-weekly-and-experts-fear-the-worst)
16. Missing, late or wrong ephemerides; only ~half of ~650 third-party operators that meet Starlink share ephemeris → all operators → Space-Track operator ephemerides, SupGP, GP → [SDxCentral](https://www.sdxcentral.com/news/spacexs-starlink-encourages-every-satellite-operator-to-share-data-with-stargaze-platform-for-safety/); [Altagrove](https://www.altagrove.com/grovewire-news/spacex-148696-starlink-collision-maneuvers-in-6-months-ending-nov-30-continued-issues-with-operators-slipshod-reporting)
17. Unannounced maneuvers: ~164,000 Starlink conjunctions in 6 months had TCA within 4 h of an unannounced maneuver → SpaceX, everyone → GP history (maneuver detection), SPLID → [SDxCentral](https://www.sdxcentral.com/news/spacexs-starlink-encourages-every-satellite-operator-to-share-data-with-stargaze-platform-for-safety/)
18. Uncoordinated post-launch close approaches (Kinetica-1 payload ~200 m from STARLINK-6079, Dec 2025) → launch providers, constellation operators → launch deployment states, early TLEs → [TechSpot](https://www.techspot.com/news/110600-spacex-satellite-near-miss-china-spacecraft-highlights-growing.html)
19. Launch "COLA gap": days–weeks before new rideshare objects are tracked and correctly identified; without operator data commercial SSA does not shorten it → OSC/TraCSS, operators → early TLEs + operator data → [AMOS 2026 COLA Gap Pathfinder](https://amostech.space/year/2026/results-and-conclusions-from-the-cola-gap-pathfinder/)
20. Hostile/non-consensual RPO (KOSMOS 2612 vs ICEYE-X36) hard to detect and attribute in real time → governments, commercial SAR operators → public TLEs → [SatTrackCam Oct 2026](https://sattrackcam.blogspot.com/2026/10/)
21. Future of the free civil conjunction service (TraCSS) uncertain (FY2027 request $11M; fee-based options) → small operators, universities → public GP → [FedScoop](https://fedscoop.com/space-commerce-official-tracss-continues/)
22. Governance risk of relying on a private operator's SSA (Stargaze) for public safety data → regulators, non-US operators → open GP + independent screening → [Via Satellite](https://www.satellitetoday.com/sustainability/2026/01/30/starlink-to-launch-free-space-situational-awareness-platform/)
23. Multiple providers give different Pc for the same event; operators must reconcile → operators → CDMs from several providers → [AMOS 2026 papers list](https://amostech.space/amos/2026/)
24. Overconfident covariances (poor uncertainty realism), especially during storms → CA analysts → GP history, storm periods → [Storm-proofing LEO cataloguing](https://amostech.space/year/2026/storm-proofing-leo-cataloguing-operational-mitigation-of-space-weather-driven-drag-uncertainty/); [Privateer (ESPF award)](https://www.privateer.com/news)
25. Catalogue numbers ran out of 5 digits on 11 July 2026; TLE-based software silently misses new objects → amateurs, universities, ground stations, legacy ops → CelesTrak/Space-Track OMM → [CelesTrak](https://celestrak.org/NORAD/documentation/gp-data-formats.php)

**Compliance and policy**
26. No public ex-post check that satellites actually deorbit within 5 years (FCC rule); ESA estimates 5–35% success among non-naturally compliant payloads → FCC, ESA, EU → GP history + drag model → [FCC 22-74](https://docs.fcc.gov/public/attachments/FCC-22-74A1.pdf); [ESA SER 2026 PDF](https://www.sdo.esoc.esa.int/environment_report/Space_Environment_Report_latest.pdf)
27. Operators need to prove EU Space Act readiness (trackability, CA capability, light/radio pollution, environmental footprint) before 2030 → EU and non-EU operators → public data proxies → [King & Spalding](https://www.kslaw.com/news-and-insights/eu-space-act-what-in-house-counsel-need-to-know-about-the-potential-regulatory-framework-for-space-activities-in-europe)
28. Voluntary Space Sustainability Rating has few public ratings; no public scoreboard of operators → investors, insurers, regulators → public behaviour metrics → [SSR](https://spacesustainabilityrating.org/)
29. Cislunar traffic: positions uncertain, sensors insufficient, no debris mitigation framework → lunar mission operators, NASA/ESA → SPICE/Horizons ephemerides → [Georgia Tech](https://sustainability.gatech.edu/hg/news/2025/07/18/georgia-tech-study-hopes-prevent-cislunar-collisions-moon-missions-increase); [Gambarotto 2026](https://re.public.polimi.it/handle/11311/1298592)

**Reentries and the atmosphere**
30. Uncontrolled reentries over populated areas (Falcon 9 stages: four failed deorbits in ~1.5 years) → public, civil protection, aviation → TIP, decay, population grids → [SatTrackCam Feb 2026](https://sattrackcam.blogspot.com/2026/02/)
31. Wide reentry windows (TIP ±1–2 h), conflicting/odd notices (ZQ-3 double reentry), objects without TIPs (XJY-7) → civil protection → TIP + GP + drag model → [SatTrackCam](https://sattrackcam.blogspot.com/)
32. Attributing ground-found debris to a source (Kenya ring) → national space agencies, victims (Liability Convention) → DECAY + GP_HISTORY + launch logs → [heise](https://heise.de/-10236740)
33. Rising aggregate casualty risk from >1,200 intact reentries per year → ESA, insurers → DISCOS/GCAT mass, reentry latitudes → [ESA SER 2026 PDF](https://www.sdo.esoc.esa.int/environment_report/Space_Environment_Report_latest.pdf)
34. Lifetime/reentry predictions are poor mainly because solar flux forecasts are poor (median 1-yr error 3.9 days → 44.9 days with forecasts; 89% of variance) → operators, regulators → F10.7 forecasts + TLE decay history → [AMOS 2026 Leonid Space](https://amostech.space/year/2026/large-scale-validation-of-satellite-lifetime-predictions-using-forecasted-space-weather/)
35. No operational inventory of metal/alumina mass deposited in the upper atmosphere by reentries → atmospheric scientists, ESA → decay + mass + material → [Maloney et al. 2025 / NOAA CSL](https://csl.noaa.gov/news/2025/427_0428.html); [Ferreira et al. 2024](https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2024GL109280)
36. Reentry and fireball sightings are not systematically matched to objects → citizen scientists, GMN, agencies → TIP + GMN data → [AMOS 2026 GMN](https://amostech.space/year/2026/observation-and-characterization-of-satellite-and-debris-reentries-with-the-global-meteor-network/)

**Space weather**
37. Storm magnitude/duration poorly predicted even a day ahead (May 2024), leading to mass maneuvers and degraded catalogues → operators, 18 SDS → ap/Kp forecasts vs TLE decay history → [Parker & Linares](https://arxiv.org/abs/2406.08617)
38. Thermospheric density is the largest uncertainty in LEO orbit prediction; few dedicated sensors → operators, SWPC → Starlink ephemerides as a density sensor (Kyoto), STORM-AI → [Kyoto University](https://www.kyoto-u.ac.jp/en/research-news/2026-08-04); [SWPC drag](https://www.spaceweather.gov/impacts/satellite-drag)
39. Newly launched satellites in very low insertion orbits are vulnerable to even moderate storms (Feb 2022 loss) → launch planners → Kp forecasts + insertion altitude → [Fang et al. 2022 (not opened)](https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2022SW003193)
40. Upstream L1 solar-wind monitoring transitioned to a single new spacecraft (DSCOVR data ended June 2026; SOLAR-1 primary) → SWPC users → SWPC JSON → [spaceweather.gov](https://www.spaceweather.gov/)
41. GNSS degradation hurts precision agriculture (~$500M initial US estimate, May 2024), drones and aviation; socioeconomic impacts poorly quantified → farmers, airlines, grid operators → Kp, TEC, GNSS data → [PolyU](https://research.polyu.edu.hk/en/publications/forward-looking-study-of-solar-maximum-impact-in-2025-effects-of-/); [Wikipedia May 2024 storms](https://en.wikipedia.org/wiki/May_2024_solar_storms)
42. Turning heliophysics AI (Surya) into operator decisions (drag, GNSS) is not done yet → SWPC, operators → SDO + Surya weights + SuryaBench → [Surya model card](https://huggingface.co/nasa-ibm-ai4science/Surya-1.0)

**Astronomy and spectrum**
43. Satellites systematically brighter than the IAU ~mag 7 limit (Starlink ~1/4 passes, Guowang >1/2, Kuiper 92% of observations) with no enforcement → astronomers, IAU, regulators → TLEs + photometry → [arXiv:2610.10834](https://arxiv.org/abs/2610.10834)
44. Streaks in Rubin/LSST (~1 in 3 twilight exposures predicted); masking misses some streaks; no per-operator attribution → Rubin, survey astronomers → survey images + TLEs (SatChecker) → [arXiv:2610.10834](https://arxiv.org/abs/2610.10834); [DMTN-197](https://dmtn-197.lsst.io/)
45. Unintended radio emission (UEMR) up to 32× stronger for Starlink Gen2, unregulated by ITU → radio astronomers (LOFAR, SKA-Low) → LOFAR/EDA2 data + TLEs → [arXiv:2409.11767](https://arxiv.org/abs/2409.11767)
46. Diffuse sky brightening (~10%) from unresolved objects; no light-pollution score in debris models → astronomers, ESA → MASTER + magnitudes → [arXiv:2103.17125](https://arxiv.org/abs/2103.17125); [ECSD 2025 MASTER brightness](https://conference.sdo.esoc.esa.int/proceedings/sdc9/paper/21)

---

## Cross-slice leads

- **SpaceX/xAI/orbital compute:** SpaceX planned on-orbit data center "A1" (120 kW) and "Gigasat" factory, FCC NEPA-exemption proposal (Gigazine, July 2026) [Gigazine](https://www.gigazine.net/gsc_news/en/20260706-spacex-starlink-satelite); Michael Nicolls is described as "SVP of Starlink at SpaceX and xAI" (SDxCentral, Oct 2026) [SDxCentral](https://www.sdxcentral.com/news/spacexs-starlink-encourages-every-satellite-operator-to-share-data-with-stargaze-platform-for-safety/); DSHR blog argues orbital data centers would multiply reentry pollution and need ~9 Starship launches/day for 15 years for a million-satellite data center (Will Lockett estimate) [DSHR](https://blog.dshr.org/2026/05/chatbots-vs-ozone.html); Stargaze/space-safety.com as SpaceX's SSA business (C1b).
- **China:** ~200,000-satellite ITU filings (CTC-1/CTC-2) [IEEE ComSoc](https://techblog.comsoc.org/2026/01/13/china-itu-filing-to-put-200k-satellites-in-orbit-fcc-authorizes-7-5k-additional-starlink-leo-satellites/); Qianfan and Long March 6A/6C upper-stage breakups (A6); Honghu-2 forcing 1,143 Starlink maneuvers (A4); Guowang brightest constellation (H1); ZQ-2E and ZQ-3 stage events (A8, E2b); Kinetica-1/CAS Space near miss (C1b); Jielong-3 debris in Australia and XJY-7 reentry without TIP (E2c).
- **US agencies:** TraCSS and OSC budget (A5); FCC 5-year rule and Starlink Gen2 approvals (I1); NOAA SWPC → spaceweather.gov, DSCOVR end, SOLAR-1 (G5); NASA ODPO battery passivation (A8); NASA CARA tools (J4).
- **ESA and other agencies:** ESA SER 2026 (A1), ESA Zero Debris, ClearSpace-1/PRELUDE, ELSA-M, UKSA ADR prime ClearSpace (D), EU SST (19 member states; services CA/reentry/fragmentation) [EU SST](https://www.eusst.eu/), JAXA CRD2/ADRAS-J (D1), ISRO Aditya-L1 data on PRADAN (J4), EU Space Act (I2).
- **Datasets:** Kelvins CDM dataset, SPLID, STORM-AI (J1–J3); full TLE history (Space-Track yearly zips); GCAT CC-BY (B3); SuryaBench on HF (G6); GFZ Kp CC BY 4.0; GOES XRS NetCDF; Global Meteor Network reentry detections (E2c).
- **Models and tools:** Surya (Apache-2.0), STARLINC trail removal, pySSEM, sgp4 2.27 with Alpha-5/OMM, KeepTrack, SatChecker, Tudat (J4).
- **EO companies / EO analytics:** ICEYE-X36 targeted by KOSMOS 2612 RPO (A9); SAR operators' exposure to hostile RPO; Planet ephemerides published via CelesTrak SupGP (B2); BlackSky and Umbra staff chairing AMOS 2026 space-based assets session.
- **Space science and literature:** atmospheric chemistry of reentry (F1); SKA-Low/LOFAR UEMR (H4); Rubin/LSST (H2); heliophysics (G); "An Orbital House of Cards" (A3).

## Leads not followed (or not verified)

- **Primary FCC filings** for Starlink semiannual reports (Dec 2025, July 2026): numbers taken from press; ICFS attachment link not opened.
- **SpaceX's 6 Oct 2026 "Space Safety" page** at starlink.com is JavaScript-rendered and returned no text; figures (650 operators, half sharing, 164,000 conjunctions) taken from SDxCentral and search summaries. The "9,000 m → 60 m" late-2025 example appears only in a search summary.
- **Feb 2022 Starlink loss (38 of 49 satellites):** numbers from memory of SpaceX's update and Fang et al. 2022; paper returned 403; needs confirmation.
- **November 2025 storm actual impacts** (observed G-level, satellite/grid/GNSS effects): only pre-storm warnings found.
- **Rwanda "Cinnamon" ITU filing (~327,000 satellites):** from prior knowledge, not re-verified.
- **Wing et al. 2026 lithium lidar paper** and **Barker et al. 2026** atmospheric paper: cited via a blog; journal pages blocked (303/403).
- **FAA 2023 report** on Starlink reentry casualty risk (PDF 403) and SpaceX's rebuttal: only search snippets.
- **ESA DISCOSweb, ESA reentry service, Aerospace Corp reentry database, SatChecker site, IAU CPS site, UNOOSA/COPUOS pages, OMNIWeb:** fetch blocked or empty; contents not verified.
- **ExoAnalytic → Anduril** relationship: only a domain redirect observed.
- **Look Up Space, Aldoria, Digantara product details**: homepages unreadable or thin.
- **LeoLabs fragmentation posts on X** (primary source for most 2025–2026 breakup counts): seen only via press.
- **USA 32 (Sept 2026) and the January 2026 Russian GEO "inspector" breakup:** mentioned in Space.com summaries; details unverified.
- **A July Long March 6A breakup with 300+ fragments** mentioned by FODNews without a year.
- **European Conference on Space Debris 2025 proceedings** (124 pages of papers) only sampled; **IAC 2025/2026 debris papers** beyond McKnight not reviewed.
- **Hugh Lewis's and Moriba Jah's social posts** not reachable; UK parliamentary evidence page returned 403.
- **Rubin measured streak fraction in 2026 data:** not found.
- **EU Space Act ITRE committee vote** and final Council general approach: not found (procedure 2025/0335(COD)).
- **AFRL Oracle cislunar mission (expected 2027)** and **ESA lunar debris framework** presentation: search snippets only.
- **NASA Starling SSA results** (AMOS 2025 Best Paper; EraDrive flight results at AMOS 2026): not read.
- **PolyU aviation cost studies, Kansas State $500M agriculture estimate, Mission Space projection:** search results only.
