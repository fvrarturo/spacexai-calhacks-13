# 03. What NASA, ESA, and SpaceX are actually saying

This file is the voices pass: agency pages, a director’s old interview that still describes the split, a September 2026 debris report, an October 2026 SpaceX safety post, and the talks around it. It is not a transcript of their X accounts. That pass failed, and the failure is documented first so the quotes that did come through X are not mistaken for a full read of the firehose.

## X, and why this section is thinner than it should be

Tried on 24 October 2026:

1. The built-in X search, including a query limited to @NASA, @NASAEarth, @nasascience, @NASAClimate, @Dr_ThomasZ, and @Astro_Pam, returned: “X search is not available for this account.” The same happened for ESA handles.
2. Chrome is running on this Mac (pid 10186). Driving that logged-in window needs Computer Use permission (Accessibility and Screen Recording). The permission dialog was raised and not granted, so your X session was not opened.
3. The in-editor browser was sent to an X search for NISAR and satellite data. X redirected to a login wall (`x.com/i/jf/onboarding/web`). That browser is a separate session. It is not your account. The screenshot of the page came back blank, which matches a login interstitial that had not rendered a feed.

What is in this file from X is secondhand, and labeled that way: a 6 October 2026 post by @SawyerMerritt quoting SpaceX’s new space-safety text, a @Starlink line quoted via Digg, and Michael Nicolls’s remarks as reported by Ars Technica from the International Astronautical Congress. A direct read of NASA Earth, ESA EO, Josef Aschbacher, Jonathan McDowell, and Chinese constellation accounts is the open loop. If Computer Use gets allowed, those searches are the first thing to add.

## NASA: the new missions are public, and the user manual is still a specialist document

### NISAR, July 2026

NASA Earthdata alert, issued 21 July 2026: calibrated L-band from the NASA–ISRO SAR mission became public on 20 July 2026 for observations on or after 17 June 2026. More of the first year of science data was promised “over the coming months,” with the full record expected by the end of 2026. Discovery paths they name: Earthdata Search, ASF Vertex, ASF SearchAPI, `asf_search`.

The user guide adds the part the press release smooths over. BETA products (January and February 2026 releases) are not fully calibrated. PROVISIONAL products (July 2026 release, acquisitions from 17 June) are calibrated and only partly validated. They do not overlap in time. Using both in one change analysis can invent a change. S-band lives on ISRO’s Bhoonidhi portal, separate from the L-band NASA archive.

The science the mission was built for, from the 20 October 2026 New Space Economy survey of the same release: a 12-day repeat, roughly six-day average revisit, aimed at crustal motion before earthquakes, Antarctic grounding lines, and soil moisture around 200 m. Dual frequency, L-band and S-band, first of its kind.

The access subproblems are in the ASF guide and are the kind of thing a weekend project will hit if it tries to be a general NISAR browser:

- S3 only from AWS us-west-2.
- Credentials last one hour.
- No bucket-to-bucket copy.
- Urgent response products retained 30 days, lower-quality orbits, separate bucket.

Sources:

- <https://www.earthdata.nasa.gov/data/alerts-outages/nisar-l-band-data-now-publicly-available>
- <https://nisar-docs.asf.alaska.edu/products-overview/>
- <https://nisar-docs.asf.alaska.edu/access-overview/>
- <https://nisar-docs.asf.alaska.edu/aws-s3-access/>
- <https://newspaceeconomy.ca/2026/10/20/the-state-of-earth-observation-2026/>

### EMIT, 16 October 2026

Eight days before the hackathon, LP DAAC released EMIT Version 2 Level 2B and Level 3 products and Version 3 Level 2B methane and CO2 enhancement products. The methane and CO2 layers are explicitly for plume complexes. Historical reprocessing was expected to take about three months, so during this weekend the archive is a mix of new acquisitions and a backlog still being rewritten.

<https://www.earthdata.nasa.gov/data/alerts-outages/emit-version-2-level-2b-level-3-version-3-level-2b-data-products-released>

