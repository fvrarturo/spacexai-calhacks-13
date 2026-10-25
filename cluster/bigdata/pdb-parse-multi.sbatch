#!/bin/bash
# Same work as pdb-parse.sbatch, but runs parse tasks T0..T1 (of NTASKS) inside ONE allocation with
# xargs -P, because mit_quicktest caps a user at 8 submitted jobs and mit_normal arrays were slow
# to schedule tonight (1,500+ pending jobs).
#   sbatch --export=ALL,FIRST=0,LAST=640,TAG=a,NTASKS=32,T0=4,T1=31 cluster/bigdata/pdb-parse-multi.sbatch
#SBATCH --job-name=of-pdb-parse
#SBATCH --partition=mit_quicktest
#SBATCH --account=mit_general
#SBATCH --time=00:15:00
#SBATCH --cpus-per-task=16
#SBATCH --mem=64G
#SBATCH --output=logs/%x_%j.out
#SBATCH --error=logs/%x_%j.err
set -euo pipefail
ROOT=${PDB_ROOT:-$HOME/orcd/scratch/orbital-foundry-20261024-01a170b7/bigdata/pdb}
CODE=$HOME/orcd/scratch/orbital-foundry-20261024-01a170b7/analysis/bigdata
cd "$ROOT"
export OMP_NUM_THREADS=1 CODE FIRST LAST TAG NTASKS
seq "${T0:-0}" "${T1:-31}" | xargs -P "$SLURM_CPUS_PER_TASK" -I{} sh -c \
  'env/bin/python -I "$CODE/pdb_parse.py" --mirror raw/mmCIF --out work/parsed --shards-file work/shards.txt \
     --first "$FIRST" --last "$LAST" --tag "$TAG" --task {} --ntasks "$NTASKS"'
