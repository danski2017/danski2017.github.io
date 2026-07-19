---
type: location_map
status: canonical
created: 2026-07-15
updated: 2026-07-18
tags:
  - atlas-platform
  - repo-map
  - einstein-toolkit
---

# Repo ET and Artifact Location Map

## Two-Tree Architecture

Atlas Platform spans two separate Desktop trees:

| Tree | Absolute root | Responsibility |
|---|---|---|
| Atlas | `/Users/danski2017/Desktop/Atlas_Solver_Project` | Viewer, configs, scripts, compact datasets, Atlas analyses, manifests, docs, logs, and Obsidian vault |
| Einstein Toolkit | `/Users/danski2017/Desktop/EinsteinToolkit/Cactus` | Cactus source/builds, ET executables, parameter files, raw HDF5, FUKA source, and importer source |

The Atlas tree is the platform brain and visual pipeline. The ET tree is the
external numerical-relativity engine and raw-output source. A viewer dataset does
not become ET-derived merely because it lives under `analysis/et_tov3_scout`.
Follow its manifest.

## Live Viewer

| Component | Repo-relative path | Notes |
|---|---|---|
| Application | `analysis/et_tov3_scout/pinch_lab_viewer/index.html` | Canonical UI; legacy directory name |
| Native payloads | `analysis/et_tov3_scout/pinch_lab_viewer/datasets/` | JSON catalogs/manifests plus binary arrays |
| Imported Tools | `analysis/et_tov3_scout/pinch_lab_viewer/imported_tools/` | Advisory launch manifest and generated audits |
| Recovery Lab | `analysis/et_tov3_scout/pinch_lab_viewer/recovery_lab/` | Removable control/convergence adapter |
| UI QA images | `analysis/et_tov3_scout/pinch_lab_viewer/pinch_lab_viewer_*` | Historical implementation screenshots; names predate product rename |

Current application baseline recorded 2026-07-15:

- SHA-256: `76979584a9ac3df0ba18afc196d49c53841f0b0add44d498dd3514168f0d7dcc`
- Size: `104341` bytes
- Viewer tree: approximately `198M`
- Baseline receipt: [[Archive/2026-07-15 Atlas Platform Baseline Receipt]]

## Viewer Dataset Producers

| Script | Reads | Writes |
|---|---|---|
| `scripts/et_tov3_scout/export_pinch_lab_viewer_001.py` | `PINCH_EIGENFIELD_LEDGER_001` | Single-target B03 viewer payload |
| `scripts/et_tov3_scout/export_pinch_lab_multitarget_002.py` | StageB and pinch ledgers | 16-removal StageB catalog |
| `scripts/et_tov3_scout/export_gaia_lsn_parent_viewer_001.py` | Gaia parent solve/config | 26-removal Gaia catalog |
| `scripts/et_tov3_scout/export_recovery_lab_viewer_001.py` | Recovery controls | Recovery Lab adapter payload |
| `scripts/et_tov3_scout/render_imported_3d_showcase.py` | Full/removed/delta NPZ caches | Imported Tools 3D audit images |
| `scripts/et_tov3_scout/audit_recovery_viewer_static_001.py` | Viewer and recovery manifests | Static adapter audit report |

## Model And Derivation Scripts

| Lane | Key scripts |
|---|---|
| StageB custom scene | `run_identity_stageb_16src_001.py`, `lichnerowicz_nbody.py` |
| Pointwise eigenfield | `run_pinch_eigenfield_ledger_001.py`, `atlas_eij_extract.py` |
| Candidate topology | `run_pinch_boundary_001.py`, `build_gaia_footprint_topology_ledger.py` |
| Gaia parent context | `prepare_gaia_lsn_parent_001.py`, `run_gaia_lsn_parent_001.py` |
| Recoverability | `identity_recoverability_cw_001.py`, `run_identity_recoverability_cw_001.py`, `run_identity_recoverability_controls_001.py`, `analyze_identity_recoverability_convergence_001.py`, `finalize_identity_recoverability_cw_001.py` |
| ET HDF5 certification | `et_hdf5_ingest/` package, including `inventory.py`, `extract.py`, `audit.py`, `render.py`, and `manifest.py` |
| Imported-tool adapters | `atlas_external_tools.py`, `atlas_external_toolkit_probe.py`, `render_imported_3d_showcase.py` |
| FUKA bridge preflight | `fuka_bridge/preflight.py` and its tests |
| Earlier maps/evolution demos | `run_fused_map_001.py`, `run_fused_map_time_001.py`, related renderers |

