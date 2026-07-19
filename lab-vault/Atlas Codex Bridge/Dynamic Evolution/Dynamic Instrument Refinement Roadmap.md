---
type: dynamic_refinement_roadmap
status: active
created: 2026-05-26
topics:
  - roadmap
  - atlas-dynamics
  - implementation
---

> [!success] PHASE 4 PARTIALLY REALIZED (2026-07-17/18)
> The momentum-constraint proxy prescribed below is IMPLEMENTED as the
> Dynamic Witnesses momentum-residual monitor (psi^-10-weighted
> divergence of the composite Bowen-York sum, baked on the declared
> volume lattice). See the 2026-07-17 Dynamic Witnesses Receipt in the
> Atlas Platform Archive. Remaining Phase-4 items (Hamiltonian residual
> hardening, constraint-vs-seam correlation) stay open.

# Dynamic Instrument Refinement Roadmap

## Goal

Refine the dynamic Atlas instrument until the field and relational ledger can predict source evolution without an externally imposed Newtonian driver.

The final target is a lawful Atlas-native animation/simulation method, confronted honestly against ADM-style evolution.

## Phase 0: Project Home

Status:
started.

Deliverables:

- Obsidian project home
- handoff register
- governance snapshot
- certification ladder
- refinement roadmap

## Phase 1: Local Reproduction

Goal:
run the handoff skeleton locally without changing scientific behavior.

Tasks:

- adapt hardcoded output path from `/home/claude/atlas_skeleton_out`
- preserve original handoff script as imported artifact
- run a minimal 3-step smoke test
- write local run manifest
- verify crossing counts, seams, nodes, clocks, and output schema

Claim ceiling:
reproduction smoke only.

## Phase 2: Repo-Native Ledger Contract

Goal:
turn dynamic output into Atlas ledger-grade artifacts.

Tasks:

- define dynamic scene passport
- define source subjective ledger schema
- define Riemann battery record schema
- define crossing ledger schema
- define seam/node lineage schema
- define run summary and manifest
- include claim ceiling and rung status in every run

## Phase 3: R5 Reproduction and Scaling

Goal:
move R5 from Observed to Reproduced.

Tasks:

- run second scene with different mass ratios or source count
- run `c_toy` sweep
- run ray/radial sensitivity
- compare R2 and R5 crossing displacement
- record self/context/cross fractions

## Phase 4: `K_ij` and Constraint Monitors

Goal:
make ADM confrontation measurable.

Tasks:

- add momentum constraint proxy
- harden Hamiltonian residual calculation
- document gauge and approximation assumptions
- map constraint residuals against seams/nodes
- test whether nodes correlate with constraint concentration

## Phase 5: Driver Isolation

Goal:
separate current mechanics from Atlas-native field prediction.

Branches:

- Branch N: Newtonian leapfrog baseline
- Branch L0: Newtonian `T - V` variational baseline diagnostics
- Branch R4: Newtonian plus Christoffel/geodesic correction
- Branch R5: 1PN shadow lane
- Branch L1: weak-field/1PN variational shadow lane
- Branch A: future Atlas-native field-derived update rule
- Branch ADM: ADM-like comparison branch

Rule:
do not call any branch Atlas-native unless the update rule is explicitly derived from ledgered field/battery quantities.

## Phase 6: First Atlas-Native Update Candidate

Goal:
define the first candidate rule by which the relational field predicts motion.

Candidate inputs:

- source-clock drift
- grid-scale drift
- tidal eigenframe transport
- R5 crossing displacement
- self/context/cross fractions
- seam/node migration
- local constraint residuals
- collective network deformation

Output:
next-step source update proposal with clear units, conservation audit, and failure mode.

## Phase 7: Confrontation

Goal:
run side-by-side evolution.

Compare:

- source trajectories
- foam geometry
- seam/node birth, death, migration
- clocks and grid scales
- R5 displacement
- constraint residuals
- conservation quantities

Interpretation:
agreement validates implementation. Disagreement is not automatically success. It is either bug, approximation failure, ADM limitation, or frontier signal.

## Immediate Next Action

Promote seam lineage into the diagnostic report as a gate, then test it against ray density, radial-shell density, and longer update windows.

Reference:

`/Users/danski2017/Desktop/Atlas_Solver_Project/Relational_Labs/Relational_Labs/Atlas Codex Bridge/Dynamic Evolution/Dynamic Battery Retention Policy Proposal.md`

`/Users/danski2017/Desktop/Atlas_Solver_Project/Relational_Labs/Relational_Labs/Atlas Codex Bridge/Dynamic Evolution/Lagrangian Integration Triage 2026-05-26.md`

`/Users/danski2017/Desktop/Atlas_Solver_Project/Relational_Labs/Relational_Labs/Atlas Codex Bridge/Dynamic Evolution/Seam Lineage Filter 2026-05-26.md`
