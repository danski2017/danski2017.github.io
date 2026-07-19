---
type: platform_change_receipt
status: archived
created: 2026-07-15
tags:
  - atlas-platform
  - phase-2
  - bake-pipeline
  - receipt
---

# 2026-07-15 Phase 2 Freeze-In-Time Receipt — BL Foam Bake Pipeline

Executes Phase 2 of [[../07 One-Model Redesign Blueprint]] (founder directive:
all model arrangements render once, then are frozen; no compute waits while
driving controls).

## Ownership Boundary

- Owning lane: BL Foam (bake path inside the existing `BL` module)
- New pipeline script: `scripts/et_tov3_scout/bake_bl_foam.mjs` (Node, no deps)
- New dataset: `pinch_lab_viewer/datasets/BL_FOAM_BAKED_001/`
  (manifest.json + 144 .f32 payloads, 5.1 MB total; roster JSON included)
- Files changed: `index.html` (baked-load path + "use frozen bake" checkbox),
  new script, new dataset directory
- Existing lanes protected: untouched; live BL compute retained as fallback
- Rollback: restore `backups/atlas_platform/index_pre_phase2_20260715.html`;
  dataset and script are additive and inert if unused

## Before

- `index.html` SHA-256:
  `841fdf610ec5e4fc94776bf4ece3fe803866fea64da0d66f187a88c777761e44`
- Disk checked: 73 GiB free; payload 5.1 MB

## Change

- Bake pipeline ports the certified kernels to Node and precomputes ALL
  arrangements at the certified march with full probe rosters (no cap):
  familyS 8 configs x {A,B} x {TF,RAW}; gaia66 10 configs x {A,B} x {TF,RAW}.
  Runtime: 8 s on the Mac mini (bounded, single core, <100 MB).
- Payload format: manifest (schema `atlas-bl-foam-baked/1`, provenance, claim
  boundary, march params, roster SHA-256, per-config counts) + little-endian
  float32 position triples + outermost-crossing arrays per probe source
  (feeds the d_AB disagreement ledger without recomputation).
- Viewer: "use frozen bake" checkbox (default ON) in Compute Budget; baked
  fetch first, live compute fallback (fast/certified + cap controls unchanged).
  Stats line shows "frozen bake — certified march, all sources" in green.

## Validation

- Bake-vs-live cross-check (exact): familyS c0 A_TF 1934 / B_TF 1939;
  gaia66 c0 A_TF 6805 — identical to live-certified runs recorded earlier
  in [[2026-07-15 BL Parity Foam Lane Receipt]].
- Physics sanity from frozen payload: Gaia AB ledger d_AB = 0.00% (weak-field
  superposition-lossless, as filed 2026-07-13); familyS AB ledger identical to
  the filed table (ember 7.84%/+4.6e-1, ash 2.24%, jasper 3.75%, flint 7.21%).
- Load times: familyS lane entry 0.35 s; gaia66 AB 0.30 s; 9 config swaps in
  ~1 s total — certified march, all 66 sources, no cap.
- Live fallback verified (bake unchecked -> fast-survey path).
- `node --check` pass; all four lanes regression-checked clean.

## Scientific Boundary

Frozen payloads are cached diagnostics of the same declared analytic
substrates — claim ceilings unchanged from the BL lane receipt. The manifest
carries the claim boundary and roster hash; re-bake required after any kernel
or roster change (drift risk between viewer kernels and bake script is
documented in both files' headers).

## After

- `index.html` SHA-256: recorded in repo lab log with this receipt.
- Re-bake command: `node scripts/et_tov3_scout/bake_bl_foam.mjs`
