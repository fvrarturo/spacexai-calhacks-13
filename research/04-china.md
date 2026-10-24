# 04. China: constellations, export rules, and the unused archive

China is running two different space races that get conflated. One is Earth observation: Jilin-1, Gaofen, Siwei Gaojing, a commercial radar fleet called Nuwa. The other is broadband mega-constellations: Qianfan (also SpaceSail, 千帆) and Guowang (国网). Both produce problems a hackathon should understand. Only the first produces imagery. The second produces the orbital-traffic problem SpaceX spent October talking about.

Counts below conflict across outlets and months. They are printed with their dates. Do not merge them into one census.

## Jilin-1, the optical constellation that already revisits faster than the West’s public systems

Operator: Chang Guang Satellite Technology (长光卫星), Jilin Province. Commercial partner often named in older English writeups: HEAD Aerospace.

Xinhua, 3 March 2025, in a story that was really about two new Siwei satellites, gave the standard official comparison:

- Jilin-1, first launch October 2015, **more than 117 satellites** at that time.
- Any point on Earth about **40 times a day**.
- Global coverage six times a year, all of China 24 times a year.
- More than 130 overseas users, for land survey, urban buildings, agriculture, and forestry.
- Pitched directly against Maxar and Airbus.

<https://english.news.cn/20250303/586b8abc0d5e43428383ac6c8f047204/c.html>

A Tencent / industry feature dated 17 March 2026 still describes the September 2025 state: **117 satellites in orbit**, 38–40 revisits a day anywhere, six global land covers a year, China every half month. It adds an operational number the English wire stories skip: **42,000 scenes a day, more than 100 TB a day**. The same piece says Chang Guang’s response to “data that is merely available” is an in-house model they call “Earth Eye,” plus an open platform, aimed at finance and power as well as maps. The phrase they use is the same phrase as the Western glut essays: move data from 可用 (usable) to 好用 (good to use).

<https://news.qq.com/rain/a/20260317A06U9I00>

Fast Technology via Sina, 20 June 2026, after the 37th Jilin-1 launch (eight satellites on 15 June):

- **162 launched, 152 still operational.**
- More than 90% are sub-meter, at 0.5 m.
- 38–40 imaging opportunities a day anywhere on land or sea, a chance roughly every 35–40 minutes.
- Half a month to cover China at sub-meter, six full covers of global land in a year.
- The trick is not one magic satellite. It is many orbit planes at different local times, plus large off-nadir pointing, plus a mix of high-res, wide, and video payloads tasked together.
- Target: **300 satellites in 2027**, and SAR added so the weather stop being a hard limit.

<https://finance.sina.com.cn/tech/roll/2026-06-20/doc-iniczxrt0599882.shtml>

eoPortal’s English mission page is behind those figures (it still describes the 2021-era plan of 138 satellites and a 10-minute revisit ambition). Use it for design history, not for the 2026 count. <https://www.eoportal.org/satellite-missions/jilin-con>

### Why this matters for a project that will not have Jilin data

Public Sentinel-2 is 5 days with two satellites, 10 m. Landsat is 8 days with two satellites, 30 m. Jilin-1’s claim is a sub-meter look every half hour of opportunity. The problems that need that cadence — a ship, a construction site, a fire front, a protest crowd, a port queue — are exactly the problems public optical data is bad at. A hackathon that pretends Sentinel-2 can do intra-day tactical monitoring will be wrong. A hackathon that uses Sentinel-2 for what it is good at, which is a decade of comparable land cover, is using the instrument honestly.

The commercial problem Chang Guang is naming out loud is not revisit. It is that customers still cannot use the scenes. That is the same bottleneck as Planet.

## Other Chinese imaging systems

### Siwei Gaojing (中国四维 / CASC)

Xinhua, 3 March 2025: Long March-2C on 27 February 2025 orbited Siwei Gaojing-1 03 and 04. CASC called them the highest spatial resolution and geometric accuracy among Chinese commercial remote-sensing satellites at that moment. Agile pointing, “anti-shake” imaging, uncontrolled geolocation claimed at an international level. The Siwei plan described then: 9 satellites up, a design of 28 (16 high-res optical, 4 wide optical, 8 SAR), expandable to 56. Uses named: maritime traffic, law enforcement, and fast images after floods, fires, and earthquakes.

Same URL as the Jilin Xinhua piece above.

### Gaofen and the civil national system

Gaofen is the state high-resolution special project, not a startup. The data rules below were written for it and then extended, in later notices, toward commercial operators. Western users should assume Gaofen scenes of China are not a free archive in the Sentinel sense.

### Nuwa

Xinhua, same March 2025 piece: 12 satellites up, described as China’s largest commercial radar constellation, with a plan of 114. This is the Chinese counterpart to the ICEYE / Capella / Umbra buildout. It has the same cloud-penetration promise and, under the rules below, a tighter export limit (public SAR primary products not sharper than 1 m).

### Hyperspectral and the science missions worth knowing

