---
type: experiment
status: completed
run_id: B010-B012
date: 2026-05-13
claim_level: internal_convergence_suite
topics:
  - resolution-ladder
  - morphology-variants
  - witness-robustness
---

# B010-B012 Convergence Suite

## Purpose

Finish the next set of controls: method-resolution ladder, galaxy morphology variants, and witness-field robustness.

## Design

10K-source summary-only suite:

- B010: refine rings, sectors, grids, and kernels
- B011: barred, bulge-heavy, thick-disk, flocculent, disturbed outer-disk variants
- B012: midplane, off-plane, halo, radial-spoke, and survey-wedge witnesses

## Key Results

B010 was the strongest addition. Increasing coarse-method resolution generally lowered scalar rotation disagreement, but electric-Weyl/eigenframe disagreement did not collapse in lockstep.

B011 morphology median ratios:

- sector-annular: eigen/vc2 4.60, E/vc2 4.07
- CIC mesh: eigen/vc2 5.53, E/vc2 3.39
- adaptive: eigen/vc2 3.30, E/vc2 2.93
- low-order: eigen/vc2 2.86, E/vc2 2.61

B012 showed witness dependence. Halo-style witnesses were quieter for some methods; disc-adjacent, off-plane, spoke, and survey-wedge witnesses retained the stronger split.

## Interpretation

The pattern is not merely a small-N artifact, and not tied to one morphology or one witness field. It is also not uniform everywhere; the witness protocol matters.

## Source Artifacts

- `/Users/danski2017/Desktop/Atlas_Solver_Project/codex_context/experiments/B010_B012_convergence_suite`
