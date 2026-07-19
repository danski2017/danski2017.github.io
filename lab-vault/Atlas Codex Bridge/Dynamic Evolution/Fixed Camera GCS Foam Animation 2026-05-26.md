---
type: dynamic_visual_audit
status: completed
created: 2026-05-26
topics:
  - atlas-dynamics
  - gcs-foam
  - visualization
  - 1pn
---

# Fixed Camera GCS Foam Animation 2026-05-26

## Purpose

Render the living GCS foam with a fixed camera so the sources move through the field while the viewer can audit foam change without camera rotation.

This supersedes the rotating diagnostic style for visual inspection.

## Source Run

`/Users/danski2017/Desktop/Atlas_Solver_Project/codex_context/dynamic_evolution/skeleton_smoke_20260526/skeleton_long_smoke_20260526_12step`

## Renderer

`/Users/danski2017/Desktop/Atlas_Solver_Project/codex_context/dynamic_evolution/skeleton_smoke_20260526/render_fixed_gcs_foam_animation.py`

## Outputs

GIF:

`/Users/danski2017/Desktop/Atlas_Solver_Project/codex_context/dynamic_evolution/skeleton_smoke_20260526/skeleton_long_smoke_20260526_12step/figures/atlas_fixed_camera_gcs_foam_animation.gif`

Final frame:

`/Users/danski2017/Desktop/Atlas_Solver_Project/codex_context/dynamic_evolution/skeleton_smoke_20260526/skeleton_long_smoke_20260526_12step/figures/atlas_fixed_camera_gcs_foam_final_frame.png`

Summary:

`/Users/danski2017/Desktop/Atlas_Solver_Project/codex_context/dynamic_evolution/skeleton_smoke_20260526/skeleton_long_smoke_20260526_12step/figures/atlas_fixed_camera_gcs_foam_animation_summary.json`

## How To Read

- colored source markers move through update steps
- colored point clouds are current-step GCS crossing foam
- black points are seams
- purple stars are nodes, when present
- colored arrows are context-excluded 1PN correction vectors magnified by `350x`

The camera is fixed at elevation `20` and azimuth `-55`.

## Read

This render makes the foam itself the object of inspection. It shows the GCS crossing clouds changing with the update step while the source tracks accumulate through the same fixed viewpoint.

The 1PN vectors are retained as a secondary audit layer, but the main visual claim is the source/foam relation.

## Claim Ceiling

Visual audit only.

The foam is computed from the existing R5-native skeleton traces, but the source evolution is still Newtonian-primary with 1PN shadow diagnostics. This is not yet an Atlas-native certified dynamics law.
