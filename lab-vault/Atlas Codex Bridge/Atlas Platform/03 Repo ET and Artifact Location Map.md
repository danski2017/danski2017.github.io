---
type: location_map
status: canonical
created: 2026-07-15
updated: 2026-07-27
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
| Einstein Toolkit installation | `/Users/danski2017/Desktop/EinsteinToolkit` | Active local Atlas/Relational Labs NR infrastructure, including Cactus and bounded external-data cache |
| Einstein Toolkit Cactus tree | `/Users/danski2017/Desktop/EinsteinToolkit/Cactus` | Cactus source/builds, ET executables, parameter files, raw HDF5, FUKA source, and importer source |

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

Archived temporal substrate added 2026-07-19:

| Location | Role |
|---|---|
| `/Users/danski2017/Desktop/EinsteinToolkit/atlas_external_data/zenodo_155394/` | Selectively retrieved, CRC-validated external raw cache for Zenodo DOI `10.5281/zenodo.155394`; not a browser dependency |
| `analysis/atlas_temporal_pilot/ATLAS_TEMPORAL_PILOT_I_ET_ARCHIVE_001/` | Canonical temporal-pilot evidence packet, ledgers, manifests, validation, and renders |
| `analysis/atlas_temporal_pilot/ATLAS_TEMPORAL_PILOT_I_CURVATURE_EXTENSION_001/` | Work Order 1B complex-Psi4/I/J evidence packet, conventions, cross-witness ledgers, validation, and renders |
| `scripts/atlas_temporal_pilot/` | Reusable TemporalScene declaration, archive adapter, bounded retrieval, build, validation, and closeout code |
| `configs/atlas_temporal_pilot/` | Frozen temporal-pilot extraction and registration configuration |
| `analysis/et_tov3_scout/pinch_lab_viewer/datasets/ATLAS_TEMPORAL_PILOT_I_ET_ARCHIVE_001/` | Compact browser payload for the existing instrument's Temporal NR lane |
| `analysis/atlas_temporal_pilot/ATLAS_TEMPORAL_PILOT_I_ET_ARCHIVE_001_DIRECTOR_SHARE_26_FILES.zip` | Integrity-tested 26-file director-facing results bundle |
| `analysis/atlas_temporal_pilot/ATLAS_TEMPORAL_PILOT_I_CURVATURE_EXTENSION_001_COMPLETE_OUTPUT.zip` | Standard complete-output curvature-extension bundle; excludes raw external cache but includes its checksum ledger |

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

Canonical temporal-harness documents:

| Role | Location |
|---|---|
| Sole current master design basis | `Relational_Labs/Relational_Labs/Atlas Codex Bridge/Atlas Platform/11 ET Temporal Harness Master Specification.md` |
| Fenced internal CG-1/CG-2/TR-1 frame | `Relational_Labs/Relational_Labs/Atlas Codex Bridge/Atlas Platform/12 Constraint Geometry and Return Maps - Internal Research Frame.md` |
| Vault compute-safety authority | `Relational_Labs/Relational_Labs/Atlas Codex Bridge/Best Practices/Compute Safety and Remote Execution Policy.md` |
| Repo execution policy | `docs/COMPUTE_SAFETY_POLICY.md` |
| Phase-I harness implementation | `scripts/atlas_temporal_harness/` |
| Phase-I mock configuration | `configs/atlas_temporal_harness/ATLAS_TEMPORAL_HARNESS_PHASE_I_MOCK.json` |
| Phase-I architecture and inventory | `docs/atlas_temporal_harness/` |
| Phase-I mock demonstrations | `analysis/atlas_temporal_harness/temporal_runs/` |
| Phase-II-A LOCAL_ET discovery/profile/config | `analysis/atlas_temporal_harness/phase_ii_a/`, `configs/atlas_temporal_harness/local_et/` |
| Phase-II-A fail-closed blocked run | `analysis/atlas_temporal_harness/temporal_runs/PHASE_IIA_LOCAL_ET_BLOCKED_20260726/` |
| Phase-II-A real completion receipt/bundle | `analysis/atlas_temporal_harness/phase_ii_a_completion_001/` |
| Phase-II-A successful A→B restart run | `analysis/atlas_temporal_harness/temporal_runs/ATLAS_TEMPORAL_HARNESS_PHASE_IIA_COMPLETION_001_RUN2/` |
| Phase-II-A optional control passport (not launched) | `analysis/atlas_temporal_harness/temporal_runs/ATLAS_TEMPORAL_HARNESS_PHASE_IIA_COMPLETION_001_CONTROL/` |

The Atlas temporal control spine and backend-neutral ET Adapter interface exist,
are mock-backend validated, and now have a bounded real `LOCAL_ET` completion
receipt. One microscopic two-iteration segment produced a genuine checkpoint;
one exact restart child advanced two more iterations with closed ancestry and
zero measured swap growth. This certifies the named Phase-II-A engineering
smoke path only, not a production envelope or physics result. The optional
uninterrupted control was not launched after its own preflight found elevated
swap. See [[Archive/2026-07-26 Atlas Temporal Harness Phase II-A Completion Receipt]].

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

### Temporal Pilot I Psi4 time ladder

