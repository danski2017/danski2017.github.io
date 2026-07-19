---
type: dynamic_parameter_sweep
status: completed
created: 2026-05-26
topics:
  - atlas-dynamics
  - seams
  - nodes
  - threshold-sensitivity
---

# Seam Threshold Sweep 2026-05-26

## Purpose

Test whether the high seam counts at larger `c_toy` are physical geometry or an artifact of the fixed seam proximity threshold.

## Sweep

Six-step runs at:

- `c_toy = 8`, seam thresholds `0.3`, `0.6`, `1.2`
- `c_toy = 12`, seam thresholds `0.3`, `0.6`, `1.2`

The `0.6` runs reuse the c-toy sweep outputs.

Summary artifacts:

`/Users/danski2017/Desktop/Atlas_Solver_Project/codex_context/dynamic_evolution/skeleton_smoke_20260526/seam_threshold_sweep_20260526/seam_threshold_sweep_summary.json`

`/Users/danski2017/Desktop/Atlas_Solver_Project/codex_context/dynamic_evolution/skeleton_smoke_20260526/seam_threshold_sweep_20260526/seam_threshold_sweep_summary.png`

Additional run sizes:

- c8 threshold 0.3: `48M`
- c8 threshold 1.2: `48M`
- c12 threshold 0.3: `43M`
- c12 threshold 1.2: `43M`

## Results

Seam totals across six steps:

| c_toy | threshold 0.3 | threshold 0.6 | threshold 1.2 |
|---:|---:|---:|---:|
| 8 | `18` | `141` | `374` |
| 12 | `59` | `380` | `785` |

Node totals across six steps:

| c_toy | threshold 0.3 | threshold 0.6 | threshold 1.2 |
|---:|---:|---:|---:|
| 8 | `0` | `0` | `9` |
| 12 | `0` | `2` | `36` |

Stepwise seams:

- c8, threshold 0.3: `[3, 3, 2, 2, 5, 3]`
- c8, threshold 0.6: `[41, 22, 23, 16, 22, 17]`
- c8, threshold 1.2: `[75, 55, 64, 64, 60, 56]`
- c12, threshold 0.3: `[7, 14, 11, 13, 8, 6]`
- c12, threshold 0.6: `[51, 73, 65, 68, 67, 56]`
- c12, threshold 1.2: `[80, 135, 144, 141, 146, 139]`

## Read

The seam/node layer is strongly threshold-sensitive at weak PN settings.

This means the current seam/node extraction should not be interpreted physically yet. The seam rise at larger `c_toy` is at least partly an extraction-threshold effect.

This does not weaken the crossing battery, Tier 1 radial trace, EIH comparison, or context-excluded 1PN result. It only limits claims about seams/nodes.

## Claim Ceiling

Seams and nodes are live diagnostics, not certified physical structures.

The current threshold rule is useful for visual inspection, but not yet a lawful, scale-normalized extraction rule.

## Next Move

Replace fixed absolute seam threshold with a scale-normalized criterion tied to local crossing-shell spacing, source GCS radius, or nearest-neighbor density.

## Follow-Up

Completed:

`/Users/danski2017/Desktop/Atlas_Solver_Project/Relational_Labs/Relational_Labs/Atlas Codex Bridge/Dynamic Evolution/Normalized Seam Sweep 2026-05-26.md`

Read:

The normalized rule is a better comparison branch than absolute distance, but it does not certify seams. A persistence/lineage filter is now the higher-value path.
