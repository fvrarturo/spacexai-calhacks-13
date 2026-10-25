# 07. Problem cards

Each card is a problem someone is already spending money or reputation on, the subproblems inside it, what is sold today, and whether a weekend project has a remaining gap. “Gap” means a user-shaped hole, not a research-shaped hole.

The cards are ordered by how often the sources in the other files brought them up, not by how fun they are.

## 1. The interpretation gap

**Problem.** Daily imagery exists. A decision does not.

**Who feels it.** Insurers, newsrooms, city staff, farmers, and the startups that thought those people would buy scenes. Planet’s pivot to defense, Gro’s shutdown, terrAIntel’s white paper, the Cambridge six-month night-lights story, and the European local-government survey are the same complaint.

**Subproblems.**

- Which product and which version.
- Activation energy: login, format, CRS, cloud mask.
- The output is not in the tool the person already uses.
- No provenance, so a professional cannot sign the result.
- Level-4 products hide the errors of level-2.

**What exists.** OPERA, Dynamic World, WorldCover, CDSE openEO, Earth Engine, foundation models, SkyFi, UP42, terrAIntel.

**Remaining gap.** One question, one place, an answer a non-specialist can read, with the scene id on the page. Not a new portal for all questions.

**Weekend.** High, if the question is narrow.

## 2. Clouds, smoke, and darkness

**Problem.** Optical satellites do not see the ground about half the time, and they never see it at night or through a fire’s smoke.

**Who feels it.** Flood insurers, wildfire agencies, maritime coast guards, anyone in the tropics.

**Subproblems.**

- SAR sees through weather and does not look like a photo, so the user does not trust it.
- Thermal sees the fire and not the damage.
- No single public product answers “what is burning, what has it hit, what can it not yet see.”
- Commercial SAR capacity grew faster than SAR literacy.

**What exists.** Sentinel-1, NISAR, ICEYE, Capella, Umbra, OPERA DSWx-S1, OroraTech plus the 22 October 2026 ICEYE wildfire deal, GOES for continental fires, FIRMS.

**Remaining gap.** A public, plain-language handoff between a FIRMS point and an OPERA or Sentinel-1 water/damage picture. The commercial version was announced this week and is not free.

**Weekend.** High for one event. Low if the goal is a global watch floor.

## 3. Floods, from “how bad” to “whose building”

**Problem.** During a flood the insurer and the emergency manager need extent, depth, and duration within hours, joined to buildings. Gauges and aerial flights do not cover the event.

**Who feels it.** ICEYE’s buyer, Floodbase’s buyer, local governments. ICEYE’s own quote is about multiple regions flooding at once (Storm Boris) and not knowing the scale for six hours.

**Subproblems.**

- First look versus the maximum extent a day later. ICEYE sells both (Rapid Impact vs Flood Insights) because they are different decisions.
- Depth is not in a free optical water mask. Depth needs a DEM and a model, which is where overclaiming starts.
- Public OPERA water products are excellent and still not a claims file.
- Urban flood water under trees and between buildings is where 10–30 m products get fuzzy.

**What exists.** OPERA DSWx, Sentinel-1, GFM (Copernicus emergency flood products when activated), ICEYE, Floodbase.

**Remaining gap.** A one-page public brief for one flood: water mask, buildings touched, what the product cannot see, link to the granule. Depth only if a cited method produces it.

**Weekend.** High for extent. Medium if depth is included honestly.

## 4. Wildfire, fragmented on purpose

**Problem.** Detection, spread, and damage are three products. ICEYE and OroraTech said so on 22 October 2026 while announcing they had stitched thermal and SAR into one paid view.

**Who feels it.** Incident commanders, utilities, insurers, people who live at the wildland edge.

**Subproblems.**

- FIRMS false alarms and late detections under cloud.
- A hotspot is not a perimeter.
- “What is in the way” needs buildings, roads, and a land-cover class.
- Damage while the fire is still burning needs radar or a plane, because the optical view is smoke.

