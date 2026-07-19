---
type: platform_change_receipt
status: archived
created: 2026-07-17
tags: [atlas-platform, commons, finger-trap, density, receipt]
---

# 2026-07-17 Receipt — Commons Density Probe 001 (finger-trap hypothesis)

## Change
New script `scripts/et_tov3_scout/commons_density_probe_001.mjs` (additive;
no viewer edits, no dataset overwrites). Packet:
`analysis/et_tov3_scout/COMMONS_DENSITY_PROBE_001/commons_density_probe_001_20260717.json`
(includes full per-rung censuses).

## Design
Founder hypothesis 2026-07-17: "star fields are like Chinese finger traps —
the more you add, the tighter the structure becomes." Tested on the real
roster, no synthetics: nested mu-rank sub-rosters (N = 16, 24, 32, 48, 66)
each treated as a declared scene; attribution over the active subset;
entropy normalized by ln(N_active); FIXED 48^3 lattice (66-source box) so
rungs are comparable; cross-rung trough matching at radius 1.0.

## Results
- Accretion: 3 -> 12 -> 19 -> 28 -> 36 troughs; disputed class 3 -> 7 ->
  10 -> 9 -> 9 (saturates).
- Locking: after the sparse N=16 rung the population stops reshuffling —
  persistence 11/12 (24->32), 12/19 (32->48), 22/28 (48->66), median
  drift down to ~0.14 (~dx/3). New sources ADD troughs without displacing
  old ones.
- Sharpening: median ambient trough entropy declines 0.88 -> 0.68 (few
  sources = everything disputed; more sources = resolved dominance
  structure with a stable disputed core).
- Object level: the lalande trough already exists at N=16 and converges
  monotonically onto its final position as members are added — distance
  to final: 1.17 -> 0.68 -> 0.35 -> 0.12 -> 0.

## Verdict
SUPPORTED at Observed rung, with the Context Sweep 001 contrast giving the
mechanism its two sides: sources added as MEMBERS of the weave pin and
tighten commons structure; amplitude added as unattributed exterior pull
loosens and destroys it. The grip comes from the weave, not from outside
pressure. Joint reading: commons objects strengthen with roster density
AND carry a declared Lambda_Pi ceiling.

## Validation
node --check pass; 0.4 s on the Mac mini; N=66 rung reproduces
COMMONS_SURVEY_001 exactly (36 troughs / 9 disputed).

## Boundary
Observed. mu-rank nesting is ONE lawful growth path; spatial-shell nesting
cross-check owed (mu-rank adds faint sources everywhere at once — a
distance-ordered growth path could behave differently at the rim).
Initial-slice diagnostic; not dynamics. Vocabulary candidate, not decision.

## Rollback
Delete `scripts/et_tov3_scout/commons_density_probe_001.mjs` and
`analysis/et_tov3_scout/COMMONS_DENSITY_PROBE_001/` (founder permission
required for deletions); no other file was touched.
