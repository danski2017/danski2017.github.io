---
type: operations_runbook
status: canonical
created: 2026-07-15
updated: 2026-07-18
tags:
  - atlas-platform
  - runbook
  - qa
---

# Operations and Validation Runbook

## Start The Viewer

From `/Users/danski2017/Desktop/Atlas_Solver_Project`:

```bash
python3 -m http.server 8792 \
  --bind 127.0.0.1 \
  --directory analysis/et_tov3_scout/pinch_lab_viewer
```

Open `http://127.0.0.1:8792/`. If that port is occupied, select another free
port and report the exact URL. Keep the server session alive while using the
viewer. A `file://` URL will show the intentional HTTP-server warning.

## Fast Health Check

```bash
curl -I http://127.0.0.1:8792/
curl -I http://127.0.0.1:8792/datasets/PINCH_STAGEB_MULTI_TARGET_002/viewer_multi_manifest.json
```

Then verify in a browser:

- the default StageB scene renders and is nonblank;
- Atlas Native, Imported Tools, and Recovery Lab switch independently;
- the target selector changes the declared removal layer;
- source controls, camera orbit, and probe drawer work;
- no panel or text overlaps at desktop and mobile widths;
- the browser console has no failed payload requests.

## UI Change Workflow

1. Read [[06 Current State and Development Contract]].
2. Record the pre-change hash of `index.html`.
3. Inspect `git status`; do not revert unrelated or user-created changes.
4. Keep the change inside its owning panel/lane where possible.
5. Do not change dataset schemas implicitly from UI code.
6. Run JavaScript syntax validation.
7. Run static adapter and manifest audits.
8. Test with the in-app browser at desktop and mobile viewports.
9. Capture a post-change screenshot for material visual changes.
10. Append [[Evolution Log]] and create a receipt from
    [[Templates/Platform Change Receipt Template]].

JavaScript syntax check used by the existing finalizer:

```bash
LC_ALL=C awk '/<script type="module">/{inside=1;next} /<\/script>/{if(inside)exit} inside' \
  analysis/et_tov3_scout/pinch_lab_viewer/index.html \
  | node --check --input-type=module
```

Recovery Lab static audit:

```bash
.venv/bin/python scripts/et_tov3_scout/audit_recovery_viewer_static_001.py
```

## Regenerate Viewer Payloads

These are export operations, not model solves. Inspect destination behavior and
existing manifests before running them.

Single B03 payload:

```bash
.venv/bin/python scripts/et_tov3_scout/export_pinch_lab_viewer_001.py
```

StageB 16-target payload:

```bash
.venv/bin/python scripts/et_tov3_scout/export_pinch_lab_multitarget_002.py
```

Gaia parent 26-removal payload:

```bash
.venv/bin/python scripts/et_tov3_scout/export_gaia_lsn_parent_viewer_001.py
```

Recovery Lab adapter:

```bash
.venv/bin/python scripts/et_tov3_scout/export_recovery_lab_viewer_001.py
```

Do not treat successful export as scientific recertification. Re-run the owning
model/audit lane when numerical inputs or definitions changed.

## ET HDF5 Ingestion

The certified ingestion source is currently:

`/Users/danski2017/Desktop/EinsteinToolkit/Cactus/ATLAS_TOV3_DIAG`

Canonical certification command recorded in its manifest:

```bash
MPLCONFIGDIR=/private/tmp/atlas_mpl .venv/bin/python \
  -m scripts.et_tov3_scout.et_hdf5_ingest.cli certify \
  --diag-dir /Users/danski2017/Desktop/EinsteinToolkit/Cactus/ATLAS_TOV3_DIAG \
  --out-dir analysis/et_tov3_scout/ET_HDF5_INGEST_001 \
  --iteration 0 \
  --stride 2 \
  --ghost-policy exclude \
  --timestamp 2026-07-11T16:41:39Z \
  --verify-determinism
```

Tests and finalization:

```bash
.venv/bin/python -m unittest discover \
  -s scripts/et_tov3_scout/et_hdf5_ingest/tests -v

MPLCONFIGDIR=/private/tmp/atlas_mpl .venv/bin/python \
  -m scripts.et_tov3_scout.et_hdf5_ingest.cli finalize \
  --out-dir analysis/et_tov3_scout/ET_HDF5_INGEST_001 \
  --timestamp 2026-07-11T16:41:39Z
```

Use a new versioned output directory and current timestamp for a new substrate;
do not overwrite the certified baseline merely to reuse this command.

## New ET Model Promotion Order

1. Preserve raw ET output and solver transcript.
2. Inventory HDF5 variables, iterations, refinement levels, components, shapes,
   coordinates, and dtypes.