**What exists.** FIRMS, GOES, MODIS/VIIRS burned area, OPERA disturbance, OroraTech, ICEYE, Canada’s WildFireSat plans, NASA’s fire-related Landsat science team work.

**Remaining gap.** The public one-pager those companies just said the market does not get for free: hotspot, what land it sits on, which buildings are within a stated distance, and a sentence that does not pretend to be a perimeter.

**Weekend.** High.

## 5. Methane super-emitters no one wrote down

**Problem.** Inventories are self-reported and miss large point sources. Satellites can see the plume. Seeing it does not notify the operator or the journalist in a form they can forward.

**Who feels it.** Regulators under methane rules, UNEP MARS, Kayrros’s clients, Carbon Mapper’s public users, communities next to landfills and oil fields.

**Subproblems.**

- Wide sensors (Sentinel-5P) cannot name the facility. Narrow sensors (EMIT, Tanager, GHGSat) can, and they do not image everywhere every day.
- EMIT’s product version changed on 16 October 2026. Old plumes and new plumes are not one time series until reprocessing finishes.
- MethaneSAT’s loss of contact in mid-2025 showed the single-satellite risk.
- Attribution: a plume over a basin is not a plume from one well. Carbon Mapper’s own tutorial joins plumes to Climate TRACE waste sites because the join is the hard part.
- Persistence: one detection is a maybe. Repeated detections are a source.

**What exists.** Carbon Mapper portal, EMIT, Sentinel-5P, Kayrros Methane Watch, GHGSat, Tanager.

**Remaining gap.** A “letter” view: this source, this sector, this instrument, how many times, the uncertainty, the nearest named facility if a public inventory has one, and the sentence a non-expert can send. Carbon Mapper already has the points. The letter is the gap, and it has to stay inside their non-commercial terms.

**Weekend.** High, and the data is eight days old.

## 6. Local government does not have a GIS hire

**Problem.** European local authorities name skills, budget, and “this does not meet our operational need” as the barriers. Aerial photos already answer many of their questions. Satellite data loses the tie.

**Who feels it.** City sustainability offices, small planning departments, civil protection.

**Subproblems.**

- Heat, trees, illegal fill, shoreline, and post-storm damage are different jobs. A platform for all of them is how Gro died.
- 10 m pixels do not settle a property dispute.
- Procurement of commercial imagery is its own barrier, separate from science.

**What exists.** Copernicus land services, national aerial programs, consulting shops, CDSE.

**Remaining gap.** One operational question for one city, using only free data, written the way a department memo is written.

**Weekend.** High if the question is picked in advance. Low if the team tries to be a platform.

## 7. Journalism under a deadline

**Problem.** Geoville: “Can we get a reliable answer in time, and show how we got it?”

**Who feels it.** Newsrooms that do not have a visual-investigations desk. Bellingcat-style desks already have methods. The gap is everyone else.

**Subproblems.**

- Commercial providers can restrict a region. When that happens, the public archive and SAR are the fallback, and they are coarser.
- A model mask without a scene id will not survive an editor.
- The story is often “what changed between Tuesday and Thursday,” which is inside the Sentinel revisit gap. Honesty about that gap is the product.

**What exists.** Sentinel Hub, Earth Engine, Maxar’s press programs, terrAIntel, Bellingcat’s open guides.

**Remaining gap.** Same as card 1, with a provenance block a copy desk can check.

**Weekend.** High, as a mode of the place-brief, not as a separate startup.

## 8. Forest carbon and “is this project real”

**Problem.** Offsets need a biomass number. Optical greenness is not biomass. Pachama, Chloris, Sylvera, and BeZero exist because buyers do not trust project developers.

**Subproblems.**

- Additionality and leakage are not pixel problems.
- ESA Biomass data is public as of January 2026 and still in a calibration campaign over a few countries.
- A green map is easy to fake in a demo and easy to tear apart.

**What exists.** GFW tree-cover loss, Biomass mission, commercial MRV, national forest inventories.

