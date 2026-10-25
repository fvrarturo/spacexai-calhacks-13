#!/bin/bash
# matdb: small prep jobs (extract COD MySQL members from the zip; SQL table -> parquet;
# COD SMILES -> InChIKeys). Run after matdb-fetch.sbatch.
#SBATCH --job-name=of-matdb-prep
#SBATCH --partition=mit_quicktest
#SBATCH --account=mit_general
#SBATCH --time=00:15:00
#SBATCH --cpus-per-task=8
#SBATCH --mem=24G
#SBATCH --output=logs/%x_%j.out
#SBATCH --error=logs/%x_%j.err
set -euo pipefail
ROOT=~/orcd/scratch/orbital-foundry-20261024-01a170b7
W=$ROOT/bigdata/matdb
cd "$W"
PY="$W/env/bin/python -I"
$PY $ROOT/analysis/bigdata/matdb_cod_extract_sql.py raw/cod/cod-cifs-mysql.zip raw/cod
$PY $ROOT/analysis/bigdata/matdb_cod_sql.py raw/cod work/cod_sql.parquet
$PY $ROOT/analysis/bigdata/matdb_cod_inchi.py raw/cod/mysql__smiles.txt work/cod_inchikeys.parquet --procs 8
