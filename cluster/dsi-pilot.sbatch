#!/bin/bash
#SBATCH --job-name=foundry-dsi
#SBATCH --partition=mit_normal
#SBATCH --account=mit_general
#SBATCH --time=00:15:00
#SBATCH --cpus-per-task=1
#SBATCH --mem=2G
#SBATCH --output=logs/%x_%j.out
#SBATCH --error=logs/%x_%j.err
set -euo pipefail
cd "$SLURM_SUBMIT_DIR"
# Pre-create this environment on a compute allocation, as documented in ENGAGING.md.
source .venv/bin/activate
python -m analysis.psi inventory
python -m analysis.psi fetch --count 12 --max-bytes 20000000
python -m analysis.psi qc
