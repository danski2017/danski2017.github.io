---
type: platform_change_receipt
status: sandbox_complete_repeat
created: 2026-07-18
tags: [atlas-platform, node0, geometric-delta, finite-source, receipt]
---

# 2026-07-18 Receipt — Node 0 Delta Accounting Stage 1–4

## Scope

Codex executed the bounded first lane of experiment
`RL_NODE0_DELTA_ACCOUNTING_001`: Node 0 self-null, one finite spherical source,
registered metric/volume/stress-energy/spatial-Ricci/electric-Weyl channels,
radial and cumulative ledgers, three-domain sweep, two-resolution sweep,
one-source ablation back to Node 0, exact x/y registration round-trip, alternate
Node 0 sensitivity, and applicable audit renders.

No viewer behavior changed. No ET solve or evolution was launched. The run
reconstructed the existing ET-validated profile A and remained `local-light`
under a 250,000-node ceiling. Approved host probe: 8 GiB RAM, 8 CPUs.

## Artifacts

- Packet: `analysis/node0_delta_accounting/RL_NODE0_DELTA_ACCOUNTING_001/`
- Passport: packet `PASSPORT.txt`
- Return packet: packet `RETURN_PACKET.md`
- Manifest: packet `MANIFEST.json`
- Config: `configs/node0_delta_accounting/RL_NODE0_DELTA_ACCOUNTING_001.json`
- Runner: `scripts/node0_delta_accounting/run_node0_delta_accounting_001.py`
- Tests: `scripts/node0_delta_accounting/tests/test_node0_delta_accounting_001.py`

Recorded SHA-256 at closeout:

- Manifest: `2fef36e948651744148c17849908e2ab3412d1b4f3ee84f3106f07151e53b6ee`
- Return packet: `f11526ac6584506820725f21e636da793dac967f36f7cb1c59417206f650c802`
- Runner: `13456b1205b1b82c9a4e22a2177e32a2cfd27a060ce749ce3a4ab3d89e1a5ce8`

## Measured boundary

- Node 0 null: `max |chi_V| = 0`; `max |R3| = 3.33e-16`; `max |E_ij| = 1.85e-17`.
- Fine baseline (`dx=1.5`, ledger radius 34.5): `B_T=1.602658`,
  `B_R2=0.871926`, `B_W2=0.100100`, `Delta0 V=34234.858`.
- Matter support ends near grid radius 8.49 under the declared relative density
  threshold. Exact vacuum Ricci is zero; the stored exterior Ricci contribution
  is explicitly a finite-difference/Hamiltonian residual, not physical support.
- Tail fits: `chi_V ~ r^-0.991`; `||E||_gamma ~ r^-2.876` on the bounded fine lane.
- Domain endpoints give `Delta0 V` 33172.9, 59679.3, 93688.2 with fitted power
  1.944. More decisively, the declared `psi-1 ~ 1/r` continuation implies
  `J_V-1 ~ 1/r` and `Delta0 V(R) ~ R^2`: no finite global volume budget exists
  in this Node 0 lane.
- Stress-energy saturates. Curvature-square ledgers approach plateaus, but the
  two-resolution `B_R2` and `B_W2` changes remain about 9%; convergence is not
  established. Fine-grid Hamiltonian relative L2 residual inside matter support
  is about 9.18%.
- The one-source ablation-of-delta identity closes exactly by construction.

## Claim boundary and decision

Status remains **SANDBOX / Seed**. The packet does not establish a conservation
law, Ricci-to-Weyl conversion, datum-independent volume, cross-regime information
retention, or public physics claim. Full four-dimensional `T_mu_nu`, `G_mu_nu`,
and `R_mu_nu` were unavailable and were not fabricated.

Required return recommendation: **REPEAT**. A third safe resolution and an
independent curvature implementation are owed before stabilization or morphology
promotion. Two-source interaction remains properly deferred to Stage 8.

## QA

Eleven unit/packet tests passed. All 46 files listed in the packet manifest matched
their SHA-256 records. Thirteen applicable named audit views were generated;
the inapplicable two-source view has an explicit `INTERACTION/NOT_RUN.json`.
