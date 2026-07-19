---
type: baseline_excess_definition_gate
status: scratch_theory
created: 2026-05-15
candidate: C5-B1
claim_status: baseline/excess definition gate / scratch theory / no calculation certified
repo_execution_authorized: false
topics:
  - c5-b1
  - baseline-excess
  - magnetic-weyl
  - bel-robinson
  - claim-boundary
---

# C5-B1 Baseline Excess Definition Gate

## Claim Status

Baseline/excess definition gate / scratch theory / no calculation certified.

This note is not certified evidence, not a calculation, not a conservation claim, not ordinary-energy accounting, and not a prediction.

## Purpose

Define what C5-B1 is allowed to measure before any integration is attempted. The goal is to prevent the Bel-Robinson / magnetic-Weyl branch from inheriting the self-budget and cutoff-dominance trap found in C5-A.

## Source Links

- [[C5-B1 Scratch Scaling Estimate v0.1]]
- [[C5-B1 Analytic Calculation Passport]]
- [[C5-A Scratch Hand Derivation v0.1]]
- [[C5-B Observer Tetrad Declaration Passport]]
- [[../Frontier Evidence Rule|Frontier Evidence Rule]]
- [[../../Best Practices/Claim Boundary Checklist|Claim Boundary Checklist]]

## Problem Carried Forward

C5-A showed that a raw integrated electric-only budget is self-budget dominated. The static `E^2` branch did not produce a clean dynamic handoff ledger.

C5-B1 found that magnetic Weyl enters as a velocity-suppressed dynamic witness, with `B^2/E^2 ~ O(v^2/c^2)`.

Before integrating `B^2` or `E^2+B^2`, C5-B1 must declare its baseline and excess grammar.

## Candidate Measurement Grammars

### Grammar A: Local ratio witness

```text
rho_local(x) = B^2(x) / E^2(x)
```

Purpose:
Measure local dynamic Weyl fraction without integrating cutoff-dominated self terms.

Pros:
Avoids some volume cutoff dominance.
Good for map/witness structure.
Can identify where magnetic Weyl is dynamically relevant.

Cons:
Observer-dependent.
Can become unstable where `E^2` is small.
Not an integrated ledger.

Claim ceiling:
local diagnostic witness.

### Grammar B: Integrated magnetic ledger

```text
S_B = integral_domain B^2 dV
```

Purpose:
Measure total magnetic-Weyl superenergy-like content in declared near-zone domain.

Pros:
Directly measures the missing C5-A channel.
May be less self-dominated than `E^2` depending on motion/source model.

Cons:
May still be cutoff/domain dominated.
Requires moving-source baseline.
Not radiative flux.

Claim ceiling:
finite-domain magnetic witness.

### Grammar C: Full Bel-Robinson excess

```text
Delta_BR = integral_domain (E^2+B^2)_binary dV - baseline
```

Purpose:
Measure total superenergy-like excess relative to a declared isolated/self baseline.

Pros:
Closest to integrated curvature-custody ledger.

Cons:
Baseline is hard.
Boosted isolated-body subtraction may be subtle.
Risk of subtractive artifact.

Claim ceiling:
candidate excess ledger only.

### Grammar D: Magnetic fraction ratio

```text
rho_mag = integral_domain B^2 dV / integral_domain E^2 dV
```

Purpose:
Measure global dynamic Weyl fraction.

Pros:
Dimensionless.
Good first scaling diagnostic.
Compatible with scratch estimate `B^2/E^2 ~ v^2/c^2`.

Cons:
Still depends on domain and baseline.
May be dominated by source neighborhoods.
Not a flux.

Claim ceiling:
dimensionless diagnostic ratio.

### Grammar E: Shell or annular witness

Integrate or average `E^2` and `B^2` only over declared shells excluding near-source cutoff zones.

Purpose:
Reduce source self-dominance and inspect separation/matching structure.

Pros:
May expose dynamic handoff geometry better than whole-domain integrals.
Useful bridge toward wave-zone matching.

Cons:
Shell choice is a datum choice and must not be treated as physical boundary.
Requires careful declaration.

Claim ceiling:
datum-shell witness.

## Required Decision Before Calculation

Choose one first branch:

A. local ratio witness,
B. integrated magnetic ledger,
C. full Bel-Robinson excess,
D. magnetic fraction ratio,
E. shell/annular witness.

## Recommended First Branch

Default recommendation:
D first: magnetic fraction ratio, plus A as local witness if needed.

Reason:
D directly tests the scratch scaling `B^2/E^2 ~ v^2/c^2` while avoiding premature claims about total superenergy conservation or radiative flux. A can support spatial diagnosis without treating the whole-domain integral as a physical boundary.

## Required Declarations For Any Branch

- observer/tetrad convention,
- domain or shell datum,
- source exclusion/worldtube rule,
- isolated moving-body baseline if subtracting,
- whether result is local, integrated, excess, or ratio,
- claim ceiling,
- no ordinary-energy interpretation.

## Failure Gates

- self-budget dominance,
- cutoff sensitivity,
- moving-source baseline ambiguity,
- observer/tetrad ambiguity,
- shell datum overinterpretation,
- accidental radiative-flux language,
- treating ratio as invariant.

## Current Ruling

C5-B1 should not proceed to raw full-domain integration yet.

Preferred next analytic target:

```text
rho_mag = integral B^2 dV / integral E^2 dV
```

as a dimensionless magnetic fraction diagnostic, with local ratio witness as optional support.

## Next Proposed Gate

OBS_018:
C5-B1 magnetic fraction diagnostic passport.
