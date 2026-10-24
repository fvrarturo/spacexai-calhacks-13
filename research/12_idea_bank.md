# 12 · Idea bank: problems we could build on this weekend

Written on 2026-10-24 (Saturday of Cal Hacks 13.0). It draws on research files 01–11 in this folder (underscore names), which hold every source behind the claims below, and on the parallel shortlist in [08-ideas.md](08-ideas.md).

**How to read this.**
- Section 1 is what the sponsor seems to want.
- Section 2 scores the top ideas.
- Section 3 gives the top five in detail.
- Section 4 lists ten strong alternates.
- Section 5 is the long tail of ideas from the research.
- Section 6 is what not to build.

---

## 1. What the sponsor seems to want (evidence, not guesses)

- **Who they are.** "SpaceXSI" / "SpaceXAI" is SpaceX's AI division: the former xAI, plus Cursor (Anysphere, bought for $60B, closed 14 Aug 2026). The Cal Hacks presence is effectively Cursor's developer-community team under the SpaceXAI brand. Sources: [05](05_spacex_xai_and_orbital_compute.md), [11 §A](11_x_twitter_findings.md).
- **Their judging habits.** Earlier SpaceXAI events (a Grokathon, a Grok Bot build night, a 2-hour game hackathon) rewarded **polished working demos with visible Cursor and Grok use**. An xAI hackathon winner in Dec 2025 was a product-shaped X tool. Sources: [05](05_spacex_xai_and_orbital_compute.md), [11 §H3](11_x_twitter_findings.md).
- **What SpaceX leadership talks about in October 2026.** Each point below points to a real, public, data-backed problem.
  1. **Space traffic coordination.** SpaceXAI President Michael Nicolls at IAC 2026: "the biggest risk as constellations grow is not debris. It's satellite operators not sharing data with each other." The figures: about 650 maneuvering third-party satellites, only about half sharing ephemeris, and about 164,000 conjunctions within 4 h of an unannounced maneuver in six months. See [11 §D](11_x_twitter_findings.md) and [06](06_space_traffic_debris_weather_astronomy.md).
  2. **StarMind, the AI compute satellites.** Up to 1M satellites filed with the FCC, Nvidia Vera Rubin payloads, and "Scaling AI in space is a thermal problem…". Elon's Q3 2026 remarks name the "SI constraint: power & cooling". See [11 §B, §G](11_x_twitter_findings.md) and [05](05_spacex_xai_and_orbital_compute.md).
  3. **Starlink as a sensor.** Starlink is "probably one of the best sensors" of upper-atmosphere density during storms (Nicolls). Stargaze uses 30,000 star trackers. NOAA buys density data from SpaceX. See [11 §D1, §J2](11_x_twitter_findings.md) and [03](03_us_agencies_nasa_noaa_usgs.md).
  4. **The Moon.** In Feb 2026 SpaceX pushed Mars back 5–7 years to focus on the Moon, and NASA's first Moon Base element is due Dec 2026. See [05](05_spacex_xai_and_orbital_compute.md) and [10](10_space_science_planetary_and_literature.md).
  5. **Agents.** "1000x demand from AI agents" and "GrokBot fastest growth ever" (Q3 remarks). Engineers run "20+ Grok cloud agents". See [11 §A, §G](11_x_twitter_findings.md).
- **The challenge text** asks for "Real space data goes in", "enormous public datasets, decades of missions, and a literature no human can read all of". It says nothing about Earth imagery specifically, so a project about orbits, space weather or the Moon is fully in scope.
- **Eligibility:** built with Cursor, with bonus points for Grok Bot used in planning and collaboration. Every idea below has a natural Grok role, and we should keep Grok Bot planning logs and screenshots for the submission.

---

## 2. Scorecard of the top ideas

Each criterion is scored 1–5 (5 = best for us this weekend). These are judgment calls.

