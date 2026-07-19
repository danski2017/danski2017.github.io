---
type: dynamic_diagnostic
status: active
created: 2026-05-26
topics:
  - atlas-dynamics
  - cluster12
  - dropout
  - gcs-extraction
  - gfro
---

# Cluster12 Dropout Diagnostic 2026-05-26

## Purpose

Diagnose the late-run GCS crossing dropout observed for sources `5` and `6` in the 12-source robust run.

This diagnostic keeps the field formula, source motion, residual mode, and cluster initial data fixed. It varies only extraction bookkeeping/search-window controls.

## Source Updates

Compute source:

`/Users/danski2017/Desktop/Atlas_Solver_Project/codex_context/dynamic_evolution/skeleton_smoke_20260526/atlas_skeleton_compute_local.py`

Added:

- `ATLAS_RANDOM_SEED`, default `1729`, to make adaptive scout selection reproducible.
- numeric source-id sorting for seam and node pair construction.
- per-source extraction metadata in `step_data`:
  - `extraction_rmax_start`
  - `extraction_rmax_next`
  - `extraction_ray_count`
  - `extraction_crossing_radius_median`
- `ATLAS_RMAX_FLOOR_NEAREST_FACTOR`, default `0.0`, to optionally prevent the adaptive radial search window from collapsing below a declared fraction of nearest-neighbor distance.

Default behavior remains unchanged unless `ATLAS_RMAX_FLOOR_NEAREST_FACTOR` is set.

## Baseline Reproduction

Run id:

`cluster12_dropout_baseline_seeded_65_20260526`

Settings:

- `ATLAS_SCENE_MODE=cluster12`
- `ATLAS_CLUSTER_SCALE=2.0`
- `ATLAS_C_TOY=20`
- `ATLAS_N_STEPS=65`
- `ATLAS_N_RAYS_BASE=120`
- `ATLAS_N_TARGETED=90`
- `ATLAS_N_SCOUT=30`
- `ATLAS_N_RADIAL=14`
- `ATLAS_INITIAL_RMAX_FACTOR=0.9`
- `ATLAS_ENABLE_EIH_ACCELERATION=0`
- `ATLAS_RANDOM_SEED=1729`

Runtime:

`470.5s`

Ledger size:

`607M`

Result:

The dropout reproduced deterministically. Sources `5` and `6` both dropped to zero crossings at update step `62`.

Late-step source `5` extraction:

| step | crossings | gated crossings | rmax start | rmax next | median crossing radius |
|---:|---:|---:|---:|---:|---:|
| 60 | 36 | 36 | 1.023008 | 0.660608 | 0.471863 |
| 61 | 18 | 16 | 0.660608 | 0.189443 | 0.135316 |
| 62 | 0 | 0 | 0.189443 | 0.189443 | null |
| 63 | 0 | 0 | 0.189443 | 0.189443 | null |
| 64 | 0 | 0 | 0.189443 | 0.189443 | null |

Late-step source `6` extraction:

| step | crossings | gated crossings | rmax start | rmax next | median crossing radius |
|---:|---:|---:|---:|---:|---:|
| 60 | 47 | 47 | 0.979939 | 0.644977 | 0.460698 |
| 61 | 44 | 44 | 0.644977 | 0.244537 | 0.174669 |
| 62 | 0 | 0 | 0.244537 | 0.244537 | null |
| 63 | 0 | 0 | 0.244537 | 0.244537 | null |
| 64 | 0 | 0 | 0.244537 | 0.244537 | null |

Root-quality gate totals:

- original crossings: `48,732`
- kept crossings: `29,804`
- original seams: `4,296`
- gated seams: `4,254`
- root multiplicity: `{1: 48718, 2: 14}`
- multi-root crossing records: `14`

## Residual Sign Probe

At step `62`, all sampled radial trace values for sources `5` and `6` inside the collapsed window were positive:

- source `5`: min residual `1553.370931`, max residual `12428016.68404`
- source `6`: min residual `590.619672`, max residual `4726205.550644`

