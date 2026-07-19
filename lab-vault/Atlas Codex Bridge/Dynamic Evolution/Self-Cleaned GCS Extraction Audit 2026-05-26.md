---
type: dynamic_extraction_audit
status: completed
created: 2026-05-26
topics:
  - atlas-dynamics
  - gcs-foam
  - r5
  - self-contamination
---

# Self-Cleaned GCS Extraction Audit 2026-05-26

## Purpose

Audit the visual anomaly where Heavy appears nested inside a compact fuzzy GCS halo.

The user flagged this as physically suspicious because Heavy is the largest source and should not naively read as nested inside a small local shell.

## Finding

The concern is valid.

The current R5 extraction residual is:

`||E_self|| - ||E_1PN_full - E_self||`

This subtracts only the Newtonian self tidal tensor from the full 1PN tensor.

Because `E_1PN_full` still contains the source's nonlinear self-A 1PN correction, the current context side is contaminated by the source's own 1PN self correction.

For Heavy, this is large enough to collapse the apparent crossing shell inward.

## Diagnostic Branch

Added a comparison-only branch:

`self_cleaned_r5`

Residual:

`||E_self|| - ||E_1PN_full - E_self - delta_self_A||`

This removes the source's own self-A correction from the context side before comparing norms.

This branch is not doctrine. It is an extraction-law audit.

## Artifacts

Compute script:

`/Users/danski2017/Desktop/Atlas_Solver_Project/codex_context/dynamic_evolution/skeleton_smoke_20260526/compute_self_cleaned_gcs_diagnostic.py`

Render script:

`/Users/danski2017/Desktop/Atlas_Solver_Project/codex_context/dynamic_evolution/skeleton_smoke_20260526/render_self_cleaned_gcs_comparison.py`

Diagnostic folder:

`/Users/danski2017/Desktop/Atlas_Solver_Project/codex_context/dynamic_evolution/skeleton_smoke_20260526/skeleton_long_smoke_20260526_12step/self_cleaned_gcs_diagnostic`

Size:

`2.9M`

GIF:

`/Users/danski2017/Desktop/Atlas_Solver_Project/codex_context/dynamic_evolution/skeleton_smoke_20260526/skeleton_long_smoke_20260526_12step/figures/atlas_current_vs_self_cleaned_gcs_animation.gif`

Final frame:

`/Users/danski2017/Desktop/Atlas_Solver_Project/codex_context/dynamic_evolution/skeleton_smoke_20260526/skeleton_long_smoke_20260526_12step/figures/atlas_current_vs_self_cleaned_gcs_final_frame.png`

Summary:

`/Users/danski2017/Desktop/Atlas_Solver_Project/codex_context/dynamic_evolution/skeleton_smoke_20260526/skeleton_long_smoke_20260526_12step/figures/atlas_current_vs_self_cleaned_gcs_summary.json`

Default self-cleaned visual diagnostic:

`/Users/danski2017/Desktop/Atlas_Solver_Project/codex_context/dynamic_evolution/skeleton_smoke_20260526/skeleton_long_smoke_20260526_12step/figures/atlas_self_cleaned_gcs_foam_animation.gif`

Default self-cleaned final frame:

`/Users/danski2017/Desktop/Atlas_Solver_Project/codex_context/dynamic_evolution/skeleton_smoke_20260526/skeleton_long_smoke_20260526_12step/figures/atlas_self_cleaned_gcs_foam_final_frame.png`

Default self-cleaned summary:

`/Users/danski2017/Desktop/Atlas_Solver_Project/codex_context/dynamic_evolution/skeleton_smoke_20260526/skeleton_long_smoke_20260526_12step/figures/atlas_self_cleaned_gcs_foam_summary.json`

## Step 11 Radius Comparison

| source | current R5 median radius | self-cleaned R5 median radius | linear R2 median radius |
|---|---:|---:|---:|
| Heavy | `1.281980` | `8.179101` | `7.975625` |
| Medium | `0.670791` | `7.371803` | `7.193503` |
| Light | `0.297276` | `6.681037` | `6.560536` |
| Dwarf | `2.109001` | `5.655446` | `5.330615` |

## Read

The current R5 foam is self-contaminated for source-centered extraction.

The self-cleaned branch moves Heavy's diagnostic support outward and aligns closely with the linear R2 context-only comparison. This confirms that the compact Heavy halo is not a trustworthy physical GCS feature.

## Claim Ceiling

The self-cleaned branch is a diagnostic correction candidate, not certified doctrine.

The current R5 extraction should be treated as suspect for source-centered GCS surfaces until the self/context/cross decomposition is explicitly handled in the extraction residual.

## Render Default

Status:
self-cleaned R5 is now the preferred visual diagnostic branch for GCS foam renders.

Current R5 remains retained as an anomaly/comparison lane.

This is a render-default promotion only. It is not a doctrine promotion and not a certification of the final lawful Atlas GCS residual.

## Next Move

Promote self/context/cross-separated extraction residuals into a formal comparison ladder:

- current R5 residual
- linear R2 context-only residual
- self-cleaned R5 residual
- cross-retaining R5 residual
- candidate lawful Atlas GCS residual

Then decide which branch is eligible for rendering and which branch remains anomaly evidence.
