---
type: platform_change_receipt
status: archived
created: 2026-07-18
tags: [atlas-platform, commons, persistence, percolation-null, receipt]
---

# 2026-07-18 Receipt — Commons Persistence Sweep 001 (founder-authorized batch)

## Change
New script `commons_persistence_sweep_001.mjs`; packet
`analysis/et_tov3_scout/COMMONS_PERSISTENCE_SWEEP_001/`. Four parts,
confirm-or-kill.

## Results
- **A. Percolation null** (20 correlation-matched gaussian random
  fields, sigma fit 1.69 cells, occupancy-matched thresholds):
  at H>=0.85 (8.7% occ) and H>=0.88 (1.5% occ) the real backbone share
  (0.867 / 0.883) BEATS ALL 20 NULLS (null median 0.35, best 0.70).
  At H>=0.75 / 0.80 the single-component result is WITHIN NULL
  (percolation-trivial occupancies — honestly reported). The connected
  commons backbone is real at the high-entropy core; the permissive-
  level connectivity is not evidence.
- **B. Resolution (96^3)**: 40 troughs; 8/9 disputed survive with
  drifts <= 0.016 (pinned far below lattice resolution).
- **C. Roster perturbation** (FAMILYS grammar, 6 variants): survival
  8-9/9 in every variant.
- **D. H-level grid**: disputed count 13 / 9 / 2 at H >= 0.70/0.75/0.80
  (smooth, no cliff at the declared 0.75).
- **EVERY failure in B and C is the SAME trough**: idx 7 at
  (0.809, 1.481, -7.843) — the same member that evaporated first in
  Context Sweep 001. One consistently fragile member; the other eight
  are robust across resolution, perturbation, and (from the earlier
  sweep) sub-floor exterior context.

## Incident
First run stalled ~30 min at 98% CPU in the trough-refinement pattern
search on the mu_alternating variant (float-precision crawl). Killed,
fixed with an iteration cap + relative-improvement threshold; rerun
completed in 2.1 s. Fix is permanent in the script; node ceiling (1e6)
also enforced. Memory never exceeded ~140 MB.

## Promotion recommendation (founder adjudicates)
- The 8 robust disputed troughs + the H>=0.85 connected backbone:
  evidence now supports promotion Observed -> Reproduced within the
  declared roster family (persistence across resolution, perturbation,
  and percolation null; Lambda_Pi ceiling from Context Sweep 001
  attached).
- Trough idx 7: DEMOTE to "fragile candidate" (fails resolution and
  3/6 perturbations; died at 1e-16 exterior amplitude).
- Webbing/frontier at H < 0.85: connectivity claims NOT supported
  (within percolation null); keep as descriptive vocabulary only.

## Rollback
Delete script + packet (founder permission required); no other file
touched.
