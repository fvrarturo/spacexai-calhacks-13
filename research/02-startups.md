# 02. Startups and companies, and the problem each one is selling against

Grouped by where they sit. A company in the first group owns satellites. A company in the second group owns a decision. The second group is where the 2026 revenue story is, and it is also where a hackathon is most likely to collide with a product that already exists.

Figures are from the sources named. Where a 2026 number was not re-checked in this pass, the entry says what the company is for and does not invent a metric.

## 1. Medium-resolution, high-revisit optical

### Planet Labs

Former NASA engineers. Dove / SuperDove constellation images land nearly daily at a few meters. SkySat, now being replaced by Pelican, is the high-resolution tasking layer. Tanager is the hyperspectral spacecraft built with the Carbon Mapper coalition and JPL, more than 400 bands, 30 m, aimed at methane and CO2 plumes down to a wellhead.

The original problem they sold: governments had infrequent, expensive imagery; agriculture, finance, and NGOs needed a daily picture. The problem they hit: daily imagery was not a daily budget. FY2026 revenue about $308 million, first non-GAAP profitable year, defense and intelligence up more than 50%. Free Sentinel-2 competes with the cheap end of the catalog.

Sources: glut essay <https://newspaceeconomy.ca/2026/04/08/the-satellite-imagery-glut-too-much-data-too-few-paying-customers-and-a-coming-shakeout-in-earth-observation/> and the 20 Oct 2026 survey <https://newspaceeconomy.ca/2026/10/20/the-state-of-earth-observation-2026/>.

### Satellogic

Argentina-founded, now a Delaware company (March 2025) because U.S. defense contracts did not show up while it was offshore. 2025 revenue $17.7 million. Merlin is an “AI-first” constellation pitched at near-daily one-meter remapping, first launch targeted October 2026. The story is a small company that discovered the commercial imagery market was not the market.

### BlackSky

Sells speed. Gen-3 is 35 cm optical with inter-satellite links and automated detection. 2025 revenue $106.6 million, backlog $345 million. The problem they own is “tell me in this hour,” mostly for defense, not “map the planet every day.”

### Airbus Defence and Space, Pléiades Neo

30 cm, eight bands, sold to mapping and civil security. Not a startup. Included because every commercial pitch is priced against it and against Vantor.

### Vantor (was Maxar Intelligence)

WorldView plus six WorldView Legion satellites, constellation completed February 2025, 34 cm, up to 15 passes a day over mid-latitudes. Tensorglobe is their fused 3D globe. Customers include NGA’s Global Enhanced GEOINT Delivery (400,000+ U.S. government users) and the Luno analytic-services program. This is the high-resolution incumbent. A hackathon will not out-collect them, and their archive is not free.

### China Siwei / Siwei Gaojing, Chang Guang / Jilin-1

Covered in [04-china.md](04-china.md). They are the other high-revisit optical reality. Jilin-1 claims 38–40 imaging opportunities a day anywhere on Earth. Western users generally cannot buy the sharp scenes.

## 2. Synthetic aperture radar

The problem they all share: clouds, smoke, night, and floods hide the ground from cameras. Radar sees through that. The problem they all then share with optical companies: a radar image is harder to explain than a photo, so the buyer still needs an interpreter.

### ICEYE

Largest commercial radar fleet. 2025–2026 launches in batches (six in June 2025, five in November 2025, two in January 2026, six on 30 March 2026, per the New Space Economy survey). Gen-4 aims at sub-meter spot, coherent change detection, and dwell modes. Two products that name a real user:

- **Flood Insights** and **Flood Rapid Impact** (announced 14 July 2025). Extent within about 6–12 hours of the first signs, updated through the event, depth and duration for insurers. They describe the insurance problem as not knowing the scale when many places flood at once (Storm Boris was their example). Texas floods in July 2025 were a public proof.
- **Wildfire, with OroraTech**, announced 22 October 2026, two days before this hackathon. Thermal detection plus radar damage, because “wildfire intelligence is often fragmented across separate sources.”

