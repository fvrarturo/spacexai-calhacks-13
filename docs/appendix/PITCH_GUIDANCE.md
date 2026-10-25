## Pitch guidance: what each result lets us say

Use this for the video, the Devpost text and the judge walkthrough. Every "say" line is backed by a result file. Every "avoid" line is a claim the data does not support.

### Materials
- **Protein crystals (whole PDB).**
  - *Say:* we parsed all 261,139 PDB entries (92.6 GB) and read 382 candidates by hand. 67 structures came from crystals grown in orbit, on Shuttle, ISS/Kibo and ESA APCF/PCDF hardware. Against same-era Earth crystals of the same protein, the space crystal was the sharpest for 54% of 28 proteins, where label shuffling predicts 21% (p < 0.001). Against Earth controls from the same paper (14 proteins), there is no clear difference.
  - *Avoid:* "microgravity makes better crystals" (this is an archive correlation), and "space crystals beat the best Earth crystals" (against the all-time best, a later Earth crystal usually wins, +0.13 Å). The census is a lower bound. Merck does not appear in the PDB data; cite its 2019 paper separately.
- **Drug crystals (COD).**
  - *Say:* among FDA drugs crystallised at least twice in the open Crystallography Open Database, 58% show two or more solid forms, versus 34% of organic compounds in general. This holds at every number of entries per compound, and it is a lower bound.
  - *Avoid:* "59% of all drugs are polymorphic", and any microgravity claim from this file. Ritonavir is absent from COD.
- **Solidification on the ISS (NASA PSI / DECLIC-DSI).**
  - *Say:* we measured cell spacing in 53,895 ISS images. Runs settle at 223–731 µm, and runs at the same pulling speed from different 2010 sequences differ 1.6–1.8×. Each 1 MB frame reduces to 16 numbers.
  - *Avoid:* a microgravity advantage (there are no matched Earth runs), a spacing–velocity law (leave-one-out flips the exponent), and calling it a cooling material (it is an SCN–camphor analogue).
- **MOF membranes (CoRE MOF).**
  - *Say:* 84% of the 12,863 distinct MOFs in CoRE MOF 2019 have pore windows between a water molecule and a hydrated Mg²⁺ ion. Only 3.3% sit in the narrow band between hydrated Li⁺ and Mg²⁺. Geometry is not the bottleneck; orientation and defects are, and orbit might change those.
  - *Avoid:* selectivity predictions, and adding the 2019 and 2024 counts together.
- **Photonic colloids (physics).**
  - *Say:* on the ground, gravity beats Brownian motion for silica spheres above about 1.1 µm. At ISS levels the crossover moves to about 36 µm.
  - *Avoid:* calling it a measurement. For ~300 nm visible-light spheres the ground problem is the compressed sediment, not single-particle settling. The 1e-7 g free-flyer level is a placeholder.

### Foundry
- **Orbit environment (TLE history).**
  - *Say:* from 253 million tracking records, drag on a foundry-sized free-flyer at 500–525 km is about 16 nano-g in active-Sun years and 1.5 nano-g in quiet years. That is 60–670× below the ISS 1 µg requirement. A passive foundry re-enters within 5 years only below about 443 km.
  - *Avoid:* "measured microgravity of our foundry". It is orbit-averaged along-track drag only, rescaled with an assumed ballistic coefficient. Gravity gradient (about 0.4 µg per metre) outweighs drag above about 450 km.
- **ISS data volume (PSI inventory).**
  - *Say:* NASA's open PSI bucket holds 30.3 TB from three ISS investigations. PK-4 alone recorded a median 702 GB of video per science day, which is why we measure on board.
  - *Avoid:* "we processed 30 TB". We catalogued it. We processed the 56.6 GB of DSI frames.
- **Return cadence (GCAT).**
  - *Say:* since 2021, a capsule a US commercial payload could ride has landed every 45 days at the median. Return, not launch, is the bottleneck.
  - *Avoid:* stating a purpose for SpaceX Starfall, and presenting the fleet model's on-time rates as achievable with today's vehicles.

### Network
- **Launch scale (GCAT).**
  - *Say:* in 2025 SpaceX flew 170 of 329 orbital launch attempts (52%) and carried 85% of the payloads that reached orbit. 23 Transporter/Bandwagon rideshares carried 1,742 payloads (median 74).
  - *Avoid:* calling Starship operational, and claiming 2026 growth (attempts are flat against 2025 to date).
- **Demand (ClinicalTrials.gov, FDA, USGS).**
  - *Say:* since 2020 the FDA has licensed subcutaneous versions of 16 antibodies first licensed as IV infusions, including Keytruda. Subcutaneous antibody trials grew about 8× from 2005. World lithium production grew 9× from 2015 to 2025.
  - *Avoid:* "the subcutaneous share is rising" (it is flat at ~21%), and claiming demand for orbit-made crystals or a MOF-membrane market.
- **Literature and partners (OpenAlex).**
  - *Say:* 4,532 works pair microgravity with a foundry process. Only 11 are about drug crystals in microgravity, and 10 of those since 2024. Only 2 grow MOFs in microgravity. The frontier is open.
  - *Avoid:* "papers on X" without the keyword-precision caveat; citing OpenAlex as evidence that SpaceX publishes here; treating zero papers as zero activity.
- **Crowding (TLE history).**
  - *Say:* 27,298 catalogued objects sit below 2,000 km today, up from 4,846 in 1990, and 92% of objects at 450–500 km are Starlink.
  - *Avoid:* treating counts as collision risk.

### How to describe the tools
- MIT Engaging, public archives and committed code produced every number.
- Describe Cursor, Grok and Grok Bot only for what you actually did with them, for example: Grok reviews of each result file (run `python3 -m analysis.grok_review` with an xAI key), Grok Bot planning threads, and Cursor sessions on this repository.
