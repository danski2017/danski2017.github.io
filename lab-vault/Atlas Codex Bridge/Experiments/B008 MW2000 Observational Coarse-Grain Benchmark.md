---
type: experiment
status: completed
run_id: B008
date: 2026-05-13
claim_level: internal_observational_benchmark
topics:
  - galaxy-coarse-graining
  - observational-reconstruction
  - tilted-ring
---

# B008 MW2000 Observational Coarse-Grain Benchmark

## Purpose

Add observation-facing reductions to the retained/coarse comparison.

## Design

2000-source scene with inclined line-of-sight velocity projection, beam-smoothed velocity/surface-density maps, tilted-ring rotation recovery, pseudo-source reconstruction, CIC mesh, adaptive kernel, and low-order multipole branches.

## Key Results

The observation-facing tilted-ring branch damaged scalar rotation too, so its tensor/scalar ratio was less clean. Other branches still showed mesoscale-curvature loss.

Median p90 ratios:

- observed tilted-ring: eigen/vc2 1.16, E/vc2 1.12
- surface-density grid: eigen/vc2 3.66, E/vc2 3.03
- CIC: eigen/vc2 4.23, E/vc2 3.77
- adaptive kernel: eigen/vc2 3.40, E/vc2 3.04
- multipole: eigen/vc2 2.75, E/vc2 2.51

## Interpretation

B008 added nuance: some observational reductions damage scalar summaries too. The stronger claim is not universal scalar preservation, but differential information transfer by method.

## Source Artifacts

- `/Users/danski2017/Desktop/Atlas_Solver_Project/codex_context/experiments/B008_mw2000_observational_coarse_grain_benchmark`
