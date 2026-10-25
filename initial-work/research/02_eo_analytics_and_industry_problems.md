# EO downstream analytics, platforms, and the industry's own discussion of its problems

**Scope.** Companies and organisations that turn satellite / Earth-observation (EO) data into insight — analytics firms, platforms and marketplaces, climate and nature monitors, insurance and finance users, defence and intelligence buyers, non-profit open monitors, and LLM / agentic geospatial products — plus the industry's own discussion of its problems (analysts, newsletters, trade press, conferences, forums) and the recurring pain-point themes. Prepared for the Cal Hacks 13.0 "Make it Legendary" space challenge: the aim is to surface clear, real problems that a two-person team could attack in 36 hours with large public space / EO datasets.

**Researched on 2026-10-24.**

**How to read an entry.** Fields used where they apply: *What it is · Problems / pain points (with short quotes) · How they're trying to solve it · Data · Off-the-shelf tech · Hackathon angle · Credibility · Sources (with dates)*. Credibility labels: *official* (company / agency primary page, filing, press release), *peer-reviewed*, *reputable press*, *trade press*, *analyst newsletter / blog*, *vendor blog* (self-interested), *social post / forum*, *rumor / unverified*. Claims seen only in a search-result snippet, a secondary aggregator or a mirror are marked as such ("not opened", "unverified", "via …"). Vendor performance numbers are vendor claims unless stated otherwise.

**Research limits.** Reddit could not be fetched from the research environment; Quilty, Novaspace, NSR/Analysys Mason and TerraWatch Premium reports are paywalled (only public excerpts and second-hand figures are used); several sites returned 403/429 (SpaceNews, Geospatial World, GeekWire, Reuters); search access was rate-limited partway through, so many later items were gathered by opening primary pages directly. See "Leads not followed" at the end.

**2026 context that shapes many entries** (details and sources in the entries):
- A US–Israel war with Iran began on 28 Feb 2026; Planet first delayed and then, on 4 Apr 2026, indefinitely withheld imagery of Iran and the Gulf at a US government request, and other providers tightened access ([Al Jazeera, 5 Apr 2026](https://aljazeera.com/news/2026/4/5/us-satellite-firm-planet-labs-announces-blackout-on-war-on-iran-images)). Open Copernicus data (e.g., Bellingcat's Sentinel-1 damage map) became the fallback ([Bellingcat, 7 Apr 2026](https://www.bellingcat.com/resources/2026/04/07/tool-damage-assessment-destruction-sentinel-satellite-imagery-iran-us-gulf/)).
- GNSS jamming and "dark" transits made AIS evidence unreliable at sea — Windward estimates 124,235 vessels affected in Q3 2026 ([Windward, 20 Oct 2026](https://windward.ai/blog/how-marine-insurers-are-closing-the-evidence-gap/)).
- The EU Deforestation Regulation applies from 30 Dec 2026 for large companies ([WRI, 6 Oct 2026](https://www.wri.org/insights/eu-deforestation-footprint-eudr)).
- The FY2027 NASA request cuts Earth science by 52% and proposes "one final Landsat satellite" ([TerraWatch, 13 Apr 2026](https://newsletter.terrawatchspace.com/earth-observation-essentials-april-13-2026/)).
- Defence, intelligence and civil government are cited as 70–80% of EO revenue ([New Space Economy, 23 Oct 2026](https://newspaceeconomy.ca/2026/10/23/why-does-defense-dominate-earth-observation-demand-over-commercial-markets/), citing TerraWatch), and standalone analytics firms keep being acquired or shut (Orbital Insight, Descartes Labs, UP42, Kayrros, Pachama, Cape Analytics, AiDASH, Gro Intelligence — see entries; TerraWatch counts >30 EO acquisitions since 2022, [11 Aug 2026](https://newsletter.terrawatchspace.com/earth-observation-essentials-august-11-2026/)).
- Google's AlphaEarth-based embeddings and agentic "Earth AI" tools are framed by TerraWatch as an "existential change" for vendors selling feature extraction and change detection ([TerraWatch, 12 Oct 2026](https://newsletter.terrawatchspace.com/earth-observation-essentials-october-12-2026/)).

**Contents**
- Part A.1 — Analytics companies, platforms and marketplaces
- Part A.2 — Climate, nature, carbon, insurance and agriculture analytics
- Part A.3 — Defence and intelligence demand (and defence analytics tooling)
- Part A.4 — Non-profits, open monitors and open-data OSINT
- Part A.5 — LLM / agentic geospatial products and tooling
- Part B.1 — Analysts, newsletters and essayists
- Part B.2 — Market-research firms
- Part B.3 — Trade press, op-eds and executive commentary
- Part B.4 — Conferences and community events
- Part B.5 — Forums and social discussion
- Part B.6 — Recurring problem themes (with evidence)
- Problem bank
- Shortlist: problems that best fit a 36-hour build
- Cross-slice leads
- Leads not followed

---

## Part A.1 — Analytics companies, platforms and marketplaces

Who turns pixels into answers for commercial and government buyers, what happened to them in 2024–2026, and what they say their customers' problems are.

### Orbital Insight → Privateer (2024)
- **What it is:** Orbital Insight was one of the first "geospatial analytics" startups (TerraScope platform: counting cars, oil tanks, ships, foot traffic from imagery and location data). Bought by Privateer, the space-situational-awareness startup co-founded by Steve Wozniak, announced 6 May 2024; TerraScope to be combined with Privateer's Wayfinder (a near-real-time visualisation of satellites/debris).
- **Problems / pain points:** A once heavily-funded pure-analytics company ended up absorbed by a different-sector startup, with financial terms undisclosed — a data point for the "analytics alone is a hard business" thesis (see Joe Morrison entries below). Customers listed included the US Air Force, NGA, DIU, Dow Jones, Mitsubishi and S&P Global.
- **How they're trying to solve it:** Privateer pitches combining "objects in space" with "activity on Earth" in one data engine; raised a $56.5M Series A alongside the deal (led by Aero X Ventures, with Lux Capital, BOKA Group, Starburst, the Winklevoss twins).
- **Data:** Commercial imagery (multiple vendors), AIS, geolocation / mobile-phone pings (historically), plus Privateer's orbital catalogue.
- **What it became (Privateer homepage, Oct 2026):** the brand survives as *TerraScope Maritime* ("global vessel tracking" with anomaly detection) inside Privateer's *Elements* all-domain fusion platform (land, sea, air, space, cyber; vessel tracking, GNSS-interference detection, space domain awareness) fed by a "Taskable Satellite Network"; headlines: partnership with Lloyd's List Intelligence, U.S.–Saudi and Gulf geospatial engagements, Moriba Jah AMOS 2026 best paper. I.e., the pioneer of "satellite analytics for finance/retail" now sells maritime and defence fusion.
- **Hackathon angle:** "Orbital Insight in a weekend" for one narrow indicator — e.g., counting vehicles in parking lots or oil-tank fill levels from free Sentinel-2 / NAIP and showing whether the signal actually predicts anything (most of these signals were never validated publicly).
- **Credibility:** Trade press.
- **Sources:** [privateer.com](https://www.privateer.com/); [Via Satellite, 8 May 2024](https://www.satellitetoday.com/finance/2024/05/08/steve-wozniaks-privateer-acquires-orbital-insight/); [SpaceNews, May 2024](https://spacenews.com/acquires-orbital-insight/); [Pulse 2.0](https://pulse2.com/privateer-raises-56-5-million-and-acquires-orbital-insight/).

---

### Descartes Labs → EarthDaily Analytics (Oct 2024)
- **What it is:** Descartes Labs (spun out of Los Alamos, 2014) built a geospatial "data refinery" / cloud platform; acquired with its government subsidiary by EarthDaily Analytics (EDA), announced 15 Oct 2024. Both were owned by private-equity firm Antarctica Capital. Products named: Marigold, Iris, Ascend (commercial), Retina and Wayfinder (US government). EDA's own EarthDaily Constellation was "set to launch in 2025".
- **Problems / pain points:** A famous platform company folded into a vertically integrated data+analytics firm — another "platforms don't stand alone" data point. Combined company's segments: insurance, energy, mining, US defence & intelligence.
- **How they're trying to solve it:** Backward integration — owning a constellation to get differentiated data (TerraWatch calls EarthDaily part of the "backward integration" wave where satellites are "enablers, not products").
- **Hackathon angle:** see the TerraWatch / Joe Morrison entries — a "one vertical, one answer" product beats a generic platform.
- **Credibility:** Official press release + trade press.
- **Sources:** [EarthDaily press release](https://earthdaily.com/descartes-labs-acquisition/); [Via Satellite, 15 Oct 2024](https://www.satellitetoday.com/imagery-and-sensing/2024/10/15/earthdaily-acquires-descartes-labs/); [Geo Week News, 17 Oct 2024](https://www.geoweeknews.com/news/earthdaily-analytics-announces-acquisition-of-descartes-labs); [TerraWatch State of Commercial EO 2025, 22 Oct 2025](https://newsletter.terrawatchspace.com/state-of-commercial-earth-observation-2025-edition/).

---

### Ursa Space Systems
- **What it is:** Ithaca, NY (founded 2014) "satellite intelligence" company, SAR-first; catalogue of "over fifty million SAR images"; focuses on change detection and monitoring (e.g., oil-storage fill levels via floating-roof tanks, maritime). Sells to energy, finance, insurance and government. CEO Adam Maher.
- **2025–2026 news:** Aug 2025 undisclosed investment from Sumitomo Corporation of America, which plans to commercialise Ursa's solutions via proofs of concept with end users. Earlier: NEC collaboration (Jun 2024), ICEYE and Umbra partnerships for SAR supply.
- **Positioning today (ursaspace.com, Oct 2026):** now a "geospatial AI company" that "fuse[s] multi-modal data"; its GeoAI "breaks a question into measurable indicators and returns a verified insights report"; 70+ commercial satellite/data sources, 10 years of archive; Custom Monitoring + Data Subscriptions; dark-vessel and ship-to-ship transfer detection; oil-storage insight; tip-and-cue collection model; NGA and US Space Force work.
- **Problems / pain points:** SAR is hard for non-experts to interpret; Ursa's business is essentially being a multi-vendor SAR broker + analyst layer (the "imagery-to-insight gap").
- **Hackathon angle:** Global oil-storage inventory estimate from free Sentinel-1 SAR (floating-roof tank shadows) is a classic Ursa product that can be partially reproduced with open data.
- **Credibility:** Official (Sumitomo release) + data aggregator (Preqin) + trade press.
- **Sources:** [ursaspace.com](https://ursaspace.com/); [Sumitomo Corp, 20 Aug 2025](https://www.sumitomocorp.com/en/jp/news/topics/2025/group/20250820); [Preqin profile](https://www.preqin.com/data/profile/asset/ursa-space-systems-inc-/257081); [Defense Daily — Ursa/ICEYE partnership](https://defensedaily.com/press-releases/ursa-and-iceye-extend-partnership-for-sar-satellite-data-and-products).

---

### SkyWatch (EarthCache → SkyWatch HUB)
- **What it is:** Waterloo, Canada imagery-access company. Its EarthCache API let developers buy imagery from many providers.
- **Problems / pain points:** Pivot away from "API for other app builders" because many customers turned out to be imagery end-users "who lacked the resources to build on the EarthCache API" (SpaceQ). This is direct evidence of the last-mile problem: an API is not a product for most buyers.
- **How they're trying to solve it:** Rebuilt EarthCache Enterprise as "SkyWatch HUB", an end-user platform from seven core services (announced at INTERGEO; exact year not shown in the result — unverified). Homepage (Oct 2026) now lists five products — EXPLORE (search/buy optical, radar, aerial with prices "shown up front"), HUB (org-wide procurement, storage, payment, sharing), MAP (into ArcGIS/GIS), BUILD (API to "400+ data providers", usage-billed, no bulk commitments), CONNECT (lets operators distribute archives and tasking, handling commerce, licensing, delivery); claims 150K+ users and coverage of "95% of commercial imaging satellites".
- **Credibility:** Trade press (SpaceQ) + official homepage.
- **Sources:** [skywatch.com](https://skywatch.com/); [SpaceQ — SkyWatch HUB](https://spaceq.ca/skywatch-unveils-full-enterprise-version-of-skywatch-hub/); [SpaceQ EarthCache tag](https://spaceq.ca/tag/earthcache/).

---

### UP42 (Airbus → Neo Space Group, 2025)
- **What it is:** Berlin-based EO marketplace/platform giving access to data and analytics from 80+ geospatial companies. Sold by Airbus Defence and Space to Neo Space Group (NSG), owned by Saudi Arabia's Public Investment Fund; announced Dec 2024, completed 10 Jul 2025. NSG had earlier bought Taqnia ETS.
- **Problems / pain points:** Even an Airbus-backed marketplace was divested — consistent with Morrison's "Stop building satellite imagery platforms and marketplaces" thesis (UP42 is named there).
- **How they're trying to solve it:** Sovereign-buyer backing (Gulf states building national EO capability); UP42 Enterprise with cost-centre budget caps and spend limits.
- **UP42 "State of Earth observation in 2026" survey (Kevin Enright, 31 Jul 2026; n = 124 professionals, 5-week survey):** 83% call EO data "mission-critical"; "92% of companies are already using or planning to use AI in their workflows"; "Multi-sensor data usage in 2026 is the norm"; the main buyer pain point "shifted from cost and data quality a few years ago to the buying process itself" — "Budget approval, unclear pricing, and licensing cause headaches for teams and companies." (Small, vendor-run survey.)
- **UP42 "Why buy EO data through a platform…? Part 1" (10 Sep 2026):** direct buying means per-provider onboarding, legal review, security assessment, procurement and invoicing; commercial terms vary "by provider, collection, order type, licensing terms, and committed volume"; minimum order sizes, minimum commitments, prepaid credits; tasking "can be rejected for capacity, lead time, geometry, restrictions, or competing priorities"; "Tasking introduces more uncertainty." "Even a feasible request doesn't always result in a successful acquisition." "There's also a cost attached to delay."
- **Credibility:** Official press release + trade press; vendor blog/survey.
- **Sources:** [UP42 — State of EO in 2026, 31 Jul 2026](https://up42.com/blog/state-of-earth-observation-in-2026); [UP42 — Buy through a platform? Part 1, 10 Sep 2026](https://up42.com/blog/buy-eo-through-platform-directly-part-1); [UP42 blog](https://up42.com/blog); [Military Aerospace](https://www.militaryaerospace.com/communications/article/55302818/neo-space-group-acquires-geospatial-firm-up42-from-airbus); [Cision/AAP release, 10 Jul 2025](https://www.aap.com.au/aapreleases/cision20250710ae19641); [Space Insider, 3 Dec 2024](https://spaceinsider.tech/2024/12/03/neo-space-group-set-to-expand-geospatial-capabilities-with-acquisition-of-up42-from-airbus).

---

### Arlula
- **What it is:** Sydney (founded 2018) imagery marketplace API: archive search, future-capture (tasking) opportunities, ordering, download, from multiple suppliers. Python package `arlulacore`/`arlulaapi`. Geospatial World reported a 1 km² minimum-order product "for as little as $10" (article date not shown — unverified date).
- **Pivot (arlula.com, Oct 2026):** now sells "Geostack", six modular back-office components for *operators and resellers* — Sales Engine (discover, price, quote, bill, entitlements), Data Normalisation Pipeline, Automation Workflows, Fulfilment Engine (standardised ordering/delivery across commercial and national providers, incl. tasking), Advanced Data Management, Constellation Orchestration (capture schedules, capacity conflicts); promotes a webinar on "scaling an EO business". I.e., the buyer-facing marketplace has become white-label infrastructure for suppliers (compare SkyWatch CONNECT).
- **Problems / pain points:** Minimum order sizes and per-km² pricing are a barrier for small users — Arlula's original pitch was lowering them; the pivot suggests buyer-side marketplace volume was insufficient (inference, not stated by Arlula).
- **Hackathon angle:** A "what does it cost to answer my question?" calculator comparing free (Sentinel/Landsat) vs paid archive options for a user's AOI.
- **Credibility:** Directory listings + trade press.
- **Sources:** [arlula.com](https://www.arlula.com/); [Geospatial World — Arlula cuts cost 25x](https://geospatialworld.net/news/australian-startup-arlula-drives-down-the-cost-of-satellite-images-by-25x); [PyPI arlulaapi](https://pypi.org/project/arlulaapi/1.2.2); [API Evangelist](https://providers.apievangelist.com/providers/arlula/).

---

### SkyFi (consumer/prosumer imagery marketplace with an AI "navigator")
- **What it is:** Marketplace covering "40+ providers" (military page says "150+ satellite sources"): archive images "from $15", tasking "from $200", analytics (object detection, hyperspectral signature analysis, commodity stockpile measurement "from $5"), free open data, maritime AIS with dark-ship detection, ATAK plugin, and direct portals for Vantor, ICEYE US, Planet Select (SkySat tasking/archive). Named partners: Vantor, Planet, ICEYE US, Umbra, Satellogic, Vexcel, Satim, OroraTech, Kpler, Ursa, GEOSAT, Pixxel. "Rowan" is "your AI navigator for Earth observation" to find, compare and order imagery. "No contracts required", "low minimum order sizes" (no per-km² figure shown).
- **Problems / pain points:** The marketplace exists because procurement is painful (see Morrison); SkyFi imagery of the 2026 Iran war entered public circulation (per a GlobalSecurity summary in search results) while Planet withheld.
- **2026 news:** SkyFi raised $12.7M (TerraWatch H1 2026 review, 27 Jul 2026); BlackSky imagery sold to retail investors via SkyFi on Robinhood (see Defence section, BlackSky Spectra entry).
- **Hackathon angle:** "Should I buy this image?" assistant — given a question and AOI, decide whether free Sentinel-1/2 suffices or a $15 archive image / $200 tasking is needed, and estimate the value of the extra resolution.
- **Credibility:** Official homepage.
- **Sources:** [skyfi.com](https://skyfi.com/); [TerraWatch H1 2026 Review, 27 Jul 2026](https://newsletter.terrawatchspace.com/earth-observation-h1-2026-review/).

---

### Danti
- **What it is:** Atlanta startup building an AI-powered "search engine for Earth data" (natural-language search across imagery, news, and other geospatial sources). Pre-seed $2.75M (Tech Square Ventures, Radius Capital); later round led by Shield Capital bringing total to ~$5M; US Space Force SBIR Phase II ($1.2M); announced US military customers.
- **Product today (danti.ai, Oct 2026):** plain-language questions answered "in seconds" by fusing imagery, news, social media, shipping data and the customer's own data; web or on-prem; main market defence & intelligence (lets users reach data without "making special requests to geospatial analysts or partners"; novices search "with the skill of experts with decades of experience" — vendor claims, no measurements), plus property/insurtech and infrastructure; NGA award logo.
- **Problems / pain points:** Analysts can't find relevant data across fragmented catalogs; search is keyword/AOI-based rather than question-based; non-analysts must queue requests to scarce GEOINT analysts.
- **Hackathon angle:** Natural-language → STAC search over Earth Search / Planetary Computer catalogs (a "Danti-lite").
- **Credibility:** Trade press (Payload, SpaceNews).
- **Sources:** [danti.ai](https://www.danti.ai/); [Payload — Danti emerges from stealth](https://payloadspace.com/danti-emerges-from-stealth-with-2-75m-pre-seed-round/); [Payload — Danti raises $5M, announces US military customers](https://payloadspace.com/danti-raises-5m-announces-us-military-customers); [SpaceNews](https://spacenews.com/?p=196075).

---

### Synthetaic → RAIC Labs (RAIC = Rapid Automatic Image Categorization)
- **What it is:** Delafield, Wisconsin company (founded 2019 by Corey Jaskolski) whose RAIC tool does few-shot / unsupervised object search over huge imagery collections (find "more things like this"); described as "ChatGPT for satellite imagery". Rebranded RAIC Labs (date not given). $15M Series B (Feb 2024; TitletownTech, Lupa Systems). Partnerships with Planet (May 2023) and Microsoft (Aug 2023; Pegasus Program, 1M Azure GPU hours). Found the Feb 2023 Chinese surveillance balloon in archival Planet data and traced it to its launch site (NYT credited it with coordinates at twelve points); for CNN detected >500 craters over 12 m (Wikipedia says "123 meters" — likely a transcription issue; unverified) for a Dec 2023 report on 2,000-lb bombs in Gaza. Website (Oct 2026): "Index once. Exploit repeatedly" — embeddings computed once, then searched repeatedly on CPUs; multi-sensor; analyst-directed search "without training and deploying a new model"; testimonial: what "used to be a multi-month process" became "a rapid pipeline"; markets: defence & intelligence, public safety/municipal, commercial GEOINT; testimonials from UN WFP, National Geographic Society, GenLogs.
- **Problems / pain points:** Labelling cost: traditional CV "requires collecting, labeling, and training data, which … must often restart as missions change"; RAIC pitches search without labelled training sets. On the balloon: "We don't have any labels. We don't know what it looks like from space." (Jaskolski); goal of processing Planet's entire daily imagery in under 24 hours; an NGA spokesperson (2023): "We see a future where these models can be trained with big spatial data to answer questions in space and time." (Defense One via GovTech, 18 Apr 2023).
- **Hackathon angle:** Few-shot "find all X" over a Sentinel-2/NAIP tile using an open embedding model (e.g., Clay, SatCLIP, AlphaEarth embeddings) — the open-source analogue of RAIC.
- **Credibility:** Wikipedia + local business press; partly promotional.
- **Sources:** [raiclabs.com](https://raiclabs.com/); [GovTech / Defense One — "ChatGPT-style tool for satellite photos already exists", 18 Apr 2023](https://www.govtech.com/products/chatgpt-style-tool-for-satellite-photos-already-exists); [Wikipedia — RAIC Labs](https://en.wikipedia.org/wiki/RAIC_Labs); [BizTimes — $15M Series B](https://biztimes.com/delafield-based-synthetaic-completes-15-million-series-b-funding-round/?amp=1).

---

### Picterra
- **What it is:** Lausanne GeoAI platform (Forge, Tracer, Accelerate) for no-code object/change detection on satellite and drone imagery; integrates with ArcGIS, QGIS, FME. Pivoted to supply-chain compliance: *Picterra Tracer* (Nov 2024) for plot monitoring, reporting and verification; Planet partnership (Dec 2024); Google Cloud Marketplace (May 2025); INPA MoU (Sep 2026); posts on EUDR delay, "What makes compliance evidence truly defensible", "Ending sustainability's trust crisis", and testing Brazil's 2026 coffee crop forecast (CONAB) against satellite data.
- **Problems / pain points:** "unprecedented influx" of geospatial data; trust crisis in corporate sustainability claims; compliance evidence must be defensible.
- **Hackathon angle:** EUDR plot checker (see GNW entry) — Picterra's pivot is market evidence it is a real buyer need.
- **Credibility:** Company blog.
- **Sources:** [Picterra blog](https://picterra.ai/blog/).

---

### Blackshark.ai
- **What it is:** Austrian company that "make[s] the world machine-readable": global 3D terrain/buildings/infrastructure from satellite and aerial imagery for simulation, autonomy and AI; products HUNTR and REPLIKA; tactical edge / on-prem / secure cloud deployment (defence).
- **Credibility:** Official homepage (news page had no items).
- **Sources:** [blackshark.ai](https://blackshark.ai/news/).

---

### Planet Insights Platform (Planet + Sentinel Hub)
- **What it is:** Planet acquired Sinergise's Sentinel Hub (2023) and announced Planet Insights Platform on 9 Apr 2024 — one login for Planet data plus Sentinel Hub cloud processing, Analysis-Ready PlanetScope ("harmonized, cloud-masked, and spatially consistent daily stacks"), weekly Road & Building Change Detection, Field Boundaries.
- **2025–2026 change:** Sentinel Hub's popular free *EO Browser* now shows "EO Browser has been deprecated. Please move your workflows to the new and improved Planet Insights Platform." and "To continue to use only public data please use the Copernicus Browser" (no end date shown, checked Oct 2026). The sentinel-hub.com homepage says the service runs "on top of Planet Insights Platform" and offers a 30-day free API trial. Net effect: a widely used free public-data viewer has been folded into a commercial platform, pushing public-data users to ESA's Copernicus Browser.
- **Problems / pain points:** Users struggle to turn daily imagery into analysis-ready time series; Planet's answer is pre-harmonised ARD + derived "Planetary Variables". Free-tier tools disappear when acquired (EO Browser deprecation; NICFI end — see Global Nature Watch entry).
- **Credibility:** Official.
- **Sources:** [EO Browser deprecation notice](https://apps.sentinel-hub.com/eo-browser/); [sentinel-hub.com](https://www.sentinel-hub.com/); [Business Wire, 9 Apr 2024](https://businesswire.com/news/home/20240409550189/en/Planet-Announces-Planet-Insights-Platform-with-Powerful-Tooling-for-Unlocking-Earth-Observation-Data); [Planet Pulse](https://www.planet.com/pulse/planet-insights-platform/); [Geo Week News](https://www.geoweeknews.com/articles/planet-insights-platform-satellite-imagery-earth-observation-ai-analytics/).

---

### Planet's own 2026 positioning (Planet Pulse)
- **What it is:** Recent Planet posts that articulate industry problems from a data supplier's view:
  - *"Why Dense Satellite Time Series Deliver More Trustworthy Insight"* (22 Oct 2026): sparse imagery "can't tell you if what you're seeing is typical, unusual, just starting, or nearly finished"; "Nearly two-thirds of the planet is under cloud at any moment"; "A nominal eight-day revisit can easily turn into a clear view every month or two, landing at unpredictable times"; a single scene can't distinguish a real disturbance from a cloud shadow (→ change-detection false positives). Cites Tuscany forest alerts at 86% user's / 92% producer's accuracy.
  - *"Beyond the Soda Straw: Why Modern Defense Needs Continual GEOINT"* (29 Sep 2026): high-res imagery "capture[s] just a tiny patch of ground at a time", is tasked only after another source raises an alarm, and its predictable passes let adversaries time activity around gaps (Antelope Reef); argues for an "un-spoofable baseline of reality" with daily wide-area scans tipping SkySat (tip-and-cue).
  - *"Introducing Populace"* (12 Oct 2026): quarterly ~40 m global population map from Planet basemaps + Microsoft AI for Good building detection + IHME modelling; free for non-profits/academics, commercial for governments, development banks, insurers; problem: censuses are expensive, infrequent and undercount fast-growing cities, conflict and disaster zones ("We cannot address risks we cannot see" — Christopher Murray, IHME).
  - Others: Tanager-2 first light (20 Oct 2026), USGS independent evaluation of Tanager (10 Sep 2026), Amazon.ia biodiversity intelligence (24 Sep 2026), persistent marine monitoring (3 Sep 2026), Slovenia automated disaster infrastructure (13 Oct 2026).
- **Credibility:** Official company blog (promotional).
- **Sources:** [Dense time series, 22 Oct 2026](https://www.planet.com/pulse/why-dense-satellite-time-series-deliver-more-trustworthy-insight/); [Beyond the Soda Straw, 29 Sep 2026](https://www.planet.com/pulse/beyond-the-soda-straw-why-modern-defense-needs-continual-geoint/); [Introducing Populace, 12 Oct 2026](https://www.planet.com/pulse/introducing-populace-mapping-humanity-in-unprecedented-detail/); [Planet Pulse index](https://www.planet.com/pulse/).

---

### Kpler acquires Spire Maritime (closed 25 Apr 2025)
- **What it is:** Commodity/maritime intelligence firm Kpler completed the purchase of Spire Global's maritime (satellite-AIS) business; reported value ~$241M ($233.5M price + $7.5M one-year services agreement). Spire had sued Kpler in Delaware over the delayed close and warned it might not otherwise repay debt; UK CMA review meant both ran independently pending review (per WorldPorts; single source for the lawsuit detail).
- **Problems / pain points:** Satellite-AIS data on its own was not a sustainable standalone business for an EO/data operator; value accrues to the analytics/trade-flow layer.
- **Credibility:** Official (Kpler) + trade press.
- **Sources:** [Kpler, 25 Apr 2025](https://kpler.com/blog/kpler-completes-acquisition-of-spire-maritime-strengthening-maritime-intelligence-capabilities); [WorldPorts](https://www.worldports.org/kpler-completes-acquisition-of-spire-maritime); [Ship Technology](https://www.ship-technology.com/newsletters/kpler-acquisition-spire-maritime).

---

### SpaceKnow
- **What it is:** Czech/US analytics firm (Guardian platform) — multi-provider imagery + AI change alerts for defence & intelligence and construction monitoring; once known for satellite-based economic indices (China lockdowns, retail, inflation — press mentions c. 2022); partners ESA, Planet, ICEYE, Satellogic, Deloitte; case studies on Dubai 2024 floods and Russian LNG.
- **Problems / pain points:** Pivot from "satellite macro indices for investors" to defence — another example of commercial-finance demand not holding (the "alt-data" hype of 2017–2021).
- **Credibility:** Official homepage.
- **Sources:** [spaceknow.com](https://www.spaceknow.com/).

---

### Wherobots (spatial lakehouse + RasterFlow)
- **What it is:** Cloud spatial SQL/raster platform (Apache Sedona creators). RasterFlow public preview (15 Sep 2026) for vision-language and custom-model inference at planetary scale with "costs predictable"; examples: AI-assisted vessel counts at Yulin Naval Base with SAM3 (12 Oct 2026); utility vegetation management with NAIP + Meta canopy height (14 Oct 2026); QGIS plugin; NVIDIA and HERE partnerships.
- **Problems / pain points:** Cost and unpredictability of running models over large imagery; analysts work in QGIS, not notebooks.
- **Credibility:** Company blog.
- **Sources:** [Wherobots blog](https://wherobots.com/blog/).

---

### Xoople ("Earth's System of Record")
- **What it is:** Spanish startup aiming to make Earth a "consumable API" for AI; claims to close "the physical-world knowledge gap that costs enterprises and governments billions a year"; partners Esri, Microsoft, EY; GMV, KSAT, VITO; funded by Spain's CDTI INNVIERTE. TerraWatch (Apr 2026) reported a $130M Series B and an L3Harris sensor contract, and noted its distribution-first strategy via Microsoft/Esri ("they laid the distribution pipes before having their own data supply"). Building on Microsoft Planetary Computer Pro.
- **Problems / pain points:** Distribution, not sensors, is the bottleneck — Xoople's strategy is an explicit bet on that thesis.
- **Credibility:** Official homepage + analyst newsletter.
- **Sources:** [xoople.com](https://www.xoople.com/); [TerraWatch EO Essentials 13 Apr 2026](https://newsletter.terrawatchspace.com/earth-observation-essentials-april-13-2026/); [Azure blog, 17 Jun 2025](https://azure.microsoft.com/en-us/blog/microsoft-planetary-computer-pro-unlocking-ai-powered-geospatial-insights-for-enterprises-across-industries/).

---

### Impact Observatory
- **What it is:** AI land-cover company (known for the Esri 10 m annual global LULC maps): IO Monitor 3 m and 10 m land cover with change monitoring, IO Maps for Good (open annual maps), Geospatial Sidekick, IO Store; defence, disaster response, urban planning, food security. Produced a global land-use/land-cover map "in less than a week" on 1,000 Azure VMs (Microsoft, Jun 2025).
- **Credibility:** Official.
- **Sources:** [impactobservatory.com](https://www.impactobservatory.com/); [Azure blog, 17 Jun 2025](https://azure.microsoft.com/en-us/blog/microsoft-planetary-computer-pro-unlocking-ai-powered-geospatial-insights-for-enterprises-across-industries/).

---

### AiDash (utility vegetation management, wildfire and storm risk)
- **What it is:** Satellite-based software for utilities: IVMS (risk-based vegetation management), CRIS Wildfire and Storm (120-hour storm-outage prediction and crew pre-positioning), AIMS (asset monitoring), biodiversity net gain; "Trusted by 200+ customers globally".
- **2026 news:** TerraWatch's M&A tally (11 Aug 2026) lists *Schneider Electric buying AiDASH* (~$350M implied EV) — another standalone EO-analytics firm absorbed into a domain incumbent's workflow (see the TerraWatch 2026 entry in Part B).
- **Problems / pain points:** Vegetation contact is a top cause of outages and ignitions — AiDash cites "70% of wildfire ignitions involve vegetation or asset contact with surface fuel" (customer survey), insured wildfire losses ">$100B since 2017" (Statista), repair after failure ~6× more costly than prevention (NIBS). Utilities trim on fixed cycles ("miles cut") instead of risk.
- **Data:** Multispectral satellite imagery, canopy height, weather, utility GIS.
- **Hackathon angle:** **Line-strike risk map** — open canopy-height model (Meta/WRI 1 m) + NAIP/Sentinel-2 + OpenStreetMap power lines + FIRMS fire history + wind forecasts → rank spans to trim first. Wherobots demonstrated the same with NAIP + Meta's canopy height model in King and Shasta counties (Oct 2026), proving open data suffices.
- **Credibility:** Official homepage (vendor claims).
- **Sources:** [aidash.com](https://www.aidash.com/); [Wherobots blog index (UVM post, 14 Oct 2026)](https://wherobots.com/blog/); [TerraWatch Essentials 11 Aug 2026](https://newsletter.terrawatchspace.com/earth-observation-essentials-august-11-2026/).

---

### ASTERRA (ex-Utilis) — satellite leak detection for water utilities
- **What it is:** Polarimetric SAR + AI to find subsurface moisture → potable-water leak detection (Recover), pipe condition (MasterPlan), soil-moisture maps for dams, levees, roads, rail, mining (EarthWorks); EO Discover 2.0 platform; inaugural AWWA Innovation Award; AWWA Opflow case study with Henry County PSA (Virginia); referenced in a California Energy Commission report.
- **Problems / pain points:** Utilities lose treated water to leaks they cannot see; acoustic surveys are slow. (No quantified results on the page — vendor.)
- **Hackathon angle:** Harder with open data (needs L-band PolSAR); NISAR L-band data (provisional release Jul 2026, per New Space Economy) could make an open version possible — flag as stretch.
- **Credibility:** Official homepage.
- **Sources:** [asterra.io](https://asterra.io/).

---

### Satelytics (pipelines, methane, water quality)
- **What it is:** Multispectral/infrared satellite analytics for oil and gas, pipelines, utilities, water, mining, agriculture; "remote sensing scientists verify alerts before clients receive them" (i.e., humans in the loop to suppress false positives). Testimonials: Duke Energy, BP, Marathon Pipe Line, Accenture, Ramboll. Vendor claims: utilities cut methane leaks 85%, vegetation-related outages −40%. Oct 2026 posts: "Your Insurance File Is Stuck in the Past", "The Fence Line Is Not the Risk Line".
- **Problems / pain points:** False alerts — the business model includes manual verification; pipelines' own SCADA misses small leaks ("Seeing What Pipelines Can't Tell You").
- **Credibility:** Official homepage (vendor claims, unaudited).
- **Sources:** [satelytics.ai](http://www.satelytics.ai/).

---

## Part A.2 — Climate, nature, carbon, insurance and agriculture analytics

Downstream EO for methane, flood and parametric insurance, carbon credits, deforestation regulation (EUDR), property risk and farm MRV. Many entries document acquisitions, shutdowns and pivots.

### Kayrros (Paris), now owned by Energy Aspects

- **What it is:** Satellite and geospatial analytics for energy, methane, supply chains, physical risk and nature. It turns "raw data from more than 20 satellite constellations into insights" on energy, supply chains, physical risk, nature and the environment ([Energy Aspects / Kayrros press release, 12 Mar 2026](https://www.kayrros.com/press_release/energy-aspects-to-acquire-kayrros/)). Products include Methane Watch, billed as the "first global platform made available commercially to private players to systematically track large methane emissions" ([Kayrros Methane Watch page, undated](https://www.kayrros.com/methane-watch/)). It also sells a methane disclosure product for corporates that detects super-emitters "using up to three different satellites in near realtime with an average two-day lag" ([Kayrros product page, undated](https://www.kayrros.com/products/methane-emissions-disclosure-for-corporates/)).
- **2025–2026 news:**
  - Energy Aspects, an energy market intelligence firm, agreed to buy Kayrros on 12 Mar 2026 and completed the deal on 21 May 2026. Terms were not disclosed ([Kayrros press release, completion](https://kayrros.com/press_release/energy-aspects-completes-acquisition-of-kayrros/); [tech.eu, 13 Mar 2026](https://tech.eu/2026/03/13/energy-aspects-to-buy-paris-based-kayrros-to-add-satellite-and-geospatial-analytics-capabilities/); [Carbon Pulse](https://carbon-pulse.com/492521/)).
  - The deal follows Energy Aspects' earlier purchases of OilX, INAS and TankWatch ([Energy Aspects insight](https://www.energyaspects.com/resources/insights/energy-aspects-to-acquire-satellite-data-and-analytics-company-kayrros)).
  - Reading: a flagship EO analytics firm ends up as a feature inside a commodity-research house, which fits the "analytics firms get absorbed by domain incumbents" pattern.
  - At COP29 (Nov 2024), Kayrros launched "KayrrosAI", a methane-focused RAG LLM that lets users query the Methane Watch map with text prompts ([Kayrros blog](https://www.kayrros.com/blog/kayrros-releases-kayrrosai-first-of-its-kind-methane-focused-rag-llm-at-cop29/)).
  - It partners with BNP Paribas on portfolio methane-footprint metrics, and on whether satellite imaging can be used "by the financial industry to measure methane abatement" ([BNP Paribas press release, undated](https://group.bnpparibas/en/press-release/kayrros-and-bnp-paribas-join-hands-to-accelerate-methane-abatement)).
- **Problems / pain points:** Standalone EO analytics struggled to stay independent at venture scale (it was acquired). Methane detection from Sentinel-5P/TROPOMI catches only the largest sources, and finer point-source satellites cover narrower areas ([Nexi.fund, 7 Aug 2026](https://nexi.fund/ai-satellite-methane-detection-2026/)). Detections must be attributed to a specific operator and asset before anyone acts on them.
- **How they're trying to solve it:** Fusing many constellations, attributing plumes to assets, wrapping detections in natural-language (RAG) interfaces, and selling into finance (BNP) and commodity intelligence (Energy Aspects).
- **Data:** Copernicus Sentinel-5P / TROPOMI and Sentinel-2 / Sentinel-3 for plumes, plus commercial constellations. Users of the platform include UNEP IMEO and the IEA Methane Tracker ([Kayrros Methane Watch](https://www.kayrros.com/methane-watch/)).
- **Off-the-shelf tech:** RAG over geospatial detections, and plume detection on Sentinel-2 band 11/12 ratios.
- **Hackathon angle:** "Methane alert to accountable asset": take a public plume list (Carbon Mapper portal, UNEP MARS, or TROPOMI hotspots) and join it to OpenStreetMap or OGIM oil-and-gas infrastructure to name the likely facility and operator. Then generate a plain-language notification letter. This mirrors what Kayrros sells, using only free inputs.
- **Credibility:** official company press releases (acquisition), reputable trade press (tech.eu, Carbon Pulse), and one blog aggregator (Nexi.fund).
- **Sources:** cited inline above.

---

### Methane plume market after the loss of MethaneSAT (GHGSat, Carbon Mapper / Planet Tanager, UNEP MARS)

- **What it is:** The demand and supply side for satellite methane detection. This is a cross-check on the space-weather/debris and EO-operator slices, but the downstream "who acts on alerts" problem belongs here.
- **Key facts:**
  - **MethaneSAT** (EDF, launched March 2024) lost contact by 20 June 2025 and was declared "likely not recoverable" ([EDF statement](https://www.edf.org/media/methanesat-loses-contact-satellite); [The Register, 2 Jul 2025](https://www.theregister.com/2025/07/02/methanesat_likely_not_recoverable/); [E&E News](https://www.eenews.net/articles/satellite-tracking-oil-and-gas-emissions-goes-dark/)). According to NYT reporting relayed by EHN, it was meant to last five years, and EDF has not announced a replacement ([EHN](https://www.ehn.org/new-satellite-designed-to-track-methane-emissions-goes-dark-in-orbit)). The team said it would keep processing the data already collected and release regional information ([MethaneSAT update](https://methanesat.org/project-updates/methanesat-loses-contact-satellite)).
  - **Carbon Mapper / Planet Tanager-1:** in Feb 2025 Carbon Mapper released 300+ methane and CO2 plumes, often within ~30 days of observation, at data.carbonmapper.org, free for non-commercial use ([Carbon Mapper](https://carbonmapper.org/articles/carbon-mapper-data-from-tanager1-satellite-reveals-methane-and-co2-super-emitters)). The first-year totals to 16 Sep 2025 were 5,392 methane plumes and 1,234 CO2 plumes from 3,563 sources ([Carbon Mapper, "Tanager-1: One Year in Space"](https://carbonmapper.org/articles/tanager-1-one-year-in-space)). Planet has released 50+ hyperspectral datasets under CC BY on its Open Data STAC ([Planet Pulse](https://www.planet.com/pulse/celebrating-one-year-of-tanager-1/)). The instrument cannot see diffuse sources such as rice paddies or livestock ([Carbon Mapper product guide](https://carbonmapper.org/articles/product-guide)).
  - **UNEP IMEO MARS:** the Oct 2025 "An Eye on Methane" report counts 3,500+ satellite alerts sent across 33 countries. Response rates rose from 1% to 12% in a year, but "nearly 90 per cent remain unanswered". The report documents 25 mitigation actions in 10 countries ([UNEP press release, Oct 2025](https://www.unep.org/news-and-stories/press-release/better-data-driving-action-methane-emissions-more-work-needed); [The Energy Mix](https://www.theenergymix.com/fossils-response-to-methane-leaks-improves-too-slowly-90-still-ignored-un-says/)). A May 2026 UNEP page says MARS has enabled over 40 mitigation cases ([UNEP MARS case studies](https://www.unep.org/topics/energy/methane/mars-case-studies)).
  - **GHGSat:** reported 702 Mt CO2e of methane detected across 127 countries from 88,000+ observations in 2025 (per the Nexi.fund article; its funding figures conflict with its own linked source, so treat them as unverified) ([Nexi.fund, 7 Aug 2026](https://nexi.fund/ai-satellite-methane-detection-2026/)).
  - **Scale:** satellites and AI detected over 5 Mt/yr of oil-and-gas methane in 2025, citing the IEA Global Methane Tracker 2026 (the Nexi.fund article, citing IEA).
  - **Regulation:** EU methane regulation entered force in 2024 with MRV duties on operators and later on imports. CARB runs a satellite methane project with Carbon Mapper (per Nexi.fund).
- **Problems / pain points:**
  - **Detection is no longer the bottleneck; action is.** About 90% of UN alerts go unanswered (UNEP).
  - Losing one flagship mission removes basin-scale quantification.
  - Point-source sensors have narrow swaths and miss diffuse sources.
  - Attributing a plume to an operator is hard.
  - Data licences: Carbon Mapper data is free only for non-commercial use.
- **How they're trying to solve it:** More satellites (Tanager, GHGSat), open portals, UN alert systems with government follow-up, and regulation (EU methane rules, Kazakhstan).
- **Data:** Carbon Mapper portal (plume lists with emission rates, non-commercial licence); Sentinel-5P TROPOMI L2 CH4 (open); Sentinel-2 SWIR; Planet Tanager open STAC (CC BY); UNEP Methane Data portal ([methanedata.unep.org](https://methanedata.unep.org/story-MARS-snapshot)).
- **Off-the-shelf tech:** Published Sentinel-2 plume-detection methods (band ratios) and open plume masks; LLMs for drafting notifications.
- **Hackathon angle:** (a) "Alert-to-action tracker": a per-facility repeat-offender leaderboard from Carbon Mapper plus TROPOMI that tracks whether a site keeps emitting after an alert. This directly measures the "90% unanswered" problem. (b) A persistence and recurrence scorer that separates intermittent super-emitters from one-off events.
- **Credibility:** official (UNEP, EDF, Carbon Mapper); reputable press (The Register, E&E); one blog aggregator (Nexi.fund).

---

### Floodbase (formerly Cloud to Street), parametric flood

- **What it is:** A flood-monitoring and parametric flood-insurance data company that "monitors flooding worldwide" and is "built on more than a decade of science and engineering" ([PR Newswire, 24 Feb 2026](https://www.prnewswire.com/news-releases/floodbase-and-liberty-mutual-launch-instant-parametric-flood-quoting-capability-for-us-commercial-market-302695451.html)). It was originally Cloud to Street, which Joe Morrison's 2020 essay names as an example of a "solutions" company ([Joe Morrison, 12 Nov 2020](https://joemorrison.substack.com/p/stop-building-satellite-imagery-platforms)).
- **2025–2026 news:**
  - Raised $5M in Feb 2025, led by Ecosystem Integrity Fund with Pulse Fund ([Artemis.bm](https://www.artemis.bm/news/floodbase-raises-5m-in-funding-to-advance-parametric-flood-insurance-solutions/)).
  - April 2025: launched an automated parametric policy for New Orleans businesses with Yokahu, which pays out when a set share of the city floods ([Life Insurance International](https://www.lifeinsuranceinternational.com/news/floodbase-yokahu-parametric-flood-coverage/)).
  - Feb 2026: launched instant quoting with Liberty Mutual for US small and mid-size commercial risks, with up to $25M limits per location ([Insurance Journal, 25 Feb 2026](https://www.insurancejournal.com/news/national/2026/02/25/859593.htm); [Business Insurance](https://www.businessinsurance.com/liberty-mutual-teams-with-floodbase-on-parametric-cover/)).
  - March 2026: a Quote API that cuts large-area parametric quoting "from weeks to instant". Partners include Aon, Amwins, Burns & Wilcox and Oneglobal ([Insurance Journal, 6 Mar 2026](https://www.insurancejournal.com/news/national/2026/03/06/860867.htm); [Coverager](https://coverager.com/floodbase-launches-parametric-flood-quote-api/)).
- **Problems / pain points:**
  - **Protection gap:** "two-thirds of modelled US flood losses are underinsured". Rising NFIP premiums and "uncertainty around federal flood insurance" add to it.
  - **Bespoke products:** parametric deals used to be "complex and bespoke".
  - **Distribution is now the constraint:** the release says the main limit is now scalable distribution, not basis risk or product standardisation (paraphrase of the 24 Feb 2026 release).
- **How they're trying to solve it:** Standardised indices of flooded area, APIs for quoting, and broker and carrier partnerships.
- **Data:** Historically, satellite flood maps (MODIS, Sentinel-1 SAR, Landsat; see the Cloud to Street / Global Flood Database below) fused with gauges and models. The 2026 release does not name data sources.
- **Off-the-shelf tech:** Sentinel-1 SAR flood-mapping thresholds; Google Flood Hub forecasts; Global Flood Database (Tellman et al., Nature 2021, from the Cloud to Street team; foundational and not re-verified here).
- **Hackathon angle:** "Basis-risk explainer": for a historic flood (e.g., New Orleans or Houston), compute a parametric trigger (% of a zone flooded) from Sentinel-1 and compare it with FEMA NFIP claims by ZIP code (OpenFEMA). This shows where a parametric policy would have paid and where it would have missed (basis risk). Both datasets are public.
- **Homepage claims (accessed 24 Oct 2026):** Floodbase describes itself as an "AI company" with deep-learning flood models that see "floods before, during, and after", from a city block to a whole country. It says physics is "an additive input, not the core". It claims a continuous 45-year US flood history and links to the Global Flood Database. Its timeline:
  - Founded 2013 with Google research grants; first government client was Sudan, via the World Bank, in 2014.
  - Nature cover in 2021.
  - In 2025 it powered "Europe's largest parametric flood policy", which "has already triggered in Italy".
  - Featured on the NYT front page after the July 2025 Texas floods; Bloomberg covered urban-scale cover for a Bay Area city in March 2025.
  - Supports a Liberty Mutual Re agricultural product in Colombia.
  - Partners named: Swiss Re, Lloyd's, AXA, the World Bank, NASA and African Risk Capacity ([Floodbase homepage](https://www.floodbase.com/)).
- **Credibility:** official press releases; reputable trade press (Insurance Journal, Artemis, Business Insurance); company homepage.

---

### Descartes Underwriting (Paris), parametric insurer and MGA

- **What it is:** A parametric insurance underwriter that uses satellite imagery, IoT and client data to trigger payouts ([Artemis, Series A coverage](https://www.artemis.bm/news/descartes-raises-18-5m-series-a-to-scale-up-parametric-insurance/)).
- **2025 news:** Launched a parametric tornado policy for US utility-scale solar farms with up to $70M cover, using "satellite imagery and advanced analytics to calculate payouts when tornadoes strike" ([FinTech Global, 24 Jan 2025](https://fintech.global/2025/01/24/descartes-underwriting-introduces-70m-parametric-insurance-product-for-solar-farms/)). A $120M Series B led by Highland Europe and Eurazeo was reported; its date was not shown in the snippet (unverified date) ([Insurance Journal topic page](https://insurancejournal.com/topics/tanguy-touffut)).
- **Scale (homepage, accessed 24 Oct 2026):**
  - "$250M+ gross written premium in 2025" and 600+ large corporations and public entities covered.
  - 35+ products in 60+ countries, 150+ risk-modelling and science staff, and $15B+ capacity deployed through 300+ broker firms.
  - Perils include hurricane, earthquake, tornado, flood, hail, drought, frost, wildfire, low/high river levels and "lack of wind", plus cyber.
  - Satellite inputs: "high-resolution Earth observation, including optical imagery, 3D data, and thermal infrared" for monitoring and claims, alongside 80+ data sources (NASA, NOAA, ECMWF) and 30–40 years of history ([Descartes Underwriting homepage](https://www.descartesunderwriting.com/)).
  - It is one of the few EO-consuming businesses with a disclosed, sizeable revenue line.
- **Problems / pain points:** Basis risk (an index triggers when there's no loss, or misses a real loss); verifying hazard intensity (hail, tornado path, wind) at asset level; uninsurable climate-exposed assets such as solar farms in hail and tornado belts.
- **How they're trying to solve it:** Satellite-derived event footprints (tornado damage tracks, hail swaths, flood extent) as objective triggers.
- **Data:** Sentinel-2 / Landsat post-event imagery (tornado scars are visible in NDVI); NOAA Storm Events database; SPC tornado tracks; GOES / MRMS radar hail products (public).
- **Hackathon angle:** "Tornado-track trigger": detect tornado damage scars from Sentinel-2 NDVI differencing after an event and intersect them with a public solar-farm dataset (e.g., USPVDB, the USGS/LBNL US Large-Scale Solar Photovoltaic Database). This would settle a mock parametric policy automatically.
- **Credibility:** reputable trade press.

---

### Sylvera (London), carbon credit ratings

- **What it is:** A carbon-credit ratings and data provider that uses satellite, LiDAR and ML to assess projects. It "does not deal in or broker... carbon credits or take payment for rating projects" ([Index Ventures, Jul 2023](https://www.indexventures.com/perspectives/sylvera-raises-57m-to-incentivize-investment-in-real-climate-impact-and-fuel-us-expansion/)).
- **Funding:** $32.6M Series A in Jan 2022 ([Venture Capital Journal](https://www.venturecapitaljournal.com/sylvera-picks-up-32-6m-series-a/)) and $57M Series B in Jul 2023 led by Balderton ([CarbonCredits.com](https://carboncredits.com/sylvera-raises-57m-help-companies-invest-in-ncarbon-credit-with-confidence); [ESG Today](https://www.esgtoday.com/?p=13257)). A search found no 2025 round; status is unverified.
- **Problems / pain points:** Buyers can't tell good credits from bad ones. The 2023 Guardian/Zeit/SourceMaterial investigation into Verra rainforest credits (see the carbon-integrity entry below) raised demand for independent ratings but also cut overall demand for nature credits.
- **How they're trying to solve it:** Independent ratings with remote-sensing evidence, baseline re-estimation and buyer tooling.
- **Pivot signal (homepage, accessed 24 Oct 2026):** the homepage now leads with compliance and regulated markets:
  - An Article 6 & CORSIA Hub, and eligibility across CORSIA, LCFS, FuelEU Maritime, CBAM and EU ETS.
  - EAC (energy attribute certificate) assurance, a "2026 EAC Market Survey: SBTi Demand, Verified CI, the Verification Gap", and a Market Gateway to "400 million tonnes" of inventory.
  - It no longer mentions satellite or LiDAR, only "independent biomass data" and "geospatial" work ([Sylvera homepage](https://www.sylvera.com/)).
  - Reading: the satellite-first nature-credit ratings model has broadened into general carbon and compliance-market intelligence, which is a sign of weak pure-nature demand.
- **Data:** Landsat / Sentinel time series; GEDI / ICESat-2 LiDAR; Hansen Global Forest Change; JRC TMF.
- **Hackathon angle:** see "Carbon integrity" below.
- **Credibility:** reputable trade and VC press.

---

### Pachama, acquired by Carbon Direct (Nov 2025)

- **What it is:** A forest-carbon digital MRV platform that combines satellite imagery, LiDAR and ML to estimate forest carbon and detect changes such as illegal logging ([Trellis interview](https://trellis.net/article/diego-saez-gil-on-how-pachama-is-revolutionizing-carbon-markets-with-satellite-and-lidar-technology)).
- **2025 news:** Carbon Direct acquired Pachama on 10 Nov 2025 to "enhance Carbon Direct's digital MRV capabilities" and speed project diligence. CEO Diego Saez Gil joined Carbon Direct ([Carbon Direct press](https://www.carbon-direct.com/press/carbon-direct-acquires-pachama); [Axios, 10 Nov 2025](https://www.axios.com/2025/11/10/carbon-direct-buys-pachama-climate); [Business Wire](https://www.businesswire.com/news/home/20251110399124/en)). Axios tied the deal to rising tech-company demand for nature credits, which Big Tech uses to offset data-centre growth.
- **Problems / pain points:** Standalone dMRV platforms consolidate into advisory and procurement firms. Buyers need diligence on baselines, leakage and permanence.
- **How they're trying to solve it:** Folding dMRV into a science-led advisory firm.
- **Data:** Optical and SAR time series, GEDI and airborne LiDAR, field plots.
- **Hackathon angle:** see "Carbon integrity" below.
- **Credibility:** official press release plus Axios.

---

### Renoster: ratings agency turned CDR developer

- **What it is:** A carbon-credit rating agency whose "Mercury Rubric" uses public satellite data (e.g., NASA) to score nature-based projects. Carbon Market Watch found Renoster relies more on algorithmic analysis than other agencies ([Carbon Market Watch comparison](https://carbonmarketwatch.org/publications/assessing-and-comparing-carbon-credit-rating-agencies/)).
- **2025 news:**
  - In Sept 2025, after reviewing 500 million nature-based credits, it said buffer pools and integrity labels are "not working very well" ([Carbon Pulse briefing](https://carbon-pulse.com/431395/)).
  - It then pivoted to carbon removal project development and signed its first offtake ([Carbon Pulse interview](https://carbon-pulse.com/436628/)). At Climate Week NYC 2025 it targeted $55–80 per credit for high-quality forest carbon ([Carbon Pulse](https://carbon-pulse.com/438566/)).
  - Its ratings are "no longer maintained" as of July 2025 ([yespress profile](https://yespress.io/renoster)).
- **Problems / pain points:** Ratings alone are not a business (pivot). Buffer pools are under-capitalised against reversal risk such as fire. Integrity labels such as ICVCM CCP don't separate quality well.
- **Data:** Public satellite archives (Landsat, Sentinel, GEDI), Hansen GFC, fire products (MODIS / VIIRS burned area).
- **Hackathon angle:** "Buffer-pool stress test": for registered forest-carbon projects (Verra registry polygons are public for many projects), compute burned or deforested area since registration from MODIS burned area plus Hansen loss. Compare that with each project's buffer contribution. This tests Renoster's claim with open data.
- **Credibility:** reputable specialist press (Carbon Pulse, partly paywalled; only snippets seen), plus an NGO report (Carbon Market Watch).

---

### Chloris Geospatial (Boston / Europe), biomass monitoring

- **What it is:** Satellite-based above-ground biomass (AGB) time series for forest-carbon projects and corporate carbon accounting.
- **2025 news:** $8.5M Series A on 7 Jul 2025 led by Future Energy Ventures, with AXA IM Alts, At One Ventures, Cisco Foundation, Counteract and Orbia Ventures. Funds go to teams, carbon-accounting partnerships and a European hub ([VCA Online / press release, 7 Jul 2025](https://www.vcaonline.com/news/2025070701/chloris-geospatial-raises-8-5-million-series-a-to-scale-satellite-based-forest-carbon-monitoring/); [FEV](https://fev.vc/fev-leads-chloris-geospatials-series-a-to-scale-satellite-based-forest-carbon-monitoring/)). A Caplight page shows conflicting totals (unverified).
- **Problems / pain points:** Biomass maps disagree with each other. Field plots are scarce. Companies need annual, consistent, historical baselines rather than one-off maps.
- **How they're trying to solve it:** Calibrated multi-sensor AGB time series back to 2000.
- **Data:** ESA CCI Biomass, GEDI L4A/L4B, NASA/ESA Biomass mission P-band (data opened Jan 2026, per [New Space Economy, 23 Oct 2026](https://newspaceeconomy.ca/2026/10/23/why-does-defense-dominate-earth-observation-demand-over-commercial-markets/)), Landsat.
- **Hackathon angle:** "Biomass map disagreement explorer": for any project polygon, overlay ESA CCI Biomass, GEDI L4B and others, and flag where they disagree by more than X%. This tells a buyer how uncertain a credit really is.
- **Credibility:** official release and VC blog.

---

### Regrow Ag, agricultural MRV (regenerative ag, Scope 3)

- **What it is:** Remote-sensing-based MRV for farm practices (cover crops, tillage) used by food companies for Scope 3 insetting programmes. Formed from a merger of FluroSat and Dagan ([Regrow Series A post](https://www.regrow.ag/post/regrow-raises-17-million-series-a-funding-to-scale-carbon-market-monitoring-and-verification); [AgFunderNews](https://agfundernews.com/regrow-raises-17m-from-cargill-microsoft-for-carbon-verification-tool)).
- **News:**
  - Series B of $38M led by Galvanize Climate Solutions, with TIME Ventures and Rethink Impact ([Regrow](https://www.regrow.ag/post/regrow-ag-secures-38m-in-series-b-to-use-agriculture-to-meet-net-zero-targets)). Preqin dates it 25 Mar 2025; other coverage appears older, so the date is unverified ([Preqin](https://www.preqin.com/data/profile/asset/regrow-agriculture-inc-/440547)).
  - March 2026 (aggregators, unverified): merger with Argentina's PUMA and an SE Ventures investment ([Unify insights](https://www.unifygtm.com/insights-headcount/regrow); [Agrofy tag](https://news.agrofy.com.ar/tags/regrow)).
  - Rice insetting programme with AgriCapture and Amazon Grocery, 11 Mar 2026 (per [Caplight](https://www.caplight.com/company/regrow), unverified).
- **Problems / pain points:** Verifying practices (cover crop, no-till) at field scale over millions of acres without farm visits; low farmer participation; scepticism about soil-carbon claims.
- **How they're trying to solve it:** "MonitorML" (an AI tool for detecting practices) and coverage expansion. One source says it covers 80% more US fields (undated, unverified).
- **Data:** Sentinel-2, Landsat, HLS (Harmonized Landsat Sentinel-2), USDA CDL, Sentinel-1.
- **Hackathon angle:** "Cover-crop verifier": detect winter green cover on fields from HLS NDVI between Nov and Mar for a county. Compare with USDA cover-crop census or OpTIS public estimates and output a verification report per field.
- **Credibility:** company blog and aggregators.

---

### Sust Global, acquired by ISS STOXX (Aug 2025)

- **What it is:** Geospatial climate-risk modelling (physical hazard exposure per asset) from satellite-derived data and climate models.
- **2025 news:** ISS Sustainability Solutions (ISS STOXX) announced the purchase on 5 Aug 2025 ([ISS insights tag](https://insights.issgovernance.com/tags/sust-global); [FS Sustainability, 7 Aug 2025](https://www.fssustainability.com.au/iss-stoxx-acquires-geospatial-risk-modelling-specialist)).
- **Problems / pain points:** Climate-risk analytics become a feature of ESG data giants rather than standalone products (consolidation). Asset-level risk scores from different vendors disagree.
- **Hackathon angle:** see Jupiter / climate-risk disagreement (below).
- **Credibility:** official and trade press.

---

### EarthScan (Mitiga Solutions; formerly Cervest)

- **What it is:** Not a satellite company. EarthScan is a climate-risk platform first built by UK startup Cervest. According to one secondary source, Cervest "entered administration on 20 June 2023, ceased trading, and made all 71 employees redundant". Its EarthScan IP was sold to Barcelona's Mitiga Solutions (a Barcelona Supercomputing Center spin-off) around 25 June 2023 ([rfp.wiki Cervest page](https://www.rfp.wiki/sustainability-esg/climate-risk-tools/cervest); [CB Insights](https://www.cbinsights.com/compare/cervest-vs-climateai)). Mitiga's EarthScan models 10+ hazards ([EEN partnering listing](https://een.ec.europa.eu/partnering-opportunities/luxembourg-earth-observation-company-offering-satellite-based)). It won the Climate Tech category at South Summit Madrid 2026 ([ecosistemastartup](https://ecosistemastartup.com/mitiga-earthscan-gana-south-summit-2026-ia-para-riesgo-climatico/)), and reportedly raised €21M afterwards (headline only, unverified) ([ecosistemastartup](https://ecosistemastartup.com/?p=91091)).
- **Problems / pain points:** Climate-risk SaaS for corporates has struggled commercially (Cervest went insolvent despite funding from Marc Benioff's TIME Ventures, per [Trellis](https://trellis.net/article/benioff-backed-software-startup-helps-companies-get-smarter-about-climate-risk)).
- **Credibility:** secondary sources; insolvency date from one source.

---

### Cape Analytics, acquired by Moody's (Jan 2025)

- **What it is:** Geospatial-AI property intelligence (roof condition, vegetation overhang, pools, building footprint) from aerial and satellite imagery, used by insurers for underwriting across the US, Canada and Australia.
- **2025 news:** Moody's agreed to acquire it on 13 Jan 2025 and expected to close in Q1 2025. Terms were undisclosed and "not expected to have a material impact" on Moody's financial results ([TechCrunch, 13 Jan 2025](https://techcrunch.com/2025/01/13/moodys-agrees-to-acquire-cape-analytics-which-develops-geospatial-ai-for-insurance-providers); [Business Wire](https://www.businesswire.com/news/home/20250113472182/en/); [Carrier Management](https://carriermanagement.com/news/2025/01/14/270543.htm)). Closing was not verified here.
- **Problems / pain points:** Insurers have limited inspection budgets and stale property data. Wildfire and hail underwriting needs property-level attributes. Regulators scrutinise insurers that use aerial imagery to drop policies (a known controversy; the source was not re-checked here, so unverified).
- **Data:** Mostly high-resolution aerial imagery (Nearmap, EagleView, Vexcel). Open alternatives: NAIP (60 cm US aerial), Microsoft/Google building footprints, Overture Maps.
- **Hackathon angle:** "Defensible-space checker": use NAIP plus building footprints to measure vegetation within 0–5 ft and 5–30 ft of each home (California Zone 0 rules), then produce a homeowner-facing mitigation report. Underwriters do this with paid imagery; NAIP makes it free.
- **Credibility:** reputable press and official release.

---

### LiveEO (Berlin): EUDR, utilities and rail

- **What it is:** Satellite and LiDAR analytics for infrastructure (vegetation encroachment on power lines and rail, ground movement, pipelines). TradeAware is its EUDR deforestation-compliance product. Customers include Deutsche Bahn, E.ON, Iberdrola and Network Rail. Partners include Accenture, AWS and SAP ([Startups Magazine, 1 Jul 2024](https://startupsmagazine.co.uk/article-liveeo-raises-eu25m-leverage-ai-powered-satellite-data-critical-infrastructure-and-climate)).
- **News:** €25M Series B in Jul 2024 (total €51.6M, ~130 staff) (same source). A later €28M first close led by Helantic covers civil infrastructure and defence, including a "Twinspector" satellite constellation. The date is around 2026 and unconfirmed ([Tamradar](https://www.tamradar.com/funding-rounds/liveeo-28m-satellite-intelligence)). LiveEO also published "The State of UVM in 2025" report ([LiveEO](https://www.live-eo.com/article/the-state-of-uvm-2025-report)).
- **Problems / pain points:**
  - "We see EU deforestation regulation (EUDR) as creating the first mass market with millions of users for EO analytics" (co-CEO Daniel Seidel, 2024).
  - "Open-source solutions can be inaccurate" (same article).
  - Utilities need tree-level risk, not pixels, and want work orders.
  - Repeated EUDR delays undermine the "mass market" thesis (see the EUDR entry).
- **How they're trying to solve it:** Workflow products (Treeline for vegetation management, TradeAware for compliance), ERP integration (SAP) and vertical integration into their own satellites.
- **Data:** Sentinel-1/2, commercial VHR, LiDAR.
- **Hackathon angle:** see the EUDR entry.
- **Credibility:** reputable startup press, company blog, funding aggregator.

---

### Overstory (Amsterdam / US), vegetation intelligence for utilities

- **What it is:** High-resolution satellite imagery plus AI that assesses vegetation at tree level for utility wildfire and outage risk. It serves "six of the ten largest utilities across the Americas" and 50+ utilities, co-ops and municipalities ([Impact Alpha](https://impactalpha.com/overstory-secures-43-million-to-predict-and-prevent-utility-sparked-fires/); [Kurrant](https://kurrant.com/kurrantly-news/overstory-secures-43-million-to-scale-ai-driven-vegetation-intelligence-and-utility-wildfire-prevention/)).
- **2025 news:** $43M Series B announced 25 Nov 2025, led by Blume Equity with Energy Impact Partners. The money funds a new "fuel detection model" that "identifies high-risk wildfire areas and advises on 'exact actions'" ([IoT M2M Council](https://iotm2mcouncil.org/iot-library/news/smart-energy-news/overstory-raises-43m-to-protect-utilities-from-vegetation/); [International Fire & Safety Journal](https://internationalfireandsafetyjournal.com/overst-wildfire-prevention/)). Earlier, a $14M Series A in 2023 was led by B Capital ([Pulse 2.0](https://pulse2.com/overstory-14-million-to-mitigate-wildfires/amp/)).
- **Problems / pain points:** Utility-ignited wildfires (e.g., PG&E Camp Fire, Maui 2023) create huge liabilities. Vegetation trimming budgets are large and spent on fixed cycles rather than by risk. Utilities need prioritised action lists.
- **How they're trying to solve it:** Tree-level species, height and health mapping; fuel detection; mapping imagery to trim crews' work orders.
- **Data:** Commercial VHR (Planet / Maxar-Vantor); open alternatives include NAIP, Meta/WRI 1 m global canopy height map, LANDFIRE fuels, HIFLD transmission lines, and OpenStreetMap power lines.
- **Off-the-shelf tech:** Meta / WRI High Resolution Canopy Height (open), SAM / segment-geospatial for tree crowns.
- **Hackathon angle:** "Grid-strike tree finder": intersect HIFLD or OSM transmission lines with the Meta 1 m canopy-height map and compute "fall-in" risk, where trees taller than their distance to the line could hit it. Combine with a wildfire hazard layer (USFS Wildfire Risk to Communities) and rank spans for inspection. All data is public, and the output (a ranked list) is something the buyer would actually use.
- **Credibility:** trade press and company announcements.

---

### Gro Intelligence (NY / Nairobi), shut down in 2024: a cautionary tale

- **What it is:** An agri and climate data platform that aggregated satellite, weather and market data for food-security forecasts.
- **What happened:** It raised $117M in total, including an $85M Series B. It struggled to meet payroll and pension payments in Feb 2024, laid off 60% of staff, replaced founder-CEO Sara Menker, failed to raise after a March 2024 bridge round, and shut down in June 2024. Former employees sued over the layoffs, and the SEC was reported to be investigating ([TechCabal, 2 Jun 2024](https://techcabal.com/2024/06/02/kenya-data-analytics-gro-intelligence-shuts-down/); [The Founder Africa](https://thefounder.africa/the-rise-and-fall-kenya-based-data-analytics-startup-gro-intelligence/); [NextBillion](https://nextbillion.net/news/ag-insights-platform-gro-intelligence-is-closing-down/); [Launch Base Africa](https://launchbaseafrica.com/2024/06/02/african-agtech-startup-gro-intelligence-funded-by-echovc-crashes-despite-100m-investment/)).
- **Problems / pain points:** It "faced challenges in achieving product-market fit". Revenue came from smaller deals, which "was not sufficient to sustain its operations" (The Founder Africa). Bids for sovereign food-security contracts with a small Asian country and a Middle Eastern oil exporter failed, and it struggled to win US government work (AgFunderNews as relayed).
- **Lesson for the pitch:** a broad "data for everything" platform without one buyer whose workflow it changes fails, even with $100M+ of funding. This echoes Joe Morrison's "nobody wants your fancy algorithm" argument.
- **Credibility:** reputable regional tech press.

---

### EUDR (EU Deforestation Regulation) as a demand driver, and its repeated delays

- **What it is:** EU regulation that requires operators placing cocoa, coffee, soy, palm oil, cattle, rubber and wood (and derived products) on the EU market to prove those products are deforestation-free after a 31 Dec 2020 cutoff. Proof relies on geolocation of production plots, which makes satellite deforestation checks the core compliance tool.
- **Timeline (per LiveEO's tracker):**
  - Originally due to apply from Dec 2024; postponed by 12 months.
  - On 19 Dec 2025 the Parliament and Council adopted amending Regulation (EU) 2025/2650.
  - New dates: **30 Dec 2026 for non-SME operators** and **30 Jun 2027 for micro and small undertakings**.
  - The amendment adds a simplified one-time declaration for micro and small primary operators, plus a "downstream operator" category that doesn't file due-diligence statements ([LiveEO, "EUDR Delay", 28 Oct 2025, updated](https://www.live-eo.com/blog/eudr-delay)).
  - The page itself contains conflicting older dates, so the dates above should be re-checked against EUR-Lex.
- **Status in Oct 2026:** the large-operator deadline is about 2 months away. The Commission's list of national competent authorities was updated 22 Sep 2026; per LiveEO, Greece and Malta had no published contacts ([LiveEO, 28 Sep 2026](https://www.live-eo.com/blog/eudr-competent-authorities---updated-list)). Vendors are publishing "What are NCAs looking for in your EUDR due diligence?" (28 Sep 2026) and "EUDR defensibility in practice" (7 Oct 2026) ([Satelligence homepage news list, accessed 24 Oct 2026](https://www.satelligence.com/)).
- **Problems / pain points:**
  - Millions of smallholder plots need polygons, and many arrive as single GPS points or bad geometries.
  - Forest baselines disagree, and the 2020 cutoff map choice is contested.
  - Plantation harvesting and cocoa agroforestry get misread as deforestation, i.e. false positives (see CTrees' MRV challenges below).
  - Operators need audit-ready evidence that will "defend" against national authorities.
  - Repeated delays erode the business case for vendors who bet on it. LiveEO's co-CEO called EUDR "the first mass market with millions of users for EO analytics" ([Startups Magazine, 1 Jul 2024](https://startupsmagazine.co.uk/article-liveeo-raises-eu25m-leverage-ai-powered-satellite-data-critical-infrastructure-and-climate)).
  - China-origin geolocation data sharing is a legal obstacle ([LiveEO, 11 Jul 2025](https://www.live-eo.com/blog)).
- **How companies are trying to solve it:** Traceability platforms (Satelligence, LiveEO TradeAware, Space Intelligence via the ICE Commodity and Traceability service), EY-assured deforestation data (Satelligence), and plot-polygon checks against forest baselines.
- **Data:** JRC Global Forest Cover 2020 map (EU Observatory; the page couldn't be read here, so details are unverified); Hansen / UMD Global Forest Change (Landsat, 30 m, annual); WRI / GFW alerts (GLAD-L, GLAD-S2, RADD Sentinel-1); JRC Tropical Moist Forest; ESA WorldCover; Sentinel-1/2.
- **Off-the-shelf tech:** Whisp (FAO / Forest Data Partnership open tool for deforestation-risk checks on plots; known but not opened here, so unverified); Google Earth Engine; GFW API.
- **Hackathon angle (strong):** "EUDR plot pre-checker":
  - The user uploads a GeoJSON or CSV of farm plots, for example a co-op's cocoa plots.
  - The tool validates the geometry (self-intersections, points versus polygons, plots over 4 ha that need polygons).
  - It intersects each plot with three forest-2020 baselines and post-2020 loss and alert layers.
  - It flags where the baselines disagree, which is likely a false positive or agroforestry.
  - It outputs a per-plot risk table plus an LLM-drafted due-diligence narrative citing the evidence.
  - Problem: exporters face a real deadline on 30 Dec 2026.
- **Credibility:** company blogs (LiveEO, Satelligence), dated; the regulation number was taken from LiveEO and not checked against EUR-Lex.

---

### Satelligence (Utrecht): deforestation and commodity-supply-chain monitoring

- **What it is:** A "nature intelligence" company offering a traceability platform, deforestation- and conversion-free (DCF) monitoring, EUDR due diligence, Scope 3 FLAG land-based emissions and NDPE verification. Commodities covered: timber, pulp, cocoa, coffee, soy, beef, palm oil, rubber and others. Customer logos include Unilever, Cargill, Mondelez, IKEA, Olam, Bunge, Nestlé, Wilmar, Lindt and Rabobank. Its deforestation and carbon data carry EY ISAE 3000 / 3402 assurance ([Satelligence homepage, accessed 24 Oct 2026](https://www.satelligence.com/)).
- **Problems / pain points:** Buyers need audit-grade, "defensible" evidence, not just maps. They also need one consistent land-use view across compliance regimes (EUDR, CSRD, SBTi FLAG, GHG Protocol); see Satelligence's 12 Oct 2026 post "One view of land use: Why consistent climate data is crucial".
- **How they're trying to solve it:** Third-party-assured data, nature and commodity baselines, and field presence.
- **Data:** Satellite plus field data, supply-chain asset data.
- **Hackathon angle:** see EUDR.
- **Credibility:** company page.

---

### Space Intelligence (Edinburgh): nature mapping for carbon markets and EUDR

- **What it is:** Satellite land-cover, above-ground biomass and screening datasets for voluntary carbon market (VCM) project screening, due diligence and monitoring; EUDR compliance via the ICE Commodity and Traceability service; Scope 3 for coffee, cocoa and palm. It uses "human-in-the-loop processes to calibrate its machine learning models locally". Products include Screening Pro (Baseline, Leakage Risk, Durability Risk modules) and Global Harmonised Layers 2026. Everland used its mapping for the Keo Seima REDD+ project in Cambodia. One news post explains "why carbon maps from different providers disagree and how to choose one" ([Space Intelligence homepage, last modified 26 Feb 2026](https://www.space-intelligence.com/)).
- **Problems / pain points:** Global maps are poorly calibrated to local land classes. Carbon maps from different providers disagree. Leakage and durability risk are hard to estimate before issuance.
- **Hackathon angle:** "Map disagreement as a feature": see Chloris.
- **Credibility:** company page.

---

### Carbon-credit integrity crisis (Verra, REDD+, ratings agencies)

- **What it is:** The voluntary carbon market's credibility crisis over nature-based credits, which is the root demand for satellite-based dMRV and ratings.
- **Key facts:**
  - **Jan 2023:** a Guardian / Die Zeit / SourceMaterial investigation found about 94% of Verra-certified rainforest credits (about 40% of all Verra credits) "do not represent a tonne of carbon dioxide equivalent". It also found deforestation threat overstated by about 400% on average. It drew on a Cambridge peer-reviewed study and another study that was not yet peer-reviewed. Verra CEO David Antonioli resigned in May 2023 ([Wikipedia "Verra (organization)", citing The Guardian 18 Jan 2023 and 23 May 2023](https://en.wikipedia.org/wiki/Verra_(organization))).
  - **2024:** Mongabay reported possible timber laundering linked to Verra Amazon projects. Brazilian police raids led to project suspensions in June 2024 (same Wikipedia page, citing Mongabay 21 May, 7 Jun and 11 Jun 2024).
  - **2026:** ICVCM lists VCS as "CCP-Eligible" (same page, retrieved 17 Feb 2026).
  - The underlying satellite method (synthetic-control comparison of project versus matched pixels; West et al., Science 2023) is foundational. The Science page was not accessible (403), so it is unverified here.
- **Ratings agencies as a response:**
  - **BeZero Carbon** published 14 ex ante rating reports on Microsoft's portfolio (18 Aug 2026). Its CEO argued in an op-ed that ESMA regulation could strengthen the market (30 Jul 2026). Its homepage warns: "Over-reliance on models can lead to false precision" ([BeZero homepage, accessed 24 Oct 2026](https://bezerocarbon.com/)).
  - **Sylvera** and **Calyx** are other rating agencies; Renoster's ratings are no longer maintained (see the Renoster entry). Carbon Market Watch compared rating agencies ([CMW, page blocked (403) when fetched](https://carbonmarketwatch.org/publications/assessing-and-comparing-carbon-credit-rating-agencies/)).
- **Problems / pain points:** Baselines are inflated. Leakage is ignored. Buffer pools are underfunded (Renoster). Ratings disagree. Ex-post satellite evaluation shows over-crediting. Demand for nature credits collapsed and then partly recovered with Big Tech buyers such as Microsoft (Axios on Pachama).
- **Data:** Verra registry project KML/shapefiles (public for many projects); Hansen GFC; JRC TMF; GEDI; CTrees JMRV / REDD+AI; MapBiomas (Brazil).
- **Off-the-shelf tech:** Synthetic-control / matching packages (e.g., the R `MatchIt` and Python `causalml` packages), Google Earth Engine.
- **Hackathon angle (strong):** "Did this offset project actually protect forest?":
  - Pick 10 public REDD+ project polygons.
  - Compute forest loss inside each project versus a matched control area (similar slope, distance to roads, initial cover) from Hansen GFC 2001–2024.
  - Compare with the credited baseline and output an "over-crediting ratio" plus a plain-language report card.
  - Pitch: a public, transparent version of what rating agencies sell, with the 2023 scandal as the hook.
- **Credibility:** encyclopedia summary of reputable press; company pages.

---

### CTrees (non-profit, Pasadena): open forest-carbon data

- **What it is:** A science non-profit (CEO Sassan Saatchi) mapping trees and carbon. Products:
  - JMRV: carbon stock, emission and removal data for 263 countries and territories, described as "open data".
  - LUCA: near-real-time land-use-change alerts worldwide.
  - REDD+AI: attributes degradation to logging, fire or roads.
  - Land Carbon Map: 1 ha, 2000 to present.
  - Tree-level data and tropical activity data.
  - Source: [CTrees homepage, accessed 24 Oct 2026](https://ctrees.org/).
- **2026 news:**
  - *Fuel Watch* (16 Oct 2026): a satellite + AI live-fuel-moisture map for LA County (30 m weekly, near-real-time down to 10 m). It reports that 93% of the county's chaparral has dried into CAL FIRE's high-risk range. It replaces costly ground sampling (clipping and weighing chamise shrubs) and is aimed at fire agencies, utilities and communities ([CTrees, 16 Oct 2026](https://ctrees.org/news/Los-Angeles-County-wildfire-spread)).
  - 3D fire-fuel mapping (7 Oct 2026); a US Endowment grant to link forest, mill and market data (2 Oct 2026); an SFI partnership on forest supply sheds (8 Jul 2026); a jurisdictional REDD+ data solution (16 Jul 2026) ([CTrees news](https://ctrees.org/news)).
- **Problems / pain points:** "8 technical challenges for jurisdictional REDD+ MRV" ([CTrees, 22 Jul 2026](https://ctrees.org/news/8-challenges-for-jredd-mrv)):
  - Dry forests are hard to map.
  - "remote sensing approaches may mis-classify plantation harvesting or management activities as deforestation".
  - "attributing change to specific drivers, such as logging or fire, remains a major challenge".
  - Large minimum mapping units "can underestimate land clearing".
  - "five-year reports can miss forest loss and regrowth dynamics".
  - Reliance on one dataset: "DETER still omits 20% of forest fire".
  - A single emission factor doesn't capture repeated fires.
  - "regrowth results in significant removals not accounted for".
- **US forest inventory (FIA):** "more than 300,000 ground plots". It is "suffering capacity constraints, even as user demand is increasing", and has no framework to fuse plots with remote sensing. Still, "wall-to-wall maps are built from ground samples, not in place of them" ([CTrees, 13 Jul 2026](https://ctrees.org/news/time-to-modernize-us-forest-inventory)).
- **Hackathon angle:** (a) "Degradation driver classifier": label disturbances in a LUCA or GFW alert region as fire, logging road or selective logging, using VIIRS fire points plus OSM road growth plus Sentinel-2 texture. (b) A Fuel Watch-style live-fuel-moisture proxy for another county using Sentinel-2 NDMI and MODIS, validated against the National Fuel Moisture Database (public).
- **Credibility:** non-profit primary pages, dated.

---

### Jupiter Intelligence: physical climate-risk analytics

- **What it is:** Asset-level, multi-peril climate projections (ClimateScore Global: 5-year steps to 2100, "22k+ data values per location"), plus adaptation ROI, entity roll-ups and compliance tools. It claims 3 of the 5 largest US banks and 40% of the largest US energy and power producers as clients. Logos include bp, Equinor, Fannie Mae and Liberty Mutual ([Jupiter homepage, accessed 24 Oct 2026](https://www.jupiterintel.com/)).
- **2026 posts:** "Close Enough Isn't Good Enough: How to Evaluate Physical Climate Risk Data" (13 Feb 2026); "Physical Climate Risk Is Already a 2% Tax on Corporate Earnings" (15 Jul 2026); "How Jupiter Uses AI for Climate Risk Intelligence" (28 Sep 2026); a PRICE framework with Arcadis (10 Jun 2026) (same page).
- **Problems / pain points:** Vendor scores disagree, which is why vendors publish "how to evaluate" guidance. Disclosure regimes (ISSB, CSRD, Fed / ECB climate stress tests) create demand but differ in what they require. Model validation is a pain point (Jupiter sells an "MRM Accelerator"). The sector is consolidating: Sust Global went to ISS STOXX (2025), Cape to Moody's (2025), and EarthScan/Cervest failed (2023).
- **Hackathon angle:** "Climate-risk vendor disagreement map": for 100 public facilities (e.g., EPA FRS power plants), compare free flood-hazard layers (FEMA NFHL, JRC global flood hazard, Fathom-based WRI Aqueduct) and show where they disagree. Sentinel-1 historical flood detections could serve as "ground truth" where available.
- **Credibility:** company page.

---

### ZestyAI: AI property-risk models for P&C insurers

- **What it is:** Risk models (Z-FIRE, Z-HAIL, Z-WIND, Z-STORM, Z-WATER, Z-SPARK), 3D roof models and roof age (from permits and aerial imagery), claiming 99.7% US property coverage and "more than 500 regulatory approvals". Customers include Allstate, Farmers, Zurich, Lemonade, and the California and Colorado FAIR Plans ([ZestyAI homepage, accessed 24 Oct 2026](https://www.zesty.ai/)).
- **Problems / pain points:** Insurers' AI models must be approved by state regulators, so explainability and "accountability for AI decisions" are a theme of its blog. Wildfire and hail losses drive non-renewals and insurers leaving California. FAIR Plans (insurers of last resort) are customers.
- **Data:** Mostly aerial imagery, permits, parcels and loss data; satellite is not emphasised.
- **Hackathon angle:** see Cape Analytics defensible-space checker, or "hail-roof triage": map hail swaths (NOAA MRMS MESH, public) against building footprints, then rank roofs for post-event inspection.
- **Credibility:** company page.

---

### Arbol: parametric climate insurance

- **What it is:** Parametric insurance where payouts are triggered by third-party data (NOAA, NASA, ESA and others), paid "in as little as 2 weeks after data verification". It claims "$2+ billion in notional risk transferred", 15+ countries, and that 50% of clients "Wouldn't Have Access to Climate Risk Products" otherwise. It recently launched cover for "data center regulatory moratorium risk" ([Arbol homepage, accessed 24 Oct 2026](https://www.arbol.io/)).
- **Problems / pain points:** Basis risk; many farmers and SMEs lack access to cover; payouts need fast, trusted data.
- **Data:** Public satellite and weather data (CHIRPS rainfall, ERA5, MODIS / VIIRS, SMAP soil moisture are typical inputs for parametric indices; Arbol's specific datasets were not confirmed).
- **Hackathon angle:** "Drought-index payout simulator": build a satellite rainfall (CHIRPS) or NDVI index for a Kenyan county and back-test payouts against historical drought years (FEWS NET reports). This shows basis risk visually.
- **Credibility:** company page.

---

### Tomorrow.io: weather intelligence turned satellite operator (EO-adjacent)

- **What it is:** A weather intelligence company that backward-integrated into its own radar and microwave-sounder satellites. Milestones: SPAC deal with Pine Technology dropped in March 2022; radar satellites launched 2023; US Air Force contract for microwave sounders in May 2024; NVIDIA Earth-2 collaboration in March 2025. In Feb 2026 it raised $175M at a valuation above $1B, reporting about $100M ARR and a fully deployed 13-satellite constellation, and announced "DeepSky" ([Wikipedia "Tomorrow.io", accessed 24 Oct 2026](https://en.wikipedia.org/wiki/Tomorrow.io)).
- **Relevance:** TerraWatch calls this "backward integration" (a downstream firm launching satellites to secure differentiated data) ([TerraWatch, 22 Oct 2025](https://newsletter.terrawatchspace.com/state-of-commercial-earth-observation-2025-edition/)). It is one of the few downstream firms to report around $100M ARR.
- **Cross-slice:** EO operators / weather.
- **Credibility:** encyclopedia.

---

### Farmers Edge becomes Corvian (Dec 2025): an agtech pivot from product to managed services

- **What it is:** Farmers Edge (Winnipeg; satellite-imagery precision-ag platform, backed by Fairfax Financial) launched **Corvian**, "the enterprise technology partner for agriculture", on 10 Dec 2025. Corvian offers managed services, strategy, data and AI agents; sustainability and compliance (US Section 45Z clean-fuel credit, Scope 3, regen ag); and insurance and lending (digital adjusting, claims intelligence, risk intelligence). Farmers Edge's own site now redirects to corvian.com ([Corvian press release, 10 Dec 2025](https://corvian.com/2025/12/farmers-edge-announces-corvian/); [Corvian homepage](https://corvian.com/)).
- **Case studies:** Saskatchewan Municipal Hail Insurance "monitoring 4.6 million acres of canola"; Sicredi (Brazil) in-season crop monitoring across 3M+ acres; carbon-intensity scoring for a renewable-fuel provider using data from 16 Ontario growers (Corvian homepage, undated).
- **Problems / pain points (their words):**
  - "Fragmented ecosystems, disconnected tools, and inconsistent data flows across business functions."
  - "Manual workflows and aging systems."
  - "the differentiator is no longer access to data but the ability to execute with it" (VP Strategy Amit Pradhan, 10 Dec 2025).
  - Related blog titles: "Chicken or Egg? The AgTech Adoption Dilemma" (May 2025), "The Next Step for AgTech: Moving Beyond the Product Model" (Sep 2025), "Transforming Crop Insurance with InsurTech: Tackling the Top 5 Industry Challenges" (Jan 2026), "The 3 Barriers to Scope 3" (Oct 2026) ([Corvian newsroom](https://corvian.com/newsroom)).
- **New demand driver:** the US **45Z** clean-fuel production credit pays more for low-carbon-intensity feedstock, which creates demand for verified farm-practice data. Corvian publishes "Section 45Z Tax Credit: How Much Is It Really Worth" (Feb 2026). Rule details are not verified here.
- **Hackathon angle:** "Crop-insurance claim triage": after a hailstorm (NOAA MRMS MESH hail swath), compute Sentinel-2 NDVI drop per field (USDA CDL for crop type) and rank fields for adjuster visits. This is the "digital adjusting" Corvian sells, built on free data.
- **Credibility:** official company pages.

---

### Indigo Ag: soil-carbon credits and biologicals

- **What it is:** Biologicals plus "Carbon By Indigo" soil-carbon credits ("measurable, compliant results") and "Source By Indigo". The homepage lists a press release on "accelerating soil carbon removals for Microsoft", a Google collaboration on Oklahoma watershed health, and a GROWMARK licence of its CLIPS device (all undated). The homepage doesn't mention remote sensing or MRV, and states that projected payments are "general estimates" ([Indigo Ag homepage, accessed 24 Oct 2026](https://www.indigoag.com/)).
- **Problems / pain points:** Soil carbon can't be observed directly from space. MRV relies on models plus sampling plus remote-sensing practice detection, and buyers are sceptical. The history of down-rounds and layoffs was not re-verified here (search budget exhausted), so it is unverified.
- **Hackathon angle:** see Regrow's cover-crop verifier.
- **Credibility:** company page.

---

### Agreena (Copenhagen): soil-carbon programme with satellite dMRV

- **What it is:** Verra-verified "AgreenaCarbon" credits ("now being issued") and Scope 3 "Impact Units" for food companies. Its dMRV combines "satellite imagery, ground truth data, and AI". It claims "5 million+ hectares", 2,500+ farmers and 20 European countries ([Agreena homepage, accessed 24 Oct 2026](https://agreena.com/)).
- **Problems / pain points:** Verifying practices on millions of hectares; ground-truth scarcity; converting credits into supply-chain "insetting" units as offset demand weakens.
- **Data:** Sentinel-1/2 practice detection (tillage, cover crops, residue).
- **Credibility:** company page.

---

### Earth Blox (Edinburgh): nature-risk screening platform

- **What it is:** A nature and climate assessment platform for screening sites, assets and supply locations, with TNFD, EUDR and CSRD solution pages. It uses data from IBAT, NASA, ESA and others, and customers can produce assessments "at volume, without hiring scarce specialists". Customers include Arcadis (joint "NEST" product), South Pole, The Nature Conservancy and Lloyds Banking Group (a 5.1M-hectare farmland analysis). West Fraser built a forestry TNFD methodology on it ([Earth Blox homepage, accessed 24 Oct 2026](https://www.earthblox.io/)).
- **Problems / pain points:** A shortage of remote-sensing specialists; one-off consultant analyses that can't be repeated; auditors need an audit trail; environmental dependencies are "largely absent from financial analysis".
- **Hackathon angle:** "TNFD LEAP in 10 minutes": the user enters a list of facility coordinates. The tool returns proximity to Key Biodiversity Areas and protected areas (WDPA, public; IBAT needs a licence), water stress (WRI Aqueduct), recent tree-cover loss (Hansen), and an LLM-written "Locate" section of a TNFD report.
- **Credibility:** company page.

---

### African Risk Capacity (ARC) and sovereign parametric insurance

- **What it is:** An African Union specialised agency giving governments rapid, predictable disaster financing (parametric sovereign insurance; Africa RiskView). Its homepage headline reads "OVER USD 29 MILLION MOBILISED TO SUPPORT MADAGASCAR" (5 Mar 2026). On 24 Sep 2026 it published "Charting Africa's path to climate resilience: Why the continent must confront its data deficits" ([ARC homepage, accessed 24 Oct 2026](https://www.arc.int/)). Floodbase lists ARC as a partner ([Floodbase](https://www.floodbase.com/)).
- **Problems / pain points:** Data deficits (ARC's own framing), basis risk for drought indices, and few ground stations. The 2016 Malawi controversy, where a satellite drought index initially failed to trigger, is foundational but not re-verified here (unverified).
- **Data:** CHIRPS / TAMSAT rainfall, MODIS / VIIRS NDVI, ESA CCI soil moisture, FEWS NET.
- **Hackathon angle:** "Index vs. reality": for past African drought years, compare a CHIRPS rainfall-index trigger with NDVI anomalies and IPC food-insecurity phases (public FEWS NET / IPC data). Show seasons where the index would have failed farmers.
- **Credibility:** official agency page.

---

### NCX (Natural Capital Exchange): forest-carbon marketplace, now a landowner tool (pivot signal)

- **What it is:** Previously known for forest-carbon "harvest deferral" credits built on a satellite basemap (foundational, not re-verified). The homepage now promotes LandBook, a free tool for landowners to record property history, plans and boundaries. Forest carbon, remote sensing and the basemap aren't mentioned ([NCX homepage, accessed 24 Oct 2026](https://ncx.com/)).
- **Reading:** another nature-credit platform that appears to have moved away from its original credit product (unverified interpretation).
- **Credibility:** company page plus interpretation.

---

### OroraTech: wildfire thermal intelligence for insurers and agencies (cross-slice: EO operators)

- **What it is:** Thermal-infrared wildfire detection from its own constellation plus 35+ thermal sources. It serves civil protection, energy, forestry, carbon and insurance customers, with 800+ users in 25 countries and 500M hectares monitored. The insurance offer covers early detection, spread prediction and burn-severity data "to speed up claims decisions". News: FOREST-20 launch (constellation at 20 satellites, 1 Oct 2026); Alabama Forestry Commission deployment (30 Sep 2026); ICEYE partnership for "full-lifecycle wildfire intelligence" (22 Oct 2026) ([OroraTech homepage, accessed 24 Oct 2026](https://ororatech.com/)).
- **Problems / pain points:** Fire detection latency at night and through smoke; insurers need portfolio exposure in near real time; claims need burn-severity footprints.
- **Hackathon angle:** "Wildfire claims footprint": take FIRMS VIIRS active-fire points plus Sentinel-2 dNBR burn severity for a recent fire, intersect with building footprints, and produce a parcel-level likely-damage list for a mock insurer's first notice of loss (FNOL). Compare with CAL FIRE DINS damage inspection points (public) as ground truth.
- **Credibility:** company page.

---

### Background evidence: why EO for carbon markets, and prior art

- **London Economics, "No Value without Verification: Earth Observation for carbon markets" (27 Sep 2022, Space in Focus #8):**
  - The offset market is "just under 300 million tonnes CO2e" (under 1% of global emissions).
  - Compensate found "only 10% of offsets deliver the verifiable action they promise". CarbonPlan found "$400 million of California offsets" with no real absorption (both as cited by LE).
  - Space-based methods are up to 7x more cost-effective than non-space methods for agriculture and up to 12x for forestry.
  - Gold Standard, VCS and CDM audit every 3–5 years; EO could make auditing quarterly or annual.
  - Barriers: "there is no single verification mechanism"; most market participants lack in-house capacity to analyse satellite data; "EO alone cannot ensure trust and accountability" without enforceable standards.
  - Source: [London Economics](https://londoneconomics.co.uk/blog/publication/no-value-without-verification-earth-observation-for-carbon-markets/).
- **Geoawesome, "Can Satellites Restore Trust in the Carbon Offsetting Market?" (17 Apr 2026, Aleks Buczkowski):** "trust in the carbon offsetting market has been massively eroded". It names Pachama, Sylvera, Albo Climate and CarbonStack (Pléiades Neo individual-tree counting). It is promotional and does not address leakage ([Geoawesome](https://geoawesome.com/can-satellites-restore-trust-in-the-carbon-offsetting-market/)).
- **Prior art to beat at a hackathon:** the PyCon US 2026 poster "Exposing Greenwashing: Satellite ML for Carbon Credit Verification" (Neeraj Pandey). It covers Landsat-8 and Sentinel-2 NDVI/SAVI, an Isolation Forest to flag carbon-stock reports that deviate from observations, and BFAST for sudden deforestation and leakage into buffer zones on REDD+ projects ([PyCon US 2026](https://us.pycon.org/2026/schedule/presentation/131/)). A PyCon Lithuania 2026 talk cites "84% of offset projects fail" with no primary source (unverified) ([pretalx](https://pretalx.com/pycon-lithuania-2026/talk/7LTK9W/)). Implication: "NDVI over a REDD+ polygon" is already done. A team would need a sharper angle, such as synthetic-control baselines, buffer-pool stress tests, or a buyer-facing report card.

---

### Useful open datasets verified while researching this sub-slice

- **Global Flood Database v1** (Cloud to Street / Floodbase team): 913 flood events from 2000-02-17 to 2018-12-10, MODIS-based 250 m maps, licensed **CC BY-NC 4.0**. Earth Engine ID `GLOBAL_FLOOD_DB/MODIS_EVENTS/V1`. Cite Tellman et al., Nature, doi:10.1038/s41586-021-03695-w ([GEE catalog](https://developers.google.com/earth-engine/datasets/catalog/GLOBAL_FLOOD_DB_MODIS_EVENTS_V1)).
- **OpenFEMA NFIP Redacted Claims:** 2.72M claim records with date of loss, reported ZIP, county, flood zone and amounts paid, via API and CSV/Parquet. v2 was frozen on 1 Jun 2026 and is being removed by 15 Oct 2026; **v3** is the successor ([OpenFEMA v2 page](https://www.fema.gov/openfema-data-page/fima-nfip-redacted-claims-v2)).
- **USPVDB v4.0 (Apr 2026):** 6,611 US PV facilities of 1 MW or more with array polygons, public domain ([USGS/LBNL](https://eerscmap.usgs.gov/uspvdb/)). Use it to join solar farms to hail and tornado footprints.
- **Carbon Mapper plume portal** (non-commercial licence), **UNEP methane data** and **Planet Tanager open STAC (CC BY)**: see the methane entry.
- **CTrees JMRV / LUCA / Land Carbon Map** ("open data"; licence terms not checked): see the CTrees entry.

---

## Part A.3 — Defence and intelligence demand (and defence analytics tooling)

The demand side that dominates EO revenue: NGA, NRO, Space Force, NATO, Ukraine, the 2026 Iran war, and the analytics/tooling firms that serve them.

### NGA Luno A and Luno B: buying commercial analytics, not pixels

- **What it is:** The two IDIQ vehicles through which the National Geospatial-Intelligence Agency (NGA) buys *unclassified commercial analytic services*, i.e. computer-vision detections, change alerts and monitoring products, rather than raw imagery. Luno A (Sept 2024) has a $290M ceiling and 10 vendors. Luno B (Jan 2025) has a $200M ceiling and 13 vendors. The combined ceiling is $490M, and both run five years. Vendors compete for each delivery order.
  - Luno A vendors: Airbus U.S. Space & Defense, Booz Allen Hamilton, BlackSky, BlueHalo, CACI, Electromagnetic Systems, Maxar Intelligence (now Vantor), NV5 Geospatial, Royce Geospatial Consultants, Ursa Space Systems.
  - Luno B vendors: all ten above plus Planet Labs, BAE Systems and Deloitte.
- **Delivery orders found so far** (from the NGA release of 2 July 2025, unless noted):
  - Luno A, Maxar, *Facility and Object Monitoring*: $3.5M.
  - Luno A, Electromagnetic Systems, *Feature ID*: $3.6M.
  - Luno A, Ursa, *Global Awareness Tracker*: $13.8M.
  - Luno A, BlackSky, *Facility and Object Monitoring 2*: $24.4M. Scope: "detect objects (e.g., aircraft, ships, ground equipment and railcars) as well as object change at specific areas of interest".
  - Luno B, NV5, *Almanac*: $4.5M. Scope: human geography baseline data.
  - Luno B, Ursa, *TrueSight*: $21M. Scope: "detection, identification, analysis and alerts describing change and/or movement of objects using commercial sources and automated models for domain awareness".
  - Luno B, Planet, *Advanced Analytics for Maritime Operations and Reconnaissance*: $12.8M (Oct 2025). Scope: Asia-Pacific maritime domain awareness (MDA) built on PlanetScope plus SynMax *Theia*. Planet says it covers "illegal, unreported, and unregulated fishing, illicit ship-to-ship transfers, and vessel spoofing", with near-daily revisit.
  - Luno B, Vantor, global change detection: about $5M (reported Feb 2026).
- **Problems / pain points:**
  - NGA's stated reason for the vehicles is that it needs *answers at scale* (objects, change, movement), not more images for analysts to look at.
  - The order titles show what the demand looks like: object counts at facilities, feature ID, global "awareness trackers", change/movement alerts, maritime anomalies, human geography baselines.
  - Devin Brande, director of NGA Commercial Operations: "We see the mission impact of commercial GEOINT every day."
  - The orders are small (most are $3–25M) compared with imagery buys, so analytics is still a modest slice of spend.
  - **Getting analytics actually used after award is the hard part.**
    - Brande at GEOINT 2025: "It's one thing to do the contract and bring that on board. It's another thing to make sure that users needs it."
    - He says NGA's "mission users are very heterogeneous", so delivery has to put analytics "at the point of mission need".
    - NGA hoped for up to 10 Luno orders in FY2025, with most tasking done by early 2026, then a shift to integration.
  - **Example: the Ursa *Global Oil Awareness Tracker*** ($13.8M, May 2025) analyses SAR imagery of petroleum production and storage facilities. Floating-roof tank fill levels can be read from shadows or SAR, a classic commodity-intelligence use case.
- **How they're trying to solve it:**
  - Each order is competed among pre-qualified vendors ("agile acquisition strategy to quickly respond to customer needs").
  - The NGA release says each contract "applies GEOINT artificial intelligence to provide decision advantage".
- **Data:** None of the outputs are public. Public proxies for the same tasks: Sentinel-1 SAR and Sentinel-2 optical (free, Copernicus licence), the xView / xView2 / xView3 datasets, the SpaceNet datasets, and AIS feeds (Global Fishing Watch).
- **Off-the-shelf tech:** Object detectors on EO data (YOLO-family models, the SAM/SAM2 segmentation models, EO foundation models such as Prithvi, Clay and SatMAE), change-detection libraries (torchgeo), and SAR vessel detection (xView3 winning solutions).
- **Hackathon angle:** Build an open "mini-Luno" order. Example: "Facility and Object Monitoring" for a port or airbase, using Sentinel-1 and Sentinel-2. Show weekly counts of ships, aircraft or railcars with a change alert, plus a confidence score and an image chip for each alert. The pitch is that NGA pays $3–25M per order for this, while journalists, NGOs and small states get nothing comparable.
- **Credibility:** Official (NGA press release PDF, opened and text-extracted), reputable trade press.
- **Sources:**
  - [NGA release 2025-10, "NGA announces new Luno A and Luno B delivery order awards" (2 Jul 2025, PDF)](https://www.nga.mil/assets/files/25-10_Release_Luno_A_B_Update.pdf)
  - [NGA: "NGA awards $290 million Luno A commercial data contract" (Sept 2024)](https://www.nga.mil/news/NGA_awards_$290_million_Luno_A_commercial_data_con.html)
  - [Intelligence Community News: Luno A awardees (Sept 2024)](https://intelligencecommunitynews.com/nga-awards-luno-a-commercial-data-contract-to-10-companies/)
  - [Via Satellite: NGA selects 13 companies for Luno B (15 Jan 2025)](https://satellitetoday.com/government-military/2025/01/15/nga-selects-13-companies-for-luno-b-program-for-geoint-data)
  - [Geo Week News: Luno B selectees](https://www.geoweeknews.com/articles/nga-announces-selectees-for-200m-luno-b-idiq/)
  - [Via Satellite: Planet nabs $13M Luno B award (17 Oct 2025)](https://www.satellitetoday.com/imagery-and-sensing/2025/10/17/planet-nabs-13m-award-under-ngas-luno-b-for-data-analytics/)
  - [Via Satellite: NGA awards Vantor $5M for global change detection (5 Feb 2026)](https://www.satellitetoday.com/government-military/2026/02/05/nga-awards-vantor-5-million-for-global-change-detection-under-luno-b-contract/)
  - [SatNews: NGA's new Luno A / Luno B delivery orders (6 Jul 2025)](https://news.satnews.com/2025/07/06/ngas-new-luno-a-luno-b-delivery-orders)
  - [Breaking Defense, T. Hitchens: "NGA hopes to award up to 10 Luno commercial analytics task orders this year" (23 May 2025)](https://breakingdefense.com/2025/05/nga-hopes-to-award-up-to-10-luno-commercial-analytics-task-orders-this-year/)

---

### NGA Maven (GEOINT AI program of record) and Palantir's Maven Smart System

- **What it is:** NGA took over Project Maven's computer-vision (CV) work. NGA Maven produces CV models for object detection, tracking, classification and pattern detection on imagery and other ISR sensors. Palantir's *Maven Smart System* (MSS) is the separate all-source software that fuses those detections with other data and is used for targeting workflows.
- **Problems / pain points:**
  - Detection volume and speed for targeting. The Army wants units able to make "1,000 high-quality targeting decisions in one hour".
  - Labelled training data is the bottleneck, which is why NGA ran a data-labelling competition (Sequoia).
    - **Sequoia was awarded on 26 Nov 2025 to Enabled Intelligence**, a VC-funded startup founded in 2020 that labels data for classified systems. It is worth up to $708M over a maximum of seven years.
    - Partners include BAE Systems, Vantor and Whiteboard Federal.
    - NGA officials call it the largest US government AI data-labelling project to date.
    - The work is labelling "reams of satellite and airborne imagery" so CV models can find targets.
  - Whitworth (June 2025) said meeting NGA Maven demand has been a major challenge.
- **Scale (GEOINT 2025, 22 May 2025, NGA Director VADM Frank Whitworth):**
  - "20,000 active users through more than 35 service and combat and command tools across three security domains."
  - "The user base has more than quadrupled since March of last year, and more than doubled since January."
  - Exercise targeting timelines dropped "from hours to minutes".
  - An 18th Airborne Corps cell of about 20 people matched a 2003 Iraq targeting cell of about 2,000.
  - Whitworth said GEOINT AI has "entered into an unchained phase".
- **Contracts:**
  - Palantir: $513M from CDAO in 2024 to expand MSS.
  - Army: $795M in new MSS licences (May 2025).
  - NGA: $28M to Palantir to extend MSS to its analysts.
- **How they're trying to solve it:**
  - Make it a program of record.
  - Run large-scale labelling (Sequoia).
  - Accredit models (AGAIM, see below).
  - Mine NGA's own archive of images paired with analyst reports as multimodal training data. Mark Munsell (NGA data and digital innovation) calls it an "AI gold mine" (Aug 2024).
- **Data:** All classified. Public analogues: xView (60 object classes, WorldView-3), DOTA, FAIR1M, and SpaceNet.
- **Off-the-shelf tech:** Open-vocabulary detectors (Grounding DINO, OWL-ViT), EO foundation models, and vision-language models (VLMs) for imagery captioning.
- **Hackathon angle:** Treat the "analyst report + image" pairing as a public problem. Use open Sentinel-2 chips plus public OSINT write-ups (Bellingcat, CSIS satellite briefs) to build a demo that drafts a structured analyst note from a before/after image pair, with every claim linked to a pixel region.
- **Credibility:** Reputable defence press quoting the NGA director on the record. Wikipedia for background.
- **Sources:**
  - [Breaking Defense, T. Hitchens: "AI 'unchained': NGA's Maven tool 'significantly' decreasing time to targeting" (22 May 2025)](https://breakingdefense.com/2025/05/ai-unchained-ngas-maven-tool-significantly-decreasing-time-to-targeting-agency-chief-says/)
  - [Breaking Defense: "NGA seeks help training AI to translate imagery for targeting intel" (Sept 2024)](https://breakingdefense.com/2024/09/nga-seeks-help-training-ai-to-translate-imagery-for-targeting-intel/)
  - [Breaking Defense: "'AI gold mine': NGA aims to exploit archive of satellite images, expert analysis" (Aug 2024)](https://breakingdefense.com/2024/08/ai-gold-mine-nga-aims-to-exploit-archive-of-satellite-images-expert-analysis/)
  - [GovConWire: NGA's $700M AI contract opportunity (Sept 2024)](https://www.govconwire.com/2024/09/what-you-should-know-about-ngas-700m-ai-contract-opportunity/)
  - [Breaking Defense: "Startup Enabled Intelligence nabs NGA's $708 million AI training contract" (26 Nov 2025)](https://breakingdefense.com/2025/11/startup-enabled-intelligence-nabs-ngas-708-million-ai-training-contract/)
  - [Wikipedia: Project Maven](https://en.wikipedia.org/wiki/Project_Maven)

---

### "Too much data, not enough analysts": the NGA 8-million-analysts figure

- **What it is:** The most-quoted statement of the defence EO bottleneck. An NGA speech at the 31st SmallSat conference (2017, Logan, Utah) said manually exploiting the imagery expected over the next 20 years would need about **eight million imagery analysts**, which the speaker called "clearly not a viable solution". Federal News Network separately reported an NGA estimate of **6 million** analysts. NPR (2020) reported that NGA receives "more than 1 million images a day" from partners.
- **Problems / pain points:**
  - Collection has outrun exploitation.
  - Most images are never looked at by a human.
- **How they're trying to solve it:** Automation (Maven), buying analytics instead of imagery (Luno), and tip-and-cue between sensors (see below).
- **Data:** Context only. Any persistent-monitoring stack (Sentinel-1 every 6–12 days, Sentinel-2 every 5 days, PlanetScope daily) shows the same imbalance.
- **Hackathon angle:** Build a triage tool that ranks which of today's N new scenes over a set of AOIs (areas of interest) a human should look at first, and show the analyst-hours saved.
- **Credibility:**
  - The NGA page exists but returned 403 when fetched, so the eight-million wording comes from the search-result summary of that page.
  - The NPR figure comes from the search-result summary (the NPR page timed out).
  - The 6M vs 8M discrepancy is noted in coverage and is unexplained. Treat both as rhetorical estimates.
- **Sources:**
  - [NGA: "Small Satellites – Big Data" (speech text, 2017; not fetched, 403)](https://www.nga.mil/news/Small_Satellites_-_Big_Data.html)
  - [NPR: "A Spy Agency's Challenge: How To Sort A Million Photos A Day" (12 Mar 2020)](https://www.npr.org/2020/03/12/807499102/a-spy-agencys-challenge-how-to-sort-a-million-photos-a-day)
  - [Federal News Network (6 million analysts figure)](https://federalnewsnetwork.com/?p=2070733)

---

### NGA AGAIM: accreditation of GEOINT AI models (the trust and verification problem)

- **What it is:** The *Accreditation of GEOINT AI Models* pilot, launched Aug–Sep 2024. It provides a "standardized evaluation framework" for models across the National System for Geospatial Intelligence (NSG), covering risk management, responsible AI, trustworthiness, interoperability, and recognising high-quality models.
- **Problems / pain points:**
  - Detections from many vendors' models feed targeting and policy decisions. Nobody has a common way to judge how good a model is, how it was tested, or how it degrades on new sensors and regions.
  - NGA's release: "AGAIM will expand the responsible use of GEOINT AI models."
  - Coverage says accredited models will be required for NGA systems. Whether commercial vendors adopt the standard independently "remains to be seen".
  - A later MeriTalk item (undated in search results) says NGA had accredited two models: one from its own Maven program and one from an IC partner.
- **How they're trying to solve it:** Process accreditation of each program's model-development and test procedures.
- **Data:** Not public.
- **Off-the-shelf tech:** Model cards, datasheets for datasets, and ML evaluation harnesses. The torchgeo benchmark suites and GEO-Bench serve as public test sets.
- **Hackathon angle:** Build a public "model report card" for EO detectors. Take two or three open ship or building detectors and test them across regions, seasons and sensors (Sentinel-2 vs NAIP vs Planet samples) to show where they break: a mini-AGAIM for open models.
- **Credibility:** Reputable trade press quoting an NGA release.
- **Sources:**
  - [MeriTalk: "NGA launches new AI accreditation pilot" (4 Sept 2024)](https://www.meritalk.com/articles/nga-launches-new-ai-accreditation-pilot/)
  - [DefenseScoop: NGA pilot program to standardize CV model accreditation (30 Aug 2024)](https://defensescoop.com/2024/08/30/nga-pilot-program-geoint-standardize-computer-vision-model-accreditation-agaim)
  - [Via Satellite: NGA launches accreditation pilot for GEOINT AI models (4 Sept 2024)](https://satellitetoday.com/government-military/2024/09/04/nga-launches-accreditation-pilot-for-geoint-ai-models)
  - [Breaking Defense: NGA slates $700M for AI data labeling, launches standard model push (Sept 2024)](https://breakingdefense.com/2024/09/nga-slates-700m-for-ai-data-labeling-launches-standard-model-push/)

---

### NGA under LTG Michele Bredenkamp (2026): "AI-first" blueprint and a Rapid Capabilities Office

- **What it is:**
  - LTG Michele Bredenkamp, NGA's "newly confirmed Director", succeeded VADM Whitworth. Wikipedia, as reported in search results, says Whitworth led NGA until November 2025.
  - In her first major speech (GEOINT 2026, Denver, 6 May 2026) she said NGA is finalising an AI framework, its "blueprint for becoming an AI first organization". It covers operationalising GEOINT and AI, modernising business operations, "revolutionizing acquisition", partnerships, and AI governance.
  - She created a **Rapid Capabilities Office** under Chris Parrett that "will take more acquisition risk to reduce our operational risk", using Other Transaction Authorities.
  - An **advanced-analytics industry day** was planned for July 2026, with classified and unclassified forums.
- **Problems / pain points:**
  - Acquisition speed.
  - Workforce AI literacy: "every employee is equipped for human machine teaming excellence with AI literacy tools".
  - Keeping humans in the loop at scale: "AI handles the volume, the speed, the pattern recognition across massive data sets." Also: "AI does not replace human judgment. It amplifies it."
- **How they're trying to solve it:** The RCO, the AI blueprint, and "human insight and machine speed".
- **Hackathon angle:** Pitch to the "human-machine teaming" problem. Build an interface where the machine pre-screens and a human confirms or rejects alerts in seconds. Every confirmation becomes a new label, closing the labelling-cost loop.
- **Credibility:** Reputable defence press reporting an on-the-record keynote, plus an official event page.
- **Sources:**
  - [Breaking Defense, T. Hitchens: "AI 'blueprint' coming soon to NGA to help 'operationalize' GEOINT" (7 May 2026)](https://breakingdefense.com/2026/05/ai-blueprint-coming-soon-to-nga-to-help-operationalize-geoint/)
  - [USGIF: NGA Director LTG Michele Bredenkamp to keynote GEOINT Symposium 2026](https://usgif.org/?p=59575)

---

### NGA "machine-generated GEOINT" label: provenance of AI-made intelligence products

- **What it is:**
  - Since 2025 NGA disseminates some intelligence products with **no human hands** involved. They carry an automatic, standardised disclosure template ("machine-generated GEOINT") showing the type and level of AI involvement, e.g. whether the image exploitation or only the dissemination was machine-generated.
  - VADM Whitworth (June 2025): "No human hands actually participate in that particular template and that particular dissemination."
  - He called the template "a living, breathing template, a real piece of art".
  - NGA declined to release the template.
- **Problems / pain points:**
  - Commanders, the defence secretary and the president need to know when a product is machine-made so they can judge it.
  - Whitworth calls for "AI humility" in targeting and navigation safety, where "a human needs to double check".
  - Data volume: "That's a lot of data… So we need some help."
- **How they're trying to solve it:** Automatic provenance labels, plus humans as "coaches and mentors" who refine the models.
- **Data:** Not public.
- **Off-the-shelf tech:** C2PA content credentials (provenance manifests), STAC metadata extensions for processing lineage (`processing:*`), and W3C PROV.
- **Hackathon angle:** **Provenance for EO-derived claims.** Build an open "nutrition label" for any satellite-derived finding, attached as C2PA plus STAC metadata. It records the scene IDs, sensor, dates, model and version, confidence, and human review status. Pair it with a verifier that checks the cited scenes really exist in the public archive (Copernicus or Landsat STAC), which also helps against fake satellite images.
- **Credibility:** Reputable defence press quoting the NGA director on the record.
- **Sources:**
  - [Breaking Defense, S. Freedberg: "'No human hands': NGA circulates AI-generated intel, director says" (5 Jun 2025)](https://breakingdefense.com/2025/06/no-human-hands-nga-circulates-ai-generated-intel-director-says/)

---

### NRO commercial imagery: EOCL, the new Commercial Solutions Opening (CSO), SAR "RCA" contracts, and AI explainability

- **What it is:** The National Reconnaissance Office (NRO) is the main US government buyer of commercial imagery.
  - **EOCL (Electro-Optical Commercial Layer):** awarded May 2022 to Maxar (now Vantor), with smaller awards to Planet and BlackSky. TerraWatch puts Maxar's share at $3.24B over ten years: a $1.5B firm five-year base plus $1.74B in options through 2032. It calls it "the largest commercial imagery acquisition the agency has ever made." BlackSky's Q3 2022 record revenue was attributed to EOCL.
  - **Commercial Solutions Opening (CSO):** issued July 2025, with a revolving five-year window and unsolicited proposals accepted. It covers EO, SAR, hyperspectral, RF geolocation and LIDAR. Awards so far:
    - Feb 2026: HEO (non-Earth imaging of satellites), SatVu (thermal MWIR) and Sierra Nevada Corp (RF geolocation).
    - May 2026 (GEOINT): EarthDaily (EO), ICEYE (RF geolocation) and Pixxel (hyperspectral).
  - **Radar Commercial Augmentation (RCA):** Aug 2026 contracts to Capella, ICEYE US and Umbra, succeeding the Dec 2025 Commercial Radar Capabilities study contracts. They have "defined performance thresholds and continuous improvement goals" and run a one-year base plus two option years to July 2029. The NRO says they integrate commercial SAR with its classified ISR systems.
- **Problems / pain points:**
  - *AI explainability and verification.* Outgoing NRO Director Chris Scolese at GEOINT 2026 (May 2026):
    - "AI 'explainability' is a major concern for us. It's still an open area of research."
    - "We must understand how we got to the product."
    - "We need to be able to look inside the black box of AI and verify the prediction and outputs of models are correct."
    - Verifying analysis of sensor data is harder than verifying spacecraft operations, because it often happens in real time.
  - *Scale.* Scolese: "As the size of our constellation grows, we will exceed the capacity of what human operators can effectively manage." He also cited "exponentially growing data volumes".
  - *Integration of purchased data into user workflows.* Pete Muend, head of the NRO Commercial Systems Program Office: "there's probably even a little bit more work to do to make sure that when we buy data…" it fits the needs of the Space Force's TacSRT program.
  - *Budget uncertainty.* NRO says further CSO awards come "budget permitting".
  - *Concentration risk for the industry.* TerraWatch notes EOCL "comes up for recompete in roughly the window Advent [Vantor's owner] would be exiting".
- **FY2026 / FY2027 budget proposals:**
  - The search budget ran out before primary sources on proposed **EOCL cuts** in the FY2026 request could be opened. This item is **unverified**; follow up with SpaceNews or Breaking Defense coverage from mid-2025.
  - Confirmed (White House FY2027 budget, via TerraWatch, Apr 2026): NASA $18.8B (−23%), NASA Earth science −52% ($2.15B → $1.02B), "one final Landsat satellite", and $109M to move Landsat toward a commercial solution.
  - TerraWatch (Dec 2025) also reports the administration proposed cutting NASA Earth Science by 50% and NOAA's research arm by 74%.
  - These are civil cuts, but they shift more weight onto commercial data and analytics.
- **How they're trying to solve it:**
  - Continuous on-ramps (CSO) instead of one big layer contract.
  - A GPU "Ultra-Dense Environment" where NRO and industry models are tested. Scolese invited companies to help develop validation methods.
  - NRO and Space Force signed an agreement in spring 2025 to share commercial ISR acquisition authority and access.
- **Data:** Classified. Public analogues: Capella, Umbra and ICEYE open SAR data programmes (Umbra and Capella have open-data S3 buckets, to verify for the Datasets slice), and Sentinel-1.
- **Off-the-shelf tech:** Explainability for vision models (Grad-CAM, SHAP for rasters, attention maps), conformal prediction for calibrated confidence, and change-detection uncertainty maps.
- **Hackathon angle:** Build an "explainable detection" demo. For each AI alert on SAR or optical imagery, show the evidence pixels, the before/after chips, a calibrated confidence, the model and data lineage, and a one-click "why" in plain language. This responds directly to the NRO director's "look inside the black box" quote.
- **Credibility:** Reputable defence press quoting officials on the record. TerraWatch is an analyst newsletter that cites the Maxar 10-K. The EOCL budget-cut claim is unverified.
- **Sources:**
  - [Breaking Defense: "AI 'explainability' is a 'major concern' for National Reconnaissance Office: Director" (7 May 2026)](https://breakingdefense.com/2026/05/ai-explainability-is-a-major-concern-for-national-reconnaissance-office-director/)
  - [Breaking Defense: "HEO, SatVu, Sierra Nevada nab first of NRO's new commercial imagery contracts" (10 Feb 2026)](https://breakingdefense.com/2026/02/heo-satvu-sierra-nevada-nab-first-of-nros-new-commercial-imagery-contracts/)
  - [Breaking Defense: "NRO awards three new contracts for commercial satellite data" (4 May 2026)](https://breakingdefense.com/2026/05/nro-awards-three-new-contracts-for-commercial-satellite-data/)
  - [Breaking Defense: "NRO issues 3 SAR satellite data providers 'rigorous' new contracts" (5 Aug 2026)](https://breakingdefense.com/2026/08/nro-issues-3-sar-satellite-data-providers-rigorous-new-contracts/)
  - [TerraWatch: "Three Years On: Analysing Advent's Maxar Acquisition" (22 May 2026)](https://newsletter.terrawatchspace.com/three-years-on-analysing-advents-maxar-acquisition/)
  - [Via Satellite: "EOCL Contract Propels BlackSky to Record Q3 Revenue" (8 Nov 2022)](https://www.satellitetoday.com/finance/2022/11/08/eocl-contract-propels-blacksky-to-record-q3-revenue/)
  - [TerraWatch Essentials, 13 Apr 2026 (FY2027 NASA budget)](https://newsletter.terrawatchspace.com/earth-observation-essentials-april-13-2026/)
  - [White House FY2027 budget PDF (linked by TerraWatch; not opened)](https://www.whitehouse.gov/wp-content/uploads/2026/04/budget_fy2027.pdf)
  - [TerraWatch Essentials, 17 Dec 2025](https://newsletter.terrawatchspace.com/earth-observation-essentials-december-17-2025/)

---

### Vantor (formerly Maxar Intelligence): from pixels to "spatial intelligence" software

- **What it is:**
  - Maxar's imagery and intelligence business, owned by Advent since 2023 and renamed **Vantor** in October 2025.
  - The spacecraft half became **Lanteris**. TerraWatch reports Intuitive Machines later bought Lanteris for $800M ($450M cash and $350M in LUNR stock).
  - Vantor's stack has four layers: **Vivid** (data foundation), **Tensorglobe** (platform: automated collection planning, high-resolution 3D models, analysis), and **Sentry** and **Raptor** (applications).
  - Partners include Anduril, Saab, Windward, Niantic Spatial and Google.
  - New constellations announced in 2026: "Vantage" / "Pulse", at 20 cm and at 40 cm with rapid revisit.
- **Problems / pain points:**
  - Revenue "historically concentrated toward the US government". CEO Dan Smoot says 90% is recurring, but TerraWatch says that base is "overwhelmingly government, not commercial".
  - US export restrictions slow diversification to allies.
  - EOCL recompete risk.
  - Brand baggage. CPO Peter Wilczynski: "That name carried a lot of connotation and held a lot of baggage."
  - TerraWatch calls customer concentration "the most likely thing to cap" the exit multiple.
  - Vantor won only a small analytics order: $5.3M Luno B change detection (Feb 2026).
- **How they're trying to solve it:**
  - Treat satellites as infrastructure. TerraWatch: "the value sits in the software on top".
  - Smoot's goal: "Solutions that people want to subscribe to."
  - Wilczynski compares Tensorglobe to Amazon turning internal infrastructure into AWS.
- **Data:**
  - Commercial and licensed.
  - **Open Data Program** for disasters: free pre/post-event imagery under CC BY-NC (to verify for the Datasets slice).
  - News Bureau imagery for media.
- **Hackathon angle:** Use Vantor/Maxar Open Data disaster imagery to build a damage-assessment "answer engine" for a non-expert (e.g. a city emergency manager). It answers "which roads into X are blocked?" with evidence chips.
- **Credibility:** Trade press interviews and an analyst newsletter.
- **Sources:**
  - [Payload: "Maxar Companies Rebrand to Lanteris, Vantor" (1 Oct 2025, updated 13 Oct 2025)](https://payloadspace.com/maxar-companies-rebrand-to-lantaris-vantor/)
  - [TerraWatch: "Three Years On: Analysing Advent's Maxar Acquisition" (22 May 2026)](https://newsletter.terrawatchspace.com/three-years-on-analysing-advents-maxar-acquisition/)
  - [TerraWatch Essentials, 13 Oct 2025 (citing SpaceNews on the rebrand)](https://newsletter.terrawatchspace.com/earth-observation-essentials-october-13-2025/)
  - [Vantor blog: expansion of its constellation, Vantage / Pulse (2026; linked by TerraWatch, not opened)](https://vantor.com/blog/vantor-introduces-expansion-of-its-satellite-constellation-vantage-pulse/)
  - [Via Satellite: Vantor $5M Luno B (5 Feb 2026)](https://www.satellitetoday.com/government-military/2026/02/05/nga-awards-vantor-5-million-for-global-change-detection-under-luno-b-contract/)

---

### Iran war 2026: commercial imagery blackouts and delays (Planet 14-day delay, then indefinite withholding; Vantor access controls)

- **What it is:**
  - During the 2026 Iran conflict, Planet issued a customer notice on 9 March 2026 imposing a **14-day delay** on imagery of Iran, nearby military bases, Gulf states and "existing conflict zones". Planet said it wanted to ensure "our imagery is not tactically leveraged by adversarial actors". A spokesperson called it "an independent decision by Planet".
  - Via Satellite (Oct 2026) reports that on 4 April Planet moved to withholding imagery of Iran and the surrounding zone **indefinitely**, retroactive to 9 March. It said the US government had asked commercial providers to do the same.
  - Vantor applies "enhanced access controls during times of geopolitical conflict" and slowed News Bureau distribution over the Persian Gulf.
  - Three industry sources told Breaking Defense that US officials had quietly urged firms to voluntarily limit access.
  - Airbus kept supplying battle-damage imagery. The US has no control over foreign providers.
  - Chinese firm **MizarVision** (AI on open-source imagery) published images of the US build-up at Middle Eastern bases (Global Times, 30 Jan 2026) and kept selling conflict imagery, per a Washington Post report of 4 Apr 2026 cited by Breaking Defense.
- **Problems / pain points:**
  - **Journalists, humanitarians and OSINT analysts lose their verification source exactly when it matters.** The BBC covered "the concerns of humanitarian organisations and journalists" (per TerraWatch; the BBC page itself was not fetchable).
  - **Policy whiplash.** In 2022 US officials praised firms for helping Ukraine. In 2026 they quietly asked for restraint.
  - **Space Force Chief Gen. Saltzman:** "We just have to recognize and adapt to the changing battle space." Commercial imagery access "is the new battle space".
  - **Buyers now ask "who can switch this off?"** Via Satellite op-ed (Oct 2026): "Anyone selling into the region who does not have a good answer to that is competing on price alone."
- **How they're trying to solve it:**
  - Vendors use voluntary delays and access controls.
  - OSINT groups turn to free Copernicus data (see the Bellingcat PWTT entry).
  - Gulf buyers write continuity terms into contracts and want in-country ground segments and local processing.
- **Data:** Sentinel-1 and Sentinel-2 (free, unrestricted) and Landsat. Airbus is commercial. MizarVision and Chinese providers are cross-slice.
- **Off-the-shelf tech:** The Bellingcat PWTT Earth Engine app, Sentinel Hub EO Browser, and the Copernicus Data Space Ecosystem.
- **Hackathon angle:** A "blackout-proof monitor": an open-data-only pipeline (Sentinel-1 + Sentinel-2) that gives journalists or NGOs a ranked list of likely-changed sites in a restricted region, with an honest confidence and resolution disclaimer. It could also track which regions are currently delayed or restricted by which vendor, which is a pricing and availability transparency problem.
- **Credibility:** Reputable defence press with named and anonymous sources, a trade-press op-ed, and a BBC item seen only via TerraWatch.
- **Sources:**
  - [Breaking Defense, T. Hitchens: "Nowhere to hide: Iran war spotlights military challenges posed by space-based remote sensing" (13 Apr 2026)](https://breakingdefense.com/2026/04/nowhere-to-hide-iran-war-spotlights-military-challenges-posed-by-space-based-remote-sensing/)
  - [Via Satellite opinion, K. Kelevitch: "The Question Gulf Buyers Are Now Asking: Who Can Switch This Off?" (22 Oct 2026)](https://www.satellitetoday.com/opinion/2026/10/22/the-question-gulf-buyers-are-now-asking-who-can-switch-this-off/)
  - [BBC article on Planet's restricted access (Apr 2026; linked by TerraWatch, not fetchable)](https://www.bbc.com/news/articles/c5y721yqe6ro)
  - [TerraWatch Essentials, 13 Apr 2026](https://newsletter.terrawatchspace.com/earth-observation-essentials-april-13-2026/)

---

### Ukraine: commercial imagery as a war input, and the March 2025 Maxar / GEGD cutoff

- **What it is:**
  - Ukraine is the reference case for commercial EO in war. Planet's CSO Robbie Schingler (Oct 2026) calls Ukraine a leading user of commercial GEOINT, treating satellites "like a reprogrammable asset".
  - **Early March 2025 cutoff:** after the Trump administration "paused" intelligence and military aid to Kyiv, Ukraine lost access to commercial imagery for barely more than a week.
    - Breaking Defense's 2025 review says **NGA** cut Ukraine's access to its database of unclassified commercial imagery. That is the Global Enhanced GEOINT Delivery (GEGD) program run by Maxar; the GEGD name is inferred, not stated in the fetched text.
    - Wikipedia says Maxar "shuts down access… following request from the Trump administration", citing Politico Europe, 7 Mar 2025.
    - Breaking Defense called it "a veritable shot heard 'round the world". It spurred EU and ESA initiatives and pushed NATO allies toward "strategic autonomy" in space.
  - **ICEYE:**
    - Since Aug 2022 Ukraine has had access to an ICEYE SAR satellite, bought via the Serhiy Prytula Charity Foundation.
    - Since Nov 2024, Germany's MoD has paid for ICEYE–Rheinmetall data sales to Ukraine.
    - In Oct 2026 ICEYE and Nokia partnered with Ukraine's MoD on sovereign satcom.
  - **NATO:** in Oct 2026 Ukraine joined the NATO Support and Procurement Agency (NSPA) Security Cooperation Support Partnership, which opens NATO procurement to Ukrainian firms. The article does not say whether this covers EO.
- **Problems / pain points:**
  - **Dependency and switch-off risk.** One political decision cut a nation's imagery feed. This, together with the Starshield slowdown in Ukraine in Oct 2026, is why Gulf and European buyers now insist on sovereign control (see Via Satellite op-ed).
  - **Volume.** Ukraine's own AI (Avengers) runs on drone and fixed-camera video, not satellites, at about 12,000 targets per week.
- **How they're trying to solve it:**
  - Diversify suppliers (European SAR via ICEYE, funded by Germany).
  - Ukraine's own data-fusion platform (Delta, see next entry).
  - Sovereign constellations for allies: ICEYE sold dedicated SAR satellites to Poland, the Netherlands, Finland, Portugal, Sweden, Greece and Germany (€1.76B Rheinmetall–ICEYE deal, Dec 2025).
- **Data:** Sentinel-1 and Sentinel-2 for open analysis. The UNOSAT damage datasets for Ukraine; the PWTT validation used them.
- **Hackathon angle:** A "supplier-independence dashboard" for a small state or NGO: given AOIs, show which revisit and resolution can be met using only open data vs each commercial provider, and the gap.
- **Credibility:** Wikipedia (with a verification tag dated Mar 2026; the cited Politico article could not be fetched), company press releases, and trade press.
- **Sources:**
  - [Breaking Defense: "Five stories that surprised the space world: 2025 review" (Dec 2025)](https://breakingdefense.com/2025/12/five-stories-that-surprised-the-space-world-2025-review/)
  - [Wikipedia: Maxar Technologies (accessed 24 Oct 2026; cites Politico, 7 Mar 2025)](https://en.wikipedia.org/wiki/Maxar_Technologies)
  - [Politico Europe: "US satellite company Maxar reportedly cuts off Ukraine's access to imagery" (7 Mar 2025; not fetchable)](https://www.politico.eu/article/us-satellite-company-maxar-cuts-off-ukraine-access-imagery-report-says/)
  - [Wikipedia: ICEYE (accessed 24 Oct 2026)](https://en.wikipedia.org/wiki/ICEYE)
  - [ICEYE newsroom (accessed 24 Oct 2026)](https://www.iceye.com/newsroom)
  - [Via Satellite: Planet CSO Robbie Schingler on sovereignty and onboard AI (20 Oct 2026)](https://www.satellitetoday.com/earth-observation/2026/10/20/planet-cso-robbie-schingler-talks-sovereignty-onboard-ai-and-the-launch-squeeze/)
  - [Via Satellite: Ukraine joins NATO support partnership (22 Oct 2026)](https://www.satellitetoday.com/government-military/2026/10/22/ukraine-joins-nato-support-partnership-to-open-new-doors-for-space-companies/)

---

### Ukraine's Delta situational-awareness system and the Avengers AI platform

- **What it is:**
  - A cloud-native battlefield-management system. It fuses reports from reconnaissance units, drones, sensors, satellite imagery and partner intelligence on a live map.
  - It was developed by the Ukrainian Center for Innovation and Development of Defense Technologies with the NGO Aerorozvidka, and first tested in 2017 under a NATO initiative.
  - **Avengers** (within the Vezha module) runs AI detection on drone and fixed-camera video.
  - MoD of Ukraine, London Defence Conference, 13 May 2025: Avengers "can identify 70% of enemy vehicles and equipment in video streams", taking 2.2 seconds per unit.
  - It passed an independent cybersecurity assessment in early 2026.
- **Problems / pain points:**
  - A 70% detection rate means many misses: camouflage, low visibility, terrain.
  - Phishing and malware attacks on Delta users (Dec 2022).
  - Satellite imagery's exact role is not disclosed.
- **How they're trying to solve it:** Expand cloud capability, run AI directly on drones, and demonstrate to NATO (TIDE Sprint 2025, Helsinki).
- **Data:** Not public.
- **Hackathon angle:** Delta is the model of "fusion beats any single sensor". A civilian analogue would fuse Sentinel alerts, geolocated social-media posts and news on one map with provenance for each item, e.g. for disaster response.
- **Credibility:** Ukrainian government (official but unverified independently), CSIS analysis cited via Wikipedia, and Wikipedia.
- **Sources:**
  - [MoD of Ukraine: "Enemy equipment detected in 2 seconds…" (13 May 2025)](https://mod.gov.ua/en/news/enemy-equipment-detected-in-2-seconds-the-ministry-of-defence-showcased-delta-and-avengers-systems-at-the-london-defence-conference)
  - [Wikipedia: Delta (situational awareness system) (accessed 24 Oct 2026)](https://en.wikipedia.org/wiki/Delta_(situational_awareness_system))
  - [CSIS, K. Bondar: "Ukraine's Delta: Lessons for Software-Defined Warfare" (11 Dec 2024; cited by Wikipedia, page returned 404 when fetched)](https://www.csis.org/analysis/ukraines-delta-lessons-software-defined-warfare)

---

### Space Force TacSRT and the NGA / NRO / Space Force turf settlement on buying commercial ISR

- **What it is:**
  - **TacSRT** (Tactical Surveillance, Reconnaissance and Tracking) is the Space Force program that buys fast, unclassified commercial ISR (imagery, RF, analytics) for combatant commands.
  - In **May 2025** Gen. Chance Saltzman and VADM Whitworth signed an accord setting the boundaries between TacSRT and NGA's commercial operations. It followed a similar Space Force–NRO agreement on unprocessed commercial imagery.
  - NRO has held acquisition authority for commercial imagery since 2018. NGA remains legally responsible for buying analytic services and products and for distributing ISR across government and to allies.
- **Problems / pain points:**
  - A roughly two-year, "sometimes bitter" turf war over who buys commercial ISR.
  - Saltzman: "This has been a long time coming." Whitworth: "It is a new standard for collaboration."
  - TacSRT is about **speed over depth**. Saltzman: "Our focus is on speed, not resolution, not breadth, not depth." Using it for targeting "would be a bridge too far."
  - NRO's Pete Muend (May 2026): NRO data must fit TacSRT needs, and there is "more work to do to make sure that when we buy data…" it reaches users.
- **How they're trying to solve it:** Written accords. Details have not been released.
- **Data:** Not public.
- **Hackathon angle:** Build a "speed, not depth" product. Given a new event (e.g. a vessel-AIS gap or a fire hotspot from FIRMS), automatically gather the freshest *free* imagery (Sentinel-1/2, Landsat, VIIRS) and produce a one-page brief within minutes. This is an open-data TacSRT.
- **Credibility:** Reputable defence press quoting officials.
- **Sources:**
  - [Breaking Defense: "NGA, Space Force ink accord on responsibilities for buying commercial ISR" (21 May 2025)](https://breakingdefense.com/2025/05/nga-space-force-ink-accord-on-responsibilities-for-buying-commercial-isr/)
  - [Breaking Defense: "NRO awards three new contracts for commercial satellite data" (4 May 2026)](https://breakingdefense.com/2026/05/nro-awards-three-new-contracts-for-commercial-satellite-data/)

---

### Tip-and-cue and maritime dark-vessel detection (SAR, RF, optical, AIS fusion)

- **What it is:**
  - **Tip-and-cue** means one cheap, wide-area sensor (AIS gaps, RF geolocation from HawkEye 360 or Unseenlabs, Sentinel-1 SAR, VIIRS night lights) *tips* an anomaly that *cues* a high-resolution tasked collection (BlackSky, Vantor, Umbra, Capella, ICEYE).
  - Maritime domain awareness (MDA) is the flagship commercial analytics use case for defence:
    - NGA Luno B bought Planet + SynMax Theia for Asia-Pacific MDA.
    - The NRO's CSO buys RF geolocation from SNC and ICEYE.
- **Problems / pain points:**
  - **Dark vessels.** Global Fishing Watch says "most fishing vessels" do not broadcast AIS. Of about 200 vessels with forced-labour cases, "only about a quarter broadcasted AIS". Only a handful of the few hundred IUU-listed vessels broadcast in the past two years.
  - **Spoofing and identity fraud.** SynMax Theia flags false positions, manipulated identities and shared MMSI numbers. Its site claims 147K+ dark detections, 143,401 ship-to-ship transfer events and 65,839 ships flagged for spoofing (vendor figures, unverified).
  - **Critical-infrastructure threats.** Windward case study (May 2026): a sanctioned Russian vessel loitered above a subsea cable for 41 days.
  - **Fused-picture gaps.** Free Sentinel imagery at 10–20 m detects most vessels over 15 m, but optical is blocked by cloud and coastlines are imaged only a few times a month. Commercial radar and optical fill gaps at a price.
- **How they're trying to solve it:**
  - GFW/DIU's **xView3** challenge produced open SAR dark-vessel detectors.
  - SynMax, Windward and Planet sell fused feeds.
  - Windward offers a Strait of Hormuz daily dashboard (2026).
- **Data:**
  - Sentinel-1 GRD (free).
  - The xView3 dataset ("a free and open large-scale dataset", registration required).
  - GFW public AIS-derived fishing effort and SAR vessel detections (to verify licence; GFW data are generally CC BY-NC).
  - VIIRS boat detections (NOAA/EOG).
  - Subsea cable maps (TeleGeography, public map).
- **Off-the-shelf tech:** The winning xView3 models (open source), GFW APIs, Sentinel Hub / Copernicus Data Space, and Earth Engine `COPERNICUS/S1_GRD`.
- **Hackathon angle:** **"Who's loitering over the cable?"** Fuse public AIS (or GFW data) with Sentinel-1 detections near Baltic, Red Sea or Taiwan Strait subsea cables. Flag dark or loitering vessels, explain each flag, and produce a shareable alert. Clear problem (cable sabotage), clear users (navies, cable operators, insurers), and all public data.
- **Credibility:** NGO research page, DIU/GFW challenge page, vendor pages (claims unverified), trade press.
- **Sources:**
  - [Global Fishing Watch: Dark Vessels research project (accessed 24 Oct 2026)](https://globalfishingwatch.org/research-project-dark-vessels/)
  - [xView3: Dark Vessels challenge (DIU / GFW)](https://iuu.xview.us/)
  - [SynMax: Theia (accessed 24 Oct 2026)](https://www.synmax.com/theia)
  - [Windward homepage, news items incl. subsea-cable loitering case study, May 2026 (accessed 24 Oct 2026)](https://windward.ai/)
  - [Via Satellite: Planet Luno B MDA award (17 Oct 2025)](https://www.satellitetoday.com/imagery-and-sensing/2025/10/17/planet-nabs-13m-award-under-ngas-luno-b-for-data-analytics/)
  - [TerraWatch Essentials, 11 May 2026 (HawkEye 360 NYSE listing at $3.1B valuation, citing Reuters)](https://newsletter.terrawatchspace.com/earth-observation-essentials-may-11-2026/)

---

### BlackSky Spectra: tasking-to-analytics in one platform, now sold to retail investors through AI agents (SkyFi on Robinhood)

- **What it is:**
  - BlackSky sells "Real-time, AI-enhanced tactical ISR". Spectra lets users task the constellation "in a few clicks" and returns imagery that is automatically analysed. BlackSky captures and auto-analyses up to **15 time-diverse images of a location per day**, with *Assured* (uncontested capacity) and *On-Demand* tiers.
  - It is a Luno A vendor: the $24.4M *Facility and Object Monitoring 2* order.
  - **30 Sep 2026:** BlackSky was named the first imagery provider for **SkyFi "Satellite Intelligence"**, a Robinhood Agent App.
    - It offers four recurring datasets on sites tied to top-traded stocks: vehicle production, e-commerce fulfilment hubs, data-centre construction, and theme-park attendance.
    - Specs: hourly revisits, 35 cm resolution, and Spectra automating tasking through to AI feature extraction in under 90 minutes.
    - SkyFi says it is "callable by any AI agent over MCP", returning an image with analysis and capture time.
- **Problems / pain points:**
  - Speed from question to answer.
  - Packaging defence-grade capability for non-experts.
  - SkyFi CEO Luke Fischer: "a question goes straight to orbit and comes back as an image with a number and date on it."
- **How they're trying to solve it:**
  - Automated tasking plus CV.
  - Agent and MCP distribution: an **LLM/agentic purchasing channel for imagery**, which belongs in the LLM/agentic geospatial section.
- **Data:** Commercial.
- **Hackathon angle:** Build the open-data version: an MCP server that answers natural-language questions ("how many cars at Tesla Fremont this month?") with Sentinel-2 / NAIP chips, a computed number, a date, and a confidence. Be explicit about resolution limits, which is honest and a differentiator.
- **Credibility:** Company press release and company homepage.
- **Sources:**
  - [BlackSky homepage (accessed 24 Oct 2026)](http://blacksky.com/)
  - [BlackSky PR: "BlackSky named first satellite imagery provider for SkyFi 'Satellite Intelligence' on Robinhood Agent Apps" (30 Sep 2026)](https://blacksky.com/press-releases/blacksky-named-first-satellite-imagery-provider-for-skyfi-satellite-intelligence-on-robinhood-agent-apps/)

---

### Safran.AI (formerly Preligens): European defence imagery AI, absorbed by a prime

- **What it is:**
  - Preligens (ex-Earthcube) was the French leader in AI for defence intelligence, best known for automated detection on satellite imagery.
  - **Safran acquired it in September 2024 for €220M**, as reported by Yahoo Finance; Wikipedia also gives $243.3M. It now sits in Safran Electronics & Defense as **Safran.AI** (Paris and Pacé/Rennes; CEO Sébastien Fabre).
  - Offers: "strategic AI for intelligence", i.e. processing large volumes of heterogeneous data to speed the intelligence cycle, and "tactical AI" for military operations.
  - Nov 2025: Safran and the UAE's Technology Innovation Institute announced an intention to "lead the next evolution in geospatial intelligence".
  - June 2026 item: "From Satellite to Decision: Accelerating Data Exploitation in the Field".
- **Problems / pain points:**
  - Same "too many images" problem as NGA.
  - Standalone European defence-AI startups struggle to scale and get bought by primes, which is part of the consolidation theme.
- **How they're trying to solve it:** Integration into Safran's sensors and C2, and Gulf partnerships.
- **Data:** Not public.
- **Hackathon angle:** None specific beyond generic object detection. Useful mainly as market context: the "AI analytics startup becomes a feature of a prime" exit pattern.
- **Credibility:** Official company page and Wikipedia (citing Yahoo Finance).
- **Sources:**
  - [Safran: Safran.AI company page (accessed 24 Oct 2026)](https://www.safran-group.com/companies/safran-ai)
  - [Wikipedia: Safran (accessed 24 Oct 2026)](https://en.wikipedia.org/wiki/Safran)
  - [Yahoo Finance: "Safran buys AI firm Preligens for 220 million euros" (2 Sep 2024; cited by Wikipedia, not opened)](https://finance.yahoo.com/news/safran-buys-ai-firm-preligens-065604597.html)

---

### Rendered.ai: synthetic training data for EO / SAR (the labelling-cost and rare-object problem)

- **What it is:**
  - A platform for physics-based synthetic imagery generation, with labels created at render time, covering EO, SAR, IR, multispectral, hyperspectral and x-ray.
  - Integrates DIRSIG, NVIDIA Omniverse and others, and has an "Agent Studio" that builds data-generation agents from natural-language prompts, including SAR simulation.
  - Pricing (vendor page): from $5,000/month (Teams) and $15,000/month (Organizations).
  - Customers shown: SatVu, COVAR, Vizgard, Kallisto AI, and others.
  - Orbital Insight testimonial: "AP scores improved across the board for identifying rare and unusual objects."
- **Problems / pain points:**
  - Real imagery is costly and slow to collect and label.
  - Rare objects and edge cases are under-represented.
  - Some data is restricted for security.
  - The page also cites an MIT study saying only 5% of integrated AI pilots extract meaningful value (secondary citation, unverified).
- **How they're trying to solve it:** Synthetic data as a service, auto-labelling of real data, and a military camouflage partnership with Kallisto AI.
- **Data:** Synthetic, generated on demand.
- **Off-the-shelf tech:** Open alternatives include BlenderProc, Omniverse Replicator, and RarePlanes (a public synthetic-plus-real aircraft dataset from CosmiQ / AI.Reverie; to verify for the Datasets slice).
- **Hackathon angle:** Quantify "how much real labelling does synthetic data save?" on one rare-object class (e.g. a specific aircraft or vessel type), using RarePlanes or a few hundred self-rendered chips.
- **Credibility:** Vendor page, with unverified claims.
- **Sources:**
  - [Rendered.ai homepage (accessed 24 Oct 2026)](https://rendered.ai/)

---

### NATO APSS ("Aquila") and Europe's push for sovereign ISR after the Ukraine cutoff

- **What it is:**
  - **Alliance Persistent Surveillance from Space (APSS)** was launched in February 2023 as "the largest multinational investment in space-based capabilities in NATO's history". Seventeen Allies signed the implementation-phase MoU in July 2024, and 19 now contribute the equivalent of more than USD 1 billion.
  - It will create **"Aquila"**, "a large-scale, virtual constellation of national and commercial surveillance satellites".
  - NATO adopted a **Commercial Space Strategy** in February 2025.
  - **ESA's Nov 2025 ministerial** brought a record €22.1B over three years, about €3.5B for EO, and member states offering up to €1.2B for a military constellation.
- **Problems / pain points:**
  - Dependence on US commercial providers, made concrete by the March 2025 Ukraine cutoff.
  - Fragmented requirements across 27 EU states. EDA's David Byrne: "Everybody realizes we need to move faster."
  - Certification is "a major issue".
  - UK officials (Sept 2026) say the UK is "not agile and responsive" and has been too risk-averse.
- **How they're trying to solve it:**
  - Pooled virtual constellations.
  - National sovereign SAR buys (ICEYE to Poland, the Netherlands, Finland, Sweden, Portugal, Greece and Germany).
  - Planet's €240M German-government-funded deal (July 2025).
  - Faster requirement cycles (EDA: from 1.5 years to about 6 months).
- **Data:** National and commercial, mostly not public.
- **Hackathon angle:** A "virtual constellation planner". Given an AOI and a question, compute which mix of free (Sentinel) and commercial sensors gives the needed revisit, resolution and latency, and how often. Use public orbit elements (TLEs from CelesTrak) and published sensor specs. This addresses tasking friction and the Aquila coordination problem.
- **Credibility:** Official NATO page, analyst newsletter, trade press.
- **Sources:**
  - [NATO: "NATO's approach to space" (accessed 24 Oct 2026)](https://www.nato.int/cps/en/natohq/topics_175419.htm)
  - [TerraWatch Essentials, 17 Dec 2025 (ESA ministerial)](https://newsletter.terrawatchspace.com/earth-observation-essentials-december-17-2025/)
  - [Via Satellite: "Europe Grapples With Faster Procurement Amid Space Defense Push" (21 Sep 2026)](https://www.satellitetoday.com/government-military/2026/09/21/europe-grapples-with-faster-procurement-amid-space-defense-push/)
  - [Via Satellite: "U.K. Defense Secretary Calls For Investment in Satellites Intelligence Gathering Capabilities" (24 Sep 2026)](https://www.satellitetoday.com/government-military/2026/09/24/u-k-defense-secretary-calls-for-investment-in-satellites-intelligence-gathering-capabilities/)
  - [Wikipedia: Planet Labs (€240M German deal, citing Payload, 2 Jul 2025)](https://en.wikipedia.org/wiki/Planet_Labs)
  - [Wikipedia: ICEYE (sovereign SAR deals)](https://en.wikipedia.org/wiki/ICEYE)

---

### EU SatCen (European Union Satellite Centre)

- **What it is:** The EU's GEOINT agency for CFSP and CSDP. It also runs the Copernicus Support to EU External and Security Action (SESA) service, using Copernicus and commercial imagery.
- **Problems / pain points:** Not researched in depth. The SatCen homepage returned no readable content.
- **Hackathon angle:** None specific.
- **Credibility:** Placeholder. Background from general knowledge, **unverified**.
- **Sources:**
  - [SatCen homepage (fetched, no readable content)](https://www.satcen.europa.eu/)

---

### US imagery-of-Israel limit (Kyl–Bingaman Amendment) and US licensing levers over commercial imagery

- **What it is:**
  - The Kyl–Bingaman Amendment (NDAA FY1997, §1064) bars US licensing of imagery of Israel at higher resolution than is available from non-US sources.
  - NOAA lowered the limit from 2 m to **0.4 m** in a Federal Register notice of 21 July 2020, finding 0.4 m imagery "readily available" abroad.
  - Wikipedia says the law has been extended to the Palestinian territories and the Golan Heights ("citation needed").
  - CRSRA (Commerce Department, Office of Space Commerce) licenses US remote-sensing operators under 15 C.F.R. Part 960.
  - The 2026 Iran-war delays were described as *voluntary* (Planet) or via "quiet urging" (Breaking Defense), not formal licence conditions.
- **Problems / pain points:**
  - Geography-specific degradation of imagery affects OSINT on Gaza and the West Bank.
  - It is unclear to users which regions are degraded, delayed or blocked, by whom and why.
- **How they're trying to solve it:** Researchers buy from non-US providers or use free Sentinel data.
- **Data:** Federal Register notice. Sentinel-2 at 10 m is unaffected.
- **Hackathon angle:** Part of a public "imagery availability map": which providers restrict which regions and at what resolution or latency.
- **Credibility:** Wikipedia (citing the Federal Register, SpaceNews and NPR) and an official CRSRA page.
- **Sources:**
  - [Wikipedia: Kyl–Bingaman Amendment (accessed 24 Oct 2026)](https://en.wikipedia.org/wiki/Kyl%E2%80%93Bingaman_Amendment)
  - [Federal Register: Notice of Findings Regarding Commercial Availability of Non-U.S. Satellite Imagery With Respect to Israel (21 Jul 2020; cited by Wikipedia, not opened)](https://www.federalregister.gov/documents/2020/07/21/2020-15770/notice-of-findings-regarding-commercial-availability-of-non-us-satellite-imagery-with-respect-to)
  - [NPR: "The U.S. has special rules for satellites over one country: Israel" (16 Nov 2023; cited by Wikipedia, not opened)](https://www.npr.org/2023/11/16/1212889717/satellite-images-us-israel-gaza)
  - [Office of Space Commerce: CRSRA (accessed 24 Oct 2026)](https://www.space.commerce.gov/regulations/commercial-remote-sensing-regulatory-affairs/)

---

### Chinese AI-on-commercial-imagery OSINT sellers (MizarVision) and imagery-provenance disputes

- **What it is:**
  - **MizarVision** is a Chinese firm that applies AI to open-source and commercial satellite imagery and publishes and sells analyses of US forces.
  - Global Times ran its images of the US build-up at Middle Eastern bases (30 Jan 2026). The Washington Post (4 Apr 2026) reported that it continued selling conflict imagery.
  - Wikipedia's Planet article says Chinese state media cited MizarVision's use of Planet imagery. Planet said MizarVision was not a client and denied owning the images in question.
- **Problems / pain points:**
  - **Provenance.** Whose satellite took this image, when, and has it been altered? This is the hook for the data-provenance and deepfake theme.
  - Western vendors' restrictions do not bind foreign resellers.
- **How they're trying to solve it:** Vendor denials. There is no technical provenance standard in use.
- **Data:** Public Sentinel and Landsat archives can be used to cross-check the date and scene of a claimed image at coarse resolution.
- **Off-the-shelf tech:** Image matching against archives (SIFT/LoFTR features vs Sentinel-2 basemaps), shadow-angle sun-position dating (solar azimuth/elevation from pysolar), C2PA.
- **Hackathon angle:** **"Is this satellite image real, and when was it taken?"** A verifier that takes an image posted on social media and (1) geolocates and matches it to Sentinel-2 or Google basemaps, (2) estimates capture date and time from shadows and sun angle, and (3) checks for inconsistencies with the archive on that date (clouds, construction state). It outputs a provenance report.
- **Credibility:** Reputable defence press citing the Washington Post, and Wikipedia.
- **Sources:**
  - [Breaking Defense: "Nowhere to hide…" (13 Apr 2026)](https://breakingdefense.com/2026/04/nowhere-to-hide-iran-war-spotlights-military-challenges-posed-by-space-based-remote-sensing/)
  - [Wikipedia: Planet Labs (accessed 24 Oct 2026)](https://en.wikipedia.org/wiki/Planet_Labs)
  - [Washington Post (4 Apr 2026; cited by Wikipedia, not opened)](https://www.washingtonpost.com/national-security/2026/04/04/china-ai-military-intelligence-iran-war/)

---

### Open-source conflict and human-rights analysts: CIR + BigData Republic "Burnscar" arson-verification pipeline (Sudan)

- **What it is:**
  - The Centre for Information Resilience (CIR) and BigData Republic built an open pipeline that verifies possible arson of civilian homes. Sudan is the first theatre; Ukraine and Myanmar may follow.
  - **How it works:**
    1. Take NASA FIRMS (VIIRS / MODIS) active-fire points.
    2. Buffer each point into an AOI.
    3. Fetch the closest Sentinel-2 scenes before and after the fire with under 10% cloud.
    4. Compute the change in Normalised Burn Ratio (dNBR) and threshold it into a burn-scar mask.
    5. Intersect the mask with Google Open Buildings footprints to count affected structures.
    6. Cluster detections in space and time.
    7. Retry validation at 11, 16 and 21 days, because imagery is often unavailable right after a fire.
    8. Hand the results to human investigators.
  - Stack: SQLMesh plus DuckDB-spatial plus Earth Engine. Code is MIT-licensed on GitHub.
- **Problems / pain points:**
  - Burned villages are "often unreported or unverified".
  - Manual validation took hours. The pipeline cut it to minutes.
  - **Limits:** "it cannot determine intent, identify perpetrators, or establish whether a war crime took place."
  - The urban mask is an imperfect false-positive filter.
  - No accuracy figures are published.
- **How they're trying to solve it:** Automate up to the point of human verification.
- **Data:**
  - NASA FIRMS (free, API key).
  - Sentinel-2 L2A (free).
  - Google Open Buildings (CC BY 4.0 / ODbL; verify).
  - GADM and GeoNames.
- **Off-the-shelf tech:** Earth Engine, DuckDB spatial, SQLMesh, and the uv-based CLI (`burnscar run`).
- **Hackathon angle:** Very strong. Fork Burnscar and add:
  - (a) Sentinel-1 SAR confirmation for cloudy scenes, following PWTT;
  - (b) a reviewer UI with before/after chips and one-click verify or reject, which creates labels;
  - (c) a published precision estimate;
  - (d) provenance-stamped evidence packets for courts and journalists.
  
  It uses public data end to end, addresses a clear problem (atrocity documentation in Sudan), and has a clear user (investigators).
- **Credibility:** Technical blog by the implementer and a public GitHub repo (MIT licence, 99 commits).
- **Sources:**
  - [BigData Republic, T. Uijtdehaag: "Detecting War Crimes from Space" (24 Sep 2025)](https://bigdatarepublic.nl/articles/detecting-war-crimes-from-space/)
  - [GitHub: Centre-for-Information-Resilience/Burnscar](https://github.com/Centre-for-Information-Resilience/Burnscar)
  - [TerraWatch Essentials, 13 Oct 2025 (pointer to the deep dive)](https://newsletter.terrawatchspace.com/earth-observation-essentials-october-13-2025/)

---

### Why EO damage assessments disagree (HOT, Venezuela earthquake 2026): the trust problem in post-event analytics

- **What it is:**
  - A Humanitarian OpenStreetMap Team analysis (6 Aug 2026) of earthquake damage maps for Venezuela.
  - In Urimare, **Microsoft's optical assessment flagged 1,620 of 10,390 buildings (15%) as damaged, while OSU's radar assessment flagged 5,417 (52%)**.
  - Optical sees roof damage. SAR sees texture change from any side, catching facade and foundation damage.
  - Ground reports via ChatMap confirmed SAR-detected damage that was invisible from above.
- **Problems / pain points:**
  - Different sensors, methods and definitions of "damaged" give incomparable numbers.
  - Remote rapid assessments are "always an estimation".
  - Quote: "the real question isn't which one is 'correct', it's what stage of response you're in, and what decision you're trying to make."
- **How they're trying to solve it:**
  - Combine optical and SAR.
  - Define severity on the ground for a specific operational use.
  - Validate with ground truth (ChatMap).
- **Data:** Sentinel-1, the Microsoft and OSU assessments, OSM building footprints, ChatMap reports.
- **Hackathon angle:** A "damage-map reconciler" that ingests two or more published damage assessments for the same event. It explains where and why they disagree (sensor, definition) and produces a consensus map with an uncertainty layer for responders. This addresses trust and verification directly.
- **Credibility:** Reputable humanitarian NGO.
- **Sources:**
  - [HOT: "Why damage assessments can vary: from image pixels to microwaves" (6 Aug 2026)](https://hotosm.org/en/news/why-damage-assessments-can-vary-from-image-pixels-to-microwaves/)
  - [TerraWatch Essentials, 12 Oct 2026 (pointer)](https://newsletter.terrawatchspace.com/earth-observation-essentials-october-12-2026/)

---

### Industry-level signal: defence-and-intelligence share of EO revenue keeps rising

- **What it is:** Analyst framing that defence and intelligence (D&I) has overtaken commercial as EO's growth engine.
  - TerraWatch (Dec 2025): "D&I revenue share is growing while share from commercial verticals is flat or declining." Also: "Hundreds of millions in new defense and intelligence contracts flowed to EO providers this year." And: "The industry is growing, but not the way the 2020-era funding narrative promised."
  - TerraWatch (Oct 2025), on Albedo leaving commercial imagery to sell VLEO buses: "The economics of selling imagery remain tough due to concentrated government demand and shrinking commercial margins."
  - TerraWatch H1 2026 review: the defence and intelligence vertical's funding rounds included **Striveworks ($33M)** and **Solafune ($30M)**, "both focused on building GEOINT platforms".
- **Problems / pain points:**
  - Single-customer dependence (budget risk, EOCL recompete).
  - Restrictions in wartime.
  - Commercial verticals remain unproven.
- **Hackathon angle:** The commercial and civil gap is the opportunity. Defence already pays for object monitoring and change detection, so a team can repurpose the same capability for an under-served civil user (NGOs, journalists, small states, insurers).
- **Credibility:** Analyst newsletter (partly paywalled; visible text only).
- **Sources:**
  - [TerraWatch Essentials, 17 Dec 2025](https://newsletter.terrawatchspace.com/earth-observation-essentials-december-17-2025/)
  - [TerraWatch Essentials, 13 Oct 2025](https://newsletter.terrawatchspace.com/earth-observation-essentials-october-13-2025/)
  - [Payload: "Exclusive: Albedo drops its commercial imagery business" (1 Oct 2025)](https://payloadspace.com/exclusive-albedo-drops-its-commercial-imagery-business/)
  - [TerraWatch: Earth Observation H1 2026 Review (27 Jul 2026, partly paywalled)](https://newsletter.terrawatchspace.com/earth-observation-h1-2026-review/)

---

## Part A.4 — Non-profits, open monitors and open-data OSINT

Free or public-interest monitors built on open satellite data (maritime, forests, emissions, pollution, conflict damage), plus the 2026 access shocks that make them more important.

### Ai2 Skylight (maritime domain awareness)
- **What it is:** Free maritime-monitoring platform from the Allen Institute for AI. Detects vessels in Sentinel-1 SAR, Sentinel-2 optical and Landsat 8/9 (plus night lights per Ai2 blog); "over 1.3 million vessels per month, or about 290,000 per week, using imagery alone"; detects "thousands of 'dark' vessels – those without AIS – daily". Sentinel-2 detections reach the database ~5 hours after capture on average. Used via API by SeaVision (US government platform used by hundreds of agencies) and the UK Marine Management Organisation. Models open-sourced (GitHub `allenai/vessel-detection-sentinels`); now runs on Ai2's OlmoEarth foundation models. A public map (no account, 18 months history) is "not about real-time monitoring or enforcement". 2026: an AI agent "Shippy" answering plain-language questions about vessel activity.
  - **Shippy (Skylight launch post, 2026):** answers e.g. daily fishing summaries for an EEZ, dark-vessel detections in a region, where vessels of a flag/type are active, patrol hotspots, satellite coverage gaps; data from Skylight live tracks/detections, Global Fishing Watch, Trygg Mat Tracking, SkyTruth oil-pollution data, ProtectedSeas Navigator (marine regulations). Safeguards: cites sources and links to map/vessel records, reproducible, notes data it can't access, stops when out of scope ("rather than guessing"), humans decide enforcement. Problem quotes: a daily brief question "is rarely simple" and "That can take hours" to assemble by hand; watch floors in under-resourced states "often lack sufficient staffing". Access: trusted agencies (UNODC, Joint Analytical Cell), later free for governments, RFMOs and qualifying NGOs. LLM not disclosed.
  - **Ai2 × Global Fishing Watch** (Climate Week NYC 2026): co-develop AI agents and detection tools; VIIRS night-time vessel-light detections on the GFW map since Mar 2026; Skylight real-time detections into GFW's marine manager portal; OlmoEarth for annotation. "Our maritime partners have made it clear that they care about having purpose-built AI" (Namrata Kolla, Head of Skylight).
  - **Impact report (1 Jun 2025 – 31 May 2026):** public map opened Oct 2025 (no-account, 3-day delayed); 3,000+ visitors from 146 countries in two months; 111 new organisations (+42% YoY); partner-reported outcomes: 21+ vessels interdicted/fined, $915,000+ fines collected, 6,000+ kg illegal fish seized, 1 RFMO IUU listing; Shippy used by 20+ early adopters incl. GFW, ProtectedSeas, UNODC, INTERPOL, UK MMO, Prefectura Naval Argentina.
- **Problems / pain points:** IUU fishing enforcement with "resources … increasingly limited"; dark vessels; analysts in small coastal states.
- **Data:** Sentinel-1/2, Landsat, (VIIRS), AIS.
- **Hackathon angle:** Fuse Skylight-style open detections with AIS to produce *dark-vessel encounter* reports for one MPA / EEZ, with an evidence pack (image chips + AIS gap) a coast guard could act on.
- **Credibility:** Official (Skylight / Ai2) + reputable tech press.
- **Sources:** [Inside Skylight — public map (c. Oct 2025)](https://skylight.global/news/inside-skylight-explore-our-public-map-and-the-ai-powering-ocean-insight); [Sentinel-2 now in Skylight](https://skylight.global/news/sentinel-2-now-available-in-skylight); [Ai2 blog — Protecting marine life with AI](https://allenai.org/blog/protecting-marine-life-with-ai-192529f8aa15); [OlmoEarth oceans testimonial](https://allenai.org/olmoearth-testimonial-oceans); [Meet Shippy (2026)](https://skylight.global/news/shippy-launch); [Ai2 and GFW unite on AI agents (2026)](https://skylight.global/news/ai2-gfw); [Skylight Year in Review 2025–2026](https://skylight.global/news/impact-report-2025-2026); [GeekWire — Shippy, 2026](https://www.geekwire.com/2026/ai2s-skylight-project-launches-shippy-an-ai-agent-that-dives-into-ocean-data/) (search snippet; page returned 403).

---

### Global Fishing Watch (GFW)
- **What it is:** Non-profit (Google, Oceana, SkyTruth origins) publishing AIS-derived fishing effort, SAR vessel detections, and APIs. Landmark *Nature* paper (3 Jan 2024, with UW-Madison, Duke, UCSB, SkyTruth): "about 75 percent of industrial fishing vessels are not publicly tracked"; "more than 25 percent" of transport/energy vessel activity missing from public tracking; offshore wind turbines more than doubled 2017–2021 and outnumbered oil platforms by 2021; analysed "about 2 million gigabytes" of imagery 2017–2021 using Google Earth Engine, AIS from Spire and ORBCOMM, ESA radar/optical.
- **Problems / pain points:** AIS is voluntary/spoofable; most fishing in Africa and South Asia is invisible to public tracking ("for every 10 fishing vessels we found on the water, seven were in Asia while only one was in Europe").
- **Data:** GFW APIs: fishing effort (~70,000 AIS-broadcasting vessels), vessel search/identity, fishing events, encounters (possible transshipment), loitering, port visits, vessel insights (AIS + authorisations), SAR vessel detections and offshore fixed infrastructure, AIS presence. Free with account + API key, attribution required (commercial-use terms not stated on the page); Python client (`gfw-api-python-client`) and R `gfwr`.
- **Hackathon angle:** same as Skylight; plus "port-state risk score" for vessels arriving at a port.
- **Credibility:** Peer-reviewed (Nature) + official press release.
- **Sources:** [GFW APIs](https://globalfishingwatch.org/our-apis/); [GFW press release, 3 Jan 2024](https://globalfishingwatch.org/press-release/new-research-harnesses-ai-and-satellite-imagery-to-reveal-the-expanding-footprint-of-human-activity-at-sea/); [Nature paper s41586-023-06825-8](https://www.nature.com/articles/s41586-023-06825-8) (paywall redirect; details via GFW release).

---

### Windward (maritime AI; 2026 shadow fleet, GNSS jamming, Hormuz)
- **What it is:** Israeli/UK maritime-intelligence company (behavioural AI over AIS + satellite). Blog posts in Oct 2026 document the 2026 Gulf war's effects on maritime data.
- **Problems / pain points (Windward's own estimates, vendor content):**
  - Shadow fleet is uncountable: "there is no register and each organization counts a different set of vessels"; EEAS range 600–1,400 vessels; of ~430 tankers in the Iran trade in Q2 2026, 87% sanctioned and 62% falsely flagged; nearly 300 tankers falsely flagged using 19 fraudulent registries (Feb 2026); 3,137 prolonged dark events in Q2 2026 vs 451 in Q1; "absence from a list is not evidence of absence of risk"; "no single source resolves a case on its own" (1 Oct 2026).
  - Marine insurers' evidence gap: GPS jamming affected 124,235 vessels in Q3 2026 and created >3.35 million false ship-to-ship meetings since "Operation Epic Fury" began; dark convoy passages were 47% of Hormuz traffic in Aug 2026 and 52% in Sep; new claim types (constructive total loss, loss of hire, dark-period disputes); a 22 May 2026 Court of Appeal ruling (*The CATALAN SEA*) on sanctions clauses makes AIS-only decisions more vulnerable to challenge. "Imagery changes what can be settled rather than argued." (20 Oct 2026).
- **How they're trying to solve it:** fuse SAR, EO, RF, documents and behavioural models into "a timestamped account where each step has a stated confidence level".
- **Data:** AIS (commercial), SAR (Sentinel-1 free; ICEYE/Capella commercial), EO, RF (HawkEye 360).
- **Hackathon angle:** **"AIS lie detector"**: for a chosen strait/port, match Sentinel-1 SAR vessel detections against AIS positions to flag (a) dark vessels and (b) AIS positions where no ship is seen (spoofing/jamming artefacts), outputting an insurer-grade evidence timeline. Directly answers a 2026 pain point with free data.
- **Credibility:** Vendor blog (numbers are Windward estimates).
- **Sources:** [What Is the Shadow Fleet, and Why Is It So Hard to Count?, 1 Oct 2026](https://windward.ai/blog/what-is-the-shadow-fleet-and-why-is-it-so-hard-to-count/); [How Marine Insurers Are Closing the Evidence Gap, 20 Oct 2026](https://windward.ai/blog/how-marine-insurers-are-closing-the-evidence-gap/); [Windward blog index](https://windward.ai/blog/).

---

### Global Forest Watch → Global Nature Watch (WRI) and the end of free NICFI Planet imagery
- **What it is:** WRI's forest-monitoring platform renamed *Global Nature Watch* (post dated 15 Sep 2026, originally 1 Jul 2026), expanding to grasslands, agricultural lands and trees outside forests; AI-driven platform *GNW Horizon* in preview; goal of helping people decide "regardless of language or technical expertise". Annual tree-cover-loss data from UMD GLAD (30 m, 2001–2025): 2025 global tree cover loss 25.5 Mha (−14%); tropical primary forest loss 4.3 Mha (−36% vs 2024 but +46% vs a decade ago); fire caused 42% of global loss; Bolivia second-highest on record; DRC record non-fire loss; Indonesia +14%.
- **Problems / pain points:**
  - *Definitions & false alarms:* tree cover loss "does not directly measure deforestation"; satellites "cannot see whether land is legally designated as forest"; PRODES counts clear-cuts ≥6.25 ha vs UMD ≥0.09 ha; different years (Aug–Jul vs calendar); fire handled differently → users misread loss as deforestation.
  - *Latency:* smoke delays detection, so late-2024 fires appear in 2025 data.
  - *Loss of free high-res data:* Planet NICFI tropical mosaics were removed from GFW on 1 Apr 2025 when "That phase of the program ended"; a limited return from 26 May 2026 to 25 May 2027 (Bezos Earth Fund, Andes Amazon Fund, Planet) covers only the Amazon basin and only areas with disturbance alerts from the past two years plus a 500 m buffer — "not a full re-launch of Planet imagery across the tropics." Users elsewhere fall back to Landsat 8 (30 m), Sentinel-2 (10 m) and Google basemaps.
  - *EUDR:* EU Deforestation Regulation applies from 30 Dec 2026 (large companies) and 30 Jun 2027 (smaller); goods must not come from land "deforested nor did they contribute to forest degradation after Dec. 31, 2020"; only 14% of 500 assessed companies cite the EUDR as reason for traceability; ~1/3 have no zero-deforestation commitments (WRI, 6 Oct 2026).
- **Data:** UMD GLAD tree cover loss, GLAD/RADD/integrated disturbance alerts, Sentinel-2, Landsat, Trase supply-chain data, Planet NICFI (restricted).
- **Hackathon angle:** **EUDR plot checker**: upload farm polygons (GeoJSON) → automatic check against UMD loss + JRC TMF + Sentinel-2 time series since 31 Dec 2020, distinguishing fire vs clearing vs plantation harvest, producing a due-diligence evidence PDF. Deadline is two months away; WRI's own explainer shows users confuse loss with deforestation.
- **Credibility:** Official (WRI/GNW).
- **Sources:** [GFW is now Global Nature Watch, 15 Sep 2026](https://globalnaturewatch.org/blog/data-and-tools/gfw-now-global-nature-watch/); [Select Planet imagery now on GNW Horizon, 8 Oct 2026](https://globalnaturewatch.org/blog/data-and-tools/planet-imagery-changes-gfw/); [2025 Tree Cover Loss Data Explained, 29 Apr 2026](https://globalnaturewatch.org/blog/data-and-tools/2025-tree-cover-loss-data-explained/); [WRI — Latest analysis of deforestation trends (2025 data)](https://gfr.wri.org/latest-analysis-deforestation-trends); [WRI — EU deforestation footprint / EUDR, 6 Oct 2026](https://www.wri.org/insights/eu-deforestation-footprint-eudr); [GNW blog index](https://globalnaturewatch.org/blog/).

---

### Climate TRACE
- **What it is:** Coalition (Al Gore-backed) producing asset-level GHG emissions using "satellite imagery and AI algorithms"; monthly releases (5.9.0 Jul 2026 through May 2026 data; 5.10.0 Aug 2026 — H1 2026 emissions marginally higher than H1 2025; 5.11.0 Sep 2026 through Jul 2026). Site claims 2,765,771 emissions sources summarised from 744,678,997 assets; >13,600 landfills; UC Berkeley + Maryland methane plan partnership (Sep 2026); SMAC Methane Inventory Tool (36 jurisdictions, 15 countries).
- **Problems / pain points:** National inventories are slow (UNFCCC reporting lags years) and self-reported; asset-level estimates are model-based and their validation is not shown on the news page (no independent evaluation visible — note for trust/verification theme).
- **Data:** Free downloads/API (check licence on site).
- **Hackathon angle:** "Ground-truth the model": compare Climate TRACE asset estimates for a set of power plants/steel mills against independent signals (Sentinel-5P NO₂, VIIRS night-time heat, Sentinel-2 plume/activity) and flag disagreements.
- **Credibility:** Official (coalition site).
- **Sources:** [Climate TRACE news](https://climatetrace.org/news).

---

### Carbon Mapper data portal
- **What it is:** Non-profit portal for methane and CO₂ "super-emitter" plumes from Planet's Tanager-1 (JPL-derived imaging spectrometer), NASA EMIT (ISS), and airborne AVIRIS / ASU GDCS campaigns. Data "intended to support the public good", free for non-commercial use by governments, operators, NGOs, journalists, researchers; commercial use/redistribution requires terms review. Data API and STAC API (registration required).
- **Problems / pain points:** Plume detections need attribution to a facility/operator and follow-up; non-commercial licence limits product builders.
- **Hackathon angle:** "Who owns this plume?" — auto-attribute Carbon Mapper / EMIT plumes to the nearest facility (OSM, EIA, landfill databases) and draft a notification to the operator/regulator; track repeat emitters.
- **Credibility:** Official.
- **Sources:** [Carbon Mapper data](https://carbonmapper.org/data).

---

### SkyTruth Cerulean (oil-slick detection)
- **What it is:** "free, open-source platform that automatically detects oil slicks from vessels and offshore oil platforms" from satellite imagery (Sentinel-1 SAR per SkyTruth's broader work — not stated on this page) and AI; matches slicks to ship traffic (AIS) — "Being able to match a spill to a ship's traffic is amazing" (user testimonial); Source Profiles extended to infrastructure (Apr 2026); API via Colab notebook; users include ProtectedSeas, ELAW, AIDA, Indonesia Ocean Justice Initiative, Lighthouse Reports, SourceMaterial.
- **Problems / pain points:** Illegal bilge dumping is common and unpunished; SAR look-alikes (low wind, biogenic films) cause false positives (methods page not opened — unverified).
- **Hackathon angle:** Auto-generate a prosecutable evidence pack linking a Cerulean slick to the AIS track of the likely polluter, with uncertainty and a draft complaint to the flag state.
- **Credibility:** Official non-profit site.
- **Sources:** [SkyTruth Cerulean](https://skytruth.org/cerulean/).

(More entries being added: climate/nature, insurance, defence demand, conferences, recurring themes, problem bank.)

---

### Earth Genome — Earth Index (and Earthrise Media)
- **What it is:** Non-profit applying AI to Earth data; *Earth Index* lets users click example patterns and give feedback, then finds similar patterns across the planet using Earth foundation models ("Search for Stuff"); uses: illegal Amazon gold mining, forest crime, super-emitters, aquaculture regulation checks in Chile; collaborators Climate TRACE, Mongabay, Amazon Mining Watch; funders include Google.org, AWS, Bezos Earth Fund, Moore, Pulitzer Center, NSF. Note: earthrise.media now 301-redirects to earthgenome.org (suggesting Earthrise Media, the satellite-journalism ML non-profit, has merged into or been absorbed by Earth Genome — no notice found; unverified).
- **Problems / pain points:** Journalists and NGOs can't train models; few-shot search lowers the labelling barrier.
- **Hackathon angle:** "Earth Index for X": a few-shot search over public embeddings (AlphaEarth annual 10 m embeddings; Clay) for a new target class (e.g., illegal landfills, brick kilns, informal airstrips), with human feedback loop.
- **Credibility:** Official site.
- **Sources:** [earthgenome.org](https://www.earthgenome.org/); [earthrise.media redirect](https://earthrise.media/); [Amazon Mining Watch](https://amazonminingwatch.org/).

---

### Bellingcat Iran Conflict Damage Proxy Map (Apr 2026) — open SAR when commercial imagery goes dark
- **What it is:** Free Google Earth Engine app (7 Apr 2026, Jake Godin; method by Ollie Ballinger, UCL) estimating likely building damage across Iran and the Gulf from Sentinel-1 SAR using the Pixel-Wise T-Test (PWTT): a year of pre-war data defines each pixel's "normal" range (99% of observations), then flags pixels persistently outside it. Earlier versions: Gaza (2023), Ukraine, Turkey.
- **Problems / pain points:** Built because "Commercial satellite providers have restricted imagery over the region" and internet blackouts in Iran limit social-media evidence. Limitations: high probability ≠ confirmed damage; small damage and damage to the sides of high-rises (drone strikes) missed; big sites (refineries, tanks) dominate; updates 1–2×/week; "not meant to be a representation of real-time damage".
- **Validation:** Peer-reviewed after two years; tested on >2 million UN-labelled building footprints in 30 cities (Gaza, Ukraine, Sudan, Syria, Iraq); building-level AUC 0.87.
- **Data:** Sentinel-1 GRD (free), Sentinel-2 for confirmation via Copernicus Browser, UNOSAT damage labels.
- **Hackathon angle:** Extend PWTT with (a) automatic Sentinel-2 cross-checks, (b) building-footprint aggregation (Overture / Microsoft footprints), (c) a plain-language, citation-backed "damage brief" per flagged site with an uncertainty statement; or attack its false positives with a filter that suppresses alerts from agriculture, construction or soil moisture; or apply PWTT to a non-conflict disaster (earthquake, wildfire, hurricane) to give insurers/responders a free first-pass map. All public data, feasible in 36 hours.
- **Credibility:** Reputable OSINT org + peer-reviewed method.
- **Sources:** [Bellingcat, 7 Apr 2026](https://www.bellingcat.com/resources/2026/04/07/tool-damage-assessment-destruction-sentinel-satellite-imagery-iran-us-gulf/); [PWTT project page](https://oballinger.github.io/PWTT) (linked from the article; not opened); [migflug.com repost](https://migflug.com/jetflights/when-satellites-go-dark-radar-sees-through-bellingcats-war-damage-tool/).

---

### Planet's 2026 Iran-war imagery blackout (access as a problem)
- **What it is:** After the US and Israel began strikes on Iran on 28 Feb 2026, Planet first imposed a 96-hour delay, then 14 days (March), then on 4 Apr 2026 announced it would "voluntarily withhold imagery over the area indefinitely until the conflict ends" (all of Iran, Gulf states, other active conflict zones; imagery back to 9 Mar), at a US government request that asked all providers for an "indefinite withhold of imagery"; replaced by "managed distribution" case-by-case for "mission-critical or in the public interest" needs. Other providers (e.g., Vantor) added access controls. Pentagon declined to comment.
- **Problems / pain points:** Removes "one of the few widely available tools for verifying strikes, assessing damage, and tracking military developments" for journalists, researchers and NGOs (TheWrap). TerraWatch flagged a BBC piece on humanitarian concern. Shows commercial imagery access is policy-contingent — free Copernicus data becomes the fallback. Later (per TerraWatch, 11 Aug 2026) Planet released ~250,000 previously restricted Iran images; TerraWatch's takeaway: "access to commercial imagery can be paused at a government's request" and for insurers, traders and energy firms "guaranteed continuity is worth more than a gain in resolution". See also the Defence section ("Iran war 2026") and Theme 18 ("shutter control") for the full timeline (CJR, Breaking Defense, Via Satellite "Who can switch this off?").
- **Hackathon angle:** "When the satellites go dark" toolkit: what *can* be verified from Sentinel-1/2, Sentinel-5P, VIIRS/FIRMS fire detections and night lights alone, with honest uncertainty.
- **Credibility:** Reputable press (Al Jazeera via Reuters; TheWrap via NYT; Boston Globe).
- **Sources:** [TerraWatch Essentials 11 Aug 2026](https://newsletter.terrawatchspace.com/earth-observation-essentials-august-11-2026/); [Al Jazeera, 5 Apr 2026](https://aljazeera.com/news/2026/4/5/us-satellite-firm-planet-labs-announces-blackout-on-war-on-iran-images); [TheWrap, 4 Apr 2026](https://www.thewrap.com/media-platforms/journalism/satellite-company-restricts-images-press-cover-iran-war-government-request/); [Boston Globe, 5 Apr 2026](https://www.bostonglobe.com/2026/04/05/nation/us-request-prompts-planet-labs-to-withhold-iran-war-images/); [Al-Monitor, Apr 2026](https://www.al-monitor.com/originals/2026/04/satellite-firm-planet-labs-indefinitely-withhold-iran-war-images); [Business & Human Rights Resource Centre](https://www.business-humanrights.org/en/latest-news/planet-labs-suspends-access-to-iran-satellite-imagery-indefinitely-at-us-request-incl-co-non-response/).

---

## Part A.5 — LLM / agentic geospatial products and tooling

Conversational and agentic interfaces to EO data from Planet, Google, Microsoft/NASA, Esri, Element 84 and startups, and what practitioners say about trust, provenance and tasking standards.

### Planet × Anthropic (Mar 2025)
- **What it is:** Planet Labs announced on 6 Mar 2025 it would use Anthropic's Claude to analyse its daily imagery; companies described "near real-time pattern recognition and anomaly detection at global scale". Will Marshall cited government threat monitoring, smallholder crop yields, California wildfire response, Congo conservation. Planet shares fell >4% on the day.
- **Problems / pain points:** The imagery-to-insight gap; too much daily imagery for humans.
- **Status:** No public measured results from the Anthropic partnership found. In May 2026 Planet showed a private-beta *agentic geospatial query* ("Where are new construction sites appearing in Florida?" → archive search, map, tracking over time, shareable report) aimed at insurance adjusters, infrastructure managers and civil officials — "Agentic AI compresses decision loops into minutes"; the LLM partner is not named in that coverage (Via Satellite, 21 May 2026 — see Part B trade-press entry).
- **Credibility:** Official press release + trade press.
- **Sources:** [Via Satellite — Planet agentic query, 21 May 2026](https://www.satellitetoday.com/imagery-and-sensing/2026/05/21/planet-is-building-an-agentic-geospatial-ai-query/); [Business Wire, 6 Mar 2025](https://businesswire.com/news/home/20250306606139/en/Planet-and-Anthropic-Partner-to-Use-Claudes-Advanced-AI-Capabilities-to-Turn-Geospatial-Satellite-Imagery-into-Actionable-Insights); [Geo Week News, 7 Mar 2025](https://geoweeknews.com/news/planet-and-anthropic-partner-to-use-claude-s-advanced-ai-capabilities-to-turn-geospatial-satellite-imagery-into-actionable-insights).

---

### Google Earth AI / Geospatial Reasoning
- **What it is:** Apr 2025 Google Research introduced geospatial foundation models and "Geospatial Reasoning"; Jul 2025 Google Earth AI launched as a collection of models/datasets (incl. AlphaEarth Foundations embeddings); 23 Oct 2025 a Gemini-based geospatial reasoning agent that "deconstructs a complex question into a multi-step plan", calls foundation models (new Imagery and Population models), queries datastores and fuses results. Access limited: US Google Earth Professional users and "Trusted Tester" companies; humanitarian orgs can apply. Early use: flood detection, algae blooms; GiveDirectly used flood + population data to target aid.
- **Details from the 23 Oct 2025 post (Niv Efron, Luke Barrington):** the agent calls sub-agents using Earth AI models plus Data Commons and Earth Engine. *Remote Sensing Foundations* (imagery VLMs, open-vocabulary detection — "find all flooded roads") report ">16% average gain on text-based image search" and a zero-shot detector that "more than doubles baseline accuracy on novel objects"; *Population Dynamics Foundations* embeddings for 17 countries, monthly (Brazil dengue 12-month-ahead R² 0.456 → 0.656 in an Oxford study); riverine flood forecasts covering 2 billion people. On a geospatial Q&A benchmark the agent scored 0.82 vs 0.50 (Gemini 2.5 Pro) and 0.39 (2.5 Flash). Population + AlphaEarth embeddings improved FEMA National Risk Index prediction by 11% R² on average across 20 hazards (tornado +25%, riverine flood +17%). Users: Bellwether (Google X; storm building damage), UN Global Pulse (post-disaster damage), GiveDirectly (flood-targeted cash aid), Google.org grantees (Khushi Baby, Cooper/Smith, Direct Relief), enterprises Public Storage, CARTO, Visiona (Embraer). Access via early-access interest forms / Vertex AI. "We are just beginning to explore the full potential of Earth AI."
- **Problems / pain points:** Multi-dataset questions ("which vulnerable communities will this storm hit?") currently need analysts to stitch together many layers; access is gated (trusted testers), so NGOs and small teams can't use it yet — an opening for open-data equivalents.
- **Hackathon angle:** Reproduce a "mini Earth AI agent" on open components (AlphaEarth embeddings on Earth Engine, GloFAS/Google flood forecasts, WorldPop/Populace, OSM) for one question type, e.g., "which clinics are in tomorrow's flood footprint?".
- **Credibility:** Official (Google Research blog) + press.
- **Sources:** [Google Research — Geospatial Reasoning, 8 Apr 2025](https://research.google/blog/geospatial-reasoning-unlocking-insights-with-generative-ai-and-multiple-foundation-models/); [Google blog — Earth AI, Jul 2025](https://blog.google/innovation-and-ai/products/google-earth-ai/); [Google Research — Earth AI cross-modal reasoning, 23 Oct 2025](https://www.research.google/blog/google-earth-ai-unlocking-geospatial-insights-with-foundation-models-and-cross-modal-reasoning/); [R&D World](https://www.rdworldonline.com/google-earth-ai-shifts-from-map-layers-to-decision-support-with-geospatial-reasoning-agent/); [The Decoder](https://the-decoder.com/google-integrates-earth-ai-and-gemini-language-models-for-what-it-calls-geospatial-reasoning/).

---

### Microsoft Planetary Computer Pro (Jun 2025) and NASA Earth Copilot (Nov 2024)
- **What it is:** *Planetary Computer Pro* (public preview, announced 17 Jun 2025) is an Azure service to ingest, catalogue, store, process and share *private* geospatial data, integrated with Microsoft Fabric, Azure AI Foundry, Power BI and Esri ArcGIS Pro/Enterprise. Named users: Space Intelligence (forest/carbon, "petabytes of data annually"), Impact Observatory (global land-use/land-cover "in less than a week" on 1,000 VMs), EY, and Xoople (building its "Earth Intelligence system" on it). *Earth Copilot* is a proof-of-concept NASA IMPACT + Microsoft assistant on Azure OpenAI to search NASA's ">100 petabytes" of Earth science data in plain language, designed to plug into NASA's VEDA platform; as of the announcement it was available only to NASA scientists for testing.
- **Problems / pain points:** "Geospatial data is complex, and often requires some level of technical expertise to navigate it" (Microsoft/NASA, Nov 2024); geospatial data is "notoriously complex and siloed across a variety of sources" (Microsoft, Jun 2025).
- **How they're trying to solve it:** managed STAC-style catalogues + LLM front ends + BI integration.
- **Hackathon angle:** an "Earth Copilot for the public" that actually ships: natural-language → NASA CMR / Planetary Computer STAC search → a map + a cited answer.
- **Credibility:** Official.
- **Sources:** [Azure blog, 17 Jun 2025](https://azure.microsoft.com/en-us/blog/microsoft-planetary-computer-pro-unlocking-ai-powered-geospatial-insights-for-enterprises-across-industries/); [Microsoft public-sector blog, 14 Nov 2024](https://blogs.microsoft.com/public-sector/2024/11/14/from-questions-to-discoveries-nasas-new-earth-copilot-brings-microsoft-ai-capabilities-to-democratize-access-to-complex-data/).

---

### Esri ArcGIS AI assistants and agents (2025–2026)
- **What it is:** Esri organises ArcGIS AI into (1) tools and pretrained models, (2) AI assistants (task assistants in ArcGIS Pro, Business Analyst, Survey123; coding assistants for Python/Arcade — ArcGIS Pro Assistant was in beta as of the Feb 2026 release), (3) agentic AI: external agents connecting to ArcGIS as a tool provider "via MCP or other mechanisms", agentic mapping apps, and geospatial agents built in ArcGIS. Esri is developing two imagery models: a remote-sensing foundation model trained on Landsat, Sentinel and NAIP, and a vision-language model for map-based queries. 2026 User Conference (Jul 2026) reiterated assistants + agentic AI "grounded in authoritative geospatial data".
- **Problems / pain points:** ArcGIS is powerful but expert-only; the assistants aim at the GIS skills gap. A UC blog notes the capabilities raise "questions" organisations should consider (governance), without detail.
- **Hackathon angle:** Esri is the incumbent; a hackathon team should not compete head-on but can build a narrow agent that uses open data where Esri's tools are licensed and expensive.
- **Credibility:** Official (Esri newsroom / architecture centre) + university extension blog.
- **Sources:** [Esri ArcNews](https://www.esri.com/about/newsroom/wp-json/wp/v2/arcnews/773548); [Esri Architecture Center — Geospatial AI](https://architecture.arcgis.com/en/industry-and-tech-patterns/ai-lens/geospatial-ai.html); [geospatialtraining.com survey of ArcGIS AI tools](https://geospatialtraining.com/survey-of-ai-tools-across-the-arcgis-platform/); [UC ANR IGIS blog — 2026 Esri UC Day 2, 15 Jul 2026](https://ucanr.edu/blog/igis/article/2026-esri-user-conference-day-2).

---

### Element 84 — Limner (ex "Queryable Earth"), Geospatial Tech Radar 2025/2026, STAPI
- **What it is:** Element 84 is a geospatial software consultancy (STAC co-creators, Earth Search, FilmDrop, Cirrus). *Limner* (Jul and Oct 2026) is a "conversational geospatial analysis tool": e.g., find new solar farms via change detection, measure area, write code to estimate output; or flood-loss estimation using flood depth COGs on S3 + USACE National Structure Inventory + depth-damage curves; data sources include NASA FIRMS, NASA CMR, Registry of Open Data on AWS, Zarr. Every tool call is recorded with inputs and full response, and all code is saved, "so you never have to guess how Limner reached its conclusion."
- **Problems / pain points (their own words):**
  - Trust/provenance: "For AI agents, an answer is only useful if someone can check it." "That's hard to do if all the intermediate steps disappear when the conversation ends." In user testing, participants asked which dataset was used before trusting results; confidence scores were "hard to interpret or unreliable", showing the chain of steps worked better (Tech Radar 2026, Oct 2026).
  - Tooling: "CNG has largely meant a pile of mostly inaccessible technologies with lots of sharp edges"; agent infrastructure "weren't designed with agents in mind, so most teams, including us, are building their own"; "federal rules increasingly restrict those models in government systems and defense contracts" (on Chinese open-weight models).
  - Tasking friction (Matt Hanson, "If AI Is Going to Task Satellites, We Need Standards", 26 Feb 2026): one provider uses REST, another SOAP, "a third relies on email and shapefiles"; delivery via FTP polling, opaque S3 buckets or download links "sent days later"; no standard way to ask feasibility; capabilities "buried in PDFs and emails". "We are trying to build Star Trek on top of infrastructure that still feels like the telegraph system." "An AI hallucinating a satellite tasking request is expensive and wasteful." Proposes STAPI (Sensor Tasking API: Discovery, Feasibility, Delivery) as the "HTTP of Tasking" — "When the task is complete, the agent doesn't get a zip file; it gets a STAC Item." (STAPI 0.1 released Apr 2025.)
  - Tech Radar 2025 (30 Oct 2025): agents/MCP to *Adopt*; pixel-level embedding fields (TESSERA, AlphaEarth) in *Assess*; GeoZarr on *Hold* because "the GeoZarr specification is completely gridlocked".
  - Tech Radar 2026 (Oct 2026): chat interfaces for geospatial data moved to *Adopt*; AlphaEarth public embeddings mirror had served 178 TB; geoembeddings.org conventions v0.0.1 to link each embedding to its model and imagery; text-aligned EO embeddings for "houses with new swimming pools"-type search; captioning imagery with an LLM then embedding captions — Claude Opus matched a satellite-specific model but "expensive at scale".
  - STAC retrospective (28 Oct 2025): before STAC "Every new dataset, whether from a government agency or a commercial provider, was its own puzzle."
  - "Building Conversational Interfaces for Querying and Analyzing Geospatial Data" (Mar 2026; NOAA-funded): an "algorithm agent" assembles a bespoke algorithm from pre-defined functions as validated JSON, then translated to Python and run on Dask — "a compromise between the flexibility of the former and the reliability of the latter"; a "data search agent" queries a knowledge graph of dataset metadata; one orchestration agent talks to the user; "it is important that all the steps performed be transparent and verifiable" (shows progress, provenance and pseudocode).
  - "ChatGSFC" (6 Apr 2026): LibreChat-based internal NASA Goddard tool used by "Over 7,000 people across NASA"; lesson: users "build agents that look correct but are inaccurate", so guardrails/training are needed; "Users will tolerate rough edges early on, but sustained adoption depends on the tool being reliable and well-maintained."
  - Further Tech Radar 2026 points: "Provenance is different from observability" and "we haven't found much tooling for it yet"; the STAC processing extension "was not designed with agents in mind"; finding change "takes more than finding similar images". Limner is built on LibreChat with MCP tools incl. the AWS Registry of Open Data MCP server and the NASA Earthdata MCP server over CMR; its "Agentic Data Storage" keeps large artefacts outside the context window with "a complete chain of custody that you can inspect and reproduce". Earlier: natural-language geocoding ("Within 10 miles of Washington DC" → GeoJSON via an LLM-generated operation tree, 7 May 2024).
- **Off-the-shelf tech:** STAC, stac-fastapi, pystac-client, odc-stac, STAPI, MCP / FastMCP (AWS RODA MCP, NASA Earthdata MCP), Pydantic AI, LibreChat, LiteLLM, Langfuse, PMTiles, GeoParquet, Zarr/Icechunk, AlphaEarth embeddings.
- **Hackathon angle:** (a) a *provenance-first* geospatial agent that emits a reproducible notebook + STAC items for every answer (directly addresses the trust gap Element 84 documents); (b) a STAPI-compatible "tasking feasibility" mock that tells a user whether a collection over an AOI is feasible given orbits (TLEs) + cloud forecast.
- **Credibility:** Company blogs (practitioner, well-regarded open-source contributors).
- **Sources:** [Tech Radar 2026, Oct 2026](https://element84.com/geospatial/geospatial-tech-radar-2026-an-emphasis-on-provenance-and-refined-tooling-from-ai-to-cloud-native/); [If AI Is Going to Task Satellites, We Need Standards, 26 Feb 2026](https://element84.com/software-engineering/if-ai-is-going-to-task-satellites-we-need-standards/); [(Re) Introducing Limner, Oct 2026](https://element84.com/machine-learning/re-introducing-limner/); [Introducing the new Limner, Jul 2026](https://element84.com/geospatial/introducing-the-new-limner-conversational-composable-and-traceable/); [Tech Radar 2025, 30 Oct 2025](https://element84.com/company/the-2025-geospatial-tech-radar-agentic-ai-eo-embeddings-and-cloud-native-maturity/); [STAC retrospective part 2, 28 Oct 2025](https://element84.com/software-engineering/stac-a-retrospective-part-2-why-stac-was-successful/); [Conversational interfaces, Mar 2026](https://element84.com/machine-learning/building-conversational-interfaces-for-querying-and-analyzing-geospatial-data/); [ChatGSFC, 6 Apr 2026](https://element84.com/machine-learning/chatgsfc-building-composable-ai-tools-for-nasa-on-open-source-tooling/); [Radar site](https://element84.com/geospatial-tech-radar-26/); [Natural Language Geocoding, 7 May 2024](https://element84.com/machine-learning/natural-language-geocoding/); [Element 84 blog index](https://element84.com/blog/).

---

### Development Seed
- **What it is:** Washington DC geospatial consultancy (NASA VEDA, eoAPI, TiTiler, open-source cloud-native tooling; named by Morrison among the consultancies that "platforms" turn into). Latest post (2 Oct 2026): "A Primer for Earth Data Embeddings" — embeddings help systems "search, compare, and reason across Earth observation data".
- **Hackathon angle:** eoAPI/TiTiler give a ready tile server for any COG/STAC data — reduces hackathon plumbing.
- **Credibility:** Company blog.
- **Sources:** [Development Seed blog](https://developmentseed.org/blog).

---

### Penn State GIS Copilot (open-source QGIS agent) and academic "geospatial copilots"
- **What it is:** QGIS plugin for natural-language spatial analysis on vector and raster data; v1.0 (Oct 2025) defaults to GPT-5 with configurable reasoning; local LLM support planned. Paper (*International Journal of Digital Earth*, 2025) tested 100+ tasks: high success on basic/intermediate tasks, "challenges remaining in fully autonomous execution of advanced tasks". Related: *GeoLLM-Squad* (arXiv Jan 2025, "Multi-agent geospatial copilots for remote sensing workflows") delegates RS tasks to specialised sub-agents; an open-source LATAM "geo-copilot" (LLM + PostGIS + MapLibre + MCP servers, with human approval).
- **Problems / pain points:** Advanced multi-step GIS tasks still fail autonomously → trust and the need for human-in-the-loop.
- **Hackathon angle:** use these as baselines; the gap is EO-specific (raster time series, cloud masking, change detection) rather than vector GIS.
- **Credibility:** Peer-reviewed (IJDE) + arXiv preprint + GitHub.
- **Sources:** [GIS Copilot paper, IJDE 2025](https://www.tandfonline.com/doi/full/10.1080/17538947.2025.2497489); [GIS Copilot v1.0 released, PSU, Oct 2025](https://giscience.psu.edu/2025/10/01/gis-copilot-v1-0-released/); [GeoLLM-Squad, arXiv 2501.16254](https://arxiv.org/html/2501.16254v1); [geoai-latam/geo-copilot on GitHub](https://github.com/geoai-latam/geo-copilot).

---

### LGND
- **What it is:** "Earth intelligence company" that "turns decades of satellite and aerial imagery into queryable datasets"; *LGND Geo* (AI agent answers "grounded in what imagery shows, with supporting evidence attached"), *LGND Studio* (no-code app for analysts to create and validate datasets), API. Few-examples → find similar features globally. Use cases: energy (construction, exploration, production), insurance (hazard modelling), logistics. Team from Google, Microsoft, NASA, Mapbox (founders and funding not stated on the homepage — unverified).
- **Problems / pain points:** finding useful information in huge imagery volumes; non-technical users.
- **2026 news (via TerraWatch):** LGND launched natural-language imagery search that plugs into ChatGPT and Claude (Oct 2026; covers Sentinel-2 and NAIP).
- **Hackathon angle:** embedding similarity search ("find more like this") over AlphaEarth / Clay embeddings with a no-code UI.
- **Credibility:** Official homepage + analyst newsletter.
- **Sources:** [lgnd.ai](https://lgnd.ai/); [TerraWatch Essentials 12 Oct 2026](https://newsletter.terrawatchspace.com/earth-observation-essentials-october-12-2026/).

---

### Mundi.ai (Bunting Labs) — hosted "AI-native GIS" shut down
- **What it is:** "An open source, AI-native web GIS" (AGPL-3.0; LLMs call geoprocessing algorithms and edit symbology; PostGIS; optional QGIS; works with local LLMs). As of Oct 2026 the homepage says the "mundi.ai cloud is no longer available" and "We are no longer providing Mundi AI online" — users can self-host from GitHub (date of shutdown not stated — unverified).
- **Problems / pain points:** Evidence that a generic AI-GIS front end is hard to sustain as a business (consistent with Morrison's "platforms" critique), even when the tech works.
- **Credibility:** Official homepage + GitHub.
- **Sources:** [mundi.ai](https://mundi.ai/); [GitHub buntinglabs/mundi.ai](https://github.com/buntinglabs/mundi.ai).

---

## Part B.1 — Analysts, newsletters and essayists

How the industry's best-known commentators describe its problems (demand, procurement, platforms, AI hype, access, consolidation).

### Joe Morrison — "A Closer Look with Joe Morrison" (Substack), 2020–2023 essays
- **What it is:** The most-cited critical essay series on commercial satellite-imagery business models. Morrison was at Azavea (Raster Foundry), then joined SAR operator Umbra in 2021 (VP Commercial Product, later listed as VP Growth). Umbra says his posts are read by tens of thousands monthly. The archive's most recent post is March 2023; no 2024–2026 posts were found.
- **Problems / pain points (by essay):**
  - *"The Commercial Satellite Imagery Business Model is Broken"* (7 Aug 2020): buying imagery is "closer to a hostage negotiation than a sales transaction". Providers depend on the US government and treat commercial buyers as an afterthought. "The lie is this: someone, somewhere is making a ton of money using satellite imagery." Archive pricing is too high: "Lack of affordability of archival imagery is stifling innovation." His fix is self-serve: "I should be able to hit an API or submit a request for exactly what I want without asking anyone for permission." Also: "Stop treating your archival data like a goldmine" and "Charge as much money as you can for tasking satellites."
  - *"Open Letter to a Newly Formed Satellite Imagery Company"* (29 Oct 2020): "There is currently next-to-no commercial demand for satellite imagery (of all sorts)." This is a chicken-and-egg problem: no demand without access, no access without demand. He names four barriers (capacity, licensing, transparency, education) and recommends releasing ~1% of capacity as CC0, publishing prices, and letting vetted buyers self-serve. "Treat your archival data like pickaxes and shovels and your tasking capacity like gold." Risks he concedes: government most-favoured-price clauses and channel conflict with resellers.
  - *"Stop Building Satellite Imagery Platforms and Marketplaces"* (12 Nov 2020): "Fundamentally, I don't think they work." Why: "One word: demand." Also: "No one wants satellite imagery, sure, but also almost no one wants information derived from satellite imagery." Platforms drift into consulting. Google Earth Engine competes for free. Suppliers fear channel conflict: "if someone at one of the major imagery providers decides you're done…you're done." His example is TerraServer (owned by PrecisionHawk), which shut abruptly in 2020. Named marketplaces: Arlula, SkyWatch, UP42, Shadowbreak. Named platforms: Astraea, Descartes Labs, Orbital Insight, SpaceKnow. Counterpoints he lists: STAC, COG and OGC API standards, and cheaper smallsats.
  - *"Satellite Imagery is Not Becoming a Commodity"* (29 Mar 2021): "It's still ridiculously difficult and expensive to buy high resolution, tasked imagery." Images are not interchangeable: change monitoring depends on calibration, co-registration and positional accuracy, as shown by comparing Ever Given images across vendors. Turning raw data into analysis-ready data takes specialist work. "satellite imagery providers who build out analytics teams will always have the upper hand."
  - *"Nobody wants your fancy algorithm"* (18 Apr 2022): "selling derived data as a subscription product does. not. work." Each customer defines "change" differently, so generic change feeds fail: "The most practical approaches I've seen to subscription data feeds are always custom." Also: "What people want is for you to solve their problems for them," and "Actions are facilitated by applications."
  - *"Open All of the Satellite Imagery Archives"* (23 May 2022): after Landsat went free in 2008–09, downloads rose ~100× in a decade. A 2017 USGS estimate put Landsat's value at $3.45B/yr. Commercial archives of petabytes sit largely unused. "No one ever got fired by the board for not giving their archive away." He proposes requester-pays cloud hosting and government buys for public use.
  - *"A Simple Mental Model for Understanding the Satellite Imagery Industry"* (29 Nov 2022): there are three "rackets": Mapping, Monitoring and Mobilizing. Mapping is lumpy, one-off and losing to aerial imagery and drones. Monitoring is the fastest-growing category but hard to differentiate from free public data. Mobilizing is the most profitable but "doesn't naturally result in recurring revenue." On where the difficulty lies: "the hardest part of building a satellite imagery company isn't the satellite imagery part - it's the company part."
  - *"How 'Internet in Space' Will Transform the Satellite Imagery Industry" Parts I–II* (30 Dec 2022; 3 Jan 2023): "There are three key value propositions in the business of satellite imagery: resolution, coverage, and latency." Also: "Latency is tightly correlated with pricing power," and "low latency is expensive to provide, and rarely necessary." Tasking uplink and downlink are ground-station-bound: "Your ideal satellite will whiz right by your target at 16,000mph in blissful ignorance." He predicts relay networks such as Starlink will make "direct tactical downlink" "go extinct" and will consolidate ground-station businesses.
  - *"How to Change an Industry"* (15 Mar 2023): Umbra opens sample data under an open licence, offers self-serve tasking and publishes prices. "Our strategy, in a nutshell, is to simply not jerk people around." He calls for "a wave of entrepreneurs able to turn this raw material into finished products."
- **How they're trying to solve it:** Open sample archives (Umbra's open data program), published price lists, self-serve tasking APIs, open licences (CC0 / CC BY 4.0), cloud-native standards (STAC, COG), and building vertical applications rather than generic feeds.
- **Data:** Umbra Open Data (SAR, CC BY 4.0, on AWS) is the concrete artifact of his argument. Landsat and Sentinel are the "free baseline" he cites.
- **Off-the-shelf tech:** STAC, Cloud-Optimized GeoTIFF, OGC API Features, Google Earth Engine, Raster Foundry (Azavea, legacy).
- **Hackathon angle:**
  - (a) A "what will this image cost me and how fast" comparator across providers that publish prices (Umbra, SkyFi, Arlula, UP42) to attack pricing opacity.
  - (b) A customer-defined "what counts as change" tool: the user gives 3–5 labelled examples and gets a tuned Sentinel-2/Sentinel-1 change alert. This targets his critique that generic change feeds fail.
  - (c) A "mobilize" demo: an event (fire, flood, port incident) triggers a pull of the newest free imagery plus a tasking quote.
- **Credibility:** Blog (an industry insider with a disclosed conflict of interest as an Umbra employee). Widely cited.
- **Sources:**
  - [Business Model is Broken, 7 Aug 2020](https://joemorrison.substack.com/p/the-commercial-satellite-imagery)
  - [Open Letter, 29 Oct 2020](https://joemorrison.substack.com/p/open-letter-to-a-newly-formed-satellite)
  - [Stop Building Platforms and Marketplaces, 12 Nov 2020](https://joemorrison.substack.com/p/stop-building-satellite-imagery-platforms)
  - [Not Becoming a Commodity, 29 Mar 2021](https://joemorrison.substack.com/p/satellite-imagery-is-not-becoming)
  - [Nobody wants your fancy algorithm, 18 Apr 2022](https://joemorrison.substack.com/p/nobody-wants-your-fancy-algorithm)
  - [Open All the Archives, 23 May 2022](https://joemorrison.substack.com/p/open-all-of-the-satellite-imagery)
  - [Mental Model, 29 Nov 2022](https://joemorrison.substack.com/p/a-simple-mental-model-for-understanding)
  - [Internet in Space I, 30 Dec 2022](https://joemorrison.substack.com/p/how-internet-in-space-will-transform)
  - [Internet in Space II, 3 Jan 2023](https://joemorrison.substack.com/p/how-internet-in-space-will-transform-11a)
  - [How to Change an Industry, 15 Mar 2023](https://joemorrison.substack.com/p/how-to-change-an-industry)
  - [Archive](https://joemorrison.substack.com/archive)
  - [Umbra announcement of his role](https://umbra.space/blog/joe-morrison-becomes-umbras-vp-of-commercial-product/)
  - [LiveEO podcast #24 (Feb 2023)](https://www.live-eo.com/blog/24-joe-morrison-on-his-companys-edge-in-earth-observation)
  - [SatSummit 2024 speaker page](https://satsummit.io/2024-washington/speakers/joe-morrison/)

---

### TerraWatch Space (Aravind Ravichandran) — "Earth Observation Essentials" newsletter, Premium reports, EO Summit
- **What it is:** An independent EO advisory and market-research firm. It publishes a free weekly/biweekly "Earth Observation Essentials" with Pro and Premium tiers. From 1 Jan 2026, Pro rose from $49 to $99/yr and Premium from $299 to $499/yr. TerraWatch also runs the user-centric EO Summit (London 2024, New York 2025, 22 June 2026 per the Satellite Applications Catapult listing) and a cohort course, "The Business of Earth Observation" (March 2026).
- **Problems / pain points (by issue):**
  - *State of Commercial EO 2025 Edition* (22 Oct 2025, paywalled; visible part only): "Governments have become the dominant buyers, but the promise of scalable commercial markets remains unproven." "Platforms are multiplying, yet it is unclear whether they can differentiate beyond selling access to pixels." On AI, the open question is "whether they solve adoption bottlenecks or simply add another layer of hype." It sorts companies into three waves: horizontal pioneers (Planet, Satellogic, BlackSky, Spire, ICEYE), vertical specialists (GHGSat, OroraTech, Constellr, Wyvern, Hydrosat) and backward integrators (Tomorrow.io, EarthDaily, SatSure), with satellites as "enablers, not products".
  - *Essentials 13 Oct 2025*: Albedo exits commercial imagery to sell VLEO buses after raising ~$100M: "even technically differentiated players will struggle to turn pixels into predictable revenue", and "selling EO infrastructure remains the short-term growth fix." Also in the issue: Maxar split into Vantor ("spatial intelligence") and Lanteris, and Muon Space won a $45M Space Force weather-data contract.
  - *Towards a Global EO Accord* (1 Dec 2025): the Sentinel-1B failure left SAR gaps and "There was no agreed framework for backup." CEOS and GEO "do not commit governments to anything", and "The gap is not technical coordination. It is political commitment."
  - *Essentials 17 Dec 2025, "Five themes that defined EO in 2025"*:
    1. Dual-use "moved from euphemism to explicit strategy".
    2. Defence became the growth engine, and the commercial scaling story "has stalled": "D&I revenue share is growing while share from commercial verticals is flat or declining."
    3. Civil EO programmes were questioned, and calibration, continuity and open data have "no commercial business case".
    4. AI moved from hype to reality but adoption lags: models struggle outside training regions, embeddings from different providers are not interoperable, and GeoAI stays in research or one-off projects.
    5. Climate EO lost traction as EU deforestation and sustainability-reporting rules were delayed or weakened and the voluntary carbon market failed to fill the gap.
    Same issue: Overstory raised a $43M Series B ("EO is disappearing into grid management workflows"), ICEYE raised €150M at a €2.4B valuation, and ESA got a record €22.1B (~€3.5B for EO).
  - *Essentials 13 Apr 2026, "2026 EO Adoption Hype Cycle"*: 20 use cases ranked by willingness to pay. The plateau use cases are government-anchored: D&I, disaster response, maritime domain awareness and mapping. "no genuinely new commercial EO use cases are forming", and the real job is "converting what it can already do into something buyers operationally and repeatedly pay for." Free Sentinel and Landsat data structurally caps commercial adoption for some use cases. Same issue: Xoople raised $130M ("they laid the distribution pipes before having their own data supply" via Microsoft/Esri), Starcloud raised $170M, and the FY27 NASA request cuts Earth science 52% ($2.15B → $1.02B) and proposes "one final Landsat satellite" plus $109M toward commercial Landsat. Also cited: a BBC piece on humanitarian and journalist concern about Planet restricting imagery access, and Bellingcat's Sentinel-1 damage-assessment tool.
  - *Essentials 11 May 2026*: the Enagás × Orbital Eye pipeline-monitoring rollout across Spain took ~5 years from pilot, and "most never get past the pilot stage." It worked because the output is binary, the alternative (patrolling ~9,000 km) is costly, and one buyer can deploy nationally. Most EO use cases have ambiguous outputs, cheap alternatives or fragmented procurement. On orbital compute: "EO workloads are now the anchor demand", since Starcloud's first satellite processes Capella SAR. Also: HawkEye 360 IPO at $3.1B, and a note that Taiwanese farms (<1 ha) break crop algorithms built for Western farms.
  - *Essentials 24 Aug 2026*: Muon Space $250M Series C, Starcloud +$250M with Nvidia, and EO operators worried that SpaceX may wind down commercial Falcon 9 launches. NOAA has awarded >$180M to commercial weather companies, "yet the commercial weather market has not thrived." On the future of Landsat, NASA/USGS want to buy *finished products* in FY27 (bathymetry, surface-water extent, burned area and severity, then evapotranspiration): "The requirement becomes the product." Multi-sensor inputs make it "a calibration problem rather than a hardware one", and he calls it "a demand signal, not a contract." It is unclear who owns or can redistribute the products. Also: Sentinel-3 data now reaches emergency services in 60 minutes instead of 180.
  - *Why an EO Summit* (16 Feb 2024): conferences are supply-side and "very technology-focused", and "hearing from users will enable the EO sector to discover things we are overestimating and overselling."
- **How they're trying to solve it:** User-centric events with enterprise tracks (insurance and risk, energy and infrastructure, agriculture and environment), problem-led rather than technology-led EO strategy, and government as a structured product buyer (the commercial Landsat products model).
- **Data:** None of its own. It points to Landsat, Sentinel, NISAR, Biomass, GHGSat and Planet.
- **Off-the-shelf tech:** Geospatial embeddings (Google AlphaEarth), IBM–ESA TerraMind, and Prithvi are named as available but under-adopted.
- **Hackathon angle:**
  - (a) A "commercial Landsat product" prototype: burned-area or surface-water-extent product fusing Landsat with Sentinel-2/HLS and a cross-sensor calibration check. This mirrors NASA/USGS's FY27 product buy.
  - (b) An embedding-interoperability demo: compare AlphaEarth embeddings with Clay/Prithvi embeddings on the same AOI and show where they disagree.
  - (c) A binary-output, high-cost-alternative use case like pipeline right-of-way encroachment detection on Sentinel-2. TerraWatch says these use cases are the ones that scale.
  - (d) A smallholder-farm (<1 ha) crop-mapping robustness check.
- **Credibility:** Analyst newsletter (reputable in the industry, partly paywalled). Some figures come only from search snippets and are marked as such.
- **Sources:**
  - [State of Commercial EO 2025, 22 Oct 2025](https://newsletter.terrawatchspace.com/state-of-commercial-earth-observation-2025-edition/)
  - [Essentials 13 Oct 2025](https://newsletter.terrawatchspace.com/earth-observation-essentials-october-13-2025/)
  - [Global EO Accord, 1 Dec 2025](https://newsletter.terrawatchspace.com/towards-a-global-earth-observation-accord/)
  - [Essentials 17 Dec 2025](https://newsletter.terrawatchspace.com/earth-observation-essentials-december-17-2025/)
  - [Essentials 13 Apr 2026](https://newsletter.terrawatchspace.com/earth-observation-essentials-april-13-2026/)
  - [Essentials 11 May 2026](https://newsletter.terrawatchspace.com/earth-observation-essentials-may-11-2026/)
  - [Essentials 24 Aug 2026](https://newsletter.terrawatchspace.com/earth-observation-essentials-august-24-2026/)
  - [Why an EO Summit, 16 Feb 2024](https://terrawatch.substack.com/p/why-an-eo-summit)
  - [EO Summit 2026 listing, Satellite Applications Catapult](https://sa.catapult.org.uk/events/eo-summit/)
  - [EO Summit 2025 NY write-up (spaceagenda)](https://www.spaceagenda.com/?p=56508)
  - [EOSDA takeaways from EO Summit 2024](https://eos.com/events/eosda-attends-eo-summit-2024-in-london/)
  - [Ravichandran, "Making EO Mainstream", GWF 2023 slides](https://geospatialworldforum.org/2023/presentation/Space-Spatial-Value-Chain/Making-Earth-Observation-Mainstream-Aravind_Ravichandran.pdf)
  - [satsearch interview, 11 Mar 2024](https://blog.satsearch.co/2024-03-11-trends-in-the-earth-observation-sector-with-aravind-ravichandran-of-terrawatch-space)

---

### TerraWatch Space — 2026 issues, continued (embeddings, sovereignty, insurance, banks, hyperspectral, M&A, H1 2026 funding)
- **What it is:** The same newsletter as above. These are the May–Oct 2026 issues, which are the most recent primary commentary on EO industry structure.
- **Problems / pain points:**
  - **Embeddings make downstream analytics obsolete** (Essentials 11 Aug and 12 Oct 2026). Google's *Custom Satellite Embeddings* (Private Preview, July 2026) is built on AlphaEarth: 64-dimensional vectors per 10 m pixel, custom AOIs refreshed on ~5-day cycles, available through the Google Maps Platform API, BigQuery and Vertex AI. TerraWatch calls this "an existential change" for firms selling feature extraction, land-cover classification or change detection, because "Downstream players will no longer be able to monetize raw" pixel-to-insight extraction. The remaining differentiation is "labelled ground truth, validation against field data, and accountability for the answer". The market is "moving away from purchasing raw imagery tiles or paying for per-square-kilometer pixels". Still, "Google's 10m foundation model cannot replace a 30cm optical image or high-resolution SAR."
  - **Embeddings are not interoperable** (Essentials 28 Sep 2026): "embeddings produced by two different EOFMs likely cannot be compared or combined, unless by design." Embeddings are "not neutral", since they depend on each model's training data. (The foundation-model Premium deep dive of 4 Sep 2026 is mostly paywalled.)
  - **Imagery supply is conditional** (Essentials 11 Aug 2026). Planet released ~250,000 previously restricted Iran images after withholding them for months at US government request: "access to commercial imagery can be paused at a government's request." The BBC and NYT turned to European and Chinese providers in the interim. For insurers, traders and energy firms, "guaranteed continuity is worth more than a gain in resolution". "over 60 countries are building their own EO national constellations" (TerraWatch internal data). Differentiation is shifting "from the capabilities to the assurances around it", and resolution, revisit and coverage no longer separate providers: "the image itself stops being the thing you choose a provider for".
  - **EO M&A wave** (11 Aug 2026): >30 EO acquisitions closed since 2022, rising from 4 to 9 per year, with 7 so far in 2026. Examples:
    - Schneider Electric buys AiDASH (~$350M implied EV)
    - Verisk buys McKenzie Intelligence Services
    - Intermap buys PCI Geomatics ($11M)
    - MSCI buys First Street ($120M)
    - Safran buys Kayrros' geospatial-intelligence activities, and Energy Aspects buys Kayrros' energy assets
    The motives: buy capability, and make EO an invisible infrastructure layer.
  - **Closed climate-risk models become the de facto standard** (Essentials 30 Jun 2026, on MSCI–First Street): "It looks like this unauditable closed layer is becoming the standard everyone trusts." There are no public benchmarks.
  - **Parametric insurance** (Essentials 26 May 2026): "Instead of paying based on what an assessor verifies, it pays based on what a measurement says," and "without EO, parametric was a small market built around weather stations." Candidate triggers are soil moisture, vegetation health, flood extent, fire severity and SST. Basis risk is not covered in the free text. Liberty × ICEYE launched a building-level parametric wildfire product (Jun 2026).
  - **Chinese banks as demand-side EO buyers** (Essentials 30 Jun 2026): Ping An, China Merchants, Pufa and Postal Savings Bank (a 0.5 m satellite with onboard AI, Apr 2026) launch satellites. MYbank's "Great Tit" scores crop conditions for farm credit. ICBC and others use EO for post-loan monitoring of construction progress, warehouses and shipping. "One bank set a threshold: the satellite investment must reduce annual bad debts by 200 million yuan." "China may be building the largest commercial EO user base in the world."
  - **Hyperspectral lacks an open seed mission** (Essentials 8 Jun 2026): "there has not been a hyperspectral equivalent of Sentinel or Landsat at the scale needed." The data are "richer, more complex, and more demanding to process", and the processing stack is immature. CHIME is due in 2028.
  - **EO is three things at once** (Essentials 16 Sep 2026): "a strategic asset and a commercial market and a public good", and "a multi-purpose technology searching for an integrated business model." Enterprises are numerous but make small purchases after long sales cycles and want workflow-ready products. Satellogic reported only $13M revenue in 2024. USDA plans to test satellite imagery and AI for crop estimates after criticism of its data reliability.
  - **Damage assessments disagree** (12 Oct 2026, recommended read from HOT): assessments of the same disaster can differ by sensor, method and definition of "damage".
  - **Methane attribution gap** (28 Sep 2026, citing a Guardian analysis of Carbon Mapper and Planet data): only about a third of detected US oil and gas plumes could be confidently tied to a specific operator.
  - **Funding shifted to "atoms than bits"** (H1 2026 Review, 27 Jul 2026): ~$1.7B of EO VC in H1 2026, of which acquisition (satellites) was ~$1.2B. ICEYE raised $520M at >$12B, Tomorrow.io $210M, Xoople $130M. Intelligence (analytics) rounds were small: Striveworks $33M, Solafune $30M, hummingbirds $55M, Varaha $20M. SkyFi raised $12.7M.
  - **ICEYE economics** (Essentials 30 Jun 2026): ~€250M revenue in 2025, >€100M operating profit, >€1.5B backlog, valued at >€10B. This is a counterexample to "EO is a bad business", driven by sovereign and defence demand.
  - **Vantor/Maxar** (Perspectives 22 May 2026): Advent's $6.4B take-private, then Lanteris sold for $800M (~1.3× revenue). EOCL is $3.24B over 10 years (a $1.5B firm base to ~2027), and it "comes up for recompete in roughly the window Advent would be exiting". The new stack is Vivid (data), Tensorglobe (platform) and Sentry/Raptor (applications), with a Palantir-like positioning. The 90% recurring revenue and $900M ARR are company claims.
- **How they're trying to solve it:** Product-level government buying (commercial Landsat products), contracted availability and multi-region sourcing, embedding-as-a-product, workflow ownership (utilities, insurance), and demand-side specification (the Chinese bank ROI thresholds).
- **Data:** Google AlphaEarth Satellite Embedding dataset (annual, on Earth Engine); Custom Satellite Embeddings (private preview); ESA World Settlement Footprint Tracker (10 m, 6-monthly); Carbon Mapper and Tanager plumes; Planet's ~250k released Iran images.
- **Off-the-shelf tech:** AlphaEarth embeddings, Tessera EOFM (Cambridge/ESA), LGND's natural-language imagery search that plugs into ChatGPT and Claude (Oct 2026; covers Sentinel-2 and NAIP), ESA EVE assistant, and Planet's agentic preview (May 2026).
- **Hackathon angle:**
  - (a) An **embedding "auditor"**: take AlphaEarth annual embeddings plus a second open EOFM over the same AOI, and show where similarity search or change flags agree or disagree with ground truth. This addresses the "accountability for the answer" moat.
  - (b) A **methane plume → operator attribution** helper: join Carbon Mapper plume data to public well, facility and permit databases to attack the "only a third attributable" problem.
  - (c) A **"loan-book satellite monitor"** in the style of the Chinese banks: track construction progress from Sentinel-2 time series for a list of project addresses and flag stalled sites.
  - (d) A **parametric trigger back-tester**: replay a soil-moisture or flood-extent trigger (SMAP, Sentinel-1) against historical events to estimate basis risk.
  - (e) A **disaster-damage reconciliation** view showing why two damage maps of the same event differ.
- **Credibility:** Analyst newsletter (reputable). Company figures are company claims as reported.
- **Sources:**
  - [Essentials 26 May 2026](https://newsletter.terrawatchspace.com/earth-observation-essentials-may-26-2026/)
  - [Perspectives 22 May 2026 (Maxar/Vantor)](https://newsletter.terrawatchspace.com/three-years-on-analysing-advents-maxar-acquisition/)
  - [Essentials 8 Jun 2026](https://newsletter.terrawatchspace.com/earth-observation-essentials-june-8-2026/)
  - [Essentials 30 Jun 2026](https://newsletter.terrawatchspace.com/earth-observation-essentials-june-30-2026/)
  - [H1 2026 Review, 27 Jul 2026](https://newsletter.terrawatchspace.com/earth-observation-h1-2026-review/)
  - [Essentials 11 Aug 2026](https://newsletter.terrawatchspace.com/earth-observation-essentials-august-11-2026/)
  - [EOFM deep dive, 4 Sep 2026](https://newsletter.terrawatchspace.com/earth-observation-foundation-models-a-deep-dive/)
  - [Essentials 16 Sep 2026](https://newsletter.terrawatchspace.com/earth-observation-essentials-september-16-2026/)
  - [Essentials 28 Sep 2026](https://newsletter.terrawatchspace.com/earth-observation-essentials-september-28-2026/)
  - [Essentials 12 Oct 2026](https://newsletter.terrawatchspace.com/earth-observation-essentials-october-12-2026/)
  - [Newsletter index](https://newsletter.terrawatchspace.com/)

---

### New Space Economy (newspaceeconomy.ca) — "Why Does Defense Dominate EO Demand…" (23 Oct 2026) and "The State of Earth Observation 2026" (20 Oct 2026)
- **What it is:** An explainer/aggregator site that synthesises TerraWatch, Novaspace, Analysys Mason, Fortune Business Insights and ESA figures. No author is listed, and the site carries an affiliate disclaimer.
- **Problems / pain points:**
  - It frames an "Earth observation defense paradox": defence and government generate 70–80% of EO revenue (citing a TerraWatch January 2026 sector assessment).
  - Commercial barriers it lists: free Landsat/Copernicus data; a pixels-vs-answers gap (enterprises want risk scores or work orders); drones at 2–5 cm vs ~30 cm from satellites; and capex vs episodic buying.
  - "Path dependency" traps: point-target tasking architecture vs continuous area coverage; security licensing vs "license once, embed everywhere"; and cleared-defence sales teams vs enterprise vertical teams.
  - The 2026 piece claims a "data-volume bottleneck in which orbital collection outpaces human analytical capacity" and says NISAR generates "tens of terabytes of raw phase data every day" (not independently verified).
- **How they're trying to solve it:** Four "crossover" shifts: continuous feeds, foundation models such as Prithvi for pixel-to-decision work, measurable line-of-business ROI, and EO embedded invisibly in enterprise software (the GPS analogy).
- **Data:** It cites NISAR provisional L-band data (released 20 Jul 2026), ESA Biomass P-band (open 26 Jan 2026) and Sentinel-1D (data open 17 Apr 2026).
- **Market figures it quotes:**
  - Novaspace: EO market $5.0B → >$8.0B by 2033; value-added services $3.1B → $4.9B.
  - Analysys Mason (Jun 2026): $29B cumulative D&I opportunity 2024–34.
  - Fortune Business Insights (Sep 2026): $7.68B (2026) → $14.55B (2034).
- **Hackathon angle:** The "embedded invisibly" thesis means building an EO signal that drops into an enterprise tool (a spreadsheet, CRM or work-order system) rather than a map.
- **Credibility:** Secondary aggregator. Figures are attributed to primaries but not verified there. Treat as a pointer.
- **Sources:**
  - [Why does defense dominate…, 23 Oct 2026](https://newspaceeconomy.ca/2026/10/23/why-does-defense-dominate-earth-observation-demand-over-commercial-markets/)
  - [State of EO 2026, 20 Oct 2026](https://newspaceeconomy.ca/2026/10/20/the-state-of-earth-observation-2026/)

---

### Will Cadell (Sparkgeo) — "Strategic Geospatial" newsletter, 2026 posts
- **What it is:** A newsletter by the CEO of Sparkgeo, a geospatial consultancy, with 3,000+ subscribers. One of the few practitioner-strategists writing regularly in 2026.
- **Problems / pain points:**
  - *"Earth is a banana"* (31 Jul 2026), on fake and AI-altered imagery and missing provenance: "Our EO data doesn't have an agreed-upon standard for provenance." Reprojection, cloud removal and super-resolution are rarely recorded. Physical features can be verified by comparing many sensor images over time, but *events* are harder to verify because few sensors cover them at a given moment. He warns of synthetic events, such as adding a nuclear plant in Iran or a crowd outside an embassy, used to "flood the zone". "the geospatial community sleepwalked into this problem, knowing it would happen." His proposal: "Provenance should be stamped into the image and additionally held alongside in STAC metadata", plus geographic benchmarks (Overture's "living POIs", OSM). Example: Google Earth's new image generation (Nano Banana 2) put Barkerville features in the wrong places and would not correct them.
  - *"90% right is 100% wrong: Benchmarking frontier AI for consumer location"* (13 Oct 2026; a talk script from the 2026 CNG Forum in Utah): 500+ questions over 6 North American cities, 9 categories and 3 personas, scored on data quality, spatial context and model reasoning. For "restaurants within 1 km" the correct answer was 8, and "Gemini returning over 30 locations and getting only 4 of the actual restaurants right". Every model missed one of two parks within a five-minute walk. "Claude chose the wrong one twice, once via a connector across the river that doesn't exist." A wildfire agent misplaced markers and replied "good catch". A "Tower of London" query returned a point on Tower Bridge. "What irks me is that I can ask a probabilistic system for a determinate fact and be given a plausible answer that's wrong." Results are preliminary.
  - *"So mid, the missing midstream"* (7 Sep 2026): EO talk focuses on upstream (satellites) and downstream (apps), but "the midstream, the distribution of data, is the critical element that creates a functioning market." Buyers assume an API "solves everything"; the reality is messier, with SLAs and IP ownership unclear.
  - *"So mid, so sovereign"* (21 Oct 2026): "If I allow my data to be downloaded, it is not sovereign," and "Compute alongside Storage == Sovereign." Pixels are duplicated across S3 buckets and sold under different licences "with little lineage or provenance", and the duplication cost lands on taxpayers. Cloud-native adoption is still small, with roughly 200–300 practitioners at the CNG Forum in Utah. He cites the UK EO Data Hub as a compute-next-to-data example. (Vendor content for Sparkgeo's Prescient.)
  - *"Innovation flux; today's three-body problem"* (12 Jul 2026): corporate geospatial buying has slowed under the twin pressures of AI and geopolitics. "Increasing sovereign capability without fixing broken procurement processes" entrenches incumbents.
- **How they're trying to solve it:** Provenance in image headers and STAC, public geographic benchmarks for LLMs, and cloud-native compute-to-data access control (notebook, API or MCP grants that can be revoked).
- **Data:** Overture Maps (POIs), OSM, STAC catalogues, Planetary Computer.
- **Hackathon angle:**
  - (a) A **geospatial LLM-answer verifier**: intercept an LLM's location or imagery claim, check it against OSM/Overture plus the actual Sentinel-2 scene, and return verified, corrected or unverifiable. This addresses "90% right is 100% wrong".
  - (b) An **image-provenance stamper and checker**: write processing history (cloud removal, super-resolution, reprojection) into COG metadata and STAC `processing:` fields, then verify that a published image matches the source scene.
- **Credibility:** Practitioner blog (vendor CEO). The benchmark is preliminary.
- **Sources:**
  - [Archive](https://www.strategicgeospatial.com/archive)
  - [Earth is a banana, 31 Jul 2026](https://www.strategicgeospatial.com/p/earth-is-a-banana)
  - [90% right is 100% wrong, 13 Oct 2026](https://www.strategicgeospatial.com/p/90-right-is-100-wrong-benchmarking)
  - [Missing midstream, 7 Sep 2026](https://www.strategicgeospatial.com/p/the-missing-midstream)
  - [So mid, so sovereign, 21 Oct 2026](https://www.strategicgeospatial.com/p/so-mid-so-sovereign)
  - [Innovation flux, 12 Jul 2026](https://www.strategicgeospatial.com/p/innovation-flux-todays-three-body)

---

### Akis Karagiannis — "Spectral Reflectance" newsletter, 2026 essays
- **What it is:** An EO newsletter (1,000+ subscribers) with weekly news plus "EO In-Depth" essays.
- **Problems / pain points:**
  - *"The EO community probably does not need your weekend package"* (25 May 2026): there is a flood of LLM-assisted EO packages and dashboards that ignore nodata, CRS, cloud masking and validation. "we are not really becoming more capable; we are mostly getting better at making unfinished work look finished." "Making something exist is no longer the hard part. Making something worth depending on still is." Core open-source infrastructure (GDAL, xarray, rasterio, STAC) is underfunded, citing Ryan Abernathey. *This is a warning label for any hackathon EO tool:* show validation, not just a UI.
  - *"The Economics of Openness: Funding EO as a Public Good"* (16 Mar 2026): "Availability is only one condition of public use. On its own, it secures very little." Case studies:
    - Norway's NICFI programme bought Planet tropical mosaics for 40+ countries. Phase 1 ended Jan 2025, and the follow-on procurement was cancelled in Sep 2025 after a legal challenge. This is a big loss of free high-resolution tropical data.
    - MethaneSAT lost contact in 2025.
    - FireSat has high social value but weak paying demand.
    - SERVIR's embedded capacity survived the 2025 US withdrawal better than donor-dependent programmes.
    Numbers it cites: California's $95M satellite-data purchase via Planet, and a Landsat economic value of $25.6B in 2023.
  - *"CNG London: People Who Fight With Data for a Living"* (2 Jul 2026): "A dataset can sit in object storage and still be painfully slow if its chunks do not match the way people query it." "Pricing, data-transfer costs and implementation details still vary between providers." Agent-driven workflows take different routes between runs, which hurts reproducibility. "Infrastructure at that scale still needs an owner." Talks:
    - Earth Genome: AlphaEarth embeddings performed best for seagrass mapping.
    - TESSERA: open-weights 10 m embeddings via Zarr v3 and STAC.
    - Barrios Visibles: building footprints imply ~7.59M people in informal settlements vs 4.15M in the official register.
    - Leeds: a 53 TB Antarctic ice-velocity Zarr cube.
    - Tilebox: an EO compute platform with agent traces.
- **Hackathon angle:**
  - (a) **"Informal settlement census gap"**: building footprints (Google Open Buildings / Overture / Microsoft) × population estimates vs official registers.
  - (b) A **NICFI-gap explainer**: which tropical forest monitoring loses resolution after the NICFI cancellation, and what Sentinel-2 or embeddings can recover.
  - (c) Any tool should ship with a **validation report** to pre-empt the "weekend package" critique.
- **Credibility:** Practitioner blog (independent). NICFI and MethaneSAT facts are attributed but should be cross-checked with primary sources.
- **Sources:**
  - [Archive](https://www.spectralreflectance.space/archive)
  - [Weekend package, 25 May 2026](https://www.spectralreflectance.space/p/the-eo-community-probably-does-not)
  - [Economics of Openness, 16 Mar 2026](https://www.spectralreflectance.space/p/the-economics-of-openness-funding)
  - [CNG London, 2 Jul 2026](https://www.spectralreflectance.space/p/cng-london-people-who-fight-with)

---

### Scene From Above podcast — Season 15–16 (2026), incl. the "GenAI for Geospatial Challenge" takeover
- **What it is:** A long-running EO podcast hosted by Julia Wagemann and Sabrina Szeto. Season 16 featured winners of the **GenAI for Geospatial Challenge**, which had 14 winning teams and AWS credits; the show notes don't fully state the organiser.
- **Problems / pain points:**
  - *BolgiaTen (S16E3, 7 Jul 2026), on maritime trust:* AIS "is based on an open trust system", so jamming and spoofing corrupt positions. This matters for insurance risk, sanctions compliance, dark port calls and ship-to-ship transfers. They fuse AIS, ownership records and EO imagery, with partner Lloyd's List Intelligence. "clear communication of uncertainty is just as important as the underlying science." Business users must learn EO limits: resolution, revisit, coverage, cost.
  - *RASID GoPilot (S16E2, 1 Jul 2026):* an agentic EO Q&A that started from methane (Methane Mapper) and generated >100,000 synthetic methane plumes for training. "generative AI acts as the reasoning layer". Users get answers "without needing to manually search satellite archives, download imagery or run complex workflows."
  - *BigData Ghana ForestTrace AI (S16E1, 24 Jun 2026):* forest and land-use intelligence for cocoa-sector actors and governments, with plain-language querying.
  - *AWS's Phil Cooper and Nadine Alameh, LunateAI and ex-OGC CEO (S16E4, 15 Jul 2026):* users need to know where information came from and how it was processed (provenance and governance). Energy and finance are adopting first.
  - *Matthias Mohr on STAC (S15E5, 27 Feb 2026):* "How organisations struggle when adopting STAC internally" (topic line only).
  - *Aimee Barciauskas, Development Seed / NASA IMPACT and MAAP (S15E4, 30 Jan 2026):* technical and cultural barriers to cloud-native EO, and "reproducibility is as much about habits as it is about tools".
- **Hackathon angle:**
  - These challenge winners are templates of what judges reward: agentic natural-language EO Q&A with evidence for a named domain user (methane, cocoa deforestation, maritime sanctions).
  - The **AIS-spoofing / dark-vessel cross-check** (AIS vs Sentinel-1 detections) is a classic 36-hour build with open data (Global Fishing Watch).
- **Credibility:** Podcast show notes (secondary summaries of interviews).
- **Sources:**
  - [Podcast home](https://scenefromabove.podbean.com/)
  - [S16E4, 15 Jul 2026](https://scenefromabove.podbean.com/e/s16e4-genai-for-geospatial-challenge-takeover-%e2%80%93-with-phil-cooper-aws-and-nadine-alameh-lunateai/)
  - [S16E3, 7 Jul 2026](https://scenefromabove.podbean.com/e/s16e3-genai-for-geospatial-challenge-takeover-%e2%80%93-in-conversation-with-bolgiaten/)
  - [S16E2, 1 Jul 2026](https://scenefromabove.podbean.com/e/s16e2-genai-for-geospatial-challenge-takeover-%e2%80%93-in-conversation-with-rasid/)
  - [S16E1, 24 Jun 2026](https://scenefromabove.podbean.com/e/s16e1-%e2%80%93-genai-for-geospatial-challenge-takeover-in-conversation-with-big-data-ghana/)
  - [S15E5, 27 Feb 2026](https://scenefromabove.podbean.com/e/s15e5-stac-%e2%80%93-a-common-language-for-finding-geospatial-data/)
  - [S15E4, 30 Jan 2026](https://scenefromabove.podbean.com/e/scene-from-above-%e2%80%94-season-15-episode-4-what-cloud-friendly-really-means-for-earth-observation/)

---

### Other newsletters and podcasts surfaced (not deeply read)
- **What it is:** EO newsletters listed by Robin Cole's satellite-image-deep-learning recommendations page: Remote Sensing News, Geospatial ML, GEOAI, Earthbound, Applied Geospatial, Spatial Thoughts, Geospatial Jobs, Hydrosat, SkyServe, and Spatial Trouble Maker. Also the LiveEO podcast (e.g., #24 with Joe Morrison, Feb 2023).
- **Credibility:** Directory listing only.
- **Sources:**
  - [satellite-image-deep-learning recommendations](https://www.satellite-image-deep-learning.com/recommendations)
  - [LiveEO podcast #24](https://www.live-eo.com/blog/24-joe-morrison-on-his-companys-edge-in-earth-observation)

---

## Part B.2 — Market-research firms

### Novaspace (ex-Euroconsult) — "From Satellite Data to Disaster Resilience" (21 Oct 2026) and "10 Trends… WSBW 2026" (16 Oct 2026)
- **What it is:** Commentary from the consultancy formed by merging Euroconsult and SpaceTec. It publishes the paywalled *Earth Observation Data & Services Market* report (17th edition, as cited by New Space Economy). Novaspace CEO Pacôme Révillon moderated a GEOINT 2026 panel.
- **Problems / pain points:**
  - Disaster EO's value depends on reaching decision-makers "in time to support effective action".
  - "The central challenge is therefore operational integration."
  - Outputs "must be delivered in formats and timeframes that match the needs".
  - Fragmented formats and systems, with field validation still needed.
  - WSBW trend #9: "Earth observation is shifting from selling images and raw data to providing information", and "the competitive challenge will be to balance speed with trust, reliability and relevance."
  - Trend #1: launch certainty, with talk that Falcon 9 may leave the commercial market around 2030.
  - About 60 space M&A deals expected in 2026.
- **How they're trying to solve it:** Standardised data-sharing protocols, joint training, satellite monitoring plus local validation (drones, ground), and a shift from post-event imagery to pre-event risk services.
- **Data:** Sentinel-1 and Sentinel-2 flood mapping (the Pakistan 2022 example, ~33M people affected).
- **Hackathon angle:** A **pre-event flood exposure plus post-event Sentinel-1 flood-extent pipeline** whose output is formatted for responders, e.g. a list of affected facilities and roads in CAP or GeoJSON. The deliverable is "formats and timeframes that match the needs".
- **Credibility:** Consultancy blog (reputable firm). The figures are mostly behind a paywall.
- **Sources:**
  - [Novaspace, 21 Oct 2026](https://nova.space/in-the-loop/from-satellite-data-to-disaster-resilience-turning-information-into-action/)
  - [Novaspace, 16 Oct 2026](https://nova.space/in-the-loop/10-trends-reshaping-the-global-space-economy-insights-from-world-space-business-week-2026/)
  - [EO Data & Services Market report page](https://digital-platform.euroconsult-ec.com/product/earth-observation-data-services-market/)

---

### Quilty Space — EO Financial Reviews and public-company earnings notes (2026)
- **What it is:** A space-sector financial research firm. It publishes paywalled *Earth Observation Financial Review* 2026 Q1 and Q2 and earnings reviews for Satellogic, Planet, HawkEye 360, BlackSky and Spire.
- **Problems / pain points:** Not visible (paywalled). Its existence signals that public EO companies' unit economics are watched quarterly.
- **Credibility:** Paid analyst research. Contents not verified.
- **Sources:**
  - [Quilty Space home](https://www.quiltyspace.com/)
  - [EO Financial Review 2026 Q2](https://www.quiltyspace.com/product-page/earth-observation-financial-review-2026-q2)

---

## Part B.3 — Trade press, op-eds and executive commentary (2025–2026)

### Via Satellite — "Commercial Markets Are Ready for EO — But the Understanding Gap Persists" (EO Summit London, 26 Jun 2026)
- **What it is:** Mark Holmes's report of an EO Summit panel. The speakers were enterprise *buyers*: Mark Nightingale (Shell), Tom van Bezooijen (Waternet utility) and Fani Kallianou de Jong (EBRD), alongside providers Awais Ahmed (Pixxel) and Sven van Haver (Orbital Eye).
- **Problems / pain points:**
  - On pricing opacity: "Data pricing is still very much a dark art." (Nightingale, Shell)
  - On overselling: "I would advise EO players not to oversell the technology." (Nightingale)
  - On resolution: "Better resolution doesn't always mean better answers." (Nightingale)
  - On the spec race: "We ask too much about the latest satellite capability." (van Haver, Orbital Eye)
  - On the last mile: "Interestingly, people in the field barely want to see the data." (van Bezooijen, Waternet). Field staff want to know *where to go*.
  - Other barriers named: cross-border regulation and EULAs, trust between providers and buyers, ease of use.
- **How they're trying to solve it:** Explain value rather than specs. Shell uses EO for pipeline monitoring and hard-to-access countries. Waternet uses EO as a comparative layer next to helicopter patrols.
- **Hackathon angle:** A **"where should the field crew go today" work-order generator**: turn Sentinel-2/Sentinel-1 anomalies along a utility or pipeline corridor into a ranked list of GPS dispatch tickets, with no map literacy needed. This targets the Waternet quote directly.
- **Credibility:** Reputable trade press, with direct quotes from buyers.
- **Sources:** [Via Satellite, 26 Jun 2026](https://www.satellitetoday.com/imagery-and-sensing/2026/06/26/commercial-markets-are-ready-for-eo-but-the-understanding-gap-persists/)

---

### Via Satellite op-ed — "Operational AI is Hitting the Limits of Earth Observation Data" (Eric von Eckartsberg, CRO EarthDaily, 8 May 2026)
- **What it is:** An op-ed from an EO data company executive arguing that EO supply chains were built to deliver *pictures*, not stable *measurements*.
- **Problems / pain points:**
  - "Calibration breaks down: Measurements vary across sensors and over time."
  - "Without stable calibration, values lose meaning and cannot be trusted in automated systems."
  - "Gaps in coverage, uneven revisit, and seasonal interruptions make long-term analysis difficult."
  - "Models trained on unstable time series degrade quickly."
  - "Durability is the real constraint."
  - Pilots hide the problem through manual clean-up that doesn't scale, so harmonisation and QC fall on users.
- **How they're trying to solve it:** CEOS Analysis Ready Data (CEOS-ARD) principles and purpose-built measurement constellations. The second is EarthDaily's own pitch, which is a conflict of interest.
- **Data:** HLS (Harmonized Landsat Sentinel-2) is the public ARD analogue. CEOS-ARD product family specifications.
- **Hackathon angle:** A **cross-sensor consistency checker**: for an AOI, compare Landsat-8/9, Sentinel-2 and HLS reflectance or NDVI time series and flag sensor-induced jumps. This shows "fake change" caused by calibration rather than the ground, and links to the change-detection false-positive problem.
- **Credibility:** Op-ed by a vendor (conflict of interest), but the technical claims are standard.
- **Sources:** [Via Satellite opinion, 8 May 2026](https://www.satellitetoday.com/opinion/2026/05/08/operational-ai-is-hitting-the-limits-of-earth-observation-data/)

---

### Via Satellite — Sovereign EO panel and BlackSky CEO interview (SDSS Paris, 15 and 25 Sep 2026)
- **What it is:** CEOs of ICEYE (Rafal Modrzewski), HawkEye 360 (John Serafini), BlackSky (Brian O'Toole) and Planet's CSO (Robbie Schingler) on the sovereign-systems market.
- **Problems / pain points:**
  - Raw sensor data needs heavy processing before it is useful, so HawkEye 360 embeds analysts with customers: "What we do is not intuitive." International sales are now 40% of HawkEye 360 revenue.
  - Schingler: latency has become the key performance measure.
  - O'Toole: "AI is really good if you know what questions you are trying to answer", and "sovereignty is probably the number one thing on everybody's mind."
  - ICEYE signed a 40-satellite deal with Germany's armed forces, with satellites built in-country.
- **How they're trying to solve it:** Selling whole sovereign systems, embedded analysts, and "Assured" subscriptions.
- **Hackathon angle:** Low for a 36-hour build, but it confirms that "knowing which question to ask" is the bottleneck. A question-formulation assistant that turns a vague user need into a concrete EO query (sensor, AOI, cadence, metric) is a plausible demo.
- **Credibility:** Trade press quoting executives (self-interested).
- **Sources:**
  - [Sovereign EO panel, 15 Sep 2026](https://www.satellitetoday.com/government-military/2026/09/15/sovereign-eo-space-capabilities-are-ready-to-go-to-the-next-level/)
  - [O'Toole interview, 25 Sep 2026](https://www.satellitetoday.com/imagery-and-sensing/2026/09/25/blacksky-ceo-sovereign-is-the-no-1-market-opportunity-right-now/)

---

### Via Satellite — NGA Director Bredenkamp at GEOINT 2026 (6 May 2026)
- **What it is:** Coverage of NGA Director Lt. Gen. Michele Bredenkamp's keynote. Her three lines of effort are mission, transformation and workforce, "all enabled by AI".
- **Problems / pain points:**
  - The aim is to shorten collection-to-decision time.
  - NGA relies on commercial providers for persistent monitoring. In late 2025 it used a commercial analytics contract to confirm China's report of debris damage to its space station "within hours".
  - Commercial imagery is unclassified and shareable with allies.
  - A new Rapid Capabilities Office will accept more risk, and an AI Framework is forthcoming, described as "our blueprint for becoming an AI first organization".
- **Hackathon angle:** "Unclassified, shareable" commercial and open imagery as the coalition currency points to an open-data shareable briefing generator.
- **Credibility:** Reputable trade press.
- **Sources:** [Via Satellite, 6 May 2026](https://www.satellitetoday.com/imagery-and-sensing/2026/05/06/enabled-by-ai-nga-director-focused-on-mission-transformation-and-workforce/)

---

### Via Satellite — Planet's agentic geospatial AI query (21 May 2026)
- **What it is:** Planet's private-beta agent. It answers natural-language questions such as "Where are new construction sites appearing in Florida?", searches the archive, maps matches, tracks sites over time and writes a shareable report. It targets non-geospatial users: insurance adjusters, infrastructure managers and civil officials. The LLM partner is not named in the article; Planet announced an Anthropic partnership in Mar 2025, which the main report covers. Planet's line: "Agentic AI compresses decision loops into minutes."
- **Problems / pain points:** The last mile to non-experts.
- **Hackathon angle:** Build the *open-data* equivalent: a natural-language question to a Sentinel-2/Landsat STAC search, an analysis step and a report with cited scenes. Cite provenance per Element 84's radar.
- **Credibility:** Trade press reporting a company blog.
- **Sources:**
  - [Via Satellite, 21 May 2026](https://www.satellitetoday.com/imagery-and-sensing/2026/05/21/planet-is-building-an-agentic-geospatial-ai-query/)
  - [Imagery & Sensing index](https://www.satellitetoday.com/imagery-and-sensing/)

---

### "Shutter control" and conditional access to imagery (2026): Planet's Iran withholding, EU Sentinel delay over the Sea of Oman, Paris Space Summit declarations
- **What it is:** A 2026 theme in TerraWatch's coverage: commercial *and even public* imagery can be paused for geopolitical reasons.
- **Problems / pain points:**
  - Planet withheld Iran imagery for months at US government request, then released ~250,000 images. During the gap the BBC and NYT used European and Chinese providers (TerraWatch, 11 Aug 2026). The 13 Apr 2026 issue recommended a BBC piece on humanitarian and journalist concern about Planet's restricted access.
  - "In July, the EU delayed releasing some Sentinel imagery over the Sea of Oman at US request". Nothing defines when restrictions apply or for how long (TerraWatch, 14 Sep 2026).
  - Paris International Space Summit (9–10 Sep 2026): a scientific-data declaration (49 countries + ESA) and a Copernicus "global public good whose continuity is essential" declaration (27 countries + 5 organisations). These create "no additional financial obligations", and the US, China, India, Russia and Japan signed neither.
  - Switzerland is opting out of Copernicus funding for 2028–2034 (TerraWatch, 8 Jun 2026).
- **How they're trying to solve it:** Multi-region sourcing, national constellations ("over 60 countries"), and contracted availability.
- **Data:** Sentinel-1/2 (normally open), Planet, Airbus, Chinese providers.
- **Hackathon angle:** An **imagery-availability monitor**: for a watch-list of AOIs, track the latency between the satellite pass and public availability of Sentinel scenes in the Copernicus Data Space Ecosystem / STAC catalogues, and flag anomalous delays. This is evidence for transparency debates and uses only public catalogue metadata.
- **Credibility:** Analyst newsletter. The underlying BBC report was not opened.
- **Sources:**
  - [TerraWatch 11 Aug 2026](https://newsletter.terrawatchspace.com/earth-observation-essentials-august-11-2026/)
  - [TerraWatch 14 Sep 2026](https://newsletter.terrawatchspace.com/can-a-global-earth-observation-accord-work-even-if-it-is-not-global/)
  - [TerraWatch 13 Apr 2026](https://newsletter.terrawatchspace.com/earth-observation-essentials-april-13-2026/)
  - [TerraWatch 8 Jun 2026](https://newsletter.terrawatchspace.com/earth-observation-essentials-june-8-2026/)

---

### Planet — "Aircraft detection at planetary scale" (19 Mar 2025) plus HN discussion (24 Mar 2025; 96 points, 86 comments)
- **What it is:** A worked example of cheap labelling plus tip-and-cue. High-res SkySat captures within 3 minutes of a PlanetScope scene give labels that transfer to PlanetScope (~3 m). There are >800 crossover pairs and ~15,000 labels. F1 = 0.82 on a global test set. Only aircraft ≥25 m are detected. One consistent "miss" turned out to be aircraft *paint on the tarmac*, confirmed by SkySat.
- **Problems / pain points:** Labelling cost and size limits. HN critics asked "how is this better/cheaper than existing ADSB based technologies" (4ndrewl). Others replied "ADS-B is opt-in" (xiii1408) and "ADSB isn't authenticated. Anyone can emit, anyone can spoof" (eastbound). One view was "The application is military" (barbazoo). On privacy: "turning the Earth into a panopticon" (simulator5g).
- **How they're trying to solve it:** Cross-sensor near-simultaneous label transfer, and a high-res follow-up for verification.
- **Data:** PlanetScope and SkySat (commercial). Public analogues are Sentinel-2 plus NAIP or Maxar Open Data, and OpenSky ADS-B.
- **Hackathon angle:** A **non-cooperative aircraft/vessel detector**: compare satellite detections with ADS-B (OpenSky) or AIS (GFW) to flag aircraft or ships that are present but not broadcasting. This is the same pattern as dark-vessel detection.
- **Credibility:** Company blog (method stated) plus forum comments.
- **Sources:**
  - [Planet Pulse, 19 Mar 2025](https://www.planet.com/pulse/aircraft-detection-at-planetary-scale/)
  - [HN 43465189](https://news.ycombinator.com/item?id=43465189)

---

### Trade-press quick hits (Via Satellite, TechCrunch), 2025–2026, relevant to industry problems
- **NGA Luno B change detection:** Luno B is a $200M-ceiling, 5-year IDIQ awarded to 13 companies in Jan 2025 for unclassified economic, environmental and geopolitical analytics. Vantor won a $5.3M order (Feb 2026) for automated global terrain-change analytics that update NGA's Land Use Land Cover classification, fusing its own and other EO and SAR operators' data. NV5, Planet and Ursa also hold Luno B orders. BlackSky won a 7-figure Luno A facility-monitoring renewal (Mar 2026). Change detection at global scale is a funded government requirement. (Via Satellite, [5 Feb 2026](https://www.satellitetoday.com/government-military/2026/02/05/nga-awards-vantor-5-million-for-global-change-detection-under-luno-b-contract/); [5 Mar 2026](https://www.satellitetoday.com/government-military/2026/03/05/nga-awards-blacksky-seven-figure-order-on-luno-a-contract/))
- **NRO commercial remote sensing awards, first tranche:** HEO, SatVu and Sierra Nevada (Feb 2026). ([Via Satellite, 10 Feb 2026](https://www.satellitetoday.com/government-military/2026/02/10/nro-taps-heo-satvu-and-sierra-nevada-for-remote-sensing-awards/))
- **Spire Q3 2025:** revenue fell to $12.7M from $28.6M (−56%) after the maritime divestment to Kpler and the US government shutdown. Over $10M of revenue slipped into 2026 and $6–8M was lost. This shows how fragile government-dependent EO revenue is. ([Via Satellite, 18 Dec 2025](https://www.satellitetoday.com/finance/2025/12/18/government-shutdown-and-maritime-divestment-impact-spire-in-q3-results/))
- **SkyFi Series A ($12.7M, Jan 2026):** a "Getty Images" for satellite imagery with 50+ providers. Imagery is "closely becoming a commodity", so the goal is "providing answers for customers". Getting providers to share data used to be hard and is now "table stakes" (CEO Luke Fischer). This is a counterpoint to Morrison's 2020 marketplace pessimism. ([TechCrunch, 14 Jan 2026](https://techcrunch.com/2026/01/14/skyfi-raises-12-7m-to-turn-satellite-images-into-insights/))
- **Earthmover ($7.2M seed, Sep 2025):** the founders found "Earth observation data alone wasn't enough for a business" and pivoted toward fast-changing weather and fire data on Icechunk/Xarray. Customers include Kettle (wildfire insurance) and RWE. ([TechCrunch, 22 Sep 2025](https://techcrunch.com/2025/09/22/earthmover-wants-to-become-the-snowflake-of-weather-and-geospatial-data/))
- **Other items (titles only, not opened):**
  - BlackSky: backlog +32% but a larger net loss (26 Feb 2026)
  - Planet × AXA AI risk platform (13 Feb 2026)
  - KSAT "Vake" maritime detection (27 Jan 2026)
  - LiveEO Twinspector infrastructure constellation (28 Jan 2026)
  - Satellogic Merlin (18 Mar 2026)
  - Planet onboard object detection on Pelican-4 (7 Apr 2026)
  ([Via Satellite Imagery & Sensing p.2](https://www.satellitetoday.com/imagery-and-sensing/page/2/))
- **Credibility:** Reputable trade press.

---

## Part B.4 — Conferences and community events

What talks, panels and agendas say the problems are.

### GEOINT Symposium 2025 (St. Louis, 18–22 May 2025) and 2026 (Aurora CO, 3–6 May 2026), plus USGIF 2026 community events
- **What it is:** USGIF's annual symposium for the US and allied geospatial-intelligence community, with 4,000+ attendees. GEOINT 2027 is 16–19 May 2027 in Kissimmee FL (lightning-talk call open to 26 Nov 2026).
- **Problems / pain points:**
  - **Data volume vs analysts (2025):** "Today's threats are more complex, the volume of data is staggering, and innovation is moving at a dizzying pace" (Johnny Sawyer, Day 2). On pilot sprawl: "Everything's moving so fast" (Don Polaski, Booz Allen). On trust: "if we cannot trust the work, the data, the architecture of those around us" (Jeff Builta, NGA). On data provenance work: "the boring work behind the scenes to ensure that the data is trusted" (Nadine Alameh, Taylor Geospatial Institute). Taegyun Jeon (SI Analytics) argued geospatial foundation models must be mission-specific.
  - **Commercial dependence on government budgets (2025):** "We need to be able to handle the surges and the valleys that we see in that budgeting process" (Frank Backes, Capella, on the CEO panel with Synspective, BlackSky and Maxar). DNI Gabbard: commercial sector advances are "indispensable".
  - **Speed and interoperability (2026):** "interoperability cannot remain a future objective". Leaders positioned AI "as an enabler of human decision-making", with emphasis on trust, validation and human judgment. Speakers included NGA Director Lt. Gen. Michele Bredenkamp and NRO Director Christopher Scolese. NGA's Chief AI Officer Michelle Aten moderated "The Intelligence Inflection Point" with Vantor CEO Dan Smoot, Niantic Spatial CTO Brian McClendon and Enabled Intelligence CEO Peter Kant.
  - **Detections outpace validation (USGIF "AI First Approaches", 22 Jul 2026):** "organizations are generating far more detections than analysts can validate" (Gina Hurtado, NGA). This is the change-detection false-positive problem in its own words. "The real constraint is organizing, conditioning, and making that data AI-ready" (Chris Parrett, NGA Rapid Capabilities Office), and "quality, accessibility, and context matter more than raw volume." Panelists want commercial datasets to arrive AI-ready. They want AI outputs held to analyst standards: confidence, reasoning, source pedigree and validation history. One analyst may supervise "dozens, hundreds, or even a thousand-plus concurrent processes". "a 30-second answer costs more than one that can wait two hours" (Sean Batir, AWS). Keyword search assumes analysts already know what to look for (Brian Bataille, DIA).
  - **"It's About Automation, Not AI" (NGA Deputy Director of Analysis Steve Hall, 28 Jul 2026):** much marketed AI is "a script running in the background". Making sense of data is now harder than collecting it. Output is still long-form PDFs, and Hall wants machine-readable intelligence fed into command-and-control. "NGA is a combat support agency where speed is measured in seconds and minutes." Siloed databases block dissemination. NGA's acquisition now aims to onboard new capabilities "within weeks".
  - **Maritime domain awareness (USGIF event, 23 Jun 2026, USCG Assistant Commandant for Intelligence Steven Griffin, SynMax demo):** "The challenge is not a lack of data." The need is to fuse commercial imagery, AIS, RF, radar and OSINT and to close the "detect-to-act" gap. Classification and legacy systems block sharing. USGIF launched a Maritime Domain Awareness Working Group (Aug 2026).
  - **Over-automation deskills operators (GEOINTeraction Colorado, Mar 2026):** expanded AI use erodes soldiers' manual geo-skills, for example during a power cut. National-level data structures don't fit squad-level, fast decisions.
- **How they're trying to solve it:** AI-first workflow redesign, layered models with human review of high-confidence detections only, data-readiness programmes, the NGA–Space Force MOA on tactical ISR (2025), allied data standards, and the MDA working group.
- **Data:** Mostly classified or commercial. Public analogues include Sentinel-1 ship detection, Global Fishing Watch AIS and SAR vessel detections, and xView/xView3 datasets.
- **Off-the-shelf tech:** Layered detection-plus-triage models, machine-readable intel formats, STAC/OGC APIs.
- **Hackathon angle:**
  - (a) A **detection triage queue**: run an open detector (e.g., ships on Sentinel-1, or building change) and rank detections by confidence, multi-sensor corroboration (AIS match / no match) and novelty, so a human validates the top 20 instead of 2,000. This directly answers the NGA quote.
  - (b) An **"AI output with pedigree" card**: every answer carries confidence, source scenes, timestamps and validation history.
  - (c) A **PDF-to-machine-readable intel** converter for imagery reports.
- **Credibility:** Official and industry-association recaps (promotional, few metrics). Quotes are as reported by USGIF.
- **Sources:**
  - [GEOINT 2025 Day One, 20 May 2025](https://usgif.org/geoint-symposium-2025-day-one-recap/)
  - [Day Two, 21 May 2025](https://usgif.org/geoint-symposium-2025-day-two-recap/)
  - [Day Three, 22 May 2025](https://usgif.org/geoint-symposium-2025-day-three-recap/)
  - [GEOINT 2026 Day One, 5 May 2026](https://usgif.org/geoint-2026-day-one/)
  - [Day Two, 6 May 2026](https://usgif.org/geoint-symposium-2026-day-2/)
  - [Wrap-up, 22 May 2026](https://usgif.org/geoint-symposium-2026-wrap-up/)
  - [AI First Approaches, 10 Aug 2026](https://usgif.org/mission-focus-ai-first-approaches/)
  - [Automation, Not AI, 10 Sep 2026](https://usgif.org/geointeraction-tuesday-its-about-automation-not-ai/)
  - [Maritime Awareness, 1 Jul 2026](https://usgif.org/turning-maritime-awareness-into-decision-advantage/)
  - [GEOINTeraction Colorado, 24 Mar 2026](https://usgif.org/geointeraction-colorado-data-standards-ai-integration-and-the-skills-that-keep-geoint-mission-ready/)
  - [GEOINT 2026 page](https://usgif.org/geoint-symposium-2026/)
  - [Event recaps index](https://usgif.org/category/event-recaps/)

---

### SatSummit (Development Seed) — St. Louis, 18–19 Nov 2026 (agenda published Sep 2026); Lisbon, 16–17 Mar 2027
- **What it is:** A conference on "satellite data for global development", running since 2015 and organised by Development Seed. It mixes providers, NGOs, journalists and humanitarian users.
- **Problems / pain points (from session titles and descriptions, Nov 18 agenda):**
  - **Imagery Providers Meet Imagery Users:** the gap between what imagery can technically do and what field teams can actually use.
  - **When It's Go Time:** "why imagery often arrives too late to help during crises" (speakers include Michael Budde, Ziad Al Achkar, Katie Picchione).
  - **What's Real Anymore:** fabricated and manipulated satellite imagery and what transparency requires (Logan Williams, Shoaib Burq, Christy Monaco). This is the deepfake satellite image problem.
  - **Can I Get a Witness?:** what it takes for imagery to hold up as credible evidence (moderated by Jamon Van Den Hoek).
  - **Worth a Thousand Words?:** how journalists decide to use satellite imagery and the cost of getting it wrong (Christoph Koettl, Sarah Cahlan, Krishna Karra and others).
  - **Beyond the Demo: AI in the Real World:** what happened when AI actually influenced decisions (Mikel Maron, Esther Rolf, Cameron Kruse).
  - **Explainable AI workshop:** evaluating and communicating uncertainty in AI decision-support (Emily Sylak-Glassman, Isaac Corley).
  - **Surviving and Thriving:** funding cliffs and mission pivots (David Saah).
  - **The Legal Frontier:** space and data law, with Kevin Pomfret.
  - **Speed Dating for Satellite Data:** build a baseline data studio with NASA Lifelines, no GIS expertise needed. This targets the last mile to non-experts.
  - The "State of Play" opener has Kumar Navulur (Synspective, satellites), Hannah Kerner (ASU, GeoAI), Maggie Cawley (OSM US, data), Catherine Nakalembe (UMD, capacity) and Karl Wurster (SkyTruth, applications). The framing is "what it takes to translate increasingly powerful capabilities into decisions and impact".
- **How they're trying to solve it:** Provider–user dialogue, cloud-native SAR workflows for humanitarian teams (workshop), and explainable-AI practice.
- **Data:** Sentinel-1 SAR, NASA Lifelines baseline layers, OSM.
- **Hackathon angle:**
  - (a) A **satellite-image authenticity checker**: given a claimed satellite image plus date and location, pull the Sentinel-2/Landsat scene for that date and compare cloud pattern, shadows and features to flag likely fakes or mismatched dates. This maps to "What's Real Anymore" and "Can I Get a Witness?".
  - (b) A **"go-time" crisis imagery latency tracker**: time from event to first usable free and commercial scene.
  - (c) A **journalist verification kit**.
- **Credibility:** Conference agenda (primary). The panel content has not happened yet; the event is in November 2026.
- **Sources:**
  - [SatSummit home](https://satsummit.io/)
  - [St. Louis agenda](https://satsummit.io/2026-st-louis/agenda/)
  - [Agenda post, Sep 2026](https://satsummit.io/updates/2026-09-24-agenda-post/)
  - [State of Play post, Sep 2026](https://satsummit.io/updates/2026-09-15-state-of-play-stl/)

---

### Cloud-Native Geospatial Forum (CNG, Radiant Earth) — Geo-Embeddings Sprints (Clark Univ., Mar 2026; Zürich, 27–28 Oct 2026) and CNG Zürich (29 Oct 2026)
- **What it is:** A Radiant Earth initiative for the community around cloud-native formats (STAC, COG, GeoParquet, Zarr/GeoZarr, Icechunk). In 2026 it convened embedding-standardisation sprints with IBM, Clark University and Planet.
- **Problems / pain points:**
  - "significant work remains before practitioners can confidently compare embedding products."
  - "users often struggle to determine whether a given embedding product is appropriate for their application."
  - "many potential users remain unfamiliar with what embeddings are, how they differ from traditional geospatial products."
  - Documentation of embedding capabilities and limits is inconsistent.
- **How they're trying to solve it:** First-sprint outcomes (Mar 2026):
  - community recommendations for storing, cataloguing and accessing embeddings
  - geoembeddings.org plus a monthly forum
  - TESSERA adopted GeoZarr conventions for pixel embeddings
  - LGND released a global Sentinel-2 embedding dataset in GeoParquet
  - Earth Genome released 2025 embeddings using a Geo-Embeddings STAC extension
  - an EO Vector Embeddings Survey launched
  The Zürich sprint targets benchmarking (TorchGeo-Bench is mentioned), fitness-for-use and adoption. Separately, CNG's "Portolan" (Sep 2026) is a serverless spatial data infrastructure of files-in-a-bucket plus STAC.
- **Data:** LGND global Sentinel-2 embeddings (GeoParquet), Earth Genome 2025 embeddings, TESSERA embeddings, Google AlphaEarth annual embeddings.
- **Off-the-shelf tech:** STAC Geo-Embeddings extension, GeoZarr, GeoParquet, TorchGeo, Icechunk.
- **Hackathon angle:** An **embedding "fitness-for-use" report card**: for a user's task (say, detecting solar farms), automatically test 2–3 open embedding products against a few labels and report which works, with uncertainty. This is exactly the gap the sprint names.
- **Credibility:** Primary (community organisation blog).
- **Sources:**
  - [CNG home](https://cloudnativegeo.org/)
  - [Announcing the Next Geo-Embeddings Sprint, 29 Jul 2026](https://cloudnativegeo.org/blog/2026/07/announcing-geo-embedding-sprint-zurich/)
  - [Introducing Portolan, 2 Sep 2026](https://cloudnativegeo.org/blog/2026/09/introducing-portolan/)

---

### EO Summit (TerraWatch) — London 13–14 Jun 2024; New York 10–11 Jun 2025; 22 Jun 2026
- **What it is:** A user-centric EO conference with enterprise tracks. In 2025 the tracks were Insurance & Finance, Agriculture & Forestry, Energy & Infrastructure, and Weather & Climate. In 2026 it had an Enterprise Track (Insurance & Risk, Energy & Infrastructure, Agriculture & Environment) and an Innovation Track (Defence & Security, Disaster Management).
- **Problems / pain points:** The premise is that the supply side dominates other conferences. In 2024 an attendee write-up noted "challenges in soil organic carbon due to soil sampling difficulties and certification validity." TerraWatch (Jun 2026) recommended an EO Summit piece on the "commercial understanding gap". Satellite Today covered the 2026 Defense & Security track (cited in TerraWatch 11 Aug 2026; not opened).
- **Hackathon angle:** Pick one enterprise-track buyer (insurer, utility, ag lender) and build its decision output rather than a map.
- **Credibility:** Organiser and attendee pages.
- **Sources:**
  - [Why an EO Summit, 16 Feb 2024](https://terrawatch.substack.com/p/why-an-eo-summit)
  - [spaceagenda 2025 listing](https://www.spaceagenda.com/?p=56508)
  - [EOSDA 2024 takeaways](https://eos.com/events/eosda-attends-eo-summit-2024-in-london/)
  - [Catapult 2026 listing](https://sa.catapult.org.uk/events/eo-summit/)

---

### Geo Week 2026 (Denver, 16–18 Feb 2026) and 2027 (Salt Lake City, 23–25 Feb 2027)
- **What it is:** The main US event for reality capture, lidar and mapping (ASPRS and partners). 2026 had 3,509 attendees and 238 exhibitors.
- **Problems / pain points (2027 sessions):**
  - *"How AI Is Rewriting Geospatial Demand"* (Jessica Touchard, GeoSearch): "AI is automating the geospatial work teams used to hire for". Feature extraction, digitising, asset detection and first-pass processing are being automated, and "Job descriptions written even two years ago are now aimed at the wrong target."
  - *"From Point Cloud to Proof: A General Counsel's Guide to Defensible Geospatial Data in the Age of AI"*: "A visually compelling product is not necessarily reliable, complete, or supportable." Defensibility "depends on whether the project team can explain what was measured, how it was measured".
  - *"Solving the Surveyor Shortage"*: "a large portion of licensed surveyors approach retirement age", which "poses an immediate bottleneck for high-stakes infrastructure, utility, and renewable energy projects".
- **Hackathon angle:** "Defensible AI geospatial output", i.e. an auditable chain from source scene to claim, for legal and insurance use.
- **Credibility:** Official conference pages.
- **Sources:**
  - [Geo Week home](https://www.geo-week.com/)
  - [2026 post-show report](https://www.geo-week.com/2026-post-show-report/)
  - [AI rewriting demand session](https://www.geo-week.com/session/how-ai-is-rewriting-geospatial-demand/)
  - [Point Cloud to Proof session](https://www.geo-week.com/session/from-point-cloud-to-proof-a-general-counsels-guide-to-defensible-geospatial-data-in-the-age-of-ai/)
  - [Surveyor shortage session](https://www.geo-week.com/session/solving-the-surveyor-shortage/)

---

### SmallSat Conference 2026 (Salt Lake City, 23–26 Aug 2026; "Clouds Above the Clouds: 40 Years of Collaboration")
- **What it is:** The main smallsat technical conference (5,550 attendees, 450 exhibitors in 2026). Proceedings are on USU DigitalCommons.
- **Problems / pain points (from 2026 paper titles):**
  - Onboard AI and edge processing:
    - "Onboard AI at the Orbital Edge: A Mission Debrief From STP-H7-CASPR"
    - "Evaluating Performance of Hardware-Accelerated Vessel Detection Algorithms"
    - "Advanced AI Deployment on SmallSats… FPGA-Gated Inference"
    - "DynaBand: Context-Aware Dynamic Band Selection for Onboard Hyperspectral Processing"
  - Calibration of cheap sensors:
    - "Metadata-Conditioned Dark-Frame Modelling… Low-Cost Hyperspectral Small-Satellite Calibration"
    - "Back From the Dead: Using Stellar PSF Calibration to Recover Operational Value From a Defocused SkySat Telescope"
  - Downlink and scheduling:
    - "ReCAP: A Study of Downlink Optimization Methods"
    - "Multi-Satellite Optical Link Scheduling…"
    - "Forecast-Aware Formation Initialization for High-Revisit VLEO Imaging"
  - Commercial data buys: "NOAA NESDIS Commercial Data Program Using Small Satellites…"
  - Maritime: "Gray Jay Pathfinder: One Year of Maritime and Airborne Vessel Monitoring…"
- **Hackathon angle:** A cloud-forecast-aware tasking planner, i.e. which pass gives a clear image, using open weather forecasts plus TLEs. This ties to the HN "no predictability" complaint.
- **Credibility:** Conference proceedings (titles only; papers not read).
- **Sources:**
  - [SmallSat home](https://smallsat.org/)
  - [2026 proceedings, all papers](https://digitalcommons.usu.edu/smallsat/2026/all2026)

---

### FOSS4G 2025 (Auckland, 17–23 Nov 2025) / FOSS4G 2026 (Hiroshima, 30 Aug–5 Sep 2026); IAC 2025 / IAC 2026 (Antalya, 5–9 Oct 2026)
- **What it is:** The open-source geospatial conference (2025 keynotes included Amy Rose, CTO of Overture Maps) and the International Astronautical Congress (IAC 2026 had 7,604 delegates from 113 countries).
- **Problems / pain points:** Not extracted. The talk listings and press release could not be parsed (the IAC 2026 press release is a PDF).
- **Credibility:** Official pages.
- **Sources:**
  - [FOSS4G 2025](https://2025.foss4g.org/)
  - [FOSS4G 2025 videos playlist](https://youtube.com/playlist?list=PLlZzWSPAR5GYPAGSgs1Z6ydhoVgL7CAHd)
  - [IAF home](https://www.iafastro.org/)
  - [IAC 2025 highlights video](https://www.iafastro.org/media/videos/iac-2025-highlights.html)

---

## Part B.5 — Forums and social discussion

### Hacker News — "The satellite imagery industry still has no idea what customers want" (18 Apr 2022; 384 points, 212 comments) and "'Internet in space' will transform the satellite imagery industry" (1 Jan 2023; 218 points, 141 comments)
- **What it is:** The largest HN threads on Joe Morrison's essays, mostly from practitioners and developers.
- **Problems / pain points (comment quotes):**
  - Niche demand: "almost everyone who wants it has a niche use case" (GlenTheMachine).
  - Simple buying and pricing: "Customers want pixels, but they need basic services: simple and a predictable price." (sandworm101) and "The first company that can provide a basic web interface for purchasing imagery quickly" (sandworm101).
  - Good-enough alternatives: "Google Earth imagery is good enough for most manual processes" (nl).
  - Unpredictable capture timing (cloud, revisit): "there is no predictability" (achow).
  - Data access: "all I really want, is a Netflix of datasets" (lokimedes).
  - Pricing: "The underlying reason for all of this is price discrimination" (Closi) and "archive satellite imagery pricing schemes are absurd." (m2fkxy).
  - Tooling: "The state of software tooling for these sensing data applications is primitive" (jandrewrogers).
  - Speed over sharpness: "People don't pay for resolution, they pay for immediacy." (JumpCrisscross).
  - Downlink: "Remote sensing is severely limited by latency and throughput of the downlink" (orbital-decay).
  - Model transfer: "Aerial imagery models don't always transfer well to satellite images." (joshvm).
  - Who really pays: "The business model is sympathy money from big governments." (JumpCrisscross).
  - Privacy objections (pool-monitoring by real-estate agents) also came up.
- **Hackathon angle:**
  - (a) An **imagery "predictability" estimator**: for an AOI and date window, estimate the probability of getting a cloud-free Sentinel-2 or commercial capture, using historical cloud statistics plus orbit/revisit. This addresses the "there is no predictability" complaint.
  - (b) A "Netflix of datasets" style search across free STAC catalogues.
- **Credibility:** Social / forum posts (practitioner anecdotes, unverified).
- **Sources:**
  - [HN 31074177](https://news.ycombinator.com/item?id=31074177)
  - [HN 34207926](https://news.ycombinator.com/item?id=34207926)
  - [HN listing of Morrison posts](https://news.ycombinator.com/from?site=joemorrison.substack.com)
  - [HN: TerraWatch Maxar analysis (item 48258209)](https://news.ycombinator.com/item?id=48258209)

---

## Part B.6 — Recurring problem themes (with evidence)

Industry-wide themes, each documented with quotes and sources. Numbering follows the original theme list; Theme 18 was added because it emerged during research.

### Theme 1 — "Too much data, not enough analysts"

- **What it is:** Collection capacity (number of satellites, revisit, sensor modes) has grown far faster than the human workforce able to look at the pixels. The US intelligence community has framed this as a headcount impossibility for almost a decade.
- **Problems / pain points:**
  - NGA's own 2017 framing: if they "attempted to manually exploit the imagery they would receive over the next 20 years, they would need eight million imagery analysts" — "clearly not a viable solution" (NGA "Small Satellites – Big Data", as quoted in search results; 2017).
  - Former NGA Director Robert Cardillo: in about five years the agency would be dealing with "a million times more" data and in 20 years would need 8 million analysts (MeriTalk). A 2018 Federal News Network piece gives a different NGA calculation of **6 million** imagery analysts; the same piece notes Planet's ~150 satellites taking ~1.5 million pictures a day (2018).
  - NGA's Justin Poole: over one year NGA ingested more than **12 million images** and generated more than **50 million indexed observations** (SpaceNews, "Geospatial intelligence agency urges faster AI deployment"; date not shown in result).
  - Data readiness, not only volume: NGA's Mark Munsell calls the archive "an AI gold mine", but the hard part is getting data "cleaned, curated, and correlated enough for the AI to ingest it" (Breaking Defense, Aug 2024).
  - Commercial SAR: a SAR constellation "generates far more imagery than analysts can review manually within the allocated time" (Space.com, as summarised in search results; date not verified).
  - Unverified/blog-tier: one blog estimates satellites beam back ~2 billion one-megapixel photos per day (not a primary source — treat as rumor-tier); an industry article says ~70% of optical images are unusable due to cloud (integrio blog; unverified).
- **How they're trying to solve it:** NGA's "triple A" strategy (AI, augmentation, automation) aimed at turning **75%** of analysis over to machines (MeriTalk); Project Maven computer vision; NGA Director Frank Whitworth said analysts sorted through **40% more** sensor imagery in a year thanks to computer vision (Defense Daily, ~2023); NGA's planned ~$700M data-labelling program (DefenseScoop, 3 Sep 2024); NGA Palantir platform licence (est. $28.3M incl. options, 2025, per NGA contract announcements page in results). At GEOINT 2025, NGA Deputy Director Brett Markham said full-scale AI adoption "is still a work in progress" (per search summary of SpaceNews coverage).
- **Data:** Sentinel-1/2 (free, ~daily-to-5-day global), Landsat 8/9, Planet NICFI tropical basemaps (free for non-commercial), Maxar/Vantor Open Data Program (disaster events, CC BY-NC), Umbra Open Data (SAR, CC BY 4.0), Capella open data.
- **Off-the-shelf tech:** Detection models (YOLO-family, SAM/SAM2, Prithvi, Clay, SatlasPretrain), vision-language models for triage, STAC APIs (Element 84 Earth Search, Microsoft Planetary Computer).
- **Hackathon angle:** "Analyst inbox triage": ingest a day of Sentinel-2/Sentinel-1 scenes over a watch-list of sites (ports, airbases, mines), auto-rank which scenes contain *something worth a human look* (change score × confidence × site priority), and show an analyst a ranked queue with a one-line VLM explanation. Measure "minutes of analyst time saved".
- **Credibility:** Official (NGA statements) + reputable press (Federal News Network, Breaking Defense, DefenseScoop, SpaceNews, Defense Daily). Analyst-count numbers are speech-era projections (2017–2018), not current figures; no 2025–2026 official analyst-gap number was found.
- **Sources:**
  - [NGA looks to stay ahead of sheer volume of satellite imagery data — Federal News Network (Sep 2018)](https://federalnewsnetwork.com/big-data/2018/09/nga-looks-to-stay-ahead-of-sheer-volume-of-satellite-imagery-data/)
  - [Small Satellites – Big Data — NGA (2017)](https://www.nga.mil/news/Small_Satellites_-_Big_Data.html)
  - [NGA Using AI to Zoom in on Geospatial Intelligence — MeriTalk (date not shown)](https://www.meritalk.com/articles/nga-using-ai-to-zoom-in-on-geospatial-intelligence/)
  - ['AI gold mine': NGA aims to exploit archive of satellite images — Breaking Defense (Aug 2024)](https://breakingdefense.com/2024/08/ai-gold-mine-nga-aims-to-exploit-archive-of-satellite-images-expert-analysis/)
  - [NGA to offer $700M for data-labeling — DefenseScoop (3 Sep 2024)](https://defensescoop.com/2024/09/03/nga-700m-data-labeling-advance-computer-vision-models/)
  - [Geospatial intelligence agency urges faster AI deployment — SpaceNews](https://spacenews.com/geospatial-intelligence-agency-urges-faster-ai-deployment/)
  - [Maven Speeding Ability To Comb Through Imagery, NGA's Whitworth Says — Defense Daily](https://www.defensedaily.com/maven-speeding-ability-to-comb-through-imagery-ngas-whitworth-says/intelligence-community/)
  - [NGA Contract Announcements (Palantir licence)](https://www.nga.mil/news/Contract_Announcements.html)
  - [The future of Earth observation: private satellites and AI — Space.com](https://www.space.com/astronomy/earth/the-future-of-earth-observation-private-satellites-and-ai-bring-benefits-but-also-pose-risks)
  - [In sea of satellite images, experts' eyes still needed — The Conversation (2016)](https://theconversation.com/in-sea-of-satellite-images-experts-eyes-still-needed-53192)

---

### Theme 2 — The imagery-to-insight gap ("pixels vs answers")

- **What it is:** Buyers outside defence do not want images, or even derived layers; they want a decision, a risk score or a work order inside the software they already use. Most EO firms sell something upstream of that, and the conversion step is bespoke, expensive and often turns analytics companies into consultancies.
- **Problems / pain points:**
  - Joe Morrison (Umbra; "A Closer Look"): "No one wants satellite imagery, sure, but also *almost* no one wants information derived from satellite imagery" (12 Nov 2020); "selling derived data as a subscription product does. not. work." and "What people want is for you to solve their problems for them" (18 Apr 2022). He argues no generic algorithm fits, because each customer defines "change" differently, so working feeds are custom-tuned.
  - TerraWatch Space, *State of Commercial EO 2025* (22 Oct 2025): "Platforms are multiplying, yet it is unclear whether they can differentiate beyond selling access to pixels"; on AI, "whether they solve adoption bottlenecks or simply add another layer of hype is still in question."
  - TerraWatch, 13 Apr 2026: "no genuinely new commercial EO use cases are forming"; the real challenge is "converting what it can already do into something buyers operationally and repeatedly pay for."
  - New Space Economy (23 Oct 2026) lists the "pixels vs. answers gap" as one of four commercial demand barriers (alongside free Landsat/Sentinel data, drones at 2–5 cm, and a capex mismatch with episodic buyers), and argues for "EO data embedded invisibly in enterprise software" (GPS analogy).
  - Gro Intelligence (agri-insight platform built partly on satellite data) closed in 2024; a former employee cited a "fundamental mismatch between the product and the market" and "chasing deals for projects that resembled bespoke consultancy work" (AgFunderNews, 31 May 2024).
- **How they're trying to solve it:** Vertical "solutions" companies (insurance, agriculture, carbon) instead of horizontal platforms; embedding EO in Esri/Microsoft/Snowflake-style platforms (TerraWatch notes Xoople "laid the distribution pipes before having their own data supply", 13 Apr 2026); LLM agents that answer questions (Google Earth AI geospatial reasoning agent, Oct 2025; Planet–Anthropic, Mar 2025 — see Part A); foundation-model embeddings (AlphaEarth, Clay) as a cheap "insight layer".
- **Data:** Any public stack (Sentinel-1/2, Landsat, HLS, VIIRS, ERA5) plus the customer's own non-EO data (assets list, claims, parcels).
- **Off-the-shelf tech:** Google Earth Engine, Microsoft Planetary Computer, AlphaEarth/Satellite Embedding dataset in GEE, LLM tool-calling over STAC.
- **Hackathon angle:** Pick one non-expert persona and deliver an *answer*, not a map: e.g., "For each of my 200 warehouses/farms/schools, give me a weekly 1-line status + alert", using embeddings-based change and a natural-language summary. The pitch writes itself from the quotes above.
- **Credibility:** Blog (Morrison — influential practitioner), analyst newsletter (TerraWatch), blog-tier aggregator (New Space Economy), reputable trade press (AgFunderNews).
- **Sources:**
  - [Stop Building Satellite Imagery Platforms and Marketplaces — Joe Morrison (12 Nov 2020)](https://joemorrison.substack.com/p/stop-building-satellite-imagery-platforms)
  - [Nobody wants your fancy algorithm — Joe Morrison (18 Apr 2022)](https://joemorrison.substack.com/p/nobody-wants-your-fancy-algorithm)
  - [The State of Commercial Earth Observation Market: 2025 Edition — TerraWatch (22 Oct 2025; paywalled beyond intro)](https://newsletter.terrawatchspace.com/state-of-commercial-earth-observation-2025-edition/)
  - [Earth Observation Essentials: April 13, 2026 — TerraWatch](https://newsletter.terrawatchspace.com/earth-observation-essentials-april-13-2026/)
  - [Why Does Defense Dominate Earth Observation Demand Over Commercial Markets? — New Space Economy (23 Oct 2026)](https://newspaceeconomy.ca/2026/10/23/why-does-defense-dominate-earth-observation-demand-over-commercial-markets/)
  - [Ag insights platform Gro Intelligence is closing down — AgFunderNews (31 May 2024)](https://agfundernews.com/breaking-ag-insights-platform-gro-intelligence-is-closing-down)

---

### Theme 3 — Tip-and-cue across sensors and providers

- **What it is:** A wide-area or cheap sensor (AIS, RF geolocation, Sentinel-1, PlanetScope) flags something; a high-resolution sensor (SkySat, WorldView, ICEYE/Umbra spotlight) is then tasked to look. Conceptually old, operationally still hard, especially across *different companies'* constellations.
- **Problems / pain points:**
  - Planet's 2021 description: the daily Dove scan "can 'tip' analysts off to change in activity on the ground", then they "cue" a SkySat; covert projects increasingly move weekly to evade monitoring (Planet Pulse, Shiloh Dockstader, 31 Aug 2021).
  - Technion paper (Weissman, Ivry, Cohen; arXiv 2512.09670, 10 Dec 2025): "Current approaches rarely support an end-to-end loop where anomaly-based triggers directly inform cue generation"; schedulers assume discrete slots and fixed windows. In their AIS-driven demo only **85 of 104** cues even had feasible imaging windows across three simulated satellites (SkySat-C11, SkySat-C15, Jilin-1) — illustrating that physical access, not analytics, often caps tip-and-cue.
  - Success "depends on latency, object type, trajectory accuracy for moving targets, and the cueing sensor's acquisition options" (Wikipedia "Tip and cue" summary). Cross-provider tasking still needs separate accounts/contracts (see Theme 4).
- **How they're trying to solve it:** Vertically integrated mixed constellations (Planet Doves+SkySat+Pelican; MDA CHORUS C-band wide + trailing X-band high-res SAR); ESA Φ-lab "Laying the Foundation for AI-Based Tip and Cue" (Apr–May 2025, simulated wide "tip" + high-res "cue" satellites); ICEYE example cueing Stripmap 12 h 38 min after a Sentinel-1 iceberg detection (Jan 2021); aggregators/orchestrators (Arlula's Fulfilment Engine and Constellation Orchestration, SkyFi, UP42) to task many providers through one API.
- **Data:** NOAA MarineCadastre AIS (free, US waters), Global Fishing Watch AIS-derived vessel presence and SAR vessel detections, Sentinel-1 GRD (free), Sentinel-2, CelesTrak TLEs (to compute who can see the target when), Umbra/Capella open SAR samples.
- **Off-the-shelf tech:** Skyfield/SGP4 for pass prediction, TrAISformer-style trajectory prediction, SAR ship detectors, VLM captioning of the cued image.
- **Hackathon angle:** "Who can look, and when?" — given an anomaly (AIS gap / dark-vessel detection in Sentinel-1), compute the next imaging opportunities across public TLEs of commercial constellations, estimate where the vessel will be (dead-reckoning from last AIS), and auto-draft a ranked tasking request. Demonstrates the tip → cue → report loop with fully public data.
- **Credibility:** Company blog (Planet), preprint (arXiv), encyclopedia summary (Wikipedia; underlying ICEYE/ESA/MDA items not opened).
- **Sources:**
  - [New Space Opportunities Supplying the Future of Tip and Cue Strategies — Planet Pulse (31 Aug 2021)](https://www.planet.com/pulse/new-space-opportunities-supplying-the-future-of-tip-and-cue-strategies/)
  - [Planet white paper: Tip and Cue (2021)](https://learn.planet.com/rs/997-CHH-265/images/White%20Paper%20-%20Tip%20and%20Cue.pdf)
  - [An Automated Tip-and-Cue Framework for Optimized Satellite Tasking and Visual Intelligence — arXiv 2512.09670 (10 Dec 2025)](https://arxiv.org/html/2512.09670v1)
  - [Tip and cue — Wikipedia (accessed 24 Oct 2026)](https://en.wikipedia.org/wiki/Tip_and_cue)

---

### Theme 4 — Tasking friction, procurement and licensing

- **What it is:** Buying or tasking high-resolution imagery has historically meant sales calls, NDAs, licence negotiation, minimum orders and per-provider accounts. Defence demand shapes licences that do not suit software embedding.
- **Problems / pain points:**
  - Morrison: buying imagery is "closer to a hostage negotiation than a sales transaction"; "I should be able to hit an API or submit a request for exactly what I want without asking anyone for permission" (7 Aug 2020).
  - New Space Economy (23 Oct 2026): "Licensing friction: controlled security licenses conflict with the 'license once, embed everywhere' model" software platforms need; "architecture mismatch: point-target tasking conflicts with the continuous area coverage commercial users need"; companies hire cleared defence sales staff rather than enterprise vertical teams.
  - Morrison on platform fragility: when TerraServer (acquired by PrecisionHawk 2015) shut abruptly in 2020, the lesson was "if someone at one of the major imagery providers decides you're done…you're done" (12 Nov 2020).
  - 2026 Iran war: commercial access can be withdrawn at government request (Theme 18); investigators had to buy non-US imagery through resellers (Soar, SI Imaging Services, UP42) or Airbus at "a few hundred dollars per image" (CJR, 11 May 2026).
- **How they're trying to solve it:** Self-serve marketplaces with no minimum spend (SkyFi: "without subscriptions, long-term commitments, or minimum spend requirements"); prepaid credits (UP42: 100 credits = €1, minimum purchase 10,000 credits = €100, credits expire after 24 months); published price lists (Umbra); B2B "fulfilment" middleware (Arlula Geostack standardises ordering, tasking and delivery across providers and claims to let operators sell "without building a custom marketplace"); open data programmes (Umbra, Capella, Maxar/Vantor Open Data, SkyFi Open Data).
- **Data:** Public provider catalogues exposed via STAC (Umbra, Capella, Maxar Open Data on AWS); SkyFi/UP42 APIs for quotes (account needed).
- **Off-the-shelf tech:** STAC API clients (pystac-client), provider SDKs (UP42 Python SDK, SkyFi API), LLM agents for form-filling.
- **Hackathon angle:** "Imagery buying copilot": a user types "I need a sub-meter image of this mine after 15 Oct, cloud-free" → agent searches open catalogues first (free Sentinel/Landsat/Open Data), then lists commercial options with published prices (Umbra list prices, EOS sample prices) and explains licence terms in plain language. Without real purchase, can still be demoed on public STAC catalogues.
- **Credibility:** Blog (Morrison), blog-tier aggregator (New Space Economy), reputable press (CJR), official vendor pages.
- **Sources:**
  - [The Commercial Satellite Imagery Business Model is Broken — Joe Morrison (7 Aug 2020)](https://joemorrison.substack.com/p/the-commercial-satellite-imagery)
  - [Stop Building Satellite Imagery Platforms and Marketplaces — Joe Morrison (12 Nov 2020)](https://joemorrison.substack.com/p/stop-building-satellite-imagery-platforms)
  - [Why Does Defense Dominate EO Demand… — New Space Economy (23 Oct 2026)](https://newspaceeconomy.ca/2026/10/23/why-does-defense-dominate-earth-observation-demand-over-commercial-markets/)
  - [Blind Spots — CJR (11 May 2026)](https://cjr.org/feature/blind-spots-satellite-osint-open-source-middle-east-iran-blackout-planet-labs-vantor-maxar.php)
  - [SkyFi pricing page (accessed 24 Oct 2026)](https://skyfi.com/en/pricing)
  - [UP42 pricing page (accessed 24 Oct 2026)](https://up42.com/pricing)
  - [Arlula homepage — Geostack (accessed 24 Oct 2026)](https://www.arlula.com/)

---

### Theme 5 — Pricing opacity

- **What it is:** Most high-resolution imagery prices are "contact sales", vary by customer, and carry minimum areas. Small buyers cannot estimate cost before engaging, which kills experimentation.
- **Problems / pain points (published price points actually found, accessed 24 Oct 2026):**
  - **Umbra (SAR)** — one of the few fully public price lists: Spotlight 5×5 km, 1-look: **$675 (1.0 m), $950 (0.5 m), $1,750 (0.35 m), $3,250 (0.25 m)**; natural-footprint 1-look $1,500–$3,750; Dwell 5×5 km $4,750 (+40% for CSI/SAR video); Scan strips $1,250–$4,000. No archive prices published.
  - **EOS Data Analytics** (reseller of Satellogic/BlackSky etc.): "from **$4.50/km²** for archive and **$12/km²** for tasking" (30 cm–1.5 m); sample sites range $1.7–$16/km² archive and $10–$24/km² tasking. Full list only in a PDF.
  - **SkyFi:** optical "starting at $15" (single archive image), tasking image "starting at $200", SAR "starting at $450", aerial from $35, analytics from $5; multispectral open data free; "low minimum order sizes" but no figures on the page.
  - **UP42:** no per-km² prices published ("UP42 provides estimates before purchase"); credits model 100 credits = €1, €100 minimum purchase, 5% bonus above 1M credits; Enterprise pricing via sales.
  - **Arlula:** no public prices on current site; an older Geospatial World article claimed images "for as little as $10" with a 1 km² minimum (undated).
  - **Planet:** public pricing page shows no prices (page contains only the title "Planet Pricing").
  - **Airbus:** "a few hundred dollars per image" for high-resolution conflict imagery bought by journalists (CJR, May 2026).
  - Morrison (2020): "Lack of affordability of archival imagery is stifling innovation"; "Stop treating your archival data like a goldmine."
  - Not verified (pages blocked 403): Apollo Mapping and LandInfo price lists.
- **How they're trying to solve it:** Public list prices (Umbra), instant quotes in-app (SkyFi, UP42), open archives (Umbra/Capella open data), Morrison's argument to price tasking high and archive low.
- **Data:** The price points above can seed a dataset; provider STAC catalogues give scene footprints/areas.
- **Off-the-shelf tech:** Simple cost model + catalogue search.
- **Hackathon angle:** "Kayak for satellite imagery": for an AOI and date window, show *free* options first (Sentinel-1/2, Landsat, HLS, open-data programmes) and estimated commercial cost ranges by resolution using published list prices, with a "do you really need 30 cm?" explainer showing what is visible at 10 m vs 50 cm. Low technical risk, clear problem statement.
- **Credibility:** Official vendor pages (prices), reputable press (CJR), blog (Morrison), trade press (Geospatial World, undated).
- **Sources:**
  - [Umbra pricing (accessed 24 Oct 2026)](https://umbra.space/pricing)
  - [EOS high-resolution images (accessed 24 Oct 2026)](https://eos.com/products/high-resolution-images/)
  - [SkyFi pricing (accessed 24 Oct 2026)](https://skyfi.com/en/pricing)
  - [UP42 pricing (accessed 24 Oct 2026)](https://up42.com/pricing)
  - [Arlula pricing page (accessed 24 Oct 2026; no prices)](https://www.arlula.com/pricing/)
  - [Planet pricing page (accessed 24 Oct 2026; no prices)](https://www.planet.com/pricing/)
  - [Australian startup Arlula drives down the cost of satellite images by 25x — Geospatial World (undated)](https://geospatialworld.net/news/australian-startup-arlula-drives-down-the-cost-of-satellite-images-by-25x)
  - [The Commercial Satellite Imagery Business Model is Broken — Joe Morrison (7 Aug 2020)](https://joemorrison.substack.com/p/the-commercial-satellite-imagery)
  - [Blind Spots — CJR (11 May 2026)](https://cjr.org/feature/blind-spots-satellite-osint-open-source-middle-east-iran-blackout-planet-labs-vantor-maxar.php)

---

### Theme 6 — Marketplace and platform failures, sales and pivots

- **What it is:** A long list of horizontal EO marketplaces/analytics platforms have shut, been sold at distressed values, or pivoted to B2B software — consistent with Morrison's 2020 prediction that platforms/marketplaces "Fundamentally, I don't think they work… One word: demand."
- **Verified cases:**
  | Company | What happened | When | Source |
  |---|---|---|---|
  | TerraServer | Imagery archive/marketplace (owned by PrecisionHawk since 2015) shut abruptly, no public explanation | 2020 | [Morrison, 12 Nov 2020](https://joemorrison.substack.com/p/stop-building-satellite-imagery-platforms) |
  | Orbital Insight | Raised ~$130M; 2023 reports of serious financial difficulty, reported $3M emergency loan at $50M valuation (only ~$0.5M secured); acquired by Privateer (Wozniak) — reported as saving it from bankruptcy | Sep 2023 → May 2024 | [Wikipedia (citing Reuters 7 May 2024, Jack Poulson Oct 2023)](https://en.wikipedia.org/wiki/Orbital_Insight); [Via Satellite, 8 May 2024](https://www.satellitetoday.com/finance/2024/05/08/steve-wozniaks-privateer-acquires-orbital-insight/) |
  | Gro Intelligence | Agri-climate data platform ($85M Series B, Jan 2021); missed payroll Feb 2024, cut 60% of staff, closed; most revenue from Unilever; "bespoke consultancy" drift | Feb–May 2024 | [AgFunderNews, 31 May 2024](https://agfundernews.com/breaking-ag-insights-platform-gro-intelligence-is-closing-down) |
  | Descartes Labs | Analytics platform; acquired by EarthDaily Analytics (both owned by Antarctica Capital) | Oct 2024 | [Via Satellite, 15 Oct 2024](https://www.satellitetoday.com/imagery-and-sensing/2024/10/15/earthdaily-acquires-descartes-labs/) |
  | Spire (maritime) | Sold its AIS ship-tracking data business to Kpler for $241M | Announced 13 Nov 2024 | [Wikipedia (citing SpaceNews 13 Nov 2024)](https://en.wikipedia.org/wiki/Spire_Global) |
  | UP42 | Airbus sold the marketplace to Saudi PIF-owned Neo Space Group | Announced Dec 2024, closed 10 Jul 2025 | [Military Aerospace](https://www.militaryaerospace.com/communications/article/55302818/neo-space-group-acquires-geospatial-firm-up42-from-airbus); [Space Insider, 3 Dec 2024](https://spaceinsider.tech/2024/12/03/neo-space-group-set-to-expand-geospatial-capabilities-with-acquisition-of-up42-from-airbus) |
  | SkyWatch | Rebuilt EarthCache (API for app builders) as SkyWatch HUB for end-users — "transition away from being an API provider" | ~2023–2025 (date not confirmed) | [SpaceQ](https://spaceq.ca/skywatch-unveils-full-enterprise-version-of-skywatch-hub/) |
  | Arlula | From imagery marketplace API to "Operational infrastructure for Earth Observation" software (Geostack: Sales Engine, Fulfilment Engine, Constellation Orchestration) | by 2026 | [arlula.com](https://www.arlula.com/) |
- **Problems / pain points:** Weak commercial demand (government = 70–80% of EO revenue per TerraWatch Jan 2026 as cited by New Space Economy); bespoke work instead of repeatable product; supplier control over licensing; free Google Earth Engine/Sentinel competition.
- **How they're trying to solve it:** Consolidation under PE/sovereign owners; vertical integration (EarthDaily constellation); pivot to selling software to operators; defence focus.
- **Unverified / to check:** Astraea (EarthAI platform) status; SpaceKnow status; Radiant MLHub retirement (mlhub.earth returns 404 — consistent with retirement, but no notice found); Satellogic's move to US/defence focus.
- **Hackathon angle:** Not a build target itself, but the table is strong "why now / why previous attempts failed" material for the pitch: the team should *not* pitch a marketplace; pitch a narrow answer for a narrow user.
- **Credibility:** Reputable trade press (Via Satellite, AgFunderNews, SpaceQ, Military Aerospace), encyclopedia (Wikipedia, with cited primary press), blog (Morrison), company site.
- **Sources:** inline in the table above, plus [Why Does Defense Dominate EO Demand… — New Space Economy (23 Oct 2026)](https://newspaceeconomy.ca/2026/10/23/why-does-defense-dominate-earth-observation-demand-over-commercial-markets/).

---

### Theme 7 — Analysis-ready data (ARD) and cross-sensor harmonisation

- **What it is:** Raw Level-1 imagery needs atmospheric correction, cloud/shadow masking, terrain correction (SAR), co-registration and radiometric harmonisation before two dates or two sensors can be compared. ARD standards try to push that work upstream to the provider.
- **Problems / pain points:**
  - CEOS: many users lack the "expertise, infrastructure and internet bandwidth" to prepare satellite data; even experienced users spend "a large proportion of their effort into data preparation", a major barrier to using space data (CEOS-ARD page, accessed 24 Oct 2026).
  - Cross-sensor mixing (e.g., Landsat + Sentinel-2) needs BRDF normalisation and spectral bandpass adjustment — the reason NASA built HLS.
  - Commercial smallsat fleets (e.g., PlanetScope's many Doves) have inter-sensor radiometric differences; Planet sells "Analysis-Ready PlanetScope" using proprietary AI to create "harmonized, cloud-masked, and spatially consistent daily stacks" (Planet Insights Platform launch, 9 Apr 2024 — see the Planet Insights Platform entry).
- **How they're trying to solve it:**
  - **CEOS-ARD Product Family Specifications** (versions listed 2026): Surface Reflectance v5.0.2, Surface Temperature v5.0.1, Aquatic Reflectance v2.0.1, Nighttime Lights Surface Radiance v1.0.1, SAR v1.3.1 (covering Normalised Radar Backscatter, Polarimetric, Ocean Radar Backscatter, Geocoded SLC, InSAR, Composite Backscatter).
  - **NASA HLS (Harmonized Landsat Sentinel-2):** 30 m surface reflectance every **~1.6 days** (chart shows 1.4 days with five satellites, reached in 2025), latency **2–3 days**; atmospheric correction, BRDF and bandpass adjustment; common 30 m grid on Sentinel-2 MGRS tiles (109.8 km); COG via LP DAAC; Sentinel-2C incorporated; **HLS vegetation index suite released Feb 2025**; **low-latency HLS "anticipated to be completed in 2027"** (page updated 21 Oct 2026).
  - ASF DAAC radiometrically terrain-corrected SAR products and HyP3 on-demand processing (NASA Earthdata SAR page).
- **Data:** HLS L30/S30 (LP DAAC, free), Sentinel-2 L2A (Copernicus Data Space; Earth Search on AWS), Landsat Collection 2 Level-2, Sentinel-1 RTC (ASF/OPERA), Planet NICFI basemaps (tropics).
- **Off-the-shelf tech:** HyP3, OPERA products, Sen2Cor, s2cloudless / OmniCloudMask (cloud masks), arosics (co-registration), Google Earth Engine harmonised collections.
- **Hackathon angle:** "ARD in one click for a non-expert": AOI → cloud-masked, harmonised HLS time series and NDVI/NDWI trend with plain-English annotation of gaps ("no clear view 3–19 Sept: clouds"). Good supporting component rather than a standalone pitch.
- **Credibility:** Official (CEOS, NASA Earthdata).
- **Sources:**
  - [CEOS Analysis Ready Data (accessed 24 Oct 2026)](https://ceos.org/ard/)
  - [Harmonized Landsat Sentinel-2 (HLS) — NASA Earthdata (updated 21 Oct 2026)](https://www.earthdata.nasa.gov/data/projects/hls)
  - [SAR basics — NASA Earthdata (accessed 24 Oct 2026)](https://www.earthdata.nasa.gov/learn/earth-observation-data-basics/sar)
  - [Planet Labs releases new Planet Insights Platform — Geo Week News (Apr 2024)](https://www.geoweeknews.com/articles/planet-insights-platform-satellite-imagery-earth-observation-ai-analytics/)

---

### Theme 8 — STAC and cloud-native interoperability

- **What it is:** Every provider historically had its own catalogue, metadata and delivery format, so each new dataset meant a new pipeline. The cloud-native geospatial stack (STAC metadata + COG/Zarr/GeoParquet/PMTiles/COPC on object storage) is the industry's answer, and is now broadly adopted.
- **Problems / pain points:** stacspec.org describes users having to build a separate pipeline for each data collection and aims to ensure "new code doesn't need to be written whenever a new data set or API is released"; provider-specific metadata conventions (e.g., `eo:bands` vs `raster:bands`) are only now being unified; commercial catalogues still vary in licences, footprints and quality flags.
- **How they're trying to solve it:**
  - **STAC v1.1.0** — "the first stable release after the 1.0.0 release" (v1.0.0 was 25 May 2021): unified `bands` construct merging `eo:bands` and `raster:bands`; `data_type`, `nodata`, `statistics`, `unit` in common metadata; SPDX licence expressions; `item_assets` into core; best-practice MIME types for COPC, GeoParquet, 3D Tiles, PMTiles (GitHub releases; 1.1.0 dated 11 Sep, year not shown on page — believed 2024, unverified).
  - stacspec.org lists catalogues such as the Copernicus Data Space Ecosystem, CEDA STAC API and Capella Open Data, and supporters including Planet, Microsoft, Element 84, Maxar, USGS, AWS, NASA, Google Earth Engine and Esri.
  - **Cloud-Native Geospatial Forum (CNG)** — a Radiant Earth initiative with ~34 sponsor/community organisations (AWS, Microsoft, Google, Esri, NASA, Planet, Element 84, Earthmover, Development Seed, Wherobots, Overture Maps, HOT, Ai2, …); upcoming **CNG Zürich, 29 Oct 2026**, and a **Geo-Embeddings Sprint, 27–28 Oct 2026** (IBM, CNG, Clark University, Planet) on benchmarking/adoption of EO embeddings; blog posts in 2026 on "Portolan: a serverless spatial data infrastructure" (2 Sep 2026) and "Hybrid Icechunk stores for serverless web mapping" (10 Aug 2026).
  - **Source Cooperative** (Radiant Earth): non-commercial data publishing on object storage; hosts e.g. VIDA's combined Google–Microsoft–OSM Open Buildings (GeoParquet, FlatGeobuf, PMTiles), Planet's RapidAI4EO, Vizzuality land/carbon indicators; pricing "not announced yet".
  - Arlula's Geostack "Data Normalisation Pipeline" converts imagery/metadata to STAC and cloud-optimised formats — interoperability as a sellable product.
- **Data:** Earth Search (Element 84) STAC, Microsoft Planetary Computer STAC, Copernicus Data Space STAC, Maxar/Umbra/Capella open-data STAC catalogues, stacindex.org.
- **Off-the-shelf tech:** pystac-client, stackstac/odc-stac, rasterio/rio-tiler, TiTiler, DuckDB-spatial on GeoParquet, Icechunk/Zarr.
- **Hackathon angle:** STAC makes a 36-hour build feasible: one search interface across free (Sentinel, Landsat) and commercial-open catalogues. Good "plumbing" for the main idea; also a possible "embeddings-as-STAC" angle tied to the CNG Geo-Embeddings Sprint happening the same week.
- **Credibility:** Official spec/community pages (stacspec.org, GitHub, CNG, Source Cooperative).
- **Sources:**
  - [STAC specification site (accessed 24 Oct 2026)](https://stacspec.org/en)
  - [radiantearth/stac-spec releases — GitHub (v1.1.0)](https://github.com/radiantearth/stac-spec/releases)
  - [Cloud-Native Geospatial Forum (accessed 24 Oct 2026)](https://cloudnativegeo.org/)
  - [Source Cooperative (accessed 24 Oct 2026)](https://source.coop/)
  - [Arlula Geostack (accessed 24 Oct 2026)](https://www.arlula.com/)

---

### Theme 9 — The change-detection false-positive problem

- **What it is:** Automated "something changed here" alerts are the core monitoring product, but naive pixel differencing fires on clouds, cloud shadows, haze, seasonal vegetation cycles, sun-angle/off-nadir differences and sub-pixel misregistration. Customers drown in alerts or stop trusting them.
- **Problems / pain points:**
  - Morrison: no generic change algorithm works because each customer defines "change" differently; workable feeds are custom-tuned (18 Apr 2022).
  - Global Forest/Nature Watch: "satellite-derived data is subject to errors including false alerts"; an alert "begins as low confidence when the first signs of potential disturbance appear"; radar RADD "may take up to 12 days to detect change" (GFW/GNW blog, updated 13 Jan 2026).
  - Search-snippet evidence (pages not opened): a 2024 ACRS study found false positives in land-cover change "frequent at the agricultural fields or cloud shadows" even after cloud masking; a JpGU 2023 Taiwan study notes traditional methods are "prone to misjudge seasonal phenology as a changed area"; a practitioner guide says half a pixel of shift creates edge-shaped phantom change; Dai & Khorram (1998) quantified misregistration effects.
  - Blog-tier: a VIIRS-based wildfire detector in Sweden reportedly produced false alarms in ~10% of cases from sunlight reflected off solar plants and factories (Max Polyakov blog, 3 Jul 2026 — unverified).
- **How they're trying to solve it:**
  - **Multi-sensor confirmation:** GFW integrated alerts (GLAD-L 30 m Landsat, GLAD-S2 10 m, RADD 10 m Sentinel-1, and since Jan 2026 DIST-ALERT 30 m for all vegetation): "Highest confidence is only reached when multiple alerts systems detect a disturbance in the same pixel location"; "False positives are effectively eliminated in the highest confidence class" (no measured figure given); integrated alerts arrived on average **nine days earlier** than any single system in the 2021 Amazon.
  - Optical-vs-SAR cross-checks ("the probability that both systems would produce the same hallucination is extremely small" — Polyakov blog).
  - Time-series methods (BFAST/CCDC-style), season-matched comparisons, embedding-distance change (AlphaEarth/Clay), sub-pixel co-registration, tile-level rather than pixel-level change (Leicester onboard system).
- **Data:** GFW integrated deforestation alerts (open), OPERA DIST-ALERT (open), Sentinel-1/2, HLS, labelled change sets (xView2/xBD, SpaceNet 7, LEVIR-CD, DynamicEarthNet).
- **Off-the-shelf tech:** Google Earth Engine CCDC, s2cloudless, arosics, AlphaEarth Satellite Embedding in GEE, SAM2 for object-level change, VLM for "is this real change?" second-pass review.
- **Hackathon angle (strong):** **"Alert de-noiser / second opinion"**: take an existing open alert stream (GFW integrated alerts or DIST-ALERT for a region), and for each alert automatically pull pre/post Sentinel-2 + Sentinel-1 chips, run checks (cloud/shadow probability, phenology match vs same month last year, SAR agreement, misregistration test), and output a triaged list: "likely real / likely artefact / needs human". Measure the share of alerts auto-dismissed vs a small hand-labelled sample. Clear user (NGO analysts, supply-chain compliance teams under EUDR), public data, demoable.
- **Credibility:** Official/NGO (GFW/WRI), blog (Morrison, Polyakov), conference abstracts and patents (search snippets only).
- **Sources:**
  - [Integrated deforestation alerts — Global Forest Watch / Global Nature Watch blog (orig. 2022, updated 13 Jan 2026)](https://globalnaturewatch.org/blog/data-and-tools/integrated-deforestation-alerts/)
  - [Nobody wants your fancy algorithm — Joe Morrison (18 Apr 2022)](https://joemorrison.substack.com/p/nobody-wants-your-fancy-algorithm)
  - [AI in Satellite Imagery: Autonomous Analysis & the Risk of Hallucinations — Max Polyakov blog (3 Jul 2026)](https://maxpolyakov.com/ai-satellite-image-analysis-hallucinations/)
  - [ACRS 2024 abstract AB0163 (search snippet; not opened)](https://acrs-aars.org/proceeding/ACRS2024/AB0163.pdf)
  - [JpGU 2023 U05-04 presentation (search snippet; not opened)](https://pub.confit.atlas.jp/en/event/jpgu2023/presentation/U05-04)
  - [Canonical Correlation Analysis for Misaligned Satellite Image Change Detection — arXiv 1812.09280 (search snippet; not opened)](https://arxiv.org/pdf/1812.09280)
  - [An onboard automatic change detection system for disaster monitoring — Univ. of Leicester (search snippet; not opened)](https://figshare.le.ac.uk/articles/journal_contribution/An_onboard_automatic_change_detection_system_for_disaster_monitoring/10181687/1)
  - [Change-detection practitioner skill guide (blog-tier; search snippet)](https://skillsmp.com/creators/muend/geoai-skills/skills-change-detection)

---

### Theme 10 — Labelling cost and label scarcity

- **What it is:** Supervised models need many expert-drawn labels; overhead objects are small, rare and need domain knowledge (SAR especially). Labels are the single most expensive input in GEOINT computer vision.
- **Problems / pain points:**
  - NGA planned an RFP worth "upwards of $700 million" for data labelling — per Director Frank Whitworth the US government's largest-ever data-labelling RFP; "Data-labeling is the process where the human actually identifies the object"; "It's really about the amount — that's a big number" (DefenseScoop, 3 Sep 2024).
  - Breaking Defense (28 Aug 2024): many AI systems depend on large numbers of low-paid labellers; NGA's advantage is decades of analyst reports paired with imagery — but curation is the hard part.
  - xView3 (DIU + Global Fishing Watch): earlier SAR vessel efforts were limited by how little labelled data could be produced because labelling "requires subject-matter expertise and large volumes of imagery"; SAR identification is complicated by resolution, incidence angle, vessel build material and missing AIS ground truth.
  - Fields of The World (Kerner et al., AAAI-2025): field boundaries are expensive to collect manually and ML progress "is restricted by the lack of labeled datasets."
  - Maven: by its second year it had labelled >4 million images of military objects (GlobalSecurity summary in search results; not opened).
- **How they're trying to solve it:** Big public benchmark datasets (xView: ~1M objects, 60 classes, 1,415 km² at 0.3 m; SpaceNet 1–9, latest SN9 cross-modal optical–SAR registration; FTW 70,462 samples in 24 countries); AIS-correlated auto-labels (xView3); foundation models for few-shot (PANGAEA finds some GFMs, e.g., CROMA, beat supervised baselines at 10% labels, but GFMs "do not consistently outperform supervised models"); SAM-assisted annotation; synthetic data (Rendered.ai — see Part A).
- **Data:** xView, xView2/xBD, xView3-SAR, SpaceNet, FTW, Open Buildings (Source Cooperative), OSM as weak labels.
- **Off-the-shelf tech:** SAM/SAM2 with geospatial wrappers (segment-geospatial), Label Studio, active-learning loops, CLIP/RemoteCLIP zero-shot retrieval.
- **Hackathon angle:** "Ten clicks to a detector": user clicks ~10 examples of an object (e.g., solar farms, brick kilns, fish ponds) on Sentinel-2/NAIP; system uses embeddings similarity search (AlphaEarth/Clay) to find all others in a region, then asks the user to verify only the uncertain ones (active learning). Shows label cost collapsing from thousands to tens.
- **Credibility:** Reputable press (DefenseScoop, Breaking Defense), official/program pages (xView, xView3, SpaceNet), peer-reviewed (FTW at AAAI, PANGAEA preprint/IEEE GRSM).
- **Sources:**
  - [NGA to offer $700M for data-labeling — DefenseScoop (3 Sep 2024)](https://defensescoop.com/2024/09/03/nga-700m-data-labeling-advance-computer-vision-models/)
  - ['AI gold mine' — Breaking Defense (28 Aug 2024)](https://breakingdefense.com/2024/08/ai-gold-mine-nga-aims-to-exploit-archive-of-satellite-images-expert-analysis/)
  - [xView3 Dark Vessel Detection (accessed 24 Oct 2026)](https://iuu.xview.us/)
  - [xView dataset (accessed 24 Oct 2026)](https://xviewdataset.org/)
  - [SpaceNet (accessed 24 Oct 2026)](https://spacenet.ai/)
  - [Fields of The World — arXiv 2409.16252 (Sep/Dec 2024)](https://arxiv.org/abs/2409.16252)
  - [PANGAEA benchmark — arXiv 2412.04204v2 (30 Apr 2025)](https://arxiv.org/html/2412.04204v2)
  - [Project Maven — GlobalSecurity (search snippet; not opened)](https://www.globalsecurity.org/intell/systems/maven.htm)

---

### Theme 11 — Ground-truth scarcity and validation

- **What it is:** Even when models exist, there is rarely independent field truth to validate them — especially in the Global South, for crops, carbon/biomass, informal settlements and maritime "dark" activity. Validation is what buyers (insurers, carbon registries, regulators) actually pay for.
- **Problems / pain points:**
  - FTW authors: existing field-boundary methods "lack sufficient geographic coverage, accuracy, and generalization capabilities"; PANGAEA authors note most benchmarks are geographically biased toward North America and Europe.
  - xView3: lack of ground-truth data like AIS hampers SAR vessel classification.
  - GFW alerts: no measured accuracy figure is given for the highest-confidence class.
  - NGA's Munsell on AI output for targeting: "you have to take those extra steps to make…that thing is 100% correct" (Breaking Defense, 28 Aug 2024).
  - Carbon markets: satellite-based baselines for REDD+ credits have been heavily contested (2023 Guardian/Die Zeit/SourceMaterial investigation into Verra — page could not be fetched; treat as lead).
- **How they're trying to solve it:** Multi-source agreement as proxy truth (GFW integrated alerts; optical–SAR cross-validation); spaceborne lidar (GEDI) and P-band SAR (ESA Biomass — data opened 26 Jan 2026 per New Space Economy) for biomass reference; crowdsourced labels; geographically diverse benchmarks (FTW, PANGAEA).
- **Data:** GEDI L2/L4 (biomass/canopy height), ESA Biomass, NISAR L-band (provisional data released 20 Jul 2026 per New Space Economy), FTW, WorldCereal, OSM, AIS (NOAA MarineCadastre, GFW).
- **Off-the-shelf tech:** Google Earth Engine, canopy height models (Meta/WRI 1 m canopy height), statistical accuracy assessment (Olofsson-style sample-based area estimation).
- **Hackathon angle:** "Independent auditor": for a given carbon project or deforestation-free supply claim polygon, compute an independent multi-sensor estimate (Sentinel-2 + GEDI + GFW alerts) and flag disagreement with the claimed baseline. Clear villain/clear user story, though validation itself stays hard.
- **Credibility:** Peer-reviewed/preprint (FTW, PANGAEA), program page (xView3), NGO (GFW), reputable press (Breaking Defense); carbon item is an unverified lead.
- **Sources:**
  - [Fields of The World — arXiv 2409.16252](https://arxiv.org/abs/2409.16252)
  - [PANGAEA — arXiv 2412.04204v2 (30 Apr 2025)](https://arxiv.org/html/2412.04204v2)
  - [xView3 (accessed 24 Oct 2026)](https://iuu.xview.us/)
  - [GFW/GNW integrated alerts blog (updated 13 Jan 2026)](https://globalnaturewatch.org/blog/data-and-tools/integrated-deforestation-alerts/)
  - ['AI gold mine' — Breaking Defense (28 Aug 2024)](https://breakingdefense.com/2024/08/ai-gold-mine-nga-aims-to-exploit-archive-of-satellite-images-expert-analysis/)
  - [New Space Economy (23 Oct 2026) — Biomass and NISAR data release dates](https://newspaceeconomy.ca/2026/10/23/why-does-defense-dominate-earth-observation-demand-over-commercial-markets/)

---

### Theme 12 — The last mile to non-expert users

- **What it is:** Farmers, insurers, journalists, municipal staff and NGO field teams cannot run GIS pipelines. Even "self-serve" APIs assume developers. The industry's own pivots show that end-users, not developers, are the paying customers.
- **Problems / pain points:**
  - SkyWatch rebuilt EarthCache as SkyWatch HUB after finding many customers were imagery end-users "who lacked the resources to build on the EarthCache API" (SpaceQ, as summarised in search results).
  - Google (8 Apr 2025): "Geospatial information can be big, complex and hard to understand"; use cases "often require various kinds of data that need to be aligned and cross-referenced"; generative AI could "reduce the significant cost, time, and domain expertise required."
  - CEOS: users lack "expertise, infrastructure and internet bandwidth."
  - New Space Economy (Oct 2026): enterprises want "automated risk scores or work orders, not raw imagery"; EO must be embedded invisibly in enterprise software.
  - Google Earth AI's reasoning features were initially limited to US Google Earth Professional users and Trusted Testers (Oct 2025 — see the Google Earth AI entry), i.e., not yet in the hands of the long tail.
- **How they're trying to solve it:** LLM agents over geospatial tools (Google Geospatial Reasoning with Airbus, Maxar, Planet as initial testers and WPP/Choreograph; Microsoft Earth Copilot; Esri AI assistants; Planet–Anthropic) — see Part A; mobile/WhatsApp-style alert products for farmers; embedding EO in existing workflows (Esri, Microsoft, Salesforce-style CRMs).
- **Data:** Any public stack; non-EO context (OSM, admin boundaries, WorldPop/Google population dynamics).
- **Off-the-shelf tech:** LLM tool-calling over STAC + Earth Engine/Planetary Computer; Leafmap/geemap; MapLibre front-ends.
- **Hackathon angle:** Pick one named non-expert (e.g., a county emergency manager, a cooperative's agronomist, a local journalist) and build a chat/alert interface whose output is a sentence + one image + a confidence, not a map. The judging criteria (clear problem, clear solution) favour this framing.
- **Credibility:** Official company research blog (Google), standards body (CEOS), trade press (SpaceQ), blog-tier aggregator (New Space Economy).
- **Sources:**
  - [Geospatial Reasoning — Google Research blog (8 Apr 2025)](https://research.google/blog/geospatial-reasoning-unlocking-insights-with-generative-ai-and-multiple-foundation-models/)
  - [SkyWatch unveils full enterprise version of SkyWatch HUB — SpaceQ](https://spaceq.ca/skywatch-unveils-full-enterprise-version-of-skywatch-hub/)
  - [CEOS-ARD (accessed 24 Oct 2026)](https://ceos.org/ard/)
  - [New Space Economy (23 Oct 2026)](https://newspaceeconomy.ca/2026/10/23/why-does-defense-dominate-earth-observation-demand-over-commercial-markets/)

---

### Theme 13 — Trust, verification and explainability of AI outputs

- **What it is:** As LLMs/VLMs and foundation models are bolted onto EO products, outputs look fluent but are often wrong on exactly the tasks EO buyers care about (counting, localisation, change over time). Users in defence, insurance and journalism need evidence trails, not just answers.
- **Problems / pain points:**
  - **GEOBench-VLM** (Danish et al., Nov 2024 / Mar 2025): best model LLaVA-OneVision reaches only **41.7%** on multiple-choice geospatial questions (~2× random). Counting accuracy: GPT-4o 0.40, Qwen2-VL 0.40, LLaVA-OV 0.44; farm-pond **change detection < 0.20** for all three; referring-expression localisation precision@0.5 IoU: **GPT-4o 0.009**, Qwen2-VL 0.15. Quotes: "current VLMs struggle to leverage temporal dependencies effectively"; GPT-4o "performs the worst, struggling significantly with all sized objects."
  - **"Good at captioning, bad at counting"** (Zhang & Wang, Stanford, 31 Jan 2024): GPT-4V strong on captioning/location recognition, but "poor spatial reasoning limits usefulness on object localization and counting tasks."
  - **PANGAEA** (30 Apr 2025): geospatial foundation models "do not consistently outperform supervised models"; for regression, "performance is so poor that even supervised baselines do better than GFMs."
  - Blog-tier: Polyakov (3 Jul 2026) warns of a "crisis of geospatial truth" — models filling noisy/low-quality pixels with plausible learned patterns; onboard AI (Φsat-2, Prithvi) speeds alerts and so speeds errors.
  - NGA: humans must double-check AI output for targeting (Munsell, Aug 2024).
- **How they're trying to solve it:** Human-in-the-loop review; explainability heat-maps; optical–SAR cross-validation; benchmark suites (GEOBench-VLM, VLEO-Bench, PANGAEA, GEO-Bench); NGA accreditation of GEOINT AI models (lead — NGA AI page returned 403, not verified).
- **Data:** GEOBench-VLM, VLEO-Bench, PANGAEA benchmark datasets (HLS Burn Scars, Sen1Floods11, xView2, SpaceNet 7, etc.).
- **Off-the-shelf tech:** Open VLMs (Qwen2-VL, LLaVA-OneVision), GeoChat/EarthDial-style RS-tuned VLMs, detector + VLM pipelines where the detector counts and the LLM only explains.
- **Hackathon angle:** "Show your work" geospatial assistant: every answer cites the exact scene IDs, dates, pixel chips and the deterministic tool (detector, index, threshold) that produced each number; the LLM is never allowed to count by itself. Include a mini-eval on a GEOBench-VLM subset to show the difference vs a raw VLM. Strong trust story for judges.
- **Credibility:** Preprints/peer-reviewed (arXiv, IEEE GRSM), reputable press (Breaking Defense), blog (Polyakov).
- **Sources:**
  - [GEOBench-VLM — arXiv 2411.19325 (v1 28 Nov 2024; v2 12 Mar 2025)](https://arxiv.org/abs/2411.19325)
  - [GEOBench-VLM full text (v2)](https://arxiv.org/html/2411.19325v2)
  - [Good at captioning, bad at counting — arXiv 2401.17600 (31 Jan 2024)](https://arxiv.org/abs/2401.17600)
  - [PANGAEA — arXiv 2412.04204v2 (30 Apr 2025)](https://arxiv.org/html/2412.04204v2)
  - [pangaea-bench code — GitHub](https://github.com/VMarsocci/pangaea-bench)
  - [AI in Satellite Imagery: … Risk of Hallucinations — Max Polyakov (3 Jul 2026)](https://maxpolyakov.com/ai-satellite-image-analysis-hallucinations/)
  - ['AI gold mine' — Breaking Defense (28 Aug 2024)](https://breakingdefense.com/2024/08/ai-gold-mine-nga-aims-to-exploit-archive-of-satellite-images-expert-analysis/)

---

### Theme 14 — Data provenance and deepfake satellite images

- **What it is:** Satellite images are treated by the public, journalists and markets as "ground truth", but generative models now make convincing fake or doctored overhead images cheap. Fakes have appeared in every major conflict since 2025, and in 2026 the problem was compounded by US providers withholding real imagery (see Theme 18).
- **Problems / pain points:**
  - **India–Pakistan (May 2025):** France 24 Observers documented three viral fakes after the 10 May ceasefire: (1) a "remarkably sharp" image of a hangar at Bholari airbase, traced via reverse image search to a Reddit post whose author said AI was used to "enhance" it — compared with a Maxar 11 May image it lacked a low wall and had mismatched roof strips; (2) Jammu airbase with six fake craters — Sentinel-2 imagery from 11 May "shows that the Indian airbase is actually intact"; (3) Adampur S-400 battery with two craters (>1 million views) — "No crater is visible in the photo taken by Sentinel-2." Debunkers: OSINT analysts Aurora Intel and Damien Symon (France 24, 16 May 2025).
  - **Ukraine (June 2025, Operation Spiderweb)** and **Israel–Iran (June 2025):** fake satellite images inflated claimed damage (TIME, Brady Africk, 27 Oct 2025). TIME: "To make high-quality fakes today, all you need is free software"; "Third-party software to detect AI-generated images exists, but it is imperfect."
  - **US–Israel war on Iran (from 28 Feb 2026):** AFP found a Tehran Times "before vs after" image of a "destroyed" US radar in Qatar was an AI-manipulated Google Earth image of a US base in **Bahrain** — betrayed by a row of cars in identical positions; another fake showing jets striking a painted aircraft silhouette had "gibberish coordinates" embedded and AFP reported detecting a **SynthID** watermark; Vantor said its own imagery confirmed images of a burning Niamey (Niger) airport terminal were fake (Al-Monitor/AFP, 8 Mar 2026). Brady Africk: fakes have "the hallmarks of imperfect AI-generation: odd angles, blurred details." BBC Verify reportedly found fabricated satellite imagery linked to the conflict drew "hundreds of millions of views" (per search summary of Jewish News/Gulf News coverage; not opened).
  - **Foundational:** University of Washington (Bo Zhao et al., 2021) "deepfake geography" study — GAN-generated fake Tacoma imagery using Seattle/Beijing styles; ~8,000-image real/fake set; detector flagged 94% of fakes (per GeekWire/Freethink coverage; original paper not opened).
  - C2PA (content credentials) is camera/editing-tool-centric; no satellite-specific C2PA deployment was found. A 2026 arXiv paper argues C2PA "was not designed to determine authenticity" and notes revoked credentials still accepted in some cases; metadata is stripped by platform re-encoding.
- **How they're trying to solve it:**
  - **Verisat.AI** (ESA Business Applications KickStart, feasibility completed 2025): upload an image → confidence score + heatmap of suspicious regions; trained on real ESA imagery plus Stable-Diffusion fakes; prototype >95% detection accuracy; engaged 30+ journalists; seeking pilots (ESA page updated 11 Aug 2025).
  - **Academic:** "Deepfake Geography: Detecting AI-Generated Satellite Images" (arXiv 2511.17766, Nov 2025) — ~134k real+synthetic images, ViT 95.11% vs CNN 87.02%, fakes mostly StyleGAN2/CycleGAN (so diffusion-era fakes are under-tested); Chapman et al. (SPIE 2024) note no public dataset of generative-AI-manipulated satellite images existed.
  - **Vendor signing:** Satellogic publishes a manifest of SHA-256 checksums signed with an RSA-4096 key for each delivery; Sandia holds a patent on sensor-side hardware signing of imagery; a 2025 US patent (12,450,371) covers blockchain hash verification. No public Planet/Vantor signing service was found (unverified gap).
  - **Practice:** OSINT debunkers compare against free same-day Sentinel-2/Sentinel-1 and archived Google Earth/Maxar; TIME proposes providers offer verification teams/tools and media disclose verification steps.
- **Data:** Sentinel-2 L2A (10 m, ~5-day revisit, free, CC BY-SA 3.0 IGO-style Copernicus licence), Sentinel-1 GRD (all-weather), Landsat, Google Earth historical imagery (view only), Maxar/Vantor Open Data (event imagery), synthetic fakes generated locally with open diffusion models; UW deepfake dataset (availability not verified).
- **Off-the-shelf tech:** Open diffusion models to generate fakes for training; ViT/CLIP-based detectors; SynthID detector (Google; limited access); image forensics (ELA, noise residuals); STAC search to pull the nearest real Sentinel scene for the claimed time and place; co-registration (e.g., arosics) and change detection to diff claim vs reality.
- **Hackathon angle (strong):** **"Satellite claim checker"** — paste a viral overhead image + claimed place/date → system geolocates (or accepts coordinates), pulls the nearest Sentinel-2 and Sentinel-1 scenes before/after the date from a public STAC API, checks whether the claimed damage (craters, burn scars, collapsed roofs) is visible at 10 m, runs a fake-image detector, and outputs a verdict card ("Consistent / Inconsistent / Unverifiable at this resolution") with side-by-side evidence. The May 2025 France 24 cases are ready-made demo cases where Sentinel-2 was exactly the debunking tool.
- **Credibility:** Reputable press (France 24, TIME, AFP via Al-Monitor), official (ESA business page), peer-reviewed/preprint (arXiv), patents (official). BBC Verify "hundreds of millions of views" figure is second-hand.
- **Sources:**
  - [India-Pakistan conflict: AI-generated or edited fake satellite images flood social media — France 24 Observers (16 May 2025)](https://observers.france24.com/en/asia-pacific/20250516-india-pakistan-conflict-ai-generated-or-edited-fake-satellite-images-flood-social-media)
  - [The Troubling Rise of Deepfake Satellite Images — TIME, Brady Africk (27 Oct 2025)](https://time.com/7328281/disinformation-satellite-images-ai/)
  - [Fake AI satellite imagery spurs US-Iran war disinformation — Al-Monitor/AFP (8 Mar 2026)](https://www.al-monitor.com/originals/2026/03/fake-ai-satellite-imagery-spurs-us-iran-war-disinformation)
  - [Gulf News mirror of the AFP story (Mar 2026)](https://gulfnews.com/world/mena/fake-ai-satellite-imagery-spurs-us-iran-war-disinformation-1.500467976)
  - [AI fakes and recycled war footage flood social media amid Iran conflict — Jewish News (2026; not opened)](https://www.jewishnews.co.uk/ai-fakes-and-recycled-war-footage-flood-social-media-amid-iran-conflict/amp/)
  - [Factly: AI-generated image falsely shared as Iran shooting down a B-2 (June 2025)](https://factly.in/an-ai-generated-image-is-falsely-shared-as-iran-shooting-down-a-u-s-b-2-stealth-bomber)
  - [Falsehoods in Conflict: Disinformation in India-Pakistan Crises — South Asian Voices (23 Jul 2025)](https://southasianvoices.org/sec-f-oth-r-india-pakistan-crisis-disinformation-07-23-2025/)
  - [How AI-Powered Disinformation Could Ignite a Nuclear Crisis in South Asia — Modern Diplomacy (6 Jul 2025)](https://moderndiplomacy.eu/2025/07/06/how-ai-powered-disinformation-could-ignite-a-nuclear-crisis-in-south-asia/)
  - [Deepfake geography presents significant risks — GeekWire (2021)](https://www.geekwire.com/2021/deepfake-geography-presents-significant-risks-researchers-detecting/)
  - [Can we stop "deepfake geography"? — Freethink (2021)](https://www.freethink.com/technology/deepfake-geography)
  - [A growing problem of deepfake geography — ACM TechNews (2021)](https://cacmb4.acm.org/news/252258-a-growing-problem-of-deepfake-geography-how-ai-falsifies-satellite-images)
  - [Deepfake Geography: Detecting AI-Generated Satellite Images — arXiv 2511.17766 (Nov 2025)](https://arxiv.org/abs/2511.17766v1)
  - [Verisat.AI — ESA Business Applications (updated 11 Aug 2025)](https://business.esa.int/projects/verisatai)
  - [Chapman et al., manipulated satellite image dataset — Newcastle eprints (SPIE 2024)](https://eprints.ncl.ac.uk/301695)
  - [Satellogic digital signature docs](https://developers.satellogic.com/data/digital-signature.html)
  - [Sandia patent: verification and authentication of remote sensing imagery](https://ip.sandia.gov/patent/systems-and-methods-for-verification-and-authentication-of-remote-sensing-imagery/)
  - [US 12,450,371 B2 — USPTO Official Gazette (21 Oct 2025)](https://patentsgazette.uspto.gov/week42/OG/html/1539-3/US12450371-20251021.html)
  - [Verifying Provenance of Digital Media: Why the C2PA Specifications Fall Short — arXiv 2604.24890 (2026)](https://arxiv.org/html/2604.24890v1)
  - [C2PA Explainer 2.2 (22 Apr 2025)](https://spec.c2pa.org/specifications/specifications/2.2/explainer/_attachments/Explainer.pdf)

---

### Theme 15 — Cloud cover and revisit gaps

- **What it is:** Optical sensors are blind under cloud and at night; most of the planet is cloudy most of the time, so "daily revisit" rarely means daily clear views — especially in the tropics and during monsoons/hurricanes, exactly when users need images.
- **Problems / pain points:** "about 67 percent of Earth's surface is typically covered by clouds"; over oceans "less than 10 percent of the sky is completely clear"; over land "30 percent of skies are completely cloud free" (NASA Earth Observatory, MODIS Aqua 2002–2015, 8 May 2015). Unverified industry claim: ~70% of optical images are unusable due to cloud (integrio blog, search snippet). GFW: radar alerts see through clouds but "may take up to 12 days"; optical alerts are blocked by clouds. TerraWatch (13 Apr 2026): NASA's tropical deforestation method combining optical with NISAR L-band SAR issues alerts "more than three months faster", addressing the cloud limitation of Landsat/Sentinel.
- **How they're trying to solve it:** SAR constellations (Sentinel-1, NISAR, ICEYE, Capella, Umbra); multi-sensor fusion (HLS 1.4–1.6-day revisit); onboard cloud screening (Φsat-2 "eliminate images that are cloudy"); cloud-removal/gap-filling models (risk: hallucination — Theme 13).
- **Data:** Sentinel-1, NISAR (provisional L-band released 20 Jul 2026), HLS, MODIS/VIIRS daily, Sentinel-2 cloud probability layers.
- **Off-the-shelf tech:** s2cloudless, OmniCloudMask, SAR-optical fusion models, Google Earth Engine.
- **Hackathon angle:** "When will I actually see it?" — for an AOI and deadline, forecast the probability of a clear optical view in the next N days (historical cloud climatology + weather forecast cloud cover + known satellite passes) and recommend SAR instead when optical odds are low. Practical for disaster responders and insurers.
- **Credibility:** Official (NASA, ESA, GFW); one blog-tier figure flagged.
- **Sources:**
  - [Cloudy Earth — NASA Earth Observatory (8 May 2015)](https://science.nasa.gov/earth/earth-observatory/cloudy-earth-85843)
  - [GFW/GNW integrated alerts (updated 13 Jan 2026)](https://globalnaturewatch.org/blog/data-and-tools/integrated-deforestation-alerts/)
  - [TerraWatch EO Essentials (13 Apr 2026)](https://newsletter.terrawatchspace.com/earth-observation-essentials-april-13-2026/)
  - [Φsat-2 — ESA (accessed 24 Oct 2026)](https://www.esa.int/Applications/Observing_the_Earth/Phsat-2)
  - [HLS — NASA Earthdata (updated 21 Oct 2026)](https://www.earthdata.nasa.gov/data/projects/hls)
  - [AI in Satellite Imagery — integrio blog (search snippet; unverified)](https://integrio.net/blog/ai-in-satellite-imagery)

---

### Theme 16 — SAR interpretability for non-experts

- **What it is:** SAR works through cloud and at night, and free global SAR (Sentinel-1, NISAR) exists, but SAR images look alien to non-specialists: speckle, layover/shadow, side-looking geometry, polarisation-dependent brightness. Much of SAR's value therefore stays locked inside specialist teams.
- **Problems / pain points:** NASA Earthdata: the look angle "significantly affects the behavior of the backscatter"; "areas of layover and shadow may occur in SAR imagery"; lower-level data needs orbit application, calibration, multilooking, speckle filtering and terrain correction before use. xView3: analysts "have long struggled" to get identification/classification from SAR. SpaceNet 9 is specifically about cross-modal optical–SAR registration for disasters (alignment itself is a hard problem). During the 2026 Iran blackout, Sentinel-1 SAR became a main free fallback (Bellingcat damage mapping; CJR).
- **How they're trying to solve it:** Analysis-ready SAR (CEOS-ARD NRB; ASF RTC; OPERA); SAR-to-optical translation models; vendor-produced derived products (Ursa, ICEYE flood/damage products — see Part A); Bellingcat's open Sentinel-1 damage tool; NISAR free L-band.
- **Data:** Sentinel-1 GRD/RTC, NISAR, Umbra/Capella open SAR, xView3-SAR, SpaceNet 6 (multi-sensor all-weather), SpaceNet 9.
- **Off-the-shelf tech:** HyP3, SNAP, ISCE, Google Earth Engine S1 collections, SAR ship detectors, SAR→optical GANs/diffusion.
- **Hackathon angle:** "Explain this radar image": user drops a Sentinel-1 or Umbra chip → tool returns a plain-language reading ("bright dots on dark water = likely ships; dark smooth patch = possible oil slick or calm wind") with a paired optical reference from the nearest clear Sentinel-2 date, and flags geometric artefacts. Bridges the "free but unusable" gap.
- **Credibility:** Official (NASA Earthdata, xView3, SpaceNet), reputable press (CJR).
- **Sources:**
  - [SAR basics — NASA Earthdata](https://www.earthdata.nasa.gov/learn/earth-observation-data-basics/sar)
  - [xView3 (accessed 24 Oct 2026)](https://iuu.xview.us/)
  - [SpaceNet (accessed 24 Oct 2026)](https://spacenet.ai/)
  - [Blind Spots — CJR (11 May 2026)](https://cjr.org/feature/blind-spots-satellite-osint-open-source-middle-east-iran-blackout-planet-labs-vantor-maxar.php)

---

### Theme 17 — Latency: time from collection to insight

- **What it is:** For disasters, maritime security and conflict, value decays in hours. Total latency = tasking + collection wait + downlink + processing + analysis + delivery to a human who acts.
- **Problems / pain points:** HLS latency is 2–3 days, with low-latency HLS only "anticipated to be completed in 2027"; GFW radar alerts up to 12 days; FIRMS global active-fire data "within 3 hours of satellite observation" (real-time only for USA & Canada); vendors market speed without metrics — BlackSky: "Tasked in minutes, delivered with urgency", "Satellites collect and return your data in near real time", up to 15 time-diverse images per day (no delivery-time figure published). Fast onboard AI also propagates errors faster (Polyakov blog).
- **How they're trying to solve it:** Onboard processing (ESA Φsat-2, launched 16 Aug 2024, with cloud detection, vessel detection, map generation, compression apps); orbital compute (Starcloud raised $170M Series A at reported $1.1B valuation; TerraWatch: "EO workloads are now the anchor demand getting orbital compute infrastructure off the ground", 13 Apr 2026 — cross-slice); NRT product lines (NASA LANCE/FIRMS, Copernicus NRT); ground-station-as-a-service; automated tip-and-cue (Theme 3).
- **Data:** FIRMS NRT fire data (free), Sentinel-1/2 NRT, GOES/Himawari geostationary (minutes), VIIRS.
- **Off-the-shelf tech:** FIRMS API, NOAA GOES on AWS, event-driven pipelines on STAC (new-item notifications).
- **Hackathon angle:** "Latency dashboard for a disaster": for a live event, show for each free source when the next/last observation is/was, measured actual latency, and what was seen — so a responder knows what the freshest trustworthy picture is. Simple, visual, real-time.
- **Credibility:** Official (NASA FIRMS, NASA HLS, ESA), company marketing (BlackSky), analyst newsletter (TerraWatch), blog (Polyakov).
- **Sources:**
  - [NASA FIRMS (accessed 24 Oct 2026)](https://firms.modaps.eosdis.nasa.gov/)
  - [HLS — NASA Earthdata (updated 21 Oct 2026)](https://www.earthdata.nasa.gov/data/projects/hls)
  - [BlackSky homepage (accessed 24 Oct 2026)](http://blacksky.com/)
  - [Φsat-2 — ESA](https://www.esa.int/Applications/Observing_the_Earth/Phsat-2)
  - [TerraWatch EO Essentials (13 Apr 2026)](https://newsletter.terrawatchspace.com/earth-observation-essentials-april-13-2026/)
  - [GFW/GNW integrated alerts (updated 13 Jan 2026)](https://globalnaturewatch.org/blog/data-and-tools/integrated-deforestation-alerts/)

---

### Theme 18 — Access control, "shutter control" and imagery blackouts (added: emerged during research)

- **What it is:** Commercial imagery is not a neutral utility: providers can delay or withhold imagery of conflict zones at government request. In 2026 this cut journalists, NGOs and researchers off exactly when verification mattered most, and opened the field to fakes and to non-US (incl. Chinese) imagery.
- **Problems / pain points:**
  - Timeline (CJR, 11 May 2026): 6 Mar 2026 Planet imposed a 4-day hold on new imagery over the Gulf States, Iraq, Kuwait; 11 Mar extended to 14 days and to all of Iran and nearby allied bases; **4 Apr made indefinite**, retroactive to 8–9 Mar, citing that "the U.S. government has requested all satellite imagery providers voluntarily implement an indefinite withhold of imagery." Release only case-by-case for "urgent, mission-critical requirements or in the public interest." Vantor (ex-Maxar) said it "may implement enhanced access controls."
  - Impact quotes (CJR): "We're effectively being asked to trust state claims at the moment we should be testing them"; Airwars: "access to expensive commercial satellite imagery is becoming a prerequisite for open-source investigators"; James Martin Center's Sam Lair: "A two-week delay solves the targeting problem. I'm not sure that the indefinite hold does." Bellingcat lost track of moving targets such as grain-smuggling ships.
  - Planet had delayed imagery before, e.g., over Gaza in 2023 (per search summaries of the April 2026 coverage). TerraWatch's 13 Apr 2026 issue flagged BBC reporting that humanitarian organisations and journalists were concerned about Planet's restricted access (per that issue).
- **How people worked around it:** Copernicus Sentinel-1 SAR and Sentinel-2/3 optical (tankers near Kharg Island, suspected oil spill; Bellingcat Sentinel-1 damage mapping); buying non-US imagery via resellers (Soar, SI Imaging Services, UP42); Airbus imagery at "a few hundred dollars per image"; smoke modelling with Meteosat, Sentinel-3 and NASA Worldview; the Washington Post verified Iran's own released satellite images against older Planet and Copernicus data (damage at 15 US sites); Chinese provider MizarVision published images of US military activity; the US sanctioned three Chinese firms for supplying imagery to Iran (CJR).
- **Data:** Sentinel-1 GRD/SLC, Sentinel-2 L2A, Sentinel-3 OLCI/SLSTR, Meteosat, NASA Worldview/GIBS, VIIRS active fires/night lights (FIRMS, Black Marble).
- **Off-the-shelf tech:** Bellingcat/UCL **Gaza Damage Proxy Map** (Ollie Ballinger, 15 Nov 2023): free Google Earth Engine app adapted from a Ukraine tool; measures change in Sentinel-1 radar reflection intensity before/after a date "adjusted for signal noise", intersects with Microsoft building footprints and LandScan population; precision 70.1% across all coloured areas but "95.4% of areas red and darker are actually damaged"; it "detects any significant changes" (e.g., tents on open land also register), and "older damage will be more confidently detected than newer damage"; updates 1–2×/week. Underlying open-source method: Dietrich et al., ETH Zurich/UZH/ICRC, "An Open-Source Tool for Mapping War Destruction at Scale in Ukraine using Sentinel-1 Time Series" (arXiv 2406.02506, Jun 2024, rev. Feb 2025) — building-level probabilistic damage on GEE with a Ukraine Damage Explorer and Rapid Damage Mapping Tool. Also: Racek et al. (PNAS Nexus) Sentinel-1 coherence-based destruction mapping validated on Beirut, Mariupol, Gaza (search snippet). openEO / Copernicus Data Space Ecosystem APIs.
- **Hackathon angle:** "Free-data OSINT kit for when commercial imagery goes dark": given an event location/time, auto-assemble the best free evidence stack (Sentinel-1 change, Sentinel-2 before/after, FIRMS thermal anomalies, VIIRS night-light drop) into a verification brief. Pairs naturally with Theme 14's claim checker.
- **Credibility:** Reputable press (CJR, Al Jazeera, Al-Monitor/AFP, Anadolu, Dawn/Arab News wires, TheWrap).
- **Sources:**
  - [Blind Spots — Columbia Journalism Review, Alex Pasternack (11 May 2026)](https://cjr.org/feature/blind-spots-satellite-osint-open-source-middle-east-iran-blackout-planet-labs-vantor-maxar.php)
  - [US satellite firm Planet Labs announces blackout on war on Iran images — Al Jazeera (5 Apr 2026)](https://aljazeera.com/news/2026/4/5/us-satellite-firm-planet-labs-announces-blackout-on-war-on-iran-images)
  - [Satellite firm Planet Labs to indefinitely withhold Iran war images — Al-Monitor (Apr 2026; not opened)](https://www.al-monitor.com/originals/2026/04/satellite-firm-planet-labs-indefinitely-withhold-iran-war-images)
  - [Satellite company halts distribution of images that help press cover Iran war — TheWrap (Apr 2026; not opened)](https://www.thewrap.com/media-platforms/journalism/satellite-company-restricts-images-press-cover-iran-war-government-request/)
  - [Access to satellite imagery restricted amid Iran war — Anadolu (2026; not opened)](https://aa.com.tr/en/world/access-to-satellite-imagery-restricted-amid-iran-war-report/3866406)
  - [US satellite imagery firm announces blackout on Middle East war pics — Arab News (Apr 2026; not opened)](https://www.arabnews.com/node/2638797/world)
  - [TerraWatch Earth Observation Essentials (13 Apr 2026)](https://newsletter.terrawatchspace.com/earth-observation-essentials-april-13-2026/)
  - [A New Tool Allows Researchers to Track Damage in Gaza — Bellingcat, Ollie Ballinger (15 Nov 2023)](https://bellingcat.com/resources/2023/11/15/a-new-tool-allows-researchers-to-track-damage-in-gaza)
  - [An Open-Source Tool for Mapping War Destruction at Scale in Ukraine using Sentinel-1 Time Series — arXiv 2406.02506 (Jun 2024; v3 Feb 2025)](https://arxiv.org/abs/2406.02506)
  - [New AI tool uses free satellite data to reveal warzone destruction in near real time — The Debrief (search snippet; not opened)](https://thedebrief.org/new-ai-tool-uses-free-satellite-data-to-reveal-warzone-destruction-in-near-real-time/)
  - [Freely available tool to document wartime destruction — phys.org (Dec 2025; search snippet via aggregator; not opened)](https://scour.ing/@matmat/p/https://phys.org/news/2025-12-freely-tool-document-wartime-destruction.html)

---

## Problem bank

Every distinct problem found, one line each: **problem → who has it → data that could address it → source**. Near-duplicates found by different parts of the research were merged; numbering is continuous across groups.

### Market structure, demand and business models

1. Commercial EO demand is concentrated in government (70–80% of revenue), and commercial verticals are flat → EO companies and investors → none directly (market problem); build for a named enterprise buyer → [TerraWatch 17 Dec 2025](https://newsletter.terrawatchspace.com/earth-observation-essentials-december-17-2025/), [New Space Economy 23 Oct 2026](https://newspaceeconomy.ca/2026/10/23/why-does-defense-dominate-earth-observation-demand-over-commercial-markets/)
2. "No genuinely new commercial EO use cases are forming", and the job is converting capability into repeat purchases → EO startups → Sentinel/Landsat plus enterprise data → [TerraWatch 13 Apr 2026](https://newsletter.terrawatchspace.com/earth-observation-essentials-april-13-2026/)
3. Most EO pilots never reach rollout. Winners have binary outputs, costly alternatives and a single national buyer → pipeline and utility operators → Sentinel-2/1 along corridors → [TerraWatch 11 May 2026](https://newsletter.terrawatchspace.com/earth-observation-essentials-may-11-2026/)
4. Buyers want answers/decisions, vendors sell pixels or layers → insurers, agribusiness, supply-chain teams → any public stack + customer asset lists → [Morrison, 18 Apr 2022](https://joemorrison.substack.com/p/nobody-wants-your-fancy-algorithm)
5. Enterprises want "automated risk scores or work orders, not raw imagery"; defence-shaped architecture and licensing block commercial scale → EO companies, enterprise buyers → n/a (market structure) → [New Space Economy, 23 Oct 2026](https://newspaceeconomy.ca/2026/10/23/why-does-defense-dominate-earth-observation-demand-over-commercial-markets/)
6. Defence-style security licences block "license once, embed everywhere" software models → SaaS platforms embedding EO → n/a → [New Space Economy, 23 Oct 2026](https://newspaceeconomy.ca/2026/10/23/why-does-defense-dominate-earth-observation-demand-over-commercial-markets/)
7. Platforms and marketplaces struggle to differentiate "beyond selling access to pixels" → UP42, SkyWatch, SkyFi, Arlula → multi-provider STAC catalogues → [TerraWatch 22 Oct 2025](https://newsletter.terrawatchspace.com/state-of-commercial-earth-observation-2025-edition/), [Morrison Nov 2020](https://joemorrison.substack.com/p/stop-building-satellite-imagery-platforms)
8. Marketplaces depend on suppliers who can cut them off ("if someone at one of the major imagery providers decides you're done…you're done") → marketplaces/platforms → open data as the only un-revocable supply → [Morrison, 12 Nov 2020](https://joemorrison.substack.com/p/stop-building-satellite-imagery-platforms)
9. Buyer-facing marketplaces pivot to supplier back-office software (Arlula Geostack, SkyWatch CONNECT) → marketplaces → n/a (market evidence) → [arlula.com](https://www.arlula.com/)
10. Horizontal marketplaces/platforms keep failing or being sold (TerraServer, Gro, Orbital Insight, Descartes Labs, UP42 sale, SkyWatch/Arlula pivots) → EO startups, investors → n/a → [AgFunderNews, 31 May 2024](https://agfundernews.com/breaking-ag-insights-platform-gro-intelligence-is-closing-down)
11. Satellite "macro" alt-data for investors faded; analytics firms pivot to defence (SpaceKnow, Orbital Insight → Privateer maritime/defence) → analytics startups → n/a → [spaceknow.com](https://www.spaceknow.com/), [privateer.com](https://www.privateer.com/)
12. Standalone climate and EO analytics firms can't stay independent (Kayrros, Pachama, Sust Global and Cape acquired; Gro shut; Cervest insolvent) → founders, investors → n/a (business-model evidence) → [Energy Aspects](https://www.energyaspects.com/resources/insights/energy-aspects-to-acquire-satellite-data-and-analytics-company-kayrros), [TechCabal](https://techcabal.com/2024/06/02/kenya-data-analytics-gro-intelligence-shuts-down/)
13. Satellite-AIS as a standalone data business didn't survive (Spire Maritime sold to Kpler for ~$241M) → data operators → n/a → [Kpler, 25 Apr 2025](https://kpler.com/blog/kpler-completes-acquisition-of-spire-maritime-strengthening-maritime-intelligence-capabilities)
14. Generic hosted "AI-native GIS" isn't a sustainable product (Mundi cloud shut) → AI-GIS startups → n/a (lesson: go vertical) → [mundi.ai](https://mundi.ai/)
15. Government-dependent EO revenue is volatile (shutdowns, budget "surges and valleys") → EO operators → n/a → [Via Satellite 18 Dec 2025](https://www.satellitetoday.com/finance/2025/12/18/government-shutdown-and-maritime-divestment-impact-spire-in-q3-results/), [USGIF 20 May 2025](https://usgif.org/geoint-symposium-2025-day-one-recap/)
16. EO vendors' revenue over-concentrated in the US government (Vantor and others; EOCL recompete risk) → Vantor, BlackSky, Planet, investors → n/a (market problem) → [TerraWatch, 22 May 2026](https://newsletter.terrawatchspace.com/three-years-on-analysing-advents-maxar-acquisition/)
17. Nature-credit ratings demand is weak, so raters pivot to compliance markets and EACs → Sylvera, Renoster → n/a → [Sylvera](https://www.sylvera.com/), [Carbon Pulse](https://carbon-pulse.com/436628/)
18. Hyperspectral lacks an open seed mission and a processing stack → hyperspectral startups, mineral and ag users → EnMAP, PRISMA, EMIT (open) → [TerraWatch 8 Jun 2026](https://newsletter.terrawatchspace.com/earth-observation-essentials-june-8-2026/)
19. NASA/USGS want to buy multi-sensor *products* (burned area, surface water, bathymetry, ET) that must be cross-calibrated with a 54-year archive → would-be Landsat product vendors → HLS, Landsat, Sentinel-2 → [TerraWatch 24 Aug 2026](https://newsletter.terrawatchspace.com/earth-observation-essentials-august-24-2026/)
20. Midstream distribution is neglected, with pixels duplicated across buckets and weak lineage → sovereign data custodians → STAC, compute-to-data → [Strategic Geospatial 7 Sep 2026](https://www.strategicgeospatial.com/p/the-missing-midstream), [21 Oct 2026](https://www.strategicgeospatial.com/p/so-mid-so-sovereign)

### Procurement, pricing and tasking

21. Imagery buying is opaque ("Data pricing is still very much a dark art"), and quote-based sales feel like a "hostage negotiation" → enterprise buyers, startups, researchers → published price lists (Umbra, SkyFi, Arlula) → [Via Satellite 26 Jun 2026](https://www.satellitetoday.com/imagery-and-sensing/2026/06/26/commercial-markets-are-ready-for-eo-but-the-understanding-gap-persists/), [Morrison 2020](https://joemorrison.substack.com/p/the-commercial-satellite-imagery)
22. Buying/tasking imagery is slow, licence-bound, per-provider → SMEs, researchers, journalists → open STAC catalogues, vendor APIs → [Morrison, 7 Aug 2020](https://joemorrison.substack.com/p/the-commercial-satellite-imagery)
23. Prices are opaque ("contact sales"), minimums vary; few public list prices → small buyers, students, NGOs → Umbra list prices, EOS/SkyFi published starting prices → [Umbra pricing](https://umbra.space/pricing)
24. Buyer pain moved "from cost and data quality … to the buying process itself" (budget approval, unclear pricing, licensing) → enterprise EO buyers → a price/licence comparison + "is free data enough?" tool → [UP42 survey, 31 Jul 2026](https://up42.com/blog/state-of-earth-observation-in-2026)
25. Tasking can be rejected "for capacity, lead time, geometry, restrictions, or competing priorities"; "Even a feasible request doesn't always result in a successful acquisition" → anyone tasking satellites → CelesTrak TLEs + cloud forecasts for a feasibility predictor → [UP42, 10 Sep 2026](https://up42.com/blog/buy-eo-through-platform-directly-part-1)
26. Tasking interfaces are fragmented (REST vs SOAP vs "email and shapefiles"; delivery via FTP or links "sent days later"; capabilities "buried in PDFs") and break agents → integrators, AI agents → STAPI spec + TLEs → [Element 84, 26 Feb 2026](https://element84.com/software-engineering/if-ai-is-going-to-task-satellites-we-need-standards/)

### Access restrictions, blackouts, sovereignty and disappearing free data

27. Commercial imagery withheld/delayed in wars at government request → journalists, NGOs, human-rights investigators → Sentinel-1/2/3, FIRMS, VIIRS night lights, Meteosat → [CJR, 11 May 2026](https://cjr.org/feature/blind-spots-satellite-osint-open-source-middle-east-iran-blackout-planet-labs-vantor-maxar.php)
28. Commercial and even Sentinel imagery can be withheld for geopolitical reasons ("shutter control") → journalists, NGOs, insurers → CDSE/STAC catalogue latency metadata → [TerraWatch 11 Aug 2026](https://newsletter.terrawatchspace.com/earth-observation-essentials-august-11-2026/), [TerraWatch 14 Sep 2026](https://newsletter.terrawatchspace.com/can-a-global-earth-observation-accord-work-even-if-it-is-not-global/)
29. "Who can switch this off?": supplier and switch-off risk for imagery and space services → Ukraine, Gulf and European governments → provider-availability tracking, open-data fallbacks → [Via Satellite op-ed, 22 Oct 2026](https://www.satellitetoday.com/opinion/2026/10/22/the-question-gulf-buyers-are-now-asking-who-can-switch-this-off/)
30. National dependence on a single foreign imagery pipe (the Ukraine cutoff, March 2025) → Ukraine, NATO allies → open data plus European SAR; a revisit-gap calculator → [Breaking Defense 2025 review](https://breakingdefense.com/2025/12/five-stories-that-surprised-the-space-world-2025-review/)
31. Investigators increasingly need to pay for commercial imagery ("a prerequisite for open-source investigators") → small newsrooms, NGOs → free Sentinel stack as substitute → [CJR, 11 May 2026](https://cjr.org/feature/blind-spots-satellite-osint-open-source-middle-east-iran-blackout-planet-labs-vantor-maxar.php)
32. Geography-specific resolution limits (Kyl–Bingaman; Israel and the Palestinian territories) → OSINT, humanitarian monitors → Sentinel-2, non-US providers → [Wikipedia: Kyl–Bingaman](https://en.wikipedia.org/wiki/Kyl%E2%80%93Bingaman_Amendment)
33. Free Planet NICFI tropical imagery ended 1 Apr 2025; return limited to Amazon disturbance-alert areas until May 2027 → forest NGOs, indigenous monitors, journalists outside the Amazon → Sentinel-2 (10 m), Sentinel-1, Landsat; super-resolution → [GNW, 8 Oct 2026](https://globalnaturewatch.org/blog/data-and-tools/planet-imagery-changes-gfw/)
34. Free public-data tools disappear after acquisitions (Sentinel Hub EO Browser "has been deprecated", users pushed to Planet Insights Platform or Copernicus Browser) → students, NGOs, journalists → Copernicus Browser / CDSE, Earth Search STAC → [EO Browser notice](https://apps.sentinel-hub.com/eo-browser/)
35. Free public-good EO lacks durable funding: NICFI cancelled (Sep 2025), MethaneSAT lost (2025), Landsat cut to one satellite and FY27 −52% Earth science → NGOs, tropical forest monitors → Sentinel-2, embeddings → [Spectral Reflectance 16 Mar 2026](https://www.spectralreflectance.space/p/the-economics-of-openness-funding), [TerraWatch 13 Apr 2026](https://newsletter.terrawatchspace.com/earth-observation-essentials-april-13-2026/)

### Imagery-to-insight gap and the last mile to non-experts

36. Generic derived-data feeds don't match each customer's definition of "change" → analytics firms and their buyers → configurable change detection on Sentinel-1/2 time series → [Morrison, 18 Apr 2022](https://joemorrison.substack.com/p/nobody-wants-your-fancy-algorithm)
37. Last mile: field staff "barely want to see the data" and want to know where to go → utilities, water managers → Sentinel-1/2 anomalies to dispatch lists → [Via Satellite 26 Jun 2026](https://www.satellitetoday.com/imagery-and-sensing/2026/06/26/commercial-markets-are-ready-for-eo-but-the-understanding-gap-persists/)
38. NASA's >100 PB of Earth data needs technical expertise to navigate; Earth Copilot stayed internal → public, journalists, local governments → NASA CMR/Earthdata, VEDA STAC → [Microsoft/NASA, 14 Nov 2024](https://blogs.microsoft.com/public-sector/2024/11/14/from-questions-to-discoveries-nasas-new-earth-copilot-brings-microsoft-ai-capabilities-to-democratize-access-to-complex-data/)
39. Geospatial data is "notoriously complex and siloed" inside enterprises → enterprises with drone/satellite/sensor data → Planetary Computer-style STAC catalogues → [Azure blog, 17 Jun 2025](https://azure.microsoft.com/en-us/blog/microsoft-planetary-computer-pro-unlocking-ai-powered-geospatial-insights-for-enterprises-across-industries/)
40. Non-analysts must queue requests to scarce GEOINT analysts → defence/intel and insurance users → natural-language search over STAC + news + AIS → [danti.ai](https://www.danti.ai/)
41. Multi-layer questions (hazard × population × infrastructure) need analysts to stitch datasets; Google's Earth AI agent is gated to trusted testers → NGOs, humanitarian responders → AlphaEarth embeddings, flood forecasts, WorldPop/Populace, OSM → [Google Research, 23 Oct 2025](https://www.research.google/blog/google-earth-ai-unlocking-geospatial-insights-with-foundation-models-and-cross-modal-reasoning/)
42. Embedding and EO literacy gap: "many potential users remain unfamiliar with what embeddings are" → enterprise and NGO users → AlphaEarth on Earth Engine → [CNG 29 Jul 2026](https://cloudnativegeo.org/blog/2026/07/announcing-geo-embedding-sprint-zurich/)
43. AI automating feature extraction shrinks GIS roles, so job descriptions are outdated → the GIS workforce → n/a → [Geo Week session](https://www.geo-week.com/session/how-ai-is-rewriting-geospatial-demand/)
44. Shortage of remote-sensing specialists for nature and TNFD assessments → corporates, banks, consultancies → WDPA, KBA, Aqueduct, Hansen → [Earth Blox](https://www.earthblox.io/)

### Too much data, triage, tip-and-cue and latency

45. Imagery volume outruns human review; most scenes never get expert eyes → NGA/NRO analysts, commercial SAR operators, OSINT teams → Sentinel-1/2, Umbra/Capella open SAR, Maxar Open Data → [Federal News Network 2018](https://federalnewsnetwork.com/big-data/2018/09/nga-looks-to-stay-ahead-of-sheer-volume-of-satellite-imagery-data/)
46. Detections outpace analyst validation ("far more detections than analysts can validate") → NGA and defence analysts → Sentinel-1 ship detections, xView3, GFW → [USGIF 10 Aug 2026](https://usgif.org/mission-focus-ai-first-approaches/)
47. "Speed, not depth": minutes-level unclassified ISR briefs → Space Force TacSRT, combatant commands → freshest free imagery plus an auto-brief → [Breaking Defense, 21 May 2025](https://breakingdefense.com/2025/05/nga-space-force-ink-accord-on-responsibilities-for-buying-commercial-isr/)
48. Collection-to-insight latency is unmeasured/unpublished by vendors; free products range 3 h (FIRMS) to 2–3 days (HLS) to 12 days (RADD) → responders → FIRMS, GOES/Himawari, Sentinel NRT → [NASA FIRMS](https://firms.modaps.eosdis.nasa.gov/)
49. Downlink and latency limit value ("People don't pay for resolution, they pay for immediacy") → time-sensitive users → TLEs and ground-station pass data → [HN 34207926](https://news.ycombinator.com/item?id=34207926), [Morrison Dec 2022](https://joemorrison.substack.com/p/how-internet-in-space-will-transform)
50. Crisis imagery arrives too late to help → humanitarian responders → Sentinel-1/2, Copernicus EMS, NASA Lifelines → [SatSummit agenda](https://satsummit.io/2026-st-louis/agenda/), [Novaspace 21 Oct 2026](https://nova.space/in-the-loop/from-satellite-data-to-disaster-resilience-turning-information-into-action/)
51. Low-latency harmonised optical (HLS) not available until 2027 → disaster responders, agriculture → HLS, Sentinel-2 NRT → [NASA HLS page](https://www.earthdata.nasa.gov/data/projects/hls)
52. Tip-and-cue loops across sensors/providers are manual; many cues have no feasible imaging window → maritime security, defence, fisheries enforcement → AIS (NOAA, GFW), Sentinel-1, CelesTrak TLEs → [arXiv 2512.09670, Dec 2025](https://arxiv.org/html/2512.09670v1)
53. Tip-and-cue orchestration: turning a cheap wide-area tip into a timely high-resolution look → TacSRT, NRO, BlackSky and Vantor users → FIRMS, AIS gaps, Sentinel-1 as tips; tasking APIs as cues → [Breaking Defense, 21 May 2025](https://breakingdefense.com/2025/05/nga-space-force-ink-accord-on-responsibilities-for-buying-commercial-isr/)
54. High-res "soda straw" tasking only after an alarm; adversaries time activity around predictable passes → defence, maritime security → wide-area daily monitoring tipping high-res → [Planet, 29 Sep 2026](https://www.planet.com/pulse/beyond-the-soda-straw-why-modern-defense-needs-continual-geoint/)
55. Intelligence products are still long-form PDFs and need to be machine-readable for C2 → NGA → n/a → [USGIF 10 Sep 2026](https://usgif.org/geointeraction-tuesday-its-about-automation-not-ai/)

### Data readiness and quality: ARD, interoperability, clouds, change-detection false positives

56. Data preparation (ARD) consumes most analyst effort; users lack expertise/bandwidth → scientists, NGOs, developing-country agencies → HLS, Sentinel-2 L2A, Sentinel-1 RTC → [CEOS-ARD](https://ceos.org/ard/)
57. Data is not "AI-ready", and conditioning data matters more than volume → NGA, DIA, enterprise AI teams → ARD (HLS, CEOS-ARD) → [USGIF 10 Aug 2026](https://usgif.org/mission-focus-ai-first-approaches/)
58. Cross-sensor calibration drift and time-series gaps break operational AI ("Durability is the real constraint") → EO analytics and ML teams → Landsat/Sentinel-2/HLS → [Via Satellite op-ed 8 May 2026](https://www.satellitetoday.com/opinion/2026/05/08/operational-ai-is-hitting-the-limits-of-earth-observation-data/)
59. Each new dataset needs a new pipeline; metadata conventions diverge → developers, platforms → STAC catalogues (Earth Search, Planetary Computer, CDSE) → [stacspec.org](https://stacspec.org/en)
60. Cloud-native tooling is "a pile of mostly inaccessible technologies with lots of sharp edges", and badly chunked data is slow → data engineers, scientists → Zarr/COG/GeoParquet → [Element 84 Radar 2026](https://element84.com/geospatial/geospatial-tech-radar-2026-an-emphasis-on-provenance-and-refined-tooling-from-ai-to-cloud-native/), [Spectral Reflectance 2 Jul 2026](https://www.spectralreflectance.space/p/cng-london-people-who-fight-with)
61. Change-detection alerts are polluted by clouds, shadows, phenology and misregistration; confidence takes days/weeks → forest monitors, EUDR compliance, insurers → GFW integrated alerts, DIST-ALERT, Sentinel-1/2 → [GFW/GNW blog, Jan 2026](https://globalnaturewatch.org/blog/data-and-tools/integrated-deforestation-alerts/)
62. Single-sensor fire detectors false-alarm on industrial heat/solar glint → fire agencies → VIIRS/MODIS FIRMS, Sentinel-2 SWIR → [Polyakov blog, 3 Jul 2026 (blog-tier)](https://maxpolyakov.com/ai-satellite-image-analysis-hallucinations/)
63. Sparse/cloudy revisit makes single-scene change ambiguous ("A nominal eight-day revisit can easily turn into a clear view every month or two") → monitoring users → dense time series, SAR–optical fusion → [Planet, 22 Oct 2026](https://www.planet.com/pulse/why-dense-satellite-time-series-deliver-more-trustworthy-insight/)
64. ~67% of Earth typically cloud-covered; "daily revisit" ≠ daily clear view → disaster responders, agriculture, insurers → Sentinel-1, NISAR, HLS, cloud climatology → [NASA Earth Observatory 2015](https://science.nasa.gov/earth/earth-observatory/cloudy-earth-85843)
65. Imagery capture is unpredictable because of cloud and revisit ("there is no predictability") → farmers, insurers → cloud climatology plus TLE/revisit → [HN 31074177](https://news.ycombinator.com/item?id=31074177)
66. SAR is free and all-weather but hard for non-experts to read (speckle, layover, geometry) → journalists, NGOs, local governments → Sentinel-1, NISAR, Umbra/Capella open data → [NASA Earthdata SAR](https://www.earthdata.nasa.gov/learn/earth-observation-data-basics/sar)
67. Optical–SAR co-registration for disasters is itself unsolved enough to be a challenge (SpaceNet 9) → disaster mappers → SpaceNet 9 data → [spacenet.ai](https://spacenet.ai/)
68. Archive data curation ("cleaned, curated, and correlated") blocks AI on decades of imagery+reports → NGA, large archives → archive imagery + text reports → [Breaking Defense, 28 Aug 2024](https://breakingdefense.com/2024/08/ai-gold-mine-nga-aims-to-exploit-archive-of-satellite-images-expert-analysis/)
69. Satellite leak/methane/vegetation alerts need human verification before release (false-positive cost) → pipeline operators, utilities → multispectral time series + analyst feedback → [satelytics.ai](http://www.satelytics.ai/)

### Labels, ground truth and validation

70. Labelling cost and labelled-data scarcity for CV → NGA Maven ($708M Sequoia to Enabled Intelligence) → human-in-the-loop review UIs that turn confirmations into labels; synthetic data → [Breaking Defense, 26 Nov 2025](https://breakingdefense.com/2025/11/startup-enabled-intelligence-nabs-ngas-708-million-ai-training-contract/)
71. Rare and novel objects with no labels → defence analysts, RAIC users → open EO embeddings, few-shot search → [GovTech/Defense One, 18 Apr 2023](https://www.govtech.com/products/chatgpt-style-tool-for-satellite-photos-already-exists)
72. Synthetic data to cut labelling cost for SAR, IR and rare classes → defence CV teams, SatVu, Orbital Insight → RarePlanes, rendered chips → [Rendered.ai](https://rendered.ai/)
73. Per-target detector training "must often restart as missions change" → analysts → embedding search ("index once, exploit repeatedly") over AlphaEarth/Clay embeddings → [raiclabs.com](https://raiclabs.com/)
74. Labelling cost: labels for medium-resolution imagery can be transferred from near-simultaneous high-resolution captures → ML teams → Sentinel-2 plus NAIP or other high-res → [Planet 19 Mar 2025](https://www.planet.com/pulse/aircraft-detection-at-planetary-scale/)
75. SAR vessel labelling hampered by missing AIS ground truth and need for SAR expertise → fisheries enforcement, coast guards → xView3-SAR, GFW, Sentinel-1 → [xView3](https://iuu.xview.us/)
76. Field-boundary/crop ground truth scarce and geographically biased → ag lenders, insurers, food-security agencies → Fields of The World, Sentinel-2 → [arXiv 2409.16252](https://arxiv.org/abs/2409.16252)
77. Benchmarks and validation biased to North America/Europe → model builders, Global South users → PANGAEA datasets → [arXiv 2412.04204v2](https://arxiv.org/html/2412.04204v2)

### Trust in AI outputs, provenance and fake imagery

78. AI-generated / doctored satellite images spread in conflicts faster than debunks → journalists, fact-checkers, governments, markets → same-day Sentinel-2/Sentinel-1, Google Earth history, synthetic fakes from open diffusion models → [France 24, 16 May 2025](https://observers.france24.com/en/asia-pacific/20250516-india-pakistan-conflict-ai-generated-or-edited-fake-satellite-images-flood-social-media)
79. No accessible verification tool / provenance standard for satellite imagery (C2PA not used for EO; vendor signing rare) → media, OSINT, imagery providers → Sentinel archive as reference; Satellogic signed manifests as model → [ESA Verisat.AI, Aug 2025](https://business.esa.int/projects/verisatai)
80. No provenance standard for EO imagery; edits like cloud removal and super-resolution go unrecorded, and fakes can "flood the zone" → journalists, OSINT, courts → Sentinel/Landsat reference scenes plus STAC metadata → [Strategic Geospatial 31 Jul 2026](https://www.strategicgeospatial.com/p/earth-is-a-banana), [SatSummit agenda](https://satsummit.io/2026-st-louis/agenda/)
81. Provenance of satellite images circulated by foreign OSINT sellers (MizarVision; Planet denies ownership) → militaries, media, vendors → Sentinel-2 archive matching, sun-angle dating → [Breaking Defense, 13 Apr 2026](https://breakingdefense.com/2026/04/nowhere-to-hide-iran-war-spotlights-military-challenges-posed-by-space-based-remote-sensing/)
82. VLMs fail at counting, localisation and change over time on EO imagery (best 41.7%; change detection <20%) → anyone deploying "geospatial copilots" → GEOBench-VLM, VLEO-Bench → [arXiv 2411.19325](https://arxiv.org/html/2411.19325v2)
83. Geospatial foundation models don't reliably beat a UNet → ML teams choosing models → PANGAEA benchmark → [arXiv 2412.04204v2](https://arxiv.org/html/2412.04204v2)
84. LLM/agent geospatial answers are plausibly wrong ("90% right is 100% wrong") → consumers, analysts, agent builders → OSM/Overture plus imagery for verification → [Strategic Geospatial 13 Oct 2026](https://www.strategicgeospatial.com/p/90-right-is-100-wrong-benchmarking)
85. AI agent answers can't be trusted unless every step is checkable ("an answer is only useful if someone can check it"); confidence scores "hard to interpret or unreliable" → users of geospatial copilots → STAC items + code logs as provenance → [Element 84 Tech Radar, Oct 2026](https://element84.com/geospatial/geospatial-tech-radar-2026-an-emphasis-on-provenance-and-refined-tooling-from-ai-to-cloud-native/)
86. AI explainability and verification of imagery analytics ("look inside the black box") → NRO, NGA, targeting cells → any detector output plus evidence pixels and calibrated confidence → [Breaking Defense, 7 May 2026](https://breakingdefense.com/2026/05/ai-explainability-is-a-major-concern-for-national-reconnaissance-office-director/)
87. No common way to accredit or benchmark GEOINT models across vendors → NGA (AGAIM) → open benchmarks (xView, SpaceNet, GEO-Bench) across regions and sensors → [MeriTalk, 4 Sep 2024](https://www.meritalk.com/articles/nga-launches-new-ai-accreditation-pilot/)
88. Provenance of machine-generated intelligence products → NGA ("machine-generated GEOINT" label), consumers of intel → STAC lineage plus C2PA manifests on derived products → [Breaking Defense, 5 Jun 2025](https://breakingdefense.com/2025/06/no-human-hands-nga-circulates-ai-generated-intel-director-says/)
89. Low-quality LLM-generated EO packages ignore nodata, CRS, cloud masking and validation → the EO open-source community → n/a (quality problem) → [Spectral Reflectance 25 May 2026](https://www.spectralreflectance.space/p/the-eo-community-probably-does-not)
90. Advanced multi-step GIS tasks still fail when run autonomously by LLM agents → GIS users → benchmark tasks from GIS Copilot paper → [IJDE 2025](https://www.tandfonline.com/doi/full/10.1080/17538947.2025.2497489)
91. Embeddings from different foundation models are not comparable or interoperable, and fitness-for-use is unclear → embedding users, CNG community → AlphaEarth, TESSERA, LGND and Earth Genome embeddings → [CNG 29 Jul 2026](https://cloudnativegeo.org/blog/2026/07/announcing-geo-embedding-sprint-zurich/), [TerraWatch 28 Sep 2026](https://newsletter.terrawatchspace.com/earth-observation-essentials-september-28-2026/)
92. Google Custom Satellite Embeddings commoditise pixel-to-insight analytics, leaving "labelled ground truth, validation against field data, and accountability for the answer" as the moat → downstream analytics firms → AlphaEarth plus field data → [TerraWatch 12 Oct 2026](https://newsletter.terrawatchspace.com/earth-observation-essentials-october-12-2026/)
93. Imagery as evidence: what makes it credible in court, journalism and human rights work → journalists, NGOs → Sentinel, Planet, Maxar Open Data → [SatSummit agenda](https://satsummit.io/2026-st-louis/agenda/)
94. Defensible geospatial data in the AI age: method and measurement documentation → engineering, legal → n/a → [Geo Week session](https://www.geo-week.com/session/from-point-cloud-to-proof-a-general-counsels-guide-to-defensible-geospatial-data-in-the-age-of-ai/)

### Maritime: dark vessels, AIS spoofing, sanctions, pollution

95. ~75% of industrial fishing vessels and >25% of transport/energy vessel activity are not publicly tracked → coastal states, fisheries enforcement, NGOs → Sentinel-1/2 detections (Skylight, GFW) + AIS → [GFW, 3 Jan 2024](https://globalfishingwatch.org/press-release/new-research-harnesses-ai-and-satellite-imagery-to-reveal-the-expanding-footprint-of-human-activity-at-sea/)
96. AIS evidence is compromised by GNSS jamming (124,235 vessels affected in Q3 2026; >3.35M false ship-to-ship meetings) and dark convoys (52% of Hormuz traffic in Sep 2026) → marine insurers, claims teams, courts → Sentinel-1 SAR vs AIS reconciliation → [Windward, 20 Oct 2026](https://windward.ai/blog/how-marine-insurers-are-closing-the-evidence-gap/)
97. AIS spoofing, identity fraud and ship-to-ship transfers (sanctions evasion) → NGA, Treasury, insurers, banks → AIS plus Sentinel-1 detections → [SynMax Theia](https://www.synmax.com/theia)
98. The shadow fleet can't be counted: "there is no register and each organization counts a different set of vessels"; 62% of Iran-trade tankers falsely flagged → sanctions authorities, insurers, ports → SAR detections + AIS + registry data → [Windward, 1 Oct 2026](https://windward.ai/blog/what-is-the-shadow-fleet-and-why-is-it-so-hard-to-count/)
99. Loitering over subsea cables (sabotage risk) → navies, cable operators, insurers → AIS, Sentinel-1, cable route maps → [Windward](https://windward.ai/)
100. Maritime "detect-to-act" gap: data fusion across AIS, RF, SAR, EO and OSINT, blocked by classification and legacy systems → USCG, navies → GFW, Sentinel-1 → [USGIF 1 Jul 2026](https://usgif.org/turning-maritime-awareness-into-decision-advantage/)
101. Illegal oil discharges go unattributed → coastal communities, prosecutors, NGOs → Sentinel-1 slicks (Cerulean) + AIS tracks → [SkyTruth Cerulean](https://skytruth.org/cerulean/)

### Conflict, damage assessment and human rights

102. False positives in SAR change-based damage proxies (agriculture, construction, moisture) → PWTT users → Sentinel-1/2 time series plus land-cover maps → [Bellingcat, 7 Apr 2026](https://www.bellingcat.com/resources/2026/04/07/tool-damage-assessment-destruction-sentinel-satellite-imagery-iran-us-gulf/)
103. Free Sentinel-1 war-damage proxies over-detect (any change counts; 70.1% overall precision) and lag for recent damage → OSINT, humanitarian orgs → Sentinel-1, Microsoft building footprints, LandScan → [Bellingcat, 15 Nov 2023](https://bellingcat.com/resources/2023/11/15/a-new-tool-allows-researchers-to-track-damage-in-gaza)
104. Free SAR damage proxies miss small and vertical damage and need corroboration; updates only 1–2×/week → OSINT, humanitarian orgs → Sentinel-1 + Sentinel-2 + geolocated media → [Bellingcat, 7 Apr 2026](https://www.bellingcat.com/resources/2026/04/07/tool-damage-assessment-destruction-sentinel-satellite-imagery-iran-us-gulf/)
105. Damage maps from different providers disagree (15% vs 52% of buildings) → HOT, responders, insurers → Sentinel-1, Microsoft/OSU assessments, OSM → [HOT, 6 Aug 2026](https://hotosm.org/en/news/why-damage-assessments-can-vary-from-image-pixels-to-microwaves/)
106. Verifying arson and burned villages at scale (atrocity documentation) → CIR, human-rights investigators → FIRMS, Sentinel-2 dNBR, Open Buildings → [BigData Republic, 24 Sep 2025](https://bigdatarepublic.nl/articles/detecting-war-crimes-from-space/)
107. Missed detections under camouflage and low visibility (Avengers detects about 70%) → Ukraine MoD → n/a publicly. Synthetic camouflage data is an option (Rendered.ai and Kallisto) → [MoD Ukraine, 13 May 2025](https://mod.gov.ua/en/news/enemy-equipment-detected-in-2-seconds-the-ministry-of-defence-showcased-delta-and-avengers-systems-at-the-london-defence-conference)

### Methane and emissions accountability

108. Satellite methane alerts mostly go unanswered (about 90%) → UNEP IMEO, regulators, NGOs, operators → Carbon Mapper plumes, TROPOMI, OSM/OGIM infrastructure → [UNEP Oct 2025](https://www.unep.org/news-and-stories/press-release/better-data-driving-action-methane-emissions-more-work-needed)
109. Methane plumes are detected but only about a third are attributable to an operator → regulators, journalists → Carbon Mapper plus well and facility registries → [TerraWatch 28 Sep 2026](https://newsletter.terrawatchspace.com/earth-observation-essentials-september-28-2026/)
110. Coverage gap after the loss of MethaneSAT (no basin-scale quantification; no replacement announced) → EDF, regulators, researchers → TROPOMI L2 CH4, archived MethaneSAT data → [EDF](https://www.edf.org/media/methanesat-loses-contact-satellite)
111. Asset-level emissions estimates published monthly without visible independent validation → policymakers, investors → Sentinel-5P NO₂, VIIRS, Sentinel-2 activity signals as cross-checks → [Climate TRACE news](https://climatetrace.org/news)

### Forests, deforestation, EUDR and carbon markets

112. Users confuse tree cover loss with deforestation; definitions differ (PRODES ≥6.25 ha Aug–Jul vs UMD ≥0.09 ha calendar year; fire) → EUDR operators, journalists, governments → UMD loss + drivers data + JRC TMF + PRODES → [GNW, 29 Apr 2026](https://globalnaturewatch.org/blog/data-and-tools/2025-tree-cover-loss-data-explained/)
113. EUDR compliance by 30 Dec 2026 for large operators: plot geolocation, 2020 forest baseline, false positives in agroforestry → cocoa, coffee, palm, rubber and soy exporters and EU importers → Hansen GFC, JRC GFC2020 / TMF, RADD / GLAD alerts, Sentinel-1/2 → [LiveEO EUDR delay](https://www.live-eo.com/blog/eudr-delay)
114. "Defensible" EUDR evidence that national competent authorities will accept → operators → audit trails with timestamped imagery → [Satelligence](https://www.satelligence.com/)
115. Over-crediting of REDD+ (about 94% of Verra rainforest credits questioned) → offset buyers (Microsoft and others), ratings agencies → Hansen GFC, JRC TMF, Verra project polygons, synthetic controls → [Wikipedia: Verra (organization)](https://en.wikipedia.org/wiki/Verra_(organization))
116. Buffer pools and integrity labels are failing (Renoster review of 500M credits) → buyers, registries, ICVCM → MODIS burned area, Hansen loss inside project polygons → [Carbon Pulse](https://carbon-pulse.com/431395/)
117. Biomass and carbon maps from different providers disagree → buyers, Chloris, Space Intelligence, BeZero → ESA CCI Biomass, GEDI L4B, CTrees Land Carbon Map → [Space Intelligence](https://www.space-intelligence.com/)
118. JREDD+ MRV challenges: plantation harvests misread as deforestation, driver attribution, large minimum mapping units, 5-year reporting gaps, single fire dataset ("DETER still omits 20% of forest fire"), unaccounted regrowth → governments, ART-TREES, CTrees → Landsat, Sentinel-2, VIIRS fire, MapBiomas → [CTrees 22 Jul 2026](https://ctrees.org/news/8-challenges-for-jredd-mrv)
119. Carbon-market audits every 3–5 years are too infrequent, and most participants can't analyse satellite data in-house → buyers, verifiers → Landsat / Sentinel time series → [London Economics](https://londoneconomics.co.uk/blog/publication/no-value-without-verification-earth-observation-for-carbon-markets/)
120. US forest inventory (FIA, 300,000+ plots) is "suffering capacity constraints" and lacks fusion with remote sensing → USFS, carbon markets, forestry → GEDI, Landsat, FIA plots → [CTrees 13 Jul 2026](https://ctrees.org/news/time-to-modernize-us-forest-inventory)

### Insurance and finance

121. Two-thirds of modelled US flood losses are underinsured, and the NFIP's future is uncertain → SMEs, municipalities, Liberty Mutual / Floodbase → Sentinel-1, Global Flood Database, OpenFEMA NFIP claims → [PR Newswire 24 Feb 2026](https://www.prnewswire.com/news-releases/floodbase-and-liberty-mutual-launch-instant-parametric-flood-quoting-capability-for-us-commercial-market-302695451.html)
122. Parametric basis risk (index pays without loss, or misses a real loss) → Floodbase, Descartes, Arbol, ARC, policyholders → Sentinel-1 flood extent vs NFIP claims; CHIRPS vs NDVI vs IPC → [Floodbase](https://www.floodbase.com/)
123. Parametric distribution is bespoke and slow (quotes took weeks) → brokers, MGAs → APIs over flood indices → [Insurance Journal 6 Mar 2026](https://www.insurancejournal.com/news/national/2026/03/06/860867.htm)
124. Settling tornado and hail parametric covers for solar farms → Descartes, solar asset owners → Sentinel-2 dNDVI scars, NOAA MRMS hail, SPC tracks, USPVDB → [FinTech Global 24 Jan 2025](https://fintech.global/2025/01/24/descartes-underwriting-introduces-70m-parametric-insurance-product-for-solar-farms/)
125. Property-level wildfire and hail underwriting with limited inspections; regulators require approval of AI models → P&C insurers, FAIR Plans → NAIP, building footprints, MRMS hail → [ZestyAI](https://www.zesty.ai/), [TechCrunch on Cape, 13 Jan 2025](https://techcrunch.com/2025/01/13/moodys-agrees-to-acquire-cape-analytics-which-develops-geospatial-ai-for-insurance-providers)
126. Physical-climate-risk vendor scores disagree, and validating them is hard → banks, asset managers, regulators → FEMA NFHL, JRC flood hazard, Sentinel-1 flood history → [Jupiter](https://www.jupiterintel.com/)
127. Closed climate-risk models (MSCI–First Street) become unauditable standards → homeowners, lenders, regulators → open flood/fire hazard plus EO → [TerraWatch 30 Jun 2026](https://newsletter.terrawatchspace.com/earth-observation-essentials-june-30-2026/)
128. Wildfire claims need parcel-level damage footprints quickly → insurers, OroraTech / ICEYE customers → FIRMS VIIRS, Sentinel-2 dNBR, CAL FIRE DINS → [OroraTech](https://ororatech.com/)
129. Banks want EO for loan monitoring (construction progress, crops, inventory) with explicit ROI thresholds → Chinese banks, and potentially Western lenders → Sentinel-2 time series → [TerraWatch 30 Jun 2026](https://newsletter.terrawatchspace.com/earth-observation-essentials-june-30-2026/)
130. Africa's climate-risk data deficits and drought-index basis risk → ARC, African governments, farmers → CHIRPS, TAMSAT, NDVI, FEWS NET / IPC → [ARC](https://www.arc.int/)

### Agriculture

131. Verifying farm practices (cover crops, no-till) at scale for Scope 3 insetting and 45Z → Regrow, Agreena, Indigo, Corvian, food companies, biofuel producers → HLS / Sentinel-2 time series, USDA CDL → [Agreena](https://agreena.com/)
132. Agtech data platforms can't get adoption: "the differentiator is no longer access to data but the ability to execute with it" → agribusinesses, insurers → n/a (a workflow problem) → [Corvian 10 Dec 2025](https://corvian.com/2025/12/farmers-edge-announces-corvian/)
133. Crop and hail insurance adjusting is slow and manual → crop insurers (Saskatchewan Municipal Hail: 4.6M acres), lenders (Sicredi) → MRMS hail swaths, Sentinel-2 NDVI drop, CDL → [Corvian](https://corvian.com/)
134. Crop algorithms built for large Western farms fail on smallholder (<1 ha) plots → Asian and African agriculture, insurers → Sentinel-2, field boundaries → [TerraWatch 11 May 2026](https://newsletter.terrawatchspace.com/earth-observation-essentials-may-11-2026/)

### Utilities, infrastructure, wildfire and population

135. Utility vegetation encroachment and wildfire ignition risk → utilities (Overstory has 6 of the 10 largest in the Americas) → Meta / WRI canopy height, NAIP, HIFLD / OSM lines, USFS wildfire risk → [Impact Alpha](https://impactalpha.com/overstory-secures-43-million-to-predict-and-prevent-utility-sparked-fires/)
136. Live fuel moisture is measured by clipping and weighing shrubs (not scalable) → fire agencies, utilities → Sentinel-2 NDMI, MODIS, National Fuel Moisture Database → [CTrees Fuel Watch 16 Oct 2026](https://ctrees.org/news/Los-Angeles-County-wildfire-spread)
137. Subsurface water leaks are invisible to utilities → water utilities → L-band SAR (NISAR provisional data from Jul 2026) → [asterra.io](https://asterra.io/)
138. Censuses are expensive, infrequent and undercount fast-growing, conflict and disaster areas → health agencies, humanitarian orgs, insurers → building footprints/density from imagery, WorldPop, Populace → [Planet, 12 Oct 2026](https://www.planet.com/pulse/introducing-populace-mapping-humanity-in-unprecedented-detail/)
139. Official registers undercount informal-settlement populations (7.59M by building footprints vs 4.15M registered) → municipal planners, NGOs → open building footprints → [Spectral Reflectance 2 Jul 2026](https://www.spectralreflectance.space/p/cng-london-people-who-fight-with)

### Defence and intelligence process

140. Commercial analytics bought but not used ("make sure that users needs it") → NGA Commercial Operations → Luno-style object and change feeds delivered into user tools → [Breaking Defense, 23 May 2025](https://breakingdefense.com/2025/05/nga-hopes-to-award-up-to-10-luno-commercial-analytics-task-orders-this-year/)
141. Facility and object monitoring at scale (aircraft, ships, railcars, oil tanks) → NGA (Luno orders) → Sentinel-1/2, xView, oil-tank shadow and SAR methods → [NGA release 2 Jul 2025](https://www.nga.mil/assets/files/25-10_Release_Luno_A_B_Update.pdf)
142. Fragmented buying authority (NGA vs NRO vs Space Force turf war) → US DoD/IC → n/a (process problem) → [Breaking Defense, 21 May 2025](https://breakingdefense.com/2025/05/nga-space-force-ink-accord-on-responsibilities-for-buying-commercial-isr/)
143. Coordinating a virtual constellation of national and commercial satellites (NATO Aquila) → NATO APSS, 19 Allies → CelesTrak TLEs plus sensor specs, a revisit planner → [NATO approach to space](https://www.nato.int/cps/en/natohq/topics_175419.htm)
144. Slow, fragmented European defence-space procurement → EDA, EU states, UK MoD → n/a (process problem) → [Via Satellite, 21 Sep 2026](https://www.satellitetoday.com/government-military/2026/09/21/europe-grapples-with-faster-procurement-amid-space-defense-push/)
145. Human-machine teaming and AI literacy for analysts → NGA under Bredenkamp → reviewer UIs, active learning → [Breaking Defense, 7 May 2026](https://breakingdefense.com/2026/05/ai-blueprint-coming-soon-to-nga-to-help-operationalize-geoint/)
146. Packaging defence-grade monitoring for non-experts via AI agents (SkyFi MCP, Robinhood) → retail investors, agent builders → Sentinel-2 or NAIP plus an MCP server → [BlackSky PR, 30 Sep 2026](https://blacksky.com/press-releases/blacksky-named-first-satellite-imagery-provider-for-skyfi-satellite-intelligence-on-robinhood-agent-apps/)
147. Over-automation deskills operators who must still work when systems fail → Army geospatial engineers → n/a → [USGIF 24 Mar 2026](https://usgif.org/geointeraction-colorado-data-standards-ai-integration-and-the-skills-that-keep-geoint-mission-ready/)

## Shortlist: problems that best fit a 36-hour build

Selected from the problem bank for: (1) a clearly named sufferer, (2) a 2025–2026 "why now", (3) large free public data, (4) a demo that ends in a decision or action rather than a map. Each line points to the entries that hold the evidence.

1. **EUDR plot pre-checker.** EU importers must prove commodities come from land not deforested after 31 Dec 2020, from 30 Dec 2026; satellite "tree cover loss" is routinely misread as deforestation. MVP: upload farm polygons → check against UMD GFC / JRC GFC2020 & TMF / RADD-GLAD alerts / Sentinel-2 time series, separate fire vs clearing vs plantation harvest, flag where baselines disagree, emit an evidence note. Evidence: Global Nature Watch / WRI, LiveEO, Picterra, Satelligence entries; [WRI, 6 Oct 2026](https://www.wri.org/insights/eu-deforestation-footprint-eudr); [GNW, 29 Apr 2026](https://globalnaturewatch.org/blog/data-and-tools/2025-tree-cover-loss-data-explained/).
2. **"AIS lie detector" for insurers and coast guards.** AIS is jammed, spoofed or switched off at record scale; claims and sanctions decisions now need independent evidence. MVP: for one strait/port, match Sentinel-1 SAR vessel detections (open xView3/Skylight models, GFW SAR detections) to AIS; flag dark vessels and AIS ghosts; produce a timestamped evidence pack. Evidence: Windward, GFW, Skylight entries; Theme 3; [Windward, 20 Oct 2026](https://windward.ai/blog/how-marine-insurers-are-closing-the-evidence-gap/); [GFW, 3 Jan 2024](https://globalfishingwatch.org/press-release/new-research-harnesses-ai-and-satellite-imagery-to-reveal-the-expanding-footprint-of-human-activity-at-sea/).
3. **Satellite-image claim checker (deepfakes / misdated images).** Fake or AI-altered "satellite images" went viral in the India–Pakistan (2025) and Iran (2026) conflicts; debunkers used free Sentinel-2. MVP: image + claimed place/date → pull nearest Sentinel-2/1 scenes from STAC, compare, run a fake detector, output "consistent / inconsistent / unverifiable at 10 m". Evidence: Theme 14; MizarVision entry; [France 24, 16 May 2025](https://observers.france24.com/en/asia-pacific/20250516-india-pakistan-conflict-ai-generated-or-edited-fake-satellite-images-flood-social-media); [Al-Monitor/AFP, 8 Mar 2026](https://www.al-monitor.com/originals/2026/03/fake-ai-satellite-imagery-spurs-us-iran-war-disinformation).
4. **Blackout-proof damage monitor.** When commercial imagery is withheld, journalists and NGOs fall back on Sentinel-1 damage proxies that over-detect and miss small damage. MVP: Bellingcat's PWTT + a false-positive filter (agriculture, construction, moisture) + automatic Sentinel-2 cross-check + a plain-language, cited brief per site. Evidence: Bellingcat, Planet blackout, Iran war entries; Theme 18; [Bellingcat, 7 Apr 2026](https://www.bellingcat.com/resources/2026/04/07/tool-damage-assessment-destruction-sentinel-satellite-imagery-iran-us-gulf/); [CJR, 11 May 2026](https://cjr.org/feature/blind-spots-satellite-osint-open-source-middle-east-iran-blackout-planet-labs-vantor-maxar.php).
5. **Methane alert → accountable operator.** Most satellite methane alerts go unanswered and only about a third of US oil-and-gas plumes can be tied to an operator. MVP: join Carbon Mapper / EMIT / TROPOMI plumes to OSM/OGIM and permit databases, name the likely facility and operator, track repeat emitters, draft the notification. Evidence: Kayrros, methane-after-MethaneSAT, Carbon Mapper, TerraWatch 2026 entries; [UNEP, Oct 2025](https://www.unep.org/news-and-stories/press-release/better-data-driving-action-methane-emissions-more-work-needed); [TerraWatch, 28 Sep 2026](https://newsletter.terrawatchspace.com/earth-observation-essentials-september-28-2026/).
6. **Change-alert de-noiser.** Deforestation / disturbance alerts are polluted by clouds, shadows, phenology and misregistration; analysts waste time on false alarms. MVP: score each GFW integrated / DIST-ALERT alert as likely real vs false using same-season history, SAR agreement and co-registration checks, with an explanation. Evidence: Theme 9; Planet dense-time-series entry; [Planet, 22 Oct 2026](https://www.planet.com/pulse/why-dense-satellite-time-series-deliver-more-trustworthy-insight/).
7. **"Show your work" geospatial answer engine.** LLM/VLM answers on imagery are often wrong (best VLM 41.7% on GEOBench-VLM; "90% right is 100% wrong") and practitioners say provenance tooling barely exists. MVP: question → STAC search → deterministic tools do the measuring → LLM explains; every claim links to the exact scenes, code and a reproduce button. Evidence: Element 84, Will Cadell, Theme 13 entries; [Element 84 Tech Radar 2026](https://element84.com/geospatial/geospatial-tech-radar-2026-an-emphasis-on-provenance-and-refined-tooling-from-ai-to-cloud-native/); [Strategic Geospatial, 13 Oct 2026](https://www.strategicgeospatial.com/p/90-right-is-100-wrong-benchmarking).
8. **Analyst triage queue.** "Far more detections than analysts can validate" (NGA speaker, 2026); collection volume dwarfs human review. MVP: run open ship/change detectors on a watch-list of sites, rank by confidence × novelty × priority, cross-check AIS/ADS-B, show a ranked queue and measure analyst minutes saved. Evidence: Theme 1; NGA entries; GEOINT/USGIF entry; [USGIF, 10 Aug 2026](https://usgif.org/mission-focus-ai-first-approaches/).
9. **Parametric flood basis-risk explainer.** Two-thirds of modelled US flood losses are underinsured and parametric products live or die on basis risk. MVP: compute a Sentinel-1 "% of zone flooded" trigger for past floods and compare with OpenFEMA NFIP claims by ZIP to show where a policy would have paid or missed. Evidence: Floodbase, Descartes Underwriting, Arbol, TerraWatch parametric entries; [PR Newswire, 24 Feb 2026](https://www.prnewswire.com/news-releases/floodbase-and-liberty-mutual-launch-instant-parametric-flood-quoting-capability-for-us-commercial-market-302695451.html).
10. **Utility line-strike / ignition risk map.** Utilities still trim on cycles; buyers just paid real money for this capability (Schneider–AiDASH, Overstory $43M). MVP: open canopy-height model + NAIP/Sentinel-2 + OSM/HIFLD lines + FIRMS fire history + wind → ranked spans to trim. Evidence: AiDash, Overstory, Wherobots entries; [Impact Alpha on Overstory](https://impactalpha.com/overstory-secures-43-million-to-predict-and-prevent-utility-sparked-fires/).
11. **"Is free data enough, and what will paid imagery cost?"** Buyers say the pain is now the buying process (budget approval, unclear pricing, licensing) and tasking feasibility. MVP: question + AOI → can Sentinel/Landsat answer it (resolution, revisit, cloud climatology)? If not, list providers with published prices (Umbra, SkyFi, EOS, UP42) and a TLE-based feasibility window. Evidence: UP42, SkyFi, Arlula, Theme 4–5 entries; [UP42, 31 Jul 2026](https://up42.com/blog/state-of-earth-observation-in-2026); [Element 84, 26 Feb 2026](https://element84.com/software-engineering/if-ai-is-going-to-task-satellites-we-need-standards/).
12. **Oil-slick polluter attribution.** Illegal discharges are detectable in Sentinel-1 but rarely prosecuted. MVP: take Cerulean slicks, back-track AIS to the likely vessel, assemble an evidence pack and a draft complaint. Evidence: SkyTruth Cerulean entry; [SkyTruth](https://skytruth.org/cerulean/).
13. **Arson / burned-village verification at scale (Sudan).** Human-rights investigators verify burned structures one by one. MVP: fork CIR's open "Burnscar" pipeline (FIRMS + Sentinel-2 dNBR + Open Buildings), add Sentinel-1 for cloudy scenes and a reviewer UI whose decisions become labels. Evidence: CIR Burnscar entry; [BigData Republic, 24 Sep 2025](https://bigdatarepublic.nl/articles/detecting-war-crimes-from-space/).
14. **Carbon-offset report card.** REDD+ over-crediting scandals; buyers want independent checks. MVP: project polygon vs matched control area on Hansen/JRC loss, with a transparent counterfactual and a grade. Needs a sharper angle than plain NDVI (done before). Evidence: carbon-integrity, Sylvera, Renoster, CTrees entries.
15. **Subsea-cable loitering watch.** Vessels loitering over cables and pipelines (Windward documented a sanctioned Russian vessel loitering for 41 days). MVP: AIS + Sentinel-1 dark-vessel detections near public cable routes, explained alerts with confidence. Evidence: tip-and-cue / maritime entry in A.3; Windward entry.

## Cross-slice leads

Short notes for the other research slices (EO operators, US agencies, ESA/Europe, SpaceX/xAI/orbital compute, space traffic/debris/space weather, China, datasets, models/tools, space science). Grouped by the sub-area of this report where they surfaced.

### From analytics, platforms, open monitors and LLM products (A.1, A.4, A.5)

- **SpaceX, xAI and orbital compute:** Starcloud raised $170M Series A at a reported ~$1.1B valuation to sell on-orbit processing; TerraWatch argues "EO workloads are now the anchor demand getting orbital compute infrastructure off the ground" ([TerraWatch, 13 Apr 2026](https://newsletter.terrawatchspace.com/earth-observation-essentials-april-13-2026/); see also the 11 May 2026 issue).
- **EO satellite operators:** Planet Tanager-2 and SuperDove Flock 4J first light (20 Oct 2026) and USGS independent Tanager evaluation (10 Sep 2026) ([Planet Pulse](https://www.planet.com/pulse/)); Vantor 20 cm + 40 cm constellations announced (TerraWatch, 13 Apr 2026); Planet manufacturing expansion in Germany (21 Sep 2026); EarthDaily constellation status not verified (newsroom login-gated).
- **US agencies:** FY2027 NASA request cuts Earth science 52% ($2.15B → $1.02B) and proposes "one final Landsat satellite" + $109M to move Landsat to a commercial solution (TerraWatch, 13 Apr 2026); NISAR provisional L-band data released 20 Jul 2026 and NASA forest-loss alerts >3 months faster with NISAR ([New Space Economy, 23 Oct 2026](https://newspaceeconomy.ca/2026/10/23/why-does-defense-dominate-earth-observation-demand-over-commercial-markets/)); NASA Earth Copilot / VEDA ([Microsoft, Nov 2024](https://blogs.microsoft.com/public-sector/2024/11/14/from-questions-to-discoveries-nasas-new-earth-copilot-brings-microsoft-ai-capabilities-to-democratize-access-to-complex-data/)); US government request to withhold Iran-war imagery ([Al Jazeera, 5 Apr 2026](https://aljazeera.com/news/2026/4/5/us-satellite-firm-planet-labs-announces-blackout-on-war-on-iran-images)).
- **ESA, Europe:** ESA Biomass P-band data opened 26 Jan 2026 (New Space Economy); EUDR application dates 30 Dec 2026 / 30 Jun 2027 ([WRI](https://www.wri.org/insights/eu-deforestation-footprint-eudr)); Copernicus Sentinel-1 is the backbone of open war-damage mapping ([Bellingcat](https://www.bellingcat.com/resources/2026/04/07/tool-damage-assessment-destruction-sentinel-satellite-imagery-iran-us-gulf/)); UP42 now owned by Saudi PIF's Neo Space Group.
- **Space traffic, debris, space weather:** GNSS jamming/spoofing at sea at unprecedented scale in 2026 (124,235 vessels affected Q3 2026 per Windward) — GNSS interference monitoring (Privateer's Elements advertises "GNSS interference detection") ([Windward](https://windward.ai/blog/how-marine-insurers-are-closing-the-evidence-gap/); [privateer.com](https://www.privateer.com/)); Privateer (ex-Orbital Insight owner) runs Wayfinder orbital catalogue.
- **China:** Chinese provider MizarVision imagery used by journalists during the Planet blackout; US sanctioned Chinese firms for supplying imagery to Iran (per CJR, in Theme 18).
- **Datasets catalogue:** GFW APIs (fishing effort, encounters, loitering, SAR detections, offshore infrastructure) ([GFW](https://globalfishingwatch.org/our-apis/)); Skylight open vessel-detection models (`allenai/vessel-detection-sentinels`); Carbon Mapper Data/STAC API; Climate TRACE monthly releases (5.11.0, Sep 2026); UMD GLAD tree cover loss 2001–2025; Planet Populace (~40 m quarterly population, free non-commercial); AlphaEarth annual 10 m embeddings (public mirror served 178 TB by Oct 2026, per Element 84); Bellingcat PWTT GEE apps.
- **Models and tools:** OlmoEarth (Ai2) under Skylight; Google Remote Sensing Foundations / Population Dynamics Foundations; geoembeddings.org conventions v0.0.1; STAPI 0.1; MCP moved to the Linux Foundation (Dec 2025, per Element 84); GIS Copilot QGIS plugin; Mundi.ai (AGPL, self-host); Wherobots RasterFlow; Esri remote-sensing FM + VLM in development.
- **Space science and literature:** PWTT peer-reviewed validation (AUC 0.87 on >2M UN-labelled buildings) cited by Bellingcat; GFW *Nature* 2024 dark-fleet paper.

### From climate, nature, carbon, insurance and agriculture (A.2)

- **EO operators:** Tomorrow.io raised $175M (Feb 2026), reports about $100M ARR and launched the "DeepSky" constellation ([Wikipedia](https://en.wikipedia.org/wiki/Tomorrow.io)). OroraTech's FOREST-20 brought its constellation to 20 satellites (1 Oct 2026) and it partnered with ICEYE (22 Oct 2026) ([OroraTech](https://ororatech.com/)). LiveEO is reportedly building its own "Twinspector" constellation ([Tamradar](https://www.tamradar.com/funding-rounds/liveeo-28m-satellite-intelligence)). GHGSat reports 2025 detection statistics ([Nexi.fund](https://nexi.fund/ai-satellite-methane-detection-2026/)).
- **US agencies:** OpenFEMA NFIP Claims v2 has been deprecated in favour of v3 ([FEMA](https://www.fema.gov/openfema-data-page/fima-nfip-redacted-claims-v2)). USFS FIA capacity constraints ([CTrees](https://ctrees.org/news/time-to-modernize-us-forest-inventory)). The FY2027 NASA budget proposal cuts Earth science 52% and moves Landsat to a "commercial solution" ([TerraWatch, 13 Apr 2026](https://newsletter.terrawatchspace.com/earth-observation-essentials-april-13-2026/)). CARB satellite methane project with Carbon Mapper.
- **ESA / Europe:** EUDR amending Regulation (EU) 2025/2650. ESA Biomass P-band data opened 26 Jan 2026 ([New Space Economy](https://newspaceeconomy.ca/2026/10/23/why-does-defense-dominate-earth-observation-demand-over-commercial-markets/)). The EU Forest Observatory (JRC GFC2020) page did not render.
- **Datasets catalogue:** Global Flood Database (CC BY-NC); USPVDB v4.0; Carbon Mapper portal; Planet Tanager open STAC (CC BY); CTrees JMRV / LUCA; UNEP methane data portal; NISAR L-band (provisional data from 20 Jul 2026) for cloud-free deforestation alerts, which NASA reports issue more than 3 months faster (TerraWatch, 13 Apr 2026).
- **Models and tools:** KayrrosAI methane RAG LLM (COP29). Earth Blox (repeatable nature assessments). Prior art: the PyCon US 2026 satellite-ML greenwashing poster.
- **Space traffic / debris / space weather:** none.
- **China:** LiveEO post on "Geolocation Data Sharing from China under EUDR" (11 Jul 2025) ([LiveEO blog](https://www.live-eo.com/blog)). Carbon Mapper detected a China coal-mine methane plume on 9 May 2026 ([Carbon Mapper](https://carbonmapper.org/articles/tanager-1-two-years-of-turning-satellite-data-into-methane-action)).

### From defence and intelligence demand (A.3)

- **US agencies slice:** The FY2027 White House budget proposes NASA at $18.8B (−23%), NASA Earth science −52%, "one final Landsat satellite", and $109M to commercialise Landsat. NASA and USGS plan to buy *finished products* for Landsat continuity, so companies without satellites could bid (TerraWatch, 24 Aug 2026; SAM.gov briefing). NOAA's commercial data program plans buys of up to $2.35B over 10 years. Sources: [TerraWatch 13 Apr 2026](https://newsletter.terrawatchspace.com/earth-observation-essentials-april-13-2026/) and [TerraWatch 24 Aug 2026](https://newsletter.terrawatchspace.com/earth-observation-essentials-august-24-2026/).
- **US agencies slice:** Roger Mason (V2X executive) was nominated as NRO director, succeeding Chris Scolese. The Senate confirmed the NRO chief in Aug 2026 (Breaking Defense headline).
- **ESA / Europe slice:** ESA Nov 2025 ministerial (€22.1B; about €3.5B EO; up to €1.2B for a military constellation). ICEYE valuation above €10B (Series F, June 2026). Planet €240M German deal. Sources: [TerraWatch 17 Dec 2025](https://newsletter.terrawatchspace.com/earth-observation-essentials-december-17-2025/) and [Wikipedia: ICEYE](https://en.wikipedia.org/wiki/ICEYE).
- **SpaceX / xAI / orbital compute slice:**
  - NRO's proliferated LEO constellation is operated by SpaceX (Scolese, May 2026).
  - Breaking Defense, May 2026: "Despite 'peak hype,' orbital data centers for AI not yet ready for NatSec prime time".
  - Starcloud processes Capella SAR data on orbit (TerraWatch, 11 May 2026).
  - BlackSky is the exclusive VHR EO provider for an "international initiative to build the world's largest AI infrastructure in space" (BlackSky PR, 9 Sep 2026).
  - Planet Pelican and Owl satellites carry Nvidia Jetson Orin / Thor GPUs (Via Satellite, 20 Oct 2026).
  - Starshield slowdown in Ukraine, Oct 2026: four Democratic senators asked SpaceX for answers (Via Satellite, 20 Oct 2026).
- **Space traffic / debris slice:** A Russian satellite manoeuvred within "extreme proximity" of an ICEYE satellite, per LeoLabs ([Via Satellite, 19 Oct 2026](https://www.satellitetoday.com/government-military/2026/10/19/russian-satellite-maneuvered-within-extreme-proximity-of-iceye-satellite-leolabs-reports/)). NRO CSO bought non-Earth imaging from HEO (Feb 2026). Kratos reports more than $100M in contracts for space intelligence data (Via Satellite, 5 Oct 2026).
- **China slice:** MizarVision (AI on open-source imagery) published and sold imagery of US forces during the 2026 Iran war (Global Times, 30 Jan 2026; Washington Post, 4 Apr 2026, via Breaking Defense).
- **Datasets slice:**
  - xView3 (Sentinel-1 dark vessels, DIU/GFW).
  - UNOSAT damage labels (used to validate PWTT on more than 2M buildings).
  - Google Open Buildings.
  - NASA FIRMS.
  - Vantor/Maxar Open Data Program (verify current status and licence after the rebrand).
  - RarePlanes.
  - Capella and Umbra open SAR data (verify).
- **Models / tools slice:**
  - Bellingcat PWTT (Earth Engine).
  - CIR Burnscar (MIT, SQLMesh + DuckDB).
  - LGND "geo" tool connecting Sentinel-2/NAIP to AI assistants for natural-language search and change detection ([LGND](https://lgnd.ai/resources/lgnd-geo), via TerraWatch 12 Oct 2026).
  - Google Custom Satellite Embeddings (AlphaEarth, private preview, July 2026). TerraWatch calls this an "existential change" for feature-extraction and change-detection vendors.
  - Element 84 Geospatial Tech Radar 2026.
  - An MDPI paper on running a geospatial foundation model on board a satellite.
- **Main Part A (non-profits):** **Planet imagery was removed from Global Forest Watch (now "Global Nature Watch") on 1 Apr 2025, when the NICFI phase ended.** Limited Amazon-only access returned on 26 May 2026 via "GNW Horizon" (Bezos Earth Fund, Andes Amazon Fund and Planet, to May 2027). Users such as Mighty Earth, HAkA and Mongabay outside the Amazon lost access. [GNW blog](https://globalnaturewatch.org/blog/data-and-tools/planet-imagery-changes-gfw/).
- **Main Part A (insurance and disaster):** ICEYE's natural-catastrophe intelligence is now in Insurity SpatialKey (29 Sep 2026). California is integrating ICEYE data into statewide emergency operations (Oct 2026). ICEYE and OroraTech are partnering on full-lifecycle wildfire intelligence (22 Oct 2026). All from the [ICEYE newsroom](https://www.iceye.com/newsroom).
- **Main Part A (Planet + LLMs):** Planet CSO Schingler (Oct 2026) says LLMs such as "Gemini and Claude" are "blind to the physical reality of the planet". His "planetary intelligence" means fusing EO data with AI. [Via Satellite, 20 Oct 2026](https://www.satellitetoday.com/earth-observation/2026/10/20/planet-cso-robbie-schingler-talks-sovereignty-onboard-ai-and-the-launch-squeeze/).

### From analysts, press and conferences (B.1–B.5)

- **US agencies:**
  - NASA FY27 request: Earth science −52% ($2.15B → $1.02B) and "one final Landsat" plus $109M for commercial Landsat ([TerraWatch 13 Apr 2026](https://newsletter.terrawatchspace.com/earth-observation-essentials-april-13-2026/)).
  - Landsat 10 (single satellite, 2031, 26 bands) and the NASA/USGS commercial-products industry event on 31 Aug 2026 ([TerraWatch 24 Aug 2026](https://newsletter.terrawatchspace.com/earth-observation-essentials-august-24-2026/)).
  - NOAA $2.35B 10-year commercial weather-data vehicle with 14 companies ([TerraWatch 16 Sep 2026](https://newsletter.terrawatchspace.com/earth-observation-essentials-september-16-2026/)).
  - NASA CSDA program added 8 providers (Hydrosat, OroraTech, ImageSat, Satlantis, Kuva, Wyvern, Orbital Sidekick, Muon) to a $476M contract ([TerraWatch 30 Jun 2026](https://newsletter.terrawatchspace.com/earth-observation-essentials-june-30-2026/)).
  - USDA testing satellite imagery and AI for crop estimates ([TerraWatch 16 Sep 2026](https://newsletter.terrawatchspace.com/earth-observation-essentials-september-16-2026/)).
  - EOCL is $3.24B over 10 years with a firm base to ~2027, up for recompete ([TerraWatch 22 May 2026](https://newsletter.terrawatchspace.com/three-years-on-analysing-advents-maxar-acquisition/)).
- **ESA / Europe:**
  - ESA €22.1B ministerial budget (~€3.5B EO) ([TerraWatch 17 Dec 2025](https://newsletter.terrawatchspace.com/earth-observation-essentials-december-17-2025/)).
  - ESA EOGS studies to ICEYE and Leonardo, and an ESA × Mistral AI agreement (EVE assistant) ([TerraWatch 28 Sep 2026](https://newsletter.terrawatchspace.com/earth-observation-essentials-september-28-2026/)).
  - Switzerland skipping Copernicus 2028–34 ([TerraWatch 8 Jun 2026](https://newsletter.terrawatchspace.com/earth-observation-essentials-june-8-2026/)).
  - Sentinel-3C first images ([TerraWatch 12 Oct 2026](https://newsletter.terrawatchspace.com/earth-observation-essentials-october-12-2026/)).
  - Sentinel-3 data reaching emergency services in 60 minutes instead of 180 ([TerraWatch 24 Aug 2026](https://newsletter.terrawatchspace.com/earth-observation-essentials-august-24-2026/)).
  - Biomass open data from 26 Jan 2026 and Sentinel-1D data from 17 Apr 2026 (per [New Space Economy](https://newspaceeconomy.ca/2026/10/20/the-state-of-earth-observation-2026/), unverified).
- **SpaceX / orbital compute:**
  - Starcloud raised $170M plus a $250M extension (Nvidia), and its first satellite processes Capella SAR. "EO workloads are now the anchor demand" ([TerraWatch 11 May 2026](https://newsletter.terrawatchspace.com/earth-observation-essentials-may-11-2026/), [24 Aug 2026](https://newsletter.terrawatchspace.com/earth-observation-essentials-august-24-2026/)).
  - Pixxel × Sarvam orbital data-centre satellite.
  - EO operators' fear of Falcon 9 commercial wind-down, and Novaspace's "Falcon 9 may leave the commercial market around 2030" ([Novaspace 16 Oct 2026](https://nova.space/in-the-loop/10-trends-reshaping-the-global-space-economy-insights-from-world-space-business-week-2026/)).
  - Loft Orbital × Marlan $1B 50-satellite constellation with Mistral onboard AI.
  - Morrison's "internet in space" relay thesis.
- **Space traffic / space weather:**
  - NGA used commercial analytics to confirm debris damage to China's space station "within hours" ([Via Satellite 6 May 2026](https://www.satellitetoday.com/imagery-and-sensing/2026/05/06/enabled-by-ai-nga-director-focused-on-mission-transformation-and-workforce/)).
  - BlackSky non-Earth imaging renewal (May 2026).
  - Ethereal Space $5M NOAA ionospheric data; WMO/ITU spectrum-interference warning ([TerraWatch 12 Oct 2026](https://newsletter.terrawatchspace.com/earth-observation-essentials-october-12-2026/)).
- **China:**
  - Chinese banks launching EO satellites and using EO for credit ([TerraWatch 30 Jun 2026](https://newsletter.terrawatchspace.com/earth-observation-essentials-june-30-2026/)).
  - Chinese providers gaining share during US shutter control ([TerraWatch 11 Aug 2026](https://newsletter.terrawatchspace.com/earth-observation-essentials-august-11-2026/)).
  - Restrictions on Chinese open-weight models for US government work ([Element 84 Radar](https://element84.com/geospatial/geospatial-tech-radar-2026-an-emphasis-on-provenance-and-refined-tooling-from-ai-to-cloud-native/)).
- **Datasets catalogue:**
  - Embedding datasets: AlphaEarth, TESSERA, LGND global Sentinel-2 GeoParquet, Earth Genome 2025 ([CNG](https://cloudnativegeo.org/blog/2026/07/announcing-geo-embedding-sprint-zurich/)).
  - ESA World Settlement Footprint Tracker.
  - Umbra Open Data (SAR; >$4M released, Mar 2024).
  - Leeds 53 TB Antarctic ice-velocity Zarr.
- **Models and tools:**
  - Google Custom Satellite Embeddings (private preview, Jul 2026), WeatherNext 3, LGND assistant connector, Element 84 Limner, Planet agentic query, RASID GoPilot.
  - NASA Earthdata MCP server and AWS Open Data MCP server ([Element 84 Limner](https://element84.com/geospatial/introducing-the-new-limner-conversational-composable-and-traceable/)).
  - Tessera EOFM.
- **EO operators:**
  - ICEYE ~€250M 2025 revenue, >€100M operating profit, >€10B valuation; HawkEye 360 IPO ($3.1B).
  - Albedo exit from imagery; Satellogic $13M 2024 revenue; Spire Q3 −56%.
  - Vantor Pulse and Vantage; Planet Germany €25M dedicated constellation.
  - Hydrosat Osiris; Muon $250M Series C.
- **Space science / literature:** The Nature Sustainability InSAR subsidence study of Indian cities (TerraWatch 17 Dec 2025) and NASA's NISAR + optical deforestation alerts >3 months faster (TerraWatch 13 Apr 2026).

### From recurring themes (B.6)

- **Global Forest Watch appears to be rebranding/expanding as "Global Nature Watch"** — globalforestwatch.org blog URLs 301-redirect to globalnaturewatch.org; DIST-ALERT added Jan 2026 (→ non-profits / open monitors in Part A; datasets catalogue).
- **US FY2027 NASA budget request** (per TerraWatch 13 Apr 2026): $18.8B total (−23%), Earth science −52% ($2.15B → $1.02B), "one final Landsat satellite" and $109M to move Landsat to a commercial solution (→ US agencies slice).
- **ESA Biomass P-band data opened 26 Jan 2026; NISAR provisional L-band data released 20 Jul 2026** (per New Space Economy) (→ ESA/agencies, datasets).
- **Starcloud $170M Series A at reported $1.1B valuation; EO as anchor demand for orbital compute** (TerraWatch 13 Apr 2026) (→ SpaceX/xAI/orbital compute slice).
- **US sanctioned three Chinese firms for supplying imagery to Iran; MizarVision published images of US military activity** (CJR 11 May 2026) (→ China slice).
- **Vantor (ex-Maxar) announced two new constellations (20 cm and 40 cm rapid revisit)** (TerraWatch 13 Apr 2026) (→ EO satellite operators slice).
- **Xoople raised $130M Series B and signed L3Harris sensor contract; embedded in Microsoft and Esri** (TerraWatch 13 Apr 2026) (→ EO operators / Part A).
- **CNG Geo-Embeddings Sprint (27–28 Oct 2026, Zürich; IBM, CNG, Clark Univ., Planet)** — embeddings benchmarking (→ models & tools slice).
- **ESA Φ-lab "Laying the Foundation for AI-Based Tip and Cue" (Apr–May 2025)** and **Φsat-2 onboard AI** (→ ESA slice).
- **Spire FY2025 revenue $71.6M** (Wikipedia citing 10-K, 19 Mar 2026) (→ EO operators slice).

## Leads not followed

Items that looked relevant but could not be opened, were paywalled, or were out of time. Useful starting points for follow-up.

### Analytics, platforms, open monitors and LLM products (A.1, A.4, A.5)

- **Reddit (r/gis, r/remotesensing, r/space):** reddit.com could not be fetched; practitioner threads on pricing, platforms and "is remote sensing a dying field" remain unchecked.
- **EarthDaily Analytics:** newsroom is login-gated; whether the EarthDaily Constellation launched (planned for 2025) and how Descartes Labs products were integrated is unverified.
- **GeekWire on Skylight's Shippy (2026):** returned 403; details taken from Skylight's own posts instead.
- **Earthrise Media → Earth Genome:** earthrise.media 301-redirects to earthgenome.org; no merger notice found — status unverified.
- **Mundi.ai cloud shutdown:** date and reason not found.
- **Danti:** 2025–2026 funding and contracts not verified (only 2023–2024 items found); **SkyWatch HUB** launch year unverified.
- **Planet × Anthropic:** no public results or case study found (claude.com customer page 404); the LLM behind Planet's May 2026 agentic query is not named in coverage.
- **NASA Earth Copilot:** public release status after the Nov 2024 proof of concept not verified.
- **Windward ownership:** FTV Capital's take-private (reported 2024) not verified; Windward's press page returned 404.
- **SkyTruth Cerulean methods/FAQ** (false-positive rates for SAR look-alikes) and **Amazon Mining Watch** methods/operator not opened.
- **Climate TRACE independent validation** studies not looked for.
- **Privateer:** what happened to the original TerraScope product and Orbital Insight staff; Lloyd's List Intelligence partnership date.
- **Ursa Space:** 2025–2026 press releases (homepage only); **RAIC Labs** newsroom content not shown.
- **Other platforms not researched:** Felt, CARTO AI agents (named as a Google Earth AI enterprise user), Fused, Earthmover, Ecopia, EOS Data Analytics, SatSure, Satellogic analytics, Solafune, Striveworks.
- **Hacker News / LinkedIn / X posts** on Planet–Anthropic, Google Earth AI and geospatial copilots were not searched.

### Climate, nature, carbon, insurance and agriculture (A.2)

- Space Intelligence funding history; Satelligence funding.
- Indigo Ag 2023–2026 valuation, layoffs and soil-carbon credit issuances.
- Pachama layoffs before its acquisition.
- Sylvera 2024–2026 layoffs or new rounds.
- Descartes Underwriting Series B date.
- Index-Based Livestock Insurance (IBLI, Kenya / Ethiopia) and the World Bank Global Index Insurance Facility.
- The 2016 Malawi ARC payout controversy.
- WSJ / regulators on insurers using aerial imagery to non-renew homeowners.
- First Street (its site now shows an MSCI terms gate, which suggests an MSCI relationship; unverified).
- Zillow and climate-risk scores.
- ICVCM CCP labels on REDD+ (VM0048).
- The Kariba REDD+ scandal (South Pole, 2023).
- Albo Climate, CarbonStack, BeZero funding.
- Earth Fire Alliance FireSat (EO operator slice).
- Ceres Imaging, Hummingbird Technologies, Cropin, SatSure, OneSoil (agri analytics status).
- Arbol "data center regulatory moratorium" cover details.
- 45Z USDA farm-practice verification rules.
- Reddit / HN threads on carbon offsets and satellite MRV (one search found none).

### Defence and intelligence demand (A.3)

- **FY2026 budget-request cuts to NRO commercial imagery / EOCL, and Congress's response:** not verified. SpaceNews returned HTTP 429 on every attempt and no primary source was opened.
- **Palantir and Anduril geospatial products:** Anduril Lattice and Vantor partnership details; Palantir MSS commercial imagery integration beyond the Maven contracts above.
- **Vantor's role in GEGD, and whether GEGD was renewed** after the March 2025 Ukraine cutoff.
- **Breaking Defense, April 2025:** "NGA field testing new processor to speed imagery to US regional commands", and the April 2025 exclusive on a new Luno A task order.
- **Breaking Defense, January 2026:** "'Overwatch' from space… foundational to Maduro mission" (commercial and national imagery in the Venezuela operation).
- **TacSRT's own program pages and spend;** Space Force commercial integration (the Commercial Space Office "Front Door").
- **EU SatCen** products and statistics; the Copernicus SESA service.
- **UK programmes:** Oberon, Tyche, ISTARI, and MoD commercial EO buying.
- **The Nature (Jan 2024) GFW paper** on untracked industrial vessels: Nature redirected to a login page, so the percentages were not verified.
- **Reuters report on HawkEye 360's NYSE listing:** Reuters is not fetchable. The $3.1B valuation and $416M raise come only via TerraWatch.
- **Striveworks and Solafune GEOINT platforms** (H1 2026 funding). Not researched.

### Analysts, press and conferences (B.1–B.5)

- Reddit r/gis, r/remotesensing, r/space: reddit.com could not be fetched from this environment, and the web-search quota ran out mid-research. Recommend a manual check of threads such as "is remote sensing a dying field" and data-cost threads.
- Payload Space / Payload Research EO market reports: payloadspace.com pages fetched showed no EO research. The Payload Research EO page was not found.
- NSR / Analysys Mason EO reports: only second-hand figures via New Space Economy ($29B D&I opportunity 2024–34, Jun 2026). Not verified at source.
- Novaspace 17th-edition EO Data & Services report: paywalled. Market figures known only second-hand ($5.0B → >$8.0B by 2033).
- Quilty Space EO Financial Reviews 2026 Q1/Q2: paywalled.
- TerraWatch Pro/Premium content: the full State of Commercial EO 2025, EOFM deep dive, H1 2026 M&A and outlook, "Anatomy of an EO Use Case" (not found), January 2026 sector assessment (only via New Space Economy), and the EO Summit 2026 Defense & Security track article in Satellite Today (URL not found).
- ESA Living Planet Symposium 2025 (Vienna): the site's TLS certificate failed to verify. Not covered.
- Φ-week: domain not resolved. CNG Forum 2026 in Utah: only referenced via Cadell. GEOINT 2025/2026 breakout sessions are not in the recaps.
- Space Symposium 2026: site returned 403. IAC 2025 (Sydney) / IAC 2026 (Antalya): EO content not extracted.
- Geospatial World (403). SpaceNews EO op-eds: none in the current opinion listing. TechCrunch, Sifted and Grist pieces on EO startup failures: only the TechCrunch tag page was checked.
- HN threads not opened: [WeatherNext 3 (item 49552299)](https://news.ycombinator.com/item?id=49552299) and the [WeatherNext cyclone thread (item 49220126)](https://news.ycombinator.com/item?id=49220126), both with 100+ comments.
- Joe Morrison posts after March 2023: none found on Substack. He may post on LinkedIn or X (not checked).
- The GenAI for Geospatial Challenge (14 winners, AWS credits): the organiser and full winner list were not confirmed.
- Strategic Geospatial "Assist.me" (20 Jul 2026) and "Deterministic Control Points" (9 Aug 2026), and Spectral Reflectance newsletters #129–137: not read.
- The BBC piece on Planet's restricted Iran imagery and the HOT piece on disagreeing damage assessments were cited only via TerraWatch and not opened.

### Recurring themes (B.6)

- Reddit (r/gis, r/remotesensing) and Hacker News threads: fetch blocked (reddit.com unreachable from this environment) and search budget ran out; not covered.
- Apollo Mapping and LandInfo public price lists (HTTP 403); Planet pricing page renders no prices.
- Original UW "deepfake geography" paper (Zhao et al., 2021, *Cartography and Geographic Information Science*) — only press coverage opened.
- BBC Verify figures on fabricated satellite imagery in the 2026 Iran war (cited second-hand).
- 2023 Guardian/Die Zeit/SourceMaterial investigation into Verra REDD+ credits (Guardian fetch blocked) — relevant to ground-truth/carbon verification.
- NGA GEOINT AI page / AI model accreditation programme (HTTP 403).
- Astraea, SpaceKnow, Radiant MLHub current status (mlhub.earth 404; no notice found).
- Whether Planet or Vantor offer cryptographic signing/verification of delivered imagery (none found).
- Space.com article on AI/EO risks (page truncated; only headline available).
