#!/bin/bash
# Orbit workstream, stage 2: aggregate the per-year reductions (drag g-levels by altitude and
# solar activity, density routes incl. NRLMSIS 2.1, lifetime simulation, Kaplan-Meier, crowding).
#SBATCH --job-name=of-orbit-analyze
#SBATCH --partition=mit_quicktest
#SBATCH --account=mit_general
#SBATCH --time=00:15:00
#SBATCH --cpus-per-task=4
#SBATCH --mem=48G
#SBATCH --output=logs/%x_%j.out
#SBATCH --error=logs/%x_%j.err
set -euo pipefail
ROOT=${ORBIT_ROOT:-$HOME/orcd/scratch/orbital-foundry-20261024-01a170b7/bigdata/orbit}
CODE=$ROOT/..
module load miniforge
source "$ROOT/env/bin/activate"
export OMP_NUM_THREADS=4
date -Is
python -I "$CODE/orbit_analyze.py" "$ROOT" "$ROOT/work/orbit_agg.json"
date -Is