**Remaining gap.** A narrow audit of one known concession using GFW loss plus a clear statement that biomass is not yet a global public layer. Anything broader will sound like the startups.

**Weekend.** Medium. High risk of saying something the data does not support.

## 9. Crops and food

**Problem.** Yield, stress, and irrigation timing. Real buyers exist (commodity desks, large farms). The startup path is littered (Gro).

**Subproblems.**

- Ground truth is the cost.
- Hyperspectral would help and is mostly commercial (Pixxel, Wyvern).
- Smallholders do not buy dashboards.

**What exists.** Sentinel-2 time series, Landsat, ESA WorldCereal-type products, national crop statistics, private platforms.

**Remaining gap.** Thin, for a hackathon. A single-crop anomaly in one county is buildable and forgettable.

**Weekend.** Buildable, weak story.

## 10. Dark vessels and illegal fishing

**Problem.** Ships turn AIS off. SAR still sees metal. RF constellations hear some of them.

**Who feels it.** Coast guards, fishery agencies, journalists, GFW’s 200-plus API users.

**Subproblems.**

- A SAR detection without a flag is not a crime.
- Matching to a registry is the product, and GFW already does it.
- Tasking a commercial radar pass is the part a public archive cannot promise.

**What exists.** GFW SAR layer and 4Wings API, Sentinel-1, Unseenlabs, HawkEye 360, ICEYE.

**Remaining gap.** A narrative on top of one GFW detection for a small agency that will never integrate the API. Easy to build, hard to justify next to GFW’s own map.

**Weekend.** Medium. Only worth it if the story is a specific fishery and the data is already public.

## 11. Ground motion, subsidence, and the new radar mission

**Problem.** Groundwater pumping, landslides, volcanoes, and earthquakes move the ground by millimeters. InSAR measures that. Almost nobody outside a geodesy group can run it.

**Who feels it.** Water agencies, dam operators, city engineers in subsiding districts, scientists who waited a decade for NISAR.

**Subproblems.**

- Sentinel-1 displacement products from OPERA are North America, 30 m, and still not a letter to a mayor.
- NISAR’s better wavelength for vegetation and deformation went public in July 2026 and is operationally awkward.
- Atmospheric noise creates fake motion. A demo that skips this will be wrong.
- BETA versus PROVISIONAL processor differences look like deformation.

**What exists.** OPERA DISP, the NISAR L2/L3 geocoded products, commercial InSAR services, national geological surveys.

**Remaining gap.** The largest scientific gap on this list, and the worst weekend risk. A honest demo is one tile, one official product, one sentence about what would make it false.

**Weekend.** Low unless someone has already opened a NISAR geocoded browse and it works from a laptop.

## 12. The orbital coordination failure

**Problem.** In 2026 Starlink saw conjunctions with about 650 maneuvering third-party satellites and only about half shared ephemerides. Over six months, about 164,000 conjunctions had closest approach within four hours of an unannounced maneuver. ESA’s health index went from about 4 to about 50 in one year. There is no global requirement to say where you are going.

**Who feels it.** Every operator in LEO, ESA’s debris office, and anyone who will live with the orbits those operators leave behind. Victoria Samson’s point is that one constellation learned to self-dodge, and several constellations will not fit in an email thread.

**Subproblems.**

- Proprietary maneuvers versus government-forbidden sharing. Different fixes.
- Public TLEs are too coarse for the claim “this was a near miss.”
- Starlink’s precise ephemeris is public. The screening tool is not.
- Chinese broadband constellations publish less health information. McDowell’s early Qianfan failure counts came from U.S. Space Force tracking, not from the operator.
- Altitude bands shift year to year.
- Unidentified debris is growing because detection got ahead of identification.
- Reentry casualty risk is a new ESA metric, still small, rising. Design-for-demise fights with atmospheric chemistry. ESA wants measurements first.
- Starmind’s million-satellite plan and Guowang’s filing make the current numbers look like the start.

**What exists.** space-track, CelesTrak, Starlink’s public files, space-safety.com for operators, LeoLabs, Slingshot, Kayhan, ESA’s annual report, TraCSS as a government program still in progress.

