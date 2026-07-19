---
type: scripts_map
status: active
created: 2026-05-13
topics:
  - scripts
  - reproducibility
---

# Scripts Map

## Root `scripts/`

Mixed active and historical execution utilities.

Active-looking families:

- `atlas_retention_*`: retention-functional lane tooling
- `e001_*`, `e002_*`: extraction/audit families
- `ems_*`: EMS parent-support and strict audit scripts
- `run_engine_v2_*`: engine v2 execution/export
- `smoke_test_*`: runtime/ledger smoke tests
- `validate_parity_tidal_eigenframe.py`: tidal eigenframe validation
- `repo_tools/*`: repo doctor, lane census, bootstrap, digest

Historical / legacy:

- `legacy_root_sweeps_20260505/*`
- older B002/B003/B004 scout scripts unless explicitly revived
- `__pycache__`

## Codex Scripts

Path: `codex_context/scripts`

Current Codex-generated active simulations include:

- `b006_mw500_mesoscale_curvature_coarse_grain_control.py`
- `b007_mw1000_coarse_method_scale_study.py`
- `b008_mw2000_observational_coarse_grain_benchmark.py`
- `b009_mw_scale_ladder_summary.py`
- `b010_b012_convergence_suite.py`
- `b013_cosmic_web_averaging_test.py`

## Use Rule

Use scripts only with matching scene/config/report context. For new work, prefer summary-only outputs unless full ledgers are scientifically necessary.

