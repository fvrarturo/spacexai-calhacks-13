# Appendix: every space-grown protein crystal in the PDB (`pdb`)

**Evidence level:** our computation on public data. **Result file:** `data/results/bigdata/pdb-microgravity.json`
**Entry table:** `data/results/bigdata/pdb-microgravity-entries.csv` (one row per space-grown entry, with its match statistics)

## Question

Across the whole Protein Data Bank, do protein crystals grown in microgravity (Space Shuttle, Mir, ISS, free-flyers) give
better diffraction data than Earth-grown crystals of the same protein? How many space-grown structures exist, from which
programmes, and how has this changed over time?

## Answer in four lines

1. **67 of 261,139 PDB entries** say in their own deposited text that the crystal grew in microgravity (65 space-grown,
   2 that merge space- and Earth-grown crystals). They cover 41 proteins or nucleic acids. 12 name a Shuttle mission,
   14 the ISS, 41 no vehicle; none names Mir.
2. **Against the best Earth crystal of the same protein from any year, space usually loses**: the median best-space
   minus best-Earth resolution is +0.13 Å (95% CI 0.00 to 0.29; 33 proteins; Wilcoxon p = 0.07), and a space entry is the
   protein's all-time best for 33% of proteins (95% CI 18–52%).
3. **Against Earth crystals from the same years, space does well**: median −0.06 Å (95% CI −0.10 to +0.09; 28 proteins),
   and the space crystal is the sharpest for 54% of proteins (95% CI 36–71%), where shuffling the space/Earth labels within
   each protein predicts 21% (permutation p < 0.001).
4. **In the cleanest comparison, same paper, same protein, space vs Earth**, there is no clear difference: median
   −0.04 Å (95% CI −0.30 to +0.19; 14 proteins; Wilcoxon p = 0.73). R-free shows no difference either.

So the archive says space-grown crystals rank well above a typical crystal of the same protein from their era, but it
cannot separate a microgravity effect from the fact that flight projects were dedicated, high-effort crystallisations.

## Data

| Dataset | What we used | Size actually processed |
|---|---|---|
| wwPDB/RCSB PDBx/mmCIF archive, `structures/divided/mmCIF` (CC0) | every entry released by 2026-10-24 | **261,139 files, 92.6 GB gzipped, 393 GB uncompressed**, 0 parse failures |
| SIFTS `pdb_chain_uniprot.tsv.gz` (PDBe, CC BY 4.0), release 2026-10-18 | chain → UniProt accession | 1,047,374 rows, 6.3 MB |
| RCSB Search API full-text search | recall cross-check only | 5 queries, 101 hits |

The mirror was fetched with `rsync -rlpt -z --port=33444 rsync.rcsb.org::ftp_data/structures/divided/mmCIF/` (8 parallel
streams, ~9 MB/s in total because the servers give ~1 MB/s per connection), plus a second job fetching shards from the
end of the list over HTTPS from `files.wwpdb.org` with 48 parallel connections (~25 MB/s). The two met in the middle; the
rsync job then verified every shard. PDBe's rsync server gave the same ~1 MB/s per stream and PDBj's module path was
refused, so they were not used. After parsing, the mirror was packed into one tar per two-letter shard
(`raw/mmCIF_tar/*.tar`, 1,294 files, 92.8 GB) to free ~260k inodes on the shared scratch.

## Pipeline

All code is in `analysis/bigdata/pdb_*.py`; job scripts are `cluster/bigdata/pdb-*.sbatch`.
Cluster folder: `~/orcd/scratch/orbital-foundry-20261024-01a170b7/bigdata/pdb/{raw,work,env,logs}`.

1. **Mirror** (`pdb-mirror.sbatch`, `pdb-mirror-http.sbatch`).
2. **Parse** (`pdb_parse.py` via `pdb-parse.sbatch` / `pdb-parse-multi.sbatch`). Each task takes every 32nd shard. For
   each file it decompresses, cuts the `_atom_site` and `_atom_site_anisotrop` loops, and parses the rest with gemmi 0.7.5.
   It writes one row per entry: methods, deposition and release dates, all `_exptl_crystal_grow` text (method, details,
   apparatus, atmosphere, temperature, pH), `_exptl_crystal` description, refinement resolution, R-free, R-work, mean B,
   `_reflns` resolution, Wilson B, Rmerge, I/σ, completeness, diffraction temperature, source and beamline, detector,
   primary citation (title, journal, year, DOI, PubMed), authors, and polymer entities (type, description, UniProt refs
   from `_struct_ref`, organism, canonical-sequence MD5). It also scans the whole header text for space vocabulary and
   stores every hit with its mmCIF category and a 320-character snippet. To make the scan fast, the long regex runs only
   in small windows around trigger words; on 120 test files it gives identical hits ~24× faster. Batch `a` (shards
   0–639) started while the mirror was still downloading; a fix-up pass (`--skip-parsed`) confirmed no file was missed.
