---
type: scratch_scaling_estimate
status: dynamic_weyl_witness_candidate
created: 2026-05-15
candidate: C5-B1
claim_status: scratch scaling estimate / dynamic Weyl witness candidate / no calculation certified
repo_execution_authorized: false
topics:
  - c5-b1
  - bel-robinson
  - magnetic-weyl
  - scaling-estimate
  - frontier-evidence
---

# C5-B1 Scratch Scaling Estimate v0.1

## Claim Status

Scratch scaling estimate / dynamic Weyl witness candidate / no calculation certified.

This note is not certified evidence, not a repo calculation, not a conservation claim, not ordinary-energy accounting, not a radiative-balance claim, and not a prediction.

## Source Links

- [[C5-B1 Analytic Calculation Passport]]
- [[C5-B Observer Tetrad Declaration Passport]]
- [[C5-B Bel-Robinson Literature Theory Map v0.1]]
- [[C5-B Bel-Robinson Superenergy Gate v0.1]]
- [[C5-A Scratch Hand Derivation v0.1]]
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

Object: schematic Bel-Robinson density witness `U_BR ~ E_ij E^ij + B_ij B^ij`.

## Scaling Estimate

Electric Weyl/tidal scale:

```text
E ~ GM / r^3
```

Therefore:

```text
E^2 ~ G^2 M^2 / r^6
```

For moving weak-field sources, magnetic Weyl is velocity-suppressed relative to electric Weyl:

```text
B ~ (v/c) E
```

Therefore:

```text
B^2 ~ (v^2/c^2) E^2
```

So the ratio is:

```text
B_ij B^ij / E_ij E^ij ~ v^2/c^2
```

For an equal-mass circular binary where `a` is the separation between the two masses, each mass orbits at radius `a/2`. Newtonian force balance gives:

```text
G M^2 / a^2 = M v^2 / (a/2)
```

so:

```text
v^2 = GM / (2a)
```

Thus:

```text
B^2/E^2 ~ GM / (2 a c^2)
```

Equivalently, with `M_tot = 2M`:

```text
B^2/E^2 ~ G M_tot / (4 a c^2)
```

## Scratch Finding

C5-B1 identifies the first dynamic Weyl-custody witness:
magnetic Weyl enters as a velocity-suppressed superenergy channel.

The schematic near-zone Bel-Robinson witness behaves as:

```text
U_BR ~ E^2 [1 + O(v^2/c^2)]
```

or for equal masses:

```text
U_BR ~ E^2 [1 + O(GM/(2ac^2))]
```

## Interpretation Ceiling

This result means:

- the magnetic-Weyl channel is absent from the strictly static C5-A branch,
- the magnetic-Weyl channel enters once motion is admitted,
- in the weak-field near zone it is PN-suppressed by `v^2/c^2` relative to `E^2`,
- it may grow in relevance as separation shrinks and orbital velocity increases,
- it does not establish radiative handoff by itself.

This is a dynamic witness candidate, not a certified ledger result.

## Relation to C5-A

C5-A showed that the static electric-only budget is self-budget dominated and does not carry the dynamic inspiral accounting role.

C5-B1 shows that the missing dynamic channel first appears as magnetic-Weyl contribution in the Bel-Robinson / superenergy family.

Atlas shorthand:

```text
C5-A identifies the receipt.
C5-B1 detects the courier's first pulse.
```

## Required Checks Before Certification

- Verify the `B ~ (v/c)E` scaling in the declared weak-field barycentric observer frame.
- Check convention factors for magnetic Weyl.
- Check whether source self magnetic terms or orbital interaction magnetic terms dominate.
- Define isolated moving-body baseline if using excess.
- Decide whether integration is meaningful or whether a ratio diagnostic is better.
- Do not proceed to full integration before baseline/excess definition.

## Current Ruling

C5-B1 passes as scratch order-counting estimate.

Finding:
`B_ij B^ij / E_ij E^ij ~ O(v^2/c^2)`, approximately `GM/(2ac^2)` for equal masses separated by `a`.

Claim ceiling:
scratch scaling witness only.

## Next Gate

Recommended next gate:
C5-B1 baseline/excess definition note.

Purpose:
Determine whether the next analytic object should be:

1. local density ratio `B^2/E^2`,
2. integrated magnetic excess,
3. full Bel-Robinson excess,
4. near-zone diagnostic ratio,
5. or defer integration until PN/tetrad setup is hardened.
