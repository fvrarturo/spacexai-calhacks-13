#!/bin/bash
# Orbit workstream, stage 1: reduce every yearly TLE parquet (1990-2026 by default) to small
# aggregate tables (drag object-months, crowding snapshots, threshold crossings). 16 CPUs max.
#SBATCH --job-name=of-orbit-process
#SBATCH --partition=mit_normal
#SBATCH --account=mit_general
#SBATCH --time=02:00:00
#SBATCH --cpus-per-task=16
#SBATCH --mem=160G
#SBATCH --output=logs/%x_%j.out
#SBATCH --error=logs/%x_%j.err
set -euo pipefail
ROOT=${ORBIT_ROOT:-$HOME/orcd/scratch/orbital-foundry-20261024-01a170b7/bigdata/orbit}
CODE=$ROOT/..
module load miniforge
source "$ROOT/env/bin/activate"
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 ARROW_NUM_THREADS=1
YEARS=${YEARS:-1990-2026}
WORKERS=${WORKERS:-10}
date -Is
python -I "$CODE/orbit_process.py" --raw "$ROOT/raw/tle" --satcat "$ROOT/raw/satcat/satcat.csv" \
  --out "$ROOT/work/reduced" --years "$YEARS" --workers "$WORKERS"
date -Is
