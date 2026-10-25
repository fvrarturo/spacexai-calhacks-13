"""One-time, lossless extraction of the initial self-contained prototype."""
import base64
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if (ROOT / 'site/sections/01-vision.html').exists():
    raise SystemExit('Migration is already complete; refusing to overwrite active source files.')
archive = ROOT / 'initial-work'
archive.mkdir(exist_ok=True)
original = ROOT / 'index.html'
if original.exists() and not (archive / 'index.html').exists():
    original.rename(archive / 'index.html')
for name in ['research', 'README.md']:
    if (ROOT / name).exists() and not (archive / name).exists():
        (ROOT / name).rename(archive / name)
source = (archive / 'index.html').read_text()
for name in ['site/sections', 'site/templates', 'site/content', 'site/static/assets',
             'site/static/js', 'site/static/css', 'analysis', 'data/results', 'docs', 'tests', 'cluster']:
    (ROOT / name).mkdir(parents=True, exist_ok=True)
data = json.loads(re.search(r'window.FOUNDRY_DATA=(.*?);?\s*</script>', source, re.S)[1].rstrip(';'))
for key, value in data.items():
    (ROOT / 'site/content' / f'{key}.json').write_text(json.dumps(value, indent=2, ensure_ascii=False) + '\n')
css = re.search(r'<style>(.*?)</style>', source, re.S)[1]
css = css.replace('}', '}\n').replace('{', ' {\n  ').replace(';', ';\n  ')
(ROOT / 'site/static/css/story.css').write_text(css)
scripts = list(re.finditer(r'<script\b[^>]*>(.*?)</script>', source, re.S))
js = scripts[-1][1].replace('const D=window.FOUNDRY_DATA;', "import { storyData as D } from './content.js';")
js = js.replace("(() => {\n'use strict';\n", '').removesuffix('\n})();\n\n')
(ROOT / 'site/static/js/story.js').write_text(js)
body = source[source.index('<body>') + 6:source.index('<script')]
for number, match in enumerate(re.finditer(r'<section\b[^>]*id="([^"]+)".*?</section>', body, re.S), 1):
    section = match[0]
    for image in re.finditer(r'data:image/bmp;base64,([A-Za-z0-9+/=]+)', section):
        binary = base64.b64decode(image[1])
        filename = 'dsi-original-sample.bmp'
        (ROOT / 'site/static/assets' / filename).write_bytes(binary)
        section = section.replace(image[0], f'assets/{filename}')
    (ROOT / 'site/sections' / f'{number:02d}-{match[1]}.html').write_text(section + '\n')
header = body[:body.index('<main')]
header = header.replace('<a href="#data">The data</a>', '<a href="#data">The data</a><a href="workspace.html">Research workspace ↗</a>')
(ROOT / 'site/templates/story-header.html').write_text(header)
footer = body[body.index('</main>') + 7:]
(ROOT / 'site/templates/story-footer.html').write_text(footer)
(archive / 'ARCHIVE.md').write_text('''# Initial work — 24 October 2026

The original website, project README, and broad idea research are preserved here.
The website is unchanged and remains self-contained. Active work lives in
`../site`, `../analysis`, `../data`, and `../docs`.
The starter-pack PDF remains in `../docs`.

Original website SHA-256: `''' + hashlib.sha256((archive / 'index.html').read_bytes()).hexdigest() + '`\n')
print('Archived original; extracted 13 sections, four content datasets, styles, scripts, and original image.')
