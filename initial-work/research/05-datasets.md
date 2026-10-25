# 05. Large public datasets

A dataset is listed here if a weekend team can reach it without a sales call. Commercial archives (Vantor, Planet tasking, Jilin-1, ICEYE tasking) are named in [02-startups.md](02-startups.md) and are not repeated as if they were open.

“Large” means multi-year or global or both. The right dataset for the brief is large and already interpreted. Raw L0 radar is large and is how weekends die.

## Land optical, the long record

| Dataset | What it is | Why it is big | Watch-out |
| --- | --- | --- | --- |
| Landsat Collection 2, 1972–present, USGS / NASA | 30 m optical, thermal on later missions. The 54-year record the Landsat Science Team is trying to protect. | Decades, global land, free. | Landsat Next is in an affordability review. The archive is the asset. |
| Sentinel-2 L2A, ESA / Copernicus | 10 m optical, five-day revisit with two satellites. | The default “free sharp enough” land dataset. CDSE holds on the order of 90+ PB of Sentinel products overall. | Clouds. Version changes after the 2024–2025 reprocessing. |
| Harmonized Landsat Sentinel-2 (HLS), NASA | 30 m, Landsat and Sentinel-2 on one grid. | The training set behind Prithvi. Input to OPERA disturbance and water products. | 30 m will not see a car. |
| MODIS, NASA | 250 m–1 km, daily, since 1999. | The long daily record for fires, snow, ocean color, vegetation. | Coarse. |
| VIIRS, NASA / NOAA | Daily night lights and fire, 375 m fire, Black Marble night lights. | The dataset the Cambridge study spent six months learning to open. | Version choice, gz/HDF friction. |

Access that does not involve downloading the archive: Planetary Computer STAC, Google Earth Engine, CDSE, AWS Open Data.

## Radar and the 2026 arrivals

| Dataset | Status on 24 Oct 2026 | Good public question | Access pain |
| --- | --- | --- | --- |
| Sentinel-1 RTC / GRD | Sentinel-1D opened 17 April 2026. Two-satellite revisit restored after Sentinel-1A phased out in July 2026. | Flood extent, ships, ice, coarse change through clouds. | Speckle. Not a photo. OPERA RTC and DSWx-S1 exist so you do not have to process SLC yourself. |
| NISAR L-band | Provisional public data since 20 July 2026, acquisitions from 17 June 2026. Full record expected by end of 2026. BETA early-2026 products are a different processor. | Ground motion, water, biomass, soil moisture. The mission’s own list. | us-west-2 S3, one-hour credentials, huge files, do not mix BETA and PROVISIONAL. |
| NISAR S-band | ISRO Bhoonidhi, beta. | Same mission, different wavelength, different portal. | A second account and a second format. |
| OPERA DSWx, DIST, DISP, RTC | Optical water and disturbance in production globally or near-globally. Several Sentinel-1 products are North America only. NISAR water and displacement were scheduled for mid and late 2026. | “Where is the water?” “What changed?” “Is this ground moving?” | Read the coverage table before promising a global demo. <https://www.jpl.nasa.gov/go/opera/products/> |
| ESA Biomass | Public data opened 26 January 2026. P-band, forest carbon. First year was tomography over Gabon, Congo, Cameroon, Brazil. | Where is the woody carbon. | Young mission. Calibration is the science. A global biomass dashboard will overclaim. |
| Umbra open scenes | Selected very high resolution SAR, down to about 16 cm, released by the company. | A single sharp radar picture. | Not a global archive. A prop for one slide. |

ASF Vertex and `asf_search` are the practical NASA radar door. HyP3 on ASF can make Sentinel-1 RTC so a team does not write a SAR processor.

## Atmosphere, gases, fire, water, ocean

| Dataset | Question it can support | Notes |
| --- | --- | --- |
| EMIT L2B methane and CO2, Version 3 | Where is the plume. | Released 16 October 2026. Archive is mid-reprocessing for about three months. ISS orbit, so coverage is not a daily global map. <https://www.earthdata.nasa.gov/data/alerts-outages/emit-version-2-level-2b-level-3-version-3-level-2b-data-products-released> |
| Carbon Mapper portal and API | Which source, which sector, which instrument (EMIT, Tanager, aircraft). | Non-commercial public use. Account required. Example source query is in their geospatial how-to PDF. <https://carbonmapper.org/data> |
| Sentinel-5P | Regional methane, NO2, other gases. The wide “tip” in tip-and-cue. | A column concentration, not a facility. |
| FIRMS | What is hot, in near real time. | Free map key, rate limits. Noisy. Not a perimeter and not a damage map. |
| SWOT | River and lake height, sea-surface topography. | PO.DAAC and AVISO. Handbook rev A, 4 March 2025. <https://swot.jpl.nasa.gov/data/> |
| PACE | Ocean color and aerosols, hyperspectral. | Young NASA mission. Good for a focused ocean story, bad for a generic map. |
| GOES-19 | Hemispheric weather, storms, fires, minute-scale. | NOAA. This is the “right now” optical/IR weather view. Different from a polar land archive. |

