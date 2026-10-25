# 01. The structural gap: too many pixels, too few decisions

This is the problem the rest of the landscape keeps rediscovering. It shows up in market essays, in a Cambridge study of non-specialists, in a survey of European local governments, in a NASA usability paper, in ESA’s own data portal, and in a Chinese column about commercial remote sensing. The wording changes. The bottleneck does not.

Collection got cheap. Interpretation did not. The customer who will pay, or the public servant who will act, wants a sentence, a boundary, or an alert inside a tool they already open. They do not want a GeoTIFF.

## The 2026 market version

Aravind Ravichandran’s TerraWatch, summarized in a Copernicus workshop deck, describes the value chain as “from pixels to impact” and lists four trends: high-volume data, cost pressure on satellite companies, a shift to onboard AI, and a need for scalable downstream insights.

Numbers from that deck:

- About **50 TB per day** downlinked from Sentinel, Landsat, and PlanetScope alone.
- **1,158** Earth-observation satellites expected to launch in the five years from 2026, across **72** companies and **44** countries with constellation plans. (The deck’s country and company counts sit next to each other in the extracted text; treat the satellite count as the firm figure and the company/country split as deck labels.)
- Hyperspectral, thermal, and multispectral missions producing **500 GB to 1 TB per day per satellite**.
- Ground stations and cloud egress called out as unsustainable: on the order of **$10–25 per TB per month** of cloud storage and about **$200 per satellite contact**.
- Onboard processors now plausible: Jetson-class boards, Hailo, KP Labs Antelope, Ubotica.

Source: TerraWatch, “The State of Earth Observation Platforms,” PDF hosted by the Copernicus Data Space Ecosystem, July 2025. <https://dataspace.copernicus.eu/sites/default/files/media/files/2025-07/0930_terrawatch_the_state_of_earth_observation_forpublication.pdf>

TerraWatch’s 2025 investment review says EO investment hit **$2 billion**, the highest year on record, up 15% from 2024. Acquisition and intelligence took over 90% of the money. Processing, the layer that would turn pixels into products, “seems to have finally picked up” after being neglected. <https://newsletter.terrawatchspace.com/earth-observation-investments-2025-review/>

Payload’s “State of EO 2026” quotes Luke Fischer, cofounder and CEO of SkyFi, that imagery “only provides one piece of the puzzle” for countries that want a complete solution. The same piece says operators have the satellites and still cannot make sense of the data. <https://payloadspace.com/the-state-of-eo-2026/>

New Space Economy’s April 2026 essay, “The Satellite Imagery Glut,” is the blunt commercial version:

- The sector built more imaging capacity than paying commercial customers.
- Planet, Satellogic, and BlackSky all survived by moving toward defense and analytics, not by selling more raw scenes.
- Free Sentinel-2 caps what anyone can charge for medium-resolution optical imagery.
- SAR (Capella, ICEYE, Umbra) added supply to a market that already had an interpretation gap. “Collecting the data is now the easy part.”

Financial snapshots in that essay, useful because they show where the money actually went:

| Company | What the essay reports |
| --- | --- |
| Planet Labs | FY2026 (year ending 31 Jan 2026) revenue about **$308 million**, up ~26%. First full year of non-GAAP profitability, adjusted EBITDA **$15.5 million**. Defense and intelligence revenue up more than 50%. |
| BlackSky | 2025 revenue **$106.6 million**, second year of positive adjusted EBITDA, backlog **$345 million**. 2026 guide $120–145 million revenue. |
| Satellogic | Redomiciled to Delaware in March 2025 to chase U.S. defense contracts. 2025 revenue **$17.7 million**, up 38%. Cash **$94.4 million** after offerings. Merlin constellation aimed at a first launch in October 2026. |
| Maxar | Taken private by Advent in 2023 for $6.4 billion. In October 2025 split and renamed: imagery is **Vantor**, manufacturing is **Lanteris**. |

The essay’s core paragraph is the one to keep:

> The bottleneck in the Earth observation value chain is not collecting imagery. Multiple satellites now image most of the Earth’s surface daily. The bottleneck is turning that imagery into decisions that a paying customer will fund consistently.

An agriculture buyer needs cloud masks, a vegetation index, an anomaly, an alert, and a drop into the farm software. An insurer after a hurricane needs change detection trained on the right buildings, a flood map joined to the property book, and a file the claims system will accept. That translation layer is slow to build. Palantir, Vantor, and defense analytics firms got durable revenue by selling it. Companies that mostly added satellites did not.

Source: <https://newspaceeconomy.ca/2026/04/08/the-satellite-imagery-glut-too-much-data-too-few-paying-customers-and-a-coming-shakeout-in-earth-observation/>

