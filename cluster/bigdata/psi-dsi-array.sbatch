#!/bin/bash
#SBATCH --job-name=of-psi-dsi
#SBATCH --partition=mit_normal
#SBATCH --account=mit_general
#SBATCH --time=02:00:00
#SBATCH --cpus-per-task=1
#SBATCH --mem=3G
#SBATCH --array=0-23%24
#SBATCH --output=bigdata/psi/logs/%x_%A_%a.out
#SBATCH --error=bigdata/psi/logs/%x_%A_%a.err
# Stream every axial (HR2) DSI frame from the public PSI bucket and compute FFT morphology features.
# 24 shards x 1 CPU (<= 24 concurrent CPUs). Nothing but small CSVs is written. Submit from project root.
set -euo pipefail
cd "$SLURM_SUBMIT_DIR"
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1
W=bigdata/psi/work
mkdir -p $W/shards
bigdata/psi/env/bin/python -I analysis/bigdata/psi_dsi_morph.py process \
  --manifest $W/dsi-hr2-manifest.tsv --mask $W/dsi-artefact-mask.npz \
  --shard $SLURM_ARRAY_TASK_ID --nshards 24 --out $W/shards/dsi-features-$(printf %02d $SLURM_ARRAY_TASK_ID).csv
