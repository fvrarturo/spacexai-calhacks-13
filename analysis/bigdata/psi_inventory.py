"""Complete, paginated inventory of the public NASA PSI S3 bucket (no credentials).

Completeness by construction: delimiter listings at depth 0 and 1 capture every
key with fewer than two '/' and enumerate every depth-2 prefix; each depth-2
prefix is then listed fully (no delimiter, following continuation tokens).

Output: gzipped TSV  key \t size \t etag \t last_modified  (one row per object).

    python -I analysis/bigdata/psi_inventory.py --out work/psi-objects.tsv.gz --threads 8
"""
import argparse
import gzip
import json
import sys
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone

BASE = 'https://nasa-psi.s3.us-west-2.amazonaws.com/'
NS = {'s': 'http://s3.amazonaws.com/doc/2006-03-01/'}


def _get(params, tries=6):
    url = BASE + '?' + urllib.parse.urlencode(params)
    for i in range(tries):
        try:
            with urllib.request.urlopen(url, timeout=90) as r:
                return ET.fromstring(r.read())
        except Exception as e:  # transient S3 / network errors: back off and retry
            if i == tries - 1:
                raise
            time.sleep(2 ** i)


def _rows(tree):
    out = []
    for c in tree.findall('s:Contents', NS):
        g = lambda k: c.findtext('s:' + k, namespaces=NS)
        out.append((g('Key'), int(g('Size')), (g('ETag') or '').strip('"'), g('LastModified')))
    return out


def list_level(prefix):
    """One delimiter level: (direct objects, child prefixes). Paginates."""
    objs, prefixes, token = [], [], None
    while True:
        p = {'list-type': 2, 'prefix': prefix, 'delimiter': '/', 'max-keys': 1000}
        if token:
            p['continuation-token'] = token
        t = _get(p)
        objs += _rows(t)
        prefixes += [x.findtext('s:Prefix', namespaces=NS) for x in t.findall('s:CommonPrefixes', NS)]
        if t.findtext('s:IsTruncated', namespaces=NS) != 'true':
            return objs, prefixes
        token = t.findtext('s:NextContinuationToken', namespaces=NS)


def list_all(prefix):
    objs, token, pages = [], None, 0
    while True:
        p = {'list-type': 2, 'prefix': prefix, 'max-keys': 1000}
        if token:
            p['continuation-token'] = token
        t = _get(p)
        pages += 1
        objs += _rows(t)
        if t.findtext('s:IsTruncated', namespaces=NS) != 'true':
            return prefix, objs, pages
        token = t.findtext('s:NextContinuationToken', namespaces=NS)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--out', required=True)
    ap.add_argument('--threads', type=int, default=8)
    a = ap.parse_args()
    t0 = time.time()
    objs, tops = list_level('')
    depth2 = []
    for tp in tops:
        o, ps = list_level(tp)
        objs += o
        depth2 += ps
    print(f'top={tops} depth2_prefixes={len(depth2)} direct_objects={len(objs)}', flush=True)
    pages = 0
    with ThreadPoolExecutor(a.threads) as ex:
        for prefix, o, n in ex.map(list_all, depth2):
            objs += o
            pages += n
            print(f'{prefix!r}: {len(o)} objects, {n} pages, {sum(x[1] for x in o)/1e9:.2f} GB', flush=True)
    keys = [x[0] for x in objs]
    assert len(keys) == len(set(keys)), 'duplicate keys -> listing logic error'
    objs.sort()
    with gzip.open(a.out, 'wt') as f:
        for k, s, e, m in objs:
            f.write(f'{k}\t{s}\t{e}\t{m}\n')
    meta = dict(bucket=BASE, accessed_at=datetime.now(timezone.utc).isoformat(), objects=len(objs),
                bytes=sum(x[1] for x in objs), depth2_prefixes=len(depth2), list_pages=pages,
                seconds=round(time.time() - t0, 1))
    with open(a.out + '.meta.json', 'w') as f:
        json.dump(meta, f, indent=1)
    print(json.dumps(meta), flush=True)


if __name__ == '__main__':
    sys.exit(main())
