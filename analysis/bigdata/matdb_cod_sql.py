#!/usr/bin/env python3
"""matdb: convert the COD MySQL `data` table dump (mysqldump --tab format, shipped
inside cod-cifs-mysql.zip as mysql/data.txt + mysql/data.sql) to parquet.

The SQL table is COD's own parse of every CIF. We use it (a) for flags that are not
in the CIF (duplicateof, status=retracted/errors, onhold) and (b) as an
independent cross-check of our own CIF parse (matdb_cod_parse.py).

Usage: python -I matdb_cod_sql.py RAW_DIR OUT_PARQUET
"""
import re
import sys

import pandas as pd

KEEP = ["file", "a", "b", "c", "alpha", "beta", "gamma", "vol", "celltemp",
        "diffrtemp", "cellpressure", "diffrpressure", "thermalhist", "compoundsource",
        "nel", "sg", "sgHall", "sgNumber", "commonname", "chemname", "mineral",
        "formula", "calcformula", "cellformula", "Z", "Zprime", "year", "doi",
        "method", "Robs", "duplicateof", "optimal", "status", "flags", "onhold",
        "title", "journal"]


def columns(sql_path):
    cols = []
    in_create = False
    for line in open(sql_path, encoding="utf-8"):
        if line.startswith("CREATE TABLE"):
            in_create = True
            continue
        if in_create:
            m = re.match(r"\s+`([^`]+)`\s", line)
            if m:
                cols.append(m.group(1))
            elif line.lstrip().startswith(("PRIMARY", ")")):
                break
    return cols


def parse_tab(path, ncol):
    """mysqldump --tab: \t field sep, \n record sep, backslash escapes, \\N = NULL."""
    raw = open(path, "rb").read()
    # protect escaped backslashes, then escaped newlines / tabs
    raw = raw.replace(b"\\\\", b"\x01")
    raw = raw.replace(b"\\\n", b"\x02").replace(b"\\\t", b"\x03")
    rows = []
    bad = 0
    for line in raw.split(b"\n"):
        if not line:
            continue
        f = line.split(b"\t")
        if len(f) != ncol:
            bad += 1
            continue
        rows.append([None if x == b"\\N" else
                     x.replace(b"\x02", b"\n").replace(b"\x03", b"\t").replace(b"\x01", b"\\")
                      .decode("utf-8", "replace") for x in f])
    return rows, bad


def main():
    raw_dir, out = sys.argv[1], sys.argv[2]
    cols = columns(f"{raw_dir}/mysql__data.sql")
    rows, bad = parse_tab(f"{raw_dir}/mysql__data.txt", len(cols))
    df = pd.DataFrame(rows, columns=cols)[KEEP]
    num = ["file", "a", "b", "c", "alpha", "beta", "gamma", "vol", "celltemp", "diffrtemp",
           "cellpressure", "diffrpressure", "sgNumber", "Z", "Zprime", "year", "Robs",
           "duplicateof", "optimal"]
    for c in num:
        df[c] = pd.to_numeric(df[c], errors="coerce")
    df.to_parquet(out, index=False)
    print(f"columns={len(cols)} rows={len(df)} malformed_rows={bad}")
    print(df["status"].value_counts(dropna=False).to_dict())
    print(df["method"].value_counts(dropna=False).to_dict())
    print("duplicateof non-null:", int(df["duplicateof"].notna().sum()))
    print("onhold non-null:", int(df["onhold"].notna().sum()))


if __name__ == "__main__":
    main()
