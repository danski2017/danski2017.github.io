---
type: dynamic_parameter_sweep
status: completed
created: 2026-05-26
topics:
  - atlas-dynamics
  - seams
  - normalized-threshold
  - lineage
---

# Normalized Seam Sweep 2026-05-26

## Purpose

Test whether a scale-normalized seam criterion improves over fixed absolute proximity threshold.

## Rule Tested

Legacy seam rule:

`distance_between_crossing_clouds < absolute_threshold`

Normalized rule:

`distance_between_crossing_clouds < coefficient * pair_local_crossing_spacing`

where pair-local crossing spacing is estimated from median nearest-neighbor spacing in the two crossing clouds.

This is a comparison branch, not a final certified seam rule.

## Sweep

Six-step runs at:

- `c_toy = 8`, spacing coefficients `1`, `2`, `4`
- `c_toy = 12`, spacing coefficients `1`, `2`, `4`

Summary artifacts:

`/Users/danski2017/Desktop/Atlas_Solver_Project/codex_context/dynamic_evolution/skeleton_smoke_20260526/normalized_seam_sweep_20260526/normalized_seam_sweep_summary.json`

`/Users/danski2017/Desktop/Atlas_Solver_Project/codex_context/dynamic_evolution/skeleton_smoke_20260526/normalized_seam_sweep_20260526/normalized_seam_sweep_summary.png`

Run sizes:

- c8 k1: `48M`
- c8 k2: `48M`
- c8 k4: `48M`
- c12 k1: `43M`
- c12 k2: `43M`
- c12 k4: `43M`

## Results

Seam totals across six steps:

| c_toy | k=1 | k=2 | k=4 |
|---:|---:|---:|---:|
| 8 | `393` | `570` | `1056` |
| 12 | `834` | `1144` | `1909` |

Node totals across six steps:

| c_toy | k=1 | k=2 | k=4 |
|---:|---:|---:|---:|
| 8 | `14` | `22` | `20` |
| 12 | `41` | `49` | `28` |

Mean effective distance thresholds:

| c_toy | k=1 | k=2 | k=4 |
|---:|---:|---:|---:|
| 8 | `0.9531996` | `1.9063989` | `3.8127980` |
| 12 | `1.3365373` | `2.6730744` | `5.3461490` |

## Read

The normalized rule is conceptually cleaner than the absolute threshold because it scales with crossing-cloud sampling density.

However, it is not yet a certified seam rule. Seam totals still scale strongly with coefficient, and `c_toy = 12` remains much denser than `c_toy = 8`.

The normalized rule improves the framing of the problem but does not solve seam certification.

## Interpretation

The seam layer probably needs more than a distance threshold.

Useful next ingredients:

- temporal persistence across update steps
- pair identity continuity
- local crossing-shell spacing
- local crossing-shell curvature
- constraint residual concentration
- radial provenance from Tier 1 traces

## Claim Ceiling

Seams/nodes remain live diagnostics only.

The normalized rule is a better comparison branch, not a final physical extraction standard.

## Next Move

Add a seam lineage/persistence filter: retain only seams that recur for the same source pair across neighboring update steps and survive modest threshold variation.

## Follow-Up

Completed:

`/Users/danski2017/Desktop/Atlas_Solver_Project/Relational_Labs/Relational_Labs/Atlas Codex Bridge/Dynamic Evolution/Seam Lineage Filter 2026-05-26.md`

Read:

The lineage filter separates transient source-pair contacts from recurring seam support. At `c_toy = 8`, source-0 pair seams are transient in the six-step window, while pairs `1-2`, `1-3`, and `2-3` persist. At `c_toy = 12`, all six source pairs persist under the tested normalized coefficients.
