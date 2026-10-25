"""Build the site result files from cluster outputs.

    python -I analysis/bigdata/psi_report.py inventory --summary work/psi-inventory-summary.json \
        --meta work/psi-objects.tsv.gz.meta.json --jobs work/jobs.json --out data/results/bigdata/psi-inventory.json
    python -I analysis/bigdata/psi_report.py morph --features work/dsi-features.csv.gz --calib work/dsi-calib.json \
        --jobs work/jobs.json --out data/results/bigdata/dsi-morphology.json
"""
import argparse
import collections
import json
import statistics
from datetime import datetime, timezone

TB = 1e12
GB = 1e9
REG = 'https://registry.opendata.aws/nasa-psi/'
BUCKET = 'https://nasa-psi.s3.us-west-2.amazonaws.com/'
ACCESSED = '2026-10-24'

DESCR = {
    'DSI': 'DECLIC-DSI (CNES/NASA, ISS 2010-2011): directional solidification of a transparent '
           'succinonitrile-0.24 wt% camphor alloy, imaging the 3-D cellular/dendritic front in situ '
           '(PI R. Trivedi, Iowa State; Co-I A. Karma, Northeastern; NASA Task Book NNX07AK69G).',
    'OASIS': 'OASIS (ISS 2015-2016): Observation and Analysis of Smectic Islands In Space - freely suspended '
             'liquid-crystal (smectic) bubbles, islands, coarsening, Marangoni and electric-field tests on 4 '
             'samples (PSI OASIS Data Organization Document).',
    'pk4': 'PK-4 (ESA/Roscosmos, ISS Columbus, 2014-2019 campaigns C00-C08): complex (dusty) plasma flowing in '
           'a DC discharge tube - on-board videos, sensor logs and ground data, curated for PSI by the '
           'University of Memphis team (PSI PK-4 summary document).',
}
# PSI documents downloaded and parsed for metadata (bytes as listed in the bucket)
DOC_FILES = {'index.html': 43067, 'DSI/DECLIC-DSI DoD.docx': 19914, 'DSI/Data/DSI-HD Solidification Plan.xlsx': 17864,
             'DSI/Data/DSI-INIT Solidification Plan.xlsx': 16752, 'DSI/Data/DSI-S1 Solidification Plan.xlsx': 27177,
             'DSI/Data/DSI-S2 Solidification Plan.xlsx': 17950, 'DSI/SRD/Final_SRD_1_101203.pdf': 3909035,
             'DSI Task Book report FY2010': 89464, 'DSI Task Book report FY2013': 87315, 'OASIS/OASIS DoD.pdf': 80143,
             'OASIS/Generating OASIS Filelist.docx': 72492, 'pk4/To_NASA_team/PK-4_Summary_-_updated_12-21-22.docx': 3922847,
             'DSI HD-9 HR2_2 filelist.txt': 163980, 'DSI HD-9 HR2_2 import.xlsx': 56257}
DOC_BYTES = sum(DOC_FILES.values())
SHORT = {'DSI': 'DSI', 'OASIS': 'OASIS', 'pk4': 'PK-4'}
COL = {'DSI': 'orange', 'OASIS': 'cyan', 'pk4': 'violet'}


def r(x, n=2):
    return None if x is None else round(x, n)


