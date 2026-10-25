# Verification record

24 October 2026. This records software and data-pipeline checks, not qualification of orbital hardware or a new materials result.

- Original tracked research files and original README compared byte-for-byte with Git HEAD after moving to `initial-work/`. The original untracked HTML was preserved before extraction; its SHA-256 is in `initial-work/ARCHIVE.md`.
- Build completed. Both generated HTML pages have unique IDs and all statically referenced local assets and files resolve.
- Eleven Python tests passed: reproducible workloads, feasible capabilities, non-overlapping chamber occupancy, return timing, conservation, empty/failure cases, hidden-outcome independence, sensitivity coverage, matching and independent-block inference.
- JavaScript compatibility assertions passed for exact resource boundaries, exceeded power/heat, camera contention and mixing/quiet-growth conflicts.
- Browser verified at 1440 and 417 px: document width matches viewport width. The pair table and navigation scroll within their containers.
- Original story: material selection, presentation start/advance/exit, and link to research workspace verified.
- Research workspace: published concentration selector, pair selection, failed resource/disturbance screens, imaging contention, matrix selection, sensitivity scenario selection, task filtering and note persistence verified. Original note content restored after the persistence check.
- No browser console errors observed during these interaction checks.
- Twelve real NASA bitmap files verified against their stored SHA-256 hashes and processed for descriptive QC.
- Published comparison arithmetic and EXPRESS power-bound arithmetic checked against stored inputs.
- All 24 local sensitivity scenarios generated and validated before summary. Engaging array `26809678` completed all 24 tasks with exit 0. All result files are byte-for-byte identical to the local run; accounting and comparisons are in `data/results/engaging.json`.

Re-run `npm test`, `npm run build`, and the relevant analysis after modifying algorithms or input data. Browser working notes are not a shared backend. The site requires HTTP serving (`npm run dev`); opening generated HTML with `file://` does not support its JSON loading.
