---
type: dynamic_integration_triage
status: active
created: 2026-05-26
topics:
  - atlas-dynamics
  - lagrangian
  - variational-integration
  - driver-isolation
---

# Lagrangian Integration Triage 2026-05-26

## Purpose

Identify where the previous session likely got stuck on Lagrangian integration and define a lawful next path without weakening the Atlas dynamic goal.

## Immediate Correction

The issue is probably "Lagrangian" integration, not "Langratian" integration.

## Current Code Status

The current skeleton uses Newtonian leapfrog as the primary source-motion driver.

Code:

`/Users/danski2017/Desktop/Atlas_Solver_Project/codex_context/dynamic_evolution/skeleton_smoke_20260526/atlas_skeleton_compute_local.py`

Relevant functions:

- `newtonian_acc`
- `leapfrog`
- `geodesic_correction`
- `geodesic_correction_1pn`

Current lanes:

- Lane N: Newtonian leapfrog primary
- Lane R4: Newtonian plus spatial-Christoffel geodesic correction shadow lane
- Lane R5/1PN: Newtonian plus 1PN geodesic correction shadow lane

The R4 and R5 lanes are computed as shadow lanes, but they do not yet drive the emitted primary foam.

## Important Distinction

Leapfrog is not a sloppy integrator. For a separable Newtonian Hamiltonian, it is a symplectic/variationally respectable method.

The problem is not numerical respectability. The problem is scientific authority:

The current primary driver is still a Newtonian source-motion law. It is not yet an Atlas-native law derived from the field ledger, crossing battery, seams, nodes, clocks, and relational network.

## Why The Lagrangian Path Gets Sticky

A conventional N-body Lagrangian is easy:

`L = T - V`

with coordinate positions, coordinate velocities, masses, and Newtonian potential.

That would reproduce the current Newtonian lane, but it would not satisfy the lab goal. It keeps the dynamics anchored in an external coordinate-time mechanics picture.

A GR-adjacent particle action is also available in principle:

`S = -m c ∫ ds`

or weak-field/1PN approximations derived from a metric.

That is closer, but still must be handled carefully. If the metric, slicing, or update parameter quietly imports a preferred background frame, it undercuts the Atlas objective.

The Atlas problem is harder:

Define an action-like scalar from ledgered relational quantities such that the next source update is predicted by the field/network itself, with Node 0 acting only as the update/reconciliation index.

## Claim Boundary

Do not call the current leapfrog lane Atlas-native.

Do not call a Newtonian `T - V` variational wrapper lawful GR dynamics.

Do not call an ADM-like action comparison an Atlas replacement unless the update rule is actually derived from Atlas ledger objects.

## Useful Decomposition

The Lagrangian question should be split into three branches.

### Branch L0: Newtonian Variational Baseline

Purpose:

Confirm that the current leapfrog lane corresponds to the ordinary Newtonian `T - V` baseline.

Value:

- energy/conservation sanity check
- baseline for animation stability
- comparison against later branches

Limitation:

Not Atlas-native.

### Branch L1: Weak-Field Metric / 1PN Action Shadow Lane

Purpose:

Build an explicitly declared weak-field action branch using the same approximations already present in the R5/1PN battery.

Value:

- compares source motion from a variational 1PN rule against current R5 shadow corrections
- keeps approximation assumptions explicit
- creates an ADM/GR-adjacent confrontation lane

Limitation:

Still not Atlas-native unless the update is chosen from relational ledger constraints rather than imported metric mechanics.

Implementation source:

The smoke implementation uses the EIH 1PN N-body Lagrangian form, cross-checked against Justin Vines, "Deriving the Einstein-Infeld-Hoffman (EIH) Lagrangian."

Reference:

`https://fiteoweb.unige.ch/~maggiore/subdir/EIHLagrangian.pdf`

### Branch LA: Atlas-Native Relational Action Candidate

Purpose:

Define a candidate scalar functional over the Atlas ledger itself.

Possible ingredients:

- R5 residual displacement
- source-clock drift
- grid-scale drift
- tidal eigenframe transport
- cross-term fraction
- seam/node migration
- Hamiltonian residual
- conservation residuals
- collective network deformation

Constraint:

