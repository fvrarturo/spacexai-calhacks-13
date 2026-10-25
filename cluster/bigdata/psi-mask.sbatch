#!/bin/bash
#SBATCH --job-name=of-psi-mask
#SBATCH --partition=mit_quicktest
#SBATCH --account=mit_general
#SBATCH --time=00:15:00
#SBATCH --cpus-per-task=4
#SBATCH --mem=12G
#SBATCH --output=bigdata/psi/logs/%x_%j.out
#SBATCH --error=bigdata/psi/logs/%x_%j.err
# Learn the fixed-artefact Fourier mask from 60 axial frames per run (8 runs). Submit from project root.
set -euo pipefail
cd "$SLURM_SUBMIT_DIR"
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1
W=bigdata/psi/work
bigdata/psi/env/bin/python -I analysis/bigdata/psi_dsi_morph.py mask --manifest $W/dsi-hr2-manifest.tsv --per-run 60 --out $W/dsi-artefact-mask.npz
