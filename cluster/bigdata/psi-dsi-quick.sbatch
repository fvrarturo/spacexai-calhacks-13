#!/bin/bash
#SBATCH --job-name=of-psi-dsiq
#SBATCH --partition=mit_quicktest
#SBATCH --account=mit_general
#SBATCH --time=00:15:00
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=24
#SBATCH --mem=48G
#SBATCH --output=bigdata/psi/logs/%x_%j.out
#SBATCH --error=bigdata/psi/logs/%x_%j.err
# Stream every axial (HR2) DSI frame from the public PSI bucket and compute FFT morphology features.
# One 24-CPU quicktest job runs the 24 shards in parallel; each shard stops cleanly after 13 min and
# resumes where it left off when the job is re-submitted (chain 2-3 of these with --dependency=afterany).
# (mit_normal had >1500 pending jobs; quicktest allows 8 submitted jobs/user, so no 24-task array.)
set -uo pipefail
cd "$SLURM_SUBMIT_DIR"
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1
W=bigdata/psi/work
mkdir -p $W/shards bigdata/psi/logs/shards
for i in $(seq 0 23); do
  bigdata/psi/env/bin/python -I analysis/bigdata/psi_dsi_morph.py process \
    --manifest $W/dsi-hr2-manifest.tsv --mask $W/dsi-artefact-mask.npz --deadline 780 \
    --shard $i --nshards 24 --out $W/shards/dsi-features-$(printf %02d $i).csv \
    >> bigdata/psi/logs/shards/shard-$(printf %02d $i).log 2>&1 &
done
wait
wc -l $W/shards/*.csv | tail -1
