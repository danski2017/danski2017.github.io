---
type: experiment
status: completed
run_id: B009
date: 2026-05-13
claim_level: internal_scale_ladder
topics:
  - source-count-scaling
  - convergence
  - galaxy-coarse-graining
---

# B009 MW Source Count Scale Ladder

## Purpose

Test whether the retained/coarse delta scales as source count rises.

## Design

Summary-only source-count ladder at 2000, 5000, and 10000 source proxies with fixed witness points and multiple coarse methods.

## Key Results

The delta should not be linearly multiplied to Milky-Way star counts. The measured quantities behave like normalized convergence diagnostics:

```text
Delta(N) = Delta_inf + A / sqrt(N)
```

Median p90 eigenframe-over-vc2 ratios:

- annular: 3.02 -> 3.59 -> 3.86
- sector-annular: 3.06 -> 3.87 -> 4.38
- adaptive kernel: 2.66 -> 3.00 -> 3.17
- low-order multipole: 2.33 -> 2.67 -> 2.76
- CIC mesh: 3.21 -> 5.63 -> 5.46

## Interpretation

Increasing source count suppresses finite-source noise and exposes a method-dependent residual floor.

## Source Artifacts

- `/Users/danski2017/Desktop/Atlas_Solver_Project/codex_context/experiments/B009_mw_scale_ladder_summary`
