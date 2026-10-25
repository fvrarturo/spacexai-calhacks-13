"""Manual verdicts on the candidate entries flagged by pdb_classify.py (read 2026-10-24).

Every one of the 382 candidates in candidates.csv was read: the 110 the automatic rule labelled
space / context_only / simulated / ground_control in full (growth text, title, keywords, citation),
and the 272 labelled "none" through their own-text hit snippets (pdbx_database_related-only hits,
i.e. mentions of *other* entries, were not treated as evidence). A loose recall sweep over all
261,139 entries (pdb_classify near-miss list) found no further space-grown entries.

LABELS   entry_id -> space | mixed | ground_control | unclear | noncrystal | none
           space          the entry's own text says its crystal grew in microgravity / in space
           mixed          data merged from space- and Earth-grown crystals (1A34, 4NIA)
           ground_control the entry's own text says it is the Earth/ground counterpart of a flight
           unclear        cannot tell from the text; kept out of both groups
           noncrystal     microgravity sample but not a crystal (cryo-EM fibrils)
           none           false positive (MIR phasing, LMS ligand, 'orbital' shaker, 'in space' = size...)
         Candidates not listed here keep the automatic label, which for all of them is "none".
PLATFORM entry_id -> Shuttle | Mir | ISS | Other | Unknown, where the automatic tag needed fixing.
KEYWORD_TIER  space entries whose evidence is a keyword / citation title only (sensitivity analysis).
"""

_none = ("12PL 1AR5 1B24 1B7E 1B9H 1BDX 1ECL 1EGA 1IGV 1JFM 1OJT 1SPP 2GAW 2IUM 2PGO 2VNS 2W8M 4RIL 4ZNN 9YT3 "
         "1GPX 1WTM 1WTN 1AZF 1B0D 1B2K 1G9W")
_space = ("1BEN 1BWJ 1DGW 1E05 1HF4 1IEE 1K6F 1KQP 1L0W 1M2T 1MVQ 1P7V 1P7W 1TVQ 1TW4 2HLC 2PVB 3D7W 3UG1 3X2L "
          "4Y04 5F2C 5YRE 5YRH 6COA 6JTB 7X4O 9BVY 9BW2 9BWM "
          "194L 1EQZ 1LGV 1LHZ 1N9H 1N9X 1NAZ 1VDP 1VDS 1VDT 1VED 1WYI 2CY1 3O5W 4A8I 4A8L 4A8N 4A8R 4I5Z 5J8L "
          "5TY5 6IJY 6JTC 6Z9Z 7RTX 8EYP 8HDD 8ZSU 9K8Z 9WQU "
          "4FMP 4I5Y 6W8E 9KL1 9L3S")
_ground = "1BWH 193L 1BVX 1BWI 1N9F 1N9I 4OQ8 4OQ9 6W7P 8ZST 9K7R 9KKZ"
_unclear = "1914 1VDQ 2ANT 7DKB 7DKC 7DKD 7DKE 8EYS 8EZC 1OBQ 1OBU"
_mixed = "1A34 4NIA"
_noncrystal = "9M5P 9M5Q 9M5R 9UMH"

LABELS: dict[str, str] = {}
for _lab, _ids in [("none", _none), ("space", _space), ("ground_control", _ground), ("unclear", _unclear),
                   ("mixed", _mixed), ("noncrystal", _noncrystal)]:
    for _i in _ids.split():
        LABELS[_i] = _lab

PLATFORM: dict[str, str] = {
    # APCF flew on several Shuttle missions and on the ISS; the text names no vehicle
    "1P7V": "Unknown", "1P7W": "Unknown",
    # 'ISS6A' / 'ISS8A' crystal labels = ISS assembly flights 6A / 8A (earth-grown twins carry the same label)
    "1N9H": "ISS", "1N9X": "ISS", "1NAZ": "ISS",
    # PCDF is ESA's protein facility on the ISS (Columbus); text says 'PCDF-PROTEIN mission'
    "4A8I": "ISS", "4A8L": "ISS", "4A8N": "ISS", "4A8R": "ISS",
    # same DPP11 '(Space)' series as 6JTB, whose text names Kibo
    "6JTC": "ISS",
    # Spacehab-01 = STS-57
    "194L": "Shuttle",
}

KEYWORD_TIER = set("1EQZ 2CY1 3O5W 4I5Y 4I5Z 4FMP 8HDD".split())

NOTES: dict[str, str] = {
    "1914": "'150 X 150 X 300 MM3 IN SPACE' reads as crystal size; no flight named",
    "1A34": "IML-1 Shuttle: 8 space-grown and 12 Earth-grown crystals merged into one data set",
    "4NIA": "IML-1 Shuttle: two crystal_grow rows, 9 space-grown and 12 Earth-grown crystals",
    "1OBQ": "space/Earth pair with identical text; cannot tell which entry is which",
    "1OBU": "space/Earth pair with identical text; cannot tell which entry is which",
    "1VDQ": "same Aibara/DeLucas series as 1VDP/1VDS/1VDT/1VED but title lacks 'in space'",
    "2ANT": "cites 'Improved diffraction of antithrombin crystals grown in microgravity' but own text silent",
    "7DKB": "keyword 'Microgravity' but hanging-drop growth and unrelated paper",
    "8EYS": "same paper as microgravity-grown 8EYP; this crystal's origin not stated",
    "8EZC": "same paper as microgravity-grown 8EYP; this crystal's origin not stated",
    "1EQZ": "keyword 'MICROGRAVITY HISTONE OCTAMER' only",
    "2CY1": "keyword MICROGRAVITY + citation on reduced twinning under microgravity",
    "3O5W": "keyword microgravity + counter-diffusion",
    "4I5Y": "keyword 'space grown' (Langmuir-Blodgett insulin)",
    "4I5Z": "keyword 'space grown' (Langmuir-Blodgett insulin)",
    "4FMP": "citation title 'elucidation of its space-grown crystal structure'",
    "8HDD": "citation title 'Microgravity environment grown crystal structure ...'",
    "9BVY": "neutron structure", "9BW2": "neutron structure", "9BWM": "neutron structure",
    "5TY5": "neutron structure", "8EYP": "joint X-ray/neutron structure",
    "12PL": "LMS = 5'-O-sulfamoyladenosine ligand", "9YT3": "LMS = ligand",
    "4RIL": "orbital mixing plate", "4ZNN": "orbital mixing plate",
}
