#!/usr/bin/env python3
"""matdb: fill the `compute` block of result JSONs from Slurm accounting.

Input: a `sacct -P -X -o jobid,jobname,partition,state,elapsedraw,ncpus,maxrss` dump.
Usage: python3 matdb_finalize.py SACCT_TXT RESULT_JSON JOBID_PREFIX[,JOBID_PREFIX...] [--storage-gb X]
"""
import json
import sys


def main():
    sacct, res_path, ids = sys.argv[1], sys.argv[2], sys.argv[3].split(",")
    storage = float(sys.argv[sys.argv.index("--storage-gb") + 1]) if "--storage-gb" in sys.argv else None
    rows = []
    for line in open(sacct):
        f = line.rstrip("\n").split("|")
        if len(f) < 6 or f[0] == "JobID":
            continue
        if any(f[0] == i or f[0].startswith(i + "_") for i in ids):
            rows.append({"jobid": f[0], "name": f[1], "partition": f[2], "state": f[3],
                         "elapsed_s": int(f[4] or 0), "ncpus": int(f[5] or 0)})
    res = json.load(open(res_path))
    cpu_h = sum(r["elapsed_s"] * r["ncpus"] for r in rows) / 3600
    wall = sum(r["elapsed_s"] for r in rows) / 60
    res["compute"].update({
        "where": "MIT Engaging",
        "partitions": sorted({r["partition"] for r in rows}),
        "job_ids": sorted({r["jobid"].split("_")[0] for r in rows}),
        "cpu_hours": round(cpu_h, 2),
        "wall_minutes": round(wall, 1),
        "jobs": rows,
        "note": "wall_minutes sums the elapsed time of every job / array task (not the critical path).",
    })
    if storage is not None:
        res["compute"]["peak_storage_gb"] = storage
    json.dump(res, open(res_path, "w"), indent=1)
    print(res_path, res["compute"]["job_ids"], res["compute"]["cpu_hours"], res["compute"]["wall_minutes"])


if __name__ == "__main__":
    main()
