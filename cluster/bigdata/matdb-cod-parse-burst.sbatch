#!/bin/bash
# matdb: helper for the CIF-parse array when mit_normal is congested. Runs the
# not-yet-done shards (highest index first) in parallel on mit_quicktest; shards
# already written by the array are skipped. Same code, same outputs.
#SBATCH --job-name=of-matdb-codparse-burst
#SBATCH --partition=mit_quicktest
#SBATCH --account=mit_general
#SBATCH --time=00:15:00
#SBATCH --cpus-per-task=14
#SBATCH --mem=60G
#SBATCH --output=logs/%x_%j.out
#SBATCH --error=logs/%x_%j.err
set -euo pipefail
ROOT=~/orcd/scratch/orbital-foundry-20261024-01a170b7
W=$ROOT/bigdata/matdb
cd "$W"
mkdir -p work/cif_shards
seq 31 -1 0 | xargs -P 14 -I{} "$W/env/bin/python" -I "$ROOT/analysis/bigdata/matdb_cod_parse.py" \
  raw/cod/cod-cifs-mysql.zip {} 32 work/cif_shards
