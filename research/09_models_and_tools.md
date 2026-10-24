# Off-the-shelf models, libraries, APIs and tools for building with space data

**Scope:** This report covers what you can download, pip-install or call today to build a space-data demo in a 36-hour hackathon (Cal Hacks 13.0, "Make it Legendary" challenge), and what each tool is good and bad at. It has ten categories:

1. EO foundation models
2. Vision-language and LLM geospatial models and agents
3. Detection, segmentation and change detection
4. Weather and climate AI
5. Heliophysics and space weather
6. Astronomy ML
7. Orbital mechanics and SSA
8. The geospatial data stack
9. Literature and knowledge tools
10. Hosted inference and compute

**Researched on 2026-10-24.** GitHub stars (★), last-push dates, latest releases and SPDX licenses were pulled from the GitHub API on 2026-10-24. Hugging Face download counts (30-day window) and licenses were pulled from the HF Hub API the same day. "NOASSERTION" means GitHub could not classify the license file; where it matters, the license text was read directly. Claims marked *(unverified)* or "seen in search results" were not confirmed on the primary page.

## Quick-pick table (all categories)

These are the most hackathon-relevant tools across all ten categories. Each section below has its own full quick-pick table and a detailed entry per tool. Effort is the time to a first working result for a team new to the tool.

| Tool | Category | What it unlocks | Effort | License |
|---|---|---|---|---|
| Grok API (grok-4.7, xai-sdk) | 2/10 Frontier LLM + vision + X/web search | Orchestrator, explainer, image Q&A, real-time X ground truth; challenge bonus | Minutes | Commercial API |
| AlphaEarth Satellite Embedding V1 | 1 Pre-computed EO embeddings | 10 m, 64-d annual embeddings of all land 2017–2024: few-shot maps, change detection | Minutes (Earth Engine) | CC-BY 4.0 |
| Major TOM SigLIP / DINOv2 embeddings | 1 Pre-computed EO embeddings | Text-to-satellite-image search over about 20M–56M Sentinel-2 patches | ~1 hour | CC-BY-SA-4.0 |
| TESSERA / geotessera | 1 Pre-computed EO embeddings | CC0 10 m embeddings outside Earth Engine | ~1 hour | MIT / CC0 |
| Prithvi-EO-2.0 + TerraTorch | 1 EO foundation model | Ready flood, burn-scar and crop fine-tunes | 1–3 hours (GPU) | Apache-2.0 |
| TerraMind 1.0 | 1 Generative EO foundation model | Any-to-any (S2→S1/LULC/DEM) generation; Colab | 1–3 hours | Apache-2.0 |
| OlmoEarth v1.3 | 1 EO foundation model family | Embeddings and fine-tuning, Nano to Large | 1–2 hours | OlmoEarth Artifact License (no defense or extractive use) |
| DINOv3 SAT-493M + CHMv2 | 1 RGB satellite backbone | High-res features; canopy height | ~1 hour (gated) | DINOv3 License |
| SAM 3 / SAM 3.1 | 3 Concept segmentation | "Segment all solar panels" from text | ~1 hour (gated, CUDA) | SAM License |
| segment-geospatial (samgeo) | 3 SAM for GeoTIFFs | Masks → vectors; text prompts; REST API | 30–60 min | MIT |
| Ultralytics YOLO26-OBB (DOTA) + SAHI | 3 Rotated detection | Ships, planes, tanks in high-res imagery | ~15 min | AGPL-3.0 / MIT |
| OmniCloudMask / Cloud Score+ | 3 Cloud masking | Clean optical time series | ~10 min | MIT / CC-BY-4.0 |
| SEN2SR / LDSR-S2 | 3 Super-resolution | Sentinel-2 to 2.5 m (beware hallucination) | ~1 hour | CC0 / see repo |
| ml4floods / Prithvi Sen1Floods11 | 3 Flood mapping | Flood extent from S2/S1 | 1–2 hours | LGPL + CC-BY-NC / Apache-2.0 |
| GFW SAR vessel detections API | 3 Pre-computed maritime detections | Dark vessels and offshore infrastructure without models | ~30 min | GFW terms |
| NASA FIRMS API | 3 Pre-computed active fires | Near-real-time fire points | ~15 min | NASA open |
| Microsoft Global ML Building Footprints | 3 Pre-computed buildings | 1.4B footprints plus heights (exposure analysis) | Minutes | See README (CDLA/ODbL) |
| WeatherNext 2 via Open-Meteo | 4 AI weather (hosted) | 64-member 15-day AI ensemble via one HTTP call | Minutes | Open-Meteo terms |
| WeatherNext repo (WN2, Cyclones, GraphCast, GenCast) | 4 Open-weights weather | Own forecasts and cyclone tracks; free Colab TPU (Mini) | 1–3 hours | Apache-2.0 / CC-BY-4.0 |
| NVIDIA Earth2Studio | 4 Weather model zoo | FourCastNet3, AIFS, GraphCast, CorrDiff behind one API | 1–2 hours (GPU) | Apache-2.0 |
| Aurora | 4 Earth-system FM | Weather, air quality, ocean waves | 1–2 hours | MIT |
| Surya | 5 Heliophysics FM | Flare (M/X, 24 h), solar wind, AR segmentation; runs on CPU/MPS for easy inference | 1–2 hours | Apache-2.0 |
| NASA-IBM Lunar Foundation Model | 5 Planetary FM | Crater detection, ice prospectivity on LROC | 1–3 hours | Apache-2.0 |
| NOAA SWPC JSON + NASA DONKI | 5 Live space-weather data | Kp, solar wind, flares, CMEs | Minutes | Public |
| AION-1 / AstroCLIP | 6 Astronomy FMs | Galaxy similarity search, cross-modal prediction | ~1–2 hours | MIT |
| ALeRCE / Fink | 6 Transient brokers (ZTF + Rubin LSST) | Live classified alerts and light curves | 15–30 min | MIT / Apache-2.0 |
| AstroSage-8B/70B | 6 Astronomy LLMs | Domain Q&A | Minutes–hours | Llama 3.1 |
| CelesTrak GP (OMM) + python-sgp4 / Skyfield | 7 Orbit data + propagation | Whole-catalogue propagation, passes; OMM for 6-digit catalog numbers | Minutes | Free / MIT |
| CesiumJS + satellite.js | 7 3D globe + JS SGP4 | Orbits on a 3D Earth in the browser | ~1 hour | Apache-2.0 / MIT |
| dSGP4 (ESA) | 7 Differentiable SGP4 (PyTorch) | GPU-batched propagation, ML-corrected SGP4 | ~1 hour | GPL-3.0 |
| NASA CARA Analysis Tools / Kessler | 7 Conjunction assessment | Probability-of-collision maths / ML for CDMs | Hours | No license / GPL-3.0 |
| Earth Search / Planetary Computer STAC + odc-stac | 8 Data access | Sentinel/Landsat/GOES/S5P/ERA5 as lazy xarray | Minutes | Free |
| Google Earth Engine + geemap | 8 Hosted analysis | Planet-scale compute, free noncommercial tiers | ~30 min | Free noncommercial |
| leafmap / lonboard / MapLibre + deck.gl | 8 Maps/UI | Interactive maps for the demo | Minutes–1 hour | MIT / MIT / BSD-3 |
| NASA ADS/SciX API + arXiv API | 9 Literature search | Space literature metadata and search | Minutes | Free (token for ADS) |
| INDUS retriever (nasa-smd-ibm-st-v2) | 9 NASA-domain embeddings | Better RAG over NASA science text | ~15 min | Apache-2.0 |
| PaperQA2 | 9 Literature agent | Cited answers from hundreds of PDFs | ~1 hour | Apache-2.0 |
| Modal | 10 Serverless GPUs | $30/month free; SAM 3 or Surya as an API | ~30 min | Commercial |
| Hugging Face Hub / Spaces | 10 Weights, demos | Most models here; Spaces demos | Minutes | Varies |

## 1. EO foundation models

**State of play (Oct 2026).** There are now dozens of open Earth-observation (EO) foundation models. They fall into two groups, and the difference matters a lot for a hackathon:

- **Encoders you run yourself.** Prithvi, TerraMind, Clay, OlmoEarth, Galileo, DOFA, Copernicus-FM, DINOv3-SAT, Panopticon, SMARTIES, AnySat and others. You download weights, feed them image chips, and either fine-tune or use the embeddings.
- **Pre-computed embedding products.** You never touch a GPU. Google's AlphaEarth Satellite Embedding (64-d per 10 m pixel per year), Cambridge's TESSERA (128-d per 10 m pixel), Major TOM's global embedding sets (SigLIP, DINOv2, SSL4EO), Copernicus-Embed-025deg (0.25° global grid) and Clay's embeddings on Source Cooperative.

