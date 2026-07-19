---
type: platform_change_receipt
status: archived
created: 2026-07-15
tags:
  - atlas-platform
  - audit
  - phase-1
  - receipt
---

# 2026-07-15 Phase 0 Knob Audit + Phase 1 Standards Receipt

Executes the first two phases of [[../07 One-Model Redesign Blueprint]].

## Phase 0 — Knob Audit (no code changes)

Method: programmatic exercise of every control in the served viewer
(dispatched input/change events), JS-error capture, and WebGL pixel-diff
per layer toggle to detect visually inert controls.

**Verdict: no broken controls found.** The sprawl is a standards/defaults
problem, not a breakage problem.

| Area | Exercised | Result |
|---|---|---|
| View/layer/compare selects (11 modes) | all | ok, no errors |
| Probe sampling modes (5) | all | ok |
| Layer checkboxes (8) | all | ok — every layer renders (pixel-diff > 0, incl. Lumen) |
| Sliders (12) | min/restore sweep | ok |
| Wink + feature buttons (6) | all | ok |
| Dataset switching (StageB / Gaia parent / B03) | all 3 | ok, targets repopulate |
| Gaia parent targets | 3 sampled | ok |
| Recovery witnesses (7) / views (6) / realizations (4) / cases (3) | all | ok |
| Imported workflows (6) | all | command box populates |
| BL Foam scenes/denominators/witness/quality/cap | all (prior receipt) | ok |

Audit notes for later phases:
- Lumen Lattice renders but remains a declared placeholder — candidate for
  preset-folding under the earns-its-keep rule.
- Probe drawer only understands Atlas Native scalars; BL/Recovery points are
  not inspectable (Phase 3 item).
- No control was found to justify removal on functional grounds; candidates
  for folding are UX decisions, not bug fixes.

## Phase 1 — Standards Alignment (code changes)

- Backup: `backups/atlas_platform/index_pre_phase1_20260715.html`
- Pre-change SHA-256: `e230a63b068826c114183fae3d8f866e235f4bc80e0fb1632f54f5c87f5e95fe`

Changes:
1. **Omni-radial default sampling** (founder standard): `probeSampling`
   default `cartesian` → `omniRadial`, initial density 100 → 55 (matches the
   existing non-cartesian auto-drop convention). Rationale recorded in the
   blueprint: radial crossing points track structure; aligned cartesian grids
   cause visual feedback/aliasing.
2. **Scene cycling keys**: `[` / `]` cycle removal targets, `\` cycles the
   layer story (baseline → removed → delta → footprint). Active only in the
   Atlas Native lane, ignored while a form control has focus. Hint line added
   under the Target select.

Validation: `node --check` pass; live QA — omni-radial active on load,
`]`/`[` cycle B03→B04→B03 with full scene reload, `\` cycles layers; keys
verified inert in BL Foam lane; BL Foam, Recovery Lab, Imported Tools
regression-checked clean after edits.

Rollback: restore the backup file above (single file).

- Post-change SHA-256: recorded in repo lab log alongside this receipt.
