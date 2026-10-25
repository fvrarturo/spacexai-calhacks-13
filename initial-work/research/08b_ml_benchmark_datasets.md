# Slice C: ML benchmark and training datasets for Earth observation (verified 2026-10-24)

**How this was verified.** The shared web-search budget was already used up when I started, so I ran zero web searches. Instead I checked everything directly:
- anonymous listings of S3, GCS and Azure buckets (sizes are totals of the actual object sizes);
- catalogue APIs: Hugging Face `/api/datasets`, Zenodo `/api/records/<id>`, Source Cooperative `/api/v1/products/<account>`, `data.source.coop`, Kaggle dataset-view, NASA CMR;
- raw GitHub READMEs and TorchGeo v0.10.1 source code;
- WebFetch of official pages.

No subagents could be spawned (the concurrent-subagent limit was reached), so I did the whole slice myself.

**Consequences:**
- **No tweets or X posts were found.** I had no way to search for them; "community" sources below are HF and Source Cooperative uploads.
- **HF sizes are each repo's `usedStorage`.** This can include file history, so treat it as an upper bound.
- **Download times assume about 20 MB/s venue Wi-Fi** (≈70 GB per hour). That is my assumption, not a measurement.

---

## 1. Quick-pick table

| Dataset | Category | Size | Access | Auth | Time-to-first-data |
|---|---|---|---|---|---|
| SpaceNet 8 (flood) | Disaster: buildings/roads | 7.3 GB (3 tarballs) | `s3://spacenet-dataset/spacenet/SN8_floods/tarballs/` | none | ~10 min |
| SpaceNet 9 (optical↔SAR registration) | Disaster / co-registration | 0.56 GB | `https://spacenet-dataset.s3.us-east-1.amazonaws.com/spacenet/SN9_cross-modal/train.zip` | none | ~1 min |
| SpaceNet 7 (multi-temporal urban) | Buildings change | 9.2 GB train + 1.25 GB test | `s3://spacenet-dataset/spacenet/SN7_buildings/tarballs/` | none | ~10 min |
| SpaceNet 1–6 | Buildings / roads / SAR | 5 GB (SN1) to ~200 GB (SN4) | `s3://spacenet-dataset/spacenet/SN{1..6}_*/tarballs/` | none | min (SN1, samples) to hours |
| fMoW-rgb / fMoW-full | Functional land use | ~200 GB / ~3.5 TB | `s3://spacenet-dataset/Hosted-Datasets/fmow/` | none | hours (ground truth 0.25 GB in min) |
| fMoW-Sentinel | Land use, S2 time series | 882k images (size not stated) | purl.stanford.edu/vg497cb6002 | none stated | unknown/hours |
| xView1 | Object detection 0.3 m | 1M objects; TACO copy 20.3 GB | registration at xviewdataset.org, or HF `isp-uv-es/xview-taco` | registration (original) / none (HF) | ~20 min via HF |
| xBD / xView2 | Building damage | ~7.8 GB train + 2.6 GB test (challenge); TACO 35 GB | xview2.org (login), HF `isp-uv-es/xview2-taco` | login / none | ~10–30 min |
| xView3-SAR | Dark-vessel detection | 991 S1 scenes, 1,400 gigapixels | iuu.xview.us | registration (unverified) | hours |
| DOTA v1/1.5/v2 | Oriented object detection | HF mirror 23.9 GB | `isaaccorley/dota` (TorchGeo `DOTA`) | none | ~20 min |
| DIOR | Object detection | 7.4 GB | HF `torchgeo/dior` | none | ~6 min |
| iSAID | Instance segmentation | annotations 0.21 GB + DOTA images | Google Drive/Baidu; HF `isaaccorley/isaid` | none | ~30 min |
| FAIR1M | Fine-grained detection | 9.2 GB | HF `blanchon/FAIR1M` | none | ~8 min |
| RarePlanes | Aircraft detection | real PS-RGB tiled 2.0 GB; full ~140 GB real + ~70 GB synthetic | `s3://rareplanes-public/` | none | ~2 min (tiled) |
| BRIGHT (DFC2025) | Multimodal building damage | 10.2 GB | HF `isaaccorley/bright` (TorchGeo `BRIGHT`) | none | ~9 min |
| Open Cities AI | Drone building footprints, Africa | 32 + 41 + 9 GB | Azure `radiantearth.blob.core.windows.net/mlhub/archives/open_cities_ai_challenge_*` | none | 30 min–1 h |
| RAMP | Building footprints, 22 cities | 0.1–2.6 GB per city | Source Coop `ramp/ramp`; Azure archives | none | ~2 min |
| HRSID | SAR ship detection | 0.61 GB (HF YOLO copy) | Google Drive/Baidu; HF `dronefreak/HRSID` | none | ~1 min |
| SSDD | SAR ship detection | 0.05 GB (HF copy) | Google Drive/Baidu; HF `dronefreak/SSDD` | none | <1 min |
| OpenSARShip | S1 ship chips | not stated | opensar.sjtu.edu.cn | not stated | unknown |
| OSSDD (2026) | S1 ship detection | 72.3 GB (TACO 12 GB) | HF `sylviaHoch/OpenSARShip-Ship-Detection-Dataset`, `isp-uv-es/ossdd-taco` | none | ~10 min (TACO) |
| ShipsNet | Ship chips, Planet | 0.45 GB | Kaggle `rhammell/ships-in-satellite-imagery` | Kaggle account | ~2 min |
| Airbus Ship Detection | Optical ship segmentation | unverified | Kaggle competition `airbus-ship-detection` | Kaggle + accept rules | ~30 min (unverified) |
| Satlas marine infrastructure | Offshore platforms / turbines | 18.6 GB | `s3://ai2-public-datasets/satlas/satlas-dataset-marine-infrastructure-v1.zip` | none | ~15 min |
| MARIDA | Marine debris (S2) | 1.16 GB | Zenodo 5151941 | none | ~1 min |
| MADOS | Marine debris + oil spill | 4.04 GB | Zenodo 10664073 | none | ~4 min |
| NASA Marine Debris (PlanetScope) | Debris object detection | ~0.08 GB | Source Coop `nasa/marine-debris`; TorchGeo `NASAMarineDebris` | none | <1 min |
| BigEarthNet v2 (reBEN) | Multi-label land cover S1/S2 | S2 ~59 GiB, S1 ~51 GiB | Zenodo 10891137 | none | 45 min–1.5 h |
| EuroSAT (MS / RGB) | Land use classification | 2.07 GB / 0.09 GB | Zenodo 7711810; HF `torchgeo/eurosat` | none | ~2 min |
| EuroSAT-SAR | S1 land use | 3.8 GB | HF `wangyi111/EuroSAT-SAR` | none | ~3 min |
| SEN12MS | S1/S2/MODIS triplets | 180,662 patches (size not stated) | FTP `dataserv.ub.tum.de` (m1474000) | public FTP credentials | "several hours" |
| SEN12MS-CR / CR-TS | Cloud removal | HF copy 389 GB | mediaTUM 1554803 / 1639953; HF `Hermanni/sen12mscr` | none | hours (subset: min) |
| SSL4EO-S12 v1 | SSL pretraining S1/S2 | 1.5 TB raw; 20–50 GB per modality (8-bit) | mediaTUM 1660427/1702379; HF `wangyi111/SSL4EO-S12` | none | ~1 h (8-bit), 600 MB sample |
| SSL4EO-S12 v1.1 | SSL, multimodal + 4 seasons | 4.8 TB repo (shardable) | HF `embed2scale/SSL4EO-S12-v1.1` | none | min (one shard) |
| SSL4EO-L | Landsat SSL | 1.74 TB; benchmark 47.8 GB | HF `torchgeo/ssl4eo_l`, `torchgeo/ssl4eo_l_benchmark` | none | ~40 min (benchmark) |
| SatlasPretrain | Huge multi-task | v1 small S2 500 GB; labels 119 GB; full >30 TB | `s3://ai2-public-datasets/satlas/` | none | hours |
| Major TOM | Global S2/S1/DEM/embeddings | 0.3 GB to 23.6 TB per repo | HF `Major-TOM/*` (parquet) | none | min (one shard) |
| TerraMesh (2025–26) | Multimodal pretraining | 18.4 TB; 9M+ patches | HF `ibm-esa-geospatial/TerraMesh` | none | min (one shard) |
| OlmoEarth pretrain | Multimodal pretraining | 16.1 TB | HF `allenai/olmoearth_pretrain_dataset` | none | min (one file) |
| Copernicus-Pretrain | S1/2/3/5P pretraining | 18.7M samples, 22.7 TB | HF `wangyi111/Copernicus-Pretrain` | none | min (shard) |
| MMEarth | 12-modality pretraining | 48 GB (100k) to 597 GB | sid.erda.dk share links | none | ~40 min (100k) |
| SeCo | Seasonal contrast pretraining | 7.3 GB (100k) / 36 GB (1M) | Zenodo 4728033 | none | ~6 min |
| S2-100K (SatCLIP) | Location-encoder pretraining | 168 GB (TACO 44 GB) | HF `torchgeo/s2-100k` | none | ~40 min (TACO) |
| Five Billion Pixels | GF-2 land cover, 24 classes | 150 images | Google Drive / Baidu | none | ~30 min (unverified size) |
| OpenEarthMap | 0.25–0.5 m land cover | 9.1 GB (+ xBD images needed) | Zenodo 7223446 | none | ~8 min |
| LoveDA | Urban/rural land cover | 9.57 GB | Zenodo 5706578 | none | ~8 min |
| LandCoverNet | Global LC, S1/S2/L8 | per continent up to ~88 GB S2 | Source Coop `radiantearth/landcovernet` | none | ~10 min (labels + L8) |
| DynamicEarthNet | Daily Planet LC change | 563 GB (HF) / 93 GB (GEO-Bench-2) | mediaTUM 1650201; HF `torchgeo/dynamic_earthnet` | none | 1–2 h (GB2 version) |
| CloudSEN12 / CloudSEN12+ | S2 cloud segmentation | 332–419 GB (streamable) | HF `tacofoundation/cloudsen12`, `isp-uv-es/CloudSEN12Plus` | none | min (streaming / TACO) |
| Cloud Cover Detection (DrivenData) | S2 cloud masks | 17.3 + 16 GB | Source Coop `radiantearth/cloud-cover-detection-challenge` | none | ~15 min |
| GEO-Bench (v1) | FM benchmark suite | ~65 GB disk | `pip install geobench; geobench-download` | none | ~1 h |
| GEO-Bench-2 | FM benchmark suite (18 sets) | 0.5–401 GB per set | `pip install geobenchv2; geobench-download` (HF `aialliance/*`) | none | min per small set |
| PANGAEA | FM benchmark suite | per dataset | GitHub `VMarsocci/pangaea-bench` | none | varies |
| Copernicus-Bench | 15 tasks, S1/S2/S3/S5P | 155 GB | HF `wangyi111/Copernicus-Bench` (TorchGeo) | none | min per task |
| TorchGeo (library) | Loader for ~75 benchmarks | n/a | `pip install torchgeo` (v0.10.1) | none | min |
| TACO catalogue (isp-uv-es) | 134 repackaged datasets | 0.03–112 GB each | HF `isp-uv-es/*-taco` | none | min |
| MOSAIKS | Precomputed features | global 0.01° grid | mosaiks.org + Redivis | Redivis account | ~30 min |
| SustainBench | 15 SDG tasks | very large ("5 TB disk") | Google Drive | Google account for big folders (unverified) | hours |
| Sen1Floods11 | Flood segmentation | 36.9 GB bucket | `gs://sen1floods11` | none | ~30 min (hand-labelled subset faster) |
| SEN12-FLOOD | Flood time series S1/S2 | 6.4 + 4.2 GB | Source Coop `esa/sen12flood`; Azure archives | none | ~10 min |
| Kuro Siwo | Global SAR flood | ~1 TB (HF); 15 GB GEO-Bench-2 | HF `orion-ai-lab/Kuro-Siwo-*`; `aialliance/kuro_siwo` | none | ~12 min (GB2) |
| WorldFloods v2 | Flood extent (S2) | 79 GB | HF `isp-uv-es/WorldFloodsv2` | none | ~1 h |
| MMFlood | SAR flood | 11.2 GB | HF `links-ads/mmflood` | none | ~9 min |
| ImpactMesh-Flood (2026) | Multimodal flood | 361 GB (modality subsets) | HF `ibm-esa-geospatial/ImpactMesh-Flood` | none | min (val/S2RGB) |
| ImpactMesh-Fire (2026) | Multimodal wildfire | 153.5 GB | HF `ibm-esa-geospatial/ImpactMesh-Fire` | none | min (subset) |
| Next Day Wildfire Spread | Fire spread | 3.96 GB | Kaggle `fantineh/next-day-wildfire-spread` | Kaggle account | ~4 min |
| WildfireSpreadTS | Fire spread time series | 48.4 GB (TACO 8.4 GB) | Zenodo 8006177 | none | ~8 min (TACO) |
| FireCube | Greece daily datacube | 23.5 GB netCDF | Zenodo 6475592 | none | ~20 min |
| SeasFire | Global seasonal fire cube | 44 GB (v0.3); 67.9 GB (monthly) | Zenodo 8055879; HF `orion-ai-lab/seasfire_monthly` | none | ~35 min |
| California Burned Areas (CaBuAr) | Burn-scar segmentation | HDF5 (repo 159 GB) | HF `DarthReca/california_burned_areas` | none | min (one config) |
| TS-SatFire | Fire lifecycle (VIIRS) | 76.3 GB | Kaggle `z789456sx/ts-satfire` | Kaggle account | ~1 h |
| HLS Burn Scars | Burn scars (Prithvi) | 804 scenes (TACO 3.7 GB) | HF `ibm-nasa-geospatial/hls_burn_scars` | none | ~3 min |
| Landslide4Sense | Landslide segmentation | 3.1 GB | Zenodo 10463239; HF `ibm-nasa-geospatial/Landslide4sense` | none | ~3 min |
| QuakeSet | Earthquake (S1) | 11 GB | HF `DarthReca/quakeset` | none | ~9 min |
| Event-SAR (2026) | InSAR quake/volcano | 92.8 GB | HF `GFM-Bench/Event-SAR` | none | ~1 h |
| STARCOP | Methane (AVIRIS-NG) | 60.8 GB; mini set on Drive | Zenodo 7863343 | none | ~5 min (mini) |
| MethaneSET (2026) | Methane S2/L8-9/EMIT | 1.1 GB (L89-finetune) to 1,165 GB (EMIT) | HF `tacofoundation/methaneset` | none | ~2 min (finetune sets) |
| CH4Net | Methane S2 (Turkmenistan) | not stated | HF `av555/ch4net` | HF login + accept terms (gated) | ~min after approval |
| MethaneS2CM | Methane S2 × Carbon Mapper | 16.1 GB | HF `H1deaki/MethaneS2CM` | none | ~13 min |
| EMIT L2B CH4 plume complexes | Methane plumes (NASA) | 1,686 granules (V002) | NASA CMR / earthaccess | Earthdata login (usual; unverified) | ~10 min |
| Carbon Mapper plumes | CH4/CO2 plumes | not stated | carbonmapper.org data portal, Data/STAC API | account for API | ~15 min |
| CropHarvest | Crop / non-crop pixels | 22.7 GB (features 0.07 GB) | Zenodo 7257688; `pip install cropharvest` | none | ~1 min (features) |
| PASTIS / PASTIS-R | Panoptic crop parcels | 28.8 / 53.7 GB (100-patch subset 4.1 GB) | Zenodo 5012942 / 5735646; HF `torchgeo/PASTIS-R-100` | none | ~4 min (subset) |
| Sen4AgriNet | Crop type, S2 (EU) | 281 GB | HF `Orion-AI-Lab/S4A`; Dropbox | none | hours |
| EuroCrops | EU crop parcels (vector) | 8.6 GB | Zenodo 8229128 | none | ~1 min per country |
| AgriFieldNet | Crop type India | 0.33 GB | Source Coop `radiantearth/agrifieldnet-competition` | none | ~1 min |
| Fields of The World (FTW) | Field boundaries, 24 countries | 56.8 GB (per-country zips) | Source Coop `kerner-lab/fields-of-the-world`; `ftw data download` | none | ~1 min (Rwanda) |
| Radiant crop sets (Kenya/Tanzania/Uganda/SA/Ghana/S-Sudan/Mali/Benin/Rwanda/DLR fusion) | Crop type | 0.1–160 GB per archive | Azure `.../mlhub/archives/`, Source Coop `radiantearth/*` | none | min–hours |
| Multi-temporal crop classification (Prithvi) | Crop type HLS | 3,854 chips (11.8 GB repo) | HF `ibm-nasa-geospatial/multi-temporal-crop-classification` | none | ~10 min |
| S2-NAIP / Satlas super-resolution | Super-resolution | val set 8,192 pairs; full 65.5 TB | GCS `satlas-satellite-super-resolution`; HF `allenai/s2-naip` | none | ~min (val/test) |
| WorldStrat | Super-resolution (SPOT vs S2) | 104 GB (TACO 37 GB) | Zenodo 15382551 | none | ~30 min (TACO) |
| SEN2NAIP / v2 / SEN2VENµS / OpenSR-test | Super-resolution | 7.2 GB to 609 GB | HF `isp-uv-es/*`, `tacofoundation/*` | none | ~6 min (opensr-test) |
| GEOBench-VLM | VLM benchmark | 9.5 GB | HF `aialliance/GEOBench-VLM` | none | ~8 min |
| EarthVQA (EarthVLSet) | VQA | 18 GB | HF `Kingdrone-Junjue/EarthVLSet` | gated (auto) | ~15 min |
| RSVQA LR / HR | VQA | 0.15 GB / 14.5 GB | Zenodo 6344334 / 6344367 | none | 1 min / 12 min |
| RS5M | Image–text pairs | ~500 GB webdataset; metadata 19 GB | HF `omlab/RS5M`, `Zilun/RS5M` | none | min (one tar) |
| SkyScript | Image–text pairs | ~74 GB (6 zips) | `https://opendatasharing.s3.us-west-2.amazonaws.com/SkyScript/` | none | ~8 min per zip |
| GeoChat_Instruct | Instruction tuning | 318k instructions; repo 102 GB | HF `MBZUAI/GeoChat_Instruct` | none | ~1 min (JSON) |
| ChatEarthNet | S2 image–text | 38.4 GB | Zenodo 11003436 | none | ~12 min (RGB zip) |
| EarthDial | Multimodal VLM data | 2.43 TB | HF `akshaydudhane/EarthDial-Dataset` | none | min (subset) |
| VRSBench | VLM benchmark | 12.7 GB | HF `xiang709/VRSBench` | none | ~10 min |
| OmniEarth-Bench | Multi-sphere VQA | 19.8 GB | HF `initiacms/OmniEarth-Bench` | none | ~15 min |
| SkyScraper (Planet, 2026) | EO time series + news text | large (JPEG stacks) | Source Coop `planet/skyscraper` | none | min (labels.csv) |
| MS Global ML Building Footprints | Building labels | 1.4B buildings | GitHub `microsoft/GlobalMLBuildingFootprints` | none | ~min per region |
| Global Renewables Watch | Solar/wind detections | 395 MB + 58 MB gpkg | GitHub releases v1.0 | none | ~1 min |
| GloSoFarID | Solar farm ID (S2) | 10.2 GB TFRecords | Zenodo 10939100 | none | ~9 min |
| Chesapeake Land Cover | 1 m land cover | LC 1.2 GB; NAIP up to 243 GB | Source Coop `microsoft/chesapeake-land-cover`; Zenodo 5866525 | none | ~5 min (prior extension) |
| Planet Amazon (Kaggle mirror) | Multi-label scenes | 1.6 GB | Kaggle `nikitarom/planets-dataset` | Kaggle account | ~2 min |
| Kaggle EO classics (hurricane damage, LandCover.ai, Massachusetts, DeepGlobe, 38-Cloud, SAT-6, water bodies, PlanesNet, Airbus aircraft/wind turbines, oil tanks) | Assorted | 0.03–17 GB | Kaggle slugs below | Kaggle account | 1–15 min |
| DSTL Satellite Imagery Feature Detection | Multiclass segmentation | unverified | Kaggle competition | Kaggle + rules | unverified |

