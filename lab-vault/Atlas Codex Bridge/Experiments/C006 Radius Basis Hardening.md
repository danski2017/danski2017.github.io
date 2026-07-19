---
type: experiment_note
experiment_id: C006_radius_basis_hardening
status: completed
created: 2026-05-13
topics:
  - curvature-identity
  - website
  - radius-basis
  - claim-boundary
---

# C006 Radius Basis Hardening

## Purpose

C006 hardens the public Curvature Identity Atlas payload by making every radius a declared, typed input.

This run does not recalculate budget, jurisdiction, or compression. It protects interpretation.

## Source

`codex_context/experiments/C005_integrated_curvature_identity_website_bundle/derived/curvature_identity_atlas_bundle_v0_1.json`

## Outputs

Primary hardened bundle:

`codex_context/experiments/C006_radius_basis_hardening/derived/curvature_identity_atlas_bundle_v0_2.json`

Patch-only view:

`codex_context/experiments/C006_radius_basis_hardening/derived/curvature_identity_radius_basis_patch_v0_1.json`

Website handoff:

`codex_context/experiments/C006_radius_basis_hardening/reports/C006_WEBSITE_HANDOFF.md`

## Radius Basis Classes

| Class | Count | Rows | Public Rule |
|---|---:|---|---|
| measured_physical_radius | 3 | proton, earth, sun | Show as observed or conventionally declared physical inputs, while preserving spherical-model language. |
| declared_effective_radius | 1 | fe-56_nucleus | Show as an effective modeling radius; avoid surface or boundary wording. |
| illustrative_scale | 2 | electron, hydrogen_atom | Show with an illustrative badge and visible warning. |
| declared_model_radius | 3 | white_dwarf, ns_1.4_msun, ns_max_2.2_msun | Show as model points; avoid population or equation-of-state claims. |
| derived_horizon_radius | 3 | bh_10_msun, sgr_astar, ton_618 | Show as derived Schwarzschild scales; avoid material-surface wording. |

## Public Payload Addition

The hardened bundle adds:

- `radius_basis` metadata to every object,
- a global `radius_basis_notice`,
- a new public-copy section for radius basis,
- safer non-claims around effective, illustrative, model, and horizon radii.

## Claim Boundary

Radius-basis labels are interpretation guards only. They do not add evidence beyond C001-C005 and do not convert effective, illustrative, model, or horizon scales into physical surfaces.

## Website Recommendation

Use:

`data/curvature_identity_atlas_bundle_v0_2.json`

The website should show a compact badge next to each radius and keep the per-object warning available in hover text, a disclosure panel, or a details drawer.