3. **Classify** (`pdb_classify.py`). Known false contexts are dropped: "space group", "Fourier/real/chemical space",
   MIR = multiple isomorphous replacement phasing, journal DOIs (`jcb`, `jem`), and token collisions in sequence and
   chem-comp loops (IML = N-methyl-isoleucine, ISS, MIR ligand codes). Only free-text categories (growth, crystal,
   struct, keywords, citation, diffrn, refine, entry details, related entries) feed the review pool. An automatic rule
   (space words inside the growth fields) labels each candidate. Funding records (`_pdbx_audit_support`) naming
   NASA/JAXA/ESA/CASIS are kept separately as partner evidence only.
4. **Manual review** (`pdb_review_labels.py`). We read all **382 candidates** (every entry with space vocabulary in its
   own text): the 110 the rule labelled space/context/simulated/ground in full, and the 272 labelled "none" through their
   own-text hit snippets. Verdicts: space 65, mixed 2, ground control 12, unclear 11, cryo-EM fibrils 4, false positive
   288. "Space" requires the entry's own text (growth fields, title or keywords) to say its crystal grew in
   microgravity or in space. 7 entries rest on a keyword or citation title only; they are flagged as `keyword_tier`, and
   a sensitivity run drops them.
5. **Match and compare** (`pdb_analyze.py`). A protein = the set of UniProt accessions over all chains (SIFTS; falling
   back to `_struct_ref` UniProt, then to the set of polymer-sequence hashes, which is used for 2 DNA/RNA entries).
   Only X-ray entries with a resolution are compared. The Earth pool excludes every entry labelled
   space/mixed/unclear/cryo-EM; explicit ground controls stay in. Per protein:
   - (a) best space resolution minus best Earth resolution (any year);
   - (b) the same with Earth entries deposited within ±3 years of the best space entry;
   - (c) whether a space entry is the protein's best;
   - same-study pairs: space and Earth entries sharing a primary citation, one best-vs-best difference per study, with
     the median over the protein's studies.
   Statistics are medians with 10,000-resample bootstrap 95% CIs over proteins, two-sided Wilcoxon signed-rank tests,
   and a **2,000-permutation label-shuffle null**. Within each protein the entries are exchangeable under "growth site
   does not matter", so we reassign which n_space entries count as "space" and recompute (a), (b) and (c). This is
   needed because comparing one space crystal with the best of hundreds of Earth crystals (lysozyme has 1,268) makes
   space look worse even when there is no effect.
6. **Write-up** (`pdb_writeup.py`) fills provenance, findings, limitations and partners from computed numbers only.
   `pdb_rcsb_check.py` runs the recall cross-check.

## Precision and recall of identification

- Any space vocabulary in an entry's own text: **67 of 382 candidates (18%) were really space-grown**.
- The automatic growth-field rule flagged 53 entries; **32 were right (60%)**. A random sample of 40 of them (seed 40)
  gave **23/40 (58%)**. 17 of its errors were "MIR" (multiple isomorphous replacement) in `_exptl_crystal.description`.
  The others were LMS (a sulfamoyl-adenosine ligand), "orbital mixing plate", and a crystal size written as "… MM3 IN
  SPACE".
- The rule found only **48%** of the final list. The rest say so only in the title or keywords, use a typo
  ("microgavity", 1WYI), or use flight labels (ISS6A/ISS8A, Spacehab-01, PCDF-PROTEIN mission).
- Near-miss sweep (`pdb_recall_sweep.py`, job 26816613): a looser regex over the text fields of all 261,139 entries ("gravity" with typos, "station", "flight",
  "orbit", "Dragon", "Soyuz"…) found 74 entries outside the pool. All were false (flight muscle, time-of-flight neutron,
  the ORBIT design software, synchrotron "station", gravitropism).
- RCSB full-text search (microgravity, space shuttle, international space station, JAXA, Kibo) returns 101 entries:
  61 are in our list; 30 were in our pool and judged Earth controls, unclear, cryo-EM or false; the 10 outside our pool
  are all false ("space group" titles, shuttle vectors, an author named Jaxa-Chamiec, JAXA as funder). Our scan finds
  6 space-grown entries that full-text search misses (1BEN, 3X2L, 4FMP, 4I5Y, 9KL1, 9L3S).

## Results (all from `pdb-microgravity.json` → `stats`)

