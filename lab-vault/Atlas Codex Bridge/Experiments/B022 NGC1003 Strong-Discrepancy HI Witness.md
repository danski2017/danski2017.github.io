---
type: experiment_note
status: completed
created: 2026-05-14
lane: galaxy-averaging
topics:
  - HALOGAS
  - SPARC
  - HI-cube
  - strong-discrepancy
  - electric-Weyl
  - NGC1003
---

# B022 NGC1003 Strong-Discrepancy HI Witness

Codex repeated the real-data HI cube witness lane on NGC1003, a stronger
SPARC discrepancy target than NGC2403.

Experiment package:

`/Users/danski2017/Desktop/Atlas_Solver_Project/codex_context/experiments/B022_ngc1003_strong_discrepancy_hi_witness`

Primary outputs:

- `derived/B022_NGC1003_HI_SOURCE_PROXY_SCENE.csv`
- `derived/B022_NGC1003_SPARC_RING_ALIGNMENT.csv`
- `derived/B022_METHOD_SUMMARY.csv`
- `derived/B022_PANEL_SUMMARY.csv`
- `derived/B022_SUMMARY.json`
- `reports/B022_REPORT.txt`

## Source

- SPARC quality flag: `1`
- SPARC median baseline `Vobs^2 / Vbar^2`: `5.023`
- SPARC max baseline `Vobs^2 / Vbar^2`: `10.034`
- HALOGAS HR cube: downloaded and checksum verified

## Main Result

Best scalar-preserving branch: `hi_sector_annular`

- p90 `vc2` delta: `0.03463`
- p90 electric-Weyl Frobenius delta: `0.16974`
- p90 eigenframe disagreement: `0.03518`
- p90 `E/vc2`: `4.9015`

Panel behavior:

- sector-annular mid-panel p90 `E/vc2`: `5.8999`
- sector-annular outer-panel p90 `E/vc2`: `3.4625`
- radial-annular outer-panel p90 `E/vc2`: `2.7107`

## Read

NGC1003 strengthens the real-data story. In a stronger SPARC-discrepancy target,
the best scalar coarse branch preserves `vc2` very tightly, while the
electric-Weyl Frobenius witness remains several times less preserved by the same
comparison ratio.

This does not explain dark matter. It says something narrower and more lawful:
even in real cube-derived HI support, scalar rotation preservation and tensorial
curvature-identity preservation are separable observables.

## Claim Boundary

No dark-matter claim. No total-baryon claim. No full-galaxy curvature claim.
This is HI-only and source-proxy-limited. It needs a baryonic merge and
multi-galaxy repeat before public claim language.

## Next

B023 should consolidate NGC2403 and NGC1003 into a two-galaxy real-data witness
comparison, then choose whether to:

- add UGC04278 as a third strong-discrepancy target, or
- merge NGC2403/NGC1003 HI with SPARC stellar disk rows for total-baryon proxy
  witnesses.
