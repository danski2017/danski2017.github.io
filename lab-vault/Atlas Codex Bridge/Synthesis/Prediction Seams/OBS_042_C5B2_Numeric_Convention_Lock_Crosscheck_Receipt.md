# OBS_042 C5-B2 Numeric Convention-Lock Crosscheck Receipt

## Files Created
- `scripts/et_tov3_scout/obs042_kappa_crosscheck.mjs` (Atlas repo)
- `analysis/et_tov3_scout/OBS042_KAPPA_CROSSCHECK/obs042_kappa_crosscheck_20260717.json`
- [[OBS_042_C5B2_Numeric_Convention_Lock_Crosscheck_Receipt]]

## Files Modified
- None in Prediction Seams.

## Claim Status
Numeric convention-lock crosscheck / C5-B2 structure CONFIRMED / kappa
locked under the declared Atlas convention. Claude-wing numeric method
(repo execution now founder-authorized for instrument work, 2026-07-17).

## Method
Full linearized-Riemann derivation, executed numerically rather than by
hand: harmonic-gauge boosted point-mass metric to O(v)
(h_00=2Phi, h_0i=-4Phi v_i, h_ij=2Phi delta_ij), linearized Riemann by
4D central differences, extraction under the OBS_041 declared convention
(signature -+++, eps_xyz=+1, E_ij=C_i0j0, B_ij=1/2 eps_i^kl C_klj0);
40 seeded sample points r in [5,15]; 4 velocity directions.

## Results
- Calibration (v=0): numeric all-lower C_{i0j0} = MINUS the Atlas
  working E = M(3nn-delta)/r^3; shape residual 4.4e-6. A declared sign
  map, not an error.
- kappa fit: **-2.0000 +/- 5e-6** in every velocity direction; candidate
  structure residual <= 3.8e-5 (O(v), as required).
- VERDICT: the C5-B2 structural candidate
  B_ij^(s) = kappa/2c [eps_kli v^k E_j^(s)l + eps_klj v^k E_i^(s)l]
  is EXACT at leading order, and kappa = -2 as provisionally locked in
  OBS_041. The pair (Atlas working E, kappa=-2) as baked in
  MAGNETIC_WEYL_001 reproduces the true magnetic Weyl.

## Still Uncertified
- The SIGN of scalar witnesses odd in E (e.g. the sign of P_BR) awaits
  an E-sign adjudication (|P_BR| unaffected).
- Literature-convention mapping (external papers) remains a separate
  exercise; this lock is internal to the declared Atlas convention.
- Lobe/sample-point sign maps, surface behavior.

## Boundary Confirmations
- Surface integration remains unauthorized.
- No radiative balance, conservation, or prediction claims.
- codex_context untouched.
