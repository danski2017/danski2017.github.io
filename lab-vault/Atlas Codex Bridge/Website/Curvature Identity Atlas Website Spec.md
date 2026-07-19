---
type: website_spec
status: draft
created: 2026-05-13
source_experiment: C001_curvature_identity_atlas_prototype
topics:
  - website
  - curvature-identity
  - calculator
  - public-tool
---

# Curvature Identity Atlas Website Spec

This is the first website-tool spec for the Curvature Identity Atlas.

Source package:

`codex_context/experiments/C001_curvature_identity_atlas_prototype`

Website payload:

`codex_context/experiments/C002_curvature_identity_website_payload/derived/curvature_identity_atlas_payload_v0_1.json`

Compression patch:

`codex_context/experiments/C003_weyl_spheroid_compression_extraction/derived/curvature_identity_compression_patch_v0_1.json`

Jurisdiction patch:

`codex_context/experiments/C004_gfro_backed_jurisdiction_examples/derived/curvature_identity_jurisdiction_patch_v0_1.json`

Integrated website bundle:

`codex_context/experiments/C005_integrated_curvature_identity_website_bundle/derived/curvature_identity_atlas_bundle_v0_1.json`

Hardened website bundle:

`codex_context/experiments/C006_radius_basis_hardening/derived/curvature_identity_atlas_bundle_v0_2.json`

Website skeleton:

`codex_context/experiments/C007_curvature_identity_website_skeleton/derived/curvature_identity_website_skeleton_v0_1.json`

Compression hardening candidate:

`codex_context/experiments/C008_weyl_spheroid_fresh_recompute/derived/curvature_identity_compression_recompute_patch_v0_1.json`

Jurisdiction hardening candidate:

`codex_context/experiments/C009_clean_gfro_jurisdiction_benchmark/derived/curvature_identity_jurisdiction_clean_benchmark_patch_v0_1.json`

Lab-review bundle:

`codex_context/experiments/C010_curvature_identity_bundle_refresh/derived/curvature_identity_atlas_review_bundle_v0_3.json`

Failure-mode caution:

`codex_context/experiments/C011_curvature_identity_failure_modes/derived/C011_SUMMARY.json`

Analytic compression control:

`codex_context/experiments/C012_analytic_spherical_compression_control/derived/C012_SUMMARY.json`

## Public Tool Name

Curvature Identity Atlas

## Public Promise

Give a reader a way to inspect three finite-source identity channels:

```text
what a source carries
where it matters
when its detail fades
```

## Inputs

Minimum:

- object preset,
- custom mass,
- custom radius,
- radius basis.

Optional:

- context mass,
- source/context separation,
- quadrupole fraction or source-detail coefficient,
- compression tolerance.

## Outputs

Primary:

- exterior Weyl-electric square budget,
- log10 budget,
- budget per mass,
- mean density.

Optional:

- source/context jurisdiction radius,
- jurisdiction fraction of separation,
- compression radius,
- compression radius in source radii.

Always visible:

- claim ceiling,
- radius-basis note,
- static-vs-dynamic note.

## Suggested First Presets

- electron, illustrative radius warning,
- proton,
- Fe-56 nucleus,
- hydrogen atom,
- Earth,
- Sun,
- white dwarf,
- neutron star,
- black hole,
- Sgr A*,
- TON 618.

## Public Copy Draft

```text
Finite sources do not all carry gravitational identity in the same way.
The Curvature Identity Atlas computes a declared source's exterior trace-free
tidal-square budget, compares it against a context when supplied, and shows
how approximation tolerance can define a compression scale.
```

Claim sentence:

```text
This is weak-field curvature bookkeeping inside declared source models, not a
new field equation, force, or observable boundary.
```

## First Page Layout

1. Short intro sentence.
2. Preset selector.
3. Mass/radius controls.
4. Budget output card.
5. Jurisdiction optional panel.
6. Compression optional panel.
7. Claim boundary footer.
8. Link to Three Measures paper.
9. Link to Weyl Spheroid paper.

## Visual Ideas

- log-scale budget ladder,
- density vs budget-per-mass scatter,
- black-hole inversion line,
- proton / neutron-star plateau callout,
- hydrogen atom cliff callout.

## Claim Hazards

- Do not call budget an observable.
- Do not imply atomic gravity affects chemistry.
- Do not imply black holes are weak objects in ordinary language; say curvature-budget dilute under the declared exterior budget measure.
- Do not present compression as a physical boundary.
- Do not claim the dynamical handoff is solved.

## Current Implementation Status

C002 has produced the first website-ready JSON payload. It can be used as a static data file or as the seed for a JavaScript calculator.

Next needed improvement:

Compression is backed by C003's Weyl Spheroid paper-result ledger. Jurisdiction is backed by C004's EMS GFRO source/context summaries.

Current implementation step:

Use the C006 hardened bundle as the first website implementation target and the C007 skeleton as the review guide for public copy and interaction behavior.

C008 is a review candidate for future compression hardening. It should not automatically replace the C003 paper-reported compression values without lab review because its diagnostic is independent finite-volume quadrature, not the original paper multipole calculation.

C009 is a review candidate for future jurisdiction hardening. It should not automatically replace C004 because C004 is EMS-rehearsal provenance while C009 is a clean controlled benchmark.

C010 recommends keeping C003/C004 as public-review anchors and adding C008/C009 as supporting hardening panels. The v0.3 bundle is for lab review only.

C011 adds the current caution: jurisdiction controls are strong, but the spherical compression null needs analytic follow-up before it is used as a public-facing failure-mode claim.

C012 completes that follow-up. It supports the order-improves-fidelity pattern but warns that near-surface finite-volume compression language should stay diagnostic-bound.

Recommended website target:

```text
data/curvature_identity_atlas_bundle_v0_2.json
```

Recommended lab-review candidate:

```text
data/curvature_identity_atlas_review_bundle_v0_3.json
```

Recommended page:

```text
curvature-identity-atlas.md
```

Publication rule:

```text
Do not touch or update the website repository until the lab explicitly approves implementation.
```