This is a NASA data team telling users, in the driest possible language, that the products changed and the old files are not the new files. The usability paper in [01-structural-gap.md](01-structural-gap.md) is about exactly this moment: which version do I use?

### OPERA

JPL’s Observational Products for End-Users from Remote Sensing Analysis is NASA admitting that raw HLS and raw Sentinel-1 are not end-user products. In production: surface water (DSWx) from optical and from Sentinel-1, surface disturbance (DIST) from optical, Sentinel-1 RTC and coregistered SLC, surface displacement, tropospheric delays. NISAR versions of water and displacement were on the 2026 schedule (DSWx-NI June 2026, DISP-NI September 2026). Coverage for several radar products is North America, not the whole Earth. That geographic limit matters if the demo is a story outside the U.S.

<https://www.jpl.nasa.gov/go/opera/products/>

### SWOT, PACE, Landsat continuity

The October 2026 survey says SWOT (surface water and ocean topography) and PACE (ocean color, aerosols) were being used together on the 2026 El Niño. SWOT data sits at PO.DAAC and AVISO, with a revised handbook dated 4 March 2025. The problem SWOT was launched for is still a clean one: rivers and lakes are not in the gauge network, and sea level at the coast is not one number.

The same survey flags a policy risk rather than a sensor risk. Landsat Next, the planned three-satellite superspectral replacement, went through affordability reviews in 2025 and January 2026. GeoXO, the next geostationary weather series, faced instrument and schedule questions. NASA and USGS still picked a 2025–2029 Landsat Science Team in December 2025 to protect a 54-year calibration record. The voiced problem: the free, boring, decades-long land record is the one under budget pressure, while commercial constellations are adding capacity the science record cannot replace.

- SWOT: <https://swot.jpl.nasa.gov/data/>
- Continuity discussion: <https://newspaceeconomy.ca/2026/10/20/the-state-of-earth-observation-2026/>

### FIRMS

NASA LANCE still runs the fire API the rest of the industry treats as the noisy first alert. Area and country CSV endpoints, a free map key, 5,000 transactions per 10 minutes. The OroraTech–ICEYE announcement on 22 October 2026 is the commercial reply to FIRMS: fast hotspots are not a damage assessment, and they are not a forecast of what the fire will hit.

- <https://firms.modaps.eosdis.nasa.gov/api>
- <https://www.iceye.com/newsroom/press-releases/iceye-partners-with-ororatech-to-deliver-full-lifecycle-wildfire-intelligence>

### The scientist paper, not a tweet

The 2026 “ten rules” paper is the closest thing in this pass to NASA-adjacent people describing their own pain in public. It is written by the ICESat-2 user community and the National Snow and Ice Data Center people who support them. The complaints are concrete: HDF5, workshops lost to login screens, hubs that vanish when the event ends, tutorials nobody maintains, cloud bills. Rules and links are in [01-structural-gap.md](01-structural-gap.md). <https://link.springer.com/article/10.1007/s12145-026-02216-5>

### What this pass did not find from NASA people

No verified 2026 thread from a named NASA Earth scientist on X, because the account search failed. No claim is made here about what Karen St. Germain, the Earth Science Division, or the current NASA leadership posted this month. Do not treat silence in this file as silence from them.

## ESA: the archive is a public utility, the orbit is not healthy, the forest mission just opened

### Copernicus as an operations story

Aschbacher’s 2014 Sentinel-1 interview remains the clearest plain-language version of ESA’s access goal: a two-satellite radar constellation, a few days of revisit, three hours to a normal user, about ten minutes for an oil spill to the coast guard in Lisbon. CDSE in 2025 is the scaled-up version of that promise, and the annual report is proud of volume (500,000 users, 91 PB, 120 million products) and explicit that the next job is services on top of the archive, not more downloads. Sentinel-1D data opened 17 April 2026. Biomass, the P-band forest mission, opened its data on 26 January 2026 after an April 2025 launch. The first year of Biomass was a tomography campaign over Gabon, Congo, Cameroon, and Brazil, because biomass is a calibration problem before it is a map.

