---
type: dataset_registry
status: canonical
created: 2026-07-15
updated: 2026-07-18
tags:
  - atlas-platform
  - datasets
  - claim-boundaries
---

# Dataset and Model Registry

## Selectable Atlas Native Families

### StageB Multi-Target 002

- Viewer catalog:
  `pinch_lab_viewer/datasets/PINCH_STAGEB_MULTI_TARGET_002/viewer_multi_manifest.json`
- UI label: `StageB multi-target / 16 removals`
- Sources: 16 asymmetric mixed-profile objects, `B00` through `B15`
- Removal layers: 16
- Viewer probes per layer: 35,937 on a `33 x 33 x 33` sample lattice
- Sample spacing: `3.0`
- Approximate family size: `63M`
- Source analyses: `IDENTITY_STAGEB_16SRC_001` and
  `PINCH_EIGENFIELD_LEDGER_001`
- Model class: custom Lichnerowicz/conformally flat static constrained diagnostic
- Claim ceiling: not full GRHydro and not an ET multi-star equilibrium

This is the current default viewer family.

### Gaia LSN Parent 001

- Viewer catalog:
  `pinch_lab_viewer/datasets/GAIA_LSN_PARENT_001/viewer_multi_manifest.json`
- UI label: `Gaia LSN parent / baseline + removal layers`
- Scene: Sun-centered 52-system normalized parent context
- Input roster: `/Users/danski2017/Desktop/05_gaia_lsn_50.json`
- Removal layers: 26 selected single and multi-source cases
- Viewer probes per layer: 35,937 on a `33 x 33 x 33` sample lattice
- Sample spacing: `6.0`
- Approximate family size: `103M`
- Source analysis: `analysis/et_tov3_scout/GAIA_LSN_PARENT_001/`
- Model class: normalized time-symmetric conformally flat Hamiltonian-constraint
  solve using a custom Atlas pipeline
- Claim ceiling: not an ET multi-star equilibrium and not a GRHydro evolution

The 26 layers include the Sun, nearby systems, heavy anchors, outer cases, and
five multi-source patterns. They are a selected experimental suite, not all 52
possible single-source removals.

### Eigenfield Ledger B03

- Viewer manifest:
  `pinch_lab_viewer/datasets/PINCH_EIGENFIELD_LEDGER_001_B03/viewer_dataset_manifest.json`
- UI label: `Eigenfield ledger / B03 only`
- Target: `B03`
- Sources: 16
- Viewer probes: 35,937
- Sample spacing: `3.0`
- Approximate family size: `3.9M`
- Role: original single-target pointwise full/removed/eigenframe diagnostic
- Claim ceiling: tolerance-defined geometric footprint diagnostic only

### Gaia Smoke Payload

- Location: `pinch_lab_viewer/datasets/GAIA_LSN_PARENT_001_SMOKE/`
- Targets: `single_sun` and `single_alpha_system`
- Approximate size: `7.9M`
- Status: export smoke/control payload; present on disk but not selectable in the
  current dataset menu

### BL Analytic Foam Scenes (BL Foam lane, 2026-07-15)

- No dataset payload: scenes are analytic and computed live in-browser
- Scenes: Family S (5 uniform conformal balls, R=0.6, mu 0.150-0.180,
  phi<=0.3), Gaia LSN-66 punctures (roster embedded from the certified
  atlas_parity_foam_v3 payload, mu = m/2), two-ball interior parity shell lab
  (probe mu=0.16, R=0.6)
- Witness: R3_ij assembled from the conformal factor; trace-free E_ij branch
  is the default lawful tidal witness; Frobenius norm is the coordinate-chart
  ||.||_delta under shared Euclidean chart identification
- Comparison contract: rho_s = ||Delta_s E||_F / ||context||_F with DEN A
  (fused re-solved ablated) and DEN B (pasted isolated-E sum); ledger d_AB
  from matched outermost crossing per ray
- Source instruments and lab notes: `~/Desktop/Claude/artifacts/BL_method/`
  (2026-07-13 Claude-wing session)
- Claim ceiling: declared analytic diagnostic substrate — not ET-fused GR,
  not physical membranes, not coordinate-independent invariants; vocabulary
  candidate, not decision
