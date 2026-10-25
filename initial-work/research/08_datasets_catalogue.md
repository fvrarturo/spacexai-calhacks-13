# Large public space datasets: catalogue and fast-access guide

**Scope:** large public datasets *about* space and *from* space (Earth observation, atmosphere, orbital objects, astronomy, heliophysics, planetary, mission engineering, literature), and how to reach each one from a laptop within an hour. Built for the Cal Hacks 13.0 "Make it Legendary" challenge.

**Researched on 2026-10-24.** Live checks (HTTP calls to STAC/TAP/REST endpoints, bucket listings, Hugging Face Hub API, PyPI) were made on that date and are marked "checked live 2026-10-24".

Section 2.3 (ML benchmarks) is a summary; the full benchmark catalogue is in [`08b_ml_benchmark_datasets.md`](08b_ml_benchmark_datasets.md).

## 1. Quick-pick table

"Time" is time-to-first-data on a laptop with decent Wi-Fi. ★ marks the best hackathon picks (fast, no or instant auth, clear problem).

| Dataset | Category | Size | Access | Auth | Time |
|---|---|---|---|---|---|
| ★ Sentinel-2 L2A COGs | EO imagery | PB (query by AOI) | Earth Search / PC STAC | no | min |
| ★ Sentinel-1 RTC | EO imagery (SAR) | PB | PC `sentinel-1-rtc` | no | min |
| Sentinel-1 SLC / bursts / global mosaics | EO imagery (SAR) | PB | CDSE STAC/S3 | free account | 15 min |
| Landsat Collection 2 | EO imagery | PB | PC / Earth Search; `s3://usgs-landsat` (requester-pays) | no / AWS | min |
| HLS v2.0 (L30/S30, VI) | EO imagery | PB | PC `hls2-*`; earthaccess | no / Earthdata | min |
| OPERA DSWx / DIST / RTC / DISP | EO derived (NASA) | TB–PB | earthaccess | Earthdata | 15–30 min |
| MODIS 061 / VIIRS | EO imagery | PB | PC `modis-*`; CDSE; `s3://noaa-nesdis-n20-pds` | no | min |
| Black Marble VNP46 / Light Every Night | Night lights | TB | earthaccess; `s3://globalnightlight` | Earthdata / no | 15 min |
| NAIP | Aerial imagery (US) | TB | PC `naip` | no | min |
| Copernicus DEM GLO-30/90 | Elevation | ~TB (1° COG tiles) | `s3://copernicus-dem-30m` | no | min |
| ALOS PALSAR mosaics | SAR mosaics | TB | PC `alos-palsar-mosaic` | no | min |
| Sentinel-3 / Sentinel-6 | Ocean/land | PB | CDSE | free account | 15 min |
| ★ Vantor Open Data (2026 events) | Commercial VHR | GB per event | `s3://vantor-opendata/events/` | no (CC BY-NC) | min |
| Maxar Open Data (56 events) | Commercial VHR | GB per event | `s3://maxar-opendata/events/` | no (CC BY-NC) | min |
| ★ Umbra SAR Open Data | Commercial SAR | GB–TB | `s3://umbra-open-data-catalog` | no | min |
| Capella / ICEYE SAR open data | Commercial SAR | GB–TB | `s3://capella-open-data`, `s3://iceye-open-data-catalog` | no | min |
| Satellogic EarthView | Commercial 1 m | TB | `s3://satellogic-earthview` | no | min |
| SpaceEye-T VVHR open data | Commercial VHR | GB | `s3://st-vvhr-opendata` | no | min |
| NISAR (Beta/Provisional) | SAR (new) | GB per granule | ASF / earthaccess | Earthdata | 30–60 min |
| SWOT HR rivers/lakes | Hydrology | GB | earthaccess | Earthdata | 15–30 min |
| EMIT (incl. CH4 plumes) | Hyperspectral | TB | earthaccess | Earthdata | 15–30 min |
| PACE OCI | Ocean colour | TB | earthaccess | Earthdata | 15–30 min |
| GEDI / ICESat-2 | Lidar | TB | earthaccess | Earthdata | 30 min |
| ECOSTRESS LST | Thermal | TB | earthaccess | Earthdata | 15–30 min |
| ESA Biomass | P-band SAR (new) | n/a | ESA portal | registration | hours |
| ESA WorldCover | Land cover | ~TB | `s3://esa-worldcover` | no | min |
| Dynamic World | Land cover (NRT) | PB | Earth Engine | EE project | 20 min |
| ★ Open buildings (VIDA: Google+MS+OSM) | Buildings | 2.7B footprints | `data.source.coop/vida/...` GeoParquet | no | min |
| ★ Overture Maps 2026-10-21.0 | Places/buildings/roads | TB | `s3://overturemaps-us-west-2/release/` | no | min |
| JRC Global Surface Water | Water | TB | PC `jrc-gsw` | no | min |
| Hansen GFC v1.13 (to 2025) | Forest loss | TB | GCS `earthenginepartners-hansen` | no | min |
| ★ NASA FIRMS active fires | Fire | 11 MB/day CSV | public 24h CSV; API with MAP_KEY | no / free key | <2 min |
| GHSL / Meta HRSL | Population/built-up | TB | `s3://jrc-ghsl`, `s3://dataforgood-fb-data/hrsl-cogs` | no | min |
| ★ Climate TRACE v7 | Emissions | API | `api.climatetrace.org/v7` | no | min |
| ★ Carbon Mapper plumes | Methane/CO2 | 45,539 plumes | `api.carbonmapper.org` | no (catalog) | min |
| UNEP IMEO MARS-S2L | Methane ML | 96 GB | HF | no (CC BY-NC-SA) | min |
| CEMS rapid mapping | Disaster maps | per activation | dashboard API | no | 15 min |
| MS AI for Good 2026 quake damage | Damage | small | PC `predicted-damage-*-2026` | no | min |
| ★ AlphaEarth Satellite Embeddings 2017–2025 | Embeddings | TB | EE / `data.source.coop/tge-labs/aef` | no / EE | min |
| TESSERA / Clay embeddings | Embeddings | TB | `s3://tessera-embeddings`, Source | no | min |
| Meta canopy height v2 / CTrees AGB | Forest carbon | TB | `s3://dataforgood-fb-data/forests/v2/...`, `s3://ctrees-agb-100m-global` | no | min |
| EO ML benchmarks (~120) | ML benchmarks | MB–TB | see `08b_ml_benchmark_datasets.md` | mostly no | min–hours |
| ★ ARCO-ERA5 | Reanalysis | 100s TB (Zarr) | `gs://gcp-public-data-arco-era5/ar/` | no | min |
| ERA5 via CDS API | Reanalysis | 100s TB | `cdsapi` | free account + licence | 15 min |
| ★ WeatherBench 2 | AI weather | TB (Zarr) | `gs://weatherbench2/datasets/` | no | min |
| ECMWF open data | Forecasts | GB/day | `ecmwf-opendata` | no | min |
| ★ GOES-18/19 ABI/GLM | Weather sat | PB | `s3://noaa-goes19` | no | min |
| Himawari-9 / GK-2A / GMGSI | Weather sat | PB | `s3://noaa-himawari9` and others | no | min |
| GPM IMERG | Precipitation | TB | `s3://dynamical-nasa-imerg` (Zarr) | no | min |
| Sentinel-5P TROPOMI | Trace gases | TB | CDSE; `s3://meeo-s5p`; PC | no / account | min |
| TEMPO (NO2, HCHO, O3) | Air quality hourly | TB | earthaccess | Earthdata | 15 min |
| OCO-2/3, OMI NO2 | CO2/NO2 | TB | earthaccess; `s3://omi-no2-nasa` | Earthdata / no | 15 min |
| SEVIR | Storm ML | ~TB | `s3://sevir` | no | min |
| WxC-Bench | Weather ML | 968 GB | HF `nasa-impact/WxC-Bench` | no | min (subset) |
| ★ CelesTrak GP + SATCAT + SOCRATES | Orbits | 7 MB active JSON | `celestrak.org/NORAD/elements/gp.php` | no | <2 min |
| Space-Track (gp_history, CDMs) | Orbits | TB-ish history | API | account | hours |
| ★ HF Space-Track TLE history mirror | Orbits | 12.5 GB / 238M rows | `hf://datasets/juliensimon/space-track-tle-history` | no | min |
| GCAT (McDowell) | Launch/objects | 19 MB satcat.tsv | planet4589.org TSV | no | min |
| ESA DISCOS | Object properties | API | discosweb API | token | 30–60 min |
| Launch Library 2 | Launches | API | `ll.thespacedevs.com/2.3.0` | no | min |
| SatNOGS DB / Network | Telemetry/RF | API | `db.satnogs.org/api` | no | min |
| ★ Kelvins collision-avoidance CDMs | Conjunction ML | 0.22 GB | Zenodo 4463683 | no | min |
| GEO manoeuvres | Orbit ML | 24.5 GB | HF `FraDra/GEO_satellite_maneuvers` | no | min |
| ★ Gaia DR3 (DR4 on 2 Dec 2026) | Astronomy | multi-TB | Gaia TAP; `s3://stpubdata/gaia/...hats` | no | min |
| SDSS DR19/DR20 | Astronomy | TB | SAS / Zora-Valis / SciServer | no | min |
| DESI DR1 | Astronomy | 18.7M spectra | `data.desi.lbl.gov/public/dr1` | no | min |
| ★ Rubin alerts via brokers | Astronomy (time-domain) | millions/night | Fink/ALeRCE/Lasair/ANTARES APIs | no | min |
| Rubin DP1/EDP2 | Astronomy | TB | Rubin Science Platform | data rights only | days |
| ZTF DR24 | Astronomy | 5.32B light curves | IRSA; `s3://ipac-irsa-ztf/...hats` | no | min |
| ★ MAST (TESS, Kepler, HST, JWST, PS1) | Astronomy | PB | `s3://stpubdata`; lightkurve | no | min |
| ★ NASA Exoplanet Archive | Exoplanets | 6,451 planets | TAP | no | <5 min |
| Euclid Q1 (DR1-Foundation Nov 2026) | Astronomy | 35 TB | `s3://nasa-irsa-euclid-q1` | no | min |
| SPHEREx QR2 | Astronomy | growing weekly | `s3://nasa-irsa-spherex/qr2` | no | min |
| WISE / NEOWISE / unWISE | Astronomy/NEO | 10s TB | `s3://nasa-irsa-wise` | no | min |
| GWOSC (GWTC-5.0) | Gravitational waves | 671 event entries; TB strain | gwosc API; HF strain mirrors | no | min |
| Galaxy Zoo (incl. Euclid) | Astronomy labels | GB | HF `mwalmsley/*` | no | min |
| Multimodal Universe | Astro ML | 100 TB | HF previews; Flatiron HTTPS | no | min–hours |
| AstroCLIP data | Astro ML | ~60 GB | HF / Globus | no | ~1 h |
| Chandra Source Catalog 2.2 | X-ray | 432,713 sources | CSCview/CLI | no | min |
| eROSITA-DE DR1 | X-ray | half sky | eRODat | no | min |
| LoTSS-DR3 | Radio | 13.7M sources | lofar-surveys.org | no | min |
| ★ Satellite-streak datasets (StreaksYolo, ASTA, HST trails, HETDEX 2026) | Astro vs. megaconstellations | 0.1–21 GB | Zenodo | no | min |
| ★ HF juliensimon space tables (~200) | Mixed space tabular | kB–12.5 GB | HF Parquet | no | <5 min |
| ★ NOAA SWPC JSON (RTSW now from IMAP) | Space weather | small, real time | `services.swpc.noaa.gov/json` | no | <1 min |
| GFZ Kp API | Space weather | small | `kp.gfz.de/app/json` | no | <1 min |
| ★ Surya Bench / core-SDO | Heliophysics ML | 363 GB (labels MB) | `s3://nasa-surya-bench`; HF | no | min |
| SDOML v2 | Heliophysics ML | TB | `s3://gov-nasa-hdrl-data1/contrib/fdl-sdoml/` | no | 15–30 min |
| GOES-19 CCOR-1 coronagraph | Space weather | 96 files/day/level | `s3://noaa-nesdis-swfo-ccor-1-pds` | no | min |
| WAM-IPE thermosphere density | Space weather/drag | GB/day | `s3://noaa-nws-wam-ipe-pds` | no | min |
| WSA-Enlil runs | CME model | GB | `s3://noaa-wsa-enlil-pds` | no | min |
| OMNI / CDAWeb / DONKI | Heliophysics | GB | cdasws/hapiclient; HF mirrors | no / key | min (HF) |
| ★ JPL SSD APIs (SBDB, CAD, Sentry, Scout, Fireball) | NEOs | 1.58M bodies | `ssd-api.jpl.nasa.gov` | no | <2 min |
| ESA NEOCC risk list | NEOs | ~1,800 rows | text download | no | <1 min |
| MPC orbits (MPCORB) | Asteroids | 94 MB gz | minorplanetcenter.net | no | min |
| Catalina Sky Survey raw | NEO survey | TB | `s3://pds-css-archive` | no | min |
| PDS Search API | Planetary | 92.8M products | `pds.mcp.nasa.gov/api/search/1` | no | min |
| USGS Astrogeology ARD (HiRISE, CTX DTMs, LOLA, Kaguya) | Planetary | TB | STAC; `s3://astrogeo-ard` | no | min |
| ★ NASA Lunar FM Bench (SomBench: craters, ice) | Lunar ML | MB–TB | HF; `s3://nasa-lunar-fm-bench` | no | min |
| Global CTX Mosaic of Mars | Mars imagery | 5.7 Tpx | murray-lab tiles | no (TLS quirk) | min |
| ShadowCam (PSRs) | Lunar | first PDS release Aug 2026 | PDS | no | ~1 h |
| ESA PSA EPN-TAP | Planetary | 39.75M granules | `psa.esa.int/psa-tap` | no | min |
| Mars-Bench / HiRISE landforms / MoonAnything | Planetary ML | 0.2–22 GB | Zenodo | no | min |
| YAOKI lunar rover (IM-2) | Telemetry | small | `s3://im2-yaoki-rover-public` | no | min |
| ★ ESA Anomaly Dataset (ESA-ADB) | Telemetry ML | 11.6 GB | Zenodo 15237121 | no | ~10 min |
| OPSSAT-AD | Telemetry ML | 0.02 GB | Zenodo 15108715 | no | <2 min |
| SMAP/MSL telemanom | Telemetry ML | small | Kaggle mirror | Kaggle | min |
| GOCE telemetry | Telemetry | 45 GB | HF | no | min (subset) |
| ★ NASA LLIS lessons learned | Engineering text | 2,135 lessons | `llis.nasa.gov/llis/lesson/_search` | no | <10 min |
| ★ NTRS | Engineering text | 648,220 records | `ntrs.nasa.gov/api/citations/search` | no | min |
| NASA ADS / SciX | Literature | ~16M+ records | API with token | free token | 10 min |
| arXiv (API / Kaggle / S3) | Literature | 5.6 GB metadata; 9.2 TB full | API; Kaggle; `s3://arxiv` (requester-pays) | no / Kaggle / AWS | min |
| OpenAlex | Literature graph | huge | API (cost-metered) | free key advised | min |
| GCN Circulars | Transient text | 46k circulars, 31.6 MB | archive.json.tar.gz | no | <5 min |
| Astro-LLM corpora (UniverseTBD, AstroMLab, NASA SMD) | Text/benchmarks | MB–GB | HF | no | min |
| Decadal surveys (4) | Policy text | PDFs | nap.edu | no | min |

## 2. Detailed entries

### 2.1 Earth observation imagery archives

Platform STAC listings used below were checked live on 2026-10-24 (see 2.11): Planetary Computer (139 collections), Earth Search (9), CDSE (427), CMR (53,634 collections).

#### Sentinel-2 L2A/L1C (ESA Copernicus): optical, 10–60 m, 13 bands
- **What:** multispectral imagery every ~5 days (2A/2B/2C), bottom-of-atmosphere L2A and top-of-atmosphere L1C. The ESA "Collection-1" reprocessing is exposed separately on Earth Search.
- **Size:** multi-PB global archive since June 2015.
- **Coverage:** global land and coast, 2015 to present.
- **Format:** COG (Earth Search, Planetary Computer); SAFE/JP2 (CDSE).
- **Access:**
  - Earth Search STAC `https://earth-search.aws.element84.com/v1`, collections `sentinel-2-l2a`, `sentinel-2-c1-l2a`, `sentinel-2-l1c`; COGs in `s3://e84-earth-search-sentinel-data` (us-west-2, public).
  - Planetary Computer `sentinel-2-l2a`.
  - CDSE `sentinel-2-l2a`, `sentinel-2-l1c`, plus `sentinel-2-global-mosaics` and `sentinel-2-night-time-acquisitions`.
  - Code: `pip install pystac-client odc-stac` (0.9.1 / 0.5.3).
