---
type: proven_architecture
status: active
created: 2026-05-13
owner: codex
topics:
  - simulation-architecture
  - reusable-patterns
---

# Proven Atlas Simulation Architecture

This note records the Atlas-native architecture that has actually worked in B006-B014. The patterns are written in lab vocabulary so future wings do not rebuild parallel abstractions.

## Pattern A: Retained vs Coarse Branch Comparison

Used in:

- B006
- B007
- B008
- B009
- B010-B012

Architecture:

```text
Scene passport
Node 1 parent/context declaration
Node 2+ retained source roster
Retained source/context relation map
Field-sieve emitted retained summary ledger
Coarse branch source roster
Branch source/context relation map
Field-sieve emitted branch summary ledger
Witness-panel comparison
Tensor/scalar ratio extraction
```

Best for:

- galaxy coarse-graining
- observational reconstruction
- method comparison
- curvature information loss

## Pattern B: Source-Count Ladder

Used in:

- B009
- B014

Architecture:

```text
for N in source_counts:
  declare Node 2+ source proxy roster
  keep witness datum panels fixed
  evaluate retained and coarse branches
  build derived source/context relation maps
  emit Node -1 summary rows from those maps
fit Delta(N) = Delta_inf + A/sqrt(N)
```

Best for:

- testing finite-source artifacts
- estimating method residual floors
- preventing bad linear extrapolation

## Pattern C: Method-Resolution Ladder

Used in:

- B010
- B014

Architecture:

```text
hold scene fixed
for method_resolution in coarse/standard/fine:
  build declared branch source proxy roster
  evaluate same witness datums
  emit branch summary rows
  compare against retained emitted summary ledger
```

Best for:

- separating method resolution from source-count convergence
- exposing transfer functions
- defending against "you just used too coarse a grid" criticism

## Pattern D: Morphology Variants

Used in:

- B011

Architecture:

```text
base source field
  -> deterministic Node 2+ morphology transforms
  -> retained/coarse comparison per variant
  -> variant-specific emitted Node -1 summary rows
```

Best for:

- checking if an effect is scene-specific
- building paper robustness

## Pattern E: Witness-Field Robustness

Used in:

- B012
- B013
- B014

Architecture:

```text
same physical scene
different witness datum panels
same branch comparisons
```

Best for:

- locating where an effect lives
- preventing overclaiming
- distinguishing disc/halo/void/filament regimes

## Pattern F: Summary-Only Heavy Compute

Used in:

- B009
- B010-B012
- B013
- B014

Architecture:

```text
compute full diagnostics in memory
emit Node -1 summary ledger tables, fits, reports, manifests
do not store raw tensor ledgers unless required
```

Best for:

- fast iteration
- large source-count or method ladders
- staying under storage caps

## Pattern G: Lumen / Wireframe Correspondence Ladder

Used in:

- Morse-Smale tidal wireframe v0.3
- EMS Lumen Lattice v0.1
- EMS-in-LSN Full-Riemann GFRO Lumen microscope
- SS wireframe-bone extraction and matched witness audits
- GFRO Arm32 seam persistence audit

Architecture:

```text
scene passport
Node 1 parent/context declaration
Node 2+ source roster
GFRO source/context relation map
field-sieve emitted zero sets / faces / seams / junctions / scaffold candidates
Node -1 emitted registry
tensor/eigen/electric-Weyl witness panels
Lumen Lattice release rule
matched controls and resolution checks
retention status
render after ledger
```

Best for:

- Lumen Lattice viewer builds
- wireframe scaffold testing
- beam/truss/rib candidate review
- separating visual datum response from evidence
- building future public figures without render-first drift

## Architecture Recommendation

Future serious runs should compose these patterns rather than start from scratch.

Example:

```text
B015 Galaxy Observational Anchor =
  Retained vs Coarse Branch Comparison
  + Method-Resolution Ladder
  + Witness-Field Robustness
  + Summary-Only Heavy Compute
```

## Atlas Governance Layer

Every architecture above sits under:

```text
Node 1 parent/context declaration
Node 2+ source roster
datum/witness roster
GFRO relation-map declaration
field-sieve emission rule
Node -1 ledger policy
Node Psi extraction status if derived structures are extracted
claim ladder status
non-claims
```

No architecture is complete without these declarations.

For Lumen or wireframe runs, add:

```text
Lumen release rule
wireframe scaffold candidate status
GFRO/Lumen correspondence measure
tensor/eigen/Weyl witness comparison
render claim ceiling
```

## GFRO Emitter Correction

Current Atlas architecture should be remembered this way:

```text
Scene first.
Source/datum lock.
Parent/context declared.
GFRO relation map built.
Field-sieve emits candidates.
Node -1 records emitted ledger.
Witnesses rank candidates.
Retention certifies scaffolds.
GR decides.
```

Do not frame new work as if queries are the primary extraction engine. Queries are downstream inspection tools over emitted ledgers and diagnostic registries.
