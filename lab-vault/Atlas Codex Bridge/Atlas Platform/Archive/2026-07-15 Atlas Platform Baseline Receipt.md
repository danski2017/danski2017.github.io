---
type: platform_baseline_receipt
status: frozen
date: 2026-07-15
platform_name: Atlas Platform
ui_name: ATLAS Field Metric Viewer
---

# 2026-07-15 Atlas Platform Baseline Receipt

## Identity

- Canonical implementation:
  `/Users/danski2017/Desktop/Atlas_Solver_Project/analysis/et_tov3_scout/pinch_lab_viewer/index.html`
- Application SHA-256:
  `76979584a9ac3df0ba18afc196d49c53841f0b0add44d498dd3514168f0d7dcc`
- Application size: `104341` bytes
- Recorded modification time: `2026-07-10 19:47:01 -0500`
- Approximate viewer tree size: `198M`

## Included Runtime Lanes

- Atlas Native
- Imported Tools
- Recovery Lab

## Dataset Families

- `PINCH_STAGEB_MULTI_TARGET_002`: 16 removal layers, approximately `63M`
- `GAIA_LSN_PARENT_001`: 26 removal layers, approximately `103M`
- `PINCH_EIGENFIELD_LEDGER_001_B03`: one layer, approximately `3.9M`
- `GAIA_LSN_PARENT_001_SMOKE`: two-layer non-menu smoke payload,
  approximately `7.9M`
- Recovery Lab adapter: three cases, four realizations each, approximately `14M`
- Imported Tools artifacts: approximately `2.3M`

## External Runtime Dependency

- Three.js `0.160.0` from `https://unpkg.com/three@0.160.0/`
- OrbitControls from the matching Three.js addon path

## ET Baseline

- Cactus root: `/Users/danski2017/Desktop/EinsteinToolkit/Cactus`
- `cactus_ATLAS_TOV3_SCOUT` SHA-256:
  `5c5f4a3d2fe6b85d30d84845a00fdf941d5bb80acb9729ec62156723fcf24efb`
- `cactus_ATLAS_TOV3_EVOLVE` SHA-256:
  `0ec35341be36c92de530c6706025a8c59041f7a98ff1e28faf3c66d4e5fdea5b`
- FUKA source: `ET_2025_05` at
  `f1259452c0a62eee3e37c2314691643659e02705`
- KadathImporter: `ET_2025_05` at
  `53db9d5d0d039db9f0e4886180e896dd22410a82`
- KadathThorn: `ET_2025_05` at
  `6d48c5ce533dc800e0ca4bc6708d3edd5be1cbc5`

## Scientific Boundary

The selectable native datasets are custom constrained/static diagnostic scenes,
not fully coupled multi-source numerical-relativity solutions. The certified ET
substrate is real ET HDF5 but based on a glued three-TOV diagnostic. The FUKA BNS
bridge has no converged coupled binary solution. Candidate identity surfaces are
tolerance- and control-dependent visualization/analysis witnesses.

## Preservation Boundary

This receipt records state; it does not duplicate or freeze the underlying
binaries. Preserve the repo paths, manifests, scripts, configs, and append-only
logs named by [[../03 Repo ET and Artifact Location Map]].