Sovereign sales: dedicated satellites and ground segments for defense ministries in Europe, NATO, Portugal, Ukraine.

<https://www.iceye.com/solutions/insurance/flood-insights>
<https://www.iceye.com/newsroom/press-releases/iceye-unveils-ml-powered-flood-rapid-impact-product>
<https://www.iceye.com/newsroom/press-releases/iceye-partners-with-ororatech-to-deliver-full-lifecycle-wildfire-intelligence>

### Capella Space

Acadia generation, higher bandwidth and power, optical inter-satellite links for faster tasking. U.S. government leaning. Same interpretation gap as the glut essay describes.

### Umbra

X-band, commercial imagery around 25 cm, open-data scenes down to 16 cm. NASA radar quality assessment in May 2026 said resolution, impulse response, and geolocation met federal scientific specs. They have shared data with Vantor. The open scenes are one of the few legal ways to show very sharp radar in a demo without a contract.

### Synspective (Japan), iQPS (Japan)

StriX and QPS-SAR. National commercial radar outside the U.S./Finland pair. Relevant because the “SAR glut” is global, not a Silicon Valley story.

### Unseenlabs, HawkEye 360, Spire

Not cameras. They collect radio-frequency emissions. Fused with radar, they are how maritime products claim to see ships that turn AIS off. Spire also sells GNSS radio occultation for weather. The problem is dark ships and signals, not pictures. Global Fishing Watch already publishes a SAR-vessel layer on top of public radar (see datasets).

## 3. Hyperspectral, thermal, and gases

The problem: RGB and even 12-band multispectral cannot name a mineral, a crop disease, or a methane plume. Narrow bands can. The data is heavier, the satellites are younger, and the buyer has to trust a fingerprint they cannot see.

### Planet Tanager and the Carbon Mapper coalition

Public-good methane and CO2 super-emitters. Portal is non-commercial for governments, journalists, researchers, nonprofits. API exists and requires an account. Instruments include Tanager-1 and NASA EMIT on the space station. Commercial reuse of Carbon Mapper data is restricted; non-methane Tanager products belong to Planet.

The problem they state: you cannot manage methane you do not measure, and self-reported inventories miss super-emitters. Kayrros has written about Turkmenistan as a case where satellite evidence moved a government.

<https://carbonmapper.org/data>
<https://www.kayrros.com/blog/how-to-reduce-methane-emissions-using-satellite-monitoring/>

### GHGSat

Private constellation aimed at facility-scale methane. Sits in the “tip and cue” stack: Sentinel-5P or another wide sensor sees a regional anomaly, GHGSat or Tanager is tasked onto the facility.

### MethaneSAT

Philanthropic, EDF-backed. The State of EO 2026 survey says contact was lost in mid-2025. Included because it is a warning: a single science satellite is a fragile source, and a product that depends on it dies. Redundant public sensors (EMIT, Sentinel-5P) are the durable layer.

### Kayrros

Analytics company, not a constellation. Methane Watch uses Copernicus data and their own algorithms for oil and gas, coal, landfills, wastewater. They also do oil-storage and industrial activity analytics. The problem is independent verification of emissions for regulators and the UN. Methane Watch supported UNEP’s MARS program.

<https://methanewatch.kayrros.com/>

### Pixxel

India and U.S. Firefly constellation: about 5 m, 150+ bands, pitched at daily revisit. Buyer: agronomy (stress before the leaf turns yellow) and mining (alteration minerals, lithium clays). Early enough that a hackathon using Pixxel data will hit a commercial wall. The public analogue is EMIT for minerals and EnMAP / PRISMA where those archives are open.

### Wyvern, Kuva Space, Orbital Sidekick

Smaller hyperspectral plays (Dragonette, Kuva, the OSK pipeline monitor). Same buyer story: agriculture, mining, methane leaks along pipes. Treat as evidence that the niche is crowded, not as data sources for this weekend.

