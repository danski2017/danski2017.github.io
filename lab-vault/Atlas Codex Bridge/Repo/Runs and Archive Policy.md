---
type: raw_artifact_policy
status: active
created: 2026-05-13
topics:
  - runs
  - archive
  - storage
---

# Runs and Archive Policy

## Runs

Path: `runs`

Status: Raw Artifact / Historical.

Size signal: about 4.2 GiB.

Use:

- reproduction
- audit
- historical run recovery

Do not use as ordinary memory. Prefer summaries, manifests, and promoted notes.

## Archive

Path: `archive`

Status: Historical / Deprecated mixed.

Size signal: about 4.1 GiB.

Use:

- provenance
- recovery of old doctrine snapshots
- cleanup history

Do not use archived files as current steering doctrine unless promoted back into active canon.

## Cleanup Rule

Do not delete raw payloads without manifesting what was removed. Keep deletion manifests in `codex_context/cleanup_manifests` or an approved vault note.

