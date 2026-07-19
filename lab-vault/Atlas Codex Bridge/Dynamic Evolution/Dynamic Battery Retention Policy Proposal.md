---
type: dynamic_retention_policy
status: tier_1_smoke_implemented
created: 2026-05-26
topics:
  - atlas-dynamics
  - ledger
  - retention
  - data-growth
---

# Dynamic Battery Retention Policy Proposal

## Purpose

Prevent data explosion while preserving lawful Atlas evidence.

Tier 1 has been implemented for the local smoke instrument. Full radial-sample tensor persistence remains unapproved for production.

## Current Fact

The skeleton smoke run now persists crossing-level battery records plus Tier 1 radial scalar traces.

Smoke dimensions:

- steps: `3`
- sources: `4`
- base rays: `300`
- radial samples per ray: `20`
- accepted crossing records: `2808`
- crossing battery JSONL: `4.9M`
- radial scalar trace records: `61760`
- radial scalar trace JSONL: `20M`
- total smoke output after current figures: `27M`

The current ledger is useful because every accepted R5 crossing carries the tensor battery needed for audit, and every sampled radial point carries enough scalar provenance to inspect extraction behavior. It is still incomplete in the sense that it does not preserve full tensor matrices at every radial sample.

## Growth Concern

Persisting every sampled radial point scales approximately as:

`steps * sources * rays_per_source * radial_samples * retained_fields`

At the smoke scale, that is already about:

`3 * 4 * 300 * 20 = 72000` sampled points before adaptive ray changes.

At a plausible larger run:

`240 * 4 * 800 * 64 = 49152000` sampled points before adaptive ray changes.

Full tensor payloads at that scale will become large quickly, especially if matrix fields and decomposition branches are written as readable JSON.

## Proposed Tiers

### Tier 0: Crossing Ledger

Persist only accepted crossing records.

Use for:

- quick visual audit
- smoke tests
- first reproduction checks
- branch comparison thumbnails

Limit:

No full radial provenance.

### Tier 1: Crossing Ledger Plus Radial Scalars

Persist accepted crossing records plus compact scalar traces for every radial sample.

Suggested radial scalar fields:

- source id
- step/update index
- ray id
- radial index
- radius
- R5 residual
- R2 residual
- cross fraction
- `K_total`
- Hamiltonian residual

Use for:

- verifying where roots appeared along rays
- detecting missed crossings
- plotting radial residual profiles
- auditing extraction stability without carrying every tensor matrix

Limit:

Tensor fields remain available only at accepted crossings.

### Tier 2: Crossing Ledger Plus Triggered Radial Battery

Persist full tensor battery only near extraction events or anomalies.

Suggested triggers:

- sign change in R5 residual
- local R5 residual minimum below threshold
- high cross-fraction pocket
- high Hamiltonian residual pocket
- seam/node candidate neighborhood

Use for:

- lawful debugging of extraction surfaces
- seam/node lineage
- constraint concentration studies
- reproducibility audits where scalar traces are insufficient

Limit:

Requires stable trigger rules and manifest recording.

### Tier 3: Full Radial Battery

Persist full tensor battery at every sampled radial point.

Use for:

- rare certification runs
- benchmark scenes
- disputes between extraction branches
- archival gold-standard evidence

Limit:

Potentially explosive storage cost. Should use binary columnar storage, chunking, and compression rather than readable JSON.

## Implemented Smoke Choice

Tier 1 is now active in the local smoke instrument.

Reason:

Tier 1 preserves the causal radial trace of each extraction without multiplying matrix payloads across every sample. It gives the lab enough information to audit whether the field is being allowed to find the crossing, while avoiding premature full-battery storage.

Implemented radial scalar fields:

- update step
- source id and name
- source position
- ray id
- ray direction
- radial index
- radius
- R5 residual
- R2 residual
- R5 cross fraction
- `K_total`
- Hamiltonian residual

## Non-Negotiables

- Do not discard accepted crossing tensor batteries.
- Do not hide retention rules outside the manifest.
- Do not call a reduced ledger complete.
- Do not treat storage convenience as a reason to weaken lawful GR/Atlas content.
- Do not alter source-siloed ledgers or Fibonacci omni-radial sampling without explicit lab approval.