- Founder note 2026-07-15: foam diagnostic reconsidered; historical "no foam"
  manifest language is provenance of wing skepticism, not doctrine

### BL Foam Baked 001 (frozen arrangements, 2026-07-15)

- Payload: `pinch_lab_viewer/datasets/BL_FOAM_BAKED_001/` (manifest + 144
  float32 payloads, 5.1 MB; gaia66 roster JSON with SHA-256 in manifest)
- Generator: `scripts/et_tov3_scout/bake_bl_foam.mjs` (re-bake after any
  kernel or roster change)
- Content: all BL foam arrangements at certified march, full probe rosters —
  familyS 8 configs, gaia66 10 configs, each x DEN {A,B} x witness {TF,RAW},
  positions + outermost-crossing arrays (ledger-ready)
- Cross-check: counts exactly match live-certified lane extractions
- Eigen substrate (2026-07-16): per-scene omni-radial lattice with per-config
  trace-free E_ij eigen-decomposition ([lam0,lam1,lam2,e0,froTF]); feeds the
  Base-Model Eigen Layers; eigenvectors gated by eigen-gap per GFRO
- Claim ceiling: identical to the BL analytic scenes entry above

### Gaia LSN 20-pc Raw Catalog (holding, 2026-07-16)

- Location: `data/rosters/GAIA_LSN500_RAW_001/` (repo root, NOT under the
  viewer) — `lsn_20pc_gaia_dr3.json` + `manifest.json` (provenance, SHA-256)
- Content: all 2,626 Gaia DR3 sources within 20 pc (plx>=50 mas, S/N>5);
  ICRS cartesian xyz_pc precomputed; astrometry, photometry, RUWE retained
- Status: RAW HOLDING for the future custom scene builder (Phase 6). No
  masses (declared mass model required at scene-build time); bright-star gap
  declared (Alpha Cen A/B etc. need a supplementary catalog); no bake
- Claim ceiling: catalog data only — no scene, no diagnostic claims

## Native Scalar Contract

The current native schema exposes, in manifest-declared order:

`absWeyl_full`, `absWeyl_removed`, full and removed `lambda0..2`,
`delta_lambda0..2`, `eigen_gap_full`, `eigenvector_delta_angle`,
`delta_absWeyl`, `delta_ricci_trace`, `delta_compression_fraction`, and
`distance_target`.

The viewer also reads full and removed principal eigenvectors, flags, positions,
and grid indexes from separate binary arrays. Eigenvector angle is sign-invariant
and must be conditioned on eigen-gap stability for interpretation.

## Recovery Lab Registry

Catalog:
`pinch_lab_viewer/recovery_lab/recovery_manifest.json`

Cases:

| Case | Role | Realizations |
|---|---|---|
| `single_sun` | Clean Sun-centered control | baseline, fine, expanded, shifted |
| `multi_nearest_parent_cluster` | Expected multi-pocket control | baseline, fine, expanded, shifted |
| `multi_diffuse_low_mass_web` | Context-distortion candidate | baseline, fine, expanded, shifted |

Controls vary resolution (`dx 2.4`), domain (`half-width 120`), and half-cell
grid shift. The module's current headline is that proper tensor-delta amplitude
and tolerance-defined support topology persist within tested controls, while
pointwise eigenframe orientation remains unresolved. This is not a universal
finite-boundary claim.

## ET Truth Substrate

### ATLAS TOV3 Diagnostic

- Raw source: `/Users/danski2017/Desktop/EinsteinToolkit/Cactus/ATLAS_TOV3_DIAG`
- Raw fields: ADMBase metric, extrinsic curvature, lapse, shift; HydroBase rho,
  pressure, epsilon, velocity; Hamiltonian and momentum constraints
- Iteration: `0`
- Reported raw shape: `55 x 105 x 105` for the certified component/layout
- Certified Atlas output: `analysis/et_tov3_scout/ET_HDF5_INGEST_001/`
- Certification status: `pass_with_documented_exclusions`
- Direct viewer status: not currently a selectable Atlas Native dataset

