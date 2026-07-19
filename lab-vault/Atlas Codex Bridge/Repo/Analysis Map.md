---
type: analysis_map
status: active
created: 2026-05-13
topics:
  - analysis
  - historical
---

# Analysis Map

`analysis/` is historical/active mixed and relatively large. Do not ingest wholesale.

## Subfolders

| Path | Status | Use |
|---|---|---|
| `analysis/parity_network` | Historical / active lineage | parity/network result archaeology |
| `analysis/paper3_figures` | Active / historical | paper figure captions/results summary |
| `analysis/repo_inventory` | Historical utility | cleanup and inventory provenance |
| `analysis/datum_refinement` | Historical / schema lineage | child datum schema history |
| `analysis/sandbox` | Historical | older scaffold/method experiments |
| `analysis/collab` | Historical / cross-wing | collaboration handoff material |
| `analysis/bridge_tidal_classifier_*` | Raw/generated | audit only |

## High-Value Sandbox Lanes

- `analysis/sandbox/lumen_lattice_benchmark_v0_1`: first interactive EMS Lumen Lattice / Released Coherence Lattice viewer.
- `analysis/sandbox/ems_in_lsn_full_riemann_gfro_lumen_v0_1`: EMS-in-LSN full-Riemann GFRO Lumen microscope lane.
- `analysis/sandbox/ems_wireframe_v0` and `analysis/sandbox/ems_wireframe_v1`: historical EMS wireframe construction lanes.
- `analysis/sandbox/ems_offset_lattice_v2`: offset lattice method lineage.

## Read Rule

Use targeted search. Prefer `paper3_results_summary.md`, figure captions, manifests, and summaries over raw artifacts.

## Current Relevance

Useful for provenance, older parity-network results, and Lumen/wireframe lineage. Current mesoscale curvature work is better represented in `codex_context/experiments/B006-B014`.
