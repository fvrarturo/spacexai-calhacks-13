#!/usr/bin/env python3
"""Orbital Foundry / logistics workstream, Q4: the literature map.

Harvests OpenAlex works that combine a space-environment term (microgravity,
spaceflight, space station, ...) with each foundry topic. It then counts works
per year, top institutions, companies and countries, and checks a candidate
partner list against the harvested affiliations.

Stdlib only. Every API response is cached under --raw-dir, keyed by URL, so a
rerun with the same cache makes zero API calls (--offline enforces this).

OpenAlex budget: without an API key each IP gets 1000 credits/day. A search
filter costs 10 credits per request; a plain list/group_by costs 1. The script
logs X-RateLimit-* headers to <raw-dir>/requests.log.jsonl after every live
request and stops before --min-remaining. Without a key, cursor paging past page
1 is refused (HTTP 401), so pages 2+ use page=N; queries with more than five
boolean operators are limited to 1 request/s, hence the 1.2 s spacing.
A full harvest from an empty cache costs about 31 requests (~300 credits).

Usage:
  python3 -I analysis/bigdata/logistics_literature.py \
      --raw-dir /path/to/cache --out data/results/bigdata/literature-map.json
"""
import argparse
import datetime as dt
import hashlib
import json
import os
import random
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from collections import Counter, defaultdict

API = "https://api.openalex.org/works"
MAILTO = "orbital-foundry-hackathon@users.noreply.github.com"
SELECT = "id,doi,title,publication_year,type,cited_by_count,authorships"
PER_PAGE = 200

SPACE = ('(microgravity OR "micro-gravity" OR spaceflight OR "space flight" OR '
         '"International Space Station" OR "space station" OR "reduced gravity")')

# key -> (label, title_and_abstract.search expression). Every topic except "ism" is ANDed with SPACE.
TOPICS = {
    "protein": ("Protein crystallization",
                '("protein crystal" OR "protein crystals" OR "protein crystallization" OR '
                '"protein crystallisation" OR "macromolecular crystal" OR "macromolecular crystallization")'),
    "pharma": ("Pharmaceutical crystallization / polymorph",
               '(pharmaceutical OR pharmaceuticals OR drug OR drugs OR "small molecule" OR "small-molecule") AND '
               '(crystallization OR crystallisation OR "crystal growth" OR polymorph OR polymorphs OR '
               '"crystal form" OR cocrystal OR cocrystals)'),
    "solid": ("Solidification / alloy",
              '(solidification OR alloy OR alloys OR "directional solidification" OR dendritic)'),
    "colloid": ("Colloid / photonic crystal",
                '(colloid OR colloids OR colloidal OR "photonic crystal" OR "photonic crystals")'),
    "mof": ("Metal-organic framework",
            '("metal-organic framework" OR "metal-organic frameworks" OR "metal organic framework" OR '
            '"metal organic frameworks")'),
    "ism": ("In-space manufacturing",
            '("in-space manufacturing" OR "in space manufacturing" OR "space manufacturing" OR '
            '"orbital manufacturing" OR "in-orbit manufacturing" OR "on-orbit manufacturing")'),
    # sensitivity / context series (not in the union)
    "pharma_narrow": ("Pharmaceutical crystallization, narrow phrase set",
                      '("pharmaceutical crystal" OR "pharmaceutical crystallization" OR "drug crystal" OR '
                      '"drug crystallization" OR "crystal polymorph" OR "polymorphic form" OR '
                      '"small molecule crystal" OR "active pharmaceutical ingredient")'),
    "zeolite": ("Zeolite (porous-crystal precedent for MOFs)", '(zeolite OR zeolites)'),
}
TOPIC_ORDER = ["protein", "pharma", "solid", "colloid", "mof", "ism"]
EXTRA = ["pharma_narrow", "zeolite"]
COLORS = {"protein": "orange", "pharma": "violet", "solid": "grey", "colloid": "cyan",
          "mof": "green", "ism": "orange"}


def topic_query(key):
    expr = TOPICS[key][1]
    return expr if key == "ism" else f"{SPACE} AND {expr}"


class BudgetStop(Exception):
    pass


class Fetcher:
    def __init__(self, raw_dir, offline=False, min_remaining=40):
        self.raw_dir = raw_dir
        self.cache_dir = os.path.join(raw_dir, "cache")
        os.makedirs(self.cache_dir, exist_ok=True)
        self.offline = offline
        self.min_remaining = min_remaining
        self.live_calls = 0
        self.cache_hits = 0
        self.bytes_live = 0
        self.last_remaining = None

    def _path(self, url):
        return os.path.join(self.cache_dir, hashlib.sha1(url.encode()).hexdigest() + ".json")

    def get(self, params):
        params = dict(params, mailto=MAILTO)
        url = API + "?" + urllib.parse.urlencode(params, quote_via=urllib.parse.quote, safe=":,*()")
        path = self._path(url)
        if os.path.exists(path):
            self.cache_hits += 1
            with open(path) as f:
                return json.load(f)["body"]
        if self.offline:
            raise BudgetStop(f"offline and not cached: {url}")
        if self.last_remaining is not None and self.last_remaining < self.min_remaining:
            raise BudgetStop(f"remaining credits {self.last_remaining} < {self.min_remaining}")
        req = urllib.request.Request(url, headers={"User-Agent": f"orbital-foundry-hackathon (mailto:{MAILTO})"})
        for attempt in range(4):
            try:
                with urllib.request.urlopen(req, timeout=90) as r:
                    raw = r.read()
                    hdr = {k.lower(): v for k, v in r.headers.items() if k.lower().startswith("x-ratelimit")}
                break
            except urllib.error.HTTPError as e:
                body = e.read()[:500].decode("utf-8", "replace")
                self._log({"url": url, "status": e.code, "error": body})
                if e.code == 429 and "per second" in body and attempt < 3:
                    time.sleep(2.5 * (attempt + 1))  # >5 boolean operators: 1 request/s without a key
                    continue
                if e.code in (401, 402, 403, 429):
                    raise BudgetStop(f"HTTP {e.code}: {body}")
                if attempt == 3 or 400 <= e.code < 500:
                    raise
                time.sleep(3 * (attempt + 1))
            except urllib.error.URLError:
                if attempt == 3:
                    raise
                time.sleep(3 * (attempt + 1))
        body = json.loads(raw)
        self.live_calls += 1
        self.bytes_live += len(raw)
        try:
            self.last_remaining = int(hdr.get("x-ratelimit-remaining"))
        except (TypeError, ValueError):
            pass
        self._log({"url": url, "status": 200, "bytes": len(raw), **hdr})
        with open(path, "w") as f:
            json.dump({"url": url, "fetched": dt.datetime.now(dt.timezone.utc).isoformat(), "headers": hdr,
                       "bytes": len(raw), "body": body}, f)
        print(f"  live call: {len(raw)/1e3:.0f} kB, credits remaining {self.last_remaining}", file=sys.stderr)
        time.sleep(1.2)  # stay under 1 request/s for long boolean queries
        return body

    def _log(self, rec):
        rec["t"] = dt.datetime.now(dt.timezone.utc).isoformat()
        with open(os.path.join(self.raw_dir, "requests.log.jsonl"), "a") as f:
            f.write(json.dumps(rec) + "\n")


def harvest(fx, key, max_pages):
    """Page through one topic. Returns (works, total_count, complete, pages).

    Without an API key OpenAlex refuses cursor paging past the first page (HTTP 401,
    "API key required for cursor paging"), so page 1 is fetched with cursor=* and
    later pages with basic page=N paging (default relevance order). Duplicates are
    dropped by work id and completeness is checked against meta.count."""
    q = topic_query(key)
    base = {"filter": f"title_and_abstract.search:{q}", "select": SELECT, "per_page": PER_PAGE}
    works, total, pages = [], None, 0
    while pages < max_pages:
        params = dict(base, cursor="*") if pages == 0 else dict(base, page=pages + 1)
        body = fx.get(params)
        pages += 1
        total = body["meta"]["count"]
        works.extend(body["results"])
        if not body["results"] or pages * PER_PAGE >= total:
            break
    uniq = len({w["id"] for w in works})
    complete = uniq >= (total or 0)
    return works, total, complete, pages