This is real Einstein Toolkit HDF5 and the canonical ingestion truth gate. The
underlying three TOV sources use `TOV_Combine_Method="maximum"`; they were not
jointly solved as a multi-body equilibrium. Use it to validate ingestion,
constraints, array order, and ET-to-Atlas provenance, not to claim a fully fused
three-star solution.

### ATLAS TOV3 Evolution

- Executable: `Cactus/exe/cactus_ATLAS_TOV3_EVOLVE`
- Output: `Cactus/ATLAS_TOV3_EVOLVE/`
- Status: early 256-iteration evolution lane
- Limitation: density-only time output, insufficient for time-dependent Weyl,
  constraint, and complete field recovery in Atlas Platform

## FUKA BNS Frontier

- Analysis: `analysis/et_tov3_scout/FUKA_BNS_BRIDGE_001/`
- Current status authority: `gate_status.json`
- Declared scene: unequal-mass `1.2 + 1.6`, separation `30`, nonspinning,
  gamma-2 EOS, spectral resolution 9
- Passed: local build, isolated-star validation, both prepared component stars,
  and shared binary restart seed
- Not passed: coupled BNS convergence, ET import, constraint certification, or
  viewer promotion
- Resource result: the coupled system exceeded the safe class of the 8 GiB Mac
- Next host: at least 32 GiB remote; 64 GiB preferred

No FUKA binary data is presently available in Atlas Platform. The resource stop
is not solver nonconvergence and not a physics result.

## Imported Tools Registry

Launch manifest:
`pinch_lab_viewer/imported_tools/tool_launch_manifest.json`

| Adapter | Current role |
|---|---|
| kuibit | Independent ET HDF5 inventory/reader cross-check |
| yt | Slices, projections, radial profiles, and edge-band volume audits |
| openPMD-api | Portable export schema planning |
| EinsteinPy | Known-metric symbolic/reference checks |
| OGRePy | Notebook/reference symbolic lane |
| Atlas 3D renderer | Static full/removed/delta and constraint audit showcases |

These outputs are advisory until promoted through an explicit validation gate.

## Interpretation Guardrails

- Nonzero scalar tails are expected and do not imply preserved identifiable
  geometry at arbitrary distance.
- Black or empty display regions can reflect thresholds, eigen-gap filtering,
  sampling, opacity, or view occlusion; they are not automatically zero delta.
- Feature displacement is a visualization of field-feature relocation, not
  literal motion of fixed coordinate probes.
- Candidate surfaces depend on tolerance, grid, context, and component rules.
- Matter and constraint residuals outrank attractive identity visualizations when
  certifying new numerical-relativity substrates.


## Addendum 2026-07-18 — New Payloads and Evidence Packets

| Payload | Contents | Claim ceiling |
|---|---|---|
| `COMMONS_ATLAS_001/` | webbing.f32 (3,325 near-parity nodes, 64^3 declared lattice), islands.json (9 troughs + certified H=0.75 surface), manifest | Troughs/backbone REPRODUCED-in-family (adjudicated 2026-07-18); webbing Observed; render-as-witness |
| `MAGNETIC_WEYL_001/` | dynwit.f32 + pvec.f32 + kinematics.json (declared synthetic, seed 2026, beta 1e-4) | Implemented/Observed; kappa=-2 LOCKED (OBS_042); not radiative/conservation/prediction |
| `MAGNETIC_WEYL_002/` | same schema, harvested SIMBAD kinematics (frame recovered, 0.78 deg) | as 001; kinematics = declared approximate astrometry, NOT ephemeris |

Evidence packets (repo, hashed in the promotion brief):
`analysis/et_tov3_scout/COMMONS_{SURVEY_001,SURVEY_002,CONTEXT_SWEEP_001,DENSITY_PROBE_001,FRONTIER_PROBE_001,PERSISTENCE_SWEEP_001,CARRIER_PERSISTENCE_001}/`,
`OBS042_KAPPA_CROSSCHECK/`, `KINEMATICS_HARVEST_001/` (raw SIMBAD CSV
receipt + kinematics_real.json).
Provenance root: `analysis/archives/atlas_gfro_solver_v0_9_rc2.zip`
(DO NOT DELETE — verified 66/66 against the baked roster).