| # | Idea (working name) | Clear problem | Sponsor fit | Big public data | Demo by Sunday | Not already done | "Legendary" |
|---|---|---:|---:|---:|---:|---:|---:|
| 1 | **Who Moved?** Unannounced-maneuver detector and "who doesn't share" board | 5 | 5 | 5 | 4 | 4 | 5 |
| 2 | **Starlink Weather Station:** upper-atmosphere drag nowcast from public satellite orbits | 4 | 5 | 5 | 3 | 4 | 5 |
| 3 | **Is This Image Real?** Satellite-image forensics: which satellite could have taken it, and does free imagery agree? | 5 | 3 | 4 | 4 | 5 | 5 |
| 4 | **Ask the Earth, with receipts:** plain-language questions answered only from cited open products | 5 | 4 | 5 | 4 | 2 | 4 |
| 5 | **Moon Base Site Picker:** rank south-pole sites with the new NASA–IBM Lunar Foundation Model and LRO data | 4 | 4 | 4 | 3 | 4 | 4 |
| 6 | Methane letter: plume → named facility → repeat count → paste-able paragraph | 5 | 2 | 4 | 5 | 3 | 4 |
| 7 | Blackout-proof damage map for journalists (Sentinel-1) | 5 | 2 | 5 | 4 | 3 | 4 |
| 8 | AIS lie detector: radar ship detections vs broadcast positions | 5 | 2 | 5 | 3 | 2 | 4 |
| 9 | CRASH Clock live: daily orbital-health index from public catalogs | 4 | 4 | 5 | 4 | 4 | 4 |
| 10 | StarMind sizer: orbit siting and radiator calculator for compute satellites | 4 | 5 | 3 | 4 | 4 | 3 |

**Recommendation:** pick **#1** if we want the sponsor's own problem with the cleanest data story. Pick **#3** if we want the widest "wow" for non-space judges. Pick **#2** if one of us is comfortable with orbital mechanics and we want the strongest science story.

Don't combine more than two of these. A portal that does everything demos worse than one sharp tool. The parallel shortlist in [08-ideas.md](08-ideas.md) reaches the same conclusion.

---

## 3. Top five in detail

### Idea 1: "Who Moved?" Unannounced maneuvers and the operators who don't share

