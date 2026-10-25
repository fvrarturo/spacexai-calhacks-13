#!/bin/bash
# matdb: parse all ~520k COD CIFs from the bulk zip, one shard per array task.
# <= 16 concurrent 1-CPU tasks (matdb CPU cap).
#SBATCH --job-name=of-matdb-codparse
#SBATCH --partition=mit_normal
#SBATCH --account=mit_general
#SBATCH --time=00:45:00
#SBATCH --cpus-per-task=1
#SBATCH --mem=6G
#SBATCH --array=0-31%16
#SBATCH --output=logs/%x_%A_%a.out
#SBATCH --error=logs/%x_%A_%a.err
set -euo pipefail
ROOT=~/orcd/scratch/orbital-foundry-20261024-01a170b7
W=$ROOT/bigdata/matdb
cd "$W"
mkdir -p work/cif_shards
"$W/env/bin/python" -I "$ROOT/analysis/bigdata/matdb_cod_parse.py" \
  raw/cod/cod-cifs-mysql.zip "$SLURM_ARRAY_TASK_ID" 32 work/cif_shards
