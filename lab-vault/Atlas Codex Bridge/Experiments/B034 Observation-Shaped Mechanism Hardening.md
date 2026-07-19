---
type: experiment_note
status: completed
created: 2026-05-15
program:
  - mesoscale-curvature
  - sparc
  - residual-closure
  - observation-shaped-hardening
claim_level: mechanism_hardening_no_dark_matter_claim
---

# B034 Observation-Shaped Mechanism Hardening

## Purpose

B034 tests whether the B033 filtered residual-vs-`E/vc2` alignment survives observation-shaped ledger perturbations.

This is not a full cube refit. It is a targeted public-readiness hardening pass using existing B033 filtered primary baryon-sector rings.

## Source Package

- Experiment package: `codex_context/experiments/B034_observation_shaped_mechanism_hardening`
- Script: `codex_context/scripts/b034_observation_shaped_mechanism_hardening.py`
- Variant table: `derived/B034_OBSERVATION_VARIANT_ROWS.csv`
- Galaxy summary: `derived/B034_GALAXY_HARDENING_SUMMARY.csv`
- Summary: `derived/B034_SUMMARY.json`

## Perturbations

B034 varied:

- local support filter:
  - all rings,
  - support above p25,
  - support above p50,
- radial metric smoothing:
  - window `1`,
  - window `3`,
  - window `5`,
- inclination-style residual perturbation:
  - `-3 deg`,
  - `0 deg`,
  - `+3 deg`.

Total variant rows: `81`.

## Result

| Galaxy | Positive Pearson | Pearson Min | Pearson Median | Pearson Max | Spearman Median |
|---|---:|---:|---:|---:|---:|
| NGC1003 | 27 / 27 | 0.7654 | 0.8247 | 0.9640 | 0.8429 |
| NGC2403 | 27 / 27 | 0.2724 | 0.6959 | 0.7471 | 0.8693 |
| NGC5055 | 27 / 27 | 0.1577 | 0.5939 | 0.6250 | 0.8883 |

Global positive Pearson fraction: `1.0`.

Global median Pearson: `0.6959`.

## Read

B034 strengthens the mechanism story.

After denominator-risk filtering in B033, the residual-vs-`E/vc2` alignment survives support filtering, radial smoothing, and inclination-style residual perturbation in all tested primary variants.

This still does not make a dark-matter claim. The result is narrower:

> In the existing local SPARC/HALOGAS source-proxy ledgers, residual-adjacent radial structure in the relative tensor/scalar transfer hierarchy survives first observation-shaped perturbations.

## Claim Boundary

- No dark-matter claim.
- No MOND test.
- Ledger perturbation only.
- Not a replacement for full cube refitting.
- Not a survey-level result.

## Consequence

B034 justifies updating the internal draft bundle. The public-readiness gap is no longer broad simulation volume; it is presentation and exact claim language.
