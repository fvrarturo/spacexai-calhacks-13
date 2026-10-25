#!/bin/bash
#SBATCH --job-name=foundry-fleet
#SBATCH --partition=mit_normal
#SBATCH --account=mit_general
#SBATCH --time=00:05:00
#SBATCH --cpus-per-task=1
#SBATCH --mem=2G
#SBATCH --array=0-23%4
#SBATCH --output=logs/%x_%A_%a.out
#SBATCH --error=logs/%x_%A_%a.err
set -euo pipefail
cd "$SLURM_SUBMIT_DIR"
module load miniforge
export OMP_NUM_THREADS=1
python -m analysis.sweep --index "$SLURM_ARRAY_TASK_ID" --seeds 100 --output data/results/sweep
