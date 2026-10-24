# US agencies: NASA (Earth science first, plus agency-wide data and AI), NOAA, USGS, Office of Space Commerce, and the problems they publish

Researched on 2026-10-24.

**Scope.** NASA Earth Science missions and data systems (Earthdata Cloud, DAACs, HLS, NISAR, SWOT, PACE, TEMPO, EMIT, GEDI, ICESat-2, GRACE-FO, OCO-2/3, SMAP, ECOSTRESS, Terra/Aqua/Aura); NASA's budget and workforce situation in 2025–2026; NASA AI and data efforts (ESTO/AIST, IMPACT, Prithvi models, Science Discovery Engine, open science); challenge problem lists (Space Apps 2024–2026, FDL, prizes, SBIR); NOAA (satellites, commercial data, cuts, data rescue); USGS (Landsat, EROS); Office of Space Commerce licensing (brief). Each entry lists the problem, current responses, data, off-the-shelf tech, a hackathon angle, credibility and sources.

**Layout.**
- **Main body:** Part A (budget, workforce, policy), Part B (NASA Earth data systems and missions), Part C (NASA AI, applications, open science), Part D (NOAA), Part E (USGS/Landsat), Part F (challenge lists: Space Apps, FDL, prizes, SBIR, IGARSS), Part G (Office of Space Commerce).
- **Section 3:** tables of Space Apps 2024–2026 challenges and SBIR subtopics.
- **Section 4:** problem bank (80 problems).
- **Section 5:** cross-slice leads.
- **Section 6:** leads not followed.

**Method note.** Web search quota was exhausted for most of the session, so most facts come from primary pages opened directly: NASA budget PDFs, NESDIS notices, the Space Apps site API, Hugging Face API, NSIDC, OIG, SpacePolicyOnline and Ars. Unverified items are marked as such.

---

## Part A. NASA budget, workforce and structure (2025–2026): the context behind most problems

### A1. FY2026 President's Budget Request (PBR): the proposed halving of NASA Earth Science