- **Auth:** no (Earth Search, PC); a free account for CDSE. The old `s3://sentinel-s2-l1c` is requester-pays.
- **License:** Copernicus free, full and open.
- **Time to first data:** minutes.
- **Hackathon problem:** illegal-mining or deforestation change detection; flood extent; crop stress; methane-flare night lights (night-time acquisitions).
- **Sources:** [Earth Search STAC (live)](https://earth-search.aws.element84.com/v1/collections), [AWS registry Sentinel-2 COGs](https://registry.opendata.aws/sentinel-2-l2a-cogs/), [CDSE STAC (live)](https://stac.dataspace.copernicus.eu/v1/collections), [PC STAC (live)](https://planetarycomputer.microsoft.com/api/stac/v1/collections)

#### Sentinel-1 (C-band SAR): GRD, RTC, SLC, bursts, OCN, global mosaics
- **What:** all-weather, day/night radar every 6–12 days (1A, plus 1C launched Dec 2024).
- **Size:** multi-PB.
- **Coverage:** global, 2014 to present.
- **Format:** COG (RTC), SAFE.
- **Access:**
  - PC `sentinel-1-grd` and **`sentinel-1-rtc`** (terrain-corrected, CC BY 4.0, easiest).
  - Earth Search `sentinel-1-grd`.
  - CDSE `sentinel-1-grd`, `sentinel-1-slc`, `sentinel-1-slc-burst`, `sentinel-1-ocn`, `sentinel-1-global-mosaics`, `sentinel-1-etad`.
  - ASF DAAC via `pip install asf-search` (14.1.0); ASF S3 for Sentinel-1A SLC/GRD is `s3://asf-ngap2w-p-s1-slc-7b420b89` / `s3://asf-ngap2w-p-s1-grd-7d1b4348` (Earthdata, in-region).
  - Precise orbits: `s3://s1-orbits` (public).
  - Seasonal coherence: `s3://sentinel-1-global-coherence-earthbigdata/data/tiles` (public).
- **Auth:** no (PC, Earth Search); Earthdata Login (ASF); CDSE account.
- **License:** Copernicus open (PC RTC: CC BY 4.0).
- **Time to first data:** minutes (PC RTC).
- **Hackathon problem:** flood mapping through clouds; dark-vessel detection; landslide and subsidence monitoring (with OPERA DISP).
- **Sources:** [PC STAC (live)](https://planetarycomputer.microsoft.com/api/stac/v1/collections), [CDSE STAC (live)](https://stac.dataspace.copernicus.eu/v1/collections), [AWS registry s1-orbits](https://registry.opendata.aws/s1-orbits/), [AWS registry global coherence](https://registry.opendata.aws/ebd-sentinel-1-global-coherence-backscatter/), [PyPI asf-search](https://pypi.org/project/asf-search/)

#### Landsat Collection 2 (USGS/NASA): L1 and L2 surface reflectance and temperature, 30 m
- **What:** 50+ years of moderate-resolution imagery (Landsat 4–9).
- **Size:** multi-PB.
- **Coverage:** global, Landsat-level data from 1982 on Earth Search `landsat-c2-l2`; Landsat 9 since 2021.
- **Format:** COG.
- **Access:** **requester-pays** `s3://usgs-landsat/collection02/` (us-west-2); free mirrors PC `landsat-c2-l1` / `landsat-c2-l2`, Earth Search `landsat-c2-l2`, CDSE `landsat-c2-l1-*`.
- **Auth:** none on PC; AWS credentials plus egress for the USGS bucket.
- **License:** "no restrictions on Landsat data."
- **Time to first data:** minutes.
- **Hackathon problem:** decades-long urban heat or glacier retreat; the continuity question (Landsat Next gap).
- **Sources:** [AWS registry USGS Landsat](https://registry.opendata.aws/usgs-landsat/), [Earth Search STAC (live)](https://earth-search.aws.element84.com/v1/collections)

#### HLS v2.0 (Harmonized Landsat Sentinel-2), plus vegetation indices
- **What:** NASA-harmonised 30 m surface reflectance from Landsat 8/9 and Sentinel-2A/2B/2C, giving a ~2–3 day revisit.
- **Size:** PB-scale.
- **Coverage:** global land, 2013 to present (PC from 2020).
- **Format:** COG.
- **Access:** CMR short names `HLSL30`, `HLSS30`, `HLSL30_VI`, `HLSS30_VI` (all cloud-hosted, checked live); `s3://lp-prod-protected/HLSL30.020`, `.../HLSS30.015` (Earthdata, in-region); PC `hls2-l30`, `hls2-s30` (no login); `earthaccess.search_data(short_name="HLSL30")`.
- **Auth:** Earthdata Login (LP DAAC) or none via PC.
- **License:** CC BY 4.0 (registry).
- **Time to first data:** minutes via PC.
- **Hackathon problem:** a field-level crop-failure early warning; burn-scar mapping.
- **Sources:** [AWS registry NASA HLS](https://registry.opendata.aws/nasa-hls/), [CMR (live)](https://cmr.earthdata.nasa.gov/search/collections.json?short_name=HLS*&options[short_name][pattern]=true)

#### NASA OPERA analysis-ready products (from HLS and Sentinel-1)
- **What:** JPL OPERA's North-America-focused (some global) products:
  - surface water: `OPERA_L3_DSWX-HLS_V1`, `OPERA_L3_DSWX-S1_V1`
  - land disturbance: `OPERA_L3_DIST-ALERT-HLS_V1`, `OPERA_L3_DIST-ANN-HLS_V1`
  - SAR: `OPERA_L2_RTC-S1_V1` (backscatter), `OPERA_L2_CSLC-S1_V1` (co-registered SLC)
  - `OPERA_L3_DISP-S1_V1` (surface displacement)
  - `OPERA_L4_TROPO-ZENITH_V1`
  - (all 11 collections are cloud-hosted, checked live in CMR)
- **Size:** TB to PB.
- **Coverage:** North America and global (product-dependent), 2023 onward.
- **Format:** COG / HDF5.
- **Access:** `earthaccess`; buckets such as `s3://podaac-ops-cumulus-protected/OPERA_L3_DSWX-HLS_V1`, `s3://lp-protected/OPERA_L3_DIST-ANN-HLS_V1.001`.
- **Auth:** Earthdata Login.
- **License:** CC BY 4.0 (registry).
- **Time to first data:** 15–30 minutes.
- **Hackathon problem:** a near-real-time flood alert service (DSWx); land-subsidence risk for infrastructure (DISP-S1); a wildfire or deforestation disturbance tracker (DIST-ALERT).
- **Sources:** [AWS registry OPERA DSWx-S1](https://registry.opendata.aws/nasa-operal3dswx-s1v1/), [AWS registry OPERA DISP-S1](https://registry.opendata.aws/nasa-operal3disp-s1v1/), [AWS registry OPERA DIST-ALERT](https://registry.opendata.aws/nasa-operal3dist-alert-hlsv1/)

#### MODIS (Terra/Aqua) and VIIRS (Suomi-NPP, NOAA-20, NOAA-21)
- **What:** daily global 250 m–1 km land, ocean and atmosphere products: reflectance, NDVI, LST, snow, fire, burned area, LAI, GPP.
- **Size:** PB.
- **Coverage:** MODIS 2000 to present (Terra/Aqua are in their end-of-mission phase); VIIRS 2012 to present.
- **Format:** HDF/COG.
- **Access:**
  - PC `modis-09A1-061`, `modis-13Q1-061`, `modis-14A1-061`, `modis-64A1-061` and others (COG, no login).
  - CDSE now mirrors the MODIS Terra/Aqua 061 suite (`modis-terra-mod13q1` and others).
  - NOAA JPSS raw and L1/L2 in `s3://noaa-nesdis-n20-pds` and `s3://noaa-nesdis-n21-pds` (public).
  - NASA collections in `lp-prod-protected` (Earthdata).
- **Auth:** none (PC, NOAA); Earthdata (LP DAAC).
- **License:** open.
- **Time to first data:** minutes.
- **Hackathon problem:** drought and vegetation-anomaly dashboard; snow-water outlook.
- **Sources:** [PC STAC (live)](https://planetarycomputer.microsoft.com/api/stac/v1/collections), [CDSE STAC (live)](https://stac.dataspace.copernicus.eu/v1/collections), [AWS registry NOAA JPSS](https://registry.opendata.aws/noaa-jpss/)

#### NASA Black Marble night lights (VNP46) and other night-light sets
- **What:** daily, monthly and yearly VIIRS day/night-band radiance, corrected for moonlight and atmosphere.
- **Products:** `VNP46A1`, `VNP46A2`, `VNP46A3`, `VNP46A4`, plus NRT `VNP46A1_NRT`, `VNP46A2_NRT`, `VNP46A1G_NRT` (CMR, checked live; 4 of 9 cloud-hosted).
- **Size:** TB.
- **Coverage:** global, 2012 to present.
- **Format:** HDF5.
- **Access:**
  - `earthaccess.search_data(short_name="VNP46A2")` (LAADS DAAC); Python `blackmarblepy` (World Bank, not verified here).
  - World Bank **Light Every Night**: `s3://globalnightlight` (monthly prefixes from 201204, public, ODbL).
  - **Nighttime Fire/Flare** from VNP46A1 thermal anomalies: `s3://us-west-2.opendata.source.coop/vnp46a1_thermal_anomaly/` ("no restrictions").
- **Auth:** Earthdata for the NASA products; none for the World Bank and Source copies.
- **Time to first data:** 15 minutes.
- **Hackathon problem:** a power-outage and recovery tracker after hurricanes and earthquakes (Vantor 2026 events below give ground truth); gas-flaring (methane) monitor; conflict-impact measurement.
- **Sources:** [CMR (live)](https://cmr.earthdata.nasa.gov/search/collections.json?short_name=VNP46A*&options[short_name][pattern]=true), [AWS registry Light Every Night](https://registry.opendata.aws/wb-light-every-night/), [AWS registry Nighttime-Fire-Flare](https://registry.opendata.aws/black_marble_combustion/)

#### NAIP (USDA): US aerial imagery, 0.3–1 m RGBN
- **Coverage and access:** CONUS; PC `naip` covers 2010–2023 (COG, no login); Earth Search `naip` 2010–2022; AWS `s3://naip-analytic` / `naip-source` / `naip-visualization` are **requester-pays**.
- **License:** public domain with attribution.
- **Time to first data:** minutes (PC).
- **Hackathon problem:** a solar-panel or swimming-pool inventory; wildfire defensible-space checker.
- **Sources:** [PC STAC (live)](https://planetarycomputer.microsoft.com/api/stac/v1/collections), [AWS registry NAIP](https://registry.opendata.aws/naip/)

#### Copernicus DEM (GLO-30/GLO-90) and other DEMs
- **What:** the global digital surface model at 30 m and 90 m (TanDEM-X based).
- **Size:** ~TB; one COG per 1°×1° tile (for example `Copernicus_DSM_COG_10_N00_00_E006_00_DEM/`, listed live).
- **Format:** COG.
- **Access:** `s3://copernicus-dem-30m`, `s3://copernicus-dem-90m` (eu-central-1, public); PC `cop-dem-glo-30/90`; Earth Search `cop-dem-glo-30/90`; CDSE `cop-dem-glo-30-dged-cog`.
- **Related:**
  - ASF **Global 30 m HAND** (Height Above Nearest Drainage) `s3://glo-30-hand`, a flood-susceptibility layer.
  - PC `nasadem` and `alos-dem`.
  - PGC **ArcticDEM** `s3://pgc-opendata-dems/arcticdem/mosaics/`, **REMA** (Antarctica) and **EarthDEM** (CC BY 4.0).
- **Auth:** no.
- **License:** GLO-30 Public and GLO-90 "available on a free basis for the general public".
- **Time to first data:** minutes.
- **Hackathon problem:** flood-risk ranking (DEM plus HAND plus population); line-of-sight for ground stations; landslide susceptibility.
- **Sources:** [AWS registry Copernicus DEM](https://registry.opendata.aws/copernicus-dem/), [bucket listing (live)](https://copernicus-dem-30m.s3.amazonaws.com/?list-type=2&delimiter=/&max-keys=60), [AWS registry HAND](https://registry.opendata.aws/glo-30-hand/), [AWS registry ArcticDEM](https://registry.opendata.aws/pgc-arcticdem/)

#### ALOS / ALOS-2 PALSAR mosaics (JAXA L-band SAR)
- **What:** annual 25 m L-band backscatter mosaics and forest/non-forest maps.
- **Access:** PC `alos-palsar-mosaic`, `alos-fnf-mosaic`, `alos-dem`. JAXA on AWS: `s3://jaxaalos2/palsar2/L2.2/Africa/` (ScanSAR CARD4L) and event sets `s3://jaxaalos2/palsar2-scansar/Bangladesh/`, `.../Rwanda/`, `.../Turkey-Syria-earthquake/`. Digital Earth Africa copy: `s3://deafrica-input-datasets/alos_palsar_mosaic` (af-south-1).
- **Auth:** no.
- **License:** JAXA terms (free).
- **Time to first data:** minutes.
- **Hackathon problem:** forest-loss detection under cloud; earthquake damage (Turkey–Syria L-band).
- **Sources:** [PC STAC (live)](https://planetarycomputer.microsoft.com/api/stac/v1/collections), [AWS registry PALSAR-2 ScanSAR](https://registry.opendata.aws/jaxa-alos-palsar2-scansar/), [AWS registry Turkey-Syria](https://registry.opendata.aws/palsar2-scansar-turkey-syria/)

#### Sentinel-3 (OLCI, SLSTR, SRAL, SYNERGY) and Sentinel-6
- **What:** ocean colour, land and sea surface temperature, fire radiative power, altimetry.
- **Access:**
  - CDSE has the full NRT/STC/NTC suite (for example `sentinel-3-sl-2-frp-nrt` for fire radiative power, `sentinel-3-olci-2-wfr-ntc` for water) and Sentinel-6 `sentinel-6-p4-2-ntc`.
  - PC `sentinel-3-*-l2-netcdf`.
  - AWS `s3://meeo-s3/NRT/` (eu-central-1).
- **Auth:** CDSE account, or none for PC.
- **Time to first data:** 15 minutes.
- **Hackathon problem:** harmful algal bloom alerts; sea-level rise visualiser.
- **Sources:** [CDSE STAC (live)](https://stac.dataspace.copernicus.eu/v1/collections), [AWS registry Sentinel-3](https://registry.opendata.aws/sentinel-3/)

#### Commercial open-data programs (very-high-resolution optical and SAR), status checked live 2026-10-24
- **Vantor Open Data Program** (Maxar's successor brand on AWS): `s3://vantor-opendata/events/` (us-east-1), **CC BY-NC 4.0**. The 11 event folders listed live are **all from 2026**: `Bordeaux-France-Wildfire-July-2026`, `Colombia-Earthquake-Aug-2026`, `DRC-Ebola-May-2026`, `Indonesia-Earthquakes-Aug-2026`, `Marianas-Typhoon-Bavi-Jul-2026`, **`Mexico-Hurricane-Simon-Oct-2026`**, `Nepal-Flooding-Aug-2026`, `Spain-Portugal-Flooding-Feb-2026`, `Spokane-Washington-Wildfire-Aug-2026`, `Typhoon-Gezani-Feb-2026`, `Venezuela-Earthquake-Jun-2026`. [AWS registry](https://registry.opendata.aws/vantor-open-data/)
- **Maxar Open Data (legacy):** `s3://maxar-opendata/events/` (us-west-2), CC BY-NC 4.0, **56 events** (2015–Dec 2025; for example `WildFires-LosAngeles-Jan-2025`, `Earthquake-Myanmar-March-2025`, `Hurricane-Melissa-Oct-2025`, `Morocco-Flooding-Dec-2025`). Pre/post VHR imagery with STAC. [AWS registry](https://registry.opendata.aws/maxar-open-data/)
- **Umbra SAR Open Data:** `s3://umbra-open-data-catalog/sar-data/tasks/` (81 named tasks listed live), for example `Nepal-Disaster-Coverage_September-2026`, `Jamaica-2025-10`, `Texas_Floods_2025-08`, ports (Rotterdam, Singapore, Long Beach…), mines (Thacker Pass lithium, Kalgoorlie Super Pit), `Kourou, French Guiana` (spaceport) and `Khavda Solar Park`. Includes `stac/`. CC BY 4.0. [AWS registry](https://registry.opendata.aws/umbra-open-data/)
- **Capella Space SAR Open Data:** `s3://capella-open-data/data/` (also `stac/`, `capella-beta-imagery/`, TileDB); CC BY 4.0. [AWS registry](https://registry.opendata.aws/capella_opendata/)
- **ICEYE SAR Open Data:** `s3://iceye-open-data-catalog` (`catalog.json`, `collections/`, `stac-items/`, `data/`); CC BY 4.0. [AWS registry](https://registry.opendata.aws/iceye-opendata/)
- **Satellogic EarthView:** `s3://satellogic-earthview` (`data/tif`, `data/png`, `data/json`, `stac/`, `colab/`); ~1 m RGBN tiles; CC BY 4.0 (also mirrored on HF/Source per the EO slices). [AWS registry](https://registry.opendata.aws/satellogic-earthview/)
- **SpaceEye-T VVHR open data** (Satrec Initiative): `s3://st-vvhr-opendata` with themed folders (`Airports/`, `Ports/`, `Satellite Launching Station, Space Centers/`, `Time Series/`, `disasters/`, `for-developers/`); CC BY 4.0. [AWS registry](https://registry.opendata.aws/st-open-data/)
- **OpenAerialMap:** `s3://oin-hotosm` (us-east-1); CC BY 4.0 drone and aerial imagery. [AWS registry](https://registry.opendata.aws/openaerialmap/)
- **Planet NICFI tropical basemaps: free phase ended.** `planet.com/nicfi` now redirects to `/impact/` (observed 2026-10-24). PC still lists `planet-nicfi-analytic/visual`, but the assets are restricted to GEO-Microsoft RFP winners. The EO-analytics slice reports NICFI mosaics were removed from Global Forest Watch on 1 Apr 2025, with a limited Amazon-only return from 26 May 2026 to 25 May 2027. Sources: [PC STAC (live)](https://planetarycomputer.microsoft.com/api/stac/v1/collections), [Planet NICFI URL](https://www.planet.com/nicfi/), and see `02_eo_analytics_and_industry_problems.md`.
- **Auth:** none for all the AWS buckets above.
- **Time to first data:** minutes.
- **Hackathon problem:** **"disaster damage in 6 hours"**: VHR pre/post (Vantor 2026 events) or SAR through clouds (Umbra/ICEYE/Capella), plus building footprints and population, giving a prioritised rescue map. Port and mine activity monitoring (Umbra tasks). **Note:** Vantor/Maxar are CC BY-NC (fine for a hackathon, not for a commercial product).

#### NISAR (NASA–ISRO L/S-band SAR, launched July 2025)
- **What:** 12-day repeat L-band SAR for deformation, ice, biomass and soil moisture.
- **Products in CMR (checked live, all cloud-hosted, "BETA_V1" and "PROVISIONAL_V1" versions):**
  - L0B: `NISAR_L0B_RRSD`, `NISAR_L0B_CRSD`
  - L1: `NISAR_L1_RSLC`, `NISAR_L1_RIFG`, `NISAR_L1_RUNW`, `NISAR_L1_ROFF`
  - L2: `NISAR_L2_GSLC`, `NISAR_L2_GCOV` (backscatter), `NISAR_L2_GUNW` (geocoded unwrapped interferograms), `NISAR_L2_GOFF`
  - L3: **`NISAR_L3_SME2`** (soil moisture)
  - ancillary: `NISAR_DEM`, `NISAR_TEC` and others
- **Size:** very large (GB per granule).
- **Coverage:** global, 2025 onward.
- **Format:** HDF5.
- **Access:** ASF DAAC (`asf_search`, Vertex), `earthaccess.search_data(short_name="NISAR_L2_GCOV_PROVISIONAL_V1")`.
- **Auth:** Earthdata Login.
- **License:** NASA open.
- **Time to first data:** 30–60 minutes (large files; pick one granule).
- **Hackathon problem:** a "first look with NISAR" crop-soil-moisture or subsidence map; "Provisional" data quality is itself a story.
- **Sources:** [CMR (live)](https://cmr.earthdata.nasa.gov/search/collections.json?short_name=NISAR*&options[short_name][pattern]=true)

#### SWOT (surface water and ocean topography)
- **What:** Ka-band interferometric altimetry: river reaches and nodes, lakes, water-surface rasters, pixel clouds.
- **Products:** `SWOT_L2_HR_RiverSP_2.0`, `SWOT_L2_HR_LakeSP_2.0`, `SWOT_L2_HR_Raster_100m_2.0`, `SWOT_L2_HR_PIXC_2.0` and others (28 HR collections, cloud-hosted, checked live).
- **Coverage:** global, 2023 onward.
- **Format:** shapefile / NetCDF.
- **Access:** PO.DAAC through `earthaccess`.
- **Auth:** Earthdata.
- **Time to first data:** 15–30 minutes (the river shapefiles are small).
- **Hackathon problem:** a transboundary river-flow monitor (dams upstream); reservoir drought tracking.
- **Sources:** [CMR (live)](https://cmr.earthdata.nasa.gov/search/collections.json?short_name=SWOT_L2_HR*&options[short_name][pattern]=true)

#### EMIT (imaging spectrometer on the ISS): reflectance, minerals, CH4/CO2 plumes
- **Products (CMR, checked live):** `EMITL2ARFL` (reflectance), `EMITL2BMIN` (minerals), **`EMITL2BCH4ENH` / `EMITL2BCH4PLM`** (methane enhancement and plume complexes), `EMITL2BCO2ENH/PLM`, `EMITL2BFRCOV`, `EMITL3ASA`, `EMITL4ESM` and others (22 collections, cloud-hosted).
- **Coverage:** ±52° latitude, 2022 onward.
- **Format:** NetCDF / COG.
- **Access:** `earthaccess`; `s3://lp-prod-protected/EMITL1BRAD.001` (in-region).
- **Auth:** Earthdata.
- **License:** CC BY 4.0.
- **Time to first data:** 15–30 minutes.
- **Hackathon problem:** a methane super-emitter attribution and alert tool (EMIT plumes, Carbon Mapper, Climate TRACE assets).
- **Sources:** [AWS registry NASA EMIT](https://registry.opendata.aws/nasa-emit/), [CMR (live)](https://cmr.earthdata.nasa.gov/search/collections.json?short_name=EMIT*&options[short_name][pattern]=true)

#### PACE (OCI hyperspectral ocean colour, plus polarimeters)
- **Products:** 64 `PACE_OCI_*` collections (cloud-hosted, checked live), including L2 `AOP`, `BGC`, `IOP`, `CLOUD`, `LANDVI`, `SFREFL`, `TRGAS`, `UVAI_UAA`, `PAR`, with NRT variants, and L1A/L1B/L1C/L3B.
- **Coverage:** global, 2024 onward.
- **Format:** NetCDF.
- **Access:** OB.DAAC through `earthaccess`.
- **Auth:** Earthdata.
- **Time to first data:** 15–30 minutes.
- **Hackathon problem:** phytoplankton-type and harmful-algal-bloom early warning for fisheries.
- **Sources:** [CMR (live)](https://cmr.earthdata.nasa.gov/search/collections.json?short_name=PACE_OCI*&options[short_name][pattern]=true)

#### GEDI (lidar on the ISS) and ICESat-2
- **GEDI:** `GEDI01_B`, `GEDI02_A`, `GEDI02_B` (CMR, cloud-hosted); `GEDI L4A` footprint biomass on ORNL. AWS registry entries `nasa-gedi02a` and `nasa-gedil4aagbdensityv212056`.
- **ICESat-2:** `ATL03` photons, `ATL08` vegetation; `s3://nsidc-cumulus-prod-protected/ATLAS/ATL03/006`.
- **Auth:** Earthdata.
- **Time to first data:** 30 minutes.
- **Hackathon problem:** forest-carbon verification for carbon credits (GEDI footprints plus canopy-height maps); sea-ice thickness.
- **Sources:** [CMR (live)](https://cmr.earthdata.nasa.gov/search/collections.json?short_name=GEDI0*&options[short_name][pattern]=true), [AWS registry ATL03](https://registry.opendata.aws/nasa-atl03/)

#### ECOSTRESS (thermal on the ISS)
- **Products:** `ECO_L2T_LSTE` (tiled land surface temperature and emissivity), `ECO_L2G_LSTE`, `ECO_L2T_STARS`, cloud (CMR, cloud-hosted); `s3://lp-prod-protected/ECO1BRAD.001`.
- **Auth:** Earthdata.
- **Time to first data:** 15–30 minutes.
- **Hackathon problem:** urban heat-island and heat-wave risk by neighbourhood; crop water stress.
- **Sources:** [AWS registry ECOSTRESS](https://registry.opendata.aws/nasa-ecostress/), [CMR (live)](https://cmr.earthdata.nasa.gov/search/collections.json?short_name=ECO_L2*&options[short_name][pattern]=true)

#### ESA Biomass (P-band SAR, Earth Explorer 7)
- **Status:** "Biomass launched on 29 April 2025"; "fully commissioned". Open Level-1 data was released in December (2025 by context; the year is not shown on the fetched page). Level-2 forest biomass and height products are being released in phases. Access is through ESA's mission data pages (MAAP / EO sign-in likely; unverified). The ESA slice notes "data open to all".
- **Time to first data:** hours (registration).
- **Hackathon problem:** a tropical forest-carbon map independent of optical clouds.
- **Sources:** [ESA Biomass mission page](https://earth.esa.int/eogateway/missions/biomass)

#### Other national open SAR and optical archives on AWS (registry metadata)
- **RADARSAT-1** (Canada, 1995–2013) COGs: `s3://radarsat-r1-l1-cog` (ca-central-1; Open Government License).
- **RCM** (RADARSAT Constellation Mission) CEOS ARD: `s3://rcm-ceos-ard` (ca-central-1).
- **CBERS-4/4A and Amazonia-1** (Brazil/China, INPE): `s3://brazil-eosats` with a STAC bucket `s3://br-eo-stac-1-0-0` (CC BY-SA 3.0).
- **GLAD Landsat ARD:** `s3://glad.landsat.ard/data/tiles/`.
- **Digital Earth Africa:** Sentinel-1/2, Landsat, GeoMAD, WOfS (`s3://deafrica-*`, af-south-1).
- **Digital Earth Pacific:** `s3://dep-public-data/*`.
- **Sources:** [AWS Open Data Registry](https://registry.opendata.aws/), [registry GitHub](https://github.com/awslabs/open-data-registry)

### 2.2 Derived global products

#### ESA WorldCover 10 m (2020, 2021)
- **What:** an 11-class global land-cover map from Sentinel-1 and Sentinel-2.
- **Size:** ~TB of COG tiles; the bucket has `v100/` (2020) and `v200/` (2021) plus a tile grid (`esa_worldcover_grid.fgb`), listed live.
- **Format:** COG.
- **Access:** `s3://esa-worldcover` (eu-central-1, public); PC `esa-worldcover`; S1/S2 annual composites `s3://esa-worldcover-s2`.
- **Auth:** no.
- **License:** CC BY 4.0.
- **Time to first data:** minutes.
- **Hackathon problem:** a baseline for change-detection apps; habitat and solar-siting suitability.
- **Sources:** [AWS registry ESA WorldCover](https://registry.opendata.aws/esa-worldcover-vito/), [bucket listing (live)](https://esa-worldcover.s3.amazonaws.com/?list-type=2&delimiter=/)

#### Dynamic World (Google/WRI): near-real-time 10 m land cover
- **What:** per-Sentinel-2-scene class probabilities (9 classes), 2015 to present.
- **Access:** Earth Engine `GOOGLE/DYNAMICWORLD/V1` (ID from the EE catalog; page not fetched in this pass, so unverified).
- **Auth:** Earth Engine project (see 2.11).
- **License:** CC BY 4.0 (unverified).
- **Time to first data:** 20 minutes (EE setup).
- **Hackathon problem:** detecting new mines, deforestation or flooding the week it happens.
- **Sources:** [Earth Engine catalog (unverified link)](https://developers.google.com/earth-engine/datasets/catalog/GOOGLE_DYNAMICWORLD_V1)

#### Impact Observatory / Esri 10 m annual LULC (9-class)
- **What:** PC `io-lulc-annual-v02` covers **2017–2023** (CC BY 4.0); also `io-lulc`, `io-lulc-9-class`, and AWS `s3://io-10m-annual-lulc` (us-west-2).
- **Auth:** no. **Time to first data:** minutes.
- **Sources:** [PC STAC (live)](https://planetarycomputer.microsoft.com/api/stac/v1/collections), [AWS registry io-lulc](https://registry.opendata.aws/io-lulc/)

#### Building footprints: Google Open Buildings v3, Microsoft Global ML Buildings, VIDA combined, Overture
- **VIDA "Google-Microsoft-OSM Open Buildings":** **2,705,459,584 footprints** in 200 partitions; GeoParquet 1.1, FlatGeobuf and PMTiles; ODbL. Read anonymously from `https://data.source.coop/vida/google-microsoft-osm-open-buildings/geoparquet/by_country/country_iso={ISO}/{ISO}.parquet` (README fetched live). The README quotes Google v3 at 1.8B buildings (Africa, South and Southeast Asia, Latin America) and Microsoft at 1.24B (Bing imagery 2014–2023).
- **Microsoft Building Footprints:** PC `ms-buildings` ("over 999 million buildings", ODbL).
- **Overture Maps Foundation:** buildings, places, transportation, base, divisions and addresses. **The latest release on S3 is `2026-10-21.0`** (also `2026-09-23.0/.1`; listed live); `s3://overturemaps-us-west-2/release/2026-10-21.0/`. Use `pip install overturemaps` (1.0.2) or DuckDB 2.0.0 `read_parquet('s3://overturemaps-us-west-2/release/2026-10-21.0/theme=buildings/type=building/*', hive_partitioning=1)` (path pattern per the Overture docs, unverified). Licenses are ODbL or CDLA per theme.
- **Auth:** no.
- **Time to first data:** minutes (one country).
- **Hackathon problem:** a who-is-exposed damage or flood estimator; "unmapped settlements" finder (Google versus OSM differences).
- **Sources:** [Source VIDA buildings](https://source.coop/vida/google-microsoft-osm-open-buildings), [README (live)](https://data.source.coop/vida/google-microsoft-osm-open-buildings/README.md), [Overture S3 listing (live)](https://overturemaps-us-west-2.s3.amazonaws.com/?list-type=2&delimiter=/&prefix=release/), [PyPI overturemaps](https://pypi.org/project/overturemaps/)

#### JRC Global Surface Water and Hansen Global Forest Change
- **JRC GSW:** water occurrence, change and seasonality 1984 to present; PC `jrc-gsw`.
- **Hansen/UMD Global Forest Change:** **a `GFC-2025-v1.13` folder exists** on Google Cloud Storage (`https://storage.googleapis.com/earthenginepartners-hansen/GFC-2025-v1.13/download.html` returned 200 on 2026-10-24, so the 2025 loss year is out), alongside `GFC-2024-v1.12`. 30 m tree cover 2000 and annual loss; GeoTIFF tiles (also EE `UMD/hansen/global_forest_change_2025_v1_13`, ID pattern unverified).
- **Auth:** no.
- **License:** CC BY 4.0 (per UMD; unverified here).
- **Time to first data:** minutes.
- **Hackathon problem:** a deforestation-risk score for supply chains (EU Deforestation Regulation compliance).
- **Sources:** [PC STAC (live)](https://planetarycomputer.microsoft.com/api/stac/v1/collections), [Hansen GFC v1.13 download page](https://storage.googleapis.com/earthenginepartners-hansen/GFC-2025-v1.13/download.html)

#### NASA FIRMS active fires (MODIS/VIIRS)
- **What:** near-real-time fire detections.
- **Size:** the public global 24-hour VIIRS S-NPP CSV `SUOMI_VIIRS_C2_Global_24h.csv` is **11.1 MB, Last-Modified 2026-10-24 21:48 GMT** (checked live).
- **Coverage:** global, MODIS from 2000 and VIIRS from 2012.
- **Format:** CSV/KML/SHP.
- **Access:** `https://firms.modaps.eosdis.nasa.gov/data/active_fire/suomi-npp-viirs-c2/csv/SUOMI_VIIRS_C2_Global_24h.csv` (no key). Area/date API: `https://firms.modaps.eosdis.nasa.gov/api/area/csv/<MAP_KEY>/VIIRS_SNPP_NRT/world/1` (returns "Invalid MAP_KEY." without a free key).
- **Auth:** none for the 24-hour files; a free MAP_KEY for the API.
- **License:** NASA open.
- **Time to first data:** under 2 minutes.
- **Hackathon problem:** a wildfire-to-infrastructure alert (fires near power lines, villages or rail); gas-flare detection.
- **Sources:** [FIRMS 24h CSV (live)](https://firms.modaps.eosdis.nasa.gov/data/active_fire/suomi-npp-viirs-c2/csv/SUOMI_VIIRS_C2_Global_24h.csv), [FIRMS API](https://firms.modaps.eosdis.nasa.gov/api/)

#### GHSL (JRC Global Human Settlement Layer), WorldPop and Meta population maps
- **GHSL on AWS:** `s3://jrc-ghsl/` with prefixes (listed live) `ghs-pop/`, `ghs-built-s/`, `ghs-built-h-agbh/`, `ghs-built-v/`, `ghs-smod/`, `ghs-age/`, `ghs-built-c-fun/`, `ghs-wup-pop/` (projections), `emc-built-s/`, `emc-built-greenness/` (eu-central-1, CC BY 4.0).
- **Meta/CIESIN High Resolution Settlement Layer** (population at ~30 m): `s3://dataforgood-fb-data/hrsl-cogs/` (CC BY 4.0).
- **WorldPop:** via worldpop.org (not checked live).
- **Auth:** no.
- **Time to first data:** minutes.
- **Hackathon problem:** a people-at-risk multiplier for any hazard layer.
- **Sources:** [AWS registry GHS-POP](https://registry.opendata.aws/ghs-pop/), [GHSL bucket listing (live)](https://jrc-ghsl.s3.amazonaws.com/?list-type=2&delimiter=/), [AWS registry Meta HRSL](https://registry.opendata.aws/dataforgood-fb-hrsl/)

#### Climate TRACE (asset-level emissions)
- **What:** facility-level greenhouse-gas emissions estimated from satellites and AI.
- **Coverage:** global; sectors from `GET https://api.climatetrace.org/v7/definitions/sectors` (checked live) are fluorinated-gases, forestry-and-land-use, buildings, manufacturing, mineral-extraction, waste, fossil-fuel-operations, agriculture, transportation, power.
- **Format:** JSON/CSV.
- **Access:** REST API v7 (no key observed).
- **Auth:** no.
- **License:** Climate TRACE terms (CC BY 4.0 per their site; unverified).
- **Time to first data:** minutes.
- **Hackathon problem:** "verify the polluter": cross-check a facility's reported emissions against satellite methane and NO2 (EMIT, TROPOMI, TEMPO).
- **Sources:** [Climate TRACE API (live)](https://api.climatetrace.org/v7/definitions/sectors)

#### Carbon Mapper plume catalog (Tanager-1, AVIRIS, EMIT)
- **What:** a public catalog of CH4 and CO2 plumes with emission rates.
- **Size:** `GET https://api.carbonmapper.org/api/v1/catalog/plumes/annotated?limit=1` reports **total_count 45,539 plumes** (checked live); the newest item is a **Tanager** CH4 plume from 2026-09-24 in the Permian Basin (−101.75, 31.52).
- **Format:** JSON (GeoJSON point plus metadata).
- **Access:** REST API (catalog endpoints answered without a token).
- **Auth:** no for the catalog (an account may be required for bulk or downloads; unverified).
- **License:** Carbon Mapper terms.
- **Time to first data:** minutes.
- **Hackathon problem:** a methane super-emitter leaderboard by operator; a repeat-offender detector.
- **Sources:** [Carbon Mapper API (live)](https://api.carbonmapper.org/api/v1/catalog/plumes/annotated?limit=1)

#### UNEP IMEO MARS methane datasets and blended methane products
- **`UNEP-IMEO/MARS-S2L`:** 96 GB on HF, **CC BY-NC-SA 4.0**, 100k–1M samples. A Sentinel-2/Landsat methane-plume dataset from the Methane Alert and Response System. Also `UNEP-IMEO/MARS-Hyperspectral`.
- **Blended TROPOMI+GOSAT methane:** `s3://blended-tropomi-gosat-methane` (us-west-2; "no restrictions").
- **Time to first data:** minutes (stream from HF).
- **Hackathon problem:** a plume-detector model (see also the methane benchmarks in 08b).
- **Sources:** [HF UNEP-IMEO](https://huggingface.co/UNEP-IMEO), [AWS registry blended methane](https://registry.opendata.aws/blended-tropomi-gosat-methane/)

#### Copernicus Emergency Management Service (CEMS) rapid mapping
- **What:** vector damage and flood delineations for each activation.
- **Access:** the public dashboard API `https://rapidmapping.emergency.copernicus.eu/backend/dashboard-api/public-activations/` answered `{"code":"Activation code parameter is mandatory"}` (live), so it is queried per activation code (for example `EMSR…`). Portal: rapidmapping.emergency.copernicus.eu.
- **Auth:** no.
- **License:** Copernicus.
- **Time to first data:** 15 minutes.
- **Hackathon problem:** ground-truth labels for damage models; comparing AI damage maps against the official ones.
- **Sources:** [CEMS rapid mapping API (live)](https://rapidmapping.emergency.copernicus.eu/backend/dashboard-api/public-activations/)

#### Microsoft AI for Good 2026 earthquake building-damage maps
- **What:** `predicted-damage-venezuela-2026` (June 2026 quakes; imagery from 25–26 June) and `predicted-damage-colombia-2026` (August 2026) on Planetary Computer, CC BY 4.0. Building-level "no damage / affected / unknown". They pair with the Vantor `Venezuela-Earthquake-Jun-2026` and `Colombia-Earthquake-Aug-2026` imagery.
- **Auth:** no. **Time to first data:** minutes.
- **Sources:** [PC STAC (live)](https://planetarycomputer.microsoft.com/api/stac/v1/collections)

#### Satellite embedding products (precomputed "foundation model features")
- **AlphaEarth Foundations Satellite Embedding (Google DeepMind):** annual 64-dim embeddings at 10 m. Earth Engine `GOOGLE/SATELLITE_EMBEDDING/V1/ANNUAL`. An **unofficial COG copy on Source Cooperative covers 2017–2025**: `https://data.source.coop/tge-labs/aef/` (= `s3://us-west-2.opendata.source.coop/tge-labs/aef`, CC BY 4.0). **Warning from the README: the COGs are "bottom-up"; use the provided `.vrt` files with GDAL.**
- **TESSERA** (Cambridge) temporal embeddings: `s3://tessera-embeddings/v1.1/dclimate.icechunk` (Icechunk/Zarr, **CC BY-SA**).
- **Clay v1.5 Sentinel-2 embeddings:** `s3://us-west-2.opendata.source.coop/clay/clay-v1-5-sentinel2` and the LGND copy `.../clay/lgnd-clay-v1-5-sentinel-2-l2a`; Clay v0 embeddings (CC BY 4.0).
- **Major TOM embeddings:** see 08b.
- **Auth:** no (EE needs a project).
- **Time to first data:** minutes for one tile.
- **Hackathon problem:** "search the planet by example" (click a solar farm or illegal airstrip and find all similar places), with no model training needed.
- **Sources:** [AWS registry AEF](https://registry.opendata.aws/aef-source/), [AEF README (live)](https://data.source.coop/tge-labs/aef/README.md), [AWS registry TESSERA](https://registry.opendata.aws/tessera/), [AWS registry Clay v1.5](https://registry.opendata.aws/clay-v1-5-sentinel2/)

#### Forest structure and carbon
- **Meta/WRI canopy height v2** (DINOv3-based global canopy height): `s3://dataforgood-fb-data/forests/v2/global/dinov3_global_chm_v2_ml3/` (CC BY 4.0); v1 at `.../forests/v1/alsgedi_global_v6_float/`.
- **CTrees global aboveground biomass 100 m:** `s3://ctrees-agb-100m-global/agb_100m_global/` (CC BY 4.0); plus Amazon canopy height and California sub-metre tree height.
- **PC `chloris-biomass`.**
- **Auth:** no.
- **Time to first data:** minutes.
- **Hackathon problem:** a carbon-credit audit (claimed forest versus measured canopy and biomass).
- **Sources:** [AWS registry Meta canopy v2](https://registry.opendata.aws/dataforgood-fb-forestsv2/), [AWS registry CTrees AGB](https://registry.opendata.aws/ctrees-agb-100m-global/)

#### Flood and hazard layers
- **RAPID NRT flood maps:** `s3://rapid-nrt-flood-maps` (CC BY-NC-SA 4.0).
- **PC `deltares-floods`** (global flood hazard), **`mtbs`** (US burn severity), **`usda-cdl`** (US crops), **`noaa-c-cap`**.
- **GOES-18/19 ABI flood products:** `ABI-Flood-Day`, `ABI-Flood-Hourly` (TIF and shapefile) prefixes in `s3://noaa-goes19` (listed live).
- **Sources:** [AWS registry RAPID](https://registry.opendata.aws/rapid-nrt-flood-maps/), [PC STAC (live)](https://planetarycomputer.microsoft.com/api/stac/v1/collections), [GOES-19 bucket listing (live)](https://noaa-goes19.s3.amazonaws.com/?list-type=2&delimiter=/)

#### Not verified in this pass (listed for completeness)
- MapBiomas (Brazil and other countries; mapbiomas.org).
- Global Fishing Watch API (token required).
- GLAD and RADD forest alerts.
- Global Mangrove Watch (a DE Africa copy exists at `s3://deafrica-input-datasets/gmw`).
- WorldCereal.
- Kontur population.

See the EO-analytics slice for coverage.
### 2.3 ML benchmark datasets

**Full catalogue in a separate file: [`08b_ml_benchmark_datasets.md`](08b_ml_benchmark_datasets.md)** (verified 2026-10-24 by bucket listings and Hugging Face, Zenodo, Source and Kaggle APIs; ~120 entries with its own quick-pick table). Summary:
- **Buildings, roads and disaster damage:** SpaceNet 1–9 (`s3://spacenet-dataset`, no auth; SN8 floods 7.3 GB; SN9 optical-SAR registration 0.56 GB), xView1, xBD/xView2, xView3-SAR, fMoW, DOTA, DIOR, iSAID, FAIR1M, RarePlanes, BRIGHT (GRSS DFC 2025).
- **Maritime:** HRSID, SSDD, OpenSARShip, OSSDD (2026), ShipsNet, Airbus ship detection, MARIDA and MADOS (marine debris and oil spills).
- **Land cover and pretraining corpora:** BigEarthNet v2 (reBEN), EuroSAT, SEN12MS, SSL4EO-S12/L, SatlasPretrain, Major TOM, TerraMesh, OlmoEarth pretraining data, Copernicus-Pretrain, MMEarth, Galileo, Five Billion Pixels, OpenEarthMap, LoveDA, CloudSEN12+, MegaEarth (OSM×S2, Oct 2026).
- **Benchmark suites and loaders:** TorchGeo v0.10.1 (29 Sep 2026), GEO-Bench and GEO-Bench-2, PANGAEA, Copernicus-Bench, the TACO catalogue (bulk update 8 Oct 2026), SustainBench, MOSAIKS.
- **Hazards:** Sen1Floods11, SEN12-FLOOD, Kuro Siwo, WorldFloods v2, MMFlood, ImpactMesh-Flood/Fire (Sep 2026), plus methane, crop-type and wildfire sets.
- **Practical note from 08b:** many original-host datasets need registration (xView), while HF/TACO mirrors are instant. Download times assume ~20 MB/s venue Wi-Fi.

### 2.4 Atmosphere, weather and climate

#### ERA5 reanalysis (ECMWF/C3S): via the CDS API, ARCO-ERA5 Zarr, Planetary Computer, AWS
- **What:** hourly global reanalysis at 0.25°, 37 pressure levels plus single levels, 1940 to present.
- **Size:** hundreds of TB.
- **Access:**
  - **ARCO-ERA5 on Google Cloud (public, no auth):** `gs://gcp-public-data-arco-era5/ar/`. It lists 19 Zarr stores (checked live), including `full_37-1h-0p25deg-chunk-1.zarr-v3`, `model-level-1h-0p25deg.zarr-v2`, `1959-2022-6h-1440x721.zarr` and coarse versions (`64x32`, `240x121`); also `co/` and `raw/`. Open with `xarray.open_zarr("gs://gcp-public-data-arco-era5/ar/full_37-1h-0p25deg-chunk-1.zarr-v3", storage_options={"token":"anon"})`.
  - **CDS API (official):** put `url: https://cds.climate.copernicus.eu/api` and `key: <PERSONAL-ACCESS-TOKEN>` in `~/.cdsapirc`; `pip install "cdsapi>=0.7.7"`. **You must accept each dataset's licence manually on its web page first.**
  - **PC `era5-pds`** (from 1979) and **AWS `s3://era5-pds`** (us-east-1).
- **Auth:** none for ARCO, PC and AWS; a free ECMWF account for CDS.
- **License:** Copernicus licence (attribution).
- **Time to first data:** minutes (ARCO slice).
- **Hackathon problem:** a launch-weather go/no-go history (upper-level winds over Cape Canaveral, Starbase, Vandenberg); training data for satellite-to-weather models.
- **Sources:** [ARCO-ERA5 bucket listing (live)](https://storage.googleapis.com/storage/v1/b/gcp-public-data-arco-era5/o?delimiter=/&prefix=ar/), [CDS how-to-API](https://cds.climate.copernicus.eu/how-to-api), [AWS registry ERA5](https://registry.opendata.aws/ecmwf-era5/)

#### WeatherBench 2 (Google Research): AI-weather benchmark and forecast archive
- **What:** ERA5 ground truth plus archived forecasts from AI and physics models. `gs://weatherbench2/datasets/` lists 27 sets (checked live): `aurora`, `ens`, `era5`, `era5-daily-climatology`, `era5-forecasts`, `fuxi`, `gencast`, `graphcast` (+`_hres_init`, `_v2`), `hres`, `hres_t0`, `ifs_ens`, `ifs_extended_range`, `keisler`, `metar`, `neuralgcm_deterministic`, `neuralgcm_ens`, `pangu`, `sphericalcnn` and others; also `benchmark_results/`.
- **Format:** Zarr.
- **Access:** `xarray.open_zarr("gs://weatherbench2/datasets/...")`, anonymous.
- **Auth:** no.
- **License:** per dataset (mostly CC BY; check).
- **Time to first data:** minutes.
- **Hackathon problem:** "which AI model would have best forecast this storm?", a forecast-verification explorer.
- **Sources:** [WeatherBench 2 bucket listing (live)](https://storage.googleapis.com/storage/v1/b/weatherbench2/o?delimiter=/&prefix=datasets/)

#### ECMWF open data (real-time IFS and AIFS forecasts)
- **Access:** `pip install ecmwf-opendata` (0.3.35, 2026-10-16); data portal `https://data.ecmwf.int/forecasts/`; PC collection `ecmwf-forecast` (CC BY 4.0).
- **Auth:** no.
- **Time to first data:** minutes.
- **Hackathon problem:** a real-time launch or recovery-zone weather briefing.
- **Sources:** [PyPI ecmwf-opendata](https://pypi.org/project/ecmwf-opendata/), [PC STAC (live)](https://planetarycomputer.microsoft.com/api/stac/v1/collections)

#### GOES-East/West (GOES-19 and GOES-18; legacy GOES-16/17) on AWS
- **What:** ABI imagery (16 bands, full disk every 10 minutes, CONUS every 5 minutes, mesoscale every 1 minute), L2 products, GLM lightning.
- **Size:** PB.
- **Coverage:** Western Hemisphere, 2017 to present.
- **Format:** NetCDF.
- **Access:** `s3://noaa-goes19`, `s3://noaa-goes18` (us-east-1, public). The live listing shows `ABI-L1b-RadF/C/M`, dozens of `ABI-L2-*` products (cloud heights, aerosol, fire and more), and **`ABI-Flood-Day`/`ABI-Flood-Hourly`** flood products (TIF and shapefile). GOES-19 also carries the CCOR-1 coronagraph (see 2.7). PC `goes-cmi`, `goes-glm`. Use `pip install goes2go` (2025.10.0) or `satpy` (0.60.0).
- **Auth:** no.
- **License:** NOAA NODD (open; attribution requested).
- **Time to first data:** minutes.
- **Hackathon problem:** a wildfire smoke and spread nowcast; a lightning-risk alert for launch pads.
- **Sources:** [AWS registry NOAA GOES](https://registry.opendata.aws/noaa-goes/), [GOES-19 bucket listing (live)](https://noaa-goes19.s3.amazonaws.com/?list-type=2&delimiter=/)

#### Himawari-9, GK-2A and the global geostationary mosaic (NOAA NODD)
- **Himawari:** `s3://noaa-himawari9` (prefixes `AHI-L1b-FLDK/`, `AHI-L1b-Japan/`, `AHI-L1b-Target/`, `AHI-L2-FLDK-Clouds/`, `AHI-L2-FLDK-ISatSS/`, `AHI-L2-FLDK-Winds/`, listed live) and `s3://noaa-himawari8`.
- **GK-2A (KMA):** `s3://noaa-gk2a-pds`.
- **GMGSI global mosaic:** `s3://noaa-gmgsi-pds`.
- **Auth:** no.
- **License:** JMA/KMA terms through NOAA.
- **Time to first data:** minutes.
- **Hackathon problem:** typhoon tracking across Asia-Pacific; a global cloud-cover forecast for EO tasking (when to schedule a VHR satellite).
- **Sources:** [AWS registry Himawari](https://registry.opendata.aws/noaa-himawari/), [AWS registry GK-2A](https://registry.opendata.aws/noaa-gk2a-pds/), [AWS registry GMGSI](https://registry.opendata.aws/noaa-gmgsi/)

#### GPM IMERG precipitation
- **What:** half-hourly and daily global precipitation at 0.1°, V07.
- **Access:**
  - NASA `GPM_3IMERGHH`, `GPM_3IMERGDF` and others in `s3://gesdisc-cumulus-prod-protected/...` (Earthdata).
  - **dynamical.org Icechunk Zarr `s3://dynamical-nasa-imerg`** (CC BY 4.0, public).
  - PC `gpm-imerg-hhr` (2000–2021 only).
- **Auth:** none (dynamical, PC) or Earthdata.
- **Time to first data:** minutes.
- **Hackathon problem:** flash-flood early warning (IMERG plus HAND plus population).
- **Sources:** [AWS registry dynamical IMERG](https://registry.opendata.aws/dynamical-nasa-imerg/), [AWS registry IMERG HH](https://registry.opendata.aws/nasa-gpm3imerghh/)

#### Sentinel-5P TROPOMI (NO2, CH4, CO, SO2, HCHO, O3, aerosol, cloud)
- **What:** daily global trace gases at ~5.5×3.5 km.
- **Access:**
  - CDSE collections `sentinel-5p-l2-no2/ch4/co/so2/hcho/o3/o3-pr/o3-tcl/aer-ai/aer-lh/cloud`, each with NRTI/OFFL/RPRO variants (listed live).
  - AWS `s3://meeo-s5p/NRTI/`, `/OFFL/`, `/RPRO/` (eu-central-1).
  - PC `sentinel-5p-l2-netcdf`.
  - Earth Engine `COPERNICUS/S5P/OFFL/L3_NO2` and similar (gridded; unverified IDs).
  - NASA GES DISC copies.
- **Auth:** none (AWS, PC) or a CDSE account.
- **License:** Copernicus.
- **Time to first data:** minutes.
- **Hackathon problem:** a pollution-hotspot attribution map (power plants, ports); methane screening before EMIT or Tanager follow-up.
- **Sources:** [CDSE STAC (live)](https://stac.dataspace.copernicus.eu/v1/collections), [AWS registry Sentinel-5P](https://registry.opendata.aws/sentinel5p/)

#### TEMPO (hourly air quality over North America, from geostationary orbit)
- **Products (CMR, checked live, LARC_CLOUD):** `TEMPO_NO2_L2/L3` plus **NRT** versions, `TEMPO_HCHO_L2/L3(+NRT)`, `TEMPO_O3TOT_L2/L3`, `TEMPO_O3PROF_L2/L3`, `TEMPO_CLDO4_L2/L3`, `TEMPO_RAD_L1`, `TEMPO_IRR_L1`.
- **Coverage:** North America, hourly daytime, 2023 onward.
- **Format:** NetCDF.
- **Access:** `earthaccess.search_data(short_name="TEMPO_NO2_L3")`.
- **Auth:** Earthdata.
- **Time to first data:** 15 minutes.
- **Hackathon problem:** hour-by-hour pollution exposure for schools; rush-hour versus wildfire NO2.
- **Sources:** [CMR (live)](https://cmr.earthdata.nasa.gov/search/collections.json?keyword=TEMPO&provider=LARC_CLOUD&page_size=50)

#### OCO-2 / OCO-3 (CO2, SIF), OMI NO2, NASA GHG products
- **OCO-2:** `s3://gesdisc-cumulus-prod-protected/OCO2_DATA/OCO2_GEOS_L3CO2_DAY.10r` (Earthdata; CC BY 4.0 per registry).
- **OMI/Aura NO2:** `s3://omi-no2-nasa` (public, "no restrictions").
- **Blended TROPOMI+GOSAT methane:** `s3://blended-tropomi-gosat-methane`.
- **Time to first data:** 15 minutes.
- **Hackathon problem:** a city CO2 dome tracker; checking national inventories against satellites.
- **Sources:** [AWS registry OCO-2](https://registry.opendata.aws/nasa-oco-2/), [AWS registry OMI NO2](https://registry.opendata.aws/omi-no2-nasa/)

#### NOAA forecast and radar buckets, plus new AI-forecast archives
- **GFS:** `s3://noaa-gfs-bdp-pds`. **HRRR:** `s3://noaa-hrrr-bdp-pds` (Zarr copy `s3://hrrrzarr`). **NEXRAD ARCO Icechunk-Zarr:** `s3://nexrad-arco`. **WIS2 global cache:** `s3://wis2globalcache`.
- **NOAA nested-EAGLE** experimental AI ensemble (PC `nested-eagle-conus` / `nested-eagle-global`, CC BY 4.0, from 2024-10).
- **Met Office global and UK deterministic forecasts** (PC `met-office-*`).
- **Auth:** no.
- **Time to first data:** minutes.
- **Sources:** [AWS registry GFS](https://registry.opendata.aws/noaa-gfs-bdp-pds/), [AWS registry HRRR](https://registry.opendata.aws/noaa-hrrr-pds/), [AWS registry NEXRAD ARCO](https://registry.opendata.aws/nexrad-arco/), [PC STAC (live)](https://planetarycomputer.microsoft.com/api/stac/v1/collections)

#### ML-ready weather and climate datasets
- **SEVIR** (Storm EVent ImageRy: GOES and NEXRAD aligned storm events): `s3://sevir` (`CATALOG.csv`, `data/`); "no restrictions". The angle: a nowcasting model.
- **WxC-Bench** (NASA-IMPACT weather and climate downstream benchmark, HF `nasa-impact/WxC-Bench`): **968 GB**, MIT.
- **MUR SST** (Zarr) `s3://mur-sst/zarr-v1`.
- **NASA POWER** (solar and meteorology for energy) `s3://nasa-power`.
- **GNSS radio occultation** `s3://gnss-ro-data`.
- **Sources:** [AWS registry SEVIR](https://registry.opendata.aws/sevir/), [HF WxC-Bench](https://huggingface.co/datasets/nasa-impact/WxC-Bench), [AWS registry MUR](https://registry.opendata.aws/mur/), [AWS registry NASA POWER](https://registry.opendata.aws/nasa-power/), [AWS registry GNSS-RO](https://registry.opendata.aws/gnss-ro-opendata/)

#### CAMS (Copernicus Atmosphere Monitoring Service)
- **What:** atmospheric composition reanalysis (EAC4) and forecasts.
- **Access:** the Atmosphere Data Store, using the same `cdsapi` client with an ADS URL and key, and per-dataset licence acceptance. Not checked live in this pass.
- **Hackathon problem:** wildfire-smoke transport forecast.
- **Sources:** [CDS how-to-API (same mechanism)](https://cds.climate.copernicus.eu/how-to-api)

### 2.5 Orbital / space-object data

#### CelesTrak GP data (OMM/TLE), SATCAT and SOCRATES
- **What:** public general-perturbations orbital elements for catalogued objects, sourced from the 18th SDS via Space-Track, plus supplemental GP from operator ephemerides. Also the satellite catalog and SOCRATES conjunction screening.
- **Size (checked live 2026-10-24):** `gp.php?GROUP=active&FORMAT=json` returned **16,792 active objects (7.1 MB)**, including **11,141 named STARLINK** and **391 KUIPER**. `https://celestrak.org/pub/satcat.csv` is 6.8 MB (Last-Modified 2026-10-24 03:20 GMT). The SOCRATES page is live.
- **Coverage:** all public catalogued objects; current elements (history needs Space-Track).
- **Format:** OMM JSON/CSV/XML, TLE, KVN.
- **Access:** `https://celestrak.org/NORAD/elements/gp.php?GROUP=active&FORMAT=json` (also `GROUP=starlink`, `CATNR=25544`, and others); `https://celestrak.org/pub/satcat.csv`; `https://celestrak.org/SOCRATES/`. Propagate with `pip install sgp4` (2.27) or `skyfield` (1.55); `orekit-jpype` (13.1.9.0) for high fidelity.
- **Auth:** no.
- **License:** CelesTrak usage policy: download each group at most once per update cycle, or IPs get blocked.
- **Time to first data:** under 2 minutes.
- **Hackathon problem:** a **"conjunction triage for small operators"** tool (rank tonight's SOCRATES close approaches by risk and manoeuvre cost); Starlink versus Kuiper shell visualiser; "what's overhead and is it bright?" for astronomers.
- **Sources:** [CelesTrak GP (live)](https://celestrak.org/NORAD/elements/gp.php?GROUP=active&FORMAT=json), [CelesTrak SATCAT CSV (live)](https://celestrak.org/pub/satcat.csv), [SOCRATES](https://celestrak.org/SOCRATES/), [CelesTrak usage policy](https://celestrak.org/usage-policy.php)

#### Space-Track.org (18th SDS): full GP history, SATCAT, decay/TIP, public CDMs
- **What:** the authoritative US catalogue and history (classes `gp`, `gp_history`, `satcat`, `decay`, `tip`, `cdm_public`, `boxscore`).
- **Access:** `https://www.space-track.org/basicspacedata/query/class/gp/...` returned **HTTP 401 without login** (checked live). Use `pip install spacetrack` (2.1.0, 2026-08-23).
- **Auth:** **yes.** A free account under a user agreement; approval is usually quick but not instant (plan ahead). Rate limits apply (see the site's API guidance).
- **License:** the **user agreement restricts redistribution** of data.
- **Shortcut:** HF `juliensimon/space-track-tle-history` (238M TLE rows 1959–2026, 12.5 GB Parquet; see 2.6) and `juliensimon/space-track-satcat` (CelesTrak-based). Treat the redistribution licence with caution.
- **Time to first data:** hours (account), or minutes via the HF mirror.
- **Hackathon problem:** a manoeuvre detector over TLE history (sudden mean-motion jumps); reentry prediction; debris growth after fragmentation events.
- **Sources:** [Space-Track](https://www.space-track.org/), [PyPI spacetrack](https://pypi.org/project/spacetrack/), [HF space-track-tle-history](https://huggingface.co/datasets/juliensimon/space-track-tle-history)

#### Jonathan McDowell's GCAT (General Catalog of Artificial Space Objects)
- **What:** an independent, richly annotated catalogue of every launch and object, with launch logs, satcat, deep-space and orbital histories.
- **Size:** `https://planet4589.org/space/gcat/tsv/cat/satcat.tsv` is **19.3 MB, Last-Modified 2026-10-24 19:04 GMT** (checked live); HF mirrors `juliensimon/gcat-satellite-catalog` (68,538 rows), `gcat-launch-vehicles`, `gcat-deep-space`.
- **Format:** TSV.
- **Access:** HTTPS (TSV files under `planet4589.org/space/gcat/tsv/`).
- **Auth:** no.
- **License:** CC BY (per the GCAT site; not re-verified here).
- **Time to first data:** minutes.
- **Hackathon problem:** a launch-cadence and failure-rate dashboard by vehicle and country; "who owns orbit" market-share tracker.
- **Sources:** [GCAT satcat.tsv (live)](https://planet4589.org/space/gcat/tsv/cat/satcat.tsv), [GCAT home](https://planet4589.org/space/gcat/)

#### ESA DISCOS (Database and Information System Characterising Objects in Space)
- **What:** object physical properties (mass, shape, dimensions), launches, reentries and fragmentation events.
- **Access:** REST API `https://discosweb.esoc.esa.int/api/objects`, which returned **401 "Authentication is required"** without a token (checked live).
- **Auth:** yes (a free account and personal token).
- **License:** ESA terms (no redistribution).
- **Time to first data:** 30–60 minutes.
- **Hackathon problem:** a reentry casualty-risk estimator (mass and material plus decay date).
- **Sources:** [DISCOSweb API (live 401)](https://discosweb.esoc.esa.int/api/objects)

#### Launch Library 2 (The Space Devs)
- **What:** a community launch database (past and upcoming launches, agencies, vehicles, pads, astronauts, events).
- **Size:** `https://ll.thespacedevs.com/2.3.0/launches/upcoming/?limit=1&mode=list` reports **474 upcoming launches** (checked live; the next listed was a Falcon 9 Starlink Group 15-15).
- **Format:** JSON REST (API v2.3.0).
- **Auth:** no (free tier rate-limited; patreon keys raise limits).
- **License:** The Space Devs terms.
- **Time to first data:** minutes.
- **Hackathon problem:** launch-schedule slippage prediction; a "launch-window weather risk" app (LL2 plus ERA5 or ECMWF).
- **Sources:** [LL2 API (live)](https://ll.thespacedevs.com/2.3.0/launches/upcoming/?limit=1&mode=list)

#### SatNOGS DB and Network (open ground-station network)
- **What:** a crowd-sourced catalogue of satellites and transmitters, plus observations and decoded telemetry from amateur ground stations.
- **Size:** `https://db.satnogs.org/api/satellites/?format=json` is 1.56 MB (checked live). Transmitters, telemetry and observations endpoints exist (network.satnogs.org); the HF mirror is `juliensimon/satnogs-transmitters`.
- **Auth:** no for reads (a token for some telemetry endpoints; unverified).
- **License:** CC BY-SA (SatNOGS DB; unverified).
- **Time to first data:** minutes.
- **Hackathon problem:** a CubeSat "is it alive?" health monitor from amateur-received telemetry; RF-interference mapping.
- **Sources:** [SatNOGS DB API (live)](https://db.satnogs.org/api/satellites/?format=json)

#### Conjunction and manoeuvre ML datasets
- **ESA Kelvins Collision Avoidance Challenge dataset** (real anonymised CDM time series): Zenodo **0.22 GB, CC BY 4.0** (2021). [doi:10.5281/zenodo.4463683](https://doi.org/10.5281/zenodo.4463683)
- **Synthetic Collision Dataset for Spacecraft Collision Avoidance:** 4.43 GB, CC BY 4.0 (2024). [doi:10.5281/zenodo.13970999](https://doi.org/10.5281/zenodo.13970999)
- **GEO satellite manoeuvres** (HF `FraDra/GEO_satellite_maneuvers`): 24.5 GB, MIT, 10k–100k samples (updated Jan 2026). [HF](https://huggingface.co/datasets/FraDra/GEO_satellite_maneuvers)
- **HF `juliensimon/satellite-conjunctions`** (SOCRATES near-miss log, 871,973 rows) and **`orbital-fragmentation-events`, `reentry-events`**: see 2.6.
- **Starlink "mechanical energy loss" dataset** (drag-derived, 2025): [doi:10.5281/zenodo.15281786](https://doi.org/10.5281/zenodo.15281786)
- **MIT ARCLab Prize** pattern-of-life ("SPLID") and space-weather/drag challenge data: **not found on Zenodo or HF by name in this pass (unverified).**
- **Time to first data:** minutes.
- **Hackathon problem:** a collision-probability forecaster (Kelvins), a manoeuvre classifier (GEO), or drag versus space-weather analysis (Starlink energy loss plus Kp/Dst).

#### Other orbital sources
- **UCS Satellite Database:** HF mirror `juliensimon/ucs-satellite-database` (updated 2026-09-20). Whether UCS still updates the original is unverified.
- **WMO OSCAR satellites** (`juliensimon/wmo-oscar-satellites`) and **FCC NGSO filings** (`juliensimon/fcc-ngso-filings`): HF mirrors.
- **Sentinel-1 precise orbit files:** `s3://s1-orbits` (public).
- **IERS Earth orientation:** `juliensimon/iers-earth-orientation`.
- **Python tools:** `sgp4` 2.27, `skyfield` 1.55, `orekit-jpype` 13.1.9.0. `poliastro` is stale (0.17.0, 2022).
### 2.6 Astronomy

#### Gaia DR3 (and DR4 on 2 Dec 2026)
- **What:** ESA astrometric survey: positions, parallaxes, proper motions, photometry, BP/RP spectra, radial velocities, variability and solar-system object tables for ~1.8 billion sources.
- **Size:** multi-TB archive. The `gaiadr3.gaia_source` table is queryable row by row, and a HATS-partitioned copy sits on S3.
- **Coverage:** all sky; DR3 is based on 34 months of data. **DR4 is scheduled for 2 December 2026** ("based on 66 months of data"). **DR5 comes "not before the end of 2030"** (full 10.5-year mission).
- **DR4 content (from ESA's DR4 content page, "still under development"):**
  - "about 2.8 billion sources"; `gaia_source` has 2,000,033,276 rows and `all_source_astrometry` 2,793,009,568
  - **epoch astrometry:** 129.6 billion records (62 TB); epoch images 113 TB; epoch photometry 121.8 billion records
  - **RVS epoch spectra:** 6.9 billion (49 TB); BP/RP epoch spectra 119 TB
  - **`vari_planetary_transit`: 1,007 transit-candidate events**
  - non-single stars: 5.9M two-body orbits, 4.3M `nss_masses`
  - variability: 403M `vari_summary` rows, 2.39M eclipsing binaries, 246k RR Lyrae, 19k Cepheids
  - total "approximately 400 TB" across 117 tables, versus 10 TB for DR3
  - a German observatory note also says ~400 TB; a Jan 2026 talk said ~500 TB
- **Hackathon note:** DR4 lands about 5 weeks after the hackathon. A "DR4-ready" tool built on DR3 (an astrometric exoplanet or brown-dwarf finder, a binary-star mass explorer) would be timely.
- **Format:** VOTable/CSV/FITS via TAP; Parquet (HATS) on S3.
- **Access:** TAP/ADQL `https://gea.esac.esa.int/tap-server/tap` (checked live 2026-10-24: `SELECT TOP 3 source_id,ra,dec,phot_g_mean_mag FROM gaiadr3.gaia_source` returned rows); `from astroquery.gaia import Gaia`; HATS on S3: `s3://stpubdata/gaia/gaia_dr3/public/hats` (us-east-1), read with `pip install lsdb` (lsdb 0.11.1, released 2026-10-22).
- **Auth:** no (an optional Gaia archive account allows bigger async jobs).
- **License:** ESA/Gaia credit and citation required. The AWS registry lists it as "Attribution required."
- **Time to first data:** minutes.
- **Hackathon problem:** star-tracker catalog builder for small satellites (a bright-star subset with proper motion propagated to the epoch); a "what changed in DR4" explorer ready for 2 Dec 2026; hunting nearby stars for exoplanet follow-up.
- **Sources:** [Gaia data release scenario](https://www.cosmos.esa.int/web/gaia/release), [Gaia DR4 content](https://www.cosmos.esa.int/web/gaia/dr4), [Gaia news 2026](https://www.cosmos.esa.int/web/gaia/news-2026), [TU Dresden DR4 note](https://tu-dresden.de/bu/umwelt/geo/ipg/astro/observatorium/news/gaia-data-release-4), [AWS registry: Gaia DR3 HATS](https://registry.opendata.aws/mast-gaia-dr3/), [LSDB docs](https://docs.lsdb.io/en/latest/index.html), [PyPI lsdb](https://pypi.org/project/lsdb/)

#### SDSS DR19 and DR20 (SDSS-V)
- **What:** SDSS-V spectroscopy. DR19 has the first Milky Way Mapper (MWM) spectra and a large Black Hole Mapper (BHM) update. DR20 adds the first BOSS spectra from Las Campanas, SPIDERS spectra of eROSITA X-ray sources, and more Local Volume Mapper tiles. **DR20 has no new APOGEE spectra; those are expected in DR21.**
- **Size:** not stated on the release pages (the DR19 paper is arXiv:2507.07093).
- **Coverage:** northern (APO) and southern (LCO) skies; stars, quasars, galaxies, nebulae.
- **Format:** FITS spectra, catalogs, Value Added Catalogs; HiPS maps for LVM.
- **Access:** the Zora and Valis web/API interfaces; SciServer Compute notebooks; Science Archive Server downloads; `astroquery.sdss` for the legacy SkyServer.
- **Auth:** no (a SciServer account is needed for hosted compute).
- **License:** SDSS public data policy (cite and acknowledge).
- **Time to first data:** minutes.
- **Hackathon problem:** spectral-type classifier or anomaly finder on SDSS-V stars; a quasar-variability explorer.
- **Sources:** [SDSS DR19](https://www.sdss.org/dr19/), [SDSS DR20](https://www.sdss.org/dr20/)

#### DESI DR1
- **What:** Dark Energy Spectroscopic Instrument Data Release 1, the largest public spectroscopic redshift sample.
- **Size:** 18,659,804 "useful" Main Survey spectra (13,049,402 galaxies, 1,553,713 quasars, 4,056,689 stars), plus 141,473 from special observations and 1,613,846 from commissioning/SV. The total TB volume is not stated on the page.
- **Coverage:** Main Survey Dark 9,528 deg², Bright 9,739 deg², Backup 2,726 deg²; observed May 2021 to June 2022.
- **Format:** FITS (DESI data model); LSS catalogs.
- **Access:** HTTPS `https://data.desi.lbl.gov/public/dr1` (EU mirror `https://webdav-hdfs.pic.es/data/public/DESI/DR1`); LSS catalogs via CosmoHub; the SPARCL API at NOIRLab for spectra (not mentioned on the DR1 page, unverified here); a `juliensimon/desi-dr1-redshifts` Parquet mirror on Hugging Face.
- **Auth:** no.
- **License:** CC BY 4.0, with the citation text required.
- **Time to first data:** minutes for catalogs, hours for bulk spectra.
- **Hackathon problem:** a 3-D cosmic-web fly-through of 18M galaxies; a spectral outlier search (rare quasars, lensed systems).
- **Sources:** [DESI DR1 release doc](https://data.desi.lbl.gov/doc/releases/dr1/), [HF juliensimon/desi-dr1-redshifts](https://huggingface.co/datasets/juliensimon/desi-dr1-redshifts)

#### Vera C. Rubin Observatory: DP1, EDP2 and the public alert stream
- **What:** LSST commissioning data previews, plus the real-time alert stream.
- **Size:**
  - DP1 covers 7 fields of ~1 deg² over 7 weeks in late 2024 (LSSTComCam), processed with Science Pipelines v29.
  - Early Data Preview 2 (EDP2) covers observations from April 2025 to January 2026, processed with v30.
  - Alerts: the full stream is expected to reach millions per night (volume per night not stated on the page).
- **Coverage:** southern sky; alerts are real time.
- **Format:** Rubin Science Platform (Butler, TAP, Portal) for the previews; Avro alert packets via brokers.
- **Access:**
  - **The alerts are "world public and have no proprietary period"**, and have been streaming to brokers since **24 February 2026**.
  - There are seven full-stream brokers: ALeRCE, AMPEL, ANTARES, Babamul, Fink, Lasair and Pitt-Google.
  - Python clients (versions from PyPI, checked live 2026-10-24): `pip install fink-client` (12.3.0), `alerce` (2.3.1), `antares-client` (2.0.2), `lasair` (0.1.4).
  - The Fink LSST REST API (Swagger) is at `https://api.lsst.fink-portal.org/` (checked live: 200).
- **Auth:**
  - DP1/EDP2: **yes, limited to Rubin data-rights holders** (scientists and students in the US and Chile plus named in-kind members); "Data are proprietary for two years after release."
  - Alerts: no for broker web/API queries (some brokers need a free account for Kafka streams).
- **License:** Rubin data policy; alerts are public.
- **Time to first data:** minutes for alerts through a broker API. Days or never for DP1 unless a teammate has US/Chile data rights (MIT students qualify as US scientists/students; account setup takes time).
- **Hackathon problem:** a transient triage assistant that ranks tonight's Rubin alerts for follow-up by small telescopes; a satellite-streak contamination tracker that cross-matches alerts with known satellites (SATCAT/TLE) to flag Starlink streaks.
- **Sources:** [DP1 docs](https://dp1.lsst.io/), [Rubin recent data releases (updated 23 Oct 2026)](https://rubinobservatory.org/for-scientists/data-products/recent-data-releases), [Rubin alerts and brokers](https://rubinobservatory.org/for-scientists/data-products/alerts-and-brokers), [Fink LSST API](https://api.lsst.fink-portal.org/), [Lasair LSST](https://lasair.lsst.ac.uk/)

#### Zwicky Transient Facility (ZTF) DR24 and alerts
- **What:** northern-sky time-domain survey (Palomar 48-inch, g/r/i).
- **Size:** DR24 (released 22 Jan 2026; observations March 2018 to October 2025) has 69.7M single-exposure images, 188k co-adds, 1,043 billion source detections and 5.32 billion light curves. **DR25 is scheduled for 20 Jan 2027.**
- **Coverage:** ~3π sky north of about −30°, 2018 to 2025.
- **Format:** FITS images; Parquet HATS catalogs on S3.
- **Access:**
  - IRSA (TAP, image services).
  - S3 objects table `s3://ipac-irsa-ztf/ztf/enhanced/dr24/objects/hats`; light curves `s3://ipac-irsa-ztf/ztf/enhanced/dr24/lc/hats` (us-east-1, no account).
  - Real-time alerts via ALeRCE, Fink and Lasair.
  - "Alerts and forced-photometry will continue to be available realtime."
- **Auth:** no.
- **License:** IRSA data use terms (cite DOIs 10.26131/IRSA597 and IRSA598).
- **Time to first data:** minutes (light curves via lsdb or the ALeRCE API).
- **Hackathon problem:** variable-star or supernova classifier; ZTF+Rubin cross-survey light-curve stitching.
- **Sources:** [ZTF public releases](https://www.ztf.caltech.edu/ztf-public-releases.html), [AWS registry ZTF](https://registry.opendata.aws/ztf/)

#### MAST public S3 bucket (`stpubdata`): TESS, Kepler, K2, HST, JWST, Pan-STARRS, GALEX, Gaia, SDSS, Roman
- **What:** STScI's Mikulski Archive mirror on AWS. The top-level prefixes, listed live 2026-10-24, are `gaia/ galex/ hst/ jwst/ k2/ kepler/ mast/ panstarrs/ roman/ sdss/ tess/`.
- **Size:** petabyte-scale in total; individual light-curve files are kB to MB.
- **Coverage:** HST 1990 to present; JWST 2022 to present (public after the proprietary period); TESS 2018 to present (nearly all-sky); Kepler 2009–2013 (~180,000 stars); K2 2014–2018; Pan-STARRS PS1 (sky north of −30°).
- **Format:** FITS.
- **Access:**
  - `s3://stpubdata/tess`, `s3://stpubdata/kepler`, `s3://stpubdata/k2`, `s3://stpubdata/hst`, `s3://stpubdata/jwst`, `s3://stpubdata/panstarrs/ps1`, `s3://stpubdata/galex` (us-east-1, `--no-sign-request`).
  - High-Level Science Products: `s3://stpubdata/mast/hlsp/qlp` (MIT Quick-Look Pipeline TESS light curves), `.../hlsp/tess-spoc`, `.../hlsp/tglc` (TESS-Gaia light curves), `.../hlsp/jades` (JWST JADES).
  - `pip install lightkurve` (2.6.0, 2026-04-16): `lightkurve.search_lightcurve("TIC 25155310").download()`.
  - `astroquery.mast` (0.4.11).
- **Auth:** no.
- **License:** public domain with attribution for the mission data; HLSPs follow MAST HLSP terms; Pan-STARRS has an STScI grant license.
- **Time to first data:** minutes.
- **Hackathon problem:** a citizen-science "planet hunter" that flags new transit candidates in TESS full-frame-image light curves; JWST image explorer; a satellite-trail detector for HST/TESS frames (a real and growing contamination problem).
- **Sources:** [AWS registry: TESS](https://registry.opendata.aws/tess/), [Kepler](https://registry.opendata.aws/kepler/), [HST](https://registry.opendata.aws/hst/), [JWST](https://registry.opendata.aws/jwst/), [Pan-STARRS](https://registry.opendata.aws/panstarrs/), [QLP](https://registry.opendata.aws/mast-qlp/), [TGLC](https://registry.opendata.aws/mast-tglc/), [JADES](https://registry.opendata.aws/mast-jades/), [AWS astronomy tag listing](https://registry.opendata.aws/tag/astronomy/), [PyPI lightkurve](https://pypi.org/project/lightkurve/)

#### NASA Exoplanet Archive
- **What:** the curated database of confirmed exoplanets, TESS Objects of Interest, Kepler candidates, and stellar and planet parameters.
- **Size (checked live 2026-10-24 via TAP):**
  - `pscomppars` (one row per confirmed planet): **6,451 planets**
  - `ps` (all parameter sets): 40,350 rows
  - `toi`: 8,151 TESS Objects of Interest
- **Coverage:** all known exoplanets.
- **Format:** CSV/VOTable/JSON via TAP.
- **Access:** `https://exoplanetarchive.ipac.caltech.edu/TAP/sync?query=select+*+from+pscomppars&format=csv`; `astroquery.ipac.nexsci.nasa_exoplanet_archive`; daily Parquet mirrors on Hugging Face (`juliensimon/nasa-exoplanets`, `juliensimon/tess-toi-candidates`).
- **Auth:** no.
- **License:** public, with acknowledgement requested.
- **Time to first data:** under 5 minutes.
- **Hackathon problem:** a "which TOIs are most worth confirming next" ranker for amateur and small-telescope observers; a habitable-zone target list for future missions (HWO).
- **Sources:** [NASA Exoplanet Archive TAP](https://exoplanetarchive.ipac.caltech.edu/docs/TAP/usingTAP.html), [HF nasa-exoplanets](https://huggingface.co/datasets/juliensimon/nasa-exoplanets)

#### Euclid Quick Release 1 (Q1)
- **What:** ESA Euclid's first quick release: VIS and NISP imaging, slitless spectra, MER mosaics and catalogs, photometric redshifts.
- **Size:** about **35 TB**; three deep fields total ~63.1 deg² (Euclid Deep Field North 22.9, Fornax 12.1, South 28.1), plus LDN1641.
- **Coverage:** Q1 was released in March 2025 (the AWS registry says it "has been finalized and will not be updated"). **Euclid DR1 was revised on 15 June 2026 into two stages.** "In November 2026, Euclid will release all raw data and calibrated images" plus catalogues and spectra, over about **1,900 deg²** ("DR1-Foundation"). The full DR1 with weak-lensing and clustering products "will then follow in mid-2027". The exact November day is to be posted on the ESA timeline. NASA/IPAC pages still show the old 21 Oct 2026 date. A gated HF dataset `mwalmsley/euclid_dr1` already exists.
- **Format:** FITS (MER tiles, NIR/VIS frames, SIR spectra), catalogs.
- **Access:**
  - IRSA (TAP, SIA, SSA, Euclid Data Explorer, astroquery).
  - S3 `s3://nasa-irsa-euclid-q1/q1/MER`, `.../q1/MER_SEG`, `.../q1/NIR`, `.../q1/VIS`, `.../q1/SIR` (us-east-1; "RequesterPays: False, AccountRequired: False").
  - ESA Euclid archive.
  - Galaxy Zoo Euclid labels plus embeddings on HF (`mwalmsley/gz_euclid`, `mwalmsley/euclid_q1_embeddings`).
- **Auth:** no.
- **License:** IRSA data use terms.
- **Time to first data:** minutes for cutouts, hours for tiles.
- **Hackathon problem:** a strong-lens finder (`mwalmsley/euclid_strong_lens_expert_judges` exists on HF); a galaxy-morphology search engine over Euclid embeddings.
- **Sources:** [IRSA Euclid Q1 overview](https://irsa.ipac.caltech.edu/data/Euclid/docs/overview_q1.html), [AWS registry Euclid Q1](https://registry.opendata.aws/euclid-q1/), [HF mwalmsley datasets](https://huggingface.co/mwalmsley), [ESA Euclid DR1 timeline (15 Jun 2026 update)](https://www.cosmos.esa.int/web/euclid/dr1-timeline), [IPAC Euclid DR1 page (outdated date)](https://euclid.caltech.edu/page/euclid-dr1), [telescoper.blog on the split release (blog)](https://telescoper.blog/tag/esa-euclid/)

#### SPHEREx Quick Release (QR2)
- **What:** NASA SPHEREx (launched March 2025), the first all-sky spectral survey, covering 0.75–5 µm in 102 bands.
- **Size:** growing weekly; spectral images with variance and zodiacal models, PSFs and gain matrices.
- **Coverage:** all sky; "SPHEREx QR is updated weekly."
- **Format:** multi-extension FITS.
- **Access:** `s3://nasa-irsa-spherex/qr2/level2` (plus `qr2/abs_gain_matrix`, `qr2/average_psf`, `qr2/dark` and others; us-east-1, no account); IRSA services.
- **Auth:** no.
- **License:** IRSA data use terms (DOIs 10.26131/IRSA629 and IRSA652).
- **Time to first data:** minutes for one image.
- **Hackathon problem:** a "spectrum of any pixel of the sky" web viewer; ice-absorption mapping.
- **Sources:** [AWS registry SPHEREx QR](https://registry.opendata.aws/spherex-qr/), [IRSA SPHEREx](https://irsa.ipac.caltech.edu/Missions/spherex.html)

#### WISE / NEOWISE / unWISE (IRSA on AWS)
- **What:** infrared all-sky survey images and catalogs. AllWISE has 747M+ objects. NEOWISE Reactivation ran 2013–2024 (decommissioned 2024).
- **Size:** tens of TB.
- **Coverage:** all sky, 2010–2024.
- **Format:** FITS, Parquet catalogs.
- **Access:** `s3://nasa-irsa-wise/wise/allwise`, `.../wise/allsky`, `.../wise/neowiser`, `.../wise/postcryo`, `.../wise/cryo-3band`, `s3://nasa-irsa-wise/unwise/` (us-west-2).
- **Auth:** no.
- **License:** IRSA data use terms.
- **Time to first data:** minutes.
- **Hackathon problem:** a NEO thermal-size estimator (NEOWISE fluxes give diameters, hence impact energy).
- **Sources:** [AWS astronomy listing](https://registry.opendata.aws/tag/astronomy/), [AWS registry NEOWISE Reactivation](https://registry.opendata.aws/wise-neowiser/)

#### Other astronomy datasets on the AWS Open Data Registry (verified from the registry metadata, 2026-10-24)
Each item: bucket; license; hackathon angle where relevant. Source: [AWS registry astronomy tag](https://registry.opendata.aws/tag/astronomy/) and the [registry GitHub repo](https://github.com/awslabs/open-data-registry).
- **NASA HEASARC high-energy mission archive** (X-ray and gamma-ray: Chandra, Swift, Fermi, XMM and others): see [registry entry](https://registry.opendata.aws/nasa-heasarc/).
- **NASA LAMBDA:** CMB mission data and maps; [registry](https://registry.opendata.aws/nasa-lambda/).
- **ASKAP RACS-low** radio survey: `s3://askap-odp/racs-low1/` (ap-southeast-2); CC BY 4.0.
- **LOFAR ELAIS-N1 cycle 2:** `s3://lofar-elais-n1` (us-east-1).
- **MWA Epoch of Reionization:** `s3://mwapublic` (us-east-1); BSD-2-Clause.
- **MeerKAT ESO 137-006:** `s3://ratt-public-data/ESO137` (af-south-1); CC BY 4.0.
- **OVRO-LWA solar observations:** `s3://ovro-lwa-solar` (us-west-2); CC BY 4.0 (also heliophysics).
- **Open VLF (CRAAM):** `s3://craam-files-bucket` (sa-east-1). VLF radio for solar-flare ionospheric effects.
- **OpenUniverse 2024 simulated Roman and Rubin images:** `s3://nasa-irsa-simulations/openuniverse2024/roman/` (us-east-1).
- **Spitzer SEIP super mosaics:** `s3://nasa-irsa-spitzer/spitzer/seip` (us-west-2).
- **NASA Astrophysics Division Galaxy Morphology benchmark** (Hubble images with morphology labels): `s3://nasa-apd-galaxymorph` (us-west-2); "no restrictions".
- **NASA APD Galaxy Segmentation benchmark** (Pan-STARRS images with component labels): `s3://nasa-apd-galaxysegment` (us-west-2).
- **NASA SOHO/LASCO C2 comet challenge:** `s3://nasa-comets-training-data` (us-east-1). About 36,000 images across 2,950 comet observations, from the Topcoder challenge that found 2 new comets; "no restrictions". The angle: an ML sungrazing-comet hunter.
- **Catalina Sky Survey raw data (PDS SBN):** `s3://pds-css-archive` (us-west-2). NEO-discovery survey images delivered nightly since 20 Jan 2022; "no restrictions". The angle: a moving-object (asteroid) detector. Pair it with the CATCH moving-target search service.

#### Satellite-streak contamination datasets (megaconstellations vs. astronomy): Zenodo cluster
A ready-made, very clear space-sector problem: LEO constellations (Starlink, Kuiper, AST SpaceMobile BlueWalker/BlueBird) leave streaks in telescope images. All entries below are from the Zenodo REST API (`https://zenodo.org/api/records?q=...&type=dataset`, queried 2026-10-24; sizes are the sum of files).
- **StreaksYoloDataset:** labeled raw astronomical images for streak detection (YOLO format); 1.4 GB; CC BY 4.0; 2024-11-06. [doi:10.5281/zenodo.14047944](https://doi.org/10.5281/zenodo.14047944)
- **ASTA (Automated Satellite Tracking for Astronomy) dataset:** 17.95 GB; CC BY 4.0; 2024-07-13. [doi:10.5281/zenodo.11642424](https://doi.org/10.5281/zenodo.11642424)
- **"The Impact of Satellite Trails on Hubble Space Telescope Observations": satellite classifications** (Kruk et al.); 0.17 GB; CC BY 4.0; 2022-12-22. [doi:10.5281/zenodo.7474191](https://doi.org/10.5281/zenodo.7474191)
- **"SPHEREx confirms predictions for artificial satellite trail pollution in Low Earth Orbit":** 0.15 GB; CC BY 4.0; 2025-12-17. [doi:10.5281/zenodo.17957748](https://doi.org/10.5281/zenodo.17957748)
- **"Satellite Streaks in HETDEX: Spectra, Orbital Identification, and Survey Impact"** (data and code): 0.15 GB; CC BY 4.0; **October 2026** (brand new). [doi:10.5281/zenodo.22962479](https://doi.org/10.5281/zenodo.22962479)
- **Raw FITS and AAV data of the BlueWalker 3 LEO communication satellite:** 21.27 GB; CC BY 4.0; 2023-07-11. [doi:10.5281/zenodo.8102655](https://doi.org/10.5281/zenodo.8102655)
- **Context Trails data:** 0.1 GB; CC BY-NC 4.0; 2025-07-10. [doi:10.5281/zenodo.15855966](https://doi.org/10.5281/zenodo.15855966)
- **Hackathon problem:** a "streak forecaster plus masker". It predicts which satellites will cross a given telescope's field tonight (CelesTrak/Starlink TLEs and SGP4), detects streaks in images (StreaksYolo/ASTA), and identifies the satellite responsible. It doubles as an evidence tool for regulators (brightness vs. IAU limits). Pairs with Rubin alerts, the HST/TESS archives and the HF `starlink-tle-latest` table.

#### Other Zenodo astronomy and planetary finds (same API query, 2026-10-24)
- **ELAsTiCC training alerts** (Rubin-style simulated alert stream): [doi:10.5281/zenodo.7108318](https://doi.org/10.5281/zenodo.7108318). **PLAsTiCC unblinded data** (7.5 GB, CC BY 4.0): [doi:10.5281/zenodo.2539456](https://doi.org/10.5281/zenodo.2539456). PLAsTiCC model sets of 31–50 GB each (for example [doi:10.5281/zenodo.3609224](https://doi.org/10.5281/zenodo.3609224)).
- **GWTC-4.0 parameter-estimation data release** (14.38 GB, CC BY 4.0, 2026-05-22): [doi:10.5281/zenodo.17602505](https://doi.org/10.5281/zenodo.17602505).
- **Galaxy Zoo 2 images (original sample)** (3.37 GB, CC BY 4.0): [doi:10.5281/zenodo.3565489](https://doi.org/10.5281/zenodo.3565489).
- **Quaia, the Gaia-unWISE quasar catalog** (0.68 GB): [doi:10.5281/zenodo.10403370](https://doi.org/10.5281/zenodo.10403370).
- **"Deep learning-assisted near-Earth asteroid tracking in astronomical images" data** (0.18 GB): [doi:10.5281/zenodo.10440838](https://doi.org/10.5281/zenodo.10440838).
- **Lunar:**
  - LU1319373, an improved global catalog of lunar craters ≥1 km with 3D morphometry (CC BY 4.0): [doi:10.5281/zenodo.4983248](https://doi.org/10.5281/zenodo.4983248)
  - Tycho-region database of craters ≥21 m (0.71 GB): [doi:10.5281/zenodo.14715016](https://doi.org/10.5281/zenodo.14715016)
  - Extent of past PSRs at both lunar poles (0.26 GB): [doi:10.5281/zenodo.14885276](https://doi.org/10.5281/zenodo.14885276)
  - "Evidence for Water Ice in Lunar Permanently Shadowed Regions using neutrons, topography…" data and software (2.44 GB, NASA Open Source Agreement 1.3): [doi:10.5281/zenodo.14002739](https://doi.org/10.5281/zenodo.14002739)
  - Wueller et al. (2026), landing sites with favourable illumination: [doi:10.5281/zenodo.17084058](https://doi.org/10.5281/zenodo.17084058)
  - Lunar cold spot at Apollo 16 South Ray crater (2.61 GB): [doi:10.5281/zenodo.15700321](https://doi.org/10.5281/zenodo.15700321)
- **Mars:**
  - Mars crater production-function shapefiles: [doi:10.5281/zenodo.13553821](https://doi.org/10.5281/zenodo.13553821)
  - Multi-resolution basemap of NW Aeolis Mons, Gale crater (39.6 GB): [doi:10.5281/zenodo.5808381](https://doi.org/10.5281/zenodo.5808381)
- **Ceres:** bright deposits in permanently shadowed craters (0.22 GB): [doi:10.5281/zenodo.11908583](https://doi.org/10.5281/zenodo.11908583).

#### LIGO/Virgo/KAGRA: GWOSC
- **What:** Gravitational Wave Open Science Center: strain data and event catalogs.
- **Size (checked live 2026-10-24):** the `allevents` API returns **671 event entries** (counting catalog versions): GWTC-5.0 (161), GWTC-4.1 (140), GWTC-4.0 (129), GWTC-2.1-confident (54), IAS-O3a (42), GWTC-2 (39), GWTC-3-confident (35), plus others. Bulk strain from O1 to O3 is TB-scale; O4 strain releases are ongoing.
- **Coverage:** 2015 to present.
- **Format:** HDF5/GWF strain; JSON event API.
- **Access:** `https://gwosc.org/eventapi/json/allevents/`; `pip install gwosc` (0.8.3) and `gwpy` (4.1.0, 2026-10-13); `gwpy.timeseries.TimeSeries.fetch_open_data('L1', t0, t1)`.
- **Auth:** no.
- **License:** CC BY 4.0 (GWOSC policy; verify per release).
- **Time to first data:** minutes.
- **Hackathon problem:** a sonified, interactive "listen to black-hole mergers" explainer; a glitch classifier for detector noise.
- **Sources:** [GWOSC event API](https://gwosc.org/eventapi/json/allevents/), [PyPI gwpy](https://pypi.org/project/gwpy/), [PyPI gwosc](https://pypi.org/project/gwosc/)

#### Galaxy Zoo labels (Zooniverse) on Hugging Face
- **What:** volunteer morphology vote fractions for galaxies from SDSS (GZ2), DECaLS/DESI (GZ DESI), Hubble, CANDELS, UKIDSS, JWST-COSMOS and Euclid. They ship with images, and embeddings exist for some sets (Zoobot).
- **Size:** the HF org `mwalmsley` has 35 datasets (`gz2`, `gz_desi`, `gz_hubble`, `gz_candels`, `gz_ukidss`, `gz_euclid`, `gz_evo`, `gz_jwst_cosmos`, `galaxy10_decals`, `euclid_q1_embeddings`, `zoobot-encoder-desi` and more; checked live). Galaxy10 DECaLS has ~17.7k images (sample count not verified on page).
- **Coverage:** hundreds of thousands to millions of galaxies.
- **Format:** HF Parquet (images plus vote columns).
- **Access:** `load_dataset("mwalmsley/gz_euclid")`.
- **Auth:** no (some, like `euclid_dr1`, are gated).
- **License:** per card (check).
- **Time to first data:** minutes.
- **Hackathon problem:** a "find me galaxies like this one" similarity search; rare-object discovery (rings, mergers, lenses).
- **Sources:** [HF mwalmsley](https://huggingface.co/mwalmsley), [HF gz_euclid card](https://huggingface.co/datasets/mwalmsley/gz_euclid)

#### Multimodal Universe (Polymathic AI / Flatiron, NeurIPS 2024)
- **What:** ML-ready collection of astronomical images, spectra, light curves and tables, aligned for multimodal models.
- **Size:** "100TBs of Astronomical Scientific Data". Sub-datasets include:
  - Images: Legacy Surveys DR10 (124M), HSC (477k), JWST (300k)
  - Spectra: Gaia BP/RP (220M), DESI (20M), SDSS-II (4M), APOGEE (716k), Chandra (129k)
  - Hyperspectral: MaNGA (12k)
  - Time series: PLAsTiCC (3.5M), TESS (160k)
  - Tables: AllWISE (747M), 2MASS (471M), and others
- **Coverage:** multi-survey, sky-wide.
- **Format:** HDF5 with HF dataset loaders.
- **Access:** HF previews of about 1k examples per survey (`load_dataset('MultimodalUniverse/plasticc', split='train', streaming=True)`). The full data is at `https://users.flatironinstitute.org/~polymathic/data/MultimodalUniverse` or via Globus (preferred for bulk). The HF org lists 24 sub-datasets: snls, gaia, vipers, yse, sdss, desi_provabgs, plasticc, hsc, desi, tess, swift_sne_ia, ssl_legacysurvey, foundation, apogee, ps1_sne_ia, des_y3_sne_ia, jwst, gz10, chandra, cfa, csp, btsbot, manga, legacysurvey.
- **Auth:** no.
- **License:** CC BY 4.0, with sub-survey terms also applying; code is MIT.
- **Time to first data:** minutes for HF streaming, hours for full subsets.
- **Hackathon problem:** a cross-modal search ("show me spectra of galaxies that look like this image").
- **Sources:** [MMU GitHub](https://github.com/MultimodalUniverse/MultimodalUniverse), [arXiv 2412.02527](https://arxiv.org/abs/2412.02527), [HF MultimodalUniverse](https://huggingface.co/MultimodalUniverse)

#### AstroCLIP training data (DESI Legacy Survey images and DESI EDR spectra)
- **What:** a cross-matched image-spectrum galaxy dataset (Stein et al. 2022 images; DESI EDR spectra). **It ships with models:** AstroCLIP (370M params), AstroDINO image encoder (302M) and SpecFormer spectrum encoder (43M), all on HF under `polymathic-ai`.
- **Size:** the HF loader "downloads about 60 GB"; the full image set is 76M galaxy images (HDF5 via Globus, in 1M-galaxy chunks).
- **Coverage:** the DESI Legacy Survey footprint.
- **Format:** HDF5 / HF datasets.
- **Access:** `load_dataset('astroclip/data/dataset.py')` from the repo; weights at `huggingface.co/polymathic-ai/astroclip`.
- **Auth:** no.
- **License:** code and weights MIT.
- **Time to first data:** about 1 hour (60 GB).
- **Hackathon problem:** a photometric-redshift or galaxy-property predictor from images alone.
- **Sources:** [AstroCLIP GitHub](https://github.com/PolymathicAI/AstroCLIP)

#### eROSITA-DE DR1
- **What:** the German half of SRG/eROSITA's first all-sky X-ray survey (eRASS1).
- **Size:** event lists, images, exposure, background and sensitivity maps, upper limits, catalogs (source count not stated on page; a 930,203-row eRASS1 mirror exists on HF as `juliensimon/erosita-erass1-xray`).
- **Coverage:** Western Galactic hemisphere, 20,626.5 deg²; first six months of eRASS1. Released 31 Jan 2024.
- **Format:** FITS, HiPS.
- **Access:** eRODat tool, catalog page, HiPS; eSASS4DR1 software.
- **Auth:** no.
- **License:** acknowledgement requested.
- **Time to first data:** minutes for catalogs.
- **Hackathon problem:** X-ray/optical cross-match to find new AGN or cataclysmic variables.
- **Sources:** [eROSITA-DE DR1](https://erosita.mpe.mpg.de/dr1/), [HF erosita-erass1-xray](https://huggingface.co/datasets/juliensimon/erosita-erass1-xray)

#### Hugging Face "space datasets" collection by Julien Simon (~200 daily-refreshed space tables)
- **What:** a large, actively maintained set of Parquet mirrors of space catalogs and feeds, most refreshed daily (lastModified 2026-10-24 for many), driven by the GitHub repo `juliensimon/space-datasets`. It is the fastest path to tabular space data in a hackathon. Highlights (row counts from the repo's `status.json` where seen):
  - **Orbital:**
    - `space-track-tle-history`: **238M rows, 1959–2026, 68 Parquet files, 12.5 GB total**; tagged CC-BY-4.0 but sourced from Space-Track, see Gotchas
    - `space-track-satcat`, `starlink-tle-latest` (Starlink and GPS TLEs, daily from CelesTrak), `constellation-tle-latest`, `constellation-census`
    - `satellite-conjunctions`: SOCRATES near-misses ≤1 km or Pc ≥1e-4, deduplicated, 871,973 rows
    - `reentry-events`, `orbital-fragmentation-events`, `gcat-satellite-catalog` (68,538 rows), `gcat-launch-vehicles`, `gcat-deep-space`, `ucs-satellite-database`
    - `wmo-oscar-satellites`, `fcc-ngso-filings`
    - fleet tables: `starlink-fleet-data`, `kuiper-fleet-data`, `oneweb-fleet-data`, `ast-spacemobile-fleet-data`, `globalstar-fleet-data`
    - `starlink-ground-stations`, `iers-earth-orientation`, `satnogs-transmitters`
  - **Launch:** `spacex-launches`, `rocket-lab-launches`, `blue-origin-launches`, `ula-launches`, `space-launch-log`, `launch-vehicles`, `space-missions`, `artemis-ii`, `deep-space-missions-tracker`, `deep-space-probes`, `astronaut-database`, `space-tourism-flights`.
  - **Space weather:**
    - `f107-solar-flux`, `goes-xray-flux` (187,477 rows), `solar-wind`, `omni-solar-wind-parameters`
    - indices: `dst-index` (588,809 rows), `geomagnetic-kp-index`, `auroral-electrojet-index`, `space-weather-indices`, `celestrak-space-weather`, `silso-sunspot-number`
    - events and feeds: `swpc-alerts`, `donki-space-weather-events`, `solar-flare-events`, `solar-radio-bursts`, `cdaw-lasco-cme-catalog` (42,744 rows), `feng-icme-catalog`, `aurora-forecast`, `substorm-onsets`
    - cosmic rays: `neutron-monitor-cosmic-rays`, `forbush-decreases`
  - **Small bodies and planetary:**
    - `jpl-small-body-database`, `sentry-impact-risk`, `neo-close-approaches`, `nhats-accessible-asteroids`, `fireball-bolide-events`
    - meteors and meteorites: `global-meteor-network` (3,628,403 rows), `meteorite-database`, `meteorite-landings`
    - craters: `lunar-craters-robbins`, `mars-craters-robbins`, `ceres-craters-dawn`, `mercury-craters-herrick`, `impact-craters`
    - Mars: `mars-perseverance-weather`, `nasa-mars-rover-images`, `mars-chemcam-compositions`, `insight-marsquake-catalog`
    - other: `lunar-sample-geochemistry`, `pds-planetary-missions`, `planetary-nomenclature`
    - ESA mission logs: `esa-exomars-tgo-observations` (27.7M rows), `esa-bepicolombo-observations`, `esa-juice-observations`, `esa-rosetta-observations`, `esa-mars-express-observations`
  - **Astronomy:** `nasa-exoplanets` (6,451 rows), `tess-toi-candidates`, `jwst-observations`, `hst-observations`, `gravitational-wave-events`, `gw-candidate-alerts`, `fermi-gbm-triggers`, `gamma-ray-bursts`, `chime-frb-catalog`, `erosita-erass1-xray`, `desi-dr1-redshifts`, `galaxy-zoo-2-morphology`, many Gaia DR3 sub-catalogs, `pulsar-catalog`, `open-supernova-catalog`, `nasa-apod`, and `stackexchange-space-qa` (text).
- **Size:** kB to 12.5 GB per dataset.
- **Format:** Parquet (some ship raw `.tle` alongside).
- **Access:** `load_dataset("juliensimon/<name>")`, or DuckDB `read_parquet('hf://datasets/juliensimon/space-track-tle-history/data/tle_2024.parquet')`.
- **Auth:** no.
- **License:** per card. Several say `celestrak-usage-policy` (other); TLE history says CC-BY-4.0 despite its Space-Track origin.
- **Time to first data:** under 5 minutes.
- **Hackathon problem:** nearly any orbital, space-weather or NEO dashboard can start here. For example, "conjunction rate vs. solar activity", "which constellations cause the most near-misses", or "reentry risk map".
- **Sources:** [HF juliensimon datasets](https://huggingface.co/juliensimon), [Orbital mechanics collection](https://huggingface.co/collections/juliensimon/orbital-mechanics-datasets-69c24caca4ab3934c9856994), [space-track-tle-history card](https://huggingface.co/datasets/juliensimon/space-track-tle-history), [satellite-conjunctions card](https://huggingface.co/datasets/juliensimon/satellite-conjunctions), [status.json](https://raw.githubusercontent.com/juliensimon/space-datasets/main/status.json)

### 2.7 Heliophysics / space weather

#### NOAA SWPC real-time JSON services (solar wind, X-rays, Kp, alerts)
- **What:** operational space-weather feeds behind the SWPC dashboards.
- **Size and recency (checked live 2026-10-24):**
  - `json/rtsw/rtsw_wind_1m.json`: 3,400 one-minute rows; the latest at 2026-10-24 22:03 had **`"source": "IMAP"`**, proton speed 367 km/s, density 5.25 cm⁻³. **NOAA's real-time solar wind now comes from NASA's IMAP at L1.**
  - `json/goes/primary/xrays-7-day.json`: 20,140 rows; latest flux 4.5×10⁻⁷ W/m² (B-class level) from GOES-18.
  - `products/noaa-planetary-k-index.json`: latest Kp 1.67 at 2026-10-24 18:00.
  - **The legacy `products/solar-wind/plasma-7-day.json` returned 404**: old tutorials break, so use the `json/rtsw/` endpoints.
- **Format:** JSON.
- **Access:** `https://services.swpc.noaa.gov/json/...`, `https://services.swpc.noaa.gov/products/...`; archive copy in `s3://noaa-swpc-pds` (`json/`, `products/`, `text/`; public).
- **Auth:** no.
- **License:** NOAA open.
- **Time to first data:** under 1 minute.
- **Hackathon problem:** **"satellite-operator space-weather copilot"**: translate solar wind, Kp and X-ray flux into plain-language risk for LEO drag, GNSS errors, HF radio and astronaut EVAs. The Feb 2022 Starlink loss of 38 satellites to a minor storm is the canonical story.
- **Sources:** [SWPC RTSW wind (live)](https://services.swpc.noaa.gov/json/rtsw/rtsw_wind_1m.json), [SWPC GOES X-rays (live)](https://services.swpc.noaa.gov/json/goes/primary/xrays-7-day.json), [SWPC Kp (live)](https://services.swpc.noaa.gov/products/noaa-planetary-k-index.json), [AWS registry NOAA space weather](https://registry.opendata.aws/noaa-space-weather/)

#### GFZ Potsdam Kp / ap / Hp30 (definitive geomagnetic indices)
- **What:** the official Kp index since 1932.
- **Access:** `https://kp.gfz.de/app/json/?start=2026-10-20T00:00:00Z&end=2026-10-24T00:00:00Z&index=Kp` (checked live; three-hourly values, max 4.667 on 21 Oct).
- **Auth:** no.
- **License:** CC BY 4.0 (per GFZ; unverified here).
- **Time to first data:** under 1 minute.
- **Hackathon problem:** labels for storm prediction; drag versus Kp correlation for Starlink decay (with the TLE history).
- **Sources:** [GFZ Kp JSON API (live)](https://kp.gfz.de/app/json/?start=2026-10-20T00:00:00Z&end=2026-10-24T00:00:00Z&index=Kp)

#### Surya Bench and core-SDO (NASA-IBM heliophysics foundation-model data)
- **What:** ML-ready SDO AIA (8 EUV/UV channels) and HMI (LOS and vector magnetograms) at Level 1.5, from 13 May 2010 to 31 Dec 2024. **Ships with the Surya heliophysics foundation model.**
- **Downstream HF tasks:**
  - `surya-bench-flare-forecasting`: 8.8 MB of labels; ≥M1.0 within a 24 h window, 2010–2024
  - `Surya-bench-solarwind`
  - `surya-bench-ar-segmentation`
  - `surya-bench-coronal-extrapolation`
  - `ar_emergence`
  - `euv-spectra`
- **Size:** `nasa-ibm-ai4science/core-sdo` is **363 GB**. `s3://nasa-surya-bench/` has year prefixes 2010–2024 (listed live).
- **Format:** NetCDF/Zarr-style arrays; CSV labels.
- **Access:** `aws s3 ls --no-sign-request s3://nasa-surya-bench/` (us-west-2); `load_dataset("nasa-ibm-ai4science/surya-bench-flare-forecasting")`.
- **Auth:** no.
- **License:** CC BY 4.0.
- **Time to first data:** minutes for labels; hours for image cubes.
- **Hackathon problem:** a 24-hour flare-risk forecaster for crewed missions (Artemis EVA planning); solar-wind speed prediction three days ahead.
- **Sources:** [AWS registry Surya Bench](https://registry.opendata.aws/surya-bench/), [HF core-sdo card](https://huggingface.co/datasets/nasa-ibm-ai4science/core-sdo), [HF flare-forecasting card](https://huggingface.co/datasets/nasa-ibm-ai4science/surya-bench-flare-forecasting)

#### SDOML v2 (FDL ML-ready SDO dataset)
- **What:** the Galvez et al. (2019) SDO ML dataset (AIA, HMI, EVE), re-packaged as cloud-friendly Zarr in v2 with "All fits header information … saved in the meta data".
- **Access:** HelioCloud public bucket **`s3://gov-nasa-hdrl-data1/contrib/fdl-sdoml/fdl-sdoml-v2/`** (also `.../fdml-sdomlv1/`; listed live); processing scripts in the SDOMLv2 GitHub repo.
- **Auth:** no.
- **License:** see the repo and paper (unverified).
- **Time to first data:** 15–30 minutes.
- **Hackathon problem:** a coronal-hole to solar-wind forecaster; EUV-irradiance nowcast for satellite drag.
- **Sources:** [HelioCloud bucket listing (live)](https://gov-nasa-hdrl-data1.s3.amazonaws.com/?list-type=2&delimiter=/&prefix=contrib/fdl-sdoml/), [SDOMLv2 README](https://raw.githubusercontent.com/SDOML/SDOMLv2/main/README.md), [Galvez et al. 2019 (ADS)](http://adsabs.harvard.edu/abs/2019ApJS..242....7G)

#### NOAA space-weather model and instrument buckets (NODD, all public)
- **GOES-19 CCOR-1 coronagraph** (SWFO): `s3://noaa-nesdis-swfo-ccor-1-pds`, "96 files per day per level" (FITS) plus daily telemetry and attitude files. The angle: automatic CME detection and arrival-time estimation.
- **WSA-Enlil CME runs** (full 3-D datacubes for runs with CMEs): `s3://noaa-wsa-enlil-pds`.
- **WAM-IPE** thermosphere and ionosphere: neutral density 100–1000 km every 10 minutes, 2-day forecasts four times daily; `s3://noaa-nws-wam-ipe-pds`. The angle: **a LEO drag and reentry-risk forecaster.**
- **DMSP SSJ auroral particle flux:** `s3://dmspssj` (CC0).
- **GNSS radio occultation** (ionosphere and atmosphere): `s3://gnss-ro-data`.
- **Sources:** [AWS registry CCOR-1](https://registry.opendata.aws/noaa-nesdis-swfo-ccor-1-pds/), [AWS registry WSA-Enlil](https://registry.opendata.aws/noaa-wsa-enlil/), [AWS registry WAM-IPE](https://registry.opendata.aws/noaa-nws-wam-ipe/), [AWS registry DMSP SSJ](https://registry.opendata.aws/dmspssj/)

#### OMNIWeb / CDAWeb (SPDF), Parker Solar Probe, DONKI, JSOC, SOAR
- **OMNI** (multi-spacecraft solar wind at 1 AU, 1963 to present), **CDAWeb** (thousands of heliophysics datasets including Parker Solar Probe FIELDS, SWEAP and ISOIS), and **CCMC DONKI** (flares, CMEs, SEPs, storms).
  - **All three GSFC hosts timed out from this network on 2026-10-24** (`cdaweb.gsfc.nasa.gov/hapi/catalog`, `spdf.gsfc.nasa.gov/pub/data/omni/...`, `kauai.ccmc.gsfc.nasa.gov/DONKI/...`), so they are not verified live.
  - Clients: `pip install cdasws` (1.8.18) and `hapiclient` (0.3.3). DONKI is also on `api.nasa.gov/DONKI/...` (key needed; DEMO_KEY was rate-limited).
  - HF daily mirrors avoid the outage: `juliensimon/omni-solar-wind-parameters`, `donki-space-weather-events`, `dst-index`, `geomagnetic-kp-index`, `goes-xray-flux`, `solar-flare-events`, `cdaw-lasco-cme-catalog`, `parker-solar-probe-encounters`.
- **JSOC (raw SDO):** `pip install drms` (0.9.1), with email registration for exports.
- **Solar Orbiter (SOAR):** `pip install sunpy-soar` (1.12.0); `sunpy` 8.0.1.
- **Time to first data:** minutes via HF; unknown for GSFC today.
- **Sources:** [PyPI cdasws](https://pypi.org/project/cdasws/), [PyPI hapiclient](https://pypi.org/project/hapiclient/), [PyPI drms](https://pypi.org/project/drms/), [PyPI sunpy-soar](https://pypi.org/project/sunpy-soar/), [HF juliensimon](https://huggingface.co/juliensimon)

#### Radio and particle data relevant to space weather (AWS, from 2.6)
- **OVRO-LWA solar** imaging spectroscopy: `s3://ovro-lwa-solar`.
- **CRAAM Open VLF** ionospheric flare signatures: `s3://craam-files-bucket`.
- HF `juliensimon/neutron-monitor-cosmic-rays`, `forbush-decreases`, `solar-radio-bursts`, `swpc-alerts`, `aurora-forecast`.

### 2.8 Planetary

#### JPL Solar System Dynamics APIs (SBDB, SBDB Query, CAD, Sentry, Scout, Fireball, NHATS, Horizons)
- **What:** JPL's small-body orbit database and derived services: close approaches, impact monitoring, NEO confirmation-page triage, bolides, human-accessible targets, ephemerides.
- **Size (checked live 2026-10-24):** SBDB Query reports **1,580,992 small bodies**. Sentry lists **2,226 objects** with non-zero impact probability. Scout has **38 current unconfirmed objects**. The CAD API returned **32 approaches within 0.05 au in the next 60 days** (for example 2026 UE at 0.0134 au on 25 Oct 2026). The Fireball API's latest event is 2026-10-04 (5.4 ×10¹⁰ J radiated).
- **Coverage:** all known asteroids and comets.
- **Format:** JSON REST.
- **Access:**
  - `https://ssd-api.jpl.nasa.gov/sbdb.api?sstr=99942` (Apophis)
  - `.../sbdb_query.api`
  - `.../cad.api?date-min=now&date-max=%2B60&dist-max=0.05`
  - `.../sentry.api`
  - `.../scout.api`
  - `.../fireball.api`
  - `.../nhats.api`
  - Horizons: `astroquery.jplhorizons`
- **Auth:** no.
- **License:** US government public data.
- **Time to first data:** under 2 minutes.
- **Hackathon problem:** a planetary-defense "impact risk explainer" or alerting bot (Torino/Palermo scale in plain English); a NEO follow-up prioritizer for amateur observers (Scout/NEOCP); an asteroid-mining target ranker (NHATS delta-v plus spectral type).
- **Sources:** [JPL SSD API docs](https://ssd-api.jpl.nasa.gov/), [SBDB API](https://ssd-api.jpl.nasa.gov/doc/sbdb.html), [CAD API](https://ssd-api.jpl.nasa.gov/doc/cad.html), [Sentry API](https://ssd-api.jpl.nasa.gov/doc/sentry.html), [Fireball API](https://ssd-api.jpl.nasa.gov/doc/fireball.html)

#### Minor Planet Center (MPC) orbit files
- **What:** the IAU MPC's orbit catalog of all numbered and unnumbered minor planets; observations in ADES.
- **Size (checked live 2026-10-24):** `MPCORB.DAT.gz` is 93,982,475 bytes (~94 MB, updated 2026-10-24 13:00 GMT); `mpcorb_extended.json.gz` is 182,677,085 bytes (~183 MB, updated 2026-10-24 20:24 GMT).
- **Coverage:** all minor planets with orbits.
- **Format:** fixed-width text; JSON.
- **Access:** `https://minorplanetcenter.net/iau/MPCORB/MPCORB.DAT.gz`; `https://minorplanetcenter.net/Extended_Files/mpcorb_extended.json.gz`.
- **Auth:** no.
- **License:** MPC terms (acknowledge the MPC).
- **Time to first data:** minutes.
- **Hackathon problem:** asteroid-family or orbit-cluster visualizer; a "how many NEOs will Rubin discover" projection.
- **Sources:** [MPCORB](https://minorplanetcenter.net/iau/MPCORB/MPCORB.DAT.gz), [MPC data](https://minorplanetcenter.net/data)

#### NASA PDS Registry / Search API
- **What:** the search API across the Planetary Data System (all PDS4 products).
- **Size (checked live 2026-10-24):** `https://pds.mcp.nasa.gov/api/search/1/products?limit=1` reports **92,774,089 products** indexed.
- **Coverage:** all NASA planetary missions archived in PDS4.
- **Format:** JSON metadata; product labels (XML) and data files (various).
- **Access:** the REST API above; `pip install pds4-tools` (1.4) to read PDS4 labels.
- **Auth:** no.
- **License:** NASA public data.
- **Time to first data:** minutes for metadata; data depends on the product.
- **Hackathon problem:** "Google for planetary data" (natural-language search over PDS metadata).
- **Sources:** [PDS Search API](https://nasa-pds.github.io/pds-api/), [live endpoint](https://pds.mcp.nasa.gov/api/search/1/products?limit=1)

#### USGS Astrogeology analysis-ready planetary data (STAC + `s3://astrogeo-ard`)
- **What:** controlled and uncontrolled planetary images and DTMs in cloud-optimized form.
- **Size (checked live 2026-10-24):** the STAC API lists 18 collections:
  - Moon: LOLA shot observations; Kaguya TC mono, stereo and SP-support observations; Kaguya TC USGS DTMs (v1, v2, v2 equatorial, v2 north polar, v2 south polar)
  - Mars: HiRISE uncontrolled observations, HiRISE SOCET DTMs, CTX controlled USGS DTMs, THEMIS IR controlled mosaics
  - Outer planets: Galileo controlled observations, mosaics and DTMs; Voyager controlled observations
- **Coverage:** Moon, Mars, Europa (Galileo/Voyager).
- **Format:** COG; COPC point clouds (LOLA).
- **Access:**
  - STAC `https://stac.astrogeology.usgs.gov/api/collections`.
  - S3 (us-west-2): `s3://astrogeo-ard/mars/mro/hirise/uncontrolled_rdr_observations/`, `.../mars/mro/hirise/controlled/dtm`, `.../mars/mro/ctx/controlled/usgs/`, `.../mars/mo/themis/controlled_mosaics/`, `.../moon/lro/lola/`, `.../moon/kaguya/terrain_camera/usgs_dtms/`, `.../moon/kaguya/terrain_camera/monoscopic/uncontrolled/`, `.../jupiter/europa/galileo_voyager/usgs_controlled_mosaics/`.
- **Auth:** no.
- **License:** Kaguya entries CC0 1.0; others NASA/USGS public (check per collection).
- **Time to first data:** minutes (`pystac-client` 0.9.1).
- **Hackathon problem:** a landing-site hazard map (slope from HiRISE/CTX DTMs plus crater density) for Mars or the lunar south pole; a Europa terrain explorer for the Clipper era.
- **Sources:** [USGS Astrogeology STAC](https://stac.astrogeology.usgs.gov/api/collections), [AWS registry HiRISE](https://registry.opendata.aws/nasa-usgs-mars-hirise/), [AWS registry CTX DTMs](https://registry.opendata.aws/nasa-usgs-controlled-mro-ctx-dtms/), [AWS registry LOLA](https://registry.opendata.aws/nasa-usgs-lunar-orbiter-laser-altimeter/), [AWS registry Kaguya TC](https://registry.opendata.aws/jaxa-usgs-nasa-kaguya-tc/)

#### NASA Lunar FM Bench (SomBench): multimodal lunar tiles plus benchmarks
- **What:** NASA ODSI/IBM benchmark for ML on the lunar surface ("formerly known as SomBench"). The pretraining corpus is co-registered 512×512 tiles anchored to LROC images: WAC track at 100 m/px (~51 km tiles), NAC track at 1 m/px (~512 m tiles). Layers are optical, topographic, spectral, radar, thermal and gravity. Downstream HF benchmarks:
  - `Sombench-NAC-Crater-Detection`: COCO boxes, 408 tiles, 105 MB
  - `Sombench-WAC-Crater-Detection`
  - `Sombench-IMP-Segmentation`
  - `Sombench-Ice-Prospectivity-Regression`: polar ±10° at 240 m/px, after Coyan et al. 2025, 380 MB
- **Size:** full corpus on S3 (size not stated); HF samples and benchmarks from MBs to hundreds of MB.
- **Coverage:** Moon.
- **Format:** Parquet, GeoTIFF, .npy, COCO JSON.
- **Access:** `aws s3 ls s3://nasa-lunar-fm-bench/ --no-sign-request` (us-west-2); `load_dataset("nasa-ibm-ai4science/Sombench-Ice-Prospectivity-Regression")`.
- **Auth:** no.
- **License:** CC BY 4.0.
- **Time to first data:** minutes.
- **Hackathon problem:** **"Where is the water? An Artemis ice-prospecting map"** (water-ice prospectivity regression near the south pole); an automated crater counter for landing-hazard and surface-age mapping.
- **Sources:** [AWS registry Lunar FM Bench](https://registry.opendata.aws/som-bench/), [HF Sombench pretraining data](https://huggingface.co/datasets/nasa-ibm-ai4science/Sombench-pretraining-data), [HF Ice Prospectivity](https://huggingface.co/datasets/nasa-ibm-ai4science/Sombench-Ice-Prospectivity-Regression), [HF NAC craters](https://huggingface.co/datasets/nasa-ibm-ai4science/Sombench-NAC-Crater-Detection)

#### YAOKI lunar rover (IM-2) telemetry and imagery
- **What:** full mission telemetry, telecommands and images from Dymon's YAOKI micro-rover on Intuitive Machines IM-2 at the lunar south pole (lat 84.79059, lon 29.19567). Operated by JAOPS with the open-source Yamcs mission control system on 2025-03-07, 02:17–04:33 UTC.
- **Size:** small (a single short mission).
- **Coverage:** one mission, March 2025.
- **Format:** Parquet time series (TM/TC channels), raw and PNG images, Yamcs RocksDB archive.
- **Access:** `s3://im2-yaoki-rover-public/timeseries/*`, `.../images/*`, `.../yamcs-data/*` (ap-northeast-1); [GitHub](https://github.com/jaops-space/im2-yaoki-yamcs-public).
- **Auth:** no.
- **License:** CC BY 4.0.
- **Time to first data:** minutes.
- **Hackathon problem:** "what went wrong on a commercial lunar landing" (IM-2 tipped over), told as a mission-replay dashboard; telemetry anomaly detection on real lunar-surface data.
- **Sources:** [AWS registry YAOKI](https://registry.opendata.aws/im2-yaoki-rover/)

#### Mars 2020 (Perseverance) raw images feed
- **What:** public JSON feed of raw rover images.
- **Size:** hundreds of thousands of images (the latest sol returned is 2018, checked live).
- **Coverage:** 2021 to present.
- **Format:** JSON metadata plus JPG/PNG.
- **Access:** `https://mars.nasa.gov/rss/api/?feed=raw_images&category=mars2020&feedtype=json&num=1`. Note: the api.nasa.gov `mars-photos` endpoint returned HTTP 429 with DEMO_KEY (rate limited); get a personal key.
- **Auth:** no for the raw feed; a free API key for api.nasa.gov.
- **License:** NASA images are generally not copyrighted (NASA media guidelines).
- **Time to first data:** minutes.
- **Hackathon problem:** a terrain-type classifier for rover driving (pairs with AI4Mars labels).
- **Sources:** [Mars 2020 raw images](https://mars.nasa.gov/mars2020/multimedia/raw-images/), [api.nasa.gov](https://api.nasa.gov/)

#### Global CTX Mosaic of Mars (Murray Lab, Caltech), V01
- **What:** a seamless global mosaic from MRO's Context Camera.
- **Size:** **5.7 terapixels** at **5.0 m/px**, built from 86,571 CTX images (out of 104,647) acquired 2006–2020, in **3,960 tiles of 4°×4°** with seam maps and tie points.
- **Coverage:** **99.5% of Mars**, 88°S–88°N.
- **Format:** GeoTIFF tiles (equirectangular), vector seam maps, KML index.
- **Access:** tiles at `https://murray-lab.caltech.edu/CTX/V01/tiles/` (coverage quad map `V01/tiles/CoverageMaps/MurrayLab_GlobalCTXMosaic_V01_quad-map.zip`); streamed in the SceneView 3D viewer, JMARS and Mars QuickMap. **The site's TLS chain was incomplete on 2026-10-24, so `curl -k` is needed** (WebFetch failed with "unable to verify the first certificate").
- **Auth:** no.
- **License:** free with citation (Dickson et al. 2024, Earth & Space Science, doi:10.1029/2024EA003555); acknowledge MSSS/JPL.
- **Time to first data:** minutes for one tile; each tile is large.
- **Hackathon problem:** "Mars landing-site finder" (flat, safe, near scientifically interesting terrain); a dust-devil-track or new-impact change detector (pair with HiRISE).
- **Sources:** [Murray Lab Global CTX Mosaic](https://murray-lab.caltech.edu/CTX/), [Dickson et al. 2024](https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2024EA003555)

#### ESA NEO Coordination Centre (NEOCC) risk list
- **What:** ESA's independent impact-monitoring list of near-Earth objects.
- **Size:** about 1,800 objects (not counted here). The file header said "Last Update: 2026-10-24 13:46 UTC". Its top entry is **2023 VD3** (14 m, impact probability 2.35×10⁻³ on 2034-11-08, Palermo −2.67), followed by 2008 JL3 and 1979 XB.
- **Coverage:** all NEOs with non-zero impact probability over the next century.
- **Format:** fixed-width text.
- **Access:** `https://neo.ssa.esa.int/PSDB-portlet/download?file=esa_risk_list` (checked live).
- **Auth:** no.
- **License:** ESA terms.
- **Time to first data:** under 1 minute.
- **Hackathon problem:** a "NASA vs ESA disagreement monitor" comparing JPL Sentry with ESA NEOCC and explaining discrepancies; an impact-corridor visualizer.
- **Sources:** [ESA NEOCC](https://neo.ssa.esa.int/), [risk list file](https://neo.ssa.esa.int/PSDB-portlet/download?file=esa_risk_list)

#### Interstellar comet 3I/ATLAS (C/2025 N1) and other comet data
- **What:** the third interstellar object, discovered July 2025. JPL SBDB returns `C/2025 N1 (ATLAS)` as a hyperbolic comet with e = 6.12, q = 1.35 au, i = 175°. The observation arc runs from 2025-10-03 to 2026-10-16 in the current orbit solution (checked live). Comet elements: MPC `CometEls.txt` (unverified path); HF `juliensimon/comet-catalog`, `juliensimon/mpc-comet-elements`.
- **Size:** small.
- **Coverage:** 2025–2026 apparition.
- **Format:** JSON / text.
- **Access:** `https://ssd-api.jpl.nasa.gov/sbdb.api?sstr=3I`; `astroquery.jplhorizons` for ephemerides.
- **Auth:** no.
- **License:** public.
- **Time to first data:** minutes.
- **Hackathon problem:** a "how fast could we intercept an interstellar visitor" mission-design calculator (ESA Comet Interceptor angle).
- **Sources:** [JPL SBDB API](https://ssd-api.jpl.nasa.gov/doc/sbdb.html)
- **Also seen:** JPL SBDB lists **2024 YR4** (`pha: false`, last observation 2026-02-26). Earth impact was ruled out in 2025; the lunar-impact question is a cross-slice lead.

#### ShadowCam (KPLO/Danuri): permanently shadowed regions imagery
- **What:** a NASA camera on Korea's KPLO lunar orbiter. It is derived from the LROC NAC but "about 200 times more sensitive", so it can image inside permanently shadowed regions (PSRs) near the poles.
- **Size:** the team "released three months of observations to PDS on 21 August 2026" (the "September 2026 release"). Image counts are not stated.
- **Coverage:** lunar polar PSRs, 2023 onward.
- **Format:** PDS image products.
- **Access:** via PDS (the Imaging Node / ASU archive; exact path not verified). The site has moved to `https://shadowcam.im-ldi.com/`.
- **Auth:** no.
- **License:** NASA PDS public.
- **Time to first data:** about 1 hour (PDS navigation).
- **Hackathon problem:** a PSR rover traverse planner, or an ice-exposure hunt for Artemis south-pole sites. Combine with the SomBench ice-prospectivity layers and LOLA DEMs.
- **Sources:** [ShadowCam site](https://shadowcam.im-ldi.com/)

#### LRO (LROC NAC/WAC, LOLA, Diviner, Mini-RF)
- **What:** Lunar Reconnaissance Orbiter data, 2009 to present: NAC images at 0.5–1 m/px, WAC global mosaics, LOLA altimetry and DEMs, Diviner thermal, Mini-RF radar.
- **Size:** hundreds of TB in total (not verified).
- **Coverage:** global Moon.
- **Format:** PDS3/PDS4 IMG, GeoTIFF, COPC (LOLA on AWS).
- **Access:** LROC PDS archive `https://pds.lroc.asu.edu/data/` (301 redirect, live); LROC QuickMap `https://quickmap.lroc.asu.edu/` (live); LOLA point clouds `s3://astrogeo-ard/moon/lro/lola/`; NAC/WAC-anchored ML tiles in Lunar FM Bench (above).
- **Auth:** no.
- **License:** NASA public.
- **Time to first data:** minutes for QuickMap or the LOLA COPC; hours for NAC strips.
- **Hackathon problem:** a boulder and crater hazard map for CLPS landers; illumination modelling at the south pole.
- **Sources:** [LROC](https://wms.lroc.asu.edu/lroc), [AWS registry LOLA COPC](https://registry.opendata.aws/nasa-usgs-lunar-orbiter-laser-altimeter/)

#### Lunar and Mars crater databases (Robbins)
- **What:** the Robbins & Hynek (2012) Mars crater database (~384k craters ≥1 km) and the Robbins (2018) lunar crater database (~1.3M craters ≥1–2 km). Both counts are commonly cited figures, not verified on a fetched page here.
- **Size:** tens to hundreds of MB.
- **Coverage:** global Moon and Mars.
- **Format:** CSV/Parquet; ready-made HF mirrors: `juliensimon/lunar-craters-robbins`, `juliensimon/mars-craters-robbins`, plus `ceres-craters-dawn`, `mercury-craters-herrick` and `impact-craters` (Earth).
- **Access:** `load_dataset("juliensimon/lunar-craters-robbins")`; originals via USGS / PDS (unverified links).
- **Auth:** no.
- **License:** per card.
- **Time to first data:** minutes.
- **Hackathon problem:** labels for training crater detectors on CTX or LROC images; an automated surface-age estimator.
- **Sources:** [HF juliensimon datasets](https://huggingface.co/juliensimon)

#### ISRO PRADAN (Chandrayaan-2/3, Aditya-L1, AstroSat, XPoSat)
- **What:** ISRO's science data archive portal (ISSDC). It lists XPoSat, Aditya-L1, Chandrayaan-3, Chandrayaan-2, AstroSat and GRASP data sets.
- **Size:** not stated.
- **Coverage:** Chandrayaan-2 (OHRC at ~0.25 m/px, TMC-2, IIRS, DFSAR and others; instrument list from memory, not on the fetched page), Chandrayaan-3 lander/rover, Aditya-L1 solar data.
- **Format:** PDS4.
- **Access:** `https://pradan.issdc.gov.in/` with single sign-on ("once the user logs-in to access any of the data sets" the others become accessible).
- **Auth:** **yes** (login; the registration and approval time is not stated, so budget hours).
- **License:** ISRO data policy.
- **Time to first data:** hours.
- **Hackathon problem:** Chandrayaan-2 OHRC images of south-pole PSR rims for landing-site safety; Aditya-L1 for solar-activity forecasting.
- **Sources:** [ISRO PRADAN](https://pradan.issdc.gov.in/)

#### China Lunar and Planetary Data Release System (CLPDS): Chang'e and Tianwen
- **What:** CNSA/NAOC portal for Chang'e-1 to Chang'e-6 and Tianwen-1 data (from prior knowledge).
- **Status 2026-10-24:** `https://moon.bao.ac.cn/` returned an empty page to the fetcher (JavaScript app). **Contents and registration requirements are unverified;** historically a registration is required. See the China slice.
- **Hackathon problem:** a Chang'e-4 far-side rover traverse replay; Tianwen-1 HiRIC versus HiRISE comparison.
- **Sources:** [CLPDS](https://moon.bao.ac.cn/)

#### Planetary ML benchmark datasets (Zenodo, queried 2026-10-24)
- **Mars-Bench** (multi-task Mars benchmark), for example `mb-mars_seg_mer` (0.29 GB, 2025-05-15) and **`mb-mars_seg_msl` (0.23 GB, 2026-09-27)**; CC BY 4.0. Rover-image terrain segmentation for Spirit/Opportunity and Curiosity. [doi:10.5281/zenodo.15494730](https://doi.org/10.5281/zenodo.15494730), [doi:10.5281/zenodo.22992914](https://doi.org/10.5281/zenodo.22992914)
- **HiRISE Landform Classification Dataset:** 1.86 GB, CC BY 4.0, **2026-07-10**. [doi:10.5281/zenodo.21300384](https://doi.org/10.5281/zenodo.21300384)
- **MoonAnything:** "A Vision Benchmark with Large-Scale Lunar Supervised Data"; 22.44 GB; CC BY 4.0; 2026-01-29. [doi:10.5281/zenodo.18415119](https://doi.org/10.5281/zenodo.18415119)
- **SimMars6K** (simulated Mars rover imagery, 13.59 GB): [doi:10.5281/zenodo.7707898](https://doi.org/10.5281/zenodo.7707898). **DepthMars** (semantic segmentation from rover images, 0.66 GB): [doi:10.5281/zenodo.10939837](https://doi.org/10.5281/zenodo.10939837).
- **Meter-scale scalloped-terrain map of Mars** (ground-ice indicator, 0.32 GB, 2026-02-19): [doi:10.5281/zenodo.18689392](https://doi.org/10.5281/zenodo.18689392). The angle: a ground-ice finder for future human landing sites.
- **Moon Mineralogy Mapper (M3) mineral maps of the lunar polar regions** (2025-09-17): [doi:10.5281/zenodo.17139505](https://doi.org/10.5281/zenodo.17139505).
- **RGB image dataset for lunar south pole analogue environments** (2026-10-08): [doi:10.5281/zenodo.23242990](https://doi.org/10.5281/zenodo.23242990).
- **Fireball networks:** debiased meteorite-dropping fireballs from EFN, EDMOND, CAMS, GMN, FRIPON and GFO ([doi:10.5281/zenodo.16945247](https://doi.org/10.5281/zenodo.16945247)); FRIPON Geminids 2016–2023 ([doi:10.5281/zenodo.15650370](https://doi.org/10.5281/zenodo.15650370)). Also the HF `juliensimon/global-meteor-network` (3.6M rows) and JPL Fireball API.
- **Starlink "mechanical energy loss" dataset** (orbital-energy loss derived from Starlink satellites, a thermosphere-drag proxy; 0.05 GB; 2025-04-25): [doi:10.5281/zenodo.15281786](https://doi.org/10.5281/zenodo.15281786). This is a space-weather and orbital cross-slice lead.

#### NAIF SPICE kernels (ephemerides for planets, spacecraft and instruments)
- **What:** NASA's SPICE geometry system. Generic kernels: planetary ephemerides **DE440/DE440s and the newer DE442/DE442s**, plus leap seconds, planetary constants and frames. Mission kernel archives exist for most NASA and many ESA missions.
- **Size:** `de440s.bsp` is 32.7 MB (checked live); full DE files are ~100 MB+; mission archives run to GBs.
- **Coverage:** solar system, ~1550–2650 for DE440 (from NAIF documentation, not re-verified).
- **Format:** binary SPK/CK/PCK kernels.
- **Access:** `https://naif.jpl.nasa.gov/pub/naif/generic_kernels/spk/planets/` (listing shows de430, de432s, de435, de438, de440, de440s, de442, de442s); `pip install spiceypy` (8.3.0, 2026-10-11) or `skyfield` (1.55).
- **Auth:** no.
- **License:** public.
- **Time to first data:** minutes.
- **Hackathon problem:** "where exactly was the instrument pointing?": footprint reconstruction for any mission image; eclipse and visibility planning for lunar landers.
- **Sources:** [NAIF generic kernels](https://naif.jpl.nasa.gov/pub/naif/generic_kernels/), [PyPI spiceypy](https://pypi.org/project/spiceypy/)

#### JunoCam raw images (citizen-science processing)
- **What:** raw and processed JunoCam images of Jupiter and its moons, released for public processing.
- **Access:** `https://www.missionjuno.swri.edu/junocam/processing` (live 200). No auth for downloads (unverified; a login is needed only for uploads).
- **Hackathon problem:** auto-processing raw JunoCam framelets into colour composites; a storm tracker on Jupiter.
- **Sources:** [JunoCam processing](https://www.missionjuno.swri.edu/junocam/processing)

#### ESA Planetary Science Archive (PSA): EPN-TAP
- **What:** ESA's archive for planetary missions: Mars Express, ExoMars TGO, Rosetta, Venus Express, BepiColombo, JUICE, SMART-1, Giotto, Huygens and others.
- **Size (checked live 2026-10-24):** `SELECT count(*) FROM psa.epn_core` returns **39,752,650 granules**.
- **Coverage:** ESA planetary missions since the 1980s.
- **Format:** EPN-TAP metadata (`access_url`, `access_format`, `instrument_host_name`, `c1min` and others); PDS3/PDS4 products.
- **Access:** TAP `https://psa.esa.int/psa-tap/tap/sync?REQUEST=doQuery&LANG=ADQL&FORMAT=csv&QUERY=SELECT+TOP+10+*+FROM+psa.epn_core` (the old `archives.esac.esa.int/psa-tap` redirects here); works with `pyvo` and TOPCAT. Ready-made HF Parquet logs: `juliensimon/esa-exomars-tgo-observations` (27.7M rows), `esa-mars-express-observations`, `esa-bepicolombo-observations`, `esa-juice-observations`, `esa-rosetta-observations`, `esa-venus-express-observations`.
- **Auth:** no.
- **License:** ESA PSA terms (cite).
- **Time to first data:** minutes.
- **Hackathon problem:** "which spot on Mars has been looked at by the most instruments" (an observation-coverage gap finder that helps plan new observations).
- **Sources:** [ESA PSA](https://psa.esa.int/), [PSA TAP tables (live)](https://psa.esa.int/psa-tap/tap/tables)

#### More planetary datasets on AWS (from the registry metadata)
Each item: bucket or registry entry; hackathon angle. Source: [AWS registry](https://registry.opendata.aws/) and the [registry GitHub](https://github.com/awslabs/open-data-registry).
- **Kaguya/SELENE Terrain Camera** observations and DTMs: `s3://astrogeo-ard/moon/kaguya/...`; CC0.
- **Controlled THEMIS IR mosaics:** `s3://astrogeo-ard/mars/mo/themis/controlled_mosaics/`.
- **Europa Galileo/Voyager controlled mosaics and DTMs:** `s3://astrogeo-ard/jupiter/europa/...`.
- **"Mars Spectrometry: Detect Evidence for Past Habitability"** (`nasa-ega`) and **"Mars Spectrometry 2: Gas Chromatography for SAM"** (`nasa-gcms`): ML-ready mass-spectrometry datasets from the NASA/DrivenData challenges. The angle: an automated habitability detector for rover instruments.
- **NASA OSDR** (space biology) `s3://nasa-osdr` and **NASA Physical Sciences Informatics** `s3://nasa-psi`: ISS experiment data. The angle: astronaut health and microgravity research.

#### Additional astronomy (verified pages)
- **Chandra Source Catalog 2.2:** "released in October 2026"; **432,713 unique compact and extended X-ray sources** and "more than 1.4 million individual detections". Access through CSCview and the CSC CLI. [CSC](https://cxc.cfa.harvard.edu/csc/)
- **Legacy Surveys DR11:** "Current Data Release: 11"; inference model and source catalogs for ~31,000 deg² of extragalactic sky. Sky Viewer and cutout URL patterns. The Multimodal Universe has a DR10 image subset (124M). [Legacy Surveys](https://www.legacysurvey.org/)
- **LOFAR LoTSS-DR3:** 19,035 deg², **13.7 million radio sources** (DR2: 5,700 deg², 4.5M). [LOFAR surveys releases](https://lofar-surveys.org/releases.html)
- **CHIME/FRB Catalog 1:** 536 fast radio bursts (18 repeaters), JSON/CSV/FITS, DOI 10.11570/21.0007. Catalog 2 was not on the fetched page; an HF mirror `juliensimon/chime-frb-catalog` has 600 rows. [CHIME/FRB catalog](https://www.chime-frb.ca/catalog)
- **NOIRLab Astro Data Lab:** a science platform with notebooks, client libraries and Data Explorer; "An account is required for full access", and accounts are free. [Astro Data Lab](https://datalab.noirlab.edu/)
- **GWOSC O4 strain mirrors on Hugging Face:** `astro-legacy-archive/gwosc-o4a-strain` (**3.63 TB**, CC BY 4.0) and `astro-legacy-archive/gwosc-o4b-strain` (**5.20 TB**, CC BY 4.0); also o3a and o2 strain and `planck-2018-chains`. [HF astro-legacy-archive](https://huggingface.co/astro-legacy-archive)
- **AstroM3 dataset** (`AstroMLCore/AstroM3Dataset`, 1.3 GB, MIT): multimodal (photometry, spectra, metadata) variable-star dataset. [HF](https://huggingface.co/datasets/AstroMLCore/AstroM3Dataset)
- **UniverseTBD Multimodal Universe re-packs** (`UniverseTBD/mmu_*`, May 2026) and HSC cross-survey embeddings (`desi_hsc_embeddings`, `jwst_hsc_embeddings`, `legacysurvey_hsc_embeddings`, `pu-embeddings`). [HF UniverseTBD](https://huggingface.co/UniverseTBD)

### 2.9 Mission engineering data

#### ESA Anomaly Dataset (ESA-ADB benchmark data)
- **What:** "the first large-scale, real-life satellite telemetry dataset with curated anomaly annotations originated from three ESA missions." Built by Airbus Defence and Space, KP Labs and ESA/ESOC under ESA's AI-for-Automation roadmap.
- **Size:** 11.61 GB: `ESA-Mission1.zip` (3.78 GB), `ESA-Mission2.zip` (4.10 GB), `ESA-Mission3.zip` (3.73 GB).
- **Coverage:** multi-year telemetry from three anonymised missions.
- **Format:** zipped time series with anomaly labels.
- **Access:** Zenodo record 15237121 (2025-04-17); benchmark code in the ESA-ADB GitHub (not fetched).
- **Auth:** no.
- **License:** **not stated in the Zenodo metadata** (`license: None`); check the record before publishing results.
- **Time to first data:** about 10 minutes for one mission zip.
- **Hackathon problem:** **an "anomaly copilot for satellite operators"**: detect anomalies in multichannel telemetry and explain them, retrieving similar NASA lessons from LLIS and NTRS (2.10).
- **Sources:** [Zenodo ESA Anomaly Dataset](https://doi.org/10.5281/zenodo.15237121), [Zenodo API record (live)](https://zenodo.org/api/records/15237121)

#### OPSSAT-AD (ESA OPS-SAT CubeSat telemetry anomaly benchmark)
- **What:** AI-ready telemetry from ESA's OPS-SAT CubeSat, with labelled anomalies and baselines from 30 algorithms.
- **Size:** 0.02 GB (tiny, instant).
- **Format:** CSV.
- **Access:** Zenodo [doi:10.5281/zenodo.15108715](https://doi.org/10.5281/zenodo.15108715). Related: "The OPS-SAT case" dataset ([doi:10.5281/zenodo.6524750](https://doi.org/10.5281/zenodo.6524750), 0.11 GB) and its test set ([doi:10.5281/zenodo.10301862](https://doi.org/10.5281/zenodo.10301862)).
- **Auth:** no.
- **License:** CC BY 4.0.
- **Time to first data:** under 2 minutes.
- **Hackathon problem:** on-board (edge) anomaly detection for CubeSats.
- **Sources:** [Zenodo API record (live)](https://zenodo.org/api/records/15108715)

#### NASA SMAP / MSL telemetry anomalies (Hundman et al. 2018, "telemanom")
- **What:** expert-labelled anomalies in SMAP and Curiosity (MSL) telemetry channels, with command encodings (the KDD 2018 benchmark).
- **Access:** **the original `https://s3-us-west-2.amazonaws.com/telemanom/data.zip` returned HTTP 403 on 2026-10-24.** The repo README now says: `kaggle datasets download -d patrickfleith/nasa-anomaly-detection-dataset-smap-msl`.
- **Auth:** a Kaggle account.
- **License:** see the Kaggle page.
- **Time to first data:** minutes.
- **Hackathon problem:** a baseline for the anomaly copilot (well-known numbers to beat).
- **Sources:** [telemanom README](https://github.com/khundman/telemanom), [arXiv 1802.04431](https://arxiv.org/abs/1802.04431), [Kaggle mirror](https://www.kaggle.com/datasets/patrickfleith/nasa-anomaly-detection-dataset-smap-msl)

#### Other spacecraft telemetry and operations datasets
- **GOCE satellite telemetry** (ESA gravity mission; HF `patrickfleith/GOCE-satellite-telemtry`): **45.3 GB**, 1B–10B rows. The angle: thermal and drag-related subsystem behaviour before reentry. [HF](https://huggingface.co/datasets/patrickfleith/GOCE-satellite-telemtry)
- **YAOKI lunar rover (IM-2)** telemetry and telecommand Parquet plus the Yamcs archive: see 2.8.
- **Spatiam DTN ISS experiment** (delay-tolerant networking between the ISS and Earth): `s3://spatiam-nlra-iss-experiment-open-data` ("no restrictions"). [AWS registry](https://registry.opendata.aws/spatiam-nlra-iss-experiments/)
- **ESA Kelvins CDM dataset** and **GEO manoeuvre** dataset: see 2.5.
- **NASA OSDR** (`s3://nasa-osdr`) and **Physical Sciences Informatics** (`s3://nasa-psi`): ISS experiment data.
- **Mars Spectrometry** challenge datasets (`nasa-ega`, `nasa-gcms` on the AWS registry): instrument data for autonomous science.
- **Not verified in this pass:** the NASA PCoE prognostics repository (C-MAPSS turbofan, batteries); ISS Live! telemetry (Lightstreamer).

#### Lessons-learned and failure records
- **NASA LLIS:** 2,135 public lessons via a JSON backend (`/llis/lesson/_search`).
- **NTRS:** 648,220 records; `isLessonsLearned` field. Both are in 2.10.
- **Launch outcomes:** Launch Library 2 (`launches/previous` with status fields), GCAT launch logs and HF `juliensimon/space-launch-log` / `spacex-launches` / `rocket-lab-launches` support launch-failure statistics.
- **Hackathon problem:** a launch-reliability estimator by vehicle family, with Bayesian priors for new vehicles.

### 2.10 Literature and text corpora

#### NASA Technical Reports Server (NTRS)
- **What:** NASA's repository of technical reports, conference papers, mishap and lessons-learned-tagged documents. Records carry a boolean `isLessonsLearned` field plus `center`, `subjectCategories`, `exportControl`, `abstract` and `distribution`.
- **Size (checked live 2026-10-24):** the API reports **648,220 citations**; a query for "anomaly" returns 2,864 (top hit: "The Mars Rover Spirit FLASH anomaly", 20060044140).
- **Coverage:** 1917 to present (NACA and NASA).
- **Format:** JSON metadata; PDFs for many records.
- **Access:** `https://ntrs.nasa.gov/api/citations/search?q=anomaly&page.size=100`; record IDs map to PDFs.
- **Auth:** no.
- **License:** mostly US government works (check each record's `copyright` field).
- **Time to first data:** minutes.
- **Hackathon problem:** **"Mission failure memory"**: a RAG assistant that, given a new design or a test anomaly, retrieves the closest historical NASA anomalies and their fixes, so engineers stop repeating known failures.
- **Sources:** [NTRS](https://ntrs.nasa.gov/), [NTRS API (live)](https://ntrs.nasa.gov/api/citations/search?q=anomaly&page.size=1)

#### NASA Lessons Learned Information System (LLIS)
- **What:** NASA's official database of lessons learned (driving event, lesson, recommendation, mission directorate, program phase, categories).
- **Size (checked live 2026-10-24):** the site's Elasticsearch-style backend reports **2,135 public lessons** (`/llis/lesson/_count`).
- **Coverage:** 1960s to present.
- **Format:** JSON documents with fields `title`, `lesson_date`, `lessonAbstract`, `description_event`, `drivingEvent`, `lesson`, `lesson_learned`, `recommendation`, `missionDirectorate`, `programPhase`, `categories`, `organization`, `tags`, `lesson_number`.
- **Access (undocumented, observed live):** `https://llis.nasa.gov/llis/lesson/{id}` (for example `/llis/lesson/1000`, Space Shuttle RCS valve leakage) and `https://llis.nasa.gov/llis/lesson/_search?q=battery&size=100` (75 hits for "battery"). Be polite: cache once and do not hammer it.
- **Auth:** no.
- **License:** US government work (public lessons only).
- **Time to first data:** under 10 minutes to pull all 2,135.
- **Hackathon problem:** "NASA lessons-learned copilot" for student CubeSat teams and NewSpace startups: paste your design review and get the relevant lessons. This is a clear, judge-friendly problem (repeat failures cost missions).
- **Sources:** [LLIS](https://llis.nasa.gov/), [example JSON](https://llis.nasa.gov/llis/lesson/1000), [count](https://llis.nasa.gov/llis/lesson/_count)

#### NASA ADS / SciX API
- **What:** the Astrophysics Data System (now branded alongside SciX, the Science Explorer, which extends to Earth, planetary, helio and bio/physical sciences): bibliographic search, citations, metrics, full-text search for many records.
- **Size:** about 16M+ records (commonly cited; not verified on a fetched page).
- **Coverage:** astronomy, physics, planetary and heliophysics literature, plus Earth science under SciX.
- **Format:** JSON (Solr-style).
- **Access:** `https://api.adsabs.harvard.edu/v1/search/query?q=...` with header `Authorization: Bearer <token>`. Without a token the API returns HTTP 401 `Missing "Authorization" in headers` (checked live). Run `pip install ads` (0.12.7). Endpoints: search, export, metrics, libraries, journals.
- **Auth:** **yes** (a free account; generate a token in the profile, which is instant).
- **Rate limit:** per endpoint; the README example shows **5,000 queries/day**, resetting at midnight UTC, with `X-RateLimit-*` headers.
- **License:** ADS terms; abstracts carry the publishers' rights.
- **Time to first data:** 10 minutes.
- **Hackathon problem:** "Literature no human can read": an agent that maps which open questions in a decadal survey have the fewest recent papers (research-gap finder); or a mission-to-papers impact tracker ("what science did Kepler actually produce?").
- **Sources:** [ADS API README](https://github.com/adsabs/adsabs-dev-api), [SciX](https://scixplorer.org/)

#### arXiv (API, OAI-PMH, bulk S3, Kaggle metadata)
- **What:** preprints, including astro-ph (GA, CO, EP, HE, IM, SR).
- **Size:**
  - The API reports **36,513 results for `cat:astro-ph.EP`** (checked live).
  - **Kaggle "arXiv Dataset" (Cornell University):** metadata JSON for "1.7M+ scholarly papers" (the subtitle is outdated; arXiv is larger now), **5.63 GB, CC0**, version 308, last updated **2026-10-17**.
  - **Bulk PDFs and source on S3:** bucket `arxiv` (us-east-1, **requester pays**), ~500 MB tar chunks (`pdf/arXiv_pdf_YYMM_NNN.tar`, `src/arXiv_src_YYMM_NNN.tar`). The complete set was "about 9.2 TB as of April 2025", growing ~100 GB/month.
- **Coverage:** 1991 to present.
- **Format:** Atom XML (API); OAI-PMH XML; JSON lines (Kaggle); PDF and LaTeX tars (S3).
- **Access:** `https://export.arxiv.org/api/query?search_query=cat:astro-ph.EP&max_results=100`; OAI-PMH `https://export.arxiv.org/oai2`; `kaggle datasets download Cornell-University/arxiv`; `aws s3 ls s3://arxiv/pdf/ --request-payer requester`.
- **Auth:** no for the API and OAI; a Kaggle account for Kaggle; AWS credentials and payment for S3.
- **License:** metadata CC0 (Kaggle). Full text is mostly the arXiv default license: "does not let arXiv grant others distribution rights", and tools must "link back to arXiv".
- **Time to first data:** minutes (API); about 15 minutes (Kaggle 5.6 GB).
- **Hackathon problem:** a daily astro-ph digest tuned to a mission team; a claim-contradiction finder across papers.
- **Sources:** [arXiv bulk data on S3](https://info.arxiv.org/help/bulk_data_s3.html), [Kaggle arXiv dataset](https://www.kaggle.com/datasets/Cornell-University/arxiv), [arXiv API](https://info.arxiv.org/help/api/index.html)

#### OpenAlex
- **What:** an open scholarly graph (works, authors, institutions, concepts), with full-text search for some works.
- **Size:** 71,953 works match a full-text search for "exoplanet" (checked live).
- **Access:** `https://api.openalex.org/works?search=exoplanet`. **New in 2026:** the API now meters usage in dollars. Without a key, "this request shares one free daily budget ($0.10) with everyone on your network's IP address"; a free key gives "$1/day". Each call reported `cost_usd: 0.001`.
- **Auth:** recommended (a free API key; get it before the hackathon, since shared Wi-Fi will exhaust the per-IP budget).
- **License:** CC0 data.
- **Time to first data:** minutes.
- **Hackathon problem:** a space-research funding and collaboration network map (which countries and institutions lead lunar-ice research).
- **Sources:** [OpenAlex API response (live)](https://api.openalex.org/works?search=exoplanet&per_page=1)

#### NASA GCN Circulars (gamma-ray bursts, neutrinos, gravitational waves, Einstein Probe transients)
- **What:** rapid human-written bulletins for multi-messenger transients.
- **Size:** latest circular **46021** (EP261015a); the archive is a **31.6 MB JSON tar.gz** (text version 30.1 MB), updated daily (Last-Modified 2026-10-24 19:38 GMT).
- **Coverage:** 1997 to present.
- **Format:** JSON (one per circular) or text.
- **Access:** `https://gcn.nasa.gov/circulars/archive.json.tar.gz` (redirects to S3); live alerts via the GCN Kafka client (`pip install gcn-kafka`; free account).
- **Auth:** no for the archive.
- **License:** not stated on the page.
- **Time to first data:** under 5 minutes.
- **Hackathon problem:** an LLM "circular-to-structured-data" extractor (coordinates, magnitudes, redshifts) that builds a live multi-messenger event table and alerts telescopes.
- **Sources:** [GCN Circulars](https://gcn.nasa.gov/circulars)

#### Astro-LLM corpora and benchmarks (datasets that ship with models)
- **UniverseTBD arXiv corpora (AstroLLaMA):** `UniverseTBD/arxiv-astro-abstracts-all` (0.23 GB, MIT, 100k–1M rows), `UniverseTBD/arxiv-abstracts-large` (3.8 GB, AFL-3.0, 1M–10M rows), `UniverseTBD/arxiv-qa-astro-ph`, `UniverseTBD/AstroLLaVA_convos`, `UniverseTBD/hypogen-dr1` (hypothesis generation), `UniverseTBD/AstroBridge-Data` (updated 2026-10-17). Models: `UniverseTBD/astrollama`, `astrollama-7b-chat-alpha`, `AstroLLaVA`, the AstroBridge series.
- **AstroMLab:** `AstroMLab/Astrobench_MCQ_v1_Public` (MCQ benchmark built from Annual Reviews of Astronomy and Astrophysics; 1k–10k items) plus a Chinese version and `AstroMLab/USAAAO_QA` (Olympiad QA, July 2026). Models: **AstroSage-8B** (and GGUF), **AstroSage-70B** (including a `-20251009` release), and the astrollama-2/3 series.
- **astroBench** (`astroBench/basic-knowledge-test`, `knowledge_application`, `scientific-calculation-test`).
- **NASA SMD (INDUS-era) benchmarks** under `nasa-impact`: `nasa-smd-qa-benchmark`, `nasa-smd-IR-benchmark` (0.22 GB), `nasa-sde-IR-benchmark-20251024-v5`, `EO-via-NLP`, `nasa-science-github-repos`, `nasa-science-code-benchmark-v0.1.1`.
- **`juliensimon/stackexchange-space-qa`** (Space Exploration Stack Exchange Q&A, 31 MB, CC BY-SA 4.0).
- **Access:** `load_dataset(...)`. **Auth:** no (`arxiv-astro-abstracts-all` is auto-gated: accept terms). **Time to first data:** minutes.
- **Hackathon problem:** evaluate whether a general LLM or a domain model (AstroSage) answers mission-ops questions correctly; build a space-domain eval set.
- **Sources:** [HF UniverseTBD](https://huggingface.co/UniverseTBD), [HF AstroMLab](https://huggingface.co/AstroMLab), [HF nasa-impact](https://huggingface.co/nasa-impact), [HF astroBench](https://huggingface.co/astroBench)

#### Decadal surveys (National Academies, free PDFs)
- **Astro2020:** *Pathways to Discovery in Astronomy and Astrophysics for the 2020s*, [NAP 26141](https://nap.nationalacademies.org/catalog/26141).
- **Planetary 2023–2032:** *Origins, Worlds, and Life*, [NAP 26522](https://nap.nationalacademies.org/catalog/26522).
- **Heliophysics 2024:** *The Next Decade of Discovery in Solar and Space Physics*, [NAP 27938](https://nap.nationalacademies.org/catalog/27938).
- **Earth Science 2018:** *Thriving on Our Changing Planet*, [NAP 24938](https://nap.nationalacademies.org/catalog/24938).
- **Access:** free PDF download (a NAP account or guest checkout may be required). **Time to first data:** minutes.
- **Hackathon problem:** a decadal-priority tracker that links each recommendation to missions, budgets and recent papers (ADS), to show which priorities are slipping.
- (All four titles verified from the NAP page titles, checked live 2026-10-24.)

#### Other text sources
- **NASA Science Discovery Engine** (now at `https://science.data.nasa.gov/science-discovery-engine/search/`, redirected from sciencediscoveryengine.nasa.gov): unified search over SMD data and documents. API status unverified.
- **ECSS standards** (European space engineering standards): **`https://ecss.nl/` redirected to an ESA "down" status page on 2026-10-24**, so plan around it.
- **ESA document repositories:** see the ESA slice.

### 2.11 Cloud access platforms
#### Microsoft Planetary Computer (data catalog plus STAC API)
- **Status in 2026:** **the Planetary Computer Hub (hosted JupyterHub) was retired on 6 June 2024.** The announcement said "the Planetary Computer Data and APIs will remain available and unchanged." Data and API functionality need no account, but Azure Blob reads still need SAS tokens, which the `planetary-computer` package signs automatically, and "account requests are no longer accepted." Planetary Computer Pro is a separate Azure product for hosting your own STAC (third-party reports say it reached GA in 2026; unverified on a Microsoft page).
- **Size (checked live 2026-10-24):** the STAC API lists **139 collections**, including:
  - optical and SAR: `sentinel-2-l2a`, `sentinel-1-grd`, `sentinel-1-rtc`, `landsat-c2-l1`, `landsat-c2-l2`, `hls2-l30`, `hls2-s30`, `naip` (2010–2023), `aster-l1t`
  - MODIS 061 suite (`modis-09A1-061` and others), Sentinel-3 OLCI/SLSTR/SRAL/SYNERGY, `sentinel-5p-l2-netcdf`
  - elevation and mosaics: `cop-dem-glo-30/90`, `nasadem`, `alos-dem`, `alos-palsar-mosaic`, `alos-fnf-mosaic`, `3dep-lidar-*`
  - land cover and buildings: `esa-worldcover`, `esa-cci-lc`, `io-lulc-annual-v02`, `jrc-gsw`, `ms-buildings`, `usda-cdl`, `mtbs`
  - weather and climate: `era5-pds`, `goes-cmi`, `goes-glm`, `gpm-imerg-hhr` (2000–2021), `ecmwf-forecast`, `noaa-hrrr`, `noaa-mrms-qpe-*`, `nasa-nex-gddp-cmip6`, `met-office-*`, `conus404`
  - Planet NICFI: `planet-nicfi-analytic` and `planet-nicfi-visual` (assets only for GEO-Microsoft RFP winners)
  - new in 2026: **`nested-eagle-conus` and `nested-eagle-global`** (NOAA's experimental AI ensemble forecasts, CC BY 4.0); **`predicted-damage-venezuela-2026`** (Microsoft AI for Good building-damage map after the June 2026 Venezuela earthquakes, CC BY 4.0); **`predicted-damage-colombia-2026`** (August 2026 Colombia earthquake, CC BY 4.0)
- **Access:** `https://planetarycomputer.microsoft.com/api/stac/v1`; `pip install pystac-client planetary-computer` (planetary-computer 1.0.0 is still the current PyPI release):
  ```python
  import pystac_client, planetary_computer
  cat = pystac_client.Client.open("https://planetarycomputer.microsoft.com/api/stac/v1", modifier=planetary_computer.sign_inplace)
  ```
- **Auth:** no.
- **License:** per collection.
- **Time to first data:** minutes.
- **Hackathon fit:** the best no-signup STAC for Sentinel-1 RTC, Sentinel-2 L2A, HLS, Landsat and the 2026 earthquake damage layers.
- **Sources:** [Hub retirement discussion #347](https://github.com/microsoft/PlanetaryComputer/discussions/347), [PC data catalog docs](https://planetarycomputer.microsoft.com/docs/concepts/data-catalog), [PC STAC collections (live)](https://planetarycomputer.microsoft.com/api/stac/v1/collections)

#### Google Earth Engine (noncommercial)
- **Status in 2026:** noncommercial quota tiers took effect on **27 April 2026** (still rolling out). Quotas are per project and reset monthly on the 1st:
  - **Community:** 150 EECU-hours/month, for all verified noncommercial projects.
  - **Contributor:** 1,000 EECU-hours/month; needs an active billing account, but noncommercial use is not charged.
  - **Partner:** 100,000 EECU-hours/month; separate application, review "can take several weeks."
  - Over the limit, jobs run in "restricted mode" at reduced throughput.
  - New projects pick a tier when they register for Earth Engine; a project with no tier defaults to Community.
- **Size:** multi-petabyte catalog (Sentinel, Landsat, MODIS, VIIRS, ERA5, Dynamic World, AlphaEarth Satellite Embedding `GOOGLE/SATELLITE_EMBEDDING/V1/ANNUAL`, and more).
- **Access:** `pip install earthengine-api` (plus `geemap`); `ee.Authenticate(); ee.Initialize(project="your-cloud-project")`.
- **Auth:** **yes.** A Google account and a Google Cloud project registered for Earth Engine with noncommercial use attested.
- **License:** per dataset; Earth Engine terms of service.
- **Time to first data:** 15–30 minutes (registration), then seconds per query.
- **Hackathon fit:** the fastest way to do planet-scale computation (time series over a country) without downloading anything. 150 EECU-hours is plenty for a weekend.
- **Sources:** [Earth Engine noncommercial tiers](https://developers.google.com/earth-engine/guides/noncommercial_tiers)

#### AWS Earth Search (Element 84)
- **What:** a public STAC API over AWS Open Data.
- **Collections (checked live 2026-10-24):** `sentinel-2-l2a`, `sentinel-2-c1-l2a` (Collection-1 reprocessing), `sentinel-2-pre-c1-l2a`, `sentinel-2-l1c`, `sentinel-1-grd`, `landsat-c2-l2` (from 1982), `naip` (2010–2022), `cop-dem-glo-30`, `cop-dem-glo-90`.
- **Access:** `https://earth-search.aws.element84.com/v1`. Data is in public COG buckets (for example `s3://e84-earth-search-sentinel-data`, us-west-2). Landsat (`s3://usgs-landsat`) and NAIP (`s3://naip-analytic`) are **requester-pays**: you need AWS credentials and pay egress.
- **Auth:** no for Sentinel-2 COGs; AWS credentials for the requester-pays buckets.
- **Time to first data:** minutes.
- **Sources:** [Earth Search STAC (live)](https://earth-search.aws.element84.com/v1/collections), [AWS registry Sentinel-2 COGs](https://registry.opendata.aws/sentinel-2-l2a-cogs/), [AWS registry USGS Landsat](https://registry.opendata.aws/usgs-landsat/)

#### AWS Open Data Registry (general)
- **What:** the catalog of public datasets hosted on S3. The GitHub repo has 1,243 dataset YAML files (checked 2026-10-24), of which about 400 match space or EO keywords.
- **Space-relevant 2025–2026 entries seen in the metadata:**
  - embeddings: **Google Satellite Embedding V1 (AlphaEarth)** mirrored at `s3://us-west-2.opendata.source.coop/tge-labs/aef` (CC BY 4.0); **TESSERA** embeddings `s3://tessera-embeddings/v1.1/dclimate.icechunk` (CC BY-SA); Clay v1.5 Sentinel-2 embeddings `s3://us-west-2.opendata.source.coop/clay/clay-v1-5-sentinel2`
  - commercial open data: **Vantor Open Data Program** `s3://vantor-opendata` (us-east-1, CC BY-NC); Maxar Open Data `s3://maxar-opendata` (us-west-2, CC BY-NC); **SpaceEye-T VVHR EO Open Data** `s3://st-vvhr-opendata` (CC BY 4.0); ICEYE `s3://iceye-open-data-catalog`; Capella `s3://capella-open-data/data/`; Umbra `s3://umbra-open-data-catalog`; Satellogic EarthView `s3://satellogic-earthview`
  - NOAA space weather: `s3://noaa-swpc-pds`; WSA-Enlil CME model runs `s3://noaa-wsa-enlil-pds`; **GOES-19 SWFO CCOR-1 coronagraph** `s3://noaa-nesdis-swfo-ccor-1-pds`; WAM-IPE thermosphere density `s3://noaa-nws-wam-ipe-pds`
  - other: DMSP SSJ auroral particles `s3://dmspssj`; GNSS radio occultation `s3://gnss-ro-data`; Sentinel-1 precise orbits `s3://s1-orbits`; Surya Bench `s3://nasa-surya-bench`; Lunar FM Bench `s3://nasa-lunar-fm-bench`; the YAOKI rover; Catalina Sky Survey; Euclid, SPHEREx, ZTF and WISE on IRSA; MAST
  - about 144 NASA Earthdata Cloud entries (protected buckets such as `lp-prod-protected`, `podaac-ops-cumulus-protected`, `gesdisc-cumulus-prod-protected`, `nsidc-cumulus-prod-protected`, `asdc-prod-protected`, `ornl-cumulus-prod-protected`) that need Earthdata Login
- **Access:** `aws s3 ls --no-sign-request s3://<bucket>/` for public buckets.
- **Sources:** [AWS Open Data Registry](https://registry.opendata.aws/), [registry GitHub](https://github.com/awslabs/open-data-registry)

#### Copernicus Data Space Ecosystem (CDSE)
- **What:** ESA/EC's official free access point for all Sentinel data plus Copernicus services.
- **Size (checked live 2026-10-24):** the STAC API `https://stac.dataspace.copernicus.eu/v1` lists **427 collections**:
  - **Sentinel-1:** GRD, SLC, SLC bursts, ETAD, OCN, and **Sentinel-1 global mosaics**
  - **Sentinel-2:** L1C, L2A, GRI, **Sentinel-2 global mosaics**, and **"Sentinel-2 Night-Time Acquisitions"**
  - **Sentinel-3:** the full OLCI/SLSTR/SRAL/SYNERGY suite, NRT/STC/NTC
  - **Sentinel-5P:** L1 and L2 for NO2, CH4, CO, SO2, HCHO, O3 and its profile, tropospheric O3, aerosols, cloud
  - **Sentinel-6:** AMR-C, P4 L1B and L2
  - **Copernicus DEM:** GLO-30/90 COG and EEA-10
  - **Landsat C2 L1** and a MODIS Terra/Aqua mirror
  - **Copernicus Contributing Missions:** `ccm-optical`, `ccm-sar`, `ccm-hyperspectral-*`, `ccm-thermal-*`, `ccm-atmospheric-ch4-*`; access restricted by user category
  - a large CLMS land-monitoring catalog (burnt area, DMP and others)
- **Access:**
  - STAC API (above), OData, openEO, Sentinel Hub APIs (Process, Catalog, Statistical), and the CDSE JupyterLab.
  - **S3:** endpoint `https://eodata.dataspace.copernicus.eu/`, bucket `eodata` (for example `s3://eodata/Sentinel-2/...`). Generate keys at `https://eodata-s3keysmanager.dataspace.copernicus.eu/` (the secret is shown only once).
- **Auth:** **yes** (a free CDSE account; minutes to register).
- **Quotas (free "Copernicus General" users):**
  - S3/OData/STAC: 2,000 requests/min (S3), 20 MB/s per connection, 4 concurrent connections, **12 TB/month**. Above 12 TB, throttled to 1 MB/s and 1 connection.
  - openEO: **10,000 credits/month**, 2 concurrent jobs.
  - Sentinel Hub: **10,000 requests/month and 10,000 PU/month**, 300 requests/min.
  - Direct COG HTTP: 50,000 requests/month.
  - Each file in a recursive S3 download counts as a request.
- **Time to first data:** 10–20 minutes.
- **Hackathon fit:** the only official source for full Sentinel-1 SLC and Sentinel-5P archives, plus global Sentinel-1/2 mosaics. Note the Sentinel-2 night-time acquisitions collection for a city-lights or gas-flare angle.
- **Sources:** [CDSE STAC (live)](https://stac.dataspace.copernicus.eu/v1/collections), [CDSE quotas](https://documentation.dataspace.copernicus.eu/Quotas.html), [CDSE S3 access](https://documentation.dataspace.copernicus.eu/APIs/S3.html)

#### NASA Earthdata Cloud (CMR + earthaccess)
- **What:** NASA's Earth science archive (DAACs) migrated to AWS us-west-2, indexed by the Common Metadata Repository.
- **Size (checked live 2026-10-24):** CMR reports **53,634 collections**, of which **9,534 are cloud-hosted**.
- **Access:** `pip install earthaccess` (0.19.0, 2026-09-04):
  ```python
  import earthaccess
  earthaccess.login()
  r = earthaccess.search_data(short_name="ATL06", bounding_box=(-10,20,10,50), temporal=("2019-01","2019-03"), count=10)
  earthaccess.download(r, "./data")
  ```
  CMR search at `https://cmr.earthdata.nasa.gov/search/collections.json`. Direct S3 reads of `*-protected` buckets are meant for in-region (us-west-2) compute; from a laptop, use HTTPS download or streaming through earthaccess.
- **Auth:** **yes** (a free NASA Earthdata Login; instant, but some datasets need per-DAAC application approval inside the profile).
- **License:** NASA open data. The AWS registry entries for Earthdata collections list CC BY 4.0.
- **Time to first data:** 10–20 minutes.
- **Sources:** [PyPI earthaccess](https://pypi.org/project/earthaccess/), [earthaccess docs](https://earthaccess.readthedocs.io/en/latest/), [CMR (live)](https://cmr.earthdata.nasa.gov/search/collections.json?page_size=1)

#### Source Cooperative (Radiant Earth)
- **What:** a nonprofit data-publishing utility on cloud object storage, and the successor home for Radiant MLHub-era datasets and many 2025–2026 EO releases (VIDA combined buildings, Clay embeddings, AlphaEarth embedding mirror, Planet RapidAI4EO, National Wetlands Inventory). The site states "all data hosted in Source is available to the public."
- **Access:**
  - Anonymous HTTPS: `https://data.source.coop/{account}/{repository}/{path}` (checked live: the VIDA README returned 200).
  - S3 bucket: `s3://us-west-2.opendata.source.coop/{account}/{repository}/` (as listed in AWS registry entries).
  - Example: `https://data.source.coop/vida/google-microsoft-osm-open-buildings/geoparquet/by_country/country_iso={ISO}/{ISO}.parquet`.
- **Auth:** no.
- **Time to first data:** minutes (DuckDB or GeoPandas on GeoParquet).
- **Sources:** [Source Cooperative](https://source.coop/), [Source docs](https://docs.source.coop/), [VIDA buildings repo page](https://source.coop/vida/google-microsoft-osm-open-buildings)

#### NASA Open Data Portal (data.nasa.gov) and NASA Image and Video Library
- **data.nasa.gov:** a CKAN catalog. `https://data.nasa.gov/api/3/action/package_search?rows=1` reports **36,451 datasets** (checked live; the first hit was Voyager 1 PRA Jupiter-encounter radio data). It is a metadata hub pointing to PDS, DAACs, OSDR and others. No auth.
- **NASA Image and Video Library API:** `https://images-api.nasa.gov/search?q=...&media_type=image`, no key required (checked live). Useful for illustrated explainers and image-text datasets. NASA media guidelines apply.
- **api.nasa.gov** (APOD, NeoWs, DONKI, EPIC, Mars photos): needs a free key; **DEMO_KEY was rate-limited (HTTP 429) on 2026-10-24.**
- **Sources:** [data.nasa.gov CKAN API (live)](https://data.nasa.gov/api/3/action/package_search?rows=1), [images-api.nasa.gov](https://images-api.nasa.gov/search?q=starlink&media_type=image), [api.nasa.gov](https://api.nasa.gov/)

#### Kaggle (space and astronomy classics)
- **Access:** `pip install kaggle` and an API token (free account). The `view` metadata endpoint works without auth: `https://www.kaggle.com/api/v1/datasets/view/<owner>/<slug>`.
- **Verified astronomy entries (metadata fetched live 2026-10-24):**
  - `Cornell-University/arxiv`: 5.63 GB, CC0, updated 2026-10-17
  - `keplersmachines/kepler-labelled-time-series-data` ("Exoplanet Hunting in Deep Space"): 291 MB, CC0, 2017
  - `nasa/kepler-exoplanet-search-results`: 3.7 MB, CC0, 2017
  - `fedesoriano/stellar-classification-dataset-sdss17`: 16.8 MB, 2022
  - `brsdincer/star-type-classification`: 8 kB, 2021
- **Time to first data:** minutes.
- **Caveat:** these are small, static, heavily used teaching sets. Judges may see them as "Kaggle tutorial" projects; prefer the live sources above.
- **Sources:** [Kaggle arXiv](https://www.kaggle.com/datasets/Cornell-University/arxiv), [Kaggle Kepler labelled time series](https://www.kaggle.com/datasets/keplersmachines/kepler-labelled-time-series-data), [Kaggle Kepler exoplanet search results](https://www.kaggle.com/datasets/nasa/kepler-exoplanet-search-results), [Kaggle SDSS17 stellar classification](https://www.kaggle.com/datasets/fedesoriano/stellar-classification-dataset-sdss17)

#### Hugging Face Hub (space and EO datasets)
- **What:** dataset hosting with streaming, Parquet and DuckDB `hf://` access.
- **Notable space and EO organizations and datasets seen via the Hub API (2026-10-24):**
  - astronomy: `juliensimon` (~200 space tables, see 2.6), `MultimodalUniverse` (24), `mwalmsley` (Galaxy Zoo, 35)
  - NASA/IBM: `nasa-ibm-ai4science` (Surya-bench tasks, SomBench lunar tasks, `core-sdo` at **363 GB**), `nasa-impact` (WxC-Bench and NASA science-domain IR/QA benchmarks)
  - methane: `UNEP-IMEO/MARS-S2L` and `UNEP-IMEO/MARS-Hyperspectral`
  - telemetry and orbits: `patrickfleith/GOCE-satellite-telemtry` (5,923 downloads); `FraDra/GEO_satellite_maneuvers`
  - spacecraft vision: `RiceD2KLab/SWiM-SpacecraftWithMasks`, EPFL `SwissCube`/`PocketQube` spacecraft pose, `arclabmit/spacecraft_issdocking_dataset`, `arclabmit/lunar_lander_dataset`
  - planetary: `harpreetsahota/Mars-HiRISE`; `elementrobotics/lunarsim-shoemaker-traverse-100m-v1`
  - EO: `isp-uv-es/seefar-sentinel-taco`, `SustainabilityLabIITGN/SentinelKilnDB`, `satellite-image-deep-learning/*` mirrors
- **Access:** `pip install datasets`; `load_dataset(id, streaming=True)`; `duckdb`: `SELECT * FROM 'hf://datasets/<id>/<file>.parquet'`.
- **Auth:** no for public datasets; a free token for gated ones.
- **Time to first data:** minutes.
- **Sources:** [HF datasets API search](https://huggingface.co/api/datasets?search=satellite), [HF juliensimon](https://huggingface.co/juliensimon), [HF nasa-ibm-ai4science](https://huggingface.co/nasa-ibm-ai4science), [HF nasa-impact](https://huggingface.co/nasa-impact)

## 3. Gotchas
- **api.nasa.gov DEMO_KEY is rate-limited per IP.** A test call on 2026-10-24 returned `429 OVER_RATE_LIMIT`. Get a free personal key at api.nasa.gov (instant); on shared hackathon Wi-Fi, DEMO_KEY will fail.
- **Rubin DP1/EDP2 need data rights.** Only Rubin Science Platform accounts for US/Chile scientists and students and in-kind members can access them; alerts are public via brokers.
- **Space-Track redistribution.** The HF `space-track-tle-history` mirror is labelled CC-BY-4.0 but is "Sourced from Space-Track.org bulk exports". Space-Track's user agreement restricts redistribution, so treat the license as uncertain for a public demo; cite and consider using CelesTrak GP data for anything you republish.
- **Earth Engine quotas since 27 Apr 2026:** 150 EECU-hours/month on Community. Register the Cloud project as noncommercial first.
- **CDSE throttling:** 4 concurrent S3 connections and 12 TB/month; each file counts as a request.
- **Requester-pays buckets** (`usgs-landsat`, `naip-analytic`, `sentinel-s2-l1c`, `modis-astraea`, arXiv `s3://arxiv`) need AWS credentials and cost egress. Prefer Planetary Computer or Earth Search COG mirrors.
- **Planetary Computer:** the Hub is gone (since June 2024); reads need SAS signing (`planetary_computer.sign_inplace`); Planet-NICFI assets there are restricted.
- **zsh tip:** `echo ====` fails in zsh (equals expansion), and CMR URLs with `options[short_name][pattern]` break unquoted (glob). Quote URLs or use Python `urllib`.
- **NASA GSFC hosts were unreachable from this network on 2026-10-24** (CDAWeb HAPI, SPDF OMNI, CCMC DONKI all timed out). Have the HF mirrors (`juliensimon/omni-solar-wind-parameters`, `donki-space-weather-events`, `dst-index`) as a fallback.
- **SWPC endpoint drift:** `products/solar-wind/plasma-7-day.json` now returns 404. Use `json/rtsw/rtsw_wind_1m.json`, whose `source` field now reads IMAP.
- **telemanom data link is dead** (S3 403); use the Kaggle mirror `patrickfleith/nasa-anomaly-detection-dataset-smap-msl`.
- **Space-Track and ESA DISCOS both return 401 without credentials.** Register on day 0; Space-Track approval is not instant.
- **CDS/ADS (ERA5, CAMS):** new endpoint `https://cds.climate.copernicus.eu/api`, `cdsapi>=0.7.7`, and **each dataset's licence must be accepted manually on the web page** or requests fail.
- **FIRMS:** the 24-hour global CSVs are open, but the area/date API needs a free MAP_KEY ("Invalid MAP_KEY." otherwise).
- **AlphaEarth COGs on Source Cooperative are "bottom-up";** open them through the provided `.vrt`, or GDAL reads them flipped.
- **Non-commercial licences:** Vantor/Maxar open data (CC BY-NC 4.0), UNEP MARS-S2L (CC BY-NC-SA), RAPID flood maps (CC BY-NC-SA), Context Trails (CC BY-NC). Fine for a hackathon demo; flag them if pitching a startup.
- **Planet NICFI's free phase has ended** (planet.com/nicfi redirects to /impact/; PC NICFI assets are restricted). Don't plan on free Planet tropics imagery.
- **Earthdata in-region buckets** (`*-protected`) are for us-west-2 compute; from a laptop use `earthaccess.download` over HTTPS. Some DAACs (e.g. NISAR via ASF) also require accepting an EULA in the Earthdata profile.
- **CelesTrak usage policy:** pull each GP group at most once per update; repeated scraping gets the IP blocked (one blocked IP at a venue hurts everyone).

## 4. Cross-slice leads
- (EO companies) **Maxar Open Data now appears as "Vantor Open Data Program"** (`s3://vantor-opendata`, us-east-1) alongside the legacy `s3://maxar-opendata` (us-west-2), both CC BY-NC. Rebrand to verify.
- (EO companies) SpaceEye-T VVHR open data on AWS (`s3://st-vvhr-opendata`, CC BY 4.0), likely Satrec Initiative's SpaceEye-T satellite.
- (EO analytics) Microsoft AI for Good's 2026 earthquake building-damage layers for Venezuela (June 2026) and Colombia (August 2026) on Planetary Computer.
- (Models and tools) NOAA "nested-EAGLE" experimental AI ensemble forecasts (Anemoi-based) published as Planetary Computer collections, citing arXiv 2608.26822.
- (Space traffic) the HF `juliensimon` collection has Starlink, Kuiper, OneWeb and AST SpaceMobile fleet tables, FCC NGSO filings and Starlink ground stations, refreshed daily.
- (SpaceX/xAI/orbital compute) HF dataset `CyberMax-tools/orbitwren-orbital-compute-tracker` (updated 2026-10-24), an orbital-compute tracker; not inspected.
- (Space science) `nasa-impact/nasa-smd-qa-benchmark`, `nasa-smd-IR-benchmark` and `nasa-sde-IR-benchmark-20251024-v5` on HF (NASA Science Mission Directorate retrieval/QA benchmarks).
- (Space weather) GOES-19 CCOR-1 coronagraph on AWS (`s3://noaa-nesdis-swfo-ccor-1-pds`), the first operational NOAA coronagraph, 96 FITS files per day per level.
- (Space weather / US agencies) **NOAA real-time solar wind (RTSW) now reports `source: IMAP`** (checked 2026-10-24), so NASA's IMAP has become the operational L1 upstream monitor feeding SWPC.
- (EO companies) **Vantor Open Data has 11 event folders, all from 2026**, including `Mexico-Hurricane-Simon-Oct-2026` and `DRC-Ebola-May-2026`. **Umbra** added `Nepal-Disaster-Coverage_September-2026` and SAR tasks over ports, lithium and gold mines, and Kourou spaceport.
- (US agencies) NISAR products in CMR are still labelled **BETA_V1 / PROVISIONAL_V1** (Oct 2026), across L0B to L3 soil moisture.
- (EO analytics) **Hansen Global Forest Change v1.13 (2025 loss year)** is posted (`GFC-2025-v1.13`). **Carbon Mapper's public catalog has 45,539 plumes**, including Tanager-1 detections from Sept 2026.
- (Space traffic) CelesTrak active catalogue on 2026-10-24: 16,792 objects, of which 11,141 are Starlink and 391 Kuiper.
- (Models and tools) WeatherBench 2 hosts archived forecasts for Aurora, GenCast, GraphCast, FuXi, Pangu and NeuralGCM, useful for AI-weather comparisons.

## 5. Leads not followed
- The exact November 2026 day of the Euclid DR1-Foundation release (watch https://www.cosmos.esa.int/web/euclid/timeline). It could land during or just after the hackathon.
- Rubin Data Preview 2 / "EDP2" release date.
- Planetary Computer Pro GA date (third-party source only).
- Dynamic World, MapBiomas, Global Fishing Watch, GLAD/RADD alerts, WorldCereal, WorldPop, Kontur: not checked live in this pass (EE IDs and URLs from documentation).
- CAMS/ADS, CDAWeb/OMNI, DONKI (CCMC): endpoints not reachable or not tested live today.
- MIT ARCLab Prize datasets (SPLID pattern-of-life, 2025 drag challenge): not located by name on Zenodo or HF.
- NASA PCoE prognostics (C-MAPSS, batteries), ISS Live! telemetry, the launch-failure database beyond LL2/GCAT.
- UCS Satellite Database: whether the original is still updated (only the HF mirror was checked).
- ESA Biomass L2 release schedule and the exact access path (MAAP).
- China's CLPDS (Chang'e/Tianwen) contents and registration.
