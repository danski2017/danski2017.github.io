---
type: scratch_hand_derivation
status: diagnostic_no_go_candidate
created: 2026-05-14
candidate: C5-A
claim_status: scratch hand derivation / diagnostic no-go candidate / no calculation certified
repo_execution_authorized: false
topics:
  - c5-a
  - scratch-derivation
  - electric-weyl
  - diagnostic-no-go
  - frontier-evidence
---

# C5-A Scratch Hand Derivation v0.1

## Claim Status

Scratch hand derivation / diagnostic no-go candidate / no calculation certified.

This note is not certified evidence, not a repo calculation, not a radiative result, not a conservation claim, and not a prediction.

## Source Links

- [[C5-A Analytic Calculation Passport]]
- [[C5 Branch Split Work Order]]
- [[C5 Bel-Robinson Comparison Gate v0.1]]
- [[../Frontier Evidence Rule|Frontier Evidence Rule]]
- [[../../Best Practices/Claim Boundary Checklist|Claim Boundary Checklist]]

## Scene Lock

Two equal compact nonspinning masses `M`.

Separation `a`.

Exclusion/source radius `R` with `a > 2R`.

Weak-field instantaneous electric-Weyl/tidal tensor only.

Domain `D = R^3` minus two exclusion balls of radius `R`.

No radiation, no magnetic Weyl, no GW luminosity, no conservation claim.

## Ledger Object

```text
B_E,total(a) = integral_D E_total:E_total dV
E_total = E_1 + E_2
E_total:E_total = E_1:E_1 + E_2:E_2 + 2 E_1:E_2
```

For one weak-field point source outside finite radius:

```text
E_ij = GM/r^3 (3 n_i n_j - delta_ij)
E:E = 6 G^2 M^2 / r^6
```

Single-source exterior budget:

```text
B_E,single(M,R) = 8 pi G^2 M^2 / R^3
```

## Scratch Derivation Summary

Naive self-budget baseline:

```text
2 B_E,single = 16 pi G^2 M^2 / R^3
```

Cross/interference term:

```text
I_12 = integral_D E_1:E_2 dV
```

Scratch result:

```text
Under spherical exclusions, the leading cross/interference term appears to cancel:
I_12 approximately 0
```

Reason:

In the vacuum region each potential is harmonic away from its own source. The Hessian-cross integral can be reduced by integration by parts to boundary terms around exclusion spheres and infinity. The infinity term vanishes. Around spherical exclusions, angular averages cancel because the companion tidal tensor is harmonic and trace-free under the declared symmetry.

Remaining separation dependence:

The leading separation-sensitive term appears as an exclusion/domain correction, not as a clean interaction ledger.

Approximate missing self-field from source 1 inside the exclusion ball around source 2:

```text
integral_ball E_1:E_1 dV approximately (6 G^2 M^2 / a^6)(4 pi R^3 / 3)
= 8 pi G^2 M^2 R^3 / a^6
```

Two symmetric missing pieces:

```text
Delta B_E(a) approximately -16 pi G^2 M^2 R^3 / a^6
plus higher exclusion-geometry corrections.
```

Provisional leading structure:

```text
B_E,total(a;M,R) approximately 16 pi G^2 M^2 / R^3 - 16 pi G^2 M^2 R^3 / a^6 + higher corrections.
```

## Interpretation Ceiling

This is a finite-domain electric-Weyl diagnostic ledger result only.

It is not radiative.

It is not energy.

It is not conserved flux.

It is not a gravitational-wave luminosity relation.

## Provisional Finding

Static electric-Weyl `B_E(a)` branch is self-budget dominated.

Cross/interference term appears to cancel under declared spherical exclusions.

Leading separation dependence appears cutoff/domain-suppressed, scaling approximately as `-R^3/a^6`.

## Frontier Evidence Rule Handling

This is not a failed seam to delete.

It is a diagnostic no-go candidate that demotes C5-A and routes live dynamic accounting toward C5-B, the Bel-Robinson / radiative-Weyl branch.

The required response is not dismissal.

The required response is escalation of rigor.

## Required Checks Before Certification

- Verify cross-term cancellation rigorously.
- Check exclusion-boundary dependence.
- Check whether nonspherical exclusions change the result.
- Check finite outer-radius `L` branch only if needed.
- Compare against direct symbolic or numerical integration.
- Confirm dimensional scaling.
- Confirm no hidden radiative interpretation was introduced.

## Current Ruling

C5-A is demoted to diagnostic witness / no-go candidate.

C5-B remains the live dynamic handoff gate.
