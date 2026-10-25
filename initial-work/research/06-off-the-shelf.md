# 06. Off-the-shelf technology

The test for this list: could a team call it this weekend without training anything. If the answer is yes, it is a material. If the answer is “only after a fine-tune,” it is a temptation.

## Catalogs and compute next to the data

| Tool | Role | Trap |
| --- | --- | --- |
| Copernicus Data Space Ecosystem, Copernicus Browser, openEO | Search and process Sentinel next to a 90 PB archive. STAC and OData. | Accounts, quotas, and a 2026 roadmap that is still finishing basic land products. |
| Google Earth Engine | The fastest way to a global map. Hosts Dynamic World and AlphaEarth embeddings. | Export limits. A judge cannot see your code unless you wrap it. |
| Microsoft Planetary Computer | STAC API, anonymous access, petabytes, the best Python-native free catalog. | The Hub is dead. Keys only affect rate limits. APIs had a migration outage in September 2026. |
| NASA Earthdata + `earthaccess` | The supported way into NISAR, EMIT, HLS, SWOT. | Login, and the ten-rules paper exists because this used to be awful. It is better and still fussy. |
| ASF Vertex, `asf_search`, HyP3 | Sentinel-1 and NISAR. HyP3 makes RTC for you. | Same Earthdata login. |
| AWS Open Data | Landsat, Sentinel, some NOAA. | Egress if you leave the region. |
| Source Cooperative | Community copies, including AlphaEarth COGs with a STAC-GeoParquet index. | Not the official Google product. |
| Radiant Earth / MLHub | Labeled EO datasets. | Better for training than for a live question. |
| Hugging Face, Major-TOM and model cards | Weights and the Major TOM metaset. | Grid and format tax. |

## Models you should call, not retrain

From Esri’s integration list and GEO-Bench-2, the ones with usable licenses:

- **TerraMind** (IBM and ESA). Any-to-any across optical, SAR, DEM, land cover, NDVI. Apache-2.0. Pretrained on TerraMesh, about 9 million aligned samples. ESA’s PANGAEA benchmark is where they claim an 8%+ gain over a field of EO foundation models at a fraction of the compute. Hugging Face. Terratorch.
- **Prithvi-EO-2.0** (NASA and IBM). 300M and 600M, HLS, multi-temporal, Apache-2.0. The right tool if the input is 30 m HLS. The wrong tool if the input is a 0.5 m photo.
- **Clay** v1, Apache-2.0. A community default embedding across Landsat, Sentinel-1/2, NAIP, MODIS. Consistent, not the winner of every task. v1.5 embeddings exist for NAIP and partial Sentinel-2.
- **DOFA**. Wavelength-aware, so different sensors can share a backbone. CC-BY-4.0 weights in the benchmark table.
- **Satlas** (Allen AI). Supervised Sentinel-2 and NAIP Swin models. ODC-BY.
- **DINOv3** satellite variant, trained on Maxar RGB. Strong at fine GSD. License is the DINO license, not Apache. Read it before shipping.
- **SAM / SAM2 via segment-geospatial (`samgeo`)**. Click a thing, get a polygon. The fastest “segmentation demo” in EO. It does not know what the thing is.
- Remote-sensing VLMs that already exist: GeoChat, EarthDial, LHRS-Bot, SkySenseGPT, RS-LLaVA and their neighbors. A general model (Grok or another multimodal model) looking at a small chip is the weekend version. Fine-tuning a VLM is not.

ArcGIS ships TerraMind, DOFA, Clay, and Prithvi as tools. That means a student project whose only trick is “we ran Prithvi” is a tutorial, not an entry.

- Esri list: <https://www.esri.com/arcgis-blog/products/arcgis-pro/geoai/earth-observation-with-remote-sensing-foundation-models-in-arcgis>
- GEO-Bench-2: <https://arxiv.org/html/2511.15658>
- Mapular guide: <https://mapular.com/blog/geospatial-foundation-models-guide>
- Embeddings registry notes: <https://tnview.org/pages/geoai/foundation-models/>

## Libraries that remove a week of pain

Python, because that is where the data libraries are:

- `pystac-client`, `stackstac`, `odc-stac` to go from a search to an array.
- `rasterio`, `rioxarray`, `xarray`, `dask` if the array is big. Prefer a small bbox so dask never becomes the project.
- `leafmap` and `geemap` for a notebook map. `lonboard` if the points are numerous.
- `duckdb` with spatial, for joining plumes to facilities without standing up Postgres.
- `geopandas` for the last mile.
- `earthaccess`, `asf_search`, `pystac`.
- TorchGeo and Terratorch if a foundation model is actually called. Both already wrap the boring parts.

JavaScript, if the demo is a web page:

- MapLibre plus PMTiles or a COG through TiTiler.
- Or a static PNG exported from the notebook, which is less fragile at 2 a.m.

Do not build a STAC server. Do not build a tile server unless the map is the product and TiTiler is one command away.

## APIs that are already the answer

| API | Returns | Key |
| --- | --- | --- |
| FIRMS area CSV | Hotspots | Free map key, 5,000 transactions / 10 min |
| Carbon Mapper | Sources and plumes, GeoJSON | Account, non-commercial terms |
| Global Forest Watch data API | Loss, alerts, boundaries | Check their current auth |
| Global Fishing Watch v3, including 4Wings | Fishing effort, SAR detections, vessel identity, events | Account and a stated purpose |
| CDSE OData / STAC / openEO | Sentinel scenes and processes | Account |
| Earthdata / CMR | NASA granules | Earthdata login |
| Starlink ephemeris manifest | Files | Public HTTP |
| CelesTrak | GP data and supplements | Public, with their use rules |
| ADS | Papers | Application id |

GFW 4Wings specifically exposes SAR vessel detections and AIS fishing on a grid, PNG or MVT tiles, CSV reports. Building a ship detector is a choice to ignore this.

## Glue that makes an answer defensible

The terrAIntel white paper’s third barrier is trust. These are the cheap ways to show your work:

- Cite the scene id, the product version, and the time range in the sentence, not in a footnote the UI hides.
- Prefer an official derived product (OPERA, FIRMS, Carbon Mapper, WorldCover) over a model you ran, and say which.
- If a model draws a polygon, show the chip it saw.
- If two years of AlphaEarth disagree, call it “the embedding changed,” not “deforestation,” unless a forest product agrees.
- Keep the demo bbox small enough to recompute live if the network behaves, and keep a cached run if it does not.

## Things that look off-the-shelf and are not, for a Sunday deadline

- A NISAR InSAR time series from SLC.
- A global embedding similarity search over AlphaEarth at 10 m. The data is 465 TB. A city is fine. The world is not, not by Sunday.
- Fine-tuning Prithvi or TerraMind. The weights are off the shelf. The labels are the project.
- A fusion of Jilin-1 and Sentinel. You will not have Jilin-1.
- space-safety.com as an API. It is an operator onboarding email.
- Any commercial tasking API (Planet, ICEYE, SkyFi) unless someone already has a key and a budget. The pack points at public data.

## A sane stack, once an idea is chosen

Not chosen yet. The stack that fits most of the ideas in [08-ideas.md](08-ideas.md):

1. Python for one notebook or script that hits STAC or a single API and writes GeoJSON plus a PNG.
2. A small web page that loads that GeoJSON and asks Grok only to phrase a paragraph from fields you already computed. The model does not get to invent a measurement.
3. Cursor for the build. Grok for the wording and the planning notes. That matches the bonus the sponsor described, without making the model the scientific instrument.
