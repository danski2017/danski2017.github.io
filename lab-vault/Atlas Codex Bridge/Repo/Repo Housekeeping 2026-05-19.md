---
type: repo_housekeeping_receipt
status: active
created: 2026-05-19
topics:
  - repo-housekeeping
  - root-surface
  - bcw
  - codex
---

# Repo Housekeeping 2026-05-19

## Summary

Codex executed the approved repo housekeeping pass for the Atlas repo.

Primary outcome:

- Root was reduced to 13 files.
- Root now functions as a concise entry surface.
- Non-entry root files were moved into `docs/`, `notes/`, or `archive/root_hygiene_20260519/`.
- Repo tools were updated for the BCW-era startup contract.
- Obsidian-facing lane classification READMEs were added for `Relational_Labs/`, `Relational_Math/`, `codex_context/`, and `docs/scene_passports/`.

## Current Root Entry Surface

Root files after cleanup:

- `.gitignore`
- `ATLAS_ARCHITECTURE_CANON.txt`
- `ATLAS_BOOTLOADER_INDEX.txt`
- `ATLAS_LANE_GOVERNANCE.txt`
- `ATLAS_ROOT_README.txt`
- `ATLAS_SCENE_PASSPORT.txt`
- `DATA_ARCHITECTURE.txt`
- `HYPOTHESIS_INDEX.txt`
- `LAB_LOG.txt`
- `MILESTONES.txt`
- `PROJECT_TRACKER.txt`
- `RUN_OUTPUT_STANDARD.txt`
- `SESSION_NOTES.txt`

## Important Moves

- `Atlas_Datum_Bible_v0_3_1_BCW_L001.txt` moved to `docs/architecture/Atlas_Datum_Bible_v0_3_1_BCW_L001.txt`.
- `ATLAS_MASTER_PROJECT_INSTRUCTIONS.txt`, `ATLAS_RETENTION_PIPELINE_INDEX.txt`, and `PREFERRED_SESSION_SEED_FILES.txt` moved to `docs/repo/`.
- Hypothesis seed files moved to `notes/hypotheses/`.
- Parity stack architecture/history files moved to `notes/private_method/architecture_history/`.
- Method notes and findings moved to `notes/private_method/method_notes/` and `notes/private_method/findings/`.
- Harvest logs, receipts, schema patches, tracker-update summaries, and root macOS metadata moved to `archive/root_hygiene_20260519/`.

## Repo Tool Updates

Updated:

- `scripts/repo_tools/atlas_session_bootstrap.py`
- `scripts/repo_tools/atlas_lane_census.py`
- `scripts/repo_tools/atlas_repo_doctor.py`
- `docs/repo/ATLAS_REPO_TOOL_BUNDLE_v0_1.txt`

Added:

- `scripts/repo_tools/atlas_hygiene_report.py`

Tooling now checks current startup doctrine:

- `docs/bootloaders/ATLAS_THREAD_STARTUP_PROTOCOL_v0_1.txt`
- `docs/bootloaders/ATLAS_THREAD_STARTUP_PROMPT_v0_1.txt`
- `docs/bootloaders/ATLAS_GFRO_ENGINE_BOOTLOADER_v0_1.txt`
- `docs/architecture/ATLAS_TIME_SLICE_GFRO_DOCTRINE_UPDATE_2026_05_19.txt`
- `ATLAS_LANE_GOVERNANCE.txt`

`CURRENT_IMPLEMENTATION_ORIENTATION.txt` and `MODEL_ARCHITECTURE_MAP.txt` remain historical/bootpack references, not required root files.

Doctrine update:
Later on 2026-05-19, GFRO was re-promoted for declared same-time-slice
modeling and BCW was demoted to historical candidate status. See
[[GFRO Time-Slice Doctrine Re-Promotion 2026-05-19|GFRO Time-Slice Doctrine Re-Promotion 2026-05-19]].

## Verification

Latest verification outputs:

- `analysis/repo_inventory/repo_doctor_20260519T050504Z/REPO_DOCTOR_REPORT.txt`
- `analysis/repo_inventory/lane_census_20260519T050504Z/`
- `analysis/repo_inventory/session_bootstrap_20260519T050504Z/`
- `analysis/repo_inventory/hygiene_report_20260519T050431Z/`

Repo doctor result:

- All required orientation files: OK
- Root file count: 13

Lane census improvement:

- `codex_context`, `Relational_Labs`, `Relational_Math`, `notes`, `docs/architecture`, and `docs/scene_passports` now classify into explicit lanes instead of falling into `OTHER`.

## Current Caution

The Git worktree still contains many pre-existing uncommitted, deleted, and untracked files. Do not interpret the status noise as a single logical change unless staged deliberately by pass.

Next recommended pass:

1. Review and stage root-surface restoration separately.
2. Review archive/root hygiene moves separately.
3. Review repo tool updates separately.
4. Defer heavy archive deletion or compression until a separate retention decision.
