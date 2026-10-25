#!/bin/bash
#SBATCH --job-name=foundry-smoke
#SBATCH --partition=mit_quicktest
#SBATCH --account=mit_general
#SBATCH --time=00:05:00
#SBATCH --cpus-per-task=1
#SBATCH --mem=1G
#SBATCH --output=logs/%x_%j.out
#SBATCH --error=logs/%x_%j.err
set -euo pipefail
cd "$SLURM_SUBMIT_DIR"
module load miniforge
python -m unittest discover -s tests -p 'test_*.py' -v
python -m analysis.fleet --seeds 5 --output data/results/cluster-smoke.json
