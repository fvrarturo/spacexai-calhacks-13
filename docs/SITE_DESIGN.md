# Orbital Foundry — cinematic site

## Routes and editing

- `index.html` and the existing `workspace.html` bookmark: vision, problem, advantages and decision gates.
- `materials.html`: mechanisms, five material dossiers, published viscosity comparison and analysis workflow.
- `foundry.html`: selectable systems schematic, sharing map, concurrent-stage screen, challenges and proposed SpaceX/xAI roles.
- `network.html`: scalable concept visualization, 24-scenario results explorer and staged expansion plan.
- `research.html`: the prior research workspace, preserved with its data and local working notes.
- `story.html`: the prior modular story and complete original source catalogue.

Narrative source: `site/pages/`. Shared navigation/footer: `site/templates/mission-*.html`. Interactive components: `site/static/js/mission/`. Styles: `site/static/css/mission.css` and `mission-interactive.css`. The five dossiers are in `site/content/material-dossiers.json`. The broader research catalogue remains intact, including bijels as an additional candidate.

The build consumes generated materials and scenario-count results for the vision metrics. Interactive result charts load the existing generated JSON. Illustrative diagrams and stage loads are explicitly labeled. The network size control changes a concept illustration; it does not calculate economic or fleet-performance predictions. There are no live external integrations or partnership claims.

## Big-data evidence layer (added 24 Oct 2026, evening)

- `site/static/js/mission/evidence.js` renders every `data/results/bigdata/*.json` into evidence panels: a headline, SVG charts (bar, hbar, stacked, hist, line with bands, scatter with reference lines, log axes), findings, data/compute chips and a link to the appendix. It also handles partner cards, the future-data lists, the home headline cards, the NASA frame gallery and the appendix. There are no external libraries.
- `scripts/build.py` writes `results/bigdata/index.json` with de-duplicated totals: "processed" bytes exclude archives that were only catalogued. It also fills `{{BIGDATA_*}}` placeholders and drops any evidence slot whose result file is missing, so the public site never shows placeholders.
- `site/content/evidence-display.json` picks charts, series and short captions per tab. The appendix always shows every chart with its full caption.
- `site/content/partners.json` holds the curated partner cards with aliases. Partners named by the analyses are matched to cards ("IN OUR DATA"), and the rest appear as compact chips.
- Styles: `site/static/css/mission-evidence.css`, imported by `mission.css`. Charts draw on scroll only when motion is enabled.
- Verified at 1440 px and at 390 px (no document-level horizontal overflow on any chapter), with zero console errors and zero placeholder panels.

## Visual system

Near-black space, cool atmospheric blue, warm furnace orange, restrained typography, thin technical rules and generous editorial spacing. Canvas particles and vapor fields respond to scrolling; the foundry SVG has animated service and observation paths. Crystals and the network are procedural editable canvas illustrations. These are not scientific simulations or microscopy.

One 30 fps animation loop serves all canvases. Off-screen scenes do not render, background tabs pause, disconnected specimen scenes are released, and pixel density is capped at 2. The system reduced-motion preference and a persistent header motion switch disable decorative movement. Navigation and controls use native links, buttons, labels, selects and disclosures. Mobile tables and the detailed foundry schematic pan within their own containers.

## Hero artwork provenance

Generated with the built-in image-generation tool, then encoded as WebP without creative edits. Final project asset: `site/static/assets/orbital-foundry-hero.webp` (329,030 bytes). Original generated PNG remains at `/Users/arturofavara/.codex/generated_images/01a170b7-4c6f-7921-8dce-618138decee4/exec-cc5bc53c-286c-4bff-84de-9dcbd9ddee17.png`. The artwork is labeled as an artist’s concept on the site.

Exact generation prompt:

> Use case: stylized-concept. Asset type: cinematic 16:9 website hero background for an orbital materials foundry research concept. Create an extraordinarily detailed, physically plausible hard-science-fiction 3D render of a compact unmanned orbital manufacturing spacecraft above Earth's curved blue atmosphere at night. Main spacecraft placed in the right half of the frame, left 45% mostly deep near-black space for overlaid typography. Spacecraft is a striking modular cylindrical silver and graphite industrial vessel, longitudinal ribbing, carefully engineered white ceramic and brushed titanium panels, small burnt-orange illuminated furnace/cartridge windows, delicate copper plumbing, precision seams, a broad dark-blue rectangular solar array angling toward lower right. Three-quarter view, vessel axis diagonal lower-left to upper-right, beautiful rim light from pale sun off-frame upper right; subtle cyan blue light reflected from Earth below. Earth occupies bottom quarter, recognizable clouds, deep ocean, thin brilliant electric-blue atmospheric limb curved across frame. Fine stars sparingly in pure black space. Mood: awe, high-end aerospace editorial, scientific precision, quiet and ambitious; exceptionally beautiful contrast and material texture. No text, no typography, no logos, no watermarks, no interface, no lasers in the image, no explosions, no people, no busy extra spacecraft. Concept art, not a diagram. Wide landscape composition.

## Verification

- Static build passes; local HTTP response 200.
- Existing 11 Python analysis tests and JS compatibility boundary checks pass.
- JavaScript syntax checks pass for the entry module and all four new component modules.
- Local page, asset and fragment references resolve for all seven public/research/story routes.
- Browser QA at 1440 × 1000 and 390 × 844; additional smallest-width home check at 320 × 780. All four chapters fit the mobile page width without document-level horizontal overflow.
- All five material selectors show the matching dossier. Viscosity concentration changes from 50 to 75 mg/ml and shows 29.7% for the latter.
- Foundry observation selector updates the system readout. Two cooling stages fail the 600 W / 400 W budgets; protein + MOF pass with staggered imaging and fail without it.
- All 24 fleet scenarios render all four policies. Scenario 0 shows +6.4 percentage points versus dedicated; scenario 23 shows −11.4 points. This is synthetic evidence, not a flight result.
- Motion pause/resume control and persistence across chapter navigation verified. OS reduced-motion behavior is implemented via media query and JavaScript preference detection; no OS setting was changed during QA.
- No browser console errors observed. The preserved research workspace still loads.
- Screenshots: `docs/mission-desktop.jpg` and `docs/mission-mobile.jpg`.

Run `npm run dev` to explore locally at `http://127.0.0.1:4173`. The QA server is stopped during teardown. No publication or deployment was performed.
