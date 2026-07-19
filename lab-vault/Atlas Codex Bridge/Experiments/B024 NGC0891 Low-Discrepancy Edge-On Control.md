---
type: experiment_note
status: completed
created: 2026-05-14
program:
  - mesoscale-curvature
  - sparc
  - halogas
  - real-data-witness
claim_level: observational_hi_control
---

# B024 NGC0891 Low-Discrepancy Edge-On Control

## Purpose

B024 answers the bias-audit question left open by B023: does the scalar/tensor separability pattern survive when the next target is selected against a large SPARC scalar discrepancy?

The selected control is NGC0891, a quality-flag-1 SPARC/HALOGAS overlap galaxy with median baseline `Vobs^2/Vbar^2 = 1.3766`.

## Source Package

- Experiment package: `codex_context/experiments/B024_ngc0891_low_discrepancy_edgeon_control`
- Script: `codex_context/scripts/b024_ngc0891_low_discrepancy_edgeon_control.py`
- HALOGAS cube folder: `codex_context/data/SPARC_Lelli2016/halogas_cubes/NGC0891_HR`
- Cube: `NGC0891-HR-cube.fits`, shape `188 x 1024 x 1024`, md5 `4fad8e8d6cb82b54f60243fabbace036`
- Moment products and column-density map were checksum verified.

## Geometry Warning

NGC0891 is edge-on in SPARC, with inclination `90 deg`.

B024 is therefore not an apples-to-apples deprojected disc witness like the NGC2403/NGC1003 runs. It is a sky-plane HI support control. The run uses HALOGAS column-density support and moment-map structure to build a declared HI source-proxy scene, but it does not treat moment-1 as a clean deprojected rotation curve.

## Run Ledger

- Active support pixels: `3511`
- Source proxies: `3511`
- Witness points: `3072`
- HI mass basis: `4.462e9 Msun`
- Support threshold: `7.07363e20`
- Inferred sky major-axis proxy: `72.9678 deg`

## Branch Results

| Branch | Coarse Proxies | p90 vc2 Delta | p90 E Delta | p90 Eigenframe | p90 E/vc2 |
|---|---:|---:|---:|---:|---:|
| `hi_sky_radial_annular_axisymmetric` | 336 | 0.4926 | 0.9341 | 0.9981 | 1.8962 |
| `hi_sky_sector_annular` | 147 | 0.00935 | 0.04297 | 0.000302 | 4.5946 |
| `hi_sky_low_order_multipole` | 7 | 0.3702 | 0.5778 | 0.4439 | 1.5607 |

## Read

The low-discrepancy control does not simply reproduce the high-discrepancy behavior. It changes the character of the signal.

In the best scalar branch, the absolute tensor and eigenframe errors are also small: p90 electric-Weyl delta is `0.04297`, and p90 eigenframe disagreement is only `0.000302`. That is important negative pressure on overclaiming.

At the same time, the scalar rotation-like proxy is preserved even more tightly: p90 `vc2` delta is `0.00935`, leaving p90 `E/vc2 = 4.5946`. So the separation remains visible as a relative preservation hierarchy, not as a large absolute tensor failure.

## Claim Boundary

- HI-only source-proxy witness.
- Edge-on sky-plane control.
- No dark-matter claim.
- No total-baryon claim.
- No survey-level correlation claim.

## Consequence

B024 strengthens the lab's honesty more than it strengthens the headline. The signal is not a one-note artifact of choosing strong-discrepancy targets, but geometry and branch choice matter enough that a face-on or moderately inclined low-discrepancy control is now the clean next move.

Recommended next target: NGC5055 as a lower-discrepancy, less edge-on SPARC/HALOGAS control before writing public-facing SPARC comparison language.
