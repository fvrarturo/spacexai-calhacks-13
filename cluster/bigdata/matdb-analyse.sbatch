#!/bin/bash
# matdb A: polymorphism analysis over the parsed COD + FDA tables.
#SBATCH --job-name=of-matdb-analyse
#SBATCH --partition=mit_quicktest
#SBATCH --account=mit_general
#SBATCH --time=00:15:00
#SBATCH --cpus-per-task=2
#SBATCH --mem=32G
#SBATCH --output=logs/%x_%j.out
#SBATCH --error=logs/%x_%j.err
set -euo pipefail
ROOT=~/orcd/scratch/orbital-foundry-20261024-01a170b7
W=$ROOT/bigdata/matdb
cd "$W"
mkdir -p work/results
"$W/env/bin/python" -I "$ROOT/analysis/bigdata/matdb_cod_polymorph.py" work work/results/cod-polymorphs.json