The action must be invariant under arbitrary relabeling of Node 0 update steps and must not treat the update index as an objective physical clock.

## Current Best Read

The last session likely got stuck by trying to jump directly from the current Newtonian update rule to a full Lagrangian replacement.

That jump is too large.

The clean path is:

1. ledger the current Newtonian variational baseline as Branch L0;
2. add conservation/action diagnostics without changing motion;
3. create a separate L1 weak-field/1PN variational shadow lane;
4. only then propose an LA Atlas-native action candidate from observed ledger signals.

## Next Implementation Step

Add L0 diagnostics only:

- kinetic energy
- Newtonian potential energy
- total energy
- angular momentum
- linear momentum
- ordinary Newtonian Lagrangian `L = T - V`
- discrete action increment `L * DT`

These should be emitted as baseline diagnostics in the manifest/run summary, not used to change source motion.

This gives the lab a clean floor before touching L1 or LA.

## L0 Smoke Implementation

Status:
implemented in the local smoke instrument.

The script now emits `l0_newtonian_variational_diagnostics` into each `step_data.json` step record.

Manifest scope:

`l0_diagnostics_scope: Newtonian T-V baseline diagnostics only; not an Atlas-native action`

Diagnostic figure:

`/Users/danski2017/Desktop/Atlas_Solver_Project/codex_context/dynamic_evolution/skeleton_smoke_20260526/out/figures/skeleton_smoke_l0_variational_diagnostics.png`

Observed smoke values:

- step 0: `T = 3.087794`, `V = -8.573666`, `E = -5.485873`, `L = 11.661460`, `L dt = 1.166146`
- step 1: `T = 3.087944`, `V = -8.573817`, `E = -5.485873`, `L = 11.661760`, `L dt = 1.166176`
- step 2: `T = 3.088395`, `V = -8.574267`, `E = -5.485873`, `L = 11.662662`, `L dt = 1.166266`

Momentum status:

- linear momentum norm: `0.0` at all three sampled update steps
- angular momentum norm: `56.028119` at all three sampled update steps

Read:

The Newtonian baseline is numerically clean over the tiny smoke. This supports using it as a baseline lane, but it does not promote it to Atlas-native dynamics.

## Revised Next Implementation Step

Add a separate L1 weak-field/1PN variational shadow lane, still non-primary, and compare it against the existing R4 and 1PN acceleration shadow lanes.

## L1 Smoke Implementation

Status:
implemented as diagnostics only.

The script now emits `l1_eih_variational_diagnostics` into each `step_data.json` step record.

Manifest scope:

`l1_diagnostics_scope: EIH 1PN barycentric weak-field Lagrangian diagnostic only; not an Atlas-native action`

Diagnostic figure:

`/Users/danski2017/Desktop/Atlas_Solver_Project/codex_context/dynamic_evolution/skeleton_smoke_20260526/out/figures/skeleton_smoke_l1_eih_variational_diagnostics.png`

Observed smoke values:

- step 0: `L_EIH = 11.928338`, L0 reference `11.661460`, 1PN correction `0.266878`, correction fraction `2.288547%`
- step 1: `L_EIH = 11.928664`, L0 reference `11.661760`, 1PN correction `0.266904`, correction fraction `2.288707%`
- step 2: `L_EIH = 11.929649`, L0 reference `11.662662`, 1PN correction `0.266987`, correction fraction `2.289243%`

Read:

The weak-field 1PN variational branch is now measurable as a shadow diagnostic. It is not yet an integrated L1 motion branch and is not an Atlas-native action.

## Revised Next Implementation Step

Compare the L1 EIH diagnostic against the existing 1PN acceleration shadow lane by ledgering shadow-lane positions and deviations from the Newtonian primary.

## Shadow Lane Position Ledger

Status:
implemented.

The script now emits matched-update shadow lane records:

`/Users/danski2017/Desktop/Atlas_Solver_Project/codex_context/dynamic_evolution/skeleton_smoke_20260526/out/shadow_lane_records.jsonl`

Diagnostic figure:

`/Users/danski2017/Desktop/Atlas_Solver_Project/codex_context/dynamic_evolution/skeleton_smoke_20260526/out/figures/skeleton_smoke_shadow_lane_deviations.png`

Records before context-excluded repair:

- `16` rows
- `2` matched update intervals
- `4` sources
- `2` shadow lanes: R4 geodesic and R5/1PN geodesic

Mean deviation from Newtonian primary:

- R4 geodesic position: `0.00073025`
- R4 geodesic velocity: `0.000340125`
- R5/1PN geodesic position: `0.10393525`
- R5/1PN geodesic velocity: `0.782919125`

Max deviation from Newtonian primary:

- R4 geodesic position: `0.001238`
- R4 geodesic velocity: `0.000733`
- R5/1PN geodesic position: `0.254963`
- R5/1PN geodesic velocity: `1.697467`

Read:

The R4 lane remains close to the Newtonian primary over the tiny smoke. The current 1PN acceleration lane diverges much more strongly. Since the L1 EIH action diagnostic is only a `~2.289%` Lagrangian correction in this scene, the 1PN acceleration lane now needs validation before it is trusted as a motion branch.

This does not disprove the 1PN lane. It marks it as a high-priority consistency check.

## ADM Sanity Check

ADM and ADM/PN point-particle treatments do not simply evaluate a particle's own singular field at the particle and feed it back as ordinary acceleration.

In ADM Hamiltonian PN work, point-mass self-field divergences require regularization. Dimensional regularization has been used to cure ambiguities in higher-order ADM Hamiltonians for compact binaries.

References:

- `https://pmc.ncbi.nlm.nih.gov/articles/PMC6133045/`
- `https://arxiv.org/abs/0804.2386`

For numerical black-hole work, singular structure is also not handled by naive self-evaluation. Depending on formulation, one uses excision, punctures, regularized variables, or other treatments that keep singular/self pieces from becoming a spurious force.

Read:

The Atlas anomaly is consistent with a known GR/PN danger: a source must not use its own singular or softened self-potential as a local motion-driving context term.

## Context-Excluded 1PN Lane

Status:
implemented.

New lane:

`R5_1pn_context_geodesic`

Legacy lane retained and renamed in the ledger:

`R5_1pn_geodesic_legacy_self_included`

Current shadow lane records:

- `24` rows
- `2` matched update intervals
- `4` sources
- `3` shadow lanes: R4 geodesic, legacy self-included 1PN, context-excluded 1PN

Mean deviation from Newtonian primary:

- R4 geodesic position: `0.00073025`
- R4 geodesic velocity: `0.000340125`
- legacy self-included 1PN position: `0.10393525`
- legacy self-included 1PN velocity: `0.782919125`
- context-excluded 1PN position: `0.000357625`
- context-excluded 1PN velocity: `0.00246325`

Max deviation from Newtonian primary:

- R4 geodesic position: `0.001238`
- R4 geodesic velocity: `0.000733`
- legacy self-included 1PN position: `0.254963`
- legacy self-included 1PN velocity: `1.697467`
- context-excluded 1PN position: `0.000464`
- context-excluded 1PN velocity: `0.004710`

Read:

The anomaly collapses when self-potential is excluded from source-motion 1PN correction. The context-excluded lane is now closer to the Newtonian primary in position than the R4 lane, while carrying a small velocity correction. The legacy lane remains valuable only as a contaminated comparison witness.

## Revised Next Implementation Step

Promote the context-excluded lane to the serious 1PN acceleration shadow candidate, keep the legacy lane as flagged negative evidence, and then compare the context-excluded lane against an EIH-derived acceleration when available.

## EIH-Derived Acceleration Diagnostic

Status:
implemented as smoke-grade finite-difference diagnostic.

The script now derives acceleration numerically from the L1 EIH Lagrangian via the Euler-Lagrange equation

`d/dt(dL/dv) - dL/dx = 0`

and compares that acceleration against:

- Newtonian primary acceleration
- R4 geodesic acceleration
- legacy self-included 1PN acceleration
- context-excluded 1PN acceleration

Ledger:

`/Users/danski2017/Desktop/Atlas_Solver_Project/codex_context/dynamic_evolution/skeleton_smoke_20260526/out/eih_acceleration_records.jsonl`

Diagnostic figure:

`/Users/danski2017/Desktop/Atlas_Solver_Project/codex_context/dynamic_evolution/skeleton_smoke_20260526/out/figures/skeleton_smoke_eih_acceleration_comparison.png`

