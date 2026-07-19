---
type: experiment_note
status: completed
created: 2026-05-15
program:
  - mesoscale-curvature
  - sparc
  - residual-closure
  - mechanism-audit
claim_level: mechanism_audit_no_dark_matter_claim
---

# B033 Scalar-Suppression Mechanism Test

## Purpose

B033 audits the B032 residual-adjacent `E/vc2` signal.

B032 showed that absolute electric-Weyl transfer loss did not positively track SPARC scalar residuals in the three primary non-edge-on galaxies, while the relative `E/vc2` ratio remained residual-adjacent. B033 asks whether that ratio survives after filtering denominator-risk rings.

## Source Package

- Experiment package: `codex_context/experiments/B033_scalar_suppression_mechanism_test`
- Script: `codex_context/scripts/b033_scalar_suppression_mechanism_test.py`
- Annotated ring table: `derived/B033_ANNOTATED_RING_MECHANISMS.csv`
- Group summary: `derived/B033_GROUP_MECHANISM_SUMMARY.csv`
- Mechanism summary: `derived/B033_MECHANISM_CLASS_SUMMARY.csv`
- Summary: `derived/B033_SUMMARY.json`

## Classification Rules

- `double_small_denominator_dominated`: `vc2 <= 0.02` and `E < 0.10`
- `scalar_suppression_with_material_E`: `vc2 <= 0.05` and `E >= 0.10`
- `material_E_with_ratio_support`: `E >= 0.30` and `E/vc2 >= 1`

## Primary Baseline Result

Primary non-edge-on baryon-sector filtered closure:

| Galaxy | All Ratio Corr | Filtered Ratio Corr | Spearman Filtered | Filtered Rings | Scalar-Suppression Rings |
|---|---:|---:|---:|---:|---:|
| NGC1003 | 0.0743 | 0.7690 | 0.8429 | 21 / 36 | 6 |
| NGC2403 | 0.5845 | 0.6917 | 0.8693 | 63 / 73 | 11 |
| NGC5055 | 0.5032 | 0.5965 | 0.8804 | 23 / 28 | 2 |

Filtered positive count: `3 / 3` primary baseline galaxies.

## Read

B033 reopens the mechanism question, but not the dark-matter claim.

After filtering denominator-dominated rings, the residual-vs-`E/vc2` alignment remains positive in all three primary baseline galaxies. This means the B032 ratio signal was not only a trivial artifact of double-small denominators.

However, absolute electric-Weyl loss still does not serve as a clean closure variable across the primary sample. The candidate mechanism is therefore not "more missing scalar residual means more absolute E loss." It is more specific:

> residual-adjacent radial structure appears in the relative tensor/scalar transfer hierarchy after scalar-denominator audit.

## Claim Boundary

- No dark-matter claim.
- No MOND test.
- No residual closure claim.
- Mechanism audit only.

## Consequence

B033 justifies targeted public-readiness nuisance tests. The next useful run is not more galaxies; it is observation-shaped perturbation of the residual-adjacent zones:

- support threshold perturbation,
- beam/proxy smoothing,
- inclination perturbation where applicable,
- retained reporting of absolute E, scalar `vc2`, and `E/vc2` together.
