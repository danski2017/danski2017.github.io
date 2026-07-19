---
type: platform_change_receipt
status: sandbox_complete_repeat
created: 2026-07-18
tags: [atlas-platform, node0, geometric-delta, asymptotic-accounting, receipt]
---

# 2026-07-18 Receipt — Node 0 Delta Accounting Repeat / Asymptotic Pass

## Scope

Codex executed `RL_NODE0_DELTA_ACCOUNTING_002`, the bounded repeat of the first
Node 0 finite-source lane. The packet adds a safe third resolution, an
independently coded semi-analytic conformal-curvature implementation,
shell-normalized volume diagnostics, asymptotic coefficient fits, an
interior-closure/exterior-tail ledger, a five-shell matter-boundary audit,
constraint residual decomposition, retained domain and Node 0 sensitivities,
and the one-source ablation serialization control.

No viewer behavior or doctrine files changed. No ET solve or evolution was
launched. The fine rung was `61^3 = 226,981` nodes with a conservative peak
estimate of 519.5 MiB (6.3% of the approved 8 GiB host). The proposed farther
fixed-`dx` domain would require `73^3 = 389,017` nodes and was not launched
because it exceeds the declared 250,000-node ceiling.

## Artifacts

- Packet: `analysis/node0_delta_accounting/RL_NODE0_DELTA_ACCOUNTING_002/`
- Passport: packet `PASSPORT.txt`
- Return packet: packet `RETURN_PACKET.md`
- Manifest: packet `MANIFEST.json`
- Config: `configs/node0_delta_accounting/RL_NODE0_DELTA_ACCOUNTING_002.json`
- Runner: `scripts/node0_delta_accounting/run_node0_delta_accounting_002.py`
- Tests: `scripts/node0_delta_accounting/tests/test_node0_delta_accounting_002.py`

Recorded SHA-256 at closeout:

- Manifest: `c0050f57dfed28ecaa1c5987398a6aa2b872a89883dcd12f9ff405fe03ad2639`
- Return packet: `ab454c500fa653e763e99a503e9094f7122a5fae73128738a4c7ff8d678d541d`
- Runner: `d9b2bb97057a1c8d15ef4678514fe3be722611661e2f6f88d2c244ed2c5a5fa8`
- Parent manifest (unchanged): `2fef36e948651744148c17849908e2ab3412d1b4f3ee84f3106f07151e53b6ee`

## Measured boundary

- At common `R=30`, mid-to-fine `B_R2` and `B_W2` changes are 4.604% and
  4.521%. Their estimated convergence orders are 1.512 and 1.517, but the
  declared 3% promotion threshold is not met.
- Fine primary/independent comparison gives electric-Weyl p95 pointwise
  relative error 0.966%, while integrated `B_R2` and `B_W2` residuals remain
  7.131% and 8.998%. These residuals improve monotonically with resolution but
  do not clear the 3% integrated tolerance.
- Fine canonical tail fits give `p_chi=0.9882`, `p_E=2.8780`,
  `p_E2=5.7612`, and `p_Sigma=1.0605`. Exponents are stable, but the `E^2`
  amplitude spread across declared runs/windows is 24.116%, beyond the 15%
  tail-stability gate.
- `Sigma_V` passes its stability gate: exponent spread 0.0195 and amplitude
  spread 6.645%. The raw cumulative `Delta0 V` divergence remains falsified and
  is not recast as a finite budget.
- Matter support closes at `R_matter=8.499`. Exact independent exterior
  `max |R3|=2.64e-19`, while the electric-Weyl channel persists. This is a
  diagnostic regime transition, not a physical conversion boundary.
- Support-interior Hamiltonian relative L2 improves from 15.126% to 8.495% to
  5.467%, narrowly missing the declared 5% gate.

## Gate decision

- Gate A — third-resolution curvature-ledger convergence: **FAIL**
- Gate B — independent integrated curvature agreement: **FAIL**
- Gate C — full asymptotic amplitude stability: **FAIL**
- Gate D — shell-normalized volume accounting: **PASS**
- Gate E — matter/Ricci-residual/Weyl regime separation: **PASS**
- Gate F — constraint control: **FAIL**

Status remains **SANDBOX / Seed**. No conservation law, Ricci-to-Weyl
conversion, universal source-to-tail relation, or compactness scaling is
claimed. The finite global Node 0 volume-displacement budget remains falsified.

Required return recommendation: **REPEAT**.

## QA

Eight unit/packet tests passed. All 37 files listed in the packet manifest
matched their SHA-256 records. Thirteen required ledger-backed figures were
generated and visually inspected. The parent packet manifest remained unchanged.
