---
type: canonical_specification
status: frozen
created: 2026-07-26
updated: 2026-07-27
convention_id: atlas-3plus1-curvature-v1.0
implementation_version: atlas-electric-weyl/1.0
magnetic_implementation_version: atlas-magnetic-weyl/1.0
---

# Atlas Curvature Convention Registry

## Canonical 3+1 convention

This note is the current authority for Atlas electric-Weyl and tidal-operator
names. The machine-readable companion is
`analysis/atlas_temporal_harness/phase_iib_convention_fix_001/CURVATURE_CONVENTION_FREEZE.json`.

- Spacetime signature: `(-,+,+,+)`.
- Riemann convention:
  `R^rho_{ sigma mu nu}=partial_mu Gamma^rho_{nu sigma}-partial_nu Gamma^rho_{mu sigma}+Gamma^rho_{mu lambda}Gamma^lambda_{nu sigma}-Gamma^rho_{nu lambda}Gamma^lambda_{mu sigma}`.
- `n^mu` is future-directed and unit timelike.
- `K_ij=-(1/2) Lie_n gamma_ij`.
- The spatial Levi-Civita tensor is right-handed:
  `epsilon_xyz=+sqrt(det(gamma))`.

The canonical electric Weyl tensor is

`E_ij=C_{i alpha j beta} n^alpha n^beta`

and its matter-inclusive 3+1 realization is

`E_ij=[R3_ij+K K_ij-K_i^k K_kj-4 pi S_ij]^TF`.

Trace removal and contractions use the physical spatial metric `gamma_ij`.
For Schwarzschild in an orthonormal frame, radial first,

`eig(E)=(-2,+1,+1) M/R^3`.

## Tidal acceleration operator

Stretch-positive relative acceleration is represented separately:

`tidal_acceleration_ij=-electric_weyl_ij`.

Thus

`D^2 xi^i/dtau^2=-E^i_j xi^j=tidal_acceleration^i_j xi^j`.

The acceleration operator is derived from `E_ij`; it is not a second electric
Weyl tensor. Historical positive-radial variables called `E` or `tidal_tensor`
must be labeled as legacy acceleration-operator data before current use.

## Magnetic and complex Weyl boundary

The formal convention is

`B_ij=(1/2) epsilon_i^{ kl} C_{kl j beta} n^beta`

using the same Riemann/Weyl sign, normal, and spatial orientation as `E_ij`.
For `K_ij=-(1/2) Lie_n gamma_ij`, the certified evolved implementation is

`B_ij=STF[epsilon_i^{ kl} D_k K_lj]`,

with all contractions and STF operations performed using `gamma_ij`. The
current complex name is `weyl_complex_ij=E_ij+i B_ij`; Phase II-C validates
both under the declared engineering scope and uncertainty bound. The real A/B
magnetic signal remains below its first conservative extraction floor and is
not physically interpreted. Legacy magnetic payloads that mixed the
positive-radial proxy with canonical Ricci/TF fields remain quarantined from
rebaking and signed interpretation.

`weyl_gap` remains definition-blocked: the master does not yet select complex
eigenvalues, Takagi values, or singular values and their ordering/degeneracy
policy. No implementation may invent that doctrinal choice merely to close a
package.

## Eigenstructure and migration

Current Atlas tensor eigenvalues are ordered by descending absolute magnitude.
Under `E -> -E`, eigenvalues negate in the same slots, eigenvectors are
unchanged up to eigenvector sign, and `eigen_gap_full` is unchanged. Signed
components, signed eigenvalues, and stretch/compression labels remain
sign-sensitive. Norms, squared budgets, and norm-based GCS/compression results
are sign-even.

Historical publications remain historical records. Current-facing readings of
them must use the convention addendum in `Papers/Current Papers` and the Phase
II-B migration audit.
