---
type: dynamic_robust_run
status: completed
created: 2026-05-26
topics:
  - atlas-dynamics
  - cluster12
  - robust-run
  - gcs-foam
  - gfro
---

# Cluster12 Robust 75 Step Run 2026-05-26

## Purpose

Set up and execute a 75-step, 12-source variable-mass cluster simulation with one visual frame per update step.

This is a robust diagnostic run, not certification.

## Source Changes

Compute source:

`/Users/danski2017/Desktop/Atlas_Solver_Project/codex_context/dynamic_evolution/skeleton_smoke_20260526/atlas_skeleton_compute_local.py`

Added:

- `ATLAS_SCENE_MODE=cluster12`
- `ATLAS_CLUSTER_SCALE`
- `ATLAS_N_RAYS_BASE`
- `ATLAS_N_TARGETED`
- `ATLAS_N_SCOUT`
- `ATLAS_N_RADIAL`
- `ATLAS_DT`
- `ATLAS_HEADROOM`
- `ATLAS_INITIAL_RMAX_FACTOR`
- `ATLAS_EXTRACT_EVERY`
- `ATLAS_ENABLE_EIH_ACCELERATION`

Render source:

`/Users/danski2017/Desktop/Atlas_Solver_Project/codex_context/dynamic_evolution/skeleton_smoke_20260526/render_fixed_gcs_foam_animation.py`

Added:

- 12-source color palette
- source-name rendering from `step_data`
- truthful legend when 1PN arrows are hidden

## Robust Run

Run id:

`cluster12_robust75_c20_scale2_20260526`

Output:

`/Users/danski2017/Desktop/Atlas_Solver_Project/codex_context/dynamic_evolution/skeleton_smoke_20260526/cluster12_robust75_c20_scale2_20260526`

Command settings:

- `ATLAS_SCENE_MODE=cluster12`
- `ATLAS_CLUSTER_SCALE=2.0`
- `ATLAS_C_TOY=20`
- `ATLAS_N_STEPS=75`
- `ATLAS_N_RAYS_BASE=120`
- `ATLAS_N_TARGETED=90`
- `ATLAS_N_SCOUT=30`
- `ATLAS_N_RADIAL=14`
- `ATLAS_INITIAL_RMAX_FACTOR=0.9`
- `ATLAS_ENABLE_EIH_ACCELERATION=0`

Runtime:

`528.0s`

Run size:

`684M`

Dynamic workspace size after run:

`1.6G`

## Manifest Summary

- scene: `cluster12`
- source count: `12`
- `c_toy`: `20.0`
- PN parameter: `0.034176`
- GCS residual mode: `self_cleaned_r5`
- GFRO status: `GFRO-structured diagnostic; not GFRO-certified`
- crossing battery records: `53,689`
- radial scalar traces: `1,174,544`
- shadow lane records: `2,664`
- EIH acceleration records: `0`

EIH finite-difference acceleration was disabled because the 12-source finite-difference EIH check is too expensive for a 75-step robust run. L0 and L1 Lagrangian summaries remain present.

## Visual Outputs

Fixed-camera GIF, one frame per update step:

`/Users/danski2017/Desktop/Atlas_Solver_Project/codex_context/dynamic_evolution/skeleton_smoke_20260526/cluster12_robust75_c20_scale2_20260526/figures/atlas_fixed_camera_gcs_foam_animation.gif`

Final frame:

`/Users/danski2017/Desktop/Atlas_Solver_Project/codex_context/dynamic_evolution/skeleton_smoke_20260526/cluster12_robust75_c20_scale2_20260526/figures/atlas_fixed_camera_gcs_foam_final_frame.png`

GIF size:

`6.6M`

Final frame size:

`180K`

1PN arrows were hidden in the visual render to keep 12-source foam readable.

## Run Diagnostics

Total seams:

`5,036`

Total nodes:

`31`

First step crossing counts:

`[28, 46, 39, 68, 59, 39, 31, 41, 35, 54, 69, 120]`

