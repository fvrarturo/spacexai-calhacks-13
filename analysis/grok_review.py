"""Adversarial review of every big-data result file by Grok (xAI API).

Grok reads each result JSON and returns a structured critique: a one-sentence
judge summary, possible overclaims, missing caveats and a verdict. Reviews are
saved next to the results and shown in the site's appendix. Grok never edits a
result; numbers come only from the analysis code.

Usage:
    export XAI_API_KEY=...            # from console.x.ai (never commit it)
    python3 -m analysis.grok_review   # reviews every data/results/bigdata/*.json
    python3 -m analysis.grok_review --only pdb-microgravity --model grok-4.7
"""
import argparse
import json
import os
import sys
import time
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / 'data/results/bigdata'
REVIEWS = RESULTS / 'reviews'
ENDPOINT = 'https://api.x.ai/v1/chat/completions'

SYSTEM = (
    'You are a skeptical scientific reviewer for a hackathon project about manufacturing materials in orbit. '
    'You receive one analysis result file (JSON). Judge only what the file itself supports. '
    'Flag any headline or finding that overstates the evidence (for example causal claims from archive correlations, '
    'non-independent samples, missing confounders, or physics calculations presented as measurements). '
    'Do not invent numbers. Reply with JSON only.'
)
SCHEMA = {
    'type': 'object',
    'properties': {
        'judge_summary': {'type': 'string', 'description': 'One plain sentence a non-expert judge can understand.'},
        'verdict': {'type': 'string', 'enum': ['supported', 'supported_with_caveats', 'overstated', 'unclear']},
        'overclaim_flags': {'type': 'array', 'items': {'type': 'string'}},
        'missing_caveats': {'type': 'array', 'items': {'type': 'string'}},
        'strongest_point': {'type': 'string'},
    },
    'required': ['judge_summary', 'verdict', 'overclaim_flags', 'missing_caveats', 'strongest_point'],
    'additionalProperties': False,
}


def review(result: dict, model: str, key: str) -> dict:
    compact = {k: result.get(k) for k in ('id', 'title', 'question', 'headline', 'evidence_level', 'datasets', 'method', 'stats', 'findings', 'limitations')}
    # Charts are summarised by title/caption only, to keep the request small.
    compact['charts'] = [{'title': c.get('title'), 'caption': c.get('caption')} for c in result.get('charts', [])]
    body = {
        'model': model,
        'messages': [{'role': 'system', 'content': SYSTEM}, {'role': 'user', 'content': json.dumps(compact, ensure_ascii=False)}],
        'response_format': {'type': 'json_schema', 'json_schema': {'name': 'review', 'schema': SCHEMA, 'strict': True}},
        'temperature': 0,
    }
    req = urllib.request.Request(ENDPOINT, data=json.dumps(body).encode(), headers={'Authorization': f'Bearer {key}', 'Content-Type': 'application/json'})
    with urllib.request.urlopen(req, timeout=120) as resp:
        payload = json.load(resp)
    content = payload['choices'][0]['message']['content']
    return {'review': json.loads(content), 'model': payload.get('model', model), 'response_id': payload.get('id'), 'usage': payload.get('usage')}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument('--model', default=os.environ.get('XAI_MODEL', 'grok-4.7'))
    parser.add_argument('--only', help='Review a single result id')
    args = parser.parse_args()
    key = os.environ.get('XAI_API_KEY')
    if not key:
        print('XAI_API_KEY is not set; no reviews were run.', file=sys.stderr)
        return 1
    REVIEWS.mkdir(parents=True, exist_ok=True)
    for path in sorted(RESULTS.glob('*.json')):
        if path.name == 'index.json':
            continue
        result = json.loads(path.read_text())
        if args.only and result.get('id') != args.only:
            continue
        out = review(result, args.model, key)
        out.update({'result_id': result['id'], 'result_file': path.name, 'reviewed_at': datetime.now(timezone.utc).isoformat()})
        (REVIEWS / f"{result['id']}.grok.json").write_text(json.dumps(out, indent=1, ensure_ascii=False))
        print(f"{result['id']}: {out['review']['verdict']} — {out['review']['judge_summary']}")
        time.sleep(1)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
