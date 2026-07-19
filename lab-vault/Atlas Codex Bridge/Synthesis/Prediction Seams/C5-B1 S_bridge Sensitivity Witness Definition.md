---
type: sensitivity_witness_definition
status: scratch_theory
created: 2026-05-15
candidate: C5-B1
claim_status: sensitivity witness definition / scratch theory / no calculation certified
repo_execution_authorized: false
whole_domain_integration_authorized: false
topics:
  - c5-b1
  - s-bridge
  - sensitivity-witness
  - magnetic-weyl
  - claim-boundary
---

# C5-B1 S_bridge Sensitivity Witness Definition

## Claim Status

Sensitivity witness definition / scratch theory / no calculation certified.

This note is not certified evidence, not a calculation, not a conservation claim, not ordinary-energy accounting, not radiative balance, and not a prediction.

## Purpose

Define `S_bridge` as a single parked sensitivity witness for C5-B1 before opening C5-B2. `S_bridge` tests whether the magnetic-Weyl fraction is especially readable in the inter-source handoff region, compared with the broader `S_mid` shell.

## Source Links

- [[C5-B1 S_mid Shell Scaling Sensitivity Estimate v0.1]]
- [[C5-B1 Shell Geometry Hardening Gate]]
- [[C5-B1 Shell Local Magnetic Fraction Witness]]
- [[C5-B1 Magnetic Fraction Diagnostic Passport]]
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

No wave-zone flux.

No ordinary-energy comparison.

No radiative-balance claim.

## Prior Witness: S_mid

`S_mid` is the default barycentric annular shell:

- center: barycenter
- `r_inner = a/4`
- `r_outer = 3a/2`
- exclude balls of radius `R_excl` around each mass
- `R_excl << a`

Scratch scaling:

```text
rho_shell(S_mid) ~ O(v^2/c^2) ~ O(GM/(2ac^2))
```

## New Parked Sensitivity Witness: S_bridge

Define `S_bridge` as an inter-source bridge-region datum.

Suggested first-pass definition:

- coordinate frame: barycentric Cartesian
- masses placed on x-axis at `x = -a/2` and `x = +a/2`
- bridge axis: x-axis segment between sources
- longitudinal range: `-a/2 + R_excl < x < +a/2 - R_excl`
- transverse radius: `sqrt(y^2 + z^2) < eta a`
- recommended eta: `eta = 1/4` for first pass
- exclude all points within `R_excl` of either source
- require `R_excl << a`

`S_bridge` is a datum volume, not a physical tube, membrane, shell, or source.

## Witness Definition

```text
rho_shell(S_bridge) =
integral_S_bridge B_ij B^ij dV / integral_S_bridge E_ij E^ij dV
```

Optional local witness inside `S_bridge`:

```text
rho_local(x) = B_ij B^ij / E_ij E^ij
```

## Expected Scaling

Expected leading order:

```text
rho_shell(S_bridge) ~ O(v^2/c^2)
```

For equal masses:

```text
v^2 = GM/(2a)
```

so:

```text
rho_shell(S_bridge) ~ O(GM/(2ac^2))
```

`S_bridge` may alter coefficients and spatial pattern relative to `S_mid`. It should not change leading PN order unless bridge-region symmetry, cancellation, or denominator instability dominates.

## Why S_bridge Matters

`S_mid` tests a broad near-zone magnetic fraction.
`S_bridge` tests whether the dynamic Weyl readability signal concentrates in the inter-source handoff region.

Atlas question:
Is the courier footprint merely global weak-motion structure, or is it geometrically concentrated near the source-source handoff corridor?

## Hazards

- bridge tube radius `eta` is a datum knob,
- inter-source electric-Weyl structure may include cancellation/saddle behavior,
- denominator `E^2` may become small or pattern-dominated in parts of the bridge,
- source exclusion geometry may affect coefficients,
- `S_bridge` is observer/frame-dependent,
- no flux interpretation,
- no physical boundary interpretation.

## Allowed Future Use

`S_bridge` may be used as one sensitivity comparison against `S_mid`.

Allowed:

- scaling/order-counting estimate,
- qualitative comparison of expected coefficient/pattern,
- local witness map concept.

Not allowed:

- coefficient certification,
- whole-domain integration,
- ordinary-energy comparison,
- radiative-flux claim,
- conservation claim,
- prediction claim,
- repo execution.

## Current Ruling

`S_bridge` is parked as the preferred C5-B1 sensitivity witness.

Do not calculate `S_bridge` unless GPT-wing explicitly authorizes it.

## Next Gate

OBS_026:
C5-B1 closeout summary, preserving `S_mid` result and `S_bridge` parked witness, then opening C5-B2 flux witness passport.