def group_years(fx, key):
    body = fx.get({"filter": f"title_and_abstract.search:{topic_query(key)}", "group_by": "publication_year"})
    return {int(g["key"]): g["count"] for g in body["group_by"] if str(g["key"]).isdigit()}


def all_works_by_year(fx):
    body = fx.get({"group_by": "publication_year"})  # plain group_by, 1 credit
    return {int(g["key"]): g["count"] for g in body["group_by"] if str(g["key"]).isdigit()}


def space_only_by_year(fx):
    body = fx.get({"filter": f"title_and_abstract.search:{SPACE}", "group_by": "publication_year"})
    return {int(g["key"]): g["count"] for g in body["group_by"] if str(g["key"]).isdigit()}, body["meta"]


def short(wid):
    return wid.rsplit("/", 1)[-1] if wid else wid


# ---------------------------------------------------------------- partners
# name -> (regex on institution display_name or raw affiliation string, why it matters)
CANDIDATES = [
    ("Merck & Co. / MSD", r"\bmerck (?:&|and) co|merck sharp|\bmsd\b|merck research lab",
     "Ran the pembrolizumab (Keytruda) crystallization experiments on the ISS, the anchor for crystalline-suspension antibody formulations."),
    ("Merck KGaA (Darmstadt)", r"merck kgaa|merck healthcare kgaa|emd serono",
     "A separate company from Merck & Co.; listed so the two are not conflated."),
    ("Redwire", r"redwire", "Owns the ISS PIL-BOX pharmaceutical crystallization and in-space manufacturing hardware lines (Made In Space, Techshot)."),
    ("Made In Space (now Redwire)", r"made in space", "Ran the first ISS 3D printers; acquired by Redwire in 2020."),
    ("Techshot (now Redwire)", r"techshot", "ISS BioFabrication Facility and furnace hardware; acquired by Redwire in 2021."),
    ("Varda Space Industries", r"\bvarda\b", "Free-flying pharmaceutical processing capsule (W-series)."),
    ("Space Tango", r"space tango", "ISS CubeLab processing payloads for commercial pharma/biotech."),
    ("Axiom Space", r"axiom space", "Private astronaut missions and a planned commercial station."),
    ("Voyager / Nanoracks", r"voyager space|nanoracks", "Commercial ISS access (Nanoracks) and the planned Starlab station."),
    ("LambdaVision", r"lambda ?vision", "Layer-by-layer protein retinal implant manufacturing on the ISS."),
    ("ACME Advanced Materials / Astral Materials", r"acme advanced materials|astral materials",
     "Microgravity-processed silicon-carbide wafers."),
    ("Sierra Space / Sierra Nevada Corp.", r"sierra space|sierra nevada corp", "Dream Chaser cargo return and the LIFE habitat."),
    ("Boeing", r"\bboeing\b", "ISS prime contractor; Starliner."),
    ("Airbus", r"\bairbus\b", "Columbus/ESA payload hardware and space-grown materials furnaces."),
    ("Bristol-Myers Squibb", r"bristol[- ]myers", "Pharma ISS protein crystallization user."),
    ("Eli Lilly", r"eli lilly|lilly research", "Pharma ISS crystallization user."),
    ("JAXA", r"japan aerospace exploration|\bjaxa\b|national space development agency of japan|\bnasda\b",
     "Runs the Kibo high-quality protein crystal growth programme."),
    ("ESA", r"european space agency|\bestec\b|\besa[- ]estec\b|european space research and technology",
     "Runs the Material Science Laboratory, the Electromagnetic Levitator and the Fluid Science Laboratory on Columbus."),
    ("NASA Marshall Space Flight Center", r"marshall space flight", "NASA's microgravity materials and protein crystal growth centre."),
    ("NASA Glenn Research Center", r"glenn research center|lewis research center", "NASA's microgravity fluids and combustion centre."),
    ("NASA (any centre)", r"\bnasa\b|national aeronautics and space administration|marshall space flight|glenn research center|"
     r"ames research center|johnson space center|kennedy space center|jet propulsion laboratory|langley research center|"
     r"goddard space flight", "Operator of the US ISS segment and a major source of microgravity research."),
    ("CASIS / ISS National Lab", r"center for the advancement of science in space|\bcasis\b|iss national lab|"
     r"international space station national lab", "Manages the US ISS National Laboratory; selects and sponsors commercial payloads."),
    ("DLR", r"deutsches zentrum f(?:ü|u)r luft|german aerospace center|\bdlr\b", "Runs electromagnetic levitation (TEMPUS/EML) solidification research."),
    ("CNES", r"centre national d'(?:é|e)tudes spatiales|\bcnes\b", "French space agency (DECLIC fluid-physics instrument)."),
    ("China Manned Space / CAS", r"chinese academy of sciences", "Tiangong station materials and life-science racks."),
    ("SpaceX", r"spacex|space exploration technologies", "Dragon is the only routine pressurised cargo-return vehicle to the ISS; the foundry's launch and return provider."),
]
# Candidates matched on raw affiliation strings only, because OpenAlex mis-resolves other strings to them (see below).
RAW_ONLY = {"SpaceX"}
# Hand-verified false partner matches: text that is not an affiliation (here a table of launch companies
# parsed into raw_affiliation_strings) is excluded from the partner check.
FALSE_MATCHES = {("SpaceX", "W4206088203")}
# Hand-verified OpenAlex affiliation-resolution errors found while checking partner matches.
PARSING_ERRORS = [
    dict(work="W7222959925", raw="Redwire Space Technologies, Inc., 401 Exploration Wy, Georgetown, IN", resolved_to="SpaceX (United States)"),
    dict(work="W4206088203", raw="Bigelow Aerospace Robert Bigelow 1998 Las Vegas, Nevada, USA (a parsed reference, not an affiliation)", resolved_to="SpaceX (United States)"),
    dict(work="W4405587250", raw="Design & Development, Redwire Space N. V., Kruibeke, Belgium", resolved_to="Macquarie University"),
    dict(work="W1667042808", raw="NASDA, 2-2-1 Sengen, Tsukuba, Japan", resolved_to="National Association of State Departments of Agriculture"),
    dict(work="W2069195367", raw="National Space Development Agency of Japan, Tsukuba, Japan", resolved_to="Iwate Prefectural University"),
]
# Why-text for companies the data surfaces; each claim is backed by the example titles printed in the evidence.
SURFACED_WHY = {
    "Maruwa Foods and Biosciences": "Co-author on JAXA Kibo high-quality protein crystal growth papers: a company with repeated flight protein-crystallization experience.",
    "Confocal Science": "Co-author on the same JAXA Kibo protein crystal growth papers: a protein-crystallization service company with flight heritage.",
    "Advanced Engineering Services": "Japanese engineering firm on JAXA microgravity papers spanning SiGe crystal growth, protein crystallization and colloids.",
    "ZIN Technologies": "NASA Glenn contractor on ISS colloid physics experiments (colloid-polymer mixtures, colloidal aggregation).",
    "Northrop Grumman": "Authors on high-vacuum fused-filament 3D printer papers (in-space manufacturing hardware).",
    "Tec-Masters": "Operated ISS Microgravity Science Glovebox furnace experiments (SUBSA, PFMI transparent directional-solidification furnaces).",
    "Boeing": "ISS prime contractor; authors on in-space soldering and telerobotic protein-crystal handling papers.",
}