Not fully re-documented in this pass, listed so they are not forgotten if the idea turns spectral:

- Zhuhai Orbita and the Zhuhai-1 / OHS hyperspectral cluster.
- Gaofen-5 class atmospheric and hyperspectral missions.
- SDGSAT-1, the sustainable-development science satellite, which has been discussed internationally more openly than Gaofen.
- LuTan-1 and Hongtu-1 as L-band / InSAR civil missions, the technical cousins of NISAR.

If one of these becomes the idea, it needs its own data-access check. Do not assume an API.

## The rule that decides whether a Cal Hacks team can touch the data

Two layers.

### International cooperation measures, CNSA, 11 April 2022

State Council repost of the CNSA interim measures. Still the clearest public text.

- Foreign users are classed: governments, research and universities, everyone else (companies and individuals). Governments are in principle free. Research is free or cheap. Companies pay.
- **Data over China is not sent abroad without authorization.** Sensitive places and sensitive times need authorization.
- Default geographic limit: a foreign partner gets data over their own country, or over their regional organization’s members. Not a global dump.
- Self-service, without a special security review, is allowed only coarser than a published line. The text’s thresholds include panchromatic at **0.5 m and coarser**, multispectral at **2 m and coarser**, hyperspectral only if spectral resolution is 5 nm or worse and spatial resolution is 10 m or coarser, infrared at 20 m and coarser, microwave imagery at **1 m and coarser**. Sharper than that, or any global land archive for research, needs CNSA or a joint review.
- Commercial Chinese operators are told to follow the same measures.

<https://www.gov.cn/zhengce/zhengceku/2022-05/05/content_5688668.htm>

### SASTIND notice, 14 March 2025, on commercial TT&C

A notice about commercial tracking stations that includes a data clause. Article 15: operators who receive remote-sensing data must follow the national civil satellite remote-sensing data measures. **Remote-sensing data acquired over China may not be given to foreign organizations or individuals without authorization. Sensitive regions and sensitive periods are distributed only with authorization.** The clause says domestic commercial satellite remote-sensing data security follows the same rule.

<https://xinwen.bjd.com.cn/content/s67d41e7ee4b068c68f1100c1.html>

### The civil data measures, as republished

A May 2025 repost of the interim measures (the underlying rules are the ones the 2025 notice points at) says public optical primary products are **not better than 0.5 m**, public SAR primary products **not better than 1 m**, and the defense industry agency can move that line. Primary products are the default delivery. Public-interest and education uses are free. Commercial use is paid, on a non-profit fee schedule, with the money going to the treasury. Emergency observations jump the queue. The confidentiality chapter repeats the foreign-transfer ban and the sensitive-area rule, and says it applies to commercial operators.

<https://www.secrss.com/articles/79163>

### Practical consequence for this team

A project that needs Chinese commercial sub-meter imagery of anywhere, or any high-resolution imagery of China, is not a weekend project. It is an export-control project. Public Sentinel, Landsat, MODIS, EMIT, SWOT, and NISAR are the datasets you can actually ship. Chinese constellations matter as **the capability the public archive does not have** (intra-day sub-meter) and as **a policy wall**, not as a STAC endpoint.

## “95% of the data is wasted”

Sina Finance column, 2 January 2026. The author says industry insiders put utilization of data from China’s launched remote-sensing satellites at **under 5%**. The rest has never been looked at. Capital formation, in the column’s breakdown: satellite internet about 41%, rockets about 25%, satellite manufacturing about 18%, remote-sensing applications about 2%.

Mechanisms the column names:

1. **The processing loop is slower than the model loop.** Daily volume is described as petabyte-scale. Models want a new training run every 5–6 days. Producing an analysis-ready product takes months. The user wanted “now.”
2. **Launch cost.** The column cites roughly 150,000 RMB per kilogram domestically against about $3,000 per kilogram for Falcon 9, “more than five times,” and says a 500 kg satellite can cost ~75 million RMB to launch, sometimes more than the satellite. Zhuque-3 (LandSpace) and Pallas-1 (Galactic Energy) are listed as planned reusable vehicles, not as operating ones.
3. **Demand was never the thing that got funded.** The application layer is 2% of the capital and 100% of the utilization problem.

Label this as a columnist’s insider claim. It matches, almost sentence for sentence, the Western “imagery glut” essays. It is not a National Bureau of Statistics figure.

<https://finance.sina.com.cn/stock/2026-01-02/doc-inhewkev3855901.shtml>

The Tencent Jilin feature is the operator’s reply to that column: a big model, an open platform, and industry packs (finance, power), so the 100 TB/day has somewhere to go. Whether “Earth Eye” is good is not something this pass can judge. The existence of the pitch is the evidence. Chang Guang knows raw revisit is not a product.

## Qianfan and Guowang, the broadband problem that feeds the debris problem

These are Starlink competitors. They do not take pictures for customers. They change the orbital environment that every imaging satellite has to fly through.