## Products that are already decisions

These are the datasets that match the brief, because someone already did the remote sensing.

| Product | What you get | Where |
| --- | --- | --- |
| Dynamic World (Google) | Near-real-time land cover from Sentinel-2, 10 m. | Earth Engine |
| ESA WorldCover | Annual global land cover, 10 m. | ESA / Planetary Computer |
| Impact Observatory / Esri land cover | Annual 10 m land cover. | Planetary Computer |
| Hansen / Global Forest Watch tree cover loss | Annual loss, plus integrated disturbance alerts. | GFW data API <https://data-api.globalforestwatch.org/> |
| Global Fishing Watch | AIS fishing effort, vessel identity, encounters, loitering, port visits, SAR vessel detections, AIS presence. | API key, free for research with a stated purpose. <https://globalfishingwatch.org/our-apis/> |
| Google / Microsoft / OSM buildings | Footprints to join a flood or a fire to “homes.” | Overture, Planetary Computer, Google Open Buildings |
| GHSL, WorldPop | Built-up and population. | Various open catalogs |
| Black Marble | Processed night lights. | NASA |
| AlphaEarth Satellite Embedding V1 | 10 m, 64-dimensional annual embedding, 2017–2024 (official), a community copy through 2025. Change is a dot product between years. | Earth Engine `GOOGLE/SATELLITE_EMBEDDING/V1/ANNUAL`. GCS bucket is provider-pays as of July 2026. Community COGs: <https://source.coop/tge-labs/aef> |
| FIRMS + buildings + land cover | A derived stack you would build, not a product. | The obvious wildfire one-pager. |

## Embeddings and ML-ready archives

Useful if the idea is “find places that look like this.” Painful if the idea needs five of them at once. The format complaints are in [01-structural-gap.md](01-structural-gap.md).

| Product | Shape | License notes from the CNG post |
| --- | --- | --- |
| AlphaEarth | 10 m pixels, 64 dims, annual | CC-BY-4.0 |
| Tessera | 10 m, 128 dims | CC0, but the API returns arrays without CRS |
| Clay v1 / v1.5 | Patches, 768 or 1024 dims | ODC-By or CC-BY depending on version |
| Major TOM embeddings | ~3 km patches, Sentinel-1 and Sentinel-2 | CC-BY-SA. Hugging Face. <https://huggingface.co/Major-TOM> |
| Earth Index | 320 m, 384 dims, GeoParquet | CC-BY-4.0. The clean one. |
| Presto | 10 m, 128 dims | CC-BY, CRS caveats |
| Copernicus-Embed | 0.25 degree | Too coarse for a city |

Major TOM Core itself is an ML-ready Sentinel-2 metaset covering most land, on the order of 50 TB in the paper’s description. <https://arxiv.org/html/2402.12095v2>

## Orbits, not images

| Dataset | What it answers | Limit |
| --- | --- | --- |
| Starlink public ephemerides | Where Starlink says it will be for the next 72 hours, with covariance, including maneuvers. | Their birds only. README: eight-hour updates. A social post says hourly. Check the manifest before believing either. <https://starlink.com/public-files/ephemerides/README.md> |
| space-track.org | The public catalog operators actually file into. | Account, and redistribution rules. |
| CelesTrak | TLEs and analyst tools built on the public catalog. | TLEs are the wrong precision for a “we almost hit” claim. Fine for “this shell is crowded.” |
| ESA Space Environment Report figures | The official trend: health index, launch counts, reentries. | Annual, not a live feed. |
| UCS / McDowell / CelesTrak satellite databases | Who operates what. | Counts go stale in months. |

space-safety.com screening is not a public dataset. It is an operator service.

## Literature

The pack names “a literature no human can read.”

- NASA ADS: papers across astronomy and much of space science. API.
- NASA NTRS: technical reports, mission documents.
- ESA publication archives and mission pages.
- CEOS and mission user guides, which are the literature that tells you whether a file is usable.

A pure literature project is weaker as a demo than a place plus the three papers that measured that place. The combination is what the pack describes.

## Benchmarks, if someone is tempted to train

xView, xView2 (disaster damage), SpaceNet, FAIR1M, DOTA, BigEarthNet. These are labeled sets for models. They are not a live picture of this week. Training on them is a research project. Scoring a pretrained model on one xView2 scene is a demo of someone else’s work.

## Picking from this list

For a two-day build, the datasets that are both large and kind:

1. OPERA water and disturbance, or Dynamic World, over one region, in Planetary Computer.
2. FIRMS plus a building layer, for one fire.
3. Carbon Mapper or EMIT plumes, for one gas story.
4. AlphaEarth annual embeddings, for “this place changed between two years,” which avoids a custom model.
5. Starlink ephemerides plus CelesTrak, for an orbital story that does not pretend to compute a probability of collision.

NISAR belongs on the list because it is the largest new public radar archive of the year. It belongs off the critical path of the demo unless the team has already opened one product and it is a geocoded browse, not an SLC.
