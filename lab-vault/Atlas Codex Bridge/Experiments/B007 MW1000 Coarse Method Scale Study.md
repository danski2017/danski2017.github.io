---
type: experiment
status: completed
run_id: B007
date: 2026-05-13
claim_level: internal_method_matrix
topics:
  - galaxy-coarse-graining
  - method-comparison
  - electric-weyl
---

# B007 MW1000 Coarse Method Scale Study

## Purpose

Move beyond a small control and test whether the retained/coarse delta depends on the averaging method.

## Design

1000-source Milky-Way-like scene with tilted-ring fit, annular averaging, sector annular averaging, CIC particle mesh, Gaussian/kernel grid, and low-order multipole proxy.

## Key Results

Method-dependent transfer functions appeared. Median p90 ratios included:

- tilted ring: eigen/vc2 3.08, E/vc2 2.76
- annular: eigen/vc2 3.17, E/vc2 2.83
- sector annular: eigen/vc2 3.21, E/vc2 2.88
- CIC mesh: eigen/vc2 3.20, E/vc2 2.86
- Gaussian kernel: eigen/vc2 2.64, E/vc2 2.41
- low-order multipole: eigen/vc2 2.46, E/vc2 2.32

## Interpretation

B007 made the story method-level rather than one-recipe-specific.

## Source Artifacts

- `/Users/danski2017/Desktop/Atlas_Solver_Project/codex_context/experiments/B007_mw1000_coarse_method_scale_study`
