---
type: flux_object_declaration_gate
status: scratch_theory
created: 2026-05-15
candidate: C5-B2
claim_status: flux-object declaration gate / scratch theory / no calculation certified
repo_execution_authorized: false
topics:
  - c5-b2
  - flux-object
  - bel-robinson
  - super-poynting
  - claim-boundary
---

# C5-B2 Flux Object Declaration Gate

## Claim Status

Flux-object declaration gate / scratch theory / no calculation certified.

This note is not certified evidence, not a calculation, not ordinary-energy accounting, not radiative balance, not conservation, and not a prediction.

## Purpose

Declare the first C5-B2 Bel-Robinson / Weyl-superenergy flux witness object before any calculation or scaling derivation.

C5-B2 is not yet comparing to gravitational-wave luminosity. It is defining a flux-like curvature-square witness under declared observer, tetrad, surface, and claim limits.

## Source Links

- [[C5-B2 Bel-Robinson Flux Witness Passport]]
- [[C5-B1 Closeout Summary]]
- [[C5-B Bel-Robinson Literature Theory Map v0.1]]
- [[C5-B Observer Tetrad Declaration Passport]]
- [[../Frontier Evidence Rule|Frontier Evidence Rule]]
- [[../../Best Practices/Claim Boundary Checklist|Claim Boundary Checklist]]

## Scene Lock

Weak-field equal-mass circular binary.

Masses: `M` and `M`.

Separation: `a`.

Circular motion with speed `v`.

Observer: Eulerian/static barycentric observer for first near-zone/matching pass.

Tetrad: orthonormal frame adapted to weak-field barycentric coordinates.

Hypersurface: constant coordinate time slice.

Node 1: asymptotically flat parent context with wave-zone comparison held pending.

No ordinary-energy comparison.

No radiative-balance claim.

## First Flux Object

Declare the first C5-B2 object as a local super-Poynting-like Bel-Robinson witness vector.

Working schematic:

```text
P_BR^i ~ epsilon^i_jk E^j_l B^kl
```

Equivalent shorthand:

```text
P_BR ~ E x B
```

This is a curvature-square flux-like witness, not ordinary energy flux.

The exact numerical normalization is not certified at this gate.

## Why Local Vector First

A local vector witness asks whether dynamic Weyl has meaningful directionality before surface integration can hide structure by cancellation.

This preserves the signal-search question:

Does the magnetic-Weyl readability found in C5-B1 organize into a directional superenergy-flow-like witness?

## First Surface

Declare `F_mid` as the first surface candidate for later use.

`F_mid`:

- closed barycentric sphere,
- center: barycenter,
- radius `R_F = a`,
- source interiors excluded only if the surface intersects source exclusion zones,
- role: near-zone/matching-surface witness,
- not wave-zone,
- not asymptotic radiation surface,
- not physical boundary.

Alternative radii may be tested later:
`R_F = a/2, a, 3a/2, 2a`

but no radius sweep is authorized by this gate.

## Normal and Orientation

For `F_mid`:
normal `n^i` is outward radial unit normal from barycenter.

Surface flux witness, if later authorized:

```text
Phi_BR(F_mid) = integral_F_mid P_BR · n dA
```

Do not compute yet.

## First Output Type

Primary first output:
local vector-direction witness `P_BR^i(x)`

Secondary future output:
surface sign/pattern witness `P_BR · n` on `F_mid`

Surface integral `Phi_BR(F_mid)` is not authorized until after vector/pattern behavior is understood.

## Required Declarations Before Any Scaling

Before scaling derivation, declare:

- whether `P_BR^i` uses `epsilon^i_jk E^j_l B^kl` or a convention-correct variant,
- whether `E` and `B` are total Weyl fields or excess fields,
- whether `B` includes orbital magnetic Weyl only or all motion-induced terms,
- whether `P_BR` is inspected locally, projected on `F_mid`, or integrated,
- whether sign patterns or absolute magnitude are being tracked,
- claim ceiling.

## Expected Scaling

Heuristic only:

```text
P_BR ~ E B
```

Since:

```text
B ~ (v/c) E
```

then:

```text
P_BR ~ (v/c) E^2
```

A normalized directional flux fraction might scale like:

```text
|P_BR| / E^2 ~ O(v/c)
```

This is not yet a certified formula.

## Hazards

- treating `P_BR` as ordinary energy flux,
- assuming a local superenergy vector is invariant without observer/tetrad declaration,
- integrating too early and losing directional structure,
- confusing near-zone `F_mid` with wave-zone radiation,
- coefficient/covention errors in Bel-Robinson contraction,
- accidental conservation language.

## Allowed Future Work

Allowed after GPT-wing adjudication:

- scaling/order-counting estimate for `|P_BR|/E^2`,
- qualitative sign/pattern reasoning on `F_mid`,
- comparison to C5-B1 `rho_shell` only at scaling level.

Not allowed:

- surface integration,
- ordinary-energy comparison,
- radiative flux interpretation,
- conservation claim,
- prediction claim,
- repo execution.

## Current Ruling

C5-B2 should begin with local super-Poynting-like vector witness `P_BR^i`, then inspect projected pattern `P_BR · n` on `F_mid` before any surface integral.

## Next Gate

OBS_029:
GPT-wing adjudication of flux-object declaration and possible authorization of local vector scaling estimate.
