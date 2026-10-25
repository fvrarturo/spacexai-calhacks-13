#!/bin/bash
#SBATCH --job-name=of-psi-inventory
#SBATCH --partition=mit_normal
#SBATCH --account=mit_general
#SBATCH --time=01:00:00
#SBATCH --cpus-per-task=2
#SBATCH --mem=8G
#SBATCH --output=bigdata/psi/logs/%x_%j.out
#SBATCH --error=bigdata/psi/logs/%x_%j.err
# Submit from the project root: ~/orcd/scratch/orbital-foundry-20261024-01a170b7/
set -euo pipefail
cd "$SLURM_SUBMIT_DIR"
module load miniforge
W=bigdata/psi/work
mkdir -p "$W"
python -I analysis/bigdata/psi_inventory.py --out "$W/psi-objects.tsv.gz" --threads 12
ls -l "$W"/psi-objects.tsv.gz*
