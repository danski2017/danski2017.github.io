---
type: atlas_platform_home
status: canonical
created: 2026-07-15
updated: 2026-07-26
aliases:
  - ATLAS Field Metric Viewer
  - Atlas Instrument
tags:
  - atlas-platform
  - viewer
  - thread-orientation
---

# Atlas Platform

> [!important] Canonical project instrument
> **Atlas Platform**, whose current UI title is **ATLAS Field Metric Viewer**, is
> the lab's single continuing project viewer. Extend this instrument through
> modular lanes. Do not build a replacement viewer unless the founder explicitly
> reverses this decision.

The live implementation is in the historical repo directory named
`pinch_lab_viewer`. The directory name is legacy; do not rename it casually
because scripts, manifests, documentation, and viewer-relative URLs depend on it.

## New Thread Start

**The vault root is the program's jump-off point.** Before (or alongside)
this platform sequence, a new thread should know the three root notes:
[[../../Atlas Mission Statement|Atlas Mission Statement]] (why the lab
exists), [[../../Atlas Platform Dashboard|Atlas Platform Dashboard]]
(current focus + all entry links), and
[[../../Lab Goals and Milestones|Lab Goals and Milestones]] (priorities
and the sprint register). The pasteable version of this whole
orientation lives in [[08 Boot Loader Prompt]]; the fastest catch-up on
current findings is [[09 Findings Digest 2026-07-18]].

Read these notes in order:

1. [[01 New Thread Orientation|New Thread Orientation]]
2. [[02 Architecture and Data Flow|Architecture and Data Flow]]
3. [[03 Repo ET and Artifact Location Map|Repo, ET, and Artifact Location Map]]
4. [[04 Operations and Validation Runbook|Operations and Validation Runbook]]
5. [[05 Dataset and Model Registry|Dataset and Model Registry]]
6. [[06 Current State and Development Contract|Current State and Development Contract]]
7. [[11 ET Temporal Harness Master Specification|ET Temporal Harness Master Specification]]
   for the sole current ET evolution/orchestration design basis
8. [[Evolution Log|Evolution Log]]
9. [[10 Vault GitHub Mirror Sync|Vault GitHub Mirror Sync]] for the controlled
   one-way Mac-source-to-GitHub vault publication routine

For the shortest safe handoff, point a new thread to this note and tell it to
follow [[01 New Thread Orientation]].

## Canonical Locations

| Role | Location |
|---|---|
| Atlas repo | `/Users/danski2017/Desktop/Atlas_Solver_Project` |
| Viewer root | `analysis/et_tov3_scout/pinch_lab_viewer/` |
| Viewer application | `analysis/et_tov3_scout/pinch_lab_viewer/index.html` |
| Viewer datasets | `analysis/et_tov3_scout/pinch_lab_viewer/datasets/` |
| Recovery Lab adapter | `analysis/et_tov3_scout/pinch_lab_viewer/recovery_lab/` |
| Imported Tools adapter | `analysis/et_tov3_scout/pinch_lab_viewer/imported_tools/` |
| Atlas ET scripts | `scripts/et_tov3_scout/` |
| Atlas ET configs | `configs/et_tov3_scout/` |
| Atlas ET analysis | `analysis/et_tov3_scout/` |
| Repo documentation | `docs/et_tov3_scout/` |
| Append-only lab log | `logs/et_tov3_scout_lab_log.txt` |
| Einstein Toolkit installation | `/Users/danski2017/Desktop/EinsteinToolkit` |
| Einstein Toolkit root | `/Users/danski2017/Desktop/EinsteinToolkit/Cactus` |
| ET diagnostic HDF5 | `/Users/danski2017/Desktop/EinsteinToolkit/Cactus/ATLAS_TOV3_DIAG` |
| Archived ET external cache | `/Users/danski2017/Desktop/EinsteinToolkit/atlas_external_data/zenodo_155394` |
| Temporal-pilot packet | `analysis/atlas_temporal_pilot/ATLAS_TEMPORAL_PILOT_I_ET_ARCHIVE_001/` |
| FUKA source | `/Users/danski2017/Desktop/EinsteinToolkit/Cactus/repos/fuka` |
| Public mirror checkout | `/Users/danski2017/Desktop/danski2017.github.io` |
| Vault mirror routine | `scripts/repo_tools/sync_vault_to_github_mirror.py` |
| ET temporal-harness master | `Atlas Codex Bridge/Atlas Platform/11 ET Temporal Harness Master Specification.md` |
| Reserved internal research frame | `Atlas Codex Bridge/Atlas Platform/12 Constraint Geometry and Return Maps - Internal Research Frame.md` |

## Viewer Launch

From the Atlas repo root:

```bash
python3 -m http.server 8792 \
  --bind 127.0.0.1 \
  --directory analysis/et_tov3_scout/pinch_lab_viewer
```

Then open `http://127.0.0.1:8792/`. The port is conventional, not permanent;
use another free port when needed. Do not open the viewer as `file://`, because
browser security blocks its dataset fetches.

## Source Of Truth

1. Manifests and machine-readable audit records control numerical provenance.
2. Repo scripts and configs control reproducibility.
3. The viewer is the lab's visual interrogation surface, not numerical proof by
   itself.
4. This Obsidian section controls orientation, operating practice, and history.
5. [[Evolution Log]] is append-only. Archived receipts are never rewritten.

## Governing Rules

- Preserve the working viewer before extending it.
- Add major features as isolated, toggleable lanes or adapters.
- Keep Atlas Native, Imported Tools, and Recovery Lab behavior independently
  removable where practical.
- Display matter density and constraint residuals before speculative overlays on
  new ET-derived substrates.
- Do not call glued, superposed, or custom conformally flat scenes fully fused GR.
- Follow [[../Best Practices/Compute Safety and Remote Execution Policy|Compute Safety and Remote Execution Policy]].
- The 8 GiB Mac mini is not a heavy numerical-relativity compute host.
- Do not touch `codex_context` unless explicitly asked.
- Append logs; do not overwrite historical log entries or trackers.

## Maintenance

Every material platform change must update:

- [[Evolution Log]] with a new appended entry;
- [[06 Current State and Development Contract]] if current behavior changed;
- [[03 Repo ET and Artifact Location Map]] if paths or dependencies changed;
- a receipt based on [[Templates/Platform Change Receipt Template]] when the
  change affects code, datasets, provenance, controls, or claim boundaries.
