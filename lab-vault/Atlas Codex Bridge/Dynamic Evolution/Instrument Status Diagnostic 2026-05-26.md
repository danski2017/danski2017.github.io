---
type: dynamic_status_diagnostic
status: completed
created: 2026-05-26
topics:
  - atlas-dynamics
  - instrument-status
  - preflight
  - r5
  - gcs-foam
---

# Instrument Status Diagnostic 2026-05-26

## Purpose

Full preflight status check before proceeding to more robust simulations.

This report summarizes the current state of the dynamic skeleton instrument, the source-level R5 GCS fix, verification runs, visual diagnostics, ledger footprint, and remaining concerns.

## Current Claim Ceiling

The instrument is alive and useful for diagnostic iteration.

It is not certified as a lawful GR-compliant or Atlas-native evolution engine.

Primary source evolution remains Newtonian leapfrog. R4 and 1PN lanes remain comparison/shadow diagnostics. Self-cleaned R5 is now the default GCS visual/extraction diagnostic branch, but not final doctrine.

## Active Source

Compute source:

`/Users/danski2017/Desktop/Atlas_Solver_Project/codex_context/dynamic_evolution/skeleton_smoke_20260526/atlas_skeleton_compute_local.py`

Important source fix:

`ATLAS_GCS_RESIDUAL_MODE`

Default:

`self_cleaned_r5`

Anomaly reproduction mode:

`current_self_contaminated_r5`

## Code Sanity

Python compile check passed for:

- `atlas_skeleton_compute_local.py`
- `render_skeleton_smoke.py`
- `render_fixed_gcs_foam_animation.py`
- `render_self_cleaned_gcs_comparison.py`
- `audit_gcs_self_contamination.py`

## Ledger Footprint

Dynamic smoke workspace:

`/Users/danski2017/Desktop/Atlas_Solver_Project/codex_context/dynamic_evolution/skeleton_smoke_20260526`

Current size:

`931M`

Notable run sizes:

- legacy 12-step long smoke: `106M`
- source-fixed 12-step diagnostic: `120M`
- source-fixed 3-step verification: `32M`
- normalized/seam/c-toy six-step runs: usually `43M-49M` each

Concern:
ledger growth is already material. More robust simulations need explicit retention rules and run naming before scaling.

## Source-Fixed 12-Step Diagnostic

Run id:

`skeleton_sourcefix_selfclean_12step_20260526`

Output:

`/Users/danski2017/Desktop/Atlas_Solver_Project/codex_context/dynamic_evolution/skeleton_smoke_20260526/skeleton_sourcefix_selfclean_12step_20260526`

Mode:

`self_cleaned_r5`

Records:

- crossing battery: `6,396`
- radial scalar traces: `217,980`
- shadow lane records: `132`
- EIH acceleration records: `192`

Rendered fixed-camera foam:

`/Users/danski2017/Desktop/Atlas_Solver_Project/codex_context/dynamic_evolution/skeleton_smoke_20260526/skeleton_sourcefix_selfclean_12step_20260526/figures/atlas_fixed_camera_gcs_foam_animation.gif`

Final frame:

`/Users/danski2017/Desktop/Atlas_Solver_Project/codex_context/dynamic_evolution/skeleton_smoke_20260526/skeleton_sourcefix_selfclean_12step_20260526/figures/atlas_fixed_camera_gcs_foam_final_frame.png`

## Source-Fix Result

The Heavy halo defect is fixed at source level.

Legacy long smoke final radii:

| source | legacy current-R5 radius |
|---|---:|
| Heavy | `1.276932` |
| Medium | `0.663492` |
| Light | `6.230284` |
| Dwarf | `5.506110` |

Source-fixed final radii:

| source | self-cleaned R5 radius |
|---|---:|
| Heavy | `8.290353` |
| Medium | `7.405595` |
| Light | `6.351361` |
| Dwarf | `5.426911` |

The source-fixed battery at step 11 shows accepted crossings are near-zero for the selected residual:

| source | selected residual abs median | old contaminated residual median | self-A / context+cross median |
|---|---:|---:|---:|
| Heavy | `0.000169` | `-0.001799` | `0.591230` |
| Medium | `0.000127` | `-0.000852` | `0.266623` |
| Light | `0.0000685` | `-0.0002595` | `0.111557` |
| Dwarf | `0.000057` | `-0.000128` | `0.062649` |

Read:
the selected residual is coherent; the old contaminated residual remains ledgered and visibly different.

