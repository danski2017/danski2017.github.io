# C5-B2 Explicit Weak Field EB Tensor Model Passport

## Claim Status
Explicit E/B tensor model passport / scratch theory / no calculation certified.

This note is not certified evidence, not a calculation, not ordinary-energy accounting, not radiative balance, not conservation, and not a prediction.

Surface integration remains unauthorized.

## Purpose
Declare the minimal weak-field electric-Weyl and magnetic-Weyl tensor model needed to test the C5-B2 F_mid sign-pattern expectation.

This passport does not compute the sign map. It declares which formulas and approximations are allowed for a future hand calculation.

## Source Links
- [[C5-B2 F_mid Sign Pattern Estimate v0.1]]
- [[C5-B2 Projected Pattern Hardening Gate]]
- [[C5-B2 F_mid Projected Pattern Witness Declaration]]
- [[C5-B2 Local Vector Scaling Estimate v0.1]]
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

## Field Convention
Use total weak-field E and total weak-field B first.

Do not use excess-field subtraction, baseline subtraction, or source-group subtraction in the first tensor model.

Reason:
The first task is to test whether total electric/magnetic Weyl coupling produces readable projected directionality on F_mid. Subtraction can introduce artificial sign structure.

## Electric Weyl Model
Use the Newtonian weak-field tidal tensor for each source:

E_ij^(s)(x) = GM [3 n_i n_j - delta_ij] / r^3

where:

r_s = x - x_s
r = |r_s|
n = r_s / r

Total electric tensor:

E_ij(x) = E_ij^(A)(x) + E_ij^(B)(x)

Normalization/sign convention must be checked before certification. At this passport stage, only the tensor structure and scaling are declared.

## Magnetic Weyl Model
Use a leading slow-motion gravitomagnetic/tidal proxy for each moving source.

Allowed first model:
B_ij^(s)(x) is velocity-suppressed relative to E_ij^(s)(x), with schematic dependence:

B^(s) ~ (v_s/c) coupled to E^(s)

The exact convention-correct magnetic Weyl formula is not certified at this passport stage.

Required before any hand sign calculation:
choose one explicit weak-field formula from PN/gravitomagnetic Weyl literature or derive it carefully from the linearized metric.

Allowed options for next gate:
1. literature-backed formula for B_ij of a moving point mass,
2. linearized-metric derivation of B_ij from gravitomagnetic potential,
3. symbolic proxy sufficient only for parity/sign testing, explicitly marked non-certified.

Preferred option:
linearized-metric derivation or literature-backed formula before sign-map calculation.

## Super-Poynting Witness Object
Declared schematic object:

P_BR^i ~ epsilon^i_jk E^j_l B^kl

Shorthand:

P_BR ~ E x B

This is a Weyl-superenergy directionality witness, not ordinary energy flux.

Exact normalization and sign convention remain pending literature/tetrad verification.

## Projected Witness
On F_mid:

P_normal(x) = P_BR(x) · n(x)

where n(x) = x/|x|.

P_normal is a sign/pattern witness only.

Surface integral Phi_BR(F_mid) remains unauthorized.

## Required Checks Before Hand Sign Calculation
Before any explicit sign-pattern calculation, verify:

1. E_ij convention and sign.
2. B_ij formula and sign.
3. Levi-Civita orientation epsilon^i_jk.
4. Source velocity convention.
5. Angular momentum direction.
6. Whether total E and total B include self/source terms at field points on F_mid.
7. Whether F_mid intersects or approaches source exclusion concerns.
8. Whether units and c-factors are tracked.
9. Whether P_normal is interpreted locally only.

## Expected Scaling
E ~ GM/r^3

B ~ (v/c)E

P_BR ~ E B ~ (v/c)E^2

Therefore:

P_normal/E^2 ~ O(v/c)

For equal masses separated by a:

v^2 = GM/(2a)

so:

P_normal/E^2 ~ O(sqrt(GM/(2ac^2)))

This passport does not certify coefficients, signs, or lobe count.

## Hazards
- magnetic Weyl formula may be convention-sensitive,
- sign of P_BR may flip under convention choice,
- total-field tensor coupling may be dominated by self/source sectors,
- F_mid may include near-source anisotropy,
- local projected pattern may not survive radius sensitivity,
- treating P_normal as flux through surface remains forbidden,
- exact tensor signs require explicit formula, not scaling language.

## Allowed Future Work
Allowed after GPT-wing adjudication:
- choose explicit weak-field B_ij formula,
- perform hand sign check at selected sample points on F_mid,
- classify qualitative lobe structure,
- compare sign pattern against OBS_033 expectation.

Not allowed:
- surface integration,
- coefficient certification,
- ordinary-energy comparison,
- radiative flux interpretation,
- conservation claim,
- prediction claim,
- repo execution.

## Current Ruling
C5-B2 should declare the weak-field E/B tensor grammar before sign-pattern calculation.

Preferred next action:
choose or derive the explicit leading-order B_ij formula under the declared observer/tetrad.

## Next Gate
OBS_035:
C5-B2 magnetic-Weyl formula selection gate.

Purpose:
Choose the explicit B_ij model for the first hand sign-pattern calculation.
