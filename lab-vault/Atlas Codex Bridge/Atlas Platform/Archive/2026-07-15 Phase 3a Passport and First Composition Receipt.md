---
type: platform_change_receipt
status: archived
created: 2026-07-15
tags:
  - atlas-platform
  - phase-3
  - passport
  - composition
  - receipt
---

# 2026-07-15 Phase 3a Receipt — Passport Ribbon + First Cross-Substrate Composition

First slice of Phase 3 of [[../07 One-Model Redesign Blueprint]]
(provenance-distinct, freely composable layers on one model).

## Ownership Boundary

- Files changed: `index.html` only
- Backup / rollback: `backups/atlas_platform/index_pre_phase3a_20260715.html`
- Existing lanes protected: all regression paths intact; overlay is a new
  additive layer, checkbox off by default

## Registration Science (prerequisite)

The Atlas Native Gaia parent roster (52 systems) and the BL LSN-66 roster
occupy the SAME coordinate frame at different normalizations. Least-squares
uniform scale over 7 matched stars (proxima, barnard, sirius, procyon, alpha,
luhman, wise 0855): **s = 6.625997, worst residual 0.0 grid units** — exact
registration, not an approximation. Declared in-code as `BL_REG_SCALE` with
derivation note.

## Change

1. **Passport ribbon** (`#passport`, under the header badges): persistent
   declaration of what is on screen — substrate + claim ceiling, witness,
   chart/norm, grid or march, and any advisory composition. Wired into all
   four lanes (Atlas Native per-update; BL per-control-change; Recovery and
   Imported on lane entry).
2. **First cross-substrate composition**: "BL parity foam overlay" checkbox
   in the Atlas Native Layers list (visible only when the Gaia parent dataset
   is selected). Loads the frozen gaia66 FULL-SCENE DEN A / TF foam
   (6,805 crossings, certified march) from `BL_FOAM_BAKED_001`, scales by
   `BL_REG_SCALE`, and renders it in the atlas world over the eigen scene.
   Badged `analytic · registered s=6.626`; the passport ribbon appends
   "+ BL foam overlay — analytic substrate, registered s=6.626, advisory
   composition" in amber while active. Overlay auto-clears and unchecks on
   dataset switch (scale is Gaia-parent-specific).

## Validation

- `node --check` pass.
- Overlay on: parity foam shells render around the parent-scene sources with
  the removed target visible (visual QA screenshots in-session, both states).
- Toggle off: scene returns to native-only; overlay object disposed
  (`__PINCH_LAB_STATE.blOverlayCount` 6805 -> 0).
- Overlay label hidden on StageB/B03 datasets; auto-clear on dataset switch.
- Passport verified in Atlas (with and without composition), BL, Recovery,
  Imported lanes.

## Scientific Boundary

The composition juxtaposes two DECLARED substrates in one registered frame:
a custom constrained static eigen-scene and an analytic BL parity foam. It is
an observation surface for candidate correspondences (e.g. foam shells vs
eigen-footprint morphology) — advisory only; no claim that the substrates
agree physically. Any observed correspondence must be written up and promoted
through the normal ladder before interpretation.

## After

- index.html SHA-256: recorded in repo lab log with this receipt.
