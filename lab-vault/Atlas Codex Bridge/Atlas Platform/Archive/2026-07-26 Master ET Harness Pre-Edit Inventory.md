---
type: pre_edit_inventory
status: archived_evidence
created: 2026-07-26
tags: [atlas-platform, et-harness, inventory, receipt]
---

# Master ET Harness Pre-Edit Inventory

## Scope

Inventory made before the 2026-07-26 Master ET Harness vault integration. No
Einstein Toolkit run, source edit, simulation, commit, push, or public-mirror
update was part of this pass.

## Findings

- Boot authority: [[../08 Boot Loader Prompt]].
- Existing ET-harness master: **none located** in the vault, Atlas repository,
  supplied earlier work orders, Desktop search, or available Claude records.
- Separately filed post-v0.1 adjudication amendment: **not located**. The merged
  2026-07-26 work order is therefore the integration authority for the current
  design basis; this is not a claim that an external copy never existed.
- Temporal material was fragmented across [[../02 Architecture and Data Flow]],
  [[../04 Operations and Validation Runbook]], [[../05 Dataset and Model Registry]],
  [[../06 Current State and Development Contract]], archived Temporal Pilot and
  SXS receipts, the compute-safety policies, the Dashboard, Goals, and queue.
- Those older records are historical evidence or current pointer surfaces. They
  are not to become competing master specifications.

## Best homes

- Canonical harness architecture, cadence, gate semantics, witness contract,
  Temporal Passport, validation, machine-health logic, and backend abstraction:
  one new master specification in `Atlas Platform/`.
- Operational Mac limits and remote-execution controls: the existing vault
  `Best Practices/Compute Safety and Remote Execution Policy` plus the repo
  `docs/COMPUTE_SAFETY_POLICY.md`, both pointed back to the master.
- CG-1, CG-2, and TR-1: one separate versioned INTERNAL research-design note,
  visible from the master but explicitly outside current doctrine and boot detail.

## Conflicts and terminology requiring adjudication

- ET timestep, extraction epoch, and Atlas temporal segment were not yet locked
  as three different cadences.
- Legacy `Q_i` proxy language risked collision with complex Weyl notation. The
  canonical complex field must be `W_ij = E_ij + i B_ij`, key
  `weyl_complex_ij`; `q_gap` must become `weyl_gap`.
- Observer/foliation-dependent quantities and invariant curvature quantities
  needed separate channels. `Psi4`, `E_ij`, `B_ij`, and W-derived products are
  not automatically invariant.
- Mesh appearance could be mistaken for temporal identity or topology. Track
  fields, registrations, and event-localization budgets must carry those claims.
- Existing fixed Mac launch limits remain incident-derived operational bounds,
  but GREEN/YELLOW/RED swap and thermal thresholds are not yet calibrated and
  must not be invented as permanent numbers.
- Existing A2 language about tensors occupying one registered tangent space is
  legitimate. It does not authorize calling the CG-1 screened derivative or
  finite ablations a tangent space.
- `submanifold`, `distance`, `holonomy`, `worldsheet`, `world-tube`, and
  invariant-boundary language require certification not present in current work.

## Preservation decision

Archived Temporal Pilot, SXS, Psi4/I/J, viewer, and safety records remain in
place with their original bounded claims. Current orientation notes may link to
the master or be corrected, but historical receipts are not rewritten.
