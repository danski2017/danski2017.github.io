---
type: current_state
status: active
created: 2026-07-15
updated: 2026-07-19
tags:
  - atlas-platform
  - current-state
  - development-contract
---

# Current State and Development Contract

## Product Decision

As of 2026-07-15, Atlas Platform is the lab's continuing project viewer. New
visual, diagnostic, ingestion, and teaching capabilities are to be integrated
here. The default is no new standalone viewer.

Exceptions require an explicit founder decision and a documented reason that the
feature cannot be safely isolated in the existing platform.

## Current Build (updated 2026-07-19)

- Product title: `ATLAS Field Metric Viewer`; historical path
  `analysis/et_tov3_scout/pinch_lab_viewer/` (single `index.html`)
- Rendering: Three.js r160 + OrbitControls, VENDORED locally in
  `pinch_lab_viewer/vendor/` — no network dependency (importmap paths need
  the `./` prefix)
- Five UI lanes: Atlas Native, Imported Tools, Recovery Lab, **BL Foam**, and
  **Temporal NR**
- **Canonical base model: the LSN-66 BL cross-term-aware timeslice**
  (blueprint directive 6). All arrangements frozen in
  `datasets/BL_FOAM_BAKED_001/` (~110 MB): 71 Gaia + 8 Family S configs x
  DEN {A,B} x witness {TF, RAW, TF gamma-own}, plus eigen substrate
  (8-float records incl. allegiance), relational network channels
  (dominance/margin/entropy + per-source amplitude matrix), GFRO Table-3
  ledger fields, roster SHA-256. Re-bake:
  `node scripts/et_tov3_scout/bake_bl_foam.mjs` (~50 s)
- BL lane composition: provenance-badged **Layer Stack** (eigen-delta,
  eigenvector pairs, dominance cells, low-margin, entropy, allegiance,
  pairwise parity faces) + all-layers-off master + **ablation wink**
  scrubber (full/removed/wink on frozen arrangements) + interior parity
  shell live lab + Compute Budget (frozen bake default, live fallback)
- Passport ribbon in all lanes: substrate, witness, norm, march, claim,
  parent-context (Lambda_Pi declared uncalibrated), composed stack
- A2 convention lane: gamma-own norm variant with convention-survival
  ledger. RESULTS: Gaia weak-field loci convention-invariant (0.00%);
  Family S compact loci shift 5-16%, negative bias
- First cross-substrate composition: BL foam overlay on the Gaia parent
  eigen scene (exact registration s=6.625997)
- GFRO emission prototype (`scripts/et_tov3_scout/gfro_emission_prototype.mjs`)
  certified vs dense truth; closure census: 50/66 cells radially closed,
  coincident-binary companions have no cell. Emission = setting, never
  default (directive 9)
- Raw catalog holding: `data/rosters/GAIA_LSN500_RAW_001/` — full Gaia DR3
  20-pc neighborhood (2,626 sources), provenance-manifested, no masses,
  no bake (future Phase 6 scene builder)
- Viewer server lifecycle: `scripts/et_tov3_scout/atlas_viewer.sh`
  start|stop|status
- Temporal NR substrate: two genuine archived ET slices at `t=0` and
  `t=898.711912089024` carrying `ML_BSSN::phi`, complex `Psi4`, and complex
  Weyl invariants `I/J`, with horizon/puncture context and 10,179 registered
  probes. Packets: `analysis/atlas_temporal_pilot/ATLAS_TEMPORAL_PILOT_I_ET_ARCHIVE_001/`
  and `analysis/atlas_temporal_pilot/ATLAS_TEMPORAL_PILOT_I_CURVATURE_EXTENSION_001/`
- Governing design record: [[07 One-Model Redesign Blueprint]] (directives
  1-9); all changes receipted in Archive with pre-change backups under
  `backups/atlas_platform/`

## Existing Capabilities To Preserve

- Full, removed, and delta field views
- Side-by-side comparison lab
- Source wink in both removal-footprint and influence-reveal stories
- Feature-shift animation and ridge displacement
- Fixed coordinate probe sampling with Cartesian, staggered, blue-noise, radial,
  and density/phase controls
- Source roster, eigenvectors, unstable-point, footprint, and candidate-surface
  layers
- Probe detail drawer that stays closed until explicitly reopened
- Lumen Lattice placeholder lane
- Atlas Native versus Imported Tools separation
- Recovery Lab case, realization, witness, volume-scale, threshold, and sampling
  controls
- BL Foam scene/configuration/denominator/witness controls, two-ball interior
  sliders, disagreement ledger, and per-lane claim boundaries
- Responsive desktop/mobile layout and centered camera/orbit behavior

## Known Technical Limitations

- The application is a large monolithic HTML/JavaScript file. Modular lanes are
  conceptual/runtime boundaries rather than separate source modules.
- Three.js is vendored locally; the viewer still must be served over HTTP so
  browser fetches can load its dataset payloads.
- The underlying repo worktree contains substantial untracked historical work.
  `git status` and targeted backups are mandatory before edits.
- The legacy directory and artifact names still use `pinch_lab_viewer`.
- Native datasets are compact derived payloads, not raw ET HDF5.
- The ET diagnostic substrate is not yet promoted into an interactive native
  matter/constraint dataset.
- Sampling modes activate existing fixed probes; they do not resample or solve
  the physical field at new coordinates.