def collect(works):
    """Per-work affiliation facts: institution ids, company ids, countries, raw strings."""
    out = {}
    for w in works:
        insts, countries, raws = {}, set(), []
        for a in w.get("authorships") or []:
            for i in a.get("institutions") or []:
                if i.get("id"):
                    insts[i["id"]] = (i.get("display_name"), i.get("type"), i.get("country_code"))
            for c in a.get("countries") or []:
                countries.add(c)
            raws.extend(a.get("raw_affiliation_strings") or [])
        out[w["id"]] = dict(insts=insts, countries=countries, raws=raws, n_auth=len(w.get("authorships") or []))
    return out


def rank(work_ids, aff, pred):
    cnt, meta = Counter(), {}
    for wid in work_ids:
        for iid, (name, typ, cc) in aff[wid]["insts"].items():
            if pred(typ):
                cnt[iid] += 1
                meta[iid] = (name, typ, cc)
    return [(iid, meta[iid][0], meta[iid][1], meta[iid][2], n) for iid, n in
            sorted(cnt.items(), key=lambda kv: (-kv[1], meta[kv[0]][0] or ""))]


def partner_check(union_ids, aff, by_id, topic_sets):
    rows = []
    for name, pat, why in CANDIDATES:
        rx = re.compile(pat, re.I)
        inst_hits, raw_hits, matched_names = set(), set(), Counter()
        for wid in union_ids:
            if (name, short(wid)) in FALSE_MATCHES:
                continue
            hit = False
            for iid, (iname, _t, _c) in aff[wid]["insts"].items():
                if name not in RAW_ONLY and iname and rx.search(iname):
                    inst_hits.add(wid); matched_names[iname] += 1; hit = True
            if not hit and any(rx.search(r) for r in aff[wid]["raws"]):
                raw_hits.add(wid)
        allhits = inst_hits | raw_hits
        ex = sorted(allhits, key=lambda w: (-(by_id[w].get("cited_by_count") or 0)))[:2]
        rows.append(dict(
            name=name, why=why, papers=len(allhits), via_institution=len(inst_hits), via_raw_string_only=len(raw_hits),
            by_topic={k: len(allhits & topic_sets[k]) for k in TOPIC_ORDER if allhits & topic_sets[k]},
            matched_institution_names=[n for n, _ in matched_names.most_common(4)],
            first_year=min((by_id[w].get("publication_year") or 9999) for w in allhits) if allhits else None,
            last_year=max((by_id[w].get("publication_year") or 0) for w in allhits) if allhits else None,
            examples=[dict(id=short(w), year=by_id[w].get("publication_year"), title=(by_id[w].get("title") or "")[:160],
                           cited_by=by_id[w].get("cited_by_count")) for w in ex]))
    return rows


# Manual spot-check verdicts on a seeded random sample of 20 titles per topic (seed below).
# 1 = on-topic (space environment AND the topic), 0 = off-topic. Filled after reading titles.
SPOT_SEED = 20261024
SPOT_VERDICTS = {  # topic -> {work id: 1 on-topic / 0 off-topic}
    # protein (criterion: protein/macromolecular crystallization in microgravity or its space hardware)
    "protein": {
        "W2051464440": 1, "W1983465165": 1, "W2331883699": 1, "W1548473716": 1, "W2066067969": 1, "W76010161": 1,
        "W1974029316": 1, "W856350096": 0, "W1994413319": 1, "W2581118512": 0, "W7160300901": 0, "W64358940": 1,
        "W2602173915": 1, "W2997193453": 1, "W639639944": 0, "W2043358321": 0, "W2050849661": 1, "W4310415632": 1,
        "W3156031144": 1, "W4407383585": 0,
    },
    # pharma broad (criterion: small-molecule/API crystallization or pharmaceutical manufacturing in microgravity)
    "pharma": {
        "W76010161": 0, "W4387765028": 0, "W2022397364": 0, "W4417297530": 1, "W1649225513": 0, "W2765294661": 0, "W4407397176": 0,
        "W1493507514": 0, "W2046416276": 0, "W4248913915": 0, "W756944869": 0, "W7155039885": 0, "W1644543676": 0,
        "W7116284342": 1, "W4283781229": 0, "W1696111016": 0, "W2779400919": 0, "W4232778142": 0, "W746487623": 0,
        "W4232769410": 0,
    },
    # pharma narrow (same criterion)
    "pharma_narrow": {
        "W4248913915": 0, "W7116284342": 1,
        "W7172402837": 0, "W2955989050": 0, "W2001042199": 0, "W4292940656": 0, "W1605973031": 0, "W3008510099": 0,
        "W4414409735": 1, "W4413303918": 1, "W7152452513": 0, "W4372335789": 0, "W1972435319": 1, "W7222959925": 1,
        "W2488994498": 0, "W32133398": 0, "W7138937255": 0, "W810553473": 0, "W7154630877": 0, "W4411272933": 0,
    },
    # solidification / alloy (criterion: solidification/alloy processing or physics in microgravity / for space research)
    "solid": {
        "W7155190214": 1, "W2049838989": 1, "W1970641617": 1, "W2365821198": 1, "W848632458": 1, "W1493718527": 0,
        "W2060382729": 1, "W4392151444": 1, "W184299435": 1, "W88346221": 1, "W561141919": 1, "W1981374162": 0,
        "W2588553531": 1, "W4377013370": 1, "W855335812": 0, "W4312246293": 0, "W752508901": 1, "W2620600967": 1,
        "W2996526610": 1, "W4311404381": 0,
    },
    # colloid / photonic (criterion: colloidal or photonic-crystal physics/assembly in microgravity)
    "colloid": {
        "W836537407": 0, "W2081798132": 0, "W1979508649": 1, "W2980925236": 1, "W1563029948": 0, "W2095429027": 1,
        "W7169772745": 1, "W1968481711": 0, "W780791603": 1, "W1992023006": 1, "W3043618068": 1, "W7139944768": 0,
        "W7108088705": 0, "W3049282034": 1, "W4213330542": 1, "W2058898570": 1, "W2079680051": 0, "W4413876772": 1,
        "W4385766927": 1, "W55129518": 0,
    },
    # MOF: all 13 records (criterion: making/growing MOFs in real or simulated microgravity)
    "mof": {
        "W4408281627": 0, "W3016413958": 1, "W2112620464": 0, "W4206986030": 0, "W1848339474": 0, "W3183262270": 1,
        "W7171726912": 0, "W4405783820": 0, "W4386852633": 0, "W4245863642": 1, "W4416970026": 0, "W7171636870": 0,
        "W4390685176": 0,
    },
    # in-space manufacturing (criterion: manufacturing in orbit / in space)
    "ism": {
        "W4406525107": 1, "W2611071836": 1, "W7118010233": 0, "W2046826446": 1, "W3043025725": 1, "W4412485415": 1,
        "W1564779470": 0, "W274768690": 0, "W4391491463": 0, "W7211903596": 1, "W7131258638": 1, "W2003655521": 1,
        "W7125760395": 1, "W4413136861": 1, "W4402840516": 1, "W2105457723": 0, "W3164395732": 0, "W7213995789": 1,
        "W4390492714": 1, "W7202094788": 0,
    },
    # zeolite (criterion: zeolite synthesis/crystallization in microgravity)
    "zeolite": {
        "W2047769585": 1, "W1964927152": 1, "W2415558546": 0, "W1490691672": 1, "W2080720770": 1, "W7172536822": 0,
        "W1666086508": 0, "W1975999709": 0, "W2521190445": 1, "W7171612252": 0, "W7160293602": 0, "W2582016209": 0,
        "W3139818384": 1, "W2025753498": 1, "W2045707585": 1, "W612681788": 0, "W4234675044": 0, "W7160246954": 0,
        "W2289732548": 0, "W2315225106": 0,
    },
}
# Full title (and, where unclear, free single-work abstract) classification of all 132 pharma keyword hits
# (broad + narrow): works whose subject is small-molecule / API crystallization, solid form, or pharmaceutical
# ingredient manufacturing in microgravity. Protein-drug crystallization papers belong to the protein pillar.
PHARMA_SMALL_MOLECULE = {
    "W1972435319",  # 1990 new copper-phthalocyanine thin-film polymorph grown under reduced gravity
    "W4392594909",  # 2024 gravity as a knob for particle size distributions of small molecules
    "W4417297530",  # 2025 deep space environment for drug design/formulation (review)
    "W4414409735",  # 2025 microgravity-grown crystals as seeds for pharmaceutical compounds
    "W7116284342",  # 2025 manufacturing in microgravity and sample re-entry, commercial rideshare platform
    "W4413303918",  # 2025 space pharmaceutical manufacturing (review)
    "W4410896693",  # 2025 small-molecule crystallization in PIL-BOX
    "W4412486415",  # 2025 microgravity seed crystals for the pharmaceutical industry
    "W7222959925",  # 2026 microgravity crystallization of APIs: crystalline forms
    "W7160987556",  # 2026 Pharmaceutical In-Space Laboratory: commercialization
    "W7126088814",  # 2026 microgravity biomanufacturing of high-value pharmaceutical ingredients (API polymorphs)
}
# The 9 of 13 MOF hits that are about USING MOFs aboard spacecraft (air revitalization, CO2/humidity, H2,
# VOC sensing, shielding) or adjacent uses, not making them in orbit.
MOF_USE = {"W4408281627", "W4206986030", "W1848339474", "W7171726912", "W4405783820", "W4386852633",
           "W4416970026", "W7171636870", "W4390685176"}


