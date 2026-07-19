---
type: experiment_note
status: completed
created: 2026-05-13
lane: galaxy-averaging
topics:
  - HALOGAS
  - SPARC
  - HI-cube
  - NGC2403
  - observational-anchor
---

# B019 NGC2403 HALOGAS Cube Pilot

Codex downloaded the first real observational HI cube for the galaxy lane:
NGC2403 from HALOGAS DR1, high-resolution product set.

Local cube folder:

`/Users/danski2017/Desktop/Atlas_Solver_Project/codex_context/data/SPARC_Lelli2016/halogas_cubes/NGC2403_HR`

Primary report:

`/Users/danski2017/Desktop/Atlas_Solver_Project/codex_context/data/SPARC_Lelli2016/halogas_cubes/NGC2403_HR/NGC2403_HR_CUBE_PILOT_REPORT.md`

## What Landed

- HI cube FITS.
- Moment-0 map.
- Moment-1 velocity map.
- Column-density map.
- Checksum verification for all four files.
- FITS audit JSON.
- Per-channel summed-flux proxy ledger.

## Cube Facts

- cube shape: `60 x 800 x 800`
- cube unit: `JY/BEAM`
- moment maps: `800 x 800`
- spectral axis: `VELO-HEL`
- spectral frame: `BARYCENT`
- beam: about `15.2 x 13.3 arcsec`

## Claim Boundary

This is observational source ingestion, not an Atlas curvature result yet.
The cube lets the lab move from SPARC radial tables toward cube-native
structure, beam geometry, velocity fields, and source-proxy extraction.

## Next Scientific Move

Build the first cube-to-Atlas bridge:

1. convert cube/moment products into a declared source-proxy scene,
2. compare cube-native moment summaries against SPARC radial rows,
3. generate an electric-Weyl/eigenframe witness panel from the reconstructed
   baryonic proxy,
4. compare that against B015-style observational coarse branches.