## Conservation And 1PN Diagnostics

L0 Newtonian baseline remains stable over 12 steps:

- total energy drift: `0.0`
- linear momentum max: `0.0`

L1 EIH correction fraction:

- first: `2.288547%`
- final: `2.311047%`

Mean acceleration difference versus EIH diagnostic in the source-fixed 12-step run:

| lane | mean delta |
|---|---:|
| Newtonian primary | `0.017185875` |
| R4 geodesic | `0.0193821875` |
| R5 1PN context geodesic | `0.002512` |
| R5 1PN legacy self-included | `5.294725125` |

Read:
the context-excluded 1PN shadow lane remains the best EIH comparison lane. This is unchanged by the GCS source fix because the motion lanes are separate from GCS extraction.

## Seam And Node Status

Important change:
self-cleaned GCS extraction strongly changes seam/node behavior.

Legacy 12-step long smoke:

- seam total: `47`
- node total: `0`

Source-fixed 12-step diagnostic:

- seam total: `278`
- node total: `16`

Source-fixed stepwise seams:

`[14, 25, 29, 27, 26, 20, 20, 26, 23, 19, 22, 27]`

Source-fixed stepwise nodes:

`[1, 2, 2, 3, 2, 2, 1, 1, 0, 1, 0, 1]`

Read:
the source fix exposes a much more active seam/node layer. This may be physically meaningful, but it may also be a threshold/sampling artifact. Do not interpret seams/nodes physically until lineage and scale-normalized criteria are rerun on the source-fixed branch.

## Current Strengths

- Root cause of Heavy halo isolated and fixed in source.
- Current R5 anomaly branch retained for reproducibility.
- Ledgers now explicitly record selected, self-cleaned, and contaminated residuals.
- Source-fixed 12-step smoke remains numerically stable at L0.
- Context-excluded 1PN lane remains best EIH comparison.
- Fixed-camera foam render is now the correct visual audit mode.
- Vault documentation is now strong enough for a new thread to orient.

## Current Concerns

1. GCS residual is improved, not certified.

Self-cleaned R5 fixes the isolated self-contamination defect, but the final lawful Atlas GCS residual still needs a formal extraction ladder, especially for cross-term handling.

2. Seams and nodes are not certified.

The source fix increased seams/nodes dramatically. This must be treated as a new diagnostic frontier, not success.

3. Absolute seam threshold is still weak.

The fixed 12-step run used `seam_mode = absolute` and `seam_threshold = 0.6`. Earlier sweeps showed strong threshold sensitivity. Source-fixed normalized seam sweeps are now required.

4. Motion is still Newtonian-primary.

The animation is not an Atlas-native evolution engine yet. Field-derived update rules are still future work.

5. Ledger size will explode.

The workspace is already `931M`. A robust simulation campaign should not start without retention controls, run manifest discipline, and a decision about which traces are Tier 1 versus temporary scratch.

6. Source fix has not yet been stress-tested across `c_toy`.

The source-level fix was verified at `c_toy = 5`. Prior c-toy sweeps were pre-fix. They need to be rerun or partially rerun under self-cleaned R5.

7. Render scripts are diagnostic, not product-grade.

They are adequate for lab audit, but not yet unified into a single instrument dashboard.

## Recommendation

Do not proceed directly to large robust simulations yet.

Proceed to a controlled source-fixed preflight ladder:

1. Formalize the dynamic GFRO extraction ladder.
2. Source-fixed normalized seam sweep at `c_toy = 5` using `k=1,2,4`.
3. Source-fixed `c_toy` mini-sweep at `c=5,8,12`, six steps each.
4. Source-fixed seam lineage pass on those runs.
5. Only then run a longer source-fixed simulation.

## Go/No-Go

Go for diagnostic sweeps.

No-go for robust production-scale simulation until source-fixed seam/node behavior is normalized and lineage-tested.

## GFRO Follow-Up

Completed:

`/Users/danski2017/Desktop/Atlas_Solver_Project/Relational_Labs/Relational_Labs/Atlas Codex Bridge/Dynamic Evolution/Dynamic GFRO Extraction Ladder 2026-05-26.md`

Read:

The instrument is now explicitly GFRO-structured in documentation: residual declaration, source/context/cross eligibility, zero-set extraction, relevance filters, and no-promotion rules are stated. Implementation still needs source-fixed normalized sweeps and cross-retaining candidate support.