---

## 2. Detailed entries

### A. Buildings, roads, objects, disaster damage

### SpaceNet bucket (overview, SN1–SN9)
- **What:** Open VHR imagery with co-registered building, road and flood labels. The site states ~67,000 km² of imagery, >11M building footprints and ~20,000 km of road labels. The bucket also has `spacenet-stac/` (SN1–6 STAC), `AOIs/` (Rio, Vegas, Paris, Shanghai, Khartoum, Atlanta, Moscow, Mumbai, San Juan, Dar es Salaam, Rotterdam), `SpaceNet_Off-Nadir_Dataset/SpaceNet-Off-Nadir_Sample.tar.gz` (3.7 GB) and `spacenet-model-weights/spacenet-{3..7}/` (winning models ship with the data).
- **Size:** per challenge below (verified by listing the bucket).
- **Coverage:** spatial: the AOIs above; temporal: 2016–2022 imagery (varies by challenge).
- **Format:** GeoTIFF + GeoJSON tarballs.
- **Access:** `aws s3 ls --no-sign-request s3://spacenet-dataset/`. The AWS registry says no AWS account is needed. Plain HTTPS works too (`https://spacenet-dataset.s3.amazonaws.com/...`). TorchGeo `SpaceNet1`…`SpaceNet8` download via `aws s3 cp --no-sign-request` (needs AWS CLI).
- **Auth:** none.
- **License:** CC BY-SA 4.0 for everything except `Hosted-Datasets/` (bucket LICENSE.md).
- **Sources:** [AWS registry](https://registry.opendata.aws/spacenet/), [bucket LICENSE.md](https://spacenet-dataset.s3.amazonaws.com/LICENSE.md), [spacenet.ai/datasets](https://spacenet.ai/datasets/), [TorchGeo SpaceNet table](https://raw.githubusercontent.com/torchgeo/torchgeo/main/docs/api/datasets/spacenet.csv), [TorchGeo spacenet base.py](https://raw.githubusercontent.com/torchgeo/torchgeo/v0.10.1/torchgeo/datasets/spacenet/base.py)

### SpaceNet 1 (Rio buildings)
- **What:** Building footprints, WorldView-2, 9,735 samples, 0.5–1 m (TorchGeo table).
- **Size:** train 3-band 2.57 GB, 8-band 0.89 GB; test 1.08 + 0.37 GB; GeoJSON 0.02 GB.
- **Coverage:** spatial: Rio de Janeiro; temporal: not stated.
- **Format:** GeoTIFF + GeoJSON.
- **Access:** `s3://spacenet-dataset/spacenet/SN1_buildings/tarballs/`; TorchGeo `SpaceNet1`.
- **Auth:** none.
- **License:** CC BY-SA 4.0.
- **Time to first data:** ~3 min.
- **Hackathon problem:** fast building-footprint baseline before moving to disaster sets.
- **Sources:** as SpaceNet overview.

### SpaceNet 2 (buildings) / SpaceNet 3 (roads)
- **What:** WorldView-3, 4 cities. SN2 has 14,119 samples; SN3 has 3,477 road samples with speed GeoJSON (TorchGeo table).
- **Size:**
  - SN2 train: Vegas 25.6, Paris 5.7, Shanghai 25.1, Khartoum 5.1 GB. Test: 8.5 / 1.9 / 8.3 / 1.7 GB.
  - SN3 train: 26.1 / 5.9 / 25.8 / 5.3 GB, plus `SN3_roads_sample.tar.gz` 0.76 GB.
- **Coverage:** spatial: Vegas, Paris, Shanghai, Khartoum; temporal: not stated.
- **Format:** GeoTIFF + GeoJSON.
- **Access:** `.../SN2_buildings/tarballs/`, `.../SN3_roads/tarballs/`; TorchGeo `SpaceNet2`/`SpaceNet3`.
- **Auth:** none.
- **License:** CC BY-SA 4.0.
- **Time to first data:** ~1 min (SN3 sample); ~5 min (Paris/Khartoum).
- **Hackathon problem:** post-disaster road-network routing (combine with SN8).
- **Sources:** bucket listing; TorchGeo SpaceNet table.

### SpaceNet 4 (off-nadir, Atlanta)
- **What:** One area imaged at 27 nadir angles (WorldView-2), 1,991 samples.
- **Size:** 27 train tarballs of ~7.0–7.8 GB each (~200 GB total), test 6.2 GB, summaryData 0.14 GB.
- **Coverage:** spatial: Atlanta; temporal: one area, many look angles.
- **Format:** GeoTIFF + GeoJSON.
- **Access:** `.../SN4_buildings/tarballs/train/Atlanta_nadir{N}_catid_*.tar.gz`.
- **Auth:** none.
- **License:** CC BY-SA 4.0.
- **Time to first data:** ~6 min per nadir angle.
- **Hackathon problem:** look-angle robustness, i.e. "how does off-nadir tasking degrade detection" (a satellite-tasking optimiser).
- **Sources:** bucket listing; TorchGeo table.

### SpaceNet 5 (roads + travel time)
- **What:** Road networks with speed labels.
- **Size:** train Moscow 37.6 GB, Mumbai 19.9 GB; test Moscow 6.2, Mumbai 3.4, San Juan 5.3 GB.
- **Coverage:** spatial: Moscow, Mumbai, San Juan; temporal: not stated.
- **Format:** GeoTIFF + GeoJSON.
- **Access:** `.../SN5_roads/tarballs/`.
- **Auth:** none.
- **License:** CC BY-SA 4.0.
- **Time to first data:** ~3–5 min (test sets).
- **Hackathon problem:** routing and ETA graphs extracted from imagery.
- **Sources:** bucket listing.

### SpaceNet 6 (multi-sensor all-weather, Rotterdam)
- **What:** SAR + optical (TorchGeo lists SAR, RGB, MSI), 5,462 samples.
- **Size:** train 41.9 GB, test 18.1 GB, train sample 0.13 GB.
- **Coverage:** spatial: Rotterdam; temporal: not stated.
- **Format:** GeoTIFF + GeoJSON.
- **Access:** `.../SN6_buildings/tarballs/`.
- **Auth:** none.
- **License:** CC BY-SA 4.0.
- **Time to first data:** <1 min (sample).
- **Hackathon problem:** night/cloud building mapping from SAR.
- **Sources:** bucket listing; TorchGeo table.

### SpaceNet 7 (multi-temporal urban development)
- **What:** Monthly Planet Dove mosaics at 4 m, 1,889 samples (TorchGeo).
- **Size:** train 9.16 GB, test 1.25 GB, csvs 0.50 GB, sample 0.14 GB.
- **Coverage:** spatial: global sites (L15 tiles); temporal: multi-month time series.
- **Format:** GeoTIFF + GeoJSON + CSV.
- **Access:** `.../SN7_buildings/tarballs/`. Also GEO-Bench-2 `aialliance/spacenet7` (6.3 GB) and `isp-uv-es/spacenet7-taco` (4.45 GB).
- **Auth:** none.
- **License:** CC BY-SA 4.0 (GEO-Bench-2 card also credits Planet imagery under CC BY-SA 4.0).
- **Time to first data:** ~1 min (sample).
- **Hackathon problem:** urbanisation tracker / construction alerts.
- **Sources:** bucket listing; [aialliance/spacenet7 card](https://huggingface.co/datasets/aialliance/spacenet7)

### SpaceNet 8 (flood-attributed roads and buildings)
- **What:** Pre- and post-event Maxar imagery; multiclass flooded/non-flooded buildings and roads. TorchGeo: 1,289 samples, 8 classes, 0.3–0.8 m.
- **Size:** Germany_Training_Public 1.36 GB, Louisiana-East_Training_Public 3.34 GB, Louisiana-West_Test_Public 2.62 GB (7.3 GB total).
- **Coverage:** spatial: New Orleans after Hurricane Ida (Aug 2021); Dernau, Germany, during the June 2021 floods; temporal: 2021 events.
- **Format:** GeoTIFF + GeoJSON annotations.
- **Access:** `aws s3 cp s3://spacenet-dataset/spacenet/SN8_floods/tarballs/Germany_Training_Public.tar.gz .`; TorchGeo `SpaceNet8`; HF `isp-uv-es/spacenet8-taco` (7.45 GB).
- **Auth:** none.
- **License:** CC BY-SA 4.0.
- **Time to first data:** ~1–3 min.
- **Hackathon problem:** "Which roads are still drivable after a hurricane?" — flood-aware evacuation routing from satellite imagery.
- **Sources:** [SN8 challenge page](https://spacenet.ai/sn8-challenge/), bucket listing.

### SpaceNet 9 (cross-modal optical↔SAR registration, 2025)
- **What:** Align Maxar Open Data optical imagery to Umbra SAR in earthquake-affected areas. The output is a 2-channel per-pixel x/y shift; scoring uses manually labelled tie-points. Page published 15 May 2025; challenge on Topcoder.
- **Size:** `train.zip` 0.40 GB, `testpublic.zip` 0.155 GB.
- **Coverage:** spatial: earthquake regions (not named); temporal: not stated.
- **Format:** zip (contents not inspected).
- **Access:** `https://spacenet-dataset.s3.us-east-1.amazonaws.com/spacenet/SN9_cross-modal/train.zip`.
- **Auth:** none.
- **License:** CC BY-SA 4.0.
- **Time to first data:** ~1 min.
- **Hackathon problem:** fuse SAR (sees through clouds and night) with optical for rapid damage mapping.
- **Sources:** [SN9 page](https://spacenet.ai/sn9-challenge/), bucket listing.

### fMoW (Functional Map of the World; rgb and full)
- **What:** IARPA land-use classification of points of interest from DigitalGlobe/Maxar imagery, 62 categories (count per the fMoW-Sentinel page).
- **Size:** fMoW-rgb ~200 GB (JPEG); fMoW-full ~3.5 TB (TIFF, 4/8-band). `groundtruth.tar.bz2` 0.245 GB; `manifest.json.bz2` 5 MB.
- **Coverage:** spatial: global; temporal: multi-temporal sequences.
- **Format:** JPEG/TIFF + JSON metadata.
- **Access:** `aws s3 ls s3://spacenet-dataset/Hosted-Datasets/fmow/fmow-rgb/` (torrents are no longer maintained). HF mirror `EVER-Z/fMoW_rgb` (337 GB repo, no license on card).
- **Auth:** none.
- **License:** "Functional Map of the World Challenge Public License" (DigitalGlobe). It explicitly says algorithms trained on the data are not "Adapted Material".
- **Time to first data:** minutes for the manifest and ground truth; hours for imagery. Use the manifest to pull single categories.
- **Hackathon problem:** facility-type recognition, e.g. finding airports, ports, solar farms and nuclear plants.
- **Sources:** [fMoW GitHub](https://github.com/fMoW/dataset), [S3 README](https://spacenet-dataset.s3.amazonaws.com/Hosted-Datasets/fmow/fmow-rgb/README.md), [S3 LICENSE](https://spacenet-dataset.s3.amazonaws.com/Hosted-Datasets/fmow/fmow-rgb/LICENSE)

### fMoW-Sentinel (SatMAE)
- **What:** Sentinel-2 time series for fMoW locations; 13 bands, 90-day cloud composites, 62 categories.
- **Size:** 712,874 train / 84,939 val / 84,966 test images; total GB not stated.
- **Coverage:** spatial: global; temporal: multi-date.
- **Format:** not stated on the landing page.
- **Access:** Stanford Digital Repository (DOI 10.25740/vg497cb6002). SatMAE ships fMoW model weights on Zenodo (record 7369797/7338613 links in the README).
- **Auth:** none stated.
- **License:** fMoW license for metadata; Sentinel-2 licence for imagery.
- **Time to first data:** unknown (probably hours).
- **Hackathon problem:** temporal land-use change classification at 10 m with free imagery.
- **Sources:** [purl.stanford.edu/vg497cb6002](https://purl.stanford.edu/vg497cb6002), [SatMAE GitHub](https://github.com/sustainlab-group/SatMAE)

### xView1
- **What:** 1M object instances, 60 classes, 1,415 km², 0.3 m (site). The TACO repack has 846 WorldView-3 chips and 601,774 objects; it notes two unlisted class codes (75, 82).
- **Size:** TACO 20.3 GB (original size not stated).
- **Coverage:** spatial: global sample of 1,415 km²; temporal: not stated.
- **Format:** original GeoTIFF + GeoJSON; TACO = COG + parquet.
- **Access:** register at challenge.xviewdataset.org/signup (the original), or `isp-uv-es/xview-taco`.
- **Auth:** registration for the original; none for HF.
- **License:** CC BY-NC-SA 4.0 (per the TACO card; the original T&C page is a DIUx legal agreement).
- **Time to first data:** ~20 min via HF.
- **Hackathon problem:** counting aircraft, vehicles and ships at bases and ports.
- **Sources:** [xviewdataset.org](https://xviewdataset.org/), [xview-taco](https://huggingface.co/datasets/isp-uv-es/xview-taco)

### xBD / xView2 (building damage)
- **What:** 11,034 pre/post WorldView pairs (1024²) over 19 events and six hazards (fire, flood, wind, earthquake, tsunami, volcano). Every building is outlined and graded on a 4-level damage scale. TorchGeo uses only the challenge train (~7.8 GB) and test (~2.6 GB) sets (3,732 samples).
- **Size:** challenge ~10.4 GB. HF: `isp-uv-es/xview2-taco` 35.2 GB; `kshitijrajsharma/xview2-xbd` 24.3 GB (community, CC BY-NC-SA).
- **Coverage:** spatial: global disaster sites; temporal: pre/post event.
- **Format:** PNG + JSON (WGS84 rings).
- **Access:** xview2.org (JavaScript site, login). TorchGeo `xBD` requires manual download. TACO via `hf_hub_download("isp-uv-es/xview2-taco","xview2.zip",repo_type="dataset")`.
- **Auth:** xView2 login (original); none on HF.
- **License:** CC BY-NC-SA 4.0.
- **Time to first data:** ~10–30 min.
- **Hackathon problem:** automatic damage triage (pair with live Maxar Open Data events — see cross-slice).
- **Sources:** [xview2-taco card](https://huggingface.co/datasets/isp-uv-es/xview2-taco), [TorchGeo xbd.py](https://raw.githubusercontent.com/torchgeo/torchgeo/v0.10.1/torchgeo/datasets/xbd.py), [TorchGeo table](https://raw.githubusercontent.com/torchgeo/torchgeo/main/docs/api/datasets/benchmark.csv)

### xView3-SAR (dark vessels)
- **What:** 991 analysis-ready Sentinel-1 IW GRD scenes, each about 29,400×24,400 px (1,400 gigapixels). 243,018 verified maritime objects over 43.2M km², labelled by AIS-to-SAR matching plus analyst review. VH/VV plus co-located bathymetry and wind rasters. Tasks: detect, classify vessel vs fishing, estimate length.
- **Size:** ≈1,400 gigapixels; GB/TB unverified.
- **Coverage:** spatial: global coastal waters; temporal: Sentinel-1 era.
- **Format:** GeoTIFF per scene + CSV labels (per the reference code).
- **Access:** https://iuu.xview.us/ (JavaScript site; I couldn't read it); code at https://github.com/DIUx-xView.
- **Auth:** registration (unverified).
- **License:** unverified.
- **Time to first data:** hours (scenes are huge; the reference notebook says "a few scenes" are enough to start).
- **Hackathon problem:** illegal-fishing "dark vessel" alerts by cross-matching SAR detections against AIS.
- **Sources:** [arXiv 2206.00897](https://arxiv.org/abs/2206.00897), [xview3-reference](https://github.com/DIUx-xView/xview3-reference)

### DOTA v1.0 / v1.5 / v2.0
- **What:** Oriented-box aerial object detection with 15 / 16 / 18 categories. Sources: Google Earth, GF-2, JL-1 and CycloMedia; PNG.
- **Size:** HF mirror `isaaccorley/dota` 23.9 GB (TorchGeo table: 5,229 samples, 800–4000 px).
- **Coverage:** spatial: global; temporal: not stated.
- **Format:** PNG + text annotations.
- **Access:** Google Drive/Baidu/OneDrive (official page) or TorchGeo `DOTA` (auto-downloads from the HF mirror).
- **Auth:** none.
- **License:** **academic use only; commercial use prohibited**; Google Earth terms also apply.
- **Time to first data:** ~20 min.
- **Hackathon problem:** port/airfield activity monitoring.
- **Sources:** [DOTA page](https://captain-whu.github.io/DOTA/dataset.html), [isaaccorley/dota](https://huggingface.co/datasets/isaaccorley/dota)

### DIOR
- **What:** 23,463 images, 20 classes, 800×800, 0.5 m.
- **Size:** 7.4 GB (HF `torchgeo/dior`).
- **Coverage:** spatial: global; temporal: not stated.
- **Format:** images + annotations (zip).
- **Access:** TorchGeo `DIOR` (auto-download from HF).
- **Auth:** none.
- **License:** CC BY-NC 4.0.
- **Time to first data:** ~6 min.
- **Hackathon problem:** multi-class infrastructure inventory.
- **Sources:** [TorchGeo table](https://raw.githubusercontent.com/torchgeo/torchgeo/main/docs/api/datasets/benchmark.csv), [torchgeo/dior](https://huggingface.co/datasets/torchgeo/dior)

### iSAID
- **What:** Instance segmentation on DOTA-v1.0 images, 15 categories.
- **Size:** annotations (HF `isaaccorley/isaid` 0.21 GB) + DOTA images.
- **Coverage:** same as DOTA.
- **Format:** PNG masks + JSON.
- **Access:** Google Drive/Baidu (extraction codes on the page).
- **Auth:** none.
- **License:** **academic only**.
- **Time to first data:** ~30 min (needs DOTA images).
- **Hackathon problem:** pixel-accurate vehicle/ship segmentation.
- **Sources:** [iSAID page](https://captain-whu.github.io/iSAID/dataset.html), [iSAID devkit](https://github.com/CAPTAIN-WHU/iSAID_Devkit)

### FAIR1M
- **What:** 15,000 Gaofen/Google Earth images, 37 fine-grained classes, 1024², 0.3–0.8 m.
- **Size:** HF `blanchon/FAIR1M` 9.2 GB (licence "unknown" on card).
- **Coverage:** spatial: China/global (not stated); temporal: not stated.
- **Format:** images + XML.
- **Access:** TorchGeo `FAIR1M` (Google Drive URLs in source) or the HF copy.
- **Auth:** none.
- **License:** CC BY-NC-SA 3.0 (TorchGeo table).
- **Time to first data:** ~8 min.
- **Hackathon problem:** aircraft-type identification.
- **Sources:** [TorchGeo table](https://raw.githubusercontent.com/torchgeo/torchgeo/main/docs/api/datasets/benchmark.csv), [blanchon/FAIR1M](https://huggingface.co/datasets/blanchon/FAIR1M)

### RarePlanes
- **What:** Real WorldView-3 aircraft annotations plus a synthetic (AI.Reverie) set.
- **Size:** real train: PS-RGB 31.4 GB, PS-RGB tiled 2.0 GB, COG 2.4 GB, PAN 23.5 GB, MS 12.7 GB; real test: PS-RGB 18.5 GB, tiled 0.93 GB; GeoJSON <5 MB. Synthetic ≈70 GB (train 46.8 GB + test 22.7 GB). Also `weights/`.
- **Coverage:** spatial: airfields (not listed); temporal: not stated.
- **Format:** GeoTIFF + GeoJSON.
- **Access:** `s3://rareplanes-public/real/tarballs/train/RarePlanes_train_PS-RGB_tiled.tar.gz` (anonymous).
- **Auth:** none.
- **License:** Creative Commons (exact variant not confirmed in the text I read); attribution to In-Q-Tel CosmiQ Works & AI.Reverie required.
- **Time to first data:** ~2 min (tiled).
- **Hackathon problem:** sim-to-real aircraft detection; airport traffic estimation.
- **Sources:** [LICENSE.txt](https://rareplanes-public.s3.amazonaws.com/LICENSE.txt), bucket listing.

### BRIGHT (IEEE GRSS DFC 2025)
- **What:** Multimodal (optical Maxar/NAIP + SAR Capella/Umbra) building damage, 3,239 samples, 4 classes, 0.1–1 m.
- **Size:** HF `isaaccorley/bright` 10.2 GB; `isp-uv-es/bright-dfc2025-taco` 10.6 GB.
- **Coverage:** spatial: disaster sites; temporal: pre/post event.
- **Format:** GeoTIFF.
- **Access:** TorchGeo `BRIGHT` (auto).
- **Auth:** none.
- **License:** CC BY 4.0 AND CC BY-NC 4.0 (mixed).
- **Time to first data:** ~9 min.
- **Hackathon problem:** all-weather damage assessment from SAR when optical is cloudy.
- **Sources:** [TorchGeo table](https://raw.githubusercontent.com/torchgeo/torchgeo/main/docs/api/datasets/benchmark.csv)

### Open Cities AI Challenge
- **What:** Drone imagery and building footprints for 10 African cities/regions (GFDRR / DrivenData).
- **Size:** train tier 1: source 32.4 GB + labels 0.016 GB; tier 2: 41.1 GB + 0.045 GB; test 9.0 GB.
- **Coverage:** spatial: 10 African cities/regions; temporal: not stated.
- **Format:** GeoTIFF + GeoJSON.
- **Access:** `https://radiantearth.blob.core.windows.net/mlhub/archives/open_cities_ai_challenge_train_tier_1_source.tar.gz` (anonymous Azure).
- **Auth:** none.
- **License:** unverified (README excerpt cut before the licence line).
- **Time to first data:** ~25 min (tier 1).
- **Hackathon problem:** building maps for disaster-risk management in data-poor cities.
- **Sources:** [README](https://radiantearth.blob.core.windows.net/mlhub/open-cities-ai-challenge/README.md), Azure listing.

### RAMP (Replicable AI for Microplanning)
- **What:** Building footprints for 22 cities (WHO/DevGlobal), e.g. Accra, Dhaka, Les Cayes, Muscat, N'Djamena, Shanghai, Paris.
- **Size:** per city source 0.09–2.55 GB, labels 1–23 MB.
- **Coverage:** spatial: 22 cities; temporal: not stated.
- **Format:** GeoTIFF + GeoJSON.
- **Access:** Source Coop `ramp/ramp` (DOI 10.34911/rdnt.b0noju); Azure `.../mlhub/archives/ramp_<city>_{source,labels}.tar.gz`.
- **Auth:** none.
- **License:** unverified.
- **Time to first data:** ~1 min.
- **Hackathon problem:** vaccination/health microplanning population maps.
- **Sources:** [Source Coop API](https://source.coop/api/v1/products/ramp), Azure listing.

---

### B. Ships, maritime, marine debris

### HRSID
- **What:** High-resolution SAR ship detection/segmentation. Includes inshore/offshore annotations, 400 pure-background images and an ALOS-2 test image.
- **Size:** HF YOLO copy 0.61 GB (official size not stated).
- **Coverage:** spatial: not stated; temporal: not stated.
- **Format:** JPG (PNG high-fidelity version also offered) + COCO.
- **Access:** Google Drive / Baidu (code bs64); unofficial HF `dronefreak/HRSID`.
- **Auth:** none.
- **License:** not stated ("unknown" on HF).
- **Time to first data:** ~1 min.
- **Hackathon problem:** SAR vessel detection near ports.
- **Sources:** [HRSID GitHub](https://github.com/chaozhong2010/HRSID), [HF copy](https://huggingface.co/datasets/dronefreak/HRSID)

### SSDD (Official-SSDD)
- **What:** SAR ship detection dataset (official repo updated with 2025 citations).
- **Size:** HF copy 0.05 GB.
- **Coverage:** not stated.
- **Format:** images + boxes.
- **Access:** Google Drive / Baidu (password 2021); HF `dronefreak/SSDD` (Apache-2.0 card, unofficial).
- **Auth:** none.
- **License:** not stated officially.
- **Time to first data:** <1 min.
- **Hackathon problem:** lightweight SAR ship detector for an on-board/edge demo.
- **Sources:** [Official-SSDD](https://github.com/TianwenZhang0825/Official-SSDD), [HF copy](https://huggingface.co/datasets/dronefreak/SSDD)

### OpenSARShip 1.0 / 2.0
- **What:** Sentinel-1 ship chips; the page lists zips OpenSARShip_1, OpenSARShip_2, original and uint8.
- **Size:** not stated.
- **Coverage:** not stated.
- **Format:** zip.
- **Access:** opensar.sjtu.edu.cn.
- **Auth:** not stated.
- **License:** none stated (cite the papers).
- **Time to first data:** unknown.
- **Hackathon problem:** ship-type classification from S1.
- **Sources:** [OpenSAR](https://opensar.sjtu.edu.cn/)

### OSSDD — Open Sentinel-1 Ship Detection Dataset (new, 2026)
- **What:** Sentinel-1 GRD chips with ship boxes (arXiv 2608.01963). Ships a PyTorch `ShipDataset` class.
- **Size:** 72.3 GB (zip + WebDataset); TACO version 12.0 GB.
- **Coverage:** not stated.
- **Format:** zip / WebDataset tar.
- **Access:** HF `sylviaHoch/OpenSARShip-Ship-Detection-Dataset` (the repo name is misleading — it's OSSDD), `isp-uv-es/ossdd-taco`.
- **Auth:** none.
- **License:** CC BY-NC-SA 4.0.
- **Time to first data:** ~10 min (TACO).
- **Hackathon problem:** free-data maritime domain awareness.
- **Sources:** [HF card](https://huggingface.co/datasets/sylviaHoch/OpenSARShip-Ship-Detection-Dataset)

### ShipsNet (Ships in Satellite Imagery)
- **What:** 4,000 80×80 Planet chips, ship / no-ship, San Francisco Bay and San Pedro Bay.
- **Size:** 0.45 GB.
- **Coverage:** spatial: San Francisco Bay, San Pedro Bay; temporal: not stated.
- **Format:** PNG + JSON.
- **Access:** `kaggle datasets download rhammell/ships-in-satellite-imagery`.
- **Auth:** Kaggle account.
- **License:** CC BY-SA 4.0.
- **Time to first data:** ~2 min.
- **Hackathon problem:** port congestion index.
- **Sources:** [Kaggle API view](https://www.kaggle.com/api/v1/datasets/view/rhammell/ships-in-satellite-imagery)

### Airbus Ship Detection (Kaggle competition)
- **What:** Optical ship instance segmentation; 192,556 ship instances (per the xView3 paper's related-work section).
- **Size:** unverified (competition page needs login).
- **Coverage:** unverified.
- **Format:** images + run-length-encoded masks (unverified).
- **Access:** Kaggle competition `airbus-ship-detection`.
- **Auth:** Kaggle account + accept rules (unverified).
- **License:** competition rules (unverified).
- **Time to first data:** unverified.
- **Hackathon problem:** ship counting from optical imagery.
- **Sources:** [arXiv 2206.00897](https://arxiv.org/abs/2206.00897); Kaggle page did not render.

### Satlas marine infrastructure
- **What:** AllenAI Satlas offshore infrastructure labels (platforms/turbines).
- **Size:** 18.6 GB zip.
- **Coverage:** not inspected.
- **Format:** zip.
- **Access:** `https://ai2-public-datasets.s3.amazonaws.com/satlas/satlas-dataset-marine-infrastructure-v1.zip`.
- **Auth:** none.
- **License:** unverified (SatlasPretrain overall is ESA/CC0/ODbL/CC BY mix).
- **Time to first data:** ~15 min.
- **Hackathon problem:** offshore wind / oil-platform change tracker.
- **Sources:** bucket listing.

### Embed2Scale S1-single-ship-downstream
- **What:** Sentinel-1 single-ship downstream task for SSL4EO.
- **Size:** 14.3 GB.
- **Coverage:** not inspected.
- **Format:** not inspected.
- **Access:** HF `embed2scale/S1-single-ship-downstream`.
- **Auth:** none.
- **License:** CC BY 4.0.
- **Time to first data:** ~12 min.
- **Hackathon problem:** evaluate foundation-model embeddings on ship detection.
- **Sources:** HF API.

### MARIDA (Marine Debris Archive)
- **What:** Sentinel-2 weakly supervised pixel segmentation of marine debris, Sargassum, ships, waves, turbid water and other sea features (NTUA).
- **Size:** 1.16 GB (Zenodo); TACO 2.3 GB.
- **Coverage:** spatial: global sites (not listed); temporal: not stated.
- **Format:** GeoTIFF patches + shapefiles + splits.
- **Access:** Zenodo 5151941; Azure `.../mlhub/archives/marida_v1_*`; HF `isp-uv-es/marida-taco`, `dronefreak/MARIDA` (detection variant).
- **Auth:** none.
- **License:** CC BY 4.0.
- **Time to first data:** ~1 min.
- **Hackathon problem:** plastic-patch alerting for cleanup boats.
- **Sources:** [Zenodo](https://zenodo.org/records/5151941), [README](https://radiantearth.blob.core.windows.net/mlhub/marida/README.md)

### MADOS (Marine Debris and Oil Spill)
- **What:** Sentinel-2 marine pollution segmentation (debris + oil); MariNeXt baseline.
- **Size:** 4.04 GB; TACO 2.5 GB.
- **Coverage:** spatial: global; temporal: not stated.
- **Format:** GeoTIFF (also a `dataset.h5` on Google Drive).
- **Access:** Zenodo 10664073.
- **Auth:** none.
- **License:** CC BY 4.0.
- **Time to first data:** ~4 min.
- **Hackathon problem:** oil-spill detector with ship-track attribution.
- **Sources:** [Zenodo](https://zenodo.org/records/10664073), [GitHub](https://github.com/gkakogeorgiou/mados)

### NASA Marine Debris (PlanetScope)
- **What:** 707 images, 256×256, 3 m, boxes for floating debris (plastics, algae, Sargassum, wood).
- **Size:** source 0.075 GB.
- **Coverage:** not stated.
- **Format:** GeoTIFF + boxes.
- **Access:** Source Coop `nasa/marine-debris` (DOI 10.34911/rdnt.9r6ekg); TorchGeo `NASAMarineDebris` (auto); TACO copy.
- **Auth:** none.
- **License:** Apache-2.0 per TorchGeo table; the TACO card says CC BY-NC 4.0 (conflict).
- **Time to first data:** <1 min.
- **Hackathon problem:** debris detection on daily PlanetScope.
- **Sources:** [Source Coop API](https://source.coop/api/v1/products/nasa), [TorchGeo table](https://raw.githubusercontent.com/torchgeo/torchgeo/main/docs/api/datasets/benchmark.csv)

---

### C. Land cover, scene classification, pretraining corpora

### BigEarthNet v2.0 (reBEN)
- **What:** 549,488 Sentinel-1/Sentinel-2 patch pairs. 115 S2 tiles and 312 S1 scenes, June 2017–May 2018, 10 European countries. CLC2018 19-class multi-labels plus pixel reference maps. Patches with snow/cloud are kept and listed in metadata.
- **Size:** S2 ~59 GiB, S1 ~51 GiB, plus reference maps.
- **Coverage:** spatial: 10 European countries; temporal: Jun 2017–May 2018.
- **Format:** `.tar.zst`, parquet metadata.
- **Access:** `https://zenodo.org/records/10891137/files/BigEarthNet-S2.tar.zst`. Also TorchGeo `BigEarthNetV2`, HF `torchgeo/bigearthnet` (123.6 GB), GEO-Bench-2 `aialliance/benv2` (24.9 GB), `isp-uv-es/bigearthnet-v2-txt-taco` (95.6 GB, with text). Pretrained models at HF `BIFOLD-BigEarthNetv2-0`.
- **Auth:** none.
- **License:** CDLA-Permissive-1.0.
- **Time to first data:** ~20 min (GEO-Bench-2 subset) to 1.5 h.
- **Hackathon problem:** land-cover change alerting across Europe.
- **Sources:** [bigearth.net](https://bigearth.net/); v1: [Zenodo 12687186](https://zenodo.org/records/12687186) (129 GB, 590,326 patches)

### EuroSAT (MS/RGB) and EuroSAT-SAR
- **What:** 27,000 64×64 Sentinel-2 patches, 10 classes. EuroSAT-SAR is a Sentinel-1 version.
- **Size:** EuroSAT_MS.zip 2.07 GB, EuroSAT_RGB.zip 0.09 GB; SAR 3.8 GB.
- **Coverage:** spatial: Europe; temporal: not stated.
- **Format:** GeoTIFF / JPG.
- **Access:** Zenodo 7711810; TorchGeo `EuroSAT`/`EuroSAT100`/`EuroSATSpatial` (auto from HF `torchgeo/eurosat`); `wangyi111/EuroSAT-SAR`; Kaggle `apollo2506/eurosat-dataset` (3.05 GB, CC0).
- **Auth:** none.
- **License:** MIT (Zenodo).
- **Time to first data:** ~1–2 min.
- **Hackathon problem:** 5-minute "hello world" land-use classifier and demo.
- **Sources:** [Zenodo](https://zenodo.org/records/7711810), [HF EuroSAT-SAR](https://huggingface.co/datasets/wangyi111/EuroSAT-SAR)

### SEN12MS
- **What:** 180,662 S1/S2/MODIS-land-cover triplets, 256×256, 4 seasons.
- **Size:** not verified (the mediaTUM page is behind bot protection).
- **Coverage:** spatial: global ROIs; temporal: 4 seasons (2017, unverified).
- **Format:** GeoTIFF tar.gz per season/source.
- **Access:** `wget "ftp://m1474000:m1474000@dataserv.ub.tum.de/ROIs1158_spring_s2.tar.gz"` (TorchGeo docstring; "will likely take several hours"); splits on GitHub `schmitt-muc/SEN12MS`.
- **Auth:** public FTP credentials.
- **License:** CC BY 4.0.
- **Time to first data:** hours (one season/source: tens of minutes, unverified).
- **Hackathon problem:** SAR-to-optical translation for cloudy regions.
- **Sources:** [TorchGeo sen12ms.py](https://raw.githubusercontent.com/torchgeo/torchgeo/v0.10.1/torchgeo/datasets/sen12ms.py), [GitHub](https://github.com/schmitt-muc/SEN12MS)

### SEN12MS-CR / SEN12MS-CR-TS
- **What:** Cloudy/cloud-free S2 paired with S1 for cloud removal (mono-temporal and time series).
- **Size:** HF copy `Hermanni/sen12mscr` 389 GB.
- **Coverage:** spatial: global ROIs (sharded by region); temporal: multi-date (TS version).
- **Format:** tar.gz per sensor/region.
- **Access:** mediaTUM 1554803 (CR), 1639953 (TS train), 1659251 (TS test); FTP `wget "ftp://m1639953:m1639953@dataserv.ub.tum.de/s1_africa.tar.gz"`; `dl_data.sh` script.
- **Auth:** public FTP credentials.
- **License:** HF copy CC BY 4.0.
- **Time to first data:** ~10–30 min (one region shard).
- **Hackathon problem:** "see through clouds" by generating cloud-free S2 from S1.
- **Sources:** [SEN12MS-CR-TS GitHub](https://github.com/PatrickTUM/SEN12MS-CR-TS)

### SSL4EO-S12 (v1)
- **What:** About 1M global S1/S2 (L1C/L2A) locations × 4 seasons for self-supervised learning.
- **Size:** raw 1.5 TB (500 GB per modality); compressed 8-bit 20–50 GB per modality; 100-patch sample 600 MB.
- **Coverage:** spatial: global; temporal: 4 seasons.
- **Format:** GeoTIFF / tar.
- **Access:** mediaTUM 1660427 (raw) / 1702379 (8-bit); HF `wangyi111/SSL4EO-S12` (1.63 TB); TorchGeo `SSL4EOS12` (1.5 TB compressed / 3.7 TB uncompressed).
- **Auth:** none.
- **License:** CC BY 4.0.
- **Time to first data:** ~1 min (sample) to ~40 min (one 8-bit modality).
- **Hackathon problem:** pretrain or finetune a tiny EO foundation model on the hackathon task.
- **Sources:** [GitHub](https://github.com/zhu-xlab/SSL4EO-S12)

### SSL4EO-S12 v1.1 (+ downstream, captions)
- **What:** 246,144 locations × 4 timestamps: S2L1C, S2L2A, S2RGB, S1GRD, LULC, DEM, NDVI. Zarr-zip samples in WebDataset tar shards.
- **Size:** HF repo 4.8 TB (Zarr version 2.6 TB); downstream 156 GB; Llama3 captions 0.6 GB (`ibm-esa-geospatial/Llama3-SSL4EO-S12-v1.1-captions`, Llama 3 licence).
- **Coverage:** spatial: global; temporal: 4 seasons.
- **Format:** Zarr zip inside tar shards.
- **Access:** HF `embed2scale/SSL4EO-S12-v1.1`; loaders at GitHub `DLR-MF-DAS/SSL4EO-S12-v1.1`.
- **Auth:** none.
- **License:** CC BY 4.0.
- **Time to first data:** minutes (single shard).
- **Hackathon problem:** multimodal retrieval ("find places like this").
- **Sources:** [HF card](https://huggingface.co/datasets/embed2scale/SSL4EO-S12-v1.1)

### SSL4EO-L (+ benchmark)
- **What:** About 1M Landsat 264×264 patches for SSL; benchmark with CDL (134 classes) and NLCD (17 classes).
- **Size:** 1.74 TB; benchmark 47.8 GB.
- **Coverage:** spatial: global (pretraining) / USA (benchmark); temporal: not stated.
- **Format:** tar.gz parts.
- **Access:** HF `torchgeo/ssl4eo_l`, `torchgeo/ssl4eo_l_benchmark`; TorchGeo `SSL4EOL`, `SSL4EOLBenchmark` (auto).
- **Auth:** none.
- **License:** CC0.
- **Time to first data:** ~40 min (benchmark).
- **Hackathon problem:** 50-year Landsat change analysis with pretrained weights.
- **Sources:** [TorchGeo pretraining table](https://raw.githubusercontent.com/torchgeo/torchgeo/main/docs/api/datasets/pretraining.csv)

### SatlasPretrain (AllenAI)
- **What:** 302M labels, 137 categories over NAIP, Sentinel-1/2 and Landsat (TorchGeo; ">30 TB" of images).
- **Size (S3 listing):**
  - `satlas-dataset-v1-sentinel2-small.tar` 500.8 GB; `naip-small` 566 GB
  - `labels-static` 119 GB; `labels-dynamic` 0.14 GB; `metadata` 7.7 GB
  - `sentinel2-a/b` ~4.1 TB each; Landsat 2.6 TB; S1 1.2 TB
  - NAIP 2011–2020: 0.19–4.2 TB per year
  - Model weights `satlas-model-v1-*.pth` 0.43–0.5 GB
- **Coverage:** spatial: global (NAIP: USA); temporal: multi-year.
- **Format:** tar.
- **Access:** `s3://ai2-public-datasets/satlas/` (anonymous); TorchGeo `SatlasPretrain` (aws CLI); URL list on GitHub `allenai/satlas`.
- **Auth:** none.
- **License:** ESA AND CC0 AND ODbL AND CC BY 4.0.
- **Time to first data:** minutes (dynamic labels/metadata); hours for imagery.
- **Hackathon problem:** use the labels (wind turbines, solar farms, platforms) as a global ground truth.
- **Sources:** [URL list](https://raw.githubusercontent.com/allenai/satlas/main/satlaspretrain_urls.txt), bucket listing.

### Major TOM (ESA Φ-lab / Asterisk Labs)
- **What:** Global, gridded, parquet-packaged EO archives. HF repo sizes:
  - Core imagery: Core-S2L2A 23.0 TB, Core-S2L1C 23.6 TB, Core-S1RTC 15.7 TB, Core-DEM 973 GB.
  - New 2025–26 repos: Core-AlphaEarth-Embeddings 6.1 TB (CC BY 4.0, Aug 2025); Core-VIIRS-Nighttime-Light 333 GB (2,108,341 patches, annual VNL 2016–2024, CC BY 4.0, May 2026); COP-GEN-Benchmark 353 GB (495 locations, Apr 2026); Core-S1RTC/S2L2A-UniverSat 4.2 / 15.6 GB (Jul–Sep 2026).
  - Subsets: Core-S2L2A-249k 352 GB, plus embedding variants for 249k (SigLIP, DINOv2, FarSLIP, SatCLIP, Clay v1.5, OlmoEarth-Base, all 0.3–2.2 GB).
  - Embeddings over the core sets: S2RGB-SigLIP 95 GB, S2RGB-DINOv2 245 GB, SSL4EO 275–360 GB, DeCUR 304–371 GB.
  - Other: Core-S2L2A-MMEarth 486 GB; Spatial-Reference-Grid 32 GB.
- **Coverage:** spatial: global; temporal: 2015–2024 (varies by repo).
- **Format:** parquet with embedded imagery bytes.
- **Access:** HF `Major-TOM/<repo>`; read single parquet files with `hf_hub_download`; TorchGeo `MajorTOMEmbeddings`.
- **Auth:** none.
- **License:** CC BY-SA 4.0 (core); CC BY 4.0 (AlphaEarth, VIIRS, COP-GEN).
- **Time to first data:** minutes (one shard or the 249k embedding sets).
- **Hackathon problem:** night-lights × S2 for disaster/power-outage detection; generative EO benchmark (COP-GEN).
- **Sources:** HF API listing; [VIIRS card](https://huggingface.co/datasets/Major-TOM/Core-VIIRS-Nighttime-Light), [COP-GEN card](https://huggingface.co/datasets/Major-TOM/COP-GEN-Benchmark)

### TerraMesh (IBM / ESA Φ-lab, 2025–2026)
- **What:** More than 9M co-registered 10 m patches: S1 GRD/RTC, S2 L1C/L2A/RGB, Copernicus DEM, NDVI, LULC. Built from Major TOM and SSL4EO-S12.
- **Size:** 18.4 TB; masks 1.16 TB (ODbL); masks-eval 5.9 GB.
- **Coverage:** spatial: global; temporal: multi-year.
- **Format:** Zarr-zip in WebDataset tars, up to 889 shards per modality.
- **Access:** HF `ibm-esa-geospatial/TerraMesh` (`terramesh.py` loader).
- **Auth:** none.
- **License:** CC BY-SA 4.0.
- **Time to first data:** minutes (one shard).
- **Hackathon problem:** any-to-any modality generation (TerraMind-style), e.g. DEM from S2.
- **Recent changes:** released 1 Aug 2025; S1 GRD temporal-alignment fix 5 Mar 2026; val buffer added 20 Aug 2026.
- **Sources:** [HF card](https://huggingface.co/datasets/ibm-esa-geospatial/TerraMesh), [arXiv 2504.11172](https://arxiv.org/abs/2504.11172)

### OlmoEarth pretraining dataset (AllenAI)
- **What:** Pretraining data for the OlmoEarth models: S2 L2A, S1 GRD, Landsat 8/9, CDL, ERA5, OSM, SRTM, WorldCereal, WorldCover, WRI/Meta canopy height.
- **Size:** 16.1 TB.
- **Coverage:** spatial: global; temporal: not stated.
- **Format:** see the GitHub doc `Pretraining-Dataset.md`.
- **Access:** HF `allenai/olmoearth_pretrain_dataset`.
- **Auth:** none.
- **License:** CC BY 4.0.
- **Time to first data:** minutes (one file).
- **Hackathon problem:** finetune OlmoEarth Nano/Tiny (1.4M–12.5M params) on a laptop.
- **Related:** `allenai/olmoearth_lcc` — land-cover change point labels, 400 GB including model output rasters, Apache-2.0.
- **Sources:** [HF card](https://huggingface.co/datasets/allenai/olmoearth_pretrain_dataset), [GitHub](https://github.com/allenai/olmoearth_pretrain), [olmoearth_lcc](https://huggingface.co/datasets/allenai/olmoearth_lcc)

### Copernicus-Pretrain
- **What:** 18.7M samples: S1/S2/S3/S5P + DEM.
- **Size:** 22.7 TB.
- **Coverage:** spatial: global; temporal: not stated.
- **Format:** GeoTIFF and WebDataset versions.
- **Access:** HF `wangyi111/Copernicus-Pretrain`; TorchGeo `CopernicusPretrain`.
- **Auth:** none.
- **License:** CC BY 4.0.
- **Time to first data:** minutes (one shard).
- **Hackathon problem:** air-quality (S5P) × land-cover representation.
- **Sources:** [Copernicus-FM GitHub](https://github.com/zhu-xlab/Copernicus-FM)

### MMEarth
- **What:** 12-modality pretraining (S2, S1, ASTER DEM, ERA5, …).
- **Size:** MMEarth 1.2M tiles 128 px: 597 GB (README) / 579 GB (TorchGeo). MMEarth64: 152 / 162 GB. MMEarth100k: 48 GB. Major TOM variant: 486 GB.
- **Coverage:** spatial: global; temporal: not stated.
- **Format:** HDF5.
- **Access:** sid.erda.dk share links (README); TorchGeo `MMEarth` (manual download).
- **Auth:** none.
- **License:** CC BY 4.0.
- **Time to first data:** ~40 min (100k).
- **Hackathon problem:** multimodal pretext training; weights ship in the MMEarth-train repo.
- **Sources:** [MMEarth-data](https://github.com/vishalned/MMEarth-data)

### Galileo pretraining data (NASA Harvest)
- **What:** Pretraining data for the Galileo model.
- **Size:** 11.8 GB.
- **Coverage:** not documented (no card).
- **Format:** not documented.
- **Access:** HF `nasaharvest/galileo-pretrain` (no README); models at `nasaharvest/galileo`.
- **Auth:** none.
- **License:** none on card.
- **Time to first data:** ~10 min.
- **Hackathon problem:** small multimodal model for crop/flood tasks.
- **Sources:** HF API; [Galileo GitHub](https://github.com/nasaharvest/galileo)

### SeCo (Seasonal Contrast)
- **What:** Uncurated S2 seasonal pretraining set plus ResNet checkpoints.
- **Size:** `seco_100k.zip` 7.3 GB; `seco_1m.zip` 36.3 GB.
- **Coverage:** spatial: global; temporal: seasonal.
- **Format:** zip.
- **Access:** Zenodo 4728033; TorchGeo `SeasonalContrastS2`.
- **Auth:** none.
- **License:** CC BY 4.0.
- **Time to first data:** ~6 min.
- **Hackathon problem:** seasonal change features.
- **Sources:** [Zenodo](https://zenodo.org/records/4728033)

### S2-100K (SatCLIP)
- **What:** 100k S2 patches for location-encoder pretraining.
- **Size:** 168 GB (HF); TACO 44 GB.
- **Coverage:** spatial: global; temporal: not stated.
- **Format:** GeoTIFF / TACO.
- **Access:** HF `torchgeo/s2-100k`; TorchGeo `S2100K`.
- **Auth:** none.
- **License:** MIT.
- **Time to first data:** ~40 min (TACO).
- **Hackathon problem:** geolocate an image ("where on Earth is this?").
- **Sources:** HF API; [TorchGeo pretraining table](https://raw.githubusercontent.com/torchgeo/torchgeo/main/docs/api/datasets/pretraining.csv)

### Five Billion Pixels
- **What:** 150 Gaofen-2 images at 4 m, 24 classes, >50,000 km² of China, >5 billion labelled pixels.
- **Size:** not stated.
- **Coverage:** spatial: China; temporal: not stated.
- **Format:** not stated.
- **Access:** Google Drive / Baidu (code FBPS, China region only).
- **Auth:** none.
- **License:** "open source license", not named.
- **Time to first data:** unknown (Google Drive throttling).
- **Hackathon problem:** fine-grained land cover in China; PANGAEA has no auto-download for it.
- **Sources:** [project page](https://x-ytong.github.io/project/Five-Billion-Pixels.html)

### OpenEarthMap
- **What:** 0.25–0.5 m global land cover, 8 classes (class count unverified).
- **Size:** 9.1 GB on Zenodo; the xBD RGB images must be added separately from xView2.
- **Coverage:** spatial: global; temporal: not stated.
- **Format:** GeoTIFF.
- **Access:** Zenodo 7223446; TACO `isp-uv-es/openearthmap-taco` (12.4 GB).
- **Auth:** none.
- **License:** Zenodo record says CC BY 4.0, but the README says label licences follow each source image's licence; the TACO card says CC BY-NC-SA 4.0. Treat as mixed.
- **Time to first data:** ~8 min.
- **Hackathon problem:** global high-res land cover for urban heat or flood exposure.
- **Sources:** [Zenodo](https://zenodo.org/records/7223446), [GitHub](https://github.com/bao18/open_earth_map)

### LoveDA
- **What:** 5,987 Google Earth 1024² images, 0.3 m, 7 classes, urban/rural domain shift.
- **Size:** 9.57 GB (Train 4.0, Val 2.4, Test 3.1 GB).
- **Coverage:** spatial: China (Nanjing/Changzhou/Wuhan, unverified); temporal: not stated.
- **Format:** PNG.
- **Access:** Zenodo 5706578; TorchGeo `LoveDA` (auto).
- **Auth:** none.
- **License:** **conflict** — Zenodo says CC BY 4.0; GitHub README and TorchGeo say CC BY-NC-SA 4.0. Treat as NC.
- **Time to first data:** ~3 min (Val).
- **Hackathon problem:** urban-vs-rural domain adaptation.
- **Sources:** [Zenodo](https://zenodo.org/records/5706578), [GitHub](https://github.com/Junjue-Wang/LoveDA)

### LandCoverNet
- **What:** Global annual 2018 land cover labelled against S1, S2 and Landsat-8.
- **Size:** e.g. Africa: S2 88 GB, S1 39 GB, L8 9.5 GB, labels 21 MB. North America: 79 / 40 / 10.5 GB. South America: 48 / 24 / 6.3 GB.
- **Coverage:** spatial: global (per continent); temporal: 2018.
- **Format:** GeoTIFF + STAC.
- **Access:** Source Coop `radiantearth/landcovernet` (DOI 10.34911/rdnt.63fxe5); `data.source.coop/radiantearth/landcovernet/`; Azure archives.
- **Auth:** none.
- **License:** not inspected.
- **Time to first data:** ~10 min (labels + Landsat-8).
- **Hackathon problem:** continental land-cover maps.
- **Sources:** [Source Coop API](https://source.coop/api/v1/products/radiantearth), Azure listing.

### DynamicEarthNet
- **What:** Daily Planet Fusion time series with monthly land-cover change labels.
- **Size:** HF `torchgeo/dynamic_earthnet` 563 GB; GEO-Bench-2 `aialliance/dynamic_earthnet` 93 GB; TACO 245 GB; video version 24.6 GB.
- **Coverage:** spatial: global sites; temporal: daily series.
- **Format:** GeoTIFF / TACO.
- **Access:** mediaTUM 1650201.
- **Auth:** none.
- **License:** varies by copy (GEO-Bench-2 card CC BY-SA 4.0; video version CC BY 4.0).
- **Time to first data:** ~20 min (video version).
- **Hackathon problem:** daily change detection.
- **Sources:** [dynnet GitHub](https://github.com/aysim/dynnet), HF API.

### CloudSEN12 / CloudSEN12+
- **What:** The largest expert-labelled S2 cloud/shadow segmentation set. v1.1 adds L1C+L2A and temporal support; patches padded to 512/2048.
- **Size:** HF repos 332–419 GB, cloud-optimised so you can stream; GEO-Bench-2 version 19.9 GB; Copernicus-Bench Cloud-S2 has 2,817 samples.
- **Coverage:** spatial: global; temporal: not stated.
- **Format:** TACO (GeoTIFF version on ScienceDataBank).
- **Access:** `import tacoreader; ds = tacoreader.load("tacofoundation:cloudsen12-l1c")`. Also on the old Azure blob `.../mlhub/cloudSEN12/`.
- **Auth:** none.
- **License:** CC0.
- **Time to first data:** minutes (streaming).
- **Hackathon problem:** on-board cloud screening to save downlink bandwidth (a space-sector problem).
- **Sources:** [CloudSEN12Plus card](https://huggingface.co/datasets/isp-uv-es/CloudSEN12Plus)

### Sentinel-2 Cloud Cover Detection (DrivenData / Radiant)
- **What:** 22,728 S2 chips with cloud masks.
- **Size:** train source 17.3 GB, test source 16.0 GB, labels <50 MB.
- **Coverage:** spatial: not stated; temporal: not stated.
- **Format:** GeoTIFF.
- **Access:** Source Coop `radiantearth/cloud-cover-detection-challenge`; TorchGeo `CloudCoverDetection` (auto from Azure).
- **Auth:** none.
- **License:** CC BY 4.0.
- **Time to first data:** ~15 min.
- **Hackathon problem:** as CloudSEN12.
- **Sources:** [TorchGeo table](https://raw.githubusercontent.com/torchgeo/torchgeo/main/docs/api/datasets/benchmark.csv), Azure listing.

### MegaEarth (OSM × Sentinel-2, Oct 2026)
- **What:** S2 L2A 2.56 km windows with OSM area labels, many classes, for zero-shot transfer.
- **Size:** 22.8 GB.
- **Coverage:** spatial: global; temporal: not stated.
- **Format:** parquet tables + imagery.
- **Access:** HF `Mead0w1ark/megaearth-osm-sentinel2`.
- **Auth:** none.
- **License:** mixed-source terms.
- **Time to first data:** ~20 min.
- **Hackathon problem:** open-vocabulary land-use search.
- **Sources:** [HF card](https://huggingface.co/datasets/Mead0w1ark/megaearth-osm-sentinel2)

---

### D. Benchmark suites and loaders

### TorchGeo (library) — v0.10.1, 29 Sep 2026
- **What:** PyTorch dataset classes for EO. The docs tables list:
  - ~75 benchmark datasets, 8 SpaceNet, 11 pretraining sets, 15 Copernicus-Bench tasks
  - 11 embedding products (Clay, Major TOM, Earth Index, Copernicus-Embed, EarthEmbeddings, Presto, Tessera, Google Satellite Embedding, Embedded Seamless Data)
  - 20 label/mask layers (CDL, NLCD, Open Buildings, Meta CHM, GlobalBuildingMap, EuroCrops, Global Mangrove Watch, …)
- **Auto-download (seen in source code):**
  - from HF: EuroSAT, DIOR, DOTA, BigEarthNet, SSL4EO-S12/L, Copernicus-Bench, PASTIS-R-100, LandCover.ai, CaBuAr, QuakeSet, MMFlood, FireRisk, BRIGHT, UC Merced, RESISC45, USAVars, Digital Typhoon, BioMassters, S2-100K
  - from Zenodo: LoveDA, PASTIS, CropHarvest, WorldStrat, BigEarthNet v1, SeCo, TreeSatAI, EuroCrops, ReforesTree
  - from Source Coop: FTW
  - from the Radiant Azure blob: AgriFieldNet, CV4A Kenya, South Africa crops, Rwanda field boundaries, NASA Marine Debris, Cloud Cover, Tropical Cyclone, Benin cashews, Western USA live fuel moisture
  - via AWS CLI: SatlasPretrain, SpaceNet
  - via S3 HTTPS: SkyScript
- **Manual download:** xBD; SEN12MS and So2Sat (FTP/mediaTUM); MMEarth; BioMassters; Inria; Potsdam/Vaihingen; DeepGlobe.
- **Size:** n/a.
- **Coverage:** n/a.
- **Format:** Python library.
- **Access:** `pip install torchgeo`; `EuroSAT(root, download=True)`.
- **Auth:** none.
- **License:** MIT (code; unverified); each dataset carries its own licence.
- **Time to first data:** minutes.
- **Hackathon problem:** fastest path from zero to a training loop.
- **Gotcha:** docs moved to docs.torchgeo.org; repo moved to github.com/torchgeo/torchgeo.
- **Sources:** [benchmark.csv](https://raw.githubusercontent.com/torchgeo/torchgeo/main/docs/api/datasets/benchmark.csv), [pretraining.csv](https://raw.githubusercontent.com/torchgeo/torchgeo/main/docs/api/datasets/pretraining.csv), [embeddings.csv](https://raw.githubusercontent.com/torchgeo/torchgeo/main/docs/api/datasets/embeddings.csv), [masks.csv](https://raw.githubusercontent.com/torchgeo/torchgeo/main/docs/api/datasets/masks.csv), [releases](https://api.github.com/repos/torchgeo/torchgeo/releases/latest)

### GEO-Bench (v1, ServiceNow)
- **What:** Foundation-model benchmark of classification and segmentation sets.
- **Size:** ~65 GB free disk needed (57 GB after cleanup); HF repo 18.2 GB.
- **Coverage:** mixed.
- **Format:** per-dataset (HDF5/webdataset copies exist).
- **Access:** `pip install geobench; geobench-download` (pulls from HF `recursix/geo-bench-1.0`). WebDataset copies: `isaaccorley/geobenchv1-webdataset`. TACO copies of individual tasks (`geobench-m-bigearthnet/so2sat/brick-kiln/forestnet/pv4ger/cashew-plant/neontree/nz-cattle/sa-crop-type`).
- **Auth:** none.
- **License:** HF card CC BY-SA 4.0; code Apache-2.0; per-dataset licences vary.
- **Time to first data:** ~1 h (all); minutes for a TACO task.
- **Hackathon problem:** benchmark a model in an afternoon.
- **Sources:** [GitHub](https://github.com/ServiceNow/geo-bench)

### GEO-Bench-2 (ServiceNow / IBM / TUM / AI Alliance, Nov 2025 – Jan 2026)
- **What:** 18 re-processed datasets on HF `aialliance/*`. Sizes:
  pastis 134.6 GB, biomassters 401 GB, substation 6.8 GB, benv2 24.9 GB, dynamic_earthnet 93.3 GB, spacenet7 6.3 GB, cloudsen12 19.9 GB, flair2 10.1 GB, kuro_siwo 15.1 GB, everwatch 3.5 GB, forestnet 5.7 GB, spacenet2 77.1 GB, burn_scars 5.5 GB, fotw 12.0 GB, nzcattle 0.5 GB, so2sat 2.4 GB, treesatai 11.4 GB, caffe 22.6 GB.
- **Size:** 0.5–401 GB per dataset (above).
- **Coverage:** mixed.
- **Format:** per-dataset.
- **Access:** `pip install geobenchv2; geobench-download --root data spacenet7 caffe`.
- **Auth:** none.
- **License:** per dataset, redistributed under the original licences (cards include attribution and takedown policy); code Apache-2.0.
- **Time to first data:** minutes for small sets.
- **Hackathon problem:** apples-to-apples evaluation of the team's model; tasks include substations (power grid), cattle, glacier fronts (CaFFe), floods, burn scars, field boundaries.
- **Sources:** [GitHub](https://github.com/The-AI-Alliance/GEO-Bench-2), [aialliance/spacenet7 card](https://huggingface.co/datasets/aialliance/spacenet7)

### PANGAEA benchmark
- **What:** FM evaluation suite: HLS Burn Scars, MADOS, PASTIS-R (via IGNF/PASTIS-HD), Sen1Floods11, xView2, Five Billion Pixels, DynamicEarthNet, CropTypeMapping-South Sudan, SpaceNet 7, AI4SmallFarms, BioMassters, and more.
- **Size:** per dataset.
- **Coverage:** mixed.
- **Format:** per dataset.
- **Access:** GitHub `VMarsocci/pangaea-bench`. Auto-download works for all except Five Billion Pixels and BioMassters.
- **Auth:** none.
- **License:** per dataset.
- **Time to first data:** varies.
- **Hackathon problem:** compare Prithvi, CROMA, DOFA, SatlasNet etc. on your task.
- **Sources:** [README](https://github.com/VMarsocci/pangaea-bench)

### Copernicus-Bench
- **What:** 15 tasks in 3 levels:
  - L1: Cloud-S2, Cloud-S3
  - L2: EuroSAT-S1/S2, BigEarthNet-S1/S2, LC100Cls/Seg-S3, DFC2020-S1/S2
  - L3: Flood-S1, LCZ-S2, Biomass-S3, AQ-NO2-S5P, AQ-O3-S5P
- **Size:** 155 GB total; tasks 1,995–27,000 samples.
- **Coverage:** mixed; Sentinel-1/2/3/5P.
- **Format:** per task.
- **Access:** HF `wangyi111/Copernicus-Bench`; TorchGeo `CopernicusBench*` classes; TACO copies (`isp-uv-es/copernicus-bench-*-taco`, e.g. flood-s1 4.8 GB).
- **Auth:** none.
- **License:** per task (CC0, CC BY 4.0, MIT, CDLA-Permissive).
- **Time to first data:** minutes per task.
- **Hackathon problem:** air-quality regression from Sentinel-5P (AQ-NO2/O3).
- **Sources:** [TorchGeo copernicus_bench.csv](https://raw.githubusercontent.com/torchgeo/torchgeo/main/docs/api/datasets/copernicus_bench.csv), [Copernicus-FM GitHub](https://github.com/zhu-xlab/Copernicus-FM)

### TACO catalogue (Univ. València ISP / ELLIOT; bulk update 8 Oct 2026)
- **What:** 134 HF datasets, mostly "repackaging, not new data" into TACO v3 with standard sample slots. Includes spacenet1–8, xview, xview2, starcop, marida, mados, mmflood, openearthmap, pastis-r, so2sat-lcz42, cropharvest, landcover-ai, crisislandmark-s1/s2, wildfires-cems, quakeset, chatearthnet, satin-*, bright-dfc2025, worldfloods-v2, treesatai, sen4agrinet, rsvqa-lr/hr, next-day-wildfire-spread, wildfirespreadts, hls-burn-scars, landsat30-au (VQA/caption), copernicus-bench-*, geobench-m-* and others.
- **Size:** 0.03–112 GB each (verified per repo).
- **Coverage:** mixed.
- **Format:** TACO v3 (COG + parquet in zip).
- **Access:** `hf_hub_download("isp-uv-es/<name>-taco", ...)` + `from taco.ml import Dataset`.
- **Auth:** none.
- **License:** each card carries the original licence.
- **Time to first data:** minutes.
- **Hackathon problem:** one uniform loader over dozens of tasks.
- **Gotcha:** the new `taco` reader builds from source (C++23, CMake, Ninja, libcurl ≥ 7.83, OpenSSL ≥ 3). Older sets use `pip`-installable `tacoreader`.
- **Sources:** [xview2-taco card](https://huggingface.co/datasets/isp-uv-es/xview2-taco), HF API listing.

### SustainBench
- **What:** 15 SDG-related tasks: poverty change, crop type mapping (Ghana/South Sudan, Kenya), crop yield, field delineation, weak cropland segmentation, brick kilns, out-of-domain land cover, representation learning, DHS-based tasks.
- **Size:** README recommends 125 GB RAM and 5 TB disk for everything; TorchGeo crop-yield subset 0.6 GB (CC BY-SA 4.0).
- **Coverage:** mixed (low/middle-income countries).
- **Format:** per task.
- **Access:** Google Drive folder from GitHub `sustainlab-group/sustainbench`.
- **Auth:** none stated.
- **License:** per dataset.
- **Time to first data:** minutes (crop yield) to hours.
- **Hackathon problem:** poverty mapping from space.
- **Sources:** [GitHub](https://github.com/sustainlab-group/sustainbench), [site](https://sustainlab-group.github.io/sustainbench/)

### MOSAIKS features
- **What:** K = 4,000 features per cell from a 2019 Q3 Planet global composite; native 0.01° grid plus 1°/0.25°/0.1° grids and ADM0–2 aggregates.
- **Size:** not stated (CSV).
- **Coverage:** spatial: global; temporal: 2019 Q3.
- **Format:** CSV.
- **Access:** mosaiks.org/global_grids, /precomputed; native resolution via Redivis (`redivis.com/datasets/8bqm-8efrp0kqg`).
- **Auth:** Redivis account.
- **License:** CC BY-NC-SA.
- **Time to first data:** ~30 min.
- **Hackathon problem:** predict any tabular socio-economic variable from space with ridge regression.
- **Sources:** [MOSAIKS API page](https://www.mosaiks.org/mosaiks_api), [mosaiks.org](https://www.mosaiks.org/)

### CoordBench (Taylor Geospatial, Oct 2026)
- **What:** Location-encoder benchmark: many configs (air temperature, bioclim, biomass, CropHarvest, human footprint, land cover, CDC PLACES, crop masks, …).
- **Size:** 0.57 GB.
- **Coverage:** mixed.
- **Format:** parquet.
- **Access:** HF `taylor-geospatial/CoordBench`.
- **Auth:** none.
- **License:** mixed per config.
- **Time to first data:** <1 min.
- **Hackathon problem:** evaluate SatCLIP/GeoCLIP-style embeddings.
- **Sources:** [HF card](https://huggingface.co/datasets/taylor-geospatial/CoordBench)

---

### E. Hazards: floods, fire, landslides, quakes, cyclones, methane

### Sen1Floods11
- **What:** Global S1/S2 flood segmentation: 446–447 hand-labelled chips plus 4,385 weakly labelled. Ships with checkpoints.
- **Size:** bucket total 36.9 GB (`v1.1/data/flood_events` 34.8 GB, `perm_water` 1.5 GB, four 0.13 GB checkpoints). README says "~14 GB". HF copy `blumenstiel/Sen1Floods11` 1.8 GB.
- **Coverage:** spatial: global flood events; temporal: event dates.
- **Format:** GeoTIFF + STAC catalog.
- **Access:** `gsutil -m rsync -r gs://sen1floods11 ./`, or anonymous HTTPS (`storage.googleapis.com/storage/v1/b/sen1floods11/o`).
- **Auth:** none.
- **License:** unverified.
- **Time to first data:** ~5 min (hand-labelled subset).
- **Hackathon problem:** near-real-time flood maps from any new S1 pass.
- **Sources:** [GitHub](https://github.com/cloudtostreet/Sen1Floods11), GCS listing.

### SEN12-FLOOD
- **What:** Co-registered S1 and S2 time series for flood detection (CNAM / ESA).
- **Size:** S1 6.36 GB, S2 4.17 GB.
- **Coverage:** spatial: flood sites; temporal: time series.
- **Format:** GeoTIFF + labels.
- **Access:** Source Coop `esa/sen12flood`; Azure `.../mlhub/archives/sen12floods_*`.
- **Auth:** none.
- **License:** CC BY 4.0.
- **Time to first data:** ~4 min.
- **Hackathon problem:** flood onset detection in time series.
- **Sources:** [README](https://radiantearth.blob.core.windows.net/mlhub/sen12floods/README.md)

### Kuro Siwo
- **What:** Global multi-temporal SAR flood mapping ("33 billion m²"), NeurIPS 2024.
- **Size:** HF GeoTIFFs 1.03 TB, WebDataset 1.19 TB; GEO-Bench-2 m-KuroSiwo 15.1 GB.
- **Coverage:** spatial: global; temporal: multi-temporal.
- **Format:** GeoTIFF / WebDataset.
- **Access:** HF `orion-ai-lab/Kuro-Siwo-GeoTIFFs`; Dropbox; `scripts/download_kuro_siwo.sh`; annotation polygons on GitHub `Orion-AI-Lab/KuroSiwo-annotations`.
- **Auth:** none.
- **License:** CC BY.
- **Time to first data:** ~12 min (GEO-Bench-2 subset).
- **Hackathon problem:** global SAR flood mapping.
- **Sources:** [GitHub](https://github.com/Orion-AI-Lab/KuroSiwo), [aialliance/kuro_siwo](https://huggingface.co/datasets/aialliance/kuro_siwo)

### WorldFloods v2 (ml4floods)
- **What:** S2 flood-extent segmentation.
- **Size:** HF repo 79 GB (README: ~76 GB); TACO 82.9 GB.
- **Coverage:** spatial: global; temporal: not stated.
- **Format:** GeoTIFF.
- **Access:** HF `isp-uv-es/WorldFloodsv2`; `pip install ml4floods`.
- **Auth:** none.
- **License:** CC BY-NC 4.0.
- **Time to first data:** ~1 h.
- **Hackathon problem:** flood mapping pipeline including deployment.
- **Sources:** [ml4floods GitHub](https://github.com/spaceml-org/ml4floods)

### MMFlood
- **What:** 1,748 S1 flood samples (with MapZen/OSM layers).
- **Size:** 11.2 GB.
- **Coverage:** spatial: global events; temporal: not stated.
- **Format:** GeoTIFF.
- **Access:** HF `links-ads/mmflood`; TorchGeo `MMFlood`.
- **Auth:** none.
- **License:** MIT.
- **Time to first data:** ~9 min.
- **Hackathon problem:** SAR flood mapping with hydrography context.
- **Sources:** HF API, TorchGeo table.

### ImpactMesh-Flood (IBM / DLR / ESA Φ-lab, Sep 2026)
- **What:** S1 RTC + S2 L2A at four time steps (pre-month, pre, event, post), DEM, Copernicus EMS masks. 24,578 samples over 206 events; `test_holdout` has 562 samples from unseen events. v1 is quality-cleaned.
- **Size:** 361 GB.
- **Coverage:** spatial: global (206 events); temporal: four steps per event.
- **Format:** tar per modality.
- **Access:** `hf download ibm-esa-geospatial/ImpactMesh-Flood --repo-type dataset --include "val/*"`.
- **Auth:** none.
- **License:** CC BY 4.0.
- **Time to first data:** minutes (val or S2RGB only).
- **Hackathon problem:** flood mapping that generalises to unseen events.
- **Sources:** [HF card](https://huggingface.co/datasets/ibm-esa-geospatial/ImpactMesh-Flood), [IBM blog link in card](https://research.ibm.com/blog/geospatial-flood-and-wildfire-mapping) (not fetched)

### ImpactMesh-Fire
- **What:** Wildfire counterpart of ImpactMesh-Flood.
- **Size:** 153.5 GB.
- **Coverage:** not inspected.
- **Format:** tar per modality (assumed same as Flood).
- **Access:** HF `ibm-esa-geospatial/ImpactMesh-Fire`.
- **Auth:** none.
- **License:** CC BY 4.0.
- **Time to first data:** minutes (subset).
- **Hackathon problem:** burned-area mapping across events.
- **Sources:** HF API.

### Other flood sets (brief)
- **C2S-MS Floods** (Azure archives): S1 2.0 GB, S2 3.3 GB.
- **NASA Flood Extent / ETCI 2021:** Source Coop `nasa/floods`, archive 4.4 GB; TorchGeo `ETCI2021` 66,810 samples.
- **Copernicus-Bench Flood-S1:** 5,000 samples, MIT.
- **FloodNet:** HF `torchgeo/floodnet` 12.8 GB (licence "other").
- **Sources:** Azure listing; [Source Coop nasa](https://source.coop/api/v1/products/nasa); TorchGeo table.

### Next Day Wildfire Spread (NDWS)
- **What:** 18,445 samples, each 64 km × 64 km at 1 km. Fire masks plus topography, vegetation, weather, drought and population. CONUS 2012–2020.
- **Size:** 3.96 GB; TACO 1.7 GB.
- **Coverage:** spatial: contiguous US; temporal: 2012–2020.
- **Format:** TFRecord.
- **Access:** `kaggle datasets download fantineh/next-day-wildfire-spread`; `isp-uv-es/next-day-wildfire-spread-taco`.
- **Auth:** Kaggle account (none for TACO).
- **License:** CC BY 4.0.
- **Time to first data:** ~2–4 min.
- **Hackathon problem:** next-day fire perimeter forecast for evacuation planning.
- **Sources:** [Kaggle API view](https://www.kaggle.com/api/v1/datasets/view/fantineh/next-day-wildfire-spread)

### WildfireSpreadTS
- **What:** Multi-modal daily time series for wildfire spread prediction.
- **Size:** 48.4 GB; TACO 8.4 GB. Converting to HDF5 doubles disk use.
- **Coverage:** spatial: US fires (unverified); temporal: daily.
- **Format:** GeoTIFF (HDF5 conversion recommended).
- **Access:** Zenodo 8006177.
- **Auth:** none.
- **License:** CC BY 4.0.
- **Time to first data:** ~8 min (TACO).
- **Hackathon problem:** multi-day spread forecasting.
- **Sources:** [Zenodo](https://zenodo.org/records/8006177), [GitHub](https://github.com/SebastianGer/WildfireSpreadTS)

### FireCube
- **What:** Daily datacube for wildfire modelling in Greece.
- **Size:** 23.5 GB.
- **Coverage:** spatial: Greece; temporal: daily.
- **Format:** single `dataset_greece.nc` (netCDF).
- **Access:** Zenodo 6475592.
- **Auth:** none.
- **License:** CC BY 4.0.
- **Time to first data:** ~20 min.
- **Hackathon problem:** daily fire-danger nowcasting.
- **Sources:** [Zenodo](https://zenodo.org/records/6475592)

### SeasFire cube
- **What:** Global seasonal fire datacube, 2001–2021 (monthly version adds SPEI and regional masks).
- **Size:** v0.3 44 GB (`seasfire_v0.3.zip`); monthly 67.9 GB; v0.4 at Zenodo 7108392 (cited in the HF card).
- **Coverage:** spatial: global; temporal: 2001–2021.
- **Format:** zarr.
- **Access:** Zenodo 8055879; HF `orion-ai-lab/seasfire_monthly`.
- **Auth:** none.
- **License:** CC BY 4.0.
- **Time to first data:** ~35 min.
- **Hackathon problem:** seasonal burned-area forecast.
- **Sources:** [Zenodo](https://zenodo.org/records/8055879), [HF](https://huggingface.co/datasets/orion-ai-lab/seasfire_monthly)

### California Burned Areas (CaBuAr)
- **What:** Pre/post-fire S2 with CAL FIRE masks.
- **Size:** HF repo storage 159 GB (multiple configs); TorchGeo: 424 samples, 512×512.
- **Coverage:** spatial: California; temporal: fire events.
- **Format:** HDF5 compressed with `hdf5plugin` BZip2.
- **Access:** `load_dataset("DarthReca/california_burned_areas", name="post-fire")`; TorchGeo `CaBuAr`.
- **Auth:** none.
- **License:** **conflict** — HF card CDLA-Permissive-2.0, TorchGeo OpenRAIL, GitHub MIT.
- **Time to first data:** minutes (one config).
- **Hackathon problem:** burn-severity mapping for recovery funding.
- **Sources:** [HF card](https://huggingface.co/datasets/DarthReca/california_burned_areas), [GitHub](https://github.com/DarthReca/CaBuAr)

### TS-SatFire
- **What:** 179 wildfire events over their full lifecycle: active-fire detection, daily monitoring, next-day prediction.
- **Size:** 76.3 GB.
- **Coverage:** spatial: not stated; temporal: event lifecycles.
- **Format:** GeoTIFF.
- **Access:** Kaggle `z789456sx/ts-satfire` (updated 2025-10-26).
- **Auth:** Kaggle account.
- **License:** CC BY 4.0.
- **Time to first data:** ~1 h.
- **Hackathon problem:** satellite active-fire tracking.
- **Sources:** [Kaggle API view](https://www.kaggle.com/api/v1/datasets/view/z789456sx/ts-satfire), [GitHub](https://github.com/zhaoyutim/TS-SatFire)

### HLS Burn Scars (NASA/IBM, used by Prithvi)
- **What:** 804 HLS 512×512 scenes, 6 bands, CONUS 2018–2021. Masks: 1 burn, 0 not burned, −1 missing.
- **Size:** repo 21 GB (incl. history); TACO 3.7 GB; GEO-Bench-2 5.5 GB.
- **Coverage:** spatial: contiguous US; temporal: 2018–2021.
- **Format:** GeoTIFF.
- **Access:** HF `ibm-nasa-geospatial/hls_burn_scars`.
- **Auth:** none.
- **License:** CC BY 4.0.
- **Time to first data:** ~3 min.
- **Hackathon problem:** finetune Prithvi on a laptop.
- **Sources:** [HF card](https://huggingface.co/datasets/ibm-nasa-geospatial/hls_burn_scars)

### FLOGA / FireRisk / Wildfires-CEMS
- **FLOGA:** S2 + MODIS, Greece burned areas.
  - Size: not stated. Coverage: Greece. Format: HDF5 (needs `hdf5plugin`).
  - Access: Dropbox. Auth: none. License: not checked.
  - Note: S2 products were reprocessed and old ones deleted, so the dataset was updated.
  - Source: [GitHub](https://github.com/Orion-AI-Lab/FLOGA)
- **FireRisk:** 91,872 NAIP images, 7 classes.
  - Access: TorchGeo `FireRisk`, HF `isaaccorley/fire_risk`. Auth: none.
  - License: CC BY-NC 4.0.
- **Wildfires-CEMS:** `isp-uv-es/wildfires-cems-taco`, 14.6 GB.
  - Auth: none. License: CC BY 4.0.

### Landslide4Sense
- **What:** 3,799 / 245 / 800 patches of 128×128, 14 bands (S2 B1–B12 + ALOS PALSAR slope + DEM), ~10 m.
- **Size:** 3.1 GB (Zenodo); HF repo 12.1 GB.
- **Coverage:** spatial: landslide regions (not listed); temporal: not stated.
- **Format:** HDF5 patches (unverified).
- **Access:** Zenodo 10463239; HF `ibm-nasa-geospatial/Landslide4sense`; IARAI cloud links.
- **Auth:** none.
- **License:** CC BY 4.0.
- **Time to first data:** ~3 min.
- **Hackathon problem:** post-monsoon/earthquake landslide inventory.
- **Sources:** [Zenodo](https://zenodo.org/records/10463239), [HF card](https://huggingface.co/datasets/ibm-nasa-geospatial/Landslide4sense)

### QuakeSet and Event-SAR (earthquakes)
- **QuakeSet:** 3,327 S1 samples; classify/regress earthquake impact.
  - Size: 11 GB. Coverage: global quakes. Format: HDF5 (unverified).
  - Access: HF `DarthReca/quakeset`; TorchGeo `QuakeSet`. Auth: none.
  - License: CC BY-NC 4.0 on HF vs OpenRAIL in TorchGeo.
  - Time to first data: ~9 min.
- **Event-SAR (GFM-Bench, Sep 2026):** 416 reviewed SAR/InSAR patches (314 from 53 earthquakes, 102 from 102 volcanic events), processed with ASF HyP3.
  - Size: 92.8 GB. Format: WebDataset tar/NumPy.
  - Access: HF `GFM-Bench/Event-SAR`. Auth: none. License: Apache-2.0.
  - Time to first data: ~1 h.
- **Hackathon problem:** rapid earthquake deformation/damage detection.
- **Sources:** HF API, [Event-SAR card](https://huggingface.co/datasets/GFM-Bench/Event-SAR)

### Tropical cyclones (NASA Tropical Storm Wind / Digital Typhoon)
- **What:** NASA Tropical Storm Wind: GOES imagery with wind speeds, 108,110 images (TorchGeo). Digital Typhoon: Himawari IR, 189,364 images.
- **Size:** NASA archives train 1.45 GB, test 0.92 GB; Digital Typhoon 179 GB (HF), TACO 108 GB.
- **Coverage:** NASA: Atlantic & East Pacific storms 2000–2019; Digital Typhoon: West Pacific.
- **Format:** images + labels.
- **Access:** Source Coop `nasa/tropical-storm-competition`; TorchGeo `TropicalCyclone`, `DigitalTyphoon`.
- **Auth:** none.
- **License:** CC BY 4.0.
- **Time to first data:** ~2 min (NASA set).
- **Hackathon problem:** wind-speed estimation from geostationary imagery.
- **Sources:** [Source Coop nasa](https://source.coop/api/v1/products/nasa), [TorchGeo table](https://raw.githubusercontent.com/torchgeo/torchgeo/main/docs/api/datasets/benchmark.csv)

### STARCOP (methane, AVIRIS-NG)
- **What:** Hyperspectral methane plume segmentation (HyperSTARCOP). Models on HF `isp-uv-es/starcop`.
- **Size:** 60.8 GB in 10 zips (e.g. `STARCOP_train_easy.zip` 9.0 GB); mini set on Google Drive (`gdown`); `previtus/starcop_allbands_mini` 2.9 GB; TACO 41.5 GB.
- **Coverage:** spatial: AVIRIS-NG flight lines (US, unverified); temporal: not stated.
- **Format:** GeoTIFF products (mag1c, TOA bands).
- **Access:** Zenodo 7863343; `pip install git+https://github.com/spaceml-org/STARCOP.git`.
- **Auth:** none.
- **License:** CC BY-NC 4.0.
- **Time to first data:** ~5 min (mini).
- **Hackathon problem:** super-emitter detection to trigger follow-up tasking.
- **Sources:** [Zenodo](https://zenodo.org/records/7863343), [GitHub](https://github.com/spaceml-org/STARCOP)

### MethaneSET (TACO Foundation, 2026)
- **What:** Unified multi-sensor methane plume sets with IMEO MARS and Carbon Mapper expert-verified masks:
  - s2-pretraining 56,344 samples / 36.9 GB
  - s2-finetune 3,552 / 6.1 GB
  - l89-pretraining 21,919 / 8.9 GB
  - l89-finetune 1,353 / 1.1 GB
  - EMIT 721 / 1,165 GB
  - synthetic plume bank 238,545 / 5.1 GB (WRF-LES)
  - bank-les 1,647 / 3.1 GB
- **Size:** per subset above.
- **Coverage:** spatial: global super-emitters; temporal: not stated.
- **Format:** parquet catalogues + COG.
- **Access:** HF `tacofoundation/methaneset` (also `csaybar/MethaneSET`); project page ipl-uv.github.io/taco-methaneset.
- **Auth:** none.
- **License:** CC BY-NC-SA 4.0.
- **Time to first data:** ~2 min (L8/9 finetune).
- **Hackathon problem:** detect plumes in free Sentinel-2/Landsat imagery, then estimate the source rate.
- **Sources:** [HF card](https://huggingface.co/datasets/tacofoundation/methaneset)

### CH4Net / MethaneS2CM / MethaneUnion / METER-ML
- **CH4Net:** methane plumes in S2 (Turkmenistan).
  - Size: not stated. Access: HF `av555/ch4net`.
  - Auth: **gated** (accept terms). License: CC BY-NC-ND 4.0.
- **MethaneS2CM:** 32×32 S2 patches at leak day T, T−90 and T−365, with Carbon Mapper plume masks and labels.
  - Size: 16.1 GB. Access: HF `H1deaki/MethaneS2CM`. Auth: none. License: CC BY-NC 4.0.
- **MethaneUnion:** Size 764 GB. Access: HF `yuyao42/MethaneUnion`.
  - Auth: **manually gated**. License: CC BY-NC 4.0.
- **METER-ML:** methane-source infrastructure classification.
  - Size: TACO 111 GB. Access: `isp-uv-es/meter-ml-taco`. Auth: none. License: CC BY 4.0.
- **Hackathon problem:** plume classification and attribution to facilities.
- **Sources:** HF API; [MethaneS2CM card](https://huggingface.co/datasets/H1deaki/MethaneS2CM)

### NASA EMIT L2B methane plume complexes / enhancement
- **What:** EMIT (ISS imaging spectrometer) methane products:
  - EMITL2BCH4PLM V002 (60 m plume complexes): 2022-08-09 → 2026-08-31, **1,686 granules** in CMR on 2026-10-24.
  - EMITL2BCH4ENH V002 + V003: 329,105 granules.
- **Size:** per granule (not summed).
- **Coverage:** spatial: ~52°N–52°S; temporal: Aug 2022 onward.
- **Format:** COG / GeoJSON (unverified).
- **Access:** NASA CMR / Earthdata Search / `earthaccess` (`short_name="EMITL2BCH4PLM"`). The LP DAAC product page now redirects to earthdata.nasa.gov.
- **Auth:** Earthdata login (usual for LP DAAC; unverified on page).
- **License:** NASA open data (unverified).
- **Time to first data:** ~10 min.
- **Hackathon problem:** live global methane-plume map from the ISS.
- **Sources:** [CMR PLM](https://cmr.earthdata.nasa.gov/search/collections.json?short_name=EMITL2BCH4PLM), [CMR ENH](https://cmr.earthdata.nasa.gov/search/collections.json?short_name=EMITL2BCH4ENH)

### Carbon Mapper plume data
- **What:** CH4/CO2 super-emitter plumes from Planet Tanager-1, NASA EMIT, AVIRIS and ASU GAO, added on an ongoing basis.
- **Size:** not stated.
- **Coverage:** spatial: global; temporal: ongoing.
- **Format:** portal, Data API, STAC API.
- **Access:** carbonmapper.org data portal.
- **Auth:** account required for the API.
- **License:** public access for non-commercial use; commercial use or redistribution requires contacting Carbon Mapper.
- **Time to first data:** ~15 min.
- **Hackathon problem:** emitter leaderboards / facility alerts.
- **Sources:** [carbonmapper.org/data](https://carbonmapper.org/data)

---

### F. Agriculture

### CropHarvest
- **What:** 70,213 crop / non-crop pixel time series, 351 classes (S1, S2, SRTM, ERA5).
- **Size:** 22.66 GB: `eo_data.tar.gz` 21.7 GB, `features.tar.gz` 0.07 GB, `labels.geojson` 0.07 GB, test features 0.78 GB.
- **Coverage:** spatial: global; temporal: not stated.
- **Format:** HDF5 features + GeoJSON.
- **Access:** Zenodo 7257688; `pip install cropharvest`; TorchGeo `CropHarvest`; TACO 3.5 GB.
- **Auth:** none.
- **License:** CC BY-SA 4.0.
- **Time to first data:** ~1 min (features).
- **Hackathon problem:** global cropland mask for food-security early warning.
- **Sources:** [Zenodo](https://zenodo.org/records/7257688), [GitHub](https://github.com/nasaharvest/cropharvest)

### PASTIS / PASTIS-R / PASTIS-HD
- **What:** 2,433 S2 time-series patches (128×128×T), 19 classes, panoptic parcels in France. PASTIS-R adds S1; PASTIS-HD adds SPOT-6.
- **Size:** PASTIS 28.8 GB; PASTIS-R 53.7 GB; pixel-set 27 GB; PASTIS-HD 91.9 GB (etalab-2.0); `torchgeo/PASTIS-R-100` 4.1 GB; GEO-Bench-2 134.6 GB.
- **Coverage:** spatial: France; temporal: one season's time series.
- **Format:** NumPy / GeoJSON (unverified).
- **Access:** Zenodo 5012942 / 5735646 / 5745151; TorchGeo `PASTIS` (auto).
- **Auth:** none.
- **License:** CC BY 4.0.
- **Time to first data:** ~4 min (100-patch subset).
- **Hackathon problem:** parcel-level crop monitoring for subsidies / insurance.
- **Sources:** [Zenodo PASTIS](https://zenodo.org/records/5012942), [GitHub](https://github.com/VSainteuf/pastis-benchmark)

### Sen4AgriNet (S4A)
- **What:** S2 crop-type time series, Catalonia / France (LPIS).
- **Size:** HF 281 GB; TACO 314 GB.
- **Coverage:** spatial: Catalonia, France; temporal: multi-year.
- **Format:** netCDF.
- **Access:** Dropbox (GitHub README); HF `Orion-AI-Lab/S4A`; `isp-uv-es/sen4agrinet-taco`.
- **Auth:** none.
- **License:** none on the HF card; TACO says CC BY-SA 4.0.
- **Time to first data:** hours (single netCDF files: minutes).
- **Hackathon problem:** European crop classification.
- **Sources:** [GitHub](https://github.com/Orion-AI-Lab/S4A)

### EuroCrops / EuroCropsML
- **What:** EuroCrops: harmonised self-declared crop parcels across the EU (vector), version 11 on Zenodo. EuroCropsML: ML-ready version.
- **Size:** EuroCrops 8.6 GB in 39 files (e.g. FR_2018 2.6 GB); EuroCropsML 7.2 GB on HF `tbbotchwey/eurocropsml` (licence none on card).
- **Coverage:** spatial: EU countries; temporal: per country-year.
- **Format:** shapefile / GeoParquet.
- **Access:** Zenodo 8229128; TorchGeo `EuroCrops`.
- **Auth:** none.
- **License:** CC BY-SA 4.0 (EuroCrops).
- **Time to first data:** ~1 min per country.
- **Hackathon problem:** label source for S2 crop classifiers.
- **Sources:** [Zenodo](https://zenodo.org/records/8229128), [GitHub](https://github.com/maja601/EuroCrops)

### AgriFieldNet (India)
- **What:** S2 crop types in Uttar Pradesh, Rajasthan, Odisha and Bihar (IDinsight). 7,081 samples, 14 classes.
- **Size:** source 0.32 GB, labels ~1 MB.
- **Coverage:** spatial: 4 Indian states; temporal: not stated.
- **Format:** GeoTIFF.
- **Access:** Source Coop `radiantearth/agrifieldnet-competition`; TorchGeo `AgriFieldNet` (auto, Azure).
- **Auth:** none.
- **License:** CC BY 4.0.
- **Time to first data:** ~1 min.
- **Hackathon problem:** smallholder crop mapping.
- **Sources:** [Source Coop API](https://source.coop/api/v1/products/radiantearth), [TorchGeo table](https://raw.githubusercontent.com/torchgeo/torchgeo/main/docs/api/datasets/benchmark.csv)

### Fields of The World (FTW)
- **What:** About 1.6M parcel boundaries and 70,000+ samples in 24 countries. Instance + 2/3-class semantic masks; bi-temporal S2 RGB+NIR (window A/B); blocked 3×3 splits (80/10/10).
- **Size:** archive 56.8 GB in per-country zips (Rwanda 0.06 GB … Austria 5.5 GB).
- **Coverage:** spatial: 24 countries on 4 continents; temporal: two windows per season.
- **Format:** GeoTIFF + GeoParquet chips file.
- **Access:** `data.source.coop/kerner-lab/fields-of-the-world-archive/rwanda.zip` (anonymous); CLI `ftw data download --countries=Rwanda`; TorchGeo `FieldsOfTheWorld`. Related: `wherobots/fields-of-the-world` (2025 model-bakeoff mosaics, Zarr), GEO-Bench-2 `aialliance/fotw` 12 GB, Planet `eu-field-boundaries` (2022), fiboa (49 products).
- **Auth:** none.
- **License:** "Various" (per-country source licences).
- **Time to first data:** ~1 min (Rwanda).
- **Hackathon problem:** delineate fields anywhere with `ftw inference` on a fresh S2 pair.
- **Sources:** [README](https://data.source.coop/kerner-lab/fields-of-the-world/README.md), [ftw-baselines](https://github.com/fieldsoftheworld/ftw-baselines)

### Radiant MLHub crop datasets (now on Source Coop + the original Azure archives)
All are under `https://radiantearth.blob.core.windows.net/mlhub/archives/` (anonymous), with Source Coop pages where they exist:

| Dataset | Archive sizes (verified) | Source Coop / TorchGeo |
|---|---|---|
| CV4A Kenya crop type (ICLR 2020) | `ref_african_crops_kenya_02_source` 3.7 GB; kenya_01 5.6 GB | `radiantearth/african-crops-kenya-02` (DOI 10.34911/rdnt.dw605x); TorchGeo `CV4AKenyaCropType` (CC BY-SA 4.0) |
| Great African Food Co. Tanzania | 43.7 GB | `radiantearth/african-crops-tanzania-01` |
| Dalberg Uganda | 63.7 GB | `radiantearth/african-crops-uganda-01` |
| South Africa crop type (Spot the Crop) | S2 train 55.9 GB (or per band ~1.7–6.8 GB), S1 6.0 GB, labels 31 MB | `radiantearth/south-africa-crops-competition`; TorchGeo `SouthAfricaCropType` (CC BY 4.0) |
| DLR fusion competition (Brandenburg + Western Cape) | S2 11.7–12.4 GB per split; Planet 5-day 15–30 GB; Planet daily 79–160 GB | `esa/fusion-competition` (DOI 10.34911/rdnt.z9y7vu) |
| Stanford Ghana / South Sudan | S2 8.2 / 20.2 GB, S1 11.9 / 32.1 GB, Planet 68.5 / 159 GB | used by SustainBench / PANGAEA |
| NASA Rwanda field boundary | 0.11 GB | `nasa/rwanda-field-boundary-competition`; TorchGeo `RwandaFieldBoundary` (NICFI + CC BY 4.0) |
| UMD Mali crop type | 0.47 GB | — |
| TechnoServe Benin cashew | 0.86 GB | TorchGeo `BeninSmallHolderCashews` (CC BY 4.0) |
| RTI Rwanda crop type | 0.10 GB (raw 28.7 GB) | — |
| CGIAR East Africa field centres | 0.86–0.87 GB | — |
| Lacuna Fund EOTG v1 | 0.01–2.3 GB parts | fiboa `lacunalabels` |

- **Coverage:** Africa / Germany / India (as above).
- **Format:** GeoTIFF + GeoJSON/STAC.
- **Auth:** none.
- **License:** per dataset (above where known).
- **Time to first data:** 1–5 min for the small ones.
- **Hackathon problem:** smallholder food-security mapping.
- **Sources:** [Azure listing](https://radiantearth.blob.core.windows.net/mlhub?restype=container&comp=list&prefix=archives/), [Source Coop radiantearth](https://source.coop/radiantearth), [esa](https://source.coop/api/v1/products/esa), [nasa](https://source.coop/api/v1/products/nasa)

### Multi-temporal crop classification (NASA/IBM, used by Prithvi)
- **What:** 3,854 chips of 224×224 at 30 m; 18 bands (6 HLS bands × 3 dates); CDL 2022 labels, 13 classes; 80/20 split.
- **Size:** HF repo 11.8 GB.
- **Coverage:** spatial: contiguous US; temporal: 2022 growing season.
- **Format:** GeoTIFF.
- **Access:** HF `ibm-nasa-geospatial/multi-temporal-crop-classification`.
- **Auth:** none.
- **License:** CC BY 4.0.
- **Time to first data:** ~10 min.
- **Hackathon problem:** finetune Prithvi for crop maps.
- **Sources:** [HF card](https://huggingface.co/datasets/ibm-nasa-geospatial/multi-temporal-crop-classification)

### Other new agriculture sets (2025–2026)
- **Planet RapidCrops:** 99M EU parcels with harmonised crop type, 7 countries × 5–7 years.
  - Access: Source Coop `planet/rapidcrops`. Auth: none.
- **Planet agroforestry India (May 2026):** individual tree detection (GeoTIFF + COCO) and tree species identification (23,156 trees; SkySat crops + S1/S2/PlanetScope time series).
  - Access: Source Coop `planet/agroforestry-*`. Auth: none.
- **torchgeo/CropClimateX** (6.5 TB, CC BY 4.0) and **torchgeo/harmonized_global_crops** (17.8 GB, CC BY-SA 4.0).
  - Access: HF. Auth: none.
- **Sources:** [Source Coop planet](https://source.coop/api/v1/products/planet), HF API.

---

### G. Super-resolution

### S2-NAIP / Satlas Super-Resolution (AllenAI)
- **What:** Sentinel-2 time series paired with NAIP (US). Splits: urban train set (cities ≥50k population), full train set, val set (8,192 pairs, 12 bands), small val set, test set (incl. Dry Tortugas, Bolivia, France, South Africa, Japan). Pretrained ESRGAN weights ship with it.
- **Size:** HF `allenai/s2-naip` 65.5 TB (Apache-2.0 card); `allenai/satlas-super-resolution` 1.1 TB.
- **Coverage:** spatial: US (NAIP) plus global test sites; temporal: S2 time series.
- **Format:** tar / 7z on GCS.
- **Access:** `https://storage.googleapis.com/satlas-satellite-super-resolution/super_resolution_val_set_2024-01-09.tar`.
- **Auth:** none.
- **License:** Apache-2.0 (HF card).
- **Time to first data:** minutes (val/test tars).
- **Hackathon problem:** "NAIP-quality" imagery anywhere from free S2.
- **Sources:** [GitHub](https://github.com/allenai/satlas-super-resolution), HF API.

### WorldStrat
- **What:** SPOT 6/7 high-res images paired with multi-temporal S2; 3,928 samples.
- **Size:** v1.1 104 GB: hr 40.8 GB, lr L1C 26.4 GB, lr L2A 25.5 GB, hr raw 11.4 GB. TACO 37.3 GB.
- **Coverage:** spatial: global stratified sample; temporal: multi-temporal S2.
- **Format:** GeoTIFF zips + CSV metadata.
- **Access:** Zenodo 15382551; TorchGeo `WorldStrat` (auto).
- **Auth:** none.
- **License:** CC BY-NC 4.0 AND CC BY 4.0.
- **Time to first data:** ~30 min (TACO).
- **Hackathon problem:** multi-frame super-resolution for humanitarian mapping.
- **Sources:** [Zenodo](https://zenodo.org/records/15382551)

### SEN2NAIP / SEN2NAIPv2 / SEN2VENµS / OpenSR-test / SEN2NEON
- **What:** Super-resolution training and test sets in TACO format.
- **Size:** SEN2NAIP 185 GB (CC BY 4.0); SEN2NAIPv2 609 GB (CC0); SEN2VENµS 338 GB (CC BY 4.0 / CC BY-NC 4.0 / etalab-2.0); opensr-test 7.2 GB (MIT); SEN2NEON 386 GB (CC BY 4.0, Aug 2026).
- **Coverage:** US (NAIP/NEON) and VENµS sites.
- **Format:** TACO.
- **Access:** HF `isp-uv-es/*`, `tacofoundation/*`.
- **Auth:** none.
- **License:** as listed.
- **Time to first data:** ~6 min (opensr-test).
- **Hackathon problem:** benchmark a super-resolution model honestly.
- **Sources:** HF API.

---

### H. Vision-language EO

### GEOBench-VLM
- **What:** More than 10,000 manually verified instructions: scene understanding, counting, localisation, fine-grained categories, temporal analysis. One config has 3,211 examples.
- **Size:** 9.5 GB.
- **Coverage:** mixed.
- **Format:** parquet with images.
- **Access:** HF `aialliance/GEOBench-VLM`.
- **Auth:** none.
- **License:** none on card.
- **Time to first data:** ~8 min.
- **Hackathon problem:** evaluate Claude/GPT/Gemini as an EO analyst.
- **Sources:** [HF card](https://huggingface.co/datasets/aialliance/GEOBench-VLM), [GitHub](https://github.com/The-AI-Alliance/GEO-Bench-VLM)

### EarthVQA (EarthVLSet)
- **What:** Relational VQA over LoveDA-style imagery.
- **Size:** 18 GB.
- **Coverage:** not inspected.
- **Format:** images + QA.
- **Access:** HF `Kingdrone-Junjue/EarthVLSet`; weights at `Kingdrone-Junjue/EarthVQA-pretrained`.
- **Auth:** **gated (auto)**.
- **License:** CC BY-NC-ND 4.0 on HF vs BY-NC-SA on GitHub.
- **Time to first data:** ~15 min.
- **Hackathon problem:** "ask the map" urban-planning assistant.
- **Sources:** [GitHub](https://github.com/Junjue-Wang/EarthVQA), HF API.

### RSVQA (LR / HR; BEN variant not checked)
- **What:** Remote-sensing visual question answering (Sentinel-2 low-res; USGS high-res).
- **Size:** LR 0.15 GB (`Images_LR.zip` 0.10 GB); HR 14.45 GB (`Images.tar` 13.5 GB).
- **Coverage:** LR: Netherlands (unverified); HR: USGS orthophotos (US).
- **Format:** images + JSON QA.
- **Access:** Zenodo 6344334 / 6344367; TACO copies.
- **Auth:** none.
- **License:** CC BY 4.0 (Zenodo; TACO card says ODbL).
- **Time to first data:** ~1 min (LR).
- **Hackathon problem:** quick VQA baseline.
- **Sources:** [Zenodo LR](https://zenodo.org/records/6344334), [Zenodo HR](https://zenodo.org/records/6344367)

### RS5M
- **What:** About 5M remote-sensing image–text pairs (128 WebDataset tars); GeoRSCLIP and GeoRSSD models ship with it.
- **Size:** ~500 GB (`omlab/RS5M` 505 GB); metadata `Zilun/RS5M` 19 GB.
- **Coverage:** mixed.
- **Format:** WebDataset.
- **Access:** HF `omlab/RS5M`; Baidu.
- **Auth:** none.
- **License:** **conflict** — `omlab` card says MIT, `Zilun` card says CC BY-NC 4.0.
- **Time to first data:** minutes (one tar).
- **Hackathon problem:** text-to-image search over EO.
- **Sources:** [GitHub](https://github.com/om-ai-lab/RS5M), HF API.

### SkyScript
- **What:** 5.2M image–text pairs (OSM tags; LLM-smoothed captions added Dec 2024); benchmarks and CLIP checkpoints included.
- **Size:** six image zips: images2 9.7 GB, images3 9.7 GB, images4–7 13.6 GB each (≈74 GB); meta 0.4 GB each.
- **Coverage:** spatial: global; sources: NAIP, SWISSIMAGE, SkySat, S2, Landsat.
- **Format:** JPG + pickle meta + CSV captions.
- **Access:** `https://opendatasharing.s3.us-west-2.amazonaws.com/SkyScript/images2.zip`; TorchGeo `SkyScript` (auto).
- **Auth:** none.
- **License:** MIT (TorchGeo).
- **Time to first data:** ~8 min per zip.
- **Hackathon problem:** open-vocabulary retrieval ("show me all marinas").
- **Sources:** [GitHub](https://github.com/wangzhecheng/SkyScript), HEAD requests on the S3 objects.

### GeoChat_Instruct
- **What:** 318k RS instruction-tuning examples (LRBEN, NWPU captions, SOTA, SIOR, FAST).
- **Size:** HF repo 102 GB (JSON + image zips).
- **Coverage:** mixed.
- **Format:** JSON + image zips.
- **Access:** HF `MBZUAI/GeoChat_Instruct`.
- **Auth:** none.
- **License:** Apache-2.0 on card; underlying images carry their own licences.
- **Time to first data:** ~1 min (JSON only).
- **Hackathon problem:** finetune a small VLM for grounded EO chat.
- **Sources:** [HF card](https://huggingface.co/datasets/MBZUAI/GeoChat_Instruct)

### ChatEarthNet
- **What:** Global S2 image–text pairs.
- **Size:** 38.4 GB: RGB 13.0 GB, bands 8/11/12 13.4 GB, bands 5/6/7 12.0 GB, JSON 0.02 GB. TACO 68.7 GB.
- **Coverage:** spatial: global; temporal: not stated.
- **Format:** image zips + JSON.
- **Access:** Zenodo 11003436.
- **Auth:** none.
- **License:** CC BY 4.0.
- **Time to first data:** ~12 min.
- **Hackathon problem:** caption generation for S2 scenes.
- **Sources:** [Zenodo](https://zenodo.org/records/11003436), [GitHub](https://github.com/zhu-xlab/ChatEarthNet)

### EarthDial
- **What:** Multi-sensor VLM training data (RGB, multispectral, SAR, temporal; methane / urban heat island tasks). EarthDial_4B models ship with it.
- **Size:** 2.43 TB.
- **Coverage:** mixed.
- **Format:** Arrow.
- **Access:** HF `akshaydudhane/EarthDial-Dataset` (`snapshot_download` with patterns).
- **Auth:** none.
- **License:** Apache-2.0 (card).
- **Time to first data:** minutes (one downstream test set).
- **Hackathon problem:** multispectral VLM demo.
- **Sources:** [GitHub](https://github.com/hiyamdebary/EarthDial)

### VRSBench
- **What:** 29,614 images, 52,472 object references, VQA pairs (README prints "3123,221" — sic, probably 123,221).
- **Size:** 12.7 GB.
- **Coverage:** mixed.
- **Format:** HF datasets (streamable).
- **Access:** `load_dataset("xiang709/VRSBench", streaming=True)`.
- **Auth:** none.
- **License:** CC BY 4.0.
- **Time to first data:** ~10 min.
- **Hackathon problem:** referring-expression grounding.
- **Sources:** [HF card](https://huggingface.co/datasets/xiang709/VRSBench)

### OmniEarth-Bench
- **What:** Multi-sphere (atmosphere, biosphere, cryosphere, ocean, lithosphere, human activity) VQA and multiple-choice.
- **Size:** 19.8 GB (MCQ variants exist). A separate `sjeeudd/OmniEarth` (9.2 GB, Apache-2.0) is unverified as to content.
- **Coverage:** mixed.
- **Format:** not inspected.
- **Access:** HF `initiacms/OmniEarth-Bench`.
- **Auth:** none.
- **License:** none on card.
- **Time to first data:** ~15 min.
- **Hackathon problem:** Earth-system VLM evaluation.
- **Sources:** [GitHub](https://github.com/nanocm/OmniEarth-Bench)

### SkyScraper (Planet, May 2026)
- **What:** Geolocated PlanetScope / Sentinel-2 image sequences linked to GDELT news articles: event type, caption, visibility, dates, article text. Croissant 1.1 metadata.
- **Size:** not summed (JPEG stacks per `article_id`).
- **Coverage:** spatial: news-event locations; temporal: e.g. 2021 (sample paths).
- **Format:** JPEG + labels.csv + JSON metadata.
- **Access:** `data.source.coop/planet/skyscraper/` (anonymous).
- **Auth:** none.
- **License:** CC BY-NC 4.0, plus Planet / Copernicus / GDELT / publisher terms.
- **Time to first data:** minutes (labels.csv).
- **Hackathon problem:** "news-to-orbit" event verification — does the satellite confirm the headline?
- **Sources:** [README](https://data.source.coop/planet/skyscraper/README.md)

---

### I. Microsoft "AI for Good" and other label layers

### Microsoft Global ML Building Footprints / US Building Footprints / Road Detections
- **What:** Global: 1.4B buildings from Bing imagery 2014–2024 (Maxar, Airbus, IGN). US: 129,591,852 footprints. Roads: 54.2M km.
- **Size:** per region (not summed).
- **Coverage:** spatial: global / US; temporal: 2014–2024 imagery.
- **Format:** GeoJSON / CSV per region.
- **Access:** GitHub download links (coverage GeoJSON at minedbuildings.z5.web.core.windows.net).
- **Auth:** none.
- **License:** global CDLA-Permissive-2.0; US ODbL; roads ODbL.
- **Time to first data:** minutes per region.
- **Hackathon problem:** labels for training or for change detection against fresh imagery.
- **Sources:** [GlobalMLBuildingFootprints](https://github.com/microsoft/GlobalMLBuildingFootprints), [USBuildingFootprints](https://github.com/microsoft/USBuildingFootprints), [RoadDetections](https://github.com/microsoft/RoadDetections)

### Global Renewables Watch (Microsoft)
- **What:** Quarterly global commercial solar PV farms and onshore wind turbines, 2017 Q4–2024 Q2, with construction dates. Solar/wind models ship in release v1.1 (128 MB / 94 MB).
- **Size:** `solar_all_2024q2_v1.gpkg` 395 MB; `wind_all_2024q2_v1.gpkg` 58 MB.
- **Coverage:** spatial: global; temporal: 2017 Q4–2024 Q2.
- **Format:** GeoPackage.
- **Access:** GitHub release v1.0.
- **Auth:** none.
- **License:** repo MIT; data licence unverified.
- **Time to first data:** ~1 min.
- **Hackathon problem:** renewable build-out tracker.
- **Sources:** [GitHub](https://github.com/microsoft/global-renewables-watch), [releases API](https://api.github.com/repos/microsoft/global-renewables-watch/releases)

### Chesapeake Land Cover (Microsoft AI for Earth) / EnviroAtlas
- **What:** 1 m land cover with NAIP, Landsat and NLCD layers.
- **Size:** Azure archives: NAIP 243 GB (v2 new/old 74 / 71 GB), LC 1.2 GB (v2 0.46 GB), Landsat leaf-on/off ~1.9–96 GB, buildings 0.1 GB. Zenodo "prior extension" 5.5 GB. EnviroAtlas 11.8 GB (Zenodo 5778193, CC BY 4.0).
- **Coverage:** spatial: Chesapeake Bay watershed (EnviroAtlas: US cities); temporal: not stated.
- **Format:** GeoTIFF.
- **Access:** Source Coop `microsoft/chesapeake-land-cover`; TorchGeo `Chesapeake*`.
- **Auth:** none.
- **License:** CC0 per TorchGeo (Zenodo records CC BY 4.0).
- **Time to first data:** ~5 min (prior extension).
- **Hackathon problem:** 1 m land cover for stormwater planning.
- **Sources:** [Zenodo 5866525](https://zenodo.org/records/5866525), Azure listing.

### GloSoFarID
- **What:** Global multispectral S2 solar-farm identification, 2021–2023.
- **Size:** 10.24 GB.
- **Coverage:** spatial: global + US subsets; temporal: 2021–2023.
- **Format:** TFRecords.
- **Access:** Zenodo 10939100.
- **Auth:** none.
- **License:** CC BY 4.0.
- **Time to first data:** ~9 min.
- **Hackathon problem:** detect new solar farms from free imagery.
- **Sources:** [Zenodo](https://zenodo.org/records/10939100)

---

### J. Kaggle EO classics
All verified through the Kaggle dataset-view API except the competitions. Each needs a Kaggle account (and `kaggle` CLI or browser).

| Slug | What | Size | License | Problem |
|---|---|---|---|---|
| `nikitarom/planets-dataset` | Mirror of Planet "Understanding the Amazon from Space" | 1.60 GB | ODbL (mirror) | deforestation/mining tags |
| `kmader/satellite-images-of-hurricane-damage` | Hurricane Harvey damage / no-damage | 0.06 GB | CC BY 4.0 | fast damage classifier |
| `adrianboguszewski/landcoverai` | LandCover.ai (Poland, aerial) | 1.55 GB | CC BY-NC-SA 4.0 | building/wood/water/road segmentation |
| `balraj98/massachusetts-roads-dataset` / `-buildings-dataset` | Aerial roads/buildings | 10.56 / 2.78 GB | Other | road extraction |
| `balraj98/deepglobe-land-cover-classification-dataset` / `-road-extraction-dataset` | DeepGlobe | 2.96 / 4.12 GB | Other | crisis road mapping |
| `sorour/38cloud-cloud-segmentation-in-satellite-images` | 38 Landsat-8 scenes cloud masks | 17.05 GB | Unknown | cloud masking |
| `franciscoescobar/satellite-images-of-water-bodies` | S2 water masks (NDWI-derived) | 0.29 GB | CC BY-NC-SA 4.0 | reservoir monitoring |
| `crawford/deepsat-sat6` | NAIP SAT-6 | 5.65 GB | CC0 | scene classification |
| `humansintheloop/semantic-segmentation-of-aerial-imagery` | Dubai (MBRSC imagery) | 0.03 GB | CC0 | urban segmentation |
| `rhammell/planesnet` | Planet plane chips | 0.23 GB | CC BY-SA 4.0 | airfield activity |
| `airbusgeo/airbus-aircrafts-sample-dataset` | Pléiades aircraft | 0.09 GB | CC BY-NC-SA 4.0 | aircraft counting |
| `airbusgeo/airbus-wind-turbines-patches` | Wind turbines | 1.05 GB | CC BY-NC-SA 4.0 | turbine inventory |
| `towardsentropy/oil-storage-tanks` | Floating-roof tanks | 1.87 GB | Unknown | oil inventory from shadows |
| `arpitjain007/game-of-deep-learning-ship-datasets` | Ship-type images | 0.08 GB | ODbL | ship classification |
| `mahmoudreda55/satellite-image-classification` | RSI-CB256, 4 classes | 0.02 GB | © original authors | toy classifier |

- **Coverage:** as described per row.
- **Format:** images + labels (per dataset).
- **Time to first data:** 1–15 min (by size above).
- **Competitions not verified (pages need login):** Planet Amazon (original), Airbus Ship Detection, DSTL Satellite Imagery Feature Detection, Understanding Clouds. Note: `airbusgeo/airbus-oil-storage-detection` returned 403.
- **Sources:** e.g. [Kaggle API view](https://www.kaggle.com/api/v1/datasets/view/kmader/satellite-images-of-hurricane-damage) (same pattern for each slug).

---

## 3. Gotchas
- **Radiant MLHub:** mlhub.earth returns HTTP 404 today. No dated shutdown post appears on radiant.earth/blog, so "shut down 2023" is unverified; its radiantearth Source Coop products were created 2023-07-05. The old Azure container `https://radiantearth.blob.core.windows.net/mlhub/` is **still publicly listable and serving**, including `archives/*.tar.gz`. TorchGeo still downloads from it. Source Coop's `radiantearth` account lists only 7 products; other ex-MLHub sets sit under `nasa/`, `esa/`, `ramp/`, `microsoft/`, `planet/` (rapidai4eo) — or only on the Azure blob (Open Cities, LandCoverNet regions, Ghana/South Sudan, Mali, the African crop sets).
- **Source Coop:** public data is listable anonymously at `https://data.source.coop/<account>/<product>/` (S3-compatible XML). The product catalogue JSON is at `https://source.coop/api/v1/products/<account>`.
- **SpaceNet auth is contradictory.** spacenet.ai says "set up an AWS account". The AWS registry says no account is needed, and anonymous HTTPS listing and downloads work (verified).
- **Sen1Floods11:** the README mentions `gs://senfloods11/` (typo, denies anonymous listing); the real bucket is `gs://sen1floods11`. README says ~14 GB; the bucket totals 36.9 GB.
- **Non-commercial or restricted licences:**
  - CC BY-NC-SA: xBD, xView (TACO card), MethaneSET, OpenEarthMap TACO copy, MOSAIKS, LandCover.ai, OSSDD.
  - Academic only: DOTA, iSAID.
  - CC BY-NC: DIOR, STARCOP, WorldFloods, SkyScraper, Maxar Open Data, Planet disaster data, QuakeSet (HF), MethaneS2CM, MethaneUnion, FireRisk.
  - CC BY-NC-SA 3.0: FAIR1M.
  - CC BY-NC-ND: CH4Net, EarthVQA (HF card).
  - Partly NC: WorldStrat, BRIGHT.
  - Fine for a hackathon demo, but flag them if the team plans a startup pitch.
- **Licence conflicts between sources:** LoveDA (CC BY on Zenodo vs NC-SA on GitHub), CaBuAr (CDLA-2.0 / OpenRAIL / MIT), RS5M (MIT vs CC BY-NC), NASA Marine Debris (Apache vs CC BY-NC), QuakeSet, OpenEarthMap, RSVQA (CC BY vs ODbL).
- **Gated HF repos** need HF login and accepting terms: `Kingdrone-Junjue/EarthVLSet` (auto), `av555/ch4net` (auto), `yuyao42/MethaneUnion` (manual approval — may not arrive in time), `satellogic/EarthView` (auto).
- **HF `usedStorage` counts history**, so it can overstate (e.g. GeoChat_Instruct 102 GB). Huge repos (Major TOM, TerraMesh, OlmoEarth, SSL4EO v1.1) are sharded — download single parquet/tar files with `allow_patterns`.
- **New TACO tooling:** the 2026 `isp-uv-es/*-taco` repos need the C++23-built `taco` reader. CloudSEN12/MethaneSET use `tacoreader`. Budget install time.
- **mediaTUM** (SEN12MS, SSL4EO, DynamicEarthNet) is behind Anubis bot protection; scripted fetches fail. Use the FTP credentials (TorchGeo docstrings) or HF mirrors.
- **Download hosts that are hard from the US:** Baidu-only mirrors (Five Billion Pixels is China-region; DOTA/iSAID/HRSID/SSDD have Baidu too) and Google Drive links (quota "too many downloads" errors are common — unverified) — prefer HF mirrors. Dropbox for Kuro Siwo, Sen4AgriNet and FLOGA.
- **Hidden dependencies:** iSAID needs DOTA images. OpenEarthMap needs xBD images from xView2 (login). xBD in TorchGeo is manual download. fMoW torrents are dead; use S3.
- **xView2 / xView3 sites are JavaScript apps** and could not be verified. Community HF copies exist for xView/xBD under NC licences; there is no xView3 mirror on HF.
- **Version and date limits:** EMIT plume-complex V002 in CMR ends 2026-08-31 (a V003 may supersede it — unverified). SatlasPretrain has v0-beta and v1 files side by side — use the v1 URL list.
- **Kaggle:** datasets need an account and API token. Competitions additionally need rules accepted, and their APIs return 401 unauthenticated.
- **TorchGeo moved:** repo is now `github.com/torchgeo/torchgeo`, docs `docs.torchgeo.org`. Latest release v0.10.1 (2026-09-29).

## 4. Cross-slice leads
- **Space traffic / debris / weather (HF, updated daily, community uploads by juliensimon):**
  - `juliensimon/space-track-tle-history`: 122 GB, every TLE 1959–2026, 238M rows, CC BY 4.0 on the card. Space-Track's redistribution terms may conflict — unverified.
  - `space-track-satcat` 0.3 GB; `starlink-fleet-data` 2.3 GB; `starlink-tle-latest`; `constellation-tle-latest`; `kuiper-fleet-data`; `oneweb-fleet-data`; `ast-spacemobile-fleet-data`.
  - `satellite-conjunctions`: CelesTrak SOCRATES events with ≤1 km miss distance or Pc ≥ 1e-4, deduplicated; 1.4 GB; CelesTrak usage policy.
  - `reentry-events`, `orbital-fragmentation-events`, `fcc-ngso-filings`, `spacex-launches`, `space-launch-log`.
  - Space weather: `space-weather-indices`, `donki-space-weather-events`, `solar-flare-events`, `solar-wind`, `geomagnetic-kp-index`, `aurora-forecast`.
  - Other: `neo-close-approaches`, `global-meteor-network` (47 GB).
  - Collection: [Orbital Mechanics Datasets](https://huggingface.co/collections/juliensimon/orbital-mechanics-datasets-69c24caca4ab3934c9856994).
  - Also `FraDra/GEO_satellite_maneuvers` (simulated GEO station-keeping, 24.5 GB, MIT) and `patrickfleith/GOCE-satellite-telemtry` (327 real ESA GOCE telemetry channels 2009–2013, 45 GB, ESA T&C) — both good for space-ops anomaly detection.
- **EO companies with open labelled or event data:**
  - **Maxar Open Data:** `s3://maxar-opendata/events/` (CC BY-NC 4.0). Includes Hurricane Melissa Oct 2025, Typhoon Kalmaegi Nov 2025, Cyclones Ditwah/Senyar Nov 2025, Morocco flooding Dec 2025, LA wildfires Jan 2025, Myanmar earthquake Mar 2025, Texas flooding Jul 2025. Natural test data for xBD-trained models. Also Source Coop `maxar/maxar-opendata` (ARD).
  - **Umbra:** `s3://umbra-open-data-catalog/sar-data/tasks/` (e.g. Jamaica-2025-10, Atmospheric-River Nov 2025, mines, airbases).
  - **Capella:** `s3://capella-open-data/`.
  - **Planet:** disaster data on Source Coop `planet/disasterdata` (STAC, CC BY-NC), incl. Philippines earthquake 2026-06-08 and Venezuela earthquakes 2026-06-24.
  - **Satellogic EarthView:** HF `satellogic/EarthView`, 24.5 TB, gated (auto), CC BY 4.0.
  - **Earth Genome:** Earth Index embeddings v7 (Source Coop, 2026-10-19), Amazon Mining Watch (Jan 2026), S2 temporal mosaics.
  - **RarePlanes** (In-Q-Tel CosmiQ).
- **Embeddings (precomputed, no GPU needed):** AlphaEarth Foundations (Source Coop `tge-labs/aef`, `aef-mosaic`; Major TOM AlphaEarth 6.1 TB), Clay v0/v1.5, Earth Index, Tessera, Copernicus-Embed, MIND, Spheer FM mosaic, Google Satellite Embedding, Presto (TorchGeo embeddings table).
- **US agencies:** NASA EMIT (CMR), NASA-IMPACT `WxC-Bench` (961 GB, MIT, weather/aviation turbulence/hurricane tasks), IBM-NASA Prithvi datasets, `ibm-nasa-geospatial/gravity-wave-parameterization` (20.9 GB), `hls_merra2_gppFlux`, IARPA fMoW, DIU xView series, NGA (xView1).
- **ESA and other agencies:** ESA Φ-lab (Major TOM, TerraMesh, ImpactMesh, Copernicus-Bench), DLR (SSL4EO v1.1, ImpactMesh), IGN France (FLAIR-HUB 728 GB, etalab-2.0; PASTIS-HD), SRON / IMEO MARS (MethaneSET labels).
- **China-origin datasets:** Five Billion Pixels (GF-2), FAIR1M (Gaofen), DOTA / iSAID (GF-2, JL-1), LoveDA, DIOR, HRSID, SSDD, OpenSARShip (SJTU). Many are Baidu-first and academic-only.
- **Models shipped with datasets:** SpaceNet winners (`s3://spacenet-dataset/spacenet-model-weights/`), Satlas `.pth`, Sen1Floods11 checkpoints, STARCOP (HF `isp-uv-es/starcop`), SeCo checkpoints, MMEarth weights, GeoRSCLIP/GeoRSSD (RS5M), EarthDial_4B, Global Renewables Watch, OlmoEarth v1 / v1_1 / v1_2 (Nano 1.4M → Large 308M params), Galileo, BigEarthNet v2 models (HF `BIFOLD-BigEarthNetv2-0`), SkyScript CLIP.
- **Space science / literature:** `nasa-impact` HF has science QA/IR benchmarks; juliensimon hosts Mars craters, exoplanets, Parker/Solar Orbiter encounters, Mars rover weather, MAVEN, Cassini.

## 5. Leads not followed (or unresolved)
- **Tweets, X posts and blogs:** none checked — zero web searches were available. The IBM ImpactMesh blog (linked from the HF card) and the AllenAI OlmoEarth / TerraMind announcements were not fetched.
- **Unresolved values:**
  - xView3: exact size, licence and registration.
  - xView2 download page sizes beyond TorchGeo's ~7.8 / 2.6 GB.
  - Kaggle competitions (Airbus ship, Planet Amazon original, DSTL, Understanding Clouds) — sizes and rules.
  - SEN12MS and SEN12MS-CR mediaTUM sizes.
  - OpenSARShip chip counts.
  - Sen1Floods11 licence; HRSID licence; Sen4AgriNet licence; Open Cities AI licence; RarePlanes exact CC variant; Global Renewables Watch data licence.
- **Datasets not examined:** UrbanSARFloods (`earthnets/UrbanSARFloodsV1`), S1GFloods, Sim2Real-Fire, DisasterM3, XLRS-Bench, GeoPixel/GeoPixInstruct, LHRS-Align/Bench, VHM/VersaD, Git-10M, RSICD / UCM / Sydney captions, RSITMD, RemoteCLIP data, RSTeller, EarthGPT/MMRS-1M, SkyEyeGPT; AnySat / GeoPlex composition; EarthNet2021 and GreenEarthNet sizes (`pip install earthnet`; the README recommends 1 TB free); AI4Arctic sea ice (`torchgeo/ai4artic-sea-ice-challenge` 69.8 GB); HySpecNet-11k (EnMAP, 63.6 GB); DL4GAM glaciers; CaFFe glacier fronts; BioMassters (201 GB); FLAIR-HUB details; Planetary Computer catalogue; NASA IMPACT HLS foundation datasets beyond those listed; `sjeeudd/OmniEarth` content; Galileo pretrain card (no README); `CIawevy/GeoBench` (2,232 downloads — unclear if EO); `kinghorton42/geo-benchmarks`; the Little-Liu EarthNet2021 npz mirror.
- **SatlasPretrain:** only file sizes checked; no per-task label breakdown.
- **Source Coop:** only the accounts I guessed were listed; there is no global catalogue endpoint, so other EO accounts may exist.