3. Extract only declared ADMBase, HydroBase, and constraint fields.
4. Audit finite values, NaNs, shape consistency, axis order, ghost policy, and
   hashes.
5. Render matter density and Hamiltonian/momentum residuals first.
6. Write a compact Node -1 ledger and JSON manifest.
7. Only then derive Ricci/Weyl, eigensystems, removal deltas, or surfaces.
8. No parity or foam overlays until constraint residuals are visible and pass
   their declared gate.
9. Add the result as a new versioned dataset/adapter in this viewer, not as a new
   application.

## Imported Tools

The browser loads command recipes from:

`analysis/et_tov3_scout/pinch_lab_viewer/imported_tools/tool_launch_manifest.json`

It does not execute them. Commands must be reviewed in the repo and launched in
a terminal. Imported adapters are optional advisory lanes and must not rewrite
native datasets.

## Heavy Compute Gate

Read [[../Best Practices/Compute Safety and Remote Execution Policy|Compute Safety and Remote Execution Policy]] before any solver launch.

- Sandbox isolation does not prove remote execution.
- Record hostname, RAM, unknown count, memory estimate, storage estimate, rank
  count, checkpoint plan, and stop method.
- Do not run coupled FUKA compact-object solves or production ET evolutions on
  the 8 GiB Mac mini.
- The interrupted resolution-9 FUKA BNS case requires at least 32 GiB remotely;
  64 GiB is preferred.

## Failure Recovery

- Stop the process group, not only the visible terminal pipeline.
- Verify all MPI ranks, launchers, `tee` processes, and log handles exited.
- Preserve partial logs and checkpoints.
- Record a resource stop separately from solver nonconvergence.
- Do not resume until the stop cause and execution host are understood.

## Viewer Server Lifecycle (added 2026-07-15)

Start, stop, and verify the local viewer server with:

```bash
scripts/et_tov3_scout/atlas_viewer.sh start   # serves 127.0.0.1:8792
scripts/et_tov3_scout/atlas_viewer.sh status  # shows PID + listening socket, or "port free"
scripts/et_tov3_scout/atlas_viewer.sh stop    # kills the server
```

Full-shutdown checklist when done viewing:

1. Close the viewer browser tab (frees all runtime memory: WebGL buffers,
   foam caches, Three.js — everything is page-lifetime JavaScript).
2. `atlas_viewer.sh stop` (the Python server otherwise idles forever, ~10 MB).
3. `atlas_viewer.sh status` must report "port 8792 is free."
4. Optional paranoia: `pgrep -fl http.server` should print nothing Atlas-related,
   and Activity Monitor's Memory Pressure should return to its baseline.

The server binds 127.0.0.1 only (never exposed to the network). The browser's
ordinary disk cache may retain static copies of viewer files; that is inert
and not a resource concern.

## BL Foam Re-Bake (added 2026-07-15)

After any change to the BL kernels, scenes, or the Gaia roster, regenerate the
frozen arrangements and re-cross-check counts against the live lane:

```bash
node scripts/et_tov3_scout/bake_bl_foam.mjs   # ~8 s, writes BL_FOAM_BAKED_001
```

## Addendum 2026-07-18 — Commons/Dynamic Operations + Sweep Discipline

Re-bake commands (each seconds-scale, deterministic seeds):
- Commons payload: `node scripts/et_tov3_scout/bake_commons_atlas.mjs`
- Magnetic (synthetic): `node scripts/et_tov3_scout/bake_magnetic_weyl.mjs`
- Magnetic (harvested): `node scripts/et_tov3_scout/bake_magnetic_weyl.mjs
  analysis/et_tov3_scout/KINEMATICS_HARVEST_001/kinematics_real.json
  MAGNETIC_WEYL_002`
  (NOTE: the bake writes manifest.json from the SCRIPT'S strings —
  claim-wording fixes must land in the script or a re-bake regresses
  them; learned 2026-07-18.)

QA pattern for any new layer (established across 7 shipped changes):
render on gaia66 with passport stack declaration matching the screen;
scene-switch to familyS must clear geometry AND passport entries;
all-layers-off must uncheck and clear; zero console errors; desktop +
mobile screenshots for layout-sensitive changes.

Sweep discipline (post-incident, 2026-07-18): refinement pattern
searches carry an ITERATION CAP + relative-improvement threshold (a
float-precision crawl once stalled 30 min at 98% CPU); sweep scripts
enforce a DECLARED NODE CEILING (1e6). Long runs go in background with
a watcher; kill anything pathological and file the incident in the
receipt.
