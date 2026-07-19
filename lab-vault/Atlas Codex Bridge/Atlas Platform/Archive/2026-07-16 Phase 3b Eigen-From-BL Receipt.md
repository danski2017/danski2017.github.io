---
type: platform_change_receipt
status: archived
created: 2026-07-16
tags:
  - atlas-platform
  - phase-3
  - eigen
  - base-model
  - receipt
---

# 2026-07-16 Phase 3b Receipt — Eigen Layers Baked From the BL Substrate

Executes the base-model unification consequence of blueprint directive 6:
native eigen-tools now read the SAME frozen BL solve that carries the foam.
One solve, many lenses.

## Ownership Boundary

- Files changed: `index.html` (eigen-layer section + loader/renderer inside
  the BL module), `scripts/et_tov3_scout/bake_bl_foam.mjs` (eigen bake stage)
- Dataset extended: `BL_FOAM_BAKED_001` now carries an eigen substrate per
  scene (positions + per-config `[lam0,lam1,lam2,e0x,e0y,e0z,froTF]`),
  total payload 88 MB
- Backup / rollback: `backups/atlas_platform/index_pre_phase3b_20260716.html`;
  eigen payloads additive and inert if unused

## Change

1. **Bake stage**: fixed omni-radial lattice from every source (24 dirs x 18
   log radii per source; founder sampling standard) — gaia66: 28,512 points,
   71 configs; familyS: 2,160 points, 8 configs. Per point, the trace-free
   E_ij is Jacobi eigen-decomposed; eigenvalues, principal eigenvector, and
   Frobenius norm stored. Bake total (foam + eigen): 44 s.
2. **Viewer**: "Base-Model Eigen Layers" section in the BL lane —
   orientation-delta cloud (angle between full-scene and ablated principal
   eigenvectors, viridis-colored) and principal eigenvector pairs (full blue,
   ablated amber). Both gated by a relative eigen-gap floor slider
   ((lam0-lam1)/||lam||), honoring the GFRO correction that eigenvector
   residuals jump at eigenvalue crossings.

## Validation

- `node --check` pass; no JS errors driving gaia66 "- sirius_a" with both
  eigen layers active at frozen certified quality.
- Visual QA: delta cloud and vector pairs render composited with the foam on
  the base model (desktop); mobile layout clean.
- Interior lab hides/clears eigen layers; existing lanes untouched.

## Scientific Boundary

Eigenstructure here is the analytic BL substrate's trace-free slice-curvature
witness, coordinate-chart convention, on a declared lattice — NOT the
ET-derived eigen datasets of Atlas Native, and not yet convention-checked
under a second norm (Phase 4). Eigenvectors remain interpretive witnesses;
the delta-angle display is gated by eigenvalue separation on BOTH scenes.

## After

- index.html SHA-256: recorded in repo lab log with this receipt.
- Re-bake: `node scripts/et_tov3_scout/bake_bl_foam.mjs` (~45 s).
