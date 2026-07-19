# C5-B2 F_mid Sign Pattern Estimate v0.1

## Claim Status
Scratch qualitative sign-pattern estimate / projected Weyl-superenergy directionality witness / no calculation certified.

This note is not certified evidence, not a repo calculation, not ordinary-energy accounting, not radiative balance, not conservation, and not a prediction.

Surface integration remains unauthorized.

## Source Links
- [[C5-B2 Projected Pattern Hardening Gate]]
- [[C5-B2 F_mid Pattern Estimate v0.1]]
- [[C5-B2 F_mid Projected Pattern Witness Declaration]]
- [[C5-B2 Local Vector Scaling Estimate v0.1]]
- [[../Frontier Evidence Rule|Frontier Evidence Rule]]
- [[../../Best Practices/Claim Boundary Checklist|Claim Boundary Checklist]]

## Locked Geometry
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
+z, subject to sign-check note from the hardening gate.

Surface:
F_mid sphere, R_F = a.

Normal:
n(x) = x / |x|.

Witness:
P_normal = P_BR · n.

Object:
P_BR ~ E x B.

Field convention:
total weak-field E and total weak-field B.

No integration.
No coefficient claim.
No radiative claim.

## Scaling Reminder
From C5-B2 local vector scaling:

P_BR ~ E x B

with:

B ~ (v/c)E

therefore:

P_BR ~ (v/c)E^2

Projection gives:

P_normal/E^2 ~ O(v/c)

For equal masses separated by a:

v^2 = GM/(2a)

therefore:

P_normal/E^2 ~ O(sqrt(GM/(2ac^2)))

unless local orientation or symmetry suppresses the projection.

## Qualitative Symmetry Estimate
The equal-mass circular binary should not produce a simple all-outward or all-inward projected pattern.

Expected morphology:
- alternating positive and negative sectors on F_mid,
- strongest organization near the orbital plane,
- tangential or near-null bands where P_BR runs mostly along the surface,
- sign changes tied to orbital phase,
- possible cancellation under full-sphere integration even when local pattern is nonzero.

The pattern is expected to be phase-organized because the witness couples:
- the electric Weyl tidal frame, which remembers source separation,
- the magnetic Weyl frame, which remembers source motion.

Thus the projected pattern should remember both where the sources are and which way they are moving.

## Sign Interpretation
P_normal > 0:
local outward-projected curvature-square directionality.

P_normal < 0:
local inward-projected curvature-square directionality.

P_normal approximately 0:
surface-tangential flow, symmetry cancellation, or weak projected direction.

The signs are local pattern witnesses only.

## Cancellation Warning
The full-sphere signed integral may cancel:

integral_F_mid P_normal dA approximately 0

while local structure remains nonzero:

P_normal(x) not approximately 0 locally

At this rung, cancellation is not failure. It may indicate that the projected witness is pattern-bearing before it is total-flux-bearing.

## Scratch Finding
C5-B2 F_mid sign-pattern estimate passes as qualitative witness expectation.

Expected order:
P_normal/E^2 ~ O(v/c) ~ O(sqrt(GM/(2ac^2)))

Expected morphology:
phase-organized lobed sign pattern on F_mid, strongest near orbital-plane or motion-coupled sectors, with possible null/tangential bands and likely signed cancellation under full-sphere integration.

## Interpretation Ceiling
This is a projected directionality-pattern witness only.

It is not:
- ordinary energy,
- gravitational-wave luminosity,
- Bondi mass loss,
- Isaacson stress-energy,
- radiative flux,
- conservation law,
- prediction,
- certified calculation,
- surface-integrated flux.

Atlas shorthand:
The courier's direction should remember both separation and motion before any flux total is allowed.

## Required Checks Before Certification
- verify exact Bel-Robinson / super-Poynting contraction convention,
- verify angular momentum sign convention,
- check sign behavior against explicit weak-field E and B tensors,
- test whether lobes are robust under F_mid radius changes,
- distinguish local projected pattern from integrated flux,
- do not compare to ordinary GW energy channels until C5-B3/B4.

## Current Ruling
C5-B2 F_mid sign-pattern estimate passes as scratch qualitative witness expectation.

Surface integration remains unauthorized.

## Next Gate
OBS_034:
C5-B2 explicit weak-field E/B tensor model passport.

Purpose:
Declare the minimal analytic tensor model needed to test the sign-pattern expectation without repo execution or surface integration.
