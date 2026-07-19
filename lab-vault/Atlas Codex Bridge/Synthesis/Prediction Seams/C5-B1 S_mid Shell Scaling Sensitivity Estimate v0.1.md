---
type: scratch_shell_scaling_sensitivity_estimate
status: dynamic_weyl_readability_witness
created: 2026-05-15
candidate: C5-B1
claim_status: scratch shell scaling/sensitivity estimate / dynamic Weyl readability witness / no calculation certified
repo_execution_authorized: false
whole_domain_integration_authorized: false
topics:
  - c5-b1
  - s-mid
  - shell-scaling
  - magnetic-weyl
  - sensitivity
---

# C5-B1 S_mid Shell Scaling Sensitivity Estimate v0.1

## Claim Status

Scratch shell scaling/sensitivity estimate / dynamic Weyl readability witness / no calculation certified.

This note is not certified evidence, not a repo calculation, not a conservation claim, not ordinary-energy accounting, not radiative balance, and not a prediction.

## Source Links

- [[C5-B1 Shell Geometry Hardening Gate]]
- [[C5-B1 Shell Local Scaling Estimate v0.1]]
- [[C5-B1 Shell Local Magnetic Fraction Witness]]
- [[C5-B1 Magnetic Fraction Diagnostic Passport]]
- [[../Frontier Evidence Rule|Frontier Evidence Rule]]
- [[../../Best Practices/Claim Boundary Checklist|Claim Boundary Checklist]]

## Scene Lock

Weak-field equal-mass circular binary.

Masses: `M` and `M`.

Separation: `a`.

Each mass speed: `v`.

`v^2 = GM/(2a)`.

Observer: Eulerian/static barycentric observer.

Witness: `rho_shell(S_mid)`.

Shell: barycentric annular shell, `r_inner = a/4`, `r_outer = 3a/2`.

Source exclusions: balls of radius `R_excl` around each mass, `R_excl << a`.

No whole-domain integration.

No coefficient certification.

No flux, energy, conservation, or prediction claim.

## Witness Definition

```text
rho_shell(S_mid) = integral_S_mid B_ij B^ij dV / integral_S_mid E_ij E^ij dV
```

`S_mid` is a datum shell, not a physical boundary.

## Scaling Derivation

In weak-field slow-motion order counting:

```text
E ~ GM/r^3
```

Magnetic Weyl from moving sources is velocity-suppressed:

```text
B ~ (v/c) E
```

Therefore:

```text
B^2 ~ (v^2/c^2) E^2
```

Substituting into the shell ratio:

```text
rho_shell(S_mid)
~ integral_S_mid (v^2/c^2) E^2 dV / integral_S_mid E^2 dV
```

If `v/c` is approximately constant for the binary on the instantaneous slice:

```text
rho_shell(S_mid) ~ v^2/c^2
```

For equal masses separated by `a`:

```text
v^2 = GM/(2a)
```

Therefore:

```text
rho_shell(S_mid) ~ GM/(2ac^2)
```

Equivalently, with `M_tot = 2M`:

```text
rho_shell(S_mid) ~ G M_tot/(4ac^2)
```

## Sensitivity Notes

`R_excl`:
If `R_excl << a` and the shell excludes immediate source neighborhoods, `R_excl` should mostly affect coefficients, not leading PN order. If `R_excl` is too small and the shell samples near-source self-budget zones, the denominator may become self-dominated.

`r_inner`:
`r_inner = a/4` keeps the shell away from immediate source neighborhoods while retaining mid-zone structure. Moving inward increases exposure to symmetry/cancellation zones and denominator instability. Moving outward may remove inter-source/mid-zone structure.

`r_outer`:
`r_outer = 3a/2` keeps the shell near-zone and source-pair-associated. Moving much farther outward risks drifting toward parent-context or wave-zone matching. Moving too close inward risks source/exclusion geometry dominance.

## Parked Alternative Shell

Preferred parked comparison: `S_bridge`.

`S_bridge` is a lens/bridge region between the two masses, excluding source neighborhoods.

Purpose:
Test whether the magnetic-Weyl fraction is concentrated in the inter-source handoff region.

Expected scaling:

```text
rho_shell(S_bridge) ~ O(v^2/c^2)
```

`S_bridge` may change coefficient and spatial pattern, but should not change leading PN order unless symmetry or shell choice dominates.

## Scratch Finding

C5-B1 `S_mid` shell witness preserves the dynamic Weyl fraction order:

```text
rho_shell(S_mid) ~ O(v^2/c^2) ~ O(GM/(2ac^2))
```

This confirms a velocity-gated magnetic-Weyl readability signal in the declared shell witness.

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

## Current Ruling

C5-B1 `S_mid` shell scaling passes as scratch witness estimate.

`S_bridge` is the preferred one-shell sensitivity witness before opening C5-B2.

## Next Gate

Recommended:
OBS_025 = C5-B1 `S_bridge` sensitivity witness definition, or stop C5-B1 and open C5-B2 flux witness passport.

GPT-wing recommendation:
Do one `S_bridge` sensitivity witness definition, then open C5-B2.
