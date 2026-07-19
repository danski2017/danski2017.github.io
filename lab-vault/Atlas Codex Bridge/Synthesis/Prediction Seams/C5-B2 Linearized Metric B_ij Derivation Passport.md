# C5-B2 Linearized Metric B_ij Derivation Passport

## Claim Status
Linearized-metric B_ij derivation passport / scratch theory / no calculation certified.

This note is not certified evidence, not a completed derivation, not a calculation, not ordinary-energy accounting, not radiative balance, not conservation, and not a prediction.

Surface integration remains unauthorized.

## Purpose
Declare the derivation setup for the leading-order magnetic Weyl tensor B_ij from the weak-field linearized metric before deriving or using any explicit B_ij formula.

This passport follows OBS_035, which selected Route B: linearized-metric derivation first, with literature formula cross-check later.

The goal is to earn B_ij under declared observer, tetrad, sign, and weak-field conventions before any C5-B2 sign-map or lobe claim.

## Source Links
- [[C5-B2 Magnetic Weyl Formula Selection Gate]]
- [[C5-B2 Explicit Weak Field EB Tensor Model Passport]]
- [[C5-B2 Projected Pattern Hardening Gate]]
- [[C5-B2 F_mid Sign Pattern Estimate v0.1]]
- [[C5-B2 Flux Object Declaration Gate]]
- [[../Frontier Evidence Rule|Frontier Evidence Rule]]
- [[../../Best Practices/Claim Boundary Checklist|Claim Boundary Checklist]]

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

## Regime
Weak-field, slow-motion, linearized GR / post-Newtonian leading-order setup.

Assumptions:
- v/c << 1
- GM/(rc^2) << 1 at witness points
- sources treated as compact point-mass approximations for field derivation
- no radiation-zone extraction
- no retarded-time wave-zone calculation at this gate
- no surface integration

## Metric Convention To Declare
Use a weak-field metric of the schematic form:

g_00 = -(1 + 2Phi/c^2)

g_0i = declared gravitomagnetic term from vector potential A_i

g_ij = (1 - 2Phi/c^2) delta_ij

The exact sign and factor convention for g_0i must be declared before derivation.

Candidate convention to check:

g_0i = -4 A_i / c^3

or equivalent PN convention, with factors of c and sign explicitly tracked.

Do not certify this convention until checked.

## Potentials
Scalar potential:

Phi(x) = - sum_s G M / |x - x_s|

Vector potential candidate:

A_i(x) = sum_s G M v_{s,i} / |x - x_s|

subject to sign and c-factor convention.

The vector potential is used only to obtain the leading gravitomagnetic contribution.

## Electric Weyl Side
Electric tensor already declared in OBS_034:

E_ij^(s)(x) = GM [3 n_i n_j - delta_ij] / r^3

where:

r_s = x - x_s
r = |r_s|
n = r_s / r

Total:

E_ij = E_ij^(A) + E_ij^(B)

Sign convention remains subject to final consistency check.

## Magnetic Weyl Target
Derive or obtain leading-order B_ij relative to the Eulerian/static barycentric observer.

Target properties:

B_ij = B_ji
B_i^i = 0
B_ij is O(v/c) relative to E_ij
B_ij depends on source velocity v_s and separation vector r_s
B_ij total = B_ij^(A) + B_ij^(B)

## Candidate Derivation Route
Use one of the following equivalent derivation paths, to be selected during derivation:

### Path 1: Weyl/Riemann route
Compute the magnetic part of Weyl:

B_ij = 1/2 epsilon_i^{ kl} C_klj0

In weak-field vacuum outside sources, C may be replaced by the relevant Riemann components at leading order.

Need:
- linearized Riemann components involving h_0i,
- Levi-Civita sign convention,
- observer u^a approximately partial_t.

### Path 2: Gravitomagnetic tidal route
Define a gravitomagnetic field from A_i, then form the symmetric trace-free magnetic tidal tensor from its derivatives.

Need:
- relation between A_i and gravitomagnetic field,
- relation between gravitomagnetic field gradient and B_ij,
- symmetrization and trace-free projection,
- sign/factor check.

### Path 3: Literature formula insertion after derivation setup
Use a published leading-order expression only after matching conventions.

Need:
- source reference,
- convention map,
- sign/factor comparison to the selected metric convention.

## Required Convention Locks Before Derivation
Before any formula is accepted, lock:

1. metric signature,
2. sign of Phi,
3. sign/factor of g_0i,
4. definition of A_i,
5. orientation of epsilon_ijk,
6. observer u^a,
7. whether B_ij = +1/2 epsilon_i^{kl} C_klj0 or sign-flipped convention,
8. units and c-factors,
9. whether fields are evaluated outside source worldtubes only,
10. how total source contributions are summed.

## Relation To C5-B2 Witness
Once B_ij is earned, future work may evaluate the declared witness:

P_BR^i ~ epsilon^i_jk E^j_l B^kl

and projected pattern:

P_normal = P_BR · n

on F_mid.

This passport does not authorize that evaluation.

## Expected Scaling Check
The derived B_ij must satisfy:

B ~ (v/c) E

Therefore:

P_BR ~ E B ~ (v/c) E^2

and:

P_normal/E^2 ~ O(v/c)

If the derived B_ij does not preserve this scaling, the derivation must be reviewed before use.

## Forbidden Shortcuts
Do not:
- use B ~ (v/c)E as the explicit formula,
- treat B as a vector,
- import radiation-zone B/E relations,
- skip symmetrization or trace-free checks,
- ignore c-factors,
- ignore sign convention,
- integrate P_normal over F_mid,
- compare to GW luminosity,
- claim flux, conservation, or prediction.

## Allowed Future Work
Allowed after GPT-wing adjudication of this passport:
- perform a hand derivation of leading-order B_ij from the declared metric setup,
- or produce a literature-backed formula map under the declared conventions.

Not allowed:
- repo execution,
- surface integration,
- coefficient certification beyond the derivation's declared convention,
- public claim,
- ordinary-energy comparison.

## Current Ruling
C5-B2 should derive B_ij from the linearized metric before any sign-pattern calculation.

The derivation must prioritize sign/factor clarity over speed.

## Next Gate
OBS_037:
C5-B2 hand derivation of leading-order B_ij, or literature-backed formula map if derivation stalls.

Recommended:
GPT-wing hand derivation first, then literature cross-check.
