#!/bin/bash
# matdb: FDA Orange Book ingredients -> PubChem structures (network-bound, 1 CPU).
#SBATCH --job-name=of-matdb-fda
#SBATCH --partition=mit_data_transfer
#SBATCH --account=mit_general
#SBATCH --time=01:30:00
#SBATCH --cpus-per-task=1
#SBATCH --mem=4G
#SBATCH --output=logs/%x_%j.out
#SBATCH --error=logs/%x_%j.err
set -euo pipefail
ROOT=~/orcd/scratch/orbital-foundry-20261024-01a170b7
W=$ROOT/bigdata/matdb
cd "$W"
mkdir -p raw/fda/ob work
[ -s raw/fda/ob/products.txt ] || (cd raw/fda/ob && unzip -o -q ../orange_book.zip)
"$W/env/bin/python" -I "$ROOT/analysis/bigdata/matdb_fda_pubchem.py" \
  raw/fda/ob/products.txt work/pubchem_cache.json work/fda_ingredients.parquet
