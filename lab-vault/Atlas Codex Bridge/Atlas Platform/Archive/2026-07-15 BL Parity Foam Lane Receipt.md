---
type: platform_change_receipt
status: archived
created: 2026-07-15
tags:
  - atlas-platform
  - bl-foam
  - receipt
---

# 2026-07-15 Atlas Platform Change Receipt — BL Parity Foam Lane

## Purpose

Integrate the BL-method innovations (2026-07-13 Claude-wing session) into Atlas
Platform as a permanent lane: analytic Brill–Lindquist / conformal-ball
substrates with Frobenius-norm E_ij parity ablation, dual-denominator
comparison contract, and the interior parity shell laboratory. Founder decision
2026-07-15: the foam diagnostic is reconsidered; older "no foam" manifest
language reflected wing skepticism, not lab doctrine.

## Ownership Boundary

- Owning lane: **BL Foam** (`blFoamPanel`, `blWorld` group, `BL` closure module)
- Inputs: none — scenes are analytic, computed live in-browser (Family S 5-ball
  roster, embedded Gaia LSN-66 roster from the certified v3 instrument payload
  with mu = m/2 puncture convention, two-ball interior lab constants)
- Outputs: rendered rho=1 crossing clouds (DEN A gold / DEN B blue / boundary-
  event red), in-panel disagreement ledger and interior-shell statistics
- Files changed: `analysis/et_tov3_scout/pinch_lab_viewer/index.html` only
- Existing lanes explicitly protected: Atlas Native, Imported Tools, Recovery
  Lab — no control removed or altered; shared changes limited to: panel switch
  grid 3→4 columns, `setToolPanel` gaining a `bl` branch, `foamBadge` id on the
  previously static header badge, probe-click guard for non-atlas lanes
- Removal/rollback: delete `blFoamPanel` div, `blPanelBtn` button, `blWorld`
  line, `bl` branches in `setToolPanel`, and the `const BL=(()=>{...})()` block;
  or restore `backups/atlas_platform/index_pre_bl_lane_20260715.html`

## Before

- `index.html` SHA-256:
  `76979584a9ac3df0ba18afc196d49c53841f0b0add44d498dd3514168f0d7dcc`
- Backup: `backups/atlas_platform/index_pre_bl_lane_20260715.html`
- Dirty-worktree observations: pre-existing modifications to
  `analysis/et_tov3_robustness_001/robustness_matrix_cleanup_and_commit_20260605_225946.txt`
  and `logs/et_tov3_scout_lab_log.txt`; untracked `.claude/`, `Atlas Project
  Instructions.rtf`, `Atlas Solver Hub/` — none touched by this change.

## Change

- Fourth panel button **BL Foam**; panel with Scene / Configuration /
  Comparison Contract (DEN A, DEN B, A+B fork ledger; witness E_ij trace-free
  vs R3_ij raw) / Two-Ball Controls (D, mu_n sliders, chi readout) / Display /
  Disagreement Ledger sections, plus claim-boundary text.
- Kernels ported verbatim from the certified instruments: uniform-ball +
  puncture conformal accumulators, isolated closed-form E pasted context,
  factored base-minus-removed assembly with per-source Float32 caches,
  Fibonacci omni-radial log ray march, sign-change root bracketing with linear
  interpolation. Corrected norm-contract comment retained (no psi^-4
  cancellation claim — coordinate-chart ||·||_delta declared).
- Extraction is async-chunked with progress reporting and token cancellation;
  Gaia-66 full extraction ~75 s one-time, then cached per
  (scene, config, denominator, witness).
- Ledger rule: d_AB from matched outermost rho=1 crossing per ray; viewer
  displays all crossings (lab-note convention).
- Defensive additions born in QA: non-finite point filtering in `addCloud`,
  NaN-guarded bounding-sphere framing with canvas-derived aspect fallback
  (embedded-pane `innerWidth=0` quirk), interior-lab camera framing.

## Validation

- JavaScript syntax: `node --check` on extracted module — pass
- JSON/schema audit: no manifests changed; embedded roster parsed from the
  certified v3 payload programmatically (66 sources)
- Desktop browser QA: all four lanes exercised over HTTP (port 8792)
- Mobile browser QA: 375x812 — panel stacks correctly, 4-button switch fits
- WebGL nonblank check: pass after NaN-framing fix; render witness saved as
  `pinch_lab_viewer/bl_foam_lane_familyS_verify_20260715.jpg`
- Existing-lane regression: Atlas Native header/scene restore, Imported Tools
  (6 workflows), Recovery Lab (3 cases, matter+constraint view) — all pass
- Numerical audit: Family S A+B ledger vs 2026-07-13 lab note — signed biases
  match exactly (ember +4.6e-1, ash +5.3e-2, flint +2.7e-1); d_AB percentages
  within definition tolerance (7.84/2.24/3.75/7.21 vs 7.54/2.13/3.66/6.89).
  Interior shell vs v0.1 table — D=3: 0.145/0.165/0.104 vs 0.145/0.165/0.105;
  D=1.5: 0.331/0.596/0.233 with 25 boundary-event rays vs 0.330/0.599/0.234.

## Scientific Boundary

Demonstrates: the certified BL diagnostic instruments run inside Atlas Platform
with reproduced ledgers. Does NOT demonstrate: ET-fused GR behavior, physical
membranes, coordinate-independent invariants, or dynamical relevance. Scenes
are declared analytic substrates; the norm is the coordinate-chart Frobenius
witness under shared Euclidean chart identification; vocabulary remains
candidate, not decision.

## After

- `index.html` SHA-256 (at receipt time):
  `dd5948257d5d8d26ac4151c02c9b0b0f7ad19f162704ccb3da37faec20484a51`
- Screenshots: in-session desktop + mobile QA; render witness JPEG above
- Evolution Log entry: 2026-07-15 — BL Parity Foam Lane
- Repo lab-log entry: appended to `logs/et_tov3_scout_lab_log.txt`

## Known Follow-ups (owed)

- DEN B interior-shell comparison; smoothed-density (Gaussian) profile scene
  with gradient-lodging behavior; roster-perturbation sweep to complete the
  Reproduced rung; ||·||_gamma-ref norm variant; Gaia coincident-binary roster
  declaration; optional worker-thread offload if Gaia-66 build time matters.