- Packet: `/Users/danski2017/Desktop/Atlas_Solver_Project/analysis/atlas_temporal_pilot/ATLAS_TEMPORAL_PILOT_I_PSI4_TIME_LADDER_001/`
- Processed viewer payload: `/Users/danski2017/Desktop/Atlas_Solver_Project/analysis/et_tov3_scout/pinch_lab_viewer/datasets/ATLAS_TEMPORAL_PILOT_I_ET_ARCHIVE_001/temporal_scene.json`
- Raw selective cache: `/Users/danski2017/Desktop/EinsteinToolkit/atlas_external_data/zenodo_155394/GW150914_28/`
- Raw cache stays outside the frontend and complete-output ZIP.

### SXS horizon dynamics bridge

- Packet: `/Users/danski2017/Desktop/Atlas_Solver_Project/analysis/atlas_temporal_pilot/ATLAS_SXS_HORIZON_DYNAMICS_001/`
- Viewer payload: `/Users/danski2017/Desktop/Atlas_Solver_Project/analysis/et_tov3_scout/pinch_lab_viewer/datasets/SXS_HORIZON_DYNAMICS_001/temporal_scene.json`
- External SXS cache: `/Users/danski2017/Desktop/EinsteinToolkit/atlas_external_data/sxs/`
- Adapter/builder: `scripts/atlas_temporal_pilot/sxs_horizon_adapter.py`, `build_sxs_horizon_dynamics.py`
- Raw cache remains outside the frontend; no full catalog mirror or local SXS evolution exists.

### SXS event-centered coherence audit

- Packet: `/Users/danski2017/Desktop/Atlas_Solver_Project/analysis/atlas_temporal_pilot/ATLAS_SXS_EVENT_CENTERED_COHERENCE_001/`
- Config: `configs/atlas_temporal_pilot/ATLAS_SXS_EVENT_CENTERED_COHERENCE_001.json`
- Analysis/validation: `scripts/atlas_temporal_pilot/event_centered_coherence.py`, `run_sxs_event_centered_coherence.py`, `validate_sxs_event_centered_coherence.py`
- Input is the existing compact SXS viewer payload; no raw-cache change, download, viewer payload, or ET artifact was produced.

## Addendum 2026-07-27 — Resolved Dynamic Curvature Pilot

Temporal Pilot I now has a bounded, genuine local ET evolution/restart evidence
root. This is separate from the older archived-Psi4 packet and does not replace
its viewer role.

| Role | Location |
|---|---|
| Frozen ET executable | `/Users/danski2017/Desktop/EinsteinToolkit/Cactus/exe/cactus_ATLAS_TEUKOLSKY_WAVE` |
| Frozen ET configuration | `/Users/danski2017/Desktop/EinsteinToolkit/Cactus/configs/ATLAS_TEUKOLSKY_WAVE/` |
| Atlas scene/configuration inputs | `configs/atlas_temporal_harness/temporal_pilot_i/` |
| Vacuum curvature adapter | `scripts/atlas_temporal_harness/temporal_pilot_i_curvature.py` |
| Production materializer | `scripts/atlas_temporal_harness/run_temporal_pilot_i_production.py` |
| Audit renderer | `scripts/atlas_temporal_harness/render_temporal_pilot_i.py` |
| Fail-closed certifier/bundler | `scripts/atlas_temporal_harness/certify_temporal_pilot_i.py` |
| Complete evidence root | `analysis/atlas_temporal_harness/temporal_pilot_i_resolved_dynamic_curvature_001/` |
| Completion ZIP | `ATLAS_TEMPORAL_PILOT_I_RESOLVED_DYNAMIC_CURVATURE_001_COMPLETE_OUTPUT.zip` |
| Pre-vault rollback set | `backups/atlas_temporal_harness/temporal_pilot_i_pre_vault_20260727/` |

The evidence root retains both calibration attempts, both production segments,
raw ordinary/checkpoint HDF5, the exact Segment-B restart input, three canonical
E/B/W epochs, two registered differences, uncertainty/history/passport
objects, 32 PNG audits, the final executable, build metadata, source/schema
snapshot, tests, manifests, and receipts. The external ET derived object tree
is not duplicated: it is 411 MiB of compiler intermediates. The completion
bundle instead carries the exact 11 MiB arm64 executable, configuration inputs,
generated configuration metadata, linkage receipt, source revisions, and
relevant Atlas source.

Load-bearing identities:

- executable SHA-256 `f73db961bfc995a9157d10c46c2144d50b93afbb77faebdd9ff1140e4ccfc65b`;
- canonical parameter SHA-256 `765dbd8e322eed647274d6948ae4ddfd6ba5af6adc6d235e1526354b291dbd8b`;
- Segment-A raw checkpoint SHA-256 `fd024eb5781dc1b6b21c0a0b032188708d6b20ed9b220b335415e53cc7b4f2be`;
- Segment-B raw checkpoint SHA-256 `2b7d25d3529786ca290ecaa6c9d2c0d2bac8f9755826ff6b76ea49153f650057`.

See [[Archive/2026-07-27 Atlas Temporal Pilot I Resolved Dynamic Curvature 001 Receipt]].
