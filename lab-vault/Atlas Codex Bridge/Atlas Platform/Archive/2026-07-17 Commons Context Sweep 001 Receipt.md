---
type: platform_change_receipt
status: archived
created: 2026-07-17
tags: [atlas-platform, commons, parent-context, scene-passport, receipt]
---

# 2026-07-17 Receipt — Commons Context Sweep 001 (parent-context robustness)

## Change
- New script `scripts/et_tov3_scout/commons_context_sweep_001.mjs` (additive;
  no viewer edits, no dataset overwrites). Evidence packet at
  `analysis/et_tov3_scout/COMMONS_CONTEXT_SWEEP_001/commons_context_sweep_001_20260717.json`.
- First EXPLICIT parent-context declaration for the LSN-66 scene (Nesting
  Appendix-B passport: the roster's implicit Pi = 0 is replaced by swept
  synthetic exterior shells — 24 seeded context-only sources at r 25-35,
  never ablated; attribution stays over the 66 roster sources). Amplitudes
  ||E_shell(centroid)|| in {1e-16, 5e-16, 2e-15, 1e-14} x 3 seeded
  orientations = 12 realizations + Pi=0 baseline (reproduces Survey 001:
  36 troughs / 9 disputed, exact cross-check).

## Question answered (founder, 2026-07-17)
Was the anomaly at the model's edge, and do the islands evaporate when
parent context is added?

## Results — a clean dose-response
- **amp 1e-16** (below the deepest floor 4.4e-16): 7-8/9 disputed troughs
  survive; lalande recurrence fully intact (all three carriers, controls
  clean).
- **amp 5e-16** (~ deepest floor): 6-7/9 survive. The lalande trough itself
  survives at its own floor amplitude, but the CARRIER SET is re-dealt:
  lalande_21185 drops out while stein_2051_b persists in every orientation.
- **amp 2e-15** (mid floors): individual survival collapses to 2-4/9, yet
  total troughs grow (50-57) and 3-10 disputed troughs still exist —
  relocated, not absent.
- **amp 1e-14** (above every floor): baseline individuals essentially all
  dead (0-2/9); ||E|| minima balloon (75-83, imposed by the shell) but only
  0-3 are disputed — the coincidence of cancellation troughs with
  attribution disputedness is DESTROYED once the exterior field dominates.
- **Per-trough ordering matches interiority, not entropy**: the deep-interior
  troughs (r 2.6-5.1 from centroid, most/all sources beyond them) are the
  most robust (survive into 2e-15, one even at 1e-14); the edge-suspect
  trough at r=10.6 (2 sources beyond) is the most fragile, dying in 2 of 3
  orientations even at 1e-16; one southern trough (r=8.3) dies everywhere.

## Verdict
- The lalande trough was NOT at the model's edge (r 8.57, 21 sources
  beyond, neighbors on all sides), and it survives exterior amplitudes up
  to roughly its own floor depth — but it IS a balance object with a
  measurable evaporation threshold E_ext ~ floor.
- Founder intuition CONFIRMED AT CLASS LEVEL, REFINED AT OBJECT LEVEL:
  individual islands are coordinates-of-the-arrangement (they migrate,
  evaporate, and re-deal their carriers under context); the commons-trough
  class persists through mid amplitudes. At exterior dominance even the
  class signature (trough-disputedness coincidence) breaks — so commons
  claims must carry a declared Lambda_Pi ceiling.
- Edge instinct validated: interiority is the robustness axis. Commons
  Survey 002 should weight interior troughs and declare the parent-context
  amplitude below which each claim holds.

## Validation
node --check pass; 2.1 s total on the Mac mini (compute-safety compliant);
Pi=0 baseline reproduces COMMONS_SURVEY_001 exactly (36/9); seeds and
amplitudes declared in the packet for exact reproduction.

## Boundary
Observed. Synthetic parent realizations on the initial-slice roster family;
NOT a measurement of the real exterior galaxy (the true Lambda_Pi is
undeclared and unknown at this rung). Vocabulary candidate, not decision.

## Rollback
Delete `scripts/et_tov3_scout/commons_context_sweep_001.mjs` and
`analysis/et_tov3_scout/COMMONS_CONTEXT_SWEEP_001/` (founder permission
required for deletions); no other file was touched.
