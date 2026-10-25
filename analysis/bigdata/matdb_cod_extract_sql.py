#!/usr/bin/env python3
"""matdb: extract the COD MySQL dump members we use from the bulk zip.

Writes raw/cod/mysql__<name> for: data.sql, data.txt, smiles.sql, smiles.txt,
chemspider_x_cod.{sql,txt}, wikidata_x_cod.{sql,txt}. (During the hackathon run these
members were first pulled with HTTP range requests on the remote zip, so the analysis
could start before the 27 GB download finished; the bytes are identical.)

Usage: python -I matdb_cod_extract_sql.py ZIP OUT_DIR
"""
import os
import sys
import zipfile

MEMBERS = ["data.sql", "data.txt", "smiles.sql", "smiles.txt", "chemspider_x_cod.sql",
           "chemspider_x_cod.txt", "wikidata_x_cod.sql", "wikidata_x_cod.txt"]


def main():
    zpath, out = sys.argv[1], sys.argv[2]
    z = zipfile.ZipFile(zpath)
    for m in MEMBERS:
        dest = os.path.join(out, "mysql__" + m)
        if os.path.exists(dest) and os.path.getsize(dest) == z.getinfo("mysql/" + m).file_size:
            print("ok (exists)", dest)
            continue
        with z.open("mysql/" + m) as src, open(dest, "wb") as dst:
            while True:
                b = src.read(16 << 20)
                if not b:
                    break
                dst.write(b)
        print("wrote", dest, os.path.getsize(dest))


if __name__ == "__main__":
    main()
