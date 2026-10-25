#!/bin/bash
# Second mirror stream: parallel HTTPS from files.wwpdb.org, walking the shard list from the END,
# so it meets the rsync job (pdb-mirror.sbatch) in the middle. Per-connection throughput from the
# PDB servers is ~1 MB/s, so many parallel connections are what make a 75 GB mirror feasible.
#SBATCH --job-name=of-pdb-mirror-http
#SBATCH --partition=mit_data_transfer
#SBATCH --account=mit_general
#SBATCH --time=04:00:00
#SBATCH --cpus-per-task=4
#SBATCH --mem=4G
#SBATCH --output=logs/%x_%j.out
#SBATCH --error=logs/%x_%j.err
set -uo pipefail
ROOT=${PDB_ROOT:-$HOME/orcd/scratch/orbital-foundry-20261024-01a170b7/bigdata/pdb}
DEST=$ROOT/raw/mmCIF
BASE=https://files.wwpdb.org/pub/pdb/data/structures/divided/mmCIF
PAR=${PAR:-48}
mkdir -p "$ROOT/work/http_lists"
date -Is
tac "$ROOT/work/shards.txt" | while read -r sh; do
  # stop when the rsync job has already reached this shard (it has every file of shards it finished)
  lst=$ROOT/work/http_lists/$sh.txt
  rsync --list-only --port=33444 "rsync.rcsb.org::ftp_data/structures/divided/mmCIF/$sh/" 2>/dev/null \
    | awk '/cif.gz/{print $5}' > "$lst"
  mkdir -p "$DEST/$sh"
  need=$(cd "$DEST/$sh" && comm -23 <(sort "$lst") <(ls | sort) | wc -l)
  if [[ $need -eq 0 ]]; then echo "$sh complete"; continue; fi
  (cd "$DEST/$sh" && comm -23 <(sort "$lst") <(ls | sort) | \
     xargs -P "$PAR" -I{} sh -c 'curl -s -f -R --retry 3 -o ".{}.part" "'"$BASE/$sh"'/{}" && mv ".{}.part" "{}"')
  echo "$sh fetched $need"
done
date -Is
