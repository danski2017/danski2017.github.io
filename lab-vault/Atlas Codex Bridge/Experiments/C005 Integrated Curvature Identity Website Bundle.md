---
type: experiment_note
status: completed
created: 2026-05-13
experiment_id: C005_integrated_curvature_identity_website_bundle
topics:
  - curvature-identity
  - website-bundle
  - public-tool
  - integration
---

# C005 Integrated Curvature Identity Website Bundle

## Status

Completed website handoff bundle.

Package:

`codex_context/experiments/C005_integrated_curvature_identity_website_bundle`

Script:

`codex_context/scripts/c005_integrated_curvature_identity_website_bundle.py`

Bundle:

`codex_context/experiments/C005_integrated_curvature_identity_website_bundle/derived/curvature_identity_atlas_bundle_v0_1.json`

Package size:

`0.021 MiB`

## Purpose

Merge the first-pass Curvature Identity Atlas channels into one website-ready payload.

Sources:

- C002 base budget/object payload,
- C003 Weyl Spheroid compression patch,
- C004 GFRO jurisdiction patch.

## Bundle Contents

| Channel | Count | Source |
|---|---:|---|
| object cards | 12 | C002 |
| budget ladder rows | 12 | C002 |
| compression witnesses | 5 | C003 |
| jurisdiction witnesses | 5 | C004 |

Recommended website target:

```text
data/curvature_identity_atlas_bundle_v0_1.json
```

Recommended page:

```text
curvature-identity-atlas.md
```

## Website Handoff

Handoff file:

`codex_context/experiments/C005_integrated_curvature_identity_website_bundle/reports/C005_WEBSITE_HANDOFF.md`

The page should show:

- budget ladder,
- selected object cards,
- jurisdiction examples,
- compression witnesses,
- links to Three Measures and Weyl Spheroid papers,
- claim boundary footer.

## Claim Boundary

C005 is an integration package only. It adds no new evidence beyond C002-C004.

Non-claims:

- no new field equation,
- no new force,
- no GR replacement,
- no observable boundary claim,
- no topology certification,
- no physical compression boundary,
- no solved dynamical handoff.

## Phase Read

The Curvature Identity Atlas first pass is now operational as a public-tool data bundle.

Next work belongs either to the website implementation lane or to deeper C-series hardening:

- C006: improved particle radius/radius-basis uncertainty notes,
- C007: website copy and interaction skeleton for the hardened bundle,
- C008: fresh Weyl Spheroid recomputation,
- C009: GFRO jurisdiction benchmark from a clean two-source and many-source ladder.