Sources in [01-structural-gap.md](01-structural-gap.md) and the 20 October 2026 survey.

At the Living Planet Symposium on 25 June 2025, ESA and the Commission added six commercial providers to Copernicus Contributing Missions: Marble Imaging, GEOSAT, SatVu, ORUS, Unseenlabs, Aerospacelab. Twenty-five commercial suppliers in total. The voiced need: Sentinels are the baseline, and some civil jobs need sharper, thermal, or RF data the Sentinels do not have.

### Space Environment Report 2026

Published 14 September 2026, data through the end of 2025. This is ESA’s Space Debris Office, not a commentator. The sentences they chose:

- More than 300 launches in 2025, more than 4,000 new payloads.
- About ten new payloads a day, and more than three intact objects reentering every day.
- Not enough satellites leave crowded orbits at end of life.
- Constellations are changing altitude year to year, so the map of “where the traffic is” does not sit still.
- A growing set of detected objects cannot be tied to a breakup or an owner. Better sensors, worse identification.
- New metric: casualty risk on the ground from surviving fragments. Still small next to everyday risks, and rising.
- Even with the forecast window cut from 200 years to 100, the projected object counts are much higher than in the previous report.
- The Space Environment Health Index, normalized to a 2014 “acceptable” mitigation scenario, jumped from **about 4 to about 50 in one year**. Their words: the long-term effect got an order of magnitude worse.
- Active debris removal is required. Mitigation alone does not stop a Kessler-style growth. Even with no new launches, fragmentations add debris faster than the atmosphere removes it.
- Design-for-demise (burn up completely) and atmospheric pollution from reentries are now in tension. They say the first task is to measure the pollution before writing a rule.
- ClearSpace-1 is the removal demonstration. CAT is a standard grapple interface so a future satellite can be removed. Zero Debris is the 2030 design goal. The Zero Debris Charter’s technical booklet is described as a to-do list.

The 2025 report, data through 2024, is the baseline those numbers shocked: about 40,000 tracked objects, about 11,000 active payloads, an estimated 1.2 million debris objects larger than 1 cm, and more than 50,000 larger than 10 cm. In some LEO bands the density of active objects is the same order as debris. Intact reentries already averaged more than three a day.

- 2026 report: <https://www.esa.int/Space_Safety/Space_Debris/ESA_Space_Environment_Report_2026>
- 2025 report: <https://www.esa.int/Space_Safety/Space_Debris/ESA_Space_Environment_Report_2025>

### Φ-week, the scientist version of “do not trust the model”

An older Φ-week breakout (the notes that are still the clearest public writeup of this argument) had Earth scientists warning that machine-learning papers were extrapolating far outside their training samples and publishing anyway. Hanna Meyer’s point, as recorded in the session notes: models are weak outside the training distribution, and high-impact papers ignored that. Ribana Roscher’s point: you can often explain a classification, and you should. The session treated naive AI as a reputational risk to Earth science, not as a tooling gap.

The notes are from a 2020 session that the organizers tied to Digital Twin Earth. They are old. They are also the objection a careful judge will raise if a demo says “the model knows” without a source image and a confidence.

<https://airdrive.eventsair.com/eventsairwesteuprod/production-nikal-public/095c72e6a8ab463abd95e44f6f17c86a>

SatSummit’s 2026 speaker call (St. Louis, 18–19 November) asks for practical development impact and “difficult questions,” and warns speakers off product pitches. Useful as a signal of what the EO-for-development community is tired of. It is not a problem statement by itself. <https://satsummit.io/updates/2026-08-05-stl-speaker-call/>

## SpaceX: the October 2026 safety argument, mostly in their own numbers

SpaceX is not an Earth-imagery company. In the first half of October 2026 they made orbital traffic their public message, at the same time as they described plans for up to 100,000 Starlink satellites and up to 1 million Starmind satellites for orbital compute. The interesting part for a project is the operational complaint, not the constellation size.

### The post and the page

