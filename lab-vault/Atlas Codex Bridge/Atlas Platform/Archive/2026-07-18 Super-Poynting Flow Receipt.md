---
type: platform_change_receipt
status: archived
created: 2026-07-18
tags: [atlas-platform, super-poynting, e-sign, flow-layer, receipt]
---

# 2026-07-18 Receipt — Signed Super-Poynting Flow Layer (ratified E-sign map)

## Change
First build under the founder-ratified E-Sign Adjudication v0.1
(ratified 2026-07-18, scope: additive, no loss of existing function):
1. **Bake** (additive): `bake_magnetic_weyl.mjs` now also writes
   `MAGNETIC_WEYL_001/pvec.f32` — the SIGNED super-Poynting vector per
   node under the ratified definition P_BR = -eps_ijk E_atlas B
   (E_atlas = stretch-positive = -C_i0j0). `dynwit.f32` regenerated
   byte-identical (deterministic seed; sanity numbers unchanged:
   magfrac 7.28e-5, max ||M|| 7.43e-20). Manifest wording fixed AT
   SOURCE to the OBS_042-locked kappa (a rebake had silently regressed
   the manually-patched manifest to "provisional" — root cause fixed).
2. **Viewer** (additive): "super-Poynting FLOW (signed vectors)" layer
   in Dynamic Witnesses — oriented streaks (dim tail -> bright head
   encodes direction), top-fraction subsampled, log-|P| colored,
   rendered in the one BL world. Wired into dynRefresh, passport
   ('super-poynting-flow'), and all-layers-off; gaia66-gated.
   Backup: `backups/atlas_platform/index_pre_pvec_20260718.html`.

## Validation
- Bug caught in implementation: the dyn-layer early-return fired before
  the flow block when ONLY the flow box was checked; guard restructured
  and the flow-only path verified live.
- In-browser: flow-only renders (streak shells around moving sources —
  the E x B flow structure visible for the first time); passport "stack
  foam + super-poynting-flow"; familyS drops it; all-layers-off clears;
  zero console errors throughout.

## Boundary
Signed DIRECTION now declared per the ratified map; still NOT radiative
balance, NOT conservation, NOT a prediction; surface integration
remains unauthorized. Kinematics remain a declared diagnostic family.

## Rollback
`cp backups/atlas_platform/index_pre_pvec_20260718.html analysis/et_tov3_scout/pinch_lab_viewer/index.html`;
delete `MAGNETIC_WEYL_001/pvec.f32` (founder permission required).
