#!/bin/bash
# Mirror the full wwPDB/RCSB mmCIF archive (divided layout) into scratch.
# 8 parallel rsync streams, one per group of two-letter shard directories.
#SBATCH --job-name=of-pdb-mirror
#SBATCH --partition=mit_data_transfer
#SBATCH --account=mit_general
#SBATCH --time=06:00:00
#SBATCH --cpus-per-task=8
#SBATCH --mem=8G
#SBATCH --output=logs/%x_%j.out
#SBATCH --error=logs/%x_%j.err
set -euo pipefail
ROOT=${PDB_ROOT:-$HOME/orcd/scratch/orbital-foundry-20261024-01a170b7/bigdata/pdb}
DEST=$ROOT/raw/mmCIF
mkdir -p "$DEST" "$ROOT/logs"
SRC=rsync.rcsb.org::ftp_data/structures/divided/mmCIF
date -Is
# list shard directories
rsync --list-only --port=33444 "$SRC/" | awk '$1 ~ /^d/ && $5 != "." {print $5}' > "$ROOT/work/shards.txt"
echo "shards: $(wc -l < "$ROOT/work/shards.txt")"
export DEST SRC
cat "$ROOT/work/shards.txt" | xargs -P 8 -I{} sh -c \
  'rsync -rlpt -z --port=33444 --timeout=300 "$SRC/{}/" "$DEST/{}/" || (sleep 10; rsync -rlpt -z --port=33444 --timeout=300 "$SRC/{}/" "$DEST/{}/")'
date -Is
echo "files: $(find "$DEST" -maxdepth 2 -name '*.cif.gz' | wc -l)"
