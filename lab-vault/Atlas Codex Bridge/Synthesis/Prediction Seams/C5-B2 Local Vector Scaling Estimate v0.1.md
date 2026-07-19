---
type: scratch_local_vector_scaling_estimate
status: weyl_superenergy_directionality_witness
created: 2026-05-15
candidate: C5-B2
claim_status: scratch local vector scaling estimate / Weyl-superenergy directionality witness / no calculation certified
repo_execution_authorized: false
surface_integration_authorized: false
topics:
  - c5-b2
  - local-vector-scaling
  - super-poynting
  - bel-robinson
  - claim-boundary
---

# C5-B2 Local Vector Scaling Estimate v0.1

## Claim Status

Scratch local vector scaling estimate / Weyl-superenergy directionality witness / no calculation certified.

This note is not certified evidence, not a repo calculation, not ordinary-energy accounting, not radiative balance, not conservation, and not a prediction.

## Source Links

- [[C5-B2 Flux Object Declaration Gate]]
- [[C5-B2 Bel-Robinson Flux Witness Passport]]
- [[C5-B1 Closeout Summary]]
- [[C5-B1 S_mid Shell Scaling Sensitivity Estimate v0.1]]
- [[../Frontier Evidence Rule|Frontier Evidence Rule]]
- [[../../Best Practices/Claim Boundary Checklist|Claim Boundary Checklist]]

## Scene Lock

Weak-field equal-mass circular binary.

Masses: `M` and `M`.

Separation: `a`.

Each mass barycentric speed: `v`.

Observer: Eulerian/static barycentric observer.

Tetrad: orthonormal frame adapted to weak-field barycentric coordinates.

Object: local super-Poynting-like Bel-Robinson witness vector.

Declared schematic object:

```text
P_BR^i ~ epsilon^i_jk E^j_l B^kl
```

Shorthand:

```text
P_BR ~ E x B
```

No surface integration.

No ordinary-energy comparison.

No radiative-balance claim.

No conservation claim.

No prediction.

## Scaling Derivation

Electric Weyl scale:

```text
E ~ GM/r^3
```

Magnetic Weyl scale for slow-moving weak-field sources:

```text
B ~ (v/c) E
```

Declared local flux-like witness:

```text
P_BR ~ E x B
```

Magnitude scaling:

```text
|P_BR| ~ E B
```

Substitute `B ~ (v/c)E`:

```text
|P_BR| ~ E[(v/c)E]
```

therefore:

```text
|P_BR| ~ (v/c)E^2
```

Natural normalized local directional witness:

```text
|P_BR|/E^2 ~ v/c
```

For equal masses separated by `a`, each mass orbits at radius `a/2` and:

```text
v^2 = GM/(2a)
```

so:

```text
v/c = sqrt(GM/(2ac^2))
```

Therefore:

```text
|P_BR|/E^2 ~ O(sqrt(GM/(2ac^2)))
```

Equivalently, with `M_tot = 2M`:

```text
|P_BR|/E^2 ~ O(sqrt(GM_tot/(4ac^2)))
```

## Relation to C5-B1

C5-B1 density fraction:

```text
B^2/E^2 ~ v^2/c^2
```

C5-B2 directional flux-like witness:

```text
|P_BR|/E^2 ~ v/c
```

Interpretive distinction:

C5-B1 sees magnetic Weyl as a density fraction.
C5-B2 sees electric-magnetic Weyl coupling as a directional witness.

## Scratch Finding

C5-B2 detects a velocity-gated directional curvature-square witness.

The directionality witness enters at `O(v/c)`, one velocity order earlier than the C5-B1 magnetic density-square fraction when normalized against `E^2`.

## Interpretation Ceiling

This is a local directionality witness only.

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

## Current Ruling

C5-B2 local vector scaling passes as scratch witness estimate.

Finding:

```text
|P_BR|/E^2 ~ O(v/c) ~ O(sqrt(GM/(2ac^2)))
```

for equal masses separated by `a`.

Atlas shorthand:

C5-B1 detects the courier's footprint.
C5-B2 detects the courier's direction.

## Required Checks Before Certification

- verify the exact Bel-Robinson / super-Poynting contraction convention,
- verify magnetic-Weyl scaling in the declared observer/tetrad frame,
- distinguish total fields from excess fields,
- check sign/direction patterns before surface integration,
- avoid treating `P_BR` as ordinary stress-energy flux,
- avoid radiative language before C5-B3/C5-B4 comparison gates.

## Next Gate

OBS_030:
C5-B2 `F_mid` projected pattern witness declaration.

Purpose:
Declare `P_BR · n` on `F_mid` as a pattern witness before any surface integral.
