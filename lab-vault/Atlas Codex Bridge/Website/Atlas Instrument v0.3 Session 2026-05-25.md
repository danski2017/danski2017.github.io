---
type: session_log
created: 2026-05-25
status: deployed_with_known_issues
topics:
  - website
  - instrument
  - v0.3
  - github-pages
related:
  - "[[Website Bridge]]"
  - "[[Website Update Checklist]]"
---

# Atlas Instrument v0.3 — Session Log 2026-05-25

## What was done

Replaced `atlas_instrument_v0_2.jsx` with `atlas_instrument_v0_3.jsx` on the live site at `https://danski2017.github.io/instrument/`.

### v0.3 new capabilities

1. **Client-side compute engine** — all geometry computed from passport sources, no file upload needed
   - R2 linearized tidal GCS extraction (Fibonacci sphere rays, log-spaced radial grid, Apollonius-based rmax)
   - R5 1PN-corrected tidal GCS extraction (cross-term formula: `E_ij^1PN = U_,ij − (1/c²)[2U·U_,ij + 3∇U_i·∇U_j − δ_ij|∇U|²]`)
   - Eigenframe: dominant eigenvector of E_ij via power iteration
   - C_VIS = 5.0 toy parameter makes 1PN correction pedagogically visible at solar-system scales

2. **Physics mode toggle** (pedagogical core)
   - NEWTONIAN R2 (orange `#cc6610`) ↔ 1PN CORRECTED R5 (cyan `#10b8cc`)
   - Switches both GCS point cloud and eigenframe simultaneously
   - Panel shows point count for each mode

3. **N-body animation**
   - Leapfrog symplectic integrator
   - Circular orbit initial conditions
   - GCS re-extracted every 8 frames via in-place Float32Array buffer update
   - Play/pause, speed 0.5–6×, step counter, reset

4. **Bug fixes from v0.2**
   - Layer opacity sync (separate Newton/1PN objects; sync effect has sole authority)
   - Empty source label column now shows distance in AU or pc
   - No file upload required

### Deployment work

Created custom `_layouts/instrument.html` to bypass Minima's `.page-content { padding: 30px 0 }` and `<div class="wrapper">` which were interfering with the full-height layout.

Key layout chain:
```
body (height: 100vh, display: flex, flex-direction: column)
  → header.site-header (~56px)
  → main (flex: 1, overflow: hidden)
    → .instrument-intro (flex-shrink: 0)
    → #instrument-wrap (flex: 1, position: relative)
      → #atlas-root (position: absolute, inset: 0)
        → React app (height: 100%)
```

### PRs merged

- [#34](https://github.com/danski2017/danski2017.github.io/pull/34) — Initial v0.3 deploy
- [#35](https://github.com/danski2017/danski2017.github.io/pull/35) — Absolute positioning on atlas-root
- [#36](https://github.com/danski2017/danski2017.github.io/pull/36) — Custom instrument layout (bypass Minima wrapper)
- [#37](https://github.com/danski2017/danski2017.github.io/pull/37) — Compact passport screen; Generate button moved to header bar
- [#38](https://github.com/danski2017/danski2017.github.io/pull/38) — `height: 100vh` on body (definite height for flex chain)
- [#39](https://github.com/danski2017/danski2017.github.io/pull/39) — Remove last `100vh`/`100vw` from StageScreen and AtlasInstrument root divs

### Root cause of bottom-clipping bug

The `AtlasInstrument` root div and `StageScreen` root div used `height: 100vh` — always exactly the viewport height. But these components sit inside `#atlas-root` which is shorter than the viewport (site header + intro are above it). The bottom ~120px was clipped by `overflow: hidden` on ancestor containers. Fixed by changing to `height: 100%` so the React app fills its actual container.

## Outstanding items

- [ ] Verify the viewport height fix is working on Daniel's browser (PR #39 merged end of session)
- [ ] Fine-tune resolution/colors — point sizes, GCS cloud density, eigenframe line length
- [ ] Full eigendecomposition (all 3 eigenvalues/vectors, not just dominant)
- [ ] "Compare" mode — show Newton + 1PN simultaneously
- [ ] SS_bones / witness_skeleton layers — seam lines, curvature edges
- [ ] Test the compute on solar system scene — verify GCS extraction produces correct clouds
- [ ] The old v0.2 JSX file still exists in the repo (`atlas-solver/atlas_instrument_v0_2.jsx`) — can be removed once v0.3 is confirmed stable

## Source files

- **Live JSX**: `atlas-solver/atlas_instrument_v0_3.jsx` in `danski2017/danski2017.github.io`
- **Local copy**: `/Users/danski2017/Desktop/Atlas Solver Hub/SolverV1/atlas_instrument_v0_3.jsx`
- **Python compute skeleton** (reference): `/tmp/atlas_handoff_inspect/atlas_skeleton_compute.py` (from dynamic evolution handoff ZIP)
- **Custom layout**: `_layouts/instrument.html` in `danski2017/danski2017.github.io`

## Doctrine compliance

- `claim_status: diagnostic_candidate_not_observational` — enforced in panel sidebar
- C_VIS = 5.0 explicitly labeled as toy parameter
- No method mechanics disclosed (node stack, flashlight sampling, GCS gate hidden)
- All geometry labeled as diagnostic/platonic — "not physical membranes, force boundaries, or observational claims"
