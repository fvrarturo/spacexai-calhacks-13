# ESA, EU Copernicus, European agencies, and other non-US / non-China agencies: problems, data, and hackathon angles

**Scope.** ESA (Earth observation, Φ-lab, Kelvins, OSIP, InCubed, CCI, ERS, CM25), the EU (Copernicus, Copernicus services, Destination Earth, EU Space Act, IRIS²), EUMETSAT / ECMWF, national European agencies (DLR, CNES, ASI, UKSA), JAXA, ISRO / IN-SPACe, KARI, UAE / MBRSC, Australia (DEA), Digital Earth Africa, Brazil (INPE), Canada (CSA), GEO, CEOS, UN-SPIDER and the International Charter. The focus is the problems these organisations publish themselves, and the public data that could address them.

**Researched on 2026-10-24.**

**Credibility scale used:** official (agency/EU primary page or document) · peer-reviewed · reputable press · trade press / blog · social post · rumor / unverified.

**Method note.** Every claim links to a page that was opened, or that appeared in search results on 2026-10-24. Items marked *(unverified)* came only from a search-result summary or a secondary source, and the primary page was not opened. A web-search budget shared by several parallel researchers ran out during this work. Coverage therefore leans on primary pages fetched directly, and some items are listed under "Leads not followed".

**Contents.**
- §0 Status board; shortlist
- §1 Sentinels
- §2 Earth Explorers / FutureEO
- §3 CDSE / openEO
- §4 Copernicus services
- §5 DestinE
- §6 Φ-lab (Φsat-2, EVE, challenges, Grand Marathon, TerraMind / Major TOM)
- §7 Kelvins
- §8 OSIP / InCubed / CCI
- §9 CM25 / ERS / EU Space Act / IRIS² / MFF / sovereignty
- §10 EUMETSAT / ECMWF
- §11 DLR / CNES / ASI / UKSA
- §12 Japan
- §13 India
- §14 Canada
- §15 Brazil
- §16 Africa / Australia / Korea / UAE
- §17 GEO / CEOS
- §18 Charter / UN-SPIDER
- §19 Hackathons and LPS25 problem index
- §20 Challenge table
- §21 Problem bank
- §22 Cross-slice leads
- §23 Leads not followed

---

## 0a. Shortlist: problems that best fit "clear problem + large public space data + 36 hours"

1. **Charter / CEMS damage-triage copilot.** The bottleneck is human interpretation (Φ-lab, LPS25 B.04.05). Activations rose to 85/yr. Live events include EMSR935 Valencia floods (Oct 2026) and the Venezuela earthquake (Jun 2026). Data: Sentinel-1 C/D, Sentinel-2, NISAR L-band. See §4.1, §18.1.
2. **"Legal or illegal?" deforestation alerts for Brazil.** INPE says legality "requires cross-referencing with authorization records". Data: DETER/PRODES (CC BY-SA) plus the CAR registry, with an El Niño 2026–27 fire-risk overlay. See §15.1.
3. **EO-literature + EO-data agent.** ESA's EVE answers from text but has no imagery search until 2027; the openEO Agent picks naive methods; the JAXA Earth API has MCP. This matches the sponsor's "literature no human can read all of". See §6.2, §3.1, §12.3.
4. **Peak-burn-period fire intensity gap filler.** WildFireSat does not arrive until 2029; fire danger indices ignore fuel; alerts are delayed by downlinks. See §14.2, §8.2.
5. **ML-ready flood archive plus "did the forecast see it?" evaluation.** ECMWF Code for Earth #20 and #41: GFM/Kuro Siwo, IFS ENS on AWS, EM-DAT. See §19.2.
6. **Volcanic ash / pyroCb "grey zone" 3D product for aviation.** EarthCARE over Anak Krakatau (Sep 2026), plus S5P SO2 and GEO imagery. See §2.3.
7. **Sentinel-1 RFI detector and world RFI map.** Public ClearSAR set (3,940 quicklooks), relevant to spectrum policy. See §1.1, §6.3.
8. **Sovereignty stress test ("if US data went dark").** Sentinel-6C is stalled on a NASA radiometer; Biomass is blind under SOTR; Canada and India have gaps after RCM ageing and the PSLV failures. See §9.6.
9. **EUDR plot-level due diligence or environmental-crime evidence packs.** LPS25 F.04.20, E.05.01 and F.04.11. See §19.5.
10. **"Know when you don't know" disaster maps.** Wrap a foundation model with SHRUG-FM-style abstention for flood, burn-scar and landslide maps. See §19.4.

---

## 0. Headline status board (October 2026)