def spot_sample(works, k=20):
    ids = sorted(w["id"] for w in works)
    rnd = random.Random(SPOT_SEED)
    return rnd.sample(ids, min(k, len(ids)))


def year_series(counter, lo, hi):
    return [[y, counter.get(y, 0)] for y in range(lo, hi + 1)]


def build(fx, args):
    accessed = dt.date.today().isoformat()
    topics = {}
    stop_note = None
    for k in TOPIC_ORDER + EXTRA:
        try:
            works, total, complete, pages = harvest(fx, k, args.max_pages)
        except BudgetStop as e:
            stop_note = str(e); print("BUDGET STOP:", e, file=sys.stderr); break
        uniq = {w["id"]: w for w in works}
        topics[k] = dict(works=list(uniq.values()), total=total, complete=complete, pages=pages)
        print(f"{k}: {len(uniq)} unique of meta.count {total} (complete={complete}, pages={pages})", file=sys.stderr)
        if not complete:
            topics[k]["years_api"] = group_years(fx, k)
    allw = all_works_by_year(fx)
    space_years, space_meta = space_only_by_year(fx)

    if args.spotcheck:
        for k in TOPIC_ORDER + EXTRA:
            by = {w["id"]: w for w in topics[k]["works"]}
            print(f"\n=== {k} ({len(by)})")
            for wid in spot_sample(topics[k]["works"]):
                w = by[wid]
                print(f"  {short(wid)} | {w.get('publication_year')} | {(w.get('title') or '')[:150]}")
        return

    by_id = {}
    topic_sets = {}
    for k in TOPIC_ORDER + EXTRA:
        for w in topics[k]["works"]:
            by_id[w["id"]] = w
        topic_sets[k] = {w["id"] for w in topics[k]["works"]}
    union_ids = set().union(*(topic_sets[k] for k in TOPIC_ORDER))
    aff = collect(by_id.values())
    this_year = dt.date.today().year

    # ---- per-year
    per_topic_year = {k: Counter(by_id[w].get("publication_year") for w in topic_sets[k]) for k in TOPIC_ORDER + EXTRA}
    union_year = Counter(by_id[w].get("publication_year") for w in union_ids)
    years_present = [y for y in union_year if y]
    y0 = max(1960, min(years_present)); y1 = this_year

    def window(cnt, a, b):
        return sum(v for y, v in cnt.items() if y and a <= y <= b)

    decade = {f"{a}-{b}": window(union_year, a, b) for a, b in [(1970, 1979), (1980, 1989), (1990, 1999), (2000, 2009), (2010, 2019), (2020, 2025)]}

    # ---- institutions / companies / countries / types
    top_inst = rank(union_ids, aff, lambda t: True)
    top_comp = rank(union_ids, aff, lambda t: t == "company")
    comp_works = {w for w in union_ids if any(t == "company" for (_n, t, _c) in aff[w]["insts"].values())}
    with_inst = {w for w in union_ids if aff[w]["insts"]}
    inst_types = Counter()
    for w in union_ids:
        for t in {t for (_n, t, _c) in aff[w]["insts"].values()}:
            inst_types[t or "unknown"] += 1
    countries = Counter()
    for w in union_ids:
        for c in aff[w]["countries"]:
            countries[c] += 1
    wtypes = Counter(by_id[w].get("type") or "unknown" for w in union_ids)
    auth_total = sum(len(by_id[w].get("authorships") or []) for w in union_ids)
    auth_noinst = sum(1 for w in union_ids for a in (by_id[w].get("authorships") or []) if not a.get("institutions"))
    auth_raw_noinst = sum(1 for w in union_ids for a in (by_id[w].get("authorships") or [])
                          if not a.get("institutions") and a.get("raw_affiliation_strings"))
    per_topic_comp = {}
    per_topic_inst = {}
    for k in TOPIC_ORDER + EXTRA:
        per_topic_comp[k] = [dict(name=n, papers=c, country=cc) for (_i, n, _t, cc, c) in rank(topic_sets[k], aff, lambda t: t == "company")[:8]]
        per_topic_inst[k] = [dict(name=n, papers=c, type=t, country=cc) for (_i, n, t, cc, c) in rank(topic_sets[k], aff, lambda t: True)[:8]]

    pc = partner_check(union_ids, aff, by_id, topic_sets)
    # zeolite / narrow-pharma hits are informative for partners too
    pc_extra = partner_check(topic_sets["zeolite"] | topic_sets["pharma_narrow"], aff, by_id, topic_sets)

    # ---- spot-check precision
    spot = {}
    for k in TOPIC_ORDER + EXTRA:
        sample = [short(w) for w in spot_sample(topics[k]["works"])]
        judged = [SPOT_VERDICTS[k][s] for s in sample if s in SPOT_VERDICTS.get(k, {})]
        if len(judged) != len(sample):
            print(f"WARNING spot-check {k}: {len(sample) - len(judged)} sampled works lack a verdict", file=sys.stderr)
        spot[k] = dict(sampled=len(sample), judged=len(judged), on_topic=sum(judged))

    # ---- bytes / records
    cache_files = [os.path.join(fx.cache_dir, f) for f in os.listdir(fx.cache_dir)]
    cache_bytes = sum(os.path.getsize(f) for f in cache_files)
    resp_bytes = 0
    for f in cache_files:
        with open(f) as fh:
            resp_bytes += json.load(fh).get("bytes", 0)
    credits_log = []
    logp = os.path.join(args.raw_dir, "requests.log.jsonl")
    if os.path.exists(logp):
        with open(logp) as fh:
            credits_log = [json.loads(l) for l in fh if l.strip()]
    live_ok = [r for r in credits_log if r.get("status") == 200]
    credits_used = sum(int(r.get("x-ratelimit-credits-used", 0)) for r in live_ok)
    ts = sorted(dt.datetime.fromisoformat(r["t"]) for r in live_ok)
    wall_min = round((ts[-1] - ts[0]).total_seconds() / 60, 1) if len(ts) > 1 else 0.0

    result = assemble(dict(locals()))
    with open(args.out, "w") as f:
        json.dump(result, f, indent=1, ensure_ascii=False)
    print(f"wrote {args.out} ({os.path.getsize(args.out)/1e3:.0f} kB); live calls this run {fx.live_calls}, "
          f"cache hits {fx.cache_hits}", file=sys.stderr)


