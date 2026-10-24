# 08. Ideas that fit the brief

Constraints used to score these, from [00-brief.md](00-brief.md) and the cards:

- Real public space data on the screen.
- A problem a non-specialist understands in one sentence.
- A thing someone would use, not a tour of a sensor.
- Buildable by Sunday. Today is Saturday 24 October 2026.
- Does not pretend to replace ICEYE, Carbon Mapper, or Global Fishing Watch.
- Does not require Chinese commercial imagery, a NISAR SLC processor, or a fine-tune.

Scores are 1–5. Higher is better for this weekend. They are judgments, not measurements.

| Idea | Problem clarity | Data is public and reachable | Weekend odds | Collision with an incumbent | “Legendary” if the demo works |
| --- | ---: | ---: | ---: | ---: | ---: |
| A. What happened here | 5 | 5 | 5 | 3 | 4 |
| B. The methane letter | 5 | 5 | 5 | 3 | 5 |
| C. The unannounced maneuver | 5 | 4 | 3 | 2 | 5 |
| D. Fire in the way | 5 | 5 | 5 | 4 | 4 |
| E. One flood, whose buildings | 5 | 4 | 4 | 4 | 4 |
| F. Papers for this place | 3 | 5 | 4 | 2 | 2 |

Incumbent collision means “someone will say this already exists.” A high number is a warning.

## A. What happened here

**Sentence.** A city staffer or a reporter types a place and a month and gets one page: what changed, whether there was water or fire, and the exact public products that say so.

**User.** The person in the Cambridge study and the European survey. They will not open QGIS. They have a question on a deadline.

**Data.** OPERA DIST and DSWx if the place is in coverage, Dynamic World or WorldCover, FIRMS for that month, AlphaEarth embeddings for the two surrounding years as a “did the year change” check. Planetary Computer or Earth Engine.

**Demo.** One scripted place you have already checked by hand, plus one live query in the same country so a failure is debuggable. The page shows maps, dates, scene or product ids, and a short paragraph written only from those fields.

**Why it matches the pack.** It uses a large archive. The idea is the page, not a model. Grok can write the paragraph and must not be allowed to add a number that is not in the JSON.

**Risk.** It becomes a generic chatbot over Earth Engine. The fix is a fixed checklist of products, not an open-ended agent. terrAIntel is the commercial cousin. You win by being specific, sourced, and free, on one kind of question.

## B. The methane letter

**Sentence.** Here is a methane plume, here is how many times it was seen, here is the public inventory site it sits on, here is the paragraph a journalist can paste, and here is what we do not know.

**User.** A reporter or a local regulator who has heard “super-emitter” and cannot read a NetCDF.

**Data.** Carbon Mapper API or portal, non-commercial terms. EMIT Version 3 methane enhancement, released 16 October 2026, used only where you have actually loaded a scene. Climate TRACE solid-waste or oil-and-gas points as the “named facility” layer, which is what Carbon Mapper’s own tutorial does.

**Demo.** Three sources: one landfill, one energy site, one single detection you label as unconfirmed. The third one is what makes the project honest.

**Why it is the sharpest story.** The problem is one physical thing. The data got a new version eight days ago. The picture is obvious. Kayrros and Carbon Mapper own the detection. You would own the letter, and only if the letter is more careful than a screenshot of their portal.

**Risk.** Reproducing their map with extra text. The fix is the join to a named site, the count of repeats, the instrument, the version, and an explicit “do not use commercially” line so you stay inside their terms.

## C. The unannounced maneuver

**Sentence.** Half the satellites Starlink had to worry about this year do not say where they are going. Here is one orbital shell tonight, split into “published a trajectory” and “only a stale catalog entry,” in words a person can read.

**User.** A space-curious public, a student journalist, a policymaker who saw the October headlines and cannot read a conjunction data message.

**Data.** Starlink’s public ephemeris manifest. CelesTrak or space-track for everyone else. ESA’s 14 September 2026 report for the trend numbers you cite and do not recompute. space-safety.com as a screenshot of the closed door, not as an API.