MERICS, “Orbital geopolitics: China’s dual-use space internet”:

- Qianfan / SpaceSail, run by Shanghai Spacecom Satellite Technology (SSST), filed toward **15,000** satellites. Guowang, the national network, toward **12,992**. Together just under 28,000 by 2030. Other private filings would push the paper total past 50,000.
- The trigger MERICS names is Starlink’s performance in Ukraine, read in Beijing as a strategic fact about low Earth orbit.
- Deployment is far behind the slides. SpaceSail’s plan of about 650 satellites by the end of 2025 was, in this report, just over 100. Guowang is a small fraction of its filing. Combined, about 260 satellites up against an ITU milestone: **10% of each planned network on orbit by the end of 2026**, which MERICS says means more than 2,600 satellites in a year. In 2025 the two together launched about 180. MERICS calls the milestone impossible at the current rocket rate.
- The bottleneck is reusable launch. LandSpace’s Zhuque series is the vehicle SSST is hoping will fly 10–18 satellites at a time. It is not yet the Falcon 9 equivalent. State rockets are shared with navigation, remote sensing, and human spaceflight.
- Technical gaps MERICS lists besides rockets: inter-satellite links, user terminals, software for a 90-minute orbit.
- About 1,000 LEO satellites can light up a thin global service. Starlink’s much larger fleet exists because each satellite has limited bandwidth and the user count is large. China’s first service does not need 15,000 birds. The filings are about spectrum rights and a later capacity, not about this year’s users.

<https://merics.org/en/report/orbital-geopolitics-chinas-dual-use-space-internet>

WIRED’s earlier deployment piece, useful for the failure mode rather than the latest count:

- At the time of that article, Qianfan had launched 90, Guowang 29, plus about a dozen Guowang experimental satellites that were not being counted.
- Jonathan McDowell, using U.S. Space Force public tracking because the operators publish little: of those 90 Qianfan satellites, **13 looked irregular**, and the October 2024 batch got **5 of 18** up to the planned altitude. He does not call them all dead. He does say the early failure rate is far above Starlink’s later rate (under 0.5%, after an early ~3%) and OneWeb (2 failed out of 600+ in that telling).
- Qianfan and Guowang chose **higher orbits than Starlink**, so a failed satellite decays more slowly and is debris for longer.
- Victoria Samson, Secure World Foundation: there is no real space traffic control. Conjunctions handled by phone and email do not survive multiple mega-constellations.
- Rocket procurement: Qianfan ran two public tenders for launch and both failed for lack of bidders.

<https://www.wired.com/story/china-starlink-competitor-satellites/>

Cross-read with SpaceX in October 2026 ([03-voices-nasa-esa-spacex.md](03-voices-nasa-esa-spacex.md)): Nicolls said Starlink has begun sharing ephemerides with some Chinese operators and not with many. The 2022–2025 Chinese data rules are about imagery, not about sharing a trajectory. The trajectory-sharing gap is its own policy problem, and both sides describe it as unsolved.

Lewis’s megaconstellation model, reported by Science, puts Guowang among the proposed fleets that tipped into runaway debris in his simulation, alongside a million-satellite Starmind. Model, not a measurement. <https://www.science.org/content/article/planned-satellite-megaconstellations-could-generate-runaway-space-debris>

## Problems a project could honestly take from the China record

1. **Public cadence versus commercial cadence.** State what Sentinel can and cannot see, using a place where the news happened between two Sentinel passes. The Chinese constellation is the existence proof that the capability is real and not available to you.
2. **Unused data is not a Western story.** The 5% claim, if even directionally right, means the application gap is the global problem. Building another satellite, even a fictional one, is the move Chinese capital already over-made.
3. **Export control as a user problem.** A journalist or a researcher outside China cannot verify a sub-meter claim about a Chinese city with Chinese data, and often cannot buy the Western sub-meter scene either. The honest tool is a statement of what the open archive shows, plus what it is blind to.
4. **Debris and unidentified objects.** Higher-orbit failures, unpublished health, and ESA’s note that more fragments are detected than identified. A public TLE map will show Qianfan and Guowang as objects. It will not show which of them are healthy. Saying so is part of being accurate.
5. **Do not build a “China watcher” military product.** The brief is a clear public problem. Ship tracking for a coast guard using Global Fishing Watch is a public problem. Tasking analysis of PLA sites is not a weekend student project and not the spirit of the open-data brief.

## Launch vehicles, only as the constraint on everything above

Reusability is the switch both MERICS and the Sina column say is still open. Names that recur: LandSpace (Zhuque), Galactic Energy (Pallas), plus the state Long March fleet that actually launched Jilin-1 and Siwei. SpaceX’s manifest in October 2026 is still flying Starlink batches of 24–27 satellites several times a month, including a Vandenberg flight targeted for 27 October. The asymmetry the Chinese sources themselves describe is launch cadence, not a lack of satellite factories.

SpaceX manifest, for the contrast: <https://www.spacex.com/launches/starlink/>
