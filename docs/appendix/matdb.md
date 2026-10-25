# matdb: materials big-data evidence (drug crystals, MOF membranes, photonic colloids)

Workstream `matdb`, tab **Materials**. Three result files; the JSONs are the source of truth for every number.

| File | Material | Evidence level |
|---|---|---|
| `data/results/bigdata/cod-polymorphs.json` | small-molecule drug crystals (`small`) | our computation on public data |
| `data/results/bigdata/mof-pore-screen.json` | MOF membranes (`mof`) | our computation on public data |
| `data/results/bigdata/colloid-sedimentation.json` | photonic colloidal crystals (`photonic`) | physics computation (not a measurement); one chart is our computation on OpenAlex abstracts |

Cluster folder: `~/orcd/scratch/orbital-foundry-20261024-01a170b7/bigdata/matdb/` (`raw/`, `work/`, `env/`, `logs/`).
Code: `analysis/bigdata/matdb_*.py`, `cluster/bigdata/matdb-*.sbatch`.

---

## A. Drug crystals: how common is polymorphism?

**Question.** How often does one molecule crystallise in more than one solid form, and how common is that among FDA-approved drugs? This is why solid-form control matters; Varda's ritonavir Form III is the project's anchor.

**Headline (our computation on public data).** Of the 123 FDA-approved active moieties crystallised at least twice in the open Crystallography Open Database, 72 (58.5%, 95% Wilson CI 49.7–66.9%) show two or more distinct solid forms. The figure for multiply-crystallised organic compounds in general is 34.0% (CI 31.8–36.2%). These are lower bounds.

