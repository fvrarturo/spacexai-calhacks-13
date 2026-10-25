#!/bin/bash
# matdb B: CoRE MOF pore-window screen (downloads small Zenodo CSVs, then screens).
#SBATCH --job-name=of-matdb-mof
#SBATCH --partition=mit_quicktest
#SBATCH --account=mit_general
#SBATCH --time=00:10:00
#SBATCH --cpus-per-task=1
#SBATCH --mem=4G
#SBATCH --output=logs/%x_%j.out
#SBATCH --error=logs/%x_%j.err
set -euo pipefail
ROOT=~/orcd/scratch/orbital-foundry-20261024-01a170b7
W=$ROOT/bigdata/matdb
cd "$W"
mkdir -p raw/mof work/results
cd raw/mof
Z24=https://zenodo.org/api/records/15055758/files
Z19=https://zenodo.org/api/records/7691378/files
for f in ASR_data_SI_20250204.csv FSR_data_SI_20250204.csv ION_data_SI_20250204.csv ASR_FSR_check.csv; do
  [ -s core2024_$f ] || curl -sSL --max-time 300 -o core2024_$f $Z24/$f/content
done
for f in 2019-11-01-ASR-internal_14142.csv; do
  [ -s core2019_$f ] || curl -sSL --max-time 300 -o core2019_$f $Z19/$f/content
done
cd "$W"
"$W/env/bin/python" -I "$ROOT/analysis/bigdata/matdb_mof.py" raw/mof work/results/mof-pore-screen.json
