#!/bin/bash
# Logistics workstream (Q1 launch scale, Q2 return cadence): fetch GCAT and rerun the analysis on MIT Engaging.
# Submit from the project root on the cluster:
#   cd ~/orcd/scratch/orbital-foundry-20261024-01a170b7 && sbatch cluster/bigdata/logistics-gcat.sbatch
#SBATCH --job-name=of-logistics-gcat
#SBATCH --account=mit_general
#SBATCH --partition=mit_quicktest
#SBATCH --cpus-per-task=1
#SBATCH --mem=4G
#SBATCH --time=00:15:00
#SBATCH --output=bigdata/logistics/logs/%x-%j.out
#SBATCH --error=bigdata/logistics/logs/%x-%j.err
set -euo pipefail
ROOT=~/orcd/scratch/orbital-foundry-20261024-01a170b7
L=$ROOT/bigdata/logistics
mkdir -p "$L/raw/gcat" "$L/work" "$L/logs"
module load miniforge >/dev/null 2>&1 || true
cd "$ROOT"
echo "host $(hostname)  start $(date -Is)"
# Stdlib only: no venv needed. -I keeps the downloaded data directory off the import path.
python3 -I analysis/bigdata/logistics_gcat.py --raw "$L/raw/gcat" --download --out-dir "$L/work" --accessed "$(date +%F)"
sha256sum "$L/raw/gcat/"*.tsv | awk '{print substr($1,1,16), $2}' > "$L/work/gcat-sha256.txt"
ls -l "$L/work" | head -20
echo "end $(date -Is)"
