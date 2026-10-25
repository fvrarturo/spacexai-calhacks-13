#!/usr/bin/env python3
"""matdb: parse every CIF in the COD bulk archive (one job-array task = one shard).

Reads members straight out of cod-cifs-mysql.zip (zip allows random access, so no
~520k-file extraction onto the shared scratch filesystem). For each CIF we extract:
COD id, sum formula, moiety formula, common / systematic / mineral names, space group
(H-M, Hall, IT number), cell (a, b, c, alpha, beta, gamma, V), Z, cell-measurement and
diffraction temperatures, pressures, and the journal year.

Parser: gemmi (C++ CIF 1.1 parser); a regex fallback handles files gemmi rejects.

Usage: python -I matdb_cod_parse.py ZIP TASK_ID N_TASKS OUT_DIR
"""
import re
import sys
import time
import zipfile

import pandas as pd

TAGS = {
    "formula_sum": ["_chemical_formula_sum"],
    "formula_moiety": ["_chemical_formula_moiety"],
    "name_common": ["_chemical_name_common"],
    "name_systematic": ["_chemical_name_systematic"],
    "name_mineral": ["_chemical_name_mineral"],
    "sg_hm": ["_space_group_name_H-M_alt", "_symmetry_space_group_name_H-M"],
    "sg_hall": ["_space_group_name_Hall", "_symmetry_space_group_name_Hall"],
    "sg_number": ["_space_group_IT_number", "_symmetry_Int_Tables_number"],
    "a": ["_cell_length_a"], "b": ["_cell_length_b"], "c": ["_cell_length_c"],
    "alpha": ["_cell_angle_alpha"], "beta": ["_cell_angle_beta"], "gamma": ["_cell_angle_gamma"],
    "vol": ["_cell_volume"],
    "Z": ["_cell_formula_units_Z"],
    "cell_T": ["_cell_measurement_temperature"],
    "diffrn_T": ["_diffrn_ambient_temperature"],
    "cell_P": ["_cell_measurement_pressure"],
    "diffrn_P": ["_diffrn_ambient_pressure"],
    "year": ["_journal_year"],
    "cod_id": ["_cod_database_code"],
}
NUM = {"sg_number", "a", "b", "c", "alpha", "beta", "gamma", "vol", "Z", "cell_T", "diffrn_T",
       "cell_P", "diffrn_P", "year"}
_num_re = re.compile(r"^\s*([-+]?\d*\.?\d+(?:[eE][-+]?\d+)?)")


def to_num(v):
    if v is None:
        return None
    m = _num_re.match(v)
    return float(m.group(1)) if m else None


def clean(v):
    if v is None:
        return None
    v = v.strip()
    if v in ("?", ".", ""):
        return None
    if len(v) >= 2 and v[0] == v[-1] and v[0] in "'\"":
        v = v[1:-1]
    if v.startswith(";"):
        v = v.strip(";").strip()
    return " ".join(v.split()) or None


def parse_gemmi(text):
    import gemmi
    doc = gemmi.cif.read_string(text)
    blk = doc[0]
    out = {}
    for k, tags in TAGS.items():
        val = None
        for t in tags:
            v = blk.find_value(t)
            if v is not None:
                val = v
                break
        out[k] = clean(val)
    return out


_tag_re = {k: [re.compile(r"^" + re.escape(t) + r"[ \t]+(.+?)\s*$", re.M | re.I) for t in tags]
           for k, tags in TAGS.items()}
_txt_re = {k: [re.compile(r"^" + re.escape(t) + r"\s*\n;(.*?)\n;", re.M | re.S | re.I) for t in tags]
           for k, tags in TAGS.items()}


def parse_regex(text):
    out = {}
    for k in TAGS:
        val = None
        for rx in _tag_re[k]:
            m = rx.search(text)
            if m:
                val = m.group(1)
                break
        if val is None:
            for rx in _txt_re[k]:
                m = rx.search(text)
                if m:
                    val = m.group(1)
                    break
        out[k] = clean(val)
    return out


def main():
    zpath, task, ntask, outdir = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
    t0 = time.time()
    import os
    final = f"{outdir}/cod_cif_{task:03d}.parquet"
    if os.path.exists(final):          # shard already done (array task or burst job)
        print(f"task {task}: exists, skipping", flush=True)
        return
    z = zipfile.ZipFile(zpath)
    members = sorted(i.filename for i in z.infolist()
                     if re.match(r"^cif/\d/\d\d/\d\d/\d{7}\.cif$", i.filename))
    mine = members[task::ntask]
    rows = []
    nbytes = 0
    for name in mine:
        raw = z.read(name)
        nbytes += len(raw)
        try:
            text = raw.decode("utf-8")
        except UnicodeDecodeError:
            text = raw.decode("latin-1")
        mode = "gemmi"
        try:
            rec = parse_gemmi(text)
        except Exception:  # noqa: BLE001
            mode = "regex"
            try:
                rec = parse_regex(text)
            except Exception:  # noqa: BLE001
                rec, mode = {k: None for k in TAGS}, "fail"
        for k in NUM:
            rec[k] = to_num(rec[k])
        rec["file"] = int(name.rsplit("/", 1)[1][:7])
        rec["parse_mode"] = mode
        rec["bytes"] = len(raw)
        rows.append(rec)
    df = pd.DataFrame(rows)
    tmp = final + f".tmp{os.getpid()}"
    df.to_parquet(tmp, index=False)
    os.replace(tmp, final)             # atomic: a half-written shard is never seen as done
    print(f"task {task}/{ntask}: total_members={len(members)} mine={len(mine)} "
          f"bytes={nbytes} modes={df.parse_mode.value_counts().to_dict()} "
          f"seconds={time.time() - t0:.0f}", flush=True)


if __name__ == "__main__":
    main()
