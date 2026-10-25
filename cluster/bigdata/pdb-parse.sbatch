#!/bin/bash
# Parse the mirrored mmCIF archive: 32 array tasks, each takes every 32nd two-letter shard
# of shards[FIRST:LAST] (the ordered list written by the mirror job). Run in two batches so
# parsing of finished shards can start while the mirror is still downloading the rest.
#   sbatch --export=ALL,FIRST=0,LAST=600,TAG=a cluster/bigdata/pdb-parse.sbatch
#   sbatch --export=ALL,FIRST=600,LAST=100000,TAG=b --dependency=afterok:<mirror job> cluster/bigdata/pdb-parse.sbatch
#SBATCH --job-name=of-pdb-parse
#SBATCH --partition=mit_normal
#SBATCH --account=mit_general
#SBATCH --time=02:00:00
#SBATCH --cpus-per-task=1
#SBATCH --mem=6G
#SBATCH --array=0-31
#SBATCH --output=logs/%x_%A_%a.out
#SBATCH --error=logs/%x_%A_%a.err
set -euo pipefail
ROOT=${PDB_ROOT:-$HOME/orcd/scratch/orbital-foundry-20261024-01a170b7/bigdata/pdb}
CODE=$HOME/orcd/scratch/orbital-foundry-20261024-01a170b7/analysis/bigdata
cd "$ROOT"
export OMP_NUM_THREADS=1
env/bin/python -I "$CODE/pdb_parse.py" --mirror raw/mmCIF --out work/parsed \
  --shards-file work/shards.txt --first "${FIRST:-0}" --last "${LAST:-100000}" --tag "${TAG:-}" \
  --task "$SLURM_ARRAY_TASK_ID" --ntasks "${NTASKS:-$SLURM_ARRAY_TASK_COUNT}"
