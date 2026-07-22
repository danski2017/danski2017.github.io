---
type: platform_change_receipt
status: archived
created: 2026-07-22
tags: [atlas-platform, vault, github, sync, receipt]
---

# 2026-07-22 Receipt — Vault GitHub Mirror Sync Routine

## Change

Established the standard one-way vault synchronization routine. The Mac vault is authoritative; GitHub `danski2017.github.io/lab-vault/` is its public mirror. Requested syncs now mean preview, scan, exact scoped copy, byte verification, scoped commit, push, and remote-SHA verification. GitHub vault content never flows back into the Mac source.

Added:

- `scripts/repo_tools/sync_vault_to_github_mirror.py`
- `configs/repo_tools/vault_github_mirror.json`
- nine tests, including an end-to-end temporary Git remote integration test
- [[../10 Vault GitHub Mirror Sync|canonical operations runbook]]

Updated the boot loader, platform home, dashboard, and publication protocol to carry the one-way source-of-truth rule. The website shell and Atlas Instrument remain outside vault-sync scope.

## Safety and verification

- The mirror checkout was fetched and safely fast-forwarded from merged PR #56 to the existing public PR #57 state (`78649e2`); no remote content was changed.
- The tool requires a clean checkout and exact configured repository/branch/remote.
- It accepts only a fast-forward remote update and refuses divergence.
- Pre-publication gates cover secrets, sensitive credential filenames, symlinks, and the 50 MB per-file ceiling.
- Local-only `.DS_Store` and `.claude/settings.local.json` are excluded.
- Source/target manifests use SHA-256 and post-copy byte identity is mandatory.
- Commit staging is restricted to `lab-vault/`; push completion is verified by remote SHA.
- Nine unit/integration tests and Python compilation pass.

## Current preview

The current Mac-to-public delta was previewed only: 355 publication-eligible source files totaling 7,936,025 bytes, with 16 additions, 15 changes, and 0 deletions relative to the PR #57 public baseline. The scan found no blocking publication findings. No sync commit or push was performed in establishing this routine.

## Rollback

Remove the new tool/config/runbook and revert the documentation additions. No GitHub rollback is required because this receipt did not publish a vault sync.
