---
type: memory_triage_register
status: active
created: 2026-05-13
owner: codex
topics:
  - repo-memory
  - obsidian
  - triage
---

# Atlas Memory Triage Register

This note tells Codex and future lab agents how to treat the repo as memory.

The repo is dense and layered. Not every file should steer current science. This register separates canonical doctrine, active program memory, historical provenance, deprecated scaffolding, and raw artifacts.

## Status Vocabulary

| Status | Meaning | Use Rule |
|---|---|---|
| Canonical | Current doctrine or trusted operating rule | Read first, cite carefully |
| Active | Current program evidence or planning | Use for current work |
| Historical | Useful provenance, superseded by newer doctrine | Read for context, not steering |
| Deprecated | Known old branch, duplicate, or superseded scaffold | Avoid unless explicitly auditing |
| Raw Artifact | Heavy data, run payload, ledgers, generated outputs | Do not ingest into memory wholesale |
| Unknown | Needs review before use | Inspect before trusting |

## Top-Level Repo Triage

| Path | Status | Why It Matters | Current Use | Superseded By / Caution |
|---|---|---|---|---|
| `ATLAS_ROOT_README.txt` | Canonical | Concise repo entry surface and doctrine warning | Session orientation | Trust over archived root files |
| `ATLAS_MASTER_PROJECT_INSTRUCTIONS.txt` | Canonical | Role, lab boundaries, GR/GFRO governance | Agent alignment | Some role labels are cross-agent, but doctrine is useful |
| `ATLAS_ARCHITECTURE_CANON.txt` | Canonical | Architecture canon | Doctrine lookup | Prefer current root version over archived versions |
| `DATA_ARCHITECTURE.txt` | Canonical | Ledger/data architecture | Reproducibility rules | Prefer root over archive snapshots |
| `ATLAS_SCENE_PASSPORT.txt` | Canonical | Scene declaration standard | Serious run setup | None |
| `PROJECT_TRACKER.txt` | Active | Large continuity tracker | Project archaeology and current strands | Verify freshness against newer notes |
| `LAB_LOG.txt` | Active | Chronological lab continuity | Provenance | Large; use targeted search |
| `ATLAS_GFRO_ORIENTATION_PACKET_20260513T044237Z.txt` | Canonical | GFRO-era orientation packet | Current boot context | Dense but high value |
| `ATLAS_FINITE_CURVATURE_BUDGET_HARVEST_20260513T044429Z.txt` | Active | Current finite curvature-budget result | Follow-on simulation planning | Claim boundaries are explicit |
| `codex_context/experiments/B006-B013` | Active | Current mesoscale curvature evidence spine | Paper/website/convergence planning | Summary notes preferred over raw ledgers |
| `codex_context/synthesis` | Active | Codex-side synthesis drafts | Obsidian import source | Draft status unless promoted |
| `Relational_Labs/Relational_Labs` | Active | Obsidian vault and human lab memory | Human-facing memory layer | Codex writes primarily in `Atlas Codex Bridge/` |
| `Relational_Labs/Relational_Labs/Papers` | Canonical / Historical | Paper corpus and public/internal theory stack | Doctrine and paper provenance | Some duplicates need dedupe |
| `Relational_Labs/Relational_Labs/_txt` | Historical / Canonical mirror | Imported root doctrine and tracker copies | Fallback mirror | Prefer current root for doctrine |
| `notes/gfro_orientation_packets_20260513` | Active | Recent GFRO orientation packets | Startup/continuity | Use latest packet first |
| `notes/retention_pipeline_20260509` | Active / Historical | Retention-functional lane | Memory curation methods | Not all candidates promoted |
| `notes/ems_in_lsn_parent_bath_audit_*` | Active / Historical | EMS/LSN parent-context audit | GFRO context research | Use summaries and decisions first |
| `papers/public/gcs_series` | Canonical | Public GCS paper series | Public theory lineage | Prefer final PDFs and matching txt when present |
| `papers/review_notes` | Active | Review/decision notes | Paper polishing and claim control | Not doctrine by itself |
| `atlas/` | Active | Core code package | Implementation source | Read code before modifying |
| `scripts/` | Active / Historical | Repo scripts and utilities | Execution/inspection | Legacy subfolder is historical |
| `docs/bootloaders` | Canonical | Session bootloaders and role-lane orientation | Agent startup | Some overlap with root docs |
| `docs/architecture` | Canonical / Historical | Ledger and architecture design notes | Architecture lookup | Verify against root canon |
| `baseline_scenes` | Raw Artifact / Historical | Node -1 / solar-neighborhood scene lineage | Reproduction and provenance | 232 MiB; do not ingest wholesale |
| `runs` | Raw Artifact / Historical | Large generated runs | Audit/reproduction only | 4.2 GiB; not active memory |
| `archive` | Historical / Deprecated | Prior snapshots, quarantines, backups | Provenance only | 4.1 GiB; never steering by default |
| `analysis` | Historical / Active mixed | Older parity/network analysis and figures | Targeted archaeology | 691 MiB; classify per subfolder |
| `project_file_packs` | Historical | Bootpacks and bundles | Rebuild old session context | Prefer current repo/vault |
| `configs` | Active / Historical | Scene and engine configs | Reproduction | Check matching run/report |
| `schemas` | Active | Data schemas | Validation | Keep small and useful |
| `data` | Raw Artifact | External/derived data | Reproduction only | Do not memory-ingest wholesale |
| `.venv` | Deprecated / Tooling | Environment payload | Ignore for memory | Never ingest |
| `.git` | Tooling | Version history | Use git commands only | Never index as lab memory |

## Current Priority Read Order

1. [[../Synthesis/Claim Boundaries|Claim Boundaries]]
2. [[Active Doctrine Index]]
3. [[Mesoscale Curvature Experiment Index]]
4. [[Repo Layer Map]]
5. [[Paper Corpus Index]]
6. [[Historical Strata and Deprecation Notes]]

## Standing Instruction

When answering science questions, prioritize Canonical and Active notes. Use Historical material for provenance. Treat Deprecated and Raw Artifact paths as non-steering unless the task is explicitly reproduction, audit, cleanup, or archaeology.