def inventory(a):
    s = json.load(open(a.summary))
    meta = json.load(open(a.meta))
    jobs = json.load(open(a.jobs)) if a.jobs else {}
    inv = s['investigations']
    invs = ['pk4', 'OASIS', 'DSI']
    total_tb = s['bytes'] / TB

    # data volume per experiment-day
    dsi = s['dsi_activities']
    oas = s['oasis_drives']
    pk4_days = dict(s['pk4_bytes_per_day'])
    # PK-4 science day = calendar date with >= 100 GB of on-board camera video (VMx-AVI); the other
    # dated days are 2-7 GB check-out/standby days (distribution is bimodal).
    vid = dict(s['pk4_video_bytes_per_day'])
    sci_days = {d: v for d, v in vid.items() if v >= 100 * GB}
    pk4_daily = sorted(v / GB for v in sci_days.values())
    camp = collections.defaultdict(lambda: [0, set()])
    for run, d, b in s['pk4_video_bytes_per_run_day']:
        if d in sci_days:
            c = run[:3]
            camp[c][0] += b
            camp[c][1].add(d)
    dsi_rate = [d['gb_per_day'] for d in dsi]
    oas_rate = [d['gb_per_day'] for d in oas]
    pk4_camp_rate = {c: v[0] / GB / len(v[1]) for c, v in sorted(camp.items()) if v[1]}

    per_day_points = []
    for d in dsi:
        per_day_points.append(['DSI ' + d['activity'].replace(' activity ', '-'), r(d['gb_per_day'], 2)])
    for d in oas:
        per_day_points.append(['OASIS ' + d['drive'].split(' - ')[0], r(d['gb_per_day'], 1)])
    for c, v in pk4_camp_rate.items():
        per_day_points.append(['PK-4 ' + c, r(v, 1)])

    types = s['file_types'][:12]
    other = s['file_types'][12:]
    med_pk4_day = statistics.median(pk4_daily) if pk4_daily else None

    dsi_frames = sum(d['bmp_frames'] for d in dsi)
    dsi_raw = sum(d['raw_bmp_bytes'] for d in dsi)
    out = dict(
        id='psi-inventory', tab='foundry',
        title='How much ISS physical-science data NASA publishes openly (PSI bucket)',
        question='How much raw data does one ISS physical-science experiment produce, and how much of it is openly available?',
        headline=dict(value=f'{total_tb:.1f}', unit='TB',
                      text=f'NASA\'s open Physical Sciences Informatics bucket holds {total_tb:.1f} TB in '
                           f'{s["objects"]:,} files from just three ISS investigations; the PK-4 plasma lab alone recorded '
                           f'a median {med_pk4_day:.0f} GB of video per science day.'),
        evidence_level='our computation on public data',
        datasets=[dict(name='NASA Physical Sciences Informatics (PSI) open-data bucket', url=BUCKET, license='NASA open data (public domain); registry ' + REG,
                       records=s['objects'], bytes=s['bytes'], accessed=ACCESSED,
                       scope='inventoried',
                       notes='Complete paginated ListObjectsV2 inventory of every key (no sampling). These bytes were LISTED, not downloaded. '
                             'Sizes are as stored; the bucket contains zip archives and duplicate copies, which we quantify separately.'),
                  dict(name='PSI listing records and documentation actually downloaded and parsed', url=BUCKET, license='NASA open data (public domain)',
                       records=s['objects'], bytes=DOC_BYTES, accessed=ACCESSED, scope='processed',
                       notes=f'{s["objects"]:,} listing records parsed (399 XML pages; response bytes not metered) plus {len(DOC_FILES)} PSI documents read for metadata '
                             '(DSI Solidification Plans, DSI DoD, SRD, Task Book reports, OASIS DoD, PK-4 summary, HD-9 filelist/import sheet): ' + ', '.join(DOC_FILES) + '.')],
        compute=dict(where='MIT Engaging', partitions=['mit_normal'], job_ids=jobs.get('inventory', []),
                     cpu_hours=jobs.get('inventory_cpu_hours', 0.0), wall_minutes=r(meta['seconds'] / 60, 1),
                     peak_storage_gb=0.01),
        method=[
            'Listed the whole bucket anonymously with S3 ListObjectsV2: delimiter listings at depth 0-1 enumerate 17 second-level prefixes, each listed to exhaustion (continuation tokens), 12 threads, one Slurm job.',
            f'{meta["list_pages"]} list pages, {s["objects"]:,} objects, {s["bytes"]:,} bytes; key uniqueness asserted.',
            'Exact duplicates = same ETag and size (identical content uploaded twice). Zip archives counted separately: in DSI they are compressed copies of the extracted image folders; in OASIS the "_Originals.zip" archives are the primary copy of the original frames (the extracted JPGs are gallery previews).',
            'Data volume per experiment-day: DSI = raw 1024x1024 BMP frame bytes / span between first and last frame of the activity, from the clock tick in each file name (23 ticks/s since 2009-01-01, derived from the PSI Solidification Plan sheets); OASIS = de-duplicated bytes on each hard-drive folder / calendar days named in the folder (HD01 "Jul 1 to Jul 6 2015" etc.); PK-4 = on-board camera video bytes (VMx-AVI files) per calendar date from file-name stamps (YYMMDD), counting "science days" with >= 100 GB (the daily distribution is bimodal: 300-790 GB science days vs 2-7 GB check-out days).',
        ],
        charts=[
            dict(id='psi-bytes-per-investigation', kind='hbar', title='Stored data per ISS investigation',
                 subtitle='NASA PSI open bucket, complete listing, terabytes (log scale)',
                 x=dict(label='Stored', unit='TB', scale='log'), y=dict(label='Investigation', unit='', scale='category'),
                 series=[dict(name='Stored bytes', color='orange',
                              points=[[SHORT[i], r(inv[i]['bytes'] / TB, 3)] for i in invs]),
                         dict(name='Exact duplicates and DSI zip copies removed', color='cyan',
                              points=[[SHORT[i], r((inv[i]['unique_nonzip_bytes'] if i == 'DSI' else inv[i]['unique_bytes']) / TB, 3)] for i in invs])],
                 annotations=[],
                 caption='PK-4 (complex plasma videos) dominates: ' f'{inv["pk4"]["bytes"]/TB:.1f} TB. OASIS {inv["OASIS"]["bytes"]/TB:.2f} TB, of which '
                         f'{inv["OASIS"]["zip_bytes"]/TB:.2f} TB are zip archives of original frames. DSI is only {inv["DSI"]["bytes"]/GB:.0f} GB stored and '
                         f'{inv["DSI"]["unique_nonzip_bytes"]/GB:.0f} GB once its zip copies and duplicates are removed. Sizes are what PSI publishes, not everything each experiment recorded.'),
            dict(id='psi-files-per-type', kind='hbar', title='What the files are',
                 subtitle='Object count per file type, whole bucket (top 12 by bytes)',
                 x=dict(label='Files', unit='count', scale='log'), y=dict(label='File type', unit='', scale='category'),
                 series=[dict(name='Files', color='violet', points=[[t, c] for t, c, b in types])],
                 annotations=[],
                 caption='; '.join(f'.{t}: {b/TB:.2f} TB' if b > 0.05 * TB else f'.{t}: {b/GB:.1f} GB' for t, c, b in types[:6]) +
                         f'. {len(other)} further types hold {sum(b for t, c, b in other)/GB:.1f} GB. Video (.avi/.ts) and zip archives carry almost all bytes; images (.bmp/.jpg/.raw/.tiff) carry most files.'),
            dict(id='psi-gb-per-experiment-day', kind='hbar', title='Raw data produced per experiment-day',
                 subtitle='GB per day of operations, per DSI activity, OASIS drive and PK-4 campaign (log scale)',
                 x=dict(label='Data volume', unit='GB/day', scale='log'), y=dict(label='Experiment unit', unit='', scale='category'),
                 series=[dict(name='DSI (raw axial+side frames)', color='orange', points=[p for p in per_day_points if p[0].startswith('DSI')]),
                         dict(name='OASIS (incl. original-frame zips)', color='cyan', points=[p for p in per_day_points if p[0].startswith('OASIS')]),
                         dict(name='PK-4 (on-board video, science days)', color='violet', points=[p for p in per_day_points if p[0].startswith('PK-4')])],
                 annotations=[],
                 caption=f'DSI: {min(dsi_rate):.1f}-{max(dsi_rate):.1f} GB/day of raw 8-bit frames. OASIS: {min(oas_rate):.0f}-{max(oas_rate):.0f} GB per calendar day '
                         f'(drive date ranges include idle days, so this is a lower bound on the rate while operating). PK-4: '
                         f'{min(pk4_camp_rate.values()):.0f}-{max(pk4_camp_rate.values()):.0f} GB of on-board video per science day by campaign; median over all {len(pk4_daily)} science days '
                         f'{med_pk4_day:.0f} GB. These are archive volumes after downlink and curation, not on-board sensor rates.'),
            dict(id='psi-daily-volume-timeline', kind='scatter', title='Daily data volume over time',
                 subtitle='GB per calendar day with dated files (DSI frame ticks; PK-4 file-name stamps)',
                 x=dict(label='Date', unit='', scale='time'), y=dict(label='Data volume', unit='GB/day', scale='log'),
                 series=[dict(name='DSI 2010-2011', color='orange', points=sorted([[d, r(v / GB, 2)] for d, v in s.get('dsi_bytes_per_day', [])])),
                         dict(name='PK-4 on-board video 2014-2019', color='violet', points=sorted([[d, r(v / GB, 1)] for d, v in s['pk4_video_bytes_per_day'] if v > 1e8]))],
                 annotations=[],
                 caption='Each point is one calendar day. PK-4 days cluster in short campaigns months apart, which suits a shared foundry that buffers, compresses and schedules downlink.'),
        ],
        stats=dict(
            objects=s['objects'], bytes=s['bytes'], unique_content_objects=s['unique_objects'],
            per_investigation={SHORT[i]: dict(objects=inv[i]['objects'], bytes=inv[i]['bytes'], zip_bytes=inv[i]['zip_bytes'],
                                              exact_dup_removed_bytes=inv[i]['unique_bytes'], dup_and_zip_removed_bytes=inv[i]['unique_nonzip_bytes'])
                               for i in invs},
            per_unit=[dict(investigation=SHORT.get(u['investigation'], u['investigation']), unit=u['unit'], objects=u['objects'], bytes=u['bytes'],
                           exact_dup_removed_bytes=u['unique_bytes']) for u in s['units'] if u['bytes'] > 1e8],
            file_types=[dict(type=t, objects=c, bytes=b) for t, c, b in s['file_types'][:25]],
            dsi_activities=dsi, oasis_drives=oas,
            pk4_campaign_video_gb_per_science_day={c: r(v, 1) for c, v in pk4_camp_rate.items()},
            pk4_median_video_gb_per_science_day=r(med_pk4_day, 1), pk4_science_days=len(pk4_daily),
            pk4_science_day_range_gb=[r(pk4_daily[0], 1), r(pk4_daily[-1], 1)],
            pk4_video_days_total=len(vid),
            pk4_fraction_of_bytes_with_date_stamp=r(s['pk4_dated_fraction'], 3),
            dsi_raw_frames=dsi_frames, dsi_raw_frame_bytes=dsi_raw,
            list_pages=meta['list_pages'], listing_seconds=meta['seconds']),
        findings=[
            f'The complete PSI bucket is {s["bytes"]/TB:.2f} TB in {s["objects"]:,} objects ({s["unique_objects"]:,} distinct by content hash), from three ISS investigations.',
            f'PK-4 complex-plasma data is {inv["pk4"]["bytes"]/TB:.1f} TB ({inv["pk4"]["bytes"]/s["bytes"]*100:.0f}% of the bucket), almost all on-board video; OASIS {inv["OASIS"]["bytes"]/TB:.1f} TB; DSI {inv["DSI"]["bytes"]/GB:.0f} GB.',
            f'The 8 public DSI solidification activities contain {dsi_frames:,} raw 1024x1024 frames ({dsi_raw/GB:.1f} GB), {min(dsi_rate):.1f}-{max(dsi_rate):.1f} GB per day of operation; the NASA Task Book reports 39 DSI experiments in the campaign, so PSI hosts about a fifth of them.',
            f'On its {len(pk4_daily)} science days PK-4 recorded a median {med_pk4_day:.0f} GB of on-board video per day (range {pk4_daily[0]:.0f}-{pk4_daily[-1]:.0f} GB); that is ~{med_pk4_day/statistics.median(dsi_rate):.0f}x the median DSI activity day, so data volume per experiment-day spans more than two orders of magnitude across facilities.',
            f'{inv["DSI"]["bytes"]/GB - inv["DSI"]["unique_nonzip_bytes"]/GB:.0f} GB of the {inv["DSI"]["bytes"]/GB:.0f} GB DSI folder is redundant (zips of extracted folders and a second extracted copy), a reminder that curation, not just storage, is needed.',
        ],
        limitations=[
            'Volumes are what PSI publishes after downlink and curation, not what the instruments recorded; PSI states that some OASIS drives were partially loaded and PK-4 videos are missing sensor data for some runs.',
            'OASIS per-day values divide by the calendar span of each hard drive, which includes idle days; the zip archives may partly overlap extracted raw/tiff frames (we did not open them).',
            'DSI per-day values span the first to last frame of each activity (melting, ~1-day homogenisation and solidification), so they average over quiet and burst acquisition.',
            'Three investigations are not a representative sample of all ISS science; the full PSI catalogue (psi.nasa.gov, registration) lists many more.',
        ],
        future_big_data=[
            'Inventory the full PSI catalogue at psi.nasa.gov (registration required), which lists dozens of further ISS physical-science investigations, to build a fleet-wide data-rate model.',
            'Open the OASIS "_Originals.zip" central directories by HTTP range requests to separate original frames from previews without downloading 7 TB.',
            'Join PK-4 file stamps with the ESA campaign express reports in pk4/To_NASA_team/Campaign_Reports to get data rate per scientific sequence, not per day.',
            'Add the ACE colloid (Advanced Colloids Experiment) and DECLIC DSI-R (2017-2018 reflight) imagery when published, for photonic and cooling materials respectively.',
        ],
        partners=[
            dict(name='NASA Physical Sciences Informatics (MSFC/GRC)', why='Curates and serves the open ISS physical-science archive a foundry would extend',
                 evidence='Hosts the 30 TB bucket; DSI Task Book contact monitor at NASA MSFC'),
            dict(name='CNES (DECLIC facility)', why='Built and operates DECLIC, the sealed multi-insert ISS facility closest to a shared process-cartridge design',
                 evidence='DSI Task Book report: "DECLIC-DSI facility built by the French Space Agency CNES"'),
            dict(name='ESA / Max Planck (PK-4 science team) and University of Memphis', why='Operate and curate the largest data stream in the bucket; experience with on-board video data handling',
                 evidence='pk4/To_NASA_team summary document prepared by the University of Memphis team (R. Gopalakrishnan); campaign reports provided by the ESA/PK-4 science team'),
        ],
        code=['analysis/bigdata/psi_inventory.py', 'analysis/bigdata/psi_inventory_summary.py', 'analysis/bigdata/psi_report.py',
              'cluster/bigdata/psi-inventory.sbatch'],
        reproduce=[
            'rsync -azR analysis/bigdata/psi* cluster/bigdata/psi-* engaging:~/orcd/scratch/orbital-foundry-20261024-01a170b7/',
            'ssh engaging "cd ~/orcd/scratch/orbital-foundry-20261024-01a170b7 && sbatch cluster/bigdata/psi-inventory.sbatch"',
            'python -I analysis/bigdata/psi_inventory_summary.py --tsv psi-objects.tsv.gz --out psi-inventory-summary.json',
            'python -I analysis/bigdata/psi_report.py inventory --summary psi-inventory-summary.json --meta psi-objects.tsv.gz.meta.json --jobs jobs.json --out data/results/bigdata/psi-inventory.json',
        ],
        investigations={SHORT[k]: v for k, v in DESCR.items()},
        generated_at=datetime.now(timezone.utc).isoformat(timespec='seconds'),
    )
    json.dump(out, open(a.out, 'w'), indent=1)
    print('wrote', a.out, len(json.dumps(out)) // 1024, 'KB')


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest='cmd', required=True)
    i = sub.add_parser('inventory')
    i.add_argument('--summary', required=True)
    i.add_argument('--meta', required=True)
    i.add_argument('--jobs')
    i.add_argument('--out', required=True)
    m = sub.add_parser('morph')
    m.add_argument('--features', required=True)
    m.add_argument('--calib')
    m.add_argument('--jobs')
    m.add_argument('--out', required=True)
    a = ap.parse_args()
    if a.cmd == 'inventory':
        inventory(a)
    else:
        import sys
        from pathlib import Path
        sys.path.insert(0, str(Path(__file__).resolve().parent))
        import psi_morph_report
        psi_morph_report.morph(a)


if __name__ == '__main__':
    main()
