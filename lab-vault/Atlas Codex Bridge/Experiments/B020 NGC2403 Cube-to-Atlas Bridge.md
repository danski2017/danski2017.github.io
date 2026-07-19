---
type: experiment_note
status: completed
created: 2026-05-13
lane: galaxy-averaging
topics:
  - HALOGAS
  - SPARC
  - HI-cube
  - source-proxy
  - NGC2403
---

# B020 NGC2403 Cube-to-Atlas Bridge

Codex converted the first real observational HI cube pilot into a compact
Atlas-readable source-proxy bridge.

Experiment package:

`/Users/danski2017/Desktop/Atlas_Solver_Project/codex_context/experiments/B020_ngc2403_cube_to_atlas_bridge`

Primary outputs:

- `derived/B020_NGC2403_HI_SOURCE_PROXY_SCENE.csv`
- `derived/B020_NGC2403_SPARC_RING_ALIGNMENT.csv`
- `derived/B020_SUMMARY.json`
- `reports/B020_REPORT.txt`

## Result

The bridge produced:

- 6000 HI source proxies selected from the strongest column-density support.
- 17 radial alignment rings.
- SPARC catalog and mass-model linkage.
- HALOGAS moment-map provenance.
- Declared geometry, mask, and mass-basis limits.

## Key Numbers

- active support pixels: 27180
- support threshold: `1.17219e21`
- active fraction of positive column-density pixels: about `0.2000`
- SPARC distance: `3.16 Mpc`
- SPARC inclination: `63 deg`
- inferred major-axis PA proxy: `108.177 deg`
- HI mass basis: `3.199e9 Msun`
- median abs fractional q90-deprojected LOS vs SPARC Vobs: `0.0531`
- p90 abs fractional q90-deprojected LOS vs SPARC Vobs: `0.739`

## Read

The cube can now speak Atlas. The inner and mid support rings align reasonably
with SPARC rotation amplitudes under a simple q90 deprojected moment-1 diagnostic.
The outer support rings become sparse and cautionary, which is useful: it tells
us where a real cube-native tilted-ring or 3DBarolo-style step matters before
claiming tensor witness structure.

## Claim Boundary

This is not a dark-matter claim. It is not a replacement for SPARC rotation
curves. It is not yet an electric-Weyl/eigenframe result. It is an observational
source-proxy bridge that makes the next curvature interrogation lawful.

## Next

B021 should run the first real-data HI-only electric-Weyl/eigenframe witness
using this source-proxy scene, after declaring the z-thickness and mass-basis
assumptions.
