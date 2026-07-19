---
type: experiment_plan
status: planned
created: 2026-05-14
program:
  - mesoscale-curvature
  - sparc
  - residual-closure
claim_level: planned_dark_matter_relevant_test
---

# B032 Residual Closure Ledger Plan

## Purpose

B032 tests the unresolved bridge question:

> Does Atlas curvature-transfer loss organize any structured part of the SPARC scalar residual `Vobs^2 - Vbar^2`?

This is the most direct route from the current transfer-function result toward dark-matter-relevant evidence, while keeping the claim boundary intact.

## Why It Matters

B026-B031 show that scalar rotation-like summaries and electric-Weyl/eigenframe structure do not pass through coarse galaxy representations with one universal fidelity.

B032 asks whether that transfer loss is related to the actual SPARC scalar residual, or whether it is orthogonal.

## Inputs

No new downloads.

Use:

- local SPARC catalog and mass-model rows,
- B020/B022/B024/B025 HI source scenes,
- B026/B027/B028/B031 synthesis and draft ledgers.

## Targets

Primary:

- NGC2403
- NGC1003
- NGC5055

Caveated:

- NGC0891 as edge-on sky-plane control only.

## Core Test

Build a ring-resolved closure ledger.

For each SPARC radial row, compare:

- scalar residual `Vobs^2 - Vbar^2`,
- residual ratio `Vobs^2 / Vbar^2`,
- electric-Weyl transfer loss,
- eigenframe disagreement,
- scalar `vc2` transfer loss,
- `E/vc2`,
- HI support proxy,
- baryonic surface-brightness proxy.

## Success / Failure Logic

B032 strengthens the dark-matter-relevant thesis if scalar residual peaks and curvature-transfer-loss peaks align radially in multiple non-edge-on galaxies.

B032 weakens the thesis if the relationship is inconsistent, geometry-driven, or collapses under modest `M/L` perturbation.

B032 still supports the bounded methods claim if transfer loss persists but does not organize the scalar residual.

## Outputs

Planned package:

`codex_context/experiments/B032_residual_closure_ledger`

Required ledgers:

- ring residual closure table,
- galaxy closure summary,
- radial panel summary,
- scene passport,
- claim-boundary summary.

## Claim Boundary

Do not claim:

- dark matter is unnecessary,
- dark matter is falsified,
- MOND is tested,
- baryons alone explain rotation curves,
- SPARC discrepancy is explained survey-wide.

Allowed if successful:

> In the tested local SPARC/HALOGAS source-proxy scenes, radial structure in scalar mass-discrepancy residuals is partially organized by Atlas curvature-transfer loss metrics.

## Recommendation

Run B032 before any public dark-matter-adjacent language. This is the experiment most likely to tip the story either way.
