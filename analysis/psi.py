"""Bounded public NASA PSI inventory, downloads and descriptive image QC.

The first images in an object listing are a convenience pilot, not a random or
representative sample. No physical calibration or gravity-effect inference.
"""
import argparse
import hashlib
import json
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
BASE='https://nasa-psi.s3.us-west-2.amazonaws.com/'
NS={'s':'http://s3.amazonaws.com/doc/2006-03-01/'}

def inventory(prefix, limit=1000):
    if not prefix.startswith('DSI/') or not 1 <= limit <= 1000:
        raise ValueError('Pilot inventory restricted to DSI/ and <=1000 objects')
    query=urllib.parse.urlencode({'list-type':2,'prefix':prefix,'max-keys':limit})
    xml=urllib.request.urlopen(BASE+'?'+query,timeout=40).read()
    tree=ET.fromstring(xml)
    objects=[]
    for item in tree.findall('s:Contents',NS):
        get=lambda k:item.findtext('s:'+k,namespaces=NS)
        objects.append(dict(key=get('Key'),size=int(get('Size')),etag=get('ETag'),last_modified=get('LastModified')))
    return dict(source=BASE,registry='https://registry.opendata.aws/nasa-psi/',prefix=prefix,
                accessed_at=datetime.now(timezone.utc).isoformat(),
                truncated=tree.findtext('s:IsTruncated',namespaces=NS)=='true',
                continuation_token=tree.findtext('s:NextContinuationToken',namespaces=NS),objects=objects)

def fetch(manifest, count=12, max_bytes=20_000_000, destination=None):
    if not 1 <= count <= 1000 or not 1 <= max_bytes <= 1_000_000_000:
        raise ValueError('Provide a bounded file count (<=1000) and byte budget (<=1GB)')
    destination=destination or ROOT/'data/raw/dsi-pilot'
    destination.mkdir(parents=True,exist_ok=True)
    selected=[]; total=0
    for obj in manifest['objects']:
        if not obj['key'].lower().endswith('.bmp'): continue
        if total+obj['size'] > max_bytes: continue
        key=obj['key']
        url=BASE+urllib.parse.quote(key,safe='/')
        local=destination/(hashlib.sha256(key.encode()).hexdigest()[:12]+'-'+Path(key).name)
        with urllib.request.urlopen(url,timeout=60) as response:
            content=response.read(obj['size']+1)
        if len(content) != obj['size']: raise ValueError('Object length changed; refresh manifest')
        local.write_bytes(content)
        resolved=local.resolve()
        local_path=str(resolved.relative_to(ROOT)) if resolved.is_relative_to(ROOT) else str(resolved)
        selected.append(dict(**obj,url=url,sha256=hashlib.sha256(content).hexdigest(),local_path=local_path))
        total+=len(content)
        if len(selected)>=count:break
    if not selected:raise ValueError('No BMP files found inside byte budget')
    return dict(**manifest,selection='First eligible bitmap objects in lexicographic listing; convenience sample.',downloaded_bytes=total,downloaded=selected)

def qc(manifest):
    import numpy as np
    from PIL import Image
    rows=[]
    for obj in manifest['downloaded']:
        p=Path(obj['local_path'])
        if not p.is_absolute():p=ROOT/p
        if hashlib.sha256(p.read_bytes()).hexdigest()!=obj['sha256']:raise ValueError('Checksum mismatch: '+str(p))
        with Image.open(p) as image:
            gray=np.asarray(image.convert('L'),dtype=float)
        rows.append(dict(key=obj['key'],sha256=obj['sha256'],width=int(gray.shape[1]),height=int(gray.shape[0]),
                         mean_intensity=float(gray.mean()),intensity_sd=float(gray.std()),
                         saturated_fraction=float(np.mean((gray==0)|(gray==255))),
                         mean_gradient=float((np.abs(np.diff(gray,axis=0)).mean()+np.abs(np.diff(gray,axis=1)).mean())/2)))
    return dict(kind='NASA raw-image descriptive QC',count=len(rows),bytes=manifest['downloaded_bytes'],
                source=BASE,selection=manifest['selection'],accessed_at=manifest['accessed_at'],
                code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                limitations=['Convenience pilot, not a representative archive sample.',
                             'Intensity and gradient metrics are image diagnostics, not calibrated morphology or material performance.',
                             'No ground controls, run-level statistical effect, physical scale, or causal microgravity advantage established.'],rows=rows)

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('command',choices=['inventory','fetch','qc'])
    parser.add_argument('--prefix',default='DSI/Data/S1 activity 1/')
    parser.add_argument('--manifest',type=Path,default=ROOT/'data/manifests/dsi-pilot.json')
    parser.add_argument('--count',type=int,default=12)
    parser.add_argument('--max-bytes',type=int,default=20_000_000)
    parser.add_argument('--destination',type=Path)
    parser.add_argument('--output',type=Path,default=ROOT/'data/results/dsi-qc.json')
    args=parser.parse_args();args.manifest.parent.mkdir(parents=True,exist_ok=True)
    if args.command=='inventory':
        result=inventory(args.prefix);args.manifest.write_text(json.dumps(result,indent=2)+'\n')
        print(f"Listed {len(result['objects'])} objects; truncated={result['truncated']}")
    elif args.command=='fetch':
        result=fetch(json.loads(args.manifest.read_text()),args.count,args.max_bytes,args.destination)
        args.manifest.write_text(json.dumps(result,indent=2)+'\n')
        print(f"Downloaded {len(result['downloaded'])} images, {result['downloaded_bytes']} bytes")
    else:
        result=qc(json.loads(args.manifest.read_text()));args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(json.dumps(result,indent=2)+'\n');print(f"Verified {result['count']} images")

if __name__=='__main__':main()
