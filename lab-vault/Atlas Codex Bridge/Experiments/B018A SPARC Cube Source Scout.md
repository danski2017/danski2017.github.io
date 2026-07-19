---
type: experiment_note
status: source-map
created: 2026-05-13
lane: galaxy-averaging
topics:
  - SPARC
  - HALOGAS
  - THINGS
  - LITTLE-THINGS
  - HI-cubes
---

# B018A SPARC Cube Source Scout

The public SPARC mirror itself is tabular, but real HI data cubes exist through
the parent/neighboring survey archives. The first concrete cube source is
HALOGAS DR1 on Zenodo.

## Confirmed Cube Source

HALOGAS DR1:

- source: https://zenodo.org/records/2552349
- products: HR/LR HI data cubes, moment-0 maps, column-density maps, moment-1 maps
- total record size: about 20.9 GB
- local metadata: `/Users/danski2017/Desktop/Atlas_Solver_Project/codex_context/data/SPARC_Lelli2016/halogas_zenodo_record_2552349.json`
- Atlas overlap index: `/Users/danski2017/Desktop/Atlas_Solver_Project/codex_context/data/SPARC_Lelli2016/atlas_index/halogas_sparc_overlap_files.csv`

Confirmed SPARC-overlap galaxies in HALOGAS:

- NGC0891
- NGC1003
- NGC2403
- NGC3198
- NGC4559
- NGC5055
- NGC5585
- UGC04278

Smallest first cube target:

- NGC2403 HR cube: about 146.6 MB
- NGC2403 LR cube: about 146.6 MB

Best first dark-residual-ish HALOGAS/SPARC target:

- NGC1003: median baseline `Vobs^2 / Vbar^2` about 5.02, cube about 332 MB
- UGC04278: median baseline `Vobs^2 / Vbar^2` about 4.82, cube about 396 MB

## Other Cube Sources Worth Mapping

THINGS:

- VLA HI nearby-galaxy survey.
- Public data products include HI cubes and moment maps.
- Strong overlap with SPARC classics: NGC2403, NGC3198, NGC5055, DDO154, IC2574, NGC2841, NGC2903, NGC3521, NGC6946, NGC7331, and others.

LITTLE THINGS:

- NRAO page explicitly provides natural-weighted and robust-weighted HI-line cubes plus moment maps.
- Best for dwarf / low-surface-brightness systems where scalar discrepancy is often strong.

WALLABY:

- Newer ASKAP survey with mosaicked data cubes and source products.
- Useful later for scale, not first-pass SPARC matching.

BIG-SPARC:

- Not a public complete database yet in this scout, but the project description says it is built from public HI data cubes across APERTIF, ASKAP, ATCA, GMRT, MeerKAT, VLA, and WSRT.
- It validates the strategy: SPARC-style work is moving from tables toward homogeneous cube-derived products.

## Recommendation

Do not download the whole HALOGAS record casually. Start with one cube plus
moment maps and prove the Atlas cube pipeline:

1. NGC2403 as small, clean, quality-1 cube pilot.
2. NGC1003 or UGC04278 as stronger scalar-discrepancy SPARC/HALOGAS test.
3. NGC3198 as canonical rotation-curve comparison once the loader is stable.

Claim boundary: cube ingestion enables real observational confrontation, but
does not by itself make a dark-matter or modified-gravity claim.
