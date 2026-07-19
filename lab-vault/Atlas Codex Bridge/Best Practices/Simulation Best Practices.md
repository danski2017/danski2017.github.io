---
type: best_practices
status: active
created: 2026-05-13
owner: codex
topics:
  - simulation
  - best-practices
  - reproducibility
---

# Atlas Simulation Best Practices

This note is the long-term memory for how Atlas should run simulations without rebuilding the wheel. It uses Atlas-native vocabulary: Nodes, sources, datums, witnesses, ledgers, GFRO, and the claim ladder.

## Core Rule

Every serious run should be:

1. scene-passported,
2. node-declared,
3. source/datum separated,
4. witness-based,
5. ledger-first,
6. GFRO/GR-governed,
7. deterministic,
8. claim-bounded,
9. manifest-backed,
10. promoted into Obsidian after closeout.

Compact mantra:

```text
Sources speak.
Datums listen.
Witnesses report.
GFRO maps source/context relations.
The field-sieve emits candidates.
Node -1 records the emitted ledger.
Renders behave.
GR decides.
```

## Node Taxonomy Requirement

Every serious run declares node roles before extraction:

| Node | Atlas Role | Simulation Use |
|---|---|---|
| Node -1 | certified relational ledger | stores lawful source/datum/witness records |
| Node 0 | primary geometric registration datum | coordinate/registering reference, not automatically a source |
| Node 1 | mandatory lawful parent scene relation | parent/context/asymptotic/observational boundary, not a scalar floor |
| Node 2+ | physical source nodes | only declared physical sources contribute modeled field |
| Node G | geometric centroid | computed diagnostic, not sovereign center |
| Node B | mass barycenter | computed diagnostic, not automatically Node 0 |
| Node Psi | extracted GCS/parity-context diagnostic layer | derived from ledgered relations, not force/evidence by itself |
| Node P | parity-junction candidate | not automatically critical |
| Node A | earned adjudication/critical-transition candidate | requires validation; never automatic |

## Source / Datum / Witness Lock

Sources contribute. Datums interrogate. Witnesses report.

Minimum declarations:

- Node 2+ source roster: source model, mass/source strength, position/worldline, contribution status.
- Datum roster: Node 0, source-associated datums, child/parent witnesses, ray/radial/sample datums where used.
- Witness panels: named non-source panels that define where the comparison is meaningful.
- Ledger target: what Node -1 will remember.

Incorrect patterns:

- treating Node 0 as a source because it is central,
- treating Node 1 as a scalar floor,
- treating a source-associated datum as the source itself,
- treating Node Psi surfaces as physical membranes,
- claiming from a render without ledger support.

## Standard Run Anatomy

Use this package shape:

```text
codex_context/experiments/<RUN_ID_slug>/
  configs/
    <RUN_ID>_CONFIG.json
  docs/
    <RUN_ID>_SCENE_PASSPORT.txt
  derived/
    <RUN_ID>_TABLE.csv
    <RUN_ID>_FITS.json
    <RUN_ID>_RUN_SUMMARY.json
  reports/
    <RUN_ID>_REPORT.txt
    <RUN_ID>_INTERPRETATION_NOTE.txt
  manifest.json
```

Full tensor ledgers are allowed only when scientifically necessary. Default to summary-only packages for ladders and method scans.

## Required Metadata

Every run should declare:

- `atlas_experiment_id`
- claim status
- node declaration
- Node 1 parent/context mode
- source model
- datum roster
- witness panels
- Node -1 ledger policy
- branch/method list
- metric register
- hard cap
- output policy
- non-claims

## Determinism

Use deterministic seeds. If a run has multiple rungs, seed them by rung in a reproducible way and record the scheme in config or report.

Good pattern:

```text
seed = base_seed + source_count
```

## Witness Discipline

Witness panels are datums in the broad Atlas sense: non-source supports that make the scene readable. They are not incidental sampling. They define what the run can claim.

Good panels:

- fixed across source-count rungs when testing scale
- varied deliberately when testing robustness
- named by physical role: midplane, off-plane, halo, void, filament, wall, lightcone proxy

## Metric Register

For mesoscale curvature and averaging work, use:

- p90 electric-Weyl Frobenius delta
- p90 eigenframe disagreement
- p90 eigenspan delta
- p90 scalar rotation or acceleration delta
- tensor/scalar ratio

Use p50 as supporting context, not headline.

For finite-source curvature identity work, keep these channels separate:

- curvature budget,
- source/context jurisdiction,
- compression tolerance boundary,
- Ricci-side source/scalar account,
- Weyl-electric tensor account,
- eigenstructure,
- handoff witness status,
- static vs dynamic claim status.

Do not collapse these into one surface or one score.

## Ledger Before Render

The order is:

```text
scene passport
source/datum/node declaration
GFRO source/context relation map
field-sieve coordinate emission
Node -1 emitted diagnostic ledger or summary ledger
witness ranking / retention check
interpretation note
render/website language
```

Renders may communicate. They do not decide.

## Lumen / Wireframe Discipline

The Lumen Lattice is a major Atlas lane and should be treated as a released datum witness.

Preferred language:

- Lumen Lattice,
- Released Coherence Lattice,
- released coordinate lattice,
- field-displaced volumetric datum lattice,
- visual datum witness,
- wireframe scaffold candidate.

Avoid:

- physical sponge,
- material spacetime lattice,
- vacuum hardware,
- proof by render,
- canonical wireframe before retention.

For serious Lumen runs, record the lattice resolution, edge rule, displacement rule, release gain, GFRO overlay provenance, tensor/eigen/Weyl witness plan, and claim ceiling.

## GFRO Emitter Posture

The current architecture is emitter-centered, not query-centered.

Older language:

```text
queries extract structures from the scene
```

Current GFRO language:

```text
declared source/context residuals form a derived relation map
the field-sieve emits coordinate candidates from that map
Node -1 records the emitted diagnostic registry
witnesses rank and validate emitted candidates
retention certifies which scaffolds survive
```

Queries may still inspect, filter, or view a ledger. They are not the primary engine grammar.

## Convergence Reads

Do not scale normalized deltas linearly by source count.

Preferred first-pass model:

```text
Delta(N) = Delta_inf + A / sqrt(N)
```

Interpretation:

- `A / sqrt(N)` is finite-source sampling behavior.
- `Delta_inf` is the method-dependent residual floor.

## Resolution Ladders

When testing a coarse method, source-count ladders are not enough. Add a method-resolution axis:

- rings/sectors
- grid cells
- kernel width
- shell count
- beam size

This separates finite-source effects from coarse-method transfer functions.

## Claim Boundaries

Every report should include explicit non-claims.

Current standard:

- no dark-matter claim
- no dark-energy claim
- no cosmological parameter claim
- no GR/SR challenge
- weak-field approximation declared when used
- not full numerical relativity unless actually built

## Storage Discipline

Default hard cap:

```text
100 MiB per experiment package
```

If a run needs more, report expected size before running or write a summary-only variant first.

## Closeout Rule

After each run:

1. confirm node/source/datum declarations survived into docs/config,
2. confirm the GFRO relation map or declared comparison map is named,
3. confirm emitted ledger/summary rows are preserved,
4. read report and tables,
5. write interpretation note,
6. check package size,
7. update Obsidian experiment note,
8. update Live Experiment Dashboard,
9. update Next Simulation Queue if needed,
10. preserve manifest.
