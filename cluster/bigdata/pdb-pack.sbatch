#!/bin/bash
# After parsing: pack the 261k-file mirror into one uncompressed tar per two-letter shard
# (files are already gzipped), cutting our file count on shared scratch from ~261k to ~1.3k.
# Re-parse later with: tar -xf raw/mmCIF_tar/<shard>.tar -C raw/mmCIF
#SBATCH --job-name=of-pdb-pack
#SBATCH --partition=mit_data_transfer
#SBATCH --account=mit_general
#SBATCH --time=03:00:00
#SBATCH --cpus-per-task=2
#SBATCH --mem=4G
#SBATCH --output=logs/%x_%j.out
#SBATCH --error=logs/%x_%j.err
set -euo pipefail
ROOT=${PDB_ROOT:-$HOME/orcd/scratch/orbital-foundry-20261024-01a170b7/bigdata/pdb}
cd "$ROOT/raw"
mkdir -p mmCIF_tar
n=0
while read -r sh; do
  [[ -d mmCIF/$sh ]] || continue
  tar -cf "mmCIF_tar/$sh.tar.part" -C mmCIF "$sh"
  want=$(ls "mmCIF/$sh" | wc -l); got=$(tar -tf "mmCIF_tar/$sh.tar.part" | grep -c 'cif.gz$' || true)
  if [[ $want -eq $got ]]; then mv "mmCIF_tar/$sh.tar.part" "mmCIF_tar/$sh.tar"; rm -rf "mmCIF/$sh"; n=$((n+1)); else echo "MISMATCH $sh $want $got"; fi
done < ../work/shards.txt
echo "packed $n shards"; date -Is
