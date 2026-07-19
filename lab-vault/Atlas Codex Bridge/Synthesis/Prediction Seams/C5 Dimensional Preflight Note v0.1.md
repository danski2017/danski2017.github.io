---
type: scratch_theory_note
status: dimensional_preflight
created: 2026-05-14
candidate: C5
claim_status: dimensional preflight note / scratch theory / no calculation certified
repo_execution_authorized: false
topics:
  - c5
  - dimensional-preflight
  - weak-field-binary
  - curvature-ledger
  - gravitational-radiation
  - claim-boundary
---

# C5 Dimensional Preflight Note v0.1

## Claim Status

Dimensional preflight note / scratch theory / no calculation certified.

This note is not an experiment, not certified evidence, not a prediction, and not a conservation claim.

## Source Links

- [[C5 Dimensional Preflight Work Order]]
- [[C5 Curvature Ledger Balance in Weak Field Binary Inspiral]]
- [[../Prediction Candidates - Atlas Diagnostic Seams v0.2|Prediction Candidates - Atlas Diagnostic Seams v0.2]]
- [[../Frontier Evidence Rule|Frontier Evidence Rule]]
- [[../../Papers/Three Measures of Gravitational Identity|Three Measures of Gravitational Identity]]
- [[../../Papers/Gravitational Field Relation Operator|Gravitational Field Relation Operator]]
- [[../../Best Practices/Claim Boundary Checklist|Claim Boundary Checklist]]

## 1. Purpose

This note tests whether the candidate curvature-ledger functional can be dimensionally compared to standard gravitational-wave radiative channels.

The purpose is classification only: identify whether a raw comparison is illegal, whether a lawful mediator is required, and which family of mediator is most likely to be relevant before any calculation is run.

## 2. Candidate Ledger Object

Start with:

```text
B_E = integral E_ij E^ij dV
```

where `E_ij` is the weak-field electric-Weyl/tidal tensor.

This object is a curvature-square volume ledger. It is not ordinary energy unless an explicit, lawful conversion is supplied and survives review.

## 3. Dimensional Audit

Use two parallel conventions during preflight:

- Geometrized units with `G = c = 1`, where length and time share dimension `L`.
- SI-like weak-field units, where tidal acceleration gradients carry `T^-2`.

| Object | Geometrized dimensional read | SI-like weak-field read | Preflight implication |
|---|---|---|---|
| `E_ij` | `L^-2` | `T^-2` | Curvature/tidal tensor, not energy. |
| `E_ij E^ij` | `L^-4` | `T^-4` | Curvature square. |
| `dV` | `L^3` | `L^3` | Domain choice matters. |
| `B_E = integral E_ij E^ij dV` | `L^-1` | `L^3 T^-4` | Finite only after domain/cutoff declaration. |
| `dB_E/dt` | `L^-2` | `L^3 T^-5` | Not directly a power. |
| `P_GW` | dimensionless in geometrized units as energy/time, `L/L`; SI `M L^2 T^-3` | `M L^2 T^-3` | Ordinary energy flux/power channel. |
| Bondi mass loss `dM_B/du` | dimensionless in geometrized units, `L/L` | power after `c^2` conversion | Standard radiative energy-loss channel, not raw curvature-square change. |
| Isaacson effective stress-energy | `L^-2` | energy density or flux after `c^4/G` factors | Mediates wave energy in high-frequency/averaged limit; gauge/averaging conditions matter. |
| News tensor | commonly `L^-1` if retarded time has length | `T^-1` | News squared is closer to a radiative flux density channel after angular/factor conventions. |
| `Psi_4` | `L^-2` | `T^-2` | Radiative Weyl curvature scalar; closer in kind to curvature than to power. |
| Bel-Robinson superenergy density or flux | `L^-4` before observer/vector contractions and integrations | curvature-square-like, not ordinary energy density without conversion | Natural curvature-square comparison family, but not automatically ordinary energy. |

Clarification: geometrized-unit dimensionlessness of `P_GW` and Bondi `dM_B/du` does not establish commensurability with curvature-square ledgers. It only reflects the collapsed length/time/mass bookkeeping after `G = c = 1`; the physical channel and mediator still have to be declared.

