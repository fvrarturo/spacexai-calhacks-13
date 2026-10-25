#!/usr/bin/env python3
"""matdb: resumable, parallel HTTP range download of one large file (stdlib only).

Used for the COD bulk archive (cod-cifs-mysql.zip, ~27 GB, one file), chosen over
`rsync rsync://www.crystallography.net/cif/` because the per-file rsync tree is
~520k small files and the shared scratch quota is 1.0M files.

The COD server resets connections when hit with many parallel streams, so: few
threads, small chunks, resume mid-chunk, persistent retries with backoff. The
state file records finished byte ranges, so a killed job resumes where it stopped.

Usage:
  python -I matdb_fetch.py URL DEST [--threads 3] [--chunk-mb 64] [--md5 HEX]
"""
import argparse
import hashlib
import json
import os
import sys
import threading
import time
import urllib.request


def content_length(url):
    req = urllib.request.Request(url, method="HEAD")
    with urllib.request.urlopen(req, timeout=60) as r:
        return int(r.headers["Content-Length"])


def fetch_range(url, fd, start, end, retries=60):
    """Fetch bytes [start, end] inclusive, pwrite at offset; resume after short reads."""
    off = start
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers={"Range": f"bytes={off}-{end}"})
            with urllib.request.urlopen(req, timeout=120) as r:
                if r.status != 206:
                    raise RuntimeError(f"expected 206, got {r.status}")
                while True:
                    buf = r.read(1 << 20)
                    if not buf:
                        break
                    os.pwrite(fd, buf, off)
                    off += len(buf)
            if off == end + 1:
                return
            raise RuntimeError(f"short read at {off}")
        except Exception as e:  # noqa: BLE001
            print(f"[retry {attempt}] {start}-{end} at {off}: {e}", file=sys.stderr, flush=True)
            time.sleep(min(60, 3 * (attempt + 1)))
    raise RuntimeError(f"failed range {start}-{end}")


def load_done(state_path, size):
    """Finished byte ranges [[s, e], ...]; understands the old {done: [chunk idx]} @256MB."""
    if not os.path.exists(state_path):
        return []
    st = json.load(open(state_path))
    if "ranges" in st:
        return [tuple(r) for r in st["ranges"]]
    c = 256 << 20
    return [(i * c, min((i + 1) * c, size) - 1) for i in st.get("done", [])]


def covered(s, e, done):
    return any(ds <= s and e <= de for ds, de in done)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("url")
    ap.add_argument("dest")
    ap.add_argument("--threads", type=int, default=3)
    ap.add_argument("--chunk-mb", type=int, default=64)
    ap.add_argument("--md5", default=None)
    a = ap.parse_args()

    size = content_length(a.url)
    chunk = a.chunk_mb << 20
    state_path = a.dest + ".state.json"
    done = load_done(state_path, size)
    ranges = [(s, min(s + chunk, size) - 1) for s in range(0, size, chunk)]
    todo = [r for r in ranges if not covered(r[0], r[1], done)]
    fd = os.open(a.dest, os.O_RDWR | os.O_CREAT, 0o644)
    if os.fstat(fd).st_size != size:
        os.ftruncate(fd, size)
    print(f"size={size} chunks={len(ranges)} todo={len(todo)}", flush=True)
    lock = threading.Lock()
    t0 = time.time()
    nbytes = [0]
    failed = []

    def worker():
        while True:
            with lock:
                if not todo:
                    return
                s, e = todo.pop(0)
            try:
                fetch_range(a.url, fd, s, e)
            except Exception as ex:  # noqa: BLE001
                with lock:
                    failed.append((s, e))
                print(f"FAILED {s}-{e}: {ex}", file=sys.stderr, flush=True)
                continue
            with lock:
                done.append((s, e))
                nbytes[0] += e - s + 1
                json.dump({"ranges": sorted(done)}, open(state_path, "w"))
                el = time.time() - t0
                left = sum(1 for r in ranges if not covered(r[0], r[1], done))
                print(f"ok {s}-{e}; chunks left {left}; {nbytes[0] / el / 1e6:.1f} MB/s",
                      flush=True)

    ths = [threading.Thread(target=worker) for _ in range(a.threads)]
    for t in ths:
        t.start()
    for t in ths:
        t.join()
    os.fsync(fd)
    os.close(fd)
    if failed or any(not covered(r[0], r[1], done) for r in ranges):
        sys.exit(f"incomplete download, failed={len(failed)}")
    if a.md5:
        h = hashlib.md5()
        with open(a.dest, "rb") as f:
            for blk in iter(lambda: f.read(16 << 20), b""):
                h.update(blk)
        got = h.hexdigest()
        print(f"md5 {got} expected {a.md5} -> {'OK' if got == a.md5 else 'MISMATCH'}", flush=True)
        if got != a.md5:
            sys.exit(2)
    print(f"done in {time.time() - t0:.0f}s", flush=True)


if __name__ == "__main__":
    main()