| Comparison | Proteins | Median Δ (Å, space − Earth) | 95% CI | Test |
|---|---|---|---|---|
| (a) vs best Earth, any year | 33 | +0.13 | 0.00 to 0.29 | Wilcoxon p = 0.07; null median +0.39 (perm. p < 0.001) |
| (b) vs best Earth within ±3 y | 28 | −0.06 | −0.10 to +0.09 | Wilcoxon p = 0.82; null median +0.30 (perm. p < 0.001) |
| same-paper pairs | 14 | −0.04 | −0.30 to +0.19 | Wilcoxon p = 0.73 |
| (a), single-chain single-UniProt only | 24 | +0.09 | −0.03 to 0.29 | Wilcoxon p = 0.14 |
| (a), explicit-text entries only (strict) | 29 | +0.04 | −0.09 to 0.22 | Wilcoxon p = 0.31 |
| (b), explicit-text entries only (strict) | 24 | −0.10 | −0.16 to +0.02 | Wilcoxon p = 0.16 |

| Share of proteins where a space entry is the best | Observed | 95% CI | Expected with no effect | Perm. p |
|---|---|---|---|---|
| (c) any year | 33% (of 33) | 18–52% | 16% | 0.008 |
| (c) Earth within ±3 y | 54% (of 28) | 36–71% | 21% | < 0.001 |
| (c) strict, ±3 y | 62% (of 24) | 42–79% | 20% | < 0.001 |

Secondary metrics: R-free of the best space entry minus the best Earth entry is +0.005 (95% CI −0.004 to +0.018;
30 proteins, 91% coverage), so no difference. Wilson B exists for only 6 pairs and is not interpreted.

Census by deposition year: Shuttle entries 1995–2002, plus two later depositions of Shuttle-grown crystals (4NIA in 2013, 6COA in 2018). ISS entries start in 2002
(myoglobin, flights 6A/8A) and continue through 2011–2022. The 2024 peak (7 entries) is three neutron MnSOD structures, two DNA/RNA
duplexes, a bioassembler lysozyme and a lipase–penfluridol complex. Counter- or liquid-diffusion is the growth method of 24 of the 35 space entries
deposited since 2010, against 7 of 32 before.

Programmes and organisations named in the text: APCF (ESA) 8, PCF 4, PCDF (ESA) 4, IML/USML/LMS Spacelab 3,
Spacehab 2, JAXA PCG/Kibo 2, GCB/GCF (Granada) 1, JCB 1. 12 entries name ESA/APCF/PCDF, 12 name NASA or a Shuttle mission,
and 4 name JAXA/NASDA/Kibo/JEM/JCB. Data collection sites: SPring-8 15, EMBL/DESY Hamburg 12, ESRF 7, ELETTRA 6, Photon
Factory 5, ORNL SNS (neutron) 4. Funders listed: NASA for 3 space entries (the neutron MnSOD series) and CASIS for 1
(5TY5). In the whole PDB, 166 entries list NASA as a funder.

## What this does not show

- **Not causal.** This is an archive correlation, not a controlled experiment.
- **Lower-bound census.** Depositors need not say where crystals grew, so unlabelled space crystals are missed and were
  counted as Earth-grown.
- **Selection.** Failed flight crystals were rarely deposited; flight proteins were chosen because they crystallise well,
  and flight teams often optimised the Earth controls too. Ranking above a random same-protein entry is also what any
  dedicated high-resolution effort achieves against ligand soaks and mutants. The same-paper pairs are the fairer test,
  and with 14 proteins they are underpowered.
- **Matching is coarse.** A UniProt set does not fix construct, mutation, ligand, crystal form, temperature (room
  temperature vs cryo), beamline, detector or the resolution-cutoff convention (I/σ vs CC½). The best Earth entries are
  often decades newer.
- **Platform unstated** for 41 of 67 entries. Mixed (2) and neutron (5) entries are excluded from the resolution
  comparison.

## Job accounting (MIT Engaging, account `mit_general`)

| Job | Name | Partition | CPUs | Elapsed | State |
|---|---|---|---|---|---|
| 26812993 | of-pdb-mirror (rsync, 8 streams) | mit_data_transfer | 8 | 00:33:03 | COMPLETED |
| 26814481 | of-pdb-mirror-http (48 HTTPS streams) | mit_data_transfer | 4 | 00:07:23 | CANCELLED by us once the two mirrors met |
| 26813881_0–3 | of-pdb-parse (array, first 4 tasks) | mit_normal | 1 each | 06:23 / 07:06 / 07:53 / 05:58 | COMPLETED |
| 26813881_4–31 | of-pdb-parse (rest of array) | mit_normal | 1 | – | CANCELLED by us (slow scheduling); rerun as 26814652 |
| 26814652 | of-pdb-parse batch a (28 tasks, xargs −P16) | mit_quicktest | 16 | 00:01:46 | COMPLETED |
| 26815259 | of-pdb-parse batch b (32 tasks, after mirror) | mit_quicktest | 16 | 00:03:07 | COMPLETED |
| 26815943 | of-pdb-fixup (skip-parsed check; 0 missing) | mit_quicktest | 1 | 00:00:03 | COMPLETED |
| 26816122 | of-pdb-classify (srun) | mit_quicktest | 2 | 00:02:14 | FAILED (output pipe closed by `head`); rerun in 26817195 |
| 26816613 | of-pdb-recall (near-miss sweep) | mit_quicktest | 1 | 00:00:40 | COMPLETED |
| 26817195 | of-pdb-analyze (classify + analyze) | mit_quicktest | 2 | 00:02:58 | COMPLETED |
| 26817670 | of-pdb-pack (tar per shard) | mit_data_transfer | 2 | 00:05:47 | COMPLETED |
| 26817788, 26818180, 26818492, 26818724 | of-pdb-analyze (analyze + strict reruns; 26818724 is final) | mit_quicktest | 2 | 1–2 min each | COMPLETED |
| 26813253, 26813438, 26813910, 26814079, 26815026 | of-pdb-test / classify-test | mit_quicktest | 1–2 | < 1 min | COMPLETED |

