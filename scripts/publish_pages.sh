#!/usr/bin/env bash
# Build the site and publish dist/ to the public GitHub Pages repo.
# Usage: scripts/publish_pages.sh [owner/repo]   (default fvrarturo/zero-g-spot)
set -euo pipefail
REPO="${1:-fvrarturo/zero-g-spot}"
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
python3 "$ROOT/scripts/build.py"
STAGE="$(mktemp -d)"
cp -R "$ROOT/dist/." "$STAGE/"
# Sponsor handout is not ours to republish.
rm -f "$STAGE/docs/SpaceXAI Cal Hacks 13.0 Starter Pack.pdf"
touch "$STAGE/.nojekyll"
cat > "$STAGE/README.md" <<'MD'
# Orbital Foundry · zero-g-spot

Live site for **Orbital Foundry**, our Cal Hacks 13.0 entry for the SpaceXAI "Make it Legendary" challenge: a shared orbital materials foundry, backed by big-data analyses of public space archives (PDB space-grown crystals, 60 years of satellite tracking, NASA ISS experiment data, launch and return records).

This repository only holds the built static site. Team: Arturo Favara and Emma Sampietro.
MD
cd "$STAGE"
git init -q -b main
git add -A
git commit -q -m "Publish Orbital Foundry site"
git remote add origin "git@github.com:${REPO}.git"
git push -q -f origin main
echo "Published to https://github.com/${REPO}"
