---
type: magnetic_fraction_diagnostic_passport
status: scratch_theory
created: 2026-05-15
candidate: C5-B1
claim_status: magnetic fraction diagnostic passport / scratch theory / no calculation certified
repo_execution_authorized: false
calculation_authorized: false
topics:
  - c5-b1
  - magnetic-fraction
  - bel-robinson
  - diagnostic-passport
  - claim-boundary
---

# C5-B1 Magnetic Fraction Diagnostic Passport

## Claim Status

Magnetic fraction diagnostic passport / scratch theory / no calculation certified.

This note is not certified evidence, not a calculation, not a conservation claim, not ordinary-energy accounting, not radiative balance, and not a prediction.

## Purpose

Define the first C5-B1 diagnostic object after baseline/excess review: a dimensionless magnetic-Weyl fraction witness for the near-zone Bel-Robinson / Weyl-superenergy branch.

## Source Links

- [[C5-B1 Baseline Excess Definition Gate]]
- [[C5-B1 Scratch Scaling Estimate v0.1]]
- [[C5-B1 Analytic Calculation Passport]]
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

Near-zone domain with source interiors/worldtubes excluded.

No wave-zone flux, no ordinary-energy comparison.

## Diagnostic Objects

Primary diagnostic:

```text
rho_mag = integral_D B_ij B^ij dV / integral_D E_ij E^ij dV
```

where `D` is a declared near-zone domain excluding source interiors/worldtubes.

Optional local witness:

```text
rho_local(x) = B_ij(x) B^ij(x) / E_ij(x) E^ij(x)
```

## Role

`rho_mag` measures the dimensionless magnetic-Weyl fraction of the near-zone curvature-square witness.

`rho_local` maps where the dynamic Weyl fraction is locally significant.

Neither object is ordinary energy, gravitational-wave luminosity, radiative flux, or conservation law.

## Expected Scaling

From scratch order-counting:

```text
B ~ (v/c) E
```

so:

```text
rho_local ~ B^2/E^2 ~ v^2/c^2
```

For equal masses with separation `a`:

```text
v^2 = GM/(2a)
```

so expected leading scaling:

```text
rho_mag ~ O(GM/(2ac^2))
```

subject to domain, baseline, and convention factors.

## Required Declarations Before Calculation

- exact near-zone domain `D` or shell datum,
- source exclusion/worldtube radius `R`,
- whether denominator uses total `E^2` or baseline-subtracted `E^2`,
- whether numerator includes self magnetic terms, orbital magnetic terms, or both,
- whether `rho_mag` is whole-domain, shell-averaged, or source-exclusion limited,
- whether local ratio is used only as witness map,
- claim ceiling.

## Hazards

- denominator dominated by `E^2` self-budget near sources,
- numerator may also have cutoff dependence,
- ratio may hide rather than solve cutoff dominance,
- local ratio may blow up where `E^2` is small,
- observer/tetrad dependence,
- magnetic Weyl convention factors,
- accidental radiative interpretation.

## Recommended First Calculation Type

Scaling/order-counting only.

Do not integrate yet unless GPT-wing explicitly authorizes it after passport review.

First calculation should classify:

- expected PN order of `rho_mag`,
- whether whole-domain ratio is likely cutoff dominated,
- whether shell/local witness is safer,
- whether `rho_mag` can serve as the first dynamic Weyl fraction witness.

## Result Classifications Allowed

- `rho_mag` scales as `O(v^2/c^2)` and is useful as diagnostic;
- whole-domain `rho_mag` is cutoff dominated but shell/local witness survives;
- numerator or denominator ill-posed without stronger PN/tetrad setup;
- local witness only is recommended;
- branch should defer to C5-B2 flux witness.

No allowed classification is a conservation law, ordinary-energy equivalence, radiative balance, or prediction.

## Next Proposed Gate

OBS_019:
GPT-wing adjudication of magnetic fraction passport and possible authorization of a scaling-only `rho_mag` estimate.

Repo execution remains unauthorized.

## GPT-Wing Adjudication - OBS_019

Ruling:
PASS WITH DOMAIN PATCH.

Authorized:
scaling/order-counting estimate for local or shell-limited magnetic fraction only.

Not authorized:
whole-domain `rho_mag` integration;
baseline-subtracted integrated ratio;
ordinary-energy comparison;
radiative-balance interpretation;
repo execution.

Domain patch:
Whole-domain `rho_mag` is not trusted as the first certified diagnostic because both numerator and denominator may inherit cutoff/self-budget structure. The first allowed diagnostic is local or shell-limited:

```text
rho_local(x) = B_ij B^ij / E_ij E^ij
```

or, if a shell datum is explicitly declared:

```text
rho_shell = shell average or shell integral ratio of B^2 to E^2.
```

Expected scaling:

```text
rho_local ~ O(v^2/c^2)
```

For equal masses separated by `a`:

```text
v^2 = GM/(2a)
```

Therefore:

```text
rho_local ~ O(GM/(2ac^2))
```

Claim ceiling:
scratch local/shell diagnostic scaling only.
not invariant without observer/tetrad declaration.
not ordinary energy.
not flux.
not radiative balance.
not prediction.

Next gate:
OBS_020 = C5-B1 shell/local magnetic fraction witness note.
