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

# B025 NGC5055 Clean Low-Discrepancy Control

## Purpose

B025 follows B024 with a cleaner low-discrepancy control. NGC0891 was valuable but edge-on. NGC5055 has a lower SPARC discrepancy than the strong target NGC1003 and a more usable inclination of `55 deg`, so it tests whether the scalar/tensor preservation hierarchy survives without the edge-on caveat.

## Source Package

- Experiment package: `codex_context/experiments/B025_ngc5055_clean_low_discrepancy_control`
- Script: `codex_context/scripts/b025_ngc5055_clean_low_discrepancy_control.py`
- HALOGAS cube folder: `codex_context/data/SPARC_Lelli2016/halogas_cubes/NGC5055_HR`
- Cube: `NGC5055-HR-cube.fits`, shape `169 x 1024 x 1024`, md5 `b79c400fe41e3c551b949d05c4b30332`
- Moment and column-density products were checksum verified.

## Geometry

SPARC inclination is `55 deg`.

B025 uses deprojected disc-plane HI support coordinates rather than the NGC0891 sky-plane control geometry. The major-axis proxy is inferred from the HALOGAS column-density support.

## Run Ledger

- SPARC median baseline `Vobs^2/Vbar^2`: `1.6335`
- SPARC max baseline `Vobs^2/Vbar^2`: `3.8333`
- Active support pixels: `23239`
- Source proxies retained: `6000`
- Witness points: `3072`
- HI mass basis: `1.1722e10 Msun`
- Support threshold: `2.85126e20`
- Inferred sky major-axis proxy: `174.939 deg`

## Branch Results

| Branch | Coarse Proxies | p90 vc2 Delta | p90 E Delta | p90 Eigenframe | p90 E/vc2 |
|---|---:|---:|---:|---:|---:|
| `hi_deprojected_radial_annular_axisymmetric` | 264 | 0.9057 | 0.9182 | 0.9771 | 1.0138 |
| `hi_deprojected_sector_annular` | 269 | 0.5326 | 0.8066 | 0.9246 | 1.5143 |
| `hi_deprojected_low_order_multipole` | 7 | 1.0000 | 0.9428 | 0.9316 | 0.9428 |

## Read

B025 weakens the dramatic version of the claim and strengthens the disciplined version.

Compared with NGC1003, the clean low-discrepancy target shows a milder tensor-over-scalar separation. The best scalar branch is still `hi_deprojected_sector_annular`, and it still preserves scalar rotation-like structure better than electric-Weyl/eigenframe structure. But the p90 `E/vc2` ratio is `1.5143`, not the several-times gap seen in NGC1003 or the edge-on relative hierarchy seen in NGC0891.

That matters. The emerging story is not "SPARC discrepancy causes Atlas tensor loss." The honest story is subtler: common coarse branches have different transfer behavior for scalar rotation proxies and electric-Weyl/eigenframe structure, and that transfer behavior appears to depend on target morphology, support geometry, and coarse method.

## Claim Boundary

- HI-only source-proxy witness.
- Deprojected low-discrepancy control.
- No dark-matter claim.
- No total-baryon claim.
- No survey-level correlation claim.

## Consequence

B025 gives the lab a cleaner control than B024. It suggests the SPARC-facing paper should avoid simple monotonic claims and instead frame the result as a method-sensitive tensor/scalar transfer-function study across real HI support scenes.

Recommended next move: synthesize B021-B025 into a four-target real-data ledger before adding more cubes.