- **What it is:** The White House FY2026 request (May–June 2025) proposed cutting NASA from $24.8B to $18.8B (−24%). Science would fall to about $3.9B, with Earth Science at $1,035.9M, down 52.8% from $2,195M in FY2025.
- **Problems / pain points:**
  - The request "ends over 40 missions, including Earth System Observatory missions." It also cuts Landsat Next and asks NASA and USGS to propose a smaller version, and it cuts Earth Science research and analysis by 50% ([AGU The Bridge, 8 Aug 2025](https://thebridge.agu.org/2025/08/08/appropriations-update-nasa-noaa-and-nsf/)).
  - The Planetary Society's analysis says the request would cancel 19 active science missions representing more than $12B of investment. It would also "slash NASA's workforce by nearly 1/3 in a single year," leaving NASA its smallest workforce since FY1960 ([Planetary Society, Casey Dreier, 8 Jun 2025](https://www.planetary.org/articles/nasa-2026-budget-proposal-in-charts)).
  - Every science division would be cut by 30% to 70%.
- **How they're trying to solve it:** Congress rejected most of the request (see A2). Scientific societies (AGU, AAS, Planetary Society "Save NASA Science") lobbied hard.
- **Data:** The budget documents are public at [nasa.gov/budgets-plans-and-reports](https://www.nasa.gov/budgets-plans-and-reports/).
- **Off-the-shelf tech:** None. This is context.
- **Hackathon angle:** A "mission value explorer" could show, for each mission proposed for termination, who uses its data: papers, downstream products, operational users such as NOAA or USDA. It would do this by mining citations (NASA ADS, the CMR collection metadata) and the DOI landing pages of each mission's datasets. This is a clear problem statement: decision-makers cannot see who depends on a mission's data before cutting it.
- **Credibility:** Official numbers; the Planetary Society and AGU are reputable advocacy and analysis sources.
- **Sources:** [AGU The Bridge, 8 Aug 2025](https://thebridge.agu.org/2025/08/08/appropriations-update-nasa-noaa-and-nsf/); [Planetary Society, 8 Jun 2025](https://www.planetary.org/articles/nasa-2026-budget-proposal-in-charts); [AAS FY26 PBR details, Jun 2025](https://aas.org/posts/news/2025/06/fy26-presidents-budget-request).

### A2. What Congress actually did for FY2026: P.L. 119-74 (signed 23 Jan 2026)

- **What it is:** H.R. 6938 is the Commerce-Justice-Science / Energy-Water / Interior minibus. The Senate passed it 82–15 on 15 Jan 2026, and President Trump signed it on 23 Jan 2026. It came after the record 43-day government shutdown in fall 2025, which ended with a CR in November 2025.
- **Numbers:**
  - NASA gets $24.438B, against $24.838B in FY2025 and $18.8B requested.
  - Science gets $7.250B.
  - **Earth Science gets $2,153M.** The House bill had $1,325M and the Senate bill $2,166M ([CRS R43419, updated 29 Apr 2026](https://www.congress.gov/crs_external_products/R/PDF/R43419/R43419.126.pdf)).
  - NOAA gets $6.171B, against $6.183B in FY2025 and $4.515B requested.
  - The Office of Space Commerce gets $55M, against $65M in FY2025 and $10M requested ([SpacePolicyOnline, 15 Jan 2026, updated 25 Jan 2026](https://spacepolicyonline.com/news/final-fy2026-nasa-noaa-appropriations-bill-clears-senate-white-house-is-next/)).
- **Report language that matters for Earth data:**
  - The Senate "rejects the proposed termination of the Earth System Observatory missions."
  - It funds $200.4M for Earth Venture-class missions and $183M for Landsat Next, and "encourages NASA to maintain the current three-satellite architecture."
  - The House allocated $70M to Sustainable Land Imaging and "directs NASA to select missions capable of operating in a spectrum-constrained environment" ([AGU The Bridge](https://thebridge.agu.org/2025/08/08/appropriations-update-nasa-noaa-and-nsf/)).
- **Problems / pain points:**
  - Even with the money restored, agencies spent most of FY2026 under a CR and a shutdown.
  - Colorado's senators voted no after an amendment to keep NCAR funded was blocked. OMB Director Russell Vought said on 17 Dec 2025 that NCAR "will be dismantled" as a source of "climate alarmism" ([SpacePolicyOnline](https://spacepolicyonline.com/news/final-fy2026-nasa-noaa-appropriations-bill-clears-senate-white-house-is-next/)). NCAR is NSF-funded, but its models and data serve NASA and NOAA users. This is a cross-agency data-continuity problem.
  - FY2027 began on 1 Oct 2026 under a CR that runs out on **11 Dec 2026**, and Congress is out until after the 3 Nov midterms ([SpacePolicyOnline weekly, Oct 4–10 2026](https://spacepolicyonline.com/news/whats-happening-in-space-policy-october-4-10-2026/)).
- **Credibility:** CRS (official), SpacePolicyOnline (reputable press).
- **Sources:** as above.

### A3. FY2027 President's Budget Request (released 3 Apr 2026): the same cuts again, plus Landsat commercialization

- **What it is:** It requests NASA $18.829B (−23%) and Science $3,893.9M. Earth Science would get **$1,021.2M**, flat at about $1.0–1.1B through FY2031.
- **Specifics for Earth Science** ([NASA FY2027 Budget Request Summary](https://www.nasa.gov/wp-content/uploads/2026/04/fiscal-year-2027-budget-request-summary.pdf); [FY2027 Full Budget Request](https://www.nasa.gov/wp-content/uploads/2026/04/fiscal-year-2027-full-budget-request.pdf)):
  - It "prioritizes missions such as NISAR, SWOT, SMAP, PACE, and GRACE-Continuity."
  - **Landsat:** "$109M within Sustainable Land Imaging to support development of one final government satellite for the Landsat program while NASA and USGS concurrently work with industry to support a phased transition to a commercial solution for the program." OMB's version is "$109 million to support a phased transition to a commercial solution" ([SpacePolicyOnline, 3 Apr 2026](https://spacepolicyonline.com/news/trump-fy2027-budget-supports-moon-missions-but-cuts-everything-else/)). The full request says this is "consistent with the findings of the Landsat Mission Alternatives Assessment Team." The Sustainable Land Imaging project will "award a spacecraft contract completing the major acquisitions for the space segment of the follow-on satellite to Landsat-9," using the LandIS instrument contract.
  - Research gets $156M, covering competitively awarded research, AI/ML for science applications and commercial cloud computing. Earth System Science Research (formerly R&A) gets $163.8M.
  - Earth Science Data Systems gets $124.8M. Earth Science Technology gets $33.0M, cut by $27.7M (see A5). Applied and Responsive Earth Science gets $107.7M (see C-section).
  - Earth Systematic Missions, Earth System Explorers and Earth System Science Pathfinder are consolidated into one "Earth System Explorers and Ventures (ESEV)" program. "Multisource Integrated Observatory" (MIO, formerly IESO) funds cross-mission science.
  - "Due to budget constraints, NASA reduced funding for Earth System Explorers Future missions in FY 2027... Both Explorer missions selected in FY 2026 will proceed to confirmation review in FY 2027; the budget supports one mission being implemented in the five-year budget window."
  - Airborne Science will retire or store three aging aircraft.
  - The Earth Science Directed Research and Technology line, which funds civil servants, is reduced "to account for lower than planned future workforce needs."
  - Planned dates: TSIS-2 launch readiness Jan 2027; MAIA launch late FY2027; Libera rides JPSS-4 (FY2028); GRACE-C launch readiness July 2029.
  - **Operating missions:** TEMPO, ECOSTRESS, GEDI, SWOT, TSIS-1, SMAP, GPM, ICESat-2, GRACE-FO, EMIT and PREFIRE are each funded "through FY 2026" and then subject to "the 2026 Senior Review recommendations anticipated in May 2026." The 2026 Senior Review began Jan 2026, with extension guidance due "by September 2026" and funding for missions "with operations extended through 2029." Their FY2027 lines show $0.0 pending that allocation from a shared "Earth Science Senior Review" line of $68.8M.
  - Terra, Aqua, Aura, OCO-2, OCO-3, CYGNSS and SAGE III are **not described as operating missions** in the FY2027 Earth Science chapter. Their status needs checking (see B-section).
- **Problems / pain points:**
  - Planning instability: two consecutive requests to halve Earth Science.
  - A one-year Senior Review cycle decides whether a dozen productive missions continue.
  - Landsat moves toward a commercial model after 54 years of free government data.
- **Hackathon angle:**
  - (a) A Landsat data-continuity risk dashboard. For each Landsat-dependent operational product (USDA crop maps, USGS NLCD, the OpenET water-use estimates in western states, wildfire burn severity MTBS), show what breaks under three scenarios: if Landsat 8 or 9 fails before the next satellite flies, if data becomes commercial-licensed, or if band specifications change.
  - (b) A Senior Review "evidence pack" generator. Given a mission, it would pull publication counts from ADS, data download stats where public, and dataset DOIs from CMR, then produce a one-page impact summary.
- **Credibility:** Official primary documents.
- **Sources:** [NASA FY2027 budget page](https://www.nasa.gov/fiscal-year-2027-budget-request/); [FY2027 summary PDF](https://www.nasa.gov/wp-content/uploads/2026/04/fiscal-year-2027-budget-request-summary.pdf); [FY2027 full request PDF](https://www.nasa.gov/wp-content/uploads/2026/04/fiscal-year-2027-full-budget-request.pdf); [SpacePolicyOnline, 3 Apr 2026](https://spacepolicyonline.com/news/trump-fy2027-budget-supports-moon-missions-but-cuts-everything-else/); [CRS R43419, 29 Apr 2026](https://www.congress.gov/crs_external_products/R/PDF/R43419/R43419.126.pdf).

### A4. NASA workforce: about 4,000 civil servants left in 2025; 7,500 contractors converted in 2026

- **What it is:** In early 2025, thousands of NASA employees left through deferred resignation and other DOGE-era programs. Ars Technica says NASA had "about 14,000 civil servants," a number that "had shrunk by about 4,000 from early 2025." In 2026, Administrator Jared Isaacman's "workforce initiative" is converting 7,500 contract positions into civil-service jobs. NASA now has "about 21,000" civil servants ([Ars Technica, Eric Berger, Oct 2026](https://arstechnica.com/space/2026/10/why-is-nasa-bringing-7500-contractors-back-to-work-as-civil-servants/)).
- **Problems / pain points:**
  - Expertise was lost in 2025, then contractors went through churn in 2026 as they were required to give up their contractor jobs.
  - The conversions are focused on "launch, operations, and mission-critical engineering capabilities." It is not clear that Earth-science data stewardship staff, who were often contractors at DAACs and SIPSs, are protected.
  - JPL laid off about 8% of its workforce, then another 550 workers ([SpacePolicyOnline: JPL lays off eight percent](https://spacepolicyonline.com/news/jpl-lays-off-eight-percent-of-workforce-amid-budget-uncertainty/); [JPL lays off another 550](https://spacepolicyonline.com/news/jpl-lays-off-another-550-workers/)). *Dates not opened; titles are from SPO listings.*
- **How they're trying to solve it:** Bringing contractors in-house to rebuild "core competencies." The Aerospace Safety Advisory Panel called it "a coherent and necessary vision" (Aug 2026, quoted by Ars).
- **Hackathon angle:** Knowledge loss when people leave. A tool that turns a mission's or data product's documentation (ATBDs, user guides, data-product READMEs on Earthdata) into a searchable Q&A "institutional memory" assistant, so a new engineer or user can get answers without the departed expert.
- **Credibility:** Reputable press (Ars); SPO.
- **Sources:** [Ars Technica, Oct 2026](https://arstechnica.com/space/2026/10/why-is-nasa-bringing-7500-contractors-back-to-work-as-civil-servants/); [SPO: Isaacman wants to restore NASA's core competencies](https://spacepolicyonline.com/news/isaacman-wants-to-restore-nasas-core-competencies/) (title only, not opened).

### A5. Earth Science Technology Office (ESTO) cuts in the FY2027 request

- **What it is:** ESTO runs the Instrument Incubator Program (IIP), Advanced Technology Initiatives (ATI), In-Space Validation of Earth Science Technology (InVEST), Advanced Modeling Technology (AMT, which absorbs AI and digital-twin work historically under AIST) and the Quantum Gravity Gradiometer (QGG).
- **Problems / pain points:**
  - "Due to budget constraints, NASA reduced the FY 2027 budget for ESTP by $27.7 million. This reduction will result in terminating some activities and delaying others within the Instrument Incubator project. Impacted activities will include delaying planned development of highly advanced lidar and radar technologies. Under Advanced Technology Initiatives, NASA will discontinue the solicitations for In-Space Validation of Earth Science Technology (InVEST) flight demonstrations."
  - AMT will focus on "transformation of NASA numerical models to make use of artificial intelligence/machine learning (AI/ML)" and on Earth System Digital Twins (ESDTs).
  - QGG (cold-atom interferometry) is to deliver an instrument for on-orbit testing in 2030 to continue the GRACE mass-change record from a single satellite ([FY2027 full request, ES-31 to ES-32](https://www.nasa.gov/wp-content/uploads/2026/04/fiscal-year-2027-full-budget-request.pdf)).
- **Hackathon angle:** ML emulators of physics-based Earth models, which is the AMT mission. For example, a fast surrogate for a land-surface or ocean-model variable trained on public reanalysis (MERRA-2, ECCO), demonstrated as "what-if" scenario exploration in seconds instead of hours.
- **Credibility:** Official.
- **Sources:** [FY2027 full request](https://www.nasa.gov/wp-content/uploads/2026/04/fiscal-year-2027-full-budget-request.pdf).

### A6. NASA SMD "New Competition Model 2.0": changing how science missions are selected (Oct 2026)

- **What it is:** NASA is "rolling out changes to how it selects science missions in an effort to speed up and simplify the process" ([SpaceNews, Jeff Foust, 22 Oct 2026](https://spacenews.com/nasa-to-change-how-it-selects-science-missions/); paywalled, only the lede was readable). An SMD town hall is scheduled for 26 Oct 2026 ([SPO event listing](https://spacepolicyonline.com/news/whats-happening-in-space-policy-october-18-24-2026/)).
- **Problems / pain points:** Proposal preparation is costly and selection is slow. The details of the change are unverified because of the paywall.
- **Hackathon angle:** A proposal-compliance or "AO checker" assistant that reads an Announcement of Opportunity (AO) and a draft proposal and flags missing requirements. Weak fit for the "space data" rule.
- **Credibility:** Reputable press (headline and lede only).
- **Sources:** [SpaceNews, 22 Oct 2026](https://spacenews.com/nasa-to-change-how-it-selects-science-missions/).

### A7. 2025 "closeout" directives and the political push to end NASA Earth science

- **What it is:**
  - **Closeout memos (Jul 2025).** In early July 2025, dozens of NASA mission leaders were told to prepare "closeout" plans "assuming closeout direction is given on October 1, 2025." Missions in operations were told to "assume closeout is complete within 3 months." Ars reports that NASA had 124 science missions in development or operations; the FY2026 request "would cancel 41 of these missions, and another 17 would see their funding zeroed out in the near future" ([Ars Technica, Jul 2025](https://arstechnica.com/space/2025/07/trump-administration-moves-to-tighten-the-noose-around-nasa-science-missions/)). Ars also reports that OMB "stopped NASA from submitting operational plans to Congress."
  - **Duffy on Earth science (Aug 2025).** Then-acting Administrator Sean Duffy said: "All the climate science... we're going to move aside... That's why we have NASA, to explore, not to do all of these Earth sciences." Ars notes that the 1958 Space Act mandates "the expansion of human knowledge of phenomena in the atmosphere and space," and that NASA has typically spent about 10% of its budget on Earth science ([Ars Technica, Aug 2025](https://arstechnica.com/space/2025/08/nasas-acting-chief-calls-for-the-end-of-earth-science-at-the-space-agency/)).
  - **Outcome (Jan 2026).** Congress funded Science at $7.25B, a 1% cut. Casey Dreier: "Those hours could have been spent running and analyzing data from these valuable missions... It created a lot of needless friction and churn." The final bill does "not undo the significant cuts to NASA's workforce through a voluntary buyout program in 2025" ([Ars Technica, Jan 2026](https://arstechnica.com/space/2026/01/nasas-science-budget-wont-be-a-train-wreck-after-all/)).
- **Problems / pain points:**
  - Missions that are switched off are "almost impossible to bring back."
  - Scientists lost months to planning for closeouts.
  - Users of Earth data face recurring uncertainty every budget cycle. FY2027 repeats the cuts, and a CR runs to 11 Dec 2026.
- **Hackathon angle:** A "**what if it's switched off?**" simulator: pick a satellite, then show which downstream products, apps, forecasts and users lose input. It would draw on the Earthdata CMR "platform/instrument → collection" graph plus the citation counts in SciX.
- **Credibility:** Reputable press (Ars), citing reviewed memos and on-record quotes.
- **Sources:** as above.

---

## Part B. NASA Earth Science data systems

### B1. Earthdata Cloud, EOSDIS and the DAACs → "Science Enabling Teams" (SETs)

- **What it is:**
  - EOSDIS has been operated by the ESDIS Project since 1994. Data is distributed by Distributed Active Archive Centers (DAACs): ASF (Fairbanks), ASDC (LaRC), GES DISC (GSFC), LP DAAC (USGS EROS, Sioux Falls), NSIDC DAAC (Boulder), ORNL DAAC, PO.DAAC (JPL), CDDIS (GSFC), GHRC (Huntsville), plus OB.DAAC, LAADS and SEDAC.
  - The archive is moving to **Earthdata Cloud** (in AWS) and is processed with **Cumulus**.
  - Core services: Earthdata Search, the Common Metadata Repository (CMR), Worldview/GIBS, LANCE near-real-time data (within 3 h of overpass) and FIRMS fire alerts ([FY2027 full request, ES-25 to ES-29](https://www.nasa.gov/wp-content/uploads/2026/04/fiscal-year-2027-full-budget-request.pdf)).
- **Problems / pain points:**
  - **Consolidation.** "Reductions to the ESDIS project will require reducing and realigning the DAACs into five thematic science teams." The schedule: ingest and archive consolidated into one team in Q2 FY2027; "Complete transition of ESD data archives to the cloud" in Q3 FY2027; user services consolidated into one team and Earthdata Web Unification complete, both in Q4 FY2027.
  - The budget concedes that "as data has migrated to the cloud, fewer support teams can modernize and handle the user support function." The risk is that domain-expert user support, such as an SAR specialist at ASF or a snow and ice specialist at NSIDC, is diluted.
  - **Long-term cost of cloud.** NASA OIG (IG-20-011, Mar 2020) recommended an "independent analysis to determine the long-term financial sustainability of supporting the cloud migration and operation while also maintaining the current Distributed Active Archive Centers footprint." The recommendation is still open in 2026 with a target date of 31 Mar 2026. NASA's response is to transform "the existing 11 Distributed Active Archive Centers [into] a small number of thematic science-enabling teams" ([NASA 2026 GAO-IG Act report, Apr 2026](https://www.nasa.gov/wp-content/uploads/2026/04/2026-gao-oig-act-report-final-040326.pdf)).
  - **Data volume.** NISAR alone is "delivering dozens of terabytes of data daily" (same source).
  - **New Foundational Data Products (FDP) project.** It centralises data production historically done by mission Science Investigator-led Processing Systems (SIPS), a $10.2M transfer into ESDS. The risk is a loss of algorithm expertise when production moves away from the science teams.
  - Customer satisfaction (ACSI) fell to 78 in 2024 from 79 in 2022.
- **How they're trying to solve it:** Cloud-native archive; web unification; consolidating DAACs into SETs; an independent review in FY2026 of the DAAC-to-SET transition plan.
- **Data:** Earthdata Cloud holds tens of petabytes of free data under NASA's open-data policy. Access needs a free Earthdata Login; in-region (AWS us-west-2) S3 access avoids egress.
- **Off-the-shelf tech:** `earthaccess` (Python), CMR API, STAC (CMR-STAC), Harmony (subsetting/reformatting), OPeNDAP/Hyrax, Zarr/Kerchunk/VirtualiZarr, xarray, Dask, Pangeo, Titiler, GIBS WMTS tiles.
- **Hackathon angle:**
  - (a) An "Earthdata concierge": an LLM agent that turns a plain-English question ("soil moisture in Iowa last July vs. 10-year mean") into CMR queries, `earthaccess` downloads and a plot, standing in for the DAAC user-services expertise being consolidated away.
  - (b) A "what changed in the archive" tracker that diffs CMR collection metadata weekly to flag datasets removed, moved or retired (see B2 for a real example).
- **Credibility:** Official primary documents.
- **Sources:** [FY2027 full request](https://www.nasa.gov/wp-content/uploads/2026/04/fiscal-year-2027-full-budget-request.pdf); [NASA 2026 GAO-IG Act report](https://www.nasa.gov/wp-content/uploads/2026/04/2026-gao-oig-act-report-final-040326.pdf).

### B2. ASF DAAC removes historical SAR datasets from regular access (1 Oct 2026)

- **What it is:** The Alaska Satellite Facility DAAC (Fairbanks) is NASA's SAR archive.
- **Problems / pain points:**
  - Starting **1 Oct 2026**, ERS-1 (1991–1997), ERS-2 (1995–2011), JERS-1 (1992–1998) and RADARSAT-1 (1996–2009) data "will no longer be available through the regular ASF search and download tools."
  - Several datasets are "temporarily offline," and "the specific date at which they will become available again online is to be determined": AIRSAR (1998–2004), GISMO (2006–2008), Glacier Speed (winters 2007–2010), RAMP (1997, 2000), Sea Ice MEaSUREs (1995–2011) and Wetlands MEaSUREs (1993–2009). Users must email ASF User Services.
  - Users are pointed to ESA (ERS), JAXA G-Portal (JERS-1) and the CSA Open Data Portal (RADARSAT-1). No reason is given.
  - This is a concrete case of decades-old SAR baselines (1990s glaciers, wetlands, sea ice) becoming harder to reach.
- **How they're trying to solve it:** Redirecting users to the partner agencies' portals.
- **Data:** The datasets listed above; MEaSUREs products were NASA-funded Earth System Data Records.
- **Off-the-shelf tech:** ASF `asf_search` Python, HyP3 on-demand processing, ESA and JAXA portals.
- **Hackathon angle:** A "dataset continuity map" that, for each retired or offline NASA dataset, finds where else the same or a successor record lives (ESA, JAXA, CSA, Zenodo, community mirrors) and how to get it. Data rescue as a service.
- **Credibility:** Official (Earthdata news post dated 2 Oct 2026, updated 20 Oct 2026).
- **Sources:** [Earthdata: Changes in Availability of Historical ASF Datasets, 2 Oct 2026](https://www.earthdata.nasa.gov/news/changes-availability-historical-asf-datasets).

---

### B3. NISAR (NASA–ISRO SAR): first public science data in July 2026, "dozens of terabytes daily"

- **What it is:** A dual-frequency (L-band NASA/JPL, S-band ISRO) SAR. It launched 30 July 2025 and began its science phase in early November 2025. It images nearly all land and ice every 12 days and is the "trailblazer" of NASA's Earth System Observatory.
- **Data timeline:**
  - **Jan 2026:** 25 uncalibrated L1–L3 sample products ([Earthdata alert: sample products](https://www.earthdata.nasa.gov/data/alerts-outages/nisar-sample-data-products-released)).
  - **27 Feb 2026:** "more than 100,000 Level 1 to Level 3 L-band data products," the second release ([Earthdata, 27 Feb 2026](https://www.earthdata.nasa.gov/news/nisar-mission-team-releases-over-100k-new-data-products)).
  - **20 Jul 2026:** first public calibrated science release, covering acquisitions on or after 17 Jun 2026. Products are all "Provisional Version 1": L0B RRSD/CRSD, L1 RSLC/RIFG/RUNW/ROFF, L2 GSLC/GCOV/GUNW/GOFF and L3 soil moisture (SME2). First-year data is to be backfilled, with "the full science record expected by the end of 2026" ([Earthdata, 21 Jul 2026](https://www.earthdata.nasa.gov/news/nisar-l-band-data-released-expanding-record-surface-changes); [ASF notice](https://asf.alaska.edu/notices/nisar-l-band-data-now-publicly-available/)).
- **Problems / pain points:**
  - **Volume.** NISAR is "delivering dozens of terabytes of data daily" ([NASA GAO-IG Act report, Apr 2026](https://www.nasa.gov/wp-content/uploads/2026/04/2026-gao-oig-act-report-final-040326.pdf)). Few users can download and process SLCs or interferograms locally.
  - **Expertise.** SAR is hard for non-specialists: phase, coherence, polarimetry, unwrapping errors.
  - **Maturity.** Products are provisional, and known issues are listed in the ASF NISAR Data User Guide.
  - The S-band (ISRO) data distribution is not described on the NASA pages.
  - The FY2027 request funds the NISAR line at $23.4M in FY2027, falling to $5.0M in FY2029 and $0 in FY2030 ([FY2027 full request, ES-16](https://www.nasa.gov/wp-content/uploads/2026/04/fiscal-year-2027-full-budget-request.pdf)). That points to a mission-funding cliff after the 3-year prime mission.
- **How they're trying to solve it:** Cloud distribution via ASF (Vertex, `asf_search`, Earthdata Search, Worldview).
  - NASA's disaster applications team plans to integrate "radar coherence and NISAR imagery" into "a unified, multimodal AI model that can support global disaster detection" in FY2027 ([FY2027 full request, ES-36](https://www.nasa.gov/wp-content/uploads/2026/04/fiscal-year-2027-full-budget-request.pdf)).
  - Space Apps 2026 has a NISAR challenge, "Dancing with the SARs," asking teams "to build an interactive application that uses radar remote sensing data from the NISAR mission to track and visualize one or more types of surface change" ([Space Apps 2026](https://www.spaceappschallenge.org/2026/challenges/dancing-with-the-sars/)).
- **Data:**
  - Free, open data; Earthdata Login required.
  - L2 GCOV (backscatter) and GUNW (interferograms) are the most hackathon-friendly products.
  - Format is HDF5. File volumes are not stated on the release pages.
- **Off-the-shelf tech:** `asf_search`, ASF HyP3, ISCE3 (the NISAR processor), MintPy (InSAR time series), xarray/h5py, the OPERA DISP and DSWx products for comparison, Prithvi-EO (optical) or SAR foundation models.
- **Hackathon angle:**
  - (a) "Ground moved here": pick 3 cities with known subsidence (for example California's Central Valley or Houston), take GUNW pairs and produce a plain-language alert map plus a time series.
  - (b) A flood or wetland extent tracker from GCOV backscatter for a recent flood.
  - (c) A "NISAR for non-radar people" explainer bot.
- **Credibility:** Official.
- **Sources:** as above.

### B4. Harmonized Landsat and Sentinel-2 (HLS) and the move to low latency

- **What it is:**
  - Harmonized surface reflectance from Landsat 8/9 OLI (HLSL30) and Sentinel-2A/B/C MSI (HLSS30), both at 30 m on the Sentinel-2 MGRS tile grid (109.8 km tiles), delivered as Cloud-Optimized GeoTIFFs.
  - Global land coverage except Antarctica.
  - Revisit is about 1.6 days with 4 satellites (2022) and about 1.4 days with 5 (2025), now including Sentinel-2C.
  - An HLS vegetation-index (VI) suite was added in Feb 2025.
  - Latency to users is 2–3 days. Low-latency HLS is anticipated to be complete in 2027 ([Earthdata HLS page, updated 21 Oct 2026](https://www.earthdata.nasa.gov/data/projects/hls)).
  - The FY2027 request lists "low latency Harmonized Landsat Sentinel data" as a solution that becomes operational in FY2027 ([FY2027 full request, ES-36](https://www.nasa.gov/wp-content/uploads/2026/04/fiscal-year-2027-full-budget-request.pdf)).
- **Problems / pain points:**
  - 2–3 day latency is too slow for crop-stress alerts, fire response and flood mapping.
  - Clouds: many tiles are cloud-covered.
  - Users must handle Fmask quality-assessment bits.
  - HLS depends on Landsat continuity (Landsat 10 is not until 2031, and the program is moving toward a commercial transition) and on Sentinel-2 continuity.
- **How they're trying to solve it:** Low-latency HLS; the VI suite; the Prithvi foundation models were pre-trained on HLS (see C2).
- **Data:** LP DAAC, free, cloud-hosted (STAC via CMR-STAC). This is one of the biggest analysis-ready optical archives.
- **Off-the-shelf tech:** `earthaccess`, `stackstac`/`odc-stac`, rioxarray, Prithvi-EO-2.0 (300M/600M) with TerraTorch, NASA AppEEARS (point and area extraction).
- **Hackathon angle:** A "field-level anomaly alert." For a farm polygon, pull the HLS NDVI/EVI time series, compare it with a 5-year baseline, then flag and explain anomalies (drought, hail, flood). This is the real-world version of the 2024 Space Apps winners Waterwise and NVS-knot.
- **Credibility:** Official.
- **Sources:** [Earthdata HLS](https://www.earthdata.nasa.gov/data/projects/hls); [FY2027 full request](https://www.nasa.gov/wp-content/uploads/2026/04/fiscal-year-2027-full-budget-request.pdf).

### B5. Terra, Aqua, Aura: the aging EOS flagships drifting toward end of life

- **What it is:** NASA's Earth Observing System flagships: Terra (launched Dec 1999), Aqua (May 2002) and Aura (2004). Their instruments include MODIS, ASTER, MISR, CERES and MOPITT on Terra; AIRS, AMSU, CERES and MODIS on Aqua; and OMI and MLS on Aura. Together they produce 20+ year climate records.
- **Problems / pain points:**
  - **Terra.** "Since 2020, Terra has been drifting to an earlier equator crossing time, and in October 2022 was lowered by ~5km in altitude." Terra "has recently been experiencing power-based limitations caused by orbital changes and solar array efficiency. In order to maintain power margins, the Terra team moved the MOPITT instrument from science mode into safe mode on February 4th, 2025, ceasing data collection." That ends a 25-year carbon-monoxide record from MOPITT. "With no maneuvers planned to sustain Terra's altitude and crossing time, Terra will slowly get closer and closer to Earth" ([terra.nasa.gov](https://terra.nasa.gov/), accessed 2026-10-24). Users asked for weekly crossing-time and altitude updates, which the team now posts.
  - **Aqua.** "completed the last of its drag makeup maneuvers in December 2021 and is now in a free-drift mode," and "slowly descending below the A-Train and drifting to later equatorial crossing times." It still returns data from 4 of 6 instruments: AIRS, AMSU, CERES and MODIS ([science.nasa.gov/mission/aqua](https://science.nasa.gov/mission/aqua/), updated 5 Oct 2026).
  - **Aura.** "Insufficient power generation by the solar array is conservatively predicted to be the life-limiting factor for the Aura satellite and instruments by mid-2028" ([aura.gsfc.nasa.gov](https://aura.gsfc.nasa.gov/)).
  - **Budget.** The FY2027 request's Earth Science chapter does not list Terra, Aqua or Aura among operating missions (see A3). Their data appear only within the Earth Radiation Data Continuity project ([FY2027 full request](https://www.nasa.gov/wp-content/uploads/2026/04/fiscal-year-2027-full-budget-request.pdf)).
  - **Drift effects.** Drifting overpass times change illumination, sun-glint and land-surface-temperature diurnal sampling. This creates artificial trends in long records unless corrected. NASA held a "Terra, Aqua, and Aura Drifting Orbits Workshop" (linked from terra.nasa.gov).
  - **Continuity.** MODIS products must transition to VIIRS (S-NPP, NOAA-20, NOAA-21). S-NPP itself is being shut off: NOAA ends S-NPP data on 2 Nov 2026 and starts deorbiting it on 1 Dec 2026 (see D4).
- **How they're trying to solve it:** The MODIS-to-VIIRS continuity products (the NASA "Land/Atmosphere SIPS" lineage); the new Foundational Data Products (FDP) project "to ensure smooth and cost-effective user transitions between data from different missions." NASA also consolidated funding for Suomi-NPP data products under ESDS ([FY2027 full request](https://www.nasa.gov/wp-content/uploads/2026/04/fiscal-year-2027-full-budget-request.pdf)).
- **Data:**
  - MODIS (LAADS DAAC, LP DAAC) runs 2000 to present.
  - The Terra 25-year archive covers "over 9,000 days" ([Space Apps 2025, Terra challenge](https://www.spaceappschallenge.org/2025/challenges/animation-celebration-of-terra-data/)).
  - VIIRS runs 2012 to present.
- **Off-the-shelf tech:** NASA Worldview/GIBS, `earthaccess`, pyhdf/netCDF4, the MODIS-VIIRS cross-calibration literature.
- **Hackathon angle:**
  - (a) A "drift artifact detector": quantify how Terra's earlier overpass biases a MODIS land-surface-temperature or NDVI trend, compared against VIIRS or Landsat at fixed overpass times.
  - (b) The 2026 Space Apps challenge "**Harmonization of MODIS and VIIRS Hot Spots**." It states that the active-fire record "is split across sensors whose data cannot be compared directly, leaving fire managers without a consistent picture" and asks for "a burning activity calendar" ([Space Apps 2026](https://www.spaceappschallenge.org/2026/challenges/modis-and-viirs-hot-spots/)). FIRMS provides both MODIS and VIIRS hotspots. This is a ready-made, well-scoped problem.
- **Credibility:** Official mission pages.
- **Sources:** [terra.nasa.gov](https://terra.nasa.gov/); [Aqua](https://science.nasa.gov/mission/aqua/); [Aura](https://aura.gsfc.nasa.gov/); [Space Apps 2026 MODIS/VIIRS](https://www.spaceappschallenge.org/2026/challenges/modis-and-viirs-hot-spots/).

### B6. OCO-2 and OCO-3: handed to Caltech under no-cost Space Act Agreements (Aug 2026)

- **What it is:** Orbiting Carbon Observatory-2 (free-flyer, launched 2014) and OCO-3 (on the ISS since 2019) measure column CO₂ and solar-induced fluorescence (SIF).
- **Problems / pain points:**
  - Both were targeted for termination in the FY2026 request.
  - NASA instead issued an "Announcement for Partnership Proposals" on 8 Jan (2026) for OCO-2 and an ISS NASA Research Announcement on 11 Aug 2025 for OCO-3.
  - On 14 Aug 2026, "NASA and Caltech have signed non-reimbursable Space Act Agreements for two Earth science missions... The partnership will last up to five years with NASA maintaining ownership of both missions and Caltech operating the missions and science data systems, including creating new data products" ([NASA OCO blog, 24 Aug 2026](https://science.nasa.gov/blogs/oco-2/2026/08/24/nasa-caltech-partner-on-two-earth-science-missions/)).
  - "Non-reimbursable" means NASA does not pay. Caltech must find the operating money, presumably philanthropic or commercial.
  - The pattern is a new one: **mission "divestiture" to non-NASA operators**. Data continuity and open-data terms under a private operator are open questions.
- **How they're trying to solve it:** A public–private partnership for operations.
- **Data:** OCO-2/3 L2 XCO₂ and SIF via GES DISC. The US Greenhouse Gas Center also publishes derived products (OCO-2 GEOS column CO₂, OCO-2 MIP top-down budgets) ([Space Apps 2024 GHG challenge](https://www.spaceappschallenge.org/nasa-space-apps-2024/challenges/uncover-the-role-of-greenhouse-gases-in-your-neighborhood/)).
- **Off-the-shelf tech:** US GHG Center (earth.gov/ghgcenter) APIs, VEDA, xarray.
- **Hackathon angle:** A "who still measures what" continuity tracker for carbon observing (OCO-2/3, GOSAT-GW, Sentinel-5P, EMIT methane, Carbon Mapper/Tanager). It would show coverage gaps after mission transitions, then a city-level CO₂ anomaly demo using OCO-3 snapshot-area-map (SAM) observations.
- **Credibility:** Official.
- **Sources:** [NASA OCO blog, 24 Aug 2026](https://science.nasa.gov/blogs/oco-2/2026/08/24/nasa-caltech-partner-on-two-earth-science-missions/).

### B7. Operating "workhorse" missions awaiting the 2026 Senior Review: SWOT, PACE, TEMPO, EMIT, GEDI, ICESat-2, GRACE-FO, SMAP, GPM, ECOSTRESS, PREFIRE, TSIS-1

- **What it is:** Missions past or near the end of prime operations, funded "through FY 2026." Funding beyond that depends on "the 2026 Senior Review recommendations anticipated in May 2026," with "extension guidance provided to the missions by September 2026" ([FY2027 full request, ES-19 to ES-24](https://www.nasa.gov/wp-content/uploads/2026/04/fiscal-year-2027-full-budget-request.pdf)).
  - **TEMPO:** hourly geostationary NO₂, O₃ and HCHO over North America, hosted on Intelsat-40e. It "completed prime operations in June 2025 and passed end-of-prime-mission review in December 2025."
  - **ECOSTRESS and GEDI** (on the ISS) were approved through Sept 2026. GEDI was stowed on the ISS between Mar 2023 and Apr 2024.
  - **SWOT** "will remain in prime mission operations until September 2026."
  - **PACE** (launched 8 Feb 2024) gets increased FY2027 funding "to increase the breadth of data processing and higher-level data products." Prime operations end in Q3 FY2027.
  - **EMIT** (ISS hyperspectral) extended until the FY2026 Senior Review. "Science teams are now extending the impact of the EMIT mission by using EMIT data in assessment of vegetation and agriculture health and critical minerals."
  - **SMAP's** radar failed in July 2015; its radiometer continues.
  - **GRACE-FO** continues the mass-change record. GRACE-C is scheduled for launch readiness July 2029, and OIG says it is "on track... and operate within cost and schedule baselines, [but] the project is facing cost pressure" ([NASA OIG IG-26-012](https://oig.nasa.gov/audits/nasas-management-of-the-gravity-recovery-and-climate-experiment-continuity-grace-c-mission/)).
- **Problems / pain points:**
  - The 2026 Senior Review outcome (Sept 2026) was **not found** in this research. Mark it as an unverified lead.
  - Several FY2027 lines show $0.0, pending allocation from a $68.8M "Earth Science Senior Review" pool. That is a small pool for about a dozen missions.
  - The ISS-hosted missions (ECOSTRESS, GEDI, EMIT, OCO-3) depend on ISS accommodation and face the ISS end of life.
  - The **mass-change gap risk** between GRACE-FO (launched 2018) and GRACE-C (2029).
- **Data:** All free on Earthdata:
  - SWOT: PO.DAAC (L2 LR_SSH, river and lake products)
  - PACE: OB.DAAC (OCI hyperspectral)
  - TEMPO: ASDC (L2/L3 hourly)
  - EMIT: LP DAAC (L2A reflectance, L2B minerals, methane plumes)
  - GEDI: LP DAAC/ORNL (L2A/L2B/L4A biomass)
  - ICESat-2: NSIDC (ATL03–ATL24)
  - GRACE-FO: PO.DAAC (mascons)
  - SMAP: NSIDC (L3/L4)
  - GPM: GES DISC (IMERG)
  - ECOSTRESS: LP DAAC (LST, ET)
- **Off-the-shelf tech:** `earthaccess`, `icepyx` (ICESat-2), `sliderule` (ICESat-2 on-demand), `harmony-py`, RSIG and RSIG-py for TEMPO, OpenET.
- **Hackathon angle:**
  - (a) **TEMPO hourly air quality + forecasting.** This is the 2025 Space Apps challenge "From EarthData to Action," which asks for "a web-based app that forecasts air quality by integrating real-time TEMPO data with ground-based air quality measurements and weather data, notifying users of poor air quality" ([Space Apps 2025](https://www.spaceappschallenge.org/2025/challenges/from-earthdata-to-action-cloud-computing-with-earth-observation-data-for-predicting-cleaner-safer-skies/)).
  - (b) **"Sharks from Space."** PACE phytoplankton plus SWOT eddies to predict foraging hotspots ([Space Apps 2025](https://www.spaceappschallenge.org/2025/challenges/sharks-from-space/)).
  - (c) **EMIT methane plume finder** linked to facility databases.
  - (d) **SWOT river discharge** for flood early warning in data-poor basins.
  - (e) **GRACE-FO groundwater depletion** explainer for agricultural regions.
  - (f) **Mission impact dossier** for the Senior Review (see A3).
- **Credibility:** Official.
- **Sources:** [FY2027 full request](https://www.nasa.gov/wp-content/uploads/2026/04/fiscal-year-2027-full-budget-request.pdf); [OIG GRACE-C](https://oig.nasa.gov/audits/nasas-management-of-the-gravity-recovery-and-climate-experiment-continuity-grace-c-mission/).

### B8. Earth System Observatory (ESO) core missions and Earth System Explorers: proposed for termination, partly rescued, now squeezed

- **What it is:** The 2017 Decadal Survey "designated observables."
  - NASA's ESO page lists five core areas: Aerosols, Cloud/Convection/Precipitation, Mass Change, Surface Biology and Geology (SBG), and Surface Deformation and Change. NISAR is the "trailblazer" ([NASA ESO page, last modified Apr 2024](https://science.nasa.gov/earth-science/missions/earth-system-observatory/)).
  - The cost-capped "Earth System Explorers" line was created after the 2023 decadal midterm.
- **Problems / pain points:**
  - The FY2026 request proposed terminating ESO missions. The Senate "rejects the proposed termination" ([AGU](https://thebridge.agu.org/2025/08/08/appropriations-update-nasa-noaa-and-nsf/)).
  - The FY2027 request does not mention the Atmosphere Observing System (AOS) or SBG at all. Only GRACE-C (mass change) and NISAR survive by name ([FY2027 full request](https://www.nasa.gov/wp-content/uploads/2026/04/fiscal-year-2027-full-budget-request.pdf); a text search found no mention of "Atmosphere Observing" or "Surface Biology").
  - Earth System Explorers: "Both Explorer missions selected in FY 2026 will proceed to confirmation review in FY 2027; the budget supports one mission being implemented in the five-year budget window."
  - Practical effect: the hyperspectral (SBG) and aerosol/cloud (AOS) observing capabilities recommended by the decadal survey may not fly. Users would have to rely on EMIT (ISS, aging), PACE, ESA CHIME (cross-slice) and commercial hyperspectral sensors.
  - OIG (Oct 2026) found NASA's decadal survey oversight "hindered by challenges." For example, the National Academies (NASEM) "often takes 2 years to complete the survey process but gives the Agency less than 10 days to review" prepublication reports. NASA "does not track how the SMD divisions are implementing decadal survey recommendations" ([NASA OIG, Oct 2026](https://oig.nasa.gov/news/nasas-decadal-survey-oversight-is-hindered-by-challenges-with-internal-processes-communication-and-progress-tracking/)).
- **Hackathon angle:**
  - A "decadal survey tracker." Parse the 2017 Earth Science Decadal Survey recommendations and track each one's implementation status from budget documents and NASA mission pages. OIG says NASA itself does not do this. It uses literature and budget data; the "space data" link is weaker but the problem is crisp.
  - Alternatively, an "SBG-lite" demo using EMIT plus PACE to show what hyperspectral-from-space delivers (minerals, methane, crop health, harmful algal blooms), as a case for continuity.
- **Credibility:** Official (budget, OIG); AGU.
- **Sources:** as above.

### B9. Earth Science Data Systems: user problems surfaced by NASA itself (SMD Data & Computing Strategy 2025–2030, Apr 2026)

- **What it is:** NASA's science-wide data strategy (NASA/SP-20260002277, April 2026, Nicky Fox and Kevin Murphy, Chief Science Data Officer).
- **Problems / pain points (verbatim list of "five critical challenges"):**
  1. "Infrastructure Fragmentation: Duplicative systems limit efficiency and interoperability while increasing costs and security vulnerabilities."
  2. "Computational Resource Limitations: Scientific demands increasingly exceed available HEC and researchers struggle to access cloud computing."
  3. "Data Standards and Interoperability: Inconsistent implementation of FAIR principles and metadata standards hinders data discovery, citation, and reuse across disciplines."
  4. "Software Recognition and Support: Insufficient recognition of software as a critical scientific asset... leads to inadequate support, preservation, maintenance, and reuse."
  5. "Workforce Skills Gap: Growing need for specialized expertise in data science, AI, and other complex methods outpaces NASA's ability to recruit and retain qualified personnel."
  - Scale: SMD "manages over 150 Petabytes (PB) of observational data... By 2030, the projected total scientific data volume... is expected to be 530 PB." It is held "across 10 repositories... Each of SMD's five divisions maintains its own data systems... While some divisions have created a single point of entry, others have a multitude of entry points. Useful software tools are often not clearly linked, and tutorials are developed inconsistently."
  - On software: "Unlike data, which has established archival processes, software frequently exists without coordinated stewardship strategies, leading to duplication of effort and lost capabilities when projects end."
  - ([SMD Data and Computing Strategy 2025–2030, Apr 2026](https://assets.science.nasa.gov/content/dam/science/cds/about-us/ocsdo/reports/SMD_Data_Computing_Strategy_2025_2030.pdf))
- **How they're trying to solve it:** Core Data and Computing Services; IMPACT; division foundation models; VEDA; CryoCloud; SciX (the successor to ADS); the OCSDO's Data Analysis Services Program; hackathons and AI training (the 2025 SPARK AI campaign).
- **Off-the-shelf tech:** SciX/ADS API, CMR, STAC, VEDA, CryoCloud JupyterHub, `nasa-impact` models on Hugging Face.
- **Hackathon angle:** A "single front door": one natural-language search across Earthdata (CMR), PDS (planetary), HEASARC/MAST (astro), SPDF (helio) and SciX papers that returns datasets plus the papers that used them plus code. NASA itself names this fragmentation as challenge #1 and #3.
- **Credibility:** Official.
- **Sources:** [SMD Data and Computing Strategy 2025–2030](https://assets.science.nasa.gov/content/dam/science/cds/about-us/ocsdo/reports/SMD_Data_Computing_Strategy_2025_2030.pdf); [NASA Open Science page, updated 15 Sep 2026](https://science.nasa.gov/open-science/).

### B10. Polar and cryosphere records at NSIDC: the 47-year passive-microwave sea-ice record stops forward processing; SMAP geolocation error; product retirements

- **What it is:** The NSIDC DAAC in Boulder distributes the passive-microwave sea-ice record (Nimbus-7 SMMR → DMSP SSM/I-SSMIS → AMSR2), plus SMAP and ICESat-2 data.
- **Problems / pain points** (from the [NSIDC data announcements](https://nsidc.org/data/user-resources/data-announcements), accessed 2026-10-24):
  - **Sea-ice record.** "The Bootstrap Sea Ice Concentrations from Nimbus-7 SMMR and DMSP SSM/I-SSMIS, Version 4 dataset... has stopped forward processing. The final temporal coverage for the data is 1 November 1978 to 31 December 2025." This climate record, 47 years long, is now static. DMSP SSM/I-SSMIS brightness temperatures were still updated "through 5 July 2026," which shows the DMSP stream is ending.
  - **Successor sensors.** AMSR2 (JAXA) products "will continue forward processing," and "NSIDC is planning for the development of AMSR3 data products in 2027." The sensor transition requires intercalibration to avoid a step change in the record.
  - **SMAP geolocation error.** "SMAP Standard and Near Real-Time data sets... experienced a geolocation issue from 14 May 2026 to 28 July 2026." Standard products were reprocessed, but "Near Real-Time products will not be replaced." "We recommend that users who previously downloaded data from that time period redownload the corrected files." Users of the bad data are not told automatically.
  - **ICESat-2 product retirement.** The ICESat-2 L3A coastal and nearshore bathymetry product v1 is retired on 23 Nov 2026, after which "data will no longer be accessible."
  - **S-NPP VIIRS** delivery into NSIDC stops on 2 Nov 2026.
  - **Sea Ice Today** tools were suspended for lack of funding (see D6).
  - The DMSP data cut-off itself (DoD decision, 2025) is not re-verified here (see Leads not followed).
- **How they're trying to solve it:** AMSR2 continuity; AMSR3 (on JAXA's GOSAT-GW) products planned for 2027; reprocessing.
- **Data:** NSIDC Sea Ice Index (G02135), Bootstrap and NASA Team concentration records, the AMSR2 unified products, SMAP L3/L4, and ICESat-2 ATL07/ATL10 (sea-ice freeboard) and ATL20/21.
- **Off-the-shelf tech:** `earthaccess`, `icepyx`, xarray. Changepoint detection (`ruptures`) can find breaks at sensor transitions.
- **Hackathon angles:**
  - (a) A **"bad data notifier."** Users subscribe their download history (CMR granule IDs), and the tool alerts them when a granule they used is reprocessed or recalled, as with the SMAP geolocation case. Nothing like this exists, and the problem applies to every DAAC.
  - (b) A **sensor-transition checker** for climate records (SSMIS→AMSR2, MODIS→VIIRS, Terra drift) that flags discontinuities.
- **Credibility:** Official.
- **Sources:** [NSIDC data announcements](https://nsidc.org/data/user-resources/data-announcements); [NSIDC Sea Ice Today](https://nsidc.org/sea-ice-today).

### B11. NASA near-real-time global flood product, FIRMS, and the LANCE near-real-time (NRT) system

- **What it is:** NASA's LANCE delivers products "within three hours of each satellite overpass."
  - **Global flood products (MODIS/VIIRS).** Since Dec 2025 they distinguish "recurring" from unusual floods: an area counts as recurring if it was flooded in "at least seven of those 22 years." A **23-year reprocessed MODIS flood archive (2003–2025)** was released in Apr 2026 on LAADS. From 2026, MODIS NRT products are "permanently archived" rather than kept for about one week ([Earthdata blog, 10 Apr 2026](https://www.earthdata.nasa.gov/news/blog/nasa-enhances-global-flood-products-smarter-detection-flooding-release-23-year-archive)).
  - **FIRMS** (active fire) added NOAA-21 OMPS Aerosol Index and Pyrocumulonimbus Aerosol Index layers in Oct 2026, at about 12×10 km versus about 50×50 km for S-NPP ([Earthdata blog, 13 Oct 2026](https://www.earthdata.nasa.gov/news/blog/new-higher-resolution-aerosol-index-pyrocumulonimbus-layers-now-available-nasa-firms)). A "Satellite Swath Outlines" product was added in Jun 2026.
- **Problems / pain points:**
  - NRT inputs cause "occasional pixel-level shifts" that affect flood detection.
  - Optical flood mapping is blocked by clouds (an inference: SAR from NISAR or Sentinel-1 is the usual fix).
  - The S-NPP data end forces users onto NOAA-20/21.
  - The Earthdata site banner warns that a "Consolidated Ingest and Archive migration will interrupt ingestion at PO.DAAC, ASF DAAC, and GES DISC on Oct. 28–30, 2026" (seen on the [Earthdata blog index](https://www.earthdata.nasa.gov/news/blog)). This is a concrete effect of the DAAC consolidation described in B1.
- **Data:** LANCE NRT, LAADS DAAC (MCDWD flood product and the new archive), FIRMS API (free MAP_KEY), GIBS tiles.
- **Off-the-shelf tech:** FIRMS REST API, GIBS WMTS, OPERA DSWx (HLS-based water), Sentinel-1 or NISAR GCOV for cloud-free floods.
- **Hackathon angle:** A **"cloud-proof flood map"**: fuse the MODIS/VIIRS flood product (fast but cloud-limited), OPERA DSWx (30 m) and SAR backscatter into one flood-extent layer with a confidence score. Use the 23-year archive to say "this flooding is unusual for this place."
- **Credibility:** Official.
- **Sources:** as above.

---

## Part C. NASA AI, applications and open-science efforts

### C1. Applied and Responsive Earth Science (formerly Applied Sciences / "Earth Action"): Disasters, Wildland Fire, Agriculture, EarthRISE, CSDA

- **What it is:** NASA's applications program. In FY2027 the "Applied Sciences Program and the Responsive Science Initiatives" are consolidated into one program ($107.7M request). The new projects are:
  - "Preparedness and Resilience": the former Disasters and Wildland Fires projects.
  - "Agriculture, Water, and Natural Resources."
  - "Earth Resources for Industry & State Empowerment (EarthRISE)."
  - "Artificial Intelligence & Advanced Modeling Applications."
  - "Commercial Satellite Data Acquisition (CSDA)."
  - ([FY2027 full request, ES-35 to ES-37](https://www.nasa.gov/wp-content/uploads/2026/04/fiscal-year-2027-full-budget-request.pdf))
  - The Earth Action web page lists Agriculture, Disasters, Ecological Conservation, Energy and Infrastructure, Health and Air Quality, Water Resources and Wildland Fires. It also lists ARSET training, "Geospatial Super Intelligence (GeoSI) for Applications Development," CSDA, the Earth Information Center (earth.gov), EarthRISE, ISON, MIO, Private Sector Engagement and SPoRT ([science.nasa.gov/earth-science/earth-action, updated 15 Oct 2026](https://science.nasa.gov/earth-science/earth-action/)).
- **Problems / pain points:**
  - "NASA reduced the total number of projects and decreased sub-elements within each project."
  - "Last-mile" problem: state, local, tribal and private users cannot easily turn satellite data into decisions, which is EarthRISE's stated purpose.
  - The Disasters program wants faster damage detection: "advance the use of AI-powered Earth observation foundation models to detect damage from hazards... deliver faster, more accurate insights for emergency response," including "radar coherence and NISAR imagery... a unified, multimodal AI model that can support global disaster detection."
  - SERVIR (USAID–NASA) was terminated in 2025; the FY2027 OMB document cites it as an example termination ([SpacePolicyOnline, 3 Apr 2026](https://spacepolicyonline.com/news/trump-fy2027-budget-supports-moon-missions-but-cuts-everything-else/)).
- **How they're trying to solve it:**
  - **CSDA** plans a "third IDIQ contract on-ramp in FY 2027."
  - **EarthRISE** will support OpenET field-scale ET for farmers.
  - **EI4Food** will "align leading food system actors (including General Mills, McDonald's, and Costco) around a shared needs assessment."
  - **ISON** will finish "the next assessment of federal agency needs."
  - **EarthRISE Developers Academy** (training, page updated 17 Jul 2026) ([EarthRISE](https://science.nasa.gov/earth-science/earth-action/earthrise/)).
  - **GeoSI** "for Applications" solicitation (NSPIRES). It uses "machine learning, Earth observation foundation models, and emerging agentic SI systems" to "broaden access, speed development, and lower computational costs." It names Prithvi-EO and Prithvi-WxC ([GeoSI page, updated 15 Oct 2026](https://science.nasa.gov/earth-science/earth-action/geosi/)).
  - Note: in 2026, US government documents increasingly use "Super Intelligence (SI)" where "AI" was used before. It appears in GeoSI, in the 2026 Space Apps challenge "Flame in Freefall" ("super intelligence (SI) powered dashboard") and in a NOAA CRADA (see D5).
- **Data:** NASA Disasters mapping portal, FIRMS, OPERA (DSWx, DIST-ALERT), HLS, NISAR, CSDA commercial data (restricted licenses; Planet, Maxar/Vantor, ICEYE, Umbra, Capella and others for funded researchers).
- **Off-the-shelf tech:** Prithvi-EO-2.0 plus TerraTorch, the GeoSI agentic stacks, OpenET API, Google Earth Engine (community), LLM tool-use over STAC.
- **Hackathon angle:**
  - (a) An **"agentic disaster analyst"**: given a disaster name and date, the agent finds pre- and post-event HLS/Sentinel-1/NISAR scenes, runs a damage or flood model and writes a FEMA-style situation report with a map. This is exactly the GeoSI pitch.
  - (b) An **"EarthRISE for a county"** last-mile dashboard (drought + ET + fire risk) for one Californian county.
- **Credibility:** Official.
- **Sources:** as above.

### C2. NASA–IBM foundation models: Prithvi-EO, Prithvi-WxC, Surya (heliophysics), the new Lunar Foundation Model, and INDUS / SDE language models

- **What it is:** Open-weight foundation models released on Hugging Face by NASA IMPACT/OCSDO with IBM Research. Release dates and downloads below are from the Hugging Face API on 2026-10-24:
  - **Prithvi-EO-1.0-100M** (Jul 2023; fine-tunes for burn scars, multi-temporal crops and Sen1Floods11).
  - **Prithvi-EO-2.0** in 300M and 600M, with temporal-location "TL" variants (Dec 2024). The 300M has about 19.5k downloads. Tiny-TL and 100M-TL variants followed (Sep 2025), plus a BurnScars fine-tune (Feb 2025) ([HF org ibm-nasa-geospatial](https://huggingface.co/ibm-nasa-geospatial)).
  - **Prithvi-WxC-1.0-2300M** (Sep 2024), a weather/climate model trained on MERRA-2, with gravity-wave parameterization and rollout fine-tunes.
  - **Surya-1.0** (Aug 2025), a heliophysics model trained on SDO data, with downstream models for solar flares, solar wind, EUV spectra and active-region segmentation. The SuryaBench datasets include core-sdo, flare-forecasting and solarwind ([HF org nasa-ibm-ai4science](https://huggingface.co/nasa-ibm-ai4science)).
  - **NASA-IBM Lunar Foundation Model** (1 Sep 2026), with crater detection, IMP segmentation and ice-prospectivity fine-tunes and the "Sombench" datasets (LRO NAC/WAC crater detection, etc.).
  - **Language models:** the `nasa-smd-ibm` "INDUS" encoder family (2023–2024) and `indus-sde` models for the Science Discovery Engine (2025–2026). Benchmarks: WxC-Bench (about 119k downloads), nasa-smd-qa, the SDE IR benchmark (Oct 2025), and nasa-science-code-benchmark (Apr 2026) ([HF org nasa-impact](https://huggingface.co/nasa-impact)).
  - **Fine-tuning datasets:** hls_burn_scars, multi-temporal-crop-classification, Landslide4sense (about 39k downloads), BioMassters, hls_merra2_gppFlux, burn_intensity, hurricane.
- **Problems / pain points:**
  - Fine-tuning needs labelled data, and labels are scarce for many hazards.
  - Large models need GPUs.
  - Fine-tunes have modest downloads, so there are few real downstream deployments.
  - "Division subject matter NASA Foundation Models" are being released but there is no unified catalogue ([SMD strategy, Apr 2026](https://assets.science.nasa.gov/content/dam/science/cds/about-us/ocsdo/reports/SMD_Data_Computing_Strategy_2025_2030.pdf)).
- **How they're trying to solve it:** TerraTorch fine-tuning toolkit (IBM), GeoSI applications, disaster AI scale-up.
- **Data:** HLS (Prithvi-EO), MERRA-2 (WxC), SDO AIA/HMI (Surya), LRO (Lunar FM).
- **Off-the-shelf tech:** Hugging Face transformers, TerraTorch, PyTorch Lightning. Prithvi-EO-2.0-300M fits on a single consumer GPU for fine-tuning; a 2–3 hour fine-tune is feasible at a hackathon.
- **Hackathon angle:**
  - (a) Fine-tune Prithvi-EO-2.0-tiny/100M on a small new labelled set (for example a 2026 wildfire burn scar from HLS) and ship a "burn-scar in 10 minutes" app.
  - (b) A Surya flare-probability dashboard for satellite operators. This is cross-slice with space weather.
  - (c) Use Prithvi embeddings for "find more places like this," a similarity search over HLS tiles.
- **Credibility:** Official model cards and HF API.
- **Sources:** [HF ibm-nasa-geospatial](https://huggingface.co/ibm-nasa-geospatial); [HF nasa-ibm-ai4science](https://huggingface.co/nasa-ibm-ai4science); [HF nasa-impact](https://huggingface.co/nasa-impact).

### C3. Science Discovery Engine (SDE), OCSDO and open science (TOPS, SPD-41a)

- **What it is:** The SDE is NASA's cross-division search engine for science data, documentation and software. sciencediscoveryengine.nasa.gov now 301-redirects to science.data.nasa.gov/science-discovery-engine/search/, part of the new "Science Data Portal" (science.data.nasa.gov). The OCSDO runs open-science policy: SPD-41a requires publications from NASA-funded science to be freely available, and the "Open Science 101" courses come from the TOPS initiative ([NASA Open Science page, updated 15 Sep 2026](https://science.nasa.gov/open-science/)).
- **Problems / pain points:**
  - The Open Science page no longer mentions TOPS by name (as of Sep 2026). Its status is unverified and it may have wound down.
  - SDMC30 says that "while some divisions have created a single point of entry, others have a multitude of entry points" ([SMD strategy](https://assets.science.nasa.gov/content/dam/science/cds/about-us/ocsdo/reports/SMD_Data_Computing_Strategy_2025_2030.pdf)).
  - OIG audits of Geospatial Data Act compliance found that NASA met 7 of 13 responsibility areas, with 5 in progress ([NASA OIG IG-26-014](https://oig.nasa.gov/audits/nasas-compliance-with-the-geospatial-data-act-for-fiscal-year-2026/)).
- **Hackathon angle:** Build on the open INDUS-SDE embedding models (`nasa-impact/indus-sde-st-v0.2`, about 4k downloads) to make a domain-tuned RAG assistant over NASA Earth science documentation (ATBDs and user guides). Evaluate it with `nasa-smd-qa-benchmark`.
- **Credibility:** Official.
- **Sources:** as above.

---

## Part D. NOAA

### D1. NOAA budget: FY2026 request vs. enacted, and the FY2027 request

- **What it is:**
  - The FY2026 request cut NOAA to $4,515.3M (−27%) from $6,182.5M.
  - It would eliminate the Office of Oceanic and Atmospheric Research (OAR, $0, −100%) including "the Climate Research Program, weather and ocean labs, cooperative institutes, National Sea Grant," and would eliminate IOOS ([AGU The Bridge, 8 Aug 2025](https://thebridge.agu.org/2025/08/08/appropriations-update-nasa-noaa-and-nsf/)).
  - Enacted FY2026: NOAA $6.171B ([SpacePolicyOnline, Jan 2026](https://spacepolicyonline.com/news/final-fy2026-nasa-noaa-appropriations-bill-clears-senate-white-house-is-next/)). The Senate "explicitly rejects the Administration's proposal to eliminate OAR" and voiced "concern about NWS staffing cuts."
- **Problems / pain points:**
  - Cooperative institutes and labs that produce long climate records were threatened.
  - NWS staffing cuts in 2025 (see D3).
  - The FY2027 NOAA request details were **not verified** in this research.
- **Credibility:** AGU; SPO.
- **Sources:** as above.

### D2. NOAA dataset and product retirements 2025–2026 (NESDIS "Notice of Changes"): the "data rescue" list

- **What it is:** NESDIS formally posts proposed product changes and retirements under the 2006 NOAA Partnership Policy, with 30-day comment windows.
- **2025 notices** (list page: [NESDIS 2025 Notice of Changes](https://www.nesdis.noaa.gov/about/documents-reports/notice-of-changes/2025-notice-of-changes)):
  - **Billion-Dollar Weather and Climate Disasters** "will be retired, with no updates…" The NCEI archive (1980–2024) remains online, citable as "NCEI U.S. Billion-Dollar Weather and Climate Disasters (2025), DOI 10.25921/stkw-7w73" ([NCEI billions](https://www.ncei.noaa.gov/access/billions/)). Climate Central continues the tally "with the same methodology and lead scientist" ([Data Index terminations tracker, updated 5 Oct 2026](https://dataindex.us/terminations-tracker)).
  - **International Satellite Cloud Climatology Project (ISCCP) H-Series Climate Data Record:** "will no longer be updated."
  - **POES (NOAA-15, -18, -19):** "NOAA will end delivery of all data from the POES constellation... [after June 16, 2025]." NOAA-18 was decommissioned 6 Jun 2025. This ends the AVHRR/HIRS/AMSU heritage stream that dates to the 1970s and 1980s.
  - **AVHRR Pathfinder SST** discontinued, with no updates beyond 31 Dec 2023; the Coral Reef Temperature Anomaly Database (CoRTAD) is affected.
  - **Manual Dvorak tropical cyclone intensity estimates** in the South Indian and South Atlantic oceans are no longer produced by the Satellite Analysis Branch.
  - **HURSAT** (hurricane satellite record): irregular updates.
  - **nClimGrid-Daily:** duplicative access point decommissioned.
  - International Ocean Atlas Series webpage (retired 30 Jun 2025), Flower Garden Banks Map Viewer, NOAA Observing System Council site, and the "Data in the Classroom" website.
- **2026 notices** ([NESDIS Notice of Changes](https://www.nesdis.noaa.gov/about/documents-reports/notice-of-changes), accessed 2026-10-24):
  - **S-NPP data cessation 2 Nov 2026, 13:00 UTC.** ATMS, CERES, OMPS Nadir, OMPS Limb and VIIRS data stop, and direct broadcast is disabled. CrIS's "End of Operational Use occurred on December 23, 2025." "All users should transition to using NOAA-21 (Primary) and NOAA-20 (Secondary)" ([NESDIS notice](https://www.nesdis.noaa.gov/news/cessation-of-suomi-national-polar-orbiting-partnership-s-npp-data-users-onafter-november-2-2026)).
  - **Retirement of the legacy GOES-R ABI Rainfall Rate/QPE product** on 2 Nov 2026, replaced by the "Enterprise" Rainfall Rate product; comments were due 1 Oct 2026 ([NESDIS notice](https://www.nesdis.noaa.gov/news/retirement-of-goes-r-rainfall-ratequantitative-precipitation-estimation-grrqpe)).
  - **High Definition Geomagnetic Model (HDGM, HDGM-RT)** "will no longer be produced by NESDIS." It is privatised: CU Boulder/CIRES licensed it to Monarch Magnetics, and NOAA stops providing it no earlier than 25 Sep 2026 ([NESDIS notice](https://www.nesdis.noaa.gov/news/high-definition-geomagnetic-model-hdgm-and-high-definition-geomagnetic-model-real-time-hdgm-rt-will-no-longer-be-produced-nesdis)). HDGM is used for directional drilling and navigation.
  - **Storm Events Database** location change.
  - **goes-r.gov website retired** 30 Sep 2026.
- **Problems / pain points:**
  - Users of the retired products must find successors or substitute products.
  - Climate-record continuity breaks (ISCCP, Pathfinder SST, POES).
  - Products are moving behind private licences (HDGM).
  - Tools are being removed even when the underlying data stays. The Data Rescue Project notes that "many data tools have been targeted, while the underlying data remain accessible... the deprecation of analysis tools reduced the utility and interpretability of the data" ([DRP, 18 Aug 2026](https://www.datarescueproject.org/data-loss-report/)).
- **How they're trying to solve it:** Volunteer and NGO data rescue (D6); Climate Central's continuation of the Billion-Dollar database.
- **Data:** The NCEI archives that remain online; DataLumos (ICPSR) rescued copies.
- **Hackathon angle:**
  - (a) **"Successor finder"**: for any retired NOAA or NASA product (the NESDIS notices are machine-readable enough to scrape), recommend the closest replacement (Enterprise QPE, NOAA-21 VIIRS, ESA CCI Cloud for ISCCP, and so on), with a validation plot comparing old and new over an overlap period.
  - (b) **Rebuild a retired product from open satellite data.** For example, a "Billion-Dollar-style" US disaster tracker that combines FEMA declarations, NOAA Storm Events and satellite-derived footprints (FIRMS, HLS flood maps).
- **Credibility:** Official notices; the DRP and Data Index are reputable NGO trackers.
- **Sources:** as above.

### D3. NWS staffing cuts and weather-balloon (radiosonde) launch reductions (2025)

- **What it is:** In 2025, staffing cuts led several NWS offices to suspend or reduce twice-daily radiosonde launches. The Senate report voiced "concern about NWS staffing cuts" ([AGU](https://thebridge.agu.org/2025/08/08/appropriations-update-nasa-noaa-and-nsf/)).
- **Problems / pain points:** Fewer upper-air profiles degrade numerical weather prediction (NWP) initialisation, especially over data-sparse regions such as Alaska and the Great Plains. *The station-level details were not re-verified in this research, so treat specific stations as unverified.*
- **How they're trying to solve it:**
  - Commercial radio occultation (RO) data buys (D5) partially substitute for radiosondes.
  - The House added $7M for the NWS Aircraft-Based Observation Program with a "focus on water vapor data" ([AGU](https://thebridge.agu.org/2025/08/08/appropriations-update-nasa-noaa-and-nsf/)).
- **Data:** Integrated Global Radiosonde Archive (NCEI IGRA), COSMIC-2 RO (UCAR CDAAC), commercial RO (restricted licence, but NOAA buys "unlimited data rights" for some orders).
- **Hackathon angle:** A "missing balloon impact map": show where radiosonde launches were cut (from IGRA station availability over 2024–2026) and how many RO profiles fall near each gap per day (from COSMIC-2 occultation locations). This makes the substitution argument visible.
- **Credibility:** The staffing cuts are confirmed by Senate report language; station specifics are unverified here.
- **Sources:** [AGU The Bridge](https://thebridge.agu.org/2025/08/08/appropriations-update-nasa-noaa-and-nsf/).

### D4. NOAA satellite fleet status: GOES-19, JPSS (NOAA-20/21, JPSS-4), S-NPP end, SOLAR-1 (ex-SWFO-L1), QuickSounder/NEON, GeoXO, DSCOVR

- **What it is** ([NESDIS satellite pages, accessed 2026-10-24](https://www.nesdis.noaa.gov/our-satellites/currently-flying/geostationary-satellites)):
  - **GOES:** GOES-19 (GOES-U, launched 2024) is GOES East and GOES-18 is GOES West. GOES-16 and -17 are on-orbit backups.
  - **JPSS:** NOAA-21 is primary and NOAA-20 secondary. **JPSS-4/NOAA-22** has launch readiness in 2027 and carries Libera (Earth energy budget, continuing CERES) ([JPSS page](https://www.nesdis.noaa.gov/our-satellites/currently-flying/joint-polar-satellite-system)).
  - **S-NPP:** data ends 2 Nov 2026 and deorbit starts 1 Dec 2026, about 12 days of burns down to 200 km and then reentry over the South Pacific. It is "NOAA's first low Earth orbit satellite designed to support a planned end-of-life disposal" ([NESDIS, S-NPP deorbit](https://www.nesdis.noaa.gov/news/noaa-deorbit-the-suomi-npp-satellite-after-more-15-years-service)).
  - **SOLAR-1** ("Space Weather Observations at L1 to Advance Readiness-1," formerly SWFO-L1) launched with IMAP on 24 Sep 2025. Its "coronagraph is in the hands of forecasters within 30 minutes, compared to other data sources that can take up to 8 hours" ([NESDIS SOLAR-1](https://www.nesdis.noaa.gov/our-satellites/currently-flying/solar-1-launch); launch date from the [FY2027 NASA request](https://www.nasa.gov/wp-content/uploads/2026/04/fiscal-year-2027-full-budget-request.pdf)).
  - **NEON (Near Earth Orbit Network):** "will supplement and eventually replace" JPSS. **QuickSounder** (a refurbished ATMS on a small satellite, built in about 3 years) is "anticipated to launch in 2027." Series 1 will carry the new Sounder for Microwave-Based Applications (SMBA) ([NESDIS NEON](https://www.nesdis.noaa.gov/our-satellites/future-programs/near-earth-orbit-network-neon)).
  - **GeoXO:** first launch planned for 2032, adding hyperspectral IR sounding ([NESDIS GeoXO](https://www.nesdis.noaa.gov/our-satellites/future-programs/geostationary-extended-observations-geoxo)).
  - **DSCOVR** (launched 2015) has an aging inertial measurement unit (MIMU) and is managed with workarounds ([NESDIS DSCOVR](https://www.nesdis.noaa.gov/our-satellites/currently-flying/dscovr-deep-space-climate-observatory)).
- **Problems / pain points:**
  - The S-NPP shutdown removes the third VIIRS/CrIS/ATMS/OMPS and the second operating OMPS-Limb. Polar sounding redundancy drops until JPSS-4 (2027).
  - LEO satellites supply "more than 80 percent of the numerical weather prediction model data used for 3 to 7 day forecasts" (NEON page). Gaps are costly.
  - GOES-R-series aging until GeoXO in 2032.
- **Data:** NOAA Open Data Dissemination (NODD) on AWS, Google and Azure buckets: GOES-16/18/19 ABI/GLM, JPSS VIIRS/CrIS/ATMS. Free.
- **Off-the-shelf tech:** `goes2go`, Satpy, `s3fs`, NOAA NODD buckets, the SWPC JSON APIs (cross-slice: space weather).
- **Hackathon angle:**
  - (a) GOES-19 ABI plus GLM lightning nowcasting of convective initiation (a 0–1 h ML nowcast, a classic problem).
  - (b) A "polar-orbiter coverage gap" visualiser after S-NPP ends.
  - (c) SOLAR-1 coronagraph CME early-warning (cross-slice).
- **Credibility:** Official.
- **Sources:** as above.

### D5. NOAA Commercial Data Program: 10-year Space-Based Environmental Monitoring (SBEM) IDIQ with 14 vendors (Sep 2026), radio occultation buys, GNSS-R winds, on-orbit processing

- **What it is:** Under the Weather Act (P.L. 115-25) and PROSWIFT (P.L. 116-181), NOAA buys commercial weather and space-weather data.
  - **SBEM IDIQ:** effective 1 Sep 2026 to 31 Aug 2036 under the ProTech 2.0 vehicle ($8B shared ceiling). It starts with "14 industry partners to acquire data across seven categories" ([NOAA, Sep 2026](https://www.noaa.gov/news-release/noaa-expands-use-of-commercial-satellite-data-to-enhance-weather-forecasting)):
    - GNSS-RO: Spire, PlanetiQ, Ethereal Space, Precursor SPC, Tomorrow.io
    - GNSS-R: Spire, Tomorrow.io, Muon Space
    - Microwave sounders (traditional and hyperspectral): Spire, Tomorrow.io, BAE Systems, Weather Stream (Orbital Micro Systems)
    - Multispectral imagery for weather, low-light and wildfire: Ethereal, Tomorrow.io, Muon, Hydrosat, Tropical Weather Analytics
    - **Thermospheric neutral density for satellite orbit prediction: Spire, PlanetiQ, Ethereal and SpaceX** (cross-slice: SpaceX/Starlink drag data)
    - Active sensors (scatterometry, altimetry, SAR, K/Ka/Ku radar): Tomorrow.io, Care Weather, ICEYE US, Umbra
    - Infrared sounders: "No vendors at this time"
  - **Task Order 1** (18 Sep 2026): $67.05M over 2 years for 10,000 near-real-time GNSS-RO profiles/day plus 500 TEC measurements/day. Spire gets $33.2M for 5,300 profiles/day, PlanetiQ $28.4M for 4,200 profiles/day plus 500 TEC tracks, and Ethereal $5.5M for 500 profiles/day. Deliveries run 1 Dec 2026 to 1 Dec 2028 ([NESDIS, Sep 2026](https://www.nesdis.noaa.gov/news/noaa-announces-new-awards-totaling-67m-purchase-operational-commercial-data-enhance-weather-forecasts-and-space-weather-monitoring)).
  - A bridge buy (RODB-2 DO-6, 13 Aug 2026) of $6.4M covered 18 Sep to 1 Dec 2026 "with unlimited data rights" ([NESDIS, Aug 2026](https://www.nesdis.noaa.gov/news/noaa-nesdis-commercial-data-program-announces-64-million-contract-awards-support-weather-forecasting-and-space-weather)).
  - A GNSS-R ocean surface winds pilot (2024–2025) "confirmed the commercial sector's capability to reliably deliver GNSS-R observations" ([NESDIS, Oct 2026](https://www.nesdis.noaa.gov/news/noaa-releases-global-navigation-satellite-system-reflectometry-gnss-r-ocean-surface-winds-executive-summary-report)).
  - **On-orbit processing CRADA:** NOAA and Cowboy Space Corporation (San Carlos, CA; CEO Baiju Bhatt) will test processing VIIRS data in orbit on the Reason-2 satellite (launch 2027) to cut latency and downlink. NOAA provides "an existing open-source SI model and historical raw satellite data from its Visible Infrared Imaging Radiometer Suite." Bhatt: "Every mission we fly is a step toward data centers in orbit" ([NESDIS, Oct 2026](https://www.nesdis.noaa.gov/news/noaa-and-cowboy-space-corporation-test-faster-satellite-data-processing)).
- **Problems / pain points:**
  - Data rights: commercial data often cannot be redistributed, so the public may not see it.
  - Quality and calibration of commercial data must be shown before NWP assimilation.
  - Raw downlink volume and latency are the reason for the on-orbit processing test.
- **Data:** COSMIC-2 open RO (UCAR CDAAC); commercial RO via NOAA (limited public access); NOAA NODD for VIIRS raw (RDR) and SDR data.
- **Off-the-shelf tech:** GNSS-RO processing (UCAR), ROPP, ML emulators for VIIRS L1→L2 (the "SI model" NOAA would ship to orbit).
- **Hackathon angle:**
  - (a) A **"what to downlink" onboard triage model**: train a tiny model on VIIRS granules to flag the 5% of scenes with fire, storm or ash, so only those are sent at full resolution. This bridges NOAA's real CRADA problem with the orbital-compute theme (cross-slice).
  - (b) A **RO profile value map**: where do RO profiles add the most information compared with radiosondes?
- **Credibility:** Official.
- **Sources:** as above.

### D6. NOAA climate communication and assessment shutdowns: climate.gov, NCA5 amendment, the Arctic Report Card; plus data rescue NGOs

- **What it is:**
  - **climate.gov** now 302-redirects to noaa.gov/climate with the notice: "In compliance with Executive Order 14303 ('Restoring Gold Standard Science')... you have been redirected to NOAA.gov. Future research products previously housed under Climate.gov will be available at NOAA.gov/climate" ([noaa.gov/climate](https://www.noaa.gov/climate), accessed 2026-10-24).
  - The same page lists a "**Proposed Amendment to the Fifth National Climate Assessment (NCA5) - White House OSTP & USGCRP (August 2026)**."
  - **NOAA ended support for the Arctic Report Card**, published annually since 2006: "coordination of the 2026 Arctic Report Card will not be facilitated through NOAA" ([Data Index tracker](https://dataindex.us/terminations-tracker)).
  - **NSIDC Sea Ice Today:** "As of October 2025, non-renewed funding resulted in several Sea Ice Today tools and services to be suspended or reduced." Monthly posts restarted in Sep 2026 with funding from the Climate Science and Communication Fund (Surge Climate Talent). Mid-month posts, the sea ice analysis tool, sea ice volume and the extent comparison tool are discontinued ([NSIDC Sea Ice Today](https://nsidc.org/sea-ice-today)). *The DMSP SSMIS data cut-off story (DoD, 2025) was not re-verified here.*
  - Also cut: the FEMA future-risk tool (rebuilt by volunteers) and the NOAA Research & Development Database (sunset) ([Data Index tracker](https://dataindex.us/terminations-tracker)).
- **Data rescue actors:**
  - **Data Rescue Project (DRP):** deposits rescued datasets in ICPSR DataLumos. It received the 2026 ALA "Documents to the People" award and is moving from a spreadsheet to a Baserow tracker.
  - **Christopher Marcum's report** "The Integrity of Public Access to Federal Data" ([Zenodo DOI 10.5281/zenodo.19556076](https://www.doi.org/10.5281/zenodo.19556076)) estimates "approximately 3,000–4,000 datasets have been removed from public access" ([DRP, 18 Aug 2026](https://www.datarescueproject.org/data-loss-report/)).
  - **Data Index:** "Federal Data Terminations Tracker," last updated 5 Oct 2026 ([dataindex.us](https://dataindex.us/terminations-tracker)).
  - **Coalition for Resilient Research Data Infrastructure (CRRDI)**, a Center for Open Science draft strategic plan.
- **Problems / pain points:**
  - Nobody knows the full inventory of what was removed ("an impossible question to answer").
  - Rescued copies lack metadata and provenance.
  - The tools that make data usable are lost even when files survive.
- **Hackathon angle:**
  - (a) An **"Earth data provenance checker"**: given a rescued file (DataLumos or Zenodo), verify it against the original checksums and metadata (CMR, NCEI ISO metadata and the Wayback Machine) and produce a trust score.
  - (b) **Rebuild a lost tool** on top of surviving data, for example a Sea-Ice-Today-style comparison tool from the NSIDC Sea Ice Index plus AMSR2.
- **Credibility:** Official pages and reputable NGO trackers.
- **Sources:** as above.

---

## Part E. USGS: Landsat, EROS and the commercialization turn

### E1. Landsat 8/9 operations, Landsat 10 (2031, 26 bands) and the "phased transition to a commercial solution"

- **What it is:** Landsat has run since 1972, "the longest continuous record of changes in Earth's surface as seen from space," and is free to users ([FY2027 full request, ES-22](https://www.nasa.gov/wp-content/uploads/2026/04/fiscal-year-2027-full-budget-request.pdf)).
  - Landsat 8 (2013) and Landsat 9 (2021) operate now.
  - The next mission, now called **Landsat 10** (formerly Landsat Next), "is planned to launch in 2031" with "26 spectral bands, 15 more than either Landsat 8 or 9," at 20 m resolution for some bands ([USGS, Oct 2026](https://www.usgs.gov/landsat-missions/news/landsat-science-team-focuses-advanced-satellite-technology); [USGS HAB article](https://www.usgs.gov/landsat-missions/news/landsat-science-team-landsat-10-improve-harmful-algal-bloom-monitoring)).
  - The 2026–2030 Landsat Science Team met at EROS in May 2026.
- **Problems / pain points:**
  - **Commercialization.** The FY2027 request funds "one final government satellite for the Landsat program while NASA and USGS concurrently work with industry to support a phased transition to a commercial solution," based on a "Landsat Mission Alternatives Assessment Team" finding that "significant progress has been made in commercial Earth observation capabilities." In parallel, "initial work will address technical remote sensing challenges and limitations in current commercial capabilities." The SLI instrument provider is Raytheon (LandIS); the host spacecraft provider is "TBD" ([FY2027 full request, ES-9 and ES-17](https://www.nasa.gov/wp-content/uploads/2026/04/fiscal-year-2027-full-budget-request.pdf)).
  - The FY2026 request had cut Landsat Next and asked for a smaller design. The Senate gave $183M and urged keeping "the current three-satellite architecture" ([AGU](https://thebridge.agu.org/2025/08/08/appropriations-update-nasa-noaa-and-nsf/)).
  - Key open questions: will data stay free? Will commercial data keep Landsat's calibration and its 54-year consistency?
  - **Gap risk.** Landsat 8 is 13 years old and Landsat 10 is not until 2031. Landsat 7 was retired (2025–2026; *exact decommission date not verified here*).
  - **Science user needs.** Landsat 8/9's "limited spectral coverage makes it difficult to distinguish cyanobacteria from other phytoplankton" (harmful algal blooms cost "up to $100 million annually in the United States"). Tree-mortality tracking: "we don't have a robust solution for precisely tracking mortality" (non-photosynthetic vegetation). Field-scale ET for irrigation is needed under "increasing water stress" ([USGS, Oct 2026](https://www.usgs.gov/landsat-missions/news/landsat-science-team-focuses-advanced-satellite-technology)).
  - **Archive quality.** "Several Landsat 2 and Landsat 3 MSS Level-1 products were recently reprocessed to correct brightness value errors that were initially discovered in early 2025" ([Latest in Landsat, Oct 2026](https://www.usgs.gov/latest-landsat-newsletter/latest-landsat-october-2026)).
  - **Access changes.** USGS is discontinuing all Landsat RSS feeds in favour of Amazon SNS topics; SNS topics for calibration files are coming in Dec 2026.
- **How they're trying to solve it:** The commercialization roadmap; Landsat Collection 2 in the "Landsat Commercial Cloud" (AWS, since 2020); HLS with Sentinel-2; machine-learning harmonization with Sentinel-2 and Sentinel-3 for water quality (the STREAM tool).
- **Data:**
  - The Landsat archive (USGS EROS) runs from 1972. Collection 2 Level-1 and Level-2 (surface reflectance and surface temperature) are free via EarthExplorer, the M2M API and AWS `s3://usgs-landsat` (requester-pays).
  - Landsat 10 will have 26 bands.
- **Off-the-shelf tech:** `pystac-client` with the USGS LandsatLook STAC, `landsatxplore`, OpenET (Landsat-based ET), Google Earth Engine, Microsoft Planetary Computer (Landsat C2).
- **Hackathon angle:**
  - (a) A **"Landsat-or-commercial?" benchmark**: for one region, compare Landsat C2 surface reflectance against a free commercial sample (Planet NICFI tropics, or an open Satellogic/Umbra sample) on calibration stability. This shows why continuity matters.
  - (b) **50-year "change story" generator**: pick any place and auto-produce an annotated 1972–2026 timelapse with detected change events. Landsat's 54-year record is the selling point.
  - (c) **Harmful algal bloom (HAB) early warning** for a lake, from Landsat/HLS plus Sentinel-3 OLCI.
- **Credibility:** Official.
- **Sources:** as above.

---

## Part F. Challenge problem lists

### F1. NASA International Space Apps Challenge: 2024, 2025, 2026 (full list in Section 3 table)

- **What it is:** NASA's annual global hackathon. Challenges are written by NASA subject-matter experts and point to specific datasets.
  - **2024:** 93,520 registered participants, 485 events in 163 countries and territories, 9,996 submissions; winners announced 16 Jan 2025 ([NASA, 16 Jan 2025](https://www.nasa.gov/learning-resources/stem-engagement-at-nasa/nasa-international-space-apps-challenge-announces-2024-global-winners/)).
  - **2025:** held 4–5 Oct 2025 with 19 challenge pages (18 plus "Create Your Own"). It drew more than 114,000 participants at 551 local events in 167 countries and territories, with more than 11,500 submissions; winners announced 18 Dec 2025 ([NASA, 18 Dec 2025](https://www.nasa.gov/learning-resources/stem-engagement-at-nasa/nasa-announces-2025-international-space-apps-challenge-global-winners/); [Earthdata event page](https://www.earthdata.nasa.gov/events/2025-nasa-space-apps-challenge)).
  - **2026:** runs **14–15 Nov 2026** with 14 challenges. Summaries were released 17 Sep 2026, and the full statements with datasets are due **28 Oct 2026** ([Space Apps FAQ](https://www.spaceappschallenge.org/resources/participant-faqs/); [astrobiology.com, 4 Sep 2026](https://astrobiology.com/2026/09/04/registration-is-now-open-for-the-2026-nasa-space-apps-challenge/)).
- **How the list was compiled:** Challenge titles, summaries and resource lists were pulled from the public Space Apps site (its GraphQL backend at api.spaceappschallenge.org) on 2026-10-24. The site reports 86 challenge pages: 32 in 2023, 21 in 2024, 19 in 2025 and 14 in 2026.
- **Why it matters for us:** These are NASA-authored problem statements with curated datasets. Several 2026 challenges were not yet public when the 2025 and 2024 hackathons ran. Highly relevant ones:
  - "Harmonization of MODIS and VIIRS Hot Spots" (2026)
  - "Be An Earth System Trend Detective!" (2026)
  - "Dancing with the SARs" (NISAR, 2026)
  - "Field Shift" (2026)
  - "Will It Rain On My Parade?" (2025)
  - "From EarthData to Action" (TEMPO, 2025)
  - "Through the Radar Looking Glass" (SAR, 2025)
  - "BloomWatch" (2025)
  - "Sharks from Space" (PACE/SWOT, 2025)
  - "Landsat Reflectance Data: On the Fly" (2024)
- **2025 Global Winners** ([NASA, 18 Dec 2025](https://www.nasa.gov/learning-resources/stem-engagement-at-nasa/nasa-announces-2025-international-space-apps-challenge-global-winners/)):
  - Best Use of Science: SpaceGenes+ (Germany), Space Biology Knowledge Engine, a radiation and microgravity molecular-health dashboard.
  - Best Use of Data: Resonant Exoplanets (US), an AI exoplanet and biosignature scanner.
  - Best Use of Technology: Twisters (Mexico), "Will It Rain on My Parade?", the SkySense hyperlocal forecast and activity-window app.
  - Galactic Impact: Astro Sweepers (Universal Event), Commercializing LEO, an orbital-debris compliance report and risk-score platform.
  - Best Mission Concept: PureFlow (Brazil), a habitat layout tool.
  - Most Inspirational: Photonics Odyssey (India), satellite internet as national infrastructure.
  - Best Storytelling: HerCode Space, "A Solar Tale."
  - Global Connection: Gaia+LEO (US), co-design of orbital and ground data-centre networks to cut Earth energy and water use.
  - Art & Technology: Zumorroda-X (Egypt), farm mini-games.
  - Local Impact: QUEÑARIS (Peru), BloomWatch, restoring queñua forests for Arequipa's water supply using satellites, drones and AI.
- **2024 Global Winners** ([NASA, 16 Jan 2025](https://www.nasa.gov/learning-resources/stem-engagement-at-nasa/nasa-international-space-apps-challenge-announces-2024-global-winners/)):
  - Best Use of Science: WMPGang (Waterloo), NEO orrery that maps satellite risk zones using live NEO and meteor-stream data.
  - Best Use of Data: GaamaRamma (US), the Waterwise farm water tool.
  - Best Use of Technology: 42 QuakeHeroes (Brazil), a deep neural net for Apollo and InSight seismic detection.
  - Galactic Impact: NVS-knot (Kyiv), soil moisture and evapotranspiration (ET) planting-risk app.
  - Best Mission Concept: AsturExplorers (Spain), Landsat Connect for pass alerts and surface-reflectance retrieval.
  - Most Inspirational: Innovisionaries (UAE), Eco-Metropolis.
  - Best Storytelling: TerraTales (Egypt).
  - Global Connection: Asteroid Destroyer (Canada), HWO exoplanet ML map.
  - Art & Technology: Connected Earth Museum (Brazil).
  - Local Impact: Team I.O. (Brazil), GIS made easy, the G.R.O.W. wildfire project.
- **Pattern in winners:** Judges reward a concrete user (farmer, event planner, debris regulator) combined with real NASA data and a working app. That matches the Cal Hacks brief.
- **Credibility:** Official.
- **Sources:** see table in Section 3.

---

### F2. NASA Frontier Development Lab (FDL.ai): now focused on heliophysics, "Ops"-grade ML

- **What it is:** FDL USA is a public–private AI research accelerator run by Trillium Technologies with NASA and partners including Google Cloud and NVIDIA ([fdl.ai](https://fdl.ai/)). Its Earth-focused sibling is the Earth Systems Lab (eslab.ai, with ESA; cross-slice).
- **Challenge areas** (FDL pages accessed 2026-10-24):
  - **FDL 2026 ("FDL OPS 2026"): "High TRL Systems for Solar Situational Intelligence."** It focuses on the "scalability, reliability, and the model life cycle of machine learning models that transform raw solar data into actionable, real-time decisions." Named needs: "Production-Scale Pipelines: Implementing automated CI/CD for complex heliospheric datasets"; "real-time latency requirements"; "Moving beyond black-box pipelines toward interpretable, reproducible high-uptime systems that can be trusted by mission control" ([fdl.ai/fdl26](https://fdl.ai/fdl26)).
  - **HelioLab 2025** ([fdl.ai/heliolab25](https://fdl.ai/heliolab25)):
    - "Active Region Characterization and Analysis of Dynamics and Evolution." Problem statement: "Can we capture and codify the dynamic state of active regions on the Sun to inform downstream chained models?"
    - Decoding solar-wind structure: "Can we identify and understand the precursors and drivers of solar wind structures, with an aim to forecast these in advance?" (uses Parker Solar Probe data).
    - "Ionosphere-Thermosphere Digital Twin": "Can we resolve local ionospheric disturbances at a global scale?"
  - **FDL 2024** ([fdl.ai/fdl2024](https://fdl.ai/fdl2024)):
    - "Thermospheric Density Continuous Learning": "Can we enable an operational data-driven live streaming service for thermospheric density prediction?"
    - "Geoeffectiveness Continuous Learning" (the DAGGER and SHEATH models).
    - "Can we predict the full EUV spectral irradiance at Mars?"
    - SuNeRF solar-atmosphere reconstruction.
    - "Forecasting Radiation Exposure for Human Space Flight."
  - **FDL BenchLab "Solar Wind Prediction 2026":** a competition for a "Responsive Solar Wind Prediction Overlay," with operational deployment collaboration for top teams ([fdl.ai/benchlab-solar-wind-prediction-2026](https://fdl.ai/benchlab-solar-wind-prediction-2026)).
- **Problems / pain points:** Research-grade ML models seldom make it into operations (CI/CD, latency, trust, interpretability). Space-weather forecasting needs real-time, continuously updated models.
- **Hackathon angle:** A thermospheric-density "drag weather" nowcast that pairs NOAA's newly purchased neutral-density data stream (D5) with public SWPC solar-wind data, built as a small production-style service. Overlaps with the space-weather slice.
- **Credibility:** Official program pages.
- **Sources:** as above.

### F3. NASA prizes and crowdsourcing challenges, 2025–2026 (NASA Tournament Lab / CoECI, TechLeap, Centennial)

- **What it is:** NASA's prize programs, listed at [NASA Prizes, Challenges, and Crowdsourcing](https://www.nasa.gov/prizes-challenges-and-crowdsourcing/) and [CoECI](https://www.nasa.gov/directorates/stmd/prizes-challenges-crowdsourcing-program/center-of-excellence-for-collaborative-innovation-coeci/), accessed 2026-10-24.
- **Challenges relevant to space data:**
  - **NASA TechLeap Prize: Orbital Clarity Challenge.** Listed on the CoECI page as an article dated 19 Aug 2026. Another researcher reports a NASA Science announcement on 18 Sep 2026; that date is not verified here.
    - It is the sixth TechLeap prize, run with the Heliophysics Division and Flight Opportunities.
    - Problem: space weather "heats and expands Earth's outer atmosphere during intense solar activity, creating orbital drag through atmospheric density changes." It calls for "low-cost methods of measuring thermospheric density, pressure, or drag in low Earth orbit," that are "inexpensive and scalable enough to be produced in quantity and flown as hosted payloads across the commercial fleet."
    - Award: "Up to four winners may receive up to $500,000 in prizes across three phases." "NASA intends to offer each winning team a test flight at no cost" ([NASA, Orbital Clarity](https://www.nasa.gov/directorates/stmd/prizes-challenges-crowdsourcing-program/nasa-techleap-prize-orbital-clarity-challenge/)).
    - Note the convergence: NOAA buys "thermospheric neutral density for satellite orbit predictions" from Spire, PlanetiQ, Ethereal and SpaceX (D5); FDL 2024 ran thermospheric density continuous learning (F2); and the SBIR orbital debris subtopic exists (F4).
  - **NASA ORBIT Challenge 2027** (posted 28 Sep 2026). University and community-college students "work with real NASA intellectual property": ORBIT Earth builds commercial applications of NASA patents and ORBIT Space builds exploration technology. Up to $500,000 in prizes ([NASA ORBIT 2027](https://www.nasa.gov/directorates/stmd/prizes-challenges-crowdsourcing-program/center-of-excellence-for-collaborative-innovation-coeci/nasa-orbit-challenge-2027/)).
  - **Other current challenges:** the Lunar Grounding Challenge (CoECI); the "2027 Human Lander Challenge for Lunar Communications"; the Mars Space Food Systems Challenge (winners announced 24 Sep 2026); and the NASA Student Aviation Challenge on infrastructure (18 Aug 2026). These are exploration-focused, not Earth-data ([NASA prizes page](https://www.nasa.gov/prizes-challenges-and-crowdsourcing/)).
  - **Other agencies' challenges** listed by CoECI ([CoECI other-agency opportunities](https://www.nasa.gov/coeci-other-government-agency-opportunities/)):
    - A NOAA crowd challenge "to develop models for forecasting Dst that push the boundary of predictive performance, under operationally viable constraints, using the real-time solar-wind data feeds from NOAA's DSCOVR and NASA's ACE satellites." This is the historic "MagNet" challenge; its year is not verified.
    - An overhead satellite imagery challenge ("critical time-sensitive information for use in areas like disaster response, navigation, and security").
    - Reclamation's water challenges.
- **Hackathon angle:** Reuse the *Orbital Clarity* problem framing on the analysis side: "estimate thermospheric density from public satellite tracking (TLE or GP) decay rates of many LEO objects." The data is free from CelesTrak and Space-Track (cross-slice).
- **Credibility:** Official.
- **Sources:** as above.

### F4. NASA SBIR/STTR FY26–27 Broad Agency Announcement (BAA): Appendix 26B (Phase I) subtopics on data, AI and remote sensing

- **What it is:** NASA moved SBIR/STTR to a Broad Agency Announcement with rolling appendices. **Appendix 26B (SBIR Phase I)** was "Originally Issued: April 21, 2026," with "Proposals Due: May 21, 2026 by 5:00 PM ET" ([NASA FY26–27 BAA Appendix 26B-I SBIR PDF](https://www.nasa.gov/wp-content/uploads/2024/01/nasa-2026-2027-sbir-sttr-baa-appendix-26b-i-sbir.pdf)). The subtopics are numbered by the new NASA technology-area scheme (AERO, GO, ENABLE, EXPAND, INSTALG, COSMO, SPWX, INSITU and others). They are listed in Section 3b.
- **Problem statements quoted from the subtopics:**
  - **INSTALG.3 Large-Scale Computing and Computational AI** (previously S17.01; ARC/GSFC):
    - "One of the largest challenges facing the HPC community today is the tremendous amount of refactoring that is typically required of existing large scale applications."
    - "Current and future NASA science requires at least 100x more powerful supercomputers and 1,000x higher application parallelism in 10 years without an increased energy demand... technologies for high fidelity computational simulation and data analytics are distinct and interfacing between tools is inefficient."
    - It mentions LLMs and small language models (SLMs) for HPC code.
  - **ENABLE.2 High Performance Onboard Computing** (JPL): "an increased need for autonomy, as well as onboard data reduction where sensor bandwidth exceeds downlink bandwidth."
  - **EXPAND.2 Orbital Debris Tracking** (ARC/GSFC): "develop a (primarily) ground-based tracking solution that can maintain custody of a piece of small debris from the time it rises above the horizon to the time it descends below the horizon... to support laser removal of orbital debris." It notes "More than 23,000 pieces of orbital debris are larger than a softball."
  - **INSTALG.5 Remote-Sensing Technologies** (GSFC/JPL/LaRC): active microwave, passive microwave and LiDAR. It cites "common technical challenges, including calibration stability, environmental robustness, long-term reliability" for "SmallSats, CubeSats, constellations."
  - Also relevant: COSMO.3 "AI for Rapid Development of Space Precision Components"; EXPAND.3 "Autonomous Onboard Health Management for Small Spacecraft and Distributed Systems"; INSITU.1 "Fault Management Technologies for Autonomous Systems"; SPWX.2 "Sensors and Instrumentation for Space Environment Measurement."
- **Problems / pain points:** Appendix 26B has **no Earth-science data or analytics subtopic**. The data and AI needs appear only as HPC, onboard computing and instrument technology. *Other appendices (26A, STTR) were not read.*
- **Hackathon angle:** "Onboard data reduction where sensor bandwidth exceeds downlink bandwidth" (ENABLE.2) is a literal NASA problem statement. A demo could compress or triage a hyperspectral cube (EMIT or PACE) on-device, keeping only anomalous pixels. Pairs with the NOAA–Cowboy Space CRADA (D5).
- **Credibility:** Official solicitation.
- **Sources:** as above.

### F5. Conferences: what the community says the problems are (IGARSS 2026)

- **What it is:** IGARSS 2026 was held in Washington, D.C., 9–14 Aug 2026. Theme: "**the Future of Earth Observations**... future Earth observation technologies for solving grand challenges" ([IGARSS 2026](https://2026.ieeeigarss.org/)).
- **Plenary** ([IGARSS 2026 plenary](https://2026.ieeeigarss.org/plenary_session.php)):
  - Tomorrow.io co-founder Rei Goffer: "Breaking the Data Barrier — How Commercial Weather Satellites Will Change Everything." Tomorrow.io claims "the world's largest commercial constellation of weather satellites" and is "the only private company to ever deploy spaceborne weather radars."
  - NASA Earth Science Division Director Karen St. Germain: "Accelerating Earth Science Discovery."
  - NOAA NESDIS's Timothy Walsh: "Designing for Decades: Strategic Agility and Scaling NOAA's Cloud-Native Architecture for Operational Environmental Intelligence."
- **Community-contributed themes stating problems** ([IGARSS 2026 CCTs](https://2026.ieeeigarss.org/community_contributed_themes.php)):
  - CCT.2: "the growing data scale also introduces significant challenges in terms of efficient storage, processing, and analysis... computational demands of these models often exceed the capabilities of conventional desktop systems," and calls for "edge computing, in-orbit AI."
  - CCT.4 (geo-foundation models for disaster response): "geoAI models demand extensive amount of annotated data and suffering limited spatio-temporal transferability... time-sensitive activities like humanitarian emergency responses require models that are capable of generalizing across different locations and time frames efficiently with minimal adaptation."
  - CCT.3: benchmark datasets lacking coverage of "low-sample, high-value scarce objects."
  - CCT.5: "geospatial chain of thought reasoning... graph foundation models... PDE foundation models."
- **Not covered:** AGU25 and AMS 2026 programs could not be fetched (Cloudflare 403); see Leads not followed.
- **Hackathon angle:** "Few-shot disaster mapping in a new country within hours" (CCT.4) is a clean, judge-friendly problem. Use Prithvi-EO-2.0 or a SAR foundation model with fewer than 50 labels.
- **Credibility:** Official conference pages.
- **Sources:** as above.

---

## Part G. Office of Space Commerce (OSC), brief: commercial remote-sensing licensing and space-economy data

- **What it is:** OSC sits within NOAA/Commerce. Its **Commercial Remote Sensing Regulatory Affairs (CRSRA)** division "licenses private operators of remote sensing space systems and monitors compliance," under the National and Commercial Space Programs Act (51 U.S.C. § 60101 et seq.) and **15 C.F.R. 960** ([OSC CRSRA](https://space.commerce.gov/regulations/commercial-remote-sensing-regulatory-affairs/)).
  - Compliance duties include "Assuring compliance with the Kyl-Bingaman Amendment for collection of imagery of Israel."
  - Licensees must give "immediate notification of any deviations from orbit," report "proposed significant or substantial foreign agreements," and file annual certifications due 15 Oct ([OSC Compliance and Monitoring](https://space.commerce.gov/regulations/commercial-remote-sensing-regulatory-affairs/compliance-and-monitoring/)).
  - The last listed listening session on licensing was in July 2024.
- **Budget:** FY2026 enacted $55M (FY2025: $65M; request: $10M). Most of the fight was over TraCSS. A Dec 18, 2025 executive order changed SPD-3's "free of direct user fees" basic SSA language (cross-slice) ([SpacePolicyOnline, Jan 2026](https://spacepolicyonline.com/news/final-fy2026-nasa-noaa-appropriations-bill-clears-senate-white-house-is-next/)).
- **Other OSC activity (2026):**
  - **"U.S. Space Economy Measurement Metrics" study.** OSC "requires a deeper, evidence-based understanding of the ecosystem," seeking "a government-verifiable baseline of metrics" for "recurring U.S. Government empirical reporting beginning in FY2027." An updated RFQ was posted on SAM.gov on 9 Oct 2026 as a small-business set-aside ([OSC](https://space.commerce.gov/osc-seeks-proposals-for-u-s-space-economy-measurement-metrics-study/)).
  - Space Commerce Certification; a Space Industry Technical Standards Online Database; a "Dataset for Conjunction Assessment Verification"; and a $5M "Project Constellation" initiative ([space.commerce.gov](https://space.commerce.gov/)).
- **Problems / pain points:**
  - Licensing conditions and timelines are opaque to newcomers.
  - The US lacks a trusted, recurring measure of the commercial space economy (OSC's own stated need).
- **Hackathon angle:** A "**space economy pulse**" dashboard built from public data: launch logs, FCC/ITU filings, CelesTrak object counts, SAM.gov awards (for example NOAA's SBEM IDIQ and NASA CSDA) and company EO catalog sizes. It answers OSC's metrics question with live data. The space-data link is moderate.
- **Credibility:** Official.
- **Sources:** as above.

---

## Section 3. Tables: NASA Space Apps challenges (2024–2026) and SBIR subtopics

### 3a. Space Apps challenges

The one-line problem statement is the "Your challenge is…" sentence from the official summary. The data column lists the first NASA resources linked on each challenge's Resources tab. The 2026 resource tabs are not yet published; full statements are due 28 Oct 2026.

| Year | Challenge | One-line problem statement | NASA division | Data / resources pointed to |
|---|---|---|---|---|
| 2024 | [Beyond Sunlight: An Aquatic Chemosynthetic World](https://www.spaceappschallenge.org/nasa-space-apps-2024/challenges/beyond-sunlight-an-aquatic-chemosynthetic-world/) | Your challenge is to design such a world and its diverse ecosystem, pushing the boundaries of astrobiology beyond traditional Earth-like conditions. |  | Ocean Worlds: Water in the Solar System and Beyond; Ocean World Resources; Network for Ocean Worlds (NOW) |
| 2024 | [Chronicles of Exoplanet Exploration](https://www.spaceappschallenge.org/nasa-space-apps-2024/challenges/chronicles-of-exoplanet-exploration/) | Your challenge is to develop engaging and accessible learning materials that leverage creativity to enlighten students about the wonders of exoplanets. |  | NASA Exoplanets; "Eyes on Exoplanets"; Jet Propulsion Laboratory STEM Lessons; NASA Exoplanet Resource Guide; NASA Exoplanet Archive |
| 2024 | [Community Mapping](https://www.spaceappschallenge.org/nasa-space-apps-2024/challenges/community-mapping/) | Your challenge is to create a map that incorporates open science data to explore how an issue in your community is shaped by the surrounding physical geography. |  | NASA Earthdata GIS (EGIS); NASA Environmental Justice Data Search Interface; NASA Worldview; Socioeconomic Data and Applications Center (SEDAC) |
| 2024 | [Create Your Own Challenge](https://www.spaceappschallenge.org/nasa-space-apps-2024/challenges/create-your-own-challenge/) | Participants are invited to create their own challenge to tackle during the hackathon. However, please note that while some Local Events may offer awards for "Create Your Own Challenge" projects, this challenge is not el |  | — |
| 2024 | [Create an Orrery Web App that Displays Near-Earth Objects](https://www.spaceappschallenge.org/nasa-space-apps-2024/challenges/create-an-orrery-web-app-that-displays-near-earth-objects/) | Your challenge is to create an interactive orrery web app that is embedded in a webpage and displays celestial bodies such as planets, Near-Earth Asteroids, Near-Earth Comets, and Potentially Hazardous Asteroids. |  | Approximate Positions of the Planets; Small-Body Database Query; Near-Earth Comets - Orbital Elements API / NASA Open Data Portal; GitHub - nasa/mission-viz: Web-based Space Mission Visualization Software; Elliptical Orbit Simulator; nasa.github.io/mission-viz/RMarkdown/ontology_based_orrery_generated_from_R_code.html |
| 2024 | [Exosky!](https://www.spaceappschallenge.org/nasa-space-apps-2024/challenges/exosky/) | Your challenge is to develop an app or interface for students that allows them to choose an exoplanet and then either display an interactive star chart or export a high-quality image for printing or viewing on a computer or virtual reality display, where they can draw and name constellations. |  | NASA Exoplanet Archive; Gaia DR3 Catalog (A Precise Three-Dimensional Database of About One Billion Stars Throughout Our Galaxy and Beyond); Deep Star Maps 2020 |
| 2024 | [GLOBE Protocol Games](https://www.spaceappschallenge.org/nasa-space-apps-2024/challenges/globe-protocol-games/) | Your challenge is to create a game that integrates Global Learning and Observations to Benefit the Environment (GLOBE) Program protocols to help players understand the world around them, develop awareness of one or more local or global environmental topics (e. |  | The GLOBE Program Website; Steps in the Scientific Process; GLOBE Visualization System; GLOBE Advanced Data Access Tool |
| 2024 | [Galactic Games: Fun in a Microgravity Environment!](https://www.spaceappschallenge.org/nasa-space-apps-2024/challenges/galactic-games-fun-in-a-microgravity-environment/) | Your task is to design a game that leverages the unique challenges and opportunities of a microgravity environment to entertain and contribute to the overall well-being and cohesion of astronaut crews, enhancing their resilience and adaptability in the extraterrestrial frontier. |  | Living and Working in Space; Experiments to Unlock How Human Bodies React to Long Space Journeys; What is Microgravity?; The Human Body in Space - NASA; 7 Sports Astronauts Love Without Gravity |
| 2024 | [Human Development & the Environment](https://www.spaceappschallenge.org/nasa-space-apps-2024/challenges/human-development-the-environment/) | The United Nations Sustainable Development Goals are a series of targets designed to promote human development and protect the environment. |  | — |
| 2024 | [Imagine our Connected Earth](https://www.spaceappschallenge.org/nasa-space-apps-2024/challenges/imagine-our-connected-earth/) | Your challenge is to devise an audio-visual interactive product (e. |  | EIC Gallery; Data Pathfinders; Images of Change; NASA Explores Earth’s Interconnected Systems; What NASA Knows from Decades of Earth System Observations; The Earth Information Center |
| 2024 | [Landsat Reflectance Data: On the Fly and at Your Fingertips](https://www.spaceappschallenge.org/nasa-space-apps-2024/challenges/landsat-reflectance-data-on-the-fly-and-at-your-fingertips/) | Your challenge is to develop a web-based application that supports the comparison of ground-based observations with Landsat data by allowing users to define a target location, receive notifications when Landsat is to pass over that location, and then access and display the corresponding Landsat SR data. |  | Landsat 9; Landsat 8; Harmonized Landsat Sentinel-2; Landsat Collection 2 Generation Timeline; Landsat Acquisition Tool; Landsat Shapefiles and Keyhole Markup Language (KML) Files |
| 2024 | [Leveraging Earth Observation Data for Informed Agricultural Decision-Making](https://www.spaceappschallenge.org/nasa-space-apps-2024/challenges/leveraging-earth-observation-data-for-informed-agricultural-decision-making/) | Your challenge is to design a tool that empowers farmers to easily explore, analyze, and utilize NASA datasets to address these water-related concerns and improve their farming practices. |  | Agriculture and Water Management Pathfinder; Floods Data Pathfinder; Extreme Heat Data Pathfinder; NASA Acres; NASA Harvest; Application for Extracting and Exploring Analysis Ready Samples (AppEEARS) |
| 2024 | [Navigator for the Habitable Worlds Observatory (HWO): Mapping the Characterizable Exoplanets in our Galaxy](https://www.spaceappschallenge.org/nasa-space-apps-2024/challenges/navigator-for-the-habitable-worlds-observatory-hwo-mapping-the-characterizable-exoplanets-in-our-galaxy/) | Your challenge is to develop an app that enables users to visualize the observational paths across our galaxy to the known exoplanets in the solar neighborhood as a function of their potential for characterization by HWO. |  | NASA Exoplanet Archive; 3D Solar System Visualizer; Probing the Capability of Future Direct-imaging Missions to Spectrally Constrain the Frequency of Earth-like Planets |
| 2024 | [PACE in the Classroom](https://www.spaceappschallenge.org/nasa-space-apps-2024/challenges/pace-in-the-classroom/) | Your challenge is to create a digestible set of materials that can be used in classrooms across the world to help students understand the data and information that PACE is gathering, and improve ocean literacy worldwide. |  | NASA PACE; NASA PACE: Access PACE Data; NASA PACE: Get Ready to Work with PACE Data; Ocean Exploration Article; Space to Learn; NOAA Ocean Explorer |
| 2024 | [SDGs in the Classroom](https://www.spaceappschallenge.org/nasa-space-apps-2024/challenges/sdgs-in-the-classroom/) | Your challenge is to develop a lesson plan that educates high school students about an SDG, and can be integrated into a science unit that may already be part of the curriculum (e. |  | Earth Observations for the Sustainable Development Goals; The Earth Observations Toolkit for Sustainable Cities and Human Settlements; NASA Earthdata Worldview; NASA Earth Observatory; NASA ARSET: Overview of SDG 15; NASA Socioeconomic Data and Applications Center (SEDAC) |
| 2024 | [Seismic Detection Across the Solar System](https://www.spaceappschallenge.org/nasa-space-apps-2024/challenges/seismic-detection-across-the-solar-system/) | Planetary seismology missions struggle with the power requirements necessary to send continuous seismic data back to Earth. But only a fraction of this data is scientifically useful! Instead of sending back all the data  |  | Space Apps 2024 Seismic Detection Data Packet; Apollo Passive Seismic Experiment Data Description; Mars InSight Seismic Data; Mars InSight Seismic Data Information Sheet |
| 2024 | [Show Us What the May 2024 Geomagnetic Storms Looked Like](https://www.spaceappschallenge.org/nasa-space-apps-2024/challenges/show-us-what-the-may-2024-geomagnetic-storms-looked-like/) | Your challenge is to use NASA data to create a visual representation (e. |  | Solar Dynamic Observatory Images; Solar Wind Magnetic Field and Plasma Data at L1; Aurorasaurus; Basic Facts About the Sun; How Scientists Around the World Track the Solar Cycle; Historic Geomagnetic Storm Dazzles |
| 2024 | [Symphony of the Stars: Harmonizing the James Webb Space Telescope in Music and Images](https://www.spaceappschallenge.org/nasa-space-apps-2024/challenges/symphony-of-the-stars-harmonizing-the-james-webb-space-telescope-in-music-and-images/) | Your challenge is to capture the spirit of this remarkable mission by creating a collage that merges stunning JWST visuals with a compelling musical backdrop, encapsulating the sense of discovery and cosmic awe that the telescope inspires in a way that appeals to people of all ages. |  | Webb Space Telescope; NASA Astrophysics Division; Webb Telescope Images |
| 2024 | [Tell Us a Climate Story!](https://www.spaceappschallenge.org/nasa-space-apps-2024/challenges/tell-us-a-climate-story/) | Your challenge is to use the open-source data on the U. |  | US GHG Center datasets; Global Atmospheric CO2: "OCO-2 GEOS Column CO₂ Concentrations:"; Global Annual CO2 Emissions and Removals: "OCO-2 MIP Top-down CO₂ Budgets:"; Global CO₂ Emissions: "ODIAC Fossil Fuel CO₂ Emissions:"; Global Carbon Fluxes: "MiCASA Land Carbon Flux:"; Global Methane Emissions from Wetlands: "Wetland Methane Emissions, LPJ-EOSIM Model:" |
| 2024 | [Uncover the Role of Greenhouse Gases in Your Neighborhood!](https://www.spaceappschallenge.org/nasa-space-apps-2024/challenges/uncover-the-role-of-greenhouse-gases-in-your-neighborhood/) | Your challenge is to use a combination of satellite and model-based datasets to map both human-caused and natural greenhouse gas emissions to enable better understanding of how these emissions contribute to a warmer world. |  | US GHG Center datasets; Global Atmospheric CO2: "OCO-2 GEOS Column CO₂ Concentrations:"; Global Annual CO2 Emissions and Removals: "OCO-2 MIP Top-down CO₂ Budgets:"; Global CO₂ Emissions: "ODIAC Fossil Fuel CO₂ Emissions:"; Global Carbon Fluxes: "MiCASA Land Carbon Flux:"; Global Methane Emissions from Wetlands: "Wetland Methane Emissions, LPJ-EOSIM Model:" |
| 2024 | [Visualize Space Science](https://www.spaceappschallenge.org/nasa-space-apps-2024/challenges/visualize-space-science/) | Your challenge is to create a tool that can generate informative and compelling visualizations of biological experiments performed in space. |  | Open Science Dataset, OSD-379; Open Science Dataset, OSD-665; NASA Open Science Data Repository (OSDR); Biological and Physical Sciences (BPS) Explainers; Exploring the Effects of Spaceflight on Mouse Physiology Using the Open Access NASA GeneLab Platform |
| 2025 | [A World Away: Hunting for Exoplanets with AI](https://www.spaceappschallenge.org/2025/challenges/a-world-away-hunting-for-exoplanets-with-ai/) | Your challenge is to create an AI/ML model that is trained on one or more of the open-source exoplanet datasets offered by NASA and that can analyze new data to accurately identify exoplanets. | Astrophysics Division | Kepler Objects of Interest (KOI); TESS Objects of Interest (TOI); K2 Planets and Candidates; Exoplanet Detection Using Machine Learning; Assessment of Ensemble-Based Machine Learning Algorithms for Exoplanet Identification |
| 2025 | [Animation Celebration of Terra Data!](https://www.spaceappschallenge.org/2025/challenges/animation-celebration-of-terra-data/) | Your challenge is to use data from any or all of Terra’s five instruments to create an animated product showcasing an Earth science story and emphasizing the impacts to you, your community, and/or the environment. | Earth Science Division | NASA Earthdata Worldview; Global Imagery Browse Services; NASA Earth Observatory; Terra Animations from NASA Jet Propulsion Laboratory's (JPL) Photojournal; JPL ASTER Data Hub; Prediction Of Worldwide Energy Resources (POWER) Project |
| 2025 | [BloomWatch: An Earth Observation Application for Global Flowering Phenology](https://www.spaceappschallenge.org/2025/challenges/bloomwatch-an-earth-observation-application-for-global-flowering-phenology/) | Your challenge is to harness the power of NASA Earth observations to create a dynamic visual tool that displays and/or detects plant blooming events around the globe—just like pollinators do–and that advances solutions for monitoring, predicting, or managing vegetation. | Earth Science Division | Wildflower Bloom Observations; NASA Takes to the Air to Study Wildflowers; Example of California superblooms; California superbloom images; Comparison between two superbloom seasons I; Comparison between two superbloom seasons II |
| 2025 | [Build a Space Biology Knowledge Engine](https://www.spaceappschallenge.org/2025/challenges/build-a-space-biology-knowledge-engine/) | Your challenge is to build a dynamic dashboard that leverages artificial intelligence (AI), knowledge graphs, and/or other tools to summarize a set of NASA bioscience publications and enables users to explore the impacts and results of the experiments these publications describe. | Earth Science Division | A list of 608 full-text open-access Space Biology publications; NASA Open Science Data Repository; NASA Space Life Sciences Library; NASA Task Book |
| 2025 | [Commercializing Low Earth Orbit (LEO)](https://www.spaceappschallenge.org/2025/challenges/commercializing-low-earth-orbit-leo/) | Your challenge is to conceptualize and design a scalable, sustainable, business model, accompanied by a prototype, that explores the unique opportunities LEO offers while addressing the complexities of operating in space. | Joint Agency Satellite Division | NASA Orbital Debris Program Office (ODPO) Resources; NASA Open Data Portal; USGS EarthExplorer; NASA Worldview; NASA Library– Space Commercialization |
| 2025 | [Create Your Own Challenge](https://www.spaceappschallenge.org/2025/challenges/create-your-own-challenge/) | Do you have an idea that doesn’t quite fit into any of our challenges? Looking for beginner experience? This is your moment to dream big and Create Your Own Challenge! Whether you want to create an app, artwork, story, l |  | — |
| 2025 | [Data Pathways to Healthy Cities and Human Settlements](https://www.spaceappschallenge.org/2025/challenges/data-pathways-to-healthy-cities-and-human-settlements/) | Your challenge is to demonstrate how an urban planner can use NASA Earth observation data to develop smart strategies for city growth that maintain both the wellbeing of people and the environment. | Earth Science Division | NASA Earthdata Worldview; NASA Earth Observatory; NASA Socioeconomic Data and Applications Center (SEDAC); European Union (EU) Copernicus Global Human Settlement Layer (GHSL); The Earth Observations Toolkit for Sustainable Cities and Human Settlements; WorldPop |
| 2025 | [Deep Dive: Immersive Data Stories from Ocean to Sky](https://www.spaceappschallenge.org/2025/challenges/deep-dive-immersive-data-stories-from-ocean-to-sky/) | Your challenge is to build a short, immersive, virtual reality (VR) experience that leverages NASA’s Earth observation datasets and visualizations to bring stories about our planet’s oceans to life, connecting a broad audience to this data, its beauty, and its impact. | Earth Science Division | Earth.gov; Earth Information Center Visualizations Developed by the Scientific Visualization Studio; Visualizations from NASA’s Plankton, Aerosol, Cloud, ocean Ecosystem (PACE) mission and the international Surface Water and Ocean Topography (SWOT) mission; Visualizations of Surface Water and Ocean Topography (SWOT) Vertical Gravity Gradient; EARTHDATA Ocean site |
| 2025 | [Embiggen Your Eyes!](https://www.spaceappschallenge.org/2025/challenges/embiggen-your-eyes/) | Your challenge is to create a platform that allows users to zoom in and out on these massive image datasets, label known features, and discover new patterns. | Astrophysics Division | NASA Worldview; Mars Reconnaissance Orbiter Online Data Volumes; Transiting Exoplanet Survey Satellite (TESS) Data Products Information; Data Portal; Solar System Treks; EarthData |
| 2025 | [From EarthData to Action: Cloud Computing with Earth Observation Data for Predicting Cleaner, Safer Skies](https://www.spaceappschallenge.org/2025/challenges/from-earthdata-to-action-cloud-computing-with-earth-observation-data-for-predicting-cleaner-safer-skies/) | Your challenge is to develop a web-based app that forecasts air quality by integrating real-time TEMPO data with ground-based air quality measurements and weather data, notifying users of poor air quality, and helping to improve public health decisions. | Earth Science Division | World Health Organization (WHO) Air Pollution; Background: 60 Second Science: Air Quality; Background: An Inside Look at How NASA Measures Air Pollution; NASA Tropospheric Emissions: Monitoring of Pollution (TEMPO) Air Quality Observation Data; SPoRt Viewer – Near Real-Time; Atmospheric Science Data Center (ASDC) Resource Hub |
| 2025 | [International Space Station 25th Anniversary Apps](https://www.spaceappschallenge.org/2025/challenges/international-space-station-25th-anniversary-apps/) | Your challenge is to create a visual tool that not only helps students and the public understand two of the most prominent sensory experiences on the station (sight and weightlessness) through the lens of the cupola and the NBL, but also informs them how these unique experiences benefit humans on Earth. | Space Operations Mission Directorate | NASA Image and Video Library – Cupola + Neutral Buoyancy Lab (NBL); NASA’s Johnson Space Center Flickr – Cupola + NBL; Station Research and Technology; NASA Open Data Portal; Neutral Buoyancy Lab Overview; Extravehicular Activity Systems Encyclopedia Entry |
| 2025 | [Meteor Madness](https://www.spaceappschallenge.org/2025/challenges/meteor-madness/) | Your challenge is to develop an interactive visualization and simulation tool that uses real data to help users model asteroid impact scenarios, predict consequences, and evaluate potential mitigation strategies. | Planetary Science Division | NASA Near-Earth Object (NEO) Web Service Application Programming Interface (API); U.S. Geological Survey (USGS) National Earthquake Information Center (NEIC) Earthquake Catalog; USGS National Map Elevation Data; USGS National Map Training Videos; Approximate Positions of the Planets; Small-Body Database Query Tool |
| 2025 | [NASA Farm Navigators: Using NASA Data Exploration in Agriculture](https://www.spaceappschallenge.org/2025/challenges/nasa-farm-navigators-using-nasa-data-exploration-in-agriculture/) | Your challenge is to create an engaging educational game that effectively utilizes NASA’s open data sets to simulate farming scenarios and enables players to learn how this data can inform innovative, sustainable, agricultural methods. | Earth Science Division | Agriculture and Water Management Pathfinder; Floods Data Pathfinder; Extreme Heat Data Pathfinder; NASA Acres; NASA Harvest; NASA Harvest Portal |
| 2025 | [Sharks from Space](https://www.spaceappschallenge.org/2025/challenges/sharks-from-space/) | Your challenge is to create a mathematical framework for identifying sharks and predicting their foraging habitats using NASA satellite data, and also to suggest a new conceptual model of a tag (a small electronic device that can be attached to an animal to track and study its movement) that could measure not only where sharks are, but also what they are eating, and in real time transmit that data back to users to enable development of predictive models. | Earth Science Division | Plankton Aerosols Clouds and Ecosystems (PACE) data for phytoplankton abundance and community composition; Moderate Resolution Imaging Spectroradiometer (MODIS)-Aqua data for phytoplankton abundance; Surface Water and Ocean Topography (SWOT) data for eddy tracking; “Mesoscale eddies release pelagic sharks from thermal constraints to foraging in the ocean twilight zone,”; “Mesoscale eddies influence the movements of mature female white sharks in the Gulf Stream and Sargasso Sea,” |
| 2025 | [SpaceTrash Hack: Revolutionizing Recycling on Mars](https://www.spaceappschallenge.org/2025/challenges/spacetrash-hack-revolutionizing-recycling-on-mars/) | During a hypothetical three-year mission to Mars and back, an eight-person crew would accumulate 12,600 kg of inorganic waste, or trash, including various packaging materials, textiles, and structural materials. This sce | Space Technology Mission Directorate | MGS-1 Mars Global Simulant; Explore Mars' Jezero Crater with NASA’s Perseverance Rover; Perseverance Explores the Jezero Crater Delta; Mars Facts; Dual Use of Packaging on the Moon: Logistics-2-Living; Waste Management Options for Long-Duration Space Missions: When to Reject, Reuse, or Recycle |
| 2025 | [Stellar Stories: Space Weather Through the Eyes of Earthlings](https://www.spaceappschallenge.org/2025/challenges/stellar-stories-space-weather-through-the-eyes-of-earthlings/) | Your challenge is to write and illustrate a digital children’s story that explains what space weather is and the varying impacts it has on different people such as farmers, pilots, astronauts, power grid operators, and the general public. | Heliophysics Division | NASA Space Weather Website; Solar Storms and Flares; Results of the First National Survey of User Needs for Space Weather (NASA resource); Space Weather Centers of Excellence; NASA Heliophysics Fleet; National Oceanic and Atmospheric Administration (NOAA) Space Weather Prediction Center |
| 2025 | [Through the Radar Looking Glass: Revealing Earth Processes with SAR](https://www.spaceappschallenge.org/2025/challenges/through-the-radar-looking-glass-revealing-earth-processes-with-sar/) | Your challenge is to download multi-frequency or multi-polarization SAR data for an interesting study area of your choice –e. | Earth Science Division | NASA Earthdata Search; Alaska Satellite Facility (ASF) Data Search Vertex; Intro to Remote Sensing; Intro to Synthetic Aperture Radar (SAR); NASA Applied Remote Sensing Training (ARSET) Trainings; SAR StoryMaps |
| 2025 | [Will It Rain On My Parade?](https://www.spaceappschallenge.org/2025/challenges/will-it-rain-on-my-parade/) | Your challenge is to construct an app with a personalized interface that enables users to conduct a customized query to tell them the likelihood of “very hot,” “very cold,” “very windy,” “very wet,” or “very uncomfortable” conditions for the location and time they specify. | Earth Science Division | GES DISC OPeNDAP server (Hyrax); Giovanni; Data Rods for Hydrology; Worldview; Earthdata Search; Data access Tutorials |
| 2025 | [Your Home in Space: The Habitat Layout Creator](https://www.spaceappschallenge.org/2025/challenges/your-home-in-space-the-habitat-layout-creator/) | Your challenge is to create a visual tool that enables users to define a space habitat’s shape/volume and explore possible layout options. | Exploration Systems Development Mission Directorate | “Defining the Net Habitable Volume for Long Duration Exploration Missions,”; Moon to Mars Architecture Definition Document; “Habitats and Surface Construction Technology and Development Roadmap,"; “Review of Habitable Softgoods Inflatable Design, Analysis, Testing, and Potential Space Applications,”; "Overview of NASA’s Moon to Mars Planetary Autonomous Construction Technology (MMPACT),"; "Internal Layout Assessment of a Lunar Surface Habitat," |
| 2026 | [Abandoned but not Forgotten: Storytelling about NASA's Discarded Equipment on the Moon and Mars](https://www.spaceappschallenge.org/2026/challenges/nasas-discarded-equipment-storytelling/) | Your challenge is to tell the story of some or all of this equipment that introduces school-age space enthusiasts to the hardware and the science it made possible. |  | Full statement with datasets due 28 Oct 2026 |
| 2026 | [Be An Earth System Trend Detective!](https://www.spaceappschallenge.org/2026/challenges/earth-system-trend-detective/) | Your challenge is to create a tool that can select variables measured by Earth science missions or produced by Earth science models, visualize how they change over time, and determine what is changing, where it is changing, how much it is changing, and if these changes are what scientists call “significant. |  | Full statement with datasets due 28 Oct 2026 |
| 2026 | [Build a Junior Astronaut Mission Trainer](https://www.spaceappschallenge.org/2026/challenges/build-a-junior-astronaut-mission-trainer/) | Your challenge is to design and build an interactive game or app that lets students run a lunar or Martian outpost, balancing competing demands like life support, radiation shielding, power, and food production, so they experience firsthand the decisions that determine whether a mission fails or succeeds. |  | Full statement with datasets due 28 Oct 2026 |
| 2026 | [Create Health Monitoring Software for Astronauts on Space Missions](https://www.spaceappschallenge.org/2026/challenges/health-monitoring-software/) | Your challenge is to build a health monitoring software that gathers health indicators and enables astronauts to evaluate and act on the status of their health. |  | Full statement with datasets due 28 Oct 2026 |
| 2026 | [Dancing with the SARs](https://www.spaceappschallenge.org/2026/challenges/dancing-with-the-sars/) | Your challenge is to build an interactive application that uses radar remote sensing data from the NASA-ISRO Synthetic Aperture Radar (NISAR) mission to track and visualize one or more types of surface change at locations around the world. |  | Full statement with datasets due 28 Oct 2026 |
| 2026 | [Field Shift: Adapting Farms with NASA Data](https://www.spaceappschallenge.org/2026/challenges/adapting-farms-with-nasa-data/) | Your challenge is to create a decision‑support tool that uses NASA Earth observations along with local soil information, crop characteristics, and farmer priorities to help farmers explore rotation strategies that could strengthen soil health and adapt their farms to changing conditions. |  | Full statement with datasets due 28 Oct 2026 |
| 2026 | [Flame in Freefall: AI-Powered Fire Safety Insights from Microgravity Combustion Data](https://www.spaceappschallenge.org/2026/challenges/flame-in-freefall/) | Your challenge is to create an interactive, super intelligence (SI) powered dashboard that summarizes, ranks, and interprets those findings to deliver fire safety insights for human space exploration. |  | Full statement with datasets due 28 Oct 2026 |
| 2026 | [Harmonization of MODIS and VIIRS Hot Spots](https://www.spaceappschallenge.org/2026/challenges/modis-and-viirs-hot-spots/) | Your challenge is to build a web application that harmonizes these records into a burning activity calendar based on active fire hotspots,  enabling early warning and emergency responders, scientists, and land managers to examine historical fire patterns, unusual conditions, and critical periods within a selected area of interest. |  | Full statement with datasets due 28 Oct 2026 |
| 2026 | [Identify Earth Locations that Analog the Permanent Moon Base Locations and Mars](https://www.spaceappschallenge.org/2026/challenges/permanent-moon-base-locations-and-mars/) | Your challenge is to use open Earth, Moon, and Mars data from NASA and other space agencies to identify and characterize new terrestrial analogs for future bases or landing sites, drawing on deserts, polar regions, volcanic and arid terrains, caves, and other environments that share conditions with the lunar or Martian surface, then present your findings as a map, visualization, or other tool. |  | Full statement with datasets due 28 Oct 2026 |
| 2026 | [Interplanetary Survival Guide: Martian Map](https://www.spaceappschallenge.org/2026/challenges/interplanetary-survival-guide-martian-map/) | Your challenge is to create a layered, integrated view of a location or route on the Martian surface that pulls together data from multiple NASA science missions and could help a human explorer plan and carry out a successful Marswalk while conducting new and exciting science along the way. |  | Full statement with datasets due 28 Oct 2026 |
| 2026 | [Lunar Landing Site Navigator](https://www.spaceappschallenge.org/2026/challenges/lunar-landing-site-navigator/) | Your challenge is to create an intuitive tool or application that lets mission planners, educators, and the public compare landing sites and dates quickly, visualizing Sun and Earth positions relative to the horizon to assess power generation potential and direct-to-Earth communication windows. |  | Full statement with datasets due 28 Oct 2026 |
| 2026 | [Planet X and SPHEREx](https://www.spaceappschallenge.org/2026/challenges/planet-x-and-spherex/) | Your challenge is to create a public-facing web tool to display images of the sky from SPHEREx mission, making it easy for anyone to quickly see how they change over time. |  | Full statement with datasets due 28 Oct 2026 |
| 2026 | [Space Mission Design Game](https://www.spaceappschallenge.org/2026/challenges/space-mission-design-game/) | Your challenge is to create an interactive game that allows participants to design, manage, and simulate a complete space mission while making engineering decisions, managing limited resources, and evaluating how each choice shapes the success of their mission. |  | Full statement with datasets due 28 Oct 2026 |
| 2026 | [The Earth Information Jukebox](https://www.spaceappschallenge.org/2026/challenges/the-earth-information-jukebox/) | Your challenge is to build an "Earth Jukebox"—an interface, script, or application that pairs EIC visual frames with dynamic sonifications generated in real time. |  | Full statement with datasets due 28 Oct 2026 |

---

**2026 note:** The 2026 hackathon runs 14–15 Nov 2026, after Cal Hacks. Its challenges are therefore fresh NASA-authored problem statements that no one has solved publicly yet.

**Unlisted entry:** "Human Development & the Environment" (2024) is listed in the challenge index, but its page returned 404 when queried, so its resource tab could not be read.

### 3b. NASA SBIR Phase I subtopics (FY26–27 BAA Appendix 26B, issued 21 Apr 2026, due 21 May 2026) relevant to data, AI, remote sensing and space operations

Source: [NASA FY26–27 BAA Appendix 26B-I SBIR (PDF)](https://www.nasa.gov/wp-content/uploads/2024/01/nasa-2026-2027-sbir-sttr-baa-appendix-26b-i-sbir.pdf). The full list of Appendix 26B subtopics follows. Rows marked ★ are the most relevant to the space-data theme.

| Subtopic | Title | Lead center | Literal problem statement (short quote) / relevance |
|---|---|---|---|
| ★ INSTALG.3.S26B (ex-S17.01) | Large-Scale Computing and Computational AI | ARC (GSFC) | "the tremendous amount of refactoring that is typically required of existing large scale applications"; "NASA science requires at least 100x more powerful supercomputers and 1,000x higher application parallelism in 10 years without an increased energy demand"; LLMs and SLMs for HPC code |
| ★ ENABLE.2.S26B | High Performance Onboard Computing | JPL (JSC, GSFC) | "onboard data reduction where sensor bandwidth exceeds downlink bandwidth"; onboard AI/ML |
| ★ EXPAND.2.S26B | Orbital Debris Tracking | ARC (GSFC) | "ground-based tracking solution that can maintain custody of a piece of small debris from the time it rises above the horizon to the time it descends" |
| ★ INSTALG.5.S26B (ex-S11.03) | Remote-Sensing Technologies | GSFC (JPL, LaRC) | Active and passive microwave and LiDAR; "calibration stability, environmental robustness, long-term reliability" for SmallSats and constellations |
| ★ EXPAND.3.S26B | Autonomous Onboard Health Management for Small Spacecraft and Distributed Systems | — | Autonomy for constellations |
| ★ INSITU.1.S26B (ex-S17.03) | Fault Management Technologies for Autonomous Systems | — | Autonomy |
| ★ COSMO.3.S26B (ex-S17.06) | AI for Rapid Development of Space Precision Components | — | AI in engineering |
| ★ SPWX.2.S26B (ex-S14.02) | Sensors and Instrumentation for Space Environment Measurement | — | Space weather (cross-slice) |
| INSTALG.4.S26B (ex-S11.04) | Detectors and Integrated Electronics | — | Instruments |
| COSMO.2 / COSMO.4 / COSMO.5 | Cryogenic Systems; Free-Form Optics and Stray-Light Suppression; Advanced Observatory Technologies | — | Instruments |
| COMNAV.1 / COMNAV.2 | Flight Dynamics and Navigation Technologies; Lunar 3GPP Capability | — | Navigation and communications |
| INSITU.2–6 | Sample Handling; Robotic Mobility; Variable Gravity Sample Prep; Contamination Control and Planetary Protection; Plant Research for Space | — | Planetary and biology |
| LAND.1–3, LWS.2, LIVEI.1, SURFMOB.1, EVA.2 | Regolith stability in landing; TPS waterproofing; carbon/phenolic felt; regolith-shielded softgoods habitats; dust mitigation; lunar surface mobility; Mars EVA suit | — | Exploration hardware |
| GO.2 / GO.3 | 3D-printed Hall thruster magnetic circuits; solar sail momentum management | — | Propulsion |
| ENABLE.1 | Laser welding with real-time nondestructive inspection | — | Manufacturing |
| AERO.1–8 | SAF fuel-system sensing; propulsion noise; engine thermal management; flight-test and wind-tunnel measurement; material discovery; Airspace Operations and Safety; fuel-to-electric conversion | — | Aeronautics |

**Gap:** No Earth-science data-analytics subtopic appears in Appendix 26B. The other FY26–27 appendices (26A, STTR) were not read; see Leads not followed.

---

## Section 4. Problem bank

Format: **problem** → who has it → data that could address it → source.

**Budget, policy, workforce**

1. **No one can see who depends on a mission's data before it is cut.** Who: OMB, NASA, Congress, Senior Review panels. Data: Earthdata CMR platform→collection graph, SciX/ADS citations, DOI usage. Sources: [AGU](https://thebridge.agu.org/2025/08/08/appropriations-update-nasa-noaa-and-nsf/), [Ars Jul 2025](https://arstechnica.com/space/2025/07/trump-administration-moves-to-tighten-the-noose-around-nasa-science-missions/).
2. **A dozen operating Earth missions compete for a $68.8M Senior Review pool and need impact evidence.** Who: NASA ESD, mission PIs. Data: CMR, SciX, mission product metrics. Source: [FY2027 request](https://www.nasa.gov/wp-content/uploads/2026/04/fiscal-year-2027-full-budget-request.pdf).
3. **Missions switched off by budget fights are "almost impossible to bring back," and scientists lose months to closeout planning.** Who: mission teams, data users. Data: mission dependency graphs. Sources: [Ars Jul 2025](https://arstechnica.com/space/2025/07/trump-administration-moves-to-tighten-the-noose-around-nasa-science-missions/), [Ars Jan 2026](https://arstechnica.com/space/2026/01/nasas-science-budget-wont-be-a-train-wreck-after-all/).
4. **Recurring budget instability.** The FY2027 request again halves Earth Science to $1.02B, and a CR runs to 11 Dec 2026. Who: all Earth-data users. Data: none (context). Sources: [SPO Apr 2026](https://spacepolicyonline.com/news/trump-fy2027-budget-supports-moon-missions-but-cuts-everything-else/), [SPO Oct 2026](https://spacepolicyonline.com/news/whats-happening-in-space-policy-october-4-10-2026/).
5. **Institutional knowledge lost** after about 4,000 NASA civil-servant departures in 2025 and contractor churn in 2026. Who: NASA, DAAC users. Data: ATBDs, user guides, forum Q&A. Source: [Ars Oct 2026](https://arstechnica.com/space/2026/10/why-is-nasa-bringing-7500-contractors-back-to-work-as-civil-servants/).
6. **NCAR (models and data used across NASA and NOAA) slated for dismantling by OMB.** Who: atmospheric modelers. Data: CESM output, reanalyses. Source: [SPO Jan 2026](https://spacepolicyonline.com/news/final-fy2026-nasa-noaa-appropriations-bill-clears-senate-white-house-is-next/).
7. **NASA does not track how decadal-survey recommendations are implemented,** and gets under 10 days to review NASEM reports. Who: NASA SMD, Congress. Data: decadal reports plus budget documents. Source: [NASA OIG Oct 2026](https://oig.nasa.gov/news/nasas-decadal-survey-oversight-is-hindered-by-challenges-with-internal-processes-communication-and-progress-tracking/).
8. **Earth System Observatory core missions (SBG hyperspectral, AOS aerosol/cloud) vanish from the FY2027 request; only one new Earth System Explorer is implementable.** Who: ecology, air-quality and climate users. Data: EMIT, PACE, commercial hyperspectral as stopgaps. Source: [FY2027 request](https://www.nasa.gov/wp-content/uploads/2026/04/fiscal-year-2027-full-budget-request.pdf).
9. **ESTO cut by $27.7M:** InVEST flight demos discontinued; advanced lidar and radar delayed. Who: instrument developers. Data: none. Source: [FY2027 request](https://www.nasa.gov/wp-content/uploads/2026/04/fiscal-year-2027-full-budget-request.pdf).
10. **Three Airborne Science aircraft retired or stored.** Who: field-campaign scientists and calibration/validation teams. Data: none. Source: [FY2027 request](https://www.nasa.gov/wp-content/uploads/2026/04/fiscal-year-2027-full-budget-request.pdf).

**NASA data systems**

11. **DAAC consolidation** into five thematic teams; domain-expert user support diluted. Who: Earthdata users. Data: CMR, `earthaccess`, documentation. Source: [FY2027 request ES-28](https://www.nasa.gov/wp-content/uploads/2026/04/fiscal-year-2027-full-budget-request.pdf).
12. **Long-term cloud-archive cost sustainability is unanalysed** (OIG recommendation open since 2020). Who: NASA ESDIS. Data: usage and cost metrics. Source: [NASA GAO-IG Act report Apr 2026](https://www.nasa.gov/wp-content/uploads/2026/04/2026-gao-oig-act-report-final-040326.pdf).
13. **Ingest outages during the archive migration** (PO.DAAC, ASF, GES DISC, 28–30 Oct 2026). Who: NRT users. Data: CMR status. Source: [Earthdata blog banner](https://www.earthdata.nasa.gov/news/blog).
14. **SMD data is fragmented across 10 repositories,** growing from 150 PB to 530 PB by 2030, with "a multitude of entry points." Who: researchers. Data: CMR, PDS, MAST, SPDF, SciX. Source: [SMD strategy Apr 2026](https://assets.science.nasa.gov/content/dam/science/cds/about-us/ocsdo/reports/SMD_Data_Computing_Strategy_2025_2030.pdf).
15. **Scientific software is not preserved,** leading to "lost capabilities when projects end." Who: research teams. Data: NASA GitHub repos (the `nasa-impact/nasa-science-github-repos` dataset). Source: [SMD strategy](https://assets.science.nasa.gov/content/dam/science/cds/about-us/ocsdo/reports/SMD_Data_Computing_Strategy_2025_2030.pdf).
16. **Data, AI and cloud skills gap** among scientists. Who: NASA, academia. Data: tutorials, notebooks. Source: [SMD strategy](https://assets.science.nasa.gov/content/dam/science/cds/about-us/ocsdo/reports/SMD_Data_Computing_Strategy_2025_2030.pdf).
17. **Users are not notified when data they downloaded is recalled or reprocessed** (for example the SMAP geolocation error of 14 May–28 Jul 2026; NRT data not replaced). Who: all DAAC users. Data: CMR granule revision history. Source: [NSIDC announcements](https://nsidc.org/data/user-resources/data-announcements).
18. **Products retired and data made inaccessible** (for example ICESat-2 ATL coastal bathymetry v1 on 23 Nov 2026). Who: coastal mappers. Data: newer product versions. Source: [NSIDC](https://nsidc.org/data/user-resources/data-announcements).
19. **1990s SAR archives (ERS-1/2, JERS-1, RADARSAT-1, MEaSUREs wetlands, sea ice, glacier speed) removed from ASF tools or offline.** Who: glaciology, wetlands and sea-ice researchers. Data: ESA, JAXA and CSA portals. Source: [Earthdata ASF notice Oct 2026](https://www.earthdata.nasa.gov/news/changes-availability-historical-asf-datasets).

**NASA missions**

20. **NISAR produces "dozens of terabytes daily"** that few users can process. Who: hazard agencies, scientists. Data: NISAR GCOV/GUNW via ASF. Source: [GAO-IG Act report](https://www.nasa.gov/wp-content/uploads/2026/04/2026-gao-oig-act-report-final-040326.pdf).
21. **SAR is hard for non-specialists** to turn into surface-change insight. Who: planners, the public. Data: NISAR, Sentinel-1, OPERA DISP. Sources: [Space Apps 2026 Dancing with the SARs](https://www.spaceappschallenge.org/2026/challenges/dancing-with-the-sars/), [2025 Radar Looking Glass](https://www.spaceappschallenge.org/2025/challenges/through-the-radar-looking-glass-revealing-earth-processes-with-sar/).
22. **NISAR funding line falls to $0 by FY2030** (post-prime cliff). Who: NISAR users. Data: none. Source: [FY2027 request](https://www.nasa.gov/wp-content/uploads/2026/04/fiscal-year-2027-full-budget-request.pdf).
23. **HLS latency of 2–3 days** is too slow for operational crop, fire and flood alerts. Who: farmers, responders. Data: HLS, low-latency HLS (2027). Source: [Earthdata HLS](https://www.earthdata.nasa.gov/data/projects/hls).
24. **Terra drift biases long climate records,** and MOPITT's 25-year CO record ended on 4 Feb 2025. Who: climate scientists. Data: MODIS, VIIRS, Landsat. Source: [terra.nasa.gov](https://terra.nasa.gov/).
25. **Aqua free drift and Aura end of life (~mid-2028)** threaten AIRS, OMI and MLS continuity. Who: atmospheric chemistry users. Data: NOAA-21 OMPS, CrIS. Sources: [Aqua](https://science.nasa.gov/mission/aqua/), [Aura](https://aura.gsfc.nasa.gov/).
26. **The MODIS vs VIIRS active-fire record is not directly comparable,** so fire managers lack a consistent history. Who: fire managers. Data: FIRMS MODIS and VIIRS. Source: [Space Apps 2026](https://www.spaceappschallenge.org/2026/challenges/modis-and-viirs-hot-spots/).
27. **OCO-2/3 divested to Caltech under no-cost agreements;** continuity and open-data terms are uncertain. Who: carbon-cycle community. Data: OCO L2, US GHG Center. Source: [NASA Aug 2026](https://science.nasa.gov/blogs/oco-2/2026/08/24/nasa-caltech-partner-on-two-earth-science-missions/).
28. **Mass-change gap risk** between GRACE-FO (2018) and GRACE-C (2029, under cost pressure). Who: water managers. Data: GRACE-FO mascons. Source: [NASA OIG IG-26-012](https://oig.nasa.gov/audits/nasas-management-of-the-gravity-recovery-and-climate-experiment-continuity-grace-c-mission/).
29. **ISS-hosted Earth instruments (ECOSTRESS, GEDI, EMIT, OCO-3) are tied to the ISS lifetime and Senior Review.** Who: ecology and agriculture users. Data: their archives. Source: [FY2027 request](https://www.nasa.gov/wp-content/uploads/2026/04/fiscal-year-2027-full-budget-request.pdf).
30. **NRT flood maps have pixel shifts and cloud gaps;** "unusual vs recurring" flooding is hard to judge. Who: responders. Data: MODIS/VIIRS flood archive (2003–2025), OPERA DSWx, SAR. Source: [Earthdata Apr 2026](https://www.earthdata.nasa.gov/news/blog/nasa-enhances-global-flood-products-smarter-detection-flooding-release-23-year-archive).

**NASA applications and AI**

31. **Disaster damage detection needs a faster, multimodal (optical + radar coherence + NISAR) AI.** Who: NASA Disasters, FEMA. Data: HLS, NISAR, Prithvi. Source: [FY2027 ES-36](https://www.nasa.gov/wp-content/uploads/2026/04/fiscal-year-2027-full-budget-request.pdf).
32. **State, local and tribal "last mile":** users can't turn satellite data into decisions. Who: EarthRISE users. Data: OpenET, HLS, SMAP. Source: [EarthRISE](https://science.nasa.gov/earth-science/earth-action/earthrise/).
33. **Food-industry firms (General Mills, McDonald's, Costco) lack shared Earth-information tools.** Who: EI4Food. Data: HLS, SMAP, ECOSTRESS, GPM. Source: [FY2027 request](https://www.nasa.gov/wp-content/uploads/2026/04/fiscal-year-2027-full-budget-request.pdf).
34. **Geo-foundation models need scarce labels and transfer poorly** to new places and times in emergencies. Who: humanitarian mappers. Data: Prithvi-EO-2.0, HF fine-tune datasets. Source: [IGARSS 2026 CCT.4](https://2026.ieeeigarss.org/community_contributed_themes.php).
35. **EO data and model compute exceed desktop capacity;** in-orbit AI and edge computing are needed. Who: the EO community. Data: HLS, VIIRS. Source: [IGARSS 2026 CCT.2](https://2026.ieeeigarss.org/community_contributed_themes.php).
36. **There is no unified catalogue of NASA's division foundation models.** Who: developers. Data: Hugging Face orgs. Sources: [HF nasa-impact](https://huggingface.co/nasa-impact), [SMD strategy](https://assets.science.nasa.gov/content/dam/science/cds/about-us/ocsdo/reports/SMD_Data_Computing_Strategy_2025_2030.pdf).

**Space Apps problem statements (NASA-authored)**

37. **Hourly air-quality forecast** fusing TEMPO, ground monitors and weather, with alerts. Who: public health. Data: TEMPO (ASDC), AirNow. Source: [Space Apps 2025](https://www.spaceappschallenge.org/2025/challenges/from-earthdata-to-action-cloud-computing-with-earth-observation-data-for-predicting-cleaner-safer-skies/).
38. **Probability of "very hot / cold / windy / wet / uncomfortable" conditions** for a place and date. Who: event planners. Data: GES DISC, MERRA-2, Data Rods. Source: [Space Apps 2025](https://www.spaceappschallenge.org/2025/challenges/will-it-rain-on-my-parade/).
39. **Global flowering and bloom detection.** Who: agriculture, pollinator managers. Data: HLS, EMIT, PACE. Source: [Space Apps 2025 BloomWatch](https://www.spaceappschallenge.org/2025/challenges/bloomwatch-an-earth-observation-application-for-global-flowering-phenology/).
40. **Predicting shark foraging habitat** from ocean colour and eddies. Who: fisheries, conservation. Data: PACE, MODIS-Aqua, SWOT. Source: [Space Apps 2025](https://www.spaceappschallenge.org/2025/challenges/sharks-from-space/).
41. **Urban planners need EO-based healthy-growth strategies.** Who: city planners. Data: SEDAC, GHSL, WorldPop, Landsat. Source: [Space Apps 2025](https://www.spaceappschallenge.org/2025/challenges/data-pathways-to-healthy-cities-and-human-settlements/).
42. **Picking which Earth variables are changing significantly, and where.** Who: scientists, the public. Data: Giovanni, MERRA-2, MODIS. Source: [Space Apps 2026 Trend Detective](https://www.spaceappschallenge.org/2026/challenges/earth-system-trend-detective/).
43. **Crop-rotation decision support under climate stress.** Who: farmers. Data: SMAP, HLS, GPM, soils. Source: [Space Apps 2026 Field Shift](https://www.spaceappschallenge.org/2026/challenges/adapting-farms-with-nasa-data/).
44. **Terrestrial analog sites for Moon and Mars are poorly characterised.** Who: mission planners. Data: Earth, Moon and Mars DEMs and spectral maps. Source: [Space Apps 2026](https://www.spaceappschallenge.org/2026/challenges/permanent-moon-base-locations-and-mars/).
45. **Microgravity combustion results are hard to find and compare.** Who: fire-safety engineers. Data: NASA PSI and experiment literature. Source: [Space Apps 2026](https://www.spaceappschallenge.org/2026/challenges/flame-in-freefall/).
46. **Space-biology publications are hard to explore** (608 open-access papers, OSDR). Who: biologists. Data: OSDR, Task Book. Source: [Space Apps 2025](https://www.spaceappschallenge.org/2025/challenges/build-a-space-biology-knowledge-engine/).
47. **Field users need Landsat overpass alerts plus matching surface reflectance** for ground comparison. Who: educators, field scientists. Data: Landsat C2, HLS. Source: [Space Apps 2024](https://www.spaceappschallenge.org/nasa-space-apps-2024/challenges/landsat-reflectance-data-on-the-fly-and-at-your-fingertips/).
48. **Farmers face drought and floods and can't navigate NASA datasets.** Who: farmers. Data: SMAP, IMERG, AppEEARS. Source: [Space Apps 2024](https://www.spaceappschallenge.org/nasa-space-apps-2024/challenges/leveraging-earth-observation-data-for-informed-agricultural-decision-making/).
49. **Mapping human and natural GHG sources and sinks at neighbourhood scale.** Who: policymakers. Data: US GHG Center, OCO-2, EMIT methane. Source: [Space Apps 2024](https://www.spaceappschallenge.org/nasa-space-apps-2024/challenges/uncover-the-role-of-greenhouse-gases-in-your-neighborhood/).
50. **Gigapixel images need zoomable, labelled exploration.** Who: the public, scientists. Data: Worldview, MRO, LRO, TESS. Source: [Space Apps 2025](https://www.spaceappschallenge.org/2025/challenges/embiggen-your-eyes/).

**NOAA**

51. **Retired NOAA products leave users without successors:** Billion-Dollar Disasters, ISCCP H-series, AVHRR Pathfinder SST, POES data, South Atlantic and Indian Dvorak, HURSAT. Who: insurers, climate researchers. Data: NCEI archive, Climate Central, ESA CCI. Source: [NESDIS 2025 notices](https://www.nesdis.noaa.gov/about/documents-reports/notice-of-changes/2025-notice-of-changes).
52. **HDGM geomagnetic model privatised (Monarch Magnetics).** Who: directional drillers, navigation. Data: WMM (open), magnetometer data. Source: [NESDIS](https://www.nesdis.noaa.gov/news/high-definition-geomagnetic-model-hdgm-and-high-definition-geomagnetic-model-real-time-hdgm-rt-will-no-longer-be-produced-nesdis).
53. **Legacy GOES-R rainfall-rate/QPE retired 2 Nov 2026;** users must migrate to the Enterprise product. Who: hydrologists. Data: GOES-18/19 Enterprise RRQPE. Source: [NESDIS](https://www.nesdis.noaa.gov/news/retirement-of-goes-r-rainfall-ratequantitative-precipitation-estimation-grrqpe).
54. **S-NPP data end 2 Nov 2026 and deorbit from 1 Dec 2026:** polar redundancy drops until JPSS-4 (2027). Who: NWP, fire and aerosol users. Data: NOAA-20/21 via PDA and NODD. Source: [NESDIS](https://www.nesdis.noaa.gov/news/cessation-of-suomi-national-polar-orbiting-partnership-s-npp-data-users-onafter-november-2-2026).
55. **NWS staffing cuts reduced radiosonde launches,** degrading NWP initialisation. Who: forecasters. Data: IGRA, COSMIC-2 and commercial RO. Source: [AGU (Senate concern)](https://thebridge.agu.org/2025/08/08/appropriations-update-nasa-noaa-and-nsf/) (station details unverified).
56. **Commercial weather data raises quality, calibration and redistribution-rights issues.** Who: NOAA, the public. Data: COSMIC-2 vs commercial RO. Source: [NOAA SBEM Sep 2026](https://www.noaa.gov/news-release/noaa-expands-use-of-commercial-satellite-data-to-enhance-weather-forecasting).
57. **Downlink and latency bottleneck:** NOAA is testing in-orbit processing of VIIRS. Who: NOAA, satellite operators. Data: VIIRS raw (RDR) and SDR on NODD. Source: [NESDIS–Cowboy Space CRADA](https://www.nesdis.noaa.gov/news/noaa-and-cowboy-space-corporation-test-faster-satellite-data-processing).
58. **Thermospheric density and drag prediction for satellite orbits.** Who: satellite operators, NOAA. Data: commercial density (SpaceX, Spire, PlanetiQ, Ethereal), TLE decay, SWPC. Sources: [NOAA SBEM](https://www.noaa.gov/news-release/noaa-expands-use-of-commercial-satellite-data-to-enhance-weather-forecasting), [NASA Orbital Clarity](https://www.nasa.gov/directorates/stmd/prizes-challenges-crowdsourcing-program/nasa-techleap-prize-orbital-clarity-challenge/).
59. **Space-weather ML models don't reach operations** (CI/CD, latency, trust). Who: SWPC, NASA. Data: SDO, DSCOVR, SOLAR-1. Source: [FDL 2026](https://fdl.ai/fdl26).
60. **Forecasting Dst from real-time solar wind** under operational constraints. Who: NOAA SWPC. Data: DSCOVR, ACE. Source: [CoECI](https://www.nasa.gov/coeci-other-government-agency-opportunities/).
61. **About 3,000–4,000 federal datasets removed;** the inventory is unknown and the analysis tools are lost even where files survive. Who: researchers, the public. Data: DataLumos, Wayback Machine, Data Index tracker. Source: [DRP Aug 2026](https://www.datarescueproject.org/data-loss-report/).
62. **Rescued copies lack provenance and metadata.** Who: data users. Data: checksums, CMR and NCEI ISO metadata. Source: [DRP](https://www.datarescueproject.org/data-loss-report/).
63. **climate.gov redirected; an NCA5 amendment proposed (Aug 2026).** Who: educators, the public. Data: NOAA climate datasets. Source: [noaa.gov/climate](https://www.noaa.gov/climate).
64. **The Arctic Report Card lost NOAA coordination.** Who: Arctic researchers and communities. Data: Arctic Data Center, NSIDC. Source: [Data Index](https://dataindex.us/terminations-tracker).
65. **Sea Ice Today tools suspended for lack of funding.** Who: media, the public. Data: Sea Ice Index. Source: [NSIDC](https://nsidc.org/sea-ice-today).
66. **The 47-year SMMR/SSM/I-SSMIS sea-ice record stopped forward processing (Dec 2025);** the SSMIS→AMSR2/AMSR3 transition risks a discontinuity. Who: climate scientists. Data: AMSR2, Bootstrap v4. Source: [NSIDC](https://nsidc.org/data/user-resources/data-announcements).

**USGS and Landsat**

67. **Landsat's move toward a "commercial solution"** puts free, calibrated, 54-year continuity at risk. Who: USDA, OpenET, MTBS, every Landsat user. Data: Landsat C2, commercial samples. Source: [FY2027 request](https://www.nasa.gov/wp-content/uploads/2026/04/fiscal-year-2027-full-budget-request.pdf).
68. **Landsat 10 is a single satellite launching in 2031;** gap risk with aging Landsat 8. Who: land managers. Data: HLS plus Sentinel-2. Sources: [USGS Landsat 10](https://www.usgs.gov/landsat-missions/landsat-next), [Landsat 7 decommissioned 4 Jun 2025](https://www.usgs.gov/landsat-missions/landsat-7).
69. **Landsat 8/9 cannot separate cyanobacteria from other phytoplankton** (harmful algal blooms cost up to $100M a year in the US). Who: water-quality managers. Data: Landsat, Sentinel-2/3, PACE. Source: [USGS Oct 2026](https://www.usgs.gov/landsat-missions/news/landsat-science-team-landsat-10-improve-harmful-algal-bloom-monitoring).
70. **No robust tree-mortality tracking** (non-photosynthetic vegetation, NPV). Who: forest and fire managers. Data: Landsat, EMIT. Source: [USGS Oct 2026](https://www.usgs.gov/landsat-missions/news/landsat-science-team-focuses-advanced-satellite-technology).
71. **Field-scale water use (ET) for irrigation under "increasing water stress."** Who: farmers, water districts. Data: OpenET, Landsat thermal, ECOSTRESS. Source: [USGS Oct 2026](https://www.usgs.gov/landsat-missions/news/landsat-science-team-focuses-advanced-satellite-technology).
72. **Landsat 2/3 MSS products had brightness errors** discovered in 2025 and since reprocessed. Who: long-term change analysts. Data: MSS C2. Source: [Latest in Landsat Oct 2026](https://www.usgs.gov/latest-landsat-newsletter/latest-landsat-october-2026).
73. **Landsat RSS feeds discontinued;** developers must migrate to AWS SNS. Who: developers. Data: SNS topics. Source: [Latest in Landsat Oct 2026](https://www.usgs.gov/latest-landsat-newsletter/latest-landsat-october-2026).

**Office of Space Commerce, SBIR and prizes**

74. **No recurring, government-verifiable metrics for the US space economy.** Who: OSC, policymakers. Data: launch logs, FCC filings, CelesTrak, SAM.gov. Source: [OSC Oct 2026](https://space.commerce.gov/osc-seeks-proposals-for-u-s-space-economy-measurement-metrics-study/).
75. **Remote-sensing licensing (15 CFR 960) obligations are opaque to newcomers.** Who: EO startups. Data: regulations text. Source: [OSC CRSRA](https://space.commerce.gov/regulations/commercial-remote-sensing-regulatory-affairs/).
76. **"Onboard data reduction where sensor bandwidth exceeds downlink bandwidth."** Who: NASA missions. Data: EMIT and PACE hyperspectral cubes. Source: [SBIR ENABLE.2](https://www.nasa.gov/wp-content/uploads/2024/01/nasa-2026-2027-sbir-sttr-baa-appendix-26b-i-sbir.pdf).
77. **HPC code refactoring for heterogeneous exascale; AI for scientific code.** Who: NASA HPC users. Data: the nasa-science-code-benchmark dataset. Source: [SBIR INSTALG.3](https://www.nasa.gov/wp-content/uploads/2024/01/nasa-2026-2027-sbir-sttr-baa-appendix-26b-i-sbir.pdf).
78. **Keeping custody of small debris across a pass.** Who: SSA, laser-removal developers. Data: optical tracking, TLEs. Source: [SBIR EXPAND.2](https://www.nasa.gov/wp-content/uploads/2024/01/nasa-2026-2027-sbir-sttr-baa-appendix-26b-i-sbir.pdf).
79. **Calibration stability of SmallSat microwave and LiDAR sensors.** Who: instrument builders, commercial data buyers. Data: cross-calibration with reference missions. Source: [SBIR INSTALG.5](https://www.nasa.gov/wp-content/uploads/2024/01/nasa-2026-2027-sbir-sttr-baa-appendix-26b-i-sbir.pdf).
80. **Commercial constellation imagery has "image-to-image variations in calibration over time."** NASA-funded research produced a fix (Yan, Roy and Huang 2026). Who: CSDA users. Data: commercial plus Landsat reference. Source: [FY2027 request ES-2](https://www.nasa.gov/wp-content/uploads/2026/04/fiscal-year-2027-full-budget-request.pdf).

---

## Section 5. Cross-slice leads

- **EO companies:**
  - NOAA SBEM IDIQ vendor list (Sep 2026), by category ([NOAA](https://www.noaa.gov/news-release/noaa-expands-use-of-commercial-satellite-data-to-enhance-weather-forecasting)): Spire, PlanetiQ, Ethereal Space, Precursor SPC, Tomorrow.io, Muon Space, BAE Systems, Weather Stream, Hydrosat, Tropical Weather Analytics, Care Weather, ICEYE US, Umbra and SpaceX.
  - NASA CSDA third IDIQ on-ramp in FY2027; NASA's FY2027 request shows an ICEYE image captured by Vantor WorldView-3.
  - Tomorrow.io gave an IGARSS 2026 plenary.
- **EO analytics and industry:**
  - EI4Food (General Mills, McDonald's, Costco).
  - OpenET in EarthRISE.
  - Climate Central now runs the Billion-Dollar Disasters database.
  - Monarch Magnetics took over HDGM.
  - Caltech now operates OCO-2/3.
- **ESA, Europe and other agencies:**
  - ASF redirects ERS users to ESA, JERS-1 to JAXA G-Portal and RADARSAT-1 to CSA.
  - HLS depends on Sentinel-2C. Sentinel-6B launched in 2025.
  - JAXA AMSR3 products are planned at NSIDC for 2027.
  - ESA CHIME is a possible stand-in for the absent NASA SBG.
  - FDL's Earth sibling is ESL (eslab.ai), whose SHRUG-FM won Best Paper at EarthVision 2026 (link on fdl.ai).
  - The NISAR S-band (ISRO) data policy is unverified.
- **SpaceX, xAI and orbital compute:**
  - **SpaceX is a NOAA vendor for "thermospheric neutral density for satellite orbit predictions."**
  - NOAA–Cowboy Space (Baiju Bhatt) CRADA for in-orbit VIIRS processing on Reason-2 (2027): "Every mission we fly is a step toward data centers in orbit."
  - Ars headlines: ["SpaceX acquires xAI, plans 1 million satellite constellation" (Feb 2026)](https://arstechnica.com/ai/2026/02/spacex-acquires-xai-plans-1-million-satellite-constellation-to-power-it/); ["Orbital data centers, part 1"](https://arstechnica.com/space/2026/03/orbital-data-centers-part-1-theres-no-way-this-is-economically-viable-right/); ["How hard is it to build orbital data centers, actually?"](https://arstechnica.com/space/2026/07/how-hard-is-it-to-build-orbital-data-centers-actually/) (titles only, not opened).
  - Space Apps 2025 winner "Gaia+LEO" on orbital and ground data-centre co-design.
  - The SBIR ENABLE.2 onboard computing subtopic.
- **Space traffic, debris and space weather:**
  - OSC TraCSS funded at $55M in FY2026. The 18 Dec 2025 EO changed the SPD-3 "free of direct user fees" language.
  - OSC "Dataset for Conjunction Assessment Verification."
  - NASA TechLeap Orbital Clarity (thermospheric drag sensors, up to $500k each plus a free test flight). The other researcher's NASA Science date of 18 Sep 2026 is not verified here; the CoECI listing shows 19 Aug 2026.
  - SBIR EXPAND.2 (small debris custody).
  - SOLAR-1 (ex-SWFO-L1) coronagraph latency of 30 min vs up to 8 h; aging DSCOVR.
  - FDL 2024–2026 thermosphere, solar-wind and active-region challenges; FDL BenchLab solar-wind 2026.
  - NOAA Dst crowd challenge; Surya and SuryaBench.
  - S-NPP controlled deorbit from 1 Dec 2026.
  - Space Apps 2025 "Astro Sweepers" debris-compliance winner.
- **China:** SpaceNews, ["Ceres-1 sea launch lofts first satellite for low-inclination Wuyang remote sensing constellation" (21 Oct 2026)](https://spacenews.com/ceres-1-sea-launch-lofts-first-satellite-for-low-inclination-wuyang-remote-sensing-constellation/) (headline only).
- **Datasets catalogue:**
  - NISAR product list (L0B–L3, Provisional V1).
  - The MODIS flood archive 2003–2025 (LAADS).
  - Landsat 10 specifications: 26 bands, WRS-3 with 265 paths, 653 km.
  - The Hugging Face datasets listed in C2 (Landslide4sense, BioMassters, hls_burn_scars, WxC-Bench, SuryaBench, Sombench lunar sets).
  - DataLumos rescued data.
  - The Data Index terminations tracker.
- **Models and tools:**
  - Prithvi-EO-2.0 (tiny, 100M, 300M, 600M) and Prithvi-WxC.
  - Surya-1.0 (Aug 2025).
  - **The NASA–IBM Lunar Foundation Model, released on Hugging Face on 1 Sep 2026,** with crater-detection, IMP-segmentation and ice-prospectivity fine-tunes ([HF nasa-ibm-ai4science](https://huggingface.co/nasa-ibm-ai4science)). This confirms the other researcher's lead.
  - INDUS and indus-sde embedding models; the nasa-science-code-benchmark (Apr 2026); NASA GeoSI (agentic "Super Intelligence") solicitation; TerraTorch.
  - Ars on Google's AI weather model during the 2025 hurricane season ([Ars Nov 2025](https://arstechnica.com/science/2025/11/googles-new-weather-model-impressed-during-its-first-hurricane-season/), title only).
- **Space science, planetary and literature:**
  - Space Apps 2026 lunar and Mars challenges (Lunar Landing Site Navigator, Martian Map, analog sites, SPHEREx Planet X).
  - The Artemis II lunar science data release (7 Oct 2026, per SPO).
  - NASA's Swift mission ended (Oct 2026, science.nasa.gov headline).
  - NASA OIG report on the decadal survey process (Oct 2026).
  - Space biology knowledge engine (608 papers, OSDR).
  - SciX, the successor to ADS.

---

## Section 6. Leads not followed (or not verified)

- **2026 Earth Science Senior Review outcome** (guidance due Sep 2026): which of SWOT, TEMPO, PACE, GEDI, ECOSTRESS, EMIT, SMAP, GPM, ICESat-2, GRACE-FO, PREFIRE and TSIS-1 were extended or terminated. Not found.
- **Fate of Terra, Aqua, Aura, CYGNSS and SAGE III** in FY2026 enacted operations. They are not described in the FY2027 Earth Science chapter.
- **DMSP SSMIS data cut-off (DoD/Navy, 2025)** and NSIDC's response. Only the end of forward processing on 31 Dec 2025 is verified here.
- **NWS radiosonde suspensions:** which stations and current status.
- **Goddard campus reorganization, building and lab closures, and library closure (2025):** recalled but not verified. GISS is still operating; its website and GISTEMP were updated in Oct 2026 ([GISS](https://www.giss.nasa.gov/), [GISTEMP](https://data.giss.nasa.gov/gistemp/)).
- **The NOAA FY2027 budget request** (NESDIS, OAR, NWS lines).
- **Landsat Mission Alternatives Assessment Team report** (basis for the commercial transition). Not located.
- **The SpaceNews article on NASA "New Competition Model 2.0"** (paywalled); the SMD town hall is on 26 Oct 2026.
- **AGU Fall Meeting 2025 and AMS 2026 programs:** blocked by Cloudflare (403). Search them for "data rescue," "federal data loss" and "AI foundation models" sessions.
- **NASA SBIR/STTR FY26–27 Appendix 26A and the STTR appendices.**
- **TOPS (Transform to Open Science) status in 2026:** no longer named on the Open Science page.
- **Earthdata Cloud egress and requester-pays costs:** no 2025–2026 source found.
- **Status of the Earth Information Center (earth.gov) and its US Greenhouse Gas Center.**
- **Details of the SERVIR termination** (USAID–NASA).
- **Names of the two Earth System Explorers selected in FY2026.**
- **Earthdata "Data User Stories" and blog posts:** crawling was stopped by an AWS WAF CAPTCHA, so only individual pages were read.
- **Space Apps 2026 full challenge statements and datasets:** due 28 Oct 2026; re-check then.
- **Climate Central Billion-Dollar Disasters page** (not opened directly).
- **The OSTP/USGCRP "Proposed Amendment to NCA5" (Aug 2026):** content not read.
- **NASA OIG IG-26-014 (Geospatial Data Act FY2026):** which 5 responsibilities remain open.
- **ESL (eslab.ai) 2025–2026 Earth challenges** (European slice).
- **X/LinkedIn posts by NASA, NOAA or USGS scientists:** not searched, because web search quota was exhausted for most of the session.
- **The Ars article "This Atlantic hurricane season is looking like a dud" (Aug 2026):** title only.
