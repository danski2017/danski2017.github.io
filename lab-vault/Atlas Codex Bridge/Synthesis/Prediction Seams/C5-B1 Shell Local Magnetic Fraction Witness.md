---
type: shell_local_witness_definition
status: scratch_theory
created: 2026-05-15
candidate: C5-B1
claim_status: shell/local witness definition / scratch theory / no calculation certified
repo_execution_authorized: false
whole_domain_integration_authorized: false
topics:
  - c5-b1
  - shell-local-witness
  - magnetic-fraction
  - bel-robinson
  - claim-boundary
---

# C5-B1 Shell Local Magnetic Fraction Witness

## Claim Status

Shell/local witness definition / scratch theory / no calculation certified.

This note is not certified evidence, not a calculation, not a conservation claim, not ordinary-energy accounting, not radiative balance, and not a prediction.

## Purpose

Define the first safe C5-B1 diagnostic after OBS_019: a local or shell-limited magnetic-Weyl fraction witness that avoids premature whole-domain integration and cutoff-dominated self-budget artifacts.

## Source Links

- [[C5-B1 Magnetic Fraction Diagnostic Passport]]
- [[C5-B1 Baseline Excess Definition Gate]]
- [[C5-B1 Scratch Scaling Estimate v0.1]]
- [[C5-B Observer Tetrad Declaration Passport]]
- [[../Frontier Evidence Rule|Frontier Evidence Rule]]
- [[../../Best Practices/Claim Boundary Checklist|Claim Boundary Checklist]]

## Scene Lock

Weak-field equal-mass circular binary.

Masses: `M` and `M`.

Separation: `a`.

Each mass orbits barycenter with speed `v`.

Observer: Eulerian/static barycentric observer.

Tetrad: orthonormal frame adapted to weak-field barycentric coordinates.

Hypersurface: constant coordinate time slice.

No wave-zone flux.

No ordinary-energy comparison.

No radiative-balance claim.

## Local Witness

Define:

```text
rho_local(x) = B_ij(x) B^ij(x) / E_ij(x) E^ij(x)
```

Role:
local magnetic-Weyl fraction of curvature-square witness.

Expected scaling:
`rho_local(x) ~ O(v^2/c^2)`, where the local geometry and observer convention may change coefficients and spatial pattern.

Hazards:

- `E^2` may become small at special locations.
- observer/tetrad dependence.
- local witness is diagnostic, not invariant truth.
- not a flux.

## Shell-Limited Witness

Define a datum shell or annular region `S`.

Example first shell candidates:

1. barycentric annular shell excluding source neighborhoods,
2. midplane shell between the two masses,
3. spherical shell centered at barycenter with radius comparable to `a`,
4. source-associated shells around each mass outside radius `R` but inside `a/2`.

Shell ratio:

```text
rho_shell(S) = integral_S B^2 dV / integral_S E^2 dV
```

or shell average of `rho_local`, declared explicitly.

Role:
shell-limited magnetic fraction diagnostic.

Expected scaling:
`rho_shell ~ O(v^2/c^2)`, with shell-dependent coefficients.

Hazards:

- shell is a datum, not a physical boundary.
- shell choice may dominate pattern.
- denominator may still be self-field dominated if shell approaches sources.
- not an integrated total ledger.

## First Recommended Shell

Default first shell:
barycentric annular shell excluding source neighborhoods.

Declare:

- inner exclusion: remove balls around each source of radius `R_excl`.
- outer boundary: finite shell radius `L_shell` of order `a` to several `a`.
- optional mid-zone: region outside source neighborhoods and inside one separation scale.

Reason:
This avoids the immediate source cutoff while probing the near-zone dynamic Weyl fraction.

## Allowed Future Calculation

Only scaling/order-counting or symbolic local/shell estimate.

Allowed:

- estimate `rho_local ~ v^2/c^2`,
- estimate `rho_shell` scaling,
- compare shell choices qualitatively,
- identify whether shell/local witness survives cutoff concerns.

Not allowed:

- full whole-domain `rho_mag` integration,
- radiative flux interpretation,
- ordinary-energy comparison,
- conservation claim,
- prediction claim,
- repo execution.

## Result Classifications Allowed

- local/shell witness survives as dynamic Weyl diagnostic,
- shell choice dominates and must be refined,
- local witness only is useful,
- `B^2` remains too convention-dependent for this branch,
- branch should route to C5-B2 flux witness.

## Current Ruling

C5-B1 should proceed, if at all, through local/shell magnetic fraction witness rather than whole-domain `rho_mag`.

Expected leading order:
`rho_local` or `rho_shell ~ O(v^2/c^2) ~ O(GM/(2ac^2))` for equal masses.

## Next Proposed Gate

OBS_021:
GPT-wing adjudication of shell/local witness note and possible authorization of a shell/local scaling derivation.
