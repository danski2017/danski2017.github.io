---
type: experiment_note
experiment_id: C012_analytic_spherical_compression_control
status: completed
created: 2026-05-13
topics:
  - curvature-identity
  - compression
  - analytic-control
  - failure-modes
---

# C012 Analytic Spherical Compression Control

## Purpose

C012 follows up the C011 sphere-null review item with an analytic control.

Instead of comparing one finite-volume sphere against another finite-volume reference, C012 compares finite-volume sphere approximations against the exact exterior unit-sphere tidal tensor.

## Analytic Reference

By the shell theorem, the exterior field of a uniform unit sphere equals the field of a point mass at the center.

For this run:

- sphere radius: `R = 1`,
- density: `rho = 1`,
- mass: `4 pi / 3`,
- `G = 1`,
- tolerance: `tau = 1e-3`.

## Outputs

Run package:

`codex_context/experiments/C012_analytic_spherical_compression_control`

Summary:

`codex_context/experiments/C012_analytic_spherical_compression_control/derived/C012_SUMMARY.json`

Radius/error ledger:

`codex_context/experiments/C012_analytic_spherical_compression_control/derived/C012_ANALYTIC_SPHERE_RADIUS_ERROR_LEDGER.csv`

## Result

| Order | Nodes | p95 cross r/R | max cross r/R | Near-surface p95 error |
|---|---:|---:|---:|---:|
| Q2 | 512 | 1.65 | 1.65 | 3.828 |
| Q4 | 1,000 | 1.48 | 1.50 | 4.682 |
| Q6 | 1,728 | 1.40 | 1.40 | 4.416 |
| Q8 | 2,744 | 1.34 | 1.34 | 3.954 |
| Q10 | 4,096 | 1.28 | 1.30 | 3.959 |

## Flags

| Test | Status | Read |
|---|---|---|
| analytic sphere mass closure | pass | Quadrature mass closes against analytic sphere volume. |
| analytic sphere order improves crossing | pass | Higher quadrature order reaches tau closer to the surface. |
| near-surface quadrature warning | review | Near-surface finite-volume point sampling remains noisy relative to analytic sphere. |

## Atlas Read

C012 clarifies C011.

The sphere-null issue is not a physics failure. It is a numerical warning:

```text
finite-volume point sampling near a source boundary can dominate the compression witness.
```

This means the public compression story should not use near-surface spherical null language casually. It should stay with declared diagnostics, tolerances, and distance-from-source language.

## Claim Boundary

C012 is an internal analytic control. It does not publish anything and does not touch the website repository.

## Next

The Curvature Identity package now has:

- paper anchors,
- independent hardening,
- failure-mode caution,
- analytic control.

The next high-value lane is likely returning to B015, the galaxy observational-anchor run.