### Data
| Dataset | Size processed | Notes |
|---|---|---|
| COD bulk archive `cod-cifs-mysql.zip` ([archives](https://www.crystallography.net/archives/)) | 27,107,247,440 bytes (27.1 GB) zip, md5 verified; **521,901 CIFs, 108.9 GB uncompressed**, all parsed | Release 2025-02-09 (SVN r297631), the latest bulk archive. COD data are CC0. |
| COD MySQL `data` table (same archive) | 521,874 rows, 466 MB | COD's own parse. Used for duplicate / retraction / on-hold flags and as a cross-check. |
| COD SMILES table (same archive) | 240,593 SMILES; 178,496 parsed by RDKit | Gives structure identity (InChIKey). |
| FDA Orange Book `products.txt` ([download](https://www.fda.gov/media/76860/download)) | 48,864 products, 2,382 unique ingredient strings | Oct 2026 data file. RX, OTC and discontinued products. |
| PubChem PUG-REST | 2,245 of 2,382 ingredient names resolved | Used only for structures. |

**Why not the rsync tree.** The per-file rsync tree is about 520k small files, and the user's scratch quota is 1.0M files, shared by all workstreams. Scratch was at 318K files when we started and 621K by the end. We used COD's single-file bulk zip instead. Zip allows random access, so the job array reads CIFs straight out of it and nothing is ever extracted.

### Pipeline (all on MIT Engaging)
1. `matdb-fetch.sbatch` (mit_data_transfer): resumable parallel HTTP range download (`matdb_fetch.py`) and md5 check.
   - The first attempt (job 26813010) used 10 parallel connections, and the COD server reset them. It was cancelled and restarted with 4 connections and mid-chunk resume as job 26813661 (29 min). The finished byte ranges were reused.
   - To start early, the SQL members were first pulled from the remote zip by HTTP range requests. `matdb_cod_extract_sql.py` re-extracts them from the local zip, byte-identical.
2. `matdb-prep.sbatch` (mit_quicktest, job 26814249):
   - extracts the MySQL members;
   - converts the `data` table to parquet (`matdb_cod_sql.py`, 521,874 rows, 0 malformed);
   - computes InChIKeys of COD SMILES components with RDKit (`matdb_cod_inchi.py`).
3. `matdb-fda.sbatch` (mit_data_transfer, job 26814250): Orange Book ingredients → PubChem structures (`matdb_fda_pubchem.py`, ≤ 4 req/s, cached). Salts are matched through their largest organic component.
4. `matdb-cod-parse.sbatch`: a 32-task array (job 26816035), 1 CPU per task, ≤ 16 concurrent. Each task parses every 32nd CIF straight from the zip with gemmi (`matdb_cod_parse.py`); all 521,901 parsed with gemmi and the regex fallback was never needed.
   - `mit_normal` was congested, so after 8 tasks a burst job on mit_quicktest (`matdb-cod-parse-burst.sbatch`, job 26816358, 14 CPUs, 1 min 49 s) ran the remaining shards with the same script.
   - 3 shards were parsed by both at the same moment; the outputs are identical and written atomically. The unstarted array tasks were then cancelled.
   - For about a minute, 3 array tasks overlapped the 14-CPU burst job (17 CPUs). The array was throttled to 2 straight away.
5. `matdb-analyse.sbatch` (mit_quicktest, job 26817191, 2 min 26 s): `matdb_cod_polymorph.py`. Jobs 26816547 and 26816712 are superseded runs; 26814637 is a failed test.

**Parse QC.** Agreement of our CIF parse with COD's SQL table: space-group number 99.36%, volume (within 0.1%) 99.99%, sum formula 99.89%.

### Definitions
- **Entry filters** (count removed, in order):
  - retracted or COD `errors` status: 158
  - theoretical: 920
  - COD-flagged duplicate: 5,415
  - on hold: 387
  - unparsable formula: 362
  - no space-group number: 2,854
  - recorded pressure outside 80–120 kPa: 4,073 (some depositors write GPa into the kPa field)
  - title or name mentions a pressure study: 4,173
  - non-integer formula (partial occupancy / disordered solvent): 56,527
  
  447,032 entries remain, of which 169,988 are organic molecular crystals (C and H, plus only N, O, S, P, F, Cl, Br, I, B, Si, Se).
- **Same compound (primary, conservative)** requires both:
  - the same GCD-reduced Hill formula;
  - a shared normalised name, common or systematic. Normalisation lowercases, maps Greek letters, and strips "form II", "β-polymorph", crystal-system words and "at 100 K".

  Entries are linked by union-find within each formula. Only 64,768 of the 169,988 organic entries carry a usable name, and unnamed entries stay singletons. Names used on three or more different formulas (118 generic or class names, such as "phthalonitrile" used for its derivatives) are dropped.
- **Cross-check identity:** RDKit InChIKey connectivity block of COD's SMILES, single-component entries only.
- **Same form:** two entries of one compound are the same form only if both of these hold:
  - **Space group.** The space groups are equal, or form a commonly mis-assigned pair (P1/P-1, Cc/C2/c, P2₁/P2₁/c, Pna2₁/Pnma, …) or one of the 11 enantiomorphic pairs (P3₁21/P3₂21, …).
  - **Volume.** Their volume per non-H atom, corrected to 293 K, agrees within 3%, plus 0.005% per K of temperature gap to allow for uncertainty in the expansion coefficient.
    - The correction uses volumetric expansion estimated from the data: median 1.68×10⁻⁴ K⁻¹ (IQR 1.23–2.13×10⁻⁴), from 663 compounds with one same-space-group pair each.
    - Volume splits need recorded temperatures on both entries.
    - Volume splits are ignored at near-integer ratios (×1.5, 2, 3, 4), which signal a Z or formula error.
  
  Forms are connected components.
- **Polymorphic:** two or more forms, excluding compounds whose only split is one Sohncke and one non-Sohncke form. That pattern usually means racemate vs enantiopure, i.e. different materials (113 such compounds excluded).

### Results
| Population | Compounds with ≥ 2 entries | Polymorphic | Share (95% CI) |
|---|---|---|---|
| All organic, formula + name (primary) | 1,803 | 613 | 34.0% (31.8–36.2) |
| All organic, InChIKey (cross-check) | 3,549 | 1,221 | 34.4% (32.9–36.0) |
| All organic, formula only (liberal; merges isomers) | 22,211 | 15,397 | 69.3% |
| FDA active moieties (InChIKey match; name + formula for entries without SMILES) | 123 | 72 | 58.5% (49.7–66.9) |

**FDA coverage.**
- The Orange Book's 2,382 ingredient strings give 1,838 unique active moieties with a structure.
- We excluded 98 metal-complex ingredients, because they would map onto their ligand's crystals.
- 295 moieties have a neat crystal structure in COD.
- 361 moieties also appear in COD as salts, solvates, hydrates or cocrystals. Those are further solid forms, not counted as polymorphs.

**Stratified by entries per compound (controls for study intensity).**

| Entries | FDA moieties: share polymorphic (n) | Other organics: share polymorphic (n) |
|---|---|---|
| 2 | 53.7% (67) | 31.3% (2,857) |
| 3–4 | 58.6% (29) | 48.5% (439) |
| 5–9 | 75.0% (16) | 38.7% (119) |
| 10+ | 63.6% (11) | 36.0% (25) |

**Sensitivity (all organic, formula + name).**

| Variant | Share polymorphic |
|---|---|
| Tolerance 2% | 36.6% |
| Tolerance 5% | 31.6% |
| Space-group-only rule | 36.0% |
| Add a Niggli reduced-cell-shape rule (gemmi; may over-split) | 48.1% |
| Counting racemate/enantiopure-only splits | 40.3% |
| Restricted to compounds with ≥ 2 distinct publications | 28.7% |

For FDA moieties, the cell-shape rule gives 70.7% and the ≥ 2 publications restriction gives 57.8% (n = 83).

**Validation on famous polymorphs.**

| Compound | Neat COD entries (structure match) | Forms found | With cell-shape rule | Literature |
|---|---|---|---|---|
| Paracetamol | 21 (30 by name) | 2 (3 by name): Form I P2₁/n, Form II Pbca | 2 | 3 at ambient pressure |
| Carbamazepine | 16 | 3: P2₁/n (III), C2/c (IV), Pbca (V) | 3 | 5 (I–V; Form V: Arlin et al., *Chem. Commun.* 47, 7074, 2011) |
| Ritonavir | 0 (not in COD) | 0 | 0 | 2 (Bauer et al., *Pharm. Res.* 18, 859, 2001) |
| Sulfathiazole | 14, all P2₁/c | 2 | **5** | 5 (I–V) |
| ROY | 4 (9 by name; a 34-entry compression series was correctly filtered) | 1 | 3 | ≥ 10 (Yu, *Acc. Chem. Res.* 43, 1257, 2010) |

The heuristic finds the right forms where COD has them. It undercounts same-space-group, similar-density polymorph families (sulfathiazole; ROY, whose P2₁ and P2₁/c forms are merged by the missed-symmetry rule). The open COD lacks many famous forms, so these counts are lower bounds.

The FDA moieties with the most forms in COD (`stats.fda.most_forms_in_cod`) are chlorpropamide (7), sulfamerazine (5), glycine (5), piroxicam (4), nilutamide (4), remdesivir (4) and carbamazepine (3).

### Failure modes and what this does not show
- **COD is incomplete.** The CSD has far more structures. Absence of a second form in COD is not evidence of monomorphism.
- **Publication bias.** Repeat determinations are often published because a new form was found, which inflates shares among multiply-crystallised compounds. For context, from deliberate industrial screens: Stahly, *Cryst. Growth Des.* 7, 1007 (2007) reports roughly half of ~245 screened compounds as polymorphic (published result).
- **Solvates and hydrates** have different formulas and are not counted. A formula that omits solvent can still create a false polymorph.
- **Salts** are matched through the neutral active moiety. For a salt product, our polymorph count describes the moiety's own crystals, not necessarily the marketed salt.
- **Names.** Different systematic names for one compound do not merge, which undercounts. Generic names could merge isomers; this is guarded by requiring the same formula and by dropping generic names.
- **Phase transitions.** Temperature-induced transitions count as distinct forms. In 497 of the 613 polymorphic compounds, forms were seen within 50 K of each other.
- **Space groups.** Mis-assignment and pseudo-symmetry can split or merge forms.
- **Drugs vs other compounds.** The comparison is confounded by attention: drugs are screened on purpose. Stratifying by number of entries helps but does not remove this.
- **No microgravity claim.** Nothing here concerns microgravity; this is the Earth-side case that solid form is a common, consequential variable.

### Reproduce
```
sbatch cluster/bigdata/matdb-fetch.sbatch        # COD zip (md5) + Orange Book
sbatch cluster/bigdata/matdb-prep.sbatch         # extract SQL members, SQL -> parquet, SMILES -> InChIKeys
sbatch cluster/bigdata/matdb-fda.sbatch          # Orange Book -> PubChem
sbatch cluster/bigdata/matdb-cod-parse.sbatch    # 32-task CIF parse array (burst helper: matdb-cod-parse-burst.sbatch)
sbatch cluster/bigdata/matdb-analyse.sbatch      # -> bigdata/matdb/work/results/cod-polymorphs.json
python3 analysis/bigdata/matdb_finalize.py sacct.txt data/results/bigdata/cod-polymorphs.json <job ids>   # compute block
```

---

## B. MOF membranes: pore windows for lithium sieving

**Question.** How many known MOFs have pore windows (pore-limiting diameter, PLD) in a range useful for separating Li⁺ from Mg²⁺?

**Data.**
- CoRE MOF 2024 public (SI) release v1.1, Zenodo [15055758](https://zenodo.org/records/15055758), CC-BY-4.0: computation-ready descriptor tables ASR (1,372), FSR (1,192) and ION (100), 2,664 records in total. This public release covers only the SI-derived part of CoRE MOF 2024. The CSD-derived structures (about 32,500 of the ~40,800 total) need a CSD licence and are not in it.
- CoRE MOF 2019 v1.1.4, Zenodo [7691378](https://zenodo.org/records/7691378), CC-BY-4.0: ASR descriptor table for 14,142 structures. The descriptors are public even where the CIF is CSD-licensed.
- Descriptors (PLD, LCD, density, ASA) were computed by the CoRE authors with Zeo++; we did not recompute geometry.

**Ion sizes (diameters).**
- Hydrated, from Nightingale, *J. Phys. Chem.* 63, 1381 (1959): Li⁺ 7.64 Å, Na⁺ 7.16 Å, K⁺ 6.62 Å, Mg²⁺ 8.56 Å, Ca²⁺ 8.24 Å.
- Bare (CN 6), from Shannon, *Acta Cryst.* A32, 751 (1976): Li⁺ 1.52 Å, Mg²⁺ 1.44 Å, Na⁺ 2.04 Å, K⁺ 2.76 Å.
- Water kinetic diameter: 2.65 Å (Breck, *Zeolite Molecular Sieves*, 1974).

**Method.**
1. Independent units. CoRE 2019 lists one MOF under several CSD refcodes (e.g. RUBTAK…RUBTAK09 for UiO-66), so we collapsed to 6-letter refcode families and took the median PLD of each: 14,142 structures became 12,863 families. CoRE 2024 lists one MOF in up to three solvent treatments, so we collapsed on the MOFid-v1 string, preferring ASR: 2,664 records became 1,385.
2. Binned the PLD at water (2.65 Å), hydrated Li⁺ (7.64 Å) and hydrated Mg²⁺ (8.56 Å).
3. Reference points: UiO-66 (RUBTAK family) and UiO-67 (WIZMAV family).

**Results (our computation on public data).**

| PLD band | CoRE 2019 (12,863) | CoRE 2024 SI (1,385) |
|---|---|---|
| < 2.65 Å (CoRE only includes PLD ≥ 2.4 Å) | 979 (7.6%) | 64 (4.6%) |
| 2.65–7.64 Å (water passes; hydrated Li⁺ must partly dehydrate) | 10,381 (80.7%) | 1,131 (81.7%) |
| 7.64–8.56 Å (between hydrated Li⁺ and Mg²⁺) | 423 (3.3%) | 40 (2.9%) |
| ≥ 8.56 Å (both hydrated ions fit) | 1,080 (8.4%) | 150 (10.8%) |

- **Headline:** 10,804 of 12,863 distinct MOFs (84.0%, 95% CI 83.4–84.6%) have a PLD between 2.65 and 8.56 Å.
- **UiO-66:** PLD 3.87 Å (10 entries, range 3.79–4.01 Å), LCD 8.73 Å.
- **UiO-67:** PLD 6.67 Å (12 entries, range 5.63–6.72 Å), LCD 12.97 Å.
- **Water stability (2024 set):** the CoRE MOF 2024 authors' ML model predicts water stability ≥ 0.5 for 874 of the 1,171 in-window MOFs. This is a model output, not a measurement.
- We did **not** use one CoRE 2024 entry named "MOF-801" as a reference point. Its LCD of 12.2 Å is inconsistent with MOF-801's published ~5–7 Å cages.

**What this does not show.** This is a geometric pre-screen only, not a selectivity prediction:
- Rigid-framework PLD ignores flexing and swelling in water.
- Selectivity depends on dehydration energetics, charge and functional groups.
- Membrane performance is dominated by growth orientation, intergrowth and defects (missing linkers, grain boundaries), none of which are in crystal-structure databases. Those are what an orbital process might change; that is a **hypothesis**.
- CoRE 2019 and 2024 may share MOFs, so we report them separately rather than summing.

**Jobs.** The small CSVs (about 7 MB) were fetched with `curl` on the login node, and the sbatch re-fetches any that are missing. The screen itself ran as mit_quicktest jobs 26814077 and 26814251; 26814251 produced the file. See `compute.jobs` in the JSON.

**Reproduce.** `sbatch cluster/bigdata/matdb-mof.sbatch` downloads the Zenodo CSVs into `bigdata/matdb/raw/mof` and writes `work/results/mof-pore-screen.json`.

---

## C. Photonic colloidal crystals: why gravity ruins large colloidal crystals

**Evidence level: physics computation, not a measurement.**

**Method.**
- Hard spheres in water at 25 °C (ρ = 997.05 kg m⁻³, η = 0.890 mPa s), with d = 100 nm–5 µm (120 log-spaced sizes).
- Materials: silica (Stöber, 2.0 g cm⁻³), PMMA (1.19 g cm⁻³) and polystyrene (1.05 g cm⁻³).
- Stokes velocity v = 2a²Δρg/(9η).
- Péclet number Pe = (4/3)πa⁴Δρg/kT, which equals v·a/D.
- Gravitational length l_g = a/Pe.
- Time to sink 1 mm = 1 mm / v.
- Pe = 1 crossover d* = 2(3kT/(4πΔρg))^¼, so d* scales as g^(−¼).
- Gravity levels:
  - 1 g;
  - 1×10⁻⁶ g, the ISS quasi-steady design level. NASA PIMS reports measured quasi-steady levels of typically a few µg ([NASA ISS acceleration environment](https://www.nasa.gov/wp-content/uploads/2016/06/acceleration-environment-iss-mini-book_detail-508c.pdf); NTRS 20100042410);
  - 1×10⁻⁷ g, a free-flyer drag level. This is a **placeholder** until the orbit workstream measures it from tracking data.

**Results.**

| d* (Pe = 1) | 1 g | 1×10⁻⁶ g | 1×10⁻⁷ g (placeholder) |
|---|---|---|---|
| silica | 1.12 µm | 35.6 µm | 63.2 µm |
| PMMA | 1.70 µm | 53.7 µm | 95.5 µm |
| polystyrene | 2.35 µm | 74.2 µm | 131.9 µm |

- **300 nm silica** sinks 1 mm in about 5.0 hours at 1 g and in about 570 years at 1×10⁻⁶ g. Its gravitational length is about 30 µm on the ground, far below a 1 mm–1 cm sample. Even where Pe < 1, a ground sample ends up as a dense, compressed, graded sediment.
- **5 µm silica** sinks 1 mm in about 1 minute at 1 g.
- **Published context (not ours).** Hard-sphere colloids that stayed glassy on Earth crystallised in microgravity on STS-73 (Zhu et al., *Nature* 387, 883, 1997).

**Optional literature angle (our computation on public data).**
- Sample: a seeded random sample of 4,000 OpenAlex articles matching colloidal crystal / opal terms.
- Extraction: sphere diameters pulled from abstracts with regexes that need a particle word next to the size; one median per paper.
- Result: 135 papers stated a size. Their median is 335 nm, and 8 papers (5.9%) use spheres above silica's 1 g crossover.
- Interpretation: most experiments use the sub-micron spheres that visible-light photonics needs. The data do not show *why* authors choose sizes.
- How it was run: from a laptop, because OpenAlex's anonymous budget is per IP and the cluster IP is shared. Raw abstracts were not kept in the repo.

**Reproduce.**
- `python3 analysis/bigdata/matdb_colloid_lit.py RAW_DIR colloid_lit.json --n 4000`
- `python3 analysis/bigdata/matdb_colloid.py data/results/bigdata/colloid-sedimentation.json colloid_lit.json`

---

## Partners named (and why)

- **Drug crystals.**
  - CCDC/CSD: the most complete record of drug solid forms. Several famous forms are missing from the open COD.
  - Pharmaceutical solid-form / polymorph-screening teams: the users of form control.
- **MOFs.**
  - CoRE MOF team and CCDC: the data source, and the owner of the licensed CSD structures.
  - NuMat: a commercial MOF producer. Not supported by this dataset; named in the brief.
  - Lithium DLE companies such as Lilac Solutions: end users of Li/Mg separation. Lilac's published approach is ion exchange, not MOF membranes.
- **Colloids.** We name no organisation; this analysis has no data pointing to one.
