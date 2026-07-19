# C5-B2 Provisional Convention Lock Attempt v0.1

## Claim Status
Provisional convention-lock attempt / magnetic-Weyl formula candidate / no calculation certified.

This note is not certified evidence, not a completed derivation, not a repo calculation, not ordinary-energy accounting, not radiative balance, not conservation, and not a prediction.

Surface integration remains unauthorized.

The kappa value below is provisional under the declared Atlas convention attempt only.

## Source Links
- [[C5-B2 Convention Lock Derivation Table]]
- [[C5-B2 Literature Convention Extraction v0.1]]
- [[C5-B2 B_ij Structural Derivation Candidate v0.1]]
- [[C5-B2 Linearized Metric B_ij Derivation Passport]]
- [[../Frontier Evidence Rule|Frontier Evidence Rule]]
- [[../../Best Practices/Claim Boundary Checklist|Claim Boundary Checklist]]

## Purpose
Preserve the GPT-wing provisional convention-lock derivation attempt for the C5-B2 magnetic-Weyl tensor.

This note records a candidate kappa value under a declared internal convention. It does not certify signs, coefficients, lobe maps, or surface flux.

## Convention Attempt
Metric signature:

(-,+,+,+)

Spatial orientation:

epsilon_xyz = +1

Observer:

Eulerian/static barycentric observer

Electric Weyl convention:

E_ij = C_i0j0

Magnetic Weyl convention:

B_ij = 1/2 epsilon_i^{kl} C_klj0

Newtonian source electric tensor:

E_ij^(s) = GM(3 n_i n_j - delta_ij)/r^3

where:

r_s = x - x_s
r = |r_s|
n = r_s/r

## Provisional Magnetic-Weyl Candidate
A static source has no leading magnetic Weyl component in this weak-field observer convention:

B_ij = 0

For a slow-moving source, the structural magnetic-Weyl candidate is velocity-rotated electric Weyl:

B_ij^(s) = kappa/c * epsilon_{kl(i} v_s^k E_{j)}^(s)l

Under this convention attempt, the provisional value is:

kappa = -2

Thus:

B_ij^(s) = -2/c * epsilon_{kl(i} v_s^k E_{j)}^(s)l

Expanded:

B_ij^(s)
=
-1/c [
  epsilon_{kli} v_s^k E_j^(s)l
  +
  epsilon_{klj} v_s^k E_i^(s)l
]

## Total Field Construction
For the equal-mass binary:

Source A:
x_A = (-a/2,0,0)
v_A = (0,-v,0)

Source B:
x_B = (+a/2,0,0)
v_B = (0,+v,0)

Total electric field:

E_total = E_A + E_B

Total magnetic field:

B_total = B_A + B_B

Important distinction:
B_s is generated from each source's own E_s and velocity v_s. The C5-B2 super-Poynting witness then couples total E with total B:

P_BR^i ~ epsilon^i_jk E_total^j_l B_total^kl

and:

P_normal = P_BR · n

## What This Supports
This provisional lock preserves:

B ~ (v/c)E

and therefore:

|P_BR|/E^2 ~ O(v/c)

and:

P_normal/E^2 ~ O(v/c)

For equal masses separated by a:

v^2 = GM/(2a)

so:

P_normal/E^2 ~ O(sqrt(GM/(2ac^2)))

## What Remains Uncertified
Still uncertified:
- absolute kappa,
- final sign,
- exact c-factor placement,
- match to external literature conventions,
- match to full linearized Riemann derivation,
- lobe signs,
- sample-point signs,
- surface behavior,
- surface integration.

The provisional kappa = -2 may flip or change under:
- E_ij sign convention,
- B_ij dual convention,
- Levi-Civita orientation,
- metric signature convention,
- g_0i sign/factor convention,
- Bel-Robinson / super-Poynting sign convention.

## Current Ruling
Classification:
B - candidate survives structurally with provisional convention lock.

Provisional kappa:
kappa = -2 under the declared Atlas convention attempt.

Certification status:
not final.

Required next:
cross-check against literature formula map or full linearized Riemann derivation before any sign-map or sample-point calculation.

## Forbidden Uses
Do not use this note to certify:
- lobe signs,
- sample-point signs,
- P_normal sign map,
- surface integration,
- ordinary-energy flux,
- radiative flux,
- conservation,
- prediction.

## Next Gate
OBS_042:
C5-B2 convention-lock cross-check decision.

Purpose:
Choose whether to:
1. perform literature formula map,
2. perform full linearized Riemann derivation,
3. or keep kappa provisional and defer sign maps.

Recommended next action:
literature formula map first, full Riemann derivation if mismatch or ambiguity remains.
