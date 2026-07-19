# Atlas Platform

This directory is the canonical implementation root for **Atlas Platform**, whose
current UI title is **ATLAS Field Metric Viewer**.

`pinch_lab_viewer` is a historical directory name retained for compatibility.
Do not rename it without migrating every script, manifest, relative URL, and
documentation reference.

## Start Here

New threads must begin with the Obsidian orientation:

`Relational_Labs/Relational_Labs/Atlas Codex Bridge/Atlas Platform/00 Atlas Platform Home.md`

Repo-side orientation:

`docs/et_tov3_scout/ATLAS_PLATFORM_START_HERE.md`

## Launch

From the Atlas repo root:

```bash
python3 -m http.server 8792 \
  --bind 127.0.0.1 \
  --directory analysis/et_tov3_scout/pinch_lab_viewer
```

Open `http://127.0.0.1:8792/`. Do not use `file://`; dataset fetches require an
HTTP origin.

## Directory Ownership

- `index.html`: live application
- `datasets/`: Atlas Native compact payloads
- `imported_tools/`: advisory external-tool launch manifest and outputs
- `recovery_lab/`: removable Recovery Lab adapter and payloads
- `pinch_lab_viewer_*`: historical UI QA screenshots

Continue this instrument in place. Major features should enter through isolated,
toggleable lanes and must preserve existing behavior, provenance, and claim
boundaries.

