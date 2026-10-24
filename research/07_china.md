# 07 — China: space data, Earth observation, AI for space, and related problems

**Scope.** Everything China is doing in space data: Earth-observation (EO) constellations and companies, AI/foundation models for remote sensing, Chinese benchmarks and competitions (their problem statements), in-orbit/space computing, megaconstellations and their debris, commercial launch and what it does to EO costs, a brief look at human spaceflight/exploration, data-access policy and sanctions, and the problems Chinese actors themselves talk about.

**Researched on 2026-10-24.**

**Method note.** Searches in English and Chinese; pages opened and read where possible. SpaceNews articles are paywalled after the first paragraph, so some SpaceNews claims come from search-result excerpts and are marked as such. Chinese state media (Xinhua, CGTN, China Daily, People's Daily, Science and Technology Daily) claims are flagged **[state media]**. Counts of satellites differ by source (launched vs. catalogued vs. working); where they conflict, all figures are given. The shared web-search quota ran out several times during this session, so after the first ~20 searches most material came from pages fetched directly — above all the daily *China in Space* newsletter (Jack C.), whose archive was read post by post for Oct 2025 – Oct 2026. Items seen only as a title or a search excerpt are marked "title only" or "search excerpt". Many Chinese government data portals are JavaScript-only and could not be read.

**Top 10 hackathon picks (36 h, 2 people, public data):** see the end of the Problem bank.

---

## Contents

- A. Earth-observation constellations and companies (Chang Guang/Jilin-1, Gaofen/CHEOS, Yaogan, Fengyun, Haiyang, SpaceTY, PIESAT, MinoSpace, STAR.VISION, GalaxySpace and city constellations, Orbita, GEOVIS, HEAD/Emposat, China Siwei, Ziyuan/mapping, environment/GHG)
- B. Sanctions, OSINT and the dual-use problem (Chang Guang, Earth Eye/Emposat, MizarVision)
- C. AI for remote sensing: competitions (Gaofen Challenge, China Siwei Cup, Tianzhi Cup, Qizhi Cup), foundation models, benchmark datasets
- D. Space computing (Three-Body, onboard AI on EO sats, policy, other orbital-compute players)
- E. Megaconstellations and debris (Qianfan, Guowang, deployment bottlenecks, upper stages, Starlink coordination and UN complaint, ITU filings, counter-Starlink research, Honghu-3/Geely/Tianqi)
- F. Commercial launch and EO costs
- G. Human spaceflight and exploration (brief)
- H. Policy and data access
- I. Problems Chinese actors themselves discuss (interpretation bottleneck, revenue/demand, price collapse, involution, silos, quality, talent, Starlink, downlink)
- Problem bank (78 problems) + Top 10 shortlist
- Cross-slice leads
- Leads not followed

---

# A. Earth-observation constellations and companies

## A1. Chang Guang Satellite Technology (长光卫星) — Jilin-1 (吉林一号)

**What it is.** China's largest commercial EO operator. Spun off on 1 Dec 2014 from the Changchun Institute of Optics, Fine Mechanics and Physics (CIOMP, Chinese Academy of Sciences), headquartered in Changchun, Jilin. Called "the first unicorn enterprise from northeastern China." People's Daily calls Jilin-1 "China's largest commercial remote-sensing constellation and the world's largest sub-metre commercial remote-sensing constellation" (我国最大的商业遥感卫星星座和全球最大的亚米级商业遥感卫星星座). ([NewSpace Economy, 2026-03-20](https://newspaceeconomy.ca/2026/03/20/the-jilin-1-constellation-chinas-commercial-eye-in-the-sky/); [People's Daily, 2025-05-15](https://paper.people.com.cn/rmrb/pc/content/202505/15/content_30073262.html))

**Size (counts conflict).**
- 70 in orbit, Aug 2022 (end of phase 1) ([Chinanews, 2022-08-10](https://www.chinanews.com.cn/gn/2022/08-10/9824303.shtml)).
- 108 operational after the 41-satellite launch of 15 Jun 2023 (largest Chinese batch at the time: 9 GF-03D, 30 GF-06A, 2 Pingtai-02A, 1 Huoerguosi-1) ([NewSpace Economy](https://newspaceeconomy.ca/2026/03/20/the-jilin-1-constellation-chinas-commercial-eye-in-the-sky/)).
- 114 in orbit after a six-satellite launch, Sep 2024 ([Beijing News, 2024-09](https://m.bjnews.com.cn/detail/1726813391129293.html)); 117 at end-2024 ([NewSpace Economy](https://newspaceeconomy.ca/2026/03/20/the-jilin-1-constellation-chinas-commercial-eye-in-the-sky/)).
- 141 after Kuanfu-02B07 on the second Gravity-1 flight, Oct 2025 ([IT Home](https://www.ithome.com/0/888/707.htm)).
- ~161 launched across 30 launches as of mid-2026 (Baidu Baike English page, July 2026) ([Baidu Baike](https://baike.baidu.com/en/item/Jilin-1%20Satellites/1467323)); WMO OSCAR lists 8 Jilin-1 GF-07A/B satellites launched 14 Apr 2026 plus batches on 15 Jun 2026 ([WMO OSCAR](https://space.oscar.wmo.int/satellites/view/jilin_1)).
- KeepTrack (data as of 2026-08-13) shows only 78 catalogued objects tagged Jilin-1, 49 in orbit — a cataloguing artefact, not a real count ([KeepTrack](https://keeptrack.space/satellites/constellations/jilin-1)).
- **Target:** raised in Oct 2022 from 138 to 300 satellites, nominally for 2025; missed. Chinanews (Jul 2025) now says 300 in orbit "by end of 2027" ([Chinanews, 2025-07-20](https://www.chinanews.com.cn/cj/2025/07-20/10450887.shtml); [NewSpace Economy](https://newspaceeconomy.ca/2026/03/20/the-jilin-1-constellation-chinas-commercial-eye-in-the-sky/)).

**Fleet.** ([NewSpace Economy, 2026-03-20](https://newspaceeconomy.ca/2026/03/20/the-jilin-1-constellation-chinas-commercial-eye-in-the-sky/))
- *Shipin* video sats (8, 2015–2018): colour video 437–720 nm, ~1.13–1.2 m, 4K.
- *Gaofen-03* family (largest group): GF-03D 75 cm pan at 535 km, ~40–50 kg, nine per Long March 2D.
- *Kuanfu* wide-swath: Kuanfu-01 >136 km swath, <4 m MS, ~1,200 kg; Kuanfu-02 ~230 kg, 0.5 m, 150 km swath.
- *Gaofen-05B-01* (Nov 2024): better than 0.5 m, a Chinese commercial record.
- *Spectrum-01/02* hyperspectral (26 bands), forestry and ocean.
- *SAR-01A* (Sep 2024): the only SAR satellite as of early 2026 — limited cloud-penetrating capacity.
- Revisit claim: any point can be imaged 23–25+ times/day across the optical fleet (theoretical, clear-sky).
- Laser comms (early 2024): 10 Gbps sat-to-ground (vehicle station), 100 Gbps inter-satellite demo.

**Data products / platforms.** Sold via the JL1 Global portal and HEAD Aerospace. Products: 0.5/0.75/1 m pan, 2 m MS, video (AVI/MOV), night imagery, stereo, AI land-cover. **Jilin-1 Net** (吉林一号网, launched Apr 2024) is a "remote sensing + AI" consumer app: >130,000 registered users and >20 billion cumulative tile accesses by early 2025 ([NewSpace Economy](https://newspaceeconomy.ca/2026/03/20/the-jilin-1-constellation-chinas-commercial-eye-in-the-sky/)). **共生地球 ("Symbiotic Earth")** app, launched 2022, >3.5 M downloads; Jilin-1 online data mall (2023) with public prices from CNY 13/km² and delivery in as little as 3 minutes; >1,000 universities get free research access ([The Paper, 2026-07-08](https://m.thepaper.cn/newsDetail_forward_33540949)). "Jilin-1 Symbiotic Earth" was one of the projects in the withdrawn 2022–2024 IPO plan ([Securities Times via ifeng, 2024-12-05](https://finance.ifeng.com/c/8f3yCnTVHV0)). 2023 revenue ~USD 80 M ([Wikipedia: CIOMP](https://en.wikipedia.org/wiki/Changchun_Institute_of_Optics,_Fine_Mechanics_and_Physics)); losses every year 2019–H1 2022 (see I2).
- **Western ground-station link:** Norway's KSAT (SvalSat) was permitted to service **42 Chang Guang satellites** (licence requested 2023); Strand Consult's John Strand called it "asking for permission to run Chinese spy satellites"; NKOM threatened KSAT with a fine on 16 Apr 2026 for "illegally communicating" with five unidentified satellites (KSAT: unrelated to CGSTL); EU, Japan, Switzerland, Ukraine and Taiwan also sanction CGSTL ([Defence24, 2026-04-21](https://defence24.com/geopolitics/nato-defence-contractor-will-service-chinese-military-satellites-should-the-west-be-concerned); [Wikipedia: CIOMP](https://en.wikipedia.org/wiki/Changchun_Institute_of_Optics,_Fine_Mechanics_and_Physics), citing Newsweek).

**Problems / pain points.**
- Schedule slip: 300-satellite goal missed for 2025; launch failures lost Mofang-01A (Hyperbola-1, Nov 2022) and Gaofen-04B (Ceres-1, Sep 2023; ~USD 7.5 M insurance claim) ([NewSpace Economy](https://newspaceeconomy.ca/2026/03/20/the-jilin-1-constellation-chinas-commercial-eye-in-the-sky/)).
- Only one SAR satellite → cloud-limited coverage; commercial tasking availability opaque.
- Dual-use/legal exposure: 2017 National Intelligence Law; a 2025 US DoD report counts >100 Jilin-1 satellites in China's ISR order of battle (>359 ISR systems as of Jan 2024) ([NewSpace Economy](https://newspaceeconomy.ca/2026/03/20/the-jilin-1-constellation-chinas-commercial-eye-in-the-sky/)).
- US sanctions (see B1).

**How they're trying to solve it.** Mass production of small sats (nine per Long March 2D); consumer AI app to build demand; laser downlink; agriculture as main commercial driver; disaster support abroad (Rio Grande do Sul floods, Apr–May 2024) ([NewSpace Economy](https://newspaceeconomy.ca/2026/03/20/the-jilin-1-constellation-chinas-commercial-eye-in-the-sky/)).

**Data.** Commercial, not free. Sample/preview imagery is browsable through the Jilin-1 Net app. Jilin-1 *video* has been used in openly downloadable academic datasets (see C-section: VISO, satellite-video MOT tracks in competitions).

**Off-the-shelf tech.** Video-object tracking (ByteTrack/BoT-SORT), tiny-object detectors, super-resolution.

**Hackathon angle.** "Satellite video as a sensor": count and track vehicles/ships/aircraft in Jilin-1-type video clips from open academic datasets, and turn the tracks into a traffic or port-activity indicator. Or: a tasking-demand map that shows where 23-25 revisits/day are wasted on cloud.

**Credibility.** Counts: mixed (state media + trackers; they disagree). Specs: secondary analysis (NewSpace Economy) drawing on company claims. Sanctions: official US government.

**Sources.** Above, plus [Wikipedia: Jilin-1](https://en.wikipedia.org/wiki/Jilin-1); [SpaceMapper Jilin-1 tracker](https://spacemapper.cn/en-us/show/constellation/jilin1).

### A1-bis. Chang Guang in 2026: money, non-Earth imaging, bank and county satellites

- **Funding.** 4 Jul 2026: ~CNY 5 B (~USD 736 M) new equity from China Orient Asset Management, Shenzhen Capital Group, Chengtong Fund, Changfa Group, Lushi Investment, Haitong Innovation; includes a CNY 500 M strategic investment by the Changchun municipal government (April). **161 satellites launched** (latest 15 Jun 2026); "190 supposedly linked to the constellation"; factory capacity **200 satellites/year**; target ~300 operational ([China in Space, 2026-07-09](https://www.china-in-space.com/p/cgstl-hongqing-technology-raise-billions)).
- **Non-Earth (space-object) imaging.** 14 Apr 2026: eight Jilin-1 GF-07A/B/C satellites (~0.5 m, "onboard AI-assisted processing") on Kinetica-1 Y12 with "non-Earth target imaging as a new capability"; tested on Jilin-1 in Sep 2025, possibly in response to a US firm imaging Shijian-26 ([China in Space, 2026-04-14](https://www.china-in-space.com/p/cgstl-deploys-eight-imaging-satellite)).
- **"Finance + space."** Jilin GF-07A03 is the "Postal Savings Bank Satellite": cooperation with the Postal Savings Bank of China to monitor international projects, farmland, new-energy infrastructure and nature reserves to improve the bank's services ([China in Space, 2026-04-14](https://www.china-in-space.com/p/cgstl-deploys-eight-imaging-satellite)).
- **Local-government "vanity"/purpose satellites built by CGSTL** (15 Jun 2026, Kinetica-1 Y14): *Caiyun Optical-01* (Yunnan geology bureau — geological-disaster prevention); *Antie-03* (Anxi County, Fujian — **tea-crop monitoring**); *Lichuan Red* (Lichuan city, Hubei — ecology and **tea industry**); *Cultural Relics-01* (National Cultural Heritage Administration — **heritage-site monitoring**). All customers are Chinese government bodies ([China in Space, 2026-06-15](https://www.china-in-space.com/p/handful-of-cgstl-built-satellites)).
- **TEE-01B**, the satellite at the centre of the Iran case, was built by CGSTL ([China in Space, 2026-05-10](https://www.china-in-space.com/p/us-sanctions-three-chinese-space)).

**Problems this reveals.** Demand is heavily government-driven (cities, counties, ministries, a state bank). Each buyer gets its "own" satellite, which fragments data across many owners — a data-silo pattern (see I-section).

**Hackathon angles.**
- *Heritage-site encroachment monitor* (what "Cultural Relics-01" is bought for): Sentinel-2 + building-change detection around UNESCO sites; alerts when new construction appears inside buffer zones.
- *Tea/plantation monitor* (Antie-03, Lichuan Red): Sentinel-2 NDVI time series over tea terraces, flag frost/drought stress.
- *Bank collateral verifier* (Postal Savings Bank satellite): given a loan's farm polygon, confirm crop presence and area each season from Sentinel-2, flag mismatches.

**Credibility.** Specialist newsletter (China in Space) citing company/official Chinese announcements.

## A2. Gaofen series and CHEOS (高分专项)

**What it is.** The China High-resolution Earth Observation System (CHEOS) — "a state-sponsored, civilian Earth-observation program" for agriculture, disaster, resource and environmental monitoring. Wikipedia (edited 20 Oct 2026) lists ~35 Gaofen launches (one failure: GF-10, 2016). Key civil sensors: **GF-1** (2 m pan / 8 m MS / 4 × 16 m WFV; plus GF-1-02/03/04), **GF-2** (0.8 m pan / 3.2 m MS), **GF-3** (C-band SAR; -02, -03), **GF-4** and **GF-13** (GEO staring: 50 m VIS, 400 m MWIR), **GF-5 / 5-02 / 5-01A** (AHSI hyperspectral 30 m, 5 nm; DPC polarimeter 3.3 km; AIUS atmospheric), **GF-6** (MS with red-edge), **GF-7** (stereo 0.8 m, 2.5 m MS). Details of **GF-8, -9, -10, -11, -12 (SAR), -14** are scarce, and they "may be dual purpose supporting both civilian and military missions." ([Wikipedia: Gaofen](https://en.wikipedia.org/wiki/Gaofen))

**Data access.** Gaofen data are understood to be distributed in China via CRESDA (中国资源卫星应用中心, a Gaofen Challenge track partner per [PEdaily](https://news.pedaily.cn/20230323/53907.shtml)) and the Natural Resources Satellite Remote Sensing Cloud Service Platform ([sasclouds.com](https://www.sasclouds.com/) — JavaScript-only, terms not readable; **distribution terms unverified**). Wikipedia notes data-sharing with Roscosmos and the BRICS agreement of Aug 2021 ([Wikipedia: Gaofen](https://en.wikipedia.org/wiki/Gaofen)). **Openly downloadable Gaofen-derived research data** (no registration with Chinese agencies needed): Five-Billion-Pixels (GF-2, 150 images, 4 m, 24 classes, >50,000 km² of China, >5 billion labelled pixels) ([project page](https://x-ytong.github.io/project/Five-Billion-Pixels.html)), GID (GF-2), parts of DOTA-v2.0 (GF-2), AIR-SET (see C3).

**Problems.** Opaque, China-only ordering portals; foreigners typically cannot self-register; military-adjacent satellites mean low transparency on what is collected.

**Hackathon angle.** Use the openly released GF-2 benchmark (Five-Billion-Pixels) to train a land-cover model and test how well it transfers to Sentinel-2 over another country — a "domestic-to-global" transfer problem Chinese groups face when selling abroad.

**Credibility.** Wikipedia + project pages.

## A3. Yaogan (遥感) military reconnaissance — context item

**What it is.** PRC designation for military reconnaissance satellites (optical Jianbing-6/9/10/11/12; SAR Jianbing-5/7, Yaogan-29/33; ELINT triplets Jianbing-8 / CX-5 that likely geolocate emitters by TDOA; Yaogan-41 in GEO). Main user: PLA (formerly SSF). Infobox: 149 successes, 1 failure ([Wikipedia: Yaogan](https://en.wikipedia.org/wiki/Yaogan)). 2026 cadence: Yaogan-40-04 ELINT triplet (24 Sep 2026); six Yaogan on Long March 4B Y78 (10 Sep 2026) and another six on Long March 4B Y81 (23 Oct 2026); a third *retrograde-orbit* Yaogan (23 Oct 2026) ([China in Space archive](https://www.china-in-space.com/archive); [China in Space, 2026-09-24](https://www.china-in-space.com/p/fourth-yaogan-40-group-enters-orbit); [China in Space, 2026-10-23](https://www.china-in-space.com/p/third-retrograde-yaogan-spacecraft)). DoD (via NewSpace Economy) counted >359 Chinese ISR satellites as of Jan 2024 ([NewSpace Economy](https://newspaceeconomy.ca/2026/03/20/the-jilin-1-constellation-chinas-commercial-eye-in-the-sky/)).

**Problem/context.** For a Western/neutral audience: "who is watching my ships/bases right now?" ELINT triplets are publicly trackable via TLEs.

**Hackathon angle.** *Overhead-pass warning for maritime/humanitarian users*: compute when known Yaogan triplets and other ISR sats pass over a given area (TLEs from CelesTrak). Same engine as B2/B3.

**Credibility.** Wikipedia; China in Space.

## A4. Fengyun (风云) meteorological satellites

**What it is.** CMA-operated weather satellites built by SAST; 21 launched since 1988 in four classes. Operational in Wikipedia's table: FY-2F/G/H (GEO), FY-3C/D/E/F (polar; FY-3E is an early-morning orbit), FY-3G (precipitation radar, 50° inclination, Apr 2023), FY-4A/B (GEO). FY-1C was the target of the 2007 ASAT test (>3,000 debris items). FY-2 was marketed as "openly available" to anyone with a receiver ([Wikipedia: Fengyun](https://en.wikipedia.org/wiki/Fengyun)). (Newer launches like FY-3H / FY-4C not confirmed — see Leads not followed.)

**Data.** CMA/NSMC runs a Fengyun data portal (satellite.nsmc.org.cn) with registration-based downloads — **unverified; portal not opened in this session**. Yunyao Aerospace's commercial GNSS-RO constellation (≥34 satellites) has supplied data to CMA since 2025 ([China in Space, 2026-04-15](https://www.china-in-space.com/p/spacety-yunyao-aerospace-raise-18)).

**Hackathon angle.** Use FY-4B full-disk imagery (or GOES/Himawari analogues) to nowcast convective storms; compare with Chinese AI weather models (Fuxi) now being put in orbit (D1).

## A5. Haiyang (海洋) ocean satellites

**What it is.** NSOAS ocean satellites. Haiyang-2E (1,500 kg, CAST) launched 2 Jul 2026 on Long March 4B Y56: radar altimeter (wave height), dual-beam scatterometer (1,300 km swath, winds), microwave radiometer imager, calibration radiometer, laser retroreflector, French DORIS. 2E/2F/2G will form a three-satellite constellation replacing aging 2B/2C/2D. Fleet: HY-1C/1D (ocean colour), HY-2A–2D (dynamics), HY-3A (ocean surveillance), HY-4-01 (salinity, Nov 2024); 11 Haiyang launched since May 2002 ([China in Space, 2026-07-02](https://www.china-in-space.com/p/replacement-haiyang-2-ocean-spacecraft)).

**Problems.** HY-1 sea-ice monitoring and SAR aquaculture segmentation are explicit Gaofen Challenge tracks (C1a) — i.e., operational problems NSOAS wants solved.

**Hackathon angle.** Sea-ice edge detection in the Bohai Sea/Arctic from HY-1-like optical data (Sentinel-3 OLCI/MODIS are open substitutes).

## A6. SpaceTY / Spacety (天仪研究院) — SAR, sanctioned

**What it is.** Changsha-based small-sat maker founded 2016 (CEO Yang Feng); "satellite-as-a-service"; 30 satellites in orbit by Dec 2023; record 4 months 21 days from contract to launch. Added to a US trade blacklist in Feb 2023 for allegedly providing imagery to Wagner; Luxembourg ministries brought a case against Spacety Luxembourg S.A. in Mar 2023 ([Wikipedia: Spacety](https://en.wikipedia.org/wiki/Spacety)). In Apr 2026 raised CNY 1.3 B (~USD 190.6 M) for mass production, data services and an "own a satellite / we operate it / buy data" model; its SAR satellites use interferometry to detect millimetre-level changes, with onboard computing and laser links ([China in Space, 2026-04-15](https://www.china-in-space.com/p/spacety-yunyao-aerospace-raise-18)).
- **City-backed SAR:** Tianyi-50 "Dianjian-1" (Wuhan) — X-band SAR monitoring of **hydroelectric power plants**, 11-day revisit (15 May 2026) ([China in Space, 2026-05-15](https://www.china-in-space.com/p/cas-space-delivers-city-backed-earth)).
- **InSAR pair:** Tianyi-51 "Caiyun-SAR-01" (Yunnan geology bureau) and Tianyi-52 "Xinglianti-Tianyuan-YG-01", C-band, 3 m/25 km or 2 m/40 km, 55° inclination for daily revisit and fewer urban blind spots, launched 17 Sep 2026 on Kuaizhou-11 ([China in Space, 2026-09-17](https://www.china-in-space.com/p/expace-delivers-commercial-insar)).
- Collected X-band SAR over the Aug 2026 Nepal–Xizang flood ([China in Space, 2026-09-02](https://www.china-in-space.com/p/space-sector-mobilized-to-assist)).

**Problems.** Sanctions cut Western business; ROI of SAR for local governments; InSAR expertise is scarce among end users.

**Hackathon angle.** *Dam and slope deformation watch*: Sentinel-1 InSAR (open, via ASF/COMET LiCSAR) over a reservoir and its slopes — exactly what Wuhan bought Dianjian-1 for. Show a "risk score" per dam.

**Credibility.** Wikipedia + China in Space.

## A7. PIESAT (航天宏图) — Hongtu/PIESAT SAR constellations

**What it is.** PIESAT Information Technology is a listed geospatial-software and data firm. The first PIESAT-1 (航天宏图一号, "Hongtu-1") quartet — an interferometric SAR formation — launched in March 2023; PIESAT-2 second-generation batches reached SSO in Nov and Dec 2024; a third batch of four (PIESAT-2 -13 to -16), built by **GalaxySpace** and operated commercially by **Zhuzhou Space Interstellar Satellite Technology**, launched 19 Sep 2026 on Long March 2D Y104, bringing the 2nd-gen fleet to 12; satellites can process data onboard before downlink ([China in Space, 2026-09-19](https://www.china-in-space.com/p/commercial-sar-quartet-deployed-by)). PIESAT imaged the Nepal–Xizang flood zone in Aug 2026 ([China in Space, 2026-09-02](https://www.china-in-space.com/p/space-sector-mobilized-to-assist)).

**Problems.** (Not opened: PIESAT's financial reports; Chinese press reports of losses — see Leads not followed.)

**Hackathon angle.** Global DEM/deformation from InSAR is PIESAT-1's pitch; an open analogue is Copernicus DEM + Sentinel-1 interferograms.

## A8. MinoSpace (微纳星空) — Taijing series

**What it is.** Beijing small-sat maker. **Taijing-4** X-band SAR (~350 kg, phased array >5 m, up to 1 m, sliding spotlight + stripmap; Taijing-4 01 carries a real-time "Live Earth" payload from Capital Normal University for disaster/traffic/ship monitoring); launches 27 Feb 2022 (CZ-8), 23 Jan 2024 (Kinetica-1, with four other Taijing sats), 21 May 2025 (02A) ([Gunter's Space Page: Taijing-4](https://space.skyrocket.de/doc_sdat/taijing-4.htm)). **Taijing-3-05A/B "Rongcheng-1-01/02"** for Chengdu city (planning, development, emergencies, agriculture) launched 15 May 2026 ([China in Space, 2026-05-15](https://www.china-in-space.com/p/cas-space-delivers-city-backed-earth)). MinoSpace delivered four post-flood image sets over Nepal–Xizang by 28 Aug 2026 ([China in Space, 2026-09-02](https://www.china-in-space.com/p/space-sector-mobilized-to-assist)); partner of STAR.VISION's Space.IDC (D3).

## A9. STAR.VISION (地卫二空间技术) — AI hyperspectral exports

**What it is.** Commercial maker of AI-equipped satellites, "Oriental Smart Eye Intelligence Network." Twins **Lampung-1** (Indonesia; marine economy, environment, agriculture) and **Samarqand-2028** (Uzbekistan/Uzcosmos; agriculture, ecology in Central Asia) = Oriental Star-05/06: ~300 kg hyperspectral, 5 m, 300 km swath, 5-day revisit, 10 TB storage, onboard AI pre-processing; contracts signed May 2025 and Nov 2025, launched 5 Aug 2026 on Jielong-3 Y12 sea launch ([China in Space, 2026-08-05](https://www.china-in-space.com/p/uzbek-indonesian-satellites-launched)). Indonesia also reportedly ordered **19 more** from a state-owned enterprise ([China in Space, 2026-06-27](https://www.china-in-space.com/p/brics-space-agency-heads-consider)). STAR.VISION monitored Nepal–Xizang flood recovery (optical/pan/MS) ([China in Space, 2026-09-02](https://www.china-in-space.com/p/space-sector-mobilized-to-assist)). Its Space.IDC computing constellation is in D3.

**Problems.** Exporting satellites to countries with little in-house analytics capacity (BRICS meetings explicitly discuss "technical gaps between members" and training — [China in Space, 2026-06-27](https://www.china-in-space.com/p/brics-space-agency-heads-consider)).

**Hackathon angle.** *Hyperspectral-to-insight for a ministry with no analysts*: use open hyperspectral data (EnMAP, PRISMA, EMIT) to deliver one ready-made product, e.g., palm-oil plantation stress in Lampung or cotton water stress in Uzbekistan, with a plain-language report.

## A10. Galaxy Space (银河航天), Guangdong Tianyuan (Wuyang constellation), Xingzhong Space, Huantian Wisdom

- **GalaxySpace**: builds the PIESAT-2 SAR satellites (A7); agreed with SpaceX (Nicolls, Musk) on the need to share orbit data ([China in Space, 2026-10-15](https://www.china-in-space.com/p/spacex-wants-chinese-spacecraft-data)).
- **Wuyang ("Five Rams") constellation / Guangda-1**: Guangdong Tianyuan Technology with Guangzhou University and Guangzhou city. Xiguang-4-01 (0.5 m optical, 2 m MS, 30 m-swath IR; "full-spectrum quantitative" system) launched 21 Oct 2026 by Ceres-1S sea launch; up to **28 satellites** in low-inclination orbits by end-2028, ~30-minute revisit over southern China, SE Asia and Belt and Road countries; Emposat handled early operations ([China in Space, 2026-10-21](https://www.china-in-space.com/p/guangzhou-focused-remote-sensing)).
- **Weitong-1-01** (Xingzhong Space Jiaxing): nano EO sat with a "real-time" onboard AI model for disaster-prevention imaging (16 Mar 2026, Kuaizhou-11 Y7) ([China in Space, 2026-03-16](https://www.china-in-space.com/p/orbital-refueling-test-ai-earth-observation)).
- **Huantian Wisdom Technology**: optical change mapping over the Nepal–Xizang flood ([China in Space, 2026-09-02](https://www.china-in-space.com/p/space-sector-mobilized-to-assist)).
- **Tianyan-27 "Youxi"** (Shanghai Xuntian Qianhe): live-streams Earth views for cultural communication; tests onboard AI on "ultra-high resolution" imagery ([China in Space, 2026-05-15](https://www.china-in-space.com/p/cas-space-delivers-city-backed-earth)).

## A10-bis. Zhuhai Orbita / 航宇微 (Zhuhai-1, hyperspectral)

**What it is.** Early listed Chinese RS satellite company (ex-Orbita, renamed 航宇微, stock 300053), operator of the **Zhuhai-1 (珠海一号)** constellation — "the first constellation built and operated by a private listed company in China" — with 12 satellites in orbit in 2019 including 8 hyperspectral (OHS) ([Qianzhan, 2025-06-03](https://www.qianzhan.com/analyst/detail/220/250603-319b5c80.html); search summary of [Stockstar, 2019-11-22](https://stock.stockstar.com/SS2019112200000132.shtml)). Tracker: [SpaceMapper Zhuhai-1](https://spacemapper.cn/en-us/show/constellation/zhuhai-1).

**Problems.** Revenue collapse and losses (CNY 572 M loss in 2022), satellite-constellation gross margin 0.85%, bad debts from local governments, falling R&D; flagship contracts were Guangdong government projects ("绿水青山一张图" CNY 83.6 M; Zhuhai Doumen drainage-pipe dredging inspection CNY 64 M); participated in Hunan's hyperspectral raw-imagery procurement (2022) ([NetEase/Space & Network, 2024-03-05](https://m.163.com/dy/article/ISI3JK1V05119RIN.html)).

**Hackathon angle.** *Hyperspectral water quality for a city*: open hyperspectral (EMIT/PRISMA/EnMAP) or Sentinel-2/3 to map chlorophyll/turbidity in a city's reservoirs — exactly the kind of local-government product Orbita sold, but done with free data.

**Credibility.** Industry blog citing filings; research-firm summary.

## A10-ter. GEOVIS (中科星图, 688568) — "digital Earth" platform

**What it is.** AIRCAS-spun listed company; co-hosts the Gaofen Challenge ("中科星图杯", C1a). Products: GEOVIS Earth intelligence engine (星图地球智脑引擎, an AI-model platform), **GEOVIS Earth data cloud (星图地球数据云)** and **daily imagery (今日影像)**, supercomputing cloud network, special-domain digital Earth and 星图洛书 big-data analysis for defence and public safety, 看天 App/API; commercial-space business includes rocket/satellite electronics, the **星眼 space-awareness constellation**, the 洞察者 v4.0 TT&C system and a global ground-station network; also low-altitude (drone) economy products ([GEOVIS website](https://www.geovis.com.cn/)). Financially the healthiest listed RS firm in 2024 (gross margin 49.6%, ROE 9.6%) ([Qianzhan, 2025-06-03](https://www.qianzhan.com/analyst/detail/220/250603-319b5c80.html)). AIRCAS's open AIR-SET dataset and the RingMo models feed this ecosystem (C2, C3).

**Hackathon angle.** GEOVIS sells "daily imagery + AI engine + API" to city governments — the analogue for a hackathon is a city dashboard on Sentinel-2/Planet NICFI basemaps with an LLM query layer.

## A10-quater. Distributors and ground segment: HEAD Aerospace, Emposat

- **HEAD Aerospace** (Beijing, with subsidiaries in Hong Kong, France, Netherlands) resells Jilin-1 and other Chinese imagery internationally ([NewSpace Economy, 2026-03-20](https://newspaceeconomy.ca/2026/03/20/the-jilin-1-constellation-chinas-commercial-eye-in-the-sky/)).
- **Emposat (航天驭星)**: commercial TT&C with seven Chinese ground sites plus hosted stations on five continents; filed YX-5 (106 satellites) at the ITU; early-orbit ops for commercial launches; implicated (not sanctioned) in the TEE-01B/Iran case (B2) ([China in Space, 2026-04-19](https://www.china-in-space.com/p/emposat-denies-knowledge-of-iran); [China in Space, 2026-01-10](https://www.china-in-space.com/p/chinese-constellation-operators-submit)).

## A11. China Siwei (中国四维) — SuperView

**What it is.** CASC-owned EO operator (SuperView / 四维高景 "Siwei Gaojing" fleet), host of the "中国四维杯" competition (C1b). Operates **16 imaging satellites** with a dozen-plus more planned; set up **Hangzhou Siwei Space Intelligent Technology** (CNY 2 B registered capital; China Siwei 25%, Aerospace Investment Holdings 24%, Hangzhou West Lake Yunchuang 26%, Hangshi Technology 15%, Zhejiang funds 10%) to develop AI for satellites and their data ([China in Space, 2026-08-20](https://www.china-in-space.com/p/chinese-firms-aim-to-expand-orbital)). 2025 launches included Siwei Gaojing-1 03/04 (Long March 2C) and Siwei Gaojing-3 02 (Long March 2D) ([China in Space 2025 recap](https://www.china-in-space.com/p/china-continues-space-progress-through)). Handled imagery with CRESDA for the Aug 2026 Nepal–Xizang flood and the 2025 Myanmar earthquake relief ([China in Space, 2026-09-02](https://www.china-in-space.com/p/space-sector-mobilized-to-assist)). **SuperView Neo (四维高景)**: built by CAST; a China Siwei slide (2026) reportedly gives a 28-satellite plan with 10 in orbit — Neo-1 optical (~0.3 m pan / 1.2 m MS; Neo-1 01/02 Apr 2022, 03/04 27 Feb 2025), Neo-2 X-band SAR (reported 0.5 m; 01/02 launched 2025), Neo-3 wide-swath optical (Neo-3 01 Apr 2024, 02 on 15 Mar 2025; reported 0.5 m, 9 bands, 130 km swath) (search excerpts of [ITU seminar slide, Hu Guang, 2026-09](https://www.itu.int/high-level-seminar-space-development/wp-content/uploads/sites/83/2026/09/Hu-Guang.pdf) and [Orbit Codex](https://orbitcodex.com/operations/superview-neo-3-02); PDF too large to open). The Ukrainian State Space Agency's note on Neo-3-02 instead gives 0.3–0.5 m pan, 1.2–2 m MS, 12–15 km swath, 540 kg, ~500 km SSO and a **16-satellite** plan ([SSAU](https://spacecenter.gov.ua/novyny/informacijna-dovidka-shhodo-zapusku-ka-superview-neo-3-02.html?lang=en)) — **specs conflict; treat as unverified**.

## A12. Ziyuan (资源), Tianhui, Gaofen-14 — state mapping satellites (brief)

2025 launches: **Ziyuan-3-04** and **Tianhui-7** (cartography) on Long March 4B; **Gaofen-14-02** optical stereo mapping (Long March 3B/E); a replacement mapping satellite (Dec 2025) and a new cartography satellite (end-2025) ([China in Space 2025 recap](https://www.china-in-space.com/p/china-continues-space-progress-through); [China in Space, 2025-12-16](https://www.china-in-space.com/p/replacement-mapping-satellite-delivered); [China in Space, 2025-12-30](https://www.china-in-space.com/p/new-cartography-satellite-launched)) (last two: titles only). Use for national mapping and data distribution terms not verified in this session. **Hackathon angle:** stereo-derived DEM change (mining, landslides) using Copernicus DEM vs. newer stereo or ICESat-2.

## A13. Environment-monitoring and GHG satellites (brief)

A second environment-monitoring satellite launched on Long March 4C Y41 (17 Apr 2026) ([China in Space, 2026-04-17](https://www.china-in-space.com/p/second-environment-monitoring-satellite), title only); **Pujiang-4** CO₂/CH₄ smallsat and **Qinling-01/02** ecological sats on Kinetica-1 Y18 (20 Sep 2026) ([China in Space, 2026-09-20](https://www.china-in-space.com/p/new-orbital-compute-demonstrating)); HKUST's **MUSICO** on Tiangong (G2). **Hackathon angle:** methane super-emitter detection with open EMIT/TROPOMI data, framed against China's coal-mine methane problem.

---

# B. Sanctions, OSINT and the dual-use problem

## B1. Chang Guang sanctions (Wagner 2023; Houthis 2025; Iran 2026)

**What it is.** The US has targeted Chang Guang three times:
1. **2023** — sanctioned for allegedly providing high-resolution imagery to Russia's Wagner Group ([The National, 2025-04-17](https://thenationalnews.com/news/us/2025/04/17/china-houthis-yemen-satellite-images)).
2. **17–18 Apr 2025** — State Department spokesperson Tammy Bruce said the company was "directly supporting Iran-backed Houthi terrorist attacks on U.S. interests," following a Financial Times report that it supplied imagery the Houthis could use to target US warships and ships in the Red Sea. China's foreign ministry said it was "not familiar" with the matter ([The National, 2025-04-17](https://thenationalnews.com/news/us/2025/04/17/china-houthis-yemen-satellite-images); [Al Arabiya, 2025-04-18](https://english.alarabiya.net/News/united-states/2025/04/18/us-says-china-satellite-company-aiding-attacks-by-yemen-s-houthis); [Marine Insight](https://www.marineinsight.com/us-accuses-chinese-satellite-firm-of-helping-houthis-strike-ships-in-red-sea/)).
3. **May 2026** — designated again: Chang Guang "collected imagery of U.S. and allied military facilities to support Iranian imagery requests" and "has previously provided satellite imagery to U.S.-designated Houthis, to target U.S. military assets" ([VOA editorial, 2026-05-11](https://editorials.voa.gov/a/holding-china-accountable-for-support-of-iran/8148868.html); [JCPA Daily Alert](https://dailyalert.org/archive/index.php?id=97666)).

**Problems / pain points.** For Chinese commercial EO: loss of Western customers and of distributor channels; for the West: no way to stop commercial imagery from cueing strikes. For everyone: **no technical method to verify who sold which image**.

**Credibility.** Official (US State Department via VOA editorial); FT reporting cited secondhand; Chinese denials.

## B2. The Earth Eye Co. (TEE-01B) and Emposat — imagery for Iran (2024–2026)

**What it is.** Per a Financial Times investigation (reported by Maritime Executive, 2026-04-15): in March 2024 China gave Iran's IRGC Aerospace Force access to the TEE-01B satellite built by Beijing-based The Earth Eye Co., for about USD 37 M. TEE-01B images at ~0.5 m; launched from Jiuquan in June 2024. **Emposat** (another Beijing firm) runs the ground station in China that controls tasking; Iran accesses it remotely, so it needs no ground infrastructure at home. Similar deals appear to exist with Malaysia and Oman. FT linked satellite passes to later Iranian missile/drone strikes on Prince Sultan AB (Saudi), Muwaffaq Salti AB (Jordan), NSA Bahrain, Ali Al Salem AB (Kuwait), Erbil, and civilian sites (Duqm, Alba aluminium, Khor Fakkan port, Qidfa desalination) and for battle-damage assessment. China's MFA (Guo Jiakun, 14 Apr 2026) called the evidence "fabricated" ([Maritime Executive, 2026-04-15](https://maritime-executive.com/article/iran-using-chinese-satellite-to-target-us-and-gcc-countries); [Al Majalla](https://en.majalla.com/node/330865/science-technology/how-chinas-earth-eye-helped-iran-target-us-bases)).
- OFAC/State action of ~8 May 2026 designated Earth Eye (aliases reported as Beijing Mumei Starry Sky Technology / Beijing Mumei Xingkong Technology) and MizarVision under an Iran conventional-arms authority (search excerpt of [Vozpópuli](https://www.vozpopuli.com/indux/en/wp-json/wp/v2/posts/5571); not verified against the state.gov release "Disrupting Iran's Overseas Military Procurement Networks").
- Satellite record: [Gunter's Space Page: TEE 01](https://space.skyrocket.de/doc_sdat/tee-01.htm).
- **Details from China in Space.** TEE-01B was **built by Chang Guang** and launched June 2024; it is Earth Eye's only satellite; Earth Eye's licence (June 2024) covered crop censuses, mapping and post-disaster imaging. On 8 May 2026 the State Department sanctioned Earth Eye (沐美星空), MizarVision (觅熵) and Chang Guang; **Emposat was accused but not sanctioned**. China's MFA (11 May 2026): "China firmly opposes illicit unilateral sanctions that have no basis in international law." The newsletter judged the sanctions "unlikely to have a real-world effect"; Chang Guang and MizarVision kept communicating publicly as if no sanctions existed ([China in Space, 2026-05-10](https://www.china-in-space.com/p/us-sanctions-three-chinese-space)).
- **Emposat's denial (19 Apr 2026).** "Our global network of ground stations is entirely under our own control and operated independently"; no knowledge of Iran or other military users. Chinese sites: Beijing, Xi'an, Zhengzhou, Zhongwei, Qitaihe, Jinghe, Hebi, plus hosted stations in Africa, Asia, Europe, South America and the South Pacific ([China in Space, 2026-04-19](https://www.china-in-space.com/p/emposat-denies-knowledge-of-iran)). Emposat also does early-orbit operations for Chinese commercial sats (e.g., Xiguang-4-01, Oct 2026) and owns robotic-arm developer Suzhou Sanyuan Aerospace ([China in Space, 2026-10-21](https://www.china-in-space.com/p/guangzhou-focused-remote-sensing); [China in Space, 2026-03-16](https://www.china-in-space.com/p/orbital-refueling-test-ai-earth-observation)).
- **Iran context.** At the June 2026 BRICS space meeting, Iran's space programme was "reportedly largely destroyed" by US/Israeli action and "allegedly now reliant on a Chinese-made satellite" ([China in Space, 2026-06-27](https://www.china-in-space.com/p/brics-space-agency-heads-consider)). Also [China in Space, 2026-04-16: Iran allegedly using Chinese satellite images, surprising US Space Force](https://www.china-in-space.com/p/iran-allegedly-using-chinese-satellite) (title only, not opened).

**Problem stated plainly.** *Ground-station-as-a-service + satellite-access-as-a-service* lets a state without space infrastructure task a 0.5 m satellite remotely. Nobody outside the operator can see who tasked what.

**Hackathon angle (strong).** *"Pass-to-strike correlation"*: take public TLEs (CelesTrak/Space-Track) for a named satellite, compute its overpasses of a list of sites, and line them up against a public timeline of strikes (e.g., ACLED). The FT did this by hand; a tool that does it automatically for any satellite × any region is a clear demo.

**Credibility.** Reputable press (FT via Maritime Executive); Chinese denials; Vozpópuli item is a search excerpt.

## B3. MizarVision (Meentropy Technology (Hangzhou) Co.) — AI-annotated OSINT of US forces

**What it is.** A Chinese private firm, founded March 2021, two funding rounds, mission: "accomplishing geospatial business intelligence through artificial intelligence, building a God's-eye view no one can refuse." Since Feb 2026 it posted annotated imagery of US Gulf bases, carriers and air defences on Weibo during the run-up to and conduct of "Operation Epic Fury" against Iran ([Pekingnology, 2026-02-27](https://www.pekingnology.com/p/viral-satellite-imagery-of-us-military); [The Defense Post, 2026-03-12](https://thedefensepost.com/2026/03/12/ai-china-middle-east/amp)). It fuses satellite imagery, webcams, radar and AIS with AI ([Breached.company](https://breached.company/mizarvision-chinese-ai-satellite-us-military-tracking-2026/) — advocacy-style blog, low credibility). Designated by the State Department in May 2026 for publishing "open-source images detailing U.S. military activity during Operation Epic Fury" ([VOA editorial, 2026-05-11](https://editorials.voa.gov/a/holding-china-accountable-for-support-of-iran/8148868.html)).

**Problems / pain points — the provenance question.** Hu Bo (SCSPI, Peking University) said he is "100% sure" the images came from US and European satellites, because ephemeris data can match an image's content and timestamp to a specific satellite's position, and resolutions matched Western sensors: "This matter cannot be attributed to China." Typical sources: ~0.3 m from Vantor (formerly Maxar Intelligence); 3–5 m or 10 m wide-swath from Planet or Sentinel. A MizarVision rep said sources were "diverse, including Western and Chinese entities" ([Pekingnology, 2026-02-27](https://www.pekingnology.com/p/viral-satellite-imagery-of-us-military)). Planet reportedly said MizarVision is not a client ([search excerpt, OpenSourceForU, 2026-04](https://www.opensourceforu.com/2026/04/chinese-open-source-satellite-ai-allegedly-helped-iran-target-us-bases/)). IFRI memo: [Toward space-based intelligence for all? The case of the spring 2026 Iranian strikes](https://www.ifri.org/en/memos/toward-space-based-intelligence-all-case-spring-2026-iranian-strikes) (not opened).

**Hackathon angle (very strong, clear problem).** *"Which satellite took this picture?"* Given an image's timestamp, location, ground resolution, sun azimuth (from shadows) and view angle, rank all imaging satellites by whether they could have taken it, using public TLEs. This is the exact argument Hu Bo made by hand. Data: CelesTrak TLEs, UCS satellite database, public sensor specs. 36-hour feasible with Skyfield + a shadow-angle estimate.

**Credibility.** Official (VOA/State), reputable newsletter (Pekingnology quoting named experts), low-credibility blogs flagged.

---

# C. AI for remote sensing: competitions, foundation models, benchmarks

## C1. Chinese remote-sensing interpretation competitions — literal problem statements

### C1a. "中科星图杯" International Gaofen Remote Sensing Image Interpretation Competition (Gaofen Challenge)
**What it is.** Run since 2017 by AIRCAS (Aerospace Information Research Institute, CAS), co-organised with IEEE GRSS and ISPRS, co-hosted by GEOVIS (中科星图) and Xiamen University; track partners CRESDA (中国资源卫星应用中心), NSOAS (国家卫星海洋应用中心) and Chang Guang. Sample data "fully domestic," including civilian Gaofen and domestic commercial data ([PEdaily, 2023-03-23](https://news.pedaily.cn/20230323/53907.shtml)). The 2020 edition had six tracks (detection and segmentation) with results in IEEE JSTARS vol. 14 ([Notice of 2020 Gaofen Challenge](https://radars.ac.cn/news/Announcements/8bbd8b05-69b8-47c3-be8c-d624617e443f_en.htm); [GRSS 2021 call for papers](https://www.grss-ieee.org/publications/call-for-papers/2021-gaofen-challenge-on-automated-high-resolution-earth-observation-image-interpretatio/); [RSLab UniTN 2020](https://rslab.disi.unitn.it/?p=4528)).

**5th edition (2023) tracks — literal problem statements** ([PEdaily, 2023-03-23](https://news.pedaily.cn/20230323/53907.shtml)):
1. 高分辨率可见光中多类目标细粒度检测识别 — fine-grained multi-class object detection/recognition in high-res optical.
2. 面向海洋一号可见光图像中海冰目标监测 — sea-ice monitoring in Haiyang-1 optical imagery.
3. 高分辨率SAR图像中近海养殖场分割 — segmentation of offshore aquaculture farms in high-res SAR.
4. 高分辨率可见光图像中建筑物普查与变化检测 — building census and change detection.
5. 高分辨率光学卫星视频中多目标跟踪 — multi-object tracking in optical satellite video.
6. 高分SAR图像中飞机目标细粒度检测识别 — fine-grained aircraft recognition in SAR.

**Data.** The AIRCAS AICyber team says it has supported the Gaofen Challenge and IEEE GRSS DFC for seven years and released the **AIR-SET (空天·四象)** high-resolution, multi-sensor, fine-grained dataset worldwide; the same data underpins the RingMo (空天·灵眸) foundation model ([National Remote Sensing Bulletin cover story, 2024-07-15](https://www.ygxb.ac.cn/zh/news/164648)).

**Hackathon angle.** Each track is a ready-made problem. Most hackable with open data: (2) sea-ice from HY-1/Sentinel-2/MODIS; (3) offshore aquaculture rafts from Sentinel-1 SAR — a real coastal-management problem in China, SE Asia and Chile; (4) building change detection with LEVIR-CD/WHU.

**Credibility.** Official organiser announcements, peer-reviewed results papers.

### C1b. "中国四维杯" 6th International High-Resolution Remote Sensing Image Intelligent Interpretation Competition (Dec 2025)
Organised by the China Remote Sensing Application Association (中国遥感应用协会), hosted by China Siwei (中国四维测绘技术有限公司), finals 5 Dec 2025 at Chongqing Engineering Polytechnic; affiliated with the 39th National Youth S&T Innovation Competition. Themes: multi-source fusion, intelligent interpretation algorithms, scenario-based industry applications; "通过遥感数据+算法模型深度挖掘信息价值" ("mine information value through remote sensing data + algorithm models"). >40 teams (PKU, Wuhan U, SYSU, BNU, CUMT…), 17 finalists; judging chaired by Wen Jiangping of the Beijing Institute of Remote Sensing Information (a military-linked institute). Track details not published in the article ([China.com Tech, 2025-12-09](https://m.tech.china.com/hea/articles/20251209/202512091778393.html)).

### C1c. Tianzhi Cup (天智杯) AI Challenge — the military's space-AI contest

**What it is.** "An AI technology contest for space applications," **guided by the CMC Equipment Development Department (军委装备发展部) and hosted by the Equipment Department of the Military Aerospace Force (军事航天部队装备部)**; aims to "推进人工智能技术在航天应用领域快速应用、深度应用" ("push rapid, deep application of AI in space applications") ([4th Tianzhi Cup notice, May 2024, PDF](https://tianzhibei.com/api/v1/file/download/data_sets/20240604c1df5bdb-cc71-433c-90bb-8fb7c84595ec.pdf)) **[official notice]**.

**4th edition (2024)** — four domains with 6/3/2/2 subjects: **遥感数据智能应用** (remote-sensing data intelligent application), **智慧地球** (smart Earth), **太空数据智能化处理应用** (space-data intelligent processing), **航天器智能管控** (intelligent spacecraft management and control). Full subject texts were posted only on the internal "全军武器装备采购信息网" network. Online-preliminary subjects named in the notice's flowchart (remote-sensing domain):
1. **高分辨率可见光图像民用车辆智能定位与分类** — intelligent localisation and classification of *civilian vehicles* in high-res optical imagery.
2. **多源卫星图像民航飞机智能定位与分类** — localisation and classification of *civil airliners* in multi-source satellite imagery.
3. **面向国土资源普查的智能任务规划** — intelligent (satellite) task planning for a national land-resources census.
4. **基于大模型的遥感图像内容生成** — large-model-based remote-sensing image *generation* (an "exploratory" subject with no prize).
Format: online preliminary on public data (1 Jun – 31 Aug 2024) → top 10 teams *with security clearance* to an offline semi-final on non-public data in Beijing → top 5 to the October final. Prizes funded as projects: CNY 1 M / 300 k / 200 k per subject (search excerpt cites a CNY 18 M total pool, [AITOP100](https://www.aitop100.cn/infomation/details.html?id=18838)). Offline entrants need an employer with "三级以上保密资质" (level-3+ secrecy qualification); all members must be PRC nationals; hardware for the RS domain was a single TITAN V workstation ([notice PDF](https://tianzhibei.com/api/v1/file/download/data_sets/20240604c1df5bdb-cc71-433c-90bb-8fb7c84595ec.pdf)).

**3rd edition (final 17 May 2023, Beijing):** 145 organisations, **1,782 teams**; domains: remote-sensing intelligent interpretation, environmental-data processing, space-data processing ([BUAA News, 2023-05-23](https://news.buaa.edu.cn/info/1002/58919.htm)). NWPU won the **态势感知数据智能化处理** ("situational-awareness data processing") track — detecting and locating targets in "multi-source, massive detection data" with complex backgrounds and wide domain spread ([NWPU, 2023-05-20](https://hangtian.nwpu.edu.cn/info/1804/21731.htm)).

**1st edition (final 18 Dec 2019):** surveying/geographic and meteorological/hydrological data; subjects included **地物要素智能提取** (intelligent extraction of ground-feature elements) and **地形数据快速生成** (rapid terrain-data generation); 104 teams from >70 institutions ([SJTU AIPT lab, 2019-12-25](https://aipt.sjtu.edu.cn/Data/View/306)).

Related: BIT faculty list Tianzhi Cup wins alongside the 眼神杯 ([BIT](https://radar.bit.edu.cn/szdw/jsfc/ktyg1/bcbf1934f77e4f4ab0718ebb31a74b2c.htm)); the 2018 眼神杯 had optical target recognition (54 teams), SAR target recognition (40), satellite-video tracking (22) and task-driven compression (7) ([36Kr, 2018-06-05](https://www.36kr.com/p/1722569801729)). **2025 (5th) Tianzhi Cup subjects: not found.**

**Hackathon angle.** Subjects 1–3 translate directly to public data: civilian vehicle/aircraft detection (DOTA, FAIR1M, xView), and **satellite tasking optimisation for a land census** (given AOIs, cloud forecasts and satellite passes from TLEs, plan which satellite images which tile when) — a clean optimisation problem with a map demo.

**Credibility.** Official PDF notice + university news pages. Note the military sponsor (relevant to how the team presents the problem).

### C1d. Related non-Chinese contests with Chinese-relevant problem statements
- IEEE GRSS Data Fusion Contest 2025: all-weather land-cover and building-damage mapping from multimodal SAR + optical; DFC 2026: InSAR analysis on high-resolution X-band SAR time series ([GRSS: In focus DFC](https://www.grss-ieee.org/resources/news/in-focus-data-fusion-contest-promotes-innovative-solutions/); [GRSS: Inside the 2026 DFC](https://www.grss-ieee.org/resources/news/in-focus-inside-the-2026-ieee-grss-data-fusion-contest/)). (Search excerpts; pages not opened.)
- PBVS/CVPR Multi-modal Aerial View Image Challenge — SAR classification (2024–2025) ([CVPRW 2025 paper](https://openaccess.thecvf.com/content/CVPR2025W/PBVS/html/Inkawhich_4th_Multi-modal_Aerial_View_Image_Challenge_SAR_Classification_-_PBVS_CVPRW_2025_paper.html)).
- NTIRE 2026 infrared remote-sensing super-resolution (InfraredSR dataset) — 4th-place write-up on CSDN ([GitCode/CSDN](https://gitcode.csdn.net/69fc9d0b54b52172bc724207.html)).

### C1e. 2025 Qizhi Cup (启智杯) — literal problem statements

First Qizhi Cup algorithm competition by **Qiyuan Lab (启元实验室)**, 20 May – 25 Jul 2025, **1,022 teams** ([China.com Tech, 2025-08-15](https://m.tech.china.com/articles/20250815/202508151714990.html)):
1. **Robust instance segmentation of satellite RS images** — large resolution/size variation, occlusion, blur, cross-sensor domain shift, small objects and **out-of-distribution / unknown categories** (final round tested zero-shot segmentation on known + unknown classes). Winner (SCUT): Co-DETR + auxiliary heads + SAM pseudo-labels.
2. **UAV ground-object detection on embedded platforms** (Huawei **Ascend 310B**), judged on accuracy, then inference efficiency, deployment stability and field tests: "在端侧平台上高效运行，参赛队伍需在「看得准」与「跑得快」之间取得极致平衡" ("teams must strike the best balance between 'seeing accurately' and 'running fast' on edge platforms"). Winner: YOLOv11 → Co-DETR with RFLA/ATSS.
3. **Adversarial robustness of multimodal large models** on visible-light RS images — VQA, captioning, change detection; 20 GB model cap, single-GPU time limit. Winner (SYSU): **Qwen2.5-VL-7B-Instruct** + self-built RS data + curriculum multi-task fine-tuning + adaptive image enhancement.

**Hackathon angle.** Track 3 is very hackathon-friendly: *"Can you fool a satellite-image chatbot?"* — red-team an open RS VLM (GeoChat/LHRS-Bot/Qwen-VL) with adversarial patches or prompt attacks on public imagery, then build a defence. Clear problem, clear demo.

**Problem pattern across Chinese contests.** The same handful of operational problems recur year after year: fine-grained ship/aircraft recognition (optical and SAR), building change detection, satellite-video multi-object tracking, sea ice, aquaculture, and compression. These are what CRESDA, NSOAS and Chang Guang ask contest organisers to set — i.e., what the operators themselves cannot yet do well.

## C2. Chinese remote-sensing foundation models and vision-language models

**Context.** China dominates the academic RS foundation-model literature. A community list (Awesome-Remote-Sensing-Foundation-Models, maintained by the SkySense author's GitHub account) shows dozens of Chinese-origin entries from 2022–2026 ([GitHub list](https://github.com/Jack-bo1220/Awesome-Remote-Sensing-Foundation-Models)).

| Model | Who | What | Release / licence | Source |
|---|---|---|---|---|
| **SkySense** (CVPR 2024) | Wuhan University + Ant Group authors (Ant Group not named on repo) | "Billion-scale" multimodal (optical + SAR, temporal) model; 21.5 M temporal sequences; 16 datasets / 7 tasks; beats 18 RSFMs | Weights released Jun 2024 (Swin V2-Huge HR backbone; ViT-L S2/S1 backbone); **non-commercial research only** | [arXiv 2312.10115](https://arxiv.org/abs/2312.10115); [GitHub](https://github.com/Jack-bo1220/SkySense) |
| **SkySense++** (Nature Machine Intelligence, 2025-08) | Wuhan U | Semantic-enhanced multimodal; RS-Semantic pretraining (13 pixel-labelled datasets incl. Five-Billion-Pixels, LoveDA, FLAIR, JL-16); 12 tasks in 7 domains; 1-shot flood eval (Flood-3i) | Code + weights (Mar 2025), non-commercial; data on Zenodo | [GitHub](https://github.com/kang-wu/SkySensePlusPlus) |
| **SkySense V2** (ICCV 2025) | Ant Group / Wuhan U authors | Single transformer backbone for all modalities + MoE; +1.8 avg over SkySense | Not confirmed | [arXiv 2507.13812](https://arxiv.org/abs/2507.13812) |
| **SkySense-O** (CVPR 2025) | — | Open-world / open-vocabulary RS interpretation | GitHub zqcrafts/SkySense-O | [list](https://github.com/Jack-bo1220/Awesome-Remote-Sensing-Foundation-Models) |
| **SkySenseGPT** | Wuhan U / Ant | RS VLM; FIT-RS 1,800,851 instruction samples; relation reasoning, scene graphs | Dataset/code on GitHub | [arXiv 2406.10100](https://arxiv.org/abs/2406.10100) |
| **RingMo (空天·灵眸)** family | AIRCAS (CAS Aerospace Information Research Institute) | RingMo (TGRS 2022), RingMo-Sense, RingMo-Lite, RingMoGPT (TGRS 2024), RingMo-Aerial (TPAMI 2025), RingMamba, **RingMoE (TPAMI 2026)**; built on AIR-SET data | Partial (GitHub comeony/RingMo) | [list](https://github.com/Jack-bo1220/Awesome-Remote-Sensing-Foundation-Models); [NRSB cover story](https://www.ygxb.ac.cn/zh/news/164648) |
| **RingMo-Agent** (arXiv 2025, v3 Aug 2026) | AIRCAS (Sun Xian, Fu Kun) | Unified VLM over optical, SAR, IR from satellite and UAV; RS-VL3M (>3 M image-text pairs) | Not confirmed | [arXiv 2507.20776](https://arxiv.org/abs/2507.20776) |
| **CGEarthEye** (arXiv 2025-07) | Authors likely from Chang Guang (not confirmed on page) | Vision FM for **Jilin-1** imagery; JLSSD 15-million-scale multi-temporal SSL dataset, global, quarterly; 5 backbones, 2.1 B params total; 10 benchmarks | Not confirmed | [arXiv 2507.00356](https://arxiv.org/abs/2507.00356) |
| **SpectralGPT** (TPAMI 2024) | Danfeng Hong et al. (AIRCAS) | 3D GPT for spectral imagery; >600 M params; 1 M spectral images | GitHub danfenghong/IEEE_TPAMI_SpectralGPT | [arXiv 2311.07113](https://arxiv.org/abs/2311.07113) |
| **HyperSIGMA** (TPAMI 2025) | Wuhan U (Zhang Liangpei, Du Bo et al.) | Hyperspectral FM, >1 B params; HyperGlobal-450K | GitHub WHU-Sigma/HyperSIGMA | [arXiv 2406.11519](https://arxiv.org/abs/2406.11519) |
| **EarthGPT / EarthGPT-X / EarthMarker** | Zhang Wei et al. | MLLM for optical, SAR, IR; MMRS-1M (>1 M pairs from 34 datasets) | GitHub wivizhang | [arXiv 2401.16822](https://arxiv.org/abs/2401.16822) |
| **LHRS-Bot / LHRS-Bot-Nova** (ECCV 2024; ISPRS 2025) | Nanjing University | RS MLLM aligned with volunteered geographic info (OSM); LHRS-Align, LHRS-Instruct, LHRS-Bench | GitHub NJU-LHRS | [arXiv 2402.02544](https://arxiv.org/abs/2402.02544) |
| **GeoRSCLIP + RS5M** (TGRS 2024) | Zhang Zilun et al. (Zhejiang U / Om AI) | ~5 M RS images with English captions (~500 GB) | MIT (repo) | [GitHub RS5M](https://github.com/om-ai-lab/RS5M) |
| Others (Chinese-origin, from list) | various | RemoteCLIP, SkyEyeGPT (NWPU), RSGPT, GeoGround, VHM (OpenDataLab), Falcon (TianHui Lab), SegEarth-R1/R2, UrbanLLaVA (Tsinghua), FUSAR-KLIP / FUSAR-GPT (Fudan, SAR), SARATR-X & SAR-JEPA (SAR ATR), CrossEarth / CrossEarth-SAR, AgriFM (RSE 2026), **AIEarth (Alibaba Cloud platform)** | mostly GitHub | [list](https://github.com/Jack-bo1220/Awesome-Remote-Sensing-Foundation-Models) |

**Problems / pain points.**
- Licences: the best Chinese models (SkySense family, LoveDA data) are **non-commercial only** — useful for a hackathon, not for a product.
- Onboard models are "loaded before launch and mostly limited to image interpretation that speeds up filtering" (Chinese RS academics, Feb 2025, via [China in Space, 2026-08-15](https://www.china-in-space.com/p/why-are-more-of-chinas-satellites)).
- Models trained on Chinese/Google Earth imagery transfer poorly to other sensors and regions (the reason for CrossEarth, LoveDA's urban/rural domain-adaptation split).

**Off-the-shelf tech for a hackathon.** SkySense weights (HR + S2/S1), GeoRSCLIP for zero-shot retrieval, LHRS-Bot/EarthGPT for natural-language Q&A over imagery, SARDet-100K-pretrained detectors for SAR ships; all via GitHub.

**Hackathon angle.** *"Ask the satellite"*: plug GeoRSCLIP/SkySense embeddings into a natural-language search over a Sentinel-2 mosaic of one region ("find new solar farms", "find aquaculture rafts"). Clear demo, public data.

**Credibility.** Peer-reviewed (CVPR, TPAMI, NMI, TGRS) and arXiv preprints.

## C3. Chinese benchmark datasets (openly downloadable)

| Dataset | Maker | Content | Licence / access | Source |
|---|---|---|---|---|
| **DOTA v1.0/1.5/2.0** | Wuhan U (CAPTAIN-WHU) | Oriented object detection. v2.0: 18 classes, 11,268 images, 1,793,658 instances; Google Earth, **GF-2**, aerial | Licence not stated on page; dev kit + AerialDetection (70 baselines) | [DOTA](https://captain-whu.github.io/DOTA/) |
| **iSAID** | Wuhan U | Instance segmentation on DOTA images (Jun 2019) | eval server since Dec 2019 | [DOTA page](https://captain-whu.github.io/DOTA/) |
| **FAIR1M** | AIRCAS (Sun Xian et al.) | >1 M instances, >15,000 images, 5 categories / 37 fine-grained subcategories, oriented boxes | — | [arXiv 2103.05569](https://arxiv.org/abs/2103.05569) |
| **LoveDA** | Wuhan U RSIDEA (Zhong Yanfei) | 5,987 images, 0.3 m, Nanjing/Changzhou/Wuhan, 7 classes; urban↔rural domain adaptation | **CC BY-NC-SA 4.0**; Zenodo; in TorchGeo/MMSeg | [GitHub](https://github.com/Junjue-Wang/LoveDA) |
| **Five-Billion-Pixels / GID** | Wuhan U (Tong Xin-Yi) | **GF-2**, 150 images, 4 m, 24 classes, >50,000 km² | open; Google/Baidu Drive | [project page](https://x-ytong.github.io/project/Five-Billion-Pixels.html) |
| **LEVIR-CD** | Beihang U | 637 pairs 1024² at 0.5 m, Texas, 2002–2018, 31,333 building changes | academic only | [LEVIR](https://justchenhao.github.io/LEVIR/) |
| **VISO** | NUDT (Hu Qingyong) | **Jilin-1 satellite video**, 40 videos, 12000×5000 px, 853,911 boxes (plane, car, ship, train); detection + SOT + MOT; data authorised by Chang Guang | **CC BY-NC-SA 4.0**; Google Drive / BaiduYun | [GitHub](https://github.com/QingyongHu/VISO) |
| **SARDet-100K** (NeurIPS 2024 spotlight) | Nankai U et al. | First COCO-scale multi-class SAR detection set, merged from 10 datasets; MSFA pretraining | GitHub zcablii/SARDet_100K | [arXiv 2403.06534](https://arxiv.org/abs/2403.06534) |
| **AIR-SET (空天·四象)** | AIRCAS AICyber | High-res, multi-sensor, fine-grained classification set; underlies RingMo | "open worldwide" | [NRSB cover story, 2024-07-15](https://www.ygxb.ac.cn/zh/news/164648) |
| **RS5M** | Zhejiang U | ~5 M RS image-caption pairs | MIT | [GitHub](https://github.com/om-ai-lab/RS5M) |
| **JL-16** | (Jilin-1 based) | pixel-annotated set used in SkySense++ RS-Semantic | Zenodo (via SkySense++) | [GitHub SkySense++](https://github.com/kang-wu/SkySensePlusPlus) |

**Hackathon angle.** VISO is the single most "China-specific" open dataset: real Jilin-1 video. *Port/airport activity index from satellite video* — run a MOT tracker on VISO, convert tracks into counts per minute, and show how a 30-second clip becomes an economic indicator.

---

# D. Space computing

## D1. Three-Body Computing Constellation (三体计算星座) — ADA Space (国星宇航) + Zhejiang Lab (之江实验室)

**What it is.** A "thousand-satellite-scale space computing infrastructure" built by Zhejiang Lab "with global partners," under the slogan "计算上天、星间互联、模型上天" ("computing into space, inter-satellite interconnection, models into space") ([Xinhua, 2026-02-13](https://www.news.cn/20260213/d985035629be4998bcb3086d1f4b6ecb/c.html)) **[state media]**.

**Timeline.**
- 14 May 2025: first 12 satellites on Long March 2D from Jiuquan ([SpaceNews, 2025-05-14](https://spacenews.com/china-launches-first-of-2800-satellites-for-ai-space-computing-constellation/); [China Daily, 2025-05-15](https://subsites.chinadaily.com.cn/gansu/jiuquan/2025-05/15/c_1093072.htm)). Catalogued as SCS-01 A–M, NORAD 63982–63993, ~97.4°, ~430–520 km ([CyberMaxTools tracker](https://cybermaxtools.com/orbital-compute/project/ada-space-three-body-constellation/)).
- Claimed specs for the first 12 (secondary sources): 5 POPS combined, 30 TB storage, laser ISL up to 100 Gbps ([OODA Loop](https://oodaloop.com/briefs/technology/china-launches-first-of-2800-satellites-for-ai-space-computing-constellation/)); 744 TOPS per satellite ([Bursa.ro](https://www.bursa.ro/china-launches-first-space-supercomputer-constellation-26997551)); ultimate 1,000 POPS ([Business Today, 2025-05-17](https://www.businesstoday.in/amp/science/story/rival-to-global-data-centres-china-launches-12-ai-satellites-in-bid-to-outpace-earths-top-supercomputers-from-space-476682-2025-05-17)).
- Feb 2026: "inter-satellite networking breakthrough"; six satellites linked; 10 AI models/apps deployed and verified, 6 models updated in orbit. Two 8-billion-parameter models (a remote-sensing model and an astronomical time-domain model). Two satellites carry an X-ray polarimeter; on-board GRB identification "while greatly reducing downlinked data and processing time, maintained 99% event identification accuracy" (在极大减少下传数据和数据处理时间的同时，保持了高达99%的事件识别准确率). Models are validated in a ground digital twin, then pushed to any node via a space-based distributed OS. Li Chao (chief technical engineer): "把模型送上天，是推动人工智能在太空应用与发展的关键" ("Getting models into space is key to AI in space") ([Xinhua, 2026-02-13](https://www.news.cn/20260213/d985035629be4998bcb3086d1f4b6ecb/c.html)) **[state media]**. ADA Space also claimed an 8-day continuous laser link between two satellites up to 1,000 km apart, 99.99% uptime (search excerpt; [China in Space](https://www.china-in-space.com/p/ada-space-eyes-launching-2800-ai)).
- Jun 2026 (SpaceNews excerpt): 11 AI models across six interlinked satellites; ultimate goal 1,000 satellites delivering one exaFLOP ([SpaceNews, 2026-06-04](https://spacenews.com/china-builds-institutional-framework-for-space-computing-push/), excerpt only).
- 24 Jul 2026: Lijian-1 Y15 launched **Jitianxing A-04 "Cloud Tip Muxi" (云尖沐曦号)** (computing sat, validates MetaX GPUs, carries Zhejiang Lab's "embodied intelligence satellite model" for autonomous health management and single/multi-satellite task planning) and **Xiguang-2 03 "Xinghuo Chuanming" (星火传明)** meteorological sat carrying **Fuxi (伏羲)** and **Dayu (大禹)** weather models (Fudan U + Shanghai Academy of AI for Science) and **Puyun (璞云)** (Hangzhou Mita Carbon Intelligence). Goal: shift from "单星智能" to "多星协同智能" (single- to multi-satellite collaborative intelligence) and "fundamentally change how weather forecasts are produced" ([Science and Technology Daily, 2026-07-24](https://www.stdaily.com/web/gdxw/2026-07/24/content_552976.html)) **[state media]**.
- Mid-July 2026: deal with SenseTime to deploy a small constellation by end-2026 (search excerpt; [China in Space](https://www.china-in-space.com/p/ada-space-eyes-launching-2800-ai)).
- Oct 2026: China in Space tracker counts **20 satellites launched (groups of 12 and 8)** plus the Jitian A-04 test satellite ([China in Space megaconstellation tracker, 2026-10-14](https://www.china-in-space.com/p/chinas-mega-constellations-mega-article)). SpaceNews (15 Oct 2026) reported Long March 12 and Zhuque-2E launches that "add space computing sats" (headline/excerpt: [SpaceNews](https://spacenews.com/chinese-launches-boost-guowang-constellation-add-space-computing-sats/)).

**Targets.** ~100 satellites by 2027, ~1,000 by 2032; at full scale "a satellite will pass over any point on Earth about every three minutes" (届时全球任意地点每三分钟就有一颗卫星经过上空). ADA Space separately pitches 2,800 sats (ITU-filed "Star Compute") ([China Daily, 2026-07-29](https://www.ehangzhou.gov.cn/2026-07/29/c_298438.htm); [Science and Technology Daily](https://www.stdaily.com/web/gdxw/2026-07/24/content_552976.html)). A third-party site says a 2025 target of >50 satellites was missed ([SpaceNexus](https://spacenexus.us/orbital-data-centers/zhejiang-lab-three-body), unverified).

**Problems / pain points (as stated by the project).** Li Chao (Zhejiang Lab): because of limited ground-station bandwidth and transmission delays, "less than 10 percent of their data can be effectively used"; ground processing takes "hours or even days"; "One remote-sensing satellite can generate about 0.1 petabyte of data per day"; processing projected volumes would need ~100,000 ground servers ([China Daily via eHangzhou, 2026-07-29](https://www.ehangzhou.gov.cn/2026-07/29/c_298438.htm)) **[state media; promotional figure, not independently measured]**. China Mobile/Tsinghua slides at IETF 125 make the same "<10% of valid data can be transmitted" claim ([IETF 125 slides](https://datatracker.ietf.org/meeting/125/materials/slides-125-space-consideration-for-space-based-computing-infrastructure-network-00)).

**Applications claimed.** Autonomous fire detection and real-time alerts; crop-yield monitoring; on-orbit tracking of air pollution; GRB triage; smart cities; natural-resource surveys ([China Daily, 2026-07-29](https://www.ehangzhou.gov.cn/2026-07/29/c_298438.htm); [Xinhua, 2026-02-13](https://www.news.cn/20260213/d985035629be4998bcb3086d1f4b6ecb/c.html)).

**Off-the-shelf tech.** Quantised small vision models (YOLO-nano, MobileSAM), on-board cloud masking, neural feature compression for downlink ([FOOL, arXiv 2403.16677](https://arxiv.org/pdf/2403.16677)); "cloud-native satellites" case study ([arXiv 2307.08530](https://arxiv.org/pdf/2307.08530)).

**Hackathon angle.** *"The 10% problem"*: build a simulated on-board triage filter — given a Sentinel-2 tile stream and a downlink budget, decide what to send (cloud-free, changed, fire-positive) and show how much more useful information reaches the ground per pass. Clear problem statement straight from the project's own words.

**More 2026 milestones (China in Space).**
- **Mar 2026 — robots tasked from orbit:** with Shanghai Jiao Tong University, voice commands to the open-source agent OpenClaw were sent up to the satellites for inference and the decisions beamed down to a humanoid and a quadruped robot. Xinhua (18 Mar): "This task pioneers the deployment of AI Token-calling services in space." The constellation has run **Alibaba Cloud's Qwen3** and ≥10 models. Group 3 = 14 satellites needing a 3,000 kg-to-525 km SSO launch in Q4 2026; up to 1,000 sats by 2030, ~2,800 by ~2035 ([China in Space, 2026-03-19](https://www.china-in-space.com/p/ai-constellation-successfully-tasks)).
- **Jun–Jul 2026 — customers:** strategic AI agreement with **Tencent** (Jun), with Shanghai Meteorological Bureau; existing customers Alibaba Cloud and SJTU; **SenseTime deal** signed at WAIC 18 Jul 2026 — a dedicated "SenseTime Space Computing Constellation" by end-2026, enough satellites for "orbit-and-Earth" infrastructure by 2028, up to 1,000 by 2030. SenseTime co-founder Yang Fan: "space-based computing power can effectively fill in the gaps in terrestrial coverage" (disaster relief, ships, wilderness). The ITU praised the constellation at AI for Good 2026 ([China in Space, 2026-07-28](https://www.china-in-space.com/p/ada-space-signs-deal-with-sensetime); [China in Space, 2026-06-19](https://www.china-in-space.com/p/ada-space-signs-strategic-ai-agreement)).
- **3 Aug 2026:** 8-day continuous laser link demo ([China in Space, 2026-08-03](https://www.china-in-space.com/p/three-body-computing-constellation), title only).
- **14 Oct 2026 — "Star Computing Plan" Group-02 (星算计划02组):** eight computing satellites (serials 39, 44–50) on LandSpace's Zhuque-2E Y4 from Jiuquan, plus Laser Starcom's Guangchuan-03/04 laser-comm test sats; constellation now **20 satellites**; goals: more onboard compute, laser links to ground, **unfurlable cooling radiators**. Jiuquan gave a commercial launch priority over a Long March 4 for the first time ([China in Space, 2026-10-14](https://www.china-in-space.com/p/three-body-computing-constellation-316)).
- Thermal AI (热数科技) supplied >300 thermal components for Group 1 in ~2.5 months ([China in Space, 2026-08-20](https://www.china-in-space.com/p/chinese-firms-aim-to-expand-orbital)).

**Credibility.** Mostly state media and company claims; specs from secondary sources disagree.

## D1-bis. Onboard AI is becoming standard on Chinese EO satellites

**What it is.** "Four out of five customer payloads" on Kinetica-1 Y15 (24 Jul 2026) carried AI ([China in Space, 2026-07-24](https://www.china-in-space.com/p/ai-utilizing-spacecraft-brought-to)). Examples:
- **Luojia-3-01** (Wuhan U): by 2023 trialled onboard pre-processing of images into useful data; based on a 2019 Wuhan U + DFH Satellite paper arguing for "intelligent" on-board processing ([DOI 10.11947/j.AGCS.2019.20190454](https://xb.chinasmp.com/), cited by [China in Space, 2026-08-15](https://www.china-in-space.com/p/why-are-more-of-chinas-satellites)).
- **Weitong-1-01** nano EO (Xingzhong Space) — real-time onboard model for disaster prevention ([China in Space, 2026-03-16](https://www.china-in-space.com/p/orbital-refueling-test-ai-earth-observation)).
- **Xiguang-2-01** hyperspectral; **Xiguang-2-03 "Fuxi"** meteorological (200 kg; IR at 1.28/5/12.5 m; onboard processing; 100 Gbps laser downlink; first of up to **230** satellites) ([China in Space, 2026-07-24](https://www.china-in-space.com/p/ai-utilizing-spacecraft-brought-to)).
- **Gande-1-01** (Liangxi Space / Aotian Technology): debris-monitoring sat with an onboard model that separates human-made objects from stars in wide-field images; first of a constellation for tracking and emergency alerts; reportedly imaged the Falcon 9 second stage days before it hit the Moon (5 Aug) ([China in Space, 2026-07-24](https://www.china-in-space.com/p/ai-utilizing-spacecraft-brought-to); [China in Space, 2026-08-15](https://www.china-in-space.com/p/why-are-more-of-chinas-satellites)).
- **Jilin-1 GF-07** (0.5 m, onboard AI-assisted processing); **STAR.VISION** hyperspectral exports; **PIESAT-2** SAR; **SpaceTY InSAR** — all advertise onboard processing (A1-bis, A6, A7, A9).

**Problem being solved (in their words).** Each satellite has only short passes over China-based ground stations; data volumes keep rising; downlinking everything is impractical; halting imaging means lost revenue. Onboard AI skips cloud and irrelevant scenes (e.g., urban areas when monitoring the Three-North Shelter Forest / "Great Green Wall") and keeps only useful data for the next pass ([China in Space, 2026-08-15](https://www.china-in-space.com/p/why-are-more-of-chinas-satellites)).

**Limits.** Models are "loaded before launch and mostly limited to image interpretation that speeds up filtering"; better space-grade chips and thermal management are needed (Chinese RS academics, Feb 2025, via [China in Space](https://www.china-in-space.com/p/why-are-more-of-chinas-satellites)).

**Hackathon angle.** *Mission-specific onboard filter*: for one mission (e.g., desertification front along the Three-North Shelter belt, or wildfire), build a tiny model that decides keep/drop per Sentinel-2 tile and report "useful pixels per downlinked MB" vs. naive downlink.

## D2. China's space-computing industrial policy (2026)

**What it is.** In April 2026 MIIT signalled policies to speed up "space computing." Zhao Ce (MIIT ICT development dept.) cited real-time in-orbit processing, low-cost energy and wide-area coverage and said the government will "strengthen systematic planning, deepen industrial cultivation"; support for radiation-hardened chips and inter-satellite laser comms. A space-computing professional committee — "China's first industrywide coordination platform" for the field — was set up in Beijing under a CAICT-initiated body; topics: onboard AI chips, thermal control, space PV. Xie Lina (CAICT): disaster warning and resource monitoring processing could drop "from hours to seconds"; China is in the "first tier" with in-orbit networking of computing satellites. Cited market projection: in-orbit data centres USD 39.09 B by 2035 (BIS Research) ([China Daily, 2026-04-10](https://mobile.chinadaily.com.cn/html5/2026-04/10/content_001_69d7ef8ced50be540e72e28a.htm)) **[state media]**. SpaceNews (excerpt): Beijing-backed Orbital Chenguang raised Pre-A1 funding and secured USD 8.4 B in credit lines in April 2026 ([SpaceNews, 2026-06-04](https://spacenews.com/china-builds-institutional-framework-for-space-computing-push/), excerpt). The 15th Five-Year Plan (adopted March 2026) reportedly includes an integrated sky-earth system combining communications, navigation, remote sensing and computing; CASC called for gigawatt-scale space computing over 2026–2030 (single-source search excerpts; [CCPIT](https://en.ccpit.org/infoById/77c1945234ae11f196230242ac1a0702/4); [Ukrainian Space Agency news digest](https://spacecenter.gov.ua/novyny/kitaj-stvoryuye-institucijnu-osnovu-dlya-prorivu-v-kosmichnix-obchislennyax.html?lang=en)).

- **Governance (Jun 2026).** Two MIIT-supervised bodies: the **Space Computing Technical Group (太空算力专业委员会)** under CAICT (software/applications, after the April 2026 Space Computing Industry Conference) and the **Space Computing Working Group (太空计算工作委员会)** under the China Computer Industry Association (hardware; set up 3 Jun 2026; >100 firms want to join). A grant challenge funds **10 projects/year at CNY 10 M each**. LandSpace experts estimate space computing and other deployments could need **500 launches/year** ([China in Space, 2026-06-24](https://www.china-in-space.com/p/china-moves-to-manage-space-based)).
- **MIIT 15th FYP for the ICT industry (7 Sep 2026, 20 pages):** integrate LEO/MEO/GEO connectivity constellations with terrestrial networks; 100 Gbps laser throughput with onboard processing; "explore forward-looking research and ecosystem development in space computing power technologies"; national compute to grow from **1,590 EFLOPS (2025) to 9,800 EFLOPS (2030)**; an Aug 2025 "Guiding Opinions" targets >10 M users on space-based services by 2030 ([China in Space, 2026-09-11](https://www.china-in-space.com/p/miit-looks-to-integrate-connectivity)).

**Credibility.** State media + SpaceNews excerpt + specialist newsletter summarising official documents; some items single-source.

## D3. Other Chinese orbital-compute players (2026)

- **STAR.VISION Space.IDC (太空之弦计算星座)** — announced 25 Sep 2026: ~1,080 spacecraft by 2035 (~720 inference, ~360 general compute); G1 40–60 PFLOPs/11.5 kW, G2 160–310 PFLOPs/48 kW, G3 460–1,000 PFLOPs/140 kW; CNY 10 B credit lines from ICBC and Agricultural Bank of China; partners include Baidu AI Cloud, MinoSpace, Hongqing Technology, UCAS Hangzhou, Xidian Hangzhou; no ITU filings yet ([China in Space, 2026-09-29](https://www.china-in-space.com/p/starvision-unveils-spaceidc-computing)).
- **Star Hub Plan (星枢计划)** — announced at WAIC Jul 2026: 1,000 computing sats (800 central + 200 edge); Shanghai Xingshu Tiansuan + Fudan University, Shanghai government support; **Xuntian Qianhe** shipped its XS-01 compute demo with a "large" onboard model on 10 Aug 2026 ([China in Space, 2026-08-20](https://www.china-in-space.com/p/chinese-firms-aim-to-expand-orbital)).
- **Orbital Chenguang (轨道辰光)** — incubator of the Beijing Astro-Future Institute of Space Technology; **CNY 57.7 B (~USD 8.5 B) strategic credit** from major banks for a decade-long orbital data-centre plan (China in Space dates it May 2026; SpaceNews's excerpt says "$8.4 billion in credit lines in April" alongside a Pre-A1 round — same deal, differing dates/exchange rates; [SpaceNews, 2026-06-04](https://spacenews.com/china-builds-institutional-framework-for-space-computing-push/); [China in Space, 2026-04-23](https://www.china-in-space.com/p/china-seriously-backs-space-based), title only); earlier backers Lenovo and the Beijing government (≥CNY 140 M, Jun 2025); plans a 16-spacecraft constellation of laser-linked gigawatt-scale data centres in 700–800 km SSO in the early 2030s and aims to prove cost parity with ground data centres by 2030 ([China in Space, 2026-02-04](https://www.china-in-space.com/p/potential-space-data-centers-attracts)); Chenguang-1 (Tianyi-48) launched 24 Jul 2026 to demo thermal dissipation and power management for space data centres, "first in a planned series ahead of gigawatt-class compute centers" ([China in Space, 2026-06-24](https://www.china-in-space.com/p/china-moves-to-manage-space-based); [China in Space, 2026-07-24](https://www.china-in-space.com/p/ai-utilizing-spacecraft-brought-to)).
- **Chaozhisuan-1 (超智算一号)** — Chaozhisuan Beijing (founded Jul 2024); laser links + 4 m camera; alliance with Zhipu AI, SenseTime, Beijing Wenge, Tsinghua (Mar 2026). **PEGA-SUS1** (Peng Cheng Lab + SUSTech, built by GalaxySpace, ~150 kg): 5G NTN base station, 100 Gbps laser, onboard AI. Both launched 20 Sep 2026 on Kinetica-1 Y18 (same launch: Pujiang-4 CO₂/CH₄ monitor, Qinling-01/02 ecology sats) ([China in Space, 2026-09-20](https://www.china-in-space.com/p/new-orbital-compute-demonstrating)).
- **China Siwei → Hangzhou Siwei Space Intelligent Technology** (CNY 2 B registered capital) to develop AI for satellites and their data; China Siwei operates **16 imaging satellites**, a dozen+ more planned ([China in Space, 2026-08-20](https://www.china-in-space.com/p/chinese-firms-aim-to-expand-orbital)).
- **Thermal AI (热数科技)** flexible radiators (>10 kW, ~2 kg/m²); **Nayuta Space** "Ālaya" concept turning reusable second stages into compute platforms ([China in Space, 2026-08-20](https://www.china-in-space.com/p/chinese-firms-aim-to-expand-orbital); [China in Space, 2026-07-01](https://www.china-in-space.com/p/nayuta-space-exploring-using-rockets)).

**Problems.** Heat rejection; radiation-hard chips; finance is bank credit lines rather than revenue; overlapping 1,000-satellite plans with no stated customers beyond AI firms.

---

# E. Megaconstellations and debris

## E1. Qianfan / Thousand Sails (千帆) — Shanghai Spacesail (垣信卫星)

**What it is.** Shanghai-government-backed LEO broadband constellation (formerly "G60 Starlink"), up to ~15,000 satellites by 2030; Gen-1 sats 267 kg with krypton Hall thrusters; Gen-2 400–500 kg, Gen-3 ~1,500 kg planned ([China in Space, 2026-10-14](https://www.china-in-space.com/p/chinas-mega-constellations-mega-article)).

**Status.** 238 launched on 14 launches (6 Aug 2024 – 5 Jul 2026, MIIT/CelesTrak); CelesTrak active list ~257 (Oct 2026). Jonathan McDowell (10 Sep 2026): 239 in orbit, 217 working (177 in the ~1,069 km operational shell), **22 failed, including 16 of the 18 from the October 2024 launch**. CelesTrak flagged 18 as "partially operational" with perigees 789–968 km. Seven-month launch pause in 2025 after thruster/gyroscope failures; resumed 7 Apr 2026. Officials' "in orbit" counts can include failed satellites ([azmth tracker](https://azmth.space/tracker/qianfan), citing planet4589.org and CelesTrak; [Orbital Radar](https://orbitalradar.com/satellite-internet/guowang-qianfan)).
- Targets: 324 in 2026, 324 in 2027, 4,000 each in 2028–29, 5,000 in 2030 (Dec 2025 plan); the earlier 648-by-2025 target was missed ([China in Space](https://www.china-in-space.com/p/chinas-mega-constellations-mega-article); [azmth](https://azmth.space/tracker/qianfan)).
- **Revenue: zero in Q1 2026** (Caixin, 2026-06-23, cited by [azmth](https://azmth.space/tracker/qianfan)); no commercial service start found as of mid-Sep 2026.
- Overseas: Brazil (Telebras MoU Nov 2024; Anatel approved up to 324 sats on 12 Feb 2026, rights to Jul 2031), Malaysia (MEASAT MoU Feb 2025), Thailand (NT, Apr 2025), Airbus in-flight connectivity (Dec 2025), trials in Malaysia/Mongolia/Kazakhstan ([azmth](https://azmth.space/tracker/qianfan); [ChoZan](https://chozan.co/spacesail/)).

**Debris.** The Long March 6A upper stage from the first Qianfan launch (6 Aug 2024) broke up after deployment; US Space Command reported >300 trackable pieces at the time; CelesTrak listed **705 debris objects** from that launch as of 14 Sep 2026, 129 re-entered ([azmth](https://azmth.space/tracker/qianfan)).

**Problems.** Satellite reliability (~9% failed), orbit-raising failures, missed targets, zero revenue, ITU milestone pressure, upper-stage breakups at ~800 km where debris lingers.

**Hackathon angle.** *"Is this satellite dead?"* Classify satellites as working/failed/drifting from public TLE histories (stalled orbit raising, plane drift, decaying perigee) — McDowell does this by hand. Apply to Qianfan and compare with official "in orbit" claims. Public data: CelesTrak GP history, Space-Track.

**Credibility.** Trackers citing official and independent sources (McDowell is the standard independent reference); Caixin reputable.

## E2. Guowang (国网) — China Satellite Network Group (中国星网)

**What it is.** State-backed LEO broadband constellation of up to ~13,000 satellites. Targets (Dec 2025): 310 in 2026, 900 in 2027, 3,600/yr in 2028–2030. 222 launched across 27 groups by mid-Oct 2026 plus three GEO support satellites and 33 test sats ([China in Space, 2026-10-14](https://www.china-in-space.com/p/chinas-mega-constellations-mega-article)). Wikipedia (Sep 2026): 27 experimental, 3 HEO/GEO, 204 LEO; a Long March 12 launch on 9 Oct 2026 carried Hulianwang 215–222 ([Wikipedia: Guowang](https://en.wikipedia.org/wiki/Guowang)). KeepTrack: 222 catalogued, ~258 real once 36 unsorted sats are counted ([KeepTrack](https://keeptrack.space/live-count/how-many-chinese-satellites-are-in-orbit)). Most batches fly on Long March 8A and Long March 12 from the Hainan commercial site.

**Problems.** Launch cadence vs ITU milestones; trackers disagree on counts; Long March 12 lower stages reportedly fell in Philippine waters (search excerpt, [Space Launch Schedule](https://www.spacelaunchschedule.com/space-news/long-march-12-launches-despite-recent-7a-failure-long-march-2c-launches-satellite-for-uae/)).

## E2-bis. Deployment bottlenecks and upper-stage debris (2026)

- As of 26 May 2026: Qianfan 9 launches / 162 sats (groups of 18); Guowang 21 launches / 168 sats (groups of 5, 9 or 10); Amazon Leo 11 launches / 302 sats. Qianfan sats ~267 kg; Guowang 695–1,000 kg. Bottlenecks: only state-owned launchers from three distant sites shared with government/military payloads; outsourced satellite production; Qianfan satellites "stranded themselves" → missions halted, hardware sent back to factories, seven-month gap until April 2026 ([China in Space, 2026-05-28](https://www.china-in-space.com/p/can-chinas-mega-constellations-deploy)).
- **Upper stages:** >30 upper stages (mostly Long March 6A) remain in orbit, tracked decaying from ~900 km to ~650 km (*Integrity Flash*, 18 May 2026, via [China in Space](https://www.china-in-space.com/p/can-chinas-mega-constellations-deploy); [ISR University Issue 145](https://isruniversity.com/2026/05/19/issue-145/)). They are left there because the constellations operate >1,000 km and lower release saves fuel. Jim Shell (LinkedIn, 26 May 2026) said China is leaving a large amount of mass in LEO, behind Russia and the US. China's rules now require commercial operators to deorbit stages; state firms follow UN guidelines ([China in Space, 2026-05-28](https://www.china-in-space.com/p/can-chinas-mega-constellations-deploy)).
- **Fragmentations:** four Long March 6A second stages fragmented 2022–2024; a Long March 12 second stage surrounded itself with debris (end-2024); **Yaogan-50 (02) broke up (Sep 2026):** the reconnaissance satellite itself (launched 15 Mar 2026 on a Long March 6A from Taiyuan into a rare ~142° retrograde orbit at ~952 km) "suffered an unidentified anomaly and broke apart"; the US Space Force had catalogued **43 debris objects by 4 Sep 2026** (Jonathan McDowell), spread over ~600–1,100 km, where decay takes centuries; cause unknown (propulsion, battery or collision hypothesised); China described the Yaogan-50 series as for land surveys, crop-yield estimation and disaster prevention ([Gizmodo, 2026-09-08](https://gizmodo.com/chinese-satellite-breaks-apart-in-rare-orbit-that-could-hold-debris-for-centuries-2000808645)). KeepTrack lists 62 new pieces over 21 days for the event (search excerpt, [KeepTrack fragmentation tag](https://keeptrack.space/tag/fragmentation)); other coverage: [NewsBytes](https://www.newsbytesapp.com/news/science/chinas-yaogan-50-02-breakup-scatters-43-fragments-could-last-centuries/tldr), [Daily Galaxy](https://dailygalaxy.com/2026/09/chinese-satellite-shattered-space-debris/). China in Space instead describes a Long March 6C (6A-family) second stage fragmenting "alongside" Yaogan-50-02 — **sources disagree on whether the satellite or a stage broke up; Gizmodo/McDowell say the satellite**. CASC's Party Group (8 Sep 2026) admitted a "**severe quality challenge**", ordered self-inspection of "laxness, looseness, and softness," "look-back" reviews, halting work with unresolved risks, and public shaming for non-compliance; reposted by CAST, CALT, SAST and the Academy of Aerospace Liquid Propulsion ([China in Space, 2026-09-09](https://www.china-in-space.com/p/state-owned-firms-vow-to-improve)).
- Other 2026 failures: Long March 7A exploded ~1 min after liftoff (Aug 2026, lost a ChinaSat spacecraft); Long March 3B/E late-ascent failure; Tianlong-3 maiden failure (Apr 2026, propellant leak); Ceres-2 debut failure (faulty nozzle); Kuaizhou-11 Y13 "disappeared after liftoff" (Jun 2026) ([China in Space, 2026-09-09](https://www.china-in-space.com/p/state-owned-firms-vow-to-improve); [China in Space, 2026-08-10](https://www.china-in-space.com/p/chinasat-spacecraft-lost-in-failed); [China in Space, 2026-09-12](https://www.china-in-space.com/p/debut-tianlong-3-flight-failed-due); [China in Space, 2026-06-20](https://www.china-in-space.com/p/galactic-energy-says-ceres-2-debut); [China in Space, 2026-06-17](https://www.china-in-space.com/p/expace-rocket-disappears-after-liftoff)) (titles from archive; first two opened).

**Hackathon angle.** *Upper-stage watchlist*: list every Chinese upper stage in LEO from public catalogues, flag those at fragmentation-prone altitudes/ages (Long March 6A family), estimate decay time and debris exposure for each constellation shell. Clear "who is at risk from what" output. (Overlaps with the debris slice.)

## E2-ter. Starlink–China coordination (Oct 2026)

At IAC 2026 (6 Oct, Türkiye) SpaceX's Michael Nicolls said operators are not sharing enough ephemeris data; a slide showed **Chinese operators as the largest group not sharing data with SpaceX** ("not unique to China"). SpaceX coordinates with CMSA on Tiangong and with select Chinese operators; GalaxySpace agreed on sharing; SpaceX's "Stargaze" SSA platform has been open since Aug 2026; the UN launched a Satellite Operator Contact Hub in Sep 2026; Chinese academics proposed Hong Kong as a global orbit-management hub; China expanded orbital observation via ground telescopes in APSCO member states ([China in Space, 2026-10-15](https://www.china-in-space.com/p/spacex-wants-chinese-spacecraft-data); [China in Space, 2026-10-07](https://www.china-in-space.com/p/experts-say-why-hong-kong-should)). (Chinese papers on countering Starlink — not reached; see Leads not followed.)

**Hackathon angle.** *Ephemeris-sharing gap map*: compare operator-published ephemerides (where available) vs. TLE-only objects and show which conjunctions are "blind" — a visual, policy-relevant demo.

## E2-quater. China's UN complaint about Starlink, close approaches, and the 200,000-satellite ITU filings

- **UN complaint (29 Dec 2025).** At a UN Security Council Arria-Formula meeting on LEO megaconstellations, China's representative criticised Starlink and others: two close approaches to Tiangong forcing manoeuvres (the 2021 formal protest went through UNOOSA); a Starlink satellite breakup (17 Dec 2025, ~418 km, hundreds of tracked pieces) posing risks to developing countries with limited tracking; use of commercial firms for military reconnaissance and battlefield comms; unlicensed service over foreign territory; use by "terrorist, separatist, and telecom fraud groups" in the Sahel, South Asia and SE Asia. "China calls on the relevant country to earnestly fulfill its obligations" ([China in Space, 2026-01-05](https://www.china-in-space.com/p/china-lodges-informal-complaint-against)). SpaceX announced (1 Jan 2026) it would lower nearly half the constellation (~4,400 sats), cutting decay time by >80% ([same](https://www.china-in-space.com/p/china-lodges-informal-complaint-against)).
- **Close approach (12 Dec 2025).** SpaceX said an object from the 10 Dec 2025 Kinetica-1 launch (nine satellites, international and Chinese customers) passed ~200 m from STARLINK-6079 at 560 km ~48 h after deployment; Nicolls: lack of ephemeris coordination "needs to change." CAS Space said launch windows are screened with a ground-based awareness system and it owns none of the nine satellites ([China in Space, 2025-12-13](https://www.china-in-space.com/p/spacex-alleges-close-approach-of)).
- **ITU filings (late Dec 2025).** GalaxySpace: **Galaxy-SAR-2 (96 SAR sats)** + BlackSpider-3 (81); Emposat YX-5 (106, likely launch-TT&C relay); Guodian Gaoke Tianqi 1,132; Spacesail 1,296; China Mobile L1 (2,520) + M1 (144); and a new Xiong'an institute's **CTC-1 and CTC-2, 96,714 satellites each (193,428 total)**. Chinese megaconstellation plans rose from 50,730 to **249,250** spacecraft. ITU milestones: 10% in 2 years, 50% in 5, 100% in 7. Chinese commentators suggested the CTC filings may be meant to challenge the ITU's first-come-first-served system ([China in Space, 2026-01-10](https://www.china-in-space.com/p/chinese-constellation-operators-submit); see also [China in Space, 2026-01-14](https://www.china-in-space.com/p/chinese-news-outlets-say-giant-constellation), title only).

- **Chinese research on countering Starlink.** An AP review (Aug 2025) counted **at least 64 papers** on Starlink by PLA-affiliated researchers, government cybersecurity teams and state universities since the Ukraine war began. Proposals: small satellites with corrosive chemicals to degrade batteries/solar panels; a "tailing" fleet of microsatellites to gather data, jam or disrupt with ion thrusters; signal jamming; supply-chain cyber exploitation (2023 paper by China's Industrial Control Systems CERT); diplomatic pressure on Starlink's foreign contracts; **commercial telescopes to track satellites**. A 2023 NUDT paper frames Starlink's integration into US military space assets as a strategic advantage ([KTVU/FOX, citing AP, 2025-08-01](https://www.ktvu.com/news/china-starlink-countermeasures)). The best-known earlier paper (2022), led by Ren Yuanzhen of the Beijing Institute of Tracking and Telecommunications (PLA SSF): "A combination of soft and hard kill methods should be adopted to make some Starlink satellites lose their functions and destroy the constellation's operating system" (search excerpt of [Legal Insurrection, 2022-05](https://legalinsurrection.com/2022/05/chinese-military-planning-to-target-elon-musks-starlink-satellites/amp); original in *Modern Defence Technology*, not opened) **[reputable wire via local TV; blog for the 2022 quote]**.

**Problem.** "Paper satellites" and spectrum warehousing: filings vastly exceed launch capacity (~200 Chinese satellites launched in 2025).

**Hackathon angle.** *Filing-vs-reality tracker*: scrape ITU SNS/SpaceExplorer filings for Chinese (and other) constellations and compare with catalogued launches → show milestone shortfalls and deadlines. Clear, data-driven, policy-relevant.

## E3. Honghu-3 (鸿鹄-3), Geely, Tianqi
- **Honghu-3**: LandSpace (48% of Hongqing Technology) JV, up to 10,000 sats, first launch pending ([China in Space](https://www.china-in-space.com/p/chinas-mega-constellations-mega-article)).
- **Geely Future Mobility Constellation (Geespace)**: 6,012 planned; 64 launched vs. 72 phase-one target (2022–2025) — missed.
- **Tianqi** (Guodian Gaoke) IoT: 1,132 planned; 41 launched.
([China in Space, 2026-10-14](https://www.china-in-space.com/p/chinas-mega-constellations-mega-article); [CircleID](https://circleid.com/%20posts/chinese-leo-satellite-internet-update-guowang-qianfan-and-honghu-3))

---

# F. Commercial launch and what it means for EO costs

## F1. Reusability milestones (Dec 2025 – Oct 2026)

| Vehicle | Operator | Event | Source |
|---|---|---|---|
| **Zhuque-3** | LandSpace | Flight 1 (3 Dec 2025): orbit reached, landing failed ("abnormal combustion"). **Flight 2 (19 Aug 2026 CST)**: first Chinese first-stage *land* landing (Minqin County, Gansu, ~390 km downrange) — booster later caught fire and tipped over (partial failure); carried Hongqing's flat-packed **Honghu-03** demo sat (radiator, electric propulsion, 100 Gbps laser). Block 1: 11.8 t LEO expended / 8 t recovered; Block 2 claim 21.3 t / 18.3 t / 12.5 t RTLS; goal 20 flights per booster; first reflight may carry Qianfan | [Wikipedia: Zhuque-3](https://en.wikipedia.org/wiki/Zhuque-3); [China in Space, 2026-08-19](https://www.china-in-space.com/p/landspace-recovers-chinas-second); [China in Space, 2026-08-22](https://www.china-in-space.com/p/zhuque-3-booster-damaged-after-first) |
| **Long March 12A** | SAST | First flight 23 Dec 2025, orbit reached, landing failed; Y2 recovery attempt NET Oct 2026. ~9 t LEO expended / ~6 t recovered | [Wikipedia: Long March 12A](https://en.wikipedia.org/wiki/Long_March_12A); [China in Space, 2025-12-23](https://www.china-in-space.com/p/shanghai-academy-debuts-reusable) |
| **Long March 10B** | CALT | **First Chinese orbital booster recovery**: 10 Jul 2026, caught on tensioned steel wires by drone ship *Linghangzhe* ~430 km downrange; payload Chuangxin-26 (CAS microsat academy, possibly Guowang-related); 16 t to 200 km with reuse | [China in Space, 2026-07-10](https://www.china-in-space.com/p/china-recovers-rocket-booster-debuts) |
| Long March 12B | — | Debut 1 Jun 2026 with 2 Qianfan sats | [China in Space, 2026-06-01](https://www.china-in-space.com/p/long-march-12b-debuts-with-qianfan) |
| Zhuque-2E | LandSpace | 6 t LEO / 4 t to 500 km SSO; flew Three-Body Group-02 and Qianfan (Sep 2026) | [China in Space, 2026-10-14](https://www.china-in-space.com/p/three-body-computing-constellation-316) |
| Kinetica-1 / -2 | CAS Space | ~10 Kinetica-1 per year; main rideshare for EO smallsats (Jilin-1, city sats); sea launch from 2026; Kinetica-2 reuse by 2028 | [China in Space, 2026-04-14](https://www.china-in-space.com/p/cgstl-deploys-eight-imaging-satellite); [archive](https://www.china-in-space.com/archive) |
| Ceres-1 / 1S / 2, Pallas-1 | Galactic Energy | Ceres-1S sea launches (e.g., Xiguang-4-01, 21 Oct 2026); Ceres-2 debut failed (faulty nozzle); Pallas-1 first flight 1 Sep 2026 | [China in Space, 2026-10-21](https://www.china-in-space.com/p/guangzhou-focused-remote-sensing); [China in Space, 2026-06-20](https://www.china-in-space.com/p/galactic-energy-says-ceres-2-debut) |
| Tianlong-3 | Space Pioneer | Maiden flight failed Apr 2026 (propellant leak, low altitude) | [China in Space, 2026-09-12](https://www.china-in-space.com/p/debut-tianlong-3-flight-failed-due) |

**Cadence.** CASC planned 100 launches in 2024 but flew 68; 93 in 2025; industry expects up to 140 in 2026; Zhuque-2E Y4 on 14 Oct 2026 was China's 72nd launch of 2026. CGWIC offers **54 rideshare opportunities to foreign satellites (Aug 2026 – end-2027)**, 50–17,900 kg, SSO/LEO; no prices published; CGWIC has launched 106 international and 326 domestic satellites since 1980 ([China in Space, 2026-05-04](https://www.china-in-space.com/p/china-opens-dozens-of-rocket-launches); [China in Space, 2026-10-14](https://www.china-in-space.com/p/three-body-computing-constellation-316)).

**What it means for EO.** Cheap, frequent rideshares (Kinetica-1, Jielong-3, Ceres-1S, Kuaizhou-11) are why **cities, counties and agencies can buy their own satellites** (A1-bis, A6, A8, A10). Reusability mainly targets megaconstellations (Qianfan/Guowang/Honghu) and computing constellations; LandSpace experts talk of 500 launches/year being needed ([China in Space, 2026-06-24](https://www.china-in-space.com/p/china-moves-to-manage-space-based)). No Chinese per-kg prices were found in sources read this session.

**Problems voiced by Chinese actors (Two Sessions, Mar 2026).** Qianfan's Zhang Qi (CPPCC) called for cheaper, more frequent launches, a "dynamic adjustment mechanism" for launch missions, supply-chain cost support and *financial stability help for operators*; CASC's Li Lin: commercial space needs better component/material supply chains, shared standards and lower costs; several delegates proposed talent pipelines ([China in Space, 2026-03-13](https://www.china-in-space.com/p/reusable-rockets-deep-space-exploration)).

**Hackathon angle.** *Rideshare matchmaker / EO mission cost calculator*: given an EO requirement (revisit, resolution, region), estimate how many smallsats and which Chinese/Western rideshares would meet it, versus buying data from existing constellations — a "build vs. buy" tool for the many local governments now buying satellites.

---

# G. Human spaceflight and exploration (brief)

## G1. Shenzhou-20 debris strike (Nov 2025)

Commander Chen Dong found window damage during final checks before the planned 5 Nov 2025 return; CMSA said the capsule "does not meet the safety requirements for a crewed return," most likely from "an external impact from space debris." Crew (Chen Dong, Chen Zhongrui, Wang Jie) returned on Shenzhou-21 on 14 Nov; Shenzhou-22 launched uncrewed on 25 Nov carrying a repair kit; cracks penetrated the first of three glass layers; Shenzhou-20 landed empty on 19 Jan 2026 at Dongfeng ([SpacePolicyOnline](https://spacepolicyonline.com/news/chinese-spacewalkers-inspect-damaged-shenzhou-20-window/); [SpacePolicyOnline: returns empty](https://spacepolicyonline.com/news/repaired-shenzhou-20-returns-to-earth-empty/); [Universe Today](https://universetoday.com/articles/chinese-astronauts-return-after-a-delay-imposed-by-space-junk); [Tribune India](https://www.tribuneindia.com/news/science-technology/chinese-astronauts-return-to-earth-after-vessel-damaged-by-space-debris); [hjkc.de](https://www.hjkc.de/_blog/26899-raumfahrt-some-of-the-cracks-had-penetrated-through-chinese-astronauts-reveal-new-details-about-spac/)).

**Debris size (preliminary):** Shenzhou designer Jia Shijin (CCTV, via Reuters, 1 Dec 2025): "Our preliminary judgement is that the piece of space debris was smaller than 1 millimetre"; "The resulting crack extends over a centimetre"; "we can't directly examine it in orbit, we will study it closely when Shenzhou-20 returns." The worst case was the crack spreading, cabin depressurisation and high-speed gas ingress. CMSA's Ji Qiming said the uncrewed return would "obtain the most authentic experimental data" ([Reuters via Dunya News, 2025-12-01](https://dunyanews.tv/en/Technology/921166-damaged-shenzhou20-spacecraft-to-return-to-earth-uncrewed-for-inspect)). SCMP described it as a fragment "about the size of a grain of dust" (search excerpt, [SCMP](https://scmp.com/news/china/science/article/3334943/space-follower-first-responder-how-china-pulled-shenzhou-rescue-mission); 403 on fetch).

Crew account (press meeting 16 Jan 2026): Chen Dong saw "a triangular crack on the window," judged it "in the outermost glass layer and had penetrated through"; ~20 days from discovery to return and Shenzhou-22's docking (China's first "emergency response" launch); crews hope future crews will "dress our space home in complete 'protective clothing and safety armor'" ([China in Space, 2026-01-21](https://www.china-in-space.com/p/shenzhou-20-crew-respond-to-questions)). The first Shenzhou-21 spacewalk inspected the damage and installed protective hardware ([China in Space, 2025-12-09](https://www.china-in-space.com/p/first-shenzhou-21-spacewalk-inspects), title only).

**Problem.** Sub-centimetre debris is untrackable yet can disable a crew vehicle; China had no "lifeboat" ready, exposing the need for a standby vehicle. **Hackathon angle:** flux estimator for Tiangong's orbit using ESA MASTER/NASA ORDEM-style models + public catalogue — probably belongs in the debris slice.

## G2. Lunar and planetary (brief)

- **Chang'e-6**: 1,935.3 g of far-side samples from Apollo basin (SPA), landed 1 Jun 2024, returned 25 Jun 2024; international payloads from France, Italy, Sweden, Pakistan; for Chang'e-5, international sample access began ~3 years after return ([Wikipedia: Chang'e 6](https://en.wikipedia.org/wiki/Chang%27e_6)).
- **Chang'e-7**: south-pole orbiter + lander + rover + hopper (into a permanently shadowed crater with water/hydrogen-isotope analysers), 21 payloads incl. 6 foreign (Bahrain, Egypt, Russia, Thailand, Italy, ILOA). The Aug 23–24 2026 window was scrubbed ("does not meet launch conditions"); rolled back 24 Aug; launch now **Feb–Mar 2027**, reason undisclosed ([Wikipedia: Chang'e 7](https://en.wikipedia.org/wiki/Chang%27e_7); [China in Space, 2026-08-31](https://www.china-in-space.com/p/change-7-moon-launch-moved-to-early)). Chang'e missions are now managed by CMSA ([China in Space, 2026-08-18](https://www.china-in-space.com/p/change-missions-are-now-managed-by), title only).
- **Lunar water-ice model for Chang'e-7** (CAS NSSC et al., *Planetary Science Journal*): thermal model of Shackleton crater using **NASA LRO terrain**, validated with **LRO Diviner** temperatures and **Chandrayaan-1** ice detections; "Most of the surface of lunar regolith inside Shackleton crater is favorable for the stable preservation of water ice" ([China in Space, 2026-03-01](https://www.china-in-space.com/p/scientists-publish-model-of-potential)). → Chinese mission planning depends on US/Indian open data.
- **Tianwen-2**: launched 28 May 2025; arrived at Kamoʻoalewa 4 Jul 2026; sampling Jul 2026 – Apr 2027; departs 24 Apr 2027; capsule lands 29 Nov 2027; then comet 311P (Jan 2035) ([Wikipedia: Tianwen-2](https://en.wikipedia.org/wiki/Tianwen-2)).
- **Tianwen-3** Mars sample return: launch 2028 on two Long March 5s, samples ~2031; international instruments invited ([China in Space, 2026-03-13](https://www.china-in-space.com/p/reusable-rockets-deep-space-exploration)).
- **ILRS**: 13 countries (China, Russia founding 2021; Venezuela, South Africa, Azerbaijan, Pakistan, Belarus, Egypt, Thailand, Nicaragua, Serbia, Kazakhstan, Senegal), plus APSCO, Univ. of Sharjah, SANSA etc.; basic station by 2035; Chang'e-8 (2028) ISRU test, carries Pakistan's rover Jinnah-1 ([Wikipedia: ILRS](https://en.wikipedia.org/wiki/International_Lunar_Research_Station)).
- **Tiangong as an EO platform**: HKUST's **MUSICO** (Multi-Spectral Imaging Carbon Observatory) — CO₂ and CH₄ over low/mid latitudes — installed outside the station and observing from Jul 2026 ([China in Space, 2026-07-06](https://www.china-in-space.com/p/tiangong-begins-monitoring-greenhouse)). Also Pujiang-4 CO₂/CH₄ smallsat (Sep 2026) ([China in Space, 2026-09-20](https://www.china-in-space.com/p/new-orbital-compute-demonstrating)). Wukong AI assistant aboard Tiangong since Aug 2025 ([China in Space, 2026-02-27](https://www.china-in-space.com/p/chinas-space-enterprises-quietly)).
- SMILE (ESA–CAS space-weather mission) launched on Vega-C 19 May 2026 ([China in Space, 2026-05-19](https://www.china-in-space.com/p/vega-c-successfully-places-sino-european), title only).

**Hackathon angle (exploration).** *Lunar cold-trap ranking*: reproduce the Shackleton ice-stability idea with open LRO LOLA/Diviner data and rank candidate hopper targets — space science slice may cover this.

---

# H. Policy and data access

## H1. National policy documents touching EO data (2025–2026)

- **15th Five-Year Plan (adopted Mar 2026):** remote-sensing satellites "to be built and shared jointly, forming an integrated space-air-ground service system that combines communication, navigation, sensing, and computing"; faster LEO internet; reusable rockets; Long March 9; ILRS; near-Earth asteroid defence; "active space defense and swarm intelligence control research"; Wenchang as a world-class commercial spaceport. CASC focus areas: debris monitoring/early warning/removal and a role in writing international rules; "Tiangong Kaiwu" asteroid-mining study; gigawatt-scale space computing ([China in Space, 2026-03-13](https://www.china-in-space.com/p/reusable-rockets-deep-space-exploration)).
- **CNSA "Action Plan for Promoting High-Quality and Safe Development of Commercial Space" (Nov 2025)** and a July 2025 safety regulation update with a dedicated oversight department ([China in Space, 2026-10-13](https://www.china-in-space.com/p/commercial-space-sector-to-be-promoted)).
- **CNSA Commercial Spaceflight Standards System v1.0 (24 Apr 2026):** six areas incl. governance (debris mitigation), manufacturing, launch/TT&C, **space application services (remote-sensing applications, megaconstellation ops, space-based computing)**, common standards, facilities; Hu Yihuai (Dept. of Commercial Space): "we have incorporated applicable standards used internationally" ([China in Space, 2026-05-02](https://www.china-in-space.com/p/china-releases-space-standards-system)).
- **CPC Central Committee & State Council "Opinions on Developing New-Quality Productive Forces" (9 Oct 2026):** "While ensuring safety, promote the healthy and orderly development of the low-altitude economy and commercial space sector," in a paragraph that also warns against "cutthroat"/involution competition; Section 7 warns against bubbles and "blind rushing into industries" ([China in Space, 2026-10-13](https://www.china-in-space.com/p/commercial-space-sector-to-be-promoted)).
- **MIIT ICT 15th FYP (Sep 2026)** and space-computing governance — see D2.

## H2. Disaster response: CNSA's space emergency mechanism (first activation, Aug 2026)

For the 26 Aug 2026 glacier-collapse/dam-burst flood on the Nepal–Xizang border (≥1,200 dead, >4,200 missing per Reuters; Gyirong Port crossing destroyed), CNSA "swiftly activat[ed] the space emergency response mechanism to coordinate satellite resources" for the first time: "Five pre-disaster images and ten post-disaster images have been dispatched in batches" (27 Aug). CASC (CRESDA + China Siwei) supplied most imagery and telecom capacity; SpaceTY (X-band SAR), Huantian Wisdom (optical change mapping), STAR.VISION, PIESAT and MinoSpace contributed; all commercial firms gave data to Chinese authorities, and CNSA shared with Nepal's government. No acquisition-to-delivery latencies were published, and the International Charter was not mentioned ([China in Space, 2026-09-02](https://www.china-in-space.com/p/space-sector-mobilized-to-assist)).

**Problem.** Many separate commercial fleets, each tasked and reported separately; a mechanism only now (2026) exists to pool them; outputs are images, not decision products; no public latency data.

**Hackathon angle (strong).** *Glacial-hazard early warning for the Himalaya*: monitor glacial lakes and debris dams on both sides of the Nepal–China border with Sentinel-1 (all-weather) + Sentinel-2, flag rapid lake growth or new landslide dams, and push alerts downstream. Real event, open data, clear stakeholders (Nepal DHM, ICIMOD).

## H3. International data-sharing offers

- **BRICS Remote Sensing Satellite Constellation:** supported since 2015; contributors China, Russia, Brazil, India share each other's data; June 2026 meeting (Bengaluru) considered letting Indonesia and Saudi Arabia contribute/access; Russia pushes a BRICS "Space Council"; topics include training/technology sharing to close "technical gaps between members" ([China in Space, 2026-06-27](https://www.china-in-space.com/p/brics-space-agency-heads-consider)). Wikipedia notes the BRICS agreement of Aug 2021 ([Wikipedia: Gaofen](https://en.wikipedia.org/wiki/Gaofen)).
- **CNSA free Gaofen data (2019):** CNSA announced (GEO meeting, Nov 2019) free public access via www.cnsageo.com to a global coverage map, historical archives and **daily-updated 16 m Gaofen imagery** (search excerpt of [Go Taikonauts, 2019-11-07](https://go-taikonauts.com/en/chinese-space-news/2762-free-public-access-to-china-space-agency-s-satellite-data); site unreachable on fetch). CNSA also has a UNOOSA/UN-SPIDER agreement on sharing imagery for disaster risk reduction ([UNOOSA](https://www.unoosa.org/oosa/en/informationfor/articles/reducing-disaster-risks_-unoosa-and-china-national-space-administration-sign-first-of-its-kind-agreement.html), search excerpt; 404 on fetch) and says it has >170 intergovernmental space agreements with ~50 countries/organisations, >40 on Earth observation ([CNSA presentation at UN COPUOS STSC 2024](https://www.unoosa.org/documents/pdf/copuos/stsc/2024/ListTechnicalPresentations/2024_STSC_technical_presentations_slides/1--China_Platform_of_Earth_Observation_System_Mr.WANG_Fengyu_China.pdf), search excerpt). No 2025–2026 policy change found.
- **APSCO** (Beijing HQ; members Bangladesh, China, Iran, Mongolia, Pakistan, Peru, Thailand, Turkey) ([Wikipedia: APSCO](https://en.wikipedia.org/wiki/Asia-Pacific_Space_Cooperation_Organization)); China expanded orbital observation via ground telescopes in APSCO states ([China in Space, 2026-10-15](https://www.china-in-space.com/p/spacex-wants-chinese-spacecraft-data)).
- **CBERS** (China–Brazil): CBERS-4 (2014; 5 m pan/10 m MS PanMUX, 40/80 m IRS, 60 m WFI) and CBERS-4A (Dec 2019) ([Wikipedia: CBERS](https://en.wikipedia.org/wiki/China%E2%80%93Brazil_Earth_Resources_Satellite_program)). INPE distributes CBERS data free (not verified in this session — see Leads not followed).
- **Satellite exports** (rather than data sharing) are the dominant model in 2025–2026: Indonesia (Lampung-1 + 19 more on order), Uzbekistan (Samarqand-2028), Pakistan (new RS satellite Apr 2026; PRSS/PakSat lineage), Algeria (two RS satellites Jan 2026), Thailand (LM-6C, Aug 2026), Egypt, UAE university sats, Arabsat-50 ([China in Space, 2026-08-05](https://www.china-in-space.com/p/uzbek-indonesian-satellites-launched); [archive](https://www.china-in-space.com/archive); [China in Space, 2026-01-15](https://www.china-in-space.com/p/algerian-remote-sensing-satellite); [China in Space, 2026-04-25](https://www.china-in-space.com/p/new-pakistani-remote-sensing-satellite)) (several titles only).

## H4. Data openness vs. the West

- Western open baselines (Landsat, Sentinel) are used heavily inside Chinese research: e.g., the Shackleton ice model relies on NASA LRO and Chandrayaan-1; SkySense++ pretrains on Sentinel-1/2; LEVIR-CD and LoveDA use Google Earth imagery ([China in Space, 2026-03-01](https://www.china-in-space.com/p/scientists-publish-model-of-potential); [GitHub SkySense++](https://github.com/kang-wu/SkySensePlusPlus); [LEVIR](https://justchenhao.github.io/LEVIR/); [LoveDA](https://github.com/Junjue-Wang/LoveDA)).
- Chinese operational data (Gaofen, Fengyun, Haiyang) are mostly accessible through Chinese portals with registration; the portals I tried (sasclouds.com, chinageoss.cn, moon.bao.ac.cn) are JavaScript apps that could not be read without a browser — itself a practical access barrier for foreign developers.
- Chinese *academic* outputs (datasets/models) are widely open on GitHub/Zenodo, usually under **non-commercial** licences (C2, C3).
- Commercial Chinese imagery remains purchasable in many markets despite sanctions; US sanctions are judged to have little practical effect inside China ([China in Space, 2026-05-10](https://www.china-in-space.com/p/us-sanctions-three-chinese-space)).

---

# I. Problems Chinese actors themselves discuss

## I1. "Interpretation is the midstream bottleneck" (解译瓶颈) — processing backlog

**What it is.** A recurring Chinese industry framing: satellites and data are plentiful, but turning imagery into answers is still largely manual. Profile of Shaanxi Yuanyi Intelligence (元翌智能, Xidian U spin-off, 2021, Huawei-supported): "当前被限制的，正是中游的解译环节" ("what is holding things back is precisely the midstream interpretation stage") and "摆脱对人的依赖，将是商业遥感爆发的核心一环" ("getting rid of dependence on people will be a core link in the take-off of commercial remote sensing"). Manual visual interpretation remains common in surveying, land, forestry and agriculture — slow, costly, long cycles; large-scale processing platforms and data sharing are "difficult to build." Figures quoted: 1,659 RS satellites in orbit worldwide, 451 launched by China; China's geoinformation industry CNY 811.1 B (8,111亿元) in 2023, 2.3× 2015; >CNY 360 B invested in remote sensing over the past decade; civil EO satellites produce >10 TB of raw data per day. Company claims (unverified): a model trained on >100 TB / >3 M km² of Gaofen imagery, 100+ land-cover classes, >85% average accuracy; "hundred-million-pixel imagery that once needed at least one person-month can now be interpreted in under 10 minutes"; kiwifruit mapping over 67,000 mu in Weinan at >95%; L0 (all-element foundation) → L1 (agriculture/forestry/water) → L2 (scene) model hierarchy ([Alibaba Cloud Developer Community, 2025-03-11](https://developer.aliyun.com/article/1656535); [Sspai](https://sspai.com/post/97234)) **[promotional blog]**.
- Academic framing (2025–2026 Chinese reviews): purely data-driven interpretation hits a bottleneck in **generalisation and interpretability** — "以突破单一数据驱动范式在泛化性和解释性上的瓶颈"; proposed fix is "data + knowledge" dual-driven methods (visual, geospatial and physical knowledge) ([Journal of Remote Sensing review, vol. 30 no. 6, 2026, Beijing Institute of Remote Sensing Information](https://www.ygxb.ac.cn/zh/article/doi/10.11834/jrs.20265172/)); heavy dependence on labelled data, poor robustness in complex scenes and difficulty fusing multi-source heterogeneous data ([Acta Aeronautica et Astronautica Sinica 2026, AIRCAS + CETC 28th Institute](https://hkxb.buaa.edu.cn/EN/Y2026/V47/I10/632103)); parameter-efficient fine-tuning review for RS interpretation ([CJIG 2026 PDF](https://www.cjig.cn/rc-pub/front/front-article/download/118335909/lowqualitypdf/面向遥感图像解译的参数高效微调研究综述.pdf), not opened).
- Same problem at the orbit end: Zhejiang Lab's "<10% of data effectively used" (D1).

**Hackathon angle.** *Zero-label land-cover for a new crop*: use a foundation model (SkySense/GeoRSCLIP) + a handful of clicks to map one specialty crop (kiwifruit, tea, cotton) over a county from Sentinel-2 — showing "person-month → minutes."

**Credibility.** Promotional blog (company claims) + peer-reviewed reviews.

## I2. Revenue and demand: who actually pays?

- **Qianfan: zero revenue in Q1 2026** (Caixin, via [azmth](https://azmth.space/tracker/qianfan)); "no recurring revenue stream yet" while raising CNY 6.7 B (Feb 2024), ~CNY 5 B (Oct 2025) and CNY 6.976 B (2026, 18 mostly state/municipal investors) ([China in Space, 2026-06-25](https://www.china-in-space.com/p/qianfan-system-testing-well-underway); [China in Space, 2026-09-04](https://www.china-in-space.com/p/geespace-receives-connectivity-service)).
- **Chang Guang revenue** was ~USD 80 M in 2023 (Wikipedia infobox) against ~160 launched satellites and a CNY 5 B raise in 2026 ([Wikipedia: CIOMP/CGSTL](https://en.wikipedia.org/wiki/Changchun_Institute_of_Optics,_Fine_Mechanics_and_Physics); [China in Space, 2026-07-09](https://www.china-in-space.com/p/cgstl-hongqing-technology-raise-billions)). It claims services in 14 sectors, >150 service categories, >170 countries and regions ([Chinanews, 2025-07-20](https://www.chinanews.com.cn/cj/2025/07-20/10450887.shtml)) **[state media]**.
- **Demand is government-led**: cities (Chengdu, Wuhan, Guangzhou), counties (Anxi tea), provincial bureaus (Yunnan geology), ministries (cultural heritage), state banks (Postal Savings) and foreign governments buy satellites (A1-bis, A6, A8, A10, H3). Financing for orbital compute comes from **bank credit lines** (Orbital Chenguang CNY 57.7 B; ADA Space CNY 5 B from Bank of China Sichuan; STAR.VISION CNY 10 B) rather than customers ([China in Space, 2026-06-24](https://www.china-in-space.com/p/china-moves-to-manage-space-based); [China in Space, 2026-02-27](https://www.china-in-space.com/p/chinas-space-enterprises-quietly); [China in Space, 2026-09-29](https://www.china-in-space.com/p/starvision-unveils-spaceidc-computing)).
- Two Sessions 2026: Qianfan's Zhang Qi asked for "financial stability help for operators" ([China in Space, 2026-03-13](https://www.china-in-space.com/p/reusable-rockets-deep-space-exploration)).

- **Chang Guang finances (IPO prospectus data).** Revenue: 2019 CNY 84.6 M, 2020 CNY 104 M, 2021 CNY 312 M, H1 2022 CNY 35.5 M; net loss: CNY 391 M (2019), 391 M (2020), 220 M (2021), 210 M (H1 2022). Top-5 customers = 60–83% of revenue. Causes: high satellite depreciation, heavy R&D, low early sales. "截至报告期末公司尚未盈利且存在累计未弥补亏损" ("as of the end of the reporting period the company has not yet been profitable and has accumulated unrecovered losses"). STAR Market IPO (CNY 2.683 B, incl. a "Jilin-1 共生地球 (Symbiotic Earth)" project and bank-loan repayment) was **withdrawn on 4 Dec 2024** ([Securities Times via ifeng, 2024-12-05](https://finance.ifeng.com/c/8f3yCnTVHV0)).
- **Orbita / 航宇微 (Zhuhai-1)**: revenue peaked >CNY 900 M (2018); 2022 revenue CNY 426 M with a **CNY 572 M loss**; 2023 forecast loss CNY 290–380 M (bad-debt provisions CNY 75–105 M, goodwill impairment CNY 210–240 M); satellite-business revenue fell from CNY 530 M (2020) to 215 M (2022); satellite-constellation gross margin **0.85%** in 2022; receivables within one year rose to 73.7% of revenue (2022); customers concentrated in (Guangdong) local governments whose "demand is derived and budgets soft-constrained"; local fiscal deficits >CNY 11 T (2022). Quotes: "被寄予厚望的卫星业务并没有给公司带来实质性的盈利提升，更像是'赔本赚吆喝'" ("the much-hoped-for satellite business has not brought real profit — more like 'losing money to drum up attention'"); "客户拓展并没有转化为业务收入的增长，卫星业务陷入了'增客不增收'的困局" ("more customers, no more revenue"); "中国的航天领域长久以来都存在着'重建设、轻应用'的现象" ("China's space sector has long had a 'heavy on building, light on applications' phenomenon"). Two 2023 county deals to build 100 satellites each ("Fuping-sat", "Zunhua-sat") were judged overlapping and doubtful. Industry data: China's RS-satellite market CNY 5.61 B (2015) → 13.08 B (2022), CAGR 12.86%; 294 civil RS sats in orbit end-2022, 189 commercial ([Space & Network WeChat via NetEase, 2024-03-05](https://m.163.com/dy/article/ISI3JK1V05119RIN.html)) **[industry blog; figures from company filings]**. 2024 revenue CNY 210 M ([Qianzhan Industry Research, 2025-06-03](https://www.qianzhan.com/analyst/detail/220/250603-319b5c80.html)).
- **Listed RS firms, 2024 (Qianzhan):** PIESAT (航天宏图) debt-to-assets 74.9%, negative ROE/EPS, still planning "the country's largest hybrid RS constellation"; GEOVIS (中科星图) gross margin 49.6%, ROE 9.6%, PE 142.7; China Spacesat (中国卫星) gross margin 11.8%, negative PE; hardware margins low ("硬件成本管控问题") ([Qianzhan, 2025-06-03](https://www.qianzhan.com/analyst/detail/220/250603-319b5c80.html)).

## I2-bis. Price collapse of Chinese high-res imagery (the "price war" in numbers)

Paper (澎湃新闻), 8 Jul 2026: a decade ago foreign high-res imagery cost **CNY 500/km²**; Jilin-1 imagery now costs **as little as CNY 13/km²**. Satellite unit cost fell from >CNY 80 M to **CNY 4 M**, mass from 420 kg (gen 1) to ~20 kg. The Jilin-1 online data mall (2023) publishes prices and delivers data in as little as 3 minutes. **>1,000 universities** certified for free access (3.52 M km² of high-res imagery used); the **共生地球 (Gongsheng Diqiu / "Symbiotic Earth") app (launched 2022) has >3.5 M downloads**; ~40 free disaster-imagery services provided. Sector uses: crop mapping (corn, rice, soy, wheat, Heilongjiang to Hainan); **pine wilt disease (>CNY 100 B losses)** — locating infected trees; black-odorous water, illegal construction, dust; insurers' post-disaster claims; banks monitoring construction progress for credit risk. Students' saying: "没有Landsat和哨兵，遥感专业学生都毕不了业" ("without Landsat and Sentinel, remote-sensing students couldn't graduate") ([The Paper, 2026-07-08](https://m.thepaper.cn/newsDetail_forward_33540949)) **[state-affiliated media]**. 2024 global 0.5 m map from 1.2 M of 6.9 M scenes, 130 M km²; AI auto-detection of aircraft, ships, oil tanks and PV plants at >95% ([Chinanews, 2025-07-20](https://www.chinanews.com.cn/cj/2025/07-20/10450887.shtml)).

**Hackathon angles.**
- *Pine wilt disease spotter*: red/brown crown detection in high-res imagery (or Sentinel-2 red-edge time series) over pine forests; a >CNY 100 B problem in China, also Korea, Japan, Portugal.
- *Insurance claim verifier*: before/after imagery around a flood/hail event + parcel boundaries → per-parcel damage estimate (what Chinese insurers buy Jilin-1 data for).

## I3. "Involution" (内卷) and bubbles — the price-war worry

The Oct 2026 CPC/State Council Opinions put commercial space in the same paragraph as avoiding "cutthroat" and involution-style competition, and warn against bubbles, "favoring novelty over feasibility" and "blind rushing into industries"; provinces are told to invest in projects "suited to local conditions" ([China in Space, 2026-10-13](https://www.china-in-space.com/p/commercial-space-sector-to-be-promoted)). With dozens of overlapping 1,000-satellite computing plans (D3) and every city buying its own satellite, the official worry is over-investment and duplicated capacity. (Direct Chinese-language reporting on EO *price wars* was not reached — search budget ran out; see Leads not followed.)

## I4. Data silos

- Each city/agency/bank now owns a satellite; data go to that owner. In the Nepal–Xizang flood, "all commercial firms said they gave their data to Chinese authorities," and CNSA activated a pooling mechanism **for the first time** only in Aug 2026 ([China in Space, 2026-09-02](https://www.china-in-space.com/p/space-sector-mobilized-to-assist)).
- The 15th FYP's call for remote-sensing satellites to be "built and shared jointly" is itself an admission of fragmentation ([China in Space, 2026-03-13](https://www.china-in-space.com/p/reusable-rockets-deep-space-exploration)).
- Yuanyi: large-scale processing platforms and data sharing are hard to build; in the 2023 Xi'an flood, Gaofen data came through the provincial emergency department and the provincial high-resolution centre — i.e., through government channels ([Sspai](https://sspai.com/post/97234)).

## I5. Quality and reliability

CASC's Party Group (8 Sep 2026): "severe quality challenge" after upper-stage fragmentations, the Long March 7A explosion, Shenzhou-20 and delays; promised "Quality Day," look-back reviews and public shaming ([China in Space, 2026-09-09](https://www.china-in-space.com/p/state-owned-firms-vow-to-improve)). Qianfan: 22 of 239 satellites failed (McDowell) ([azmth](https://azmth.space/tracker/qianfan)).

## I6. Talent

Two Sessions 2026 proposals on digital talent, worker recognition and an industry-led talent pipeline ([China in Space, 2026-03-13](https://www.china-in-space.com/p/reusable-rockets-deep-space-exploration)); competitions are explicitly framed as talent-discovery tools ("挖掘更多优秀的技术和专业人才") ([36Kr, 2018-06-05](https://www.36kr.com/p/1722569801729)); the 2025 Qizhi Cup drew 1,022 teams ([China.com Tech, 2025-08-15](https://m.tech.china.com/articles/20250815/202508151714990.html)).

## I7. Starlink and spectrum/orbit "occupation"

China's UN statement (Dec 2025) frames Starlink as consuming "frequency and orbital resources" and raising collision/debris risk; Chinese operators then filed for ~200,000 satellites at the ITU, which commentators said may aim to challenge first-come-first-served allocation (E2-quater). Chinese operators are also the largest group not sharing ephemerides with SpaceX (E2-ter).

## I8. Orbit-to-ground bottleneck (stated by Zhejiang Lab, CAICT, China Mobile/Tsinghua)

"Less than 10 percent" of data effectively used; "hours or even days" of processing; ~0.1 PB/day per RS satellite; "from hours to seconds" for disaster warning with orbital compute (D1, D2).

---

---

# Problem bank

Format: problem → who has it → data that could address it → source.

**Orbit-to-ground and onboard AI**
1. Less than 10% of collected satellite data is "effectively used"; ground processing takes hours to days → Zhejiang Lab / Three-Body, all high-volume EO operators → Sentinel-2 L1C + s2cloudless masks to simulate onboard triage → [China Daily, 2026-07-29](https://www.ehangzhou.gov.cn/2026-07/29/c_298438.htm)
2. Short ground-station passes over China force operators to either halt imaging (lost revenue) or filter onboard → Chinese commercial EO firms → Sentinel-2 tiles + pass schedules from TLEs → [China in Space, 2026-08-15](https://www.china-in-space.com/p/why-are-more-of-chinas-satellites)
3. Onboard models are frozen at launch and only do filtering; no in-orbit retraining → Chinese EO satellites (academics' critique) → any EO stream for an update-in-orbit demo → [China in Space, 2026-08-15](https://www.china-in-space.com/p/why-are-more-of-chinas-satellites)
4. Mission-specific keep/drop filtering (e.g., Three-North Shelter forest, skip cities and cloud) → Chinese forestry/EO operators → Landsat/Sentinel-2 over the Gobi margin → [China in Space, 2026-08-15](https://www.china-in-space.com/p/why-are-more-of-chinas-satellites)
5. On-board transient triage with 99% accuracy while cutting downlink (GRBs) → Three-Body astronomy payload → Fermi GBM / Swift public event data → [Xinhua, 2026-02-13](https://www.news.cn/20260213/d985035629be4998bcb3086d1f4b6ecb/c.html)
6. Disaster warning "from hours to seconds" via orbital compute → CAICT/MIIT → FIRMS fire data, Sentinel-1 flood → [China Daily, 2026-04-10](https://mobile.chinadaily.com.cn/html5/2026-04/10/content_001_69d7ef8ced50be540e72e28a.htm)
7. Heat rejection and power limits for computing satellites → Thermal AI, Orbital Chenguang, Three-Body → spacecraft thermal models (no EO data) → [China in Space, 2026-08-20](https://www.china-in-space.com/p/chinese-firms-aim-to-expand-orbital)
8. Weather models moved into orbit (Fuxi/Dayu/Puyun) — need on-orbit nowcasting from raw IR → Xinghuo Chuanming, Fudan → FY-4B/Himawari/GOES + ERA5 → [Science and Technology Daily, 2026-07-24](https://www.stdaily.com/web/gdxw/2026-07/24/content_552976.html)

**Dual use, provenance and sanctions**
9. Nobody can verify which satellite took a viral image → SCSPI/Hu Bo, OSINT analysts, State Dept → CelesTrak TLEs + UCS satellite DB + shadow/sun geometry → [Pekingnology, 2026-02-27](https://www.pekingnology.com/p/viral-satellite-imagery-of-us-military)
10. Commercial 0.5 m imagery cueing strikes; correlating satellite passes with attacks done by hand → FT, US/GCC militaries → TLEs + ACLED event data → [Maritime Executive, 2026-04-15](https://maritime-executive.com/article/iran-using-chinese-satellite-to-target-us-and-gcc-countries)
11. Satellite-access-as-a-service + remote ground stations hide who is tasking → regulators, State Dept → ground-station locations, TLEs → [China in Space, 2026-04-19](https://www.china-in-space.com/p/emposat-denies-knowledge-of-iran)
12. Western ground stations serving sanctioned Chinese EO sats (KSAT, 42 CGSTL sats) → Norwegian regulator NKOM, NATO → licence lists + SatNOGS/TLE pass overlaps → [Defence24, 2026-04-21](https://defence24.com/geopolitics/nato-defence-contractor-will-service-chinese-military-satellites-should-the-west-be-concerned)
13. Sanctions have little real-world effect on Chinese EO firms → US government → company announcements/launch records → [China in Space, 2026-05-10](https://www.china-in-space.com/p/us-sanctions-three-chinese-space)
14. AI fusion of imagery + AIS + webcams makes "God's-eye view" OSINT cheap → MizarVision's targets, navies → Sentinel-1 + open AIS → [Pekingnology, 2026-02-27](https://www.pekingnology.com/p/viral-satellite-imagery-of-us-military)
15. "Who is overhead right now?" warnings (Yaogan ELINT triplets, retrograde Yaogan) → ships, NGOs, militaries → TLEs → [Wikipedia: Yaogan](https://en.wikipedia.org/wiki/Yaogan)
16. EO satellites now image other spacecraft (non-Earth imaging) — no public catalogue of who images whom → SSA community → TLE conjunction geometry → [China in Space, 2026-04-14](https://www.china-in-space.com/p/cgstl-deploys-eight-imaging-satellite)

**Megaconstellations, debris and traffic**
17. Officials' "in orbit" counts include dead satellites; ~9% of Qianfan failed → Spacesail, investors, SSA → CelesTrak GP history → [azmth Qianfan tracker](https://azmth.space/tracker/qianfan)
18. Long March 6A-family upper stages fragment (>30 stages decaying from ~900 to ~650 km; 705 debris from one launch) and a 6-month-old Yaogan-50 (02) broke into 43+ objects in a ~142° retrograde orbit where debris lasts centuries → all LEO operators → Space-Track/CelesTrak debris catalogues → [China in Space, 2026-05-28](https://www.china-in-space.com/p/can-chinas-mega-constellations-deploy); [Gizmodo, 2026-09-08](https://gizmodo.com/chinese-satellite-breaks-apart-in-rare-orbit-that-could-hold-debris-for-centuries-2000808645)
19. Chinese operators are the largest group not sharing ephemerides with SpaceX → SpaceX, all operators → TLE vs. operator ephemerides → [China in Space, 2026-10-15](https://www.china-in-space.com/p/spacex-wants-chinese-spacecraft-data)
20. Close approaches right after rideshare deployment (Kinetica-1 vs Starlink, ~200 m) → CAS Space, SpaceX → TLEs of new launches → [China in Space, 2025-12-13](https://www.china-in-space.com/p/spacex-alleges-close-approach-of)
21. Spectrum warehousing: ~249,000 satellites filed vs ~200 launched/year; ITU 10/50/100% milestones → ITU, regulators → ITU filings + launch catalogue → [China in Space, 2026-01-10](https://www.china-in-space.com/p/chinese-constellation-operators-submit)
22. Megaconstellation deployment limited by state launchers, three distant sites, outsourced production → Qianfan, Guowang → launch logs → [China in Space, 2026-05-28](https://www.china-in-space.com/p/can-chinas-mega-constellations-deploy)
23. China's UN complaint: Starlink close approaches to Tiangong, breakups, unlicensed service → China, developing countries → TLEs → [China in Space, 2026-01-05](https://www.china-in-space.com/p/china-lodges-informal-complaint-against)
24. A sub-millimetre (untrackable) debris particle cracked a crew-return window (>1 cm crack) and grounded Shenzhou-20 → CMSA → MASTER/ORDEM flux models + catalogue → [Reuters via Dunya News, 2025-12-01](https://dunyanews.tv/en/Technology/921166-damaged-shenzhou20-spacecraft-to-return-to-earth-uncrewed-for-inspect); [SpacePolicyOnline](https://spacepolicyonline.com/news/chinese-spacewalkers-inspect-damaged-shenzhou-20-window/)
25. Launch/vehicle quality crisis ("severe quality challenge") → CASC → launch-failure records → [China in Space, 2026-09-09](https://www.china-in-space.com/p/state-owned-firms-vow-to-improve)

**Interpretation and AI (literal contest problems)**
26. Interpretation is still manual — the "midstream bottleneck" → Chinese RS industry → Gaofen/Sentinel-2 + foundation models → [Alibaba Cloud Developer, 2025-03-11](https://developer.aliyun.com/article/1656535)
27. Data-driven models fail to generalise and explain → Chinese RS academia → LoveDA (urban/rural shift) → [Journal of Remote Sensing 2026 review](https://www.ygxb.ac.cn/zh/article/doi/10.11834/jrs.20265172/)
28. Label scarcity and multi-source fusion → AIRCAS/CETC → SkySense++ few-shot data → [Acta Aeronautica 2026](https://hkxb.buaa.edu.cn/EN/Y2026/V47/I10/632103)
29. Instance segmentation robust to sensor shift, blur and unknown classes (zero-shot) → Qiyuan Lab (Qizhi Cup T1) → iSAID, DOTA → [China.com Tech, 2025-08-15](https://m.tech.china.com/articles/20250815/202508151714990.html)
30. Accurate + fast detection on edge chips (Ascend 310B) → Qizhi Cup T2 → VisDrone/DOTA → [same](https://m.tech.china.com/articles/20250815/202508151714990.html)
31. Adversarial robustness of RS multimodal LLMs (VQA, captioning, change detection) → Qizhi Cup T3 → RS VQA sets, RS5M → [same](https://m.tech.china.com/articles/20250815/202508151714990.html)
32. Fine-grained multi-class object recognition in high-res optical → AIRCAS Gaofen Challenge → FAIR1M, DOTA v2 → [PEdaily, 2023-03-23](https://news.pedaily.cn/20230323/53907.shtml)
33. Sea-ice monitoring in HY-1 optical → NSOAS → Sentinel-3 OLCI/MODIS → [PEdaily](https://news.pedaily.cn/20230323/53907.shtml)
34. Offshore aquaculture segmentation in SAR → NSOAS → Sentinel-1 → [PEdaily](https://news.pedaily.cn/20230323/53907.shtml)
35. Building census + change detection → CRESDA → LEVIR-CD, WHU → [PEdaily](https://news.pedaily.cn/20230323/53907.shtml)
36. Multi-object tracking in satellite video → Chang Guang → VISO (Jilin-1 video) → [PEdaily](https://news.pedaily.cn/20230323/53907.shtml); [VISO](https://github.com/QingyongHu/VISO)
37. Fine-grained aircraft recognition in SAR → Gaofen Challenge → SARDet-100K → [PEdaily](https://news.pedaily.cn/20230323/53907.shtml)
38. Task-driven intelligent image compression → 眼神杯 / NSFC → Sentinel-2 → [36Kr, 2018-06-05](https://www.36kr.com/p/1722569801729)
39. Best Chinese models/datasets are non-commercial only → startups → SkySense, LoveDA → [SkySense GitHub](https://github.com/Jack-bo1220/SkySense)

**Applications Chinese customers pay for**
40. Glacier-collapse / landslide-dam outburst floods across the Nepal–Xizang border (≥1,200 dead) → CNSA, Nepal, ICIMOD → Sentinel-1/2, glacial-lake inventories → [China in Space, 2026-09-02](https://www.china-in-space.com/p/space-sector-mobilized-to-assist)
41. Disaster imagery from many fleets is pooled ad hoc; no latency metrics → CNSA (first activation 2026) → Charter/Copernicus EMS products for benchmarking → [same](https://www.china-in-space.com/p/space-sector-mobilized-to-assist)
42. Pine wilt disease, >CNY 100 B losses → Chinese forestry → Sentinel-2 red-edge + high-res crowns → [The Paper, 2026-07-08](https://m.thepaper.cn/newsDetail_forward_33540949)
43. Staple-crop mapping from sowing to harvest (corn/rice/soy/wheat) → agriculture agencies → Sentinel-1/2 time series → [The Paper](https://m.thepaper.cn/newsDetail_forward_33540949)
44. Specialty-crop mapping (kiwifruit, tea) → Weinan, Anxi, Lichuan → Sentinel-2 → [Alibaba Cloud Developer](https://developer.aliyun.com/article/1656535); [China in Space, 2026-06-15](https://www.china-in-space.com/p/handful-of-cgstl-built-satellites)
45. Post-disaster agricultural insurance claims → Chinese insurers → before/after Sentinel-1/2 → [The Paper](https://m.thepaper.cn/newsDetail_forward_33540949)
46. Bank credit risk: construction progress and collateral checks → Postal Savings Bank, banks → Sentinel-2 + building change → [China in Space, 2026-04-14](https://www.china-in-space.com/p/cgstl-deploys-eight-imaging-satellite); [The Paper](https://m.thepaper.cn/newsDetail_forward_33540949)
47. Black-odorous water, illegal construction, dust → environment bureaus → Sentinel-2, PlanetScope samples → [The Paper](https://m.thepaper.cn/newsDetail_forward_33540949)
48. Cultural-heritage site encroachment → National Cultural Heritage Administration → Sentinel-2 + building change → [China in Space, 2026-06-15](https://www.china-in-space.com/p/handful-of-cgstl-built-satellites)
49. Hydropower dam and slope deformation → Wuhan (Dianjian-1 SAR) → Sentinel-1 InSAR (LiCSAR) → [China in Space, 2026-05-15](https://www.china-in-space.com/p/cas-space-delivers-city-backed-earth)
50. Geological-disaster prevention in mountainous provinces → Yunnan geology bureau → Sentinel-1 InSAR, DEM → [China in Space, 2026-09-17](https://www.china-in-space.com/p/expace-delivers-commercial-insar)
51. Urban SAR blind spots (layover/shadow) → SpaceTY → multi-geometry Sentinel-1 → [same](https://www.china-in-space.com/p/expace-delivers-commercial-insar)
52. Countries buying Chinese hyperspectral sats lack analysts → Indonesia, Uzbekistan → EMIT/EnMAP/PRISMA → [China in Space, 2026-08-05](https://www.china-in-space.com/p/uzbek-indonesian-satellites-launched)
53. City-scale water quality from hyperspectral → Guangdong/Hunan governments (Orbita customers) → EMIT/Sentinel-3 → [NetEase, 2024-03-05](https://m.163.com/dy/article/ISI3JK1V05119RIN.html)
54. Greenhouse-gas source attribution (MUSICO, Pujiang-4) → HKUST, CAS → TROPOMI/OCO-2/EMIT methane → [China in Space, 2026-07-06](https://www.china-in-space.com/p/tiangong-begins-monitoring-greenhouse)
55. Jilin-1 has one SAR sat → cloud-limited coverage → Chang Guang customers → Sentinel-1 fusion → [NewSpace Economy, 2026-03-20](https://newspaceeconomy.ca/2026/03/20/the-jilin-1-constellation-chinas-commercial-eye-in-the-sky/)
56. Desertification front along the Three-North Shelter belt → Chinese forestry → Landsat/Sentinel-2 → [China in Space, 2026-08-15](https://www.china-in-space.com/p/why-are-more-of-chinas-satellites)

**Business, policy and data access**
57. "More customers, no more revenue"; government-only demand; unpaid receivables → Orbita and peers → (finance, not EO data) → [NetEase, 2024-03-05](https://m.163.com/dy/article/ISI3JK1V05119RIN.html)
58. "Heavy on building, light on applications" (重建设、轻应用) → Chinese space sector → open data + apps → [NetEase](https://m.163.com/dy/article/ISI3JK1V05119RIN.html)
59. Chang Guang unprofitable 2019–2022, IPO withdrawn → CGSTL → — → [ifeng, 2024-12-05](https://finance.ifeng.com/c/8f3yCnTVHV0)
60. Imagery price collapse from CNY 500 to CNY 13/km² → all Chinese EO firms → — → [The Paper](https://m.thepaper.cn/newsDetail_forward_33540949)
61. Qianfan has zero revenue while raising billions → Spacesail → — → [azmth](https://azmth.space/tracker/qianfan)
62. Over-investment and "involution" in commercial space → State Council → — → [China in Space, 2026-10-13](https://www.china-in-space.com/p/commercial-space-sector-to-be-promoted)
63. Every city/agency owns its own satellite → data silos → local governments → shared catalogue of Chinese EO assets → [China in Space, 2026-05-15](https://www.china-in-space.com/p/cas-space-delivers-city-backed-earth)
64. Build-vs-buy: is a city satellite worth it vs. buying data? → Chinese cities/counties → revisit/resolution needs + rideshare data → [China in Space, 2026-05-04](https://www.china-in-space.com/p/china-opens-dozens-of-rocket-launches)
65. Students and researchers depend on Landsat/Sentinel ("couldn't graduate without them") → Chinese universities → — → [The Paper](https://m.thepaper.cn/newsDetail_forward_33540949)
66. Chinese data portals are JS-only and China-centric → foreign researchers → — → [sasclouds.com](https://www.sasclouds.com/) (observation)
67. Closing technical gaps among BRICS members → BRICS agencies → BRICS constellation data → [China in Space, 2026-06-27](https://www.china-in-space.com/p/brics-space-agency-heads-consider)
68. Launches need to be cheaper, more frequent, with dynamic scheduling → Qianfan (Zhang Qi) → — → [China in Space, 2026-03-13](https://www.china-in-space.com/p/reusable-rockets-deep-space-exploration)
69. Talent shortages → Two Sessions delegates → — → [China in Space, 2026-03-13](https://www.china-in-space.com/p/reusable-rockets-deep-space-exploration)

**Exploration**
70. Picking Chang'e-7 hopper targets in permanently shadowed cold traps → CAS NSSC → LRO LOLA/Diviner, Chandrayaan-1 M3 → [China in Space, 2026-03-01](https://www.china-in-space.com/p/scientists-publish-model-of-potential)
71. Chang'e-7 delayed to 2027 with undisclosed cause; launch-schedule conflicts (Xuntian) → CMSA → — → [China in Space, 2026-08-31](https://www.china-in-space.com/p/change-7-moon-launch-moved-to-early)

**Literal Tianzhi Cup subjects (military-sponsored; added)**
72. Localise and classify civilian vehicles in high-res optical imagery → Military Aerospace Force (Tianzhi Cup 2024) → DOTA, xView, FAIR1M → [Tianzhi notice 2024](https://tianzhibei.com/api/v1/file/download/data_sets/20240604c1df5bdb-cc71-433c-90bb-8fb7c84595ec.pdf)
73. Localise and classify civil airliners across multi-source satellite imagery → same → FAIR1M, DOTA, SAR-AIRcraft → [same](https://tianzhibei.com/api/v1/file/download/data_sets/20240604c1df5bdb-cc71-433c-90bb-8fb7c84595ec.pdf)
74. Intelligent satellite task planning for a national land-resources census → same; also every commercial operator with queued tasking → TLE passes + cloud forecasts + AOI grid → [same](https://tianzhibei.com/api/v1/file/download/data_sets/20240604c1df5bdb-cc71-433c-90bb-8fb7c84595ec.pdf)
75. Large-model remote-sensing image generation (synthetic training data) → same ("exploratory") → RS5M, LoveDA → [same](https://tianzhibei.com/api/v1/file/download/data_sets/20240604c1df5bdb-cc71-433c-90bb-8fb7c84595ec.pdf)
76. Target detection and localisation in multi-source, massive "situational-awareness" data with complex backgrounds → Tianzhi Cup 2023 → SSA image sets / star-field imagery → [NWPU, 2023-05-20](https://hangtian.nwpu.edu.cn/info/1804/21731.htm)
77. Rapid terrain-data generation and ground-feature extraction for mapping → Tianzhi Cup 2019 → Copernicus DEM, OSM, SpaceNet → [SJTU AIPT, 2019-12-25](https://aipt.sjtu.edu.cn/Data/View/306)
78. Crew-vehicle and constellation risk: sub-mm debris flux at Tiangong's altitude (see #24) and long-lived retrograde fragments (Yaogan-50-02) → CMSA, all operators → ESA MASTER / NASA ORDEM → [Gizmodo, 2026-09-08](https://gizmodo.com/chinese-satellite-breaks-apart-in-rare-orbit-that-could-hold-debris-for-centuries-2000808645)

## Top 10 for a 36-hour, 2-person team (judged on problem clarity + public data)

1. **"Which satellite took this picture?"** (#9). Rank candidate satellites for an image from its time, place, resolution and shadow direction, using TLEs. Real 2026 controversy (MizarVision/Hu Bo); data: CelesTrak + UCS DB + Skyfield.
2. **Overhead-pass ↔ event correlator** (#10, #15). For any satellite and any set of sites, show passes before strikes, disasters or port calls. Repeats the FT's TEE-01B analysis automatically.
3. **The "<10% of data used" triage simulator** (#1–#4). An onboard keep/drop model on Sentinel-2 under a downlink budget; reports useful pixels per MB. The problem comes straight from Zhejiang Lab.
4. **Himalayan glacier-collapse / landslide-dam flood watch** (#40–#41). Sentinel-1/2 change detection on glacial lakes and debris dams on the Nepal–Xizang border; follows the Aug 2026 disaster (≥1,200 dead).
5. **Pine wilt disease spotter** (#42). A >CNY 100 B forestry loss; Sentinel-2 red-edge time series plus high-res crown checks.
6. **Dead-or-alive satellite classifier** (#17). Use TLE histories to flag stalled orbit-raising, drift and decay; check it against McDowell's count of 22 failed Qianfan satellites.
7. **ITU "paper satellite" tracker** (#21–#22). Compare ~249,000 Chinese filed satellites with launches against the 10/50/100% milestones.
8. **Dam and slope deformation risk score** (#49–#50). Sentinel-1 InSAR over reservoirs and mountain roads, the job Wuhan and Yunnan bought their own SAR satellites for.
9. **Activity index from satellite video** (#36). Multi-object tracking on Jilin-1 video (VISO dataset), turning a clip into counts of cars, ships and planes.
10. **Red-teaming satellite-image chatbots** (#31). Adversarial attacks and defences for remote-sensing VLMs; the literal 2025 Qizhi Cup Track 3.

Runners-up: satellite tasking planner for a land census (#74, a literal 2024 Tianzhi Cup subject), bank collateral / crop-loan verifier (#46), post-disaster insurance claims (#45), hyperspectral "insight in a box" for importing countries (#52), upper-stage debris watchlist (#18), heritage-site encroachment (#48).

---

# Cross-slice leads

- **EO companies outside China:** Planet reportedly said MizarVision was not a client; Vantor (ex-Maxar) and Sentinel identified as likely MizarVision sources ([Pekingnology](https://www.pekingnology.com/p/viral-satellite-imagery-of-us-military)); KSAT servicing 42 Chang Guang sats ([Defence24](https://defence24.com/geopolitics/nato-defence-contractor-will-service-chinese-military-satellites-should-the-west-be-concerned)); Satellogic AI EO satellite 2027 and Google–Planet Suncatcher TPU prototypes 2027 ([China in Space, 2026-02-27](https://www.china-in-space.com/p/chinas-space-enterprises-quietly)).
- **EO analytics:** FT's pass-vs-strike correlation method; IFRI memo on space intelligence "for all" in the spring 2026 Iranian strikes ([IFRI](https://www.ifri.org/en/memos/toward-space-based-intelligence-all-case-spring-2026-iranian-strikes)); Le Monde's Planet-based analysis of the US buildup (21 Feb 2026, via Pekingnology).
- **US agencies:** State Dept/OFAC designations of 8 May 2026 (Earth Eye, MizarVision, Chang Guang); DoD count of >359 Chinese ISR sats; US Space Force on attacking Chinese satellites ([China in Space, 2026-03-03](https://www.china-in-space.com/p/us-space-force-looking-into-attacking), title only); China's lunar ice model uses NASA LRO data.
- **ESA and other agencies:** SMILE (ESA–CAS) launched 19 May 2026; ESA and CNSA heads met in Jan 2026 for the first time since 2017 ([China in Space, 2026-01-17](https://www.china-in-space.com/p/european-chinese-space-agency-heads), title only); BRICS meeting in Bengaluru (ISRO chair); Brazil's Anatel approved Qianfan; NARIT (Thailand) on Chang'e-7; Pakistan/Algeria/Egypt satellite purchases.
- **SpaceX, xAI and orbital compute:** SpaceX's one-million-satellite compute filing after merging with xAI; Starcloud-1 (H100) trained a Gemini version in Dec 2025, ~15 months after ADA Space's 2024 in-orbit training; IEEE Spectrum's ~USD 51 B per GW in space vs ~USD 16 B on Earth; Starship reached orbit 28 Sep 2026 with 26 satellites; Stargaze SSA platform (Aug 2026) ([China in Space, 2026-02-27](https://www.china-in-space.com/p/chinas-space-enterprises-quietly); [China in Space, 2026-10-15](https://www.china-in-space.com/p/spacex-wants-chinese-spacecraft-data)).
- **Space traffic, debris and weather:** LM-6A breakups (705 pieces from Aug 2024); Yaogan-50 (02) breakup (43+ objects, Sep 2026); Shenzhou-20 sub-mm debris strike; Starlink breakup 17 Dec 2025 at ~418 km; Starlink lowering ~4,400 sats; UN Satellite Operator Contact Hub (Sep 2026); Gande-1 debris-monitoring smallsat; Hong Kong as orbit-management hub; SWF Global Counterspace 2026 (China refuelling test in GEO, possible new DA-ASAT) ([SWF](https://swfound.org/counterspace/)); Shijian-21/25 GEO refuelling ([China in Space, 2025-12-15](https://www.china-in-space.com/p/china-appears-to-have-refueled-a), title only).
- **Datasets:** DOTA v2, iSAID, FAIR1M, LoveDA, Five-Billion-Pixels/GID, LEVIR-CD, VISO, SARDet-100K, RS5M, AIR-SET, SkySense++ RS-Semantic (Zenodo), FIT-RS, MMRS-1M, RS-VL3M, HyperGlobal-450K, JLSSD (unreleased).
- **Models and tools:** SkySense / SkySense++ / V2 / -O / GPT; RingMo family incl. RingMoE and RingMo-Agent; CGEarthEye (Jilin-1); SpectralGPT; HyperSIGMA; EarthGPT; LHRS-Bot; GeoRSCLIP; Alibaba AIEarth; Qwen3 and Qwen2.5-VL used for RS; Co-DETR winning Chinese contests ([Awesome RSFM list](https://github.com/Jack-bo1220/Awesome-Remote-Sensing-Foundation-Models)).
- **Space science and literature:** Chang'e-6 far-side samples; Chang'e-7 (2027); Shackleton ice-stability paper (*PSJ*); Tianwen-2 at Kamoʻoalewa; Tianwen-3 (2028); on-orbit GRB classification on Three-Body; Xuntian telescope early 2027.

# Leads not followed

- **Tianzhi Cup (天智杯) 2025 (5th) and 2026 subjects** — not found; the 2024 notice says full subject texts sit on an internal military procurement network. Official site: tianzhibei.com.
- **SuperView Neo (高景) specs** — sources conflict (16- vs 28-satellite plan; Neo-3 swath 12–15 km vs 130 km); the 2026 ITU slide by Hu Guang was too large to fetch.
- **Chinese military papers on countering Starlink** (SCMP coverage, e.g., 2022 "must be able to destroy Starlink") — SCMP returned 403; not verified.
- **Gaofen / CRESDA / NSMC / NSOAS data-access terms** — portals are JS-only; the 2019 cnsageo.com free 16 m offer is known only from a search excerpt; current status unverified.
- **Fengyun-3H and Fengyun-4C** (launched 2025 per [China in Space recap](https://www.china-in-space.com/p/china-continues-space-progress-through)) — instruments and data access not checked.
- **PIESAT 2025 annual report**, Head Aerospace, GEOVIS's own constellation, Galaxy Space's EO plans (Galaxy-SAR-2 ITU filing for 96 SAR sats) — partially covered.
- **CASI "Chang Guang Satellite Technology Company Overview"** ([CASI](https://www.airuniversity.af.edu/CASI/Display/Article/3727764/chang-guang-satellite-technology-company-overview/)) — 403 on fetch.
- **X posts by @AJ_FI and @CNSpaceflight** — none surfaced in two targeted searches; China in Space cites a STAR.VISION_cn post on X about newer AI satellites ([China in Space, 2026-08-15](https://www.china-in-space.com/p/why-are-more-of-chinas-satellites)) and McDowell's posts (Yaogan-50-02 count, via Gizmodo).
- **SpaceNews full texts** (Andrew Jones) — paywalled; only first paragraphs/excerpts used.
- **"Kongtian" model** — not verified as a separate model; "空天" (Kongtian, "aerospace") is the prefix of AIRCAS's products (空天·灵眸 = RingMo; 空天·四象 = AIR-SET).
- **LuoJia** — only Luojia-3-01 onboard processing (via China in Space) covered; LuoJiaNET framework not checked. **GeoChat** is from MBZUAI (UAE), not China.
- **APSCO data-sharing platform and APOSOS** telescope network; **Chang'e sample loans** to foreign institutions; **CBERS free data** policy — not verified.
- **Chinese-language reporting on EO price wars** beyond the CNY 500 → 13/km² figure, and on talent shortages in RS interpretation.
- **Tracker discrepancies:** Jilin-1 (117 in orbit / 140–161 launched / "190 linked"), Qianfan (238–257), Guowang (186–258) — reconcile with planet4589.org before quoting a single number.