The same outlet’s 20 October 2026 survey, “The State of Earth Observation 2026,” says the competitive center has moved from pixels to cloud catalogs, STAC, and foundation models, and that enterprise buyers outside defense “rarely wish to purchase raw orthorectified TIFF files or complex radar interferograms.” They buy scores and alerts that land in ERP or GIS software. Fortune Business Insights, cited there, puts the EO market at **$7.68 billion in 2026**, toward $14.55 billion by 2034. Defense is still the anchor. <https://newspaceeconomy.ca/2026/10/20/the-state-of-earth-observation-2026/>

A Geoville white paper, terrAIntel (12 March 2026), says the same thing for newsrooms. Three barriers, repeated:

1. Fragmented access. Different catalogs, standards, and docs.
2. High activation energy. Expertise, method, and compute.
3. Hard to act on. Slow time-to-insight, weak provenance, so the result is not trusted.

Their line for journalism: the question is not “can we get satellite data?” It is “can we get a reliable answer in time, and show how we got it?” <https://www.geoville.com/fileadmin/geoville/user_upload/Website_Relaunch/News/terrAIntel_whitepaper_12032026.pdf>

## What happens when a non-specialist tries

“Challenges in using satellite data for non-remote sensing specialists” (Data & Policy, Cambridge) follows a research group whose goal was simple: use night lights to find large, bright areas. It took about **six months**. Unzipping a VIIRS `.gz` was a hurdle. Choosing which version of a NASA product to use had little guidance aimed at non-specialists. Level 1 and Level 2 products are free and demand heavy preprocessing. Level 3 and Level 4 products are what people actually want, and they come with three traps: they are specialized, they can hide errors from the lower levels, and they still have to be joined to other data.

The paper’s practical requests are modest and still mostly unmet: video walkthroughs for common GIS tools, and written guidance for non-specialists on which version of a dataset to use.

<https://www.cambridge.org/core/journals/data-and-policy/article/challenges-in-using-satellite-data-for-nonremote-sensing-specialists-an-exploratory-case-study/D65CFBF5A4B76F1B625D225A6B896C3E>

## What a city government says when asked

A 2025 survey of European local authorities (Urban Science, MDPI) asked people, including non-users, to pick their top barriers to Earth-observation data. The most common:

- Lack of skilled staff and training (17 of the respondents in that question).
- Limited budget (12).
- “EO satellite data do not fully meet our operational and knowledge needs” (11).
- Procurement complexity (6), technology complexity (5), lack of management or legal push (5 each).

Two respondents who do not use EO at all named the operational mismatch as their only barrier. One Swedish regional agency said they have no strong use case because they already rely on aerial photos. Skill and budget are real, and so is a product problem: the data does not answer the question the office has on Monday.

<https://www.mdpi.com/2413-8851/9/11/489>

## What NASA’s own data people wrote down

“Ten rules to increase the usability of earth observation mission datasets” (Earth Science Informatics, 2026) starts from a number: NASA mission data alone was projected to pass **320 petabytes by 2030** (cited to Frontier Development Lab 2023). Users spend disproportionate time on data engineering before any science (Robinson et al. 2020). Moving archives to commercial cloud did not, by itself, make the data cloud-shaped.

The case study is ICESat-2, a laser altimeter, not a camera. The failure mode generalizes. Data ships as HDF5, which is a reasonable archive format and a poor format for the way people now read data in the cloud. At the first hands-on workshop in 2019, attendees spent the first days fighting access tools they could not customize. The community then built `earthaccess` and `icepyx` on top of NASA’s metadata, and NSIDC started showing up at hackweeks.

The ten rules, shortened:

1. Put outside researchers and software people in the room when formats and distribution are designed.
2. Make archive staff collaborate with users, not only answer tickets.
3. Host regular hackweeks. Early ones should argue about formats and access, not only science.
4. Keep a shared JupyterHub alive between events. CryoCloud (since October 2022) exists because event hubs disappear and mission teams are bad at running their own.
5. Keep an asynchronous room (they use Slack) where new users can find the last person who hit the same error.
6. Maintain one obvious set of tutorials, including a small example and a large one that does not fit in laptop memory.
7. Build open, extensible tools.
8. Pay the developers, the user-support people, and the open-source contributors.
9. Create actual jobs for community management.
10. Set performance and reproducibility expectations. Cloud-native from the start. Do not assume a later conversion of petabytes.

This paper is a map of the subproblems inside “NASA data is free.” Free, and slow to start, and easy to misuse, and dependent on a few people who know which file to open.

<https://link.springer.com/article/10.1007/s12145-026-02216-5>

