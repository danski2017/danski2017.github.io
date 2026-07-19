---
type: platform_change_receipt
status: archived
created: 2026-07-17
tags: [atlas-platform, magnetic-weyl, momentum-constraint, c5-b2, receipt]
---

# 2026-07-17 Receipt — Dynamic Witnesses: Magnetic Weyl + Momentum Monitor

## Change
Realizes two long-owed features from the C5-B2 seam and the Dynamic
Evolution roadmap inside the instrument (founder directive 2026-07-17):
1. **Bake** `scripts/et_tov3_scout/bake_magnetic_weyl.mjs` →
   `datasets/MAGNETIC_WEYL_001/`:
   - `kinematics.json` — DECLARED seeded kinematic extension of the
     gaia66 roster (mulberry32 seed 2026, isotropic gaussian, beta_ref
     1e-4). NOT astrometry. B and the monitor are linear in beta.
   - `dynwit.f32` — 257,482 nodes on the declared 64^3 volume lattice
     (same box/guard as COMMONS_ATLAS_001), per node: ||B||_F, magnetic
     fraction, |P_BR|, momentum residual ||M||, ||E||_F.
   - Physics: C5-B2 structural magnetic candidate B_ij^(s) =
     kappa/2c eps_kl(i v^k E_j)^(s)l with PROVISIONAL kappa = -2
     (OBS_041; sign/factor uncertified, OBS_042 crosscheck owed);
     super-Poynting P^i = eps^i_jk E^j_l B^kl on totals (declared C5-B2
     witness); momentum monitor M^i = d_j(psi^-10 Ahat^ij) over the
     composite Bowen-York sum (roadmap Phase-4 proxy; ladder
     prerequisite for K_ij promotion), central differences 0.02.
   - Sanity at bake: mean magnetic fraction 7.3e-5 ~ O(beta) as the
     seam scaling requires; residual finite (max 7.4e-20), nonzero only
     through the psi coupling — the pasted-sum violation the monitor
     exists to display.
2. **Viewer**: `blDynSection` in the BL Layer Stack — four toggleable
   layers (magnetic Weyl norm, magnetic fraction, super-Poynting,
   momentum residual), top-fraction slider (default 20%), log-normalized
   coloring; gaia66-gated with passport-truthful stack declaration;
   covered by all-layers-off. Claim note in-panel preserves every seam
   boundary (not radiative balance / conservation / prediction; surface
   integration remains unauthorized).
Backups: `index_pre_commons_layers_20260717.html` remains the session
rollback root; this change is JS/HTML-additive on top.

## Validation
node --check pass; bake 6.1 s. In-browser: gaia66 + layers render with
passport "stack foam + magnetic-weyl + momentum-residual"; Family S
switch drops geometry AND passport entries ("stack foam"); all-layers-off
unchecks and clears; zero console errors throughout. One nesting defect
(commons note swallowed by the new section) caught and fixed during
implementation.

## Boundary
Implemented/Observed. The magnetic tensor SHAPE is the certified part;
kappa sign/factor provisional. Kinematics are a declared diagnostic
family. The momentum layer is a constraint-residual display honoring the
promotion-order doctrine, not a solved constraint. OBS_042
(literature/Riemann convention crosscheck) is the gate to firm kappa.

## Rollback
Remove blDynSection + dynLayersUpdate wiring from index.html (or restore
backups/atlas_platform/index_pre_commons_layers_20260717.html and re-apply
the commons-layer receipt), delete datasets/MAGNETIC_WEYL_001/ and
bake_magnetic_weyl.mjs (founder permission required for deletions).