- Candidate surfaces are threshold previews, not certified physical boundaries.
- Recovery Lab orientation convergence remains unresolved.
- The Temporal NR lane contains genuine archived evolved scalar and curvature
  witnesses, but lacks a complete time series of ADM, Hydro, constraint, and
  `E_ij` fields. Psi4 is tetrad-dependent and is not `E_ij`. Every registered
  residual is coordinate- and interpolation-dependent, not a gauge-free
  physical change observable; cross-witness correlation is not causation.

## Development Contract

### Preserve

- Inspect the actual source and manifests before changing behavior.
- Record pre-change hashes and dirty-worktree state.
- Keep defaults stable unless the change explicitly targets a default.
- Preserve dataset schema compatibility or version the schema and adapter.
- Keep all existing lanes usable after adding a new one.
- Keep numerical provenance visible and claim boundaries conservative.

### Extend

- Prefer a new toggle, panel section, adapter manifest, or versioned dataset over
  invasive shared-state changes.
- New major lanes must declare inputs, outputs, ownership, failure isolation, and
  removal procedure.
- Promote ET-derived data in the order matter, constraints, base fields, derived
  curvature, identity diagnostics.
- Integrate future time evolution as a time control/data adapter within Atlas
  Platform, not as a replacement application.

### Verify

- Syntax-check embedded JavaScript.
- Validate every changed JSON manifest and binary length contract.
- Serve over HTTP and test actual fetches.
- Use browser screenshots and nonblank WebGL checks at desktop and mobile sizes.
- Exercise all five top-level lanes after shared code changes.
- Re-run numerical audits when data or definitions changed; UI QA alone is not
  scientific validation.

### Record

- Append [[Evolution Log]].
- Add a receipt under `Atlas Platform/Archive/` for material changes.
- Append the repo lab log for numerical or execution events.
- Update [[03 Repo ET and Artifact Location Map]] when paths change.
- Update [[05 Dataset and Model Registry]] when data or claims change.

## Immediate Frontier

The highest-value scientific frontier remains a genuinely coupled,
constraint-solved compact-object scene that can complete this route:

`remote FUKA solve -> separate ET importer -> complete ADM/Hydro/constraint HDF5
-> Atlas HDF5 certification -> matter/constraint viewer layer -> curvature and
identity diagnostics`.

The preserved FUKA BNS seed is useful migration material, but the solve must move
to verified larger-memory hardware. Do not weaken resolution merely to obtain a
passing label.

## Safety Boundary

The 8 GiB Mac mini may serve and develop the viewer, inspect data, run compact
audits, and perform bounded smoke tests. It may not run coupled FUKA binaries,
production ET evolutions, or other unbounded heavy solves. See
[[../Best Practices/Compute Safety and Remote Execution Policy]].


## Addendum 2026-07-18 — Commons + Dynamic Witnesses Era

The BL lane's Layer Stack now carries two additional native sections
(both gaia66-gated, passport-truthful, all-layers-off covered):

- **Commons Layers**: parity webbing (banded near-parity nodes, strict
  rung filter), the 9 high-attribution-entropy tidal-amplitude troughs,
  the H=0.75 frontier patch, and a commons<->network wink scrubber.
  Payload `datasets/COMMONS_ATLAS_001/` (frozen). Dedicated 3D module:
  `commons_atlas.html`.
- **Dynamic Witnesses**: magnetic Weyl ||B|| (C5-B2, kappa=-2 LOCKED by
  OBS_042), magnetic fraction, |P_BR|, signed super-Poynting FLOW
  streaks (ratified E-sign map), momentum-constraint residual monitor;
  kinematics selector (harvested SIMBAD astrometry default /
  declared synthetic). Payloads `MAGNETIC_WEYL_001` (synthetic) and
  `MAGNETIC_WEYL_002` (harvested).

Adjudicated claim state (GPT wing, 2026-07-18): 8 troughs + H>=0.85
backbone REPRODUCED within the declared roster family (Lambda_Pi
uncalibrated footer attached); idx-7 fragile candidate/canary; no
connectivity claims below H 0.85; webbing Observed. Carrier-persistence claims
ADJUDICATED REPRODUCED in-family (A5 ruling 2026-07-18; tightened
custody wording; strong dichotomy not canonized). See the Archive receipts of 2026-07-17/18 and
[[2026-07-18 Commons Promotion Brief for GPT Adjudication]].

## Temporal NR current capability — 2026-07-19

The archived-ET Temporal NR lane supports a three-rung common full-3D phi/Psi4/I/J ladder, adjacent registered complex residuals, puncture and horizon context, and an aligned finite-radius multipolar Psi4 history. Preserve the distinction between spatial grid Psi4 and spin-weighted multipoles. The same archive does not contain additional common full-3D rungs; use this as a frozen ET baseline rather than reconstructing missing slices.

## SXS temporal source context — 2026-07-21

The same Temporal NR lane now also hosts `SXS:BBH:0305v3.0` as a dense
`HORIZON_TRAJECTORY_SERIES`: native A/B/C centers, masses, spins, areas,
coordinate kinematics, upstream common-horizon state, remnant history, and N2
strain (2,2). Preserve distinct horizon-coordinate and waveform-retarded time
semantics and apply no hidden shift. This is source context, not a spatial-field
archive, local Weyl tensor, merger prediction, causal result, or handoff law.

The first event-centered audit is now closed negative. The upstream event was
not distinguished at `p<=0.05` by the only continuous two-sided family
(waveform), and the diagnostic maximum moved to `+20 M` under anchor jitter.
Near-zero A/B orbital/mass/spin features are endpoint-sensitive. Preserve the
coexistence, waveform-ordering, and provisional settling ledgers, but do not
replicate or promote a source-context handoff signature from this score.