**Remaining gap.** A public explanation of one shell for one evening: who publishes a trajectory, who is only a TLE, what SpaceX and ESA each measured, and what this page refuses to claim. Not a collision-probability service. That service is what Kayhan and SpaceX sell to operators, and doing it badly is worse than not doing it.

**Weekend.** Medium. The story is the strongest “this month” story in the pack. The honest version is a narrative map, not a flight-dynamics product.

## 13. Reentry, the ground, and the upper atmosphere

**Problem.** More than three intact objects reenter on an average day. ESA added on-ground casualty risk to the 2026 report because the cumulative chance rose. At the same time, burning up completely may load the upper atmosphere with metals. They say the pollution is not yet measured well enough to regulate.

**Who feels it.** Range-safety people, the public under uncontrolled reentries, atmospheric chemists, operators designing the next bus.

**Subproblems.** Data is annual and statistical, not “this object hits this town.” A live reentry tracker exists in the hobbyist world and is not a casualty model.

**What exists.** ESA report, space-track decay lists, Aerospace reentry notices.

**Remaining gap.** Mostly a science measurement gap. A hackathon can illustrate the trend. It cannot discover the atmospheric chemistry.

**Weekend.** Low as a standalone. A single chart inside card 12 is enough.

## 14. Continuity of the free record

**Problem.** Landsat Next and GeoXO spent 2025–2026 in affordability reviews. Commercial constellations do not replace a 54-year calibrated land record or a geostationary weather record.

**Who feels it.** Climate services, USDA-type users, weather agencies, anyone whose method depends on last year’s pixel meaning the same as 2005’s.

**Subproblems.** Budget, instrument descopes, and the fact that the public does not notice a data gap until a fire season or a crop report breaks.

**What exists.** Landsat Science Team, Copernicus continuity (Sentinel-1C/D already up, Sentinel-3C expected late 2026), NOAA GOES-19.

**Remaining gap.** Political and programmatic. A student project can show what a gap would do to one time series. It will not restore a satellite.

**Weekend.** Only as a sentence inside a Landsat demo, not as the project.

## 15. Labels, the expensive half of “AI for Earth”

**Problem.** Foundation models cut the number of labels. They do not create trust. GEO-Bench-2 says no model wins every task. Φ-week scientists said extrapolation outside the training set has already produced bad high-impact papers. Embeddings from different groups do not share a grid, a CRS, or a file format.

**Who feels it.** Every team that thought “we will just use the foundation model.”

**Subproblems.** License differences (Apache versus DINO versus ODC). AlphaEarth’s official bucket is provider-pays. Tessera has no CRS. Major TOM’s grid is not MGRS.

**What exists.** The model list in [06-off-the-shelf.md](06-off-the-shelf.md).

**Remaining gap.** Not a model. A rule for when the model is allowed to speak, which is a product decision.

**Weekend.** Do not make this the project. Use it as a constraint on whatever you build.

## 16. Chinese data that exists and cannot be used here

**Problem.** Jilin-1 can look dozens of times a day at sub-meter resolution. Utilization inside China is claimed, by insiders in one column, to be under 5%. Export of sharp data, and of any data over China, is gated.

**Who feels it.** Chang Guang’s own product team, foreign researchers, journalists, and the capital stack that funded rockets instead of applications.

**Subproblems.** See [04-china.md](04-china.md).

**Remaining gap.** A public-data project that is explicit about the cadence it does not have. Not a scraper of Chinese imagery.

**Weekend.** As a constraint, not as a dataset.

## How to read the cards against the brief

The brief wants a clear problem and a credible idea, with technical detail in second place. Cards 1, 3, 4, and 5 can be said in one sentence and demoed on public data. Card 12 can be said in one sentence and must be demoed carefully so it does not become fake flight dynamics. Cards 11, 13, and 14 are real and are the wrong size for Sunday. Cards 8, 9, and 10 are real and already have a well-known product on top of them.
