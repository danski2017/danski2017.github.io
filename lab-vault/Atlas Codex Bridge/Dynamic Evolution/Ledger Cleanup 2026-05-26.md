---
type: ledger_cleanup
status: completed
created: 2026-05-26
topics:
  - atlas-dynamics
  - ledger-retention
  - cleanup
---

# Ledger Cleanup 2026-05-26

## Purpose

Reduce generated ledger size after the Cluster12 robust run and dropout diagnostics.

The heavy ledgers had already been audited and summarized in Obsidian notes, so retaining all raw JSONL traces was no longer necessary.

## Before

Dynamic workspace:

`2.8G`

Largest generated ledgers:

- `cluster12_robust75_c20_scale2_20260526`: `703M`
- `cluster12_dropout_baseline_seeded_65_20260526`: `607M`
- `cluster12_dropout_rfloor075_63_20260526`: `598M`

## Preserved

Lightweight retained artifacts:

`/Users/danski2017/Desktop/Atlas_Solver_Project/codex_context/dynamic_evolution/skeleton_smoke_20260526/retained_run_summaries`

Preserved:

- robust 75 manifest
- robust 75 root-quality summary
- robust 75 seam-lineage summary
- robust 75 GIF and final frame
- dropout baseline manifest
- dropout baseline root-quality summary
- radius-floor dropout manifest
- radius-floor dropout root-quality summary
- radius-floor dropout seam-lineage summary

The Obsidian notes remain the narrative audit record.

## Removed

Removed raw heavy run directories:

- `cluster12_robust75_c20_scale2_20260526`
- `cluster12_dropout_baseline_seeded_65_20260526`
- `cluster12_dropout_rfloor075_63_20260526`
- cluster12 dry runs
- old c-toy sweep run ledgers
- old normalized seam sweep run ledgers
- old seam threshold sweep run ledgers
- old long/sourcefix smoke ledgers

Kept:

- source code and render scripts
- small sweep summaries
- small seam lineage summaries
- `skeleton_gfro_rootmeta_1step_20260526` as a compact root-metadata verification fixture
- current `out` folder

## After

Dynamic workspace:

`48M`

Retained summaries:

`7.1M`

## Read

The raw ledgers were cleaned after audit. The retained state is now documentation-first plus lightweight reproducibility artifacts.

Future robust runs should be treated as deliberate certification candidates, and should either use a reduced-retention mode or be cleaned immediately after manifest/gate/lineage summaries are written.
