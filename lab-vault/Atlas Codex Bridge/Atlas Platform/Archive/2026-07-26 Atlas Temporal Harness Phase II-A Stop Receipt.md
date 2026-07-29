---
type: implementation_receipt
status: partial_stopped_safely
created: 2026-07-26
updated: 2026-07-26
tags: [atlas-platform, temporal-harness, local-et, machine-health, stop-condition]
---

# Atlas Temporal Harness Phase II-A Stop Receipt

## Outcome

Phase II-A implemented and tested the frozen `LOCAL_ET` adapter and hardened
macOS telemetry, but did not launch a real ET segment. A mandatory machine-health
stop condition was reached during telemetry probing and was honored.

## Implemented

- read-only ET discovery and environment receipt;
- hash-frozen executable, source parfile, ThornList, OptionList, compiler, and
  selected configuration identity;
- passive total/process/system/compressed memory, swap, pressure, CPU/load,
  elapsed-time, and disk-growth telemetry;
- configuration-driven provisional swap policy and explicit execution latch;
- LOCAL_ET preflight/derive/launch/monitor/stop/runtime/checkpoint/extraction/
  resume lifecycle behind the unchanged Phase-I interface;
- Carpet checkpoint discovery requiring readable HDF5 and ET timestep metadata,
  never filename alone;
- HDF5 scientific-field metadata inventory and conservative operational witness;
- missing-executable and execution-disabled fail-closed tests with no ET launch.

## Stop event

`memory_pressure -l critical -s 1` was mistakenly invoked during command-format
probing as though it were passive. It is an active load generator. The initial
tool session was terminated immediately, a surviving child was found and
terminated, and no Cactus process was present. Swap rose from roughly 2.85 GiB
to a peak near 21.25 GiB, later receding to roughly 4.64 GiB but remaining above
baseline. `memory_pressure -Q` was then GREEN, but the work order explicitly
forbids pushing through meaningful swap escalation.

No Einstein Toolkit source, parameter file, executable, build configuration, or
output was modified. No real ET executable was launched.

## Evidence

- Implementation report:
  `analysis/atlas_temporal_harness/phase_ii_a/PHASE_IIA_IMPLEMENTATION_REPORT.md`
- Discovery receipt:
  `analysis/atlas_temporal_harness/phase_ii_a/local_et_discovery/LOCAL_ET_ENVIRONMENT_RECEIPT.json`
- Stop receipt:
  `analysis/atlas_temporal_harness/phase_ii_a/MACHINE_HEALTH_STOP_RECEIPT.json`
- Blocked run:
  `analysis/atlas_temporal_harness/temporal_runs/PHASE_IIA_LOCAL_ET_BLOCKED_20260726/`
- Tests: 30/30 harness and 20/20 Temporal Pilot pass.

## Claim state

Preserved: **ATLAS TEMPORAL HARNESS CONTROL SPINE — IMPLEMENTED /
MOCK-BACKEND VALIDATED**.

Supported engineering statement: **LOCAL_ET ADAPTER IMPLEMENTED / UNIT- AND
FAIL-CLOSED-VALIDATED; REAL SMOKE BLOCKED BY MACHINE-HEALTH STOP CONDITION**.

Not earned: real-segment smoke validation, restart validation, segmented versus
uninterrupted consistency, no-swap envelope certification, E/B/W validation,
five-source NR, or any temporal science claim.

## Next lawful action

Restart or otherwise return the Mac to a known quiet baseline, recheck swap using
passive commands only, reverify the frozen profile, then authorize exactly one
new two-iteration run identity. Phase II-B must wait until the Phase-II-A real
segment, restart, and control conditions pass safely.
