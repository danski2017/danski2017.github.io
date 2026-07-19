---
type: dynamic_ledger_audit
status: completed
created: 2026-05-26
topics:
  - atlas-dynamics
  - gcs-foam
  - r5
  - ledger-audit
  - defect-isolation
---

# GCS Self-Contamination Ledger Audit 2026-05-26

## Purpose

Audit why Heavy rendered as if nested inside a compact fuzzy halo.

Goal:
isolate whether the defect came from the renderer, ledger storage, radial crossing detection, tensor battery decomposition, or extraction residual definition.

## Audit Artifacts

Audit script:

`/Users/danski2017/Desktop/Atlas_Solver_Project/codex_context/dynamic_evolution/skeleton_smoke_20260526/audit_gcs_self_contamination.py`

Audit folder:

`/Users/danski2017/Desktop/Atlas_Solver_Project/codex_context/dynamic_evolution/skeleton_smoke_20260526/skeleton_long_smoke_20260526_12step/gcs_self_contamination_audit`

Files:

- `gcs_self_contamination_audit_summary.json`
- `step_crossing_radius_audit.csv`
- `battery_self_contamination_audit.csv`
- `radial_zero_crossing_audit.csv`

## Defect Boundary

Rendering:
not the primary cause. The renderer plotted the crossing clouds found in `step_data`.

Ledger storage:
not the primary cause. Reported `gcs_r` values match direct crossing-cloud radii.

Radial zero reconstruction:
not the primary cause. Reconstructed radial zero crossings match `step_data` crossing radii.

Tensor battery:
contains the evidence needed to isolate the defect.

Extraction residual:
primary defect. The current R5 residual leaves source self-A 1PN correction inside the context-side norm.

## Step 11 Evidence

`step_data` crossing radii:

| source | reported `gcs_r` | direct median radius | crossings |
|---|---:|---:|---:|
| Heavy | `1.276932` | `1.276932` | `250` |
| Medium | `0.663492` | `0.663492` | `250` |
| Light | `6.230284` | `6.230284` | `134` |
| Dwarf | `5.506110` | `5.506110` | `179` |

Radial zero reconstruction:

| source | radial zero median | radial zero count |
|---|---:|---:|
| Heavy | `1.276932` | `250` |
| Medium | `0.663492` | `250` |
| Light | `6.230270` | `134` |
| Dwarf | `5.506138` | `179` |

Battery decomposition at accepted current-R5 crossings:

| source | radius median | self-A mean | context-self mean | cross mean | self-A / (context + cross), median |
|---|---:|---:|---:|---:|---:|
| Heavy | `1.276932` | `11.060217` | `0.000781` | `0.668295` | `16.523522` |
| Medium | `0.663492` | `37.925785` | `0.002390` | `3.873003` | `9.785029` |
| Light | `6.230284` | `0.000955` | `0.005455` | `0.002788` | `0.112162` |
| Dwarf | `5.506110` | `0.000409` | `0.004146` | `0.002132` | `0.062126` |

## Interpretation

The Heavy halo was not a plotting illusion.

It was a faithful rendering of a compact crossing shell produced by the current R5 residual.

The current residual is:

`||E_self|| - ||E_1PN_full - E_self||`

That expression subtracts only the Newtonian self tidal tensor. It does not remove the source's own nonlinear self-A 1PN correction from the right-hand side.

Therefore the context side is not purely context.

For Heavy and Medium, the accepted compact crossings are dominated by self-A. Heavy's median self-A dominance ratio is `16.52`; Medium's is `9.79`.

For Light and Dwarf, self-A is small relative to context plus cross, so the defect is less visually catastrophic.

## Isolated Defect

Current R5 extraction conflates source self correction with context field when computing the GCS residual.

This is a residual-definition defect, not a render defect and not a ledger serialization defect.

## Claim Ceiling

Current R5 source-centered GCS extraction is quarantined as self-contaminated.

Self-cleaned R5 is a leading diagnostic candidate, but not yet certified doctrine.

## Next Move

Formalize the extraction ladder and make every branch explicit:

- current R5: anomaly lane
- linear R2: comparison lane
- self-cleaned R5: visual diagnostic candidate
- cross-retaining R5: next lawful candidate to test
- final Atlas GCS residual: not yet certified
