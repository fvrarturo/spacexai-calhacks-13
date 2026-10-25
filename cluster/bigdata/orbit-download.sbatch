#!/bin/bash
# Orbit workstream: download the full Space-Track TLE history mirror (Hugging Face
# juliensimon/space-track-tle-history, 68 yearly parquet files, ~12.5 GB), the CelesTrak
# SATCAT and the GFZ Potsdam F10.7 / Kp / Ap history into scratch.
# Raw TLEs are NEVER re-hosted (Space-Track terms); only aggregates leave the cluster.
#SBATCH --job-name=of-orbit-download
#SBATCH --partition=mit_data_transfer
#SBATCH --account=mit_general
#SBATCH --time=04:00:00
#SBATCH --cpus-per-task=4
#SBATCH --mem=8G
#SBATCH --output=logs/%x_%j.out
#SBATCH --error=logs/%x_%j.err
set -euo pipefail
ROOT=${ORBIT_ROOT:-$HOME/orcd/scratch/orbital-foundry-20261024-01a170b7/bigdata/orbit}
export HF_HOME=$ROOT/raw/hf_home
RAW=$ROOT/raw
mkdir -p "$RAW/tle" "$RAW/satcat" "$RAW/solar" "$HF_HOME" "$ROOT/logs"
date -Is

# 1) SATCAT (CelesTrak) and space weather (GFZ Potsdam; CelesTrak SW-All as a cross-check)
curl -sSfL --retry 5 -o "$RAW/satcat/satcat.csv" https://celestrak.org/pub/satcat.csv
curl -sSfL --retry 5 -o "$RAW/solar/Kp_ap_Ap_SN_F107_since_1932.txt" \
  https://kp.gfz-potsdam.de/app/files/Kp_ap_Ap_SN_F107_since_1932.txt
curl -sSfL --retry 5 -o "$RAW/solar/SW-All.csv" https://celestrak.org/SpaceData/SW-All.csv || true
ls -l "$RAW/satcat" "$RAW/solar"

# 2) TLE history: one parquet per year, 4 parallel streams, resumable
BASE=https://huggingface.co/datasets/juliensimon/space-track-tle-history/resolve/main/data
export BASE RAW
seq 1959 2026 | xargs -P 4 -I{} sh -c \
  'f=tle_{}.parquet; curl -sSfL --retry 8 --retry-delay 5 -C - -o "$RAW/tle/$f" "$BASE/$f" || (sleep 20; curl -sSfL --retry 8 -o "$RAW/tle/$f" "$BASE/$f")'
curl -sSfL -o "$RAW/tle/README.md" https://huggingface.co/datasets/juliensimon/space-track-tle-history/raw/main/README.md
date -Is
echo "tle files: $(ls "$RAW/tle"/*.parquet | wc -l)"
echo "tle bytes: $(stat -c %s "$RAW/tle"/*.parquet | awk "{s+=\$1} END {print s}")"
