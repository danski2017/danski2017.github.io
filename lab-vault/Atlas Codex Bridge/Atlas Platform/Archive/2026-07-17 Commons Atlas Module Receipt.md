---
type: platform_change_receipt
status: archived
created: 2026-07-17
tags: [atlas-platform, commons, viewer-module, bake, receipt]
---

# 2026-07-17 Receipt — Commons Atlas Module (bake + 3D adapter + viewer link)

## Change
Three additive pieces, wiring the commons diagnostic into the instrument
(founder request 2026-07-17):
1. **Bake** `scripts/et_tov3_scout/bake_commons_atlas.mjs` →
   `datasets/COMMONS_ATLAS_001/` (frozen payload, freeze-in-time
   directive 7): `webbing.f32` (3,325 near-parity nodes on a declared 64^3
   volume lattice, per point x,y,z, ||E||-decile band, nearC@eps0.2,
   nearC@eps0.3, entropy, min|Psi|), `islands.json` (the 9 disputed
   troughs with full panel data + the certified H=0.75 entropy surface,
   640 pts), `manifest.json` (provenance, declared vocabulary, claim).
2. **Adapter page** `pinch_lab_viewer/commons_atlas.html` (isolated module,
   lalande-showcase grammar: vendored Three.js + importmap, no external
   deps, no live solves — renders the frozen payload only). Layers:
   webbing point cloud / island troughs / H-surface / roster, each
   toggleable (keyboard W/I/H/R); webbing filters: per-band buttons
   b0-b9, strict rung (nearC@0.2 >= 3), color by band / entropy / carrier
   count; point-size slider; passport ribbon with live counts; claim
   boundary on-screen.
3. **Viewer link**: `index.html` gained a `blCommonsSection` block inside
   the BL Layer Stack (pure HTML — link + provenance note; no JS touched,
   no existing control altered). Backup:
   `backups/atlas_platform/index_pre_commons_link_20260717.html`.

## Validation
- Adapter QA in-browser (HTTP-served): renders clean, zero console
  errors; strict rung filters 3,325 -> 644 nodes with passport count
  updating; entropy color mode verified; desktop + mobile viewport
  screenshots checked.
- Main viewer QA after edit: loads clean, zero console errors; all four
  lane buttons work; BL lane shows the Commons Module with resolving
  link (DOM-verified: section exists, visible, href correct).

## Boundary
The render is a witness, not evidence — the survey packets
(COMMONS_SURVEY_001/002, CONTEXT_SWEEP_001, DENSITY_PROBE_001) came
first. Two-phase vocabulary (islands + webbing) remains a candidate at
Observed; islands carry a Lambda_Pi ceiling; webbing connectivity is
proximity-inferred; thin sheets undersampled at dx ~ 0.36. Full in-lane
layer-stack integration (webbing as a toggleable layer inside the one
render world, wink-grammar A/B against network layers) is the owed next
step; this module is the declared first rung.

## Rollback
`cp backups/atlas_platform/index_pre_commons_link_20260717.html analysis/et_tov3_scout/pinch_lab_viewer/index.html`
and remove `commons_atlas.html`, `datasets/COMMONS_ATLAS_001/`,
`bake_commons_atlas.mjs` (founder permission required for deletions).
