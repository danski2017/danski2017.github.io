---
type: reusable_components
status: active
created: 2026-05-13
topics:
  - architecture
  - reusable-code
---

# Reusable Components Register

## Current Reusable Code Sources

### B009 Core

Path:

`codex_context/scripts/b009_mw_scale_ladder_summary.py`

Reusable pieces:

- package layout helpers
- cap enforcement
- sha256 manifest pattern
- deterministic witness sampling
- source-count ladder pattern
- electric-Weyl/eigen evaluator
- retained/coarse summarizer
- asymptote fitting

### B013 Cosmic Web

Path:

`codex_context/scripts/b013_cosmic_web_averaging_test.py`

Reusable pieces:

- cosmic-web source builder
- void/filament/wall/cluster/lightcone witness panels
- cartesian grid reduction
- Gaussian density grid reduction
- spherical average reduction
- component centroid reduction
- acceleration-based scalar comparison

### B014 Convergence Ladder

Path:

`codex_context/scripts/b014_cosmic_web_convergence_ladder.py`

Reusable pieces:

- two-axis source-count/resolution ladder
- multi-panel convergence table
- asymptote fits across source-count rungs
- Obsidian-friendly summary interpretation

## Refactor Candidate

The repeated helpers have been promoted into a small reusable module under:

`codex_context/scripts/atlas_simlib.py`

Current functions:

- package setup and manifest
- cap enforcement
- CSV/JSON writing
- asymptote fitting
- retained/coarse summary metrics
- p50/p90 helpers
- ratio helper

Remaining future candidates:

- witness panel utilities
- common report section builder
- domain-specific source builders

Keep this library inside `codex_context` unless the lab decides to promote stable pieces into the main `atlas/` package.

## Adoption Rule

New B-runs should import `atlas_simlib` for package layout, cap checks, CSV/JSON writing, manifests, and asymptote fits. Completed B006-B014 artifacts should not be rewritten just to adopt the helper.

New B-runs should also include an Atlas declaration block: Node -1, Node 0, Node 1, Node 2+, datum roster, witness panels, GFRO relation-map declaration, field-sieve emission rule, Node Psi emitted-diagnostic status, Node P/A status, retention status, and claim ladder status.

## GFRO Emitter Support Candidate

Future `atlas_simlib` helpers should support:

- relation-map metadata blocks,
- emitted ledger/registry manifest helpers,
- retention-status fields,
- witness-ranking summaries,
- field-sieve emission provenance.
