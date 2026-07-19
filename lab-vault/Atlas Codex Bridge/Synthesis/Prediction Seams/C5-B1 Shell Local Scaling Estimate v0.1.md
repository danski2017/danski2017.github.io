---
type: scratch_shell_local_scaling_estimate
status: dynamic_weyl_readability_witness
created: 2026-05-15
candidate: C5-B1
claim_status: scratch shell/local scaling estimate / dynamic Weyl readability witness / no calculation certified
repo_execution_authorized: false
whole_domain_integration_authorized: false
topics:
  - c5-b1
  - shell-local-scaling
  - magnetic-weyl
  - dynamic-weyl-readability
  - claim-boundary
---

# C5-B1 Shell Local Scaling Estimate v0.1

## Claim Status

Scratch shell/local scaling estimate / dynamic Weyl readability witness / no calculation certified.

This note is not certified evidence, not a repo calculation, not a conservation claim, not ordinary-energy accounting, not radiative balance, and not a prediction.

## Source Links

- [[C5-B1 Shell Local Magnetic Fraction Witness]]
- [[C5-B1 Magnetic Fraction Diagnostic Passport]]
- [[C5-B1 Scratch Scaling Estimate v0.1]]
- [[C5-B Observer Tetrad Declaration Passport]]
- [[../Frontier Evidence Rule|Frontier Evidence Rule]]
- [[../../Best Practices/Claim Boundary Checklist|Claim Boundary Checklist]]

## Scene Lock

Weak-field equal-mass circular binary.

Masses: `M` and `M`.

Separation: `a`.

Each mass orbits the barycenter with speed `v`.

Observer: Eulerian/static barycentric observer.

Tetrad: orthonormal frame adapted to weak-field barycentric coordinates.

Hypersurface: constant coordinate time slice.

Default shell: barycentric annular shell excluding source neighborhoods.

No whole-domain integration.

No wave-zone flux.

No ordinary-energy comparison.

No radiative-balance claim.

## Witness Definitions

Local witness:

```text
rho_local(x) = B_ij(x) B^ij(x) / E_ij(x) E^ij(x)
```

Shell witness:

```text
rho_shell(S) = integral_S B_ij B^ij dV / integral_S E_ij E^ij dV
```

where `S` is a declared barycentric annular shell, treated as a datum rather than a physical boundary.

## Scaling Estimate

Weak-field electric Weyl scale:

```text
E ~ GM / r^3
```

For moving weak-field sources, magnetic Weyl is velocity-suppressed:

```text
B ~ (v/c) E
```

Therefore:

```text
rho_local(x) ~ B^2/E^2 ~ v^2/c^2
```

For an equal-mass circular binary with separation `a`, each mass orbits at radius `a/2`. Newtonian force balance gives:

```text
G M^2 / a^2 = M v^2 / (a/2)
```

so:

```text
v^2 = GM / (2a)
```

Therefore:

```text
rho_local(x) ~ GM / (2 a c^2)
```

For a non-pathological barycentric annular shell that avoids source neighborhoods and special cancellation regions:

```text
rho_shell(S) ~ O(v^2/c^2) ~ O(GM/(2ac^2))
```

Shell choice may change coefficient and spatial pattern but should not change the leading PN order unless the shell is pathological or symmetry-suppressed.

## Scratch Finding

C5-B1 shell/local witness survives as a dynamic Weyl diagnostic.

The magnetic-Weyl fraction is:

- not present in the strictly static C5-A branch,
- admitted once orbital motion is declared,
- velocity-gated,
- weak-field suppressed,
- potentially more significant as separation shrinks and orbital speed rises.

## Interpretation Ceiling

This is a readability witness only.

It is not:

- ordinary energy,
- gravitational-wave luminosity,
- radiative flux,
- conservation law,
- prediction,
- certified calculation,
- whole-domain ledger.

## Relation to C5-A

C5-A found that the static electric-only budget is self-budget dominated and does not carry dynamic inspiral accounting.

C5-B1 shell/local witness identifies where the dynamic Weyl fraction first becomes readable under a declared observer frame and datum shell.

Atlas shorthand:
C5-A identified the receipt.
C5-B1 detects the courier's first footprint.

## Required Checks Before Certification

- verify `B ~ (v/c)E` scaling in the declared observer/tetrad frame,
- check magnetic-Weyl convention factors,
- declare shell geometry explicitly before any calculation,
- test whether shell choice changes only coefficients or changes qualitative pattern,
- avoid regions where `E^2` is small or cancellation-dominated,
- compare against PN/tetrad literature before certification,
- do not integrate whole-domain `rho_mag` without separate authorization.

## Current Ruling

C5-B1 shell/local scaling passes as scratch witness estimate.

Finding:
`rho_local` and `rho_shell` scale as `O(v^2/c^2)`, approximately `GM/(2ac^2)` for equal masses separated by `a`.

Claim ceiling:
scratch diagnostic witness only.

## Next Gate

Decision required:

1. Harden C5-B1 shell witness with explicit shell geometry, or
2. advance to C5-B2 Bel-Robinson flux witness passport.

Recommended next action:
Harden C5-B1 shell witness once, then decide whether C5-B2 should open.
