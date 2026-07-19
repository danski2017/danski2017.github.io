---
type: experiment_note
status: completed
created: 2026-05-14
program:
  - mesoscale-curvature
  - sparc
  - residual-closure
claim_level: residual_closure_test_no_dark_matter_claim
---

# B032 Residual Closure Ledger

## Purpose

B032 tested the dark-matter-relevant bridge question:

> Does Atlas curvature-transfer loss organize the SPARC scalar residual `Vobs^2 - Vbar^2` in the existing local data?

No new data was downloaded.

## Source Package

- Experiment package: `codex_context/experiments/B032_residual_closure_ledger`
- Script: `codex_context/scripts/b032_residual_closure_ledger.py`
- Ring table: `derived/B032_RING_RESIDUAL_CLOSURE_TABLE.csv`
- Galaxy summary: `derived/B032_GALAXY_CLOSURE_SUMMARY.csv`
- Panel summary: `derived/B032_PANEL_SUMMARY.csv`
- Summary: `derived/B032_SUMMARY.json`

## Run Scope

- Ring closure rows: `930`
- Galaxy summary rows: `24`
- Panel rows: `72`
- Branches:
  - `hi_sector_ring`
  - `baryon_sector_ring`
- `M/L` variants:
  - low: disk `0.35`, bulge `0.50`
  - baseline: disk `0.50`, bulge `0.70`
  - high: disk `0.65`, bulge `0.90`

## Baseline Primary Result

Primary non-edge-on baryon-sector closure:

| Galaxy | Residual vs E | Residual vs E/vc2 | Spearman Residual vs E/vc2 | Median E/vc2 |
|---|---:|---:|---:|---:|
| NGC1003 | -0.7962 | 0.0743 | -0.2178 | 3.490 |
| NGC2403 | -0.6557 | 0.5845 | 0.8161 | 2.374 |
| NGC5055 | -0.3141 | 0.5032 | 0.8648 | 1.941 |

## Read

B032 does **not** close the dark-matter loop.

The absolute electric-Weyl transfer loss does not positively track the SPARC scalar residual in the three primary non-edge-on galaxies. In fact, baseline residual-vs-E correlations are negative for NGC1003, NGC2403, and NGC5055.

The relative `E/vc2` ratio is more residual-adjacent: it is positive in all three primary galaxies by Pearson correlation, and strongly positive by Spearman rank in NGC2403 and NGC5055. But that pattern appears because scalar `vc2` transfer error collapses faster than electric-Weyl transfer error in some radial zones, not because absolute E loss directly rises with the scalar residual.

## Interpretation

B032 strengthens the disciplined version of the thesis and blocks the premature version.

It does not support saying:

> The missing scalar residual is simply retained curvature that averaging threw away.

It does support saying:

> Residual structure is adjacent to a relative tensor/scalar transfer hierarchy, and the next question is whether scalar suppression under coarse transfer is the relevant mechanism.

## Claim Boundary

- No dark-matter claim.
- No MOND test.
- No survey-level closure.
- Ring correlations are descriptive.
- NGC0891 remains edge-on control only.

## Consequence

The next useful experiment, if any, should not be more galaxies. It should be a scalar-suppression mechanism test:

- hold absolute E transfer loss and scalar `vc2` transfer loss separately,
- identify where `vc2` collapse creates high `E/vc2`,
- test whether those zones correspond to SPARC residual structure under observation-shaped perturbations.
