#!/bin/bash
# ClinicalTrials.gov full-registry route analysis (logistics workstream, demand signals).
#
# Two stages, same script:
#   download (1 CPU):  sbatch -c 1 --mem=2G  -J of-logistics-ctgov-dl    cluster/bigdata/logistics-ctgov.sbatch download
#   parse    (6 CPUs): sbatch -c 6 --mem=24G -J of-logistics-ctgov-parse --dependency=afterok:<dl job> cluster/bigdata/logistics-ctgov.sbatch parse
#
# The bulk zip is streamed member-by-member by analysis/bigdata/logistics_ctgov.py; it is never fully extracted.
#SBATCH --account=mit_general
#SBATCH --partition=mit_normal
#SBATCH --time=02:00:00
#SBATCH --output=/home/%u/orcd/scratch/orbital-foundry-20261024-01a170b7/bigdata/logistics/logs/%x-%j.out
#SBATCH --error=/home/%u/orcd/scratch/orbital-foundry-20261024-01a170b7/bigdata/logistics/logs/%x-%j.err
set -euo pipefail

ROOT=$HOME/orcd/scratch/orbital-foundry-20261024-01a170b7
BD=$ROOT/bigdata/logistics
RAW=$BD/raw/ctgov
WORK=$BD/work
mkdir -p "$RAW" "$WORK" "$BD/logs"
MODE=${1:-parse}
echo "mode=$MODE host=$(hostname) start=$(date -Is) cpus=${SLURM_CPUS_PER_TASK:-1}"

if [ "$MODE" = "download" ]; then
  ZIP=$RAW/ctg-studies.json.zip
  curl -sS -L --retry 5 --retry-delay 10 -o "$ZIP.part" \
    "https://clinicaltrials.gov/api/v2/studies/download?format=json.zip"
  mv "$ZIP.part" "$ZIP"
  date -Is > "$RAW/ctg-studies.accessed.txt"
  ls -l "$ZIP"
  sha256sum "$ZIP" | tee "$RAW/ctg-studies.sha256"
  python3 -c "import zipfile,sys; z=zipfile.ZipFile(sys.argv[1]); n=z.infolist(); print('members',len(n),'uncompressed_bytes',sum(i.file_size for i in n))" "$ZIP"
elif [ "$MODE" = "parse" ]; then
  module load miniforge
  python3 -I "$ROOT/analysis/bigdata/logistics_ctgov.py" \
    --zip "$RAW/ctg-studies.json.zip" \
    --out "$WORK/ctgov-routes.json" \
    --samples "$WORK/ctgov-route-samples.json" \
    --workers "${SLURM_CPUS_PER_TASK:-6}"
else
  echo "unknown mode $MODE" >&2; exit 2
fi
echo "end=$(date -Is)"