Positive residual means `||E_self|| > ||E_context||` everywhere sampled. That means the extractor had not sampled far enough outward to find the next zero crossing.

Offline same-step probing with wider radial shells found roots again:

Source `5`, nearest-neighbor distance `3.361256`:

| rmax factor | rmax | roots |
|---:|---:|---:|
| 0.25 | 0.840314 | 0 |
| 0.50 | 1.680628 | 0 |
| 0.75 | 2.520942 | 33 |
| 1.00 | 3.361256 | 54 |
| 1.50 | 5.041884 | 86 |
| 2.00 | 6.722512 | 130 |
| 3.00 | 10.083769 | 219 |

Source `6`, nearest-neighbor distance `3.361256`:

| rmax factor | rmax | roots |
|---:|---:|---:|
| 0.25 | 0.840314 | 0 |
| 0.50 | 1.680628 | 2 |
| 0.75 | 2.520942 | 45 |
| 1.00 | 3.361256 | 65 |
| 1.50 | 5.041884 | 93 |
| 2.00 | 6.722512 | 136 |
| 3.00 | 10.083769 | 240 |

## Radius-Floor Verification

Run id:

`cluster12_dropout_rfloor075_63_20260526`

Settings match the baseline reproduction except:

- `ATLAS_N_STEPS=63`
- `ATLAS_RMAX_FLOOR_NEAREST_FACTOR=0.75`

Runtime:

`466.8s`

Ledger size:

`598M`

Result:

The dropout was removed at update step `62`.

Late-step source `5` extraction:

| step | crossings | gated crossings | rmax start | rmax next | median crossing radius |
|---:|---:|---:|---:|---:|---:|
| 58 | 28 | 28 | 1.572415 | 1.326352 | 0.947394 |
| 59 | 32 | 32 | 1.326352 | 1.023007 | 0.730719 |
| 60 | 36 | 36 | 1.023007 | 0.660608 | 0.471863 |
| 61 | 16 | 12 | 0.660608 | 0.199508 | 0.142506 |
| 62 | 7 | 7 | 2.520942 | 2.943817 | 2.102727 |

Late-step source `6` extraction:

| step | crossings | gated crossings | rmax start | rmax next | median crossing radius |
|---:|---:|---:|---:|---:|---:|
| 58 | 41 | 41 | 1.581367 | 1.326504 | 0.947503 |
| 59 | 41 | 41 | 1.326504 | 0.979939 | 0.699956 |
| 60 | 47 | 47 | 0.979939 | 0.644977 | 0.460698 |
| 61 | 45 | 45 | 0.644977 | 0.241682 | 0.172630 |
| 62 | 23 | 23 | 2.520942 | 2.796186 | 1.997276 |

Root-quality gate totals:

- original crossings: `48,615`
- kept crossings: `29,537`
- original seams: `4,492`
- gated seams: `4,449`
- root multiplicity: `{1: 48607, 2: 8}`
- multi-root crossing records: `8`

Gated lineage:

- retained lineage candidates: `1`
- intermittent lineage candidates: `10`

## Interpretation

The source `5` and `6` dropout was isolated as adaptive radial-window collapse.

The GCS residual did not disappear. The extractor stopped looking far enough outward after the median crossing radius collapsed near the source at step `61`.

This is not a physics certification. It is an extraction robustness fix.

## Concern

Ledger cost remains large:

- baseline 65-step dropout reproduction: `607M`
- radius-floor 63-step verification: `598M`
- dynamic workspace after these diagnostics: `2.8G`

Any full 75-step rerun with the radius floor should be treated as a deliberate certification candidate, not casual exploration.

## Next Move

Run a 75-step cluster candidate with:

- `ATLAS_RMAX_FLOOR_NEAREST_FACTOR=0.75`
- fixed `ATLAS_RANDOM_SEED=1729`
- same field and motion settings as the robust run

Then apply root-quality gate and seam lineage before rendering or interpretation.