### Satellite Vu (SatVu)

Thermal infrared from orbit. Added to Copernicus Contributing Missions in June 2025 along with Marble Imaging, GEOSAT, ORUS, Unseenlabs, and Aerospacelab. Problem: heat leaks, industrial activity, night-time fires, building efficiency. Public stand-in is Landsat thermal, which is coarser and less frequent, and ECOSTRESS on the station.

### OroraTech

Thermal wildfire constellation. The 22 October 2026 ICEYE partnership is the clearest statement of the unsolved product problem: detection, fire-front tracking, and damage assessment still live in different systems. Public stand-in is NASA FIRMS (MODIS, VIIRS, Landsat), which is fast and noisy.

### Hydrosat, constellr

Thermal and land-surface temperature for agriculture and water stress. Public stand-in: Landsat surface temperature, Copernicus LST products that CDSE started onboarding in 2026.

## 4. Downstream analytics, the layer that actually matches the brief

These companies do not need to own a satellite. They own a workflow. They are the competitive set for a hackathon, because a judge who has seen a demo reel will pattern-match.

### Insurance and disaster

- **ICEYE** flood products, above. The buyer is a P&C insurer who needs depth, extent, and duration within hours, then a claims file.
- **Floodbase** (formerly Cloud to Street). Parametric flood insurance from satellites. Same problem, a different contract: pay when the pixel says water, not when an adjuster arrives.
- **Descartes Underwriting**. Parametric climate covers. Satellite triggers are one input among weather stations.
- Property imagery firms (**Cape Analytics, ZestyAI, Arturo**) lean on aerial and street-level imagery more than on orbit. Mentioned so a “roof damage” idea is not mistaken for an open satellite problem.

### Infrastructure and vegetation

- **LiveEO, Overstory, AiDash**. Trees versus power lines, pipeline encroachment, rail vegetation. The buyer is a utility that gets fined or burns if a tree hits a line. Radar and optical time series plus a work-order system. Very real, very sold.
- **Ursa Space**. SAR analytics for floods, commodities, and change, sold as a subscription rather than scenes.

### Commodities and industrial activity

- **Kayrros, SynMax, and the old Orbital Insight product**. Count cars, measure oil tanks, watch ports. Orbital Insight was bought by Privateer in May 2024 and folded toward Wayfinder / TerraScope. The classic “hedge fund satellite” pitch is a decade old and consolidated.
- **Gro Intelligence**. The cautionary death. Raised over $115 million, claimed a global climate and agriculture data platform, shut down in June 2024. AgFunder and later writeups point at the same failure: no single sticky use case, revenue that did not scale, a broad product that was everyone’s second screen. Assets reportedly went to Almanac. A hackathon crop-yield dashboard is walking into this graveyard.

<https://agfundernews.com/breaking-ag-insights-platform-gro-intelligence-is-closing-down>
<https://www.reuters.com/markets/deals/wozniaks-space-firm-privateer-buys-orbital-insight-raises-565-million-2024-05-06/>
<https://www.privateer.com/blog/welcome-to-the-crew-orbital-insight>

### Forests, carbon, nature

- **Pachama, Chloris, Sylvera, BeZero, NCX**. Forest carbon projects need a biomass number an auditor will accept. ESA Biomass (P-band, public data opened 26 January 2026) is the new public instrument aimed at the same physical quantity. The commercial problem is trust and additionality, not the existence of a green map. Easy to demo, hard to say something true.

### Maritime

- **Global Fishing Watch** is a nonprofit, not a startup, and it already fuses AIS with SAR vessel detections and publishes an API. Any “find illegal fishing” demo is a thin client of GFW unless it answers a question GFW’s map does not.
- HawkEye 360, Unseenlabs, ICEYE, and Spire sell the proprietary layer on top: RF plus tasking plus a coast-guard workflow.

