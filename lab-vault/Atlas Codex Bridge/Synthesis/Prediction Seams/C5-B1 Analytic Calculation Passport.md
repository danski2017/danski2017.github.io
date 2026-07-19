---
type: analytic_calculation_passport
status: scratch_theory
created: 2026-05-14
candidate: C5-B1
claim_status: analytic calculation passport / scratch theory / no calculation certified
repo_execution_authorized: false
formula_derivation_authorized: false
topics:
  - c5-b1
  - bel-robinson
  - analytic-passport
  - near-zone
  - superenergy
---

# C5-B1 Analytic Calculation Passport

## Claim Status

Analytic calculation passport / scratch theory / no calculation certified.

This note is not certified evidence, not a formula derivation, not a conservation claim, not ordinary-energy accounting, and not a prediction.

## Purpose

Define the first analytic calculation for C5-B1: a near-zone Bel-Robinson / Weyl-superenergy density witness for a weak-field equal-mass circular binary, under the declared observer/tetrad convention.

## Source Links

- [[C5-B Observer Tetrad Declaration Passport]]
- [[C5-B Bel-Robinson Literature Theory Map v0.1]]
- [[C5-B Bel-Robinson Superenergy Gate v0.1]]
- [[C5-A Scratch Hand Derivation v0.1]]
- [[../Frontier Evidence Rule|Frontier Evidence Rule]]
- [[../../Best Practices/Claim Boundary Checklist|Claim Boundary Checklist]]

## Scene Declaration

Scene ID:
`C5B1_weak_field_binary_bel_robinson_density_v0_1`

Scene title:
C5-B1 near-zone Weyl-superenergy density witness for weak-field equal-mass binary

Regime:
weak-field / post-Newtonian-ready / pre-merger / no near-merger claim

Sources:
two compact nonspinning equal masses `M`

Separation:
`a`

Motion:
circular orbit, but first calculation may use instantaneous orbital state with velocity `v` declared

Coordinates:
barycentric Cartesian

Observer:
Eulerian/static barycentric observer

Tetrad:
orthonormal frame adapted to weak-field barycentric coordinates

Hypersurface:
constant coordinate time slice

Domain:
near-zone finite domain excluding source interiors/worldtubes

Node 1:
asymptotically flat parent context with wave-zone comparison channel held pending

## Candidate Witness Object

Schematic Bel-Robinson density witness:

```text
U_BR ~ E_ij E^ij + B_ij B^ij
```

where:

```text
E_ij = electric Weyl / tidal tensor relative to declared observer
B_ij = magnetic Weyl relative to declared observer
```

This is superenergy-like curvature-square structure, not ordinary energy density.

## Required Decomposition

The eventual calculation must separate:

1. electric-only component:
   `E^2 = E_ij E^ij`
2. magnetic component:
   `B^2 = B_ij B^ij`
3. possible cross or coupling structure if the chosen convention includes it
4. source self contributions
5. interaction/excess contribution relative to isolated boosted/translated bodies if definable
6. velocity/order counting:
   quasi-static `E` terms;
   velocity-dependent `B` terms;
   radiative-order terms, if deferred

## Candidate Calculands

Define but do not derive:

A. `U_BR,total(x; M,a,v,R)`
local density witness

B. `S_BR,total(M,a,v,R,L)`
integrated near-zone superenergy-like ledger, if finite:

```text
S_BR = integral_domain (E^2 + B^2) dV
```

C. Magnetic excess:

```text
Delta_B = integral_domain B^2 dV
```

or a better-declared magnetic witness

D. Full superenergy excess:

```text
Delta_BR = S_BR,total - isolated/self baseline
```

E. Ratio diagnostic:

```text
rho_mag = integral B^2 dV / integral E^2 dV
```

or declared alternative

## Required Dimensional Checks

Track dimensions of:

- `E_ij`
- `B_ij`
- `E^2`
- `B^2`
- `U_BR`
- `dV`
- integrated `S_BR`
- velocity `v`
- orbital frequency `Omega`
- `v/c` or PN order

State explicitly:

`S_BR` is not ordinary energy.

`dS_BR/dt` is not luminosity.

No direct comparison to `P_GW` is authorized.

## Expected Mathematical Hazards

- `B_ij` vanishes in strictly static Newtonian limit, so motion/order counting matters.
- Magnetic Weyl may depend on velocity, slicing, and observer convention.
- Integrated `E^2` remains self-budget dominated unless an excess/renormalized branch is declared.
- `B^2` may be cutoff/domain sensitive.
- Near-zone `B^2` is not automatically radiative flux.
- Observer-relative density cannot be promoted as invariant.
- Isolated boosted-body baseline must be declared carefully if using excess.

## Result Classification Allowed

Future calculation may produce:

- magnetic component negligible at chosen order,
- magnetic component gives a clean velocity-dependent diagnostic,
- `E^2+B^2` remains self-budget dominated,
- excess branch is meaningful only after baseline subtraction,
- object is ill-posed without a more rigorous PN/tetrad setup,
- useful dimensionless ratio only.

No allowed classification is a conservation law, wave-flux identity, ordinary-energy equivalence, or prediction.

## Recommendation

Recommend whether GPT-wing should perform the first hand analytic estimate in chat.

Default recommendation:

```text
Yes, but only at scaling/order-counting level first:
estimate how B^2 scales relative to E^2 in weak-field circular motion, before attempting full integration.
```

## Next Proposed Gate

OBS_016:
GPT-wing adjudication of C5-B1 passport and possible authorization of scaling/order-counting derivation.

Formula derivation is not automatically authorized by Codex.

Repo execution remains unauthorized.