All of these are under `/Users/danski2017/Desktop/Atlas_Solver_Project/scripts/et_tov3_scout/`.

## Active Configuration Files

Directory: `configs/et_tov3_scout/`

| Config | Role |
|---|---|
| `IDENTITY_STAGEB_16SRC_001.json` | 16-source asymmetric custom scene |
| `PINCH_EIGENFIELD_LEDGER_001.json` | B03 eigenfield removal ledger |
| `GAIA_LSN_PARENT_001.json` | 52-system Sun-centered parent context and removals |
| `IDENTITY_RECOVERABILITY_CW_001.json` | Recovery cases, controls, thresholds, and promotion policy |
| `EXTERNAL_TOOLKIT_ADAPTERS.json` | Optional imported-tool adapters |
| `FUKA_BNS_BRIDGE_001.json` | Original BNS bridge declaration; planning status is stale |
| `FUKA_BNS_BRIDGE_001_SPRINT.json` | Current sprint state |
| `FUSED_MAP_001.json`, `FUSED_MAP_TIME_001.json` | Earlier static and time-demo lanes |
| `tov3_glued_equal_static_scout.par` | Atlas-side copy of ET scout parameter intent |
| `ET_TOV3_scout.th` | Atlas-side ET thorn list |

For FUKA status, `analysis/et_tov3_scout/FUKA_BNS_BRIDGE_001/gate_status.json`
overrides the stale `planned_not_built` field in the original declaration.

## Canonical Analysis Roots

| Analysis root | Responsibility |
|---|---|
| `analysis/et_tov3_scout/IDENTITY_STAGEB_16SRC_001/` | StageB full and removal solves/caches |
| `analysis/et_tov3_scout/PINCH_EIGENFIELD_LEDGER_001/` | Pointwise Weyl eigen data and B03 delta ledger |
| `analysis/et_tov3_scout/GAIA_LSN_PARENT_001/` | Gaia parent caches, 26 removal layers, topology ledger |
| `analysis/et_tov3_scout/IDENTITY_RECOVERABILITY_CW_001/` | Controls, convergence, validation, audits |
| `analysis/et_tov3_scout/ET_HDF5_INGEST_001/` | Certified ET HDF5 substrate, ledger, renders, audit |
| `analysis/et_tov3_scout/EXTERNAL_TOOLKIT_PROBE_001/` | Optional tool probe outputs |
| `analysis/et_tov3_scout/FUKA_BNS_BRIDGE_001/` | FUKA build staging, run evidence, gate status, restart seed |
| `analysis/et_tov3_scout/FUSED_MAP_001/` | Earlier static fused-map demonstration |
| `analysis/et_tov3_scout/FUSED_MAP_TIME_001*/` | Earlier illustrative time sequences |

Historical build-triage folders also remain under `analysis/et_tov3_scout/`.
They are evidence, not current platform entry points.

## Source Roster And Profiles

- Gaia source roster: `/Users/danski2017/Desktop/05_gaia_lsn_50.json`
- Gaia normalized scene declaration: `configs/et_tov3_scout/GAIA_LSN_PARENT_001.json`
- ET-validated/custom profile arrays:
  `scripts/et_tov3_scout/tov_profile.npz`, `tov_profile_B.npz`, and
  `tov_profile_C.npz`

The Gaia config records 66 input sources collapsed into 51 systems plus the Sun,
for 52 Atlas scene sources. The current viewer catalog contains 26 selected
single and multiple removal cases, not one layer for every source.

## Einstein Toolkit Tree

Root: `/Users/danski2017/Desktop/EinsteinToolkit/Cactus`

| Location | Role |
|---|---|
| `arrangements/` | ET thorns checked out by the toolkit |
| `configs/ATLAS_TOV3_SCOUT/` | Built static/scout configuration |
| `configs/ATLAS_TOV3_EVOLVE/` | Built evolution configuration |
| `exe/cactus_ATLAS_TOV3_SCOUT` | Scout executable |
| `exe/cactus_ATLAS_TOV3_EVOLVE` | Evolution executable |
| `ATLAS_TOV3_DIAG.par` | Complete three-TOV diagnostic parameter file |
| `ATLAS_TOV3_DIAG/` | Raw iteration-zero ADMBase/HydroBase/constraint HDF5 |
| `ATLAS_TOV3_EVOLVE.par` | Early evolution parameter file |
| `ATLAS_TOV3_EVOLVE/` | Early evolution outputs; density-only time output |
| `atlas_runs/` | ET run directories and refinement/shift controls |
| `repos/fuka/` | FUKA/Kadath source |
| `repos/KadathImporter/` | ET importer source |
| `repos/KadathThorn/` | ET Kadath integration source |

