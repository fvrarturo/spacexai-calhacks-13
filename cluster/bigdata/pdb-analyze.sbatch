#!/bin/bash
# Merge parsed shards, flag space-grown entries, run the matched comparison.
# STAGE=classify (merge + candidates.csv) or STAGE=analyze (stats + result JSON/CSV) or STAGE=all
#SBATCH --job-name=of-pdb-analyze
#SBATCH --partition=mit_normal
#SBATCH --account=mit_general
#SBATCH --time=01:00:00
#SBATCH --cpus-per-task=2
#SBATCH --mem=24G
#SBATCH --output=logs/%x_%j.out
#SBATCH --error=logs/%x_%j.err
set -euo pipefail
ROOT=${PDB_ROOT:-$HOME/orcd/scratch/orbital-foundry-20261024-01a170b7/bigdata/pdb}
CODE=$HOME/orcd/scratch/orbital-foundry-20261024-01a170b7/analysis/bigdata
cd "$ROOT"
STAGE=${STAGE:-all}
if [[ $STAGE == classify || $STAGE == all ]]; then
  env/bin/python -I "$CODE/pdb_classify.py" --parsed work/parsed --out work/analysis
fi
if [[ $STAGE == analyze || $STAGE == all ]]; then
  mkdir -p work/results
  META=""; [[ -f work/results/meta.json ]] && META="--meta work/results/meta.json"
  env/bin/python -I "$CODE/pdb_analyze.py" --work work/analysis --sifts raw/sifts/pdb_chain_uniprot.tsv.gz \
    --labels "$CODE/pdb_review_labels.py" --out-json work/results/pdb-microgravity.json \
    --out-csv work/results/pdb-microgravity-entries.csv $META
  # sensitivity: only entries whose growth text or title states space growth (drops keyword-only cases)
  env/bin/python -I "$CODE/pdb_analyze.py" --work work/analysis --sifts raw/sifts/pdb_chain_uniprot.tsv.gz \
    --labels "$CODE/pdb_review_labels.py" --out-json work/results/pdb-microgravity-strict.json \
    --out-csv work/results/strict-entries.csv --strict > /dev/null
fi
