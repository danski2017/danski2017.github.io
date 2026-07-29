# Atlas Temporal Harness Phase II-C Curvature Robustness and Full Weyl Receipt

Date: 2026-07-27  
Work order: `ATLAS_TEMPORAL_HARNESS_PHASE_IIC_CURVATURE_ROBUSTNESS_FULL_WEYL_001`  
Result: **C1/C2/C3 PASS; C4 PASS WITH BOUND**

## Result

Atlas now possesses a complete evolved E/B/complex-Weyl measurement subsystem
validated within the declared offline engineering scope. This does not promote
the tiny real A-to-B changes to resolved physical dynamics.

## Electric robustness and reproduction

The inherited production E path exhibits controlled second-order convergence
on three isotropic-Schwarzschild resolutions. Relative RMS orders are 2.010 and
2.063; the original 2.106% radial magnitude error decreases to 0.489%; raw
Ricci antisymmetry decreases from 1.854% to 0.538% of exact peak E. An
independently coded explicit-stencil Christoffel/Ricci/E path reproduces the
same-order production result on references and both real epochs. The diagnostic
fourth-order route converges at orders 4.117 and 4.058. It is retained as an
operator-disagreement estimate rather than silently replacing Phase II-B.

## Magnetic and complex Weyl

The canonical evolved implementation is
`B_ij=STF[epsilon_i^{kl}D_kK_lj]` under
`atlas-3plus1-curvature-v1.0`, `K_ij=-(1/2)Lie_n gamma_ij`, and right-handed
`epsilon_xyz=+sqrt(det gamma)`. Static K=0 reduction is exact. The independent
manufactured case `K_yy=sin(x), K_zz=-sin(x)` reproduces
`B_yz=B_zy=cos(x)` with second- and fourth-order convergence. Real A/B output
is symmetric, trace-free, and finite on declared support.

`weyl_complex_ij=E_ij+iB_ij` is stored as complex128 with exact float64 real
and imaginary mirrors. B=0 reduces exactly to W=E. A regression discovered
that the first implementation allowed invalid-mask NaN(B) to contaminate the
complex real channel outside valid support; channel-wise construction corrected
it before completion.

## First uncertainty floor and history ruling

The structured, conservative maximum-component envelope is:

- E peak `3.171280288e-4`; RMS `1.114974084e-4`.
- B peak `2.324983231e-5`; RMS `3.949099402e-6`.

Measured A-to-B differences are E peak `4.352718719e-6`, RMS
`1.262223773e-6`; B peak `1.011841374e-5`, RMS `2.553818787e-6`.
Neither channel exceeds its matching peak or RMS floor. The A/B history is
therefore observed and engineering-validated with a bound, not physically
resolved.

`weyl_gap` is definition-blocked because current authority does not choose
among complex eigenvalue, Takagi, or singular-value constructions and their
ordering/degeneracy policies. That subtask stopped without blocking E/B/W.

## Safety, tests, and claims

No ET process was launched. Peak RSS was 1,297,317,888 bytes. Passive swap was
207.44 MiB before and after. Harness tests pass 84/84 and Temporal Pilot passes
20/20. Fourteen 2D/3D audit renders were emitted; renders are not proof.

Earned within declared scope: E extraction reproduced/numerically
characterized; B extraction implemented/validated; full evolved Weyl bundle
implemented/validated with uncertainty bound; A/B E/B/W history observed and
engineering-validated; first curvature uncertainty floor defined/implemented.

Not earned: real-data continuum convergence, production NR, physical
gravitational-wave detection, invariant memory, source attribution, Commons,
invariant significance of A-to-B change, publication-grade NR, or new GR
physics.