Baseline executable hashes:

- `cactus_ATLAS_TOV3_SCOUT`:
  `5c5f4a3d2fe6b85d30d84845a00fdf941d5bb80acb9729ec62156723fcf24efb`
- `cactus_ATLAS_TOV3_EVOLVE`:
  `0ec35341be36c92de530c6706025a8c59041f7a98ff1e28faf3c66d4e5fdea5b`

ET component source identities recorded 2026-07-15:

- FUKA: branch `ET_2025_05`, commit
  `f1259452c0a62eee3e37c2314691643659e02705`
- KadathImporter: branch `ET_2025_05`, commit
  `53db9d5d0d039db9f0e4886180e896dd22410a82`
- KadathThorn: branch `ET_2025_05`, commit
  `6d48c5ce533dc800e0ca4bc6708d3edd5be1cbc5`

The KadathThorn checkout currently contains untracked `src/fuka/`; inspect and
preserve it when working on that lane.

## Documentation And Logs

Repo policies and status:

- `docs/COMPUTE_SAFETY_POLICY.md`
- `docs/et_tov3_scout/ATLAS_ET_HDF5_SUBSTRATE_CERT_001.md`
- `docs/et_tov3_scout/ATLAS_IDENTITY_RECOVERABILITY_CW_001_ARCHITECTURE_AND_PROVENANCE.md`
- `docs/et_tov3_scout/ATLAS_IDENTITY_RECOVERABILITY_CW_001_CONTRACT.md`
- `docs/et_tov3_scout/ATLAS_IDENTITY_RECOVERABILITY_CW_001_VIEWER_QA.md`
- `docs/et_tov3_scout/ATLAS_EXTERNAL_TOOLKIT_INTEGRATION_LANE_REPORT_20260704.md`
- `docs/et_tov3_scout/ATLAS_EXTERNAL_TOOLKIT_SCOUT_20260703.md`
- `docs/et_tov3_scout/ATLAS_FUKA_BNS_BRIDGE_001_PLAN.md`
- `docs/et_tov3_scout/ATLAS_FUKA_BNS_BRIDGE_001_SPRINT.md`
- `docs/et_tov3_scout/ATLAS_FUKA_BNS_RESOURCE_INCIDENT_001.md`

Primary append-only running lab record:

`logs/et_tov3_scout_lab_log.txt`

This Obsidian section records platform evolution. The repo lab log remains the
detailed numerical and execution notebook.

## Roster Catalogs (added 2026-07-16)

| Role | Location |
|---|---|
| Gaia DR3 20-pc raw catalog | `data/rosters/GAIA_LSN500_RAW_001/` |
| Roster catalog conventions | `data/rosters/README.md` |

## Addendum 2026-07-18 — New Artifacts (Commons + Dynamic Witnesses)

| Role | Location |
|---|---|
| Commons atlas payload (frozen) | `analysis/et_tov3_scout/pinch_lab_viewer/datasets/COMMONS_ATLAS_001/` |
| Magnetic Weyl payloads | `.../datasets/MAGNETIC_WEYL_001/` (synthetic kin), `.../datasets/MAGNETIC_WEYL_002/` (harvested kin) |
| Commons 3D module | `analysis/et_tov3_scout/pinch_lab_viewer/commons_atlas.html` |
| Evidence packets | `analysis/et_tov3_scout/COMMONS_{SURVEY_001,SURVEY_002,CONTEXT_SWEEP_001,DENSITY_PROBE_001,FRONTIER_PROBE_001,PERSISTENCE_SWEEP_001,CARRIER_PERSISTENCE_001}/` |
| OBS_042 crosscheck | `analysis/et_tov3_scout/OBS042_KAPPA_CROSSCHECK/` |
| Kinematics harvest (raw receipt + derived) | `analysis/et_tov3_scout/KINEMATICS_HARVEST_001/` |
| Commons/dynamic bake + survey scripts | `scripts/et_tov3_scout/commons_*.mjs`, `bake_commons_atlas.mjs`, `bake_magnetic_weyl.mjs`, `harvest_kinematics.mjs`, `obs042_kappa_crosscheck.mjs` |
| Index backups (session roots) | `backups/atlas_platform/index_pre_{commons_link,commons_layers}_20260717.html`, `index_pre_pvec_20260718.html` |