| Item | Status as of Oct 2026 | Source |
|---|---|---|
| Sentinel-1A | Retired; operations ended 29 Jun 2026, mission concluded 30 Jun 2026 | [ESA "Time to say goodbye to Sentinel-1A" (Jun 2026)](https://www.esa.int/Applications/Observing_the_Earth/Copernicus/Sentinel-1/Time_to_say_goodbye_to_Sentinel-1A); [EC DEFIS (30 Jun 2026)](https://defence-industry-space.ec.europa.eu/sentinel-1a-concludes-its-mission-leaving-lasting-legacy-copernicus-2026-06-30_en) |
| Sentinel-1C / 1D | 1C operational; 1D launched 4 Nov 2025 on Ariane 6 (VA265); 1C and 1D now fly 180° apart | [ESA press release (Nov 2025)](https://www.esa.int/Newsroom/Press_Releases/Copernicus_Sentinel-1D_reaches_orbit_on_Ariane_6); [Arianespace](https://ariane.group/en/news/with-ariane-6-arianespace-successfully-launches-copernicus-sentinel-1d-satellite/) |
| Sentinel-2A | Extended campaign since 13 Mar 2025, planned until May 2026. ESA was talking with the Commission about a further 19 months to end 2027, "pending funding availability" | [CDSE news (28 Feb 2025)](https://dataspace.copernicus.eu/news/2025-2-28-sentinel-2a-extended-campaign-starting-march-13-2025); [Floberghagen, FutureEO post-CM25 slides (24 Mar 2026)](https://climate.esa.int/media/documents/1_FutureEO_post-CM25_-_Floberghagen.pdf) |
| Sentinel-2B / 2C / 2D | 2B and 2C nominal (2C took over from 2A on 21 Jan 2025); 2D passed its Flight Acceptance Review and is in storage | [Floberghagen slides (Mar 2026)](https://climate.esa.int/media/documents/1_FutureEO_post-CM25_-_Floberghagen.pdf) |
| Sentinel-3C | Launched 15 Sep 2026 on Vega-C VV30 with FLEX; first images 8 Oct 2026; SLSTR imaged Hurricane Rachel on 2 Oct | [ESA press release N°50–2026](https://www.esa.int/Applications/Observing_the_Earth/FLEX_and_Sentinel-3C_launched); [ESA Observing the Earth (Oct 2026)](https://www.esa.int/Applications/Observing_the_Earth) |
| Sentinel-4 (on MTG-S1) | Launched Jul 2025; first images (NO2, O3, SO2) taken 8 Oct 2025; in commissioning; MTG-S1 first IRS images released 27 Jan 2026 | [EUMETSAT (Oct 2025)](https://www.eumetsat.int/first-copernicus-sentinel-4-images-showcase-europes-hourly-air-pollution-watch); [DLR (22 Oct 2025)](https://www.dlr.de/en/eoc/latest/news/2025/copernicus-sentinel-4-delivers-first-images-of-air-quality-over-europe) |
| Sentinel-5A (on MetOp-SG-A1) | Launched 13 Aug 2025 on Ariane 6; In-Orbit Commissioning Review passed; satellite SIOV review passed 4 Dec 2025 | [ESA press release (Aug 2025)](https://www.esa.int/Newsroom/Press_Releases/First_MetOp-SG_satellite_and_Sentinel-5A_launched); [Floberghagen slides](https://climate.esa.int/media/documents/1_FutureEO_post-CM25_-_Floberghagen.pdf) |
| Sentinel-6B | Launched 17 Nov 2025 (Falcon 9, Vandenberg); in-orbit validation finished early Feb 2026 | [ESA (Nov 2025)](https://www.esa.int/ESA_Multimedia/Images/2025/11/Sentinel-6B_launches); [Copernicus Marine](https://marine.copernicus.eu/news/sentinel-6b-launch-new-era-measuring-sea-level-space) |
| Sentinel-6C | Contract not approved "due to the uncertainties on the EUMETSAT contribution and on the availability of the NASA radiometer"; ESA is looking at speeding up Sentinel-6 NG instead | [Floberghagen slides (Mar 2026)](https://climate.esa.int/media/documents/1_FutureEO_post-CM25_-_Floberghagen.pdf) |
| MetOp-SG-B1 | Arrived at Kourou 20 Oct 2026; launch planned Q4 2026 | [ESA Observing the Earth](https://www.esa.int/Applications/Observing_the_Earth) |
| FLEX (Earth Explorer 8) | Launched 15 Sep 2026; will first fly in tandem with Sentinel-3A, later replaced in the formation by Sentinel-3C | [ESA](https://www.esa.int/Applications/Observing_the_Earth/FLEX_and_Sentinel-3C_launched) |
| Biomass (EE7) | Launched Apr 2025; commissioning complete; data open to all | [Floberghagen slides](https://climate.esa.int/media/documents/1_FutureEO_post-CM25_-_Floberghagen.pdf) |
| EarthCARE (EE6) | Operating; JAXA L2 products public since 17 Mar 2025; observed a volcanic plume (Oct 2026) and a fire cloud (Oct 2026) | [JAXA Satnavi (17 Mar 2025)](https://www.satnavi.jaxa.jp/en/news/2025/03/17/10746/index.html); [ESA Observing the Earth](https://www.esa.int/Applications/Observing_the_Earth) |
| Φsat-2 | Operations end planned for Q1 to Mar 2026; 2,535 registered data users by Feb 2026; ESA considering a one-year extension | [CEOS WGISS-61 slides (2026)](https://ceos.org/document_management/Working_Groups/WGISS/Meetings/WGISS-61/7.4_Phisat-2_ESA%20V3.pdf); [Floberghagen slides](https://climate.esa.int/media/documents/1_FutureEO_post-CM25_-_Floberghagen.pdf) |
| IRIDE (Italy) | Eaglet II launches completed the constellation (2 Oct 2026); first Eaglet II images show Gibraltar | [ESA Observing the Earth (Oct 2026)](https://www.esa.int/Applications/Observing_the_Earth) |
| ESA EVE (Earth Virtual Expert) | Φ-lab LLM for EO knowledge, introduced 8 Oct 2026; built on Mistral Small 3.2 24B | [ESA "Introducing ESA's Earth Virtual Expert" (Oct 2026)](https://www.esa.int/Applications/Observing_the_Earth/FutureEO/Introducing_ESA_s_Earth_Virtual_Expert); [HF eve-esa](https://huggingface.co/eve-esa) |
| CM25 (Bremen, 26–27 Nov 2025) | €22.1 bn (European Spaceflight, SpacePolicyOnline) or €22.3 bn (ESA slides); EOP €3.4 bn; FutureEO about €1.8 bn; CSC-4 €839 M; new ERS programme "massively subscribed" | [European Spaceflight (27 Nov 2025)](https://europeanspaceflight.com/?p=5630); [Floberghagen slides](https://climate.esa.int/media/documents/1_FutureEO_post-CM25_-_Floberghagen.pdf); [EARSC (13 Jan 2026)](https://earsc.org/2026/01/13/eocafe-esa-cm25-outcomes-and-opportunities-whats-next-for-the-eo-industry/) |

---

## 1. ESA / EU Earth observation: Copernicus Sentinels

### 1.1 Sentinel-1 (C-band SAR): constellation replenished, Sentinel-1A retired
- **What it is:** Copernicus C-band SAR. It images day and night through cloud and is the workhorse for floods, ships, sea ice, ground motion (InSAR) and oil spills. Sentinel-1B suffered a hardware failure and its mission ended in August 2022, which left a single-satellite gap until Sentinel-1C (launched Dec 2024) ([Wikipedia Copernicus Programme](https://en.wikipedia.org/wiki/Copernicus_Programme)). Sentinel-1D launched 4 Nov 2025 on Ariane 6 VA265 into a 693 km sun-synchronous orbit, 180° apart from 1C ([Arianespace](https://ariane.group/en/news/with-ariane-6-arianespace-successfully-launches-copernicus-sentinel-1d-satellite/); [ESA press release, Nov 2025](https://www.esa.int/Newsroom/Press_Releases/Copernicus_Sentinel-1D_reaches_orbit_on_Ariane_6)). Sentinel-1A ended operations on 29 Jun 2026, after about 12 years against a planned 7-year life ([ESA, Jun 2026](https://www.esa.int/Applications/Observing_the_Earth/Copernicus/Sentinel-1/Time_to_say_goodbye_to_Sentinel-1A); [CDSE notice](https://dataspace.copernicus.eu/node/4026); [EC DEFIS, 30 Jun 2026](https://defence-industry-space.ec.europa.eu/sentinel-1a-concludes-its-mission-leaving-lasting-legacy-copernicus-2026-06-30_en)). In March 2026 the "disposal approach" for 1A was still "under consolidation" ([Floberghagen slides, 24 Mar 2026](https://climate.esa.int/media/documents/1_FutureEO_post-CM25_-_Floberghagen.pdf)).
- **Problems / pain points:**
  - **Continuity risk.** After 1B failed, the constellation repeat went from 6 to 12 days for about 2.5 years *(6/12-day figures are standard Sentinel-1 specs, not re-verified here)*. Long InSAR time series have gaps in 2022–2024 and geometry changes between satellites.
  - **Radio-frequency interference (RFI).** "Shared frequency bands mean RFI can cause image artifacts, undetected biases, or complete data loss". Most RFI detection uses raw products that are too heavy to run in operations ([ESA Φ-lab ClearSAR challenge](https://platform-challenges.philab.esa.int/clear-sar)).
  - **End-of-life disposal** of 1A, a debris issue (cross-slice).
- **How they're trying to solve it:** 1C and 1D restore 6-day repeat. Sentinel-1 NG: "contract proposal approved at IPC and Proc Board. KO planned end March [2026]" ([Floberghagen slides](https://climate.esa.int/media/documents/1_FutureEO_post-CM25_-_Floberghagen.pdf)). The ClearSAR challenge targets RFI. ESA released curated, ready-to-use thematic SAR data collections on 22 Oct 2026 ([ESA Earth Online news listing, *search summary*](https://earth.esa.int/eogateway/news)).
- **Data:** Sentinel-1 GRD/SLC/OCN via the Copernicus Data Space Ecosystem (CDSE), free and open under the Copernicus licence. Also on AWS/Microsoft Planetary Computer (GRD, RTC). About 1 PB/year scale *(volume not verified on this pass)*.
- **Off-the-shelf tech:** SNAP / ESA SNAPPY, ISCE / MintPy, HyP3 (ASF), the EGMS (European Ground Motion Service) product, openEO, Sentinel Hub.
- **Hackathon angle:** (a) Build a "quicklook RFI detector" on the public ClearSAR set: 3,940 RGB quicklooks, 3,154 with bounding boxes, scored by mAP. Then map *where* in the world RFI hits (spectrum-policy evidence). (b) Use a 1C/1D 6-day stack to detect flood extent or ships for a live event.
- **Credibility:** official.
- **Sources:** as linked above.

### 1.2 Sentinel-2 (optical, 10 m, 13 bands): 2A extended campaign, 2C operational, funding-dependent extension
- **What it is:** Copernicus multispectral imager, the most-used open optical dataset in the world. Sentinel-2C launched Sep 2024 and replaced 2A on 21 Jan 2025 "between two consecutive orbits". 2A then began an "extended campaign" on 13 Mar 2025, planned for one year, to "increase global revisit frequency and maximise revisit frequency over Europe and tropical regions of Africa and South America" ([CDSE news, 28 Feb 2025](https://dataspace.copernicus.eu/news/2025-2-28-sentinel-2a-extended-campaign-starting-march-13-2025); [EC DEFIS, 6 Feb 2025](https://defence-industry-space.ec.europa.eu/sentinel-2a-extending-operations-meet-user-needs-2025-02-06_en)). As of March 2026: "Extended campaign ongoing since March 2025, until May 2026. Discussions on-going with COM for a further 19 months extension until end 2027 (pending funding availability)". Sentinel-2D "successful Flight Acceptance Review, satellite in storage" ([Floberghagen slides, 24 Mar 2026](https://climate.esa.int/media/documents/1_FutureEO_post-CM25_-_Floberghagen.pdf)).
- **Problems / pain points:**
  - **Revisit vs cloud cover**, especially in the tropics. This is why 2A was kept flying.
  - **The extension is "pending funding availability"**: the EU pays for operations, not ESA.
  - The EC calls the extension a pilot, "subject to an assessment to evaluate its efficiency and potential continuation" ([EC DEFIS](https://defence-industry-space.ec.europa.eu/sentinel-2a-extending-operations-meet-user-needs-2025-02-06_en)). So there is an *open question about the value of a fourth-satellite revisit*.
- **How they're trying to solve it:** 3-satellite operations (2A, 2B, 2C). Sentinel-2 NG is in Phase B1 ISRR, with B2/C/D/E1 funded at CM25 ([Floberghagen slides](https://climate.esa.int/media/documents/1_FutureEO_post-CM25_-_Floberghagen.pdf)).
- **Data:** L1C/L2A via CDSE; also AWS Open Data (COGs), Planetary Computer, Google Earth Engine. Free and open (Copernicus licence).
- **Off-the-shelf tech:** Sen2Cor, s2cloudless / OmniCloudMask, SatlasPretrain, TerraMind, Prithvi-EO-2.0, Major TOM embeddings.
- **Hackathon angle:** "Was the 2A extended campaign worth it?" Quantify, by region, how many extra cloud-free observations the third satellite gave in 2025–26 (e.g., over the Amazon and Congo) versus a 2-satellite baseline. That is a concrete evidence product for the EC's efficiency assessment. Metadata-only analysis on the STAC catalogue is feasible in 36 h.
- **Credibility:** official.
- **Sources:** as linked.

### 1.3 Sentinel-3 (ocean/land colour, SLSTR temperature, SRAL altimetry): Sentinel-3C launched Sep 2026
- **What it is:** Sentinel-3C launched 15 Sep 2026 on Vega-C VV30, the first Vega-C dual launch (with FLEX, using the Vespa adapter). It returned first views 8 Oct 2026 and imaged Hurricane Rachel 2 Oct 2026. Once operational it is handed to EUMETSAT ([ESA press release N°50–2026](https://www.esa.int/Applications/Observing_the_Earth/FLEX_and_Sentinel-3C_launched); [ESA Observing the Earth](https://www.esa.int/Applications/Observing_the_Earth)). Sentinel-3D is in storage. Sentinel-3 NG Optical and NG Topography are in procurement ([Floberghagen slides](https://climate.esa.int/media/documents/1_FutureEO_post-CM25_-_Floberghagen.pdf)).
- **Problems / pain points:** 300 m OLCI is too coarse for small water bodies and coasts. SLSTR at 1 km is too coarse for urban heat (LSTM will help). Sentinel-3A is ageing, which is why 3C replaces it in the FLEX tandem.
- **How they're trying to solve it:** 3C launch; S3 NGO funded at CM25.
- **Data:** EUMETSAT Data Store and CDSE (marine products via EUMETSAT, land via CDSE). Free.
- **Off-the-shelf tech:** SNAP S3 toolbox, C2RCC (water quality), Copernicus Marine Toolbox.
- **Hackathon angle:** Sentinel-3 OLCI plus Sentinel-2 fusion for harmful algal bloom early warning on lakes (see CMEMS and C3S below).
- **Credibility:** official.

### 1.4 Sentinel-4 and Sentinel-5 / 5P (atmospheric composition)
- **What it is:** Sentinel-4 is a UVN spectrometer on MTG-Sounder (MTG-S1) in GEO. It gives *hourly* NO2/O3/SO2/HCHO/aerosol over Europe and North Africa. MTG-S1 launched July 2025 (DLR gives 4 July; RAL Space had a 1 July plan). First images were taken 8 Oct 2025 and showed NO2 over the Po Valley, O3 over the Balkans and SO2 plumes ([EUMETSAT](https://www.eumetsat.int/first-copernicus-sentinel-4-images-showcase-europes-hourly-air-pollution-watch); [DLR, 22 Oct 2025](https://www.dlr.de/en/eoc/latest/news/2025/copernicus-sentinel-4-delivers-first-images-of-air-quality-over-europe)). The MTG-S1 Infrared Sounder released first images 27 Jan 2026 ([Floberghagen slides](https://climate.esa.int/media/documents/1_FutureEO_post-CM25_-_Floberghagen.pdf)). Sentinel-5 (on MetOp-SG-A1) launched 13 Aug 2025 on Ariane 6 from Kourou ([ESA press release](https://www.esa.int/Newsroom/Press_Releases/First_MetOp-SG_satellite_and_Sentinel-5A_launched)). Sentinel-5P/TROPOMI is still in "nominal operations with continuous high performance" ([Floberghagen slides](https://climate.esa.int/media/documents/1_FutureEO_post-CM25_-_Floberghagen.pdf)).
- **Problems / pain points:** Hourly GEO data is a new regime: diurnal cycles of NO2, morning rush hour, plume transport. Users are not yet set up for 10–20× more scenes. Commissioning means data are "preliminary"; EUMETSAT says hourly streams will be available "once commissioning is complete". The CAMS resolution (about 40 km global, about 10 km Europe) is too coarse for local health exposure ([Φ-lab Air Quality & Health challenge](https://platform-challenges.philab.esa.int/air-quality-and-health)).
- **How they're trying to solve it:** CAMS assimilation; the Φ-lab/ECMWF AI downscaling challenge; CAMS National Collaboration Programme downscaling ([CAMS user forum slides, Peuch](https://atmosphere.copernicus.eu/sites/default/files/custom-uploads/CAMS%207th%20GA/Atmosphere-user-forum/6a.%20PEUCH%20downscaling%20.pdf)). An EGU25 study downscaled CAMS reanalyses from about 10 km to 1 km for Europe ([EGU25-9157](https://meetingorganizer.copernicus.org/EGU25/EGU25-9157.html)).
- **Data:** Sentinel-5P L2 via CDSE (free). Sentinel-4 L2 via EUMETSAT once released. CAMS via the Atmosphere Data Store (ADS). EEA air-quality station data (in situ).
- **Off-the-shelf tech:** xarray, Harp, Google Earth Engine S5P collections, ERA5/CAMS via cdsapi.
- **Hackathon angle:** "Hourly emissions fingerprinting": use the first months of Sentinel-4 hourly NO2 (where public) or TROPOMI daily NO2 plus wind to attribute plumes to individual power plants, ports or highways in the Po Valley. Or: 1 km street-level NO2 exposure downscaling with S5P plus land use plus EEA stations.
- **Credibility:** official.

### 1.5 Sentinel-6 (reference altimetry) and the Sentinel-6C funding gap
- **What it is:** Sentinel-6B launched 17 Nov 2025 (UTC) on Falcon 9 from Vandenberg, continuing the reference sea-level record "until at least 2030". It flies in tandem with Sentinel-6 Michael Freilich for one year for cross-calibration ([ESA](https://www.esa.int/ESA_Multimedia/Images/2025/11/Sentinel-6B_launches); [Copernicus Marine](https://marine.copernicus.eu/news/sentinel-6b-launch-new-era-measuring-sea-level-space); [Ocean News](https://oceannews.com/news/science-technology/sentinel-6b-launched-to-extend-record-of-sea-level-rise)). Copernicus Marine cites 3.7 mm/yr average sea-level rise 1993–2024.
- **Problems / pain points:** **Sentinel-6C: "due to the uncertainties on the EUMETSAT contribution and on the availability of the NASA radiometer, contract proposal has not been approved. ESA working on a new approach based on S6 NG acceleration"** ([Floberghagen slides, 24 Mar 2026](https://climate.esa.int/media/documents/1_FutureEO_post-CM25_-_Floberghagen.pdf)). This is a concrete example of US budget uncertainty (the NASA AMR-C radiometer) threatening a European climate data record. Cross-slice: US agencies.
- **How they're trying to solve it:** Accelerate Sentinel-6 NG (Phase A/B1 in FutureEO; procurement proposal submitted to IPC).
- **Data:** Sentinel-6 L2 via EUMETSAT/CDSE/PO.DAAC. CMEMS sea level products. Free.
- **Hackathon angle:** "Gap-risk simulator": show how a 1–3 year gap in reference altimetry (if 6C slips) would raise uncertainty in the global mean sea-level trend. Use the existing 30-year record with synthetic gaps and cross-calibration offsets. This frames a very clear policy problem.
- **Credibility:** official (ESA slides).

### 1.6 Sentinel-1C/1D one-day repeat window (mid-April to end of June 2026): an unusual dataset
- **What it is:** From mid-April to the end of June 2026 the constellation ran with three satellites. "Sentinel-1D follows the Sentinel-1C ground track and repeats its acquisitions one day later." In the second half of June, 1C manoeuvred for about two weeks, "will not be acquiring", to restore a 6-day C/D revisit. The new C/D orbit "shift[s] the 6-day revisit pattern by one day" relative to the old A/B pattern. Sentinel-1D user data opened 17 Apr 2026 ([CDSE, 2 Apr 2026](https://dataspace.copernicus.eu/news/2026-4-2-sentinel-1d-user-data-opening-and-future-plans)). The final orbital configuration was reached 24 Jun 2026 ([CDSE news list](https://dataspace.copernicus.eu/news)).
- **Problems / pain points:**
  - Sentinel-1D SAR data from 29 May 2026 16:03 UTC to 1 Jun 2026 18:00 UTC are degraded because the instrument's "internal clock [was] temporarily corrupted" ([CDSE, 4 Jun 2026](https://dataspace.copernicus.eu/news/2026-6-4-sentinel-1d-sar-data-quality-degradation)).
  - Many unavailability notices for S1A/S1C/S1D in Jan–May 2026 ([CDSE news list](https://dataspace.copernicus.eu/news)).
  - The phase change breaks pipelines that assume the A/B acquisition calendar.
- **How they're trying to solve it:** MPC quality disclaimers (sar-mpc.eu disclaimer 379); a new Sentinel-1 L1/L2 processing baseline on 22 Oct 2026 ([CDSE news list](https://dataspace.copernicus.eu/news)).
- **Data:** About 2.5 months of 1-day-baseline C-band pairs, free on CDSE. This is the shortest Sentinel-1 repeat ever available. The previous best was 6 days with A/B; 1-day C-band repeat had not been seen since the ERS-1/2 tandem in the 1990s *(that historical comparison is background knowledge, not verified on this pass)*.
- **Off-the-shelf tech:** ISCE3, SNAP, HyP3 (ASF on-demand InSAR), MintPy.
- **Hackathon angle:** "1-day coherence atlas": map where C-band coherence survives 1 day versus 6 days (glacier flow, fast landslides, crop growth, wet snow). Or detect very fast ground motion such as glacier surges that 6-day pairs alias. The project would be novel because this short-baseline window will not recur.
- **Credibility:** official.

### 1.7 Copernicus Expansion missions (CO2M, CHIME, CIMR, CRISTAL, LSTM, ROSE-L) and Next Generation
- **What it is:** Six "High-Priority Candidate Missions" fill Copernicus observation gaps ([ESA Expansion missions page](https://www.esa.int/Applications/Observing_the_Earth/Copernicus/Copernicus_Sentinel_Expansion_missions)):
  - **CO2M (Sentinel-7):** CO2 and CH4 spectrometer to estimate *anthropogenic* emissions "at local, national, and regional scales" for Paris Agreement and EU decarbonisation policy.
  - **CHIME (Sentinel-10):** hyperspectral imager for crop and soil properties, minerals, inland and coastal water.
  - **CIMR (Sentinel-11):** wide-swath conically scanning multi-frequency microwave radiometer for SST, sea-ice concentration and salinity.
  - **CRISTAL (Sentinel-9):** dual-frequency radar altimeter for sea-ice thickness, snow on sea ice, ice-sheet height, rivers and lakes.
  - **LSTM (Sentinel-8):** high-resolution thermal IR for land surface temperature, evapotranspiration, drought, urban heat.
  - **ROSE-L (Sentinel-12):** L-band SAR for geohazards, forest, food security, maritime and the Arctic.
- **Problems / pain points:**
  - **Schedule slip.** CO2M was originally aimed at "the end of 2025". An ESA/EUMETSAT advisory group now gives 2027 (CO2M-A), 2028 (B) and 2029 (C) ([ESA CO2M Mission Advisory Group page](https://missionadvice.esa.int/?p=760); [Wikipedia Copernicus Programme, community-edited](https://en.wikipedia.org/wiki/Copernicus_Programme)). Wikipedia lists LSTM-A 2028, CRISTAL-A 2028, CHIME-A 2028, CIMR-A 2029, ROSE-L A "2028 or 2029", and B units in 2030–2031. WMO OSCAR lists later ranges, e.g. CHIME-A 2029–2034 and ROSE-L A 2030–2035 ([WMO OSCAR](https://space.oscar.wmo.int/satelliteprogrammes/view/copernicus_sentinel_expansion_missions)).
  - **Funding.** Completing the Expansion missions depended on the UK re-entering Copernicus (decided October 2024) ([Wikipedia](https://en.wikipedia.org/wiki/Copernicus_Programme)). A January 2026 article says funding is "now secured for all six" ([Ecoticias, trade press](https://www.ecoticias.com/en/europe-has-just-secured-a-new-generation-of-satellites-that-will-monitor-emissions-ice-oceans-and-crops-like-never-before/25493/)).
  - The 2028–2034 EU budget (MFF) is still under negotiation. Industry (Eurospace) asks for a ring-fenced €40–60 bn space envelope versus about €19 bn today ([Eurospace position](https://eurospace.org/?p=7551); [EPRS MFF briefing](https://www.europarl.europa.eu/thinktank/en/document/EPRS_BRI(2025)775885)).
  - CSC-4 (Copernicus Space Component phase 3) was "substantially fully subscribed at 839 million euros" at CM25 ([EARSC EOcafé, Jan 2026](https://earsc.org/2026/01/13/eocafe-esa-cm25-outcomes-and-opportunities-whats-next-for-the-eo-industry/), *search summary*).
- **How they're trying to solve it:** Hardware progress as of March 2026 ([Floberghagen slides](https://climate.esa.int/media/documents/1_FutureEO_post-CM25_-_Floberghagen.pdf)):
  - CO2M: platform and payload AIT proceeding; a CO2M instrument passed vacuum testing (Jun 2026) ([ESA Expansion page, related articles](https://www.esa.int/Applications/Observing_the_Earth/Copernicus/Copernicus_Sentinel_Expansion_missions)).
  - CRISTAL: AOCS closed-loop tests done.
  - CHIME: system CDR close-out.
  - CIMR: Large Deployable Reflector EQM test readiness review.
  - LSTM: platform integration.
  - ROSE-L: SAR structural-model antenna wing deployed.
  - Next Generation: S1-NG kick-off end of March 2026; S2-NG Phase B1; S3-NG TOPO offers under evaluation; S3-NG OPT Phase B1; S6-NG Phase A/B1.
- **Data (now):** Precursors that teams can use today: PRISMA (ASI), EnMAP (DLR) and EMIT (NASA) for CHIME-like hyperspectral data; ECOSTRESS and Landsat TIRS for LSTM-like thermal data; ALOS-2/4, SAOCOM and NISAR for ROSE-L-like L-band; OCO-2/3, GOSAT-2 and GOSAT-GW for CO2M-like data; CryoSat-2, ICESat-2 and SWOT for CRISTAL-like data; AMSR2 and AMSR3 (GOSAT-GW) for CIMR-like data.
- **Off-the-shelf tech:** HyperSpectral foundation models (e.g., SpectralGPT), the EnMAP-Box, the CO2M L2 prototype algorithm (unverified availability).
- **Hackathon angle:** (a) "CO2M before CO2M": point-source CO2/CH4 plume inversion with existing OCO-3 SAM / EMIT / TROPOMI data for the EU's largest emitters (EU ETS verified emissions as ground truth). (b) "CHIME simulator": build a crop/soil nutrient product from EnMAP or PRISMA (HYPERVIEW2 data exist) so users are ready when CHIME flies.
- **Credibility:** official (ESA slides and pages); Wikipedia and Ecoticias are secondary.

---

## 2. ESA Earth Explorers and FutureEO

### 2.1 FutureEO programme and CM25 outcome for Earth observation
- **What it is:** ESA's research EO envelope programme. In March 2026: 22 missions in preparation or development, 9 launched, 7 in orbit, 15 scientific campaigns, €1.5 bn to industry in 5 years, "ca 1PB Data downloaded (in 2023)", 400+ papers/year from Earth Explorer data ([Floberghagen, ESA FutureEO post-CM25, 24 Mar 2026](https://climate.esa.int/media/documents/1_FutureEO_post-CM25_-_Floberghagen.pdf)).
- **CM25 outcome:**
  - "Extremely positive results for Earth Observation: 3.4B€ subscribed to EOP"; FutureEO about 1,800 M€.
  - "From CM22, the EO subscribed programmes increase by 27% (+8% if we consider the inflation)".
  - All lines secured: S2 NG, S3 NGO, NGGM (B2/C), WIVERN (phase B only), Scouts 3rd wave, Harmony (launchers and phase E1), mission ops, cal/val, campaigns, data quality, and Earth Action.
  - "A new programme is born: European Resilience from Space (ERS) – Massively subscribed" ([same slides](https://climate.esa.int/media/documents/1_FutureEO_post-CM25_-_Floberghagen.pdf)).
  - The ESA headline for the whole agency is "A record 22.3 B€ budget for ESA at CM25". European Spaceflight reports €22.1 bn against €22.25 bn proposed ([European Spaceflight, 27 Nov 2025](https://europeanspaceflight.com/?p=5630)). SpacePolicyOnline reports €22.070 bn approved against €22.254 bn proposed ([SpacePolicyOnline](https://spacepolicyonline.com/?p=85281), *search summary*).
- **New "Earth Action" pillar:** It merges CCI / Climate Space, GDA (Global Development Assistance) and Φ-lab. It addresses "the 'triple crisis' Climate Change, Biodiversity Loss, Pollution/Waste" and aligns with development finance: "Current alignment with EOP programs ~150M€ DG RTD, 75M$ with IFI (GDA) and ~55M€ so far delegated by INTPA". Potential partners listed are the World Bank, ADB, Global Gateway and the Green Climate Fund ([slides](https://climate.esa.int/media/documents/1_FutureEO_post-CM25_-_Floberghagen.pdf)).
- **Problems / pain points (stated objectives):** "Ensure availability and uptake of valorised EO data & information products". "Further develop space solutions to enable Earth action, addressing climate, sustainability, SDGs, food security, regulatory enforcement, water & carbon management". **The uptake gap is ESA's own stated problem.**
- **Hackathon angle:** Any "uptake" product that turns open EO into a decision for a non-expert user, for example regulatory enforcement such as EUDR deforestation-free supply chains, or water and carbon management, fits ESA's stated Earth Action objective word for word.
- **Credibility:** official.

### 2.2 Biomass (Earth Explorer 7): first P-band SAR in space
- **What it is:** Launched 29 Apr 2025 on Vega-C. Fully polarimetric P-band SAR, 12 m reflector, dawn-dusk SSO at 666 km, 3-day repeat for interferometry, minimum life 5.5 years. Objective: "first global, repeat systematic estimates of forest biomass and height to reduce uncertainties in land carbon stocks and fluxes" ([ESA Biomass facts](https://www.esa.int/Applications/Observing_the_Earth/FutureEO/Biomass/Facts_and_figures)). Data "open and accessible to all" since 26 Jan 2026. Phases: an 18-month tomographic global phase, then 9-month interferometric global coverages ([ESA, 26 Jan 2026](https://www.esa.int/Applications/Observing_the_Earth/FutureEO/Biomass/ESA_s_Biomass_goes_live_with_data_now_open_to_all)). Other stories: Brazil preparing to use Biomass data (13 Nov 2025); Niger Delta mangrove degradation images (9 Sep 2026) ([ESA Biomass hub](https://www.esa.int/Applications/Observing_the_Earth/FutureEO/Biomass)).
- **Problems / pain points:**
  - "lack of accurate, global data on how much carbon is stored in forests" (Klaus Scipal, quoted by [ESA](https://www.esa.int/Applications/Observing_the_Earth/FutureEO/Biomass/ESA_s_Biomass_goes_live_with_data_now_open_to_all)).
  - **RFI and a US radar restriction.** A 2025 overview says RFI "requires blanking transmissions over parts of Europe and North America". A paper says "restrictions imposed by the U.S. Space Object Tracking Radar (SOTR) have led to the implementation of a global acquisition mask, limiting data access and spatial coverage" ([LCLUC/UMD announcement](https://lcluc.umd.edu/announcements/esas-biomass-forest-carbon-maps-progressive-release); [EO College](https://eo-college.org/?p=388510); both *search summaries*, unverified on the primary page). So Biomass has *no* data over much of Europe and North America by design.
  - The "full potential of Biomass has yet to be realised"; calibration is still being checked against airborne data ([ESA](https://www.esa.int/Applications/Observing_the_Earth/FutureEO/Biomass/ESA_s_Biomass_goes_live_with_data_now_open_to_all)).
- **How they're trying to solve it:** Progressive releases of refined biomass and carbon maps through 2026 ([LCLUC](https://lcluc.umd.edu/announcements/esas-biomass-forest-carbon-maps-progressive-release)); cal/val campaigns (AfriSAR-type).
- **Data:** ESA Earth Online Biomass data ([portal link via ESA](https://earth.esa.int/eogateway/missions/biomass/biomass-data)); ESA–NASA MAAP. Open.
- **Off-the-shelf tech:** ESA MAAP, SNAP P-band support (unverified), GEDI L4A/L4B biomass for comparison, ESA CCI Biomass maps.
- **Hackathon angle:** "Carbon cross-check": compare first Biomass AGB transects (Gabon, Congo, Cameroon, CAR) with GEDI L4B, ESA CCI Biomass and the NASA/JPL maps. Flag disagreement hot spots, which is an MRV problem for REDD+ and carbon credits. Or map the SOTR/RFI acquisition mask itself as a "where Biomass is blind" layer.
- **Credibility:** official, plus unverified secondary on the RFI and SOTR claims.

### 2.3 EarthCARE (Earth Explorer 6, with JAXA)
- **What it is:** ESA–JAXA cloud, aerosol and radiation explorer (lidar ATLID, cloud profiling radar CPR, multispectral imager MSI, broadband radiometer BBR). JAXA began public L2 release on 17 Mar 2025 ([JAXA Satnavi](https://www.satnavi.jaxa.jp/en/news/2025/03/17/10746/index.html)). ESA L2 products followed at the in-orbit validation workshop ([ACTRIS](https://actris.eu/news-events/news/close-look-earthcare-data-during-esa-jaxa-earthcare-orbit-validation-workshop)). Products: single-sensor and "synergy" products, e.g. aerosol extinction profiles, boundary layer height, aerosol type ([ESA EarthCARE data products](https://www.esa.int/Applications/Observing_the_Earth/FutureEO/EarthCARE/EarthCARE_data_products)). As of March 2026: "BBR operations adapted to match 10y lifetime estimate. L2 products released at Science & Validation WS 1-5 Dec., Tokyo" ([Floberghagen slides](https://climate.esa.int/media/documents/1_FutureEO_post-CM25_-_Floberghagen.pdf)). Recent stories: a volcanic plume view that "boosts air safety" (1 Oct 2026) and a "rare fire cloud over Europe" (14 Oct 2026) ([ESA Observing the Earth](https://www.esa.int/Applications/Observing_the_Earth)).
- **Problems / pain points:** Cloud–aerosol–radiation interactions are the largest uncertainty in climate sensitivity *(general knowledge)*. Aviation needs better volcanic ash vertical profiles. Pyrocumulonimbus (fire cloud) frequency is rising in Europe.
- **Data:** ESA (EO-CAT / MAAP) and JAXA G-Portal; open after registration.
- **Hackathon angle:** "Ash layer altitude for aviation": combine EarthCARE ATLID curtains with Sentinel-5P SO2 and MTG FCI imagery to give a 3D ash or smoke layer product for one event (Oct 2026 plume). Or a pyroCb detector over Europe using MTG-FCI plus EarthCARE validation.
- **Credibility:** official.

### 2.4 FLEX (Earth Explorer 8): launched 15 Sep 2026
- **What it is:** First satellite designed to measure photosynthetic activity (solar-induced chlorophyll fluorescence) using the FLORIS spectrometer. It will fly in tandem with Sentinel-3A, later replaced by Sentinel-3C, so fluorescence can be combined "with near-simultaneous Sentinel-3 observations of clouds, aerosols, water vapour, surface temperature, land-cover type". Purpose: "advance our understanding of plant health and the role of photosynthesis in the carbon and water cycles" ([ESA press release N°50–2026](https://www.esa.int/Applications/Observing_the_Earth/FLEX_and_Sentinel-3C_launched)). Product: monthly global maps at 300 m × 300 m ([search summary of ESA FLEX facts](https://www.esa.int/Applications/Observing_the_Earth/FLEX/Facts_and_figures)).
- **Problems / pain points:** Vegetation indices (NDVI) show greenness, not photosynthetic function. Crop stress is detected late. Commissioning means no science data yet in Oct 2026.
- **Data now:** TROPOMI SIF and OCO-2/3 SIF as stand-ins; Sentinel-3 OLCI.
- **Hackathon angle:** "Stress before brown": a demo showing SIF (TROPOMI) dropping before NDVI during the 2025/2026 European heat and drought, with a pipeline ready to swap in FLEX data. The JRC reported "worsening drought and record heat in Europe" on 12 Aug 2026 ([Copernicus EMS front page](https://emergency.copernicus.eu/)).
- **Credibility:** official.

### 2.5 FORUM, Harmony, WIVERN, NGGM, Scouts, ALTIUS, Aeolus-2, TRUTHS (pipeline)
- **FORUM (EE9):** far-infrared outgoing radiation. "System CDR Successfully closed" (Mar 2026) ([Floberghagen slides](https://climate.esa.int/media/documents/1_FutureEO_post-CM25_-_Floberghagen.pdf)).
- **Harmony (EE10):** two receive-only satellites flying with Sentinel-1 for ocean, ice and land motion. "On-track for end of year CDR"; dual-launch adapter kick-off Q1 2026; CM25 funded "launchers and phase E1" ([slides](https://climate.esa.int/media/documents/1_FutureEO_post-CM25_-_Floberghagen.pdf)).
- **WIVERN (EE11):** Doppler wind radar in clouds. Phase B1 kicked off with 2 parallel consortia; CM25 funded "phase B only" ([slides](https://climate.esa.int/media/documents/1_FutureEO_post-CM25_-_Floberghagen.pdf)).
- **EE12:** "Ongoing Phase 0 … iterations on cost reduction measures". A User Consultation Meeting was set for 8–9 July 2026 ([slides](https://climate.esa.int/media/documents/1_FutureEO_post-CM25_-_Floberghagen.pdf)). This shows cost pressure in the pipeline.
- **NGGM / MAGIC (gravity):** bridging phase, SRR summer 2026 ([slides](https://climate.esa.int/media/documents/1_FutureEO_post-CM25_-_Floberghagen.pdf)).
- **Scouts:**
  - HydroGNSS (Scout-2) is commissioning, with "Successful acquisition of the E5/L5 reflections".
  - NanoMagSat (Scout-3) is in launcher selection.
  - Tango (Scout-4, CO2/NO2 plume imaging) has SRR closeout progressing.
  - Scouts 5 and 6 are funded ([slides](https://climate.esa.int/media/documents/1_FutureEO_post-CM25_-_Floberghagen.pdf)).
- **Aeolus (ended 2023):** "Development of Baseline 17 progressing nominally public release summer 2027". Aeolus-2 (EPS-Aeolus) got PATP for Phase B2 on 28 Jan 2026 ([slides](https://climate.esa.int/media/documents/1_FutureEO_post-CM25_-_Floberghagen.pdf)).
- **SMOS** (16+ years), **CryoSat** (15+ years) and **Swarm** (12+ years) are still performing excellently ([slides](https://climate.esa.int/media/documents/1_FutureEO_post-CM25_-_Floberghagen.pdf)). These are ageing assets with no like-for-like successors for some (e.g., SMOS L-band salinity until CIMR).
- **TRUTHS** (UK-led climate calibration "metrology lab in space"): not mentioned in the CM25 EOP "secured" list in the March 2026 slides. Its status after the UK's reduced CM25 contribution (−€172 M, share down from 11.2% to 7.7%, per [European Spaceflight](https://europeanspaceflight.com/?p=5630)) is **unverified**; see "Leads not followed".
- **Hackathon angle:** "Ageing fleet risk dashboard": list every European climate data record that relies on a satellite past its design life (SMOS, CryoSat, Swarm, Sentinel-3A, TerraSAR-X), with the expected successor and the gap length. This is a clear problem with clear data.
- **Credibility:** official.

---

## 3. Copernicus Data Space Ecosystem (CDSE), openEO and access infrastructure

### 3.1 CDSE: scale, outages, AI agent
- **What it is:** The EU's official Copernicus data access and processing platform, run by a consortium for ESA and the EC since 2023. It includes the Copernicus Browser, STAC/OData catalogues, Sentinel Hub APIs, openEO, JupyterLab and S3 access.
- **Scale (Annual Report 2025, released 24 Sep 2026):**
  - 542,622 registered users by Dec 2025 (251,659 new in 2025).
  - **>242 PB delivered in 2025**, of which 129.9 PB were Sentinel downloads across 14.7 billion download events; direct Sentinel downloads exceeded 100 PB for the first time.
  - 78.4% of download volume went to European users.
  - >120 million products in the archive; about 91 PB online.
  - Sentinel Hub handled >2.5 billion requests; openEO powers >75% of Copernicus Browser processing ([CDSE, 24 Sep 2026](https://dataspace.copernicus.eu/news/2026-9-24-copernicus-data-space-ecosystem-cdse-releases-annual-report-2025)).
- **Problems / pain points:**
  - **Reliability.** The 2026 news list shows dozens of unavailability and delay notices: Sentinel-1/2/3/5P data, openEO outages (e.g., 29 Jun 2026) and batch-job issues, Catalogue API (28 and 30 Jan), STAC API (5 Mar), networking (16–17 Mar), and forum/docs/marketplace down (23 Mar) ([CDSE news](https://dataspace.copernicus.eu/news)).
  - **Credits and quotas.** "Platform-wide openEO credit billing updates" were announced 2 Mar 2026 ([CDSE news](https://dataspace.copernicus.eu/news)).
  - **Environmental footprint of data use.** ESA and Capgemini launched a survey on "CDSE data usage and environmental sustainability" on 16 Jan 2026 ([CDSE news](https://dataspace.copernicus.eu/news)).
- **How they're trying to solve it:**
  - **openEO Agent (5 Oct 2026).** An AI assistant that turns user questions into openEO process graphs, validates them, submits batch jobs and reads failure logs. "Powered by Claude Sonnet 5", with RAG over openEO/Python docs and live collection discovery via MCP. It needs user approval before running. Limited access at chat.openeo.vito.be. Python client only, CDSE backend only. Known limitation: method choices "may default to basic vegetation-index approaches" for crop classification ([CDSE, 5 Oct 2026](https://dataspace.copernicus.eu/news/2026-10-5-openeo-agent-questions-turn-earth-observation-workflow)).
  - New STAC backend; large-area processing; openEO became an OGC community standard (May 2026) ([CDSE news](https://dataspace.copernicus.eu/news)).
- **Data:** Free and open Copernicus data and Contributing Missions. API access needs an account; heavy processing is limited by credit quotas.
- **Off-the-shelf tech:** openEO Python client, Sentinel Hub Process API, pystac-client, CDSE S3, the openEO MCP tools.
- **Hackathon angle:** (a) Build a *better* open agent than the openEO Agent for one vertical, e.g. "insurer flood-claim checker" or "EUDR plot deforestation checker", using the same open APIs. The openEO Agent's stated weakness (naive methods) is a ready pitch. (b) A "CDSE status oracle": scrape CDSE notices plus the STAC catalogue to tell an operational user, in real time, whether their area or product is affected by an outage, a degraded acquisition (e.g., the S1D clock corruption) or a processing-baseline change.
- **Credibility:** official.

---

## 4. Copernicus core services and the problems they report

### 4.1 Copernicus Emergency Management Service (CEMS)
- **What it is:** On-demand (rapid) mapping; floods (EFAS, GloFAS); wildfires (EFFIS/GWIS); droughts (EDO, GDO); exposure mapping (GHSL) ([CEMS portal](https://emergency.copernicus.eu/)).
- **Recent activations (2026):**
  - EMSR927 flood in Nepal (report 26 Aug 2026)
  - EMSR933 flood in Crete (4 Oct 2026)
  - EMSR934 earthquake in Panama (9 Oct 2026)
  - EMSR935 flood in the Alicante–Valencia regions, Spain (19 Oct 2026)
  - JRC news on "worsening drought and record heat in Europe" (12 Aug 2026) ([CEMS portal](https://emergency.copernicus.eu/))
  - A workshop on "AI for building damage assessment after earthquakes and storms" is listed for 10 Nov 2026 ([CEMS portal](https://emergency.copernicus.eu/)).
- **Problems / pain points:** Building damage assessment is still largely manual ("Mapping earthquake damage still depends heavily on human interpretation of satellite imagery, which is slow when time is critical", [Φ-lab challenge text](https://philab.esa.int/a-bold-new-chapter-for-ai4eo-with-esa-%cf%86-lab-challenges/)). Optical tasking is blocked by cloud during floods. Delivery takes hours to days.
- **How they're trying to solve it:** AI damage-assessment workshops; the Φ-lab "AI for Earthquake Response" challenge with Charter data; SAR-based flood mapping (the GFM component of GloFAS).
- **Data:** CEMS rapid mapping vector products (open download, EMSR codes); EFAS/GloFAS (GloFAS data open via CDS / EWDS); EFFIS burnt areas (open).
- **Off-the-shelf tech:** xView2 baseline models, ChangeOS, the Microsoft building damage model, Prithvi/TerraMind fine-tunes (ImpactMesh flood and fire, [IBM Research](https://research.ibm.com/blog/geospatial-flood-and-wildfire-mapping)).
- **Hackathon angle:** "EMSR935 in 36 hours": run Sentinel-1 (6-day C/D) flood mapping plus Sentinel-2 over Alicante–Valencia for the Oct 2026 event. Compare with the official CEMS delineation, and measure time-to-map and agreement.
- **Credibility:** official.

### 4.2 CAMS (Atmosphere Monitoring Service)
- **What it is:** Global and European air-quality forecasts and reanalyses, emissions, greenhouse gases and the solar radiation service. Data come through the Atmosphere Data Store.
- **Problems / pain points:** Global surface pollutant information at about 40 km and about 10 km over Europe, which is too coarse for local health. "In situ datasets are often incomplete, poorly connected, or in incompatible formats" ([Φ-lab Air Quality & Health challenge](https://platform-challenges.philab.esa.int/air-quality-and-health); [challenge blog](https://platform-challenges.philab.esa.int/blog/introducing-the-air-quality-and-health-challenge)). CAMS also aims for European AQ maps "with a high degree of consistency at the borders" ([CAMS user forum, Peuch](https://atmosphere.copernicus.eu/sites/default/files/custom-uploads/CAMS%207th%20GA/Atmosphere-user-forum/6a.%20PEUCH%20downscaling%20.pdf), *search summary*).
- **How they're trying to solve it:** AI downscaling challenge (PM2.5 from CAMS, NO2 from S5P; 500 × 500 km areas in Northern Italy, California, South Africa); National Collaboration Programme downscaling; Sentinel-4 hourly data.
- **Data:** ADS (free, CC-BY-like Copernicus licence), EEA AQ e-reporting, Sentinel-5P, Sentinel-4.
- **Hackathon angle:** 1 km NO2/PM2.5 nowcast for a city from S5P plus CAMS plus OpenStreetMap traffic proxies plus EEA stations, with a "which school is in the worst air today" output.
- **Credibility:** official.

### 4.3 C3S (Climate Change Service), CMEMS (Marine) and CLMS (Land)
- **What it is:** C3S provides ERA5 reanalysis, seasonal forecasts and climate indicators. CMEMS provides ocean physics and biogeochemistry analyses and forecasts and Ocean Monitoring Indicators (e.g., 3.7 mm/yr global mean sea-level rise 1993–2024, [Copernicus Marine](https://marine.copernicus.eu/news/sentinel-6b-launch-new-era-measuring-sea-level-space)). CLMS provides land cover, the high-resolution layers, vegetation phenology, and the European Ground Motion Service.
- **Problems / pain points:** *(not researched in depth on this pass: see Leads not followed)*. Known issues from public sources here: CLMS data were added to CDSE in 2025 ([CDSE report summary](https://dataspace.copernicus.eu/news/2026-9-24-copernicus-data-space-ecosystem-cdse-releases-annual-report-2025)).
- **Hackathon angle:** Marine heatwave and harmful-algal-bloom early warning for aquaculture using CMEMS SST plus OLCI chlorophyll.
- **Credibility:** official (limited).

---

## 5. Destination Earth (DestinE)

- **What it is:** EC flagship digital twin of the Earth, implemented by ECMWF (digital twins), ESA (platform) and EUMETSAT (Data Lake). Timeline: launched 2022; core platform, Data Lake and first two twins demonstrated by 2024; "further enhancement and integration of additional digital twins" by 2026; "full" digital replica by 2030 ([destination-earth.eu](https://destination-earth.eu/)). Twins: Climate Change Adaptation (multi-decadal) and Weather-induced Extremes (high-resolution, on-demand) ([ECMWF DestinE page](https://www.ecmwf.int/en/about/what-we-do/environmental-services-and-future-vision/destination-earth)). The Climate DT is now "NEW – GEN 2 … Km-scale simulations of climate scenarios". Featured services: FloodMIND, DEFAIR (AI-ready data preparation), UHEATS, and HiReNext ("Coming Soon") ([DestinE Platform](https://platform.destine.eu/)). October 2026 news: "DEFAIR: AI-ready data preparation made easy" (21 Oct), "DestinE Forum" (19 Oct), "Dipping into the DestinE Data Lake" (6 Oct) ([destination-earth.eu](https://destination-earth.eu/)).
- **Problems / pain points:**
  - **Access restriction.** Free registration gives basic services, but "advanced features tied to the DestinE Digital Twins data are reserved for European actors", with an upgrade application ([DestinE Platform](https://platform.destine.eu/)). Non-EU hackers cannot get full twin data.
  - **Data volume** of km-scale simulations, which needs streaming and on-the-fly data reduction *(specific PB/day numbers not verified on this pass)*.
  - **AI-readiness.** The need for DEFAIR shows that raw twin output is not ML-ready.
- **How they're trying to solve it:** Data Lake with edge services near HPC; DEFAIR; the DestinE Forum community.
- **Data:** Platform with free tier; upgraded access for eligible European public, research and some commercial users.
- **Off-the-shelf tech:** earthkit, polytope (ECMWF feature extraction), Anemoi.
- **Hackathon angle:** Limited for a US team because of access restrictions. Open alternatives are ERA5 plus AIFS open data. A "mini digital twin" for one city's heat or flood using open ECMWF forecasts plus Sentinel data is feasible.
- **Credibility:** official.

---

## 6. ESA Φ-lab: AI, onboard processing, challenges, foundation models, LLMs

### 6.1 Φsat-2 (onboard AI cubesat)
- **What it is:** A 6U cubesat launched 16 Aug 2024 (Transporter-11) with an onboard AI processor. Preloaded apps: cloud removal / detection, emergency street-map generation, vessel detection and classification, and deep compression. Two OrbitalAI challenge winners were added after launch: marine pollution / anomaly detection and wildfire detection ([ESA "Φsat-2 gets two new AI apps"](https://www.esa.int/Applications/Observing_the_Earth/Phsat-2/Phsat-2_gets_two_new_AI_apps); [SmallSat 2025 paper](https://digitalcommons.usu.edu/smallsat/2025/E-S1-2025/3)). L1 data free on the Insula platform after registration ([ESA science phase article](https://www.esa.int/Applications/Observing_the_Earth/Phsat-2/Phsat-2_begins_science_phase_for_AI_Earth_images)). March 2026: "Nominal operations with slow orbital decay. End of operations planned March 2026" ([Floberghagen slides](https://climate.esa.int/media/documents/1_FutureEO_post-CM25_-_Floberghagen.pdf)). CEOS WGISS-61 slides: 2,535 registered users by Feb 2026; ESA proposing a one-year extension due to user interest ([CEOS WGISS-61](https://ceos.org/document_management/Working_Groups/WGISS/Meetings/WGISS-61/7.4_Phisat-2_ESA%20V3.pdf), *search summary*).
- **Problems / pain points:** Downlink bottleneck. The InCubed wildfire call says "Wildfire alerts can be delayed by satellite downlinks and ground-processing loops" ([InCubed, 31 Aug 2026](https://incubed.esa.int/eight-new-earth-observation-based-wildfire-applications-co-funded-by-esa-incubed/)). Onboard models must be tiny and robust to domain shift (cubesat radiometry differs from Sentinel-2).
- **How they're trying to solve it:** Onboard AI (Φsat-2, FIREWISE: "software framework to run EO foundation models onboard satellites… faster alerts that include uncertainty information" ([InCubed](https://incubed.esa.int/eight-new-earth-observation-based-wildfire-applications-co-funded-by-esa-incubed/))); the OPS-SAT Kelvins case; the Grand Marathon asks for "edge or on-board processing, or smart tasking" ([Φ-lab Grand Marathon](https://cin.philab.esa.int/databases/news-db/esa-lab-grand-marathon)).
- **Data:** Φsat-2 L1 on Insula; OPS-SAT dataset (Kelvins).
- **Hackathon angle:** "What should a satellite downlink first?" Train a tiny (<1 MB) model on Sentinel-2 (and Φsat-2 L1) that ranks tiles by "urgency" (fire, flood, oil slick, ship in a protected area). Report the bandwidth saved versus latency gained. Clear problem, clear metric.
- **Credibility:** official.

### 6.2 ESA EVE: Earth Virtual Expert (LLM, Oct 2026)
- **What it is:** Φ-lab's EO-domain LLM, introduced 8 Oct 2026. Built with Pi School, Mistral and Imperative Space; trained on ESA, NASA and Copernicus web content, manuscripts and peer-reviewed research (including via Wiley). RAG over recent Wiley articles; an "LLM-as-a-judge" filter. "The model, code, curated training datasets, and benchmarks are public on Hugging Face and GitHub" ([ESA, Oct 2026](https://www.esa.int/Applications/Observing_the_Earth/FutureEO/Introducing_ESA_s_Earth_Virtual_Expert)). The base model is described elsewhere as Mistral Small 3.2 24B fine-tuned ([HF eve-esa](https://huggingface.co/eve-esa); [EVE README](https://eve-esa-readme.static.hf.space)). Planned phase two: "retrieving and analysing Earth observation data, multi-step tasks, satellite imagery search in 2027" ([ESA](https://www.esa.int/Applications/Observing_the_Earth/FutureEO/Introducing_ESA_s_Earth_Virtual_Expert)).
- **Problems / pain points:** "Finding, comparing and understanding this information can be difficult", which "limits its accessibility to policymakers and the wider public" ([ESA](https://www.esa.int/Applications/Observing_the_Earth/FutureEO/Introducing_ESA_s_Earth_Virtual_Expert)). This matches the sponsor brief exactly ("a literature no human can read all of").
- **How they're trying to solve it:** EVE, the openEO Agent (CDSE), and JAXA Earth API MCP modules (see §12.3).
- **Data:** EVE weights and datasets on HF (eve-esa). Licence claims "Apache 2.0 / CC-BY" per the project README ([EVE README](https://eve-esa-readme.static.hf.space), *search summary*).
- **Hackathon angle:** **Ship EVE's 2027 roadmap item now**: "satellite imagery search + EO data retrieval" as an agent that answers a policy question ("Has the Valencia flood plain been rebuilt since 2024?") by retrieving literature (EVE) *and* pulling Sentinel data via CDSE/openEO or JAXA Earth API MCP, with citations. This combines the sponsor's "literature" and "data" themes.
- **Credibility:** official.

### 6.3 Φ-lab Challenges (formerly AI4EO): full portfolio
- **What it is:** Since Aug 2025, "AI4EO is evolving into 'ESA Φ-lab Challenges'", implemented by Novaspace, Planetek Italia, Sinergise, GMATICS and EarthPulse ([Φ-lab blog, 12 Aug 2025](https://philab.esa.int/a-bold-new-chapter-for-ai4eo-with-esa-%cf%86-lab-challenges/)). Portfolio at [challenges.philab.esa.int](https://challenges.philab.esa.int/): AI for Earthquake Response; PANGAEA; Sentinel-2 (agriculture); Food Security (time series); HYPERVIEW; AutoICE (Sentinel-1 sea-ice mapping); MapYourCity; HYPERVIEW2 (EASi/ECAI 2025); ClearSAR Track 1 (Sentinel-1 RFI); "Reaching new heights with GeoFM"; Air Quality & Health; OrbitalAI. See the full table in §20.
- **Key problem statements (verbatim or near-verbatim):**
  - *AI for Earthquake Response:* "Mapping earthquake damage still depends heavily on human interpretation… The challenge asks for AI models that automatically classify buildings as damaged or undamaged using pre- and post-event imagery". Data: "multi-mission, high-resolution satellite imagery from previous International Charter activations, accessed through Charter Mapper and … EOTDL" ([Φ-lab blog](https://philab.esa.int/a-bold-new-chapter-for-ai4eo-with-esa-%cf%86-lab-challenges/)).
  - *HYPERVIEW2:* explainable AI to estimate soil B, Cu, Zn, Fe, S and Mn from airborne hyperspectral, Sentinel-2 and PRISMA ([same](https://philab.esa.int/a-bold-new-chapter-for-ai4eo-with-esa-%cf%86-lab-challenges/)).
  - *PANGAEA:* standardized benchmarking of geospatial foundation models, with recurring Data Sprints.
  - *ClearSAR:* "automated RFI detection methods that scale and fit into the Sentinel-1 processing chain". Track 1 has 3,940 quicklook RGB images (3,154 training with bounding boxes, 786 test), scored by mAP; results at IEEE ICIP 2026 (13–17 Sep 2026) ([platform page](https://platform-challenges.philab.esa.int/clear-sar); [data](https://platform-challenges.philab.esa.int/clear-sar/data)). An unofficial LinkedIn post claims a team from Egypt's Applied Innovation Center won (social post, unverified).
  - *Reaching new heights with GeoFM (with ITU / AI for Good, KTH, GEO):* building and vegetation height plus 3D semantic segmentation from pre-computed embeddings (AlphaEarth, TESSERA, TerraMind, THOR). Train on a few regions, generalise globally. Closed 30 Jun 2026; prizes >€9k ([platform page](https://platform-challenges.philab.esa.int/geoai); [ADB challenge mirror](https://challenges.adb.org/en/challenges/reaching-new-heights-with-geofm); [ITU slides](https://www.itu.int/en/ITU-T/academia/kaleidoscope/2026/Documents/Presentations/MANARA-presentation.pdf)). Motivation includes better ITU radio-propagation models.
  - *Air Quality & Health (with ECMWF/CAMS):* AI downscaling of PM2.5 (from CAMS) and NO2 (from S5P) ([platform page](https://platform-challenges.philab.esa.int/air-quality-and-health)).
- **Hackathon angle:** These challenges come with *public data and baselines*. The best fits for 36 h are ClearSAR (object detection on RGB quicklooks), Earthquake damage (Charter imagery via EOTDL), GeoFM heights (embeddings make it compute-light), and AQ downscaling.
- **Credibility:** official.

### 6.4 ESA Φ-lab Grand Marathon (civilian protection)
- **What it is:** A milestone-based challenge, "powered by Hello Tomorrow". The 2nd edition, 2025–26, theme: "next-generation Earth Observation concepts that enhance crisis monitoring and protect civilian populations, especially in conflict and disaster contexts". It asks for AI-enabled EO to "detect short-lived hazards, deliver near-real-time insights, and support humanitarian and civil protection actions". Expected tech: "AI/ML, novel sensors, edge or on-board processing, or smart tasking". Emphasis on "benefit for children and adolescents". Deadline 11 Jan 2026; prizes up to €215K / €65K / €15K; finalists at the Hello Tomorrow Summit, Amsterdam, 11–12 Jun 2026 ([Φ-lab CIN page](https://cin.philab.esa.int/databases/news-db/esa-lab-grand-marathon); [Φ-lab collaborations portal](https://philab.esa.int/%CF%86-lab-collaborations-portal/)). Winners not found.
- **Hackathon angle:** A conflict-zone civilian-harm early warning tool from open data is ethically sensitive. A safer framing is "short-lived hazards to children": flash floods near schools, heat on school routes, or smoke over schools, using open Sentinel and AIFS forecasts.
- **Credibility:** official.

### 6.5 TerraMind, Major TOM, embeddings (brief: covered by the "models and tools" slice)
- **What it is:** TerraMind is an IBM + ESA Φ-lab "any-to-any generative" multimodal EO foundation model, trained on TerraMesh (>9 M samples, 8 aligned modalities, 500B tokens). Open on HF ([HF TerraMind-1.0-base](https://huggingface.co/ibm-esa-geospatial/TerraMind-1.0-base); [DLR news 2025](https://www.dlr.de/en/eoc/latest/news/2025/new-ai-model-for-a-better-understanding-of-our-planet)). It was later fine-tuned on ImpactMesh for floods and wildfire ([IBM Research blog](https://research.ibm.com/blog/geospatial-flood-and-wildfire-mapping)). Major TOM is a Φ-lab standard for EO dataset curation. Core-S2L2A has 2,245,886 patches, about 23 TB ([Major TOM README](https://major-tom-readme.static.hf.space/README.md)). Global embeddings: "51 TB of AI embeddings… more than 40 billion embedding vectors… processing of 147 TB of raw satellite data", released with CloudFerro on CREODIAS ([CloudFerro](https://cloudferro.com/news/creodias-platform-updated-with-advanced-global-ai-embeddings/)).
- **Hackathon angle:** Embeddings make global "find places like this" search feasible in 36 h without GPUs.
- **Credibility:** official / vendor.

---

## 7. ESA Advanced Concepts Team: Kelvins competitions

### 7.1 Kelvins platform (kelvins.esa.int): complete list as of 24 Oct 2026
- **What it is:** ESA ACT's competition platform for "space-flavoured" ML and optimisation problems with public datasets and leaderboards ([kelvins.esa.int](https://kelvins.esa.int/)). Most are off-topic for EO, but several are directly useful for the space traffic, debris and onboard-autonomy slices.
- **Full list** (taglines from the homepage, [kelvins.esa.int](https://kelvins.esa.int/)):
  1. **Lunar X-view** (active, 1 Nov 2026 – 31 Mar 2027): "Alone on the Moon. One panorama. One map." Match a rover's ground-level panorama to an orbital map to self-localise without Earth signal. Run with Institute of Science Tokyo, Adelaide University and Politecnico di Milano ([Lunar X-view](https://kelvins.esa.int/lunar-x-view/)).
  2. **ELOPE** (Event-based Lunar OPtical flow Egomotion estimation): estimate camera motion from event-based optical flow. Ended 31 Aug 2025.
  3. **The OPS-SAT case**: edge-AI image classification on the OPS-SAT cubesat's raw imagery. Ended 31 Oct 2022.
  4. **Pose Estimation 2021 (SPEC2021)**: bridge the synthetic-to-real domain gap with SPEED+. Ended 31 Mar 2022.
  5. **Planetary defence challenge**: deflect an asteroid. Ended 5 Sep 2021.
  6. **Space debris: the origin**: identify the parent event of debris pieces. Ended 5 Sep 2021.
  7. **spotGEO**: detect faint GEO satellites in ground telescope image sequences. Ended 1 Sep 2020.
  8. **Collision Avoidance Challenge**: predict final collision risk from CDM time series (decide to manoeuvre). Ended 16 Dec 2019.
  9. **Pose Estimation Challenge (SPEC2019)**: satellite pose from one image. Ended 1 Jul 2019.
  10. **PROBA-V Super Resolution**: multi-frame super-resolution of PROBA-V. Ended 1 Jun 2019.
  11. **The Kessler Run (GTOC9)**: debris-removal trajectory optimisation. Ended 2 May 2017.
  12. **Star Trackers: First contact**. Ended 1 Sep 2017.
  13. **Mars Express Power Challenge**: predict thermal power consumption to extend the mission. Ended 1 Aug 2016.
- **Problems / pain points:** Each competition is a *real operational problem* from ESA (e.g., CDM-based collision decisions, GEO object detection). Datasets stay public.
- **Hackathon angle:** The Collision Avoidance dataset (CDMs) and spotGEO remain excellent 36-hour starters for the debris slice. For EO, PROBA-V super-resolution is a classic.
- **Credibility:** official.

---

## 8. ESA OSIP (Open Space Innovation Platform), InCubed and CCI

### 8.1 OSIP
- **What it is:** ESA's idea-intake portal (ideas.esa.int). "Campaigns" ask specific questions on a short timeline; a continuously open "Channel" takes anything else ([ESA OSIP page](https://www.esa.int/Enabling_Support/Preparing_for_the_Future/Discovery_and_Preparation/The_Open_Space_Innovation_Platform_OSIP)). The portal needs a login, so campaign lists could not be read on this pass ([ideas.esa.int](https://ideas.esa.int/)).
- **Campaigns found in 2025–2026 (via search summaries, *unverified on the primary page*):**
  - "Quantum technologies for exploration" (HRE Directorate; submissions due 12 Apr 2026; first phase unfunded).
  - IBPER radiation (biological and physical effects of radiation; full proposal deadline 23 Mar 2025).
  - Life/Physical Sciences Working Group calls (28 Feb 2025) ([BSGN listing](https://bsgn.esa.int/?p=102792); [ESA OSIP page](https://www.esa.int/Enabling_Support/Preparing_for_the_Future/Discovery_and_Preparation/The_Open_Space_Innovation_Platform_OSIP)).
  - Φ-lab's "Call for Φdeas" (ideas.esa.int) is the EO-specific open call ([Φ-lab collaborations portal](https://philab.esa.int/%CF%86-lab-collaborations-portal/)).
- **Hackathon angle:** OSIP campaigns are literally phrased as problems. Re-check the portal (login) for EO campaigns before final pitch framing.
- **Credibility:** official (portal), with unverified campaign details.

### 8.2 InCubed (Investing in Industrial Innovation): commercial EO co-funding
- **What it is:** Φ-lab-run zero-equity co-funding for commercial EO products: "Your equity and Intellectual Property Rights, 100%, stay with you" ([incubed.esa.int](https://incubed.esa.int/)). InCubed-3 was part of the CM25 FutureEO package ([Floberghagen slides](https://climate.esa.int/media/documents/1_FutureEO_post-CM25_-_Floberghagen.pdf)). There is a new ESA–UKSA UK InCubed call (17 Jul 2026) ([InCubed](https://incubed.esa.int/esa-and-uksa-launch-a-new-incubed-call-for-the-united-kingdom/)). Current activities include BrightSkies methane emissions, MPSSERV (mission planning as a service), SolarEye, ac-URBAN (actinia-copilot), and constellr thermal data ([incubed.esa.int](https://incubed.esa.int/)).
- **Wildfire call (InCubed + Spanish Space Agency AEE, €3 M, eight projects kicked off July 2026):** FIREAI-OPS (fire-spread anticipation, AI plus physics), FIREWISE (onboard EO foundation models with uncertainty), EO4PYRO (risk / post-fire digital twin), FirEOcast (fuel-aware danger forecasts), DVSTAI thermal extension, PiroSAR/F2DEM (multi-SAR fire-front tracking day and night), Horizon Wildfire Insights (Airbus), and FireTwin ([InCubed, 31 Aug 2026](https://incubed.esa.int/eight-new-earth-observation-based-wildfire-applications-co-funded-by-esa-incubed/)).
- **Problems stated (verbatim):** "Wildfire alerts can be delayed by satellite downlinks and ground-processing loops." Smoke, cloud and darkness block optical, thermal and airborne systems. Teams get "fragmented, static, or outdated information". "Conventional fire-danger indices rely mostly on weather variables and underrepresent atmospheric instability, fuel properties, and fuel moisture" ([InCubed](https://incubed.esa.int/eight-new-earth-observation-based-wildfire-applications-co-funded-by-esa-incubed/)).
- **Hackathon angle:** "Fuel-aware fire danger": augment the weather-only Canadian FWI with Sentinel-2-derived live fuel moisture and Sentinel-1 backscatter for a Spanish region, validated on EFFIS 2025 burnt areas. This addresses a stated gap and uses open data.
- **Credibility:** official.

### 8.3 ESA Climate Change Initiative (CCI) and Climate Space
- **What it is:** ESA's programme producing satellite climate data records for Essential Climate Variables (ECVs). Recent releases: "Six new and updated satellite datasets" (28 Jul 2026), "seven new and updated datasets on sea state and ocean wave height" (17 Sep 2026), a water-vapour record update (1 Sep 2026), "A new tool to accelerate climate model assessment" (15 Sep 2026), and "2025 breaks climate records, says BAMS report" (12 Aug 2026) ([climate.esa.int](https://climate.esa.int/en/)). CCI moves into the new FutureEO "Earth Action" pillar after CM25 ([Floberghagen slides, presented at the CCI colocation & CMUG meeting, 24 Mar 2026](https://climate.esa.int/media/documents/1_FutureEO_post-CM25_-_Floberghagen.pdf)).
- **Problems / pain points:** Long records depend on ageing missions and inter-satellite calibration (cf. TRUTHS, the Sentinel-6C gap). The uptake by climate modellers is slow, hence the "new tool to accelerate climate model assessment".
- **Data:** CCI Open Data Portal (free, mostly CC-BY), the CCI Toolbox (xcube).
- **Hackathon angle:** "Climate record health check": for each CCI ECV, display record length, the satellites it relies on, their design life versus actual age, and the gap risk.
- **Credibility:** official.

---

## 9. ESA CM25, European Resilience from Space (ERS) and EU-level policy

### 9.1 ESA Ministerial Council CM25 (Bremen, 26–27 Nov 2025)
- **What it is:** ESA's three-yearly funding conference.
- **Totals:** €22.1 bn over 3 years (proposal €22.25 bn), up from €16.9 bn ([European Spaceflight, 27 Nov 2025](https://europeanspaceflight.com/?p=5630)). ESA's own slide says "A record 22.3 B€ budget" ([Floberghagen](https://climate.esa.int/media/documents/1_FutureEO_post-CM25_-_Floberghagen.pdf)). Final subscription tables: [ESA/C-M(2025)100 Rev.5](https://www.rymdstyrelsen.se/contentassets/6de457f7799045f2bfce0332c8f003c4/esa_c-m_2025_100rev.5_en.pdf); [BELSPO debrief](https://www.belspo.be/belspo/space/doc/Presentations/20251205_CM-ESA-Bremen-2025_BELSPO-Debriefing-presentation.pdf).
- **Winners and losers:**
  - Human and Robotic Exploration got just over €2.9 bn against €3.7 bn projected, a shortfall above 20% ([European Spaceflight](https://europeanspaceflight.com/?p=5630)).
  - Space Transportation rose to over €4.4 bn, including about €900 M for the European Launcher Challenge.
  - The UK fell from €1.878 bn to €1.706 bn (share 11.2% → 7.7%, now 5th behind Spain).
  - Germany rose to just over €5 bn (23.11%).
- **EO:** EOP €3.4 bn (15% of the total); 26 countries contributing; "Provision of mandate given for engaging in defence and security"; "EO Enters Defence While Preserving its DNA" ([Floberghagen](https://climate.esa.int/media/documents/1_FutureEO_post-CM25_-_Floberghagen.pdf)).
- **Industry context:** The EARSC Industry Survey 2025 found the European EO services sector grew 9.16% to €2.66 bn revenue and >16,000 employees, "strongly driven by defence and security", with growth "concentrated primarily among large and medium companies" ([EARSC, 13 Jan 2026](https://earsc.org/2026/01/13/eocafe-esa-cm25-outcomes-and-opportunities-whats-next-for-the-eo-industry/)).
- **Credibility:** official and reputable trade press.

### 9.2 European Resilience from Space (ERS) and the EU EO Governmental Service (EOGS)
- **What it is:** A new ESA optional programme (resolution adopted 12 Jun 2025, per the [Canada–ESA treaty text](https://www.treaty-accord.gc.ca/Treaty_Docs/PDF/105834.pdf)), "massively subscribed" at CM25. ERS-EO goals: "Enhanced situational awareness of EU & Member States: Early detection of crisis, Intelligence, Surveillance, Reconnaissance, Geospatial support". It needs "VHR optical & radar, possibly advanced sensors", "Fast revisit capability: large EO constellations" and "Guaranteed, secure and fast access to data: Global, Reactive, Reliable", "Meeting both civil & military needs". Structure:
  - Element 1: "Prepare & accelerate the EU's EO Governmental Services (EOGS)"
  - Element 2: "Federated system of national and multi-lateral resources", i.e. a "Federation of National Observation Capabilities" with Cluster 1 "Alpstar", Cluster 2 "ECSA+", and "Space Resilience Nodes"
  ([Floberghagen slides](https://climate.esa.int/media/documents/1_FutureEO_post-CM25_-_Floberghagen.pdf)). The EC proposes EOGS under the 2028–2034 MFF ([Friends of Europe event page](https://www.friendsofeurope.org/events/strengthening-europes-space-capabilities-for-resilience-boosting-synergies-in-view-of-future-earth-observation-capabilities/)).
- **Problems / pain points:** Europe lacks sovereign, guaranteed, fast-revisit VHR access for crises and security. Today it is fragmented across national systems (CSO, SAR-Lupe/SARah, COSMO-SkyMed, IRIDE, Pléiades Neo) and US commercial providers.
- **How they're trying to solve it:** Federate national assets (the "Space Resilience Nodes"); procure commercial constellations.
- **Hackathon angle:** A "federated tasking broker" mock-up. Given a crisis polygon and deadline, query the *public* catalogues of several open and commercial sources (CDSE Sentinel, IRIDE when public, Planet/Umbra/Capella open data programmes, NISAR, ALOS-4 via JAXA) and return "the first usable image will be at T+X h from source Y". This is the ERS-EO "guaranteed fast access" problem in miniature.
- **Credibility:** official.

### 9.3 EU Space Act (proposal, 25 Jun 2025)
- **What it is:** A proposed EU regulation, [COM(2025)335](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=celex:52025PC0335), with three pillars ([EC DEFIS EU Space Act page](https://defence-industry-space.ec.europa.eu/eu-space-act_en)):
  - **Safety:** "robust rules for tracking space objects and mitigating space debris".
  - **Resilience:** "Tailored cybersecurity requirements".
  - **Sustainability:** operators assess and reduce environmental impact.
  It applies to "EU and non-EU operators providing space services in Europe", scaled by size and risk. It replaces "13 different national approaches". Public consultation ran 15 Jul – 7 Nov 2025. The proposal is in the ordinary legislative procedure.
- **Problems / pain points:** Fragmentation across national laws; debris; cyber threats. Compliance burden for start-ups. For non-EU constellations it applies extraterritorially *(industry and US reaction not verified on this pass)*.
- **Hackathon angle:** A "Space Act compliance checker" for a satellite operator that estimates collision-avoidance obligations from public TLEs/CDMs and an environmental-footprint estimate. This sits mostly in the space-traffic slice.
- **Credibility:** official.

### 9.4 IRIS² (EU secure connectivity constellation)
- **What it is:** "the EU's satellite network" of "348 satellites" in LEO and MEO for secure governmental and commercial connectivity, under Regulation (EU) 2023/588 ([EC DEFIS IRIS² page](https://defence-industry-space.ec.europa.eu/eu-space/iris2-secure-connectivity_en)). A 2026 EC item is titled "The European Union is accelerating and reinforcing IRIS²" (press release ip_26_1726, *text not read*). ESA co-develops IRIS² ([ESA Connectivity](https://connectivity.esa.int/?p=25271)).
- **Effects on Europe / EO relevance:** IRIS² is a sovereignty answer to Starlink/Starshield. For EO, it could provide secure low-latency relay for ERS crisis imagery *(inference)*.
- **Hackathon angle:** Low for EO data. Cross-slice: SpaceX / orbital compute.
- **Credibility:** official.

### 9.5 EU budget 2028–2034 (MFF) and the space envelope
- **What it is:** The Commission proposed the next MFF on 16 Jul 2025, almost €1.8 trillion in commitments ([EPRS briefing](https://www.europarl.europa.eu/thinktank/en/document/EPRS_BRI(2025)775885)). Space and defence are channelled through a European Competitiveness Fund: €131 bn for defence and space, "five times the previous framework" ([To Vima, search summary](https://www.tovima.com/world/eu-unveils-ambitious-and-forward-looking-2028-2034-budget-framework/amp/)). Eurospace (2 Jul 2025) asks for a ring-fenced €40–60 bn EU Space Programme versus "the current 19B€", protecting Galileo, Copernicus, IRIS² and SSA. It also asks for Copernicus continuity and evolution "in a security and defence framework" ([Eurospace](https://eurospace.org/?p=7551)). Member states aim for agreement by end-2026 ([fasi.eu, search summary](https://fasi.eu/en/articles/news/30506-eu-mff-2028-2034.html)).
- **Problems / pain points:** Copernicus operations funding (e.g., the Sentinel-2A extension "pending funding availability") competes with defence inside a merged fund.
- **Credibility:** official and industry position.

### 9.6 European sovereignty and data-dependence concerns (US budget, US instruments)
- **Concrete evidence found on this pass:**
  1. **Sentinel-6C** contract not approved "due to the uncertainties on the EUMETSAT contribution and on the availability of the NASA radiometer" ([ESA slides, Mar 2026](https://climate.esa.int/media/documents/1_FutureEO_post-CM25_-_Floberghagen.pdf)).
  2. **Biomass** cannot image where the US Space Object Tracking Radar operates: a "global acquisition mask, limiting data access and spatial coverage" ([EO College, search summary](https://eo-college.org/?p=388510)).
  3. ESA CM25 messaging stresses "Fundamental importance of European autonomy" ([slides](https://climate.esa.int/media/documents/1_FutureEO_post-CM25_-_Floberghagen.pdf)).
  4. Canada frames RCM replenishment as "sovereign satellite capacity" in "an increasingly dangerous and divided world" ([Canada.ca, 30 Jun 2026](https://www.canada.ca/en/space-agency/news/2026/06/minister-joly-announces-688m-to-strengthen-canadas-sovereign-satellite-capacity-with-radarsat-constellation-mission-replenishment-satellite.html)).
- **Not verified on this pass:** specific European statements reacting to proposed FY2026 NASA Earth science cuts or Landsat Next restructuring (see Leads not followed; mostly the US-agencies slice).
- **Hackathon angle:** "If US data went dark": for a chosen application (e.g., crop monitoring in Europe or Africa), quantify how much accuracy or revisit is lost if only European, Japanese and Indian open data are available (Sentinel-1/2/3, ALOS-4 ScanSAR, GCOM-C, Resourcesat AWiFS) versus with Landsat, MODIS and VIIRS. This is a clear, quantifiable sovereignty problem.
- **Credibility:** official, plus unverified items.

---

## 10. EUMETSAT and ECMWF

### 10.1 MTG (Meteosat Third Generation) and MetOp-SG
- **What it is:** MTG-I1 (imager: FCI plus Lightning Imager) is operational. MTG-S1 (IRS hyperspectral sounder plus Sentinel-4 UVN) launched 4 Jul 2025 ([DLR](https://www.dlr.de/en/eoc/latest/news/2025/copernicus-sentinel-4-delivers-first-images-of-air-quality-over-europe)), with first IRS images released 27 Jan 2026 showing Storm Claudia ([Floberghagen slides](https://climate.esa.int/media/documents/1_FutureEO_post-CM25_-_Floberghagen.pdf)). The MTG-I2 Flight Acceptance Review kicked off 13 Jan 2026, with launch planned Q3 2026 per the March slides *(launch not confirmed by Oct 2026 on this pass)*. MetOp-SG-A1 (with Sentinel-5) launched 13 Aug 2025 ([ESA](https://www.esa.int/Newsroom/Press_Releases/First_MetOp-SG_satellite_and_Sentinel-5A_launched)). MetOp-SG-B1 (scatterometer, MWI, ICI, RO, Argos-4) arrived at Kourou 20 Oct 2026 for an Ariane 6 launch "at the end of 2026" ([ESA, 20 Oct 2026](https://www.esa.int/Applications/Observing_the_Earth/Meteorological_missions/MetOp_Second_Generation/MetOp-SG-B1_weather_satellite_arrives_at_Europe_s_Spaceport)). AWS (Arctic Weather Satellite) runs under ESA funding until Aug 2026, after which EUMETSAT "confirmed intention to fund" (EPS-Sterna) ([slides](https://climate.esa.int/media/documents/1_FutureEO_post-CM25_-_Floberghagen.pdf)).
- **Problems / pain points:** MTG-S1 IRS produces hyperspectral sounding every 30 min over Europe, a huge data stream that NWP centres must thin or compress *(volume not verified; EUMETSAT pages returned HTTP 403 on this pass)*. Lightning Imager data are new to forecasters (nowcasting use is immature). EUMETSAT's share of Sentinel-6C is uncertain.
- **Data:** EUMETSAT Data Store and EUMETCast; free for most users under the EUMETSAT data policy.
- **Hackathon angle:** "Lightning-to-flash-flood nowcast": MTG LI flash density plus FCI cloud tops plus AIFS precipitation to issue 0–2 h flash-flood alerts for an event like EMSR935 (Valencia, Oct 2026).
- **Credibility:** official.

### 10.2 ECMWF AIFS (AI forecasting system) and open data
- **What it is:** AIFS Single became operational in Feb 2025 and AIFS ENS (51 members, 31 km) on 1 Jul 2025. Claims: "gains of up to 20%" on many measures including surface temperature; "more than 10 times faster"; "approximately 1,000 times" less energy. Limitations: 31 km resolution versus 9 km IFS ENS, and "Initial conditions still depend on physics-based data assimilation" ([ECMWF news, 1 Jul 2025](https://www.ecmwf.int/en/about/media-centre/news/2025/ecmwfs-ensemble-ai-forecasts-become-operational)). The Anemoi training framework is open source.
- **Open data:** IFS and AIFS real-time subsets are free under **CC-BY-4.0**, "may be redistributed and used commercially", four runs a day, on AWS, Azure and GCP, via the `ecmwf-opendata` client. **From 20 Oct 2026 IFS open data are also at 0.1°**; AIFS remains 0.25°. Rolling archive of the last 12 runs ([ECMWF open data](https://www.ecmwf.int/en/forecasts/datasets/open-data)).
- **Data volumes:** ECMWF's Data Handling System holds 510 PB primary plus 188 PB secondary, grows about 287 TB on a typical day, and serves about 215 TB/day of retrievals ([ECMWF DHS](https://www.ecmwf.int/en/computing/our-facilities/data-handling-system)).
- **Problems / pain points:** Resolution gap for local extremes; dependence on physics-based data assimilation (AI-DA is the next frontier); data volume.
- **Hackathon angle:** (a) "AIFS downscaler": learn 31 km → 1–3 km precipitation or wind for a mountainous region using ERA5-Land or CERRA plus Sentinel-derived terrain. (b) Turn AIFS ENS probabilities into impact-based warnings for a specific user (farm, solar park, festival).
- **Credibility:** official.

---

## 11. National European agencies

### 11.1 DLR (Germany): EnMAP, TerraSAR-X / TanDEM-X ageing
- **TerraSAR-X:** launched 15 Jun 2007 with a mission life "planned for 5 years", and still "active (as of 2026)", i.e. about 19 years in orbit. TanDEM-X has flown in formation since 2010 (the WorldDEM / TanDEM-X DEM). Science data via DLR proposals; operations co-funded by Airbus under a continuation agreement since 2016 ([DLR TerraSAR-X page, updated 14 Oct 2026](https://www.dlr.de/en/research-and-transfer/projects-and-missions/terrasar-x)). No successor named on that page *(TSX-NG / HRWS status unverified)*.
- **EnMAP:** German hyperspectral mission (launched 2022). As of Oct 2026, L1B, L1C and L2A ARD products are available through EOC-Geoservice (16 Oct 2026). "Winter Mode" runs Nov 2026 – Feb 2027: Europe only south of the Alps, with focus on the Southern Hemisphere ([enmap.org](https://www.enmap.org/)).
- **Problems / pain points:** The German X-band SAR heritage is 13–19 years past design life, with no announced like-for-like successor here. EnMAP coverage is tasked rather than global (seasonal modes).
- **Hackathon angle:** EnMAP ARD as a CHIME precursor for mineral, critical raw material or mine-waste mapping (EnMAP's Oct 2026 image of the month was mines near Lubumbashi, DRC). This ties to EU Critical Raw Materials Act supply-chain due diligence.
- **Credibility:** official.

### 11.2 CNES (France): SWOT, TRISHNA
- **SWOT** (CNES–NASA, launched 16 Dec 2022): KaRIn gives water surface height of rivers >100 m wide, lakes and flood zones, and river slope; V2 products public since Oct 2024 ([CNES SWOT](https://cnes.fr/en/projects/swot)). June 2026 CNES item: "How satellites are helping predict El Niño".
- **TRISHNA** (CNES–ISRO): visible plus thermal IR at about 60 m, revisiting "every 3 days" at the equator, "several times a week" goal, launch target 2027. The problem it addresses, verbatim: field-level temperature data are "currently available only monthly, or at about 1 km resolution at higher frequency from geostationary satellites". Purpose: plant water stress, evapotranspiration, efficient irrigation ([CNES TRISHNA](https://cnes.fr/en/projects/trishna)).
- **Hackathon angle:** "Irrigation water-stress map" fusing Landsat thermal (100 m, 8–16 d), ECOSTRESS and Sentinel-3 SLSTR (1 km daily), as a TRISHNA/LSTM pre-cursor for one irrigated basin (e.g., Ebro or Po).
- **Credibility:** official.

### 11.3 ASI (Italy): IRIDE, COSMO-SkyMed
- **IRIDE:** an Italian national EO system developed by ESA for ASI and funded by the PNRR (National Recovery and Resilience Plan). As of 2 Oct 2026 it has 39 satellites in orbit:
  - Eaglet II: 24 satellites (OHB Italia), multispectral plus AIS, complete after the 1 Oct 2026 launch.
  - HEO "Hawk for Earth Observation": 14 satellites (Argotec), launched Jun 2025 and May 2026.
  - Pathfinder Hawk: 1 satellite, Jan 2025.
  "Further launches are planned in the coming months". Services: ground motion, land cover, hydrogeology, fires, coastal protection, air quality, weather and critical infrastructure ([ESA, 2 Oct 2026](https://www.esa.int/Applications/Observing_the_Earth/IRIDE/Italy_s_IRIDE_completes_Eaglet_II_constellation)). ESA's 2026 slides list "IRIDE 32 Satellites" among planned 2026 national launches ([slides](https://climate.esa.int/media/documents/1_FutureEO_post-CM25_-_Floberghagen.pdf)).
- **Problems / pain points:** The data policy is not public on the ESA page (who outside the Italian public administration can access it?). The PNRR money comes with a hard deadline (the PNRR ends in 2026) *(inference)*.
- **COSMO-SkyMed:** not researched on this pass.
- **Hackathon angle:** Limited until IRIDE data are open. Watch for an open-data portal.
- **Credibility:** official.

### 11.4 UK Space Agency (UKSA)
- **Status:** The gov.uk organisation page lists UKSA's contact under DSIT. The page did not confirm a merger date *(reported plans to fold UKSA into DSIT are unverified on this pass)* ([gov.uk UKSA](https://www.gov.uk/government/organisations/uk-space-agency)). UK CM25 contribution fell €172 M ([European Spaceflight](https://europeanspaceflight.com/?p=5630)). The UK re-joined Copernicus in 2024 ([Wikipedia](https://en.wikipedia.org/wiki/Copernicus_Programme)). There is a UK InCubed call with ESA (Jul 2026) ([InCubed](https://incubed.esa.int/esa-and-uksa-launch-a-new-incubed-call-for-the-united-kingdom/)).
- **Credibility:** official (partial).

---

## 12. Japan: JAXA, MOE/NIES, JMA

### 12.1 GOSAT-GW (IBUKI-GW): greenhouse gases plus water cycle, launched 29 Jun 2025
- **What it is:** Launched 29 Jun 2025 on the 50th and final H-IIA. Nominal operations from 9 Oct 2025 ([NIES one-year page](https://gosat-gw.nies.go.jp/1st_anniversary/index-e.html)). It carries two instruments ([JAXA Satnavi GOSAT-GW](https://www.satnavi.jaxa.jp/files/project/gosat-gw/en/)):
  - **TANSO-3:** CO2, CH4 and *new* NO2. Wide mode: 911 km swath at 10 km. Focus mode: 90 km swath at 3 km, about 90 locations every 3 days.
  - **AMSR3:** SST, ocean wind, soil moisture, snow depth, sea ice, snowfall and upper-tropospheric water vapour. 10 GHz at 30 km (AMSR2 was 50 km), plus new 166/183 GHz channels at 5 km.
  - Orbit 666 km, 3-day repeat, design life 7+ years.
  Initial TANSO-3 analysis (8 Jan 2026) mapped CO2, CH4 and NO2 distributions over a metropolitan area in one field of view ([MOE press release, 8 Jan 2026](https://www.env.go.jp/en/press/press_02489.html)). A search summary says the area was in the United States. A NASA–Japan Tokyo field campaign ran in March 2026; Railroad Valley vicarious calibration ran Oct 2025 and Jun 2026 ([NIES](https://gosat-gw.nies.go.jp/1st_anniversary/index-e.html)).
- **Problems / pain points:** Data latency to users. L1B was planned for spring 2026 (NIES listed V101.101 from 23 Jul 2026 per a search summary). **L2 XCO2/XCH4/NO2 is planned for spring 2027**, "sufficient quality after calibration and validation" ([MOE](https://www.env.go.jp/en/press/press_02489.html); [NIES news, search summary](https://www.nies.go.jp/soc/en/news/)). AMSR3 data are "not yet" in the JAXA portals ([JAXA](https://www.satnavi.jaxa.jp/files/project/gosat-gw/en/)).
- **How they're trying to solve it:** Staged release via the TANSO-3 Data Distribution Website (product.gosat-gw.nies.go.jp), opened Oct 2025.
- **Data:** TANSO-3 L1B (registration), GOSAT/GOSAT-2 archives (NIES), GOSAT monthly GHG maps (EORC).
- **Hackathon angle:** "City CO2 + NO2 co-emission ratio". NO2 is a short-lived tracer that locates CO2 plumes. Prototype the GOSAT-GW/CO2M "NO2-guided CO2 plume" method with TROPOMI NO2 plus OCO-3 SAM data now, then swap in TANSO-3 L1B/L2 later.
- **Credibility:** official.

### 12.2 ALOS-4 (DAICHI-4) and the L-band SAR heritage
- **What it is:** Launched 1 Jul 2024 on H3 F3. PALSAR-3 L-band phased array: spotlight 1×3 m over 35 km; stripmap up to 3 m over a **200 km swath** (ALOS-2 had 50 km); ScanSAR 25 m over 700 km. 14-day repeat, 628 km SSO, Ka-band 1.8/3.6 Gbps plus optical inter-orbit link, SPAISE3 AIS ([JAXA EORC ALOS-4](https://www.eorc.jaxa.jp/ALOS/en/alos-4/a4_about_e.htm); [JAXA Satnavi ALOS-4](https://www.satnavi.jaxa.jp/files/project/alos4/en/)). Goals: crustal deformation and volcano precursors via InSAR, floods and earthquake damage, forests and rice paddies.
- **Problems / pain points:** The distribution policy is not described on the JAXA pages (high-resolution data are typically commercial via a distributor; *licensing not verified on this pass*). JAXA is the main source of L-band data until ROSE-L, alongside NISAR (open) and SAOCOM.
- **Hackathon angle:** L-band (NISAR open plus ALOS-4) versus C-band (Sentinel-1) coherence over forests and crops, as a ROSE-L readiness demo.
- **Credibility:** official.

### 12.3 JAXA Earth API: COG/STAC with MCP for AI agents
- **What it is:** Serverless COG plus STAC catalogue of 100+ JAXA datasets: ALOS/ALOS-2 mosaics (10–30 m), GSMaP precipitation (since Mar 2000), GCOM-C LST (~5 km), SST (~250 m), chlorophyll-a (~250 m), NDVI, and GCOM-W soil moisture and sea ice. Python and JavaScript modules. **The Python module 0.1.5 (14 Jan 2026) added MCP support "for generative AI integration"; the JS module 2.0.0 (18 Feb 2026) also has MCP.** No registration, API key or usage limits. Data under JAXA research terms "may be used commercially" with attribution ("This data was obtained using JAXA Earth API") ([JAXA Earth API](https://data.earth.jaxa.jp/en/)).
- **Problems / pain points:** Provided "AS IS", "publication may stop without notice" ([JAXA Earth API](https://data.earth.jaxa.jp/en/)). GCOM-C and GCOM-W are ageing *(launch years 2017/2012, background knowledge)*.
- **Hackathon angle:** **Zero-friction data for an LLM agent.** A Claude/LLM agent over the JAXA Earth MCP plus CDSE openEO that answers "how unusual is this month's rainfall / SST here?" with plots and citations. It needs no keys, so it is demo-safe for 36 hours.
- **Credibility:** official.

### 12.4 Himawari (JMA)
- **What it is:** Himawari-9 is the operational GEO imager at 140.7°E. The JMA MSC page posted a Himawari-9 AHI sensitivity-trend calibration update on 14 Oct 2026 ([JMA MSC](https://www.data.jma.go.jp/mscweb/en/index.html)). Himawari-10 (with a hyperspectral IR sounder) is planned around 2029 *(not confirmed on the page; unverified)*.
- **Data:** HimawariCloud (for agencies); full-disk data are also on NOAA/AWS open data *(cross-slice, unverified here)*.
- **Hackathon angle:** 10-minute GEO imagery for typhoon or smoke tracking in Asia-Pacific; a pairing with EarthCARE for the Anak Krakatau ash event (Sep 2026).
- **Credibility:** official (partial).

---

## 13. India: ISRO, NRSC, IN-SPACe

### 13.1 NISAR (NASA–ISRO, L- and S-band SAR), launched 30 Jul 2025
- **What it is:** First dual-frequency SAR (L-band 24 cm, S-band 9.4 cm), now in the "Science Phase" ([NASA NISAR page, updated 29 Sep 2026](https://science.nasa.gov/mission/nisar/)). **The first public L-band science release began 20 Jul 2026**, covering acquisitions from 17 Jun 2026 onward. Products (Provisional V1) are GSLC, GUNW, GCOV, GOFF, RSLC, RUNW, RIFG, ROFF, L0B, and L3 SME2 soil moisture. Example uses: South Africa crop-type change and the **June 2026 Venezuela earthquake** displacement near Caracas and La Guaira ([NASA Earthdata, 21 Jul 2026](https://www.earthdata.nasa.gov/news/nisar-l-band-data-released-expanding-record-surface-changes)). First-year backfill continues, with "the complete science record expected to be available by the end of 2026" (same). ISRO releases daily S-band products via **Bhoonidhi** ([NASA page](https://science.nasa.gov/mission/nisar/)). NRSC posted S-band image releases: Vijayawada (19 Jan 2026), Krishna Delta (20 Mar 2026), Kumbakonam (2 Jul 2026), West Antarctica (12 Aug 2026) ([NRSC](https://www.nrsc.gov.in/)).
- **Problems / pain points:** Products are "PROVISIONAL pending more complete validation over larger areas" ([ASF HyP3 NISAR docs, search summary](https://hyp3-docs.asf.alaska.edu/nisar-docs/availability-overview/)). It took about a year from launch to the first science release. The data volume is large *(per-day TB figure not verified on this pass)*.
- **Data:** ASF DAAC (free; Earthdata Search, Vertex, asf_search) and ISRO Bhoonidhi (S-band).
- **Hackathon angle:** "Venezuela 2026 earthquake in L-band": GUNW interferograms plus Sentinel-1 C/D for a building-damage or landslide map. Or NISAR GCOV for crop-type mapping in India's kharif season using L- and S-band.
- **Credibility:** official.

### 13.2 Launch-failure shock: PSLV-C61 (EOS-09/RISAT-1B) and PSLV-C62 (EOS-N1)
- **What it is:** PSLV-C61 failed on 18 May 2025 because of a third-stage problem (chamber pressure drop), losing **EOS-09 / RISAT-1B**, a C-band SAR meant for surveillance and disaster response. The failure report went to the PMO in Aug 2025 but remained unpublished. **PSLV-C62 (12 Jan 2026), carrying EOS-N1, also failed** ([Wikipedia PSLV-C61, community-edited](https://en.wikipedia.org/wiki/PSLV-C61); [Wikipedia PSLV](https://en.wikipedia.org/wiki/Polar_Satellite_Launch_Vehicle)).
- **Problems / pain points:** Two consecutive PSLV losses leave a gap in Indian SAR and EO capacity and dent confidence in India's workhorse launcher.
- **Hackathon angle:** Which Indian disaster-response needs (e.g., monsoon floods) were meant for EOS-09, and can open SAR (Sentinel-1, NISAR) cover them? A gap-coverage analysis.
- **Credibility:** secondary (Wikipedia). Verify with ISRO statements.

### 13.3 IN-SPACe EO-PPP: India's first private national EO constellation
- **What it is:** On 18 Aug 2025 IN-SPACe selected a **Pixxel-led consortium (Pixxel, SatSure/KaleidEO, PierSight, Dhruva Space)** to design, build, own, operate and commercialise **12 satellites** (panchromatic, multispectral, hyperspectral, SAR). Investment above ₹1,200 crore over 4–5 years. Uses: agriculture, defence, disaster response, maritime (PierSight SAR). Quote: "a defining moment for the private space ecosystem in India" (Pawan Goenka, IN-SPACe) ([The Machine Maker, 18 Aug 2025](https://themachinemaker.com/news/private-consortium-selected-to-develop-indias-first-national-earth-observation-satellite-network/); [Infrastructure Today](https://infrastructuretoday.co.in/pixxelspace-led-consortium-to-build-indias-first-indigenous-commercial-eo-satellite-constellation/)).
- **Problems / pain points:** Sovereign capacity ("independent space-based intelligence capacity" — SatSure CEO); commercial viability of a national PPP.
- **Data:** Not yet. Pixxel's existing Firefly hyperspectral data are commercial.
- **Credibility:** reputable trade press.

### 13.4 NRSC portals (Bhuvan, Bhoonidhi, NDEM, NICES, India-WRIS) and the data-openness question
- **What it is:** India's official EO portals: Bhoonidhi (archive and orders), Bhuvan (geoportal, including a near-real-time lightning service and Bhuvan Panchayat 3.0), NDEM (disaster), NICES (climate), India-WRIS (water) ([NRSC](https://www.nrsc.gov.in/)). Recent NRSC products:
  - EOS-06 (Oceansat-3) OCM-3 winter phytoplankton bloom in the Arabian Sea.
  - Cartosat-3 flash-flood damage maps and pre/post-flood imagery for the Aug 2026 Nepal floods.
  - Resourcesat-2 AWiFS image of the Strait of Hormuz (5 Jul 2026).
  - A Bharatiya Antariksh Hackathon 2026 final (6–7 Aug 2026) ([NRSC](https://www.nrsc.gov.in/)).
- **Problems / pain points:** The NRSC page does not state what is free at which resolution. The *2025 geospatial/remote-sensing policy specifics were not verified on this pass* (search budget exhausted; see Leads not followed).
- **Hackathon angle:** A "Nepal Aug 2026 floods" replication using open Sentinel-1/2 plus Resourcesat AWiFS (if accessible) versus NRSC Cartosat-3 maps.
- **Credibility:** official.

### 13.5 TRISHNA (CNES–ISRO), FLEX cal/val cooperation
- TRISHNA is covered in §11.2 (launch target 2027). ESA–ISRO also signed a "collaboration agreement for joint Cal/Val activities and scientific studies for EO missions with a specific focus on FLEX" ([Floberghagen slides](https://climate.esa.int/media/documents/1_FutureEO_post-CM25_-_Floberghagen.pdf)).

---

## 14. Canada: CSA (RCM, WildFireSat)

### 14.1 RADARSAT Constellation Mission (RCM): sovereignty and replenishment
- **What it is:** Three C-band SAR satellites launched 12 Jun 2019 for maritime surveillance, ecosystems and disasters ([CSA RCM page](https://www.asc-csa.gc.ca/eng/satellites/radarsat/default.asp)). Funding:
  - **4 Dec 2025:** $47 M, including $44.7 M to MDA Space for long-lead parts for a replacement satellite and three concept studies (C-CORE, Kepler, MDA; up to $747k each) for a next-generation EO system, to "maintain uninterrupted access to critical satellite data" ([Canada.ca, 4 Dec 2025](https://www.canada.ca/en/space-agency/news/2025/12/government-of-canada-invests-47-million-to-secure-access-to-essential-canadian-earth-observation-data.html)).
  - **30 Jun 2026:** $688 M contract to MDA Space for an **RCM replenishment satellite** (CHORUS-based SAR), with launch in the **early 2030s**. Part of a $1.012 bn 15-year plan (Oct 2023). RCM serves "over 10 federal departments". Quote: "In an increasingly dangerous and divided world, Canada is investing in modern surveillance systems to detect threats earlier" (Minister Joly) ([Canada.ca, 30 Jun 2026](https://www.canada.ca/en/space-agency/news/2026/06/minister-joly-announces-688m-to-strengthen-canadas-sovereign-satellite-capacity-with-radarsat-constellation-mission-replenishment-satellite.html)).
- **Problems / pain points:** RCM ages toward the end of its design life *(7-year design life is background knowledge, not verified on the page)* and the replacement does not arrive until the early 2030s, which is a continuity gap risk. Arctic sea-ice and maritime surveillance needs are rising.
- **Data:** RCM data access is mostly for government; some open products ("Access to RCM data" page not opened). Sentinel-1 is the open alternative.
- **Hackathon angle:** "Arctic shipping and ice watch": Sentinel-1 C/D plus AMSR2 sea-ice plus AIS for the Northwest Passage. Flag vessels in ice-hazard zones. This is the same mission need RCM covers.
- **Credibility:** official.

### 14.2 WildFireSat
- **What it is:** "The first government-owned satellite mission to monitor active wildfires across Canada on a daily basis", targeting **2029**, with a 5-year mission. It measures in the "late-afternoon and early-evening 'peak burn period', which current public satellites don't cover", with near-real-time updates twice a day. Partners: CSA (satellites and operations), Canadian Forest Service (products), CCMEO (ground segment), ECCC (smoke and air-quality forecasts) ([CSA WildFireSat](https://www.asc-csa.gc.ca/eng/satellites/wildfiresat/default.asp)).
- **Problems stated:** No public satellite covers the peak burn period. "Reconnaissance aircraft flights are high-risk". "Hundreds of fires can burn at once, and firefighting resources are limited" ([CSA](https://www.asc-csa.gc.ca/eng/satellites/wildfiresat/default.asp)).
- **Hackathon angle:** "Peak-burn gap filler": combine GOES-18/19 ABI (10-min GEO fire detections) and VIIRS afternoon passes with Sentinel-3 SLSTR night FRP to estimate fire-intensity curves through the afternoon. Then prioritise which of "hundreds of fires" need aircraft. This is a clear problem with clear open data (the GOES part is cross-slice).
- **Credibility:** official.

---

## 15. Brazil: INPE (PRODES, DETER, CBERS, SIM-Biomas)

### 15.1 PRODES/DETER deforestation monitoring: record lows, Cerrado now the hotspot
- **What it is:** PRODES gives annual native-vegetation suppression (1 Aug – 31 Jul); DETER gives near-daily alerts. Both are published on TerraBrasilis under **CC BY-SA 4.0** with WMS/WFS/WCS ([TerraBrasilis](http://terrabrasilis.dpi.inpe.br/en/home-page/)). Latest figures:
  - **Amazon PRODES 2026 estimate (Aug 2025 – Jul 2026): 3,335 km², −41.8%**, the lowest since 1988. The prior cycle was 5,731 km².
  - **Cerrado: 5,516.69 km², −23.8%**, with the MATOPIBA states at 74.3% of the total.
  ([INPE, 16 Oct 2026](https://www.gov.br/inpe/pt-br/assuntos/ultimas-noticias/brasil-alcanca-menores-taxas-de-desmatamento-da-serie-historica-na-amazonia-e-no-cerrado); [INPE, 18 Aug 2026](https://www.gov.br/inpe/pt-br/assuntos/ultimas-noticias/sistema-do-inpe-aponta-5-731-km2-de-desmatamento-na-amazonia-em-2025)). PRODES for all biomes is now in the TerraBrasilis Situation Room (13 Aug 2026). BiomasBR updated suppression data on 16 Oct 2026.
- **Problems / pain points (from INPE methodology notes and the SIM-Biomas project):**
  - **Legality:** "Authorized and unauthorized suppression are both included… Determining legality requires cross-referencing with authorization records".
  - **Fire:** fire is not automatically counted as deforestation; hotspots ≠ burned area.
  - Outside the Cerrado, national burned-area monitoring "operates at 1 km spatial resolution".
  - DETER covers only the Amazon, Cerrado and Pantanal daily.
  - PRODES is annual (low frequency).
  - Long lag from detection to enforcement ([INPE SIM-Biomas, Oct 2026](https://www.gov.br/inpe/pt-br/assuntos/ultimas-noticias/inpe-recebera-apoio-do-fundo-amazonia-para-aprimorar-monitoramento-ambiental)).
  - Context: a "very strong" **El Niño 2026–27 with 95% probability for Oct–Dec** ([INPE bulletin, 1 Oct 2026](https://www.gov.br/inpe/pt-br/assuntos/ultimas-noticias/painel-el-nino-2026-2027-quarto-boletim-sobre-o-monitoramento-do-fenomeno-no-brasil-e-publicado)) means elevated Amazon drought and fire risk in 2026–27.
- **How they're trying to solve it:** **SIM-Biomas: R$147.6 M from the Amazon Fund (BNDES), 60 months.** It will integrate PRODES and DETER with AI and raise PRODES frequency (intra-annual). It adds short-term risk indicators for deforestation, degradation and fire (combined with land tenure, socioeconomic and climate data), 30 m burn scars for all biomes, DETER for the Caatinga, Atlantic Forest and Pampa, aircraft GHG sampling, and TerraBrasilis++ ([INPE](https://www.gov.br/inpe/pt-br/assuntos/ultimas-noticias/inpe-recebera-apoio-do-fundo-amazonia-para-aprimorar-monitoramento-ambiental)). A Nature paper (Gatti et al., Oct 2026) found deforestation and fire dominate Amazon carbon emissions in two of three analysed periods ([INPE, 21 Oct 2026](https://www.gov.br/inpe/pt-br/assuntos/ultimas-noticias/estudo-do-inpe-publicado-na-nature-aponta-atividades-humanas-como-principal-fator-das-emissoes-de-carbono-na-amazonia)).
- **Data:** TerraBrasilis (PRODES/DETER vectors, CC BY-SA), Brazil Data Cube, CBERS-4/4A and Amazonia-1 (INPE catalogue, free), Sentinel-1/2, Biomass (P-band; Brazil "preparing to use Biomass data" per [ESA](https://www.esa.int/Applications/Observing_the_Earth/FutureEO/Biomass)).
- **Hackathon angle (strong):**
  - **"Legal or illegal?":** intersect DETER/PRODES polygons with public CAR (rural property registry) and authorisation records (state ASV permits where public). Rank alerts by likelihood of illegality for IBAMA. INPE says this is required and not done in the product.
  - **"Next-month deforestation and fire risk"** for the 2026–27 El Niño: a short-term risk indicator from DETER history plus ECMWF seasonal forecasts plus roads. This is exactly the SIM-Biomas goal.
- **Credibility:** official.

### 15.2 CBERS and Brazil in the Charter
- CBERS-4 imagery was tasked through the International Charter for a glacial-collapse disaster on the Nepal–Tibet border (28 Aug 2026) ([INPE](https://www.gov.br/inpe/pt-br/assuntos/ultimas-noticias/inpe-apoia-resposta-a-desastre-no-nepal-com-imagens-do-cbers-4)). The Charter received the IAF World Space Award 2026 ([INPE, 6 Oct 2026](https://www.gov.br/inpe/pt-br/assuntos/ultimas-noticias/carta-internacional-espaco-e-grandes-desastres-recebe-premio-internacional)). INPE's MONAN weather model became operational at 10 km on the Jaci supercomputer (4 Sep 2026). INPE and ICCT launched contrail climate-impact monitoring over Brazil (9 Oct 2026) ([INPE news list](https://www.gov.br/inpe/pt-br/assuntos/ultimas-noticias)).
- **Hackathon angle:** "Contrail avoidance": combine MTG/GOES imagery with ERA5 humidity to flag persistent-contrail regions on Brazilian routes (also cross-slice).

---

## 16. Africa, Australia, Korea, UAE

### 16.1 Digital Earth Africa (DE Africa)
- **What it is:** A programme of icipe (with AfriGEO) providing analysis-ready Landsat and Sentinel-1/2 for Africa. Services: Coastlines, Cropland Extent, Fractional Cover, GeoMAD, NDVI anomalies, Waterbodies, Water Observations from Space (WOfS), and Water Quality. Access via DE Africa Map, Sandbox, notebooks and OGC services; "openly accessible and freely available" (licence not stated on the home page). 2026 news: Somaliland ministry training (30 Sep), Rusangu University (21 Sep), and "Water tracking to map malaria's mosquito habitats" (28 Jul) ([digitalearthafrica.org](https://www.digitalearthafrica.org/)).
- **Problems / pain points:** Capacity building; uptake by ministries; funding sustainability *(not stated on page; inference)*. The ECMWF Code for Earth Challenge 41 cites "a lack of systematic flood-relevant forecast evaluation" in East Africa ([GitHub issue](https://github.com/ECMWFCode4Earth/Challenges_2026/issues/16)).
- **Hackathon angle:** "Malaria habitat from WOfS": small ephemeral water bodies (Sentinel-1/2) plus temperature, giving an Anopheles breeding-site risk map for a district. DE Africa is already working on it, which validates the problem.
- **Credibility:** official.

### 16.2 Digital Earth Australia (Geoscience Australia)
- **What it is:** Analysis-ready, decades-deep Landsat/Sentinel archive for Australia on the Open Data Cube, "freely available", via DEA Maps. Example: Victoria's CFA used DEA waterbody maps to find water to fight fires ([GA DEA page](https://www.ga.gov.au/scientific-topics/dea)).
- **Problems / pain points:** Not stated on the page. Landsat dependency and the Landsat Next restructuring are a likely concern *(unverified; cross-slice US)*.
- **Hackathon angle:** "Firefighting water finder" generalised (DE Africa or Europe): nearest reachable water body with current water present, from WOfS plus Sentinel-2.
- **Credibility:** official.

### 16.3 Korea (KASA / KARI)
- **What it is:** The Korea AeroSpace Administration was founded 27 May 2024. It oversees KARI and KASI. FY2026 budget ₩1.12 trillion (~US$749 M). EO assets include the CAS500 series and GEO-KOMPSAT (Chollian) ([Wikipedia KASA, community-edited](https://en.wikipedia.org/wiki/Korea_AeroSpace_Administration)).
- **Problems / pain points:** Not researched in depth. The KOMPSAT data policy and 2025–26 launches are unverified.
- **Credibility:** secondary.

### 16.4 UAE (MBRSC)
- **What it is:** MBZ-SAT launched 14 Jan 2025 on Falcon 9 from Vandenberg. Developed by MBRSC (infobox lists Satrec Initiative as manufacturer). "Ultra-high-resolution imagery"; data delivered "within two hours"; for environment, infrastructure and disaster relief ([Wikipedia MBZ-SAT](https://en.wikipedia.org/wiki/MBZ-SAT)).
- **Problems / pain points:** The data policy is not public. The UAE Sirb SAR constellation was not verified on this pass.
- **Credibility:** secondary.

---

## 17. Coordination bodies: GEO and CEOS

### 17.1 GEO (Group on Earth Observations)
- **What it is:** An intergovernmental network hosted by WMO in Geneva. Tagline: "Earth Intelligence for All". Nine solution areas: agriculture and food security; water and land; ecosystems, biodiversity and carbon; weather, hazards and disaster resilience; climate, energy and urbanisation; One Health; community impact; open data and infrastructure; application driver. It cites "exponential data growth and planetary-scale crises" ([earthobservations.org](https://earthobservations.org/)). Recent items: 2026 GEO Symposium Report (~400 participants, Geneva); "AfriGEO" decade (Oct 2026); presence at CBD COP17. GEO was a partner in the Φ-lab/ITU GeoFM height challenge ([ITU slides](https://www.itu.int/en/ITU-T/academia/kaleidoscope/2026/Documents/Presentations/MANARA-presentation.pdf), via search).
- **Global Ecosystems Atlas** (GEO with ESA, Google, Ai2, Esri, IUCN, CBD, JCU): "the world's most comprehensive, standardised map of Earth's ecosystems", aligned to the IUCN Ecosystem Typology. In beta with **77% global coverage: 7/10 realms, 18/25 biomes, 85/110 ecosystem functional groups**. Full release "by early 2027". A related article is headed "Ambiguous data licences undermine global ecosystem mapping efforts" ([globalecosystemsatlas.org](https://www.globalecosystemsatlas.org/)).
- **Problems / pain points:** 23% of the globe is unmapped, 25 ecosystem functional groups are missing, and licences are ambiguous. Kunming-Montreal GBF reporting needs ecosystem extent maps.
- **Hackathon angle:** **"Fill one missing ecosystem type"**: map an unmapped IUCN functional group (e.g., intermittent wetlands or kelp forests) for one region, with embeddings (Major TOM, AlphaEarth) plus a few labels. Also a "licence clarity checker" for input datasets.
- **Credibility:** official.

### 17.2 CEOS (Committee on Earth Observation Satellites)
- **What it is:** Coordination of civil space EO agencies. Working groups: Capacity Building & Data Democracy; Climate (with CGMS); Cal/Val; Disasters; Information Systems & Services. Virtual constellations: Atmospheric Composition, COAST, Biodiversity, LSI, Ocean Colour, OST, OSVW, Precipitation, SST. Activities: CEOS-ARD, Global Stocktake, SDGs. Recent titles include "Policy Interoperability…", "Updating the CEOS-ARD Governance Framework" and "Why a Pretty Map Is Not Always an Accurate One" ([ceos.org](https://ceos.org/)). LPS25 F.04.26 (CEOS/CGMS) stresses the transition of GHG monitoring "from research to operations" ([LPS25 sessions](https://lps25.esa.int/sessions/)).
- **Hackathon angle:** "Is this map accurate?": an automatic accuracy and uncertainty report card for any EO-derived map, using CEOS cal/val reference sites and SHRUG-FM-style abstention (see §19.4).
- **Credibility:** official.

---

## 18. Disaster response: International Charter, UN-SPIDER, and bottlenecks

### 18.1 International Charter "Space and Major Disasters"
- **What it is:** Agencies pool satellite tasking for disasters; authorised users trigger activations; Universal Access extends eligibility. Activations ([24th Annual Report, search summary](https://disasterscharter.org/news/24th-annual-report-of-the-charter); [23rd report](https://upload.disasterscharter.org/news/23rd-annual-report-of-the-charter)):
  - **2024: 85 activations in 52 countries.** Mandated organisations from 43 disaster-prone countries had joined via Universal Access.
  - 2023: 63 activations in 40 countries, 6 of them first-time countries.
  - Germany told COPUOS (Feb 2025) that DLR supported 70 activations and called rising activations partly a sign of worsening climate-driven disasters ([UNOOSA statement, search summary](https://www.unoosa.org/documents/pdf/copuos/stsc/2025/Statements/6_Germany.pdf)).
  - The Charter won the IAF World Space Award 2026 ([INPE](https://www.gov.br/inpe/pt-br/assuntos/ultimas-noticias/carta-internacional-espaco-e-grandes-desastres-recebe-premio-internacional)).
  - The Charter website returned errors (HTTP 404/500, timeouts) on 24 Oct 2026, so 2025–26 counts were **not verified**.
- **Problems / pain points (bottlenecks):**
  1. **Manual damage interpretation:** "Mapping earthquake damage still depends heavily on human interpretation of satellite imagery, which is slow" ([Φ-lab](https://philab.esa.int/a-bold-new-chapter-for-ai4eo-with-esa-%cf%86-lab-challenges/)). LPS25 B.04.05: area-wide mapping "is time-consuming and requires a large number of experienced interpreters" and "the amount of remote sensing data… [makes] it impossible in practice to assess all available data visually" ([LPS25 sessions](https://lps25.esa.int/sessions/)).
  2. **Optical blocked by cloud and smoke at night.**
  3. **Product licensing:** Charter VHR imagery is restricted to authorised users *(general knowledge)*.
  4. **Volume of activations rising** (63 → 85, 2023 → 2024).
- **How they're trying to solve it:** ESA Charter Mapper (cloud processing for project managers); the Φ-lab "AI for Earthquake Response" challenge with Charter archive imagery on EOTDL; CEMS AI damage-assessment workshops (10 Nov 2026).
- **Hackathon angle:** "Charter triage copilot": given an activation (event polygon, date), pull open pre/post Sentinel-1/2 plus NISAR, run change detection, and give the volunteer project manager a ranked list of tiles to look at first. Abstain where uncertain (SHRUG-FM). The bottleneck is human attention, which makes a clear pitch.
- **Credibility:** official (partly via search summaries).

### 18.2 UN-SPIDER (UNOOSA)
- **What it is:** UNOOSA's platform for space-based disaster management: technical advisory missions, Recommended Practices (step-by-step mapping guides), and capacity building. 2026 items: disaster response to the **Venezuela earthquake** (9 Jul 2026); technical advisory mission to Kyrgyzstan (8 Jul); Nepal national flood simulation exercise (27 Apr); multi-hazard risk capacity building in the Philippines (30 Apr); "Satellite imagery for monitoring environmental impacts in crisis-affected areas" (15 Apr) ([UN-SPIDER news](https://www.un-spider.org/news-and-events/news)). LPS25 B.04.08 presented UN-SPIDER Recommended Practices with ZFL Bonn (SPEAR project, Africa focus) ([LPS25 sessions](https://lps25.esa.int/sessions/)).
- **Problems / pain points:** Capacity gaps in national agencies; the long tail of countries without in-house EO skills.
- **Hackathon angle:** Turn a UN-SPIDER Recommended Practice (e.g., Sentinel-1 flood mapping) into a one-click, LLM-guided workflow for a non-expert disaster agency.
- **Credibility:** official.

---

## 19. Other published problem sources (hackathons, programmes, conferences)

### 19.1 CASSINI Hackathons and CASSINI Challenges (EU / EUSPA)
- **12th CASSINI Hackathon "EU Space for Peace and Resilience" (27–29 Nov 2026)** has three challenges ([cassini.eu/hackathons](https://www.cassini.eu/hackathons)):
  1. *Cybersecurity for space-based strategic enablers*: Copernicus and Galileo data to validate signals and identify anomalies.
  2. *Space-enabled crisis response and civil resilience*: map conflict damage with EO, route goods and people with Galileo, and improve civilian infrastructure safety.
  3. *Countering transnational crime and terrorism with space data*: borders, critical infrastructure, smuggling routes.
  Prizes €5k / €3k / €1k plus 6 months mentoring.
- **Past winners show what judges reward** ([CASSINI portfolio](https://www.cassini.eu/hackathons/portfolio)):
  - 2026 "Space for Water": Viadrus AI (pipeline leaks from ground subsidence), Blue Pixel (water pollution alerts), FieldCheck (irrigation guidance).
  - 2025 "Consumer Experience": avalanche probability, Crowdless (over-tourism).
  - 2025 "Healthcare": SpaceScope, EnviroCopilot (offline heat/pollution/UV alerts).
  - 2024 "Defence & Security": SpaceGuardian (collision avoidance), SignalHawk (GNSS spoofing).
  - 2024 "Green Transition": TerraMetallum (heavy metals in soil), WasteNoTime (illegal landfills).
  - 2023: FoodSafe, Salamat (refugee flows), FireWatch, Forest Defender (illegal deforestation).
  - 2022: YOLANDA (bark beetle), Cropernicus (yield).
  - 2021: Arctic soil erosion, IceBlink (ice detection for vessels), "Have Sea Will Swim" (bathing water), Project HIVE (beehive siting).
- **CASSINI Challenges 2026:** 12 × €100k prizes; requires TRL ≥5 and CRL ≥4; closed 26 Mar 2026 ([EUSPA](https://www.euspa.europa.eu/cassinichallenges)).
- **Credibility:** official.

### 19.2 ECMWF Code for Earth 2026: full challenge list
- **What it is:** ECMWF's summer open-source programme (since 2018). The 2026 edition closed 23 Sep 2026. Partners: ICPAC, AfriClimate AI, ENTSO-E. Streams: Africa, Data Visualisation, ML, Software ([Code for Earth](https://codeforearth.ecmwf.int/); [streams](https://codeforearth.ecmwf.int/streams)). The 16 challenges, with GitHub issue numbers ([Challenges_2026 issues](https://github.com/ECMWFCode4Earth/Challenges_2026/issues)):
  - **Visualisation:** 10 PyroScope (fire products web viz); 11 interactive flood-forecast dashboard; 12 topology-safe geometry simplification; 13 reconciling model data with observations; 14 visualising climate-change impact on the European power system (ENTSO-E).
  - **ML:** 20 **ML-ready archive of satellite-derived river flood inundation observations**; 21 AIrWISE (AI air-quality reporting); 22 HydroML-Verify (physical consistency of ML streamflow forecasts); 23 COMPEXT (compound extremes for energy security); 24 AI energy.
  - **Software:** 30 GIS app on the Data Stores Service; 31 CLAM (cloud template for an NWP local-area model); 32 "Smart User Requirements: AI-assisted insights for C3S"; 33 automated air-quality feature detection ("from thresholds to events").
  - **Africa:** 40 **compressing AI NWP models for edge deployment** (AfriClimate AI); 41 **"Missed Opportunities in Flood Disaster Risk Management"** (ICPAC).
- **Detail, Challenge 20:** "Satellite flood products are abundant, but… retrieval scripts have only been run ad hoc for a few events… there is no large archive of flood observations for training". Inputs: GFM and VIIRS for the 43 Kuro Siwo events, then Copernicus Rapid Flood Mapping, MODIS, Maxar open data, SenForFlood, UrbanSARFloods ([issue #2](https://github.com/ECMWFCode4Earth/Challenges_2026/issues/2)).
- **Detail, Challenge 41:** make the >1 PB ECMWF IFS ensemble archive on AWS (GRIB2, 51 members) analysis-ready (Zarr v3 / IceChunk). Compute rainfall exceedance probabilities against CMORPH return periods. Validate against EM-DAT floods and IMERG at admin-1 for East Africa. Stated problem: "a lack of systematic flood-relevant forecast evaluation" ([issue #16](https://github.com/ECMWFCode4Earth/Challenges_2026/issues/16)).
- **Credibility:** official.

### 19.3 ActInSpace 2026 (CNES/ESA)
- A hackathon on ESA and CNES patents, 30–31 Jan 2026. The Φ-lab/InCubed prize was an invitation to the Φnnovation Summit (ESRIN, 23–25 Jun 2026) ([Φ-lab](https://philab.esa.int/?p=8284)).

### 19.4 Φ-lab programme items that are literal problem statements
- **EO Virtual Constellation (EOVC), call for collaborators (21 Sep 2026):** onboard AI "typically follows static instructions and runs pre-scheduled tasks over fixed areas, sometimes days ahead". The goal is satellites that trigger actions and recruit other sensors in near real time. The first demonstration is **flood monitoring in the Danube and French river networks**, led by CS Group. "For decades, we have looked at Earth observation as a collection of individual satellites" (Nicolas Longépé) ([Φ-lab](https://philab.esa.int/esa-%cf%86-lab-calls-for-collaborators-to-expand-the-earth-observation-virtual-constellation/)).
- **SHRUG-FM (EarthVision 2026 Best Paper, 4 Jun 2026):** geospatial foundation models are "confidently wrong" in under-represented environments. SHRUG-FM lets a model predict, warn or "shrug", and reduces risk on burn scars, floods and landslides. Code: github.com/vishalned/SHRUG-FM ([Φ-lab](https://philab.esa.int/shrug-fm-wins-best-paper-award-at-the-earthvision-2026-workshop/)).
- **SPRINT4EO (OHB Digital Services, through Jun 2027):** first sprints are EOMAS (an agentic EO multi-agent assistant), Carbonherence (urban vegetation carbon from multispectral, SAR, thermal and LiDAR), and HYPERFUSE (VHR proxy mosaics from Sentinel-2) ([Φ-lab](https://philab.esa.int/sprint4eo-giving-europe-a-running-start-in-earth-observation-innovation/)).
- ESA's first quantum computer (15 Jul 2026) and OroraTech as a Copernicus Contributing Mission (thermal wildfire, FOREST-3 launched Jan 2025) ([Φ-lab news list](https://philab.esa.int/); [Φ-lab OroraTech](https://philab.esa.int/ororatechs-journey-from-start-up-to-copernicus-data-provider/)).

### 19.5 Living Planet Symposium 2025 (Vienna, 23–27 Jun 2025): problem index from 461 session descriptions
- **What it is:** ESA's flagship EO conference: 6,900 participants from 125 nationalities, 250+ sessions, 60+ agoras, 4,200+ presentations ([lps25.esa.int](https://lps25.esa.int/)). All 461 session descriptions were parsed from the site's session data file ([lps25.esa.int/sessions](https://lps25.esa.int/sessions/); data in `sessions.js` on the same site). The LPS25 "Challenges" page ran design-thinking workshops (C.01.17) asking: "How could a mission benefit people and the planet? What current challenges could an Earth observation mission address? Where are current technology gaps…?" The winners were to shape the next YPSat mission ([LPS25 challenges](https://lps25.esa.int/challenges/)).
- **Session counts by theme (461 total):**
  - D.03 Open Science 33; D.04 Cloud EO ecosystems 30; **D.02 AI/data fusion/big data 29**; C.01 New mission concepts 25; **F.04 Enabling environmental policies 25**; C.03 Copernicus missions 22; C.02 Research missions 21.
  - A.08 Ocean 20; D.01 Digital Twin / DestinE 19; C.06 Cal/val and data quality 18; A.01 Atmosphere 17; F.02 International cooperation 17; A.02 Terrestrial biosphere 16.
  - F.01 Education 15; A.05 Climate 13; B.03 Adaptation/mitigation/resilience 12; E.01 Commercialisation 12; A.09 Polar 11 (+1); F.05 Socio-economic benefits 11; A.07 Hydrology 10; C.05 National missions 10.
  - B.01 Sustainable development / climate finance 9; B.04 Extremes and risks 8; A.03 Carbon 7; A.10 Solid Earth 6; B.02 Planet under pressure 6; D.06 Emerging tech 6.
  - D.05 Operations frameworks 5 (+2); E.05 User/market needs 5; A.04 GHG 4; E.03 PPPs 4; A.06 Geospace 3; C.04 Meteorology 3; F.03 Third-party missions 3; E.02 Tech uptake 2; A.11 Earth energy budget 1.
- **One-line problem statements by theme** (paraphrased or quoted from session descriptions; session code in brackets):
  - **B. Climate action and sustainability**
    - [B.01.03] Global ARD "is not necessarily fully tailored to particular local issues"; gaps between ARD and local needs "need to be mitigated and ultimately closed"; community projects struggle to stay self-sustaining.
    - [B.01.05] In-situ terrestrial networks behind ECVs run on "short-term research efforts" without long-term support, which threatens cal/val and the climate records.
    - [B.01.07] "The EO industry often lacks a clear understanding of how IFIs operate", which blocks EO in development finance (World Bank, ADB).
    - [B.03.02] Adaptation gaps "will continue to grow"; by 2030 all UNFCCC Parties must run adaptation monitoring, evaluation and learning systems; EO's role "is only beginning to be explored".
    - [B.03.06] Disease seasonality (dengue, West Nile, cholera after floods) has inter-annual variability "difficult to predict"; climate-health EO is underused.
    - [B.03.16] Irrigation is about 70% of global freshwater withdrawals; evapotranspiration and root-zone soil moisture from Sentinel-2/3 plus C3S are needed for water management.
    - [B.04.01] Geohazards (landslides, volcanoes, inactive mines, coastal lowlands) need multi-year, high-resolution terrain-motion monitoring, including new L-band.
    - [B.04.02] Compounding and cascading multi-hazards (flood after drought) are poorly predicted.
    - [B.04.04] EM-DAT counted 399 disasters in 2023, 86,473 deaths and 93.1 M affected; AI mapping needed.
    - [B.04.05] Rapid, scalable, reliable disaster information "remains a major challenge"; manual interpretation is a bottleneck.
    - [B.04.06] Wildfire detection, spread modelling, burned-area mapping, on-orbit processing; benchmark datasets wanted.
    - [B.04.07] Damage Proxy Maps (SAR coherence change) need easier on-demand generation and thresholding.
  - **C. Missions**
    - [C.03.10] CO2M is needed because "uncertainties associated with current anthropogenic emission estimates at national and regional scales need to be improved".
    - [C.03.13] Onboarding a new Sentinel-1 unit (1C) into existing pipelines is a challenge (and now 1D: see §1.6).
    - [C.03.18] Contributing Missions (commercial VHR, SAR, hyperspectral, thermal) fill "critical spatial, temporal, and thematic observation gaps".
    - [C.03.19] Copernicus services must constantly evolve to stay "fit for the purpose".
    - [C.03.21] "SentiBoard" is a real-time Copernicus operations dashboard, so ops transparency is wanted (cf. the CDSE outage list).
    - [C.03.03] Prepare CHIME applications with EnMAP, EMIT, HiSUI, PRISMA and DESIS.
    - [C.01.17] Design the next tech-demo mission (YPSat).
  - **D. Digital, AI, twins**
    - [D.02.02] "Significant gap in publications for cryosphere applications"; AI4EO has not realised its potential in polar science.
    - [D.02.06] Labelled data "rarely available in environmental applications"; "data output and storage have already become a major bottleneck for high-resolution climate modeling".
    - [D.02.07] LLM agents for EO: "bridging the gap between complex data and user understanding".
    - [D.02.08] AI must show "explainability, physics-awareness, and trustworthiness" to be fit for Earth Action.
    - [D.02.11] AI super-resolution "suffers from the black-box syndrome".
    - [D.02.12] Ocean monitoring: harmonisation, data fusion and gap filling with AI.
    - [D.02.13] AI compression for downlink and onboard memory limits.
    - [D.02.21] Foundation-model adoption faces "prohibitive costs" and a "domain adaptation gap".
    - [D.02.22] GIS lacks deep-learning support and DL lacks geospatial support; few multispectral pretrained models.
    - [D.02.27] Labelling is "one of the key bottlenecks" (SCANEO active learning).
    - [D.02.29] "RSFMs are on the rise but their evaluation is difficult" (GeoBreeze).
    - [D.02.31] Maritime littering with AI and EO (Edge-SpAIce).
    - [D.01.02] Digital twins need interoperability standards.
    - [D.01.16] There is a gap between complex climate data and public understanding.
    - [D.05.03] "The Sentinel data processors, developed over a decade ago, require upgrades to remain viable for the next 15 years", which means a move to cloud-native Zarr (EOPF).
    - [D.05.04] AI could bring "millions of new users" to Copernicus, while policy makers are "challenged to keep the investment momentum" for "European sovereign AI".
    - [D.05.05] CDSE annual user review (co-creation).
  - **E. Industry and users**
    - [E.01.02] End users need "spatial, temporal, and thematic detail at a level unobtainable from public missions alone".
    - [E.01.07] EO uptake "remains limited" because of "fragmentation of the EO service landscape", "lack of scaling and funding mechanisms", heterogeneous integration needs and "access barriers"; there is a "long tail of users".
    - [E.01.12] Natural-language search over EO and in-situ catalogues (IEOTO LLM assistant).
    - [E.03.02] EO "return on investment… could be improved"; end users "are often unaware that space can contribute"; users want information "when they want, where they need it, at an affordable cost, and through known, common interfaces".
    - [E.05.01] EUDR supply-chain monitoring needs "traceability systems linking products to accurate and complete geographic ground (vector) data" (Forest Data Partnership: Google, FAO, Unilever, WRI; Whisp tool).
    - [E.05.02] EU ETS and CBAM drive demand for "accurate, timely and transparent" CO2/CH4 monitoring before EO is formally in regulation.
  - **F. Policy**
    - [F.04.01] Common Agricultural Policy monitoring.
    - [F.04.02] Global food security.
    - [F.04.03] Topsoil mapping for the EU Soil Monitoring Law.
    - [F.04.05] Water scarcity affects more than 40% of the world's population; lake volume, surface water extent, altimetry.
    - [F.04.06] Ramsar wetland inventory.
    - [F.04.07] GBF and SDG indicator tracking.
    - [F.04.08] Nature finance and ecosystem accounting (TNFD-type disclosure).
    - [F.04.11] Environmental crime is "increasing by 5-7% annually" (illegal waste, logging, water abstraction); "data privacy, quality, availability, and legal admissibility must be overcome" (new EU Environmental Crime Directive).
    - [F.04.13] Urban resilience.
    - [F.04.15] Coastal adaptation.
    - [F.04.16] Blue economy.
    - [F.04.20] EUDR: seven commodities, December 2020 cut-off, commodity mapping and field-data strategies.
    - [F.04.22] National Statistical Offices' reporting burden.
    - [F.04.23] Nature Restoration Regulation: restore ≥20% of EU land and sea by 2030, with "existing data gaps" and consistency issues.
    - [F.04.26] CEOS/CGMS GHG monitoring must move "from research to operations".
    - [F.04.29] EO should "fill the current monitoring gaps" for EU Ambient Air Quality Directives.
    - [F.04.30] "Persistent data gaps, particularly in low-income and vulnerable regions, continue to hamper" SDG tracking.
    - [F.04.32] Aquatic carbon roadmap for the Global Stocktake.
    - [F.04.33] BBNJ high-seas MPAs: "compliance and enforcement will remain a challenge" without satellite and vessel monitoring.
- **Hackathon angle:** LPS25 shows where ESA's community *itself* says the gaps are. The strongest overlap with "clear problem + public data + 36 h" is in B.04 (disaster automation), E.01.07/E.03.02 (last-mile uptake), F.04.11 (environmental crime), F.04.20 / E.05.01 (EUDR), F.04.33 (high-seas MPAs), and D.02.07 (LLM agents for EO).
- **Credibility:** official (session descriptions written by ESA and community convenors).

---

## 20. Table of published challenge and competition problem statements

| # | Programme | Challenge | Problem statement (short) | Data provided / suggested | Status / dates | Source |
|---|---|---|---|---|---|---|
| 1 | ESA Kelvins (ACT) | Lunar X-view | Localise a lunar rover by matching a ground panorama to an orbital map, with no Earth signal | Dataset and starter kit on Kelvins | Open 1 Nov 2026 – 31 Mar 2027 | [Kelvins](https://kelvins.esa.int/lunar-x-view/) |
| 2 | Kelvins | ELOPE | Estimate lunar-lander ego-motion from event-camera optical flow | Event-camera data | Closed 31 Aug 2025 | [Kelvins](https://kelvins.esa.int/) |
| 3 | Kelvins | The OPS-SAT case | Edge-AI classification of raw imagery from the OPS-SAT cubesat with few labels | OPS-SAT images | Closed 31 Oct 2022 | [Kelvins](https://kelvins.esa.int/) |
| 4 | Kelvins | Pose Estimation 2021 (SPEC2021) | Close the synthetic-to-real domain gap for spacecraft pose | SPEED+ | Closed 31 Mar 2022 | [Kelvins](https://kelvins.esa.int/) |
| 5 | Kelvins | Planetary defence | Design an asteroid deflection | Simulated scenario | Closed 5 Sep 2021 | [Kelvins](https://kelvins.esa.int/) |
| 6 | Kelvins | Space debris: the origin | Identify the parent event of debris fragments | Orbital elements | Closed 5 Sep 2021 | [Kelvins](https://kelvins.esa.int/) |
| 7 | Kelvins | spotGEO | Detect faint GEO satellites in ground-telescope image sequences | Image sequences | Closed 1 Sep 2020 | [Kelvins](https://kelvins.esa.int/) |
| 8 | Kelvins | Collision Avoidance Challenge | Predict final collision risk from CDM time series (decide to manoeuvre) | ESA CDM dataset | Closed 16 Dec 2019 | [Kelvins](https://kelvins.esa.int/) |
| 9 | Kelvins | Pose Estimation (SPEC2019) | Satellite 6-DoF pose from one image | SPEED | Closed 1 Jul 2019 | [Kelvins](https://kelvins.esa.int/) |
| 10 | Kelvins | PROBA-V Super Resolution | Multi-frame super-resolution of PROBA-V 300 m → 100 m | PROBA-V | Closed 1 Jun 2019 | [Kelvins](https://kelvins.esa.int/) |
| 11 | Kelvins | The Kessler Run (GTOC9) | Debris-removal trajectory optimisation | Problem file | Closed 2 May 2017 | [Kelvins](https://kelvins.esa.int/) |
| 12 | Kelvins | Star Trackers: First contact | Star identification | Synthetic star fields | Closed 1 Sep 2017 | [Kelvins](https://kelvins.esa.int/) |
| 13 | Kelvins | Mars Express Power | Predict thermal power consumption to extend the mission | MEX telemetry | Closed 1 Aug 2016 | [Kelvins](https://kelvins.esa.int/) |
| 14 | ESA Φ-lab Challenges | AI for Earthquake Response (with Int'l Charter) | Automatically classify buildings damaged or undamaged from pre/post imagery; replace slow manual interpretation | Multi-mission HR imagery from past Charter activations via Charter Mapper and EOTDL | Final 15 Sep 2025; prizes €3k/2k/1k | [Φ-lab blog](https://philab.esa.int/a-bold-new-chapter-for-ai4eo-with-esa-%cf%86-lab-challenges/) |
| 15 | Φ-lab | HYPERVIEW2 (XAI) | Explainable estimation of soil B, Cu, Zn, Fe, S, Mn | Airborne hyperspectral, Sentinel-2, PRISMA | Awards at ECAI/EASi, Oct 2025 | [Φ-lab blog](https://philab.esa.int/a-bold-new-chapter-for-ai4eo-with-esa-%cf%86-lab-challenges/) |
| 16 | Φ-lab | PANGAEA GeoFM benchmark + Data Sprints | Standardised evaluation of geospatial foundation models across sensors, resolutions and tasks | PANGAEA benchmark | Open-ended | [Φ-lab blog](https://philab.esa.int/a-bold-new-chapter-for-ai4eo-with-esa-%cf%86-lab-challenges/) |
| 17 | Φ-lab | ClearSAR Track 1 | Detect RFI in Sentinel-1 quicklooks so it can be handled operationally | 3,940 RGB quicklooks (3,154 train with boxes, 786 test); mAP | Awards at IEEE ICIP, 13–17 Sep 2026; Track 2 (processing chain) announced | [Φ-lab platform](https://platform-challenges.philab.esa.int/clear-sar) |
| 18 | Φ-lab + ITU AI for Good (+KTH, GEO) | Reaching new heights with GeoFM | Building and vegetation height plus 3D semantic segmentation from embeddings; train regionally, generalise globally | Precomputed embeddings (AlphaEarth, TESSERA, TerraMind, THOR) | Closed 30 Jun 2026; >€9k | [Φ-lab platform](https://platform-challenges.philab.esa.int/geoai); [ADB mirror](https://challenges.adb.org/en/challenges/reaching-new-heights-with-geofm) |
| 19 | Φ-lab (AI4EO) + ECMWF/CAMS | Air Quality & Health | AI downscaling of PM2.5 (CAMS ~10 km) and NO2 (S5P) to local scale | CAMS, S5P, 3 AOIs 500×500 km (N Italy, California, South Africa) | Closed | [Φ-lab platform](https://platform-challenges.philab.esa.int/air-quality-and-health) |
| 20 | Φ-lab (AI4EO) | AutoICE | Automated sea-ice charting from Sentinel-1 SAR | Sentinel-1 plus ice charts | Closed | [Φ-lab challenges](https://challenges.philab.esa.int/) |
| 21 | Φ-lab (AI4EO) | Food Security | Deep learning on dense time series for near-real-time crop monitoring | Sentinel time series | Closed | [Φ-lab challenges](https://challenges.philab.esa.int/) |
| 22 | Φ-lab (AI4EO) | HYPERVIEW (2022) | Soil parameters from hyperspectral for farm sustainability | Airborne hyperspectral | Closed | [Φ-lab challenges](https://challenges.philab.esa.int/) |
| 23 | Φ-lab (AI4EO) | MapYourCity | (Building/urban mapping; details not shown on page) | — | Closed | [Φ-lab challenges](https://challenges.philab.esa.int/) |
| 24 | Φ-lab (AI4EO) | Sentinel-2 (agriculture) | Agriculture from Sentinel-2 (details not shown) | Sentinel-2 | Closed | [Φ-lab challenges](https://challenges.philab.esa.int/) |
| 25 | Φ-lab | OrbitalAI (Φsat-2 apps) | In-orbit AI apps for sustainability, business, science; winners flew on Φsat-2 (marine pollution, wildfire) | Φsat-2 simulator / L1 | Closed (2023) | [ESA](https://www.esa.int/Applications/Observing_the_Earth/Phsat-2/Phsat-2_gets_two_new_AI_apps) |
| 26 | Φ-lab + Hello Tomorrow | Grand Marathon (2nd ed.) | AI-enabled EO to detect "short-lived hazards", give near-real-time insight, protect civilians in conflict and disaster (incl. children) | Open; MVP with EO test data | Deadline 11 Jan 2026; finals 11–12 Jun 2026; up to €215k | [Φ-lab CIN](https://cin.philab.esa.int/databases/news-db/esa-lab-grand-marathon) |
| 27 | Φ-lab | Call for Φdeas / Sprints / EOVC call | Open idea call; ESL sprints (e.g., FMs for extreme environments → SHRUG-FM); EO Virtual Constellation collaborators | — | Rolling | [Φ-lab portal](https://philab.esa.int/%CF%86-lab-collaborations-portal/) |
| 28 | ESA OSIP | Quantum technologies for exploration (HRE) | Quantum computing, sensing, comms and materials for LEO, Moon, Mars | — | Due 12 Apr 2026 (unverified) | [ESA OSIP](https://www.esa.int/Enabling_Support/Preparing_for_the_Future/Discovery_and_Preparation/The_Open_Space_Innovation_Platform_OSIP) |
| 29 | ESA OSIP | IBPER radiation | Biological and physical effects of space radiation | — | Due 23 Mar 2025 (unverified) | [BSGN](https://bsgn.esa.int/?p=102792) |
| 30 | ESA OSIP | Open Channel | Any idea not covered by a campaign (EO-relevant via Φ-lab "Call for Φdeas") | — | Continuous | [ESA OSIP](https://www.esa.int/Enabling_Support/Preparing_for_the_Future/Discovery_and_Preparation/The_Open_Space_Innovation_Platform_OSIP) |
| 31 | Copernicus Masters (AZO/ESA) | — | **No 2025 or 2026 edition found.** copernicus-masters.com returned an expired TLS certificate on 24 Oct 2026. The last details found are for 2020–2022 (e.g., a 2022 prize pool of €531k; DLR "Environment, Energy & Health" and Portugal Space "Blue" challenges; a 2021 edition with 10 topics incl. AI, smart farming, maritime) | — | Status unverified | [Search: Terraviva Grants](https://www.terravivagrants.org/copernicus-masters-environment-energy-health-challenge/); [ESA 2021](https://www.esa.int/Applications/Observing_the_Earth/Copernicus/Copernicus_Masters_2021_submissions_open) |
| 32 | EU CASSINI Hackathon #12 | Cybersecurity for space-based strategic enablers | Validate signals, detect anomalies with Copernicus and Galileo | EU Space data | 27–29 Nov 2026 | [CASSINI](https://www.cassini.eu/hackathons) |
| 33 | CASSINI #12 | Space-enabled crisis response and civil resilience | Map conflict damage with EO; Galileo routing for goods and people; civilian infrastructure safety | Copernicus, Galileo | 27–29 Nov 2026 | [CASSINI](https://www.cassini.eu/hackathons) |
| 34 | CASSINI #12 | Countering transnational crime and terrorism | Border and critical-infrastructure monitoring; smuggling routes | Copernicus | 27–29 Nov 2026 | [CASSINI](https://www.cassini.eu/hackathons) |
| 35 | EUSPA | CASSINI Challenges 2026 | Use EU Space data or tech for global challenges; TRL≥5, CRL≥4 | Galileo, Copernicus, SST, GOVSATCOM | Closed 26 Mar 2026; 12×€100k | [EUSPA](https://www.euspa.europa.eu/cassinichallenges) |
| 36 | ECMWF Code for Earth 2026 | #20 ML-ready flood inundation archive | Build a standardised ML-ready archive of satellite flood extents; evaluation is "ad hoc" | GFM, VIIRS, Kuro Siwo (43 events), MODIS, Maxar open, UrbanSARFloods | Completed Sep 2026 | [GitHub #2](https://github.com/ECMWFCode4Earth/Challenges_2026/issues/2) |
| 37 | Code for Earth 2026 | #41 Missed opportunities in flood DRM (ICPAC) | Make the >1 PB IFS ensemble analysis-ready; evaluate rainfall-flood signals vs EM-DAT floods in East Africa | IFS ENS on AWS, CMORPH, IMERG, EM-DAT, GADM | Completed | [GitHub #16](https://github.com/ECMWFCode4Earth/Challenges_2026/issues/16) |
| 38 | Code for Earth 2026 | #40 Compress AI NWP for edge (AfriClimate AI) | Run AI weather models on edge devices in Africa | AIFS/Anemoi | Completed | [GitHub issues](https://github.com/ECMWFCode4Earth/Challenges_2026/issues) |
| 39 | Code for Earth 2026 | #10, 11, 12, 13, 14 (viz); #21, 22, 23, 24 (ML); #30, 31, 32, 33 (software) | PyroScope fire viz; flood dashboard; geometry simplification; model–obs reconciliation; power-system climate impact (ENTSO-E); AIrWISE; HydroML-Verify; COMPEXT compound extremes; AI energy; DSS GIS app; cloud LAM template; AI user-requirements for C3S; AQ event detection | ECMWF / Copernicus data | Completed | [GitHub issues](https://github.com/ECMWFCode4Earth/Challenges_2026/issues) |
| 40 | CNES/ESA | ActInSpace 2026 | Build products from ESA/CNES patents (EO, AI, robotics, sustainability) | Patents | 30–31 Jan 2026 | [Φ-lab](https://philab.esa.int/?p=8284) |
| 41 | ESA LPS25 | C.01.17 "Perfect Bouquet" tech-demo design | Identify EO mission concepts that "benefit people and the planet" and fill technology gaps (next YPSat) | — | 27 Jun 2025 | [LPS25](https://lps25.esa.int/challenges/) |
| 42 | ESA InCubed + AEE | Wildfire call (8 projects) | Fire-spread anticipation, onboard FMs, fuel-aware danger, SAR fire fronts, post-fire twins | Multi-source EO | Kicked off Jul 2026 | [InCubed](https://incubed.esa.int/eight-new-earth-observation-based-wildfire-applications-co-funded-by-esa-incubed/) |

*Space Apps-style note:* NASA Space Apps is in the US-agencies slice. ESA is a Space Apps partner *(not verified on this pass)*.

---

## 21. Problem bank (one line each: problem → who has it → data → source)

1. Sentinel-1 RFI corrupts SAR images and is detected only in heavy raw data → ESA/Copernicus SAR users → Sentinel-1 quicklooks (ClearSAR set) → [Φ-lab ClearSAR](https://platform-challenges.philab.esa.int/clear-sar)
2. Biomass P-band cannot acquire over large areas because of the US SOTR radar mask and RFI, so there are carbon-map holes → forest-carbon / REDD+ community → Biomass L1/L2, GEDI, CCI Biomass → [EO College (search)](https://eo-college.org/?p=388510)
3. Global forest carbon stocks are uncertain ("lack of accurate, global data") → UNFCCC, REDD+, carbon markets → Biomass, GEDI L4B, CCI Biomass → [ESA Biomass](https://www.esa.int/Applications/Observing_the_Earth/FutureEO/Biomass/ESA_s_Biomass_goes_live_with_data_now_open_to_all)
4. Sentinel-6C is unfunded because of EUMETSAT and NASA-radiometer uncertainty, so the reference sea-level record is at risk → ESA, EUMETSAT, climate science → Sentinel-6/Jason record, CMEMS → [ESA slides](https://climate.esa.int/media/documents/1_FutureEO_post-CM25_-_Floberghagen.pdf)
5. The Sentinel-2A extension depends on EU funding and needs evidence of added value → EC DG DEFIS → Sentinel-2 STAC metadata (cloud-free obs counts) → [CDSE](https://dataspace.copernicus.eu/news/2026-10-9-sentinel-2a-extension-campaign-continue-until-end-2027)
6. CDSE suffers frequent outages, delays and baseline changes, so operational users cannot tell whether their data are affected → CDSE users (542k registered) → CDSE news feed, STAC → [CDSE news](https://dataspace.copernicus.eu/news)
7. EO processing is hard for non-experts; the openEO Agent defaults to naive methods → CDSE users → openEO + LLM/MCP → [CDSE openEO Agent](https://dataspace.copernicus.eu/news/2026-10-5-openeo-agent-questions-turn-earth-observation-workflow)
8. EO knowledge is scattered across papers and docs ("difficult to find, compare, understand"), and imagery search is not yet in EVE (planned 2027) → policymakers, public → EVE (HF), CDSE, JAXA Earth MCP → [ESA EVE](https://www.esa.int/Applications/Observing_the_Earth/FutureEO/Introducing_ESA_s_Earth_Virtual_Expert)
9. Earthquake building-damage mapping is manual and slow → International Charter, CEMS → Charter archive via EOTDL, Sentinel-1/2, NISAR → [Φ-lab](https://philab.esa.int/a-bold-new-chapter-for-ai4eo-with-esa-%cf%86-lab-challenges/)
10. Disaster mapping cannot keep up with data volume ("impossible… to assess all available data visually") → rescue forces, aid orgs → multi-modal EO → [LPS25 B.04.05](https://lps25.esa.int/sessions/)
11. Charter activations are rising (63 → 85/yr) and human interpretation is the bottleneck → Charter project managers → open pre/post imagery → [Charter 24th report (search)](https://disasterscharter.org/news/24th-annual-report-of-the-charter)
12. Flood products exist but no ML-ready archive does; model evaluation is ad hoc → ECMWF/GloFAS → GFM, VIIRS, Kuro Siwo, Sentinel-1 → [Code for Earth #20](https://github.com/ECMWFCode4Earth/Challenges_2026/issues/2)
13. No systematic evaluation of whether forecasts flagged past East African floods → ICPAC, disaster managers → IFS ENS (AWS), CMORPH, IMERG, EM-DAT → [Code for Earth #41](https://github.com/ECMWFCode4Earth/Challenges_2026/issues/16)
14. Live flood event (EMSR935 Alicante–Valencia, Oct 2026) needs fast, cloud-free mapping → CEMS, Spanish civil protection → Sentinel-1 C/D, Sentinel-2, MTG → [CEMS](https://emergency.copernicus.eu/)
15. Wildfire alerts are delayed by downlinks and ground processing → fire services → Φsat-2-style onboard AI; Sentinel-2/3, VIIRS → [InCubed](https://incubed.esa.int/eight-new-earth-observation-based-wildfire-applications-co-funded-by-esa-incubed/)
16. Fire-danger indices ignore fuel properties and moisture → fire agencies (Spain, Canada) → Sentinel-2 LFMC proxies, Sentinel-1, ERA5 → [InCubed](https://incubed.esa.int/eight-new-earth-observation-based-wildfire-applications-co-funded-by-esa-incubed/)
17. No public satellite covers the late-afternoon peak burn period → Canadian fire managers → GOES ABI, VIIRS, SLSTR → [CSA WildFireSat](https://www.asc-csa.gc.ca/eng/satellites/wildfiresat/default.asp)
18. Satellite downlink is the bottleneck; satellites should decide what to send or task → ESA Φ-lab, EOVC → Sentinel-2, Φsat-2 L1 → [Φ-lab EOVC](https://philab.esa.int/esa-%cf%86-lab-calls-for-collaborators-to-expand-the-earth-observation-virtual-constellation/)
19. Geospatial foundation models are "confidently wrong" in unfamiliar places, which is dangerous in disasters → responders, model users → SHRUG-FM code, flood/burn/landslide sets → [Φ-lab SHRUG-FM](https://philab.esa.int/shrug-fm-wins-best-paper-award-at-the-earthvision-2026-workshop/)
20. GeoFM evaluation is hard and inconsistent → researchers, ESA → PANGAEA, GeoBreeze → [Φ-lab](https://philab.esa.int/a-bold-new-chapter-for-ai4eo-with-esa-%cf%86-lab-challenges/); [LPS25 D.02.29](https://lps25.esa.int/sessions/)
21. Foundation-model adoption is blocked by cost and the domain gap → NGOs, humanitarian orgs → TerraMind, Prithvi, embeddings → [LPS25 D.02.21](https://lps25.esa.int/sessions/)
22. Labelling is a key bottleneck for EO deep learning → all EO-AI users → active learning on Sentinel-2 → [LPS25 D.02.27](https://lps25.esa.int/sessions/)
23. Building and vegetation height maps are lacking globally (also needed for radio propagation) → ITU, urban planners, DRR → embeddings (AlphaEarth, TerraMind) → [Φ-lab GeoFM](https://platform-challenges.philab.esa.int/geoai)
24. CAMS air quality (~10–40 km) is too coarse for health exposure → health agencies, cities → CAMS, S5P, EEA stations → [Φ-lab AQ challenge](https://platform-challenges.philab.esa.int/air-quality-and-health)
25. Hourly GEO air-quality data (Sentinel-4) is a new regime that users are not ready for → CAMS, AQ agencies → Sentinel-4 L2, TROPOMI → [EUMETSAT/DLR](https://www.dlr.de/en/eoc/latest/news/2025/copernicus-sentinel-4-delivers-first-images-of-air-quality-over-europe)
26. EU Ambient Air Quality Directives have monitoring gaps → member-state regulators → S5P, Sentinel-4, CAMS → [LPS25 F.04.29](https://lps25.esa.int/sessions/)
27. National and regional anthropogenic CO2/CH4 estimates are too uncertain; CO2M is delayed to 2027 → EU, UNFCCC → OCO-2/3, TROPOMI, EMIT, GOSAT-GW → [LPS25 C.03.10](https://lps25.esa.int/sessions/); [ESA CO2M MAG](https://missionadvice.esa.int/?p=760)
28. EU ETS and CBAM create GHG-monitoring demand before EO is in the regulation → compliance teams, EO firms → TROPOMI, EMIT, Sentinel-2 methane → [LPS25 E.05.02](https://lps25.esa.int/sessions/)
29. GOSAT-GW L2 will not be public until spring 2027 → GHG researchers → TANSO-3 L1B, TROPOMI → [MOE Japan](https://www.env.go.jp/en/press/press_02489.html)
30. GHG monitoring must move from research to operations → CEOS/CGMS, inventory agencies → GHG L2 products → [LPS25 F.04.26](https://lps25.esa.int/sessions/)
31. EUDR needs traceable plot-level evidence of no deforestation after Dec 2020 → importers, competent authorities → Sentinel-2, Hansen/GFW, JRC forest maps, Whisp → [LPS25 F.04.20/E.05.01](https://lps25.esa.int/sessions/)
32. Brazil's PRODES/DETER do not say whether clearing is legal → IBAMA, prosecutors, buyers → DETER/PRODES (CC BY-SA), CAR registry → [INPE](https://www.gov.br/inpe/pt-br/assuntos/ultimas-noticias/brasil-alcanca-menores-taxas-de-desmatamento-da-serie-historica-na-amazonia-e-no-cerrado)
33. Short-term risk forecasting of deforestation, degradation and fire is missing, with a very strong El Niño ahead → INPE, IBAMA → DETER history, ECMWF seasonal, roads → [INPE SIM-Biomas](https://www.gov.br/inpe/pt-br/assuntos/ultimas-noticias/inpe-recebera-apoio-do-fundo-amazonia-para-aprimorar-monitoramento-ambiental)
34. Brazil's burned-area mapping is at 1 km outside the Cerrado → INPE, fire managers → Sentinel-2, Landsat (30 m) → [INPE SIM-Biomas](https://www.gov.br/inpe/pt-br/assuntos/ultimas-noticias/inpe-recebera-apoio-do-fundo-amazonia-para-aprimorar-monitoramento-ambiental)
35. The Cerrado (MATOPIBA, 74% of loss) is now the bigger clearing frontier → Brazil gov, soy buyers → PRODES Cerrado, Sentinel-2 → [INPE](https://www.gov.br/inpe/pt-br/assuntos/ultimas-noticias/brasil-alcanca-menores-taxas-de-desmatamento-da-serie-historica-na-amazonia-e-no-cerrado)
36. Environmental crime is growing 5–7%/yr, and EO evidence faces legal-admissibility hurdles → police, prosecutors (EU Env. Crime Directive) → Sentinel-1/2, VHR → [LPS25 F.04.11](https://lps25.esa.int/sessions/)
37. Illegal landfills and waste dumping → municipalities, EU enforcement → Sentinel-2, VHR → [CASSINI winners (WasteNoTime)](https://www.cassini.eu/hackathons/portfolio); [LPS25 F.04.11](https://lps25.esa.int/sessions/)
38. High-seas MPAs under BBNJ cannot be enforced without monitoring → MPA managers, NGOs → Sentinel-1 ship detection, AIS → [LPS25 F.04.33](https://lps25.esa.int/sessions/)
39. Arctic shipping in sea ice needs safety and sovereignty awareness → Canada, Arctic states → Sentinel-1 C/D, AMSR2/AMSR3, AIS → [Canada.ca RCM](https://www.canada.ca/en/space-agency/news/2026/06/minister-joly-announces-688m-to-strengthen-canadas-sovereign-satellite-capacity-with-radarsat-constellation-mission-replenishment-satellite.html)
40. Automated sea-ice charting → ice services → Sentinel-1, AutoICE data → [Φ-lab AutoICE](https://challenges.philab.esa.int/)
41. AI4EO under-serves cryosphere and polar science → polar scientists → Sentinel-1, CryoSat-2 → [LPS25 D.02.02](https://lps25.esa.int/sessions/)
42. The RCM continuity gap lasts until the early-2030s replacement → Canadian federal departments → Sentinel-1 as fallback → [Canada.ca](https://www.canada.ca/en/space-agency/news/2025/12/government-of-canada-invests-47-million-to-secure-access-to-essential-canadian-earth-observation-data.html)
43. Two PSLV failures (EOS-09, EOS-N1) left Indian SAR/EO gaps → India NDMA, ISRO → Sentinel-1, NISAR → [Wikipedia PSLV-C61](https://en.wikipedia.org/wiki/PSLV-C61)
44. NISAR products are provisional and validated only at limited sites → NASA/ISRO, users → NISAR GUNW/GCOV, Sentinel-1, GNSS → [NASA Earthdata](https://www.earthdata.nasa.gov/news/nisar-l-band-data-released-expanding-record-surface-changes)
45. Field-scale thermal data are only monthly or at 1 km, which hurts irrigation efficiency → farmers, water agencies → Landsat TIRS, ECOSTRESS, SLSTR → [CNES TRISHNA](https://cnes.fr/en/projects/trishna)
46. Irrigation uses about 70% of freshwater; ET and root-zone soil moisture products are needed → water managers → Sentinel-2/3, C3S → [LPS25 B.03.16](https://lps25.esa.int/sessions/)
47. Water scarcity affects more than 40% of people; lake volumes and levels are poorly monitored → water agencies → Sentinel-3/6 altimetry, SWOT, Sentinel-2 → [LPS25 F.04.05](https://lps25.esa.int/sessions/); [CNES SWOT](https://cnes.fr/en/projects/swot)
48. Plant stress is seen too late by greenness indices; FLEX is not yet producing data → agriculture, food security → TROPOMI SIF, OLCI, FLEX later → [ESA FLEX](https://www.esa.int/Applications/Observing_the_Earth/FLEX_and_Sentinel-3C_launched)
49. Record European heat and drought in 2026 → C3S, farmers, utilities → ERA5, Sentinel-2/3, SMAP/SMOS → [C3S](https://climate.copernicus.eu/)
50. Volcanic-ash "grey zone": the lidar cannot see through thick sulphate and the radar cannot see fine ash, so aircraft are told "do not fly" → VAACs, airlines → EarthCARE ATLID/CPR/MSI, S5P SO2, Himawari → [ESA EarthCARE](https://www.esa.int/Applications/Observing_the_Earth/FutureEO/EarthCARE/EarthCARE_s_view_of_volcanic_plume_boosts_air_safety)
51. Pyrocumulonimbus (fire clouds) are becoming more common in Europe → aviation, fire services → EarthCARE, MTG FCI → [ESA Observing the Earth](https://www.esa.int/Applications/Observing_the_Earth)
52. AI weather (AIFS) runs at 31 km and still relies on physics-based data assimilation → NWP centres, local forecasters → AIFS/IFS open data (CC-BY), ERA5 → [ECMWF](https://www.ecmwf.int/en/about/media-centre/news/2025/ecmwfs-ensemble-ai-forecasts-become-operational)
53. AI NWP models are too heavy to run on edge devices in Africa → African NMHSs → AIFS/Anemoi → [Code for Earth #40](https://github.com/ECMWFCode4Earth/Challenges_2026/issues)
54. Weather and climate data volume is huge (ECMWF grows ~287 TB/day; DHS 510 PB primary) → ECMWF, DestinE → [ECMWF DHS](https://www.ecmwf.int/en/computing/our-facilities/data-handling-system)
55. "Data output and storage have already become a major bottleneck for high-resolution climate modeling" → DestinE, climate modellers → [LPS25 D.02.06](https://lps25.esa.int/sessions/)
56. DestinE twin data are limited to "European actors" and raw twin output is not AI-ready (hence DEFAIR) → non-EU and SME users → DestinE platform → [DestinE](https://platform.destine.eu/)
57. Sentinel processors are a decade old and must be re-engineered for cloud-native Zarr → ESA EOPF → [LPS25 D.05.03](https://lps25.esa.int/sessions/)
58. EO uptake is limited by a fragmented service landscape, no scaling or funding path, and access barriers (the "long tail of users") → ESA, EO industry → [LPS25 E.01.07](https://lps25.esa.int/sessions/)
59. End users do not know EO can help, and they want answers "through known, common interfaces" → European public and private users → [LPS25 E.03.02](https://lps25.esa.int/sessions/)
60. Global ARD is not tailored to local problems → local governments, communities → CEOS-ARD, DE Africa → [LPS25 B.01.03](https://lps25.esa.int/sessions/)
61. The EO industry does not understand how development banks procure, so EO is missing from development finance → ESA GDA, World Bank, ADB → [LPS25 B.01.07](https://lps25.esa.int/sessions/)
62. Climate adaptation must be monitored by every UNFCCC Party by 2030, and EO's role is barely explored → national governments → C3S, Sentinel → [LPS25 B.03.02](https://lps25.esa.int/sessions/)
63. SDG data gaps in low-income countries → National Statistical Offices, UN → DE Africa, Sentinel → [LPS25 F.04.30](https://lps25.esa.int/sessions/)
64. The Nature Restoration Regulation (20% by 2030) has data gaps and inconsistent baselines → EU member states → CLMS, Sentinel-2, Biomass → [LPS25 F.04.23](https://lps25.esa.int/sessions/)
65. The Global Ecosystems Atlas is 23% unmapped, and ambiguous licences undermine it → GEO, CBD parties → embeddings, Sentinel → [Global Ecosystems Atlas](https://www.globalecosystemsatlas.org/)
66. In-situ climate networks lack long-term funding, which threatens cal/val → GCOS, ESA CCI → [LPS25 B.01.05](https://lps25.esa.int/sessions/)
67. Ageing satellites far past design life (TerraSAR-X 19 yrs vs 5; SMOS 16+; CryoSat 15+) put climate records at risk → ESA, DLR, CCI → mission metadata → [DLR](https://www.dlr.de/en/research-and-transfer/projects-and-missions/terrasar-x); [ESA slides](https://climate.esa.int/media/documents/1_FutureEO_post-CM25_-_Floberghagen.pdf)
68. Europe needs sovereign, guaranteed, fast-revisit VHR for crises (ERS-EO / EOGS) → EU, member states, defence → national and commercial constellations, Sentinel → [ESA slides](https://climate.esa.int/media/documents/1_FutureEO_post-CM25_-_Floberghagen.pdf)
69. Dependence on US instruments and data (NASA radiometer, Landsat, SOTR mask) is a sovereignty risk → ESA, EU, Canada → European, Japanese and Indian open data → [ESA slides](https://climate.esa.int/media/documents/1_FutureEO_post-CM25_-_Floberghagen.pdf)
70. The disease–environment link (dengue, malaria habitats) is hard to predict → health ministries → WOfS, Sentinel-1/2, ERA5 → [LPS25 B.03.06](https://lps25.esa.int/sessions/); [DE Africa](https://www.digitalearthafrica.org/)
71. Fragmented national space laws (13 regimes), debris and cyber risks → EU operators → TLEs, CDMs → [EC EU Space Act](https://defence-industry-space.ec.europa.eu/eu-space-act_en)
72. A 1-day Sentinel-1C/1D repeat window (Apr–Jun 2026) is an unexploited unique dataset → InSAR scientists → CDSE Sentinel-1 → [CDSE](https://dataspace.copernicus.eu/news/2026-4-2-sentinel-1d-user-data-opening-and-future-plans)
73. Sentinel-1D clock-corruption data (29 May – 1 Jun 2026) may silently contaminate pipelines → S1 users → CDSE metadata → [CDSE](https://dataspace.copernicus.eu/news/2026-6-4-sentinel-1d-sar-data-quality-degradation)
74. Contributing-mission VHR data are restricted to eligible EU users → non-EU/NGO users → open Maxar/Umbra/Capella programmes → [LPS25 C.03.23](https://lps25.esa.int/sessions/)
75. Persistent contrails have climate impact → INPE, ICCT, airlines → MTG/GOES, ERA5 humidity → [INPE](https://www.gov.br/inpe/pt-br/assuntos/ultimas-noticias/inpe-e-icct-lancam-projeto-pioneiro-para-monitorar-o-impacto-climatico-de-trilhas-de-condensacao-de-aeronaves-no-brasil)
76. Hyperspectral readiness for CHIME (crop nutrients, minerals, critical raw materials) → farmers, mining due diligence → EnMAP ARD, PRISMA, EMIT → [EnMAP](https://www.enmap.org/); [LPS25 C.03.03](https://lps25.esa.int/sessions/)
77. Grassland and drought productivity monitoring → farmers, CAP → Sentinel-1/2, MODIS → [LPS25 B.02.10/E.01.10](https://lps25.esa.int/sessions/)
78. Policy makers find EO science not "actionable" → science-policy interface → [LPS25 F.04.24](https://lps25.esa.int/sessions/)
79. The tropics are cloud-covered, and optical revisit is insufficient (the reason 2A was extended) → tropical monitoring → Sentinel-1, Sentinel-2 three-satellite → [CDSE](https://dataspace.copernicus.eu/news/2025-2-28-sentinel-2a-extended-campaign-starting-march-13-2025)
80. A national PPP EO constellation (India) and IRIDE (Italy) have unclear open-data policies → researchers, SMEs → (TBD) → [The Machine Maker](https://themachinemaker.com/news/private-consortium-selected-to-develop-indias-first-national-earth-observation-satellite-network/); [ESA IRIDE](https://www.esa.int/Applications/Observing_the_Earth/IRIDE/Italy_s_IRIDE_completes_Eaglet_II_constellation)

---

## 22. Cross-slice leads

- **US agencies:**
  - The Sentinel-6C stall is tied to "availability of the NASA radiometer" ([ESA slides](https://climate.esa.int/media/documents/1_FutureEO_post-CM25_-_Floberghagen.pdf)).
  - The Biomass acquisition mask is due to the US Space Object Tracking Radar ([EO College](https://eo-college.org/?p=388510)).
  - NISAR L-band release on ASF (Jul 2026); DEA and DE Africa depend on Landsat.
  - A NASA–Japan Tokyo GHG field campaign (Mar 2026) validated GOSAT-GW.
- **SpaceX / orbital compute:**
  - Sentinel-6B launched on Falcon 9; MBZ-SAT on Falcon 9.
  - IRIS² (348 satellites) is the EU's Starlink answer.
  - The openEO Agent on CDSE runs on Claude Sonnet 5 via MCP; EVE is Mistral-based. Both are examples of "LLM over EO archives".
  - The Φ-lab EOVC multi-agent tasking concept and onboard foundation models (InCubed FIREWISE) relate to orbital compute.
  - ESA's first quantum computer (Jul 2026).
- **Space traffic, debris, weather:**
  - EU Space Act (debris, trackability, cyber) and Sentinel-1A disposal "under consolidation".
  - Kelvins Collision Avoidance, spotGEO and debris-origin datasets.
  - UK £25M space surveillance radar contract (Jul 2027) ([European Spaceflight](https://europeanspaceflight.com/uk-to-award-25m-space-surveillance-radar-contract-in-july-2027/)).
  - ESA 4D Ionosphere workshop (20–22 Oct 2026); MetOp-SG RO ionosphere data; LPS25 A.06 geospace sessions.
  - The CASSINI #12 cybersecurity challenge (GNSS spoofing).
- **China:**
  - CBERS (China–Brazil) imagery was used for Charter activations (2026).
  - The Nepal–Tibet glacial-collapse disaster (Aug 2026).
- **EO companies:**
  - IN-SPACe EO-PPP (Pixxel, SatSure, PierSight, Dhruva).
  - OroraTech as a Copernicus Contributing Mission; constellr (InCubed thermal).
  - IRIDE builders OHB Italia and Argotec; MDA CHORUS for RCM.
  - EARSC: European EO revenue €2.66 bn (+9.16%), driven by defence.
- **EO analytics and industry:**
  - InCubed wildfire projects (GEOAI Analytics, Multiverse, ARQUIMEA, isardSAT, Telespazio, Airbus, Agresta).
  - The Forest Data Partnership's Whisp (EUDR).
  - GTIF (Green Transition Information Factories) and the GDA APP.
- **Datasets catalogue:**
  - CDSE (91 PB online; 242 PB delivered in 2025).
  - JAXA Earth API (COG/STAC, MCP).
  - TerraBrasilis (CC BY-SA).
  - ECMWF open data (CC-BY-4.0, IFS at 0.1° from 20 Oct 2026; the IFS ENS archive >1 PB on AWS).
  - Kuro Siwo, Major TOM (Core-S2L2A ~23 TB; 51 TB of embeddings), ClearSAR, EOTDL.
  - The DE Africa sandbox.
  - NISAR on ASF; EnMAP ARD.
  - Global Ecosystems Atlas API.
- **Models and tools:**
  - TerraMind (IBM–ESA), EVE (Φ-lab LLM), SHRUG-FM, PANGAEA, GeoBreeze, TorchGeo.
  - The openEO Agent; Anemoi/AIFS; CoMet uncertainty toolkit (LPS25 D.03.09).
  - The ImpactMesh flood and wildfire fine-tunes.
- **Space science and literature:**
  - EVE's corpus (ESA, NASA, Copernicus, Wiley).
  - LPS25's 4,200+ presentations are online ([LPS25](https://lps25.esa.int/lps25-presentations/)), a mineable literature corpus.
  - Lunar X-view (Kelvins) for planetary navigation.

---

## 23. Leads not followed (or not verified), with reasons

1. **OSIP campaign list:** ideas.esa.int needs a login. The EO-specific 2025–26 campaigns are unverified.
2. **Copernicus Masters 2025/2026:** the site's TLS certificate had expired. Whether the competition still runs is unknown.
3. **EU Space Act legislative progress (EP ITRE / Council positions, 2026), application date and US/industry reactions:** the EC page lacks detail and EUR-Lex and the press corner did not render. The shared search budget was exhausted.
4. **International Charter 2025 activation count and 25th annual report:** disasterscharter.org returned 404/500 errors and timeouts.
5. **CEMS rapid-mapping annual statistics and lessons learned from the Valencia DANA (2024) and the Oct 2026 EMSR935 event:** not opened.
6. **CMEMS, CLMS and C3S service-specific pain points** (e.g., ERA5 latency, EGMS update cadence): only landing pages were checked.
7. **TRUTHS status after the UK's reduced CM25 subscription:** absent from the March 2026 "secured" list. Not confirmed either way.
8. **UKSA merger into DSIT:** reported plans not verified (the gov.uk page was ambiguous).
9. **TerraSAR-X / TanDEM-X successor (TSX-NG / HRWS) and COSMO-SkyMed Second Generation status:** not checked.
10. **India's 2025 geospatial / remote-sensing data policy specifics** (free resolution thresholds, Bhuvan/Bhoonidhi open-data changes): search budget exhausted; the IN-SPACe site is JavaScript-only.
11. **Oceansat-3 / EOS-06 and Cartosat data access terms:** not checked.
12. **KARI CAS500-2, KOMPSAT-6 and Korean data policy; UAE Sirb SAR constellation:** not verified.
13. **Himawari-10 schedule and NOAA/AWS Himawari mirror:** not verified.
14. **EUMETSAT MTG data volumes, Lightning Imager and IRS user readiness:** eumetsat.int returned HTTP 403.
15. **DestinE data volumes (PB/day) and Climate DT Gen 2 resolution:** not on the pages opened.
16. **Φ-lab Grand Marathon 2025–26 winners (Hello Tomorrow, Jun 2026) and ClearSAR official winners:** not found.
17. **ESA Φsat-2 extension decision and final results:** March 2026 slides say operations end in March 2026, while CEOS slides propose an extension. Unresolved.
18. **European statements reacting to proposed US FY2026 NASA/NOAA Earth-science cuts:** not found on this pass (mostly the US slice).
19. **IRIS² 2026 "accelerating and reinforcing" package (EC ip_26_1726):** text not read.
20. **The MFF 2028–2034 Copernicus line and the ROSE-L budget:** no Copernicus-specific figure found.
21. **LinkedIn and X posts by ESA staff (e.g., Josef Aschbacher):** none surfaced on this pass because of the search budget. Only one LinkedIn post (ClearSAR winner claim) appeared and it is unverified.
22. **Euroconsult EO market reports and SpaceNews Europe coverage:** not reached because of the search budget.
23. **ECMWF Code for Earth 2026 final results:** challenge pages read, outcomes not checked.
24. **MTG-I2 launch status (planned Q3 2026):** not confirmed by Oct 2026.
25. **GOSAT-GW L1B public release (planned from 23 Jul 2026):** not confirmed.

---

## Entry count

Main-body entries (sections 1–19): 1.1–1.7 (7), 2.1–2.5 (5), 3.1 (1), 4.1–4.3 (3), 5 (1), 6.1–6.5 (5), 7.1 (1), 8.1–8.3 (3), 9.1–9.6 (6), 10.1–10.2 (2), 11.1–11.4 (4), 12.1–12.4 (4), 13.1–13.5 (5), 14.1–14.2 (2), 15.1–15.2 (2), 16.1–16.4 (4), 17.1–17.2 (2), 18.1–18.2 (2), 19.1–19.5 (5) = **64 entries**. Plus 42 challenge-table rows and 80 problem-bank items.
