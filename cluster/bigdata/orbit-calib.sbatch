#!/bin/bash
# Orbit workstream: calibrate the NRLMSIS 2.1 density route on the Starshine 3 sphere (known m, A).
#SBATCH --job-name=of-orbit-calib
#SBATCH --partition=mit_quicktest
#SBATCH --account=mit_general
#SBATCH --time=00:15:00
#SBATCH --cpus-per-task=2
#SBATCH --mem=16G
#SBATCH --output=logs/%x_%j.out
#SBATCH --error=logs/%x_%j.err
set -euo pipefail
ROOT=${ORBIT_ROOT:-$HOME/orcd/scratch/orbital-foundry-20261024-01a170b7/bigdata/orbit}
module load miniforge
source "$ROOT/env/bin/activate"
python -I "$ROOT/../orbit_calib.py" "$ROOT" "$ROOT/work/orbit_calib.json"