- **One sentence.** Half the satellites Starlink has to dodge never say where they're going. We read the public orbit catalog every day, flag every satellite that changed its orbit, and show which operators shared that move in advance and which didn't.
- **Who has the problem.**
  - SpaceX/Starlink. About 1,000 avoidance moves a day; ~207k maneuvers in six months per the FCC filing. "The biggest risk… operators not sharing data". About 164k conjunctions within 4 h of an unannounced maneuver.
  - Every other operator, plus regulators (FCC, ESA, the Office of Space Commerce).
  - Governments watching hostile close approaches. Example: KOSMOS 2612 approaching ICEYE-X36 in Oct 2026, spotted from public orbit data alone.
  - Sources: [11 §D](11_x_twitter_findings.md), [06 problem bank #16–#20](06_space_traffic_debris_weather_astronomy.md), [05 #1–#7](05_spacex_xai_and_orbital_compute.md).
- **Data (public, big).**
  - Space-Track GP_HISTORY: full TLE history since 1957, distributed as yearly bulk zips.
  - CelesTrak GP by group: Starlink, OneWeb, Kuiper, Qianfan, Guowang.
  - CelesTrak **SupGP**: operator-supplied orbits for Starlink, Kuiper, OneWeb, Planet, the Chinese space station and others. This *is* the "who shares" list.
  - McDowell's GCAT, for owners.
  - **MIT SPLID**: a labelled maneuver dataset with a devkit, for training and validation.
  - Watch the Space-Track rate limits: GP_HISTORY is "1 / lifetime" via bulk files.
  - Since 11 Jul 2026, new objects have 6-digit catalog numbers and are missing from legacy TLE files, so use the OMM/JSON formats.
  - Sources: [06 §B1–B2, J2](06_space_traffic_debris_weather_astronomy.md).
- **Off-the-shelf tech.** `sgp4` / Skyfield for propagation; a change-point detector on mean elements, or the SPLID baselines. Visuals: CesiumJS or deck.gl globe. See [09](09_models_and_tools.md).
- **Demo.**
  1. A globe of one crowded orbital shell (e.g. 500–560 km).
  2. A live list of "moved in the last 24 h" satellites, each tagged *shared in advance* (in SupGP) or *not shared*.
  3. A per-operator transparency scorecard.
  4. A Grok agent that writes a short, cautious notice for each event, e.g. "Object X raised its orbit by ~4 km at T; no operator ephemeris was published; nearest Starlink pass ≥ … km". It writes only from computed fields.
  5. Replay a known event to show it works: the Amazon Leo deployment in Feb 2026 that forced 30 Starlink maneuvers, or KOSMOS 2612.
- **Grok / Cursor fit.**
  - Grok Bot plans the pipeline. A Grok agent writes the daily brief and answers "why was this flagged?".
  - This mirrors the sponsor's own Stargaze plus space-safety platform ask ("join the platform and share your positions").
- **Risks and how to stay honest.**
  - Public TLEs are km-level accurate, so **don't compute collision probabilities** or claim "near misses".
  - Say "orbit change detected" and "not shared publicly".
  - Validate the detector on SPLID and on operator-announced maneuvers first.
  - Hugh Lewis, Jonathan McDowell and SpaceX's own team would grade this harshly if it overclaims.
- **Why it's "legendary".** It's the sponsor president's #1 problem, from three weeks ago, solved with free data. It's a public accountability tool nobody has published.

### Idea 2: "Starlink Weather Station". Drag and density nowcast from public orbits

- **One sentence.** Solar storms puff up the upper atmosphere and drag satellites off course. The ~10,000 Starlinks are the densest set of "falling sensors" ever flown, and their public orbits can map that drag every few hours.
- **Who has the problem.**
  - Every LEO operator. Feb 2022: 38 of 49 new Starlinks were lost to a storm. May 2024: "air density in orbit jumped 5x in a few hours".
  - NASA, which is offering up to **$500k per team** in the TechLeap *Orbital Clarity Challenge* for "low-cost, scalable" drag measurement.
  - NOAA, which buys commercial density data, including from SpaceX.
  - Reentry and conjunction forecasters. Lifetime prediction error grows from 3.9 to 44.9 days with real forecasts, and 89% of that comes from solar-flux forecasts (AMOS 2026).
  - Sources: [03 F-section, #58](03_us_agencies_nasa_noaa_usgs.md), [06 G5b, J3](06_space_traffic_debris_weather_astronomy.md), [11 §J2](11_x_twitter_findings.md).
- **Proof it works.** Kyoto University (Yamamoto, *Earth, Planets and Space* 78:175, 2026) made the first tomographic thermosphere density map from public orbit data of ~1,200 Starlinks at ~482 km, validated against ESA Swarm. See [06 G5b](06_space_traffic_debris_weather_astronomy.md).
- **Data.**
  - CelesTrak GP/SupGP history for Starlink, OneWeb and Kuiper.
  - NOAA SWPC Kp/Dst and F10.7, and GFZ Kp (CC BY 4.0).
  - The MIT STORM-AI dataset (orbital elements + densities + solar wind) as a ready baseline.
  - ESA Swarm densities for validation.
  - Sources: [06 J3](06_space_traffic_debris_weather_astronomy.md), [08](08_datasets_catalogue.md).
- **Demo.**
  1. "Storm replay" of May 2024 or Nov 2025: the map of drag over time vs the Kp index.
  2. A "today" panel with each satellite group's decay rate vs normal.
  3. A Grok-written operator bulletin: "expect N km extra decay for sats below 400 km over 48 h; reentry windows shift by …".
- **Risks.**
  - Physics and estimation take real time.
  - Starlink's own manoeuvres contaminate decay, so filter by quiet periods or use SupGP.
  - Fallback: decay *anomaly* maps (relative), not absolute density.
- **Why it fits.** It turns the sponsor's fleet into a public science instrument, and it lines up with a live NASA prize and a peer-reviewed proof of concept.

### Idea 3: "Is This Image Real?" Satellite-image forensics

- **One sentence.** In the 2026 Iran war and the India–Pakistan clashes, doctored, AI-generated and misdated "satellite images" spread faster than any check. Given an image and its claimed place and time, we list which satellites could physically have taken it, then compare it with free same-day imagery.
- **Who has the problem.**
  - Journalists and fact-checkers.
  - OSINT investigators, who lost commercial imagery: Planet withheld the Middle East from 4 Apr 2026 at US-government request.
  - Courts and governments. A House committee traced Airbus imagery to China's MizarVision using orbits, camera-pointing limits and daylight. The State Department sanctioned MizarVision, The Earth Eye and Chang Guang (8 May 2026).
  - The public. Google rolled back an AI image model on Google Earth after backlash (Aug 2026).
  - Sources: [01 #38–#39 and the cross-cutting section](01_eo_satellite_companies.md), [02 #78–#81](02_eo_analytics_and_industry_problems.md), [07 top-10 #1](07_china.md), [11 §C1](11_x_twitter_findings.md).
- **Data.**
  - Public TLE history for every imaging satellite. Its imaging capability comes from UCS/GCAT and company specs.
  - Sun position from the ephemeris, to check shadows.
  - Same-day Sentinel-2/Sentinel-1/Landsat scenes via STAC (Earth Search, Planetary Computer, Copernicus Data Space).
  - Optionally, a few known-fake examples from France 24 / Bellingcat debunks.
- **Demo.**
  1. Upload an image and type a place and time.
  2. The app shows (a) satellites overhead in that window that could resolve it, (b) the sun angle vs the image's shadows, and (c) the closest free scene, side by side, with a difference view.
  3. Grok writes a verdict card, "consistent / inconsistent / can't tell", with every reason linked.
- **Risks.**
  - Shadow analysis on arbitrary images is hard. Keep the user marking the shadow direction manually.
  - Don't claim AI-fake detection from pixels alone. The strength is *physical consistency* (orbits + sun + free imagery).
  - Don't build an "is a satellite overhead right now" warning for people trying to avoid being seen. That is a different and ethically worse product (see §6).
- **Why it's "legendary".** It's a clear public-interest problem from this year's news, and the image upload is an easy, compelling demo.

### Idea 4: "Ask the Earth, with receipts"

- **One sentence.** A reporter, city staffer or insurer types "what happened here in September?" and gets one page: what changed, whether there was water or fire, and the exact public products and scene IDs that say so. Every number traces to a file.
- **Who has the problem.**
  - "The ability to type questions and get answers derived from geospatial data will be the biggest unlock in the industry" (Aravind, TerraWatch).
  - Non-experts can't use NASA's >100 PB archive.
  - VLMs score only 41.7% on GEOBench-VLM and 21.6% on height and terrain questions, and "90% right is 100% wrong".
  - Sources: [11 §C1, C3](11_x_twitter_findings.md), [02 #38–#42, #82–#85](02_eo_analytics_and_industry_problems.md), [08-ideas.md A](08-ideas.md).
- **Data.**
  - OPERA DIST/DSWx (disturbance and water), NASA FIRMS (fire), Dynamic World / ESA WorldCover.
  - **AlphaEarth Satellite Embeddings**: 64 numbers per 10 m patch, used for a "did this place change this year?" check. Yohan's tomato-field example shows how strong they are.
  - Accessed via Earth Engine or Planetary Computer.
- **Demo.** A fixed checklist of products (not an open-ended agent) → JSON → Grok writes the paragraph from the JSON only → the page shows maps, dates, product IDs and "what we don't know" (clouds, revisit gaps).
- **Risks.** It turns into a generic chatbot, and Google Earth AI, Danti and terrAIntel exist. Win by being narrow (one kind of question), sourced and free.

### Idea 5: Moon Base Site Picker

- **One sentence.** NASA's first Moon Base element is due in December and SpaceX has pivoted to the Moon. We rank south-pole landing and base sites on sunlight, nearby ice, slope, Earth visibility and how navigable the terrain looks to a landing camera.
- **Who has the problem.** NASA Moon Base and the commercial lunar landers (CLPS). Three landers failed on sensing and navigation: IM-2's altimeter and lighting, ispace's laser rangefinder, and Ingenuity on featureless terrain. ShadowCam (Mar 2026) found surface ice scarcer than hoped. Sources: [10 top-10 #2–#3, problem bank #26–#31](10_space_science_planetary_and_literature.md), [05 #32, #43](05_spacex_xai_and_orbital_compute.md).
- **Data and tech.**
  - The **NASA–IBM Lunar Foundation Model** (Hugging Face `nasa-ibm-ai4science`, 1 Sep 2026), with crater, segmentation and ice-prospectivity fine-tunes.
  - LRO LOLA DEMs and the PGDA 5 m/px south-pole illumination maps.
  - Diviner and ShadowCam. Sources: [03 C2](03_us_agencies_nasa_noaa_usgs.md), [10](10_space_science_planetary_and_literature.md).
- **Demo.** An interactive south-pole map with weight sliders, a ranked site list, and a Grok-written rationale per site. A stretch goal is a "what a descent camera sees" render under real sun angles.
- **Risks.** Big rasters. Pre-cut a small region tonight.

---

## 4. Ten strong alternates (short form)

| # | Idea | Problem in one line | Data | Sources |
|---|---|---|---|---|
| 6 | **Methane letter** | About 90% of satellite methane alerts go unanswered and only about a third of plumes are tied to an operator. We turn a plume into a named facility, a repeat count and a paragraph a reporter can paste | Carbon Mapper API, EMIT L2B v3 (released 16 Oct 2026), TROPOMI, Climate TRACE | [02 #108–#111](02_eo_analytics_and_industry_problems.md), [08-ideas.md B](08-ideas.md) |
| 7 | **Blackout-proof damage map** | Commercial imagery is withheld in wars, and the free Sentinel-1 proxy over-detects (70% precision). We add a false-positive filter, a Sentinel-2 cross-check and a cited brief per site | Sentinel-1/2, building footprints, Bellingcat PWTT | [02 #102–#105](02_eo_analytics_and_industry_problems.md), [01 #37](01_eo_satellite_companies.md) |
| 8 | **AIS lie detector** | GPS jamming hit 124k vessels in Q3 2026, and ~75% of industrial fishing vessels are untracked. We match radar ship detections with AIS and produce evidence packs | Sentinel-1, Global Fishing Watch, xView3-SAR | [02 #95–#101](02_eo_analytics_and_industry_problems.md), [11 §C4](11_x_twitter_findings.md) |
| 9 | **CRASH Clock live** | The time to a likely collision if everyone stopped maneuvering fell from 164 days (2018) to 2.5 days (May 2026), but it is published rarely. We compute it daily, with "what-if" sliders | Space-Track/CelesTrak catalog | [06 A3](06_space_traffic_debris_weather_astronomy.md) |
| 10 | **StarMind sizer** | How big must radiators and solar panels be for 250 kW in orbit, which orbits give the most sun with the least drag and debris, and how many launches does it take? | Physics + public catalogs + StarMind specs (250 kW, 160 m²) | [05 #18–#23](05_spacex_xai_and_orbital_compute.md), [11 §G](11_x_twitter_findings.md) |
| 11 | **Alert triage copilot** | Operators get hundreds of collision alerts a week and about 2 matter. We rank which alerts will turn high-risk and explain why | ESA Kelvins CDM dataset (162,634 real messages) | [06 J1](06_space_traffic_debris_weather_astronomy.md) |
| 12 | **EUDR pre-checker** | EU deforestation rules apply from 30 Dec 2026, and tree-loss maps get misread as deforestation. Upload a farm plot, get an evidence pack | Hansen GFC, JRC GFC2020/TMF, Sentinel-2 | [02 #112–#114](02_eo_analytics_and_industry_problems.md) |
| 13 | **Glacial-lake / landslide-dam watch** | The Aug 2026 Nepal–Xizang disaster killed ≥1,200, and the Oct 2026 Budhi Gandaki dam was visible in imagery a day early | Sentinel-1/2, Copernicus DEM | [07 top-10 #4](07_china.md), [11 §F3](11_x_twitter_findings.md) |
| 14 | **Rubin "what to observe tonight"** | Rubin issues ~800k–7M alerts per night and <1% get a spectrum. We rank alerts for the small telescopes actually available, or run a precovery search (3I/ATLAS was in TESS data 55 days early) | Rubin/ZTF brokers, TESS, JPL Horizons | [10 #1–#6, #34](10_space_science_planetary_and_literature.md) |
| 15 | **"What we lose" mission cards** | The FY2027 request ends about 53 NASA missions and cuts Earth science about 50%. Who depends on each dataset? A dependency graph from citations and downloads | NASA CMR, ADS/SciX, DAAC metrics | [10 #40–#41](10_space_science_planetary_and_literature.md), [03 top-10 #6](03_us_agencies_nasa_noaa_usgs.md) |

---

## 5. Long tail (one line each; source file in brackets)

**Orbits and space safety**
- Dead-or-alive satellite classifier from orbit histories. McDowell counts 22 of 239 Qianfan satellites as failed, and Joe Morrison asked "what % of flying satellites are working" [07, 11].
- 5-year deorbit compliance auditor [06].
- Breakup detector and debris-cloud forecaster: Yaogan-50 02, Luch/Olymp, Starlink 35956 [06, 11].
- Public catalog error flagger: missed decays, bogus orbits [11 §D3].
- UN registry gap: SATCAT vs UNOOSA vs FCC/ITU filings, and "paper satellites" (~249k Chinese ITU filings) [07, 11].
- Rideshare "which object is which" identifier [05, 06].
- Maneuver-load forecaster as Kuiper, Chinese constellations and the 1M-satellite filing arrive [05].
- Reentry footprint and aluminium-pollution ledger [05, 06].
- "Who dropped this?" debris-find forensics [06].
- Six-digit catalog migration checker for legacy tools [06].
- Satellite-streak attribution for Rubin images [06, 10].

**Earth observation**
- Thermal anomaly classifier for strike vs routine flaring [11 §H1].
- Every-satellite-pass timeline of an event [11 §H2].
- Wildfire "last mile" card [08-ideas D].
- MODIS↔VIIRS fire record harmonisation (a NASA Space Apps 2026 challenge) [03].
- NISAR plain-language change alerts [03].
- Flood × buildings × NFIP basis-risk back-test [02].
- Crop-insurance claim triage [01].
- Is this plant or data centre running? (Landsat/ECOSTRESS thermal) [01].
- Cross-sensor "fake change" detector [01].
- Downlink and onboard triage simulator; Zhejiang Lab says "less than 10% of data used" [01, 05, 07].
- Imagery buying assistant: "is free data enough?" [02].
- Satellite-claim fact checker for viral posts [11 §H1].
- Sinking-city InSAR alerts [11 §C1].
- Pine wilt disease detector [07].
- Activity index from satellite video (VISO dataset) [07].
- Red-teaming remote-sensing VLMs [07].
- Power-line vegetation strike risk [02].
- Subsea-cable loitering detection [02].
- Carbon-offset report card [02].
- Retired-dataset "successor finder" and recall notifier [03].
- Disaster damage triage copilot for live Copernicus Emergency Management Service and International Charter activations, e.g. the Oct 2026 Valencia floods (EMSR935) and the June 2026 Venezuela earthquake [04].
- "Legal or illegal?" deforestation: intersect Brazil's DETER/PRODES alerts with the CAR property registry, plus an El Niño fire-risk overlay [04].
- Volcanic-ash "grey zone" for aviation: fuse EarthCARE, Sentinel-5P SO₂ and geostationary imagery [04].
- Sentinel-1 radio-interference detector on the public ClearSAR set, plus a global interference map for spectrum policy [04].
- Sovereignty stress test: what Europe, Canada or Africa lose if US data or instruments disappear (Sentinel-6C stalled, the Biomass blind zone, the RADARSAT gap) [04].
- "Know when you don't know" disaster maps: abstention wrappers on foundation-model flood and burn maps (EarthVision 2026 best paper) [04].
- An EO literature-plus-data agent: ESA's EVE (text-only) joined to CDSE/openEO and the JAXA Earth API's MCP, with citations [04].

**Science, the Moon, Mars and literature**
- Mars relay-gap calculator after MAVEN's loss [10].
- Mars dust-storm nowcast with MDAD labels [10].
- TESS TOI backlog triage [10].
- "Who already observed this target?" dossier [10].
- NASA lessons-learned copilot plus ESA-ADB anomaly explainer, given the ~4,000 staff who left NASA in 2025 [10].
- Euclid lens-candidate triage [10].
- Lunar archive search for small targets: lost landers, boulders [11 §J1].

---

## 6. What not to build (and why)

- **A new foundation model or a fine-tune** of Prithvi or TerraMind. It eats the weekend, and the brief rewards the problem, not the model.
- **A marketplace or "platform for everything".** Industry history is a graveyard of these ([02 #7–#14](02_eo_analytics_and_industry_problems.md)).
- **Collision probabilities from public TLEs, presented as fact.** Public element sets are off by kilometres. Experts will notice.
- **An open-ended agent that picks its own datasets.** It hallucinates; GEOBench-VLM shows 41.7% accuracy. Use a fixed product checklist and have Grok write only from fetched fields.
- **"Who is overhead right now" alerts aimed at hiding from satellites.** This is dual-use and helps people evade monitoring. Forensics after the fact (Idea 3) is the defensible version.
- **Anything that needs paid or restricted imagery** (Jilin-1, Vantor, tasking budgets) or Chinese commercial portals.

---

## 7. Next 30 minutes (suggested)

1. **Pick one of Ideas 1, 2 or 3, with 4 as the safe fallback.**
2. Open a Grok Bot planning thread and screenshot it, because bonus points are for Grok Bot in planning.
3. Pull the data first:
   - Idea 1/2: CelesTrak GP JSON for Starlink plus one other group, and the Space-Track bulk history for 2024–2026 (needs a free account; approval can take time, so register now).
   - Idea 3: an Earth Search STAC query for Sentinel-2 over one test site.
4. Build the demo page around one replayable real event before generalising.

**Accounts and keys to request now** (some need manual approval, and the hackathon Wi-Fi shares one IP, so shared demo keys are already rate-limited). From [09](09_models_and_tools.md):
- Space-Track account (Ideas 1, 2, 9, 11).
- api.nasa.gov key, NASA Earthdata login, ADS/SciX API token, Semantic Scholar and OpenAlex keys.
- Google Earth Engine project registration (AlphaEarth embeddings, Idea 4).
- Hugging Face access requests for SAM 3 and the DINOv3 satellite model. Both are gated with manual approval.
- Grok API key (the xai-sdk; OpenAI-compatible, reads images, has web/X search and code execution). Use Grok as the orchestrator and narrator, not as the pixel reader: frontier VLMs score 5–42% on remote-sensing localisation and counting benchmarks.

**Data gotchas**
- Cache CelesTrak downloads. More than 50 errors in 2 hours can get an IP firewalled.
- Use the **OMM/JSON** format, not TLE. New objects have 6-digit catalog numbers since 11 Jul 2026, and TLE files silently drop them.
- OlmoEarth's licence forbids military, surveillance and mining/oil/gas use, so don't use it for Ideas 6–8.
- Open-Meteo serves Google's WeatherNext 2 AI ensemble for free with no key. Use it if weather matters to the demo.

**Data shortcuts found by the datasets pass** ([08](08_datasets_catalogue.md)):
- **Ideas 1, 2, 9:**
  - A Hugging Face mirror of the Space-Track TLE history: about 238M rows, 12.5 GB. It lets us start before a Space-Track account is approved. Space-Track's terms restrict redistribution, so don't re-host it publicly; cite the original source.
  - A Hugging Face conjunction log with about 872k close approaches.
  - CelesTrak live counts on 24 Oct 2026: 16,792 active objects, 11,141 of them Starlink and 391 Kuiper.
  - GFZ Kp API and the NOAA SWPC JSON feeds. The real-time solar-wind feed now comes from IMAP; an old feed URL returns 404.
- **Idea 2:** NOAA buckets with WAM-IPE thermosphere density runs, for validation.
- **Idea 3, and disaster ideas:**
  - Vantor Open Data has 11 event folders from 2026, including Hurricane Simon (Mexico, Oct 2026).
  - Umbra open SAR has 81 tasks, including Nepal (Sept 2026).
  - Microsoft's 2026 earthquake damage layers.
  - A combined 2.7B building-footprint set.
- **Idea 4:**
  - The FIRMS global 24-hour CSV is open; the API needs a free key.
  - Overture Maps release 2026-10-21.0.
  - AlphaEarth embeddings for 2017–2025 are also on Source Cooperative, but stored upside-down, so open them through the provided `.vrt` files.
- **Idea 5:** NASA Lunar FM Bench (ice-prospectivity and crater tasks), LOLA DEMs and ShadowCam.
- **Idea 6:** the Carbon Mapper API (45,539 plumes) and the Climate TRACE API, both keyless.
- **Planetary defence (extra):** the JPL small-body APIs (Sentry, close approaches, Scout, fireballs) and the ESA NEOCC risk list are keyless and live.