Final step crossing counts:

`[10, 14, 70, 23, 27, 0, 0, 24, 35, 60, 67, 109]`

First step GCS radii:

`[3.426962, 2.781256, 3.093690, 4.733942, 5.401450, 5.213854, 4.283826, 6.330871, 5.608138, 7.258975, 6.936701, 7.366587]`

Final step GCS radii:

`[0.913956, 0.863303, 10.156733, 1.572415, 1.424176, 0.189443, 0.244537, 3.341038, 3.219378, 2.540989, 3.294619, 7.527711]`

Root multiplicity:

- root histogram: `{1: 53574, 2: 88, 3: 27}`
- crossing records in multi-root rays: `115`

Residual slope magnitude:

- min: `0.000023`
- median: `0.010650`
- max: `584196.060268`

## Concerns

1. Some sources lose GCS crossings late in the run.

Sources `5` and `6` have zero accepted crossings by the final frame. This may represent real local dominance/occlusion under the declared residual, or it may signal extraction-radius/adaptive-ray failure.

2. Multi-root rays appeared.

The robust run produced `115` crossing records from multi-root rays. This confirms root metadata was needed.

3. Seam/node counts are active but uncertified.

`5,036` seams and `31` nodes should not be physically interpreted until root-quality gating and lineage are applied.

4. Ledger size is now a hard constraint.

This single robust diagnostic run is `684M`.

5. EIH acceleration comparison is disabled.

This is acceptable for setup, but the run lacks finite-difference EIH acceleration comparison.

## Read

The robust 12-source cluster simulation is successfully set up and rendered.

The run is useful as a stress diagnostic. It is not yet a certification run.

The most important new signal is that the larger scene produced multi-root rays and late-run crossing loss for some sources. Those are exactly the cases the new GFRO root metadata was intended to expose.

## Next Move

Apply root-quality gating and seam lineage to this robust run before changing the physics or increasing resolution.

## Root Quality Gate Pass

Date:

`2026-05-26`

Gate source:

`/Users/danski2017/Desktop/Atlas_Solver_Project/codex_context/dynamic_evolution/skeleton_smoke_20260526/apply_root_quality_gate.py`

Gate output:

`/Users/danski2017/Desktop/Atlas_Solver_Project/codex_context/dynamic_evolution/skeleton_smoke_20260526/cluster12_robust75_c20_scale2_20260526/root_quality_gate`

Gate settings:

- minimum absolute R5 residual slope: `0.005`
- multi-root rays allowed: `false`
- seam threshold: `0.6`

Gate totals:

- original crossings: `53,689`
- kept crossings: `33,541`
- rejected crossings: `20,148`
- kept fraction: `0.624728`
- original seams: `5,036`
- gated seams: `4,963`

First frame:

- original crossings: `629`
- kept crossings: `486`
- original seams: `73`
- gated seams: `73`

Final frame:

- original crossings: `439`
- kept crossings: `315`
- original seams: `64`
- gated seams: `58`

Source survival summary:

| source | original | kept | kept fraction | zero original steps | zero gated steps | final original | final kept |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 1,919 | 1,919 | 1.000000 | 0 | 0 | 10 | 10 |
| 1 | 1,982 | 1,982 | 1.000000 | 14 | 14 | 14 | 14 |
| 2 | 3,718 | 2,720 | 0.731576 | 1 | 1 | 70 | 27 |
| 3 | 3,493 | 3,493 | 1.000000 | 0 | 0 | 23 | 23 |
| 4 | 4,005 | 4,005 | 1.000000 | 0 | 0 | 27 | 27 |
| 5 | 3,246 | 3,228 | 0.994455 | 13 | 13 | 0 | 0 |
| 6 | 2,020 | 2,020 | 1.000000 | 13 | 13 | 0 | 0 |
| 7 | 4,266 | 3,331 | 0.780825 | 0 | 0 | 24 | 24 |
| 8 | 6,647 | 2,844 | 0.427862 | 0 | 0 | 35 | 35 |
| 9 | 6,932 | 2,965 | 0.427726 | 0 | 0 | 60 | 60 |
| 10 | 7,450 | 2,961 | 0.397450 | 0 | 0 | 67 | 67 |
| 11 | 8,011 | 2,073 | 0.258769 | 0 | 0 | 109 | 28 |

