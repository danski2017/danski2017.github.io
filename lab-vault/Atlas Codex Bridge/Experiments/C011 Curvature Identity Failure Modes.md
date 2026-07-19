---
type: experiment_note
experiment_id: C011_curvature_identity_failure_modes
status: completed
created: 2026-05-13
topics:
  - curvature-identity
  - failure-modes
  - null-scenes
  - claim-boundary
---

# C011 Curvature Identity Failure Modes

## Purpose

C011 stress-tests the staged Curvature Identity story before any public review decision.

This run asks where the story gets quieter, where branches agree, and where zero-set closure is partial.

## Outputs

Run package:

`codex_context/experiments/C011_curvature_identity_failure_modes`

Summary:

`codex_context/experiments/C011_curvature_identity_failure_modes/derived/C011_SUMMARY.json`

Compression null table:

`codex_context/experiments/C011_curvature_identity_failure_modes/derived/C011_COMPRESSION_FAILURE_MODES.csv`

Jurisdiction null table:

`codex_context/experiments/C011_curvature_identity_failure_modes/derived/C011_JURISDICTION_FAILURE_MODES.csv`

## Compression Stress Read

| Shape | Q2 p95 cross | Q6 p95 cross | Q10 p95 cross | Read |
|---|---:|---:|---:|---|
| sphere null | 1.65 | 1.40 | 1.30 | Review item: not easier than oblate under this finite-volume discretization. |
| near-sphere control | 1.65 | 1.40 | 1.30 | Similar crossing ladder; not a clean null. |
| oblate repeat | 1.60 | 1.40 | 1.30 | Repeats C008-style inward compression trend. |

The sphere null did not behave as a clean easy-compression null in this finite-volume test. That should be treated as a quadrature-null review item, not ignored.

## Jurisdiction Stress Read

| Scene | Tensor closure | Scalar closure | Tensor/Scalar p50 ratio | Read |
|---|---:|---:|---:|---|
| equal single partial closure control | 0.458 | 0.458 | 1.000 | Branch agreement where crossings exist; partial closure visible. |
| symmetric tetra context | 1.000 | 1.000 | 0.871 | Symmetry reduces branch drama but does not erase branch sensitivity. |
| distant shell context | 1.000 | 1.000 | 0.843 | Near-isotropic context remains branch-sensitive in this witness. |

## Flags

| Test | Status | Read |
|---|---|---|
| compression null sphere | review | Sphere null was not easier than the oblate repeat under this finite-volume discretization. |
| jurisdiction equal-single branch agreement | pass | Equal single context preserves tensor/scalar parity agreement on crossing rays. |
| partial closure visible | pass | Not every scene yields full zero-set closure over all directions. |

## Atlas Read

The failure-mode run strengthens the public candidate by refusing to make the story too smooth.

The jurisdiction lane is clean: it has an agreement control and a partial-closure control.

The compression null lane needs more care: finite-volume quadrature error can dominate near-surface behavior, even for a sphere. Any public compression language should stay tied to the declared diagnostic.

## Claim Boundary

C011 is an internal stress test. It does not publish anything, does not touch the website repository, and does not weaken the C010 review bundle by itself. It adds caution for lab review.

## Next

C012 should either improve the compression null with an analytic spherical control or return to the B-series galaxy observational-anchor lane.
