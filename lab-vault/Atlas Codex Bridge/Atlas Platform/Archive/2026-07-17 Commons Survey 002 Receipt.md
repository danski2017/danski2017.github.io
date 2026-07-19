---
type: platform_change_receipt
status: archived
created: 2026-07-17
tags: [atlas-platform, commons, banded-survey, parity-proximity, receipt]
---

# 2026-07-17 Receipt — Commons Survey 002 (banded parity-proximity atlas)

## Change
New script `scripts/et_tov3_scout/commons_survey_002.mjs` (additive; no
viewer edits, no dataset overwrites). Packets (one per declared EPS rung):
`analysis/et_tov3_scout/COMMONS_SURVEY_002/commons_survey_002_eps{0.05,0.1,0.2,0.3}_k3_20260717.json`.

## Design
Inverts Survey 001's primitive: instead of finding ||E|| troughs and asking
whether parity visits them, compute near-parity EVERYWHERE on the declared
48^3 volume lattice and stratify by ||E|| decile band. Per node: all 66
Psi_a (DEN-A), nearC = #{a : |Psi_a| < EPS}, min|Psi_a|, entropy. Commons
candidate = nearC >= 3 outside a 1.0 guard radius of every source
(excludes each source's own primary shell). Candidates clustered
(26-connectivity); every cluster interrogated at centroid; largest novel
clusters get a bounded emission crawl of the best-aligned source's
Psi_a = 0 set, detachment measured against that source's baked main-cell
median radius (criterion: closest approach > 2 x medR).

## Results
- EPS ladder (0.05 / 0.1 / 0.2 / 0.3): flagged nodes 5 / 33 / 264 / 1365;
  clusters 3 / 17 / 55 / 38 (merging at 0.3); novel-beyond-Survey-001
  clusters 1 / 4 / 24 / 26. The strict rung is nearly empty — triple
  near-parity coincidence is thin at dx ~ 0.485 — occupancy grows smoothly
  with EPS (no cliff), so the vocabulary is stable under the sweep.
- **Band occupancy peaks at MID-TO-HIGH amplitude, not in the cancellation
  band**: at EPS 0.3, deciles b5-b8 carry 1.9-2.7% near-parity occupancy
  vs 0.5% in b0. Most clusters sit in bands 5-8 at every EPS rung. The
  unmapped bands are genuinely occupied — Survey 001's trough census saw
  only the b0 tail of the commons.
- **But every emission crawl (19 across the ladder) came back CONNECTED**:
  closest approach to the carrier source always < 2 x its main-cell median
  radius. No new detached island was found in the mid bands at this
  resolution and EPS range.

## Verdict — a two-phase commons
1. **Trough islands** (cancellation band b0): detached re-emergence
   components, balance objects with a Lambda_Pi ceiling (Survey 001 +
   Context Sweep 001).
2. **Parity webbing** (mid-to-high bands b5-b8): extended sheets where the
   outer skirts of several sources' PRIMARY parity cells interleave —
   multi-source near-parity coincidence that stays connected to the cells.
   This is the structure behind the founder's "source parity always closes
   against a neighbor": in the mid bands it closes AS the weave, not as
   islands.
The finger-trap grip (Density Probe 001) and the webbing are consistent:
the weave IS the interleaved skirts; troughs are its knots' shadows in the
cancellation band.

## Validation
node --check pass; ~1 s per rung on the Mac mini; EPS=0.05 rung archived
alongside the ladder; detachment criterion and all thresholds declared in
each packet.

## Boundary
Observed. Detachment inference is proximity-based (crawl patch within
radius cap 3.0; connection inferred from closest approach, not from a
walked path); a walked-path connectivity check is owed if webbing is
promoted. Persistence sweeps owed: lattice resolution (thin-sheet
undersampling is the known risk at dx 0.485), EPS/KMIN grid, roster
perturbation, Lambda_Pi ceiling. Vocabulary candidate, not decision.

## Rollback
Delete `scripts/et_tov3_scout/commons_survey_002.mjs` and
`analysis/et_tov3_scout/COMMONS_SURVEY_002/` (founder permission required
for deletions); no other file was touched.
