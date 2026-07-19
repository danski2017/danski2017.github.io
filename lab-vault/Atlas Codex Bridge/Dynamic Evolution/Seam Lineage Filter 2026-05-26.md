---
type: dynamic_diagnostic
status: completed
created: 2026-05-26
topics:
  - atlas-dynamics
  - seams
  - lineage
  - persistence
---

# Seam Lineage Filter 2026-05-26

## Purpose

Add a temporal lineage diagnostic on top of the normalized seam sweep.

This is a post-processing filter only. It does not change the compute engine, update rule, crossing battery, or seam extraction law.

## Rule Tested

For each source pair and neighboring update-step transition, count how many seams have a successor nearby in the next update step.

Retain a pair-level lineage candidate when:

- the source pair is active across the run
- multiple neighboring-step transitions survive
- mean transition persistence is high enough to separate recurring seam support from one-step contacts

This is a diagnostic gate, not a certified physical rule.

## Artifacts

Artifact folder:

`/Users/danski2017/Desktop/Atlas_Solver_Project/codex_context/dynamic_evolution/skeleton_smoke_20260526/seam_lineage_filter_20260526`

Size:

`112K`

Files:

- `seam_lineage_records.json`
- `seam_lineage_summary.json`
- `seam_lineage_summary.png`
- `seam_lineage_gate_summary.json`
- `seam_lineage_retention_matrix.csv`
- `seam_lineage_diagnostic_report.png`
- `seam_lineage_report.md`

Visual summary:

`/Users/danski2017/Desktop/Atlas_Solver_Project/codex_context/dynamic_evolution/skeleton_smoke_20260526/seam_lineage_filter_20260526/seam_lineage_summary.png`

Diagnostic report figure:

`/Users/danski2017/Desktop/Atlas_Solver_Project/codex_context/dynamic_evolution/skeleton_smoke_20260526/seam_lineage_filter_20260526/seam_lineage_diagnostic_report.png`

Reusable report generator:

`/Users/danski2017/Desktop/Atlas_Solver_Project/codex_context/dynamic_evolution/skeleton_smoke_20260526/render_seam_lineage_report.py`

## Runs Compared

- `skeleton_normseam_c8_k1_6step`
- `skeleton_normseam_c8_k2_6step`
- `skeleton_normseam_c12_k1_6step`
- `skeleton_normseam_c12_k2_6step`

## Retained Lineage Candidates

Gate summary:

- runs compared: `4`
- pair-run entries: `24`
- retained pair-run entries: `18`
- transition records: `120`

| run | pair | mean persistence | step counts |
|---|---:|---:|---|
| c8 k1 | 1-2 | `0.779` | `18/28/31/34/31/32` |
| c8 k1 | 1-3 | `0.841` | `10/20/24/22/23/24` |
| c8 k1 | 2-3 | `0.775` | `15/10/13/13/10/7` |
| c8 k2 | 1-2 | `0.910` | `25/38/43/44/44/42` |
| c8 k2 | 1-3 | `0.902` | `15/25/31/29/32/32` |
| c8 k2 | 2-3 | `1.000` | `30/22/25/25/23/14` |
| c12 k1 | 0-1 | `0.890` | `25/45/47/46/48/46` |
| c12 k1 | 0-2 | `0.830` | `9/23/29/29/29/28` |
| c12 k1 | 0-3 | `0.790` | `1/17/18/18/18/19` |
| c12 k1 | 1-2 | `0.811` | `19/27/29/32/29/32` |
| c12 k1 | 1-3 | `0.839` | `11/19/21/19/21/22` |
| c12 k1 | 2-3 | `0.821` | `14/9/10/9/11/5` |
| c12 k2 | 0-1 | `0.943` | `27/52/54/55/57/56` |
| c12 k2 | 0-2 | `0.893` | `13/32/37/37/37/38` |
| c12 k2 | 0-3 | `0.879` | `2/23/25/24/23/23` |
| c12 k2 | 1-2 | `0.974` | `26/38/44/43/46/41` |
| c12 k2 | 1-3 | `0.963` | `16/27/30/27/30/30` |
| c12 k2 | 2-3 | `1.000` | `29/22/19/21/22/18` |

## Read

At `c_toy = 8`, source-0 seams are transient in this six-step window. Pairs `1-2`, `1-3`, and `2-3` show persistent seam support under both tested normalized coefficients.

At `c_toy = 12`, all six source pairs show persistent seam support under both tested normalized coefficients.

This means the lineage filter is doing useful work: it separates one-step seam contacts from recurring pair-level geometry.

## Interpretation

The `c8` result suggests that some normalized seams are extraction noise or initial-condition contacts, especially for source-0 pairings.

The `c12` result is not automatically physical certification. It may indicate richer weak-PN geometry, denser crossing-cloud support, threshold densification, or a combination.

The lawful reading is:

lineage persistence is now a necessary diagnostic before physical interpretation of seams/nodes, but not yet a sufficient certification test.

## Claim Ceiling

Seams remain live diagnostics.

The lineage filter improves auditability and lowers false confidence, but it does not certify seam ontology.

## Next Move

Promote seam lineage into the diagnostic report as a gate, then test it against ray density, radial-shell density, and longer update windows.

## All-Coefficient Extension

Status:
completed as post-processing only.

Reusable compute script:

`/Users/danski2017/Desktop/Atlas_Solver_Project/codex_context/dynamic_evolution/skeleton_smoke_20260526/compute_seam_lineage_filter.py`

Expanded artifact folder:

`/Users/danski2017/Desktop/Atlas_Solver_Project/codex_context/dynamic_evolution/skeleton_smoke_20260526/seam_lineage_filter_20260526_allk`

Size:

`200K`

Runs compared:

- `skeleton_normseam_c8_k1_6step`
- `skeleton_normseam_c8_k2_6step`
- `skeleton_normseam_c8_k4_6step`
- `skeleton_normseam_c12_k1_6step`
- `skeleton_normseam_c12_k2_6step`
- `skeleton_normseam_c12_k4_6step`

Gate summary:

- pair-run entries: `36`
- retained pair-run entries: `25`
- transition records: `180`

Diagnostic report:

`/Users/danski2017/Desktop/Atlas_Solver_Project/codex_context/dynamic_evolution/skeleton_smoke_20260526/seam_lineage_filter_20260526_allk/seam_lineage_diagnostic_report.png`

Read:

At `c_toy = 8`, the all-coefficient pass continues to exclude source-0 pairings from the retained lineage set. Pairs `1-2` and `1-3` persist at all tested coefficients; pair `2-3` persists at `k=2` and `k=4`.

At `c_toy = 12`, retained support is broad. The `k=2` and `k=4` runs retain all six pairs; the `k=1` run retains five of six under the stricter reusable threshold rule.

Interpretation:

The coefficient extension supports the earlier read: source-0 seams at `c_toy = 8` are likely transient/extraction contacts in this window, while `c_toy = 12` produces broad recurring pair support. This is still a diagnostic gate, not physical certification.

Next refinement:

Run lineage against either longer normalized windows or sampling-density variants before assigning ontology to the retained seams.
