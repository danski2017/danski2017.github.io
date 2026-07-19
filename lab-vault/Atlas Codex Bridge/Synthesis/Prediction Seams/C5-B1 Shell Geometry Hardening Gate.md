---
type: shell_geometry_hardening_gate
status: scratch_theory
created: 2026-05-15
candidate: C5-B1
claim_status: shell geometry hardening gate / scratch theory / no calculation certified
repo_execution_authorized: false
topics:
  - c5-b1
  - shell-geometry
  - magnetic-weyl
  - shell-local-witness
  - claim-boundary
---

# C5-B1 Shell Geometry Hardening Gate

## Claim Status

Shell geometry hardening gate / scratch theory / no calculation certified.

This note is not certified evidence, not a calculation, not a conservation claim, not ordinary-energy accounting, not radiative balance, and not a prediction.

## Purpose

Declare the first shell datum for the C5-B1 magnetic-Weyl fraction witness before any calculation or integration is attempted.

The shell is a datum, not a physical boundary.

## Source Links

- [[C5-B1 Shell Local Scaling Estimate v0.1]]
- [[C5-B1 Shell Local Magnetic Fraction Witness]]
- [[C5-B1 Magnetic Fraction Diagnostic Passport]]
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

## Default Shell Datum: Mid-Zone Barycentric Annular Shell

Define a first shell datum `S_mid`:

- center: barycenter
- exclude: balls of radius `R_excl` around each mass
- inner radial bound: `r_inner = a/4` from barycenter, unless it intersects exclusion balls
- outer radial bound: `r_outer = 3a/2`
- optional angular mask: none for first pass
- source exclusion condition: remove all points within `R_excl` of either mass
- required relation: `R_excl << a`

Purpose:
Probe near-zone dynamic Weyl fraction outside immediate source neighborhoods while staying inside a few separation scales.

## Why This Shell

- avoids immediate source cutoff dominance,
- remains near-zone rather than asymptotic wave-zone,
- includes inter-source and surrounding barycentric region,
- gives a declared datum for `rho_shell`,
- does not pretend to be a physical boundary.

## Witness Definitions

Local witness:

```text
rho_local(x) = B_ij B^ij / E_ij E^ij
```

Shell witness:

```text
rho_shell(S_mid) = integral_S_mid B_ij B^ij dV / integral_S_mid E_ij E^ij dV
```

## Expected Scaling

```text
rho_local ~ O(v^2/c^2)
rho_shell(S_mid) ~ O(v^2/c^2)
```

For equal masses:

```text
v^2 = GM/(2a)
```

so:

```text
rho_shell(S_mid) ~ O(GM/(2ac^2))
```

Shell geometry may alter coefficients and spatial patterns, not the expected leading PN order unless symmetry or cancellation dominates.

## Hazards

- `r_inner`/`r_outer` choices are datum choices,
- shell may include electric-Weyl cancellation regions,
- denominator may be small in localized zones,
- exclusion radius `R_excl` may still affect coefficients,
- shell is not invariant,
- observer/tetrad dependence remains,
- no flux interpretation.

## Allowed Future Work

Allowed after GPT-wing adjudication:

- scaling/order-counting estimate for `S_mid`,
- qualitative shell sensitivity check,
- possible comparison to alternative shell `S_alt`.

Not allowed:

- whole-domain `rho_mag`,
- ordinary-energy comparison,
- radiative flux claim,
- conservation claim,
- repo execution.

## Alternative Shells To Park

`S_source`:
source-associated shells around each mass, outside `R_excl` and inside `a/2`.

`S_bridge`:
lens/bridge region between the two masses excluding source neighborhoods.

`S_outer`:
barycentric shell from `a` to several `a`, still near-zone if declared.

These are parked and not active until explicitly authorized.

## Current Ruling

C5-B1 should harden `S_mid` as the first shell datum.

## Next Gate

OBS_023:
GPT-wing adjudication of shell geometry hardening and possible authorization of `S_mid` scaling/sensitivity estimate.

## GPT-Wing Adjudication - OBS_023

Ruling:
PASS WITH SENSITIVITY CONDITIONS.

`S_mid` is clean enough to serve as the first declared shell datum for C5-B1 shell/local magnetic fraction work, provided it remains explicitly a datum and not a physical boundary.

Authorized:

- scaling/order-counting estimate for `rho_shell(S_mid)`,
- qualitative sensitivity check against `R_excl`,
- qualitative sensitivity check against `r_inner` and `r_outer`,
- comparison to one parked alternative shell only if used as a sensitivity witness.

Not authorized:

- whole-domain `rho_mag`,
- coefficient-level certification,
- baseline-subtracted integrated ledger,
- ordinary-energy comparison,
- radiative flux claim,
- conservation claim,
- prediction claim,
- repo execution.

Sensitivity conditions:

- keep `R_excl << a`,
- state when `r_inner = a/4` intersects source exclusion geometry,
- treat `r_inner`, `r_outer`, and `R_excl` as datum choices,
- flag any denominator-small or cancellation-dominated region,
- do not promote shell-stable order counting into invariant evidence,
- preserve observer/tetrad dependence in the claim ceiling.

Authorized target:

```text
rho_shell(S_mid) ~ O(v^2/c^2) ~ O(GM/(2ac^2))
```

Claim ceiling:
scratch shell scaling/sensitivity estimate only.
not certified calculation.
not ordinary energy.
not flux.
not radiative balance.
not prediction.

Next gate:
OBS_024 = C5-B1 `S_mid` shell scaling/sensitivity estimate archive.