CEOS, the committee of space agencies that defines “analysis-ready data,” wrote in its 2025 plenary concept note that CARD (CEOS Analysis Ready Data) still does not put quantitative bounds on quality. Flags, masks, and weak documentation all change whether a product is actually ready. Analysis-ready is a label, not a guarantee. <https://ceos.org/ard/files/Future%20of%20CEOS-ARD%20Concept%20Note.pdf>

## What the newest NASA mission still feels like

NISAR, the NASA–ISRO radar satellite, launched 30 July 2025. Routine science operations began in January 2026. Provisional, calibrated L-band products for acquisitions on or after 17 June 2026 were released publicly on 20 July 2026. Earlier January–February data is BETA, not fully calibrated, and the two collections do not overlap in time. Mixing them can show a “change” that is only a processor change. The full science record was expected by the end of 2026, so as of this weekend it may still be incomplete.

NASA’s own pitch for NISAR is legible: millimeter-scale motion of the ground, ice, soil moisture, floods, biomass. The access path is not.

- Products live in NASA’s Earthdata Cloud on AWS.
- Direct S3 access works only from **us-west-2**. From anywhere else, Access Denied.
- Temporary credentials expire after **one hour**.
- You cannot copy the bucket into another bucket. You download, or you compute next to the data.
- Urgent-response products, the ones that would matter in a disaster, are kept for **30 days** and may use a less precise orbit.

Sources:

- <https://www.earthdata.nasa.gov/data/alerts-outages/nisar-l-band-data-now-publicly-available>
- <https://nisar-docs.asf.alaska.edu/products-overview/>
- <https://nisar-docs.asf.alaska.edu/aws-s3-access/>

OPERA, the JPL project that turns Sentinel-1, Landsat, Sentinel-2, and eventually NISAR into surface-water, disturbance, and displacement products, exists because raw SAR is not a product. Several OPERA suites are in production. NISAR-based water and displacement products were scheduled around June and September 2026. <https://www.jpl.nasa.gov/go/opera/products/>

The subproblem: the mission that was supposed to make radar usable just shipped, and the usable layer is still a specialist download with a one-hour key.

## Europe’s portal is huge and still a portal

The Copernicus Data Space Ecosystem annual report for 2025:

- Registered users passed **500,000**, up from 289,592 at the end of 2024. More than 50,000 monthly active users.
- Archive grew from more than 78 PB and 100 million Sentinel products to about **91 PB** and **120 million** products.
- In 2025 the platform published **31.47 million products, 19.72 PB**.
- Sentinel-2 reprocessing that started in 2024 finished in September 2025.
- Sentinel-1C and Sentinel-2C launched; Sentinel-1D user data opened 17 April 2026; Sentinel-1A was phased out in July 2026, restoring the six-day two-satellite radar revisit.
- The strategic shift they describe: stop being a download hose, start being a place where pixels are processed next to the archive (openEO, Copernicus Browser, STAC).

2026 roadmap language: performance, a wider data offer, openEO, “AI empowerment,” browser features, and a service-provider ecosystem. New Sentinel-3C is expected in Q4 2026. High-resolution land products (water, snow, urban atlas, vegetation phenology) are still being onboarded.

Sources:

- CDSE Annual Report 2025, CloudFerro PDF. <https://s3.waw3-1.cloudferro.com/swift/v1/portal_uploads_prod/CDSE_Annual_Report_2025%20.pdf>
- Roadmap deck, September 2026. <https://dataspace.copernicus.eu/sites/default/files/media/files/2026-09/1015_update_on_the_cdse_developments_roadmap_2026.pdf>

Older practitioner pain is still in the record. The ESA STEP forum thread on the long-term archive is full of quota errors: one scene is annoying, a time series is how projects die. That thread is from the previous access system, and CDSE was built to replace it. It is still evidence of the behavior users learned: bulk download fails, so people give up. <https://forum.step.esa.int/t/esa-copernicus-data-access-long-term-archive-and-its-drawbacks/15394>

Josef Aschbacher, now ESA Director General, said the same access problem in plainer words when he was running Copernicus planning in 2014. Revisit is one problem. Getting the file to the user is the other. Oil-spill users in Lisbon needed an image in about ten minutes. Everyone else was promised three hours, which was already a leap from Envisat. The interview is old. The split it describes is still the split: a few operational users get a product, everyone else gets a scene. <https://www.esa.int/Applications/Observing_the_Earth/Copernicus/Sentinel-1/Josef_Aschbacher_Head_of_Programme_Planning_and_Coordination_Service>

## Foundation models did not close the gap, they added a format war

By 2026 there are many Earth foundation models and several global embedding layers. A February 2026 Cloud-Native Geospatial post, “The Technical Debt of Earth Embedding Products,” describes what happens when a team tries to use more than one:

