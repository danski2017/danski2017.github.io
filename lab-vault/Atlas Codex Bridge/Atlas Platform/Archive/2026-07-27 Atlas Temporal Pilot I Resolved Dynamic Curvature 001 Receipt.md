---
type: completion_receipt
status: full_pass
created: 2026-07-27
updated: 2026-07-27
tags: [atlas-platform, temporal-harness, teukolsky-wave, curvature, restart, full-pass]
---

# Atlas Temporal Pilot I Resolved Dynamic Curvature 001 Receipt

## Decision

**FULL PASS — RESOLVED TEMPORAL CURVATURE HISTORY OBSERVED /
ENGINEERING-VALIDATED IN THE DECLARED TEUKOLSKY BENCHMARK.** The canonical
temporal E/B witness pipeline and bounded ET-to-Atlas loop are operational in
this named Mac/resource scope.

## Scene and cadence

- Existing Einstein Toolkit even-parity m=2 Teukolsky Eppley packet, amplitude
  `1e-3`, vacuum ML_BSSN evolution with 1+log lapse and Gamma-driver shift.
- One uniform, half-cell-staggered physical grid: 33^3 points on
  `[-4.125,3.875]^3`, `dx=0.25`; 39^3 serialized points include three ghost
  zones; `dt=0.0625`.
- Certified epochs: iteration/time 0/0, 2/0.125, and 4/0.25.
- Segment B genuinely restarted from Segment A's exact t1 raw HDF5 checkpoint.
  Source and restart-input SHA-256:
  `fd024eb5781dc1b6b21c0a0b032188708d6b20ed9b220b335415e53cc7b4f2be`.

Calibration attempt 001 is preserved as a fail-closed record: a centered grid
sampled the analytic coordinate-axis singularity and produced 39 NaNs.
Calibration attempt 002 adopted the documented half-cell stagger, passed, and
bounded the production cadence.

## Numerical result

The declared comparison currency is the peak tensor-Frobenius temporal change
against the matching conservative peak extraction/registration floor.

| Transition | E change / floor / ratio | B change / floor / ratio | Status |
|---|---:|---:|---|
| t0->t1 | 0.002495516 / 0.034485234 / 0.072365 | 0.041544118 / 0.004137509 / 10.040853 | E unresolved; B strong resolved |
| t1->t2 | 0.012420636 / 0.033867711 / 0.366740 | 0.040038597 / 0.008107144 / 4.938681 | E unresolved; B strong resolved |

The B channel exceeds both the required ratio-1 threshold and the stronger
pilot ratio-3 target on both transitions. E changes are measured and retained,
but do not clear their matching floors. B/E peak amplitude ratios evolve from
0 at t0 to 0.25749 at t1 and 0.54775 at t2.

Eigenvalue and principal-direction changes are recorded only where
`eigen_gap_full` permits interpretation. They remain diagnostic because this
pilot did not certify a temporal angular/eigenvalue uncertainty floor.

## Evolution, extraction, and resource gates

- All Segment A/B Evolution Gates and all three epoch Extraction Gates pass.
- Hamiltonian RMS: `2.80177633e-4`, `2.82475125e-4`, `2.88507837e-4` from
  t0 through t2; momentum-coordinate-norm RMS: `0`, `4.2292934e-5`,
  `8.3102406e-5`. Values remain finite and bounded over the short pilot.
- Segment A peak RSS: 133,103,616 bytes; Segment B peak RSS: 140,132,352
  bytes. Pressure remained green and swap growth was zero in both segments.
- The calibrated bounded segments met the declared unattended-execution safety
  conditions. This is run-specific evidence, not a general Mac envelope.
- The ET executable SHA-256 is
  `f73db961bfc995a9157d10c46c2144d50b93afbb77faebdd9ff1140e4ccfc65b`.
  It is exact local evidence and retains Homebrew dynamic-library dependencies;
  it is not represented as a portable standalone binary.

## Claim ceiling and nonclaims

Earned only for the declared benchmark:

- resolved temporal curvature history: observed / engineering-validated;
- temporal E/B witness pipeline: operational;
- bounded ET-to-Atlas temporal loop: operational.

Not earned: continuum convergence; publication-grade or astrophysical NR
accuracy; a general production/safety envelope; gauge-independent, invariant,
or source-resolved history; compression-retention behavior; Commons; holonomy;
return-map or constraint-manifold memory; attribution; or new gravitational
physics. `weyl_gap` remains definition-blocked.

## Artifacts and recovery

- Canonical artifact root:
  `analysis/atlas_temporal_harness/temporal_pilot_i_resolved_dynamic_curvature_001/`
- Completion ZIP:
  `ATLAS_TEMPORAL_PILOT_I_RESOLVED_DYNAMIC_CURVATURE_001_COMPLETE_OUTPUT.zip`
- ZIP SHA-256: `b9e238444dce0085c20cd7157744dbc06257a8c6ca5cc1c1adda7f7d53c49f8c`
- Exact pre-edit vault backups and hash manifest:
  `backups/atlas_temporal_harness/temporal_pilot_i_pre_vault_20260727/`

The bundle contains the exact work order, scene decision, build/executable
snapshot, failed and successful calibration evidence, raw checkpoint lineage,
three epoch arrays and witnesses, temporal differences and uncertainty budget,
restart receipt, Temporal Passport, 2D/3D renders, tests, inventories, and
certification receipts.

## Next gate

Atlas is ready for design of a minimal source-model-agnostic **Temporal Pilot
II — Resolved vs Compressed Curvature Retention** experiment. Launch is not
automatic; it requires its own work order, passport, registration contract,
uncertainty comparison, and bounded resource preflight.
