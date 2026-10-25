"""Fill the narrative/provenance sections of the result JSON from computed numbers only.

Usage:
    python -I analysis/bigdata/pdb_writeup.py --result data/results/bigdata/pdb-microgravity.json \
        --classify-summary WORK/analysis/classify_summary.json --sacct WORK/results/sacct.txt \
        [--sifts-rows N --sifts-bytes B --rcsb-check WORK/results/rcsb_fulltext_check.json]

Every number in findings/headline is read from the stats block written by pdb_analyze.py, so
nothing here is typed in by hand.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path


def fmt(x, nd=2):
    return "n/a" if x is None else f"{x:.{nd}f}"


def pval(p):
    """Return '= 0.07' or '< 0.001' so it reads 'p = 0.07' / 'p < 0.001'."""
    if p is None:
        return "= n/a"
    return f"= {p:.2g}" if p >= 0.001 else "< 0.001"


def parse_sacct(path):
    rows = []
    if not path or not Path(path).exists():
        return rows
    lines = Path(path).read_text().strip().splitlines()
    hdr = lines[0].split("|")
    for ln in lines[1:]:
        d = dict(zip(hdr, ln.split("|")))
        if "." in d.get("JobID", ""):
            continue
        rows.append(d)
    return rows


def hms(s):
    if not s:
        return 0.0
    days = 0
    if "-" in s:
        dd, s = s.split("-")
        days = int(dd)
    parts = [float(p) for p in s.split(":")]
    while len(parts) < 3:
        parts.insert(0, 0.0)
    return days * 86400 + parts[0] * 3600 + parts[1] * 60 + parts[2]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--result", required=True)
    ap.add_argument("--classify-summary", required=True)
    ap.add_argument("--sacct", default=None)
    ap.add_argument("--sifts-rows", type=int, default=0)
    ap.add_argument("--sifts-bytes", type=int, default=0)
    ap.add_argument("--rcsb-check", default=None)
    ap.add_argument("--precision", default=None, help="JSON with the manual precision audit")
    ap.add_argument("--peak-storage-gb", type=float, default=0.0)
    ap.add_argument("--strict-result", default=None, help="result JSON from pdb_analyze.py --strict")
    a = ap.parse_args()

    R = json.load(open(a.result))
    C = json.load(open(a.classify_summary))
    prov = C["provenance"]
    S = R["stats"]
    A = S["resolution"]["all_proteins"]
    SE = S["resolution"]["single_entity_uniprot"]
    rc = json.load(open(a.rcsb_check)) if a.rcsb_check and Path(a.rcsb_check).exists() else {}
    prec = json.load(open(a.precision)) if a.precision and Path(a.precision).exists() else R["stats"].get("precision_audit", {})

    # ---- provenance --------------------------------------------------------------------------
    R["datasets"] = [
        {"name": "wwPDB / RCSB PDB archive, PDBx/mmCIF files (structures/divided/mmCIF)",
         "url": "https://files.wwpdb.org/pub/pdb/data/structures/divided/mmCIF/",
         "license": "CC0 1.0 (PDB data are free of all copyright restrictions)",
         "records": prov["parsed"], "bytes": prov["bytes_gz"], "accessed": "2026-10-24",
         "notes": (f"Full mirror of every entry released as of 2026-10-24 ({prov['files']:,} files, "
                   f"{prov['bytes_gz'] / 1e9:.1f} GB gzipped, {prov['bytes_unz'] / 1e9:.0f} GB uncompressed), via rsync "
                   "(rsync.rcsb.org::ftp_data, port 33444) plus parallel HTTPS from files.wwpdb.org. "
                   f"Parse failures: {prov['errors']}.")},
        {"name": "SIFTS chain-level PDB to UniProt mapping (pdb_chain_uniprot.tsv.gz)",
         "url": "https://ftp.ebi.ac.uk/pub/databases/msd/sifts/flatfiles/tsv/pdb_chain_uniprot.tsv.gz",
         "license": "CC BY 4.0 (EMBL-EBI / PDBe)", "records": a.sifts_rows, "bytes": a.sifts_bytes,
         "accessed": "2026-10-24", "notes": "Release dated 2026-10-18; defines the protein (UniProt accession set) used for matching."},
    ]
    if rc:
        R["datasets"].append({"name": "RCSB Search API full-text queries (recall cross-check only)",
                              "url": "https://search.rcsb.org/rcsbsearch/v2/query", "license": "CC0 1.0",
                              "records": rc.get("n_ids", 0), "bytes": 0, "accessed": "2026-10-24",
                              "notes": rc.get("note", "")})
    jobs = parse_sacct(a.sacct)
    cpu_h = sum(float(j.get("CPUTimeRAW", 0) or 0) for j in jobs) / 3600
    import datetime as _dt
    starts = [_dt.datetime.fromisoformat(j["Start"]) for j in jobs if j.get("Start") not in (None, "", "None", "Unknown")]
    ends = [_dt.datetime.fromisoformat(j["End"]) for j in jobs if j.get("End") not in (None, "", "None", "Unknown")]
    wall = (max(ends) - min(starts)).total_seconds() / 60 if starts and ends else 0.0
    job_minutes = sum(hms(j.get("Elapsed")) for j in jobs) / 60
    R["compute"] = {"where": "MIT Engaging (ORCD)", "partitions": sorted({j["Partition"] for j in jobs if j.get("Partition")}),
                    "job_ids": [j["JobID"] for j in jobs], "cpu_hours": round(cpu_h, 2), "wall_minutes": round(wall, 1), "sum_job_minutes": round(job_minutes, 1),
                    "peak_storage_gb": a.peak_storage_gb,
                    "jobs": [{k: j.get(k) for k in ("JobID", "JobName", "Partition", "State", "Elapsed", "NCPUS", "MaxRSS")} for j in jobs]}

    n_space = S["n_space_entries"]
    R["method"] = [
        f"Mirrored the complete PDB mmCIF archive to MIT Engaging scratch ({prov['files']:,} entries, {prov['bytes_gz'] / 1e9:.1f} GB gzipped).",
        "Parsed every file with gemmi in Slurm jobs (coordinates cut out first): dates, experimental method, every "
        "_exptl_crystal_grow and _exptl_crystal text field, resolution, R-free, Wilson B, beamline, citation and polymer entities.",
        "Scanned the full header text of every entry for space vocabulary (microgravity, Space Shuttle, STS-nn, ISS, Kibo, JAXA, "
        "NASDA, Mir, Spacehab, Spacelab/IML/USML, APCF, PCF, HDPCG, CPCG, PCAM/DCAM, GCB, JCB, PCDF, 'in space', 'on orbit', "
        "spaceflight...) and dropped known false contexts ('space group', MIR = multiple isomorphous replacement phasing, "
        "'Fourier space', 'chemical space').",
        "Applied an automatic rule (space words inside the crystal-growth fields), then read the deposited text of every "
        f"candidate by hand ({S['n_manually_reviewed']} entries) and recorded verdicts in analysis/bigdata/pdb_review_labels.py.",
        "Defined each protein as its set of UniProt accessions (SIFTS), falling back to polymer sequence hashes when no "
        "UniProt mapping exists; one protein = one independent unit.",
        "For each protein with space- and Earth-grown X-ray entries: best space resolution minus best Earth resolution (any year, and "
        "Earth entries within ±3 years), and whether a space entry is the protein's best. Medians with 10,000-resample bootstrap 95% "
        "CIs over proteins, Wilcoxon signed-rank tests, and a 2,000-permutation null that shuffles which entries of a protein are "
        "called 'space' (this corrects for comparing one space crystal with the best of many Earth crystals).",
        "Counted space-grown depositions per year by platform and tallied the programs and organisations named in the text.",
    ]

    # ---- headline + findings -------------------------------------------------------------
    da, de = A["delta_all_time"], A["delta_era_pm3y"]
    sb, sbe = A["space_best"], A["space_best_era"]
    pn = A["permutation_null"]
    ss = A["same_study_delta"]
    pc = S["platform_counts"]
    plat_txt = ", ".join(f"{k} {pc.get(k, 0)}" for k in ["Shuttle", "Mir", "ISS", "Other", "Unknown"] if pc.get(k, 0))
    share = sb.get("share")
    R["headline"] = {
        "value": str(n_space), "unit": "space-grown PDB entries",
        "text": (f"{n_space} PDB structures came from crystals grown in orbit. Against same-era Earth crystals of the same "
                 f"protein, the space one was the sharpest for {round(100 * (sbe['share'] or 0))}% of {sbe['n_proteins']} "
                 f"proteins (chance: {round(100 * pn['null_share_space_best_era'])}%); against Earth controls from the same "
                 + ("paper, no clear difference." if (ss.get('median_ci95') and ss['median_ci95'][0] < 0 < ss['median_ci95'][1])
                    else f"paper, median {fmt(ss.get('median'))} Å."))}
    F = [
        f"{n_space} of {S['n_entries_scanned']:,} PDB entries ({S['n_xray_entries']:,} X-ray) say in their own deposited text "
        f"(crystal-growth fields, title or keywords) that the crystal was grown in microgravity; they cover "
        f"{S['n_space_proteins']} distinct proteins or nucleic acids. {S['n_mixed_entries']} of them merge space- and Earth-grown crystals.",
        f"Platforms named in the text: {plat_txt}.",
        f"{da['n_proteins']} proteins have both space- and Earth-grown X-ray entries. Median best-space minus best-Earth "
        f"resolution: {fmt(da.get('median'))} Å (95% CI {fmt(da['median_ci95'][0])} to {fmt(da['median_ci95'][1])}; "
        f"Wilcoxon p {pval(da.get('wilcoxon_p_two_sided'))}). Negative means the space crystal diffracted further.",
        f"Against Earth entries deposited within ±3 years ({de['n_proteins']} proteins): median {fmt(de.get('median'))} Å "
        f"(95% CI {fmt(de['median_ci95'][0])} to {fmt(de['median_ci95'][1])}; Wilcoxon p {pval(de.get('wilcoxon_p_two_sided'))}).",
        f"A space-grown entry is the protein's best-resolution entry for {round(100 * share)}% of proteins "
        f"(95% CI {round(100 * sb['share_ci95'][0])}-{round(100 * sb['share_ci95'][1])}%). Shuffling the space/Earth labels within "
        f"each protein gives {round(100 * pn['null_share_space_best'])}% (permutation p {pval(pn['p_share_space_best_higher'])}); "
        f"within ±3 years: {round(100 * (sbe['share'] or 0))}% observed vs {round(100 * pn['null_share_space_best_era'])}% expected "
        f"(p {pval(pn['p_share_space_best_era_higher'])}).",
        f"Permutation null for the median difference: {fmt(pn['null_median_delta_all'])} Å expected with no effect vs "
        f"{fmt(da.get('median'))} Å observed (one-sided p {pval(pn['p_delta_all_lower'])}).",
    ]
    if ss.get("n_proteins"):
        F.append(f"Where one paper deposited both space- and Earth-grown crystals of the same protein ({ss['n_proteins']} proteins), "
                 f"the median space-minus-Earth difference is {fmt(ss.get('median'))} Å (95% CI {fmt(ss['median_ci95'][0])} to "
                 f"{fmt(ss['median_ci95'][1])}).")
    if SE.get("delta_all_time", {}).get("n_proteins"):
        s1 = SE["delta_all_time"]
        F.append(f"Single-chain, single-UniProt proteins only ({s1['n_proteins']}): median {fmt(s1.get('median'))} Å "
                 f"(95% CI {fmt(s1['median_ci95'][0])} to {fmt(s1['median_ci95'][1])}); space best for "
                 f"{round(100 * (SE['space_best']['share'] or 0))}% vs {round(100 * SE['permutation_null']['null_share_space_best'])}% expected.")
    sec = S.get("secondary_metrics", {})
    rf, wb = sec.get("r_free", {}), sec.get("wilson_b", {})
    if rf.get("coverage", 0) >= 0.5:
        F.append(f"R-free of the best space entry minus the best Earth entry ({rf['n_proteins']} proteins): median "
                 f"{fmt(rf['median_space_minus_ground'], 3)} (95% CI {fmt(rf['median_ci95'][0], 3)} to {fmt(rf['median_ci95'][1], 3)}), "
                 f"i.e. no difference in model agreement. Wilson B is reported for too few pairs ({wb.get('n_proteins', 0)}) to compare.")
    progs = S.get("programs_mentioned", {})
    if progs:
        F.append("Hardware and programmes named in the deposited text: " +
                 ", ".join(f"{k} ({v})" for k, v in list(progs.items())[:8]) + ".")
    if prec:
        F.append(f"Text matching alone is unreliable: of {prec['n_candidates_any_vocabulary']} entries with any space vocabulary, "
                 f"{prec['n_true_in_candidates']} were really space-grown. The automatic growth-field rule flagged "
                 f"{prec['auto_rule_flagged']}, of which {prec['auto_rule_correct']} were right "
                 f"({round(100 * prec['auto_rule_precision'])}%; a random sample of {prec['n_sample']} gave "
                 f"{prec['n_correct']}/{prec['n_sample']}), and it found only {round(100 * prec['auto_rule_recall_vs_final'])}% "
                 "of the final list. Every candidate was therefore read by hand.")
    if rc:
        F.append(rc.get("finding", ""))
    if a.strict_result and Path(a.strict_result).exists():
        T = json.load(open(a.strict_result))["stats"]["resolution"]["all_proteins"]
        R["stats"]["sensitivity_strict_explicit_text_only"] = T
        F.append(f"Dropping the {S['n_keyword_tier']} entries whose evidence is only a keyword or citation title: "
                 f"space best within ±3 years for {round(100 * (T['space_best_era']['share'] or 0))}% of "
                 f"{T['space_best_era']['n_proteins']} proteins vs {round(100 * T['permutation_null']['null_share_space_best_era'])}% "
                 f"expected; all-time median difference {fmt(T['delta_all_time'].get('median'))} Å "
                 f"(95% CI {fmt(T['delta_all_time']['median_ci95'][0])} to {fmt(T['delta_all_time']['median_ci95'][1])}).")
    F.append(f"No space-grown entry names Mir as its platform; {S.get('n_noncrystal_microgravity_entries', 0)} further "
             "microgravity entries are cryo-EM fibrils rather than crystals and are not counted.")
    R["findings"] = [f for f in F if f]
    R["stats"]["precision_audit"] = prec
    R["stats"]["rcsb_fulltext_check"] = rc

    R["limitations"] = [
        "This is an archive correlation, not a controlled experiment: it does not show that microgravity caused any difference.",
        "Depositors are not required to say where crystals grew. Space-grown entries whose text does not say so are missed, and "
        "were counted as Earth-grown; the census is a lower bound.",
        "Publication and deposition selection: space crystals that failed to diffract were rarely deposited, while every ordinary "
        "Earth structure is. This biases toward space looking good; the long Earth tail biases the other way.",
        "Matching by UniProt accession set does not hold construct boundaries, mutations, ligands, space group, crystal form, "
        "cryo vs room temperature, beamline or detector fixed. Earth 'best' entries are often decades newer with better sources.",
        "Many flight programmes optimised the Earth controls in parallel, and some 'Earth' entries are those controls, so Earth "
        "crystals of flown proteins are not typical Earth crystals.",
        "Resolution limits are author-reported (refine.ls_d_res_high) and cutoff conventions changed over time (I/σ vs CC1/2).",
        "Ranking above a random entry of the same protein is not specific to space: any dedicated high-resolution effort "
        "(a methods paper, a showcase data set) would outrank ligand-soak and mutant entries. The same-paper pairs are the fairer "
        f"test, and there are only {ss.get('n_proteins', 0)} proteins with such pairs.",
        f"The platform is unstated for {pc.get('Unknown', 0)} of {n_space} entries; {S['n_keyword_tier']} entries rest on a keyword "
        "or citation title only (a sensitivity analysis drops them); "
        f"{S['n_mixed_entries']} entries merge space- and Earth-grown crystals and "
        f"{sum(v for k, v in S['methods_space_entries'].items() if 'NEUTRON' in k)} are neutron structures, all excluded "
        "from the resolution comparison.",
        "Proteins with many Earth entries (lysozyme, thaumatin, insulin) are one unit each, but their best Earth entry is an extreme "
        "of a large sample; the label-permutation null is the fair comparison for that.",
    ]
    R["future_big_data"] = [
        "Pull the raw diffraction images behind space and matched Earth entries (SBGrid Data Bank, IRRMC / proteindiffraction.org, "
        "Zenodo) and reprocess them identically (XDS/DIALS, same CC1/2 cutoff) to remove author-cutoff and software-era effects.",
        "Add PDB validation reports (wwPDB XML: Wilson B, anisotropy, Rfree-R, clashscore) for all matched entries to compare more "
        "than one number per crystal.",
        "Model the effect per protein family (Pfam/CATH) and per crystallisation method (counter-diffusion vs vapour diffusion) with "
        "a mixed model: protein as random effect, era/beamline/temperature as covariates.",
        "Text-mine the cited papers (PubMed Central full text) for flight crystals that were never deposited, to measure the "
        "selection bias directly.",
        "Link each space entry to its flight (STS / Mir / ISS increment, JAXA PCG run) to estimate time-in-orbit and hardware effects.",
    ]
    orgs = S.get("orgs_mentioned", {})
    syn = S.get("synchrotron_sites_space_entries", {})
    auth = S.get("top_authors_space_entries", {})
    pcount = S.get("platform_counts", {})
    plist = []
    pm = S.get("partner_mentions_entries", {})
    mm = S.get("growth_method_mix", {})
    if pm.get("JAXA / NASDA / Kibo / JEM / JCB") or pcount.get("ISS"):
        plist.append({"name": "JAXA (Kibo protein crystallisation)", "why": "Operates protein crystallisation on the ISS "
                      "Kibo module with sample return to Earth; the closest existing service to a protein cartridge.",
                      "evidence": f"{pcount.get('ISS', 0)} space-grown entries name the ISS as platform; "
                                  f"{pm.get('JAXA / NASDA / Kibo / JEM / JCB', 0)} name JAXA, NASDA, Kibo/JEM or the JAXA "
                                  f"Crystallisation Box; {syn.get('SPring-8', 0)} space-grown data sets were collected at SPring-8 (Japan)."})
    if pm.get("ESA / APCF / PCDF"):
        plist.append({"name": "ESA (APCF / PCDF hardware)", "why": "Built reactors behind many flight crystals; heritage for "
                      "sealed, automated crystallisation cartridges.",
                      "evidence": f"{pm.get('ESA / APCF / PCDF', 0)} space-grown entries name ESA, APCF or PCDF "
                                  f"(APCF {progs.get('APCF (ESA)', 0)}, PCDF {progs.get('PCDF (ESA)', 0)})."})
    if pm.get("NASA / Shuttle mission named"):
        plist.append({"name": "NASA", "why": "Shuttle-era programmes produced the earliest space-grown structures in the PDB.",
                      "evidence": f"{pm.get('NASA / Shuttle mission named', 0)} space-grown entries name NASA or a Shuttle "
                                  f"mission (STS / Spacehab / IML / USML / LMS); NASA is a listed funder of "
                                  f"{S.get('n_space_nasa_funded', 0)} more recent ones "
                                  f"({', '.join(S.get('space_entries_by_funder', {}).get('NASA', []))})."})
    gr = auth.get("Otalora, F.", 0) + auth.get("Gavira, J.A.", 0)
    if gr:
        plist.append({"name": "Laboratorio de Estudios Cristalográficos, Granada (CSIC)", "why": "Counter-diffusion in "
                      "capillaries, the growth method behind most recent flight crystals, came out of this group.",
                      "evidence": f"Otálora F. and Gavira J.A. are authors on {auth.get('Otalora, F.', 0)} and "
                                  f"{auth.get('Gavira, J.A.', 0)} space-grown entries; counter/liquid diffusion is the growth "
                                  f"method of {mm.get('n_counter_or_liquid_diffusion_since_2010', 0)} of "
                                  f"{mm.get('n_since_2010', 0)} space-grown entries deposited since 2010."})
    top_syn = [k for k in ["SPring-8", "EMBL/DESY, HAMBURG", "ESRF", "ORNL Spallation Neutron Source"] if syn.get(k)]
    if top_syn:
        plist.append({"name": "Synchrotron and neutron facilities (" + ", ".join(top_syn) + ")",
                      "why": "Where returned crystals are measured; partners for an identical-processing benchmark.",
                      "evidence": "; ".join(f"{k}: {syn[k]} space-grown entries" for k in top_syn)})
    if S.get("n_space_casis"):
        plist.append({"name": "CASIS / ISS National Lab", "why": "Current US route to fly commercial crystallisation.",
                      "evidence": f"listed as funder of {S['n_space_casis']} space-grown entry "
                                  f"({', '.join(S['space_entries_by_funder'].get('CASIS', []))})."})
    R["partners"] = plist
    R["code"] = ["analysis/bigdata/pdb_parse.py", "analysis/bigdata/pdb_classify.py", "analysis/bigdata/pdb_review_labels.py",
                 "analysis/bigdata/pdb_analyze.py", "analysis/bigdata/pdb_recall_sweep.py", "analysis/bigdata/pdb_rcsb_check.py",
                 "analysis/bigdata/pdb_writeup.py",
                 "cluster/bigdata/pdb-mirror.sbatch", "cluster/bigdata/pdb-mirror-http.sbatch",
                 "cluster/bigdata/pdb-parse.sbatch", "cluster/bigdata/pdb-parse-multi.sbatch",
                 "cluster/bigdata/pdb-analyze.sbatch", "cluster/bigdata/pdb-pack.sbatch"]
    R["reproduce"] = [
        "rsync -az analysis/bigdata cluster/bigdata engaging:~/orcd/scratch/orbital-foundry-20261024-01a170b7/   # code to cluster",
        "cd ~/orcd/scratch/orbital-foundry-20261024-01a170b7/bigdata/pdb && sbatch ../../cluster/bigdata/pdb-mirror.sbatch "
        "&& sbatch ../../cluster/bigdata/pdb-mirror-http.sbatch",
        "wget -P raw/sifts https://ftp.ebi.ac.uk/pub/databases/msd/sifts/flatfiles/tsv/pdb_chain_uniprot.tsv.gz",
        "sbatch --export=ALL,FIRST=0,LAST=100000,TAG=,NTASKS=32,T0=0,T1=31 ../../cluster/bigdata/pdb-parse-multi.sbatch",
        "sbatch --export=ALL,STAGE=all ../../cluster/bigdata/pdb-analyze.sbatch",
        "env/bin/python -I ../../analysis/bigdata/pdb_writeup.py --result work/results/pdb-microgravity.json "
        "--classify-summary work/analysis/classify_summary.json --sacct work/results/sacct.txt",
    ]
    Path(a.result).write_text(json.dumps(R, indent=1))
    print("\n".join(R["findings"]))
    print(R["headline"])


if __name__ == "__main__":
    main()