Rejection diagnosis:

- weak single-root crossings: `20,033`
- weak multi-root crossings: `64`
- multi-root crossings above slope threshold: `51`

This means the gate is mostly rejecting weakly-conditioned roots, not mostly rejecting root ambiguity.

Important finding:

The late source `5` and `6` crossing dropouts remain after gating. The gate does not explain or fix them. They are either a real consequence of the declared residual in this cluster scene, or an extraction-radius/adaptive-sampling failure that needs a targeted run.

## Cluster Seam Lineage Pass

Lineage source:

`/Users/danski2017/Desktop/Atlas_Solver_Project/codex_context/dynamic_evolution/skeleton_smoke_20260526/compute_cluster_seam_lineage.py`

Lineage output:

`/Users/danski2017/Desktop/Atlas_Solver_Project/codex_context/dynamic_evolution/skeleton_smoke_20260526/cluster12_robust75_c20_scale2_20260526/root_quality_gate/seam_lineage`

Scope:

`root_quality_gated`

Pair count:

`66`

Lineage summary:

- retained lineage candidates: `1`
- intermittent lineage candidates: `10`

Top gated seam relationships:

| pair | active steps | stable transitions | weighted persistence | mean count | max count | status |
|---|---:|---:|---:|---:|---:|---|
| `9-10` | 72 | 15 | 0.551 | 3.97 | 8 | retained |
| `5-6` | 62 | 1 | 0.528 | 12.23 | 36 | intermittent |
| `7-8` | 75 | 4 | 0.526 | 7.88 | 19 | intermittent |
| `3-4` | 75 | 5 | 0.524 | 12.72 | 25 | intermittent |
| `1-2` | 24 | 0 | 0.505 | 7.32 | 30 | intermittent |
| `2-10` | 31 | 6 | 0.500 | 1.09 | 8 | intermittent |
| `0-2` | 27 | 3 | 0.500 | 3.01 | 20 | intermittent |
| `0-1` | 60 | 1 | 0.493 | 15.68 | 28 | intermittent |
| `4-5` | 26 | 5 | 0.463 | 0.56 | 3 | intermittent |
| `2-9` | 29 | 3 | 0.457 | 1.25 | 8 | intermittent |
| `2-11` | 18 | 2 | 0.235 | 0.45 | 4 | intermittent |

Interpretation:

The gated foam has frame-local structure, but only one pair currently meets the retained-lineage rule. This is not enough to call the seam network certified. It is enough to identify where the next diagnostic should focus: improve or explain extraction stability before using seam/node patterns as physical evidence.

## Post-Processing Defect Fixed

During the lineage pass, a 12-source bookkeeping defect was found in the root-quality gate. Seam pair keys were sorted as strings rather than source numbers, allowing labels such as `10-9`.

Fix:

`find_seams` now sorts source ids with `key=int`.

Effect:

The underlying crossing and seam totals did not materially change. The defect affected pair naming/canonicalization, not the extracted crossing positions.

## Certification Status After Gate And Lineage

This run is still not 1PN certified.

Current status:

- robust 12-source diagnostic run: passed
- self-cleaned R5 GCS extraction: active
- root-quality post-processing: complete
- cluster seam lineage audit: complete
- 1PN shadow lane: present
- 1PN/EIH acceleration evolution: disabled in this run
- seam network: not certified
- late crossing dropouts: unresolved

Revised next move:

Run a targeted dropout diagnostic for sources `5` and `6`, preferably without changing the physics first. The first pass should vary extraction radius/headroom and ray density around the same initial data so we can tell whether the loss is sampling/extraction geometry or a genuine consequence of the current residual definition.
