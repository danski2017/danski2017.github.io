
> [!success] RESOLVED DOWNSTREAM (2026-07-17/18)
> The structural candidate below was CONFIRMED EXACT at O(v) and
> kappa = -2 LOCKED by numeric linearized-Riemann derivation:
> [[OBS_042_C5B2_Numeric_Convention_Lock_Crosscheck_Receipt]].
> E-sign adjudicated and founder-ratified:
> [[C5-B2 E-Sign Adjudication Candidate v0.1]]. The uncertified-sign
> language below is the historical state at drafting time.
# C5-B2 B_ij Structural Derivation Candidate v0.1

## Claim Status
Scratch B_ij structural derivation candidate / magnetic-Weyl formula provisional / no calculation certified.

This note is not certified evidence, not a completed derivation, not a repo calculation, not ordinary-energy accounting, not radiative balance, not conservation, and not a prediction.

Surface integration remains unauthorized.

The sign and numerical factor are not certified.

## Source Links
- [[C5-B2 Linearized Metric B_ij Derivation Passport]]
- [[C5-B2 Magnetic Weyl Formula Selection Gate]]
- [[C5-B2 Explicit Weak Field EB Tensor Model Passport]]
- [[C5-B2 F_mid Sign Pattern Estimate v0.1]]
- [[../Frontier Evidence Rule|Frontier Evidence Rule]]
- [[../../Best Practices/Claim Boundary Checklist|Claim Boundary Checklist]]

## Purpose
Preserve the GPT-wing scratch structural derivation candidate for the leading-order magnetic-Weyl tensor B_ij of a slow-moving weak-field source.

This note earns the tensor shape only. It does not certify sign, factor, lobe pattern, surface flux, or radiative interpretation.

## Scene Lock
Equal-mass weak-field circular binary.

Source A:
x_A = (-a/2, 0, 0)
v_A = (0, -v, 0)

Source B:
x_B = (+a/2, 0, 0)
v_B = (0, +v, 0)

Orbital plane:
xy.

Angular momentum axis:
+z, pending sign verification.

Surface:
F_mid sphere, R_F = a.

Normal:
n(x) = x / |x|.

Observer:
Eulerian/static barycentric observer.

Tetrad:
weak-field barycentric orthonormal frame.

## Electric Tensor
For each source:

E_ij^(s)(x) = GM [3 n_i n_j - delta_ij] / r^3

where:

r_s = x - x_s
r = |r_s|
n = r_s / r

Total electric tensor:

E_ij = E_ij^(A) + E_ij^(B)

Sign convention remains subject to final consistency check.

## Structural Magnetic-Weyl Candidate
For a source at rest relative to the observer, the leading Newtonian magnetic Weyl component vanishes:

B_ij = 0

For a slow-moving source, the leading-order magnetic Weyl tensor must be velocity-suppressed relative to E_ij:

B ~ (v/c) E

The structural candidate is:

B_ij^(s) = kappa/c * epsilon_{kl(i} v_s^k E_{j)}^{(s)l}

Expanded:

B_ij^(s)
=
kappa/(2c) [
  epsilon_{kli} v_s^k E_j^{(s)l}
  +
  epsilon_{klj} v_s^k E_i^{(s)l}
]

where:
- epsilon_ijk is the spatial Levi-Civita symbol,
- parentheses denote symmetrization over i,j,
- kappa is a convention-dependent sign/factor to be determined.

## Required Properties
The candidate has the required structural properties:

1. symmetric in i,j,
2. trace-free because the antisymmetric epsilon contraction is paired with symmetric E,
3. linear in source velocity,
4. linear in electric Weyl,
5. order B ~ (v/c)E,
6. vanishes when v = 0.

## Total Magnetic Tensor
Total magnetic Weyl candidate:

B_ij(x) = B_ij^(A)(x) + B_ij^(B)(x)

Important distinction:
B_ij^(s) uses each source's own E_ij^(s) in the magnetic contribution. The later super-Poynting witness uses total E and total B:

P_BR[E_total, B_total]

## Relation To C5-B2 Witness
The declared C5-B2 witness is:

P_BR^i ~ epsilon^i_jk E^j_l B^kl

Substituting the structural magnetic candidate gives schematic coupling:

P_BR ~ E x B ~ E x [velocity-rotated E]

or:

P_BR = electric-tidal frame coupled to velocity-rotated electric-tidal frame.

This preserves the archived C5-B2 scaling:

P_BR ~ (v/c) E^2

and:

P_normal/E^2 ~ O(v/c)

For equal masses:

v^2 = GM/(2a)

so:

P_normal/E^2 ~ O(sqrt(GM/(2ac^2)))

## Provisional Constant
kappa is not certified.

Possible sign/factor family:
kappa = ±2 or related convention-dependent value.

The exact value depends on:
- definition of B_ij,
- metric convention,
- g_0i sign/factor,
- Levi-Civita orientation,
- observer/tetrad convention,
- linearized Riemann/Weyl sign convention.

No downstream sign or lobe claim may be certified until kappa and the sign convention are checked.

## Allowed Use
Allowed:
- scaling checks,
- structural sign intuition,
- preparation for literature/convention cross-check,
- preparation for explicit hand derivation review.

Not allowed:
- certified lobe signs,
- sample-point sign claims,
- coefficient claims,
- surface integration,
- ordinary-energy comparison,
- radiative flux interpretation,
- conservation claim,
- prediction claim,
- repo execution.

## Current Ruling
The B_ij tensor shape is earned as a structural candidate.

The sign/factor compass is not yet calibrated.

## Next Gate
OBS_038:
C5-B2 magnetic-Weyl literature/convention cross-check.

Purpose:
Lock or correct kappa, sign, c-factors, and exact definition of B_ij before any sign-map or sample-point calculation.
