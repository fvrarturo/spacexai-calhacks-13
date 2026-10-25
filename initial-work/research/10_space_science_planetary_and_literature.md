# Space science (astronomy, planetary, heliophysics), mission archives, spacecraft operations data, and "a literature no human can read all of"

**Scope.** Problems, sub-problems, current solutions and off-the-shelf tech in (1) the astronomy data deluge (Rubin/LSST, SKA, Euclid, Roman, JWST, DESI, ZTF, LIGO, citizen science), (2) exoplanets, (3) planetary science (Mars, Moon, asteroids, outer planets), (4) heliophysics science data, (5) mission archives and "dark data", (6) spacecraft operations and engineering knowledge, and (7) the scientific literature itself. Written for a 2-person, 36-hour hackathon team (Cal Hacks 13.0, "Make it Legendary" challenge) looking for a clear problem plus clear solution built on large public space datasets.

**Researched on 2026-10-24.** Status of anything after mid-2026 was checked against the most recent sources found; where a figure could not be confirmed it is marked *unverified*.

Entries whose hackathon angle is marked **Strong candidate**: 3.4 (Mars dust), 3.6 (descent navigation), 3.8 (south-pole ice/site ranking), 3.13 (precovery), 5.1 (mission value under budget cuts), 6.1 (telemetry anomalies), 6.2 (lessons learned), 7.8 (target dossier / duplicate observations).

Credibility scale used: **official** (agency/observatory/mission page or document), **peer-reviewed**, **preprint** (arXiv, not yet refereed), **reputable press**, **trade/blog**, **social post**, **rumor/unverified**.

---

## Part 1. Astronomy data deluge

### 1.1 Vera C. Rubin Observatory / LSST: survey status and alert volume

