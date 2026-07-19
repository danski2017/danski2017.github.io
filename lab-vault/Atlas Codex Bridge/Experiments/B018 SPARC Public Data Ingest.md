---
type: experiment_note
status: source-data-ingested
created: 2026-05-13
lane: galaxy-averaging
topics:
  - SPARC
  - galaxy-rotation
  - observational-anchor
  - dark-matter-signal-quarantine
---

# B018 SPARC Public Data Ingest

Codex mirrored the public SPARC Lelli-McGaugh-Schombert dataset into the Atlas
context shelf for future galaxy-lane confrontation.

Source record: https://zenodo.org/records/16284118  
DOI: 10.5281/zenodo.16284118  
Local mirror: `/Users/danski2017/Desktop/Atlas_Solver_Project/codex_context/data/SPARC_Lelli2016`

## What Landed

- 175-galaxy SPARC sample catalog.
- 175-galaxy radial mass-model table.
- 175 per-galaxy rotation/mass-model `.dat` files.
- Saved Zenodo metadata.
- Checksum-verified source archives.
- Atlas-generated target-selection indices under `atlas_index/`.

## First Atlas Index

The first index computes a target-selection mass-discrepancy proxy:

`Vobs^2 / Vbar^2`

using signed gas contribution and fixed baseline mass-to-light assumptions:

- disk `M/L[3.6] = 0.5`
- bulge `M/L[3.6] = 0.7`

This index is only for choosing SPARC galaxies to confront against Atlas
curvature-identity diagnostics. It is not a dark-matter claim.

## Top Initial Strong-Residual Targets

By median baseline `Vobs^2 / Vbar^2`, the first selection queue begins with:

- NGC2915
- UGC06667
- F583-1
- NGC3741
- F563-1
- F568-V1
- NGC1705
- UGC07399
- UGC00731
- UGC07608

## Claim Boundary

SPARC gives observed scalar/radial rotation and baryonic mass-model structure.
Atlas has not yet projected these galaxies into a full electric-Weyl/eigenframe
curvature-identity comparison. The next scientific move is to compare SPARC
mass-discrepancy strength against Atlas curvature-identity vulnerability under
matched observational coarse-graining.

Public-safe sentence:

Scalar mass discrepancy and tensorial curvature-identity loss are now separable
axes we can test against the same galaxy roster.
