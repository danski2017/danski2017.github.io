---
type: dynamic_gfro_spec
status: active
created: 2026-05-26
topics:
  - atlas-dynamics
  - gfro
  - gcs
  - zero-set
  - extraction-ladder
---

# Dynamic GFRO Extraction Ladder 2026-05-26

## Purpose

Bring the dynamic skeleton closer to GFRO discipline before running larger simulations.

The source-fixed R5 branch now behaves better, but it must be placed inside a formal extraction ladder rather than treated as final doctrine because it looks better.

## Canonical Reminder

A GCS is a parity horizon where a declared gravitational contribution reaches equality with its derived gravitational context under a declared readability rule.

It is not a force boundary, material membrane, causal horizon, event horizon, or orbital-stability limit.

Dynamic seams, nodes, handoff supports, and closure diagnostics are downstream of the retained GCS/parity-context extraction. They do not replace the declared residual, zero-set extraction, or relevance filters.

## Dynamic GFRO Inputs

Declared source:

- source id
- mass
- source position
- source velocity
- local clock/grid values
- update index from Node 0

Declared battery:

- R0 potential
- R1 acceleration
- R2 tidal tensor
- R3 lapse/spatial scale
- R4 Christoffel/geodesic correction
- R5 1PN tidal tensor
- R5 self/context/cross decomposition
- `K_ij` / `K_total`
- ADM comparison residuals

Declared sampling:

- source-centered omni-radial sampling
- Fibonacci angular spacing
- radial scalar traces for all samples
- full tensor battery at accepted crossings

## Residual Ladder

Every dynamic GFRO run should declare and ledger its residual mode.

### R2 Linear Context

Name:

`linear_r2_context`

Residual:

`||E_self|| - ||E_context_R2||`

Use:
baseline comparison only.

### Current R5 Anomaly Lane

Name:

`current_self_contaminated_r5`

Residual:

`||E_self|| - ||E_1PN_full - E_self||`

Use:
historical reproduction and anomaly evidence only.

Status:
quarantined for source-centered GCS extraction because it leaves source self-A correction inside the context side.

### Self-Cleaned R5 Candidate

Name:

`self_cleaned_r5`

Residual:

`||E_self|| - ||E_1PN_full - E_self - delta_self_A||`

Use:
current default visual and diagnostic extraction branch.

Status:
candidate, not certified.

### Cross-Retaining R5 Candidate

Name:

`cross_retaining_r5`

Residual:
to be declared explicitly before implementation.

Open issue:
whether cross terms belong entirely on the derived context side, partly in a separate parity channel, or in a higher-order jurisdiction diagnostic.

Rule:
do not silently fold cross terms into context without declaring the readability meaning.

### Final Atlas Dynamic GCS Residual

Name:

not yet certified.

Requirement:
must survive source-fix sweeps, normalized seam/lineage tests, tensor-battery audits, and comparison against R2/EIH/ADM-like monitors.

## Zero-Set Extraction Rule

Current implementation:

- sample residual along source-centered rays
- find radial sign changes
- interpolate crossing radius
- retain crossing point and tensor battery

Required next hardening:

- record bracket endpoints for accepted crossings
- record residual slope or local conditioning
- flag multiple roots per ray
- distinguish first root, outer root, and all roots
- compare radial resolution sensitivity
- compare ray-density sensitivity

Completed source update:

`/Users/danski2017/Desktop/Atlas_Solver_Project/Relational_Labs/Relational_Labs/Atlas Codex Bridge/Dynamic Evolution/GFRO Root Metadata Source Update 2026-05-26.md`

## Relevance Filters

No seam/node should be physically promoted unless it survives:

- normalized distance threshold
- source-pair identity tracking
- update-step lineage
- ray-density sensitivity
- radial-resolution sensitivity
- false-positive separated-scene check

## Dynamic Claim Ceiling

The current instrument is GFRO-structured, not GFRO-certified.

It uses source-centered residual zero-set extraction and ledgered battery records. It does not yet implement a mature GFRO retained-boundary certification pipeline.

## Immediate Implementation Requirements

Before robust simulations:

1. Add `linear_r2_context` and future `cross_retaining_r5` as explicit residual ladder entries in code or manifest.
2. Run source-fixed normalized seam sweeps.
3. Run source-fixed seam lineage.
4. Add radial root conditioning fields.
5. Add root multiplicity reporting per ray.

## No-Promotion Rules

- Do not call self-cleaned R5 final because it fixed Heavy.
- Do not call seams/nodes physical because they are more active after the fix.
- Do not call the dynamic foam GFRO-certified until the retained-boundary filters pass.
- Do not use the Newtonian-primary animation as proof of Atlas-native dynamics.
