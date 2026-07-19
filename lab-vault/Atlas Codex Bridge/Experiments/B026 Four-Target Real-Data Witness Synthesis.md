---
type: experiment_note
status: completed
created: 2026-05-14
program:
  - mesoscale-curvature
  - sparc
  - halogas
  - real-data-synthesis
claim_level: internal_synthesis
---

# B026 Four-Target Real-Data Witness Synthesis

## Purpose

B026 consolidates the current HALOGAS/SPARC HI witness lane before adding more cubes. The goal is to see the shape across targets, not chase the loudest single number.

## Source Package

- Experiment package: `codex_context/experiments/B026_four_target_real_data_witness_synthesis`
- Script: `codex_context/scripts/b026_four_target_real_data_witness_synthesis.py`
- Table: `derived/B026_FOUR_TARGET_WITNESS_TABLE.csv`
- Summary: `derived/B026_SUMMARY.json`

## Four-Target Ledger

| Run | Galaxy | Class | Geometry | SPARC Median | p90 vc2 | p90 E | p90 Eigen | E/vc2 |
|---|---|---|---|---:|---:|---:|---:|---:|
| B021 | NGC2403 | moderate discrepancy pilot | deprojected disc bridge | 2.277 | 0.3238 | 0.4431 | 0.7280 | 1.3686 |
| B022 | NGC1003 | strong discrepancy target | deprojected disc control | 5.023 | 0.03463 | 0.1697 | 0.03518 | 4.9015 |
| B024 | NGC0891 | low discrepancy control | edge-on sky-plane | 1.377 | 0.00935 | 0.04297 | 0.000302 | 4.5946 |
| B025 | NGC5055 | low discrepancy control | deprojected disc control | 1.634 | 0.5326 | 0.8066 | 0.9246 | 1.5143 |

## Small-N Diagnostics

- Pearson SPARC discrepancy vs p90 `E/vc2`: `0.4815`
- Pearson SPARC discrepancy vs p90 `E`: `-0.3128`
- Pearson SPARC discrepancy vs p90 `vc2`: `-0.4199`
- Pearson SPARC discrepancy vs p90 eigenframe: `-0.4227`

These are descriptive only. `n=4` and the geometries are heterogeneous.

## Read

B026 says the honest paper spine is a transfer-function story, not a monotonic SPARC-discrepancy story.

The strongest ratio case is NGC1003, but NGC0891 also has a high ratio because the scalar branch is extremely tightly preserved in an edge-on sky-plane control. NGC5055 is the cleanest low-discrepancy deprojected control and shows a milder split. That combination rules out a simple "strong scalar discrepancy means stronger tensor loss" story at this stage.

What survives is still important: common coarse branches do not transfer scalar rotation-like information and local electric-Weyl/eigenframe structure with one universal fidelity.

## Claim Boundary

- Internal synthesis only.
- HI-only source-proxy witnesses.
- No dark-matter claim.
- No MOND test.
- No total-baryon claim.
- No survey-level monotonic law.

## Next Move

The next science move should be baryonic merge or nuisance hardening, not simply more cubes:

- merge SPARC stellar disk and bulge mass-model rows into matched source-proxy scenes,
- add beam/noise/inclination nuisance sweeps,
- then decide whether more HALOGAS cubes are needed.
