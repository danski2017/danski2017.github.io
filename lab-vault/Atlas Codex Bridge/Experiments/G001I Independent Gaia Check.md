---
type: experiment_note
status: completed
created: 2026-05-15
topics:
  - gaia
  - independent-check
  - gfro
  - verification
---

# G001I Independent Gaia Check

G001I independently re-evaluates the G001H baseline branch/panel relation map over the same Gaia 25 pc cache, same source cuts, photometric mass proxy, and 0.05 pc softening.

The check intentionally uses a differently structured evaluator: it iterates over witness blocks rather than source blocks and writes a separate relation-map summary before comparing to G001H.

## Package

- Experiment package: `codex_context/experiments/G001I_independent_gaia_check`
- Report: `reports/G001I_REPORT.md`
- Comparison table: `derived/G001I_G001H_COMPARISON.csv`
- Certification: `certification/G001I_CERTIFICATION_DECISION.txt`

## Result

- Decision: `passed`
- Retained sources: `3894`
- Comparison rows: `12`
- Rows passing tolerance: `12/12`
- Tolerance: 2 percent relative p90 `E/scalar` plus sign match.

## Correction Caught

The first independent run exposed a scalar-channel issue in G001H: the scalar acceleration had been accumulated as per-block magnitudes instead of vector-summed before taking the norm.

G001H was corrected and rerun. After correction, G001I matched G001H across all 12 comparison rows.

## Corrected Baseline Best Split

- Panel: `field_fine`
- Branch: `local_cell_4pc`
- p90 scalar delta: `0.511363`
- p90 E delta: `4.10621`
- p90 eigenframe disagreement: `0.843221`
- p90 `E/scalar`: `8.02995`

## Boundary

This verifies the G001H implementation path. It does not change the mass-policy limitation or public claim boundary.