- **What it is:** 8.4 m survey telescope with a 3,200-megapixel camera in Chile, running the 10-year Legacy Survey of Space and Time (LSST). It images the whole southern sky every few nights and issues a public alert for every change it detects.
- **Status (2026):**
  - First alerts generated on the night of 24 Feb 2026: **800,000 alerts in one night**, each issued "within minutes of image capture" ([Sky & Telescope, 4 Mar 2026](https://skyandtelescope.org/astronomy-news/rubin-observatory-sends-800000-alerts-to-astronomers-per-night/)).
  - LSST formally began **30 June 2026** (some outlets say 1 July) after "a careful operational review of technical readiness, data system performance, and scientific validation" (Ž. Ivezić) ([Tech Times, 1 Jul 2026](https://www.techtimes.com/articles/319434/20260701/rubin-observatory-begins-lsst-nightly-7-million-alert-stream-will-test-if-dark-energy-evolves.htm); [Eastern Herald, 2 Jul 2026](https://easternherald.com/2026/07/02/vera-rubin-observatory-lsst-survey-universe/)).
  - At full capacity, up to **~7 million alerts/night** (older design documents say ~10 million) ([Sky & Telescope](https://skyandtelescope.org/astronomy-news/rubin-observatory-sends-800000-alerts-to-astronomers-per-night/); [Lasair paper, arXiv:2404.08315](https://arxiv.org/pdf/2404.08315)). For comparison, ZTF has produced ~300k alerts/night since 2018 ([CAOSP broker review, 2025](https://www.ta3.sk/caosp/Eedition/Abstracts/2025/Vol_55/No_2/pp95-105_abstract.html)).
  - About **10 TB of images per night** that must be mined quickly ([heise, Feb 2026](https://heise.de/-11192717), via search summary); about **500 PB** over ten years; ~800 visits to each point of the southern sky ([Tech Times](https://www.techtimes.com/articles/319434/20260701/rubin-observatory-begins-lsst-nightly-7-million-alert-stream-will-test-if-dark-energy-evolves.htm)).
  - Data releases: Data Preview 2 planned Jul–Sep 2026; first annual Data Release (DR1) about two years after survey start, around 2028 ([Tech Times](https://www.techtimes.com/articles/319434/20260701/rubin-observatory-begins-lsst-nightly-7-million-alert-stream-will-test-if-dark-energy-evolves.htm)).
- **Problems / pain points:**
  - Volume jump. Or Graur: previous discovery rates were "a few hundred to a few thousand transients per year… Going from that to 800,000 alerts per night is a sea change" ([Sky & Telescope](https://skyandtelescope.org/astronomy-news/rubin-observatory-sends-800000-alerts-to-astronomers-per-night/)).
  - Following up every alert is impossible, so filtering and classification have to be done by machine learning ([Sky & Telescope](https://skyandtelescope.org/astronomy-news/rubin-observatory-sends-800000-alerts-to-astronomers-per-night/)).
  - Alert rate in Feb 2026 was still "relatively low" while template images were being built; each alert carries the light-curve history plus "postage stamp" cutouts (science, template, difference). Rubin reserves a small fraction of time for target-of-opportunity follow-up of LIGO-Virgo-KAGRA events. Rubin's social-media announcement: "The largest spot-the-difference effort ever has begun!" ([APS Physics 19, 31, 5 Mar 2026](https://physics.aps.org/articles/pdf/10.1103/Physics.19.31)). Eric Bellm: alerts are designed to give "enough notice to rapidly obtain time-critical follow-up observations" from "10 terabytes of images nightly" ([AURA, 25 Feb 2026](https://www.aura-astronomy.org/blog/2026/02/25/nsf-doe-vera-c-rubin-observatory-launches-real-time-discovery-machine-for-monitoring-the-night-sky/)).
- **How they're trying to solve it:** Seven community "full-stream" alert brokers (1.2) plus downstream brokers, and ML classifiers. South Africa's SALT (11 m, spectroscopy) and the robotic 1 m Lesedi began following selected Rubin alerts in Feb 2026, with Lesedi characterising photometry fast and SALT classifying ([SAAO, 25 Feb 2026](https://www.saao.ac.za/2026/02/25/south-african-telescopes-to-follow-up-rubin-observatory-alerts-this-week/)).
- **Data:** Alert stream (Avro over Kafka) via brokers. Alerts are world-public with no proprietary period ([Rubin alerts & brokers page](https://rubinobservatory.org/for-scientists/data-products/alerts-and-brokers)). **Data Preview 1** (30 Jun 2025): Science Pipelines v29 images and catalogs from the Commissioning Camera, seven ~1 deg² fields observed over seven weeks in late 2024, only on the Rubin Science Platform and only for data-rights holders, i.e. "all scientists and students in the US and Chile" plus named in-kind members ([DP1 docs](https://dp1.lsst.io/)). A US-university hackathon team qualifies but needs an RSP account. DP2 planned Jul–Sep 2026.
- **Off-the-shelf tech:** Broker APIs/Python clients (ALeRCE client, Fink client, Lasair API, ANTARES client), Kafka, Avro, Google Cloud Pub/Sub (Pitt-Google).
- **Hackathon angle:** "Personal transient feed": a natural-language filter builder that turns "show me young, fast-rising blue transients near galaxies within 100 Mpc" into Lasair SQL / Fink filters, run against the live ZTF+Rubin public streams, with an LLM-written daily digest.
- **Credibility:** reputable press + official.
- **Sources:** [Sky & Telescope, 4 Mar 2026](https://skyandtelescope.org/astronomy-news/rubin-observatory-sends-800000-alerts-to-astronomers-per-night/); [Tech Times, 1 Jul 2026](https://www.techtimes.com/articles/319434/20260701/rubin-observatory-begins-lsst-nightly-7-million-alert-stream-will-test-if-dark-energy-evolves.htm); [NOIRLab press release noirlab2605 (Feb 2026)](https://noirlab.edu/public/news/noirlab2605/) (page did not render when fetched); [Lasair, arXiv:2404.08315 (Apr 2024)](https://arxiv.org/pdf/2404.08315).

### 1.2 Rubin alert brokers (ALeRCE, AMPEL, ANTARES, Babamul, Fink, Lasair, Pitt-Google)

- **What it is:** Rubin lists **seven full-stream brokers**: ALeRCE, AMPEL, ANTARES, Babamul, Fink, Lasair, Pitt-Google. Two downstream brokers, SNAPS and POI, get subsets through partnerships ([Rubin alerts & brokers](https://rubinobservatory.org/for-scientists/data-products/alerts-and-brokers)). Brokers ingest, cross-match, classify, filter and redistribute alerts in real time and are "the public interface to the LSST alert stream" ([Rubin Broker Summit, Institut Pascal, 8–19 Jun 2026](https://www.institut-pascal.universite-paris-saclay.fr/en/scientific-programs/rbs-rubin-broker-summit)).
  - **ALeRCE** (Chile): ingestion, aggregation, cross-matching, ML classification, visualization, Python API.
  - **Lasair** (UK): SQL filters on tabular data plus watchlists and watchmaps ([CAOSP review 2025](https://ftp.ta3.sk/caosp/Eedition/FullTexts/vol55no2/pp95-105.pdf)).
  - **ANTARES** (NOIRLab): as of May 2026 processing the Rubin stream and the ZTF public stream together, running on Google Cloud with Kafka, and helping fulfil Rubin's internal alert-filtering service ([Matheson slides, AmLight, 20 May 2026](https://www.amlight.net/wp-content/uploads/2026/01/Matheson-ANTARES-SA3CC-Tom-Matheson.pdf)).
- **Problems / pain points:**
  - Each broker has its own classifier taxonomy, filter language and API. A scientist has to learn several systems.
  - Classifiers are trained on simulated data (ELAsTiCC/PLAsTiCC) or ZTF and then have to cope with real Rubin data.
- **How they're trying to solve it:** Broker summits, shared taxonomies, active learning (Fink).
- **Data:** Public broker databases (ZTF since 2018, Rubin since Feb 2026).
- **Off-the-shelf tech:** `alerce` and `fink-client` Python packages, the Lasair API, ANTARES Python client, Pitt-Google BigQuery tables.
- **Hackathon angle:** A cross-broker "consensus view": for any object, pull classifications from ALeRCE, Fink, Lasair and ANTARES, show where they disagree, and rank the disagreements as follow-up targets.
- **Credibility:** official + peer-reviewed review.
- **Sources:** [Rubin alerts & brokers page](https://rubinobservatory.org/for-scientists/data-products/alerts-and-brokers); [CAOSP 55(2) 2025 broker review](https://www.ta3.sk/caosp/Eedition/Abstracts/2025/Vol_55/No_2/pp95-105_abstract.html); [ANTARES slides, May 2026](https://www.amlight.net/wp-content/uploads/2026/01/Matheson-ANTARES-SA3CC-Tom-Matheson.pdf); [Rubin Broker Summit 2026](https://www.institut-pascal.universite-paris-saclay.fr/en/scientific-programs/rbs-rubin-broker-summit).

### 1.3 The spectroscopic follow-up bottleneck ("too many transients, too few spectra")

- **What it is:** Classifying a transient definitively usually needs a spectrum. Spectrographs are scarce and slow compared with the alert rate.
- **Problems / pain points:**
  - Kulkarni's analysis of 2019 Transient Name Server reports (surveys then produced ~50 transient candidates per night): "only a tenth of the transients were spectrally classified". He argued the bottleneck would worsen by a factor of 20 or more with LSST, and proposed classifying all SNe brighter than ~19.5 mag and all transients within 200 Mpc ([Kulkarni 2020, "Towards an Integrated Optical Transient Utility", arXiv:2004.03511](https://authors.library.caltech.edu/102525)).
  - Estimates for Rubin: <1% of events will get follow-up (RESSPECT project page, cited in search results); ≲0.1% of all events ([ApJS 2021, iopscience](https://iopscience.iop.org/article/10.3847/1538-4365/ac0893)); "we will be unable to get spectroscopy of more than a handful percent of the discovered transients" ([Fink active-learning paper, arXiv:2502.19555, Feb 2025](https://arxiv.org/pdf/2502.19555)).
- **How they're trying to solve it:**
  - **Active learning to choose which transients get spectra** (Fink + RESSPECT) for early SN Ia classification ([arXiv:2502.19555](https://arxiv.org/pdf/2502.19555)).
  - **4MOST TiDES** survey on ESO VISTA: Rubin-era multiplexed spectroscopy of SNe Ia, AGN, transients and hosts. Automated spectral classifiers DASH + NGSF reach 99.9% purity for SN Ia on 4MOST-like blended spectra but struggle with non-Ia types ([arXiv:2502.12890](https://arxiv.org/html/2502.12890v2)).
  - Photometric classification (no spectrum) with ML.
- **Data:** TNS (Transient Name Server) public reports with classification flags; ZTF Bright Transient Survey; WISeREP spectra archive; broker light curves.
- **Off-the-shelf tech:** SuperNNova, RAPID, ParSNIP, ALeRCE LC classifier, DASH, NGSF, SNID.
- **Hackathon angle:** "Spectrum triage": given tonight's public candidates and a list of telescopes with open time (location, aperture, limiting magnitude), produce a ranked follow-up queue that maximises expected scientific value per hour (rarity score × classifier uncertainty × brightness). Measure against past TNS data: "how many interesting objects would we have caught?"
- **Credibility:** peer-reviewed + preprint.
- **Sources:** [Kulkarni 2020, CaltechAUTHORS](https://resolver.caltech.edu/CaltechAUTHORS:20200414-093156733); [Fink/RESSPECT arXiv:2502.19555 (Feb 2025)](https://arxiv.org/pdf/2502.19555); [4MOST classification arXiv:2502.12890 (Feb 2025)](https://arxiv.org/html/2502.12890v2); [ApJS 2021](https://iopscience.iop.org/article/10.3847/1538-4365/ac0893).

### 1.4 Anomaly detection in survey streams

- **What it is:** Finding the "weird ones" (new classes of objects) in millions of light curves.
- **Problems / pain points:** Supervised classifiers only find what they were trained on. Rare classes are tiny in training sets.
- **How they're trying to solve it:**
  - Isolation forests trained only on signal-free light curves, which flag microlensing and other transients in simulated LSST data, with a drip-feed real-time test for brokers ([Crispim Romão, Croon & Godines, arXiv:2503.09699, MNRAS 543, 351, 2025](https://arxiv.org/pdf/2503.09699)).
  - Real-time anomaly detectors on ZTF that model a known population and treat large deviations as anomalies ([arXiv:2111.00036, 2021](https://arxiv.org/pdf/2111.00036)).
  - Active anomaly detection for extragalactic transients ([Villar et al., arXiv:2103.12102](https://arxiv.org/pdf/2103.12102v1.pdf)).
  - Georgios Dimitriadis on early Rubin data: "Even with the current alert stream, we have identified transients that would be completely missed" ([Sky & Telescope](https://skyandtelescope.org/astronomy-news/rubin-observatory-sends-800000-alerts-to-astronomers-per-night/)).
- **Data:** ZTF public alerts (since 2018), Rubin alerts (2026), ELAsTiCC simulated LSST stream, PLAsTiCC Kaggle dataset.
- **Off-the-shelf tech:** scikit-learn IsolationForest, astronomaly, Fink's anomaly module, foundation models for light curves (see Models & tools slice).
- **Hackathon angle:** "Weirdness radar": embed every public ZTF light curve with a pre-trained light-curve encoder, flag the top-k outliers each night, and let an expert-in-the-loop give thumbs up/down (active learning) in a slick UI.
- **Credibility:** peer-reviewed.
- **Sources:** [arXiv:2503.09699 (Mar 2025)](https://arxiv.org/pdf/2503.09699); [arXiv:2111.00036 (Nov 2021)](https://arxiv.org/pdf/2111.00036); [arXiv:2103.12102 (Mar 2021)](https://arxiv.org/pdf/2103.12102v1.pdf).

### 1.5 Satellite streaks in Rubin images (brief; see Space traffic slice)

- **What it is:** Low-Earth-orbit satellites cross Rubin's 3.5° field of view and leave bright streaks.
- **Problems / pain points:** Rubin FAQ (updated Mar 2026): LEO satellites "pose a real challenge… rendering the underlying sources undetectable"; LSST is "especially vulnerable to systematic errors" from this light pollution ([Rubin LEO-sats FAQ](https://rubinobservatory.org/es/for-scientists/frequently-asked-questions/leo-sats)). Older projection: 30–40% of exposures on very wide-field telescopes like Rubin compromised in twilight hours ([Inverse](https://www.inverse.com/science/elon-musks-starlink-is-having-a-pernicious-effect-on-astronomy), older). Simulation: trading 10% of observing time for satellite avoidance halves the fraction of visits with streaks ([Hu et al. 2022, arXiv:2211.15908](https://ar5iv.labs.arxiv.org/html/2211.15908)).
- **How they're trying to solve it:** Scheduler-level avoidance, streak masking in the pipeline, SpaceX darkening/brightness mitigation.
- **Data:** Rubin DP1/DP2 images; public TLEs/ephemerides (CelesTrak).
- **Hackathon angle:** Predict which Rubin pointings tonight will be crossed by catalogued satellites, using TLEs and the published Rubin schedule. A small "satellite weather forecast" for observers.
- **Credibility:** official + preprint.
- **Sources:** [Rubin FAQ (Mar 2026)](https://rubinobservatory.org/es/for-scientists/frequently-asked-questions/leo-sats); [arXiv:2211.15908 (2022)](https://ar5iv.labs.arxiv.org/html/2211.15908); [Lu 2024, arXiv:2403.11118](https://arxiv.org/html/2403.11118v1); [Clear Orbit substack](https://clearorbit.substack.com/p/science-vs-satellite-swarms) (blog).

### 1.6 SKA Observatory: data rates and the compute problem

- **What it is:** Square Kilometre Array (SKA-Low in Australia, SKA-Mid in South Africa), under construction, science verification 2026–27.
- **Problems / pain points:**
  - Raw digitised data for SKA-Low "at the rate of about two petabytes per second" (SKAO computing lead, quoted in [DatacenterDynamics](https://www.datacenterdynamics.com/en/analysis/square-kilometer-array/)).
  - Delivered science data products **~700 PB/year** (other sources ~600 PB/year) to a global network of SKA Regional Centres (SRCNet) ([arXiv:2504.03103, "The challenge of the data in the SRCNetwork", Apr 2025](https://arxiv.org/pdf/2504.03103)).
  - Ramp: science verification weeks in 2026–27 estimated at ~1.5 PB/week (Low, 29 Gbps) and ~2 PB/week (Mid, 39 Gbps); from 2030, 216 PB/yr (Low) + 400 PB/yr (Mid) ([SKAO/SRCNet LHCOPN slides, 2025](https://indico.cern.ch/event/1479019/contributions/6379931/attachments/3035107/5359575/SKAO%20and%20SRCNet%20LHCOPN%20meeting%20presentation%20-%20Shari%20&%20Rosie.pdf)).
  - Users cannot download data; they must compute where the data is. Figures across sources are inconsistent (per telescope vs combined, peak vs average).
- **How they're trying to solve it:** SRCNet federated science platform (Rucio data management, IVOA services); user interaction with SRCNet expected towards end of 2026 ([arXiv:2504.03103](https://arxiv.org/pdf/2504.03103)); SKA Science Data Challenges.
- **Data:** SKA precursors are public now: MeerKAT, ASKAP (RACS, EMU, WALLABY via CASDA), MWA, LOFAR (LoTSS). SKA Data Challenge datasets.
- **Off-the-shelf tech:** CASA, WSClean, PyBDSF, source finders (SoFiA), radio-galaxy morphology classifiers.
- **Hackathon angle:** Radio source cross-identification: match ASKAP/EMU radio blobs to optical/IR host galaxies (a task currently done by Radio Galaxy Zoo volunteers).
- **Credibility:** preprint + official slides + trade press.
- **Sources:** [arXiv:2504.03103 (Apr 2025)](https://arxiv.org/pdf/2504.03103); [LHCOPN slides (2025)](https://indico.cern.ch/event/1479019/contributions/6379931/attachments/3035107/5359575/SKAO%20and%20SRCNet%20LHCOPN%20meeting%20presentation%20-%20Shari%20&%20Rosie.pdf); [DatacenterDynamics](https://www.datacenterdynamics.com/en/analysis/square-kilometer-array/); [UKSRC slides](https://indico.ph.qmul.ac.uk/event/2275/sessions/1467/attachments/3325/2632/UKSRC%20Data%20distribution%20modelling%20Slides%20-%20JW.pdf); [SKAO "Handling a deluge of big data"](https://skao.int/af/node/24).

### 1.7 Euclid: strong-lens search as a human + machine pipeline

- **What it is:** ESA's wide survey telescope (launched 2023). Quick Release Q1 (Mar 2025) and the first data release DR1 (search ongoing).
- **Problems / pain points:**
  - Networks trained only on simulations "recover up to 92% of simulated lenses with 100% purity, but only achieve 50% completeness with 24% purity on real Euclid data" ([Euclid Q1 Strong Lensing Discovery Engine C, arXiv:2503.15326](https://arxiv.org/pdf/2503.15326)).
  - Volume: for DR1, ML lens finders classified "a whopping 72 million galaxies"; volunteers now inspect "hundreds of thousands of high scoring lens candidates" ([Space Warps – ESA Euclid, Zooniverse](https://www.zooniverse.org/projects/aprajita/space-warps-esa-euclid/about/results)).
- **How they're trying to solve it:** Zoobot (fine-tuned) ranks 1 M Q1 objects; the top 1,000 contained 122 grade-A and 41 grade-B lenses; citizen scientists plus experts produced a catalogue of ~500 high-quality lenses, almost all new ([arXiv:2503.15326](https://arxiv.org/pdf/2503.15326); [Space Warps blog, 19 Mar 2025](https://blog.spacewarps.org/2025/03/19/space-warps-helps-to-find-497-spectacular-lenses-in-euclid-data/)). 5 million classifications since Q1 search began, 2.7 M in DR1 search ([Space Warps blog](https://blog.spacewarps.org/tag/euclid)).
- **Data:** Euclid Q1 (public, ESA Euclid Science Archive / IRSA mirror), ~63 deg²; DR1 under proprietary period then public.
- **Off-the-shelf tech:** Zoobot (Hugging Face weights), Galaxy Zoo labels.
- **Hackathon angle:** Lens-candidate triage with a vision foundation model plus similarity search ("find more like this lens") on Euclid Q1 cutouts.
- **Credibility:** peer-reviewed (Euclid collaboration A&A) + official project pages.
- **Sources:** [arXiv:2503.15326 (Mar 2025)](https://arxiv.org/pdf/2503.15326); [arXiv:2508.14624 (Aug 2025)](https://arxiv.org/pdf/2508.14624); [Space Warps blog (Mar 2025)](https://blog.spacewarps.org/2025/03/19/space-warps-helps-to-find-497-spectacular-lenses-in-euclid-data/); [Zooniverse Space Warps Euclid](https://www.zooniverse.org/projects/aprajita/space-warps-esa-euclid).

### 1.8 Nancy Grace Roman Space Telescope

- **What it is:** NASA wide-field infrared flagship.
- **Status:** **Launched 30 Aug 2026, 7:26 a.m. EDT on a Falcon Heavy from LC-39A**, three-month cruise to Sun-Earth L2 ([NASA SVS / science.nasa.gov](https://science.nasa.gov/?p=1225642); [Sci.News](https://www.sci.news/astronomy/roman-space-telescope-launch-15027.html)). It was ready about eight months ahead of the May 2027 commitment date ([SpacePolicyOnline](https://spacepolicyonline.com/news/nasa-sets-launch-date-for-roman-space-telescope/)).
- **Problems / pain points:** Roman will produce many times Hubble's sky area at Hubble-like resolution. Data rates and community readiness (processing, cross-matching with Rubin and Euclid) are open problems; Roman is listed as protected in the FY2027 request ([Planetary Society, 23 Apr 2026](https://www.planetary.org/articles/analyzing-the-fy-2027-nasa-budget-request)).
- **Data:** Will be public with no proprietary period (Roman policy; *unverified in this pass*). Simulated Roman data exist (OpenUniverse/Roman simulations).
- **Hackathon angle:** Rubin × Euclid × Roman cross-match "deblending" demos with simulations; probably too heavy for 36 h.
- **Credibility:** official + reputable press.
- **Sources:** [science.nasa.gov (Aug 2026)](https://science.nasa.gov/?p=1225642); [Sci.News (Aug 2026)](https://www.sci.news/astronomy/roman-space-telescope-launch-15027.html); [SpacePolicyOnline](https://spacepolicyonline.com/news/nasa-sets-launch-date-for-roman-space-telescope/); [Live Science](https://livescience.com/space/space-exploration/nasas-nancy-grace-roman-space-telescope-is-set-to-launch-this-weekend-when-will-we-see-its-first-photos).

### 1.9 JWST proposal oversubscription (Cycle 5)

- **What it is:** Competition for JWST time.
- **Problems / pain points:**
  - Cycle 5: **2,930 proposals submitted**, "a new record for proposals received in response to any Call for Proposals by a major observatory"; 2,855 compliant after 75 disqualified ([STScI newsletter 2026 vol. 43 issue 01](https://www.stsci.edu/contents/newsletters/2026-volume-43-issue-01/jwst-cycle-5-proposal-selection)).
  - Oversubscription: GO 1 in 11.4 by proposals and 1 in 12.5 by prime hours; Surveys 1 in 17.3; Archival 1 in 9.6 ([JW5 TAC results](https://stsci-docs.stsci.edu/policies/files/250513868/250513872/1/1778695182011/JW5-TAC-Results-Public.pdf)). About 8,000 hours of prime time, cycle starting 1 Jul 2026.
  - Every proposal needs multiple expert reviewers: the review burden scales with submissions.
- **How they're trying to solve it:** Dual-anonymous review; external panels; at ESO and ALMA, distributed peer review (see 7.10).
- **Data:** STScI publishes accepted programs (abstracts, targets) and MAST holds all past observations: so "has this been done?" is answerable (see 7.11).
- **Hackathon angle:** "Proposal prior-art check": paste an abstract + target list, get back all past JWST/HST programs on those targets and similar science, plus relevant papers (MAST + ADS APIs).
- **Credibility:** official.
- **Sources:** [STScI Cycle 5 selection (2026)](https://www.stsci.edu/contents/newsletters/2026-volume-43-issue-01/jwst-cycle-5-proposal-selection); [JW5 TAC results PDF](https://stsci-docs.stsci.edu/policies/files/250513868/250513872/1/1778695182011/JW5-TAC-Results-Public.pdf).

### 1.10 DESI (Dark Energy Spectroscopic Instrument)

- **What it is:** 5,000-fibre spectroscopic survey at Kitt Peak.
- **Data volume:** Public DR1 = ~14.5 M extragalactic + 4 M stellar spectra (first year). DR2 (three years) covers >33 M extragalactic + 12 M stellar spectra, but DR2 spectra/redshifts were not yet public as of the documentation page; only cosmology chains released ([DESI key publications](https://data.desi.lbl.gov/doc/papers/); [arXiv:2605.02999](https://arxiv.org/pdf/2605.02999)).
- **Problems / pain points:** DR2 BAO is in mild 2.3σ tension with CMB-preferred parameters (evolving dark energy hint) ([DESI DR2 guide, 19 Mar 2025](https://www.desi.lbl.gov/2025/03/19/desi-dr2-results-march-19-guide/)). Tens of millions of spectra, with very few humans looking at any individual one.
- **Hackathon angle:** Spectral anomaly search ("find the weirdest 100 spectra in DESI DR1") using embeddings from a spectrum foundation model. Public, large, and clearly framed.
- **Credibility:** official + preprint.
- **Sources:** [DESI DR2 guide (Mar 2025)](https://www.desi.lbl.gov/2025/03/19/desi-dr2-results-march-19-guide/); [DESI papers page](https://data.desi.lbl.gov/doc/papers/); [arXiv:2605.02999 (May 2026)](https://arxiv.org/pdf/2605.02999).

### 1.11 Zwicky Transient Facility (ZTF)

- **What it is:** Palomar 48-inch survey, Rubin's northern precursor.
- **Status:** NSF granted ~$1.6 M to continue science operations in 2025 and 2026, overlapping Rubin ([ZTF news](https://www.ztf.caltech.edu/new/nsf-funds-ztf-to-work-with-vera-rubin.html)); Data Release 24 on 22 Jan 2026 ([IRSA ZTF](https://irsawebops2.ipac.caltech.edu/Missions/ztf.html)). Funding beyond 2026 not found (*unverified*).
- **Problems / pain points:** Possible end of northern-sky time-domain coverage after 2026; data continuity.
- **Data:** ~300k alerts/night public; light curves via IRSA; >8 years of baseline. Open.
- **Hackathon angle:** ZTF is the best ready-made sandbox for anything Rubin-flavoured: tested broker APIs, long baselines, labelled samples (Bright Transient Survey).
- **Credibility:** official.
- **Sources:** [ZTF NSF funding news](https://www.ztf.caltech.edu/new/nsf-funds-ztf-to-work-with-vera-rubin.html); [ZTF newsletter issue 14](https://sites.astro.caltech.edu/ztf-newsletter/issue-14/index.html); [IRSA ZTF page](https://irsawebops2.ipac.caltech.edu/Missions/ztf.html).

### 1.12 Gravitational waves: LIGO–Virgo–KAGRA O4 and what comes next

- **What it is:** Ground-based gravitational-wave detectors issuing public low-latency alerts.
- **Status:**
  - O4 ran 24 May 2023 – 18 Nov 2025. About **250 candidate signals** in real time; offline analysis of the first segment yielded 128 significant events (GWTC-4.0); 218 confident detections cumulatively through O4a vs 90 in O1–O3 ([LIGO news, Nov 2025](https://ligo.org/ligo-virgo-kagra-collaboration-successfully-wraps-up-its-fourth-observing-run/)).
  - GWTC-5.0 (second O4 segment): 1,886 candidates with FAR < 2/day in at least one pipeline, 161 with p_astro ≥ 0.5 ([arXiv:2605.27225](https://arxiv.org/pdf/2605.27225)).
  - Next: a ~six-month run expected to start late summer/early fall 2026 ([LIGO news](https://ligo.org/ligo-virgo-kagra-collaboration-successfully-wraps-up-its-fourth-observing-run/)); Wikipedia says November 2026 ([List of GW observations](https://en.wikipedia.org/wiki/List_of_gravitational_wave_observations)); O5 was "currently expected to start in late 2027" ([LVK OpenMMA update, Feb 2025](https://dcc.ligo.org/public/0198/G2500315/002/20250220_OpenMMA_LVKUpdate.pdf); [observing plan](https://observing.docs.ligo.org/plan)).
- **Problems / pain points:**
  - Budget: FY2026 White House request proposed closing one of the two LIGO sites and cutting operations from $48 M to $29 M ([Sky & Telescope](https://skyandtelescope.org/astronomy-news/shattering-nsf-budget-proposal-threatens-gravitational-wave-science/); [Yahoo/Tri-City Herald](https://www.yahoo.com/news/trump-science-cuts-may-close-120000151.html)). Congress reportedly rejected closure and allotted "not less than $49 million" ([Big Think](https://bigthink.com/?p=596712), *verify against bill text*).
  - Electromagnetic follow-up of GW sky maps (tens to hundreds of deg²) is a tiling and galaxy-ranking problem; glitches (detector noise transients) need classification (Gravity Spy on Zooniverse).
- **Data:** GraceDB public superevents; GCN Kafka alerts; GWOSC strain data and catalogs (open).
- **Off-the-shelf tech:** gwpy, ligo.skymap, Gravity Spy labels.
- **Hackathon angle:** "Where to point": given a GW sky map, rank galaxies in the localisation volume (GLADE+ catalog) and generate an observing plan for small telescopes worldwide.
- **Credibility:** official + peer-reviewed.
- **Sources:** [LIGO O4 wrap-up (Nov 2025)](https://ligo.org/ligo-virgo-kagra-collaboration-successfully-wraps-up-its-fourth-observing-run/); [GWTC-4.0 arXiv:2508.18082](https://arxiv.org/pdf/2508.18082); [GWTC-5.0 arXiv:2605.27225](https://arxiv.org/pdf/2605.27225); [LVK detchar O4b/c arXiv:2608.12193](https://arxiv.org/pdf/2608.12193); [Sky & Telescope on NSF cut](https://skyandtelescope.org/astronomy-news/shattering-nsf-budget-proposal-threatens-gravitational-wave-science/).

### 1.13 Citizen science (Zooniverse) and the classification-scaling problem

- **What it is:** Zooniverse: >120 projects and nearly 1.7 M volunteers (2018 abstract, figure via search summary; [arXiv:1903.07776](https://arxiv.org/pdf/1903.07776), [science.gov records](https://www.science.gov/topicpages/z/zoo+supernova+project)). Current totals not verified.
- **Problems / pain points:** "Humans don't scale. Surveys keep getting bigger, but we will always have the same number of volunteers" ([Galaxy Zoo blog](https://blog.galaxyzoo.org/tag/galaxy-zoo)). Models need tens to hundreds of thousands of labelled images and still struggle with rare classes (lenses, irregulars, mergers) ([Galaxy Zoo: Cosmic Dawn, arXiv:2509.22311](https://arxiv.org/pdf/2509.22311)). No public, current backlog figures found.
- **How they're trying to solve it:** Human-machine partnership: Zoobot pre-classifies easy objects and runs active learning so volunteers see the hard cases ([arXiv:2509.22311](https://arxiv.org/pdf/2509.22311)). Backyard Worlds "Cool Neighbors" used ML pre-selection; volunteers made ~3× more classifications per unit time than in the sibling project without AI ([Citizen Science: Theory and Practice, Dec 2024](https://doaj.org/article/122c378549a84b31a3ddb968abc9ffa5)).
- **Data:** Galaxy Zoo labels (DECaLS, GZ2, Cosmic Dawn), Space Warps, Gravity Spy, Bursts from Space: MeerKAT ([arXiv:2304.14157](https://arxiv.org/pdf/2304.14157)).
- **Off-the-shelf tech:** Zoobot, Panoptes CLI, Zooniverse Project Builder.
- **Hackathon angle:** "Which images should humans see?": an uncertainty-ranked queue for any Zooniverse-style project, demonstrating how many volunteer-hours are saved for equal accuracy.
- **Credibility:** peer-reviewed + blog.
- **Sources:** as linked above; [Optimizing the Human-Machine Partnership with Zooniverse](https://deepai.org/publication/optimizing-the-human-machine-partnership-with-zooniverse).

### 1.14 Hubble: operating on one gyro and a shrinking budget

- **What it is:** HST (launched 1990; last servicing 2009). It has run in **one-gyro mode since 14 Jun 2024** ([Sky & Telescope](https://skyandtelescope.org/astronomy-news/hubble-pauses-science-operations-for-transition-to-one-gyro-mode/)). That cuts observations ~12% (85 → 74 orbits/week, NASA estimate) and halves the observable sky at any one time ("approximately half", Tom Brown, STScI). NASA declined a private reboost/rescue mission ([Scientific American](https://www.scientificamerican.com/article/nasa-rejects-hubble-space-telescope-rescue-mission-and-trims-its-science/)).
- **Problems / pain points:** The 2025 Senior Review told Hubble to budget at President's-request levels, ">20%" below the cost of unchanged operations. STScI's proposal keeps all modes but makes **ACS/WFC and WFC3/IR "shared-risk" with no observer support and minimal calibration** (impactful science for ~3 years), cuts grants ~30% below Cycle 32 and allocates them by formula rather than peer review, and removes staff "expert in responding to unexpected failures", which raises mission risk ([STScI STUC newsletter 2025 vol. 42](https://www.stsci.edu/contents/newsletters/2025-volume-42-issue-01/meeting-of-hubble's-space-telescope-users-committee-stuc); [HST Operational Paradigm Change Review](https://hst-docs.stsci.edu/hsp/hst-general-science-policies/nasa-hubble-operational-paradigm-change-review-and-hubble-observations); [Astronomy.com](https://www.astronomy.com/science/james-webb-hubble-space-telescopes-face-reduction-in-operations-over-funding-shortfalls/)). Budget numbers vary ($93.3 M planned for 2024 → $85 M for 2026 per one report; FY25 request $88.9 M per STScI). The final FY2026 Hubble level was not confirmed.
- **Why it matters for the hackathon:** Less calibration support and fewer support scientists mean archival users must self-diagnose calibration problems. Knowledge capture (6.2/6.3) applies to observatories too.
- **Data:** MAST HST archive (public), HST bibliography.
- **Hackathon angle:** "Calibration-drift watchdog": track zero-points and PSF from public HST calibration observations over time and alert archival users when shared-risk modes drift.
- **Credibility:** official (STScI) + reputable press.

---

## Part 2. Exoplanets

### 2.1 TESS candidate backlog and false-positive vetting

- **What it is:** TESS flags transit-like signals ("Threshold Crossing Events", TCEs). Promising ones become TESS Objects of Interest (TOIs). Confirmation needs ground-based follow-up (TFOP), and TESS's large pixels (21″) mean blended eclipsing binaries are a common false positive.
- **Problems / pain points:** Low angular resolution means nearby stars can cause false positives that TESS cannot rule out, so ground observers with larger telescopes must confirm ([Union College TFOP summary 2026](https://steinmetz.union.edu/node/1440503797)). Some candidates have only two transits years apart, so the period is ambiguous (TOI-2076 c/d, [arXiv:2111.01311](https://export.arxiv.org/abs/2111.01311)).
- **How they're trying to solve it:** ML vetting (ExoMiner++, 2.2), statistical validation (TRICERATOPS, VESPA), TFOP coordination on ExoFOP.
- **The backlog in numbers (Oct 2026):** **8,151 TOIs** listed on ExoFOP-TESS ([ExoFOP-TESS](https://exofop.ipac.caltech.edu/tess/)) and in the NASA Exoplanet Archive vs **1,012 TESS confirmed planets**, out of 6,451 confirmed exoplanets in total ([NASA Exoplanet Archive counts](https://exoplanetarchive.ipac.caltech.edu/docs/counts_detail.html)). TESS crossed 1,000 confirmed planets in the week of 8 Oct 2026 ([Wikipedia, TESS](https://en.wikipedia.org/wiki/Transiting_Exoplanet_Survey_Satellite)). So **~7,000 TOIs are unresolved or false positives**, roughly 8 candidates for every confirmation. Kepler still has 1,977 unconfirmed candidates (Exoplanet Archive).
- **Data:** ExoFOP-TESS TOI table (public, CSV); MAST TESS light curves (2-min, 20-s, FFIs); NASA Exoplanet Archive.
- **Hackathon angle:** "Which TOI should I observe tonight?": given an amateur/small-college telescope location and aperture, rank open TOIs by predicted transit visibility tonight, depth detectability, and how much a new observation would reduce false-positive probability.
- **Credibility:** peer-reviewed + official.
- **Sources:** [TESS TOI catalog paper (Guerrero et al. 2021)](https://oro.open.ac.uk/77923); [EPSC 2026 TOI-261 abstract](https://meetingorganizer.copernicus.org/EPSC2026/EPSC2026-891.html); [TOI-2076/1807 arXiv:2111.01311](https://export.arxiv.org/abs/2111.01311).

### 2.2 ExoMiner / ExoMiner++ (NASA Ames)

- **What it is:** Deep-learning transit classifier. ExoMiner++ (Feb 2025) uses transfer learning from Kepler to 2-min TESS data.
- **Results:** Of 147,568 unlabeled TCEs, 7,330 flagged as planet candidates, corresponding to 1,868 existing TOIs, 69 CTOIs and 50 new; of 2,506 ExoFOP planet candidates, 1,797 kept as candidates; a full vetting catalog with scores released ([Valizadegan et al., arXiv:2502.09790](https://arxiv.org/abs/2502.09790)). Reportedly released open-source on GitHub (Jan 2026 report, [SuperKalam](https://superkalam.com/current-affairs/26-01-2026/exominer-planet-spotter-pgii-74818a19-c7dc-4d8c-8574-21eb791ca612), *unverified against a NASA source*).
- **Problems / pain points:** Noisy TESS labels; most TCEs are false positives; disagreement between ML scores and human dispositions.
- **Hackathon angle:** "Second opinion on TOIs": take the ExoMiner++ catalog, find TOIs where ExoMiner++ and ExoFOP dispositions disagree, and present the evidence (light curve, centroid, odd/even depths) in a vetting card. A follow-up shortlist.
- **Credibility:** peer-reviewed (AJ) + aggregator.
- **Sources:** [arXiv:2502.09790 (Feb 2025)](https://arxiv.org/abs/2502.09790); [astrobiology.com summary (18 Feb 2025)](https://astrobiology.com/2025/02/18/exominer-on-tess-with-transfer-learning-from-kepler-transit-classification-and-vetting-catalog-for-2-min-data/).

### 2.3 Habitable Worlds Observatory (HWO) planning

- **What it is:** NASA's future flagship to directly image Earth-like exoplanets (2020 Astrophysics Decadal's top recommendation).
- **Status:** FY2026 enacted $150 M for HWO; FY2027 request (3 Apr 2026) asks for **$5 M** ([Wikipedia HWO](https://en.wikipedia.org/wiki/Habitable_Worlds_Observatory)). Jan 2026: seven companies reportedly got three-year fixed-price technology study contracts (same source, *unverified*). Concept maturation paper Jan 2026 ([astrobiology.com](https://astrobiology.com/2026/01/21/habitable-worlds-observatorys-concept-and-technology-maturation-initial-feasibility-and-trade-space-exploration/)).
- **Problems / pain points:** Precursor science: the stellar properties of ~100s of target stars (activity, companions, exozodi dust) must be characterised before launch. The community list is HWO TSS25 (PASP, Oct 2025), tiered by priority and urgency of precursor observations ([TSS25 summary](https://astrobiology.com/2025/09/hwo-target-stars-and-systems-a-prioritized-community-list-of-potential-stellar-targets-for-the-habitable-worlds-observatorys-exoearth-survey.html); [Caltech record](https://authors.library.caltech.edu/records/y4tp1-btn45)).
- **Data:** TSS25 target list; Gaia DR3; TESS/Kepler; archival RV.
- **Hackathon angle:** "HWO target dossier": for each TSS25 star, auto-assemble what is known (Gaia, TESS, RV surveys, literature via ADS) and flag knowledge gaps. A precursor-science gap map.
- **Credibility:** peer-reviewed + Wikipedia.
- **Sources:** [Wikipedia HWO](https://en.wikipedia.org/wiki/Habitable_Worlds_Observatory); [TSS25 (PASP, Oct 2025)](https://www.ipac.caltech.edu/publication/2025PASP..137j4402T); [ExEP target list webinar (Mar 2023)](https://exoplanets.nasa.gov/internal_resources/2675/TargetListSeminar_HWO_202303.pdf).

---

## Part 3. Planetary science

### 3.1 Mars relay network crisis (MAVEN lost, Odyssey near end, MRO aging)

- **What it is:** Curiosity and Perseverance send almost all of their data through orbiters (the Mars Relay Network). Before Dec 2025 the network had five orbiters (one a backup): NASA's MRO (2005), Odyssey (2001), MAVEN (2013), and ESA's Trace Gas Orbiter and Mars Express (2003).
- **Problems / pain points:**
  - **MAVEN lost.** Last telemetry 4 Dec 2025, then contact lost during a planned occultation; tracking fragments suggested it was "rotating in an unexpected manner". NASA formally ended the mission **3 Jun 2026** ([Scientific American, 3 Jun 2026](https://scientificamerican.com/article/nasas-mars-mission-maven-is-lost-forever)). MAVEN ranked second in relay traffic after TGO and did far more relay work than NASA's other two relays (same source). Its FY2026 request had zeroed its funding (it cost $22.6 M to operate in 2024) ([search summary of reporting](https://www.galvnews.com/ap/nasa-loses-contact-with-its-maven-spacecraft-orbiting-mars-for-the-past-decade/article_637e6d91-0ee4-55aa-bb75-895f63f5ff5b.html)).
  - **Odyssey** will run out of fuel "probably some time in the next couple of years" (Ars Technica, Dec 2025, via [search result](https://scour.ing/@emschwartz/p/https://arstechnica.com/space/2025/12/nasa-just-lost-contact-with-a-mars-orbiter-and-will-soon-lose-another-one)); Odyssey is named for cancellation in the FY2027 request ([Planetary Society, 23 Apr 2026](https://www.planetary.org/articles/analyzing-the-fy-2027-nasa-budget-request)).
  - **Mars Express** (23 years) has a highly elliptical orbit (300–10,000 km) that gives rovers only narrow relay windows ([Hackaday, 24 Sep 2026](https://hackaday.com/2026/09/24/after-decades-nasa-may-finally-replace-mars-relays/)).
  - **MRO** has fuel into the 2030s (Ars, via search), but its eventual failure "would create a capability gap that no current NASA mission is positioned to fill" ([cislunarspace.cn, Jun 2026](https://cislunarspace.cn/en/space-news/2026/06/2026-06-03-nasa-maven-mission-end/), aggregator).
- **How they're trying to solve it:** July 2025 reconciliation bill allocated **$700 M** to revive a Mars Telecommunications Orbiter (launch by 2028). NASA issued an RFP for the renamed Mars Telecommunications Network in May 2026 (≥1 TB store-and-forward, 150 Mbps Mars-to-Earth target, ≥20 kg science payload). **Blue Origin won the fixed-price contract in Sep 2026; Rocket Lab protested to the GAO**, which halts work for up to 100 days. Mars launch windows are 26 months apart, so delay risks pushing it to the next decade ([Hackaday, 24 Sep 2026](https://hackaday.com/2026/09/24/after-decades-nasa-may-finally-replace-mars-relays/)).
- **Data:** Relay pass schedules aren't public, but orbiter ephemerides are (NAIF SPICE kernels via PDS NAIF node). Rover downlink volumes per sol are partly published in PDS release notes and mission blogs.
- **Off-the-shelf tech:** SPICE (spiceypy), Delay/Disruption-Tolerant Networking (ION-DTN), scheduling solvers (OR-Tools).
- **Hackathon angle:** "Mars relay planner": use SPICE ephemerides for MRO, Odyssey, TGO and Mars Express plus rover positions to compute every relay overpass for the next month, then show how much rover data capacity disappears when MAVEN (gone) and Odyssey (next) drop out, and how much a 2029 MTN orbiter would restore. A clear "problem → number → solution" story.
- **Credibility:** reputable press (SciAm, Hackaday) + aggregator.
- **Sources:** [Scientific American (3 Jun 2026)](https://scientificamerican.com/article/nasas-mars-mission-maven-is-lost-forever); [Hackaday (24 Sep 2026)](https://hackaday.com/2026/09/24/after-decades-nasa-may-finally-replace-mars-relays/); [Planetary Society FY27 analysis (23 Apr 2026)](https://www.planetary.org/articles/analyzing-the-fy-2027-nasa-budget-request); [Slashdot thread on MAVEN loss (11 Dec 2025)](https://tech.slashdot.org/story/25/12/11/0026246/) (social).

### 3.2 HiRISE and Mars orbital imagery volume

- **What it is:** MRO's HiRISE camera (~25–30 cm/pixel) plus CTX (6 m/pixel, near-global) and CRISM.
- **Problems / pain points:** Sheer volume relative to the number of people who look at it. HiRISE had captured ">6 million images", ">194 terabytes of data sent from Mars since 2006" by MRO's 15th anniversary (~2020) ([search summary of NASA-sourced figure](https://www.universetoday.com/articles/how-much-science-data-has-the-mars-reconnaissance-orbiter-sent-to-earth)); a 2019 HiRISE ops talk reported ">39,800 gigapixels or 39 TB of raw data" ([HiRISE SciOps, ISOW 2019](https://isow.space.swri.edu/downloads/Day2/002%20kblock_HiRISE_SciOps_ISOW_2019.pdf)). Figures differ by counting method: *treat as order-of-magnitude*.
- **How they're trying to solve it:** HiWish public targeting, PDS Imaging Node, USGS mosaics; ML landmark classifiers used for PDS image search (*background knowledge, not re-verified in this pass*).
- **Data:** PDS Imaging Node (HiRISE RDRs and DTMs); a global CTX mosaic exists (Murray Lab, Caltech; *not re-verified in this pass*). NASA data are generally public domain.
- **Off-the-shelf tech:** CLIP/SigLIP image embeddings, SAM segmentation, GDAL, Mars Trek APIs.
- **Hackathon angle:** "Semantic Mars search": embed HiRISE browse images and let a user type "fresh impact crater with dark ejecta near a recurring slope lineae site". Change detection between repeat HiRISE images (new impacts, dune motion, gully activity) is another option.
- **Credibility:** official (older numbers).
- **Sources:** [Universe Today](https://www.universetoday.com/articles/how-much-science-data-has-the-mars-reconnaissance-orbiter-sent-to-earth); [HiRISE SciOps 2019](https://isow.space.swri.edu/downloads/Day2/002%20kblock_HiRISE_SciOps_ISOW_2019.pdf); [MRO archive plan (PDS)](https://pds-imaging.jpl.nasa.gov/data/mro/mars_reconnaissance_orbiter/ctx/mrox_0357/document/mro_arch_plan.pdf).

### 3.3 Crater detection and counting (surface dating)

- **What it is:** Crater size-frequency distributions are the main way to date planetary surfaces, and they're also used for navigation (crater-based terrain-relative navigation).
- **Problems / pain points:** Manual counting is slow and inconsistent between counters; small craters are numerous; ML catalogs disagree with human catalogs at small sizes.
- **How they're trying to solve it:**
  - DeepMoon/UNet on DEMs (Lee 2019) found ~¾ of resolvable craters with 5–10% median diameter error vs existing catalog; a 2020 follow-up found 80% of known Mars craters >3 km plus ~7,000 potentially new craters ([arXiv:1904.07991](https://arxiv.org/pdf/1904.07991); [human-level crater detection](https://cs.paperswithcode.com/paper/automated-crater-detection-with-human-level)).
  - YOLO-based Moon+Mars two-stage framework ([Ma, Yu & Chandra, arXiv:2508.03920, Aug 2025](https://arxiv.org/html/2508.03920v1)).
  - LU5M812TGT AI global lunar catalog of craters ≥0.4 km (ISPRS J. Photogramm., 2025) ([AMiner record](https://cn.aminer.org/pub/675ae6a3ae8580e7ff91e4d4/lu-m-tgt-an-ai-powered-global-database-of-impact-craters-km)).
- **Data:** Robbins Mars (~384k craters ≥1 km) and Moon (~1.3 M craters ≥1 km) catalogs (*not re-verified in this pass*); THEMIS IR, CTX, LRO WAC/NAC, LOLA/Kaguya DEMs.
- **Off-the-shelf tech:** YOLOv8/v11, SAM, Craterstats (crater-age fitting).
- **Hackathon angle:** "Date this terrain": user draws a polygon on a CTX/LRO mosaic, a detector counts craters, and Craterstats-style fitting returns a model age with uncertainty, alongside the human catalog's answer.
- **Credibility:** peer-reviewed + preprint.
- **Sources:** as linked.

### 3.4 Mars dust storm monitoring

- **What it is:** Dust storms threaten solar-powered landers and affect atmospheric entry and landing. MRO's MARCI produces daily global weather maps.
- **Problems / pain points:** Storm identification is largely manual; MARCI maps have gaps.
- **How they're trying to solve it:**
  - **MDAD (Mars Dust Activity Database) v1.1**: storm boundary masks for Mars Years 28–32, NetCDF, on Zenodo ([Zenodo 7480334, 24 Dec 2022](https://zenodo.org/records/7480334)).
  - CBAM-attention U-Net segmentation of MARCI MDGMs: IoU 0.65, Dice 0.69, ~1.95 M parameters vs ~23 M for prior methods, with a patching strategy for missing data ([Univ. Udine record, 2025](https://air.uniud.it/handle/11390/1318266)).
  - Mask R-CNN on MGS MOC daily maps, mAP50 ~62% ([Alshehhi & Gebhardt 2022, PEPS](https://progearthplanetsci.springeropen.com/articles/10.1186/s40645-021-00464-1)).
- **Data:** MARCI Daily Global Maps PDS4 archive v2 (0.1° or 0.05° grids, ~3 PM local time, 13 swaths per map) ([USGS Astrogeology](https://astrogeology.usgs.gov/search/map/mars_mro_marci_daily_global_weather_maps_pds4_archive)); MDAD labels. Public.
- **Off-the-shelf tech:** U-Net / SegFormer, xarray.
- **Hackathon angle:** **Strong candidate.** Labelled data, a clear task, and a clear user (landers, rovers, future crews). "Mars dust nowcast": segment storms in MARCI maps, track them over days, and push a "dust risk at Jezero/Gale/landing site X" alert. Good visuals.
- **Credibility:** peer-reviewed + official dataset.
- **Sources:** [MDAD Zenodo](https://zenodo.org/records/7480334); [USGS MARCI MDGM archive](https://astrogeology.usgs.gov/search/map/mars_mro_marci_daily_global_weather_maps_pds4_archive); [UAEU Mask R-CNN](https://research.uaeu.ac.ae/en/publications/detection-of-martian-dust-storms-using-mask-regional-convolutiona/); [EPSC2024-1334 presentation](https://presentations.copernicus.org/EPSC2024/EPSC2024-1334_presentation.pdf).

### 3.5 Mars Sample Return (MSR): cancelled in its existing form

- **What it is:** Plan to return Perseverance's sealed sample tubes to Earth.
- **Status:** The FY2026 CJS appropriations act (signed 23 Jan 2026) says "the agreement does not support the existing Mars Sample Return (MSR) program" and funds a new **Mars Future Missions** line ($110 M) to develop "common technological heritage" ([search summary of bill text](https://payloadspace.com/house-minibus-bill-would-kill-mars-sample-return/); [Planetary Society, 2026](https://www.planetary.org/articles/advocacy-success-fy2026-nasa-budget)). The Planetary Society says the minibus "formally closes the program office" ([Planetary Society](https://www.planetary.org/articles/advocacy-success-fy2026-nasa-budget)). Scientific American framed 2026 as the year MSR's fate is decided ([SciAm](https://scientificamerican.com/article/the-fate-of-nasas-mars-sample-return-program-may-be-decided-in-2026)).
- **Problems / pain points:** Perseverance has cached and depot-deposited tubes on the surface with no retrieval plan. FY2027 request would cut Perseverance's operating funds roughly in half ([Planetary Society FY27](https://www.planetary.org/articles/analyzing-the-fy-2027-nasa-budget-request)).
- **Data:** Perseverance PDS releases (Mastcam-Z, SHERLOC, PIXL, SuperCam), sample dossiers.
- **Hackathon angle:** "Sample dossier explorer": link each of the sample tubes to all instrument observations made at the sampling site and to the papers citing them. Useful whoever eventually retrieves them.
- **Credibility:** official (bill) via reputable press.
- **Sources:** [Space.com](https://space.com/space-exploration/mars-rovers/the-trump-administration-wants-to-cancel-nasas-mars-sample-return-mission-experts-say-thats-a-major-step-back); [SpacePolicyOnline](https://spacepolicyonline.com/?p=82756); [Payload](https://payloadspace.com/house-minibus-bill-would-kill-mars-sample-return/); [SciAm](https://scientificamerican.com/article/the-fate-of-nasas-mars-sample-return-program-may-be-decided-in-2026).

### 3.6 Landing-site selection and descent navigation failures (Moon and Mars)

- **What it is:** Choosing safe, scientifically valuable landing sites and navigating to them autonomously.
- **Problems / pain points (recent failures share a sensing/navigation root cause):**
  - **Intuitive Machines IM-2 "Athena"** (landed 6 Mar 2025, tipped over, mission over in <1 day): altimeters suffered "signal noise and distortion"; south-polar "long shadows and dim lighting conditions… challenged the precision capability of our landing system" (CEO Altemus); optical navigation relied on LRO images taken from ~100 km that did not represent low-altitude views under polar lighting ([SpacePolicyOnline](https://spacepolicyonline.com/news/im-2-mission-ends-one-day-after-lunar-landing/); [The Space Bucket](https://thespacebucket.com/the-athena-lunar-lander-couldnt-measure-its-distance-from-the-surface/); [spacecenter.gov.ua](https://spacecenter.gov.ua/novyny/stala-vidoma-prichina-chomu-privatnij-misyachnij-aparat-athena-perekinuvsya-pislya-posadki.html?lang=en)).
  - **ispace Resilience** (crashed 6 Jun 2025): "The laser rangefinder… experienced delays in obtaining valid measurement values. As a result, the lander was unable to decelerate sufficiently" ([Universe Today](https://www.universetoday.com/articles/hakuto-r-mission-2s-crash-was-caused-by-its-laser-range-finder); [Spaceflight Now, 6 Jun 2025](https://spaceflightnow.com/2025/06/06/ispaces-resilience-lander-crash-lands-on-the-moon/)).
  - **Ingenuity** (flight 72, 18 Jan 2024): ~20 s after takeoff the navigation system couldn't find enough surface features to track over "steep, relatively featureless sand ripples", leading to a hard, sideways touchdown and four broken blades. Lead investigator Håvard Grip: "Lack of surface texture gave the navigation system too little information to work with." Future Mars aircraft need navigation that works over low-texture terrain ([NASA JPL, 11 Dec 2024](https://www.jpl.nasa.gov/news/nasa-performs-first-aircraft-accident-investigation-on-another-world/); [Wikipedia, Ingenuity](https://en.wikipedia.org/wiki/Ingenuity_(helicopter))).
  - **Firefly Blue Ghost M1** (Mar 2025) remains the only fully successful CLPS landing; in Sep 2026 NASA expected Astrobotic's Griffin-1 to be the only CLPS launch in 2026 (Nov 2026, Falcon Heavy), with IM-3 and Blue Moon Pathfinder slipping to 2027 ([Wikipedia, Griffin Mission One](https://en.wikipedia.org/wiki/Griffin_Mission_One)).
- **How they're trying to solve it:** Terrain-relative navigation, hazard-detection lidar, better reference maps (ShadowCam, LRO NAC DTMs), pre-flight simulation with realistic polar lighting (*general engineering practice, not individually sourced*).
- **Data:** LRO NAC/WAC, LOLA DEMs (5 m/px south pole), ShadowCam (PSR imagery), Kaguya, Chandrayaan-2 OHRC; Mars HiRISE DTMs.
- **Off-the-shelf tech:** Blender/Unreal renders of DEMs under arbitrary sun angles, feature matchers (SuperPoint/LightGlue, LoFTR), crater-based TRN.
- **Hackathon angle:** **Strong candidate.** "Will my nav camera see anything?": for any candidate south-pole landing site and arrival date/time, render the terrain from LOLA DEMs at the actual sun angle for descent altitudes and score how many trackable features a camera would see. That is exactly the failure mode of IM-2 and Ingenuity. Output: a site × time "navigability" map for Artemis/Moon Base candidate sites.
- **Credibility:** official + reputable press.
- **Sources:** as linked; [Wikipedia IM-3](https://en.wikipedia.org/wiki/IM-3).

### 3.7 Artemis II, Artemis III and NASA's "Moon Base" pivot (context)

- **Artemis II:** crewed lunar flyby (Wiseman, Glover, Koch, Hansen), ~10 days, splashdown off San Diego **10 Apr 2026**; Administrator Isaacman called it "a perfect mission" ([Times of San Diego, 10 Apr 2026](https://timesofsandiego.com/tech/2026/04/10/historic-return-moon-culminates-dramatic-splashdown-san-diego/); [Legal Insurrection](https://legalinsurrection.com/2026/04/artemis-ii-concludes-successful-mission-with-splashdown-off-san-diegos-coast/)). PDS posted an **Artemis II Mission Data Release** on 7 Oct 2026 (Geosciences node) ([PDS home](https://pds.nasa.gov/)).
- **Artemis III:** restructured (Feb 2026) into a **low-Earth-orbit test** of one or both landers, rendezvous with Orion and suits; first crewed landing moved to **Artemis IV, NET 2028** ([CRS IF11643, 25 Jun 2026](https://www.everycrsreport.com/files/2026-06-25_IF11643_f42f123e3663b5d6aef757a78d6406c1af3dc8be.html); [CSIS](https://www.csis.org/analysis/what-comes-next-artemis)). Artemis III date "TBD" ([SpacePolicyOnline](https://spacepolicyonline.com/?p=88965)). OIG concluded Axiom's suit may not be ready until 2031 (via CRS summary).
- **Moon Base:** May 2026 plan for a permanent south-pole presence (reported $20–30 B, 2036 target). **Gateway** was paused "as designed" in **March 2026** in favour of a 2029–2036 surface base. Its PPE is to be repurposed for "Space Reactor-1 Freedom" (nuclear electric propulsion); OIG reported ~$1.9 B spent on HALO, whose primary-structure corrosion could have pushed delivery to 2031 ([Wikipedia, Lunar Gateway](https://en.wikipedia.org/wiki/Lunar_Gateway)). Early missions: Moon Base I (Blue Moon Mk1 near Shackleton Connecting Ridge), Moon Base II (Astrobotic Griffin with Astrolab FLIP rover), Moon Base III (IM Nova-C "Trinity" with Lunar Vertex); LTV awards to Astrolab ($219 M) and Lunar Outpost ($220 M) ([Scientific American](https://www.scientificamerican.com/article/nasa-unveils-new-ambitious-moon-base-plans/); [SciAm on rovers/landers](https://www.scientificamerican.com/article/nasas-jared-isaacman-unveiled-the-first-moon-base-rovers-and-landers/); [IANS, 27 May 2026](https://ianslive.in/moon-base-push-marks-nasas-new-lunar-era--20260527075403)). New Glenn exploded on the pad on 28 May 2026, putting Moon Base I in doubt (via Wikipedia Griffin article, above).
- **Why it matters for the hackathon:** The south pole is now *the* US destination. Site selection, PSR resources, navigation and boulder hazards are first-order problems with large public datasets.
- **Credibility:** official (CRS) + reputable press.

### 3.8 Lunar south-pole water ice and permanently shadowed regions (PSRs)

- **What it is:** Whether PSRs hold usable ice. This drives Moon Base siting.
- **Problems / pain points:**
  - **ShadowCam** (NASA camera on Korea's KPLO) found "no evidence of widespread water ice in PSRs at abundances above the detection limit of 20 to 30 wt %"; a few small high-reflectance, forward-scattering spots could be >10 wt % ice, often near young craters, so more may be buried ([Li et al., Science Advances, 18 Mar 2026, via U. Hawaiʻi](https://www.soest.hawaii.edu/soestwp/announce/news/scarce-ice-in-moons-darkest-regions/); [EarthSky](https://earthsky.org/space/ice-in-moons-shadows-shadowcam-moon/); [Scientific American](https://www.scientificamerican.com/article/there-might-be-less-water-on-the-moon-than-wed-hoped/)). An earlier U. Hawaiʻi study said less than 20% of dark craters hold ice ([Business Today, Apr 2025](https://www.businesstoday.in/amp/science/story/university-of-hawaii-study-finds-less-than-20-of-moons-dark-craters-hold-ice-clouding-hopes-for-lunar-water-473770-2025-04-27)).
  - Stereo observations needed for the forward-scattering test were available at only six locations; more stereo expected through the extended mission to early 2028.
  - **Lunar Trailblazer** (water-mapping smallsat, launched with IM-2 on 26 Feb 2025) lost contact on 27 Feb 2025, probably because misaligned solar arrays drained its batteries. NASA ended the mission on 31 Jul 2025 ([NASA/JPL](https://www.jpl.nasa.gov/news/nasas-lunar-trailblazer-moon-mission-ends/)). That leaves a gap in high-resolution surface water mapping.
- **How they're trying to solve it:** ShadowCam extended mission; LRO (Diviner, LAMP, LOLA, Mini-RF); **VIPER**: cancelled Jul 2024, revived Sep 2025 as a CLPS delivery on Blue Origin's Blue Moon MK1 (New Glenn), landing planned 2027, contingent on MK1's first flight ([Wikipedia, VIPER](https://en.wikipedia.org/wiki/VIPER_(rover))); Chandrayaan-2 DFSAR.
- **Topography/illumination data ready to use:** NASA PGDA products: 5 m/px LOLA south-pole DEM mosaic 87–90°S (product 81), enhanced 5 m/px shape-from-shading topography of the 2022 Artemis III candidate regions (product 104), improved LOLA DEMs for south-pole landing sites with illumination error estimates (78), Lunar Polar Illumination (69) ([PGDA](https://pgda.gsfc.nasa.gov/); [product 81](https://pgda.gsfc.nasa.gov/products/81); [product 104](https://pgda.gsfc.nasa.gov/products/104)).
- **Data:** ShadowCam PDS releases are quarterly. The May 2026 release covered 5,250 observations (Apr–Jun 2025) = **6.65 TiB**, plus mosaics, DTMs and vector products ([ShadowCam PDS release, Jun 2026](https://shadowcam.im-ldi.com/news/1479); [Mar 2026](https://shadowcam.im-ldi.com/news/1472); [Dec 2025](https://shadowcam.im-ldi.com/news/1467)). LRO Diviner temperatures, LOLA albedo, LAMP Lyman-α, Mini-RF CPR. All open.
- **Off-the-shelf tech:** Multi-layer GIS fusion (rasterio, xarray), simple Bayesian or gradient-boosted "ice likelihood" models.
- **Hackathon angle:** **Strong candidate.** "South-pole resource prospector": fuse Diviner max temperature (cold-trap stability), LOLA albedo, LAMP, Mini-RF CPR and ShadowCam reflectance into one ice-likelihood map. Overlay the Moon Base candidate regions and LOLA-derived illumination and Earth visibility, then rank sites by "ice within X km + sunlight + comms + slope".
- **Credibility:** peer-reviewed + official.
- **Sources:** as linked; [ShadowCam PDS releases](https://shadowcam.im-ldi.com/news/1479).

### 3.9 Lunar boulders and rockfalls (hazard mapping)

- **What it is:** Boulders are landing hazards and rover obstacles, and they also record impacts and quakes.
- **Data / existing work:**
  - **~94 million boulders** mapped by a CNN on **635,000 LRO NAC images** from 60°S to 60°N, with a near-global map for boulders >4.5 m; CSVs on Zenodo (v3, 26 May 2025) ([Eos editor highlight](https://eos.org/editor-highlights/nearly-94-million-boulders-mapped-on-the-moon-using-deep-learning); [Zenodo 15520275](https://zenodo.org/records/15520275)).
  - Global rockfall catalog (Bickel et al. 2020, Nat. Commun.), with known duplicate entries in the 80°-capped catalogs; a 687-rockfall detailed catalog (2021); JPL RMaM-2020 training set of 2,822 lunar and martian rockfall labels ([b2find](https://b2find.eudat.eu/dataset/3ccf0070-f75d-50ab-91b9-4a2b8a7eb6bd); [687 rockfalls](https://b2find.eudat.eu/dataset/77bb52ef-ed58-5836-8bc2-4f62dd3f7be3)).
- **Problems / pain points:** The global boulder map stops at ±60°, but the Moon Base sites are at the south pole, where lighting makes detection hard.
- **Hackathon angle:** Extend boulder detection poleward using ShadowCam/NAC polar mosaics and produce a "boulder hazard density" layer for Moon Base candidate sites.
- **Credibility:** peer-reviewed + open datasets.
- **Sources:** as linked.

### 3.10 Lunar navigation and communications (LunaNet)

- **What it is:** NASA/ESA/JAXA framework for a "lunar internet" with delay-tolerant store-and-forward and navigation services (orbit determination, surface navigation). LunaNet Interoperability Specification v5 published Feb 2025. Implementations: NASA LCRNS, JAXA LNSS; ESA Moonlight adopts LunaNet ([Wikipedia, LunaNet](https://en.wikipedia.org/wiki/LunaNet)).
- **Problems / pain points:** No dedicated GNSS at the Moon; south-pole sites have limited Earth visibility; landers repeatedly failed on altimetry/navigation (3.6).
- **Evidence it can work:** Firefly Blue Ghost M1 (landed 2 Mar 2025, Mare Crisium; ~14 days of operations; >110 GB returned) carried **LuGRE**, which received and used GPS and Galileo signals at lunar distance and on the surface ([Wikipedia, Blue Ghost Mission 1](https://en.wikipedia.org/wiki/Blue_Ghost_Mission_1)).
- **Data:** LOLA DEM-based Earth visibility and illumination maps; LNIS documents.
- **Hackathon angle:** Earth-visibility + relay-coverage calculator for south-pole sites (combine with 3.8).
- **Credibility:** Wikipedia (secondary).
- **Sources:** [Wikipedia LunaNet](https://en.wikipedia.org/wiki/LunaNet).

### 3.11 Planetary defense: 2024 YR4, NEO Surveyor, Hera, and Rubin's asteroid flood at the MPC

- **2024 YR4:** Earth-impact odds peaked at 3.1% on 18 Feb 2025 and then fell to ~0.004%. Lunar-impact odds for 22 Dec 2032 were as high as 4.3%. **JWST observations on 18 and 26 Feb 2026** (faintest NEO detection ever, V≈30.5) ruled out a lunar impact: predicted passage 22,900 ± 800 km from the Moon's centre, uncertainty reduced >30×; no Earth impact in the next 100 years; diameter 60 ± 7 m ([AAS Nova, 20 May 2026](https://aasnova.org/2026/05/20/asteroid-2024-yr4-wont-hit-the-moon-new-jwst-observations-show/); [NAU Experts (de Wit et al.)](https://experts.nau.edu/en/publications/jwst-observations-of-asteroid-2024-yr4-rule-out-a-2032-lunar-impa); [ScienceAlert](https://www.sciencealert.com/its-official-nasa-confirms-asteroid-2024-yr4-will-fly-past-the-moon)).
- **NEO Surveyor:** in integration and test; launch NET Sep 2027 on Falcon 9 to Sun-Earth L1; goal of finding 90% of NEOs ≥140 m ([NASA/JPL, 5 May 2026](https://www.jpl.nasa.gov/news/nasas-next-gen-near-earth-asteroid-space-telescope-takes-shape/)). Protected in the FY2027 request ([Planetary Society](https://www.planetary.org/articles/analyzing-the-fy-2027-nasa-budget-request)).
- **Hera (ESA):** arrival at Didymos–Dimorphos **November 2026** (a month early); CubeSats Milani and Juventas deploy ~6 weeks later ([ESA](https://www.esa.int/Space_Safety/Hera/ESA_s_Hera_targets_early_arrival_at_Didymos_asteroids); [EPSC 2026 session](https://meetingorganizer.copernicus.org/EPSC2026/session/59571)).
- **Rubin → MPC load:** Rubin's first big submission: ~1 M observations over ~6 weeks, >11,000 new asteroids, >80,000 known (some "lost"), 33 new NEOs, ~380 TNOs ([NOIRLab via GeekWire, Apr 2026](https://www.geekwire.com/2026/rubin-observatory-11000-new-asteroids/); [EarthSky](https://earthsky.org/space/11000-new-asteroids-rubin-obervatory-380-tnos/)). On 2 Feb 2026 Rubin submitted 698,926 observations of 64,346 known objects; on 9 Feb, 246,754 observations of 19,630 candidate discoveries ([Rubin Community forum, Feb 2026](https://community.lsst.org/t/rubin-solar-system-february-2026-updates/11640)). MPC newsletter (28 Feb 2026): the batch was "a valuable end-to-end stress test of our pipeline" that exposed bottlenecks. The standard identification pipeline "would take too long" for this volume, so the MPC built a dedicated pipeline for pre-linked Rubin data; Rubin submissions still get extra manual vetting; several hundred tracklets may match known objects; an X05 code bug and a Daily Orbit Update bug were fixed ([MPC newsletter, Feb 2026](https://buttondown.com/MPC_newsletter/archive/newsletter-february-2026/)). Reported claim that the MPC needs more processing staff is *unverified* ([wwwhatsnew, Apr 2026](https://wwwhatsnew.com/2026/04/09/rubin-observatory-11000-asteroides-nuevos-2026-noirlab/)). Rubin full survey may find ~90,000 new NEOs ([Free Astronomy Magazine, Jul–Aug 2026](https://www.astropublishing.com/4FAM2026/48/)).
- **Problems / pain points:** Linking tracklets across nights at scale; false associations; manual vetting; the human bottleneck at the MPC; small NEOs' risk often unresolvable without space telescopes (JWST was needed for YR4).
- **Data:** MPC observations and orbits (MPCORB, public), JPL Small-Body Database and Sentry/Scout APIs, NEOCC (ESA), Rubin solar-system products (SSSource/DiaSource).
- **Off-the-shelf tech:** HelioLinC3D, THOR, `find_orb`, `sbpy`, `astroquery.jplhorizons`.
- **Hackathon angle:** "Impact-risk explainer": pull a newly discovered object from Scout/Sentry and show, in plain language and 3-D, why the risk is what it is and which future observation (where, when, how faint) would shrink it most. That is the YR4 story generalised: "who should observe next to retire the risk?"
- **Credibility:** official + peer-reviewed.
- **Sources:** as linked.

### 3.12 Outer planets and Titan (brief)

- **Europa Clipper:** Mars flyby 1 Mar 2025; **Earth flyby 3 Dec 2026**; Jupiter orbit insertion ~Apr 2030; Ka-band downlink up to ~500 kbps in optimal conditions, with up to a year of transmission time between flybys ([Wikipedia](https://en.wikipedia.org/wiki/Europa_Clipper)).
- **Dragonfly:** launch window 5–25 Jul 2028 on Falcon Heavy; arrival 2034; lifecycle cost revised to **$3.35 B** (Apr 2024); CDR passed Apr 2025; construction began 10 Mar 2026; fuselage delivered 29 Jun 2026. One-way light time 70–90 min forces autonomous landing and flight ([Wikipedia](https://en.wikipedia.org/wiki/Dragonfly_(Titan_space_probe))). Protected in FY2027 request ([Planetary Society](https://www.planetary.org/articles/analyzing-the-fy-2027-nasa-budget-request)).
- **JUICE (ESA):** Venus flyby 31 Aug 2025; lost contact for ~20 h on 16 Jul 2025 (tied to a scheduled onboard timer restart); second Earth flyby **28 Sep 2026**; third Jan 2029; Jupiter orbit insertion **Jul 2031**. Onboard storage 1.25 Tb; downlink up to ~2 Gb/day. Observing interstellar comet 3I/ATLAS produced 11.18 Gbit that took two 11-hour passes (17 and 20 Feb 2026) to downlink ([Wikipedia, JUICE](https://en.wikipedia.org/wiki/Jupiter_Icy_Moons_Explorer)).
- **Juno:** funded at $27.2 M in FY2026 after being proposed for termination ([Planetary Society](https://www.planetary.org/articles/advocacy-success-fy2026-nasa-budget)); extended to Sep 2028 with no deorbit planned; radiation-induced safe mode Apr 2025, JunoCam annealed ([Wikipedia, Juno](https://en.wikipedia.org/wiki/Juno_(spacecraft))).
- **New Horizons:** funded $10.0 M in FY2026; ~64 AU from Earth (Apr 2026); expected to exit the Kuiper Belt in 2028–29 ([Wikipedia](https://en.wikipedia.org/wiki/New_Horizons)).
- **Problems / pain points:** Low bandwidth means onboard data selection and compression matter; autonomy (Dragonfly hazard detection) matters too.
- **Hackathon angle:** "Onboard science triage": given a fixed downlink budget, choose which images or segments of a Cassini/Juno dataset to send first, ranked by novelty. Demonstrated on archival Cassini ISS images.
- **Credibility:** Wikipedia (secondary).

### 3.13 Interstellar comet 3I/ATLAS and the precovery problem

- **What it is:** Third known interstellar object, discovered by ATLAS (Río Hurtado, Chile) on **1 Jul 2025** at mag ~18 and announced by the MPC on 2 Jul. Perihelion 29 Oct 2025 at 1.36 AU ([Wikipedia, 3I/ATLAS](https://en.wikipedia.org/wiki/3I/ATLAS)).
- **Why it's relevant:** It was already in archival data. **TESS precovery images go back to 7 May 2025 (55 days before discovery)**; ZTF images 22 May–21 Jun; Weizmann 21 May; ATLAS from 5 Jun; Rubin imaged it during science validation 21 Jun–3 Jul and "would have found the comet before ATLAS had it started two weeks earlier". Observed by HST, JWST (Aug and Dec 2025), SPHEREx (water ice and CO₂), Swift, ExoMars TGO CaSSIS, and JUICE in Mar 2026. 782 of 7,886 observations used in the orbit solution (same source).
- **Problems / pain points:**
  - **Precovery is manual and slow:** finding earlier detections in archives requires predicting where the object was in each survey's footprint at each epoch and then searching images.
  - **Data access during shutdown:** MRO observed the comet but its data "was not released because NASA was shut down" (Oct 2025 government shutdown) (same source).
  - **Misinformation:** Avi Loeb et al. posted an arXiv paper (16 Jul 2025) suggesting it could be an alien spacecraft. Astronomers (Lintott, Manley, Kipping, Seligman, Lawler) rebutted it; Loeb later wrote it is most likely a natural comet (same source). Public confusion is a communication problem.
- **Data:** MPC observations; JPL Horizons ephemerides; ZTF/IRSA, TESS FFIs (MAST), Pan-STARRS, DECam (NOIRLab Astro Data Archive) image archives; SkyBoT / IMCCE and SSOIS (CADC Solar System Object Image Search) for "which images contain this object".
- **Off-the-shelf tech:** `astroquery` (JPL Horizons, MAST, IRSA), CADC SSOIS, `sbpy`, TESScut.
- **Hackathon angle:** **Strong candidate.** "Precovery engine": given any newly designated object (comet, NEO, interstellar visitor), compute its past positions, query TESS/ZTF/Pan-STARRS/DECam footprints, return the image cutouts where it should be visible, and run a simple detector on them. Demo: re-discover 3I/ATLAS in TESS data from May 2025. Clear story: "it was there 55 days earlier; we'd have found it on day 1."
- **Credibility:** Wikipedia (citing primary papers).
- **Sources:** [Wikipedia, 3I/ATLAS](https://en.wikipedia.org/wiki/3I/ATLAS); [Wikipedia, JUICE (3I/ATLAS downlink)](https://en.wikipedia.org/wiki/Jupiter_Icy_Moons_Explorer).

---

## Part 4. Heliophysics (science side only)

### 4.1 Parker Solar Probe, Solar Orbiter, PUNCH: multi-viewpoint data fusion

- **Parker Solar Probe:** record perihelion 24 Dec 2024 (~6.16 M km from the surface), with continuing perihelia every ~88 days (e.g. 11 Mar, 8 Jun, 4 Sep 2026); **extension approved in 2026 through 2029**. During each perihelion science phase (<0.25 AU) communication is largely cut off and data are downlinked later in the orbit, with gaps when the heat shield blocks the antenna or the Sun swamps the link ([Wikipedia](https://en.wikipedia.org/wiki/Parker_Solar_Probe)).
- **PUNCH:** four smallsats (one NFI + three WFIs) launched 11/12 Mar 2025 with SPHEREx; first images Apr 2025; background-subtracted polarimetric images at a **4-minute cadence**, distributed through NASA's SDAC and the Virtual Solar Observatory; ground merging of four spacecraft's images is "the mission's greatest technical challenge"; STEAM X-ray spectrometer off due to hardware anomalies ([Wikipedia](https://en.wikipedia.org/wiki/Polarimeter_to_Unify_the_Corona_and_Heliosphere); [NASA PUNCH](https://science.nasa.gov/mission/punch/)).
- **Solar Orbiter (ESA/NASA):** Feb 2025 Venus flyby raised inclination to 17°; first-ever images of the Sun's south pole (taken Mar 2025, released Jun 2025); Dec 2026 flyby raises it to 24° (33° in a proposed extension); nominal mission to end-2026, possible extension to 2030; coordinated campaigns with PSP and DKIST; most data stored onboard and downlinked in ~8-hour passes ([Wikipedia, Solar Orbiter](https://en.wikipedia.org/wiki/Solar_Orbiter)).
- **Problems / pain points:** Linking remote images of structures (CMEs, streamers, switchbacks) to the in-situ plasma measured later by a spacecraft at a different position (connectivity mapping). Data live in different archives and formats (CDF, FITS), with different time standards and coordinate frames.
- **How they're trying to solve it:** Magnetic-connectivity modelling tools, the heliophysics Python ecosystem (SunPy, sunkit-image, pySPEDAS) and HelioCloud (*background knowledge; tool names and status not re-verified in this pass*).
- **Data:** PSP (SPDF/CDAWeb), Solar Orbiter (SOAR), PUNCH (SDAC/VSO), SDO (JSOC), STEREO, SOHO. Open.
- **Off-the-shelf tech:** SunPy, pfsspy, HelioPy, pySPEDAS, astrospice.
- **Hackathon angle:** "Where did this solar wind come from?": for any time in the PSP or Solar Orbiter record, trace the plasma back (Parker spiral + PFSS) to its source region on an SDO image, and show the PUNCH view of the same stream. A visual "solar wind provenance" tool.
- **Credibility:** Wikipedia + official.
- **Sources:** as linked.

### 4.2 Heliophysics fleet budget risk

- FY2027 request would cancel **17 heliophysics missions** (most of any division) per the Planetary Society count ([Planetary Society, 23 Apr 2026](https://www.planetary.org/articles/analyzing-the-fy-2027-nasa-budget-request)). FY2026 enacted heliophysics at **$874.8 M** (+23%) ([Planetary Society FY26](https://www.planetary.org/articles/advocacy-success-fy2026-nasa-budget)). FY2026 request had proposed cancelling THEMIS-ARTEMIS, IBEX, MMS, TIMED, GOLD ([Friends of NASA, 1 Jun 2025](https://www.friendsofnasa.org/2025/06/19-active-science-missions-cancelled-in.html)).
- **Hackathon angle:** see 5.1 ("What we lose" mission-value cards).

---

## Part 5. Mission archives, "dark data" and the budget threat

### 5.0 How big are NASA's science archives? (SMD repository metrics, FY2024)

- **Numbers:** NASA's Science Data Portal publishes repository metrics (FY2024): **Astrophysics 15.7 PB** (46 "datasets", i.e. archive collections; ~8.8 M unique IPs/yr; +2.1 PB/yr; projected 70 PB by 2030); **Heliophysics 3.15 PB** (11,500 datasets; +0.47 PB/yr; 35 PB by 2030); **Planetary 3.86 PB** (27,460 datasets; +0.785 PB/yr; 24 PB by 2030); Earth Science 127.7 PB; BPS 0.24 PB. **Total 150.6 PB, 54,532 datasets, projected ~530 PB by 2030.** Annual on-prem downloads ~64 PB; cloud egress ~649 PB (mostly Earth science). "Users" are unique IPs and include bots ([NASA SMD Science Data Repository Metrics](https://science.data.nasa.gov/about/repository-metrics)).
- **Why it matters:** Planetary and heliophysics archives will grow ~6–10× by 2030 while staff and budgets shrink (5.1, 6.3).
- **Other entry points:** The Science Data Portal links the Science Discovery Engine (cross-SMD search of data, docs, code), Science Cloud, the AWS Open Data Registry, and SciX ([science.data.nasa.gov](https://science.data.nasa.gov/)). Sep 2026 highlights include HEASARC reprocessing of all past IXPE data and a new Zooniverse-style project, **Artifact InSPECtor**, asking volunteers to flag artifacts in Euclid spectra (Roman data from early 2027) ([Data & software highlights, Sep 2026](https://science.data.nasa.gov/features-events/data-software-highlights-september-2026)).
- **Credibility:** official.

### 5.1 NASA science budget: FY2026 fight and the FY2027 repeat

- **What happened:**
  - **FY2026 request (May 2025):** NASA −24%, Science −47% ($7.3 B → $3.9 B); "cancel 41 science projects — fully a third of NASA's science portfolio" ([Planetary Society press release](https://www.planetary.org/press-releases/the-planetary-society-reissues-urgent-call-to-reject-disastrous-budget-proposal-for-nasa); [SpaceNews](https://spacenews.com/nasa-budget-would-cancel-dozens-of-science-missions-lay-off-thousands/); [AAS, Jun 2025](https://aas.org/posts/news/2025/06/fy26-presidents-budget-request); [Astrobites, 2 Jun 2025](https://astrobites.org/2025/06/02/budget-cuts-threaten-astronomy/)). Active missions proposed for termination included Juno, MAVEN, New Horizons, Terra, Aqua, DSCOVR/EPIC, Chandra, Mars Odyssey, TIMED, Aura, THEMIS-ARTEMIS, Fermi, IBEX, OCO-2, MMS, OSIRIS-APEX, SAGE III, GOLD, OCO-3 ([Friends of NASA, 1 Jun 2025](https://www.friendsofnasa.org/2025/06/19-active-science-missions-cancelled-in.html)); plus DAVINCI, VERITAS, EnVision and MSR.
  - **FY2026 enacted (P.L. 119-74, signed 23 Jan 2026):** NASA $24.44 B; Science $7.25 B (−1%); Planetary $2,541.2 M, Astrophysics $1,595.0 M, Earth $2,153.0 M, Heliophysics $874.8 M. Named missions funded: New Horizons $10.0 M, Juno $27.2 M, Chandra $63.0 M, MAVEN $22.5 M, Odyssey $10.6 M, OSIRIS-APEX $20.0 M, MMS $20.0 M; MSR $0. "No less than" language guards against impoundment ([Planetary Society](https://www.planetary.org/articles/advocacy-success-fy2026-nasa-budget); [Astronomy.com](https://astronomy.com/science/congress-passes-nasa-budget-rejects-trump-cuts); [Space.com](https://space.com/space-exploration/in-rejection-of-trumps-deep-cuts-congress-passes-usd24-4-billion-budget-for-nasa); [CRS R43419, 27 Feb 2026](https://www.everycrsreport.com/files/2026-02-27_R43419_273405e895035be3ea37bc8934d2304aced578b2.html)).
  - **FY2027 request (3 Apr 2026):** NASA $18.8 B (−$5.6 B); Science $3.894 B (−46%). Planetary Society counts **53 missions** likely terminated (Planetary 10, Earth 16, Astrophysics 10, Heliophysics 17; $13.19 B lifecycle cost of operating assets), nearly half in extended operations. Mission lines "simply disappear" rather than being marked for termination ("a practice without precedent"). Named: OCO-2/3, Aura, AOS, DAVINCI, VERITAS, EnVision (US share), Mars Odyssey, partner contributions (Rosalind Franklin, Athena, LISA, Mars Express, XRISM, Solar-B, ULTRASAT, CODEX). Protected: Roman, Dragonfly, NEO Surveyor; Perseverance ops ~halved ([Planetary Society, 23 Apr 2026](https://www.planetary.org/articles/analyzing-the-fy-2027-nasa-budget-request); [R&D World](https://www.rdworldonline.com/senate-largely-hearing-splits-on-party-lines-over-5-6-billion-nasa-cut/); [Payload](https://payloadspace.com/white-house-requests-18-8b-fy27-budget-for-nasa); [MeriTalk](https://www.meritalk.com/articles/trumps-2027-budget-request-cuts-5-6b-from-nasa/); [UCS blog](https://blog.ucs.org/?p=97550)). The House CJS bill holds NASA's topline flat but **cuts the Science Mission Directorate by 17%** ([AGU The Bridge, 26 May 2026](https://thebridge.agu.org/2026/05/26/fy2027-appropriations-update-nasa-noaa-and-nsf/); [Save NASA Science hub](https://planetary.org/save-nasa-science)). Senate CJS leaders Moran and Van Hollen called $18.8 B inadequate ([SpacePolicyOnline](https://spacepolicyonline.com/news/key-senators-agree-nasa-fy2027-budget-request-inadequate/)). **Current status: NASA is running on a continuing resolution (P.L. 119-103, signed 2 Sep 2026) at the FY2026 level of $24.4 B through 11 Dec 2026.** The CR also blocks an OMB rule changing how federal grants are awarded ([SpacePolicyOnline, 3 Sep 2026](https://spacepolicyonline.com/news/house-clears-fy2027-cr-now-to-the-president/)). The fight resumes in December.
- **Problems / pain points:** "Terminating extended missions would permanently wipe out years of priceless data" ([Planetary Society FY27](https://www.planetary.org/articles/analyzing-the-fy-2027-nasa-budget-request)). Until Congress acts, the request "will be the baseline plan that NASA must adhere to" (same). Legislators and the public lack an easy way to see what each mission produces per dollar (papers, data users, unique capabilities).
- **Data:** NASA budget documents; ADS/SciX bibliographies per mission (papers using Chandra, Juno…); MAST/HEASARC/PDS download stats; Senior Review reports.
- **Hackathon angle:** **Strong candidate (policy-flavoured; very clear problem statement).** "What we lose": for each of the 53 threatened missions, auto-assemble cost per year, papers per year (ADS API), unique datasets, and "what no other mission can do", plus a one-page shareable card. Clear problem, clear solution, big public datasets.
- **Credibility:** official (CRS, bill) + advocacy (Planetary Society) + reputable press.

### 5.2 Planetary Data System (PDS) and PDS4 modernization

- **What it is:** NASA's planetary archive, with 6 discipline nodes (Atmospheres, Geosciences, Cartography & Imaging, PPI, Ring-Moon Systems, Small Bodies) and 2 support nodes (Engineering, NAIF/SPICE) ([Wikipedia](https://en.wikipedia.org/wiki/Planetary_Data_System)). Archive "nearly 1 petabyte" per the 2017–2026 roadmap (dated).
- **PDS4:** required for NASA-funded mission archives "since 2011" ([PDS data standards](https://pds.nasa.gov/datastandards/about/)); older missions remain in PDS3.
- **2026 status:** New beta portal at **pds.mcp.nasa.gov** (MCP = NASA Mission Cloud Platform: a cloud move); PDS Search API was flagged as "currently experiencing instability"; recent releases include **Artemis II data (7 Oct 2026)** and Odyssey Release 97 (1 Oct 2026) ([PDS home](https://pds.nasa.gov/)).
- **Problems / pain points:** Two formats (PDS3 labels vs PDS4 XML); data spread across nodes with different search UIs; discoverability depends on knowing instrument and product names; API instability.
- **How they're trying to solve it:** PDS4 Registry and Search API, cloud migration, the beta portal, SciX data linking (5.x / 7.x).
- **Data:** All PDS holdings (public domain).
- **Off-the-shelf tech:** `pds4_tools`, `planetarypy`, PDS Registry API, LLM label-to-text summarisation.
- **Hackathon angle:** "Ask the PDS": natural-language search over PDS4 labels ("all HiRISE images of Jezero after Feb 2021 with DTMs") that returns direct product links, built by embedding labels and calling the PDS Search API.
- **Credibility:** official.
- **Sources:** as linked.

### 5.3 Legacy data and data rescue (Lunar Orbiter, Apollo, Voyager, Viking)

- **Lunar Orbiter Image Recovery Project (LOIRP):** digitised ~1,500 analog tapes from five 1966–67 Lunar Orbiters using restored Ampex FR-900 drives and a hand-built demodulator; primary capture completed 20 Feb 2014; all images in PDS by Apr 2017 ([Wikipedia](https://en.wikipedia.org/wiki/Lunar_Orbiter_Image_Recovery_Project)). They are the highest-resolution orbital lunar images before LRO, which makes them useful for 50-year change detection.
- **Voyager:** RTG power declining. Instruments are being switched off to extend the mission; communications expected until ~2036 if nothing else fails; 2023–24 memory-chip anomaly recovered ([Wikipedia](https://en.wikipedia.org/wiki/Voyager_program)). NASA posts: "NASA Shuts Off Instrument on Voyager 1 to Keep Spacecraft Operating" (17 Apr 2026); engineers "successfully freed up power on Voyager 2" (4 Aug 2026); Voyager 1 revived backup thrusters before a command pause (14 May 2025). **Voyager 1 will be one light-day from Earth around 18 Nov 2026** (NASA countdown) ([NASA Voyager mission page](https://science.nasa.gov/mission/voyager/)). Which instrument was shut off is not stated on the summary page.
- **Apollo heat-flow data rescue:** The Apollo Heat Flow Experiment ran 1971–1977, but only data through Dec 1974 were archived. In 2011 researchers found ~10% of the missing open-reel tapes at the Washington National Records Center and reconstructed much of the rest from weekly JSC performance logs and contractor calibration memos. The recovered data showed the subsurface warming through 1977, which they attribute to astronauts disturbing the surface (Nagihara et al., JGR Planets) ([Eos, 25 Jun 2018](https://eos.org/articles/the-case-of-the-missing-lunar-heat-flow-data-is-finally-solved)). Apollo active-seismic data were archived only in 2009 (Brzostowski & Brzostowski, *The Leading Edge*, cited in [Wikipedia ALSEP](https://en.wikipedia.org/wiki/Apollo_Lunar_Surface_Experiments_Package)).
- **Viking:** The 1976 life-detection results keep being re-analysed decades later (2006, 2010–11 perchlorate reinterpretation, 2012 complexity analysis of Labeled Release data, 2018 GC-MS reanalysis suggesting organics may have been detected), and NASA hosts a public Viking Labeled Release data set ([Wikipedia, Viking biological experiments](https://en.wikipedia.org/wiki/Viking_lander_biological_experiments)). Old data stays scientifically live, which is the argument for rescue.
- **Problems / pain points:** Old formats, undocumented tapes, retired experts, and only "best effort" funding. The Goddard library closure (5.4) shows physical "dark data" is still at risk in 2026.
- **Hackathon angle:** "Then vs now": align Lunar Orbiter (1966–67) frames with LRO NAC images of the same spot and auto-detect new craters or boulder falls over ~50 years. A legendary-sounding headline built on real public data.
- **Credibility:** Wikipedia (secondary), official PDS.

### 5.4 Goddard closures, NASA library loss and physical "dark data"

- **What happened:** Goddard is closing **13 buildings** and ~**100 laboratories** by Mar 2026 as campus "consolidation"; the **Goddard library** (NASA's largest; the Goddard Information and Collaboration Center, formerly Homer E. Newell Memorial Library) paused services 9 Dec 2025 and closed **2 Jan 2026**. It held ~**100,000 volumes** including technical manuals, mission data, engineering documentation and historical research materials. NASA says the closures save $10 M/yr and avoid $63.8 M of deferred maintenance ([NPR, 6 Jan 2026](https://npr.org/2026/01/06/nx-s1-5667084/a-beloved-library-closes-at-nasas-goddard-space-flight-center); [Library Journal](https://www.libraryjournal.com/story/nasa-closes-goddard-campus-library); details via search summaries, NPR page timed out on fetch). NASA said holdings would be reviewed in 60 days, with some warehoused and the rest discarded ([NYT via Slashdot, 31 Dec 2025](https://tech.slashdot.org/story/25/12/31/2216247); [Gigazine, 5 Jan 2026](https://gigazine.net/gsc_news/en/20260105-nasa-gsfc-closure); [WTOP, Jan 2026](https://wtop.com/prince-georges-county/2026/01/nasa-says-historic-materials-will-be-preserved-as-goddard-research-library-shuts-down/)). A union source said "only about 10-15%" would be preserved directly by NASA. NASA went from **eleven libraries at the start of 2022 to three** (Glenn, Ames, JPL) ([Jalopnik](https://www.jalopnik.com/2066321/nasa-closing-biggest-library-lost-forever); [search summary](https://www.thebanner.com/politics-power/national-politics/nasa-goddard-trump-closure-W264DCJC4JA6JBXKPUDOG4KAXQ/)). Isaacman called it a "long-planned facilities consolidation"; IFPTE's Matt Biggs called his statements "patently false" and the shutdown "rapid and haphazard": "NASA's scientists and engineers shouldn't have to be dumpster divers to do their work" ([Astronomy.com, 9 Jan 2026](https://www.astronomy.com/science/union-leader-accuses-isaacman/)).
- **Problems / pain points:** Unique, non-digitised journals, reports and copyrighted materials not available digitally (union claim). No public inventory of what was discarded.
- **Hackathon angle:** "NTRS gap finder": compare what's cited in NASA technical reports with what exists digitally in NTRS/ADS and flag likely undigitised documents. Ambitious; framing is strong.
- **Credibility:** reputable press + union statements (partisan) + NASA statements (partisan).

---

## Part 6. Spacecraft operations and engineering knowledge

### 6.1 Telemetry anomaly detection benchmarks (ESA-ADB, NASA SMAP/MSL, OPS-SAT)

- **ESA Anomaly Detection Benchmark (ESA-ADB)** (Kotowski et al., arXiv:2406.17826, v2 Aug 2025): real telemetry from **three ESA missions** (two used in the benchmark), annotated by operations engineers and ML experts. The authors conclude that "new approaches are necessary to address operators' needs" ([arXiv](https://arxiv.org/abs/2406.17826)). Data: **11.6 GB** (Mission1 3.8 GB, Mission2 4.1 GB, Mission3 3.7 GB), **CC BY 3.0 IGO**, Zenodo (25 Jun 2024) ([Zenodo 12528696](https://zenodo.org/records/12528696)); code MIT ([GitHub kplabs-pl/ESA-ADB](https://github.com/kplabs-pl/ESA-ADB)). Caveat: all algorithms currently treat rare *nominal* events as anomalies (README).
- **NASA SMAP/MSL (Telemanom)** (Hundman et al., KDD 2018, arXiv:1802.04431): 82 channels (55 SMAP, 27 MSL), 105 anomaly sequences, values pre-scaled to (−1, 1), Apache-2.0 ([GitHub khundman/telemanom](https://github.com/khundman/telemanom)). It is widely used but small and anonymised.
- **OPS-SAT (OPSSAT-AD)** (Ruszczak et al., arXiv:2407.04730, Jun 2024): real CubeSat telemetry benchmark, 30 baseline ML methods, proposed standard metrics ([arXiv](https://arxiv.org/abs/2407.04730)).
- **ESOC framing:** ESA calls it "the first open, large-scale dataset of real satellite telemetry anomalies" (~31 GB from three missions; the Zenodo zips total 11.6 GB, presumably compressed), funded under ESA's Artificial Intelligence for Automation (A²I) roadmap. Gabriele De Canio (ESA) wants methods that "tackle challenges like learning infrequent nominal events and reducing false alarms" and says manual anomaly detection "is arduous and demands intense concentration". He sees it as "a catalyst for the creation of a future anomaly repository" ([ESOC news](https://esoc.esa.int/esa-releases-building-block-open-database-satellite-anomalies); [SpaceOps 2025 paper](https://publications.spaceops.org/2025/download_by_id.php?id=0152)).
- **Euclid ops:** thousands of housekeeping parameters; XGBoost forecasting of 11 temperature channels from 35 covariates plus SHAP explanations to find hidden states affecting science data quality ([Gómez et al., arXiv:2411.05596, IAC 2024](https://arxiv.org/abs/2411.05596)).
- **LLM + detector agents (2026):** **COMET** (Georgia Tech, SmallSat 2026, 23 Aug 2026): an LSTM-autoencoder detector plus a language model that explains each flagged window using the mission's own documents and procedures. Advisory and traceable; targets university/small teams with few staff; proof of concept on simulated telemetry ([USU Digital Commons](https://digitalcommons.usu.edu/smallsat/2026/all2026/179)). **SpaceHMchat**: conversational LLM with function calling for power-system health management in mega-constellations ([arXiv:2601.12667, Jan 2026](https://arxiv.org/pdf/2601.12667)). These are close prior art for the hackathon angle below. Differentiate with real ESA-ADB data, real NASA lessons, and evaluation.
- **Problems / pain points:** Operators drown in false alarms; benchmarks show standard time-series anomaly detection isn't good enough; labels are scarce; fleets are shrinking staff (6.3); small/university teams have even fewer people.
- **Off-the-shelf tech:** Telemanom (LSTM), TranAD, Anomaly Transformer, time-series foundation models (Chronos, TimesFM, Moirai), Merlion, PyOD.
- **Hackathon angle:** **Strong candidate.** "Flight-controller copilot": run a foundation-model anomaly detector on ESA-ADB, then have an LLM explain each alarm in operator language ("battery temp channel X diverged from its usual eclipse pattern; similar to anomaly #17 in 2009"), and retrieve similar past anomalies and lessons learned (6.2). Score on ESA-ADB's event-wise metrics.
- **Credibility:** peer-reviewed/preprint + open datasets.

### 6.2 NASA Lessons Learned Information System (LLIS): a knowledge base that people don't use

- **What it is:** NASA's online lessons-learned database since 1994 (public at llis.nasa.gov).
- **Problems / pain points (OIG IG-12-012, 6 Mar 2012):** "only 16 of the 28 (57 percent) project managers indicated that they used LLIS", and only 12 of 28 (43%) contributed. Managers called it "outdated, is not user friendly, and does not contain information relevant to their projects". Other than JPL, no centre consistently contributed in 2005–2010 (Glenn and JSC averaged ~1 lesson/year vs ~12/year at JPL). FY2011 funding was $782,000. LLIS "has been marginalized… and is of diminishing and questionable value" ([NASA OIG IG-12-012](https://www.oversight.gov/sites/default/files/oig-reports/IG-12-012.pdf); [SpacePolicyOnline](https://spacepolicyonline.com/news/nasa-ig-lessons-learned-system-rarely-used-marginalized/); [Nextgov, Mar 2012](https://www.nextgov.com/people/2012/03/nasa-knowledge-management-database-used-rarely/205923/)). 6 of 10 centres did not cross-reference lessons to their engineering standards.
- **How they're trying to solve it:** NASA Engineering Network (NEN), APPEL, knowledge-capture interviews; no recent public AI-search initiative found (*unverified*).
- **Data:** LLIS public lessons (scrapable web pages), NASA Technical Reports Server (NTRS), mishap investigation board reports (public subsets), GAO and OIG reports.
- **Off-the-shelf tech:** RAG (embeddings + reranker), LLM summarisation, knowledge graphs.
- **Hackathon angle:** **Strong candidate.** "Lessons-learned copilot": paste a design review slide or a requirement and get the 5 most relevant past lessons, mishaps and OIG findings with citations. It addresses a documented, decade-old failure (57% usage) made worse by the 2025 brain drain (6.3).
- **Credibility:** official (OIG).

### 6.3 Knowledge loss from NASA's 2025 workforce shrinkage

- **What happened:** Nearly **4,000** employees (~3,870) took the Deferred Resignation Program in 2025. With normal attrition (~500), headcount falls ~20%, from ~18,000 to ~14,000 ([KPBS/NPR, 26 Jul 2025](https://www.kpbs.org/news/national/2025/07/26/nearly-4-000-nasa-employees-opt-to-leave-agency-through-deferred-resignation-program); [WGBH](https://www.wgbh.org/news/national/2025-07-28/nearly-4-000-nasa-employees-opt-to-leave-agency-through-deferred-resignation-program); [Gulf News](https://gulfnews.com/world/americas/nasa-to-lose-nearly-4000-employees-in-mass-resignation-push-1.500211784)). Politico tally: **2,145 senior-grade staff**, >1,800 from core mission areas, Goddard hardest hit ([Columbia Sabin Center tracker](https://climate.law.columbia.edu/content/nasa-lose-2145-senior-staff)). A Caltech scientist warned of "deep knowledge and expertise holes across all NASA centres" ([WION](https://www.wionews.com/world/more-than-20-nasa-employees-to-quit-1753528086659)). The Planetary Society said the program was approved "seemingly without consideration of skills, agency needs, or expertise" and charts losses per centre ([Planetary Society chart](https://www.planetary.org/charts/2025-workforce-losses-at-every-nasa-center)). Proposed workforce would be the lowest since FY1960 ([Planetary Society FY26](https://www.planetary.org/articles/advocacy-success-fy2026-nasa-budget)). Open letter by >350 employees warned of safety risks ([SAN](https://san.com/?p=439558), *not independently verified*).
- **Problems / pain points:** Tacit knowledge about decades-old spacecraft (Voyager, Hubble, Chandra, Odyssey) sits with people near retirement, and the ADS team flags the same risk for software ("irreparable harm in terms of technical debt, team integrity, and retaining the know-how", [ADSUG 2025](https://ads.harvard.edu/adsug/2025/ADSUG-2025-Report.pdf)).
- **Hackathon angle:** "Mission memory": turn a spacecraft's public anomaly reports, ops papers, PDS documentation and mission blog posts into a searchable "ask the retired engineer" assistant. Pair it with 6.1/6.2.
- **Credibility:** reputable press + advocacy.

### 6.4 Failure investigations and mishap reports as a dataset

- **What it is:** Public root-cause narratives: Ingenuity (featureless terrain), IM-2 (altimeter noise, polar lighting), ispace Resilience (laser rangefinder latency), Lunar Trailblazer (solar arrays/power), MAVEN (unexpected rotation, root cause pending), Voyager 1 (memory chip) (sources in 3.1, 3.6, 3.8, 5.3).
- **Problems / pain points:** Reports are scattered across press releases, OIG, GAO, NTRS and company statements. No structured, searchable failure taxonomy exists for small/commercial missions (*claim based on absence in this research*). Failure modes repeat: three 2024–25 landing/flight failures were descent-sensing or navigation.
- **Data:** NASA NTRS, OIG/GAO reports, mission press releases, Wikipedia's lists of spacecraft failures, the Seradata/Gunter's Space Page launch logs (*access/licence vary*).
- **Hackathon angle:** "Space failure atlas": LLM-extract (mission, subsystem, phase, root cause, detection, fix) from public failure write-ups into a table, then show recurring patterns ("navigation sensor during terminal descent: 3 of the last 5 lunar landing failures").
- **Credibility:** mixed (official + press).

### 6.5 Requirements and document search

- **What it is:** Engineers need to find relevant standards, requirements, test reports and prior designs across NASA Technical Standards, NTRS, NPRs and mission docs.
- **Problems / pain points:** Same as LLIS: siloed repositories and keyword search; 6 of 10 centres didn't link lessons to standards (OIG 2012, above).
- **Off-the-shelf tech:** INDUS embedding models (7.3), hybrid BM25 + dense retrieval, requirement-similarity models.
- **Hackathon angle:** "Requirement linter": paste a requirement, get similar requirements from public NASA standards and the lessons that motivated them, and flag ambiguity ("shall be adequate").
- **Credibility:** inferred from OIG + standard practice.

---

## Part 7. "A literature no human can read all of"

### 7.1 Volume: astro-ph growth

- **Numbers (arXiv listing counts):** astro-ph had **12,900 articles + 2,050 cross-lists (14,950) in 2015** ([arXiv astro-ph 2015](https://arxiv.org/year/astro-ph/2015)), and **18,660 + 3,238 (21,898) in 2025** ([arXiv astro-ph 2025](https://arxiv.org/year/astro-ph/2025)). **2026 through mid-October: 17,011 + 2,742 = 19,753**, with record months of 2,339 (Jun) and 2,397 (Sep) ([arXiv astro-ph 2026](https://arxiv.org/year/astro-ph/2026)). That is ~60–70 new astro-ph papers every weekday. 2026 is on pace for ~24,000 (extrapolation).
- **NASA ADS:** "over 15 million records" across its collections ([Wikipedia, ADS](https://en.wikipedia.org/wiki/Astrophysics_Data_System)); ~5 million annual ADS users ([ADSUG 2025 report](https://ads.harvard.edu/adsug/2025/ADSUG-2025-Report.pdf)). SciX ingests ~100K Earth-science articles per week (same).
- **Problems / pain points:** Nobody can track even a sub-field; literature review is a bottleneck; early-career researchers "now routinely rely on alternative tools such as Google Scholar, Scholar Labs, and AI-based systems like ChatGPT" ([ADSUG 2025](https://ads.harvard.edu/adsug/2025/ADSUG-2025-Report.pdf)).
- **Credibility:** official.

### 7.2 NASA ADS → SciX (Science Explorer) transition

- **What it is:** SciX extends ADS to all NASA Science Mission Directorate disciplines (astro, helio, planetary, Earth, biological and physical sciences). Beta Dec 2023; **official launch 29 Sep 2025** ([ADS funding slides, ADSUG Nov 2025](https://ads.harvard.edu/adsug/2025/01-03-ADSUG2025-ADSFundingandCharge.pdf); [ADS blog: SciX launch](https://ui.adsabs.harvard.edu/blog/scix-launch)). ADS users to be moved to SciX's astrophysics instance in 2026 ([UCLA event, Feb 2026](https://community.ucla.edu/event/f428091a-6659-4861-9d3c-51736e33ad0d); [APS 2026 poster](https://meetings-archive.aps.org/smt/2026/mar-h00-02/41/)). Final ADS cut-over date not confirmed (*unverified*).
- **Problems / pain points (from the Nov 2025 ADSUG meeting):**
  - Funding: ADS funded by NASA Astrophysics at ~$4.5 M/yr; SciX by the Office of the Chief Science Data Officer at a reduced $3 M/yr (25% below the $4 M request); "2026 funding for SciX is not guaranteed"; FY25 funds last "through the end of March 2026". In an ADS-only scenario, staffing drops "to 12 FTEs from the current level of 20 FTEs" and AI/ML integration would be "severely limited" ([ADS funding slides](https://ads.harvard.edu/adsug/2025/01-03-ADSUG2025-ADSFundingandCharge.pdf)). ADSUG later noted "confirmed substantial funding for SciX in FY26" ([ADSUG 2025 report](https://ads.harvard.edu/adsug/2025/ADSUG-2025-Report.pdf)).
  - Adoption: "only about 13k active SciX users (compared to 5M annual ADS users)" (ADSUG report).
  - Scale: "there is no scenario under which traditional ingest and curation alone can scale up to enable an ingestion of SciX content twice the size of the current ADS system" (funding slides).
  - Curation roadmap (data links, NER of missions, taxonomies) runs 2025–2030 per discipline; heliophysics data links 2026; Earth science 2025–28 (funding slides).
- **How they're trying to solve it:** AI/ML subteam (keyword labelling via **KAILAS**); new feature linking papers to mentioned software and grants (NSF/NASA awards); data and software links even without DOIs ([ADSUG 2025 report](https://ads.harvard.edu/adsug/2025/ADSUG-2025-Report.pdf)).
- **Data:** ADS/SciX API (free token), full metadata, citations, data links (Datalinks), astronomy full text (restricted).
- **Hackathon angle:** Build on the SciX API: "mission → data → papers" graphs (7.8), or an "astro-ph morning brief" agent personalised from a user's ADS library.
- **Credibility:** official.

### 7.3 NASA INDUS models and the Science Discovery Engine

- **What it is:** INDUS (NASA + IBM, EMNLP 2024 Industry Track): encoder with domain vocabulary, contrastive text-embedding model for retrieval, and distilled small models, trained on curated corpora across Earth science, biology, physics, heliophysics, planetary science and astrophysics. New benchmarks: CLIMATE-CHANGE NER, NASA-QA, NASA-IR. Outperforms RoBERTa and SciBERT; used for large-scale vector search and auto-tagging ([arXiv:2405.10725](https://arxiv.org/abs/2405.10725)). The **Science Discovery Engine** (sciencediscoveryengine.nasa.gov now redirects to science.data.nasa.gov/science-discovery-engine) is described as "an integrated search platform to help you find what you need across NASA's vast stores of open science data", including documentation, code and tools ([NASA Science Data Portal](https://science.data.nasa.gov/)). Index size and AI features were not shown.
- **Off-the-shelf tech:** INDUS models on Hugging Face under **nasa-impact**: `indus-sde-st-v0.2` (sentence similarity), `indus-sde-v0.2` (fill-mask), `nasa-ibm-st.38m`, `modernbert-sde-v0.2`, plus classifiers (`science-keyword-classification`, `division-classifier`) and benchmarks (`nasa-smd-IR-benchmark`, `nasa-smd-qa-benchmark`, `nasa-sde-IR-benchmark-20251024-v5`, `nasa-science-code-benchmark`) ([Hugging Face nasa-impact](https://huggingface.co/nasa-impact)). Licences per model card not checked.
- **Hackathon angle:** Use INDUS-retriever embeddings as the backbone of any NASA-document RAG (6.2, 6.5, 5.2).
- **Credibility:** peer-reviewed (EMNLP Industry).

### 7.4 Astronomy-specific LLMs and benchmarks (AstroLLaMA, AstroSage, AstroMLab)

- **AstroLLaMA** (Sep 2023): 7B LLaMA-2 fine-tuned on >300,000 arXiv astronomy abstracts; Hugging Face `universeTBD/astrollama` ([arXiv:2309.06126](https://arxiv.org/abs/2309.06126)).
- **AstroMLab 1** (Jul 2024, Astronomy & Computing): first astronomy LLM benchmark, **4,425 MCQs from Annual Review of Astronomy & Astrophysics**. Claude-3.5-Sonnet 85.0% (top), LLaMA-3-70B 80.6%, Qwen-2-72B 77.7%. Cost to reach a given score falls every 3–12 months; top models well calibrated (>0.9 correlation) ([arXiv:2407.11194](https://arxiv.org/abs/2407.11194)).
- **AstroSage-Llama-3.1-8B (AstroMLab 3)** (Sci Rep 15, 13751, 2025): 80.9% on AstroMLab-1, "on par with GPT-4o", trained on all astro arXiv papers 2007–2024 plus millions of synthetic Q&A pairs; freely available ([arXiv:2411.09012](https://arxiv.org/abs/2411.09012)).
- **Problems / pain points:** MCQ benchmarks don't test research-grade reasoning or citing correctly; hallucinated references.
- **Hackathon angle:** Use a small open astro model locally for cheap bulk tagging of thousands of abstracts; compare against a frontier model.
- **Credibility:** peer-reviewed.

### 7.5 pathfinder (UniverseTBD)

- **What it is:** Semantic literature search + LLM synthesis over ~**350,000** peer-reviewed ADS astronomy papers, with time- and citation-based weighting; visualises research landscapes and tracks the impact of observatories and methods; online at pfdr.app ([Iyer et al., arXiv:2408.01556, Aug 2024](https://arxiv.org/abs/2408.01556)).
- **Hackathon angle:** pathfinder shows demand. A hackathon could add *data*: "papers + the exact observations they used".
- **Credibility:** preprint.

### 7.6 General AI research assistants for science

- **PaperQA2 (FutureHouse):** "matches or exceeds subject matter expert performance" on three literature tasks; writes cited summaries more accurate than Wikipedia; finds **2.34 ± 1.99 contradictions per paper** in biology papers, 70% validated by experts ([Skarlinski et al., arXiv:2409.13740, Sep 2024](https://arxiv.org/abs/2409.13740)).
- **Google AI co-scientist:** Gemini multi-agent "generate, debate, evolve" hypothesis system; validated in biomedicine (AML drug repurposing in vitro, target discovery, AMR mechanisms); v2 Jun 2026 with a Nature (2026) publication ([arXiv:2502.18864](https://arxiv.org/abs/2502.18864)).
- **PaperQA2 code:** `paper-qa` on GitHub, **Apache-2.0**, calendar versioning since Dec 2025, works with any LiteLLM model (Claude, Gemini, local) over local PDFs and other files; notes that 7B local models perform poorly ([GitHub Future-House/paper-qa](https://github.com/Future-House/paper-qa)).
- **Astro-native research agents:** **cmbagent**: ~30 LLM agents in a planning-and-control loop that retrieve from papers and codebases, write and run code, and critique, applied to measuring cosmological parameters from supernova data ([Xu et al., arXiv:2507.07257, Jul 2025](https://arxiv.org/abs/2507.07257)). **Denario**: multi-agent research assistant (ideas → literature check → plan → code → plots → paper draft → review) using cmbagent as backend; demos across astrophysics and planetary science; code on GitHub (AstroPilot-AI/Denario), HF Spaces demo ([Villaescusa-Navarro et al., arXiv:2510.26887, Oct 2025](https://arxiv.org/abs/2510.26887)).
- **AstroMLab 2 warning:** earlier AstroLLaMA (7B) models *underperformed their base model*; small models suffered catastrophic forgetting, while continual pretraining helped at 70B ([arXiv:2409.19750, Sep 2024](https://arxiv.org/abs/2409.19750)). Domain fine-tuning is not automatically better.
- **OpenAI science efforts, FutureHouse hosted platform:** *not verified in this pass*.
- **Problems / pain points:** These tools are biology-centric; astronomy needs data-aware agents (query archives, run code), not just text synthesis.
- **Hackathon angle:** "Contradiction finder for astronomy": run a PaperQA-style agent over all papers on one hot topic (e.g. the Hubble tension, DESI evolving dark energy, little red dots in JWST) and map which papers disagree and why.
- **Credibility:** preprint/peer-reviewed.

### 7.7 Telescope proposal review overload and distributed peer review (ESO, ALMA)

- **What it is:** Proposal numbers are rising (JWST Cycle 5: 2,930 proposals, a record; see 1.9) and the reviewer pool can't keep up.
- **How they're trying to solve it:**
  - **ESO Distributed Peer Review (DPR)**, introduced in **P110**: each PI reviews **10 proposals per proposal submitted**; each proposal gets 10 reviewers matched by 2–5 scientific keywords, with some non-experts included and overlap minimised; failure to review causes automatic rejection. ESO is "actively exploring" ML for matching scores ([ESO DPR page](https://www.eso.org/sci/observing/phase1/distributed-peer-review.html)).
  - **DPR experiment** (Kerzendorf et al., Nature Astronomy 2020): DPR results were statistically similar to a panel; the ML algorithm predicted reviewer expertise "with a high success rate" ([arXiv:2004.04165](https://arxiv.org/abs/2004.04165)).
  - ALMA also uses DPR (per ESO page).
- **Problems / pain points:** Reviewer-proposal matching by keyword is crude; conflicts of interest; consistency.
- **Hackathon angle:** "Reviewer matcher": embed proposal abstracts and reviewers' ADS publication records, assign 10 reviewers per proposal with conflict-of-interest detection (co-authorship graph) and diversity constraints, and compare with keyword matching. Uses public JWST/HST accepted abstracts as stand-ins.
- **Credibility:** official + peer-reviewed.

### 7.8 "Who has already observed this target?" Duplicate observations and paper↔data linking

- **What it is:** Before proposing, astronomers must check archives (MAST, ESO, HEASARC, IRSA, CADC) for existing data. JWST and HST have formal duplication rules. And when reading a paper, it's often hard to find the exact data it used.
- **Problems / pain points:**
  - Archives are siloed by mission; checking duplication across JWST, HST, Chandra, XMM, ALMA, VLT and Keck means many separate tools (*JWST duplicate policy page returned 404 when fetched; policy exists per JWST docs, not re-verified*).
  - SciX's curation roadmap puts "Data Links" work across disciplines from 2025 to 2028, i.e. paper-data linking is still incomplete ([ADS funding slides](https://ads.harvard.edu/adsug/2025/01-03-ADSUG2025-ADSFundingandCharge.pdf)).
  - JWST archival oversubscription is 1 in 9.6 ([JW5 TAC results](https://stsci-docs.stsci.edu/policies/files/250513868/250513872/1/1778695182011/JW5-TAC-Results-Public.pdf)): there is strong demand to reuse data.
- **How they're trying to solve it:** IVOA standards (ObsCore/TAP) allow one query across many archives; ADS data links; MAST portal; ESASky.
- **Data:** IVOA ObsCore TAP services (MAST, ESO, CADC, HEASARC, IRSA, ESASky), all public; ADS API for papers.
- **Off-the-shelf tech:** `pyvo`, `astroquery` (MAST, ESO, HEASARC, Gaia), Simbad name resolver.
- **Hackathon angle:** **Strong candidate.** "Target dossier in one click": type an object name and get every observation of it across ~10 archives (instrument, wavelength, exposure, date, proprietary status) as a sky/wavelength/time coverage chart, plus the papers that used each dataset, and an LLM verdict: "your proposed NIRSpec IFU observation would duplicate program 1234". A real time-saver for every proposer, built only from public archives.
- **Credibility:** official (inferred practice).

### 7.9 Reproducibility and software citation

- **What it is:** Astronomy papers often depend on code and data that aren't linked or archived.
- **How they're trying to solve it:** ADS/SciX now "connects papers to mentioned software and grants" ([ADSUG 2025](https://ads.harvard.edu/adsug/2025/ADSUG-2025-Report.pdf)); the ASCL (Astrophysics Source Code Library, "making codes discoverable since 1999", indexed by ADS and Web of Science, with a citable ascl ID per code) ([ascl.net](https://ascl.net/)); Zenodo DOIs. ASCL's total code count wasn't shown on its home page.
- **Hackathon angle:** "Reproducibility score": for a paper, check whether its data (archive IDs), code (GitHub/ASCL) and figures are findable, and output a badge plus the missing links.
- **Credibility:** official.

---

## Problem bank

Format: problem → who has it → data that could address it → source.

1. Rubin's alert flood (800k on night one, up to ~7 M/night) is far beyond human review → time-domain astronomers, broker teams → Rubin + ZTF public alert streams via brokers → [Sky & Telescope](https://skyandtelescope.org/astronomy-news/rubin-observatory-sends-800000-alerts-to-astronomers-per-night/)
2. Seven brokers, seven taxonomies, APIs and filter languages; classifications disagree → scientists consuming alerts → ALeRCE/Fink/Lasair/ANTARES/Pitt-Google APIs → [Rubin alerts & brokers](https://rubinobservatory.org/for-scientists/data-products/alerts-and-brokers)
3. Spectroscopic follow-up bottleneck: ~10% of 2019 TNS transients classified; Rubin era <1% to a few % → SN/transient community, SALT, 4MOST/TiDES → TNS, ZTF BTS, WISeREP, broker light curves → [Kulkarni 2020](https://authors.library.caltech.edu/102525)
4. Deciding which transients get scarce spectra → Fink/RESSPECT, follow-up telescope schedulers → broker light curves + classifier probabilities → [arXiv:2502.19555](https://arxiv.org/pdf/2502.19555)
5. Finding genuinely new classes ("weird ones") in millions of light curves → broker anomaly teams → ZTF/Rubin light curves, ELAsTiCC → [arXiv:2503.09699](https://arxiv.org/pdf/2503.09699)
6. Satellite streaks make sources in Rubin visits undetectable → Rubin, survey astronomers → TLEs (CelesTrak) + Rubin pointing history → [Rubin LEO FAQ](https://rubinobservatory.org/es/for-scientists/frequently-asked-questions/leo-sats)
7. SKA's ~600–700 PB/yr of products can't be downloaded; compute must go to the data → radio astronomers, SRCNet → ASKAP/MeerKAT/LOFAR precursor surveys → [arXiv:2504.03103](https://arxiv.org/pdf/2504.03103)
8. Simulation-trained lens finders collapse on real data (50% completeness, 24% purity) → Euclid strong-lensing team → Euclid Q1 cutouts + Space Warps labels → [arXiv:2503.15326](https://arxiv.org/pdf/2503.15326)
9. Hundreds of thousands of lens candidates from 72 M DR1 galaxies need eyeballing → Space Warps volunteers → Euclid DR1 + Zoobot → [Zooniverse Space Warps Euclid](https://www.zooniverse.org/projects/aprajita/space-warps-esa-euclid/about/results)
10. Record JWST demand (2,930 Cycle 5 proposals; 1 in 12.5 by hours) overloads reviewers → STScI, TAC members → accepted-program abstracts, MAST holdings → [STScI](https://www.stsci.edu/contents/newsletters/2026-volume-43-issue-01/jwst-cycle-5-proposal-selection)
11. Tens of millions of DESI spectra are never looked at individually → DESI, galaxy/stellar astronomers → DESI DR1 (18.5 M spectra) → [DESI papers](https://data.desi.lbl.gov/doc/papers/)
12. ZTF funding beyond 2026 unclear; risk of a northern time-domain gap → time-domain community → ZTF DR24 / alert archive → [ZTF news](https://www.ztf.caltech.edu/new/nsf-funds-ztf-to-work-with-vera-rubin.html)
13. Gravitational-wave sky maps are huge; where should small telescopes point? → EM follow-up teams → GraceDB/GCN sky maps + GLADE+ galaxy catalog → [LIGO O4 wrap-up](https://ligo.org/ligo-virgo-kagra-collaboration-successfully-wraps-up-its-fourth-observing-run/)
14. Proposed closure of one LIGO site / ops cut $48 M → $29 M → LVK → n/a (policy) → [Sky & Telescope](https://skyandtelescope.org/astronomy-news/shattering-nsf-budget-proposal-threatens-gravitational-wave-science/)
15. "Humans don't scale": volunteers can't keep up with surveys → Zooniverse projects → Galaxy Zoo/Space Warps/Gravity Spy labels → [Galaxy Zoo blog](https://blog.galaxyzoo.org/tag/galaxy-zoo)
16. TESS backlog: 8,151 TOIs vs 1,012 confirmed planets → TFOP observers, exoplanet community → ExoFOP TOI table, MAST light curves → [ExoFOP](https://exofop.ipac.caltech.edu/tess/), [Exoplanet Archive](https://exoplanetarchive.ipac.caltech.edu/docs/counts_detail.html)
17. ML vetting scores disagree with human TOI dispositions → TESS vetting teams → ExoMiner++ catalog vs ExoFOP → [arXiv:2502.09790](https://arxiv.org/abs/2502.09790)
18. Sparse transits leave periods ambiguous → TFOP schedulers → TESS light curves + ephemeris tools → [arXiv:2111.01311](https://export.arxiv.org/abs/2111.01311)
19. HWO precursor-science gaps on target stars, with FY27 request cutting HWO to $5 M → HWO/ExEP → TSS25 list + Gaia + TESS + RV archives → [TSS25](https://www.ipac.caltech.edu/publication/2025PASP..137j4402T), [Wikipedia HWO](https://en.wikipedia.org/wiki/Habitable_Worlds_Observatory)
20. Mars relay capacity shrinking (MAVEN lost Dec 2025, Odyssey near end of fuel, Mars Express elliptical) → Curiosity/Perseverance ops, JPL → NAIF SPICE ephemerides → [SciAm](https://scientificamerican.com/article/nasas-mars-mission-maven-is-lost-forever), [Hackaday](https://hackaday.com/2026/09/24/after-decades-nasa-may-finally-replace-mars-relays/)
21. Replacement relay (MTN, $700 M) frozen by Rocket Lab's GAO protest of Blue Origin award; 26-month launch windows → NASA Mars program → n/a → [Hackaday](https://hackaday.com/2026/09/24/after-decades-nasa-may-finally-replace-mars-relays/)
22. Millions of HiRISE/CTX images with no semantic search → Mars scientists, landing-site teams → PDS Imaging Node HiRISE/CTX → [Universe Today](https://www.universetoday.com/articles/how-much-science-data-has-the-mars-reconnaissance-orbiter-sent-to-earth)
23. Manual crater counting is slow and inconsistent → planetary geologists, surface-dating studies → CTX/LRO mosaics, DEMs, Robbins catalogs → [arXiv:2508.03920](https://arxiv.org/html/2508.03920v1)
24. Dust storm identification is mostly manual; MARCI maps have gaps → Mars weather/ops, future landers → MARCI MDGMs + MDAD masks → [Zenodo MDAD](https://zenodo.org/records/7480334)
25. MSR cancelled in existing form; cached samples stranded; Perseverance ops ~halved in FY27 request → Mars science community → Perseverance PDS sample-site data → [Planetary Society](https://www.planetary.org/articles/advocacy-success-fy2026-nasa-budget)
26. Terminal-descent sensing/navigation failures (IM-2 altimeter noise + polar lighting; ispace LRF latency; Ingenuity featureless terrain) → CLPS providers, NASA → LOLA DEMs, LRO NAC, ShadowCam, HiRISE DTMs → [SpacePolicyOnline](https://spacepolicyonline.com/news/im-2-mission-ends-one-day-after-lunar-landing/), [Universe Today](https://www.universetoday.com/articles/hakuto-r-mission-2s-crash-was-caused-by-its-laser-range-finder)
27. Choosing Moon Base sites that combine ice, sunlight, Earth visibility and safe slopes → NASA Moon Base, CLPS, LTV teams → PGDA south-pole DEMs/illumination, Diviner, ShadowCam → [SciAm](https://www.scientificamerican.com/article/nasa-unveils-new-ambitious-moon-base-plans/), [PGDA](https://pgda.gsfc.nasa.gov/)
28. PSR ice is scarcer than hoped (no widespread >20–30 wt% surface ice) → ISRU planners → ShadowCam PDS (6.65 TiB per quarterly release) + LRO → [U. Hawaiʻi](https://www.soest.hawaii.edu/soestwp/announce/news/scarce-ice-in-moons-darkest-regions/)
29. Lunar Trailblazer's loss left a gap in high-resolution water mapping → lunar science → existing M3, LAMP, Diviner data → [NASA JPL](https://www.jpl.nasa.gov/news/nasas-lunar-trailblazer-moon-mission-ends/)
30. Global boulder hazard map stops at ±60°, not covering the south pole → landers, rovers → NAC/ShadowCam polar images; 94 M-boulder catalog for training → [Zenodo 15520275](https://zenodo.org/records/15520275)
31. Lunar navigation and Earth visibility at south-pole sites without dedicated GNSS → LunaNet/LCRNS, landers → LOLA DEMs, LuGRE results → [Wikipedia LunaNet](https://en.wikipedia.org/wiki/LunaNet)
32. MPC pipelines strained by Rubin (standard identification "would take too long"; manual vetting) → Minor Planet Center → MPC/Rubin submissions → [MPC newsletter Feb 2026](https://buttondown.com/MPC_newsletter/archive/newsletter-february-2026/)
33. Small-NEO impact risk often can't be retired without rare space-telescope time (YR4 needed JWST) → planetary defense → JPL Sentry/Scout, MPC → [AAS Nova](https://aasnova.org/2026/05/20/asteroid-2024-yr4-wont-hit-the-moon-new-jwst-observations-show/)
34. Precovery search is manual (3I/ATLAS was in TESS data 55 days before discovery) → small-body community → TESS FFIs, ZTF, Pan-STARRS, DECam + SSOIS → [Wikipedia 3I/ATLAS](https://en.wikipedia.org/wiki/3I/ATLAS)
35. Data withheld during government shutdowns (MRO's 3I/ATLAS images) → researchers, public → n/a → [Wikipedia 3I/ATLAS](https://en.wikipedia.org/wiki/3I/ATLAS)
36. Viral misinformation around discoveries ("alien" 3I/ATLAS) → public, journalists → papers + observations → [Wikipedia 3I/ATLAS](https://en.wikipedia.org/wiki/3I/ATLAS)
37. Deep-space downlink is tiny (JUICE ~2 Gb/day; Clipper ~500 kbps), so onboard data selection matters → outer-planet mission teams → Cassini/Juno archives → [Wikipedia JUICE](https://en.wikipedia.org/wiki/Jupiter_Icy_Moons_Explorer)
38. Linking remote images of solar structures to in-situ plasma measured elsewhere → heliophysicists → PSP, Solar Orbiter, PUNCH, SDO archives → [Wikipedia PUNCH](https://en.wikipedia.org/wiki/Polarimeter_to_Unify_the_Corona_and_Heliosphere)
39. PSP's perihelion data arrive with gaps and delays → PSP science teams → PSP CDAWeb data → [Wikipedia PSP](https://en.wikipedia.org/wiki/Parker_Solar_Probe)
40. 53 missions threatened in the FY27 request, and their value is hard to communicate → Congress, public, scientists → budget docs, ADS bibliographies, archive download stats → [Planetary Society FY27](https://www.planetary.org/articles/analyzing-the-fy-2027-nasa-budget-request)
41. Mission line items "disappear" from the budget instead of being marked terminated, hard to track → policy analysts, advocates → FY26 vs FY27 budget PDFs → [Planetary Society FY27](https://www.planetary.org/articles/analyzing-the-fy-2027-nasa-budget-request)
42. PDS split between PDS3 and PDS4, siloed nodes, unstable Search API → planetary data users → PDS Registry/Search API → [PDS](https://pds.nasa.gov/)
43. Planetary archive projected to grow 3.86 → 24 PB and heliophysics 3.15 → 35 PB by 2030 while staff shrink → NASA SMD → repository metrics → [science.data.nasa.gov](https://science.data.nasa.gov/about/repository-metrics)
44. Legacy analog mission data needs rescue (LOIRP: 1,500 tapes, hand-built demodulator) → archivists, change-detection scientists → PDS LOIRP volumes → [Wikipedia LOIRP](https://en.wikipedia.org/wiki/Lunar_Orbiter_Image_Recovery_Project)
45. Voyager instruments being switched off as RTG power declines → Voyager team, heliophysics → PDS Voyager data → [Wikipedia Voyager](https://en.wikipedia.org/wiki/Voyager_program)
46. Goddard library (~100,000 volumes, some undigitised) closed; 85–90% of holdings reportedly not kept by NASA → NASA engineers/scientists, historians → NTRS, ADS → [Astronomy.com](https://www.astronomy.com/science/union-leader-accuses-isaacman/), [WTOP](https://wtop.com/prince-georges-county/2026/01/nasa-says-historic-materials-will-be-preserved-as-goddard-research-library-shuts-down/)
47. Standard time-series anomaly detection doesn't meet operators' needs → ESA/NASA flight ops → ESA-ADB (11.6 GB, CC BY 3.0 IGO), SMAP/MSL, OPSSAT-AD → [arXiv:2406.17826](https://arxiv.org/abs/2406.17826)
48. Detectors flag rare-but-nominal events as anomalies (false alarms) → flight controllers → ESA-ADB → [GitHub ESA-ADB](https://github.com/kplabs-pl/ESA-ADB)
49. NASA's lessons-learned system is under-used (57% of PMs use it, 43% contribute, "not user friendly") → NASA project managers/engineers → LLIS public lessons → [OIG IG-12-012](https://www.oversight.gov/sites/default/files/oig-reports/IG-12-012.pdf)
50. Brain drain: ~4,000 NASA staff left in 2025, 2,145 senior; tacit knowledge on aging missions at risk → NASA centres, mission teams → mission docs, ops papers, PDS docs → [KPBS/NPR](https://www.kpbs.org/news/national/2025/07/26/nearly-4-000-nasa-employees-opt-to-leave-agency-through-deferred-resignation-program), [Columbia](https://climate.law.columbia.edu/content/nasa-lose-2145-senior-staff)
51. Failure lessons from commercial/small missions are scattered, with no structured taxonomy; descent-nav failures repeat → mission designers, insurers → press releases, OIG/GAO, NTRS → [SpacePolicyOnline](https://spacepolicyonline.com/news/im-2-mission-ends-one-day-after-lunar-landing/)
52. Requirements/standards not linked to lessons (6 of 10 centres don't cross-reference) → systems engineers → NASA standards + LLIS → [OIG IG-12-012](https://www.oversight.gov/sites/default/files/oig-reports/IG-12-012.pdf)
53. Literature volume: ~22k astro-ph listings in 2025, ~24k pace in 2026 → every astronomer → arXiv, ADS/SciX API → [arXiv 2025](https://arxiv.org/year/astro-ph/2025)
54. ADS→SciX: two systems "not sustainable", 13k SciX users vs 5 M ADS users, funding uncertain → ADS team, all astronomers → SciX API → [ADSUG 2025](https://ads.harvard.edu/adsug/2025/ADSUG-2025-Report.pdf)
55. Manual curation can't scale to SciX (2× ADS content), so AI is needed for tagging and linking → ADS/SciX curators → SciX metadata, KAILAS → [ADS funding slides](https://ads.harvard.edu/adsug/2025/01-03-ADSUG2025-ADSFundingandCharge.pdf)
56. Domain-fine-tuned astro LLMs can underperform their base models → astro-ML researchers → AstroMLab benchmarks → [arXiv:2409.19750](https://arxiv.org/abs/2409.19750)
57. LLM benchmarks (MCQ) don't measure research-grade literature use → astro-ML, librarians → AstroMLab-1 (4,425 Qs) → [arXiv:2407.11194](https://arxiv.org/abs/2407.11194)
58. Contradictions across papers go unnoticed → researchers, reviewers → arXiv full text + PaperQA2 → [arXiv:2409.13740](https://arxiv.org/abs/2409.13740)
59. Proposal reviewer matching by 2–5 keywords is crude; reviewer load scales with submissions → ESO, ALMA, STScI → ADS publication records + proposal abstracts → [ESO DPR](https://www.eso.org/sci/observing/phase1/distributed-peer-review.html), [arXiv:2004.04165](https://arxiv.org/abs/2004.04165)
60. "Who has already observed this target?" means querying many siloed archives → proposers, TACs → IVOA ObsCore/TAP (MAST, ESO, HEASARC, IRSA, CADC) → [JW5 TAC results](https://stsci-docs.stsci.edu/policies/files/250513868/250513872/1/1778695182011/JW5-TAC-Results-Public.pdf)
61. Paper↔dataset links incomplete (SciX data-links curation scheduled through 2028) → readers, reproducibility → ADS datalinks + archive bibliographies → [ADS funding slides](https://ads.harvard.edu/adsug/2025/01-03-ADSUG2025-ADSFundingandCharge.pdf)
62. Software behind papers is hard to find or cite → researchers → ASCL, SciX software mentions → [ADSUG 2025](https://ads.harvard.edu/adsug/2025/ADSUG-2025-Report.pdf)
63. Early-career researchers drifting to Google Scholar/ChatGPT; ADS must prove value → ADS/SciX → n/a → [ADSUG 2025](https://ads.harvard.edu/adsug/2025/ADSUG-2025-Report.pdf)
64. Archives reprocess old data (e.g. all IXPE) so published results may shift; users must check processing dates → high-energy astronomers → HEASARC → [NASA data highlights Sep 2026](https://science.data.nasa.gov/features-events/data-software-highlights-september-2026)
65. Artifacts in Euclid (and soon Roman) spectra need human flagging → Euclid/Roman teams → Euclid spectra (Artifact InSPECtor) → [NASA data highlights Sep 2026](https://science.data.nasa.gov/features-events/data-software-highlights-september-2026)
66. Juno, JUICE and Clipper suffer radiation/timer anomalies far from Earth (Juno safe mode Apr 2025; JUICE 20-h loss Jul 2025), so autonomy and quick diagnosis matter → mission ops → mission telemetry (not public) / ESA-ADB proxy → [Wikipedia Juno](https://en.wikipedia.org/wiki/Juno_(spacecraft)), [Wikipedia JUICE](https://en.wikipedia.org/wiki/Jupiter_Icy_Moons_Explorer)
67. Titan's 70–90-minute light time forces fully autonomous landing and flight for Dragonfly → Dragonfly team → Cassini RADAR/VIMS Titan maps → [Wikipedia Dragonfly](https://en.wikipedia.org/wiki/Dragonfly_(Titan_space_probe))
68. Hubble's shared-risk modes (ACS/WFC, WFC3/IR) lose observer and calibration support; grants cut ~30% and allocated by formula → HST archival users, STScI → MAST calibration data → [STScI STUC](https://www.stsci.edu/contents/newsletters/2025-volume-42-issue-01/meeting-of-hubble's-space-telescope-users-committee-stuc)

---

## Cross-slice leads

- **EO companies / EO analytics / US agencies:** Earth science is 127.7 PB of NASA SMD's 150.6 PB holdings and projected 400 PB by 2030; cloud egress ~648 PB/yr ([SMD metrics](https://science.data.nasa.gov/about/repository-metrics)). FY27 request would end 16 Earth-science missions incl. OCO-2, OCO-3, Aura, AOS ([Planetary Society](https://www.planetary.org/articles/analyzing-the-fy-2027-nasa-budget-request)); FY26 request had targeted Terra, Aqua, DSCOVR/EPIC, SAGE III, GOLD, TIMED ([Friends of NASA](https://www.friendsofnasa.org/2025/06/19-active-science-missions-cancelled-in.html)). SciX ingests ~100K Earth-science articles/week but has few Earth-science users ([ADSUG](https://ads.harvard.edu/adsug/2025/ADSUG-2025-Report.pdf)). INDUS includes a CLIMATE-CHANGE NER benchmark; nasa-impact HF hosts `EO-via-NLP` and `WxC-Bench`. Sep 2026: Landsat/HLS Global Cropland Intensity Product v1 (CONUS 2020) ([NASA data highlights](https://science.data.nasa.gov/features-events/data-software-highlights-september-2026)).
- **US agencies:** NASA workforce −20% (~4,000), Goddard 13 buildings/~100 labs closed, library closure, FY26 enacted vs FY27 request numbers (Part 5); PDS moving to NASA's Mission Cloud Platform (pds.mcp.nasa.gov beta) ([PDS](https://pds.nasa.gov/)); NASA Science Data Portal + Science Discovery Engine (science.data.nasa.gov).
- **Space traffic, debris and space weather:** Rubin satellite streak problem ([Rubin FAQ](https://rubinobservatory.org/es/for-scientists/frequently-asked-questions/leo-sats)). CCMC launched beta **Mars CME Scoreboard** and **Mars SEP Scoreboard** (Sep 2026) and re-platformed DONKI ([NASA data highlights](https://science.data.nasa.gov/features-events/data-software-highlights-september-2026)). PUNCH 4-minute CME imagery useful for CME arrival forecasting. MAVEN's loss ends Mars upper-atmosphere/space-weather monitoring.
- **SpaceX, xAI and orbital compute:** Roman launched on Falcon Heavy (30 Aug 2026); NEO Surveyor on Falcon 9 (~$100 M contract); Griffin-1 on Falcon Heavy (Nov 2026); Starship HLS delays (no in-space refuelling or uncrewed lunar test yet as of mid-2026) drove Artemis III's restructure into a LEO test ([CRS](https://www.everycrsreport.com/files/2026-06-25_IF11643_f42f123e3663b5d6aef757a78d6406c1af3dc8be.html)). Deep-space downlink scarcity (JUICE ~2 Gb/day) and SKA's "compute at the data" are arguments for onboard/edge compute. Blue Origin won the Mars Telecommunications Network contract (Rocket Lab protest).
- **ESA and other agencies:** ESA-ADB and OPS-SAT benchmarks (Part 6); Hera arrives at Didymos Nov 2026; Euclid Q1/DR1; ESA Moonlight adopts LunaNet; ESA Gateway elements (I-Hab, Lunar Link, Lunar View) being repurposed after Gateway pause ([Wikipedia](https://en.wikipedia.org/wiki/Lunar_Gateway)); JUICE second Earth flyby 28 Sep 2026; Solar Orbiter Dec 2026 flyby to 24°; ESO DPR; FY27 request would drop NASA contributions to Rosalind Franklin, LISA, Athena, Mars Express, XRISM, Solar-B, ULTRASAT, CODEX ([Planetary Society](https://www.planetary.org/articles/analyzing-the-fy-2027-nasa-budget-request)). ExoFOP news (20 Oct 2026): "Gaia Follow-up Observing Program has launched" ([ExoFOP](https://exofop.ipac.caltech.edu/tess/)), *not investigated*.
- **China:** Korea's KPLO (Danuri) hosts NASA's ShadowCam; Chinese south-pole missions (Chang'e-7, 2026) and Chang'e-6 far-side samples are relevant to Moon Base siting and the MSR vacuum. Not researched here.
- **Datasets catalogue:** ESA-ADB (Zenodo 12528696), Telemanom SMAP/MSL, OPSSAT-AD; MDAD dust masks (Zenodo 7480334); MARCI MDGM PDS4; LRO boulder catalog (Zenodo 15520275); lunar rockfall catalogs; ShadowCam PDS; PGDA south-pole DEMs (81, 104, 78, 69); ExoMiner++ vetting catalog; ExoFOP TOI table; Euclid Q1; DESI DR1; ZTF DR24; GWOSC/GraceDB; MPC; nasa-impact HF IR/QA benchmarks; NASA SMD repository metrics.
- **Models and tools:** Zoobot; INDUS (nasa-impact); AstroLLaMA, AstroLLaMA-2-70B, AstroSage-Llama-3.1-8B; AstroMLab benchmarks; pathfinder (pfdr.app); PaperQA2 (Apache-2.0); cmbagent; Denario; Google AI co-scientist; Telemanom; broker Python clients; DASH/NGSF; SunPy/pySPEDAS; SPICE.

---

## Leads not followed

The web-search budget shared across parallel researchers ran out several times, so these leads were identified but not verified:

- **Social posts** (Bluesky, X, Mastodon, r/astronomy, r/space, Hacker News) on Rubin alerts, MAVEN, ADS→SciX and NASA layoffs. Reddit isn't reachable by the search tool; only Slashdot threads surfaced ([MAVEN thread](https://tech.slashdot.org/story/25/12/11/0026246/), [Goddard library thread](https://tech.slashdot.org/story/25/12/31/2216247), [Rubin data volume thread](https://tech.slashdot.org/story/25/06/29/0119223/)).
- **Conference abstracts:** LPSC 2026 site returned 403; EPSC 2026 session programme did not render; AAS 247 and DPS 2026 ML sessions not searched.
- **Data rescue:** Apollo passive-seismic restoration and the NSSDCA restoration programme in general (heat-flow and Viking items covered in 5.3).
- **Voyager:** which instrument was switched off on Voyager 1 in Apr 2026 (NASA summary page doesn't say; JPL 2025 article URL 404'd).
- **Hubble**: final FY2026 operating level and which modes went shared-risk; **Chandra** 2026 operating level.
- **OpenAI for Science**, FutureHouse hosted platform, Google Scholar Labs, AstroMLab 4 / larger AstroSage models.
- **JWST duplicate-observation policy page** (two URLs 404'd) and **HST archival-publication fraction** (502).
- **MPC staffing/modernisation funding** and annual Rubin observation totals.
- **NASA Technical Reports Server (NTRS)** size and any AI search; recent NASA OIG audits of PDS or science-data management.
- **SKA SRCNet** user access status in late 2026.
- **LIGO** start date of the 2026 interim run and confirmed O5 schedule.
- **FY2027 Senate CJS bill** content and what happens after the CR expires on 11 Dec 2026.
- **ExoMiner++ open-source release** confirmation from NASA.
- **Spacecraft autonomy** programmes 2025–26 (onboard planning, autonomous fault response); ESA-specific LLM ops work (only COMET/SpaceHMchat found, 6.1).
- **Prior-art check for the top hackathon ideas**: existing precovery services (CADC SSOIS and others), lunar descent-imagery simulators and TRN datasets, existing multi-archive target-dossier tools (e.g. ESASky) were not searched in depth. Do this before committing.
- **Mars Future Missions** ($110 M line) content and any MSR successor architecture.
- **Robbins crater catalog** sizes; Roman data policy (no proprietary period) confirmation.
- Rubin first real-time follow-up story ([DIY Photography](https://www.diyphotography.net/?p=317563), not readable) and GeekWire Rubin data-alert piece (403).