On 6 October 2026, @SawyerMerritt posted SpaceX’s space-safety text. Digg and Les Numériques quote the same passage and date it 6 October. The underlying page is <https://starlink.com/updates/space-safety>, which did not render in a non-JavaScript fetch. The product page that did render is <https://space-safety.com>.

Quoted claims, attributed to SpaceX via those writeups:

- Plans: up to 100,000 Starlink satellites, up to 1 million Starmind AI satellites.
- In 2026, Starlink had conjunctions with about **650 unique maneuvering third-party satellites**. About **half** of them share ephemeris.
- Some operators will not share because future maneuvers are considered proprietary. Others are willing and cannot get government permission. SpaceX calls those policies counterproductive.
- Over six months, about **164,000 conjunctions** where closest approach fell within four hours after an unannounced maneuver. Not all were high risk. The stated harm is false confidence: the conjunction is invisible if you do not have the post-maneuver trajectory.
- Starlink publishes high-accuracy ephemerides, including upcoming maneuvers. The public file mirror is described at <https://starlink.com/public-files/ephemerides/README.md>: Modified ITC format, position and velocity covariance, 72-hour predictions, updated every eight hours, also on space-track.org. A Digg quote of @Starlink says the public publish is hourly. The README says every eight hours. Both can be true of different products. Do not collapse them.

<https://xitter.cf/SawyerMerritt/status/2107495655694295206>
<https://digg.com/tech/n0x6rddo>
<https://www.theregister.com/offbeat/2026/10/07/starlinks-plan-to-avoid-orbital-near-misses-ephemeris-sharing/5301650>
<https://www.lesnumeriques.com/spatial/l-espace-est-immense-elon-musk-veut-y-loger-1-million-de-satellites-ia-et-voici-son-plan-anti-collision-n262950.html>

### space-safety.com, the actual tool

Fetched directly:

- Free ephemeris sharing, screening, and prediction analysis.
- “Dozens” of operators upload ephemerides for “thousands” of satellites. Files from space-track.org formats are accepted. Upload as often as every ground contact.
- Screening results in about a minute.
- Stargaze: **30,000 optical sensors**, tracking **50% of objects below 600 km perigee**.
- Hypothetical trajectory screening for maneuver planning.
- A quality check of your ephemeris against Stargaze observations.
- Sign-up is limited to satellite operators. The door is `space-safety-onboarding@spacex.com`.

So the public can read Starlink’s ephemerides, and cannot use the screening service. That is a product gap with a shape: the data is partly public, the decision tool is closed, and the stated reason for the tool is that other people’s data is missing.

### Michael Nicolls at IAC, 6 October 2026

Ars Technica, 8 October 2026, reporting Nicolls (senior vice president of Starlink at SpaceX and xAI) in Antalya:

- Other operators maneuvered without telling anyone. Conjunctions of **tens of meters to hundreds of meters**. “Way too close to comfort.”
- No implication of an attack. The failure is unpublished ephemeris, or maneuvering without looking at anyone else’s.
- Starlink satellites do about **1,000 collision-avoidance maneuvers a day**.
- Onboard cameras (Stargaze) track about **90% of maneuvering satellites** that cross Starlink orbits. Ars’s 90% and space-safety.com’s “50% of objects below 600 km” are different denominators. One is maneuvering satellites in the relevant orbits. The other is all objects under 600 km. Both are from SpaceX-side descriptions in the same month. Keep them apart.
- If a dodge is impossible in time, the satellite “ducks,” pointing to present a smaller risk.
- Nicolls’s minimum standard: know where your satellite is, know where it is going, and make that prediction reliable.
- There is no global rule that requires an operator to broadcast location and maneuvers.

Data Center Dynamics, mid-October 2026, adds a sharper edge to “public.” Nicolls said SpaceX has started sharing with some Chinese operators and not with many others. DCD argues the safety site’s alerts are conjunction messages to participants, not an open catalog, and that “public” ephemerides still flow through registries that can exclude users. Treat DCD as a critique, and the Ars quotes as the primary reported speech.

