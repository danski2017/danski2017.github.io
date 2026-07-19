---
type: experiment_note
experiment_id: C010_curvature_identity_bundle_refresh
status: completed
created: 2026-05-13
topics:
  - curvature-identity
  - review-bundle
  - website-staging
  - claim-boundary
---

# C010 Curvature Identity Bundle Refresh

## Purpose

C010 refreshes the Curvature Identity Atlas review bundle after the compression and jurisdiction hardening runs.

It does not publish anything and does not touch the website repository.

## Inputs

- C006 hardened Curvature Identity bundle,
- C007 website skeleton,
- C003 Weyl Spheroid paper-reported compression ledger,
- C004 EMS GFRO jurisdiction ledger,
- C008 independent finite-volume compression recomputation,
- C009 clean GFRO-style jurisdiction benchmark.

## Outputs

Review bundle:

`codex_context/experiments/C010_curvature_identity_bundle_refresh/derived/curvature_identity_atlas_review_bundle_v0_3.json`

Recommendation:

`codex_context/experiments/C010_curvature_identity_bundle_refresh/derived/C010_REVIEW_RECOMMENDATION.json`

Handoff:

`codex_context/experiments/C010_curvature_identity_bundle_refresh/reports/C010_WEBSITE_HANDOFF.md`

## Decision

Keep C003 and C004 as the public-review anchors. Add C008 and C009 as supporting hardening panels.

Atlas reason:

```text
Do not replace provenance with a different diagnostic.
Layer the evidence and label the channels.
```

## Compression Comparison

| Order | C003 paper multipole r_tau/a | C008 finite-volume r_tau/a | Delta |
|---:|---:|---:|---:|
| 2 | 2.610 | 1.600 | -1.010 |
| 4 | 1.630 | 1.460 | -0.170 |
| 6 | 1.330 | 1.380 | 0.050 |
| 8 | 1.170 | 1.320 | 0.150 |
| 10 | 1.080 | 1.280 | 0.200 |

Read: C008 does not numerically replace C003, but it supports the same directional compression pattern.

## Jurisdiction Comparison

| Scene | Tensor/Scalar p50 ratio | Closure minimum |
|---|---:|---:|
| single equal context D10 | 1.000 | 0.438 |
| single heavy context D10 | 1.570 | 1.000 |
| binary context balanced | 1.274 | 1.000 |
| ring context 12 | 1.084 | 1.000 |
| cloud context 48 | 1.278 | 1.000 |

Read: C009 gives a clean branch-sensitivity benchmark. C004 remains the EMS provenance anchor.

## Claim Boundary

C010 is a lab-review refresh only. It is not publication, not a website update, and not permission to replace provenance anchors without review.

## Next

The Curvature Identity package is now ready for lab review as a staged public candidate. The next science run should either deepen C008/C009 with failure modes or return to the B-series galaxy/averaging line.