def wilson(k, n, z=1.96):
    if n == 0:
        return (None, None)
    p = k / n
    d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d
    h = z * ((p * (1 - p) / n + z * z / (4 * n * n)) ** 0.5) / d
    return (round(c - h, 3), round(c + h, 3))


def assemble(c):
    by_id, topic_sets, union_ids = c["by_id"], c["topic_sets"], c["union_ids"]
    this_year = c["this_year"]
    per_topic_year, union_year, allw = c["per_topic_year"], c["union_year"], c["allw"]
    y0 = c["y0"]
    lab = {k: TOPICS[k][0] for k in TOPICS}
    n_union = len(union_ids)
    spot = c["spot"]

    # per-topic stats
    tstats = {}
    for k in TOPIC_ORDER + EXTRA:
        t = c["topics"][k]
        s = spot[k]
        p = s["on_topic"] / s["judged"] if s["judged"] else None
        lo, hi = wilson(s["on_topic"], s["judged"])
        n = len(topic_sets[k])
        tstats[k] = dict(label=lab[k], query=topic_query(k), api_count=t["total"], harvested_unique=n,
                         complete=t["complete"], pages=t["pages"],
                         spotcheck=dict(s, precision=round(p, 3) if p is not None else None, wilson95=[lo, hi]),
                         est_on_topic=round(n * p) if p is not None else None,
                         est_on_topic_95=[round(n * lo), round(n * hi)] if p is not None else None,
                         works_2016_2025=sum(v for y, v in per_topic_year[k].items() if y and 2016 <= y <= 2025),
                         works_2006_2015=sum(v for y, v in per_topic_year[k].items() if y and 2006 <= y <= 2015),
                         peak_year=max(((v, y) for y, v in per_topic_year[k].items() if y and y < this_year), default=(0, None))[1],
                         top_institutions=c["per_topic_inst"][k], top_companies=c["per_topic_comp"][k])
        if t.get("years_api"):
            tstats[k]["years_api_group_by"] = t["years_api"]

    pharma_sm = sorted(PHARMA_SMALL_MOLECULE & (topic_sets["pharma"] | topic_sets["pharma_narrow"]),
                       key=lambda w: by_id[w].get("publication_year") or 0)
    pharma_sm_ids = [w for w in by_id if short(w) in PHARMA_SMALL_MOLECULE]
    sm_years = Counter(by_id[w].get("publication_year") for w in pharma_sm_ids)
    sm_recent = sum(v for y, v in sm_years.items() if y and y >= 2024)
    mof_make = [w for w in topic_sets["mof"] if SPOT_VERDICTS["mof"].get(short(w)) == 1]
    mof_use = [w for w in topic_sets["mof"] if short(w) in MOF_USE]

    comp_share = len(c["comp_works"]) / n_union if n_union else 0
    inst_cov = len(c["with_inst"]) / n_union if n_union else 0
    comp_year = Counter(by_id[w].get("publication_year") for w in c["comp_works"])

    def share_window(a, b):
        tot = sum(union_year.get(y, 0) for y in range(a, b + 1))
        cw = sum(comp_year.get(y, 0) for y in range(a, b + 1))
        return dict(works=tot, company_works=cw, share=round(cw / tot, 3) if tot else None)

    company_share_by_era = {f"{a}-{b}": share_window(a, b) for a, b in [(1980, 1999), (2000, 2014), (2015, 2025)]}

    # charts -----------------------------------------------------------
    yr_lo, yr_hi = max(1965, y0), this_year
    ch_topics = dict(
        id="lit-per-year", kind="line",
        title="Papers per year pairing microgravity/spaceflight with each foundry process",
        subtitle=f"OpenAlex title+abstract keyword hits, {yr_lo}-{yr_hi} ({this_year} is partial)",
        x=dict(label="Publication year", unit="year", scale="time"),
        y=dict(label="Works", unit="works/year", scale="linear"),
        series=[dict(name=lab[k], points=year_series(per_topic_year[k], yr_lo, yr_hi), color=COLORS[k])
                for k in ["protein", "pharma", "solid", "colloid", "mof"]],
        annotations=[dict(x=this_year, y=0, text=f"{this_year}: partial year")],
        caption=("Raw keyword hits, not curated counts. Spot-check precision (share of 20 sampled titles that are on topic): "
                 + "; ".join(f"{lab[k]} {spot[k]['on_topic']}/{spot[k]['judged']}" for k in ["protein", "pharma", "solid", "colloid", "mof"])
                 + ". Pharma and MOF hits are mostly off-topic: see the frontier chart for their hand-classified counts."))
    per_m = []
    for y in range(max(1980, yr_lo), this_year):
        if allw.get(y):
            per_m.append([y, round(1e6 * union_year.get(y, 0) / allw[y], 2)])
    ch_ism = dict(
        id="ism-per-year", kind="line",
        title="In-space manufacturing papers per year",
        subtitle="Works matching an in-space / orbital / on-orbit manufacturing phrase (no space-term filter needed)",
        x=dict(label="Publication year", unit="year", scale="time"),
        y=dict(label="Works", unit="works/year", scale="linear"),
        series=[dict(name=lab["ism"], points=year_series(per_topic_year["ism"], yr_lo, yr_hi), color="orange")],
        annotations=[dict(x=this_year, y=0, text=f"{this_year}: partial year")],
        caption=(f"Keyword hits; spot-check precision {spot['ism']['on_topic']}/{spot['ism']['judged']}. Includes conference papers and NASA reports, "
                 "and some records about manufacturing on Earth for space."))
    mat_ids_c = set().union(*(topic_sets[k] for k in ["protein", "pharma", "solid", "colloid", "mof"]))
    mat_year_c = Counter(by_id[w].get("publication_year") for w in mat_ids_c)
    per_m_mat = [[y, round(1e6 * mat_year_c.get(y, 0) / allw[y], 2)] for y in range(max(1980, yr_lo), this_year) if allw.get(y)]
    ch_norm = dict(
        id="lit-per-million", kind="line",
        title="Share of the whole literature: foundry-process papers per million OpenAlex works",
        subtitle="Removes the growth of the literature as a whole (denominator: every OpenAlex work that year)",
        x=dict(label="Publication year", unit="year", scale="time"),
        y=dict(label="Works per million OpenAlex works", unit="per million", scale="linear"),
        series=[dict(name="All six topics (union)", points=per_m, color="cyan"),
                dict(name="Five materials topics (no in-space manufacturing)", points=per_m_mat, color="violet")],
        annotations=[],
        caption=("The 1990s Shuttle/Spacelab peak is visible. Since 2020 the gap between the two lines is in-space manufacturing. "
                 "OpenAlex indexes more non-article records over time, so part of the long decline reflects the denominator."))
    fr_years = list(range(1990, this_year + 1))
    mof_make_years = Counter(by_id[w].get("publication_year") for w in mof_make)
    ch_frontier = dict(
        id="lit-frontier", kind="bar",
        title="The thin frontier: hand-classified papers on making small-molecule drug crystals or MOFs in microgravity",
        subtitle=f"All {len(topic_sets['pharma'] | topic_sets['pharma_narrow'])} pharma and {len(topic_sets['mof'])} MOF keyword hits read by title (abstract where unclear)",
        x=dict(label="Publication year", unit="year", scale="time"),
        y=dict(label="Works", unit="works/year", scale="linear"),
        series=[dict(name="Small-molecule / API crystallization or pharma manufacturing in microgravity",
                     points=[[y, sm_years.get(y, 0)] for y in fr_years], color="violet"),
                dict(name="MOF growth in real or simulated microgravity",
                     points=[[y, mof_make_years.get(y, 0)] for y in fr_years], color="green")],
        annotations=[],
        caption=(f"{len(pharma_sm_ids)} small-molecule works ({sm_recent} from 2024 onward) and {len(mof_make)} MOF records "
                 f"(2 distinct studies plus a journal-cover record of one of them). {len(mof_use)} of the {len(topic_sets['mof'])} MOF hits are about using MOFs aboard "
                 "spacecraft (CO2, humidity, hydrogen, VOC sensing, shielding), not making them. Classification is ours; "
                 "keyword recall is not measured, so the true literature may be somewhat larger."))
    top_inst = c["top_inst"][:20]
    ch_inst = dict(
        id="lit-top-institutions", kind="hbar",
        title="Who publishes on foundry processes in space: top institutions",
        subtitle=f"Distinct works in the {n_union}-work union, by OpenAlex institution",
        x=dict(label="Institution", unit="", scale="category"),
        y=dict(label="Works", unit="works", scale="linear"),
        series=[dict(name="Works", points=[[n, k] for (_i, n, _t, _cc, k) in top_inst], color="cyan")],
        annotations=[],
        caption=("Counts every work on which at least one author lists the institution (fractional credit not applied). "
                 f"{round(100*inst_cov)}% of works have at least one resolved institution, so older NASA technical reports and conference abstracts are under-attributed."))
    top_comp = c["top_comp"][:20]
    ch_comp = dict(
        id="lit-top-companies", kind="hbar",
        title="Companies on the papers",
        subtitle="OpenAlex institutions typed 'company', distinct works in the union",
        x=dict(label="Company", unit="", scale="category"),
        y=dict(label="Works", unit="works", scale="linear"),
        series=[dict(name="Works", points=[[n, k] for (_i, n, _t, _cc, k) in top_comp], color="orange")],
        annotations=[],
        caption=(f"Companies appear on {len(c['comp_works'])} of {n_union} works ({round(100*comp_share,1)}%). Industry work is "
                 "mostly unpublished or patented, so this is a lower bound on industrial activity, not a market share."))
    pc_rows = [r for r in c["pc"]]
    ch_partner = dict(
        id="lit-partner-check", kind="hbar",
        title="Candidate partners: how many of these papers carry their affiliation?",
        subtitle="Regex match on OpenAlex institution names, plus raw affiliation strings where no institution was resolved",
        x=dict(label="Organisation", unit="", scale="category"),
        y=dict(label="Works", unit="works", scale="linear"),
        series=[dict(name="Works in the union", points=[[r["name"], r["papers"]] for r in pc_rows], color="green")],
        annotations=[],
        caption="Zero means no affiliated paper in this keyword set, not absence of activity: start-ups publish little and many results sit in patents and press releases.")
    countries = c["countries"].most_common(15)
    ch_cty = dict(
        id="lit-countries", kind="hbar", title="Countries of author institutions",
        subtitle="Distinct works with at least one author in the country",
        x=dict(label="Country (ISO-2)", unit="", scale="category"),
        y=dict(label="Works", unit="works", scale="linear"),
        series=[dict(name="Works", points=[[cc, k] for cc, k in countries], color="violet")],
        annotations=[], caption="Country is taken from OpenAlex authorship countries; works with no resolved affiliation are not counted.")

    # partners -------------------------------------------------------
    partners = []
    pc_by = {r["name"]: r for r in c["pc"]}
    for r in c["pc"]:
        if r["name"] == "SpaceX":
            rx_ = next((x for x in c["pc_extra"] if x["name"] == "SpaceX"), None)
            ex = "; ".join(f"{e['id']} ({e['year']}) \"{e['title'][:110]}\"" for e in (rx_ or {}).get("examples", []))
            partners.append(dict(name="SpaceX", why=r["why"] + " (Published fact about Dragon; the literature link is thin.)",
                                 evidence=(f"Our computation: {r['papers']} verified SpaceX-affiliated works in the six-topic union and "
                                           f"{(rx_ or {}).get('papers', 0)} in the narrow pharma set: {ex}. Two further OpenAlex 'SpaceX' "
                                           "attributions are parsing errors (W7222959925 is a Redwire author; W4206088203 is a parsed table).")))
            continue
        if r["papers"] == 0 or r["name"].startswith("NASA (any") or r["name"].startswith("Merck KGaA"):
            continue
        ex = "; ".join(f"{e['id']} ({e['year']}) \"{e['title'][:90]}\"" for e in r["examples"])
        bt = ", ".join(f"{lab[k]} {v}" for k, v in sorted(r["by_topic"].items(), key=lambda kv: -kv[1]))
        partners.append(dict(name=r["name"], why=r["why"],
                             evidence=(f"Our computation: {r['papers']} OpenAlex works in the {n_union}-work union carry this affiliation "
                                       f"({r['via_institution']} via a resolved institution, {r['via_raw_string_only']} via the raw affiliation string only); "
                                       f"{r['first_year']}-{r['last_year']}; by topic: {bt}. Examples: {ex}.")))
    # top data-surfaced companies not already in the candidate list
    cand_rx = [re.compile(p, re.I) for _n, p, _w in CANDIDATES]
    aff = c["aff"]

    def inst_evidence(iid):
        ws = [w for w in union_ids if iid in aff[w]["insts"]]
        bt = Counter(k for w in ws for k in TOPIC_ORDER if w in topic_sets[k])
        ex = sorted(ws, key=lambda w: -(by_id[w].get("cited_by_count") or 0))[:2]
        return ws, bt, ex

    surfaced = []
    for (iid, n, _t, cc, k) in c["top_comp"][:12]:
        if any(rx.search(n or "") for rx in cand_rx):
            continue
        if not any(key.lower() in (n or "").lower() for key in SURFACED_WHY):
            continue  # only companies whose example papers we reviewed
        surfaced.append((iid, n, cc, k))
    for iid, n, cc, k in surfaced[:7]:
        ws, bt, ex = inst_evidence(iid)
        why = "Surfaced by the data. " + next(v for key, v in SURFACED_WHY.items() if key.lower() in (n or "").lower())
        exs = "; ".join(f"{short(w)} ({by_id[w].get('publication_year')}) \"{(by_id[w].get('title') or '')[:90]}\"" for w in ex)
        partners.append(dict(name=n, why=why,
                             evidence=(f"Our computation: {k} works in the union list this company (OpenAlex {short(iid)}, {cc}); by topic: "
                                       + ", ".join(f"{lab[t]} {v}" for t, v in bt.most_common()) + f". Examples: {exs}.")))
    # who wrote the small-molecule frontier papers
    rx_red = re.compile(r"redwire", re.I)
    sm_red = [w for w in pharma_sm_ids if any(rx_red.search(r) for r in aff[w]["raws"]) or
              any(rx_red.search(n or "") for (n, _t, _c) in aff[w]["insts"].values())]
    sm_butler = [w for w in pharma_sm_ids if any("butler university" in (n or "").lower() for (n, _t, _c) in aff[w]["insts"].values())]
    sm_noaff = [w for w in pharma_sm_ids if not aff[w]["insts"] and not aff[w]["raws"]]
    if sm_butler:
        partners.append(dict(name="Butler University (with Redwire PIL-BOX)",
                             why="The academic group behind most published small-molecule crystallization results from Redwire's PIL-BOX on the ISS.",
                             evidence=(f"Our computation: Butler University is on {len(sm_butler)} of the {len(pharma_sm_ids)} hand-classified small-molecule "
                                       f"microgravity papers, and Redwire is on {len(sm_red)}: "
                                       + "; ".join(f"{short(w)} ({by_id[w].get('publication_year')})" for w in sm_butler) + ".")))
    per_m_dec = {}
    for a, b in [(1980, 1989), (1990, 1999), (2000, 2009), (2010, 2019), (2020, 2025)]:
        tot_u = sum(union_year.get(y, 0) for y in range(a, b + 1)); tot_a = sum(allw.get(y, 0) for y in range(a, b + 1))
        per_m_dec[f"{a}-{b}"] = round(1e6 * tot_u / tot_a, 1) if tot_a else None
    mat_ids = set().union(*(topic_sets[k] for k in ["protein", "pharma", "solid", "colloid", "mof"]))
    mat_year = Counter(by_id[w].get("publication_year") for w in mat_ids)
    per_m_dec_mat = {}
    for a, b in [(1980, 1989), (1990, 1999), (2000, 2009), (2010, 2019), (2020, 2025)]:
        tot_a = sum(allw.get(y, 0) for y in range(a, b + 1))
        per_m_dec_mat[f"{a}-{b}"] = round(1e6 * sum(mat_year.get(y, 0) for y in range(a, b + 1)) / tot_a, 1) if tot_a else None
    spx = pc_by.get("SpaceX", {})
    spx_extra = next((r for r in c["pc_extra"] if r["name"] == "SpaceX"), {})
    extra_hits = {r["name"] for r in c["pc_extra"] if r["papers"]}
    zero = [r["name"] for r in c["pc"] if r["papers"] == 0 and r["name"] not in extra_hits]

    # findings ---------------------------------------------------------
    tp = tstats
    top3 = ", ".join(f"{n} ({k})" for (_i, n, _t, _cc, k) in c["top_inst"][:3])
    topc = ", ".join(f"{n} ({k})" for (_i, n, _t, _cc, k) in c["top_comp"][:5])
    findings = [
        f"{n_union} distinct OpenAlex works pair a space-environment term with one of the six foundry processes in their title or abstract "
        f"(keyword hits; {c['space_meta']['count']} works match the space terms alone).",
        f"Solidification/alloy dominates the keyword set ({tp['solid']['harvested_unique']} works, spot-check precision {spot['solid']['on_topic']}/{spot['solid']['judged']}), "
        f"followed by in-space manufacturing ({tp['ism']['harvested_unique']}, {spot['ism']['on_topic']}/{spot['ism']['judged']}) and protein crystallization "
        f"({tp['protein']['harvested_unique']}, {spot['protein']['on_topic']}/{spot['protein']['judged']}).",
        f"Only {len(pharma_sm_ids)} works concern small-molecule crystals (APIs, pharmaceutical seed crystals, one pigment polymorph) or pharmaceutical-ingredient manufacturing in microgravity, "
        f"after hand-reading all {len(topic_sets['pharma'] | topic_sets['pharma_narrow'])} pharma keyword hits; {sm_recent} of them appeared in 2024 or later. This is a new and very thin literature.",
        f"MOF growth in (simulated) microgravity has {len(mof_make)} records (2 distinct studies). {len(mof_use)} of the {len(topic_sets['mof'])} MOF+space hits are about using MOFs aboard spacecraft. "
        f"Zeolites, the closest porous-crystal precedent, have {tp['zeolite']['harvested_unique']} keyword hits with spot-check precision {spot['zeolite']['on_topic']}/{spot['zeolite']['judged']}, much of it from 1987-2003 Shuttle/EURECA work.",
        f"Top institutions by distinct papers: {top3}.",
        f"Companies are on {len(c['comp_works'])} of {n_union} works ({round(100*comp_share,1)}%). The most frequent are {topc}.",
        "Company share by era (works with at least one company affiliation): "
        + "; ".join(f"{e} {v['company_works']}/{v['works']}" for e, v in company_share_by_era.items()) + ".",
        f"In-space manufacturing papers peaked in {tp['ism']['peak_year']} among complete years: {tp['ism']['works_2016_2025']} in 2016-2025 vs {tp['ism']['works_2006_2015']} in 2006-2015.",
        ("Candidate partners with zero affiliated works in this set: " + ", ".join(zero).rstrip(".") + ". A zero is not evidence of no activity.") if zero else "Every candidate partner has at least one affiliated work.",
        f"The small-molecule frontier is concentrated: Redwire is on {len(sm_red)} and Butler University on {len(sm_butler)} of the {len(pharma_sm_ids)} papers, "
        f"Varda on {pc_by['Varda Space Industries']['papers']}, and {len(sm_noaff)} {'carries' if len(sm_noaff) == 1 else 'carry'} no affiliation data at all.",
        f"Normalised to all OpenAlex works, the six-topic union went from {per_m_dec['1990-1999']} per million works in the 1990s (the Shuttle/Spacelab era) to {per_m_dec['2010-2019']} in the 2010s "
        f"and {per_m_dec['2020-2025']} in 2020-2025. The five materials topics alone went {per_m_dec_mat['1990-1999']} to {per_m_dec_mat['2010-2019']} to {per_m_dec_mat['2020-2025']}, "
        "so the recent uptick is mostly in-space manufacturing, while materials-in-microgravity research is a steady niche.",
        f"SpaceX is a verified author affiliation on {spx.get('papers', 0)} union works and {spx_extra.get('papers', 0)} in the narrow pharma set "
        "(drug content after a commercial EVA). OpenAlex attributes two other works to SpaceX by mistake, so its institution field alone cannot be trusted here.",
    ]
    limitations = [
        "Keyword search over titles and abstracts (OpenAlex stemmed title_and_abstract.search). Precision was measured by reading a seeded random sample of 20 titles per topic "
        "(all 13 for MOF); recall was not measured, so works that never use our phrases are missed.",
        "Precision varies widely: " + "; ".join(f"{lab[k]} {spot[k]['on_topic']}/{spot[k]['judged']} (95% Wilson {tstats[k]['spotcheck']['wilson95'][0]}-{tstats[k]['spotcheck']['wilson95'][1]})" for k in TOPIC_ORDER + EXTRA) + ".",
        "The on-topic judgements and the small-molecule/MOF classification are ours (an AI agent reading titles, plus abstracts from free single-work lookups where unclear). They are not peer-reviewed.",
        "OpenAlex mis-resolves some affiliation strings (hand-verified examples in stats.affiliation_parsing_errors_found: a Redwire author resolved to SpaceX, NASDA to an agricultural association). "
        "Institution counts therefore carry noise of a few works per organisation.",
        f"OpenAlex affiliation coverage is incomplete: {round(100*inst_cov)}% of works have at least one resolved institution, and {c['auth_noinst']} of {c['auth_total']} authorships have none "
        f"({c['auth_raw_noinst']} of those still carry a raw affiliation string, which we search for partners). Institution parsing errors and mergers (e.g. Techshot and Made In Space into Redwire) split counts.",
        f"{this_year} is a partial year, and recent works are still being indexed.",
        "The per-million normalisation divides by every OpenAlex record, and OpenAlex's coverage of non-article records grows over time, so the normalised decline partly reflects indexing, not only attention.",
        "Records include conference abstracts, NASA technical reports, journal covers, corrections and duplicates (e.g. three 'Manufacturing in the Void' records), so counts are works, not independent studies.",
        "Company affiliation counts undercount industry work: most pharma and materials process data is unpublished, patented, or released as press material.",
        f"Without an API key OpenAlex refuses cursor paging past page 1, so pages 2+ used basic page=N paging. For solidification this returned {tp['solid']['harvested_unique']} of {tp['solid']['api_count']} works "
        "(the API's own group_by counts per year are stored in stats for comparison).",
        "A correlation between publication volume and any market is not established here. Paper counts measure research attention, not demand or technical maturity.",
    ]
    stats = dict(
        union_works=n_union, space_terms_only_works=c["space_meta"]["count"],
        union_by_decade=c["decade"], company_works=len(c["comp_works"]), company_share=round(comp_share, 4),
        company_share_by_era=company_share_by_era,
        works_with_resolved_institution=len(c["with_inst"]), authorships=c["auth_total"], authorships_without_institution=c["auth_noinst"],
        institution_type_mix=dict(c["inst_types"].most_common()), work_type_mix=dict(c["wtypes"].most_common()),
        topics=tstats,
        pharma_small_molecule_works=[dict(id=short(w), year=by_id[w].get("publication_year"), title=by_id[w].get("title")) for w in
                                     sorted(pharma_sm_ids, key=lambda w: by_id[w].get("publication_year") or 0)],
        mof_microgravity_growth_works=[dict(id=short(w), year=by_id[w].get("publication_year"), title=by_id[w].get("title")) for w in mof_make],
        top_institutions=[dict(name=n, type=t, country=cc, works=k, id=short(i)) for (i, n, t, cc, k) in c["top_inst"][:40]],
        top_companies=[dict(name=n, country=cc, works=k, id=short(i)) for (i, n, t, cc, k) in c["top_comp"][:40]],
        countries=dict(c["countries"].most_common(25)),
        partner_check=c["pc"], partner_check_zeolite_and_narrow_pharma=[r for r in c["pc_extra"] if r["papers"]],
        affiliation_parsing_errors_found=PARSING_ERRORS, union_per_million_openalex_works_by_decade=per_m_dec,
        materials_topics_per_million_openalex_works_by_decade=per_m_dec_mat,
        small_molecule_frontier_affiliations=dict(redwire=[short(w) for w in sm_red], butler=[short(w) for w in sm_butler],
                                                  no_affiliation_data=[short(w) for w in sm_noaff]),
        openalex_all_works_by_year={str(y): allw[y] for y in sorted(allw) if 1960 <= y <= this_year},
        space_terms_by_year={str(y): v for y, v in sorted(c["space_years"].items()) if 1960 <= y <= this_year},
        api_budget=dict(credits_used_logged=c["credits_used"], live_requests_logged=len(c["live_ok"]),
                        last_remaining=(c["live_ok"][-1].get("x-ratelimit-remaining") if c["live_ok"] else None),
                        note="Logged on the Mac IP only; single-work lookups used to read unclear abstracts are free and are not logged."),
    )
    total_records = sum(len(topic_sets[k]) for k in TOPIC_ORDER + EXTRA)
    return {
        "id": "literature-map",
        "tab": "network",
        "title": "The literature no human can read: 50 years of microgravity process papers",
        "question": "How much published work pairs microgravity or spaceflight with each foundry process, who writes it, and which partners does the record actually support?",
        "headline": {"value": f"{len(pharma_sm_ids)}",
                     "unit": "papers",
                     "text": (f"Of {n_union:,} papers pairing microgravity with a foundry process, just {len(pharma_sm_ids)} concern crystallizing small molecules or drug ingredients "
                              f"in microgravity, and {sm_recent} of those are from 2024 or later. The pharma-crystal frontier is brand new.")},
        "evidence_level": "our computation on public data",
        "datasets": [{"name": "OpenAlex works API (title_and_abstract.search, 8 queries)",
                      "url": "https://api.openalex.org/works", "license": "CC0",
                      "records": total_records, "bytes": c["resp_bytes"], "accessed": c["accessed"],
                      "notes": (f"{len(by_id)} distinct works harvested across 8 queries ({n_union} in the six-topic union); "
                                "fields id, doi, title, publication_year, type, cited_by_count, authorships (institutions, countries, raw affiliation strings). "
                                "Plus 3 group_by calls (all works by year, space terms by year, solidification by year). Raw JSON cached outside the repo.")}],
        "compute": {"where": "local Mac (API work, stdlib Python)", "partitions": [], "job_ids": [], "cpu_hours": 0.0,
                    "wall_minutes": c["wall_min"], "peak_storage_gb": round(c["cache_bytes"] / 1e9, 3),
                    "notes": (f"{c['credits_used']} OpenAlex credits logged on the Mac IP ({len(c['live_ok'])} live requests, plus one 10-credit manual paging test); "
                              "0 on the Engaging IP. No API key. wall_minutes is the span from the first to the last live request (it includes probing pauses).")},
        "method": [
            "Space terms: microgravity OR \"micro-gravity\" OR spaceflight OR \"space flight\" OR \"International Space Station\" OR \"space station\" OR \"reduced gravity\" (a bare 'ISS' was avoided as ambiguous).",
            "Each topic phrase set was ANDed with the space terms inside one OpenAlex title_and_abstract.search filter (boolean parsing verified in meta.x_query). In-space manufacturing was searched on its own.",
            "All matching works were harvested (page 1 via cursor=*, pages 2+ via page=N, 200 per page), deduplicated by OpenAlex work id, and analysed locally.",
            "Works per year per topic come from the harvested records; the union de-duplicates across the six topics. A plain group_by over all OpenAlex works gives the per-million normalisation.",
            "Institutions were counted per distinct work (any author). Companies are institutions whose OpenAlex type is 'company'. Countries come from authorship countries.",
            "Precision: a seeded random sample of 20 titles per topic (all 13 for MOF) was judged on- or off-topic. All 132 pharma hits were read and classified, and unclear abstracts were checked with free single-work lookups.",
            "Partner check: case-insensitive regexes for each candidate organisation, matched against resolved institution names, and against raw affiliation strings for authorships with no resolved institution.",
        ],
        "charts": [ch_topics, ch_frontier, ch_ism, ch_norm, ch_inst, ch_comp, ch_partner, ch_cty],
        "stats": stats,
        "findings": findings,
        "limitations": limitations,
        "future_big_data": [
            "Run the same queries on the OpenAlex S3 snapshot (s3://openalex, about 0.5 TB of works) on Engaging. It has no API budget, and would allow full-text-free recall checks and citation-network analysis (who cites the pembrolizumab and PIL-BOX papers).",
            "Add patents (USPTO PatentsView, Lens.org) and NASA Technical Reports Server records, where most industrial microgravity process work lives.",
            "Link to the ISS National Lab and NASA Physical Sciences Informatics payload lists to connect each paper to a flown experiment and its return vehicle.",
            "Replace keyword matching with an embedding classifier trained on our hand labels, and measure recall against a curated bibliography such as the NASA protein crystal growth reviews.",
        ],
        "partners": partners,
        "code": ["analysis/bigdata/logistics_literature.py"],
        "reproduce": [
            "python3 -I analysis/bigdata/logistics_literature.py --raw-dir <cache-dir> --out data/results/bigdata/literature-map.json --max-pages 20",
            "# rerun from the cached responses with zero API calls:",
            "python3 -I analysis/bigdata/logistics_literature.py --raw-dir <cache-dir> --out data/results/bigdata/literature-map.json --max-pages 20 --offline",
        ],
        "generated_at": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"),
    }

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--raw-dir", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--offline", action="store_true", help="use cache only; fail on any uncached call")
    ap.add_argument("--max-pages", type=int, default=20, help="cap per topic (x200 works)")
    ap.add_argument("--min-remaining", type=int, default=40)
    ap.add_argument("--probe", action="store_true", help="fetch one page per topic and print counts")
    ap.add_argument("--spotcheck", action="store_true", help="print a random 20-title sample per topic")
    ap.add_argument("--topics", default=",".join(TOPIC_ORDER))
    args = ap.parse_args()
    fx = Fetcher(args.raw_dir, args.offline, args.min_remaining)

    if args.probe:
        for k in args.topics.split(","):
            w, total, complete, pages = harvest(fx, k, 1)
            body = fx.get({"filter": f"title_and_abstract.search:{topic_query(k)}", "select": SELECT,
                           "per_page": PER_PAGE, "cursor": "*"})
            print(k, "count", total, "per_page", body["meta"].get("per_page"), "got", len(w))
            print("   oqo:", json.dumps(body["meta"].get("x_query", {}).get("oql", ""))[:400])
        return

    build(fx, args)


if __name__ == "__main__":
    main()