Mean acceleration difference against EIH:

- Newtonian primary: `0.017150667`
- R4 geodesic: `0.019344667`
- legacy self-included 1PN: `5.286551`
- context-excluded 1PN: `0.002488083`

Max acceleration difference against EIH:

- Newtonian primary: `0.021854`
- R4 geodesic: `0.025442`
- legacy self-included 1PN: `8.568357`
- context-excluded 1PN: `0.003976`

Read:

The context-excluded 1PN lane is the closest tested acceleration lane to the EIH-derived acceleration. The legacy self-included lane is rejected as a self-field contaminated negative control.

## Sidebar: ADM Modeling Choices

Daniel's instinct is right: ADM contains human modeling choices.

ADM is not "the field with no decisions." It chooses a 3+1 split, lapse/shift handling, coordinate/gauge conventions, regularization strategy for point masses, boundary conditions, and numerical treatment of singularities.

The mature ADM/PN virtue is not absence of choices. It is that serious ADM work names and constrains those choices, then checks them through Hamiltonian constraints, momentum constraints, regularization consistency, coordinate comparisons, and agreement across methods.

Atlas should treat ADM as a disciplined comparison technology, not as a metaphysical authority. The live question is whether Atlas can make different, more relational modeling choices while being at least as explicit and at least as accountable.

## Revised Next Implementation Step

Promote the context-excluded 1PN lane as the serious acceleration shadow candidate in reports and diagnostics, keep the legacy lane as a negative control, then run a longer smoke to check whether the EIH agreement persists beyond three update steps.

## 12-Step Long Smoke

Status:
completed.

Run note:

`/Users/danski2017/Desktop/Atlas_Solver_Project/Relational_Labs/Relational_Labs/Atlas Codex Bridge/Dynamic Evolution/Long Smoke 12 Step 2026-05-26.md`

Read:

The context-excluded 1PN lane remains closest to the EIH-derived acceleration across all twelve update steps.

Mean acceleration difference against EIH:

- Newtonian primary: `0.017185875`
- R4 geodesic: `0.0193821875`
- legacy self-included 1PN: `5.294725125`
- context-excluded 1PN: `0.002512`

The longer run supports promoting the context-excluded lane to serious 1PN acceleration shadow candidate status. It does not promote it to primary dynamics.

## Revised Next Implementation Step

Run a modest `c_toy` sweep to test whether the EIH agreement and legacy-lane failure scale sensibly with PN strength.

## C Toy Sweep

Status:
completed.

Run note:

`/Users/danski2017/Desktop/Atlas_Solver_Project/Relational_Labs/Relational_Labs/Atlas Codex Bridge/Dynamic Evolution/C Toy Sweep 6 Step 2026-05-26.md`

Read:

The context-excluded 1PN lane remains closest to the EIH-derived acceleration at every tested `c_toy`: `4`, `5`, `8`, and `12`.

The legacy self-included lane improves as `c_toy` increases, but remains far worse than the context-excluded lane. This supports the self-contamination diagnosis.

The sweep also exposed a separate geometry sensitivity: seam counts rise sharply at larger `c_toy` under the fixed threshold. That should be treated as a threshold/radius-scaling question before it is interpreted physically.

## Revised Next Implementation Step

Run seam-threshold sensitivity at `c_toy = 8` and `c_toy = 12` to determine whether the seam rise is physical geometry or extraction-threshold artifact.

## Seam Threshold Follow-Up

Status:
completed.

Run note:

`/Users/danski2017/Desktop/Atlas_Solver_Project/Relational_Labs/Relational_Labs/Atlas Codex Bridge/Dynamic Evolution/Seam Threshold Sweep 2026-05-26.md`

Read:

The seam/node layer is strongly threshold-sensitive. At c12, seam totals move from `59` to `380` to `785` as threshold moves from `0.3` to `0.6` to `1.2`. Node totals move from `0` to `2` to `36`.

Conclusion:

Do not interpret seam/node counts physically until the fixed absolute threshold is replaced by a scale-normalized criterion.

## Revised Next Implementation Step

Replace fixed absolute seam threshold with a scale-normalized criterion tied to local crossing-shell spacing, source GCS radius, or nearest-neighbor density.
