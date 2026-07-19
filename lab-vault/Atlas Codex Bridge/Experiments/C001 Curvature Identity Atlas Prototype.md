---
type: experiment_note
status: completed
created: 2026-05-13
experiment_id: C001_curvature_identity_atlas_prototype
topics:
  - curvature-identity
  - budget
  - jurisdiction
  - compression
  - website-tool
---

# C001 Curvature Identity Atlas Prototype

## Status

Completed internal prototype.

Package:

`codex_context/experiments/C001_curvature_identity_atlas_prototype`

Script:

`codex_context/scripts/c001_curvature_identity_atlas_prototype.py`

Package size:

`0.020 MiB`

## Purpose

Build the first summary-only data package for the Curvature Identity Atlas public tool.

Channels:

- exterior Weyl-electric square budget,
- toy source/context jurisdiction,
- toy multipole compression.

## Budget Ladder

The run reproduced the declared spherical-source budget:

```text
B_E = 8 pi G^2 M^2 / R^3
```

and confirmed the density identity:

```text
B_E / M = (32 pi^2 / 3) G^2 rho_bar
```

Max relative error in the density identity table:

```text
2.371e-16
```

Headline rows:

| Object | log10 B_E | B_E / M |
|---|---:|---:|
| proton | -27.330 | 2.795e-01 |
| hydrogen atom | -41.674 | 1.264e-15 |
| NS max (2.2 Msun) | 30.267 | 4.231e-01 |
| BH (10 Msun) | 30.235 | 8.642e-02 |
| TON 618 | 20.416 | 1.984e-21 |

Declared table peak:

```text
NS max (2.2 Msun), log10 B_E = 30.267
```

## Jurisdiction Examples

Toy source/context rule:

```text
Q_source ~ M_source / r^3 equals Q_context ~ M_context / D^3
```

| Example | Jurisdiction radius | Fraction of separation |
|---|---:|---:|
| Earth in solar context | 2.158e9 m | 0.014428 |
| Moon in Earth context | 8.872e7 m | 0.230795 |
| Sun in Sgr A* context | 1.590e18 m | 0.006300 |

These are calculator-design examples, not final jurisdiction doctrine for every readable.

## Compression Examples

Toy quadrupole rule:

```text
|J2| * (R/r)^2 <= tolerance
```

This gives website-design examples for how a declared tolerance turns resolved source detail into a compression radius. Serious spheroid work should use actual multipole ledgers from the Weyl Spheroid lane.

## Website Tool Shape

Inputs:

- object preset or custom mass/radius,
- optional context mass and separation,
- optional tolerance and quadrupole fraction,
- radius-basis declaration.

Outputs:

- exterior Weyl-electric square budget,
- budget per mass,
- mean density,
- density identity check,
- source/context jurisdiction radius,
- toy compression radius,
- claim-boundary note.

## Claim Boundary

This is static weak-field diagnostic bookkeeping.

Non-claims:

- no new field equation,
- no new force,
- no GR replacement,
- no observable claim,
- no quantum-gravity claim,
- particle radii are declared effective radii,
- compression examples are design toys until backed by multipole ledger,
- handoff remains open.

## Next Gates

- Add a website-ready JSON shape with display labels and units.
- Add uncertainty/radius-basis notes for particle entries.
- Add first proper compression examples from Weyl Spheroid multipole tables.
- Add a public copy block for the website calculator page.

