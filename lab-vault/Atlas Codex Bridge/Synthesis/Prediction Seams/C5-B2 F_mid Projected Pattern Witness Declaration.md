---
type: projected_pattern_witness_declaration
status: scratch_theory
created: 2026-05-15
candidate: C5-B2
claim_status: projected pattern witness declaration / scratch theory / no calculation certified
repo_execution_authorized: false
surface_integration_authorized: false
topics:
  - c5-b2
  - f-mid
  - projected-pattern
  - super-poynting
  - claim-boundary
---

# C5-B2 F_mid Projected Pattern Witness Declaration

## Claim Status

Projected pattern witness declaration / scratch theory / no calculation certified.

This note is not certified evidence, not a calculation, not ordinary-energy accounting, not radiative balance, not conservation, and not a prediction.

Surface integration remains unauthorized.

## Purpose

Declare the next C5-B2 witness after local vector scaling: the projected super-Poynting-like directionality pattern on the near-zone matching surface `F_mid`.

The purpose is to inspect directional structure before any surface integral can erase or falsely promote it.

## Source Links

- [[C5-B2 Local Vector Scaling Estimate v0.1]]
- [[C5-B2 Flux Object Declaration Gate]]
- [[C5-B2 Bel-Robinson Flux Witness Passport]]
- [[C5-B1 Closeout Summary]]
- [[../Frontier Evidence Rule|Frontier Evidence Rule]]
- [[../../Best Practices/Claim Boundary Checklist|Claim Boundary Checklist]]

## Scene Lock

Weak-field equal-mass circular binary.

Masses: `M` and `M`.

Separation: `a`.

Circular motion with speed `v`.

Observer: Eulerian/static barycentric observer.

Tetrad: orthonormal frame adapted to weak-field barycentric coordinates.

Hypersurface: constant coordinate time slice.

No wave-zone claim.

No ordinary-energy comparison.

No radiative-balance claim.

## Prior C5-B2 Result

Local vector scaling:

```text
P_BR ~ E x B
```

with:

```text
B ~ (v/c)E
```

therefore:

```text
|P_BR|/E^2 ~ O(v/c)
```

For equal masses separated by `a`:

```text
|P_BR|/E^2 ~ O(sqrt(GM/(2ac^2)))
```

## Declared Surface: F_mid

`F_mid` is a near-zone barycentric sphere:

- center: barycenter
- radius: `R_F = a`
- normal: outward radial unit normal `n` from barycenter
- role: near-zone projected pattern witness
- not wave-zone
- not asymptotic radiation surface
- not physical boundary

## Projected Pattern Witness

Declare:

```text
P_normal(x) = P_BR(x) · n(x), for x on F_mid
```

where:

```text
P_BR^i ~ epsilon^i_jk E^j_l B^kl
```

or convention-correct variant after literature/tetrad review.

`P_normal` is a sign/pattern witness.

It is not a surface-integrated flux and not an energy flux.

## Pattern Questions

The first pattern inquiry asks:

1. Does `P_normal` show coherent outgoing/incoming lobes on `F_mid`?
2. Are signs organized by orbital phase, source positions, or symmetry axes?
3. Does the pattern cancel globally while remaining locally structured?
4. Is the pattern dominated by near-source sectors or distributed across the shell?
5. Does `P_normal` preserve the expected `O(v/c)` local scaling?
6. Does the pattern suggest a lawful next surface or tetrad revision?

## Allowed Future Work

Allowed after GPT-wing adjudication:

- scaling/order-counting for `P_normal/E^2`,
- qualitative sign/pattern reasoning,
- symmetry classification of expected lobes,
- comparison to C5-B1 `S_mid` readability witness at low claim status.

Not allowed:

- integral `Phi_BR(F_mid)`,
- total flux claim,
- ordinary-energy comparison,
- radiative-flux interpretation,
- conservation claim,
- prediction claim,
- repo execution.

## Expected Scaling

Since:

```text
P_BR ~ (v/c) E^2
```

then projection onto `n` should preserve the same order unless symmetry or local orientation suppresses it:

```text
P_normal/E^2 ~ O(v/c)
```

For equal masses:

```text
P_normal/E^2 ~ O(sqrt(GM/(2ac^2)))
```

This is only a projected pattern estimate, not a flux integral.

## Hazards

- projection may introduce sign cancellations,
- high symmetry may produce zero net pattern even with nonzero local structure,
- local pattern may depend on observer/tetrad convention,
- `F_mid` radius choice may affect morphology,
- treating `P_normal` as flux through surface is forbidden at this gate,
- integrating too early can hide structure or falsely imply conservation.

## Current Ruling

C5-B2 should next inspect `P_BR · n` on `F_mid` as a projected pattern witness before any surface integration.

## Next Gate

OBS_031:
GPT-wing adjudication of projected pattern witness and possible authorization of qualitative symmetry/sign-pattern estimate.
