"""Build the static site from independently editable sections and JSON content."""
import json
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / 'site'
OUT = ROOT / 'dist'

def shell(title, body, css, script):
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="theme-color" content="#08121e">
<meta name="description" content="Orbital Foundry: a research and operating plan for specialized materials manufacturing in orbit.">
<title>{title}</title><link rel="icon" type="image/svg+xml" href="favicon.svg"><link rel="stylesheet" href="css/{css}">
</head><body>{body}<script type="module" src="js/{script}"></script></body></html>'''

def human_bytes(n):
    units = ['B', 'KB', 'MB', 'GB', 'TB', 'PB']
    v = float(n or 0); i = 0
    while v >= 1000 and i < len(units) - 1:
        v /= 1000; i += 1
    return f"{v:.0f} {units[i]}" if v >= 100 else f"{v:.1f} {units[i]}"

def human_count(n):
    n = int(n or 0)
    for div, suffix in ((1e9, 'B'), (1e6, 'M'), (1e3, 'k')):
        if n >= div:
            return f"{n / div:.1f}{suffix}" if n < div * 10 else f"{n / div:.0f}{suffix}"
    return str(n)

def drop_missing_evidence(html, available):
    """Remove evidence/headline slots whose result file has not been generated."""
    import re
    html = re.sub(r'<div data-evidence="([^"]+)"[^>]*></div>', lambda m: m.group(0) if m.group(1) in available else '', html)
    html = re.sub(r'<a class="headline-card"[^>]*data-headline="([^"]+)".*?</a>', lambda m: m.group(0) if m.group(1) in available else '', html, flags=re.S)
    return html

def bigdata_index():
    """Index every big-data result, with totals that count each dataset and job once."""
    folder = ROOT / 'data/results/bigdata'
    analyses, seen_data, seen_jobs, dataset_rows = [], {}, set(), []
    cpu_hours = 0.0
    docs = {p.stem for p in (ROOT / 'docs/appendix').glob('*.md')} if (ROOT / 'docs/appendix').exists() else set()
    for path in sorted(folder.glob('*.json')) if folder.exists() else []:
        if path.name == 'index.json':
            continue
        try:
            r = json.loads(path.read_text())
        except json.JSONDecodeError:
            print(f'Skipping invalid result {path.name}'); continue
        if not isinstance(r, dict) or 'id' not in r or 'tab' not in r:
            continue
        prefixes = [Path(c).stem.split('_')[0].split('-')[0] for c in r.get('code', [])]
        doc = next((f'docs/appendix/{p}.md' for p in prefixes + [r['id'].split('-')[0]] if p in docs), None)
        for d in r.get('datasets', []):
            key = (d.get('url') or d.get('name') or '').strip().lower() + '|' + (d.get('scope') or '')
            if key and key not in seen_data:
                dataset_rows.append({'name': d.get('name'), 'bytes': int(d.get('bytes') or 0), 'records': int(d.get('records') or 0), 'analysis': r['id'], 'tab': r['tab'],
                                     'scope': d.get('scope') or ('inventoried' if any(w in f"{d.get('name', '')} {d.get('notes', '')}".lower() for w in ('listobjects', 'inventory')) else 'processed')})
                text = f"{d.get('name', '')} {d.get('notes', '')}".lower()
                inventoried = d.get('scope') == 'inventoried' or (not d.get('scope') and ('listobjects' in text or 'inventory' in text))
                seen_data[key] = (0 if inventoried else int(d.get('bytes') or 0), 0 if inventoried else int(d.get('records') or 0), int(d.get('bytes') or 0) if inventoried else 0)
        compute = r.get('compute') or {}
        new_jobs = [j for j in compute.get('job_ids', []) if j not in seen_jobs]
        seen_jobs.update(new_jobs)
        cpu_hours += float(compute.get('cpu_hours') or 0)
        review = None
        review_path = folder / 'reviews' / f"{r['id']}.grok.json"
        if review_path.exists():
            rv = json.loads(review_path.read_text())
            review = {**rv.get('review', {}), 'model': rv.get('model'), 'reviewed_at': rv.get('reviewed_at')}
        analyses.append({'id': r['id'], 'tab': r['tab'], 'tabs': r.get('tabs', []), 'material': r.get('material'), 'title': r.get('title'), 'headline': r.get('headline'), 'doc': doc, 'file': path.name, 'review': review})
    distinct = {k.split('|')[0] for k in seen_data}
    totals = {'analyses': len(analyses), 'datasets': len(distinct), 'bytes': sum(v[0] for v in seen_data.values()),
              'records': sum(v[1] for v in seen_data.values()), 'bytes_inventoried': sum(v[2] for v in seen_data.values()),
              'jobs': len(seen_jobs), 'cpu_hours': round(cpu_hours, 2)}
    return {'analyses': analyses, 'totals': totals, 'datasets': sorted(dataset_rows, key=lambda d: -d['bytes'])}

def build():
    OUT.mkdir(exist_ok=True)
    shutil.copytree(SITE / 'static', OUT, dirs_exist_ok=True)
    story = {p.stem: json.loads(p.read_text()) for p in (SITE / 'content').glob('*.json') if p.stem in ['sources','programs','datasets','modules']}
    (OUT / 'js/content.js').write_text('export const storyData = ' + json.dumps(story, ensure_ascii=False) + ';\n')
    body = (SITE / 'templates/story-header.html').read_text()
    body += '<main id="main">' + '\n'.join(p.read_text() for p in sorted((SITE / 'sections').glob('*.html'))) + '</main>'
    body += (SITE / 'templates/story-footer.html').read_text()
    (OUT / 'story.html').write_text(shell('Orbital Foundry — Original concept', body.replace('href="workspace.html"', 'href="research.html"'), 'story.css', 'story.js'))
    if (SITE / 'templates/workspace.html').exists():
        workspace = (SITE / 'templates/workspace.html').read_text().replace('href="index.html#sources"', 'href="story.html#sources"')
        (OUT / 'research.html').write_text(shell('Orbital Foundry — Research workspace', workspace, 'workspace.css', 'workspace.js'))
    header = (SITE / 'templates/mission-header.html').read_text()
    footer = (SITE / 'templates/mission-footer.html').read_text()
    material_results = json.loads((ROOT / 'data/results/materials.json').read_text())
    material_effect = next(row['relative_reduction_pct'] for row in material_results['rows'] if row['concentration_mg_ml'] == 50)
    scenario_count = json.loads((ROOT / 'data/results/sensitivity.json').read_text())['scenario_count']
    bigdata = bigdata_index()
    totals = bigdata['totals']
    replacements = {
        '{{MATERIAL_EFFECT}}': f'{material_effect:.1f}', '{{SCENARIO_COUNT}}': str(scenario_count),
        '{{BIGDATA_BYTES}}': human_bytes(totals['bytes']), '{{BIGDATA_RECORDS}}': human_count(totals['records']),
        '{{BIGDATA_CPUH}}': f"{totals['cpu_hours']:.0f}" if totals['cpu_hours'] >= 10 else f"{totals['cpu_hours']:.1f}",
        '{{BIGDATA_JOBS}}': str(totals['jobs']), '{{BIGDATA_INVENTORIED}}': human_bytes(totals['bytes_inventoried']), '{{BIGDATA_COUNT}}': str(totals['analyses']), '{{BIGDATA_DATASETS}}': str(totals['datasets']),
    }
    pages = [('vision', 'index', 'The next factory floor'), ('materials', 'materials', 'The materials'), ('foundry', 'foundry', 'Inside the foundry'), ('network', 'network', 'An orbital industry'), ('appendix', 'appendix', 'Appendix: data & methods')]
    for key, route, title in pages:
        navigation = header.replace(f'data-page="{key}"', f'data-page="{key}" aria-current="page"')
        narrative = (SITE / 'pages' / f'{key}.html').read_text()
        for marker, value in replacements.items():
            narrative = narrative.replace(marker, value)
        narrative = drop_missing_evidence(narrative, {a['id'] for a in bigdata['analyses']})
        page_body = navigation + '<main id="main" data-chapter="' + key + '">' + narrative + '</main>' + footer
        page = shell(f'Orbital Foundry — {title}', page_body, 'mission.css', 'mission.js')
        (OUT / f'{route}.html').write_text(page)
        if key == 'vision':
            # Preserve the user's existing preview/bookmark as an entry to the new site.
            (OUT / 'workspace.html').write_text(page)
    shutil.copytree(SITE / 'content', OUT / 'content', dirs_exist_ok=True)
    shutil.copytree(ROOT / 'data/results', OUT / 'results', dirs_exist_ok=True)
    shutil.copytree(ROOT / 'docs', OUT / 'docs', dirs_exist_ok=True)
    (OUT / 'results/bigdata').mkdir(parents=True, exist_ok=True)
    (OUT / 'results/bigdata/index.json').write_text(json.dumps(bigdata, indent=1))
    print(f'Built {OUT} · {totals["analyses"]} big-data analyses · {human_bytes(totals["bytes"])} · {totals["jobs"]} Slurm jobs')

if __name__ == '__main__':
    build()