- Clay tiles were named in a non-standard way. The grid had to be reverse-engineered from file paths.
- Major TOM is Parquet on a private grid, not the MGRS grid everyone else uses, and the embedding models (DINOv2, SigLIP, SSL4EO) are already dated relative to newer Earth models.
- Earth Index is clean GeoParquet. The post treats it as the pattern the others should have copied.
- Copernicus-Embed is 0.25 degrees, about 25 km. Climate-scale, not a city.
- Presto’s GeoTIFFs carry a CRS assumption that does not match the imagery.
- Tessera is an API on a university server that returns raw NumPy. No CRS, no bounds.
- AlphaEarth was locked in Earth Engine and GCP. A 465 TB copy had to be moved to Source Cooperative before other people could index it. As of July 2026 the official GCS bucket is “provider pays.”

The post’s line: every team solves distribution alone, and the user pays that tax once per product. At city scale any one product is fine. At global scale the missing shared standard is the bottleneck, not model quality.

<https://cloudnativegeo.org/blog/2026/02/the-technical-debt-of-earth-embedding-products/>

GEO-Bench-2 (arXiv, November 2025) evaluated a pile of these models and found no winner. TerraMind leads some multispectral and multi-temporal tasks. DINOv3 trained on Maxar RGB leads at fine resolution. Clay is consistent and not dominant. The practical subproblem: “use a foundation model” is not a decision. The model has to match the sensor, the resolution, and the task, and the labels to test that match are the expensive part.

<https://arxiv.org/html/2511.15658>

Mapular’s June 2026 guide states the economic version cleanly: imagery is no longer the scarce input. Labels are. Foundation models matter because they cut the labeled data a new task needs. They do not remove the need for a person who knows whether the answer is right. <https://mapular.com/blog/geospatial-foundation-models-guide>

## Microsoft’s cautionary platform story

The Planetary Computer catalog and STAC API are still up, and they are the most practical free stack for a weekend prototype. The Hub, which was the free Jupyter environment, was retired on 6 June 2024. Hub home directories were deleted on 4 September 2024. Microsoft’s reason was a company-wide security change the Hub could not meet. A September 2026 migration took the APIs down for a scheduled window. Subscription keys still raise rate limits, and users were still asking in December 2025 whether those keys did anything.

The subproblem for anyone building on “free planetary cloud”: the data can outlive the notebook, the login, and the tutorial. A hackathon project should treat Planetary Computer as a catalog, and keep its own copy of any result it needs to demo.

- <https://github.com/microsoft/PlanetaryComputer/discussions/347>
- <https://github.com/microsoft/PlanetaryComputer/discussions/504>
- <https://github.com/microsoft/PlanetaryComputer/issues/464>
- <https://planetarycomputer.microsoft.com/docs>

## The same complaint, in China

A 2 January 2026 Sina Finance column says industry insiders put utilization of data from China’s already-launched remote-sensing satellites at **under 5%**. The other 95% sits on disk. Capital, in that column’s split, went upstream: satellite internet 41%, rockets 25%, manufacturing 18%, and remote-sensing applications 2%. Three mechanisms:

- Models want to retrain every 5–6 days. The data-production cycle is months. The user asked for “now” and received last year’s scene.
- Launch is the expensive step. The column puts domestic launch near 150,000 RMB per kilogram against Falcon 9 near $3,000 per kilogram, a gap of more than 5×. A 500 kg satellite can cost more to launch than to build.
- The application companies that would create demand are the ones not getting funded.

This is a column citing insiders, not a State Council statistic. It is still the same sentence as the New Space Economy essay, written from the other side of the industry. Full notes are in [04-china.md](04-china.md). <https://finance.sina.com.cn/stock/2026-01-02/doc-inhewkev3855901.shtml>

## What this means for a hackathon

The gap is not “there is no satellite data.” The gap is a person, a question, a deadline, and a pile of portals.

Subproblems that sit inside the gap, each of them a possible project and most of them already half-solved by someone:

- Which product, which version, which date range.
- Cloud cover, and what to do when the optical pass is useless.
- Provenance a journalist or a city attorney will accept.
- Joining the pixel to a thing with a name: a building, a well, a ship, a city department.
- Latency: the event is underway, the archive is yesterday.
- Trust: level-4 products hide errors.
- Distribution: embeddings and new missions are free and still painful to open.
- Money: the buyer with a budget is a defense ministry. The user with the clearest public need often has no budget and no GIS hire.

A weekend project that rebuilds collection, or rebuilds a foundation model, is working on the part of the chain that is already crowded. A weekend project that picks one user and one question, and answers it from data that is already public, is working on the part everyone agrees is open.