Total: 7.3 CPU-hours over 79 minutes of wall-clock time (31 jobs); at most 30 CPUs at once; peak scratch about 93 GB.
`compute.jobs` in the result file has the exact `sacct` rows.

## Reproduce

```bash
# from the repo root on the Mac
rsync -az analysis/bigdata engaging:~/orcd/scratch/orbital-foundry-20261024-01a170b7/analysis/
rsync -az cluster/bigdata  engaging:~/orcd/scratch/orbital-foundry-20261024-01a170b7/cluster/
ssh engaging
cd ~/orcd/scratch/orbital-foundry-20261024-01a170b7/bigdata/pdb
module load miniforge && python -m venv env && PIP_CACHE_DIR=~/orcd/scratch/pip_cache env/bin/pip install gemmi pandas pyarrow scipy numpy
mkdir -p raw/sifts work logs && wget -P raw/sifts https://ftp.ebi.ac.uk/pub/databases/msd/sifts/flatfiles/tsv/pdb_chain_uniprot.tsv.gz
sbatch ../../cluster/bigdata/pdb-mirror.sbatch          # writes work/shards.txt, then rsyncs all shards
sbatch ../../cluster/bigdata/pdb-mirror-http.sbatch     # optional second stream from the end of the list
sbatch --dependency=afterok:<mirror job> --export=ALL,FIRST=0,LAST=100000,TAG=,NTASKS=32,T0=0,T1=31 \
       ../../cluster/bigdata/pdb-parse-multi.sbatch
sbatch --export=ALL,STAGE=all ../../cluster/bigdata/pdb-analyze.sbatch      # classify + analyze + strict run
sbatch ../../cluster/bigdata/pdb-pack.sbatch           # optional: pack the mirror into per-shard tars
# back on the Mac: pull work/results and work/analysis/{classify_summary.json,candidates_final.csv}, then
python3 analysis/bigdata/pdb_rcsb_check.py --entries <pulled>/pdb-microgravity-entries.csv \
        --labels-csv <pulled>/candidates_final.csv --out <pulled>/rcsb_fulltext_check.json
cp <pulled>/pdb-microgravity.json <pulled>/pdb-microgravity-entries.csv data/results/bigdata/
python3 analysis/bigdata/pdb_writeup.py --result data/results/bigdata/pdb-microgravity.json \
        --classify-summary <pulled>/classify_summary.json --sacct <pulled>/sacct.txt \
        --sifts-rows 1047374 --sifts-bytes 6293000 --rcsb-check <pulled>/rcsb_fulltext_check.json \
        --strict-result <pulled>/pdb-microgravity-strict.json --peak-storage-gb 92.8
```

The mirror is a moving target (the PDB adds about 300 entries a week), so counts from a later mirror will differ slightly.
The manual verdicts in `pdb_review_labels.py` cover the 382 candidates from the 2026-10-24 mirror; new candidates in a
later mirror would keep their automatic label until someone reads them.

## Extending it

- Reprocess the raw diffraction images behind space entries and their matched Earth entries identically (SBGrid Data
  Bank, IRRMC/proteindiffraction.org, Zenodo), with the same XDS/DIALS pipeline and CC½ cutoff. This removes
  author-cutoff and software-era effects.
- Add the wwPDB validation XML (Wilson B, anisotropy, R-free − R, clashscore) for all matched entries.
- Fit a mixed model with protein as a random effect and era, temperature, beamline and growth method (counter-diffusion
  vs vapour diffusion) as covariates, then break the effect down by protein family (Pfam/CATH).
- Text-mine PubMed Central for flight crystals that were never deposited, to measure the selection bias directly.
- Link each entry to its flight (STS number, ISS increment, JAXA PCG run) to study time in orbit and hardware.
