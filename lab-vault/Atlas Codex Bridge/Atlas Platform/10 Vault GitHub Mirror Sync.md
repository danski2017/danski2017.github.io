---
type: operations_runbook
status: canonical
created: 2026-07-22
updated: 2026-07-22
tags: [atlas-platform, vault, github, sync, publication]
---

# Vault GitHub Mirror Sync

## Authority and direction

The Mac vault is always the source of truth:

`/Users/danski2017/Desktop/Atlas_Solver_Project/Relational_Labs/Relational_Labs/`

The public GitHub mirror target is only:

`/Users/danski2017/Desktop/danski2017.github.io/lab-vault/`

Direction is strictly Mac vault → GitHub `lab-vault/`. Nothing in this routine copies, merges, or restores GitHub vault content into the Mac source. A GitHub-only vault edit is temporary and will be replaced on the next sync. Local deletions propagate to the mirror.

The website shell and `atlas-instrument/` are outside this routine.

## Standard commands

Run from `/Users/danski2017/Desktop/Atlas_Solver_Project`.

Preview without changing mirror content:

```bash
python3 scripts/repo_tools/sync_vault_to_github_mirror.py preview
```

Publish the verified Mac state to GitHub:

```bash
python3 scripts/repo_tools/sync_vault_to_github_mirror.py sync \
  --confirm-mac-sot \
  --report analysis/vault_github_sync/latest_sync.json
```

`--confirm-mac-sot` is deliberately required because an exact sync can delete files from the public mirror when they were deleted locally.

## Enforced sequence

1. Validate the pinned source, checkout, branch, target, and GitHub remote.
2. Require a clean website checkout.
3. Fetch GitHub and fast-forward local `main` only. Divergence stops the run.
4. Build SHA-256 manifests for source and mirror.
5. Block private keys, recognized service-token patterns, sensitive credential filenames, symlinks, and files above 50 MB.
6. Exclude only non-public local metadata declared in configuration: `.DS_Store` and `.claude/settings.local.json`.
7. Report additions, changes, and deletions before publication.
8. Replace only `lab-vault/` from the Mac source and verify the resulting eligible file tree byte-for-byte.
9. Stage and commit only `lab-vault/`.
10. Push `main` and verify the remote branch SHA equals the local commit.

If any gate fails, the sync is not complete. Do not work around a failure by pulling GitHub vault files into the Mac vault.

## Configuration and implementation

- Config: `configs/repo_tools/vault_github_mirror.json`
- Tool: `scripts/repo_tools/sync_vault_to_github_mirror.py`
- Tests: `scripts/repo_tools/tests/test_sync_vault_to_github_mirror.py`
- Public repository: `https://github.com/danski2017/danski2017.github.io`

The routine is manual-by-request. It is not a background daemon or scheduled job. “Sync the vault” means run this one-way publication procedure through verified remote completion.
