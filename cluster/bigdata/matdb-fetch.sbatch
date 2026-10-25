#!/bin/bash
# matdb: download the COD bulk archive (one 27 GB zip: all CIFs + MySQL dump)
# and the FDA Orange Book on the data-transfer partition.
#SBATCH --job-name=of-matdb-fetch
#SBATCH --partition=mit_data_transfer
#SBATCH --account=mit_general
#SBATCH --time=06:00:00
#SBATCH --cpus-per-task=4
#SBATCH --mem=4G
#SBATCH --output=logs/%x_%j.out
#SBATCH --error=logs/%x_%j.err
set -euo pipefail
ROOT=~/orcd/scratch/orbital-foundry-20261024-01a170b7
W=$ROOT/bigdata/matdb
cd "$W"
mkdir -p raw/cod raw/fda
# FDA Orange Book (products.txt inside a zip) - small, do first
[ -s raw/fda/orange_book.zip ] || curl -sSL --max-time 600 -o raw/fda/orange_book.zip "https://www.fda.gov/media/76860/download" || echo "orange book fetch failed"
# COD bulk archive, md5 from https://www.crystallography.net/archives/md5sum.dat
"$W/env/bin/python" -I "$ROOT/analysis/bigdata/matdb_fetch.py" \
  https://www.crystallography.net/archives/cod-cifs-mysql.zip raw/cod/cod-cifs-mysql.zip \
  --threads 4 --chunk-mb 64 --md5 78e49ae4254823a948dd87b25a38cee4
ls -l raw/cod raw/fda
