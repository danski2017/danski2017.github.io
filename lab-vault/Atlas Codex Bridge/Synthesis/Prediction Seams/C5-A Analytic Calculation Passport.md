---
type: analytic_calculation_passport
status: scratch_theory
created: 2026-05-14
candidate: C5-A
scene_id: C5A_weak_field_equal_mass_binary_BE_diagnostic_v0_1
claim_status: analytic calculation passport / scratch theory / no calculation certified
formula_derivation_authorized: false
repo_execution_authorized: false
topics:
  - c5-a
  - analytic-passport
  - electric-weyl
  - weak-field-binary
  - claim-boundary
---

# C5-A Analytic Calculation Passport

## Claim Status

Analytic calculation passport / scratch theory / no calculation certified.

This is not an experiment note, not certified evidence, not a formula derivation, not a conservation claim, and not a radiative-balance claim.

## Source Links

- [[C5 Branch Split Work Order]]
- [[C5 Bel-Robinson Comparison Gate v0.1]]
- [[C5 Dimensional Preflight Note v0.1]]
- [[../Frontier Evidence Rule|Frontier Evidence Rule]]
- [[../../Best Practices/Claim Boundary Checklist|Claim Boundary Checklist]]
- [[../../Templates/Experiment Note Template|Experiment Note Template]]
- [[../../Templates/Simulation Run Template|Simulation Run Template]]

## 1. Passport Header

| Field | Declaration |
|---|---|
| Scene ID | `C5A_weak_field_equal_mass_binary_BE_diagnostic_v0_1` |
| Scene title | C5-A finite-domain electric-Weyl budget diagnostic for weak-field equal-mass binary |
| Mode | theory preflight |
| Lane | private method / prediction seam |
| Claim status | scratch theory / no calculation certified |
| Primary purpose | define the analytic calculation for `B_E(a)` as a finite-domain near-zone diagnostic ledger |
| Do not claim | radiative balance, GW luminosity equivalence, conservation law, gauge-invariant residual, observational prediction |

## 2. Scene Declaration

| Field | Declaration |
|---|---|
| Regime | weak-field Newtonian / electric-Weyl tidal approximation |
| Sources | two compact nonspinning equal masses `M` |
| Separation | circular binary separation `a`, fixed instant |
| Source radius/exclusion radius | `R`, with `R << a` |
| Coordinates | barycentric Cartesian, masses at `x = +/- a/2` |
| Node 1 | asymptotically flat parent / null exterior comparison context |
| Domain | `R^3` minus two exclusion spheres, or a declared finite outer radius `L` if needed |
| Time status | instantaneous slice, quasi-static diagnostic, not wave-zone radiation |

This scene is a near-zone diagnostic scene. It does not include magnetic Weyl, radiative extraction, News, `Psi_4`, Isaacson stress-energy, or Bondi mass loss.

## 3. Ledger Object

Candidate ledger:

```text
B_E(a) = integral_domain E_ij E^ij dV
```

where `E_ij` is the total weak-field electric tidal tensor from both masses.

Required decomposition:

- self terms,
- cross terms,
- optional interaction budget,
- optional subtractive excess relative to isolated bodies.

The decomposition must decide whether the branch is reporting total finite-domain content, interaction/excess content, or both.

## 4. Candidate Calculands

Define but do not derive:

A. Total finite-domain ledger:

```text
B_E,total(a; M, R, L)
```

B. Isolated-body baseline:

```text
2 B_E,single(M, R)
```

C. Interaction/excess ledger, if finite and well-declared:

```text
Delta B_E(a) = B_E,total - 2 B_E,single
```

D. Cutoff sensitivity with respect to `R` and `L`.

E. Large-separation asymptotic scaling of `Delta B_E(a)`.

No formula is derived in this passport.

## 5. Required Dimensional Checks

Track dimensions of:

- `E_ij`,
- `E_ij E^ij`,
- `dV`,
- `B_E`,
- `Delta B_E`,
- `dB_E/da` if later used,
- `dB_E/dt` if later combined with `da/dt`.

None of these are ordinary energy without mediation.

`dB_E/dt`, if later formed, is not gravitational-wave luminosity and is not radiative balance unless a separate, lawful comparison channel is declared and adjudicated.

## 6. Expected Mathematical Hazards

- self-field divergence near each mass,
- cross-term integral may depend on exclusion geometry,
- outer-domain convergence must be checked,
- point-mass idealization may dominate result with cutoff terms,
- coordinate/slicing assumptions are Newtonian weak-field only,
- no magnetic-Weyl/radiative channel included.

If cutoff terms dominate, the output should say so directly. If the interaction/excess definition is the only meaningful branch, the total-ledger branch should not be overread.

## 7. Result Classification Allowed

The eventual calculation may produce:

- finite interaction ledger with clear `a`-scaling,
- cutoff-dominated result requiring renormalized/excess definition,
- zero or negligible cross-term after domain subtraction,
- divergent/ill-posed object requiring reformulation,
- useful diagnostic ratio only.

No allowed classification is a conservation law, wave-flux identity, GW luminosity equivalence, or observational prediction.

## 8. Recommendation

Recommendation:

```text
yes, GPT-wing should derive the leading structure by hand first, because this is a doctrine-sensitive object.
```

The first hand derivation should remain in chat or a written scratch-theory note until adjudicated. Codex/repo calculation should not begin from this passport.

## 9. Next Proposed Packet

```text
OBS_008 = GPT-wing or Codex export of passport for adjudication.
```

No repo execution authorized.

Formula derivation is not automatically authorized by Codex. It requires GPT-wing adjudication after passport review.

## Frontier Evidence Rule Note

If C5-A yields a no-go or cutoff-dominated result, the result should be preserved as a diagnostic witness rather than deleted or overread. The proper response is branch demotion and routing to the richer C5-B channel, not dismissal of the whole seam.

## Non-Claims

- No calculation certified.
- No formula derived.
- No experiment evidence.
- No radiative balance claim.
- No conservation claim.
- No gauge-invariant residual claim.
- No observational prediction.
- No repo execution authorized.