<https://arstechnica.com/space/2026/10/spacex-calls-for-better-coordination-in-orbit-after-near-misses-with-starlink/>
<https://www.datacenterdynamics.com/en/news/spacexs-starlink-encourages-every-satellite-operator-to-share-data-with-stargaze-platform-for-safety/>

### The skeptical replies, because a one-sided SpaceX quote is not the discussion

Scientific American, on a Starlink “anomaly” that lost contact near 560 km: LeoLabs read the radar as an internal energetic event, not a collision. Peter Plavchan (George Mason): failure counts rise with satellite counts. Jonathan McDowell: he does not see how the risk to the station or to Artemis II is literally zero, even if debris reenters quickly, and a design flaw that repeats across many Starlinks would change the risk “a lot.”

Aerospace America, Victoria Samson of the Secure World Foundation: she was worried in 2019 when Starlink 44 had a 1-in-1,000 conjunction with ESA’s Aeolus and Aeolus moved. Six years later she says it has gone better than she feared, and Starlink had avoided collisions at a fleet of about 8,300, roughly two-thirds of active satellites at the time of that article. Her remaining worry is several Starlink-sized fleets, including Chinese ones, with no rules of the road. Ian Christensen, same organization: email does not scale as a conjunction protocol. SpaceX’s own filings, as reported there, tightened the maneuver threshold over time, most recently to 3 in 10 million. Hugh Lewis’s comment in that piece: there is no business case for maneuvering that often, so the motive is safety, and the fuel cost shortens life.

A Science / AAAS piece on Lewis’s megaconstellation model is the long-run version: of 16 planned constellations in his study, totaling nearly 1.7 million satellites, six crossed into runaway debris in the model, including China’s Guowang and SpaceX’s Starmind plan for 1 million satellites. This is a model, not a measurement. It belongs next to ESA’s health index, not instead of it.

- <https://www.scientificamerican.com/article/spacex-starlink-satellite-suffers-mysterious-anomaly-in-orbit/>
- <https://aerospaceamerica.aiaa.org/features/heavy-traffic-ahead/>
- <https://www.science.org/content/article/planned-satellite-megaconstellations-could-generate-runaway-space-debris>

### The subproblems inside SpaceX’s complaint

These are the pieces a project could pick up without pretending to be a space-traffic authority:

1. **Unannounced maneuvers.** The 164,000 figure is a detection gap, not a crash count. The plain-language version: after someone moves, the old prediction is a lie for hours.
2. **Half of the relevant operators do not share.** Some will not, some are not allowed to. A public page cannot shame a secret military satellite, and it can show how much of the public catalog is stale.
3. **The screening tool is closed.** space-safety.com is for operators. Everyone else gets a README and a manifest.
4. **Identification is behind detection.** ESA says more objects are seen than can be tied to an owner. Slingshot’s whole product is “one pixel, but the pixel has a fingerprint.”
5. **Altitude bands move.** ESA’s 2026 report says constellations change altitude year to year. A map of “the crowded shell” has a date on it or it is wrong.
6. **Reentry is now a ground problem and an atmosphere problem.** Casualty risk is up. Burning up completely may pollute the upper atmosphere. ESA says they need measurements before rules.
7. **Starmind-scale plans make the current complaint louder.** Asking the world to share ephemerides while filing a plan for a million more satellites is the political context of the October posts. A project that only repeats SpaceX’s graphic will look like a press release. A project that shows the public data, the missing half, and the closed tool is a different object.

## What the three institutions agree on, even when they want different things

- NASA and ESA are opening more data than a person can analyze, and they are spending effort on analysis-ready products (OPERA, CDSE on-demand processing, Biomass calibration) because the raw files failed.
- ESA’s debris office and SpaceX’s Starlink office, in the same six weeks, described a low-Earth orbit whose risk is dominated by behavior and missing trajectories, not by a lack of sensors.
- Neither the Earth-data gap nor the orbit gap is solved by another dashboard of dots. Both are solved, if they are solved, by a sentence a non-specialist can act on, with the file it came from one click away.
