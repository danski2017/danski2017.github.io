---
title: Compute Safety and Remote Execution Policy
status: active
date: 2026-07-26
tags:
  - atlas
  - operations
  - compute-safety
  - numerical-relativity
---

# Compute Safety and Remote Execution Policy

## Lab Rule

The 8 GiB Mac mini is the Atlas cockpit, not the heavy-compute engine. Use it for
planning, code, inspection, compact ET/HDF5 ingestion, audits, plotting, and the
viewer. Offload large numerical-relativity solves and production evolutions to a
verified remote machine.

**A sandbox is not necessarily a remote computer.** Filesystem/process isolation
can still run directly on the Mac and consume its RAM, swap, CPU, and disk. No
heavy job starts until the execution hostname and physical memory are positively
recorded.

## Launch Gate

Every model run must declare:

- local or remote execution host;
- physical RAM and CPU count;
- unknown count and conservative peak-memory estimate;
- output/storage estimate;
- rank and thread count;
- checkpoint and termination method;
- resource class: `local-light`, `remote-medium`, or `remote-heavy`.

Unknown host or unknown memory means **do not launch**.

On the Mac mini, coupled FUKA binaries, production ET evolutions, jobs estimated
above 2 GiB before overhead, jobs expected to swap, and unattended heavy compute
are prohibited without a specific written founder override.

## Temporal Harness Machine Gate — 2026-07-26

[[../Atlas Platform/11 ET Temporal Harness Master Specification]] governs future
segment-level machine adjudication. Swap is a first-class evolution gate. The
local objective is the largest stable **NO-SWAP** envelope, not the largest run
that can be forced to finish.

- GREEN: no swap activity/growth and stable pressure, thermals, throughput, and I/O.
- YELLOW: an uncertified compression, pressure, thermal, I/O, or slowdown trend;
  checkpoint, shorten/hold, and diagnose.
- RED: swap use/growth, hardware warning, severe pressure/throttling, unbounded
  I/O, stalled progress, or unsafe process state; stop and preserve restart evidence.

These traffic lights are qualitative until measured. Do not invent permanent
numeric swap or thermal thresholds. The existing 2 GiB and related prohibitions
remain conservative incident-derived launch bounds, not calibration results.

The future local ladder is H0 at approximately `48^3` or smaller, H1 at
approximately `64^3`, and H2 at approximately `96^3` only after clear no-swap
headroom. `128^3` is not routine; AMR is a separate resource multiplier. The
fixed-step `32^3/48^3/64^3` calibration is queued, not authorized by this note.
Prefer a dedicated Linux backend for sustained ET work. The portable flow is
Mac cockpit -> ET Adapter -> backend -> checkpoint + extraction -> Atlas; Apple
eGPU support is not a dependency.

## 2026-07-11 FUKA Incident

The near miss was a FUKA/Kadath unequal-mass BNS XCTS initial-data solve: one
three-dimensional constraint-solved slice, not a time evolution. The direct
restart formed a 48,397-unknown system with an estimated 18.74 GB dense matrix
before solver/MPI overhead on an 8 GiB Mac. No coupled Newton step completed.

The process group was terminated after the hardware warning. Isolated stars and
the shared binary seed survived; there is no fused BNS result yet. This was a
resource stop, not nonconvergence and not a physics result.

For this case, use at least 32 GiB RAM remotely; 64 GiB is preferred.

## Canonical Repo Records

- `docs/COMPUTE_SAFETY_POLICY.md`
- `docs/et_tov3_scout/ATLAS_FUKA_BNS_RESOURCE_INCIDENT_001.md`
- `analysis/et_tov3_scout/FUKA_BNS_BRIDGE_001/gate_status.json`
- `analysis/et_tov3_scout/FUKA_BNS_BRIDGE_001/run/bns_scout/RESOURCE_STOP_001.json`

This note is the Obsidian operational mirror. The repo policy controls execution.