Clarification: Bel-Robinson density or flux interpretations require observer/tetrad and hypersurface choices. A superenergy-family comparison is closer in dimensional kind to curvature-square bookkeeping, but it is not observer-free by default and is not automatically an ordinary-energy flux.

Immediate dimensional read:

```text
dB_E/dt has curvature-square-volume-per-time dimensions.
P_GW has ordinary energy-per-time dimensions.
They are not directly commensurate.
```

## 4. Immediate Classification

`dB_E/dt` and `P_GW` are not directly commensurate at the raw dimensional level.

Any comparison needs explicit mediation. Possible mediation families:

- mass/length/time normalization,
- geometrized-unit conversion with all `G` and `c` factors restored,
- superenergy comparison,
- curvature flux comparison,
- dimensionless diagnostic ratio.

The raw object cannot be read as gravitational-wave luminosity and cannot be used to claim energy conservation.

Geometrized-unit bookkeeping does not remove this boundary. A dimensionless power channel and a curvature-square ledger can both look compact in `G = c = 1` units while still belonging to different comparison families.

## 5. Domain and Cutoff Issue

The integral

```text
integral E_ij E^ij dV
```

is domain-sensitive.

For compact masses, the near-source/self-field region can diverge or dominate unless the domain is declared. Equal compact masses require either:

- declared finite source radius `R` for each body, or
- exclusion spheres around each compact object, plus a rule for how those exclusions evolve with separation.

The preflight cannot treat two point masses as a finite ledger without a cutoff, source radius, worldtube boundary, or other regularization rule.

## 6. Near-Zone / Wave-Zone Separation

The candidate `B_E` ledger is naturally a near-zone or finite-domain curvature ledger unless otherwise declared.

Gravitational-wave luminosity is a wave-zone/asymptotic flux concept. Bondi mass loss, News tensor flux, and `Psi_4` radiation extraction live in an asymptotic or wave-zone comparison channel.

Therefore:

- near-zone curvature-square change is not automatically wave-zone radiation flux,
- finite-domain ledger change is not automatically Bondi mass loss,
- any comparison must state the matching surface, extraction domain, averaging rule, and gauge-invariant radiative quantity.

## 7. Candidate Comparison Paths

Lawful comparison paths for future work:

A. Curvature-square ledger vs curvature-square radiative flux

Compare `E_ij E^ij`-type finite-domain behavior to a radiative Weyl-square or `Psi_4`-based channel after domain and normalization are declared.

B. Bel-Robinson-like superenergy object vs radiative Weyl channel

Use a Bel-Robinson family object as the closest same-family mediator because it is built from curvature squared. This remains superenergy-like, not ordinary energy, unless a further conversion is justified.

C. Dimensionless normalized diagnostic ratio

Construct a ratio such as normalized `dB_E/dt` against a declared curvature/radiative scale. This can be useful diagnostically without claiming equality with luminosity.

D. Ordinary energy flux comparison only after explicit conversion or rejection

Attempt comparison to `P_GW`, Bondi mass loss, or Isaacson flux only after restoring dimensions and declaring the conversion. If no lawful conversion exists, reject the ordinary-energy comparison.

## 8. Preliminary Outcome

Preliminary classification:

```text
Bel-Robinson family likely comparison target.
```

Supporting read:

Raw identity between `dB_E/dt` and `P_GW` is impossible at the immediate dimensional level. A clean proportionality is possible only after mediation, and the most natural mediation family is curvature-square/superenergy rather than ordinary power. Any structured residual is not claimable at this preflight stage.

## 9. Next Required Step

Recommendation:

```text
pursue Bel-Robinson comparison first
```

Before deriving `B_E(a)`, write a short comparison map that places the finite-domain electric-Weyl square ledger beside:

- Bel-Robinson superenergy density/flux,
- `Psi_4` or radiative Weyl curvature,
- News tensor flux,
- Isaacson effective stress-energy,
- Bondi mass loss.

That map should decide whether `B_E(a)` is worth deriving as a diagnostic ledger or whether the ledger functional should be revised before calculation.

## 10. Claim Discipline

No conservation claim.

No radiative equivalence claim.

No gauge-invariant residual claim.

No prediction claim.

Additional non-claims:

- No certified calculation.
- No experiment evidence.
- No ordinary-energy interpretation of curvature-square budget.
- No direct `B_E` to gravitational-wave luminosity comparison.
- No completed C5 result.