### Marketplaces, the “access” startups

- **SkyFi**. Luke Fischer’s line in Payload: imagery is one piece of the puzzle. SkyFi is a storefront across providers so a person can task without seven contracts. The remaining problem is that a purchased scene is still a scene.
- **UP42** (Airbus). Workflows and third-party algorithms on top of a catalog.
- **SkyWatch, Astraea**. Discovery and delivery. Astraea’s historical pitch was “query the archive with a model.” That pitch is now table stakes for foundation-model demos.
- **Picterra**. User trains a detector on their own imagery. The problem is custom objects (tents, ponds, equipment) that no global model knows.

### Newsrooms

- **terrAIntel / Geoville**. Evidence packs with provenance, explicitly because journalists cannot run QGIS on deadline. This is the closest commercial statement of the hackathon-shaped product: a question in, a sourced answer out. It is also a warning that “chat with satellites for journalists” is a pitch someone is already writing white papers about.

## 5. Space domain awareness, a different dataset

Not Earth imagery. Included because the pack says “space,” and because October 2026 is when SpaceX itself made this the public problem. Company-level detail is in [03-voices-nasa-esa-spacex.md](03-voices-nasa-esa-spacex.md) and [07-problem-cards.md](07-problem-cards.md).

| Company | Problem they claim |
| --- | --- |
| LeoLabs | Radar catalog of LEO down to about 10 cm. Their CEO Tony Frazier: almost half of satellites expected by decade’s end will be operated by U.S. adversaries, “primarily China,” and managing the data is now harder than collecting it. |
| Slingshot Aerospace | Optical network, photometric fingerprints (RAPTOR, AFWERX). Objects are one pixel. Identity after a maneuver is the product. |
| Privateer | Fusion and visualization. Diana Klochkova: governments want air-traffic-control for space and do not have it, so commercial tools fill the gap. Also the new home of Orbital Insight. |
| Kayhan Space | Autonomous conjunction avoidance for operators. |
| Neuraspace | AI space-traffic management, Europe. |
| HEO Robotics | Pictures of other spacecraft, taken from space. Anomaly inspection, not Earth pictures. |
| Digantara, Aldoria (ex Share My Space), ExoAnalytic, NorthStar, Vyoma, Look Up Space | Regional SSA sensors and software. The list in the New Space Economy SSA survey is long, which is itself evidence of a crowded tools market on top of a public catalog that operators do not trust. |
| Astroscale, ClearSpace | Removal and servicing. ESA’s ClearSpace-1 is the public cousin. The problem (debris already up there) is agreed. The service is not a weekend software project. |

LeoLabs / Privateer quotes: <https://space4peace.org/managing-space-domain-awareness-data-has-become-a-greater-challenge-than-collecting-it/>

SSA company table: <https://newspaceeconomy.ca/2026/01/31/the-global-ecosystem-of-space-situational-awareness-and-traffic-management/>

## 6. What the startup map says about a student project

Patterns worth keeping:

- **The buyer with money is a government, an insurer, or a utility.** Agriculture was the 2018 pitch and the 2024 graveyard (Gro).
- **The product that survives is a workflow artifact**: a flood polygon in the claims system, a tree ticket for a crew, a plume attached to a facility, a conjunction message to an operator. It is not a map for its own sake.
- **Public data already covers the medium-resolution world.** Startups win on resolution, revisit, weather independence, spectral specialty, or integration. A hackathon using Sentinel, Landsat, EMIT, FIRMS, or NISAR wins only if the last mile is the product.
- **“Chat with imagery” is in the air** (terrAIntel, SkyFi, Astraea, foundation models inside ArcGIS). The version that is still open is a narrow question with a source trail, on data so new or so awkward that the incumbents have not productized it. NISAR’s first public summer, EMIT’s 16 October 2026 reprocessing, and SpaceX’s October ephemeris complaint are the three freshest openings.
