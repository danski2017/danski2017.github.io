---
type: dynamic_quality_gate
status: active
created: 2026-05-26
topics:
  - atlas-dynamics
  - gfro
  - root-quality
  - seams
---

# Root Quality Gate 2026-05-26

## Purpose

Use GFRO root metadata as a post-processing quality gate before seam lineage.

This is intentionally post-processing first. It tests whether weak or ambiguous roots affect seams before any root-quality threshold is promoted into the compute path.

## Gate Script

`/Users/danski2017/Desktop/Atlas_Solver_Project/codex_context/dynamic_evolution/skeleton_smoke_20260526/apply_root_quality_gate.py`

## Default Gate

- minimum absolute residual slope: `0.005`
- multi-root rays allowed: `false`
- seam threshold for recomputed gated seams: `0.6`

## Verification Run

Input run:

`skeleton_gfro_rootmeta_1step_20260526`

Output:

`/Users/danski2017/Desktop/Atlas_Solver_Project/codex_context/dynamic_evolution/skeleton_smoke_20260526/skeleton_gfro_rootmeta_1step_20260526/root_quality_gate`

Summary:

| metric | value |
|---|---:|
| original crossings | `552` |
| kept crossings | `428` |
| rejected crossings | `124` |
| original seams | `14` |
| gated seams | `14` |

Per source:

| source | original | kept |
|---|---:|---:|
| Heavy | `26` | `26` |
| Medium | `77` | `77` |
| Light | `170` | `147` |
| Dwarf | `279` | `178` |

## Read

The first root-quality gate rejected weak-slope crossings primarily from Light and Dwarf, but the one-step seam count remained unchanged.

This means root quality is affecting the crossing cloud, but we do not yet know whether it changes persistent seam/node lineage across time.

## Important Limitation

The existing source-fixed 12-step run cannot be root-quality gated because it was generated before root metadata fields were added.

Do not infer root-quality lineage from that run.

## Claim Ceiling

Root-quality gating is active as a diagnostic tool, not doctrine.

The threshold `0.005` is a starting audit threshold only.

## Next Move

Run fresh source-fixed normalized seam sweeps with root metadata enabled, then apply the root-quality gate before seam lineage.
