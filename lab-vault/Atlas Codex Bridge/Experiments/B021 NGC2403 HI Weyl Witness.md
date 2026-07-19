---
type: experiment_note
status: completed
created: 2026-05-13
lane: galaxy-averaging
topics:
  - HALOGAS
  - SPARC
  - HI-cube
  - electric-Weyl
  - eigenframe
  - NGC2403
---

# B021 NGC2403 HI Weyl Witness

Codex ran the first real-data HI-only electric-Weyl/eigenframe witness from the
B020 NGC2403 cube-to-Atlas bridge.

Experiment package:

`/Users/danski2017/Desktop/Atlas_Solver_Project/codex_context/experiments/B021_ngc2403_hi_weyl_witness`

Primary outputs:

- `derived/B021_METHOD_SUMMARY.csv`
- `derived/B021_PANEL_SUMMARY.csv`
- `derived/B021_SUMMARY.json`
- `reports/B021_REPORT.txt`

## Setup

- retained branch: 6000 selected HI source proxies
- witness points: 3072
- z-thickness: `0.22 kpc`
- softening: `0.075 kpc`
- mass basis: HI-only, normalized to SPARC MHI from B020
- excluded: stars, molecular gas, dark halo, total baryonic model, full tilted-ring cube fitting

## Main Result

The best scalar-preserving branch was `hi_sector_annular`:

- p90 `vc2` delta: `0.3238`
- p90 electric-Weyl Frobenius delta: `0.4431`
- p90 eigenframe disagreement: `0.7280`
- p90 `E/vc2`: `1.3686`
- p90 eigenframe/vc2: `2.2484`

Mid-panel branch behavior was sharper:

- `hi_sector_annular` mid-panel p90 `E/vc2`: `1.9067`
- `hi_low_order_multipole` mid-panel p90 `E/vc2`: `1.9525`

## Read

The first real cube-derived HI source-proxy scene does not collapse into a
purely scalar story. Sector-annular coarse graining preserves scalar structure
best, but tensor/eigenframe witnesses remain visibly method-sensitive.

This is a real-data continuation of the synthetic B-lane, but only for declared
HI support. It is a bridge from toy/source-proxy work into observational
cube-native structure, not a final galaxy claim.

## Claim Boundary

No dark-matter claim. No total-baryon claim. No full-galaxy curvature claim.
This is HI-only, weak-field, source-proxy-limited, and requires stellar/baryonic
merge before SPARC-scale confrontation.

## Next

B022 should either:

- repeat this on a stronger scalar-discrepancy HALOGAS/SPARC target such as
  NGC1003 or UGC04278, or
- merge NGC2403 HI with SPARC stellar disk/baryonic rows before broader
  curvature-identity comparison.
