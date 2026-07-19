---
type: dynamic_source_fix
status: completed
created: 2026-05-26
topics:
  - atlas-dynamics
  - gcs-foam
  - r5
  - source-fix
---

# GCS Self-Contamination Source Fix 2026-05-26

## Purpose

Fix the Heavy halo defect at the source-code level.

The defect was isolated by ledger audit:
current R5 source-centered GCS extraction left the source's own self-A 1PN correction inside the context-side norm.

## Source File

`/Users/danski2017/Desktop/Atlas_Solver_Project/codex_context/dynamic_evolution/skeleton_smoke_20260526/atlas_skeleton_compute_local.py`

## Code Change

Added a named GCS residual mode:

`ATLAS_GCS_RESIDUAL_MODE`

Default:

`self_cleaned_r5`

Available modes:

- `self_cleaned_r5`
- `current_self_contaminated_r5`

The default branch removes source self-A from the context side:

`E_context_self_cleaned = E_1PN_full - E_self - delta_self_A`

The historical branch is retained explicitly as anomaly evidence:

`E_context_current = E_1PN_full - E_self`

## Ledger Changes

Radial traces now include:

- `gcs_residual_mode`
- `residual_r5_self_cleaned`
- `residual_r5_current_self_contaminated`

Crossing battery records now include:

- `gcs_residual_mode`
- `residual_r5_self_cleaned`
- `residual_r5_current_self_contaminated`
- `R5_E_context_selected`
- `R5_E_context_self_cleaned`
- `R5_E_context_current_self_contaminated`

Manifest now includes:

- `gcs_residual_mode`
- `gcs_residual_modes_available`
- `gcs_residual_default_policy`

## Verification Run

Run id:

`skeleton_sourcefix_selfclean_3step_20260526`

Output folder:

`/Users/danski2017/Desktop/Atlas_Solver_Project/codex_context/dynamic_evolution/skeleton_smoke_20260526/skeleton_sourcefix_selfclean_3step_20260526`

Size:

`30M`

Command:

`ATLAS_RUN_ID=skeleton_sourcefix_selfclean_3step_20260526 ATLAS_N_STEPS=3 ... atlas_skeleton_compute_local.py`

## Verification Results

Stepwise median GCS radii:

| step | Heavy | Medium | Light | Dwarf |
|---:|---:|---:|---:|---:|
| 0 | `7.427087` | `6.787816` | `5.915156` | `5.589470` |
| 1 | `8.184591` | `7.191422` | `6.203649` | `5.552387` |
| 2 | `8.232496` | `7.422268` | `6.230638` | `5.551518` |

Stepwise crossing counts:

| step | Heavy | Medium | Light | Dwarf |
|---:|---:|---:|---:|---:|
| 0 | `26` | `77` | `170` | `279` |
| 1 | `68` | `111` | `143` | `186` |
| 2 | `75` | `122` | `142` | `203` |

Rendered verification panel:

`/Users/danski2017/Desktop/Atlas_Solver_Project/codex_context/dynamic_evolution/skeleton_smoke_20260526/skeleton_sourcefix_selfclean_3step_20260526/figures/skeleton_smoke_steps_panel.png`

## Read

The Heavy compact halo is removed at the compute-source level.

The fixed source no longer relies on post-processing self-cleaned diagnostics. New runs default to the self-cleaned residual and ledger the historical self-contaminated residual as an anomaly lane.

## Claim Ceiling

This fixes the isolated self-contamination defect.

It does not certify the final lawful Atlas GCS residual. The extraction ladder still needs to compare self-cleaned, cross-retaining, and other candidate residual definitions.

## Next Move

Run a 12-step source-level self-cleaned smoke and compare against the previous long smoke:

- source radii
- crossing counts
- seam/node lineage
- EIH lane diagnostics
- fixed-camera foam render
