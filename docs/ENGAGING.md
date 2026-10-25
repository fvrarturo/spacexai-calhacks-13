# Engaging runbook

Prepared 24 October 2026 using local `orcd-slurm-jobs` cluster notes and [MIT ORCD documentation](https://orcd-docs.mit.edu/running-jobs/requesting-resources/). Cluster limits must be rechecked live. The reusable SSH connection is verified. CPU smoke job `26809356` completed successfully (11 tests plus five benchmark seeds, exit 0). Sensitivity array `26809678` completed all 24 tasks with exit 0, using at most four one-CPU tasks concurrently. All 24 result files match the local run byte-for-byte. Accounting and file hashes are saved in `data/results/engaging.json` and `data/results/engaging-accounting.txt`. Live limits: `mit_normal` 12 h, `mit_quicktest` 15 min; account `mit_general`.

## Connection

On the Mac, authenticate using the existing SSH alias:

```bash
ssh -MNf -o ControlPersist=8h engaging
ssh -O check engaging
```

This keeps the SSH master alive for eight hours; it does not reserve compute resources. If a master is already running, its original persistence setting may apply. Do not terminate an existing connection used by other work merely to change its duration.

## Inspect before submission

```bash
ssh engaging 'sinfo -s; squeue --me; scontrol show partition mit_normal; sacctmgr -nP show assoc user=$USER format=account,qos,maxsubmit'
```

Read `/etc/claude-code/CLAUDE.md` on the cluster before running jobs. The prepared scripts request one CPU each, use account `mit_general` and cap array concurrency at four. They request 5–15 minutes, not an eight-hour idle allocation. The skill's prior limits were `mit_normal` ≤12 h and `mit_quicktest` ≤15 min; verify these and module availability.

## Sync only this project's files

Choose a project directory without overwriting other work:

```bash
ssh engaging 'mkdir -p ~/orcd/scratch/orbital-foundry-20261024-01a170b7/analysis ~/orcd/scratch/orbital-foundry-20261024-01a170b7/cluster ~/orcd/scratch/orbital-foundry-20261024-01a170b7/data/results ~/orcd/scratch/orbital-foundry-20261024-01a170b7/tests ~/orcd/scratch/orbital-foundry-20261024-01a170b7/logs'
rsync -az analysis cluster tests engaging:~/orcd/scratch/orbital-foundry-20261024-01a170b7/
rsync -az data/published-materials.json engaging:~/orcd/scratch/orbital-foundry-20261024-01a170b7/data/
```

No secrets, `.git`, browser state, original archive or unnecessary raw imagery are transferred. Do not use `--delete`.

## CPU simulation smoke and array

On Engaging:

```bash
cd ~/orcd/scratch/orbital-foundry-20261024-01a170b7
mkdir -p logs
module avail miniforge
sbatch --test-only cluster/smoke.sbatch
sbatch cluster/smoke.sbatch
```

Check completion before submitting the array:

```bash
sacct -j JOB_ID -o jobid,state,elapsed,maxrss,alloctres%40
sbatch --test-only cluster/fleet-array.sbatch
sbatch cluster/fleet-array.sbatch
squeue --me
```

Replace `JOB_ID` with the returned ID. [ORCD job arrays](https://orcd-docs.mit.edu/running-jobs/job-arrays/) explain the array task model. Each scenario writes its own result atomically. Re-running a failed task deterministically recreates that scenario; no GPU is required. Do not run the sweep on a login node.

## NASA pilot

The bitmap QC requires NumPy and Pillow. Create the environment on a small compute allocation:

```bash
srun -p mit_quicktest -c 1 --mem=2G -t 00:10:00 --pty bash
cd ~/orcd/scratch/orbital-foundry-20261024-01a170b7
module load miniforge
python -m venv .venv
.venv/bin/pip install -r analysis/requirements.txt
exit
sbatch --test-only cluster/dsi-pilot.sbatch
sbatch cluster/dsi-pilot.sbatch
```

The pilot lists at most 1,000 objects and fetches 12 images within a 20 MB cap. Expand only after reviewing the run protocol, calibration and control mapping. Future extraction arrays should write one partition per complete run, preserve manifest hashes and reuse checked files. The current CLI does not implement full archive pagination or scientific image segmentation.

## Retrieve compact results

On the Mac, from the project checkout:

```bash
rsync -az engaging:~/orcd/scratch/orbital-foundry-20261024-01a170b7/data/results/sweep/ data/results/sweep/
python3 -m analysis.summarize_sweep
npm run build
```

Keep raw images in scratch. Preserve job IDs, partition, resource requests, environment versions, code hash and exit state alongside results. An SSH login or a successful submission is not evidence of a completed analysis.
