---
type: experiment_note
experiment_id: C008_weyl_spheroid_fresh_recompute
status: completed
created: 2026-05-13
topics:
  - weyl-spheroid
  - compression
  - electric-weyl
  - finite-volume
  - evidence-hardening
---

# C008 Weyl Spheroid Fresh Recompute

## Purpose

C008 is the first local recomputation pass for the Weyl Spheroid compression lane.

C003 ledgered the paper-reported multipole compression radii. C008 asks a narrower independent question:

```text
If a retained high-resolution finite-volume spheroid is the reference,
how far away must a compressed quadrature description sit before its
electric-Weyl tensor witness is faithful under tau = 1e-3?
```

## Scene

- uniform-density oblate spheroid,
- `a = 1`,
- `c = 0.5`,
- `rho0 = 1`,
- `G = 1`,
- retained reference: 24,576 deterministic volume nodes,
- witness panel: 96 exterior directions,
- tolerance: `tau = 1e-3`.

## Outputs

Run package:

`codex_context/experiments/C008_weyl_spheroid_fresh_recompute`

Summary:

`codex_context/experiments/C008_weyl_spheroid_fresh_recompute/derived/C008_SUMMARY.json`

Radius/error ledger:

`codex_context/experiments/C008_weyl_spheroid_fresh_recompute/derived/C008_RADIUS_ERROR_LEDGER.csv`

Website compression patch candidate:

`codex_context/experiments/C008_weyl_spheroid_fresh_recompute/derived/curvature_identity_compression_recompute_patch_v0_1.json`

## Result

| Order | Source nodes | C008 p95 E-Fro r_tau/a | C008 strict max E-Fro r_tau/a | C003 paper multipole r_tau/a |
|---:|---:|---:|---:|---:|
| Q2 | 512 | 1.60 | 1.60 | 2.61 |
| Q4 | 1,000 | 1.46 | 1.46 | 1.63 |
| Q6 | 1,728 | 1.38 | 1.38 | 1.33 |
| Q8 | 2,744 | 1.32 | 1.32 | 1.17 |
| Q10 | 4,096 | 1.28 | 1.28 | 1.08 |

## Read

C008 does not numerically reproduce the paper's exact multipole compression ladder. It is an independent finite-volume benchmark, so the diagnostic is different.

The important agreement is qualitative and structural: increasing retained order moves the faithful approximation radius inward.

Atlas reading:

```text
Compression is real, diagnostic-dependent, and claim-bounded.
```

## Claim Boundary

This is a weak-field finite-volume electric-Weyl recomputation. It is not a replacement for the Weyl Spheroid paper, not a physical boundary, not a new field equation, and not a solved Ricci-to-Weyl dynamical handoff.

## Next

C009 should build a clean GFRO jurisdiction benchmark so the Curvature Identity Atlas has the same kind of independent hardening for source/context parity that C008 gives the compression lane.
