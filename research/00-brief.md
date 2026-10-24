# 00. What the starter pack actually asks for

Source: `docs/SpaceXAI Cal Hacks 13.0 Starter Pack.pdf`, read 24 October 2026. The sponsor name on the PDF is **SpaceXSI**, not SpaceX. The project README already paraphrases the challenge. This note keeps the original constraints next to the research so idea selection does not drift.

## What they give

- One month of X Premium for every attendee: Cursor, Grok Bot, X, and Grok. Codes were handed out at the SpaceXSI booth.
- A workshop on Friday 23 October 2026 at 8:00 PM.
- People on site: Zach Carlo, and the Berkeley campus leads. Help is the booth or the Cal Hacks Discord.

## The challenge, in their words

“Space gives you more to work with than almost any other field. You have access to enormous public datasets, decades of missions, and a literature no human can read all of. Real space data goes in and a legendary project comes out.”

Eligibility:

- The project must be built with Cursor. They say more Cursor use makes a win more likely.
- Bonus points for using Grok Bot for project planning and team collaboration.
- Submit to the **Make it Legendary** challenge on Devpost.

Prizes: a Cursor mechanical keyboard for every member of the winning team. Everyone who submits is in a raffle for a Cursor Owala bottle.

## What the team already wrote down

From the project README, which matches the pack:

- Use big data about space: Earth observation, satellite imagery, mission archives, and the space literature.
- Lead with the problem. Pick a clear, real problem and a credible idea for solving it. The technical details matter less than the problem and the idea.

Team: Arturo Favara, Emma Sampietro.

## What “legendary” can mean this weekend

Today is Saturday 24 October 2026. The workshop was last night. A judge will see the project for a few minutes. The pack does not define a rubric beyond “real space data goes in” and “legendary.” Reading the pack against the 2026 market (see [01-structural-gap.md](01-structural-gap.md)) suggests four tests:

1. **A person who is not a remote-sensing specialist understands the problem in one sentence.** The industry’s own complaint is that pixels do not become decisions. A project whose problem requires a SAR lecture has already lost the brief.
2. **Real public data is on the screen.** A mock of a commercial API, or a model trained on a toy chip, does not match “real space data goes in.”
3. **The idea is a thing someone would use**, not a tour of a dataset. The pack says the literature is too big to read and the datasets are enormous. The legendary version is a person asking a question and getting an answer with a picture and a source.
4. **The technical flex is optional.** Foundation models, InSAR processors, and new constellations are what startups spend years on. The brief says the idea matters more than the technical detail. Calling an existing analysis-ready product and explaining it is aligned. Training a new Earth foundation model is not.

## Environment, as far as it should go before an idea is chosen

Cursor is the required build environment. Grok is available in this chat. No application stack is set up yet, on purpose: Earth Engine, Planetary Computer, a Python map, and a small web page are different projects, and picking one before the problem creates junk.

X Premium on your own account was not reachable from this session. Details are in the [index](README.md).

## How the rest of the research is aimed

The pack names four piles of input: Earth observation, satellite imagery, mission archives, and the literature. The research treats those as the supply. The demand is the thing the pack does not name: a person who needs an answer. Almost every source below says the supply is no longer the scarce part.
