---
type: repo_overview
status: active
created: 2026-05-13
topics:
  - repo-map
  - atlas
---

# Repo Overview

The repo is a layered research instrument, not a flat memory corpus.

> Housekeeping update - 2026-05-19
>
> Root has been restored to a concise 13-file entry surface. Non-entry root
> notes, receipts, manifests, and historical method files were moved into
> `docs/`, `notes/`, or `archive/root_hygiene_20260519/`. See
> [[Repo Housekeeping 2026-05-19|Repo Housekeeping 2026-05-19]].

## Major Lanes

| Lane | Status | Size Signal | Use Rule |
|---|---|---:|---|
| `atlas/` | Active code | small | Read before implementation; current package map |
| `scripts/` | Active / historical mixed | about 1.1 MiB | Use targeted; legacy folder is historical |
| `docs/` | Canonical / supporting docs | small | Bootloaders, architecture references, repo support notes |
| `notes/` | Active / historical mixed | about 8 MiB | Hypotheses, private method history, retention notes, thread continuity |
| `papers/` | Canonical / review mixed | about 10 MiB | Public and internal paper corpus |
| `codex_context/` | Read-only Codex context cache unless promoted | about 2.4 GiB | Scripts, experiments, data mirrors, summaries, viewers; promote selectively |
| `Relational_Labs/Relational_Labs/` | Active Obsidian vault | about 25 MiB | Human-facing curated memory |
| `Relational_Math/` | First-class exploratory math lane | small | Math notes, ledgers, projects, passports |
| `configs/` | Active / historical configs | small | Reproduction inputs |
| `schemas/` | Active schemas | small | Validation and data contracts |
| `analysis/` | Historical / active mixed | about 858 MiB | Targeted archaeology, repo inventory, sandbox outputs |
| `baseline_scenes/` | Raw artifact / historical | about 232 MiB | Node -1 / solar-neighborhood lineage |
| `runs/` | Raw artifact / historical | about 800 MiB | Reproduction only |
| `archive/` | Historical / deprecated mixed | about 7.5 GiB | Provenance, quarantine, historical snapshots |
| `project_file_packs/` | Historical | about 34 MiB | Bootpack archaeology |

## Read Priority

For current science:

1. Obsidian bridge indexes and claim boundaries.
2. Root doctrine, current thread startup protocol, GFRO bootloader, and time-slice doctrine update.
3. Current experiment summaries B006-B013.
4. Papers and review notes.
5. Code/configs only when implementing or auditing.
6. Historical/raw lanes only by targeted search.

## Write Rule

Codex writes to:

- `codex_context/`
- `Relational_Labs/Relational_Labs/`

Other repo lanes are read-only unless explicitly authorized.

Current root doctrine and startup:

- `ATLAS_ROOT_README.txt`
- `ATLAS_BOOTLOADER_INDEX.txt`
- `docs/bootloaders/ATLAS_THREAD_STARTUP_PROTOCOL_v0_1.txt`
- `docs/bootloaders/ATLAS_THREAD_STARTUP_PROMPT_v0_1.txt`
- `docs/bootloaders/ATLAS_GFRO_ENGINE_BOOTLOADER_v0_1.txt`
- `docs/architecture/ATLAS_TIME_SLICE_GFRO_DOCTRINE_UPDATE_2026_05_19.txt`
- `DATA_ARCHITECTURE.txt`
- `RUN_OUTPUT_STANDARD.txt`
- `ATLAS_LANE_GOVERNANCE.txt`
