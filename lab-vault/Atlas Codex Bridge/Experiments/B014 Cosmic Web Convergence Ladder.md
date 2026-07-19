---
type: experiment
status: completed
run_id: B014
date: 2026-05-13
claim_level: internal_convergence_probe
topics:
  - cosmic-web
  - averaging
  - convergence
  - electric-weyl
---

# B014 Cosmic Web Convergence Ladder

## Purpose

Follow up B013 with a two-axis convergence ladder: source count and coarse-method resolution.

## Design

Source counts:

- 9000
- 18000
- 36000

Witness panels:

- void
- filament
- wall
- cluster outskirts
- mixed lightcone proxy

Methods:

- cartesian grid: coarse / standard / fine
- Gaussian density grid: coarse / standard / fine
- spherical average: coarse / standard / fine
- component centroids: fixed

Outputs were summary-only. No full tensor ledgers were stored.

## Key Results

B014 did not wash out the B013 signal. It showed method-dependent residuals under source-count and resolution refinement.

The cosmic-web lane is subtler than the galaxy lane. Scalar acceleration deltas often improve with resolution, while electric-Weyl/eigenframe disagreements remain high by branch and panel.

Selected asymptote fits:

- cartesian grid fine: accel 0.435, E 0.717, eigenframe 0.914, eigen/accel 1.81
- cartesian grid standard: accel 0.520, E 0.662, eigenframe 0.921, eigen/accel 1.47
- Gaussian fine: accel 0.719, E 0.805, eigenframe 0.917, eigen/accel 1.30
- spherical fine: accel 0.648, E 0.863, eigenframe 0.916, eigen/accel 1.19
- component centroids: accel 0.841, E 0.862, eigenframe 0.961, eigen/accel 1.04

## Interpretation

Safe claim:

> In a weak-field cosmic-web proxy, averaging operations exhibit method-dependent geometric transfer functions that remain visible under source-count and resolution refinement.

This is not a cosmological parameter claim. It is not a dark-energy or dark-matter claim. It is an internal transfer-function result.

## Source Artifacts

- `/Users/danski2017/Desktop/Atlas_Solver_Project/codex_context/experiments/B014_cosmic_web_convergence_ladder`

