---
type: code_map
status: active
created: 2026-05-13
topics:
  - atlas-code
  - implementation
---

# Atlas Code Map

## Purpose

`atlas/` is the core Python package. It contains configuration loading, weak-field/GR-relevant primitives, engine v2 runtime machinery, GCS/parity scaffolding, IO, and models.

## Subpackages

| Path | Status | Role |
|---|---|---|
| `atlas/config` | Active | Config load/validation |
| `atlas/core` | Active | Anchors, Christoffels, derivatives, metric, potentials, query |
| `atlas/diagnostics` | Active | Weak-field diagnostics |
| `atlas/engine_v2` | Active / legacy mixed | Runtime, ledgers, datums, parity runtime, patch frames, tidal tools |
| `atlas/evolve` | Active | Geodesics |
| `atlas/gcs` | Historical / scaffold active | GCS base, parity field/network, monopole visibility |
| `atlas/io` | Active | Anchors, diagnostics, ledgers, manifests, relational ledger exports, tidal eigenframe IO |
| `atlas/models` | Active | Anchor, node, probe, run state models |

## Current Read Rule

Read code before implementation. Do not assume root scripts are current if package code has an equivalent.

## Current Interpretation Rule

`atlas/gcs` and parity/Q tooling may still be useful for indexing/comparison/history. GFRO-era interpretation should prioritize declared GR-relevant quantities, ledgers, witness data, and electric-Weyl/eigenstructure where relevant.

## Hygiene Notes

There are `.DS_Store` and `__pycache__` artifacts in the code tree. Treat them as tooling noise, not memory.