**Demo.** One altitude band. Starlink tracks in one color. A handful of other public objects in another. A side panel with SpaceX’s own 650 / 164,000 figures and ESA’s health-index jump, each linked. A list of claims you refuse to make: no probability of collision, no “near miss” unless the source is SpaceX or ESA’s wording, no health diagnosis of a Chinese satellite from a TLE.

**Why a SpaceX-sponsored table might remember it.** It is the sponsor’s own problem, from the last three weeks, and the project does not flatter it. The closed screening tool and the missing half are the point. Earth imagery is absent. The pack allows mission data and “space,” not only pictures of the ground. If the team wants the project to feel like space rather than like a mapping startup, this is the one.

**Risk.** Fake precision. Hugh Lewis, McDowell, and Samson are the people who will mentally grade it, and a wrong probability is a failed project. The other risk is that it looks like a CelesTrak skin. The writing and the refusal-to-claim are the product.

## D. Fire in the way

**Sentence.** A FIRMS detection is not a fire perimeter. It is a point. Here is the land under it and the buildings within a distance you chose, and here is the last optical scene, including if that scene is cloudy or smoked out.

**User.** A local desk, a mutual-aid coordinator, a person checking on a place.

**Data.** FIRMS API, a building footprint layer, WorldCover or Dynamic World, one Sentinel-2 or Landsat browse.

**Demo.** A fire from this season that you have verified, shown as a card. A button that admits “we do not have a perimeter.”

**Risk.** ICEYE and OroraTech announced the paid version of “full lifecycle wildfire” on Wednesday. You are the public, worse, faster, honest card. That is a fine hackathon. It is a bad startup pitch. Say the limitation out loud.

## E. One flood, whose buildings

**Sentence.** For this flood, this is the public water mask, these are the building footprints that touch it, this is the time of the scene, this is not a depth and not an insurance payout.

**User.** The same person ICEYE sells to, without a contract.

**Data.** OPERA DSWx or a Copernicus emergency activation if one is public for the event you pick. Building footprints. A DEM only if you are willing to explain a depth method in one paragraph you can defend.

**Risk.** Depth. Skip depth unless you can cite a method and show where it fails in dense streets. Extent plus buildings is enough.

## F. Papers for this place

**Sentence.** The pack says nobody can read the literature. For this dataset or this place, here are the papers and the open question they agree on.

**Data.** ADS and NTRS, plus one of the archives above.

**Why it is last.** It matches a line in the starter pack and it demos badly next to a map. Use it as a tab inside A or B (“what has been published about this site”), not as the whole project.

## Recommendation

Build **B, the methane letter**, if you want the clearest problem and the newest data. The picture is a plume. The user is obvious. The off-the-shelf pieces are an API and a join. The technical story stays in the background, which is what the brief asked for.

Build **A, what happened here**, if you want the project to stand for the whole industry problem rather than one gas. It is the safer demo and the easier one to extend if a judge asks “can it do a flood too.”

Build **C, the unannounced maneuver**, if the room you are pitching cares that the sponsor is a space company and you are willing to be strict about what you will not compute. It is the most timely. It is the easiest to get wrong.

Do not build a hybrid of A, B, and C. Three problems on one map is how the demo becomes a portal, and the portals are the thing users already cannot use.

## What to leave alone

- A new foundation model, or a fine-tune of Prithvi or TerraMind.
- A satellite marketplace.
- A crop-yield platform.
- A Global Fishing Watch clone.
- A global carbon-offset auditor.
- A NISAR processor.
- Anything that needs Jilin-1, Vantor, or a tasking budget.
- A chatbot that picks its own datasets. The Φ-week warning and the versioning mess (EMIT this month, NISAR BETA versus PROVISIONAL) are the reasons.

## A shape that stays credible

Whatever you pick, the page has five blocks and no more:

1. The question, in the user’s words.
2. The picture, from a named product and a named time.
3. The sentence, with numbers only from the file you fetched.
4. The unknowns: clouds, version, revisit gap, commercial terms, no perimeter, no probability.
5. The links: granule, paper or user guide, and the incumbent who already does the professional version.

That is the whole idea. The rest of this folder is why those five blocks are the part nobody has finished, even though the pixels are already down.