The honest finding from the benchmarks is that **no single model wins everywhere**, and gains over a well-tuned U-Net are often small:
- PANGAEA says GFMs "do not consistently outperform supervised models" ([arXiv 2412.04204](https://arxiv.org/abs/2412.04204)).
- GEO-Bench-2 says "no single model dominates across all tasks". It finds that natural-image backbones (ConvNeXt, DINOv3) are best on high-resolution RGB tasks, while EO-specific models (TerraMind, Prithvi, Clay) win on multispectral agriculture and disaster tasks ([arXiv 2511.15658](https://arxiv.org/abs/2511.15658)).

For a hackathon, the pre-computed embeddings are the fastest way to show "AI over the whole planet" in a few hours. The fine-tunable encoders are worth it only when there is a ready fine-tuned checkpoint (flood, burn scar, crops) or a TerraTorch config to copy.

Stars, push dates and releases below come from the GitHub API on 2026-10-24. "dl/30d" is the Hugging Face 30-day download counter from the HF API on the same day.

### Quick-pick (EO foundation models)

| Tool | Category | What it unlocks | Effort | License |
|---|---|---|---|---|
| AlphaEarth Satellite Embedding V1 | Pre-computed embeddings | Global 10 m, 64-d annual embeddings 2017–2024; few-shot mapping and change detection with no GPU | Minutes (Earth Engine) | CC-BY 4.0 |
| TESSERA / geotessera | Pre-computed embeddings | 128-d, 10 m embeddings; global for 2024, US/Europe 2017–2025 | ~1 hour | MIT code, CC0 embeddings |
| Major TOM embeddings | Pre-computed embeddings | 56M Sentinel-2 patch embeddings (DINOv2, SSL4EO) and 20M SigLIP embeddings: text-to-image search over the planet | ~1 hour (big parquet files) | CC-BY-SA-4.0 |
| Copernicus-Embed-025deg | Pre-computed embeddings | Global 721×1440×768 embedding map on the ERA5 grid; links the land surface to weather and climate | ~1 hour | CC-BY-4.0 |
| Prithvi-EO-2.0 (+ fine-tunes) | Encoder (MAE ViT, multi-temporal) | Flood, burn-scar, landslide and crop checkpoints/configs ready in TerraTorch | ~1–3 hours (GPU) | Apache-2.0 weights, MIT code |
| TerraMind 1.0 | Generative any-to-any encoder | Generate S1↔S2↔land cover↔DEM; "Thinking-in-Modalities" fine-tuning; Colab notebooks | ~1–3 hours (GPU) | Apache-2.0 |
| OlmoEarth v1–v1.3 | Encoder family (Nano→Large) | S1+S2+Landsat embeddings and fine-tuning; NGO-oriented platform | ~1–3 hours | OlmoEarth Artifact License (use restrictions) |
| Clay v1.5 | Encoder (MAE) | Embeddings for any place and time; similarity search tutorials | ~1–2 hours | Apache-2.0 |
| DINOv3 SAT-493M | Natural-image SSL backbone trained on satellite RGB | Strongest high-res RGB features; canopy height (CHMv2) via HF Transformers | ~1 hour (gated download) | DINOv3 License (custom) |
| Galileo | Encoder (S1, S2, time series, static) | Pixel/patch time-series features; includes a Copernicus data-download GUI | ~1–2 hours | MIT |
| DOFA / DOFA v2 | Wavelength-conditioned encoder | One model for any band count (S1, S2, NAIP, hyperspectral) | ~1 hour (torch.hub, TorchGeo) | MIT code, CC-BY-4.0 weights |
| Copernicus-FM | Encoder for all Sentinels (S1–S5P) | Atmosphere and land in one model; air-quality regression | Hours | Apache-2.0 code, CC-BY-4.0 weights |
| Panopticon | Any-sensor DINOv2-style encoder | Channel-agnostic features via torch.hub; in TorchGeo 0.7+ | ~1 hour | Apache-2.0 |
| SMARTIES | Spectrum-aware multi-sensor encoder | One-line HF Transformers load | ~1 hour | Apache-2.0 |
| AnySat | JEPA multi-resolution encoder | Any of 11 sensors, 0.3–2600 ha tiles, torch.hub one-liner | ~1 hour | MIT |
| Presto | Lightweight pixel time-series transformer | Crop/land-cover from pixel time series on CPU | ~1 hour | MIT |
| Satlas / SatlasPretrain | Pretrained backbones plus AI-generated global products | Global solar farms, wind turbines, offshore platforms and tree cover from Sentinel-2 | Minutes (products) to hours (models) | Apache-2.0 |
| RemoteCLIP / GeoRSCLIP / SkyCLIP | Remote-sensing CLIP | Zero-shot classification and text↔image retrieval over aerial chips | ~30 min (OpenCLIP) | Apache-2.0 / MIT / MIT |
| CROMA | Radar-optical contrastive MAE | Fused SAR+optical features (works under cloud) | ~1 hour | MIT |
| SatMAE / SatMAE++ / Scale-MAE / SpectralGPT / SkySense | Earlier research encoders | Mostly superseded; useful only for paper comparisons | Hours | Mixed (see entries) |
| TerraTorch | Fine-tuning toolkit | No-code `terratorch fit -c config.yaml` for Prithvi, TerraMind, DOFA and others | ~1 hour | Apache-2.0 |
| GEO-Bench-2 / PANGAEA / Copernicus-Bench | Benchmarks | Pick a model with evidence; ready-made evaluation datasets | Hours | Apache-2.0 / GPL-3.0 / CC-BY-4.0 |

### AlphaEarth Foundations / Satellite Embedding V1 (Google DeepMind, July 2025)
- **What it does:** An "embedding field" model that fuses many EO sources into a **64-dimensional vector for every 10 m pixel for each calendar year**, published as the Satellite Embedding dataset `GOOGLE/SATELLITE_EMBEDDING/V1/ANNUAL` in Earth Engine. Bands A00–A63 take values in [-1, 1] and are meant to be used together ([EE catalog](https://developers.google.com/earth-engine/datasets/catalog/GOOGLE_SATELLITE_EMBEDDING_V1_ANNUAL)). DeepMind reports a 24% lower error rate on average than the other models tested, 16× less storage, and "over 1.4 trillion embedding footprints per year" ([DeepMind blog, 30 Jul 2025](https://deepmind.google/discover/blog/alphaearth-foundations-helps-map-our-planet-in-unprecedented-detail/)). The paper claims the embeddings are "the only to consistently outperform" the featurisation approaches tested, without retraining ([arXiv 2507.22291](https://arxiv.org/abs/2507.22291)).
- **Maturity:** Production dataset. The catalog lists availability from 2017-01-01 to 2025-01-01, i.e. annual layers 2017–2024 ([EE catalog](https://developers.google.com/earth-engine/datasets/catalog/GOOGLE_SATELLITE_EMBEDDING_V1_ANNUAL)). License CC-BY 4.0, with the attribution "The AlphaEarth Foundations Satellite Embedding dataset is produced by Google and Google DeepMind." It is also on Google Cloud Storage at `gs://alphaearth_foundations`, which the catalog describes as "provider pays" as of July 2026. Google says it tested the dataset with more than 50 organisations, including FAO, MapBiomas and the Global Ecosystems Atlas ([DeepMind blog](https://deepmind.google/discover/blog/alphaearth-foundations-helps-map-our-planet-in-unprecedented-detail/)). Model weights do not appear to be released; only the embeddings (unverified beyond the blog and catalog pages).
- **Hackathon effort:** **Minutes.** Register a noncommercial Earth Engine Cloud project; per Google, "Earth Engine access is enabled immediately" after registration ([EE access guide](https://developers.google.com/earth-engine/guides/access)). Then use the Code Editor, the Python API or geemap. The default Community tier gives 150 EECU-hours per month, and the Contributor tier gives 1,000 if a billing account is attached (noncommercial use is not charged) ([EE noncommercial tiers](https://developers.google.com/earth-engine/guides/noncommercial_tiers)).
- **Known limitations and complaints:**
  - Polar coverage is limited, and "some large scale swath and data availability artifacts remain" ([EE catalog](https://developers.google.com/earth-engine/datasets/catalog/GOOGLE_SATELLITE_EMBEDDING_V1_ANNUAL)).
  - The data is annual only. A 2026 disease-modelling preprint notes that the layers are static annual composites and miss intra-annual dynamics ([arXiv 2605.10949](https://arxiv.org/pdf/2605.10949), seen in search results).
  - Earth Genome found that averaging embeddings over a tile can wash out small objects, such as a poultry barn that is a small share of the tile ([Earth Genome tech note](https://www.earthgenome.org/blog/quick-tech-note-adapting-alphaearth-embeddings-to-new-workflows), seen in search results).
  - Dimensions are not individually interpretable.
- **Example problem it unlocks:**
  - Year-over-year change detection: the cosine distance between 2018 and 2024 embeddings flags new mines, deforestation, construction or flood damage worldwide.
  - Few-shot mapping: about 20 labelled points plus a k-NN or linear probe gives a map of, for example, informal settlements, solar farms or crop types for a country.
- **Sources:** [EE catalog](https://developers.google.com/earth-engine/datasets/catalog/GOOGLE_SATELLITE_EMBEDDING_V1_ANNUAL), [DeepMind blog](https://deepmind.google/discover/blog/alphaearth-foundations-helps-map-our-planet-in-unprecedented-detail/), [arXiv 2507.22291](https://arxiv.org/abs/2507.22291), [Earth Engine tiers](https://developers.google.com/earth-engine/guides/noncommercial_tiers), [Google Earth AI page](https://ai.google/earth-ai/).

### TESSERA and geotessera (University of Cambridge, CVPR 2026)
- **What it does:** A foundation model that turns Sentinel-1/2 time series into **128-d per-pixel embeddings at 10 m**. The v2 student models output Matryoshka embeddings that can be truncated to 16, 32 or 64 dimensions ([GitHub](https://github.com/ucam-eo/tessera)).
- **Maturity:**
  - tessera: ★767, MIT, last push 2026-08-17.
  - geotessera library: ★361, release v0.11.0 (2026-10-04), MIT ([GitHub](https://github.com/ucam-eo/geotessera)).
  - Embeddings and weights are **CC0**. Coverage is global at 10 m for 2024; US and Europe have 2017–2025, with back-filling to 2017 planned. The badge says CVPR26, while the publications list says "To Appear, CVPR 2026" ([GitHub](https://github.com/ucam-eo/tessera)).
- **Hackathon effort:** **~1 hour** to pull pre-computed tiles with `geotessera`. Generating your own embeddings is not hackathon-feasible: it needs at least 1 TB of storage per 100×100 km, at least 128 GB RAM, about 10 hours per 110×110 km tile, and macOS is not supported for preprocessing ([GitHub](https://github.com/ucam-eo/tessera)).
- **Known limitations and complaints:** The data is annual, and the 10 m resolution suits landscape-scale analysis. v2 embeddings are still rolling out. Checkpoints from different versions are not interchangeable ([GitHub](https://github.com/ucam-eo/tessera)).
- **Example problem it unlocks:** A no-GPU alternative to AlphaEarth outside Earth Engine, which also suits a CC0-licensed open product: crop maps, habitat maps, or canopy-height regression from a few labels.
- **Sources:** [ucam-eo/tessera](https://github.com/ucam-eo/tessera), [ucam-eo/geotessera](https://github.com/ucam-eo/geotessera).

### Major TOM image and embedding datasets (ESA Φ-lab, 2024–2025)
- **What it does:** A standard for terabyte-scale EO datasets on a global 10 km grid, plus official image and embedding sets on Hugging Face ([GitHub](https://github.com/ESA-PhiLab/Major-TOM)):
  - Images:
    - Core-S2L2A: 2,245,886 patches, about 23 TB.
    - Core-S1RTC: 1,469,955 patches, about 16 TB.
    - Core-DEM.
  - Embeddings:
    - Core-S2L1C-SSL4EO: 56,147,150 embeddings, 252.9 GB.
    - Core-S1RTC-SSL4EO: 36,748,875 embeddings, 332.5 GB.
    - Core-S2RGB-DINOv2: 56,147,150 embeddings, 223.1 GB.
    - **Core-S2RGB-SigLIP: 20,212,974 embeddings, 41.3 GB.** SigLIP is text-aligned, so it supports text queries.
- **Maturity:** Repo ★234, Apache-2.0, pushed 2026-10-24. Datasets are CC-BY-SA-4.0. Core-S2L2A had 22,677 dl/30d; Core-S2RGB-SigLIP was updated 2025-12-09 (HF API). There is a browser viewer ([Space](https://huggingface.co/spaces/Major-TOM/MajorTOM-Core-Viewer)) and a paper ([arXiv 2402.12095](https://arxiv.org/abs/2402.12095)).
- **Hackathon effort:** **~1 hour.** Stream a region's parquet shards from HF, build a FAISS index, and use the SigLIP text encoder for queries.
- **Known limitations and complaints:** The sets are large. SigLIP and DINOv2 embeddings are RGB-only, from general-purpose models. The S2 patches are one snapshot per cell, not time series. CC-BY-SA is share-alike.
- **Example problem it unlocks:** "Google for the planet": type "open-pit mine", "airport", "flooded fields" or "solar farm" and get matching Sentinel-2 tiles worldwide. This is an instant, visual demo.
- **Sources:** [ESA-PhiLab/Major-TOM](https://github.com/ESA-PhiLab/Major-TOM), [Major-TOM/Core-S2RGB-SigLIP](https://huggingface.co/datasets/Major-TOM/Core-S2RGB-SigLIP).

### Prithvi-EO-2.0 (IBM + NASA, Dec 2024) and Prithvi-EO-1.0
- **What it does:** A ViT masked-autoencoder with 3D (space-time) patch embeddings and optional time and location ("TL") embeddings. It was pretrained on 4.2M global time-series samples of NASA Harmonized Landsat-Sentinel data. It comes in 300M, 300M-TL, 600M and 600M-TL sizes, and the 600M-TL beats Prithvi-EO-1.0 by 8% on GEO-Bench ([GitHub](https://github.com/NASA-IMPACT/Prithvi-EO-2.0), [arXiv 2412.02732](https://arxiv.org/abs/2412.02732)). TerraTorch configs are provided for:
  - flood (Sen1Floods11)
  - wildfire scar
  - burn intensity
  - landslide (Landslide4Sense)
  - US multi-temporal crops
  - Europe land cover and crops (Sen4Map)
  - above-ground biomass (BioMassters)
- **Maturity:**
  - Repo ★330, MIT, last push 2025-02-13.
  - HF weights are Apache-2.0. Prithvi-EO-2.0-300M had 19,504 dl/30d; Prithvi-EO-1.0-100M has 292 likes.
  - Ready fine-tuned checkpoints include `Prithvi-EO-2.0-300M-TL-Sen1Floods11` (updated 2026-08-25) and `Prithvi-EO-2.0-300M-BurnScars` (HF API).
  - Demo Space: [Prithvi-EO-2.0-Demo](https://huggingface.co/spaces/ibm-nasa-geospatial/Prithvi-EO-2.0-Demo).
- **Hackathon effort:** **~1 hour** to run a ready flood or burn-scar checkpoint on a Sentinel-2/HLS chip. Allow **3+ hours** to fine-tune on a new label set; a GPU is advisable (a Colab T4 works for 300M).
- **Known limitations and complaints:**
  - Inputs must match the HLS band set and normalisation.
  - Gains over U-Nets are dataset-dependent. One comparison surfaced in search found the 300M model best on the full Landslide4Sense set, with results shifting on smaller training subsets (search snippet only; underlying page not opened, unverified — possibly the [GRSS 2026 slides](https://www.grss-ieee.org/wp-content/uploads/2026/08/Day3_1_Benedikt-Blumenstiel.pdf)). PANGAEA-style critiques apply ([arXiv 2412.04204](https://arxiv.org/abs/2412.04204)).
  - The repo has not been pushed since Feb 2025; development moved to TerraTorch.
- **Example problem it unlocks:** Rapid flood-extent or burn-scar mapping for a disaster that happened this week, comparing pre- and post-event HLS scenes.
- **Sources:** [NASA-IMPACT/Prithvi-EO-2.0](https://github.com/NASA-IMPACT/Prithvi-EO-2.0), [HF ibm-nasa-geospatial](https://huggingface.co/ibm-nasa-geospatial), [arXiv 2412.02732](https://arxiv.org/abs/2412.02732).

### TerraMind 1.0 (IBM + ESA Φ-lab + FAST-EO, 2025; ICCV 2025)
- **What it does:** Billed as "the first any-to-any generative foundation model for Earth Observation", in tiny, small, base and large sizes. It can generate one modality from another, such as S2 to S1 SAR, land cover or DEM, using six tokenizers. It also supports "Thinking-in-Modalities" (TiM) fine-tuning, where the model first generates, for example, a land-use/land-cover map as an intermediate step ([GitHub](https://github.com/IBM/terramind), [arXiv 2504.11171](https://arxiv.org/abs/2504.11171)).
- **Maturity:** Repo ★326, Apache-2.0, pushed 2026-10-19. TerraMind-1.0-base had 36,475 dl/30d, and large had 4,130 (HF API, weights Apache-2.0). It is fully integrated into TerraTorch (`pip install "terratorch>=1.2.5"`) and has Colab notebooks for Sen1Floods11, multi-temporal crops, burn scars, generation and large-tile generation ([GitHub](https://github.com/IBM/terramind)). Results from IBM/ESA's TerraMind Blue-Sky Challenge are on HF ([challenge Space](https://huggingface.co/spaces/ibm-esa-geospatial/challenge)).
- **Hackathon effort:** **~1 hour** for the generation Colab, i.e. a "make me a SAR image from this optical image" demo. Fine-tuning takes **2–3 hours** via `terratorch fit -c <config>` ([GitHub](https://github.com/IBM/terramind)).
- **Known limitations and complaints:**
  - The README warns Mac users that "the UNetDecoder can lead to some failures because of the batch norms when training on MPS". Pins such as `diffusers==0.30.0` and `setuptools<81` are needed ([GitHub](https://github.com/IBM/terramind)).
  - Christopher Ren's critique: on PANGAEA, TerraMind-L averages only about +1.9 mIoU over a supervised U-Net and wins 4 of 9 tasks. It notes the U-Net encoder was trainable while the FM encoders were frozen; an IBM-affiliated commenter replied that the gain is about 4% ([Applied Geospatial Substack, 21 May 2025](https://christopherren.substack.com/p/geospatial-foundational-disappointments)).
  - Generated SAR or DEM outputs are plausible-looking but synthetic. Do not present them as measurements.
- **Example problem it unlocks:** Cloud-gap filling, i.e. synthesising a radar view or a land-cover map when optical imagery is cloudy during a flood. Or one model fine-tuned on S1+S2 for all-weather flood mapping.
- **Sources:** [IBM/terramind](https://github.com/IBM/terramind), [HF TerraMind-1.0-base](https://huggingface.co/ibm-esa-geospatial/TerraMind-1.0-base), [arXiv 2504.11171](https://arxiv.org/abs/2504.11171), [Substack critique](https://christopherren.substack.com/p/geospatial-foundational-disappointments).

### OlmoEarth (Ai2, v1 Nov 2025 → v1.3 Oct 2026)
- **What it does:** A family of multimodal, spatio-temporal encoders trained on Sentinel-2, Sentinel-1 and Landsat plus six derived maps: OpenStreetMap, WorldCover, USDA CDL, SRTM, WRI canopy height and WorldCereal ([GitHub](https://github.com/allenai/olmoearth_pretrain)). It is the backbone of the OlmoEarth Platform, which is aimed at non-profits and NGOs.
- **Versions** ([changelog](http://docs.olmoearth.allenai.org/changelog/)):
  - v1 (4 Nov 2025): Nano 1.4M, Tiny 6.2M, Base 89M and Large 308M encoder parameters.
  - v1.1 (May 2026): up to 3× less compute.
  - v1.2 (June 2026): RoPE positional embeddings and a new Small 35.6M model.
  - **v1.3 (Oct 2026): embeddings-focused, with an attention pooler and a 768→128-d distillation head.**
- **Benchmarks:** The paper reports OlmoEarth best on 15 of 24 tasks with frozen embeddings and 19 of 29 with full fine-tuning, against 12 other FMs ([arXiv 2511.13655](https://arxiv.org/abs/2511.13655)).
- **Maturity:** olmoearth_pretrain ★345, pushed 2026-10-24, release v0.1.2 (2026-09-16). OlmoEarth-v1_2-Base had 19,215 dl/30d (HF API). Companion tools: rslearn (★94, Apache-2.0, v0.1.18, 2026-10-14) and olmoearth_projects (★87).
- **License:** The **OlmoEarth Artifact License** forbids use for "any military and defense-related applications", "intelligence gathering, or human surveillance and policing", and "extractive activities… oil, natural gas and minerals… drilling, mining, and deforestation". The restrictions must be passed on downstream ([LICENSE](https://github.com/allenai/olmoearth_pretrain/blob/main/LICENSE)).
- **Hackathon effort:** **~1–2 hours**. Python 3.12 and `uv sync --locked`, then follow the Inference Quickstart. Tutorials cover embeddings and segmentation fine-tuning ([GitHub](https://github.com/allenai/olmoearth_pretrain)).
- **Known limitations and complaints:** The license rules out pitches about mining, oil and gas, or defense, so check the use case. The software is young (v0.1.x) and the Platform is NGO-oriented; how to get access was not verified.
- **Example problem it unlocks:** NGO-style monitoring such as mangrove loss, crop-type maps for food security, or wildfire fuel mapping, using a small model (Nano or Tiny) that runs on CPU.
- **Sources:** [allenai/olmoearth_pretrain](https://github.com/allenai/olmoearth_pretrain), [OlmoEarth changelog](http://docs.olmoearth.allenai.org/changelog/), [arXiv 2511.13655](https://arxiv.org/abs/2511.13655), [HF OlmoEarth-v1_2-Base](https://huggingface.co/allenai/OlmoEarth-v1_2-Base).

### Clay Foundation Model v1.5 (Clay / Renaissance Philanthropy)
- **What it does:** A ViT MAE "foundational model of Earth" for embeddings, fine-tuning and use as a backbone ([HF card](https://huggingface.co/made-with-clay/Clay)). Tutorials cover embedding exploration, Chesapeake segmentation, EuroSAT classification, BioMassters regression and an embeddings-database workflow ([docs](https://clay-foundation.github.io/model/)).
- **Maturity:** Repo ★622, Apache-2.0 for code and weights, pushed 2026-05-11. The last GitHub release is v1.0.1 (2025-07-05), while the docs list **v1.5** as the latest model ([docs](https://clay-foundation.github.io/model/)). HF `made-with-clay/Clay` had only 171 dl/30d. v0 embeddings are on Source Cooperative under ODC-BY ([HF card](https://huggingface.co/made-with-clay/Clay)).
- **Hackathon effort:** **~1–2 hours** (`pip install git+https://github.com/Clay-foundation/model.git`). The README notes the environment "has been tested on Linux devices with CUDA GPUs" ([GitHub](https://github.com/Clay-foundation/model)).
- **Known limitations and complaints:** Downloads are low compared with Prithvi and TerraMind, so the community is smaller. The release numbering is confusing (v1.0.1 on GitHub vs v1.5 in the docs). GEO-Bench-2 still finds Clay competitive on multispectral tasks ([arXiv 2511.15658](https://arxiv.org/abs/2511.15658)).
- **Example problem it unlocks:** "Find more places like this" similarity search over a region, e.g. illegal airstrips or new quarries.
- **Sources:** [Clay-foundation/model](https://github.com/Clay-foundation/model), [docs](https://clay-foundation.github.io/model/), [HF card](https://huggingface.co/made-with-clay/Clay).

### DINOv3 with the SAT-493M satellite backbones (Meta, Aug 2025) and CHMv2 (Mar 2026)
- **What it does:** Meta's self-supervised vision backbones, including a **ViT-L/16 distilled (300M)** and a **ViT-7B/16 (6,716M)** pretrained on a 493M-image satellite dataset (SAT-493M) ([GitHub](https://github.com/facebookresearch/dinov3)). Built on it:
  - **Canopy Height Maps v2 (CHMv2)** model, released 2026-03-10, available in HF Transformers ([HF](https://huggingface.co/facebook/dinov3-vitl16-chmv2-dpt-head), [arXiv 2603.06382](https://arxiv.org/abs/2603.06382)).
  - A metadata-guided training branch "FINO" with FMoW satellite recipes, released 2026-06-12 ([arXiv 2606.05107](https://arxiv.org/abs/2606.05107)).
- **Maturity:** dinov3 ★11,623, pushed 2026-07-15. The license is the custom "DINOv3 License". HF `dinov3-vitl16-pretrain-sat493m` is **gated (manual approval)** and had 44,861 dl/30d (HF API). Supported in Transformers ≥4.56.0.
- **Hackathon effort:** **~1 hour** once access is approved. Request access at the start of the hackathon, because approval is manual.
- **Known limitations and complaints:** RGB only, so no multispectral or SAR. The license is custom. GEO-Bench-2 finds DINOv3 among the best on high-resolution tasks but weaker than EO-specific models on multispectral tasks ([arXiv 2511.15658](https://arxiv.org/abs/2511.15658)).
- **Example problem it unlocks:** Tree height and carbon estimates from RGB imagery (CHMv2), or dense features for zero-shot segmentation of high-resolution imagery (NAIP, Maxar Open Data).
- **Sources:** [facebookresearch/dinov3](https://github.com/facebookresearch/dinov3), [HF dinov3-vitl16-pretrain-sat493m](https://huggingface.co/facebook/dinov3-vitl16-pretrain-sat493m).

### Galileo (NASA Harvest and collaborators, 2025)
- **What it does:** A family of pretrained remote-sensing encoders for multimodal, multi-temporal inputs, with space-time, space-only, time-only and static band groups ([GitHub](https://github.com/nasaharvest/galileo), [arXiv 2502.09356](https://arxiv.org/abs/2502.09356)). It ships a single-file encoder and a marimo app for visualising embeddings. It also includes a **Copernicus marimo GUI** to search and download Sentinel-1/2 with a free CDSE account, with a time slider and GeoTIFF export.
- **Maturity:** ★203, MIT, pushed 2026-04-21, no GitHub release.
- **Hackathon effort:** **~1–2 hours.** Inputs must be assembled into its `MaskedOutput` structure, though a helper `construct_galileo_input` exists ([GitHub](https://github.com/nasaharvest/galileo)).
- **Known limitations and complaints:** The input schema is complex, and weights load from a local folder (`models/nano`).
- **Example problem it unlocks:** Pixel time-series crop or flood classification. The bundled Copernicus GUI alone is useful for any team needing S1/S2 downloads.
- **Sources:** [nasaharvest/galileo](https://github.com/nasaharvest/galileo).

### DOFA and DOFA v2 (TUM zhu-xlab, 2024–2025)
- **What it does:** A "Dynamic One-For-All" encoder whose patch embedding is conditioned on each band's **wavelength**, so one model ingests any number of channels (S1 SAR, S2, NAIP RGB-NIR, hyperspectral). It loads via `torch.hub.load('zhu-xlab/DOFA','vit_base_dofa', pretrained=True)` or through TorchGeo (`dofa_base_patch16_224`). TerraTorch has detection and instance-segmentation examples ([GitHub](https://github.com/zhu-xlab/DOFA), [arXiv 2403.15356](https://arxiv.org/abs/2403.15356)).
- **Maturity:** ★216, MIT, pushed 2026-07-22. HF weights `earthflow/DOFA` are CC-BY-4.0 (HF API).
- **Hackathon effort:** **~1 hour.**
- **Known limitations and complaints:** You must supply band wavelengths. A `timm==0.9.2` pin is needed for hub loading, and the README warns that the new weights need the new `wave_dynamic_layer.py` ([GitHub](https://github.com/zhu-xlab/DOFA)).
- **Example problem it unlocks:** Fusing a new or unusual sensor, e.g. EMIT hyperspectral or Landsat thermal, with Sentinel data without training a new model.
- **Sources:** [zhu-xlab/DOFA](https://github.com/zhu-xlab/DOFA).

### Copernicus-FM, Copernicus-Pretrain, Copernicus-Bench and Copernicus-Embed-025deg (TUM et al., ICCV 2025 oral)
- **What it does:**
  - **Copernicus-FM** extends DOFA with dynamic hypernetworks and metadata encoding so it can handle any spectral or non-spectral modality from **all Sentinels (S1–S5P)**.
  - **Copernicus-Pretrain** is 18.7M aligned images on about 310K grid cells of 0.25°.
  - **Copernicus-Bench** has 15 tasks, including Sentinel-3 cloud, S5P NO₂ and O₃ air-quality regression, and Kuro Siwo flood.
  - **Copernicus-Embed-025deg** is a global 721×1440×768 embedding map on the ERA5 grid ([GitHub](https://github.com/zhu-xlab/Copernicus-FM), [arXiv 2503.11849](https://arxiv.org/abs/2503.11849)).
- **Maturity:** ★151, pushed 2025-10-02. Code is Apache-2.0; weights, the pretrain set and the new benchmark sets are CC-BY-4.0 ([GitHub](https://github.com/zhu-xlab/Copernicus-FM)).
- **Hackathon effort:** **~1 hour** for the embedding map (a single HF dataset). **Hours** for the model itself.
- **Known limitations and complaints:** It is research code. HF reported 0 dl/30d for the weights, so it is rarely used in practice.
- **Example problem it unlocks:** Using surface embeddings as extra predictors for weather or air-quality models, e.g. "which regions' NO₂ is anomalous given their land surface?".
- **Sources:** [zhu-xlab/Copernicus-FM](https://github.com/zhu-xlab/Copernicus-FM), [HF Copernicus-Embed-025deg](https://huggingface.co/datasets/wangyi111/Copernicus-Embed-025deg).

### Panopticon (2025; EarthVision CVPR 2025 best paper)
- **What it does:** An any-sensor encoder based on DINOv2 that takes per-channel wavelength IDs (SAR channels get special IDs), loaded with `torch.hub.load('Panopticon-FM/panopticon','panopticon_vitb14')`. It was added to TorchGeo 0.7 ([GitHub](https://github.com/Panopticon-FM/panopticon), [arXiv 2503.10845](https://www.arxiv.org/abs/2503.10845)).
- **Maturity:** ★48, Apache-2.0, pushed 2025-10-03. The evaluation code was refactored into "Geobreeze".
- **Hackathon effort:** **~1 hour.**
- **Known limitations and complaints:** A small community. Best results need 224×224 inputs and standard normalisation, per the README.
- **Example problem it unlocks:** Same as DOFA: one encoder for a mix of sensors.
- **Sources:** [Panopticon-FM/panopticon](https://github.com/Panopticon-FM/panopticon).

### SMARTIES (ICCV 2025)
- **What it does:** A spectrum-aware multi-sensor autoencoder that projects bands from any sensor into a shared spectrum-aware space. It handles optical (S2), radar (S1) and sub-meter RGB, including unseen sensors zero-shot. Since July 2025 it loads in one line via the HF Transformers interface ([GitHub](https://github.com/gsumbul/SMARTIES), [arXiv 2506.19585](https://arxiv.org/abs/2506.19585)).
- **Maturity:** ★25, Apache-2.0, pushed 2025-07-08. Weights: SMARTIES-v1-ViT-B and ViT-L on HF.
- **Hackathon effort:** **~1 hour.**
- **Known limitations and complaints:** Very small community. Training uses wandb by default.
- **Example problem it unlocks:** Mixing commercial high-resolution RGB with Sentinel-2 in one pipeline.
- **Sources:** [gsumbul/SMARTIES](https://github.com/gsumbul/SMARTIES).

### AnySat (CVPR 2025 Highlight)
- **What it does:** A scale-adaptive JEPA trained on "GeoPlex" (5 datasets, 11 sensors). It handles 3–11 channels and tiles from 0.3 to 2,600 ha, and loads with `torch.hub.load('gastruc/anysat','anysat', pretrained=True, flash_attn=False)` ([GitHub](https://github.com/gastruc/AnySat), [arXiv 2412.14123](https://arxiv.org/abs/2412.14123)).
- **Maturity:** ★218, MIT, pushed 2025-10-16.
- **Hackathon effort:** **~1 hour** (demo notebook).
- **Known limitations and complaints:** Mostly trained on European datasets (unverified).
- **Example problem it unlocks:** Tree-species, crop-type or land-cover maps from mixed-resolution inputs.
- **Sources:** [gastruc/AnySat](https://github.com/gastruc/AnySat).

### Presto (NASA Harvest, 2023)
- **What it does:** A lightweight transformer for **pixel-level remote-sensing time series** (S1, S2, ERA5, DEM, etc.), with a single-file version and a demo notebook ([GitHub](https://github.com/nasaharvest/presto), [arXiv 2304.14065](https://arxiv.org/abs/2304.14065)).
- **Maturity:** ★285, MIT, pushed 2026-06-10.
- **Hackathon effort:** **~1 hour.** Small enough for CPU.
- **Known limitations and complaints:** Pixel time series only, with no spatial context.
- **Example problem it unlocks:** Crop-type mapping, or "is this field irrigated?", over a farm region.
- **Sources:** [nasaharvest/presto](https://github.com/nasaharvest/presto).

### Satlas and SatlasPretrain (Ai2, 2023–)
- **What it does:**
  - **SatlasPretrain:** 302M labels in 137 categories (ICCV 2023), with pretrained backbones in `satlaspretrain_models`.
  - **Satlas data products:** AI-generated global layers computed from Sentinel-2 and updated monthly, e.g. solar farms, wind turbines, offshore platforms and tree cover ([GitHub](https://github.com/allenai/satlas)).
  - Global super-resolution outputs (see §3).
- **Maturity:** satlas ★287, Apache-2.0, pushed 2026-03-27. satlaspretrain_models ★155, last push 2024-10-24 (stale).
- **Hackathon effort:** **Minutes** to download the product GeoJSONs ([GeospatialDataProducts.md](https://github.com/allenai/satlas/blob/main/GeospatialDataProducts.md)). **Hours** for the models.
- **Known limitations and complaints:** The model repo is no longer active. Product update cadence after 2024 was not verified.
- **Example problem it unlocks:** "Where is offshore wind being built, and how fast?", or solar-farm growth by country.
- **Sources:** [allenai/satlas](https://github.com/allenai/satlas), [allenai/satlaspretrain_models](https://github.com/allenai/satlaspretrain_models).

### Remote-sensing CLIPs: RemoteCLIP, GeoRSCLIP (RS5M), SkyCLIP (SkyScript)
- **What it does:** CLIP models tuned on aerial and satellite image-text pairs for zero-shot classification, text↔image retrieval and counting.
  - RemoteCLIP checkpoints are OpenCLIP-compatible. They beat prior SOTA by 9.14% mean recall on RSICD and CLIP by up to 6.39% on zero-shot classification across 12 datasets. An Autodistill plugin allows auto-labelling ([GitHub](https://github.com/ChenDelong1999/RemoteCLIP)).
- **Maturity:**
  - RemoteCLIP: ★599, Apache-2.0, last push 2024-06-27.
  - RS5M/GeoRSCLIP: ★321, MIT, last push 2025-03-17.
  - SkyScript/SkyCLIP: ★212, MIT, last push 2024-12-10.
  - None has seen major updates since 2024.
- **Hackathon effort:** **~30 minutes** (`open_clip` plus a checkpoint download).
- **Known limitations and complaints:** RGB only and trained on chips. Counting and small objects are weak (the same failure family as the VLM results in §2). Now overshadowed by SigLIP-style general models.
- **Example problem it unlocks:** A text-search box over your own imagery tiles ("ships in harbour", "burned area").
- **Sources:** [RemoteCLIP](https://github.com/ChenDelong1999/RemoteCLIP), [RS5M](https://github.com/om-ai-lab/RS5M), [SkyScript](https://github.com/wangzhecheng/SkyScript).

### CROMA (NeurIPS 2023)
- **What it does:** A contrastive radar-optical masked autoencoder for paired Sentinel-1 (2 channels) and Sentinel-2 (12 channels) at a default size of 120×120 px. The author aims to be "noob-friendly"; weights are on HF `antofuller/CROMA` ([GitHub](https://github.com/antofuller/CROMA)).
- **Maturity:** ★59, MIT, last push 2024-01-10.
- **Hackathon effort:** **~1 hour.**
- **Known limitations and complaints:** Stale. Requires both S1 and S2 inputs to be preprocessed the same way as in pretraining.
- **Example problem it unlocks:** Mapping under persistent cloud (tropics, monsoon floods) with SAR+optical fusion.
- **Sources:** [antofuller/CROMA](https://github.com/antofuller/CROMA).

### Earlier research encoders: SatMAE, SatMAE++, Scale-MAE, SpectralGPT, SkySense and SkySense++, SSL4EO-S12
- **SatMAE** (NeurIPS 2022): ★265, last push 2025-08-10, no SPDX license ([GitHub](https://github.com/sustainlab-group/SatMAE)). **SatMAE++** (CVPR 2024): ★134, Apache-2.0 ([GitHub](https://github.com/techmn/satmae_pp)). **Scale-MAE** (ICCV 2023): ★173, last push 2024-02-17 ([GitHub](https://github.com/bair-climate-initiative/scale-mae)). These are FMoW-era encoders; use them only for comparison.
- **SpectralGPT** (TPAMI 2024): ★283, **no license file**. Pretrained on 8× RTX 4090, and some data is hosted on Baidu Pan ([GitHub](https://github.com/danfenghong/IEEE_TPAMI_SpectralGPT)). Hackathon value is low.
- **SkySense** (Ant Group + Wuhan University, CVPR 2024): checkpoints via a Notion link. **SkySense++** was published in *Nature Machine Intelligence* (Aug 2025), with code and weights in a separate repo (kang-wu/SkySensePlusPlus). It requires an old stack (Python 3.8, PyTorch 1.13.1, MMCV 1.7.1, GDAL 3.4.0). ★90, no SPDX license ([GitHub](https://github.com/Jack-bo1220/SkySense)). Expect **hours** of environment setup.
- **SSL4EO-S12** (TUM): dataset plus ResNet/ViT weights for S1/S2. ★301, Apache-2.0, last push 2024-04-20 ([GitHub](https://github.com/zhu-xlab/SSL4EO-S12)). Its weights power the Major TOM SSL4EO embeddings.

### TerraTorch (IBM → torchgeo org) — the fine-tuning harness
- **What it does:** A PyTorch Lightning plus TorchGeo toolkit for fine-tuning GFMs (Prithvi, TerraMind, DOFA and others) with YAML configs and CLI commands `terratorch fit/test/predict`. It "provides tools for fine-tuning and using pretrained models. No models are hosted by TerraTorch", and checking model licenses is the user's responsibility ([GitHub](https://github.com/torchgeo/terratorch)).
- **Maturity:** ★877, Apache-2.0, release v1.2.13 (2026-09-16), pushed 2026-10-22. The repo moved from IBM/terratorch to torchgeo/terratorch (GitHub API redirect). An HPO/NAS companion tool, "Iterate", is available.
- **Hackathon effort:** **~1 hour** to run an existing config. Sample configs in the Prithvi and TerraMind repos cover flood, burn scar, crops, landslide and biomass.
- **Known limitations and complaints:** Version pins matter (TerraMind needs ≥1.2.5). There are Mac MPS caveats (see TerraMind).
- **Example problem it unlocks:** Any segmentation task with labelled GeoTIFFs, with no training code to write.
- **Sources:** [torchgeo/terratorch](https://github.com/torchgeo/terratorch).

### Benchmarks and what they say
- **GEO-Bench-2** (AI Alliance with IBM, ServiceNow and TUM; arXiv Nov 2025, v2 Feb 2026). The paper describes 19 permissively licensed datasets across classification, segmentation, regression, detection and instance segmentation. The repo lists 17 datasets: benv2, biomassters, burn_scars, caffe, cloudsen12, dynamic_earthnet, everwatch, flair2, forestnet, fotw, kuro_siwo, pastis, spacenet2, spacenet7, substation, treesatai and so2sat. Install with `pip install GeoBenchV2`. Findings ([arXiv 2511.15658](https://arxiv.org/abs/2511.15658)):
  - "No single model dominates across all tasks".
  - ConvNeXt (ImageNet) and DINOv3 are best on high-resolution tasks.
  - TerraMind, Prithvi and Clay win on multispectral agriculture and disaster response.

  The leaderboard is an HF Space ([leaderboard](https://huggingface.co/spaces/aialliance/GEO-Bench-2-Leaderboard)); its contents were not readable via fetch. See also the [GitHub repo](https://github.com/The-AI-Alliance/GEO-Bench-2) and [site](https://the-ai-alliance.github.io/GEO-Bench-2/).
- **GEO-Bench v1** (ServiceNow): ★195, Apache-2.0, release v1.1.0 (2026-09-28). The README itself says "We recommend using GEO-Bench-2 instead" and flags a band-labelling issue in m-eurosat and m-brick-kiln ([GitHub](https://github.com/ServiceNow/geo-bench)).
- **PANGAEA** (Marsocci et al.; v2 Apr 2025): ★290, GPL-3.0. It finds GFMs "do not consistently outperform supervised models" like U-Net, and that existing benchmarks are geographically biased toward North America and Europe ([arXiv 2412.04204](https://arxiv.org/abs/2412.04204), [GitHub](https://github.com/VMarsocci/pangaea-bench)).
- **Copernicus-Bench**: 15 tasks across S1, S2, S3 and S5P (see the Copernicus-FM entry).
- **Critiques to quote in a pitch about the "foundation-model gap"** ([Substack](https://christopherren.substack.com/p/geospatial-foundational-disappointments)). Ren argues that:
  - most GFMs were trained on about 0.1 tokens per parameter;
  - TerraMind's roughly 10²¹ FLOPs bought only about a 3–4% relative mIoU gain;
  - pixel-reconstruction objectives do not teach boundaries or classes;
  - integration friction (tiling and stitching, GPUs) blocks adoption;
  - practitioners should "keep a tuned U-Net as the default baseline".

  Those are the author's estimates. A 2026 preprint surfaced in search also concludes there is "not a single winner" and that results need dataset-level characterisation (exact paper unverified; candidate [arXiv 2602.10720](https://arxiv.org/abs/2602.10720v1) from the same search). A 2026 ecological study (also search-only, unverified) reports TerraMind marginally beating Prithvi, and clearly beating ResNet/Prithvi once extra modalities are added.

## 2. Vision-language and LLM geospatial models and agents

**State of play (Oct 2026).** There are three layers.

1. **Frontier general models with vision** (Grok, GPT, Gemini, Claude). They are excellent at captions, scene description and world-knowledge reasoning ("this looks like a port in the Gulf"). Every benchmark finds them **bad at counting, localising (bounding boxes), small objects, change detection and anything non-RGB**:
   - "Good at captioning, bad at counting" ([arXiv 2401.17600](https://arxiv.org/abs/2401.17600)).
   - GPT-4V's visual-grounding Acc@0.5 on VRSBench is **5.1%**, against 49.8% for the small remote-sensing model GeoChat ([VRSBench README](https://github.com/lx709/VRSBench)).
   - The best model on GEOBench-VLM reaches "only 41.7% accuracy on MCQs" ([arXiv 2411.19325](https://arxiv.org/abs/2411.19325)).
2. **Remote-sensing-tuned open VLMs** (GeoChat, EarthDial, TEOChat, LHRS-Bot, SkyEyeGPT, EarthGPT, GeoPixel). They are better at grounding and remote-sensing VQA, but most are 2024-era LLaVA derivatives, need a GPU, and have stale code.
3. **Agent and copilot systems** that call geospatial tools: Google Earth AI's Geospatial Reasoning, Microsoft's Planetary Explorer (formerly NASA Earth Copilot), GeoLLM-Engine, and MCP-exposed toolkits.

**The winning hackathon pattern is layer 3 built by hand**: a frontier LLM such as Grok orchestrating specialist tools (STAC search, SAM/YOLO, embeddings, weather APIs). Do not ask the LLM to count ships from pixels.

### Quick-pick (VLMs and agents)

| Tool | Category | What it unlocks | Effort | License |
|---|---|---|---|---|
| Grok API (grok-4.7 etc.) | Frontier LLM with image input and server-side tools | Image Q&A, web/X search, code execution, collections (RAG); OpenAI-compatible | Minutes | Commercial API |
| GPT / Gemini / Claude vision APIs | Frontier LLMs | Same pattern; useful as cross-checks | Minutes | Commercial API |
| Google Earth AI / Geospatial Reasoning | Hosted geospatial agent and models | Gemini plus imagery, population, weather models (experimental, interest form) | Days (access) | Proprietary |
| Planetary Explorer (formerly NASA Earth Copilot) | Open-source multi-agent geospatial chat (Azure) | Chat-to-map over Planetary Computer STAC; MCP tools | Hours (Azure deploy) | MIT |
| GeoLLM-Engine | Research environment for geospatial copilots | Half a million multi-tool tasks over 1.1M images for evaluating agents | Hours | See paper |
| GeoChat | RS VLM (LLaVA-1.5, 7B) | Grounded RS chat, region captions, boxes | ~2–3 hours (GPU) | Apache-2.0 weights (HF) |
| GeoPixel | RS pixel-grounding LMM (7B) | Masks from language on high-resolution imagery up to 4K | ~2–3 hours (GPU) | Apache-2.0 |
| EarthDial | RS VLM (4B, RGB/MS/SAR/methane/UHI variants) | Multi-sensor dialogue incl. methane and urban heat | ~2–3 hours (GPU) | MIT code |
| TEOChat | Temporal EO VLM (ICLR 2025) | Change questions over image sequences; HF demo | ~1 hour (demo) to hours | Apache-2.0 |
| LHRS-Bot / LHRS-Bot-Nova / ScoreRS | RS MLLM (ECCV 2024) | RS VQA; LHRS-Bench | Hours | Apache-2.0 code |
| SkyEyeGPT, EarthGPT | RS MLLMs | Research baselines; datasets (SkyEye-968k, MMRS-1M) | Hours | Unclear |
| VRSBench, GEOBench-VLM, XLRS-Bench, VLEO-Bench | Benchmarks | Evidence for the "LLMs can't count from orbit" problem framing | Minutes (read) | CC-BY-4.0 / various |

### Grok API (xAI) — image understanding and agentic tools
- **What it does:** Chat and reasoning models that accept images. The Responses API takes `input_image` items as a URL or base64, in JPG/PNG up to **20 MiB per image**, with no stated limit on images per request ([image understanding guide](https://docs.x.ai/docs/guides/image-understanding)). It is **OpenAI-SDK compatible** via `base_url="https://api.x.ai/v1"`. Server-side tools are **Web Search, X Search, Code Execution (`code_interpreter`), Image Generation and Collections Search** over uploaded documents ([tools overview](https://docs.x.ai/docs/guides/tools/overview)). The official Python SDK `xai-sdk` is gRPC-based and supports image understanding, image and video generation, and agentic tool calling ([GitHub](https://github.com/xai-org/xai-sdk-python), ★590, Apache-2.0, v1.21.0 released 2026-10-23).
- **Maturity and pricing** (models page, 2026-10-24):
  - **grok-4.7** (recommended, 500k context): $2.00 input / $6.00 output per 1M tokens below 200k context.
  - grok-4.3 and grok-4.20-0309 variants (1M context): $1.25 / $2.50.
  - grok-build-0.1: $1.00 / $2.00.
  - Image generation: grok-imagine-image at $0.02/image, quality tier at $0.05.
  - Video generation: grok-imagine-video at $0.05/s ([models page](https://docs.x.ai/docs/models)).
  - Rate limits: grok-4.7 allows 150 RPS and 50M TPM at Tier 0. Tiers unlock with cumulative spend since 1 Jan 2026. The docs mention no free credits ([rate limits](https://docs.x.ai/docs/key-information/consumption-and-rate-limits)).
  - The Cal Hacks starter pack says attendees get **one month of X Premium "which includes Cursor, Grok Bot, X and Grok"**. Whether that includes API credits is not stated (starter pack PDF in `docs/`).
- **Hackathon effort:** **Minutes.** Swap the base URL in any OpenAI client.
- **Known limitations and complaints:**
  - The docs give no image-token pricing and do not explain the `detail` parameter ([guide](https://docs.x.ai/docs/guides/image-understanding)). They warn that storing conversation history server-side "may cause image requests to fail", and the SDK lists a `DATA_LOSS` error for image URLs that cannot be fetched ([SDK README](https://github.com/xai-org/xai-sdk-python)).
  - No published remote-sensing benchmark of Grok was found. Expect the same failure modes as other frontier VLMs (see below); this is unverified for Grok specifically.
- **Example problem it unlocks:** An analyst copilot.
  - Grok plans a query and calls your tools: STAC search, YOLO-OBB ship counts, AlphaEarth change scores.
  - It explains results in plain language, and X Search pulls real-time posts about the event (a flood, a launch, a fire) to cross-check against what the satellite shows.
  - Using X Search is a natural fit for the "bonus points for Grok" rule.
- **Sources:** [docs.x.ai models](https://docs.x.ai/docs/models), [image understanding](https://docs.x.ai/docs/guides/image-understanding), [tools](https://docs.x.ai/docs/guides/tools/overview), [rate limits](https://docs.x.ai/docs/key-information/consumption-and-rate-limits), [xai-sdk-python](https://github.com/xai-org/xai-sdk-python).

### GPT, Gemini and Claude vision APIs (OpenAI, Google, Anthropic)
- **What it does:** General multimodal LLMs with image input. Gemini is also wired into Google's Earth AI stack (below).
- **Maturity:** Production APIs. Current model names and prices were not re-verified for this report (unverified). Google's Gemini API rate-limit page says limits are per project, not per key, and that free tier limits are shown in AI Studio ([Gemini rate limits](https://ai.google.dev/gemini-api/docs/rate-limits)).
- **Hackathon effort:** Minutes.
- **Known limitations and complaints (evidence from remote-sensing benchmarks):**
  - **VLEO-Bench (GPT-4V):** "strong performance on open-ended tasks such as location understanding and image captioning", but "poor spatial reasoning limits usefulness on object localization and counting tasks" ([arXiv 2401.17600](https://arxiv.org/abs/2401.17600)).
  - **VRSBench:** GPT-4V gets **5.1% Acc@0.5** on visual grounding, versus 49.8% for GeoChat and 41.6% for LLaVA-1.5. GPT-4V has the highest CLAIR caption score (0.83) but only 65.6% on VQA, versus 76–78% for fine-tuned open models ([VRSBench README](https://github.com/lx709/VRSBench)).
  - **GEOBench-VLM** (10,000+ manually verified instructions): the best model, LLaVA-OneVision, reaches "only 41.7% accuracy on MCQs", slightly above GPT-4o and about double random. The named hard areas are temporal change detection, large-scale counting, tiny objects and relationships between entities ([arXiv 2411.19325](https://arxiv.org/abs/2411.19325)).
  - **XLRS-Bench** (images averaging 8500×8500 px; CVPR 2025): "further efforts are needed for real-world RS applications" ([arXiv 2503.23771](https://arxiv.org/abs/2503.23771)).
- **Example problem it unlocks:** Natural-language reports, triage of which images need a human, and captioning tiles for search. These are not measurements.
- **Sources:** as cited.

### Google Earth AI and Geospatial Reasoning (Google, 2025–2026)
- **What it does:** An umbrella for Google's geospatial models, in three families:
  - **Imagery:** AlphaEarth Foundations, ForestCast deforestation-risk forecasting, Natural Forests of the World, Open Buildings, and "Aerial & Satellite Insights".
  - **Population:** Population Dynamics Foundation Model and embeddings, Mobility AI.
  - **Environment and weather:** WeatherNext, the Weather Lab cyclone model, Flood Hub, Groundsource flash-flood prediction, SpeciesNet, NeuralGCM, and the Air Quality and Pollen APIs.

  On top sits **Geospatial Reasoning**, "an experimental agent" that links these capabilities to custom agents or Cloud workflows in Gemini ([Google Earth AI](https://ai.google/earth-ai/)).
- **Maturity and access:**
  - Geospatial Reasoning and the planetary prediction engine are **experimental, by interest form**.
  - Imagery search in Google Earth is limited to Professional / Professional Advanced users in the US.
  - Google's Remote Sensing Foundation Models are available only to **Planet and Airbus via a trusted-tester programme**.
  - WeatherNext 3 is listed for enterprise use ([Google Earth AI](https://ai.google/earth-ai/)).
- **Hackathon effort:** Not accessible in 36 hours, except for the parts already public: AlphaEarth embeddings in Earth Engine, WeatherNext in Earth Engine/BigQuery or via Open-Meteo (see §4), the Maps Platform APIs, and Open Buildings.
- **Known limitations and complaints:** Most of it is gated.
- **Example problem it unlocks:** Use the public pieces to build your own small "geospatial reasoning" agent; that is the pitch.
- **Sources:** [ai.google/earth-ai](https://ai.google/earth-ai/).

### Planetary Explorer (formerly NASA Earth Copilot; Microsoft)
- **What it does:** An open-source multi-agent app that "turns natural-language questions into grounded geospatial answers". It covers:
  - STAC chat-to-map over **Microsoft Planetary Computer's 130+ public collections** and MPC Pro.
  - Fabric lakehouses and Azure AI Search for grounding docs.
  - Foundry LLMs plus weather models (Aurora, NVIDIA Earth-2 FCN, MAI Weather).
  - Front ends: a React app, a Teams bot, an M365 Copilot agent, and **every agent exposed as MCP tools** for VS Code and Claude Desktop.

  Satya Nadella introduced NASA Earth Copilot, its inspiration, at Ignite 2024 ([GitHub](https://github.com/microsoft/Planetary-Explorer)). The old `microsoft/Earth-Copilot` path now redirects to this repo (GitHub API).
- **Maturity:** ★200, MIT, pushed 2026-09-10. "It is not a supported Microsoft product" ([GitHub](https://github.com/microsoft/Planetary-Explorer)).
- **Hackathon effort:** **Hours**, plus an Azure subscription. Deployment uses Bicep and GitHub Actions, "within one hour" per the README. The architecture is worth copying even if you do not deploy it.
- **Known limitations and complaints:** Heavily tied to Azure (AI Foundry, Agent Service, Fabric).
- **Example problem it unlocks:** "Show coastal land-cover change in California" → an STAC query, a rendered map and an explanation. Reuse its prompt and agent patterns with Grok and the public Planetary Computer STAC API.
- **Sources:** [microsoft/Planetary-Explorer](https://github.com/microsoft/Planetary-Explorer).

### GeoLLM-Engine (Singh, Fore, Stamoulis; CVPR EarthVision 2024)
- **What it does:** An environment for tool-augmented LLM agents doing realistic remote-sensing analyst workflows, with geospatial API tools, dynamic maps and UIs, and multimodal knowledge bases. It generated "over half a million diverse multi-tool tasks" across 1.1 million satellite images ([arXiv 2404.15500](https://arxiv.org/abs/2404.15500)).
- **Maturity:** A research paper; code availability was not verified.
- **Hackathon effort:** Use it as a design reference and task inspiration.
- **Known limitations and complaints:** The abstract reports no results; see the paper.
- **Example problem it unlocks:** An evaluation harness idea: "our agent solves X% of GeoLLM-Engine-style tasks".
- **Sources:** [arXiv 2404.15500](https://arxiv.org/abs/2404.15500).

### Planet Insights Platform (Planet Labs)
- **What it does:** A "cloud-native, broad-area-management destination for daily Earth data and analytics", with GIS integrations, developer APIs and analysis-ready mosaics ([Planet](https://www.planet.com/products/planet-insights-platform/)). The product page does not mention natural-language or agent features; any Planet AI-agent announcements were not verified. The Python client `planet-client-python` is ★300, Apache-2.0, v3.7.0 (2026-09-28) ([GitHub](https://github.com/planetlabs/planet-client-python)). Planet is a trusted tester of Google's Remote Sensing Foundation Models ([Google Earth AI](https://ai.google/earth-ai/)).
- **Hackathon effort:** Requires an account. Research and education access exists via Science Programs (terms not verified).
- **Example problem it unlocks:** High-cadence (daily) 3–5 m imagery if you can get access. Otherwise use NICFI tropical mosaics on Planetary Computer (`planet-nicfi-visual` and `planet-nicfi-analytic` collections, confirmed in the live STAC collection list).
- **Sources:** [Planet Insights Platform](https://www.planet.com/products/planet-insights-platform/), [planet-client-python](https://github.com/planetlabs/planet-client-python).

### GeoChat (MBZUAI, CVPR 2024)
- **What it does:** "The first grounded Large Vision Language Model for Remote Sensing", built from LLaVA-1.5 and fine-tuned on GeoChat_Instruct, which has 318k Vicuna-generated instruction samples. It does region-level reasoning, grounded captions and boxes ([GitHub](https://github.com/mbzuai-oryx/GeoChat)).
- **Maturity:** ★759, no license file on GitHub. Last push 2024-11-28; code released Feb 2024. HF `MBZUAI/geochat-7B` is Apache-2.0 with 838 dl/30d. It is the strongest grounder on VRSBench at 49.8% Acc@0.5 ([VRSBench](https://github.com/lx709/VRSBench)).
- **Hackathon effort:** **2–3 hours.** It is a 7B LLaVA stack, needs a GPU (roughly 16 GB+ VRAM for a 7B model in fp16 — estimate), and uses old dependencies.
- **Known limitations and complaints:** The code is stale (2024). Without fine-tuning on VRSBench it does poorly: "GeoChat w/o ft" gets 12.9% grounding ([VRSBench](https://github.com/lx709/VRSBench)).
- **Example problem it unlocks:** "Where are the storage tanks?" returns boxes on a high-resolution image.
- **Sources:** [mbzuai-oryx/GeoChat](https://github.com/mbzuai-oryx/GeoChat), [HF geochat-7B](https://huggingface.co/MBZUAI/geochat-7B).

### GeoPixel (MBZUAI, ICML 2025)
- **What it does:** A pixel-grounding LMM for high-resolution remote sensing. It outputs interleaved masks, uses adaptive image partitioning up to 4K, and comes with the GeoPixelD dataset and benchmark ([GitHub](https://github.com/mbzuai-oryx/GeoPixel), [arXiv 2501.13925](https://arxiv.org/abs/2501.13925)).
- **Maturity:** ★157, Apache-2.0, pushed 2026-09-05. HF `MBZUAI/GeoPixel-7B` had 74,104 dl/30d (HF API), which is high for a remote-sensing VLM.
- **Hackathon effort:** **2–3 hours** (7B, GPU).
- **Known limitations and complaints:** Heavy. The training data is generated.
- **Example problem it unlocks:** "Segment every damaged roof" as a language-to-mask demo.
- **Sources:** [mbzuai-oryx/GeoPixel](https://github.com/mbzuai-oryx/GeoPixel).

### EarthDial (CVPR 2025)
- **What it does:** A multi-sensory EO dialogue model with separate 4B checkpoints: `EarthDial_4B_RGB`, `_MS` (multispectral) and `_Methane_UHI` (methane and urban heat island) ([GitHub](https://github.com/hiyamdebary/EarthDial), [arXiv 2412.15190](https://arxiv.org/abs/2412.15190)).
- **Maturity:** ★148, MIT, last push 2025-06-20. HF EarthDial_4B_RGB had 2,579 dl/30d.
- **Hackathon effort:** **2–3 hours.**
- **Known limitations and complaints:** Small community; README placeholders ("Model Property" link empty).
- **Example problem it unlocks:** A chat over methane or urban-heat imagery.
- **Sources:** [hiyamdebary/EarthDial](https://github.com/hiyamdebary/EarthDial).

### TEOChat (Stanford Ermon group, ICLR 2025)
- **What it does:** "The first vision-language assistant for temporal earth observation data". It answers change and temporal questions over image sequences. It has an **HF Spaces demo** and the TEOChatlas dataset ([GitHub](https://github.com/ermongroup/TEOChat), [arXiv 2410.06234](https://arxiv.org/abs/2410.06234)).
- **Maturity:** ★157, Apache-2.0, pushed 2025-12-01. Fine-tuning and validation code arrived in March 2025.
- **Hackathon effort:** **Minutes** for the demo Space; **hours** to self-host.
- **Known limitations and complaints:** Based on Video-LLaVA. Temporal reasoning remains hard per GEOBench-VLM.
- **Example problem it unlocks:** "What changed between these two dates?" for disaster before/after.
- **Sources:** [ermongroup/TEOChat](https://github.com/ermongroup/TEOChat), [HF demo](https://huggingface.co/spaces/jirvin16/TEOChat).

### LHRS-Bot, LHRS-Bot-Nova and ScoreRS (Nanjing University, ECCV 2024)
- **What it does:** An RS MLLM that uses volunteered geographic information (OSM) with images. Nova (Sep 2024) upgraded the base model. **ScoreRS** (Mar 2025) adds a vision-language data scoring model. LHRS-Bench is released ([GitHub](https://github.com/NJU-LHRS/LHRS-Bot)).
- **Maturity:** ★194, Apache-2.0, last push 2025-03-04. Weights are on Google Drive and Baidu.
- **Hackathon effort:** Hours. It requires requesting Llama-2-7B-Chat access.
- **Known limitations and complaints:** Old base model; weights are off-HF.
- **Sources:** [NJU-LHRS/LHRS-Bot](https://github.com/NJU-LHRS/LHRS-Bot).

### SkyEyeGPT (ISPRS 2025) and EarthGPT (TGRS 2024)
- **SkyEyeGPT:** Unifies remote-sensing vision-language tasks via instruction tuning. The checkpoint was released May 2025 on HF and runs with MiniGPT-v2. The SkyEye-968k dataset is available. The README still says "Chatbot, codebase, and model inference tutorial coming soon" ([GitHub](https://github.com/ZhanYang-nwpu/SkyEyeGPT)). ★140, no license file.
- **EarthGPT:** A multi-sensor (optical, SAR, infrared) MLLM. The MMRS-1M dataset was open-sourced Oct 2024; no model weights are linked in the README ([GitHub](https://github.com/wivizhang/EarthGPT)). ★161.
- **Hackathon value:** Low. Their curated awesome-lists are useful for discovery ([Awesome RS MLLM](https://github.com/ZhanYang-nwpu/Awesome-Remote-Sensing-Multimodal-Large-Language-Model)).

### How well frontier models read satellite imagery (evidence summary)

| Benchmark | What it tests | Headline | Source |
|---|---|---|---|
| VLEO-Bench (Jan 2024) | GPT-4V on scene understanding, localisation and counting, change detection | Good at location understanding and captions; poor spatial reasoning hurts localisation and counting | [arXiv 2401.17600](https://arxiv.org/abs/2401.17600) |
| VRSBench (2024) | 29,614 images; captioning, grounding, VQA | Grounding Acc@0.5: GPT-4V **5.1**, LLaVA-1.5 41.6, GeoChat 49.8. VQA: GPT-4V 65.6 vs Mini-Gemini 77.8. Captions (CLAIR): GPT-4V best at 0.83 | [README](https://github.com/lx709/VRSBench), [arXiv 2406.12384](https://arxiv.org/abs/2406.12384) |
| GEOBench-VLM (Nov 2024 / Mar 2025) | 10k+ verified instructions; counting, tiny objects, temporal, relations | Best (LLaVA-OneVision) only **41.7%** MCQ accuracy, GPT-4o slightly below; about 2× random | [arXiv 2411.19325](https://arxiv.org/abs/2411.19325) |
| XLRS-Bench (CVPR 2025) | Ultra-high-resolution (~8500² px), 16 sub-tasks | Current MLLMs fall short for real-world RS | [arXiv 2503.23771](https://arxiv.org/abs/2503.23771) |
| VRSBench-SAR (Feb 2026) | SAR image-text annotations for SARDet-100k | Annotations *generated by GPT-5.1 and not human-verified*, so treat with caution | [VRSBench README](https://github.com/lx709/VRSBench) |

**Failure modes to design around:**
- counting
- small objects
- bounding boxes
- orientation
- temporal change
- non-RGB bands (multispectral, SAR, thermal), which a chat model cannot ingest natively
- ultra-large images, which must be tiled

**Mitigations:**
- Give the LLM numbers from specialist models (YOLO-OBB, SAM 3, embeddings), not pixels.
- Tile the image with SAHI.
- Render false-colour composites before asking.
- Ask for captions and explanations, not measurements.

No published remote-sensing benchmark of **Grok** specifically was found in this research (unverified gap). A small, fair head-to-head on VRSBench or GEOBench-VLM between Grok and an open remote-sensing VLM would itself be a credible hackathon result.

## 3. Detection, segmentation and change detection

**State of play (Oct 2026).** For demos, three families matter.

- **Promptable segmentation.** Meta's SAM 3 (Nov 2025) and SAM 3.1 (Mar 2026) segment "concepts" from text, such as "solar panels" or "swimming pools". `segment-geospatial` (samgeo) wraps SAM 1/2/3 for GeoTIFFs and exports vectors.
- **Rotated-box detection.** Ultralytics YOLO26 ships DOTA-v1 oriented-bounding-box checkpoints (ships, planes, storage tanks, vehicles and more) that run in one line. SAHI tiling fixes the small-object problem.
- **Task-specific EO models with public weights.** Cloud masks (OmniCloudMask, s2cloudless, Cloud Score+), super-resolution (SEN2SR, LDSR-S2, Satlas SR), floods (ml4floods, Prithvi Sen1Floods11), methane (CH4Net, STARCOP), fields (FTW), vessels (Skylight, xView3) and damage (Microsoft BDA).

There are also several **ready-made model-output datasets**: Microsoft's 1.4B building footprints, Satlas, Google's Cloud Score+, NASA FIRMS fires, and Global Fishing Watch SAR vessel detections. These let a team skip inference entirely.

### Quick-pick (detection, segmentation, change)

| Tool | Category | What it unlocks | Effort | License |
|---|---|---|---|---|
| SAM 3 / SAM 3.1 | Text/concept-promptable segmentation | "Segment all solar panels" on any image, zero-shot | ~1 hour (gated, CUDA 12.6+) | SAM License (custom) |
| segment-geospatial (samgeo) | SAM wrapper for GeoTIFFs | GeoTIFF → masks → GeoPackage/GeoJSON; text prompts; QGIS plugin; REST API | ~30–60 min | MIT |
| SAM 2 / SAM 2.1 | Promptable segmentation (+video) | Point/box prompts; track objects through image time series | ~30 min | Apache-2.0 |
| Ultralytics YOLO26-OBB (DOTA-v1) | Rotated object detection | Ships, planes, tanks, vehicles, bridges in high-res imagery | ~15 min | AGPL-3.0 (enterprise license for commercial) |
| SAHI | Sliced inference | Small objects in huge scenes with any detector | ~15 min | MIT |
| RF-DETR | Real-time DETR detector | Fine-tune a strong detector on a small labelled set | ~1–2 hours | Apache-2.0 |
| Grounding DINO / OWLv2 / Florence-2 | Open-vocabulary detection | Text-prompted boxes without training | ~30 min | Apache-2.0 / Apache-2.0 / MIT |
| MMRotate | Rotated detection toolbox | DOTA/FAIR1M research models | Hours (stale) | Apache-2.0 |
| open-cd / ChangeFormer / BIT | Supervised change detection | Building and land-change masks from bi-temporal pairs | ~1–3 hours | Apache-2.0 / MIT / none |
| torchange (AnyChange, Changen2) | Zero-shot change detection | SAM-based change masks without training | ~1–2 hours | Apache-2.0 |
| Microsoft building-damage-assessment | Disaster damage toolkit | Label, fine-tune and map building damage; SAR damage-proxy maps | Hours | MIT |
| OmniCloudMask | Cloud/shadow segmentation | Clear/thick/thin/shadow masks for S2, Landsat, PlanetScope, Maxar | ~10 min | MIT |
| s2cloudless | Cloud detection (LightGBM) | Classic S2 cloud probability | ~10 min | CC-BY-SA-4.0 |
| Cloud Score+ (Earth Engine) | Pre-computed S2 clear-pixel scores | One-line cloud masking in Earth Engine | Minutes | CC-BY-4.0 |
| SEN2SR / LDSR-S2 (ESA OpenSR) | Sentinel-2 super-resolution | 10 m → 2.5 m RGB-NIR (and 20 m → 10 m) | ~1 hour | CC0 / see repo |
| Satlas Super-Resolution | S2 → high-res SR | Global 2023 SR outputs; train/infer code | Hours | Apache-2.0 |
| ml4floods | Flood segmentation pipeline | WorldFloods models for S2 flood extent | ~1–2 hours | LGPL-3.0 code; CC-BY-NC models |
| CH4Net | Methane plume segmentation (S2) | Super-emitter plumes from S2 SWIR bands | Hours | MIT |
| STARCOP | Methane plume segmentation (hyperspectral) | EMIT/AVIRIS-NG plumes | Hours | GPL-3.0 |
| Skylight vessel detection (Ai2) | S1 SAR and S2 vessel detection | Ship detections like the production Skylight platform | Hours | Apache-2.0 |
| xView3 1st place | SAR dark-vessel detection | Benchmark-winning S1 vessel/fishing classifier | Hours | MIT |
| GFW SAR vessel detections API | Pre-computed detections | Dark vessels and offshore infrastructure without running models | ~30 min (free key) | GFW terms |
| NASA FIRMS | Pre-computed active fires | Near-real-time fire hotspots by area | ~15 min (free MAP_KEY) | NASA open data |
| FTW baselines / ftw-tools | Field-boundary segmentation | Field polygons from S2 anywhere via CLI | ~1 hour | MIT |
| Microsoft Global ML Building Footprints | Pre-computed buildings | 1.4B footprints, plus height estimates | Minutes | ODbL (per README; verify) |
| Meta canopy height (HighResCanopyHeight, CHMv2) | Canopy height models | Tree height and carbon from RGB | ~1 hour | Apache-2.0 / DINOv3 License |

### 3.1 Segment Anything family

#### SAM 3 and SAM 3.1 (Meta Superintelligence Labs, Nov 2025 / Mar 2026)
- **What it does:** "Segment Anything with Concepts". It detects, segments and tracks every instance of a noun-phrase concept in images and video. **SAM 3.1 Object Multiplex** (27 Mar 2026) adds a shared-memory multi-object tracker that is "significantly faster without sacrificing accuracy" ([GitHub](https://github.com/facebookresearch/sam3)).
- **Maturity:** ★12,092, pushed 2026-10-23. The license is the custom "SAM License". HF `facebook/sam3` is **gated (manual)**, with 5,019 likes and about 1.86M dl/30d; `facebook/sam3.1` had about 125k dl/30d (HF API). It requires Python 3.12+ and a CUDA GPU with CUDA 12.6+ ([GitHub](https://github.com/facebookresearch/sam3)).
- **Hackathon effort:** **~1 hour**, mostly waiting for gated access. Request access on HF immediately, or use `segment-geospatial[samgeo3]` ([samgeo README](https://github.com/opengeos/segment-geospatial)).
- **Known limitations and complaints:**
  - It was trained on natural images, so overhead imagery is out-of-domain. Small objects at 10 m Sentinel-2 resolution, such as cars, will fail; use sub-meter imagery (NAIP, Maxar Open Data, OpenAerialMap).
  - It is CUDA-only per the requirements, so on a Mac use Colab or Modal.
  - A remote-sensing benchmark of SAM 3 was not found in this research (unverified).
- **Example problem it unlocks:** "Count every swimming pool, solar array or blue tarp after a hurricane in this town" from one text prompt. This is visually striking for judges.
- **Sources:** [facebookresearch/sam3](https://github.com/facebookresearch/sam3), [HF facebook/sam3](https://huggingface.co/facebook/sam3), [HF facebook/sam3.1](https://huggingface.co/facebook/sam3.1).

#### segment-geospatial / samgeo (Qiusheng Wu, opengeos)
- **What it does:**
  - Downloads map tiles to GeoTIFF.
  - Segments with SAM, HQ-SAM, SAM 2, SAM 3 or FastSAM.
  - Supports **text prompts** (via Grounding DINO for SAM 1/2) and interactive markers.
  - Handles time series.
  - Exports GeoPackage, Shapefile or GeoJSON.
  - Offers a **REST API** (FastAPI) and a QGIS plugin.

  It installs as extras: `segment-geospatial[samgeo3]`, `[samgeo2]`, `[text]`, `[api]` and others ([GitHub](https://github.com/opengeos/segment-geospatial), docs at [samgeo.gishub.org](https://samgeo.gishub.org)).
- **Maturity:** ★4,175, MIT, v1.4.2 (2026-08-22), pushed 2026-10-19. A JOSS paper backs it.
- **Hackathon effort:** **30–60 minutes** to run the notebooks. The README recommends **pixi** for reliable PyTorch/CUDA and SAM 3 installs, especially on Windows.
- **Known limitations and complaints:** Dependency weight, since PyTorch, CUDA and SAM 3 gating are the usual pain points flagged in the README. Masks need post-filtering by area and shape.
- **Example problem it unlocks:** An end-to-end "type a concept, get a vector layer on a web map" pipeline for building, water or tree inventories.
- **Sources:** [opengeos/segment-geospatial](https://github.com/opengeos/segment-geospatial).

#### SAM 2 / SAM 2.1 and SAM 1 (Meta, 2024 / 2023)
- **What it does:** Point- and box-promptable segmentation. SAM 2 adds video, which is usable for satellite image time series ([SAM 2](https://github.com/facebookresearch/sam2), [SAM](https://github.com/facebookresearch/segment-anything)).
- **Maturity:** SAM 2: ★20,054, Apache-2.0; `sam2.1-hiera-large` had 287k dl/30d and is **not gated**. SAM 1: ★55,055, Apache-2.0, last push 2024-09-18.
- **Hackathon effort:** **~30 minutes.** It has no gating, unlike SAM 3, which makes it the fallback if SAM 3 access is slow.
- **Known limitations and complaints:** No text prompts natively; it needs Grounding DINO for those (samgeo `[text]`).
- **Sources:** as linked.

### 3.2 Object detection

#### Ultralytics YOLO26 / YOLO11 OBB (Ultralytics)
- **What it does:** One-line detection, segmentation, pose and **oriented bounding box (OBB)** models. The **YOLO26-OBB** checkpoints are trained on **DOTA-v1 (15 classes)** at 1024 px. DOTA-v1 test mAP50 ranges from 78.9 (n) to 81.7 (x), and YOLO26n-obb has 2.4M parameters. YOLO27 is listed as "Coming Soon", with "no launch date" ([GitHub](https://github.com/ultralytics/ultralytics)).
- **Maturity:** ★62,808, release v8.4.188 (2026-10-24).
- **Hackathon effort:** **~15 minutes**: `yolo predict model=yolo26n-obb.pt source=tile.png`.
- **Known limitations and complaints:**
  - The license is **AGPL-3.0**; commercial use needs an Enterprise License ([GitHub](https://github.com/ultralytics/ultralytics)). This is a common complaint for startups.
  - DOTA is aerial and sub-meter (Google Earth, GF-2, JL-1), so models will not work on 10 m Sentinel-2.
  - DOTA images are academic-use-only ([VRSBench README note on DOTA](https://github.com/lx709/VRSBench)).
- **Example problem it unlocks:** Port or airbase activity monitoring, i.e. counting ships, planes and storage tanks over time from Maxar Open Data or NAIP, with Grok narrating trends.
- **Sources:** [ultralytics/ultralytics](https://github.com/ultralytics/ultralytics).

#### SAHI — Slicing Aided Hyper Inference (OBSS)
- **What it does:** A framework-agnostic sliced/tiled inference library for small objects in large images, with error-analysis plots ([GitHub](https://github.com/obss/sahi)).
- **Maturity:** ★5,562, MIT, v0.12.8 (2026-09-30).
- **Hackathon effort:** **~15 minutes** to wrap YOLO or RF-DETR.
- **Known limitations and complaints:** Duplicate detections at tile edges need tuning of the merge thresholds.
- **Sources:** [obss/sahi](https://github.com/obss/sahi).

#### RF-DETR (Roboflow)
- **What it does:** A real-time transformer detector and segmenter on a DINOv2 backbone, SOTA on COCO and RF100-VL. It installs with `pip install rfdetr` ([GitHub](https://github.com/roboflow/rf-detr)).
- **Maturity:** ★9,884, Apache-2.0, release 1.11.2 (2026-10-04). HF `Roboflow/rf-detr-base` had 16,533 dl/30d.
- **Hackathon effort:** **1–2 hours** to fine-tune on a few hundred labelled chips.
- **Known limitations and complaints:** It needs labels; no remote-sensing weights are provided.
- **Example problem it unlocks:** A custom detector for something DOTA lacks, such as rocket launch pads, illegal mining pits or greenhouses.
- **Sources:** [roboflow/rf-detr](https://github.com/roboflow/rf-detr).

#### Open-vocabulary detectors: Grounding DINO, OWLv2, Florence-2
- **What it does:** Boxes from text prompts with no training:
  - `IDEA-Research/grounding-dino-base`: Apache-2.0, about 2.26M dl/30d.
  - `google/owlv2-base-patch16-ensemble`: Apache-2.0, about 1.57M dl/30d.
  - `microsoft/Florence-2-large`: MIT, about 375k dl/30d.

  Download figures are from the HF API.
- **Hackathon effort:** **~30 minutes** via HF Transformers.
- **Known limitations and complaints:** They are trained on natural images, so expect misses on top-down views and tiny objects (the same story as the VLM benchmarks in §2). samgeo uses Grounding DINO for its SAM 1/2 text mode.
- **Sources:** [HF grounding-dino-base](https://huggingface.co/IDEA-Research/grounding-dino-base), [HF owlv2](https://huggingface.co/google/owlv2-base-patch16-ensemble), [HF Florence-2-large](https://huggingface.co/microsoft/Florence-2-large).

#### MMRotate (OpenMMLab)
- **What it does:** A rotated-object-detection toolbox and benchmark: DOTA, HRSC and FAIR1M models.
- **Maturity:** ★2,177, Apache-2.0. **Last release v0.3.4 (2023-02-01), last push 2024-09-28**, so effectively unmaintained ([GitHub](https://github.com/open-mmlab/mmrotate)).
- **Hackathon effort:** Hours, because of MMCV version hell. Prefer YOLO-OBB.
- **Sources:** [open-mmlab/mmrotate](https://github.com/open-mmlab/mmrotate).

### 3.3 Change detection and damage

#### open-cd (likyoo)
- **What it does:** A change-detection toolbox on OpenMMLab, with ChangerEx, BAN, TTP, CGNet, ChangeStar, FarSeg and others. It added the MTKD method and JL1-CD dataset in Apr 2025, and has a technical report accepted at ACM MM 2025 ([GitHub](https://github.com/likyoo/open-cd)).
- **Maturity:** ★897, Apache-2.0, pushed 2026-06-15. Last release v1.1.0 (2024-02-10). The model zoo is on HF (`likyoo/Open-CD_Model_Zoo`).
- **Hackathon effort:** **1–3 hours** (MMCV environment).
- **Known limitations and complaints:** OpenMMLab dependency pinning. Models are trained on LEVIR-CD-style very-high-resolution building change.
- **Sources:** [likyoo/open-cd](https://github.com/likyoo/open-cd).

#### ChangeFormer and BIT
- **What it does:** Transformer Siamese change detectors on LEVIR-CD and DSIFN-CD ([ChangeFormer](https://github.com/wgcban/ChangeFormer), [BIT_CD](https://github.com/justchenhao/BIT_CD)).
- **Maturity:** ChangeFormer: ★627, MIT, last push 2024-01-31. BIT: ★521, no license file, last push 2021-07-25. Both are stale.
- **Hackathon effort:** 1–2 hours to run pretrained weights on very-high-resolution pairs.
- **Sources:** as linked.

#### torchange — AnyChange (zero-shot), Changen2 (Zheng et al.)
- **What it does:** A unified change-model library including **AnyChange ("Segment Any Change", NeurIPS 2024), zero-shot change detection built on SAM**, and the Changen/Changen2 generative change foundation models ([GitHub](https://github.com/Z-Zheng/pytorch-change-models)).
- **Maturity:** ★269, Apache-2.0, release v0.0.4 (2026-01-31). The API is "in beta and may change". It is maintained by a single person ("a significant burden for a single maintainer").
- **Hackathon effort:** **1–2 hours.**
- **Known limitations and complaints:** Beta API; single-file implementations.
- **Example problem it unlocks:** Before/after disaster change masks with no training labels.
- **Sources:** [Z-Zheng/pytorch-change-models](https://github.com/Z-Zheng/pytorch-change-models).

#### Microsoft building-damage-assessment toolkit (AI for Good Lab)
- **What it does:** Two workflows. (1) Label and fine-tune a building-damage model on Maxar Open Data imagery. (2) Analyse **SAR Damage Proxy Maps** (e.g. from NASA JPL ARIA) against building footprints. It was used for the Turkey/Syria earthquakes and other disasters ([GitHub](https://github.com/microsoft/building-damage-assessment)).
- **Maturity:** ★165, MIT, pushed 2026-08-11.
- **Hackathon effort:** **Hours** (conda env). The DPM workflow is faster than training.
- **Example problem it unlocks:** "Which buildings were damaged by this week's earthquake, flood or hurricane?" Pair it with Planetary Computer's live `predicted-damage-*-2026` collections (seen in the STAC collection list) or Maxar Open Data.
- **Sources:** [microsoft/building-damage-assessment](https://github.com/microsoft/building-damage-assessment).

### 3.4 Cloud masking

#### OmniCloudMask (DPIRD, Western Australia)
- **What it does:** Cloud and cloud-shadow segmentation for any imagery with **Red, Green and NIR** at 10–50 m, and down to 5 m with recent versions. It is validated on Sentinel-2, Landsat 8, PlanetScope and Maxar. Output classes are 0 clear, 1 thick cloud, 2 thin cloud, 3 shadow ([GitHub](https://github.com/DPIRD-DMA/OmniCloudMask), paper in *Remote Sensing of Environment* 2025).
- **Maturity:** ★202, MIT, v1.8.0 (2026-10-19), pushed today.
- **Hackathon effort:** **~10 minutes** (`pip install omnicloudmask`, then `predict_from_array`).
- **Known limitations and complaints:** It needs a NIR band, so RGB-only imagery is not supported.
- **Sources:** [DPIRD-DMA/OmniCloudMask](https://github.com/DPIRD-DMA/OmniCloudMask).

#### s2cloudless (Sentinel Hub)
- **What it does:** A single-scene, pixel-based LightGBM cloud detector for Sentinel-2. Its masks are also precomputed as a Sentinel Hub layer ([GitHub](https://github.com/sentinel-hub/sentinel2-cloud-detector)).
- **Maturity:** ★496, CC-BY-SA-4.0, last release v1.7.3 (2024-09-27).
- **Hackathon effort:** ~10 minutes.
- **Known limitations and complaints:** It is older and per-pixel, so expect thin-cloud and shadow misses; it does not detect shadows. LightGBM installation can be painful on some platforms, per the README.
- **Sources:** [sentinel-hub/sentinel2-cloud-detector](https://github.com/sentinel-hub/sentinel2-cloud-detector).

#### Cloud Score+ (Google, Earth Engine)
- **What it does:** Pre-computed per-pixel clear-sky scores (`cs`, `cs_cdf`, at 10 m) for harmonized Sentinel-2. The suggested masking threshold is **0.50–0.65** (0.60 in the example). Availability runs from 2015-06-27 to the present; archive backfill is ongoing. License CC-BY-4.0 ([EE catalog](https://developers.google.com/earth-engine/datasets/catalog/GOOGLE_CLOUD_SCORE_PLUS_V1_S2_HARMONIZED)).
- **Hackathon effort:** **Minutes** in Earth Engine.
- **Known limitations and complaints:** Earth Engine only. Subtiles processed without temporal context make `cs_cdf` less reliable there (inferred from the `NO_CONTEXT_FRACTION` property).
- **Sources:** [EE catalog](https://developers.google.com/earth-engine/datasets/catalog/GOOGLE_CLOUD_SCORE_PLUS_V1_S2_HARMONIZED).

**Other cloud tools not individually verified:** CloudSEN12 models (the `cloudsen12` package and the TACO version on HF, used in Copernicus-Bench), SEnSeIv2, Fmask, KappaMask, and the Sen2Cor SCL band included in L2A products (*unverified, leads*).

### 3.5 Super-resolution

#### SEN2SR and LDSR-S2 (ESA OpenSR)
- **What it does:**
  - **SEN2SR** super-resolves Sentinel-2 10 m and 20 m bands to **2.5 m** "radiometrically and spatially consistent", with Lite and full models, large-image prediction, and a local attention map for explainability ([GitHub](https://github.com/ESAOpenSR/SEN2SR), paper in *Remote Sensing of Environment*).
  - **LDSR-S2 (opensr-model)** is a latent-diffusion super-resolution model for RGB-NIR. v1.2.0 (Oct 2026) defaults to 3-step DPM-Solver++ with spectral back-projection, and it offers uncertainty estimates ([GitHub](https://github.com/ESAOpenSR/opensr-model)).
- **Maturity:** SEN2SR: ★185, CC0-1.0, pushed 2026-10-22. opensr-model: ★150, v1.2.2 (2026-10-23). Both have Colab notebooks.
- **Hackathon effort:** **~1 hour.**
- **Known limitations and complaints:** Super-resolution **hallucinates plausible detail**. Do not count cars on 2.5 m SR output or present it as real imagery. The diffusion version's uncertainty map helps.
- **Example problem it unlocks:** Prettier free imagery for a demo map, and better boundary delineation (fields, ponds) from free Sentinel-2.
- **Sources:** [ESAOpenSR/SEN2SR](https://github.com/ESAOpenSR/SEN2SR), [ESAOpenSR/opensr-model](https://github.com/ESAOpenSR/opensr-model).

#### Satlas Super-Resolution (Ai2)
- **What it does:** Training and inference code plus weights behind Satlas's globally generated 2023 super-resolution imagery. The training data includes an urban set of about 1.1M Sentinel-2/NAIP pairs from US cities ([GitHub](https://github.com/allenai/satlas-super-resolution), [arXiv 2311.18082](https://arxiv.org/pdf/2311.18082.pdf)).
- **Maturity:** ★348, Apache-2.0, pushed 2026-03-23.
- **Hackathon effort:** Hours (conda plus GDAL). The pre-generated outputs are faster to use.
- **Known limitations and complaints:** Trained on US NAIP, so it hallucinates US-style textures elsewhere.
- **Sources:** [allenai/satlas-super-resolution](https://github.com/allenai/satlas-super-resolution).

**Not verified:** S2DR3 (Gamma Earth), WorldStrat models, DiffusionSat and Text2Earth (generative) are left as leads.

### 3.6 Flood mapping

#### ml4floods / FloodMapper (Trillium / SpaceML / FDL)
- **What it does:** An end-to-end ML pipeline for flood extent, covering data, training, deployment and visualisation. It includes the WorldFloods v2 dataset (509 Sentinel-2 image/mask pairs, about 76 GB) and pretrained models ([GitHub](https://github.com/spaceml-org/ml4floods)).
- **Maturity:** ★184, LGPL-3.0 code, pushed 2026-05-20. **The dataset and pretrained models are CC BY-NC** (non-commercial).
- **Hackathon effort:** **1–2 hours** (`pip install ml4floods`, then the tutorials).
- **Known limitations and complaints:** Optical only, so clouds during floods are the classic failure. Pair it with Sentinel-1 or Prithvi/TerraMind Sen1Floods11 models. The licence is non-commercial.
- **Example problem it unlocks:** Flood-extent maps for an ongoing event, with population exposure computed from building footprints.
- **Sources:** [spaceml-org/ml4floods](https://github.com/spaceml-org/ml4floods).

**Also:** the Prithvi-EO-2.0-300M-TL-Sen1Floods11 and TerraMind Sen1Floods11 configs (§1); Kuro Siwo (S1 flood change, in Copernicus-Bench and GEO-Bench-2); Google Flood Hub (forecasts in over 100 countries; [Google Earth AI](https://ai.google/earth-ai/)); and Copernicus Global Flood Monitoring (lead, unverified).

### 3.7 Methane plume detection

#### CH4Net (Vaughan et al., 2023)
- **What it does:** A "fast, simple" model for methane super-emitter plumes in **Sentinel-2**, trained either on all 12 bands or on only SWIR bands 11 and 12. Data is on Zenodo ([GitHub](https://github.com/anna-allen/CH4Net), [EGUsphere preprint](https://egusphere.copernicus.org/preprints/2023/egusphere-2023-563/)).
- **Maturity:** ★14, MIT, last push 2023-08-21. The repo moved from `annavaughan` to `anna-allen` (GitHub API redirect).
- **Hackathon effort:** Hours, since weights may require training (not verified).
- **Known limitations and complaints:** Sentinel-2 detects only very large plumes, and false positives over bright surfaces are a known challenge (general knowledge, unverified here).
- **Sources:** [anna-allen/CH4Net](https://github.com/anna-allen/CH4Net).

#### STARCOP (SpaceML / Trillium)
- **What it does:** Semantic segmentation of methane plumes in **hyperspectral** data (AVIRIS-NG, and **EMIT on the ISS**, 2022–2023 detections shown). It also provides simulated WorldView-3 multispectral views ([GitHub](https://github.com/spaceml-org/STARCOP)).
- **Maturity:** ★74, GPL-3.0, pushed 2025-07-24. Data is on Zenodo, with a mini set on HF.
- **Hackathon effort:** Hours.
- **Example problem it unlocks:** "Find methane super-emitters in this oil and gas basin from public EMIT scenes", paired with Grok explanations and operator lookups. Note that the OlmoEarth license bans extractive-industry use, but STARCOP is GPL.
- **Sources:** [spaceml-org/STARCOP](https://github.com/spaceml-org/STARCOP).

**Leads:** Carbon Mapper's public plume data portal and Tanager data, UNEP IMEO MARS, MethaneSAT status, and TROPOMI-based plume detection. These are covered by the EO companies and analytics slices (unverified here).

### 3.8 Fire and burn scar

#### NASA FIRMS API (pre-computed active fires)
- **What it does:** Fire hotspots by area, date and sensor in CSV, KML footprints, and data-availability endpoints (API v4.2.2). The `country` endpoint is marked "Feature currently not available". A MAP_KEY is required ([FIRMS API](https://firms.modaps.eosdis.nasa.gov/api/)).
- **Maturity:** An operational NASA service.
- **Hackathon effort:** **~15 minutes**, including getting a MAP_KEY.
- **Known limitations and complaints:** Transaction limits are not stated on the API page; check the map_key page.
- **Example problem it unlocks:** Wildfire-response dashboards that combine FIRMS points with weather from WeatherNext via Open-Meteo (§4) and building footprints.
- **Sources:** [FIRMS API](https://firms.modaps.eosdis.nasa.gov/api/).

**Also:** the Prithvi-EO-2.0-300M-BurnScars checkpoint and `hls_burn_scars` dataset (CC-BY-4.0, 1,665 dl/30d) (§1). Leads not verified: FireSat (Google / Earth Fire Alliance / Muon), and the Next Day Wildfire Spread dataset and models.

### 3.9 SAR ships and maritime

#### Skylight vessel detection (Ai2) — Sentinel-1 SAR and Sentinel-2
- **What it does:** Vessel detection in Sentinel-1 SAR and Sentinel-2 EO/IR imagery. The models "run at global scale in production in Skylight", Ai2's free maritime-intelligence platform ([GitHub](https://github.com/allenai/vessel-detection-sentinels), [arXiv 2312.03207](https://arxiv.org/abs/2312.03207)).
- **Maturity:** ★53, Apache-2.0, last push 2024-05-11.
- **Hackathon effort:** Hours: download imagery from ESA with the scripts, then run the models.
- **Example problem it unlocks:** Dark-vessel detection, i.e. ships with no AIS near marine protected areas.
- **Sources:** [allenai/vessel-detection-sentinels](https://github.com/allenai/vessel-detection-sentinels).

#### xView3 first-place solution (Eugene Khvedchenya)
- **What it does:** The winning solution for the xView3 SAR dark-vessel challenge, scoring an aggregate 0.603 on the public leaderboard and 0.617 on the holdout ([GitHub](https://github.com/DIUx-xView/xView3_first_place)).
- **Maturity:** ★20, MIT, 2022, stale.
- **Hackathon effort:** Hours, and the xView3 data needs registration.
- **Sources:** [DIUx-xView/xView3_first_place](https://github.com/DIUx-xView/xView3_first_place).

#### Global Fishing Watch APIs (pre-computed)
- **What it does:** Several APIs:
  - fishing effort for about 70,000 AIS vessels
  - vessel identity search
  - events (fishing, encounters, loitering, port visits)
  - **SAR vessel detections and offshore fixed infrastructure**, filterable by AIS matching and by label (oil, wind, unknown)

  Access is via a free API key, with terms and attribution required ([GFW APIs](https://globalfishingwatch.org/our-apis/)).
- **Hackathon effort:** **~30 minutes.**
- **Known limitations and complaints:** Rate limits and non-commercial terms are not stated on the overview page (unverified).
- **Example problem it unlocks:** "Ships that don't broadcast AIS near protected areas", with no model to run.
- **Sources:** [GFW APIs](https://globalfishingwatch.org/our-apis/).

**Leads not verified:** SARDet-100K and its MSFA model, SSDD and HRSID datasets, SAR foundation models (SARATR-X, SAR-JEPA), and oil-spill detection models.

### 3.10 Other task models and ready-made model outputs

#### Fields of The World (FTW) baselines and `ftw-tools` CLI
- **What it does:** Instance segmentation of agricultural **field boundaries** from Sentinel-2. The `ftw inference all` command downloads an S2 scene and predicts field polygons ([GitHub](https://github.com/fieldsoftheworld/ftw-baselines)). The dataset is on Source Cooperative.
- **Maturity:** ★162, MIT, release v3.1 (2025-11-30), pushed 2026-10-24.
- **Hackathon effort:** **~1 hour** (uv install).
- **Example problem it unlocks:** Field-level crop insurance or food-security analytics anywhere.
- **Sources:** [fieldsoftheworld/ftw-baselines](https://github.com/fieldsoftheworld/ftw-baselines).

#### Microsoft Global ML Building Footprints (Bing Maps)
- **What it does:** **1.4B building footprints** detected from Bing Maps imagery (Maxar, Airbus, IGN France, 2014–2024). There are frequent 2026 additions with **height estimates** from Vexcel imagery; the 13 Aug 2026 refresh covers 30,340 tiles in 225 regions. The hosting URL moved on 24 Jul 2026 to `bfppub.blob.core.windows.net` ([GitHub](https://github.com/microsoft/GlobalMLBuildingFootprints)). The README states the data is available under CDLA Permissive (truncated in the excerpt read; check the license).
- **Maturity:** ★1,973, last push 2026-08-14. It is also on Planetary Computer as `ms-buildings`.
- **Hackathon effort:** **Minutes.**
- **Known limitations and complaints:** Imagery dates vary by region, so footprints can be years old. Hosting moved twice (Nov 2024 and Jul 2026), so old links break.
- **Sources:** [microsoft/GlobalMLBuildingFootprints](https://github.com/microsoft/GlobalMLBuildingFootprints).

#### Meta canopy height: HighResCanopyHeight (2024) and CHMv2 (2026)
- **What it does:** Canopy-height inference from aerial or satellite RGB. CHMv2 (Mar 2026) uses the DINOv3 satellite ViT-L backbone and is in HF Transformers ([HighResCanopyHeight](https://github.com/facebookresearch/HighResCanopyHeight), [DINOv3 README](https://github.com/facebookresearch/dinov3)).
- **Maturity:** HighResCanopyHeight: ★367, Apache-2.0. CHMv2 weights are gated on HF.
- **Example problem it unlocks:** Urban tree-canopy and heat-island equity maps, and forest-carbon baselines.

#### GeoAI (opengeos) — high-level wrapper
- **What it does:**
  - Search and download imagery (Sentinel, Landsat, NAIP).
  - Chip images and generate labels.
  - Train and run inference for classification, detection and segmentation (segmentation_models.pytorch).
  - Integrates Overture Maps data, leafmap/MapLibre visualisation and a QGIS plugin.

  There is a 2026 JOSS paper and a book ([GitHub](https://github.com/opengeos/geoai)).
- **Maturity:** ★3,438, MIT, v0.43.1 (2026-09-21).
- **Hackathon effort:** **~1 hour** for building, water or solar-panel segmentation notebooks.
- **Sources:** [opengeos/geoai](https://github.com/opengeos/geoai).

**Ready-made land-cover products** (used as model outputs; the datasets slice covers these): ESA WorldCover, Esri 10 m LULC (`io-lulc-annual-v02` on Planetary Computer), Dynamic World, JRC Global Surface Water (`jrc-gsw`), MTBS burn severity (`mtbs`) and MODIS fire (`modis-14A1-061`). All appear in the live Planetary Computer STAC collection list fetched 2026-10-24.

## 4. Weather and climate AI

**State of play (Oct 2026).** AI weather models are now operational, and several have open weights.

- **Google DeepMind** consolidated GraphCast, GenCast and its cyclone model under **WeatherNext**. The `google-deepmind/graphcast` repo now redirects to `google-deepmind/weathernext`, which ships **WeatherNext 2** weights; the WeatherNext Cyclones model ran live in the 2025 Atlantic season ([GitHub](https://github.com/google-deepmind/weathernext)).
- **Microsoft's Aurora** (Nature, May 2025) is MIT-licensed on PyPI.
- **ECMWF AIFS** has open weights under CC-BY-4.0.
- **NVIDIA Earth2Studio** wraps most models behind one API.

**The hackathon shortcut is not to run any model.** Open-Meteo serves the 64-member WeatherNext 2 ensemble as a free HTTP API ([Open-Meteo](https://open-meteo.com/en/docs/google-weathernext-api)).

### Quick-pick (weather and climate)

| Tool | Category | What it unlocks | Effort | License |
|---|---|---|---|---|
| WeatherNext 2 via Open-Meteo API | Hosted AI ensemble forecast | 64-member, 0.25°, 15-day AI forecast for any lat/lon with one HTTP call | Minutes | Open-Meteo terms (non-commercial option) |
| WeatherNext (weathernext repo: WN2, Cyclones, GraphCast, GenCast) | Open-weights global models | Run your own forecasts and cyclone tracks; Colab on a free TPU (Mini models) | 1–3 hours | Apache-2.0 code, CC-BY-4.0 weights |
| Earth2Studio (NVIDIA) | Inference toolkit / model zoo | FourCastNet3, AIFS, GraphCast, WeatherNext 2 Cyclones, CorrDiff, FuXi-S2S behind one API | ~1–2 hours (GPU) | Apache-2.0 (model licenses vary) |
| Aurora (Microsoft) | Earth-system foundation model | Weather, air pollution, ocean waves, high-res 0.1° | ~1–2 hours (GPU) | MIT |
| ECMWF AIFS Single / ENS + anemoi | Operational open model | ECMWF's own AI forecast; runnable via anemoi-inference | Hours | CC-BY-4.0 weights |
| Prithvi-WxC (NASA/IBM) | 2.3B weather foundation model | Downscaling, gravity-wave parameterisation, masked reconstruction | Hours (big GPU) | MIT code, CDLA-Permissive-2.0 weights |
| NeuralGCM (Google) | Hybrid ML+physics GCM | Weather-to-climate simulations | Hours | Apache-2.0 code, CC-BY-SA-4.0 weights |
| ACE / ACE2 (Ai2) | Climate emulator | Century-scale climate runs on a free Colab GPU | ~1–2 hours | Apache-2.0 |
| Pangu-Weather / FuXi / FengWu | Chinese global models | Baselines; FuXi-2.1 sharper extremes | Hours | Pangu weights CC BY-NC-SA (no commercial) |
| WeatherBench 2 (+ WeatherBench-X) | Benchmark + ARCO ERA5 | Compare models; free cloud ERA5 | ~1 hour | Apache-2.0 |
| ARCO-ERA5 | Cloud-optimised reanalysis | 1979–present hourly ERA5 Zarr on GCS | ~30 min | ERA5 terms |
| pysteps / DGMR / MetNet | Nowcasting | 0–6 h radar/satellite precipitation nowcasts | 1–3 hours | BSD-3 / MIT / MIT |
| earthkit (ECMWF) | Data toolkit | Read GRIB/NetCDF/ODB, plotting | ~30 min | Apache-2.0 |

### WeatherNext 2, WeatherNext Cyclones, GraphCast and GenCast (Google DeepMind)
- **What it does:** A single repo for WeatherNext 2 (WN2), "the global, medium-range atmospheric and cyclone forecasting model", together with the legacy **WeatherNext Graph (GraphCast)** and **WeatherNext Gen (GenCast)**.
  - WN2 runs at 0.25° and is initialised from operational HRES. It also predicts 100 m wind.
  - The WeatherNext Cyclones checkpoint "ran live during the 2025 Atlantic hurricane season", publicly called FNV3; NHC's post-processed version was GDMI ([GitHub](https://github.com/google-deepmind/weathernext)).
  - Papers: the FGN/WN2 technical report ([arXiv 2506.10772](https://arxiv.org/abs/2506.10772)) and the cyclone paper in Nature ([s41586-026-10953-2](https://www.nature.com/articles/s41586-026-10953-2)).
  - Forecast feeds are available via Google Cloud (Earth Engine, BigQuery, Vertex AI), [WeatherLab](https://deepmind.google.com/science/weatherlab) and Open-Meteo.
- **Maturity:** ★7,719 (the former graphcast repo), release v0.3.0 (2026-08-06). Code is Apache-2.0; other materials are CC-BY-4.0 ([GitHub](https://github.com/google-deepmind/weathernext)).
- **Hackathon effort:** **1–3 hours.** The Colab defaults to "WeatherNext Cyclones Mini" on a **free v5e-1 TPU runtime**. Non-Mini models need a v5p TPU or an **H100**; Mini models "should manage inference on a P100" ([GitHub](https://github.com/google-deepmind/weathernext)).
- **Known limitations and complaints:** Optimised for TPU. On GPU the attention implementation must be switched. Initial conditions (HRES or ERA5) are needed.
- **Example problem it unlocks:** Hurricane track and intensity explainers, wind-farm output forecasts (100 m wind), or comparing the AI ensemble against NHC.
- **Sources:** [google-deepmind/weathernext](https://github.com/google-deepmind/weathernext).

### WeatherNext 2 via the Open-Meteo API
- **What it does:** Serves WeatherNext 2 as a **64-member ensemble** plus an ensemble mean computed by Open-Meteo. It is a 0.25° grid with 6-hourly source data interpolated to hourly, runs to **15 days**, and updates every 12 h (00 and 12 UTC). Variables include surface fields, 13 pressure levels and ensemble spread. Example call: `https://ensemble-api.open-meteo.com/v1/ensemble?latitude=52.52&longitude=13.41&hourly=temperature_2m&models=google_weathernext2_ensemble` ([Open-Meteo](https://open-meteo.com/en/docs/google-weathernext-api)).
- **Maturity:** Live. The page offers non-commercial, commercial and self-hosted options but does not state free limits for this model (unverified).
- **Hackathon effort:** **Minutes**, with no key.
- **Known limitations and complaints:** It runs only the 00 and 12 UTC runs, with a 6-hourly native step.
- **Example problem it unlocks:** "Probability that wind exceeds a launch-commit limit at Cape Canaveral or Starbase in the next 7 days", or a probabilistic wildfire-weather alert. Ensembles give honest uncertainty.
- **Sources:** [Open-Meteo WeatherNext 2 API](https://open-meteo.com/en/docs/google-weathernext-api).

### NVIDIA Earth2Studio (+ PhysicsNeMo, Earth-2 open models)
- **What it does:** "AI inference pipeline toolkit" for weather and climate with a unified API across:
  - **models:** FourCastNet3, ECMWF AIFS, GraphCast Operational, WeatherNext 2 Cyclones wrappers, CAMulator, FuXi-S2S, CorrDiff ERA5→HRRR downscaling
  - **data sources:** GFS, ERA5 and others
  - **IO:** Zarr

  It also publishes agent "skills" (`npx skills add NVIDIA/skills --skill earth2studio-install`) ([GitHub](https://github.com/NVIDIA/earth2studio)).
- **Maturity:** ★1,213, Apache-2.0, release 0.19.0 (2026-09-30). PhysicsNeMo (training framework): ★3,385, Apache-2.0, v2.2.2. HF `nvidia/fourcastnet3`: Apache-2.0. The original FourCastNet repo is stale (2023).
- **Hackathon effort:** **1–2 hours** on a CUDA GPU (Modal or Colab).
- **Known limitations and complaints:** "Licenses for these assets are owned by their providers" ([GitHub](https://github.com/NVIDIA/earth2studio)). Each model's license must be checked.
- **Example problem it unlocks:** Kilometre-scale US downscaling (CorrDiff) for severe-weather risk to ground stations or launch sites.
- **Sources:** [NVIDIA/earth2studio](https://github.com/NVIDIA/earth2studio), [NVIDIA/physicsnemo](https://github.com/NVIDIA/physicsnemo).

### Aurora (Microsoft Research; Nature 2025)
- **What it does:** A foundation model for the Earth system. There are specialised versions for medium-resolution weather, **high-resolution 0.1° weather, air pollution and ocean waves**. Install with `pip install microsoft-aurora` ([GitHub](https://github.com/microsoft/aurora), [Nature](https://www.nature.com/articles/s41586-025-09005-y)).
- **Maturity:** ★1,032, **MIT**, release v2.0.1 (2026-08-04). It also appears in Microsoft Planetary Explorer's model list.
- **Hackathon effort:** **1–2 hours**. The docs include an ERA5 example. A GPU is needed.
- **Known limitations and complaints:** Microsoft asks commercial users to email them, although the code license is MIT. WeatherBench 2 notes that Aurora is initialised from operational IFS ([WeatherBench](https://sites.research.google/weatherbench/)).
- **Example problem it unlocks:** Air-quality (NO₂, O₃) forecasts for cities, combined with Sentinel-5P observations.
- **Sources:** [microsoft/aurora](https://github.com/microsoft/aurora).

### ECMWF AIFS (Single 1.0, ENS 1.0) and the Anemoi framework
- **What it does:** ECMWF's operational AI forecasting system. Weights are on HF as `ecmwf/aifs-single-1.0` (Feb 2025) and `ecmwf/aifs-ens-1.0` (Jun 2025), both **CC-BY-4.0** (HF API). anemoi-core (★170, Apache-2.0) and anemoi-inference (★44, v0.13.0, 2026-10-21) run them ([anemoi-inference](https://github.com/ecmwf/anemoi-inference)). The older `ai-models` CLI is **archived**: "should NOT be used for any active operational purposes" ([ecmwf-lab/ai-models](https://github.com/ecmwf-lab/ai-models)).
- **Hackathon effort:** Hours. AIFS also runs inside Earth2Studio.
- **Sources:** [HF ecmwf/aifs-single-1.0](https://huggingface.co/ecmwf/aifs-single-1.0), [ecmwf/anemoi-core](https://github.com/ecmwf/anemoi-core).

### Prithvi-WxC (NASA/IBM, 2024)
- **What it does:** A 2.3B-parameter weather and climate foundation model trained on MERRA-2. Fine-tunes cover downscaling (MERRA-2, EURO-CORDEX via IBM granite-wxc) and gravity-wave parameterisation (ERA5), plus zero-shot masked reconstruction and forecasting ([GitHub](https://github.com/NASA-IMPACT/Prithvi-WxC)).
- **Maturity:** ★205, MIT. HF weights `Prithvi-WxC-1.0-2300M` are CDLA-Permissive-2.0, 4,935 dl/30d. **The 25 Mar 2025 update fixed "a number of bugs that led to incorrect model outputs and worse performance than in our paper"** ([GitHub](https://github.com/NASA-IMPACT/Prithvi-WxC)).
- **Hackathon effort:** Hours, on a large GPU.
- **Known limitations and complaints:** The bug history means you should use the latest code and run the provided validation script.
- **Sources:** [NASA-IMPACT/Prithvi-WxC](https://github.com/NASA-IMPACT/Prithvi-WxC).

### NeuralGCM (Google Research)
- **What it does:** A hybrid ML/physics atmospheric model for weather and climate ([GitHub](https://github.com/neuralgcm/neuralgcm), [arXiv 2311.07222](https://arxiv.org/abs/2311.07222)).
- **Maturity:** ★1,029, release v1.2.2 (2025-07-31). Code is Apache-2.0; **weights are CC-BY-SA-4.0**. It is on WeatherBench 2 as NeuralGCM 0.7° and NeuralGCM ENS.
- **Hackathon effort:** Hours (JAX).
- **Sources:** [neuralgcm/neuralgcm](https://github.com/neuralgcm/neuralgcm).

### ACE / ACE2 — Ai2 Climate Emulator
- **What it does:** A fast ML emulator of global atmospheric variability "from hours to centuries". It installs as `pip install fme`; checkpoints are on HF. Workshop notebooks run ACE, SamudrACE and HiRO-ACE **on free Colab GPUs** ([GitHub](https://github.com/ai2cm/ace)).
- **Maturity:** ★258, Apache-2.0, release v2026.10.0 (2026-10-20).
- **Hackathon effort:** **1–2 hours.**
- **Example problem it unlocks:** A "what-if" climate scenario explorer, e.g. heat extremes under different forcing.
- **Sources:** [ai2cm/ace](https://github.com/ai2cm/ace).

### Pangu-Weather (Huawei), FuXi (Fudan), FengWu (Shanghai AI Lab)
- **Pangu-Weather** (Nature 2023): ★1,399. The weights are **CC BY-NC-SA 4.0, "The commercial use of these models is forbidden"**. Some resources are on Baidu Netdisk ([GitHub](https://github.com/198808xc/Pangu-Weather)).
- **FuXi:** ★193. **FuXi-2.1** is out on HF (`tpys/fuxi-2.1`): "much sharper, more detailed predictions — resolving extreme rain and wind that earlier models blur away" ([GitHub](https://github.com/tpys/FuXi)).
- **FengWu:** inference code and pretrained model, with skill "beyond 10 days lead" ([GitHub](https://github.com/OpenEarthLab/FengWu), ★181).
- **ClimaX** (Microsoft) is **archived** (★703).
- **Hackathon value:** These are comparison baselines. The China slice covers the institutional context.

### WeatherBench 2 / WeatherBench-X, ARCO-ERA5, earthkit
- **WeatherBench 2:** Scorecards compare deterministic models against IFS HRES and probabilistic models against IFS ENS on 2022. Listed models include:
  - Pangu
  - GraphCast
  - FuXi
  - SphericalCNN
  - Excarta
  - ArchesWeather
  - Baguan
  - WeatherMesh 4 (flagged as trained on future years)
  - Aurora
  - Tianji
  - NeuralGCM
  - GenCast
  - Stormer
  - ArchesWeatherGen
  - FGN

  Aurora and FGN are initialised from operational IFS. Evaluation code is now **WeatherBench-X** ([WeatherBench](https://sites.research.google/weatherbench/)). The weatherbench2 repo is ★646, Apache-2.0 ([GitHub](https://github.com/google-research/weatherbench2)). The leaderboard scores are images and were not readable in this research.
- **ARCO-ERA5:** Hourly ERA5 from 1979 to present at about 0.28°, roughly 5 PB, in Google Cloud Public Datasets (★513, Apache-2.0) ([GitHub](https://github.com/google-research/arco-era5)). It is the fastest way to get initial conditions and history without a Copernicus CDS queue.
- **earthkit (ECMWF):** v1.0.0 (2026-06-29), Apache-2.0, ★319 ([GitHub](https://github.com/ecmwf/earthkit)).

### Nowcasting: pysteps, DGMR, MetNet
- **pysteps:** A Python framework for short-term ensemble precipitation nowcasting. ★593, BSD-3, v1.21.5 (2026-08-14) ([GitHub](https://github.com/pySTEPS/pysteps)).
- **DGMR:** Open Climate Fix's PyTorch implementation of DeepMind's radar nowcasting GAN (`pip install dgmr`). ★300, MIT, v1.4.4 ([GitHub](https://github.com/openclimatefix/skillful_nowcasting)).
- **MetNet / MetNet-2:** Open Climate Fix implementation, ★304, MIT ([GitHub](https://github.com/openclimatefix/metnet)). A MetNet-3 port exists (lucidrains, stale since 2023, [GitHub](https://github.com/lucidrains/metnet3-pytorch)).
- **Hackathon effort:** 1–3 hours. The data is the hard part: radar mosaics (NOAA MRMS on Planetary Computer `noaa-mrms-qpe-*`) or GOES ABI (`goes-cmi` on Planetary Computer).
- **Example problem it unlocks:** "Will this thunderstorm hit the launch pad, stadium or airport in the next 90 minutes?"

## 5. Heliophysics, space-weather and planetary models

**State of play (Oct 2026).** NASA and IBM released **Surya** (Aug 2025), the first heliophysics foundation model trained on full-resolution SDO data. They followed it with the **NASA-IBM Lunar Foundation Model** (HF, 1 Sep 2026; repo created 30 Jul 2026). Otherwise space-weather ML is mostly papers. The fastest demos combine **live NOAA SWPC JSON feeds** with Surya flare forecasts and an LLM explainer. The team should check the problem side in the space-weather slice; the May 2024 storm and the Feb 2022 Starlink loss are the usual motivators.

### Quick-pick (helio, space weather, planetary)

| Tool | Category | What it unlocks | Effort | License |
|---|---|---|---|---|
| Surya (NASA/IBM) | Heliophysics foundation model (366M) | Flare forecasting (M/X class, 24 h), active-region segmentation, solar wind, EUV spectra; zero-shot forecasting | ~1–2 hours (GPU; CPU/MPS works for easy inference) | Apache-2.0 |
| core-sdo / SuryaBench data | SDO AIA+HMI training data (HF, public S3) | Ready ML-format solar images | ~30 min | CC-BY-4.0 |
| NASA-IBM Lunar Foundation Model | Lunar multimodal FM (ViT-B, TerraMind-style) | Crater detection, ice prospectivity, IMP segmentation on LROC NAC/WAC | ~1–3 hours | Apache-2.0 |
| SDO-FM (SpaceML) | Solar foundation model (research) | Alternative SDO embeddings | Hours | No license file |
| NOAA SWPC JSON services | Live space-weather data | Kp, solar wind, alerts — no key | Minutes | US Gov public |
| NASA DONKI (via api.nasa.gov) | Event database (flares, CMEs, storms) | Historical and live event catalogue | Minutes (free key) | US Gov public |
| SunPy (+ aiapy, ndcube) | Solar-physics Python stack | Fetch and plot SDO/AIA, coordinates | ~30 min | BSD-2 |

### Surya (NASA IMPACT + IBM, Aug 2025)
- **What it does:** A **366M-parameter** spatiotemporal transformer. It is trained on full-resolution (4096×4096, 12-minute cadence) SDO data covering 8 AIA channels and 5 HMI channels. It forecasts solar dynamics zero-shot and is LoRA-fine-tunable. Reported downstream results versus baselines ([GitHub](https://github.com/NASA-IMPACT/Surya)):

  | Task | Surya | Baseline |
  |---|---|---|
  | Flare forecasting (TSS) | **0.436** | 0.358 (AlexNet) |
  | Active-region segmentation (IoU) | **0.768** | 0.688 (U-Net) |
  | Solar-wind prediction (RMSE) | **75.92** | 93.76 (ResNet50) |
  | EUV spectra (MAPE) | **1.48%** | 1.68% |

  Flare forecasting covers "M-class and X-class solar flares up to 24 hours in advance".
- **Maturity:** ★180, Apache-2.0, release v1.0.0 (2025-08-19), pushed 2026-04-29. HF `nasa-ibm-ai4science/Surya-1.0` has 108 likes, plus downstream checkpoints `solar_flares_surya`, `solar_wind_surya`, `ar_segmentation_surya` and `euv_spectra_surya`. The dataset `core-sdo` is CC-BY-4.0, 1,443 dl/30d (HF API).
- **Hackathon effort:** **~1–2 hours.** `uv sync`, then `python easy_inference/run_easy_inference.py`. This downloads the needed `.nc` files from the public S3 bucket `nasa-surya-bench` for a date range and runs on **CUDA, Apple MPS or CPU** ([GitHub](https://github.com/NASA-IMPACT/Surya)).
- **Known limitations and complaints:** A flare TSS of 0.436 is better than the baseline but far from operational reliability; say so in a pitch. Full-resolution data is heavy.
- **Example problem it unlocks:** "Solar-storm early warning for satellite operators". The steps are:
  - a Surya flare probability
  - live SWPC Kp and solar wind
  - satellite drag and orbit-decay context for a constellation
  - Grok writing an operator bulletin

  This ties directly to the Feb 2022 Starlink loss (problem facts in the space-weather slice).
- **Sources:** [NASA-IMPACT/Surya](https://github.com/NASA-IMPACT/Surya), [HF Surya-1.0](https://huggingface.co/nasa-ibm-ai4science/Surya-1.0), [HF core-sdo](https://huggingface.co/datasets/nasa-ibm-ai4science/core-sdo).

### NASA-IBM Lunar Foundation Model (NASA IMPACT + IBM, Sep 2026)
- **What it does:** A multimodal, multi-resolution lunar remote-sensing FM.
  - **Architecture:** a ViT-B encoder-decoder trained from scratch with TerraMind's any-to-any masked-token recipe, plus FlexiViT patch resizing.
  - **Training data:** **SomBench**, about 2M co-registered tile bundles with **11 modalities** at two scales: LROC NAC at about 1 m/px and LROC WAC at about 100 m/px.
  - **Geometry:** illumination geometry is given as explicit input tokens.
  - **Downstream:** adaptation through TerraTorch, with released fine-tunes for **crater detection, IMP (irregular mare patch) segmentation and ice prospectivity**.
  - **Pretraining cost:** 16× H100, about 1.1k GPU-hours.

  Sources: [HF model card](https://huggingface.co/nasa-ibm-ai4science/NASA-IBM-Lunar-Foundation-Model), paper [arXiv 2609.13283](https://arxiv.org/pdf/2609.13283).
- **Maturity:**
  - HF weights are **Apache-2.0** (54 likes, 2,421 dl/30d); companion HF repos `Crater-Detection-…`, `IMP-Segmentation-…` and `Ice-Prospectivity-…` were all created 2026-09-01 (HF API).
  - GitHub [NASA-IMPACT/NASA-IBM-Lunar-Foundation-Model](https://github.com/NASA-IMPACT/NASA-IBM-Lunar-Foundation-Model) is ★57. It contains finetuning and inference packages (`ni_lfm`, `terratorch_integration`) and configs; "pretraining code is not included".
- **Hackathon effort:** **1–3 hours.** Python 3.12, `pip install -e .`, `snapshot_download` of the backbone and datasets, then symlink `data/` and `backbone/` ([GitHub](https://github.com/NASA-IMPACT/NASA-IBM-Lunar-Foundation-Model)).
- **Known limitations and complaints:** Brand new (weeks old). The config wiring (required `backbone_cfg`, symlinked roots) is fiddly. It works only on LROC-style products.
- **Example problem it unlocks:** "Artemis landing-site and water-ice prospecting assistant": ice-prospectivity maps plus crater hazards for south-pole sites, explained by an LLM, with LROC imagery in a CesiumJS Moon globe. This is very on-theme for a SpaceX-sponsored challenge (Starship HLS).
- **Sources:** as linked.

### SDO-FM (SpaceML / FDL)
- **What it does:** "A foundation model for the Sun" from the SpaceML community ([GitHub](https://github.com/spaceml-org/SDO-FM)).
- **Maturity:** ★8, no license file, pushed 2026-05-22. It is a research prototype.
- **Hackathon value:** Low versus Surya.

### Live space-weather data APIs

| API | What | Auth | Notes / source |
|---|---|---|---|
| NOAA SWPC JSON (`services.swpc.noaa.gov/json/`, `/products/noaa-planetary-k-index.json`) | Kp, solar wind (DSCOVR/ACE), X-ray flux, alerts | None | Tested 2026-10-24: Kp JSON returned 3-hourly values ([endpoint](https://services.swpc.noaa.gov/products/noaa-planetary-k-index.json)) |
| NASA DONKI (`api.nasa.gov/DONKI/FLR`, CME, GST…) | Flares, CMEs, geomagnetic storms, SEPs | api.nasa.gov key | `DEMO_KEY` returned **HTTP 429 OVER_RATE_LIMIT** (limit 10) in testing, so register a free personal key ([api.nasa.gov](https://api.nasa.gov)) |
| SDO data via SunPy/Fido, JSOC (`drms`) | AIA/HMI images | JSOC needs email registration for exports (unverified) | [SunPy](https://github.com/sunpy/sunpy) |
| Surya S3 bucket `nasa-surya-bench` | ML-ready SDO NetCDF | None | [Surya README](https://github.com/NASA-IMPACT/Surya) |
| HAPI servers, ESA SWE portal, SpaceWeatherLive | Time series and portals | Varies | Leads, unverified |

### SunPy, aiapy, ndcube
- **SunPy:** ★1,047, BSD-2, **v8.0.1 (2026-10-09)** ([GitHub](https://github.com/sunpy/sunpy)). Fido search and download of SDO, SOHO, GOES and more; solar coordinate frames; Map plotting.
- **aiapy:** BSD-3, v0.12.1, for AIA calibration. The GitHub mirror is at LM-SAL ([GitHub](https://github.com/LM-SAL/aiapy)).
- **ndcube:** ★50, v2.4.2 ([GitHub](https://github.com/sunpy/ndcube)).
- **Hackathon effort:** About 30 minutes to pull and plot AIA 171 Å images of today's Sun.

**Other ML space-weather forecasters** (flare CNNs, CME arrival-time ML, Dst/Kp LSTMs, thermosphere-density ML for drag, e.g. MIT ARCLab's challenge) were not individually verified in this pass; they are listed under leads.

## 6. Astronomy ML

**State of play (Oct 2026).** Astronomy has three groups of tools:

1. **Multimodal foundation models.**
   - **AION-1** (Polymathic AI, 2025) is an omnimodal model over images, spectra and catalogues, installed with `pip install polymathic-aion`.
   - **AstroCLIP** builds a joint embedding space for galaxy images and spectra.
   - Both are trained on the 100 TB **Multimodal Universe**.
2. **Domain LLMs.** AstroSage-8B and AstroSage-70B, from AstroMLab.
3. **Production pipelines with public APIs.** Transient brokers ALeRCE and Fink, now multi-survey with ZTF and **Rubin LSST**, plus NASA's ExoMiner for exoplanet vetting, Zoobot for galaxy morphology, and lightkurve and astroquery for data access.

For a hackathon, the brokers and archives are the "live data" hook, and the FMs give "similarity search across the sky".

### Quick-pick (astronomy)

| Tool | Category | What it unlocks | Effort | License |
|---|---|---|---|---|
| AION-1 (Polymathic AI) | Omnimodal astronomy FM | Embed and cross-predict images, spectra and catalogue values (Legacy Survey, DESI, Gaia…) | ~1–2 hours (GPU) | MIT |
| AstroCLIP | Image↔spectrum contrastive FM | Cross-modal galaxy similarity search; Colab and Streamlit app | ~1 hour (Colab) | MIT |
| Multimodal Universe | 100 TB ML-ready astro dataset | `load_dataset('MultimodalUniverse/…')` streaming of images, spectra and light curves | ~30 min | MIT (repo) |
| Zoobot 2 | Galaxy-morphology models | Fine-tune a galaxy classifier on about 500 labels; free Colab | ~1 hour | GPL-3.0 code, Apache-2.0 HF encoders |
| AstroSage-8B / 70B | Astronomy LLMs | Domain Q&A and tutoring; benchmark-topping astronomy QA (70B) | Minutes (8B local) to hours (70B) | Llama 3.1 Community |
| ALeRCE client | Transient broker API (ZTF + LSST) | Classified light curves, stamps and crossmatches in pandas | ~15 min | MIT |
| Fink (broker + client) | Transient broker (Rubin-first) | Live alert streams (Kafka) and science-portal REST API | ~30 min | Apache-2.0 |
| ExoMiner pipeline (NASA) | Exoplanet vetting | TIC IDs → planet-candidate scores via a Podman image | ~1–2 hours | No license file |
| lightkurve | Kepler/TESS toolkit | Download and plot light curves; BLS transit search | ~15 min | MIT |
| astroquery + astropy | Archive access | MAST, Gaia, SDSS, SIMBAD and more in a few lines | ~15 min | BSD-3 |
| NASA Exoplanet Archive TAP | Catalogue API | ADQL over 40,350 planetary-system rows (tested) | Minutes | Public |

### AION-1 — AstronomIcal Omnimodal Network (Polymathic AI, 2025)
- **What it does:** A large omnimodal model for astronomical surveys. It tokenises each modality with codecs, such as Legacy Survey g/r/i/z images and spectra. It loads with `AION.from_pretrained('polymathic-ai/aion-base')`, with `aion-large` and `aion-xlarge` also listed ([GitHub](https://github.com/PolymathicAI/AION)).
- **Maturity:** ★155, MIT, v0.0.2 (2025-06-27), pushed 2026-08-31. HF `polymathic-ai/aion-base` is MIT with 1,335 dl/30d; `aion-large` was added 2026-04-08 (HF API).
- **Hackathon effort:** **1–2 hours** (`pip install polymathic-aion`, CUDA recommended).
- **Known limitations and complaints:** Early versions (v0.0.x). The codec and modality setup is survey-specific.
- **Example problem it unlocks:** "Find galaxies like this one and predict their redshift from an image alone". Or anomaly hunting in survey data.
- **Sources:** [PolymathicAI/AION](https://github.com/PolymathicAI/AION), [HF aion-base](https://huggingface.co/polymathic-ai/aion-base).

### AstroCLIP (Polymathic AI; MNRAS 2024)
- **What it does:** A cross-modal self-supervised model with a shared embedding space for multi-band galaxy images and optical spectra. It has a **Colab tutorial** and a **Streamlit similarity-search app** ([GitHub](https://github.com/PolymathicAI/AstroCLIP)).
- **Maturity:** ★183, MIT, pushed 2025-12-17.
- **Hackathon effort:** **~1 hour** via the Colab. A local install is painful, with pinned torch 2.0 + cu117, cuML and a pinned DINOv2 commit; it is "only tested… [on] Linux".
- **Sources:** [PolymathicAI/AstroCLIP](https://github.com/PolymathicAI/AstroCLIP), [app](https://astroclip.streamlit.app/).

### The Multimodal Universe (dataset and loaders)
- **What it does:** About 100 TB of multimodal astronomy data: images, spectra and light curves. Previews of about 1k examples per survey can be streamed from HF, e.g. `load_dataset('MultimodalUniverse/plasticc', streaming=True)`. The full data is at the Flatiron Institute via HTTPS or Globus ([GitHub](https://github.com/MultimodalUniverse/MultimodalUniverse)).
- **Maturity:** ★516, MIT, v1.5 (2026-06-17).
- **Hackathon effort:** **~30 minutes** for the streamed previews.
- **Known limitations and complaints:** Cross-matching utilities need the full local download.
- **Sources:** [MultimodalUniverse](https://github.com/MultimodalUniverse/MultimodalUniverse).

### Zoobot 2 (Mike Walmsley; Galaxy Zoo)
- **What it does:** Galaxy-morphology models trained on millions of Galaxy Zoo volunteer answers. Retrain for your own task, e.g. "find ringed galaxies" from about 500 labels. A free Colab notebook is provided ([GitHub](https://github.com/mwalmsley/zoobot)).
- **Maturity:** ★127, GPL-3.0 code, v2.9.0 (2025-07-25). HF encoders such as `zoobot-encoder-convnext_nano` are Apache-2.0 (HF API). The `galaxy-datasets` helper is ★67.
- **Hackathon effort:** **~1 hour.** It runs on CPU, slowly.
- **Sources:** [mwalmsley/zoobot](https://github.com/mwalmsley/zoobot).

### AstroSage-8B and AstroSage-70B (AstroMLab)
- **What it does:** Astronomy-specialised LLMs built on Llama-3.1 with continued pretraining on astronomical literature. AstroSage-70B (v1.0, released 2025-05-20) reports "benchmark-topping performance in astronomy Q&A" ([HF card](https://huggingface.co/AstroMLab/AstroSage-70B), [arXiv 2505.17592](https://arxiv.org/abs/2505.17592)).
- **Maturity:** The license is the Llama 3.1 Community License. HF downloads: 8B 623 dl/30d; 70B 20 dl/30d.
- **Hackathon effort:** The 8B runs locally or on a Colab GPU in **minutes**. The 70B needs multi-GPU or a hosted provider.
- **Known limitations and complaints:** It was fine-tuned on 8k-token sequences. It is a knowledge model, not grounded retrieval, so pair it with ADS/SciX for citations.
- **Sources:** [HF AstroSage-70B](https://huggingface.co/AstroMLab/AstroSage-70B), [HF AstroSage-8B](https://huggingface.co/AstroMLab/AstroSage-8B).

### ALeRCE (Chile) — transient broker and Python client
- **What it does:** A multi-survey client for **ZTF and LSST** covering objects, light curves (detections, non-detections, forced photometry), stamps, classifiers and catsHTM crossmatches. It returns JSON, pandas or VOTable ([GitHub](https://github.com/alercebroker/alerce_client)).
- **Maturity:** The client is ★9, MIT, v2.3.1 (2026-08-07). The public REST API `api.alerce.online/ztf/v1/objects/` responded in testing (it redirects to a trailing-slash URL).
- **Hackathon effort:** **~15 minutes.**
- **Example problem it unlocks:** A "supernova of the day" explainer or a follow-up prioritiser for amateur telescopes.
- **Sources:** [alercebroker/alerce_client](https://github.com/alercebroker/alerce_client).

### Fink — Rubin/ZTF alert broker
- **What it does:** A Spark-based broker whose "main scientific objective is to optimize the scientific impact of the Rubin Observatory alert data stream". It has science modules (classifiers), filters, a **Science Portal REST API**, and `fink-client` for Kafka livestreams. Separate docs exist for LSST and ZTF ([fink-broker](https://github.com/astrolabsoftware/fink-broker), [fink-client](https://github.com/astrolabsoftware/fink-client)).
- **Maturity:** fink-broker ★88, Apache-2.0, **v5.0.0 (2026-09-07)**. fink-client v12.3.0 (2026-10-09).
- **Hackathon effort:** **~30 minutes** for the REST portal. Livestream access requires registration (unverified).
- **Known limitations and complaints:** A REST endpoint guessed during this research timed out, so use the documented URLs from [doc.lsst.fink-broker.org](https://doc.lsst.fink-broker.org/).
- **Sources:** as linked.

### ExoMiner (NASA Ames)
- **What it does:** Deep-learning vetting and validation of transit signals from Kepler and TESS. The new **ExoMiner Pipeline** goes from TIC IDs to ExoMiner scores for TESS SPOC TCEs in 2-minute and FFI data, packaged as a **Podman image** ([GitHub](https://github.com/nasa/ExoMiner)).
- **Maturity:** ★95, no license file, v1.0.0 (2025-05-20), pushed 2026-10-13. Google's older `exoplanet-ml` (AstroNet) is **archived** ([GitHub](https://github.com/google-research/exoplanet-ml)).
- **Hackathon effort:** **1–2 hours** with Podman.
- **Example problem it unlocks:** "Vet this new TESS candidate", a citizen-science triage tool.
- **Sources:** [nasa/ExoMiner](https://github.com/nasa/ExoMiner).

### lightkurve, astroquery, astropy and the NASA Exoplanet Archive TAP
- **lightkurve:** ★546, MIT, v2.6.0 (2026-04-16). A friendly Kepler/TESS time-series package ([GitHub](https://github.com/lightkurve/lightkurve)).
- **astroquery:** ★800, BSD-3, v0.4.11. MAST, Gaia, SDSS, SIMBAD and more ([GitHub](https://github.com/astropy/astroquery)).
- **astropy:** ★5,359, BSD-3, v8.0.1 (2026-07-08) ([GitHub](https://github.com/astropy/astropy)).
- **NASA Exoplanet Archive TAP:** `https://exoplanetarchive.ipac.caltech.edu/TAP/sync?query=select+count(*)+from+ps&format=json` returned **40,350** rows in the `ps` table when tested on 2026-10-24.
- **Hackathon effort:** **Minutes.**

**Not verified in this pass:**
- AstroLLaMA
- Pathfinder (the UniverseTBD GitHub repo is ★0, so the live app is elsewhere)
- Lasair, ANTARES, AMPEL and Pitt-Google brokers
- Euclid Q1 ML catalogues
- Astronomaly
- GWOSC
- SETI ML

See leads.

## 7. Orbital mechanics, space situational awareness and 3D globes

**State of play (Oct 2026). The single most important fact in this category is new.** CelesTrak says **five-digit NORAD catalog numbers ran out on 2026-07-11**. Newly catalogued objects have six-digit numbers and **cannot be expressed in the TLE format at all**. Users must switch to OMM, the CCSDS Orbit Mean-Elements Message, in XML, JSON or CSV ([CelesTrak GP formats](https://celestrak.org/NORAD/documentation/gp-data-formats.php)).

Library support for OMM is mixed:
- **python-sgp4** has "experimental" OMM support.
- **satellite.js** (v7) supports OMM and calls it "preferred for new applications".
- **dSGP4** parses TLE and OMM.

Tools, tutorials and LLM-written code that assume TLEs will silently miss new objects. That is a concrete, timely problem and an easy demo hook.

For propagation, Skyfield and sgp4 (Python) or satellite.js (browser) take minutes. For a 3D visual, CesiumJS with satellite.js, or a fork of KeepTrack, is the standard hackathon look.

### Quick-pick (orbital, SSA, globes)

| Tool | Category | What it unlocks | Effort | License |
|---|---|---|---|---|
| CelesTrak GP API | Orbit data (no account) | Current elements for groups, e.g. active or starlink, in OMM JSON/XML/CSV or TLE | Minutes | Free (strict download etiquette) |
| Space-Track.org API + `spacetrack` client | Authoritative orbit catalogue | GP, GP_HISTORY, SATCAT, decay; CDMs only for operators | ~30 min (account) | Free account, usage policy |
| python-sgp4 | SGP4 propagator | Vectorised C++ propagation of thousands of objects; OMM support | Minutes | MIT |
| Skyfield | High-level astronomy/satellite library | Passes, look angles, sunlit checks, ground tracks | Minutes | MIT |
| satellite.js | SGP4 in JavaScript | Browser-side propagation of TLE/OMM for web globes | Minutes | MIT |
| CesiumJS (+ Resium) | 3D globe | Orbits, ground tracks, imagery overlays, 3D Tiles in the browser | ~1 hour | Apache-2.0 (ion services have quotas) |
| KeepTrack | Full open-source satellite-tracking web app | Fork a polished 3D tracker | ~1–2 hours | AGPL-3.0 |
| Orekit (Java) | Flight-dynamics library | Precise propagation, orbit determination, collision probability | Hours | Apache-2.0 |
| NASA GMAT | Mission-analysis tool | Trajectory and manoeuvre design (GUI and scripts) | Hours | Apache-2.0 |
| Basilisk | Spacecraft simulation framework | Attitude/orbit dynamics and GNC simulation | Hours | ISC |
| nyx-space / ANISE | Rust astrodynamics (Python bindings) | High-fidelity propagation, OD; SPICE alternative | Hours | AGPL-3.0 / MPL-2.0 |
| tudatpy, heyoka.py, pykep, SpiceyPy | Research astrodynamics | Interplanetary design, Taylor integration, SPICE kernels | Hours | BSD-3 / MPL-2.0 / MPL-2.0 / MIT |
| hapsira (poliastro fork) | Python orbital mechanics | Lambert, maneuvers, plots (poliastro is archived) | ~1 hour | MIT |
| dSGP4 (ESA) | Differentiable SGP4 in PyTorch | Batched GPU propagation; ML-corrected SGP4 | ~1 hour | GPL-3.0 |
| NASA CARA Analysis Tools | Conjunction-assessment SDK | Pc (probability of collision) computations from NASA's CARA team | Hours (MATLAB/Git LFS) | No license file |
| Kessler (ESA/FDL) | ML for collision avoidance | CDM handling, simulation-based inference | Hours | GPL-3.0 |
| gpredict, pyorbital | Pass prediction | Ground-station pass schedules | Minutes | GPL-2.0 / Apache-2.0 |
| OpenSpace | Astro-visualisation app | Cinematic solar-system and mission visualisation | Hours | MIT (NOASSERTION on GitHub) |

### 7.1 Propagation and astrodynamics libraries

#### python-sgp4 (Brandon Rhodes)
- **What it does:** The official SGP4 algorithm in Python. It computes "a whole array of output positions using a fast C++ loop" ("Array Acceleration") and reads TLE or, experimentally, OMM (`from sgp4 import omm`) ([GitHub](https://github.com/brandon-rhodes/python-sgp4)). The README notes the "1–3 km/day" by which real satellites deviate from SGP4's ideal orbits.
- **Maturity:** ★477, MIT, PyPI **2.27 (2026-07-03)**.
- **Hackathon effort:** **Minutes** (`pip install sgp4`).
- **Known limitations and complaints:** Accuracy is inherently a few km after days, so it is not good enough for real conjunction assessment. OMM support is labelled experimental.
- **Example problem it unlocks:** Propagate the whole active catalogue (about 10k+ objects) to find close approaches. Explain that a real screen needs covariance and high-precision ephemerides.
- **Sources:** [python-sgp4](https://github.com/brandon-rhodes/python-sgp4).

#### Skyfield (Brandon Rhodes)
- **What it does:** "Elegant astronomy for Python": satellite passes, alt/az, sunlit/eclipse checks, planets and stars.
- **Maturity:** ★1,795, MIT, PyPI **1.55 (2026-08-07)** ([GitHub](https://github.com/skyfielders/python-skyfield)).
- **Hackathon effort:** **Minutes.**
- **Example problem it unlocks:** "When can I see Starship or ISS tonight from Berkeley?", or astronomer-impact estimates of satellite streaks.
- **Sources:** [skyfielders/python-skyfield](https://github.com/skyfielders/python-skyfield).

#### satellite.js
- **What it does:** "Modular set of functions for SGP4 and SDP4 propagation of TLE and OMM" in JavaScript, with `json2satrec(omm)`. The README calls OMM "preferred for new applications" ([GitHub](https://github.com/shashwatak/satellite-js)).
- **Maturity:** ★1,097, MIT, **7.1.0 (2026-07-23)**.
- **Hackathon effort:** **Minutes.**
- **Sources:** [shashwatak/satellite-js](https://github.com/shashwatak/satellite-js).

#### Orekit (CS GROUP)
- **What it does:** A low-level Java space-dynamics library: propagators, orbit determination, events and frames. Its main home is CS GROUP's GitLab ([GitHub mirror](https://github.com/CS-SI/Orekit)).
- **Maturity:** ★304 on the mirror, Apache-2.0, **13.1.9 (2026-10-03)**. Python access is through wrappers (orekit-jpype / conda `orekit`; not verified in this pass).
- **Hackathon effort:** Hours, given the Java and JVM setup.
- **Sources:** [CS-SI/Orekit](https://github.com/CS-SI/Orekit).

#### NASA GMAT
- **What it does:** "The world's leading enterprise, multi-mission, open source" mission-analysis tool, now on GitHub ([nasa/GMAT](https://github.com/nasa/GMAT)).
- **Maturity:** ★138, Apache-2.0, pushed 2026-10-09. An older community fork by C. Rabotin is marked unmaintained.
- **Hackathon effort:** Hours. It is GUI-centric.
- **Sources:** [nasa/GMAT](https://github.com/nasa/GMAT).

#### Basilisk (AVS Lab, CU Boulder)
- **What it does:** An astrodynamics and spacecraft simulation framework with a C/C++ core and a Python interface ([GitHub](https://github.com/AVSLab/basilisk)).
- **Maturity:** ★411, ISC, v2.12.0 (2026-09-21).
- **Hackathon effort:** Hours (build).
- **Example problem it unlocks:** Attitude and GNC "digital twin" demos.

#### nyx-space and ANISE (Rust)
- **nyx:** "High fidelity, fast, reliable and validated astrodynamics toolkit" in Rust with Python bindings. ★501, **AGPL-3.0**, 2.6.0 (2026-09-12) ([GitHub](https://github.com/nyx-space/nyx)).
- **ANISE:** "A thread-safe alternative to NASA SPICE toolkit". ★285, MPL-2.0, 0.10.6 ([GitHub](https://github.com/nyx-space/anise)).

#### Research libraries: tudatpy, heyoka.py, pykep, SpiceyPy, Open Space Toolkit
- **tudatpy** (TU Delft): ★96, BSD-3. The GitHub "latest release" tag is old (0.6.0, 2022) but the repo was pushed 2026-10-24 ([GitHub](https://github.com/tudat-team/tudatpy)).
- **heyoka.py** (Taylor integrator via LLVM): ★92, MPL-2.0, v7.13.2 ([GitHub](https://github.com/bluescarni/heyoka.py)).
- **pykep** (ESA, interplanetary trajectory design): ★426, MPL-2.0, **v3.0.0 (2026-05-23)** ([GitHub](https://github.com/esa/pykep)).
- **SpiceyPy** (NASA NAIF SPICE wrapper): ★491, MIT, v8.3.0 (2026-10-11) ([GitHub](https://github.com/AndrewAnnex/SpiceyPy)).
- **Open Space Toolkit** (Loft Orbital; flight profile, orbit, attitude, access): ★82, Apache-2.0, 17.15.0 ([GitHub](https://github.com/open-space-collective/open-space-toolkit-astrodynamics)).

#### poliastro → hapsira
- **What it does:** **poliastro was archived in October 2023** (★1,018, last release v0.17.0, 2022) ([GitHub](https://github.com/poliastro/poliastro)). **hapsira** is the maintained fork (★44, MIT). It supports Python 3.8–3.11 and was waiting on numba for 3.12. Its last push was 2024-05-09, so it is also quiet ([GitHub](https://github.com/pleiszenburg/hapsira)).
- **Known limitations and complaints:** Many tutorials and LLM answers still use poliastro, which will not install on modern Python. Expect friction.

#### dSGP4 (ESA Advanced Concepts Team)
- **What it does:** **Differentiable SGP4 in PyTorch.** It provides batched and GPU propagation, gradients with respect to time and TLE parameters, TLE and OMM parsing and conversion, and `mldsgp4`, a hybrid ML correction of SGP4 ([GitHub](https://github.com/esa/dSGP4), Acta Astronautica 2025).
- **Maturity:** ★99, GPL-3.0, v1.5.1 (2026-10-16).
- **Hackathon effort:** **~1 hour.**
- **Example problem it unlocks:** "ML-corrected SGP4", i.e. better orbit predictions from public data, or fast whole-catalogue conjunction screening on a GPU.
- **Sources:** [esa/dSGP4](https://github.com/esa/dSGP4).

### 7.2 Orbit data sources and clients

#### CelesTrak GP API
- **What it does:** `https://celestrak.org/NORAD/elements/gp.php?{CATNR|INTDES|GROUP|NAME|SPECIAL}=…&FORMAT={TLE|2LE|XML|KVN|JSON|JSON-PRETTY|CSV}`. The default format is CSV. SPECIAL values include `GPZ`, `GPZ-PLUS` and `DECAYING` ([CelesTrak](https://celestrak.org/NORAD/documentation/gp-data-formats.php)).
- **Rules (important for hackathons):**
  - Data updates about every 2 hours.
  - **Only one download per data update**; repeats return HTTP 403.
  - Do not download overlapping sets; e.g. Starlink is a subset of Active.
  - Use `celestrak.org`, not `.com`.
  - **More than 50 HTTP errors in 2 hours can get your IP firewalled** ([CelesTrak](https://celestrak.org/NORAD/documentation/gp-data-formats.php)).

  Cache locally, and do not let a hot-reloading dev server hammer it.
- **Known limitations and complaints:** The catalog-number exhaustion described above. The FAQ rejects "alpha-5" letter-extended numbers as a fix.
- **Sources:** [CelesTrak GP data formats](https://celestrak.org/NORAD/documentation/gp-data-formats.php).

#### Space-Track.org API and the `spacetrack` Python client
- **What it does:** The US catalogue (GP, GP_HISTORY, SATCAT, decay). **Limits are under 30 requests per minute and 300 per hour.** GP queries should run at most hourly, at a random minute. CDMs (conjunction data messages) go to satellite owners and operators via a Primary Representative and are not public ([Space-Track API docs](https://www.space-track.org/documentation#/api)). The `spacetrack` client is ★93, MIT, 2.1.0 (2026-08-23) ([GitHub](https://github.com/python-astrodynamics/spacetrack)).
- **Hackathon effort:** About 30 minutes, including account creation; the delay is unverified.
- **Sources:** as linked.

### 7.3 Conjunction screening and collision probability

#### NASA CARA Analysis Tools
- **What it does:** An SDK from NASA's Conjunction Assessment Risk Analysis team with tools to assess close-approach risk, such as probability-of-collision (Pc) computations. **Since the January 2026 release, `.mat` files require Git LFS** ([GitHub](https://github.com/nasa/CARA_Analysis_Tools)).
- **Maturity:** ★110, no license file, pushed 2026-10-05.
- **Hackathon effort:** Hours. It is largely MATLAB with some Python (not verified per tool).
- **Example problem it unlocks:** A "conjunction explainer": take a (synthetic or public) CDM and compute and explain Pc and manoeuvre options.
- **Sources:** [nasa/CARA_Analysis_Tools](https://github.com/nasa/CARA_Analysis_Tools).

#### Kessler (ESA ESOC + FDL Europe)
- **What it does:** "Simulation-based inference and machine learning for space collision avoidance and assessment" ([GitHub](https://github.com/kesslerlib/kessler)).
- **Maturity:** ★68, GPL-3.0, v1.0.1 (2025-04-24).
- **Hackathon effort:** Hours.
- **Example problem it unlocks:** CDM time-series risk forecasting, as in ESA's Kelvins collision-avoidance challenge (lead).
- **Sources:** [kesslerlib/kessler](https://github.com/kesslerlib/kessler).

**Others (leads, not verified):**
- CelesTrak SOCRATES conjunction reports
- Orekit's collision-probability methods
- CCSDS CDM parsers
- Commercial screening services (LeoLabs, Slingshot, Privateer)

The space-traffic slice covers the problem side.

### 7.4 3D globes and visualisation

#### CesiumJS and Resium
- **What it does:** An open-source JavaScript library for "world-class 3D globes and maps". It has CZML time-dynamic entities, which suit orbits ([GitHub](https://github.com/CesiumGS/cesium)). Resium provides React components ([GitHub](https://github.com/reearth/resium)).
- **Maturity:** CesiumJS ★15,880, Apache-2.0, **1.146 (2026-10-01)**. Resium ★885, MIT, v1.27.0.
- **Cesium ion free "Community" plan:**
  - 10 GB storage
  - 15 GB/month streaming
  - 1,000 global-imagery sessions/month
  - 1,000 Google Photorealistic 3D Tiles root tiles/month
  - 50,000 geocodes/month
  - for "personal and non-commercial use"; organisations with over $50K revenue or funding must pay

  Commercial plans start at $149/month ([Cesium pricing](https://cesium.com/platform/cesium-ion/pricing/)).
- **Hackathon effort:** **~1 hour** for orbits on a globe with satellite.js.
- **Known limitations and complaints:** The ion token and quotas apply. A judging-day traffic spike could exhaust free imagery sessions; pre-test, or use self-hosted imagery tiles.
- **Sources:** as linked.

#### KeepTrack and Stuff in Space
- **KeepTrack:** "TypeScript Astrodynamics Software for Non-Engineers. 3D visualization of satellite data". ★1,618, **AGPL-3.0**, pushed 2026-10-19 ([GitHub](https://github.com/thkruz/keeptrack.space)).
- **Stuff in Space:** a real-time WebGL visualisation of orbital objects. ★834, no license file, last push 2024-01-09 ([GitHub](https://github.com/jeyoder/StuffInSpace)).
- **Hackathon value:** Fork KeepTrack for a polished UI in an hour, but the AGPL obligations apply.

#### OpenSpace and NASA WorldWind
- **OpenSpace** (AMNH/NASA astro-visualisation): ★1,289, v0.22.0 (2026-06-12) ([GitHub](https://github.com/OpenSpace/OpenSpace)).
- **Web WorldWind:** last release v0.11.0 in 2022, effectively dormant ([GitHub](https://github.com/NASAWorldWind/WebWorldWind)).

### 7.5 Pass prediction and ground stations
- **gpredict:** a desktop satellite tracker. ★1,196, GPL-2.0, v2.6 (2026-08-16) ([GitHub](https://github.com/csete/gpredict)).
- **pyorbital** (pytroll): orbital and astronomy computations for weather-satellite passes. ★260, Apache-2.0, v1.14.0 (2026-10-12) ([GitHub](https://github.com/pytroll/pyorbital)).
- **sat_code** (Bill Gray, C SGP4/SDP4 and TLE tools): ★177, MIT ([GitHub](https://github.com/Bill-Gray/sat_code)).
- **SatNOGS DB:** the GitHub mirror `satnogs/satnogs-db` is archived (2018). Development is on GitLab (unverified).

## 8. Geospatial data stack

**State of play (Oct 2026).** The open cloud-native stack is mature. Data comes from STAC catalogues of Cloud-Optimized GeoTIFFs (COGs) on AWS (Element 84 Earth Search), Microsoft Planetary Computer and Copernicus Data Space. You load it lazily with `pystac-client` + `odc-stac` (or `stackstac`) into `xarray`, process it, and show it with leafmap, lonboard or deck.gl/MapLibre, using titiler for tiles. For vectors, use GeoParquet + DuckDB spatial. Earth Engine plus geemap is the "no download" alternative.

Two live checks were done on 2026-10-24:
- **Earth Search v1** lists `sentinel-2-l2a`, `sentinel-2-c1-l2a`, `sentinel-2-l1c`, `sentinel-1-grd`, `landsat-c2-l2`, `naip` and `cop-dem-glo-30/90`.
- **Planetary Computer's STAC API is live with 139 collections**, including:
  - optical: `sentinel-2-l2a`, `hls2-l30`/`hls2-s30`, `landsat-c2-l2`
  - atmosphere and weather: `sentinel-5p-l2`, `goes-cmi`, `goes-glm`, `era5-pds`, `ecmwf-forecast`
  - fire: `modis-14A1-061`, `mtbs`
  - buildings and imagery: `ms-buildings`, `planet-nicfi-*`
  - 2026 damage-prediction layers: `predicted-damage-colombia-2026` and `predicted-damage-venezuela-2026`

### Quick-pick (geospatial stack)

| Tool | Category | What it unlocks | Effort | License |
|---|---|---|---|---|
| Earth Search (Element 84) STAC | Free STAC API over AWS Open Data | S2 L2A COGs, Landsat, S1, NAIP, Copernicus DEM with no auth | Minutes | Free (data licenses vary) |
| Microsoft Planetary Computer STAC | Free STAC API | 139 collections incl. GOES, S5P, ERA5, HLS, MODIS | Minutes (SAS token signing via `planetary-computer` package) | Free (data licenses vary) |
| Copernicus Data Space (CDSE) + Sentinel Hub / openEO | ESA's official access | All Sentinels; 10k Sentinel Hub PUs/month; 10k openEO credits/month | ~30 min (free account) | Free quotas |
| Google Earth Engine + geemap | Hosted planetary analysis | Petabyte catalog incl. AlphaEarth, Cloud Score+, WeatherNext; 150 EECU-h/month free | ~30 min (Cloud project) | Noncommercial free |
| NASA earthaccess | NASA Earthdata search/download/stream | HLS, EMIT, GEDI, MODIS, ICESat-2, SWOT… | ~30 min (Earthdata login) | MIT |
| pystac-client + odc-stac / stackstac | STAC → xarray | Lazy time series of COGs | ~30 min | Apache-2.0 / MIT |
| rasterio, GDAL, xarray, rioxarray | Raster core | Read/write/reproject anything | Minutes | BSD/MIT-style, Apache-2.0 |
| Zarr / GeoZarr / Icechunk / obstore | Cloud arrays | Fast chunked cubes on S3/GCS | ~1 hour | MIT / CC-BY-4.0 / Apache-2.0 / MIT |
| TorchGeo | Geospatial PyTorch | Datasets, samplers, pretrained EO weights (DOFA, Panopticon…) | ~1 hour | MIT |
| eo-learn | EO processing framework | Sentinel Hub-based ML pipelines | ~1 hour | MIT |
| leafmap / geemap | Python interactive maps | Split-panel maps, COG/STAC layers, Streamlit/Solara apps | Minutes | MIT |
| lonboard | GPU maps in Jupyter (deck.gl + GeoArrow) | Millions of points/polygons interactively | Minutes | MIT |
| deck.gl / kepler.gl / MapLibre GL JS | Web map rendering | Production-style web map UIs | ~1 hour | MIT / MIT / BSD-3 |
| titiler | Dynamic tile server | Serve COGs/STAC as web tiles (FastAPI) | ~30 min | MIT |
| DuckDB spatial + GeoParquet | Vector analytics | SQL over Overture/buildings parquet on S3 | Minutes | MIT / Apache-2.0 |
| PMTiles / martin / tippecanoe | Vector tiles | Static-hosted map tiles | ~1 hour | BSD-3 / Apache-2.0 / BSD-2 |
| Streamlit / Gradio / Dash | Python app UIs | Demo front ends in hours | Minutes | Apache-2.0 / Apache-2.0 / MIT |

### Data access

#### Element 84 Earth Search (STAC API v1)
- **What it does:** A "free-to-use STAC API" over the Registry of Open Data on AWS. It covers USGS Landsat Collection 2, Sentinel-2, Sentinel-1, Copernicus DEM and NAIP. It includes a console and an ingestion dashboard ([Element 84](https://element84.com/earth-search/)). The endpoint `https://earth-search.aws.element84.com/v1` was tested and returned the 9 collections listed above. The Sentinel-2 C1 L2A collection is the newer processing baseline.
- **Hackathon effort:** **Minutes**, with no key.
- **Known limitations and complaints:** It hosts both `sentinel-2-l2a` and `sentinel-2-c1-l2a`, which is easy to confuse. NAIP covers only the US.
- **Sources:** [Element 84 Earth Search](https://element84.com/earth-search/), [issue tracker](https://github.com/Element84/earth-search), [FilmDrop UI](https://github.com/Element84/filmdrop-ui) (★34, v7.0.0).

#### Microsoft Planetary Computer (public STAC + data)
- **What it does:** A STAC API at `planetarycomputer.microsoft.com/api/stac/v1` with **139 collections** (live list fetched 2026-10-24). The examples repo ★461 was pushed 2026-09-24 ([GitHub](https://github.com/microsoft/PlanetaryComputerExamples)). Planetary Computer Pro / GeoCatalog is the commercial Azure product used by Planetary Explorer ([GitHub](https://github.com/microsoft/Planetary-Explorer)).
- **Hackathon effort:** **Minutes** (`pip install pystac-client planetary-computer`).
- **Known limitations and complaints:** The hosted JupyterHub compute environment was retired in 2024 (unverified here; the homepage did not render via fetch). Data assets need SAS-token signing.
- **Sources:** as linked.

#### Copernicus Data Space Ecosystem (CDSE), with Sentinel Hub and openEO
- **What it does:** ESA's official Sentinel access through STAC/OData/S3 downloads, Sentinel Hub APIs and the openEO API.
- **Free quotas** ("Copernicus General Users") ([CDSE quotas](https://documentation.dataspace.copernicus.eu/Quotas.html)):
  - **Sentinel Hub:** 10,000 processing units and 10,000 requests per month (300/minute), plus 50,000 direct COG requests per month.
  - **openEO:** 10,000 credits per month ("temporary boost"), 2 concurrent jobs.
  - **Downloads:** 12 TB/month at 20 MB/s per connection, 4 concurrent connections. Access tokens last 10 minutes.
- **Clients:**
  - `sentinelhub-py`: ★912, MIT, v3.12.0 (2026-09-16) ([GitHub](https://github.com/sentinel-hub/sentinelhub-py)).
  - `openeo` Python client: ★219, Apache-2.0, v0.53.0 (2026-10-06) ([GitHub](https://github.com/Open-EO/openeo-python-client)).
  - `eo-learn`: ★1,255, MIT, last release v1.5.7 (2024) ([GitHub](https://github.com/sentinel-hub/eo-learn)).
- **Hackathon effort:** **~30 minutes** (free account, no credit card per the Galileo README).
- **Known limitations and complaints:** The 10-minute token lifetime trips long scripts. Data Workspace (offline) orders are limited to 1 concurrent.

#### Google Earth Engine (+ geemap, Xee)
- **What it does:** Hosted petabyte-scale analysis with the AlphaEarth embeddings, Cloud Score+, WeatherNext and most public EO data. Noncommercial projects register instantly. **Community tier: 150 EECU-hours/month. Contributor: 1,000 (needs a billing account, not charged). Partner: 100,000 (application, climate-focused)** ([EE access](https://developers.google.com/earth-engine/guides/access), [tiers](https://developers.google.com/earth-engine/guides/noncommercial_tiers)). Since Sep 2025 noncommercial projects must complete an eligibility questionnaire and reverify periodically.
- **Libraries:**
  - `earthengine-api`: ★3,462, Apache-2.0, v1.7.49 (2026-10-19) ([GitHub](https://github.com/google/earthengine-api)).
  - **geemap**: ★4,049, MIT, v0.38.9 ([GitHub](https://github.com/gee-community/geemap)).
  - **Xee** (Earth Engine → xarray): ★377, Apache-2.0, v0.1.2. "v0.1.0 includes a major refactor with breaking API changes", so old snippets break ([GitHub](https://github.com/google/Xee)).
- **Hackathon effort:** **~30 minutes.**
- **Known limitations and complaints:** Over-quota projects go into a "restricted mode" with limited concurrency. Commercial use needs a paid plan.

#### NASA earthaccess
- **What it does:** Search, download or **stream** NASA Earthdata (CMR) with a few lines of code, built out of NASA Openscapes workshops ([GitHub](https://github.com/earthaccess-dev/earthaccess)).
- **Maturity:** ★646, MIT, v0.19.0 (2026-09-04). The repo moved from `nsidc/earthaccess` to `earthaccess-dev/earthaccess`.
- **Hackathon effort:** **~30 minutes** (free Earthdata Login).
- **Example problem it unlocks:** EMIT methane and minerals, GEDI forest structure, ICESat-2 ice and SWOT water levels, i.e. NASA-only datasets.

### Loading and processing
- **pystac-client** (★211, v0.9.1, 2026-10-20) and **pystac** (★469, v1.15.2) ([GitHub](https://github.com/stac-utils/pystac-client)).
- **odc-stac** (★206, Apache-2.0, v0.5.3) loads STAC items into xarray ([GitHub](https://github.com/opendatacube/odc-stac)).
- **stackstac** (★272, MIT) is **stale since v0.5.1 (Aug 2024)** ([GitHub](https://github.com/gjoseph92/stackstac)), so prefer odc-stac.
- **rustac** (Rust STAC tooling, ★147) ([GitHub](https://github.com/stac-utils/rustac)).
- Open Data Cube core (★593, 1.9.22).
- **rasterio** ★2,585, 1.5.2 (2026-09-30).
- **GDAL** ★6,115, v3.13.3 (2026-08-18).
- **xarray** ★4,215, v2026.09.0.
- **rioxarray** ★626, 0.23.0. The repo is now `vylor/rioxarray` (GitHub redirect from corteva).
- **geopandas** ★5,284, v1.2.0.
- **dask-geopandas** v0.5.0.
- **Zarr-python** ★2,078, MIT, **v3.4.1**.
- **GeoZarr spec** (★219, CC-BY-4.0, draft conventions).
- **Icechunk** (Earthmover; transactional Zarr storage): ★696, Apache-2.0, **v2.3.0** ([GitHub](https://github.com/earth-mover/icechunk)).
- **obstore** (Rust-backed S3/GCS/Azure I/O): ★829, MIT ([GitHub](https://github.com/developmentseed/obstore)).

All stars and versions are from the GitHub API on 2026-10-24.

- **TorchGeo** (now the `torchgeo` org): ★4,211, MIT, **v0.10.1 (2026-09-29)**. Datasets, samplers, transforms and pretrained weights; DOFA and Panopticon are included ([GitHub](https://github.com/torchgeo/torchgeo)).

### Visualisation and UI
- **leafmap** (★3,788, MIT, v0.63.1) and **geemap**. Leafmap is "a Python package for geospatial analysis and interactive mapping in a Jupyter environment" and can be deployed as Streamlit or Solara apps ([GitHub](https://github.com/opengeos/leafmap)). A multipage Streamlit geospatial template is available ([opengeos/streamlit-geospatial](https://github.com/opengeos/streamlit-geospatial), ★1,032).
- **lonboard** (Development Seed): ★973, MIT, v0.17.0. It builds on GeoArrow, GeoParquet and **GPU rendering via deck.gl** to show millions of features in Jupyter ([GitHub](https://github.com/developmentseed/lonboard)).
- **deck.gl** ★14,697, v9.4.0. **kepler.gl** ★12,062, v3.3.0-alpha.18. **MapLibre GL JS** ★11,932, v6.15.0. These are the standard web map stack ([deck.gl](https://github.com/visgl/deck.gl), [kepler.gl](https://github.com/keplergl/kepler.gl), [MapLibre](https://github.com/maplibre/maplibre-gl-js)).
- **titiler** (Development Seed): ★1,195, MIT, **2.4.0**. FastAPI dynamic tiling for COG and STAC ([GitHub](https://github.com/developmentseed/titiler)). eoAPI bundles STAC + raster + vector services (★335) ([GitHub](https://github.com/developmentseed/eoAPI)). stac-fastapi is ★325, 7.0.0. STAC Browser is ★429, v5.1.0.
- **DuckDB spatial** (★720, MIT; its README still says "work in progress") ([GitHub](https://github.com/duckdb/duckdb-spatial)). **GeoParquet** spec v2.0.0-rc.1 (2026-07-19) ([GitHub](https://github.com/opengeospatial/geoparquet)).
- **PMTiles** ★3,096. **martin** tile server ★4,021, v1.16.0. **tippecanoe** (Felt fork) ★1,625, 2.79.0 ([PMTiles](https://github.com/protomaps/PMTiles), [martin](https://github.com/maplibre/martin), [felt/tippecanoe](https://github.com/felt/tippecanoe)). Felt's hosted map platform itself was not evaluated (unverified).
- **App frameworks:**
  - Streamlit: ★46,093, 1.66.1.
  - Gradio: ★43,867, gradio@6.30.0.
  - Dash: ★24,468, v4.4.1.
  - GeoViews: ★637, v1.16.0.
- **Hackathon effort:** Minutes to an hour each.
- **Known limitations and complaints:** WebGL map stacks plus a Python backend means two languages. For a 36-hour build, Streamlit + leafmap, or a Next.js + MapLibre/deck.gl front end (Cursor writes this well), are the pragmatic choices.

## 9. Literature and knowledge tools

**State of play (Oct 2026).** The space literature is well covered by free APIs. **NASA ADS** (now fronted by the **SciX / Science Explorer** UI) covers astrophysics, heliophysics, planetary and Earth science, and needs a token with 5,000 queries/day by default. **arXiv** is free at 1 request per 3 seconds. **Semantic Scholar** and **OpenAlex** have free keyed tiers; OpenAlex now meters usage by money. For retrieval, NASA/IBM's **INDUS** embedding models are tuned on NASA Science Mission Directorate text. For "read the literature for me", **PaperQA2** is the most mature open agent and produces citations.

### Quick-pick (literature)

| Tool | Category | What it unlocks | Effort | License / terms |
|---|---|---|---|---|
| NASA ADS / SciX API | Bibliographic search over astro/helio/planetary/earth science | Full-text-indexed search, metrics, export; 5,000 req/day per token | ~15 min (token) | Free with token |
| arXiv API (+ OAI-PMH, S3 bulk) | Preprint search/metadata | Query astro-ph, physics.space-ph, cs.CV etc. | Minutes | Metadata CC0; 1 req/3 s |
| Semantic Scholar API | Citation graph + SPECTER2 embeddings + recommendations | Paper graph, embeddings, bulk datasets | Minutes (key recommended) | S2 API license |
| OpenAlex API | Open scholarly graph | Works/authors/institutions; new key-based daily budgets | Minutes | Free key ($1/day budget) |
| INDUS (nasa-smd-ibm-v0.1, Indus-Retriever st-v2) | NASA-science language models | Better retrieval over NASA science text (RAG embeddings) | ~15 min | Apache-2.0 |
| PaperQA2 (FutureHouse) | Agentic RAG with citations | "Answer this question from these 200 PDFs" | ~1 hour | Apache-2.0 |
| Ai2 Scholar QA lib / Asta | Literature QA system | Multi-step scholarly answers (docker or package) | ~1–2 hours | Apache-2.0 |
| STORM / GPT-Researcher | Report-writing research agents | Wikipedia-style or deep-research reports with citations | ~1 hour | MIT / Apache-2.0 |
| arxiv.py, `ads`, `semanticscholar`, pyalex | Python clients | Fast wrappers | Minutes | MIT |

### NASA ADS API / SciX (Science Explorer)
- **What it does:** The ADS developer API at `https://api.adsabs.harvard.edu/v1/search/query?q=…`. Every request needs an `Authorization: Bearer <token>` header, with a key generated in the user profile. **Each endpoint is individually rate-limited, e.g. `X-RateLimit-Limit: 5000` daily**, resetting at midnight UTC ([adsabs-dev-api](https://github.com/adsabs/adsabs-dev-api)). Without a token the API returned **HTTP 401** in testing. SciX ([scixplorer.org](https://scixplorer.org/)) is the expanded multi-discipline UI on the same backend; its page did not render via fetch, so the details are unverified. Python client: `ads` (★191, MIT) ([GitHub](https://github.com/andycasey/ads)).
- **Hackathon effort:** **~15 minutes.**
- **Known limitations and complaints:** The daily quota is per token. Full text is indexed but not always redistributable.
- **Example problem it unlocks:** A "mission-literature copilot" that finds every paper using SDO/AIA data on flare prediction since 2020 and summarises the methods. Combine it with Surya.

### arXiv API
- **What it does:** Atom-feed search (`export.arxiv.org/api/query?search_query=…`), tested working on 2026-10-24. The terms ask clients to "make no more than one request every three seconds" over a single connection, across all machines you control. **Metadata is CC0**. E-prints remain under their authors' copyright, so do not re-host PDFs; bulk full text is via S3 ([arXiv API ToU](https://info.arxiv.org/help/api/tou.html)). Client: `arxiv.py` (★1,553, MIT, **4.0.1**, 2026-07-31) ([GitHub](https://github.com/lukasschwab/arxiv.py)).
- **Hackathon effort:** **Minutes.**

### Semantic Scholar API
- **What it does:** The Academic Graph (papers, authors, citations) with **SPECTER2 embeddings**, a Recommendations API, and the Datasets API (S2AG bulk JSON). Unauthenticated use shares "1000 requests per second shared among all unauthenticated users"; a key gives an introductory "1 RPS on all endpoints" ([S2 API](https://www.semanticscholar.org/product/api)). **An unauthenticated test on 2026-10-24 got HTTP 429 "Too Many Requests"**, so request a key early. Client: `semanticscholar` (★484, MIT) ([GitHub](https://github.com/danielnsilva/semanticscholar)).
- **Hackathon effort:** Minutes once a key is issued. Key turnaround is not stated (unverified).

### OpenAlex API
- **What it does:** An open scholarly graph. **The 2026 API response notice:** with no key, requests share one free daily budget ($0.10) with everyone on your IP address, while a free personal key gives "$1/day" (seen in the live API response on 2026-10-24, [api.openalex.org](https://api.openalex.org/works?search=space%20debris)). Client: `pyalex` (★427, MIT, v0.21) ([GitHub](https://github.com/J535D165/pyalex)).
- **Hackathon effort:** Minutes. Get a key, because hackathon Wi-Fi shares one IP.

### INDUS — NASA/IBM science language models
- **What it does:** Encoders trained for NASA Science Mission Directorate domains.
  - `nasa-impact/nasa-smd-ibm-v0.1`: the encoder, 746 dl/30d.
  - **Indus-Retriever `nasa-smd-ibm-st-v2`**: a 125M sentence-transformer fine-tuned on about 271M sentence pairs plus 2.6M NASA SMD title/abstract pairs, for retrieval. It is evaluated on BEIR and the NASA-IR benchmark (`nasa-impact/nasa-smd-IR-benchmark` dataset).
  - A distilled 38M version is available.

  Weights are Apache-2.0 and the model is labelled experimental ([HF card](https://huggingface.co/nasa-impact/nasa-smd-ibm-st-v2), [arXiv 2405.10725](https://arxiv.org/abs/2405.10725)).
- **Hackathon effort:** **~15 minutes** (`SentenceTransformer("nasa-impact/nasa-smd-ibm-st-v2")`). The card's snippet has an import typo (`Util` vs `util`).
- **Example problem it unlocks:** Domain-tuned embeddings for a RAG over NASA mission documents, the lessons-learned database or ADS abstracts.

### NASA Science Discovery Engine (SDE)
- **What it does:** NASA SMD's search over science data, documents, software and mission pages. The old domain redirects to `science.data.nasa.gov/science-discovery-engine/search/`, but the page did not render via fetch. NASA-IMPACT's 2026 repos (`sde-curation-engine`, `sde-crawl4ai-scraper`) show active development ([NASA-IMPACT GitHub](https://github.com/NASA-IMPACT)). A public API was not verified.
- **Related NASA-IMPACT 2026 releases** seen in the org listing (lead):
  - `veda-ui-mcp`, an **MCP server for the VEDA STAC catalog**
  - `akd-agentic-eo-berlin-2026` ("EO MCP tools")
  - `astroakd-bench`, a benchmark for data-search agents
  - `geospatial-studio`

### PaperQA2 (FutureHouse)
- **What it does:** "High accuracy RAG for answering questions from scientific documents with citations". It works over PDFs, text, Office files and code, with agentic search, contradiction detection and summarisation ([GitHub](https://github.com/Future-House/paper-qa)). It uses **CalVer since Dec 2025** (e.g. `v2026.08.12`); "PaperQA2" means `paper-qa>=5` and requires Python 3.11+.
- **Maturity:** ★9,461, Apache-2.0, pushed 2026-10-20.
- **Hackathon effort:** **~1 hour.** `pip install paper-qa`, then set an LLM key. Any LiteLLM-compatible model should work, including Grok through an OpenAI-compatible base URL (unverified). The README advises metadata-service API keys to avoid public rate limits.
- **Known limitations and complaints:** CalVer removes backward-compatibility guarantees, per the maintainers. Cost and latency rise with corpus size.
- **Example problem it unlocks:** "Ask 500 papers on space-debris removal what actually works", with cited answers.

### Other research agents and tools
- **Ai2 Scholar QA:** ★287, Apache-2.0. The code behind [scholarqa.allen.ai](https://scholarqa.allen.ai/), runnable as docker or the `ai2-scholar-qa` package ([GitHub](https://github.com/allenai/ai2-scholarqa-lib)). Ai2's **asta-bench** is ★142 ([GitHub](https://github.com/allenai/asta-bench)).
- **STORM** (Stanford OVAL): ★31,689, MIT. Writes cited, Wikipedia-style reports; last push 2025-09-30 ([GitHub](https://github.com/stanford-oval/storm)).
- **GPT-Researcher:** ★30,282, Apache-2.0, v3.7.0 (2026-09-26). "Deep research on any data using any LLM providers" ([GitHub](https://github.com/assafelovic/gpt-researcher)).
- **arxiv-sanity-lite** (Karpathy): ★1,708, stale since 2023 ([GitHub](https://github.com/karpathy/arxiv-sanity-lite)).
- **astro-ph knowledge graph** (Y.-S. Ting): ★15 ([GitHub](https://github.com/tingyuansen/astro-ph_knowledge_graph)).
- **Not verified:** Elicit, Consensus, Scite, Undermind, NotebookLM, NASA NTRS API, NASA Lessons Learned (LLIS) export, Papers with Code successors.

### API limits cheat-sheet

| API | Auth | Limit | Bulk option | Source |
|---|---|---|---|---|
| NASA ADS / SciX | Bearer token | 5,000/day per endpoint (default) | Export endpoints | [adsabs-dev-api](https://github.com/adsabs/adsabs-dev-api) |
| arXiv API | None | 1 request / 3 s, single connection | S3 full text, OAI-PMH | [ToU](https://info.arxiv.org/help/api/tou.html) |
| Semantic Scholar | Optional key | 1000 RPS shared (unauth); 1 RPS intro with key | S2AG datasets | [S2 API](https://www.semanticscholar.org/product/api) |
| OpenAlex | Free key | $0.10/day shared per IP without key; $1/day with key | Snapshot (unverified) | live API notice |
| NASA api.nasa.gov (DONKI etc.) | Key (DEMO_KEY exists) | DEMO_KEY hit 429 at limit 10 in testing | — | tested |

## 10. Hosted inference and compute

**State of play (Oct 2026).** For a 36-hour build, the binding constraints are GPU access and API quotas, not model quality. The recommended split:
- **Grok** (included via the SpaceXSI X Premium offer, and a judging bonus) for reasoning, vision Q&A and X/web search.
- **Colab or Kaggle** free GPUs, or **Modal** ($30/month free), for SAM 3, YOLO, Surya and Prithvi.
- **Earth Engine / Planetary Computer / Earth Search / Open-Meteo** so you never download raw data.

### Quick-pick (inference and compute)

| Service | What it gives | Free amount | Friction | Source |
|---|---|---|---|---|
| xAI Grok API | grok-4.7 etc. with image input; web/X search, code execution, collections; OpenAI-compatible | No free credits stated; X Premium for attendees includes "Grok" (API credit coverage unverified) | API key, prepaid credits | [docs.x.ai](https://docs.x.ai/docs/models), starter pack |
| Modal | Serverless GPUs (T4→B200) per second | **$30/month** Starter credits; academics can apply for up to $10k | Account (card requirement not stated) | [Modal pricing](https://modal.com/pricing) |
| Hugging Face Inference Providers | 200+ hosted models via one router (OpenAI-compatible) | **None for free users; $2/month for PRO**, also spendable on ZeroGPU beyond quota, Endpoints, Jobs | HF token | [HF pricing](https://huggingface.co/docs/inference-providers/pricing) |
| Google Colab | Free GPU notebooks (T4 typical), TPU v5e-1 runtime | Free tier (limits not published) | Google account | WeatherNext README mentions free v5e-1 ([GitHub](https://github.com/google-deepmind/weathernext)); other details unverified |
| Kaggle Notebooks | Free GPUs (P100 / 2×T4) | About 30 GPU-h/week historically (unverified) | Phone verification (unverified) | — |
| Google Earth Engine | Server-side compute on the EE catalog | 150 EECU-h/month (Community) or 1,000 (Contributor) | Cloud project + questionnaire | [EE tiers](https://developers.google.com/earth-engine/guides/noncommercial_tiers) |
| Copernicus Data Space | Sentinel Hub / openEO processing | 10k PUs + 10k openEO credits/month | Free account | [CDSE quotas](https://documentation.dataspace.copernicus.eu/Quotas.html) |
| Open-Meteo | Weather incl. WeatherNext 2 ensemble | Free non-commercial (limits not stated on the WeatherNext page) | None | [Open-Meteo](https://open-meteo.com/en/docs/google-weathernext-api) |
| Cesium ion | Globe imagery/terrain/3D tiles | 15 GB/month streaming, 1,000 imagery sessions | Token | [Cesium pricing](https://cesium.com/platform/cesium-ion/pricing/) |
| Gemini API (AI Studio) | Gemini with image/video input | Free tier exists; limits shown per project in AI Studio | Google account | [Gemini rate limits](https://ai.google.dev/gemini-api/docs/rate-limits) |
| Replicate | Hosted open models (SAM/YOLO-style) | Not verified | Card | — |

### xAI Grok API (see §2 for full detail)
- **Hackathon role:** The orchestrator and explainer.
  - Image understanding for screenshots, quick-look PNGs and plots. Send rendered false-colour composites, not raw multispectral data.
  - **X Search** for real-time ground truth: people posting about a flood, launch or outage.
  - **Collections Search** for RAG over mission docs.
  - Code execution.
  - Function calling into your geospatial tools.
- **Facts:** Base URL `https://api.x.ai/v1` (OpenAI SDK compatible). grok-4.7 costs $2/$6 per 1M input/output tokens with 500k context. Images are JPG/PNG up to 20 MiB. Tier 0 allows 150 RPS / 50M TPM ([models](https://docs.x.ai/docs/models), [image guide](https://docs.x.ai/docs/guides/image-understanding), [rate limits](https://docs.x.ai/docs/key-information/consumption-and-rate-limits)). The Python SDK `xai-sdk` is v1.21.0 ([GitHub](https://github.com/xai-org/xai-sdk-python)). Grok-1 open weights (2024) remain on GitHub, ★52,214, Apache-2.0 ([GitHub](https://github.com/xai-org/grok-1)), but are irrelevant for a hackathon.
- **Grok Bot:** The desktop app at x.ai/bot, which the starter pack says to download for "project planning and team collaboration" bonus points. The page returned HTTP 403 to automated fetch, so its features are unverified.

### Modal
- **What it does:** Serverless Python with GPUs billed per second. Rates per hour (derived from the page's per-second prices):

  | GPU | Price |
  |---|---|
  | T4 | ≈ $0.59/h |
  | L4 | ≈ $0.80/h |
  | A100-40GB | ≈ $2.10/h |
  | A100-80GB | ≈ $2.50/h |
  | H100 | ≈ $3.95/h |
  | B200 | ≈ $6.25/h |

  **The Starter plan includes $30/month free compute.** Academics can apply for up to $10k in credits ([Modal pricing](https://modal.com/pricing)).
- **Hackathon effort:** **~30 minutes** to wrap a SAM 3 or Surya inference function as an HTTPS endpoint the front end can call.
- **Example:** About 7 hours of H100 time fit in the free $30; the T4 is enough for YOLO, SAM 2 and Prithvi-300M.

### Hugging Face (Hub, Spaces, Inference Providers)
- **What it does:** Hosting for weights and datasets (most models in this report), Spaces demos (TEOChat, Prithvi, Major TOM viewer), and Inference Providers routing to 200+ models. **Free users get no monthly inference credits; PRO gets $2/month**, usable on ZeroGPU beyond quota, Endpoints and Jobs. `hf-inference` focuses mostly on CPU models as of July 2025 ([HF pricing](https://huggingface.co/docs/inference-providers/pricing)).
- **Hackathon effort:** Minutes. Request gated models (SAM 3, DINOv3-SAT) early, because approval is manual.

### Colab / Kaggle / others
- **Colab:** The WeatherNext README confirms a **free v5e-1 TPU Colab runtime** suitable for WeatherNext Mini ([GitHub](https://github.com/google-deepmind/weathernext)). Many repos ship Colab notebooks: TerraMind, AstroCLIP, Zoobot, ACE, Multimodal Universe, SEN2SR.
- **Free GPU limits:** Colab and Kaggle quotas were not verifiable via fetch (the pages are JavaScript-rendered).
- **Not verified:** Lightning AI, Together, Fireworks, Groq, AWS SageMaker geospatial, Replicate satellite models.

### Cursor
- The challenge requires building with Cursor, and the SpaceXSI starter pack gives attendees one month of X Premium "which includes Cursor, Grok Bot, X and Grok" (starter pack PDF in this repo's `docs/`).
- Several tools ship agent-friendly material that Cursor can use directly, e.g. Earth2Studio's agent "skills" ([GitHub](https://github.com/NVIDIA/earth2studio)) and Planetary Explorer's MCP server ([GitHub](https://github.com/microsoft/Planetary-Explorer)).

## Demo-in-a-day stacks

Each stack combines a dataset, a model and a UI, is tied to a concrete space-sector problem, and uses only tools verified above. Grok is the orchestrator and narrator in every stack, for the bonus and because LLMs are good at explanation but bad at counting from pixels.

### Stack 1 — "Lost in the catalog": six-digit satellites that TLE-based tools can't see
- **Problem:** Five-digit NORAD catalog numbers ran out on **2026-07-11**. New objects get six-digit numbers that **cannot be written as TLEs**, so any tracker, tutorial or LLM-generated code that still parses TLEs silently misses them ([CelesTrak](https://celestrak.org/NORAD/documentation/gp-data-formats.php)).
- **Data:** CelesTrak GP in OMM JSON (`FORMAT=JSON`, group `active`), with the TLE feed for comparison. Follow the download etiquette: cache, one fetch per 2-hour update.
- **Model/compute:**
  - `python-sgp4` OMM support or `satellite.js` `json2satrec` to propagate.
  - **dSGP4** for GPU-batched whole-catalogue close-approach screening.
  - NASA CARA formulas, or a simple Pc approximation, to rank conjunctions.
- **UI:** CesiumJS + satellite.js (or a KeepTrack fork). Highlight "objects invisible to legacy TLE tools" in red.
- **Grok:** Explains each close approach in plain language and uses X Search to pull operator or launch news about the new objects.
- **Why it works:** The problem is crisp and new (July 2026), the data is real and the visual is striking. Build time is about 12–18 hours.

### Stack 2 — Solar-storm early warning for satellite operators
- **Problem:** Geomagnetic storms raise thermospheric drag and can doom freshly launched satellites. The Feb 2022 Starlink loss is the canonical example; get the problem facts from the space-weather slice.
- **Data:**
  - **NOAA SWPC JSON** (Kp, solar wind) and **DONKI** flares/CMEs (free api.nasa.gov key).
  - Surya's public S3 SDO data (`nasa-surya-bench`).
  - CelesTrak OMM for low-perigee constellations.
- **Model:** **Surya** easy inference or the `solar_flares_surya` fine-tune for 24-hour M/X flare probability (TSS 0.436, honestly better than baselines but far from perfect) ([Surya](https://github.com/NASA-IMPACT/Surya)). Skyfield/sgp4 provides altitude context.
- **UI:** Streamlit dashboard showing the Sun image, flare probability gauge, Kp timeline and at-risk satellites list.
- **Grok:** Writes an "operator bulletin" and searches X for reported anomalies.
- **Build time:** About 10–16 hours. Surya runs on CPU/MPS for easy inference, so it is laptop-friendly.

### Stack 3 — Planet-scale change alerts with no training labels
- **Problem:** Illegal mining, deforestation or unpermitted construction happens faster than humans can review imagery, and labelled data is scarce.
- **Data:** **AlphaEarth Satellite Embedding** (2017–2024) in Earth Engine, plus Sentinel-2 quick-looks with Cloud Score+ masking ([EE catalog](https://developers.google.com/earth-engine/datasets/catalog/GOOGLE_SATELLITE_EMBEDDING_V1_ANNUAL)).
- **Model:**
  - Cosine distance between years as a change score.
  - A k-NN with 10–20 user-clicked examples ("find more like this").
  - Optional: Major TOM SigLIP embeddings for **text search** ("open-pit mine").
- **UI:** geemap or leafmap split-panel map (before/after) inside Streamlit.
- **Grok:** Takes ranked hotspots plus rendered before/after PNGs and writes a triage note. It is not asked to count.
- **Caveats:** Annual resolution only; small features wash out in tile averages ([Earth Genome note](https://www.earthgenome.org/blog/quick-tech-note-adapting-alphaearth-embeddings-to-new-workflows)). Do not use OlmoEarth for a mining pitch (license).
- **Build time:** About 8–12 hours.

### Stack 4 — Disaster rapid-mapping copilot (flood or fire)
- **Problem:** In the first 24–72 hours after a flood or fire, responders need extent, exposed buildings and the next days' weather. Clouds block optical imagery.
- **Data:**
  - Sentinel-1 and Sentinel-2 via Earth Search or Planetary Computer STAC.
  - **Microsoft building footprints**.
  - **NASA FIRMS** (fires).
  - **WeatherNext 2 ensemble via Open-Meteo** (rain or wind probabilities).
- **Model:** **Prithvi-EO-2.0-300M-TL-Sen1Floods11** or the TerraMind Sen1Floods11 config, with ml4floods as a fallback. OmniCloudMask for cloud filtering. Optionally SAM 3 with "blue tarp" or "flooded road" prompts on high-res open imagery.
- **UI:** MapLibre or deck.gl web map (Cursor-generated Next.js) or leafmap/Streamlit.
- **Grok:** X Search for on-the-ground posts, cross-referenced with the satellite flood map, then a situation report.
- **Build time:** About 14–20 hours.

### Stack 5 — "LLMs can't count from orbit": port and airbase activity monitor
- **Problem:** Frontier VLMs fail at counting and localisation. GPT-4V gets 5.1% grounding accuracy on VRSBench, and the best GEOBench-VLM model reaches 41.7% ([VRSBench](https://github.com/lx709/VRSBench), [arXiv 2411.19325](https://arxiv.org/abs/2411.19325)). Analysts still need counts.
- **Data:** High-res open imagery (NAIP via Earth Search, Maxar Open Data, OpenAerialMap) at a few ports or airports, several dates.
- **Model:** **YOLO26-OBB (DOTA)** + **SAHI** tiling for ships, planes and tanks. SAM 3 for concepts DOTA lacks.
- **UI:** Time slider with counts chart (Streamlit or Dash).
- **Grok:** Narrates trends from the detector's numbers. As a mini-benchmark slide, show Grok's raw-pixel count against the detector's.
- **Caveats:** Ultralytics weights are AGPL (fine for a hackathon). DOTA images are academic-use-only.
- **Build time:** About 8–12 hours.

### Stack 6 — Dark-vessel watch for marine protected areas
- **Problem:** Illegal fishing by vessels that switch off AIS.
- **Data:** **Global Fishing Watch API**: SAR vessel detections (AIS-matched or not) and events (free key) ([GFW](https://globalfishingwatch.org/our-apis/)). Optional Skylight vessel models on Sentinel-1.
- **UI:** deck.gl or lonboard map of unmatched detections inside protected-area polygons.
- **Grok:** Builds a per-vessel "suspicion" narrative and searches X/web for news.
- **Build time:** About 8–12 hours. It is mostly API work.

### Stack 7 — Launch-day weather go/no-go assistant
- **Problem:** Weather scrubs are costly. Ensemble probabilities of upper-level and surface wind and precipitation drive launch-commit criteria.
- **Data:** **WeatherNext 2 64-member ensemble** at the launch site via Open-Meteo, including pressure-level winds. GOES ABI and GLM (lightning) via the Planetary Computer `goes-cmi` and `goes-glm` collections for nowcasting.
- **Model:** Ensemble post-processing (probability of exceedance). Optional pysteps nowcast.
- **UI:** Fan charts plus a map. **Grok** turns probabilities into a "go/no-go" briefing with explicit uncertainty.
- **Build time:** About 8–12 hours.

### Stack 8 — Artemis landing-site and lunar-ice prospector
- **Problem:** Selecting south-pole landing sites trades off hazards (craters) against water-ice access.
- **Data:** SomBench / LROC tiles and ice-prospectivity datasets on HF ([NASA-IBM LFM](https://huggingface.co/nasa-ibm-ai4science/NASA-IBM-Lunar-Foundation-Model)).
- **Model:** **NASA-IBM Lunar Foundation Model** fine-tunes for crater detection and ice prospectivity, run via TerraTorch configs ([GitHub](https://github.com/NASA-IMPACT/NASA-IBM-Lunar-Foundation-Model)).
- **UI:** CesiumJS with a Moon ellipsoid, or a simple map viewer. Grok answers "why this site?".
- **Caveat:** The model is weeks old and the config wiring is fiddly. Budget time for it.
- **Build time:** About 14–20 hours.

### Stack 9 — "Read the literature for me" mission-design copilot
- **Problem:** The brief says space has "a literature no human can read all of". Mission designers rediscover lessons that are already published.
- **Data:** **NASA ADS/SciX API** (token, 5k/day), **arXiv API**, optionally Semantic Scholar SPECTER2 embeddings and NASA technical reports.
- **Model:** **INDUS retriever** embeddings plus **PaperQA2** for cited answers. Grok Collections Search can stand in for the vector store.
- **UI:** Chat interface with citation cards and an evidence map, e.g. "Which debris-removal techniques have flight heritage?".
- **Build time:** About 6–10 hours. It is the lowest-risk technically, but it needs a strong problem framing to stand out.

### Stack 10 — Methane super-emitter finder (stretch)
- **Problem:** A small number of super-emitters dominate oil and gas methane.
- **Data:** EMIT scenes via **earthaccess** (NASA Earthdata login), and Sentinel-2 SWIR.
- **Model:** **STARCOP** (hyperspectral) or **CH4Net** (S2).
- **UI:** Plume map plus per-site cards. Grok links plumes to facilities via web search.
- **Caveat:** Highest technical risk of these stacks, because the models need setup and false positives are common.

## Cross-slice leads

- **SpaceX / xAI / orbital compute**
  - The `xai-org/xai-sdk-python` repo description now reads "The official Python SDK for the **SpaceXAI** API" (GitHub API, 2026-10-24). That suggests xAI branding changed after a SpaceX tie-up; the SpaceX/xAI slice should confirm.
  - Current Grok API models are grok-4.7, 4.6, 4.5, 4.3 and 4.20, plus Imagine image/video and grok-voice-3.0 ([docs.x.ai](https://docs.x.ai/docs/models)).
  - Grok Bot (x.ai/bot) blocks automated fetch.
  - The Starship HLS link makes the NASA-IBM Lunar FM (Stack 8) on-theme.
- **Space traffic, debris and weather**
  - **CelesTrak: 5-digit catalog numbers exhausted on 2026-07-11**; TLE cannot represent new objects; alpha-5 was rejected ([CelesTrak](https://celestrak.org/NORAD/documentation/gp-data-formats.php)).
  - Space-Track CDMs are not public; the API limit is under 30 requests per minute and 300 per hour ([Space-Track](https://www.space-track.org/documentation#/api)).
  - NASA CARA tools moved `.mat` files to Git LFS in January 2026.
  - ESA dSGP4 v1.5.1 (Oct 2026) and Kessler.
  - WeatherNext Cyclones (FNV3/GDMI) ran operationally in the 2025 Atlantic season, with a Nature paper in 2026 ([weathernext](https://github.com/google-deepmind/weathernext)).
- **US agencies (NASA, NOAA)**
  - NASA-IMPACT released the **NASA-IBM Lunar Foundation Model** (Sep 2026).
  - Other new 2026 NASA-IMPACT repos: `veda-ui-mcp` (MCP server for the VEDA STAC catalog), `geospatial-studio`, `akd-agentic-eo-berlin-2026` (EO MCP tools), `astroakd-bench` (data-search agents benchmark) and `Trust17-Norms-for-Scientific-Agents` ([NASA-IMPACT org](https://github.com/NASA-IMPACT)).
  - NASA FIRMS `country` endpoint is "currently not available".
  - The api.nasa.gov DEMO_KEY gets rate-limited quickly.
  - NASA GMAT is now on GitHub (nasa/GMAT, Apache-2.0).
- **ESA and other agencies**
  - Major TOM embedding sets (ESA Φ-lab).
  - ESA OpenSR (SEN2SR, LDSR-S2 v1.2.x, Oct 2026).
  - CDSE free quotas: 10k Sentinel Hub PUs and 10k openEO credits per month, "temporary boost" ([CDSE](https://documentation.dataspace.copernicus.eu/Quotas.html)).
  - TerraMind (IBM + ESA).
  - ESA pykep v3.0.0 (May 2026).
  - ECMWF archived `ai-models` and moved to anemoi; AIFS weights are CC-BY-4.0.
- **EO companies**
  - **Planet and Airbus** are the only trusted testers of Google's Remote Sensing Foundation Models ([Google Earth AI](https://ai.google/earth-ai/)).
  - Microsoft building footprints now include Vexcel-derived heights (2026 updates).
  - Element 84 Earth Search hosts both S2 L2A and C1 L2A collections.
  - Ultralytics AGPL licensing is a known startup pain point.
  - Microsoft Planetary Explorer (formerly NASA Earth Copilot) targets defense and national security among its use cases.
- **EO analytics**
  - AlphaEarth limitations: annual composites; tile-averaging washes out small objects ([Earth Genome](https://www.earthgenome.org/blog/quick-tech-note-adapting-alphaearth-embeddings-to-new-workflows)).
  - The **OlmoEarth license bans military, intelligence, surveillance and extractive uses** ([LICENSE](https://github.com/allenai/olmoearth_pretrain/blob/main/LICENSE)).
  - GEO-Bench-2 finds natural-image backbones (ConvNeXt/DINOv3) best on high-res tasks.
  - Planetary Computer hosts `predicted-damage-colombia-2026` and `predicted-damage-venezuela-2026` collections; their origin is worth checking.
- **China**
  - SkySense/SkySense++ (Ant Group and Wuhan University; *Nature Machine Intelligence* 2025).
  - Pangu-Weather (non-commercial weights).
  - FuXi-2.1 (new, on HF).
  - FengWu (Shanghai AI Lab).
  - LHRS-Bot (Nanjing University).
  - SkyEyeGPT (NWPU).
  - EarthGPT.
  - The JL1-CD change dataset (Jilin-1 satellites) in open-cd.
- **Datasets catalogue**
  - Major TOM (Core-S2L2A 2.25M patches, about 23 TB).
  - Copernicus-Pretrain (18.7M images), Copernicus-Bench and Copernicus-Embed-025deg.
  - SomBench (lunar, about 2M bundles).
  - core-sdo (Surya).
  - Multimodal Universe (100 TB).
  - WorldFloods v2.
  - Fields of The World.
  - VRSBench and VRSBench-SAR (GPT-5.1-generated, unverified annotations).
  - GEO-Bench-2 (17–19 datasets).
  - ARCO-ERA5.
  - Satlas products.
  - TESSERA (CC0).
  - Planetary Computer: 139 collections.
- **Space science and literature**
  - AstroSage-70B (May 2025).
  - INDUS retriever and NASA-IR benchmark.
  - SciX.
  - **OpenAlex moved to key-based dollar budgets** ($0.10/day shared per IP without a key, $1/day with one).
  - Semantic Scholar unauthenticated calls returned 429.
  - PaperQA2 moved to CalVer.
  - Fink broker v5.0.0 and ALeRCE client now multi-survey with Rubin LSST.

## Leads not followed

These were seen or recalled but not verified in this pass. Web search was exhausted for most of the session, so they need checking before relying on them.

- **EO foundation models:**
  - Clay v1.5 release notes (parameter count, sensors)
  - GEO-Bench-2 leaderboard contents (the HF Space did not render)
  - Earth Genome / Earth Index embeddings
  - Element 84 embeddings work
  - THOR, Aion-EO, FlexiMo, SatVision-TOA, Embed2Scale
  - SenPa-MAE, USat, msGFM, SoftCon, DeCUR as standalone repos
  - Google's own AlphaEarth model weights (not public, as far as seen)
- **VLMs and agents:**
  - GeoGround, EarthMarker, Falcon, GeoLLaVA, RS-LLaVA, VHM, EarthMind, Geo-R1 / RL-tuned RS reasoning models
  - DisasterM3
  - Any Grok-specific remote-sensing evaluation
  - Planet agent and LLM partnerships
  - Earth Engine MCP and STAC MCP servers beyond NASA-IMPACT `veda-ui-mcp` and Planetary Explorer
  - Esri AI assistants
  - GeoGuessr-style geolocation results for frontier models
- **Detection and segmentation:**
  - Remote-sensing evaluations of SAM 3
  - S2DR3 (Gamma Earth)
  - CloudSEN12 models and SEnSeIv2
  - KappaMask
  - SARDet-100K/MSFA, SAR foundation models (SARATR-X, SAR-JEPA)
  - xView2 winners
  - Carbon Mapper API, UNEP IMEO MARS
  - MethaneSAT status
  - FireSat status
  - Copernicus GFM flood service
  - Google Open Buildings 2.5D
  - Amazon Mining Watch, GLAD alerts
  - Next Day Wildfire Spread models
- **Weather:**
  - WeatherBench 2 headline numbers (scorecards are images)
  - WeatherNext 3 access
  - Weather Lab vs NHC 2025 verification numbers
  - Commercial models (Silurian, Jua, WindBorne, Brightband)
  - ArchesWeather repo
  - Aardvark Weather
  - Copernicus CDS API changes
- **Heliophysics:**
  - SuryaBench details
  - SDOML v2 on AWS
  - Flare/CME/Dst ML repos
  - MIT ARCLab thermosphere-drag challenge results
  - HAPI servers
  - ESA SWE portal API
- **Astronomy:**
  - AstroLLaMA and its HF status
  - Pathfinder (UniverseTBD) live app
  - Lasair, ANTARES, AMPEL, Pitt-Google, Babamul
  - Rubin alert-stream public access terms
  - Euclid Q1 ML catalogues
  - Astronomaly
  - GWOSC
  - SETI/Breakthrough Listen ML
  - ExoMiner++ naming
- **Orbital:**
  - orekit Python wrapper status
  - Ansys STK free tiers
  - FreeFlyer
  - SatNOGS API (GitLab)
  - N2YO API limits
  - ESA DISCOS API
  - LeoLabs, Slingshot, Privateer public tools
  - CelesTrak SOCRATES status
- **Stack and compute:**
  - Planetary Computer Hub retirement date
  - Colab and Kaggle current GPU quotas
  - Replicate satellite models
  - Gemini free-tier limits
  - Lightning AI, Together, Fireworks, Groq free tiers
  - Felt
  - xAI hackathon credits
  - Whether X Premium includes API credits
  - Grok Bot features
