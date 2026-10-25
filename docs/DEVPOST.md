## Inspiration

For forty years, materials made in orbit have come home different. Merck grew pembrolizumab (Keytruda) crystal suspensions on the ISS that were more uniform and flowed more easily. Varda crystallised ritonavir in orbit and brought it back in an autonomous capsule. ISS colloid experiments grew photonic crystals too large to assemble on the ground. Each result stands alone: one material, one flight, one paper. Nobody has asked the industrial question: could these processes share one factory, and do four decades of public space data say it's worth building?

The SpaceXAI challenge offered exactly what that question needs: enormous public datasets, decades of missions, and a literature no human can read all of. So we turned the archives on our own idea and let the data decide whether an orbital foundry should exist.

## What it does

**Orbital Foundry is a free-flying factory that makes the materials gravity spoils on Earth (drug crystals, membranes, optical materials) and sends them home by capsule.** Sealed process cartridges share one platform's power, heat rejection, cameras and data, and each keeps its own chemistry.

Each design decision rests on a public dataset.

**What to make**
- **Protein crystals.** We parsed all **261,139** Protein Data Bank entries and checked 382 candidates by hand. **67** structures came from crystals grown in orbit. Against Earth crystals of the same protein from the same years, the space crystal was the sharpest **54%** of the time, where shuffling the labels predicts 21% ($p < 0.001$).
- **Drug crystals.** In the 521,901-structure Crystallography Open Database, **58%** of the FDA drugs crystallised at least twice show two or more solid forms, against 34% of organic compounds overall. Which form you get decides how a drug dissolves and how long it keeps. In 1998 an unexpected ritonavir form forced Abbott to pull its capsules.
- **Solidification.** We measured cell patterns in **53,895** ISS images from the NASA/CNES DECLIC-DSI furnace. 57 GB of frames became a run-level morphology record.
- **MOF membranes.** **84%** of 12,863 known MOFs already have pore windows in the lithium-separation range. The bottleneck is crystal orientation and defects, which is what quiet growth could change.
- **Photonic colloids.** Gravity beats Brownian motion once the sedimentation Péclet number passes 1:

$$\mathrm{Pe} \sim \frac{\Delta\rho\, g\, a^4}{k_B T}, \qquad d^* \propto g^{-1/4}$$

For silica, that crossover sits at **1.1 µm** on the ground and moves to **36 µm** at ISS gravity levels.

**Where to fly it.** We analysed **253 million** satellite-tracking records from 1959 to 2026. Drag on a foundry-sized free-flyer at 500–525 km works out to **1.5–16 nano-g**, which is **60–670×** quieter than the ISS 1 µg requirement. A dawn–dusk sun-synchronous orbit there stays in sunlight 94–96% of the time.

**Why a network.** SpaceX flew 52% of the world's launches in 2025 and carried 85% of the payloads, so getting up is solved. Getting back isn't: since 2021, a capsule a US commercial payload could ride has landed only once every **45 days** at the median. That is the case for a fleet that carries its own return capsules. Demand is there too: since 2020 the FDA has licensed under-the-skin versions of **16** antibodies first given by IV, a shift that depends on high-concentration formulations such as crystal suspensions.

Everything lives on our site (**[zerogspot.us](https://zerogspot.us)**) in five chapters: Vision, Materials, Foundry, Network and a Methods appendix. Every chart is drawn from a result file.

## How we built it

- **Big data, at full scale.** We ran 12 analyses on MIT's Engaging cluster: **192 GB** processed, about **256 million** records, 36 public datasets and **64 Slurm jobs**. That covered job arrays for parsing and a data-transfer partition for mirroring. We mirrored the entire PDB (92.6 GB) and COD (109 GB uncompressed), streamed 68 years of orbit history, and catalogued NASA's 30.3 TB Physical Sciences Informatics archive object by object.
- **Why size mattered.** Samples would have misled us:
  - Keyword search finds space-grown crystals with only 18% precision, so a defensible census needed the whole archive plus hand review.
  - Our drag figures are medians over 15,573 passive objects and 442 months, not one lucky satellite.
- **Sources:** PDB + SIFTS, COD, CoRE MOF, NASA PSI, Space-Track/CelesTrak, GCAT, ClinicalTrials.gov (608,415 studies), FDA Purple and Orange Books, USGS and OpenAlex.
- **SpaceXAI tools:**
  - **Cursor** was our main coding environment for the analysis modules, the cluster scripts and the site.
  - **Grok** was our research partner. It helped us brainstorm, pressure-test our assumptions and check the idea's novelty against the literature.
  - **Grok Imagine** generated the scenes in our mission video.
- **Engineering:**
  - Reproducible Python modules, one compact JSON result per analysis, and unit tests on the simulation invariants.
  - A static site with no dependencies that pulls its numbers from the result files and hides any chart that has no data behind it.
  - Deployed on GitHub Pages.
- **Fleet model:** a seeded simulation of 24 scenarios × 100 paired seeds, comparing shared coordination with dedicated single-purpose missions.

## Challenges we ran into

- **Our own model said no.** Under our first assumptions, the coordinated fleet lost to dedicated missions by about **20 points** of on-time delivery, because changeovers are expensive. We kept that result and mapped where sharing wins: with zero changeover cost and fast return, it comes out **+6.4 points** ahead. The real return record (45 days, not hours) then told us which lever matters most.
- **Correlation isn't proof.** Against the best Earth crystal of all time, a later Earth crystal usually wins, and same-paper pairs show no clear difference. We wrote down exactly what the PDB result does and doesn't show.
- **Messy archives.**
  - Crystal names don't merge cleanly, and open databases miss most pharmaceutical forms; ritonavir isn't in COD at all.
  - One ISS experiment records a median **702 GB** of video per science day.
- **Fragile fits.** A leave-one-out check flipped the sign of the spacing–velocity exponent in the DSI images, so we dropped the claim.

## Accomplishments that we're proud of

- A hand-checked census of every orbit-grown crystal structure in the PDB. Against same-era Earth crystals of the same protein, the space crystal was sharpest 2.5× as often as chance predicts.
- A pipeline that runs on whole archives: 192 GB, 64 cluster jobs and 12 reproducible analyses. Each has an appendix entry with its data, jobs, methods and limits.
- An honest evidence boundary. Every claim on the site and in the video links to a result file, and every claim the data doesn't support is listed next to it.

## What we learned

- Space manufacturing is a logistics problem as much as a physics problem. Launch is abundant; return is scarce.
- Orbit is stunningly quiet. Above about 450 km, the gravity gradient across the spacecraft (0.4 µg per metre) outweighs drag, so where a cartridge sits inside the foundry matters more than altitude.
- The research frontier is wide open. Of 4,532 works pairing microgravity with a foundry process, only **11** are about drug crystals (10 of them since 2024), and only **2** grow MOFs.
- A negative result, reported clearly, makes a pitch more credible.

## What's next for Orbital Foundry

- Pick one lead material, process and application, and set the performance bar it must clear against the best Earth method.
- Make return cadence a design variable: model foundries with their own capsules, and test batching and selective sharing on fresh held-out seeds.
- Scale the evidence: process more of NASA's 30.3 TB archive, find matched Earth control runs, and reprocess raw diffraction images for the 67 space-grown structures.
- Talk to the partners the data points to:
  - JAXA and ESA crystallisation programmes
  - Merck and other subcutaneous-antibody developers
  - MOF membrane groups
  - SpaceX rideshare and Dragon return, and Varda
