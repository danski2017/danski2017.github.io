---
type: operating_system
status: active
created: 2026-05-13
owner: codex
topics:
  - obsidian
  - lab-memory
  - workflow
---

# Lab Memory Operating System

## Purpose

The Obsidian vault is the human-facing memory of the lab. The repo remains the source of artifacts, code, ledgers, papers, and history. Codex maintains the bridge between them.

## Roles

- Obsidian: curated memory, dashboards, indexes, claim boundaries, paper spines.
- `codex_context`: machine-side run products, scripts, summaries, cleanup manifests.
- Repo root: source doctrine, code, historical data, papers, and raw artifacts.

## Codex Write Zones

Codex may write to:

- `/Users/danski2017/Desktop/Atlas_Solver_Project/codex_context`
- `/Users/danski2017/Desktop/Atlas_Solver_Project/Relational_Labs/Relational_Labs`

Default vault writes should stay inside:

- `Relational_Labs/Relational_Labs/Atlas Codex Bridge`

## Curation Loop

1. Inventory relevant repo paths.
2. Classify them in [[../Indexes/Atlas Memory Triage Register|Atlas Memory Triage Register]].
3. Promote summaries into Obsidian notes.
4. Link notes into indexes and dashboards.
5. Keep claim boundaries close to public-facing language.
6. Avoid importing raw ledgers or heavy payloads as memory.

## Frontier Signal Memory

The vault should preserve frontier signals that survive initial sanity checks, even when interpretation is unsettled. Obsidian is the memory layer for these signals; repo execution comes only after passport and work-order discipline.

See [[Frontier Evidence Rule|Frontier Evidence Rule]].

## Promotion Criteria

A repo artifact deserves Obsidian promotion if it:

- changes current doctrine,
- supports an active experiment spine,
- defines a reusable method,
- closes or opens a scientific question,
- is needed for public/paper-facing explanation,
- preserves provenance for a current claim.

## Demotion Criteria

Treat material as historical or deprecated when it is:

- superseded by newer GFRO doctrine,
- duplicated by current root notes,
- a raw run payload without a current summary,
- a visually interesting artifact without validation,
- an old Q-readable scaffold not used for current interpretation.
