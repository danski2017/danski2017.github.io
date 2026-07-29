---
type: receipt
status: closed
created: 2026-07-22
tags: [atlas-platform, vault, github, sync, publication, receipt]
---

# Receipt — First Vault GitHub Mirror Publication (2026-07-22)

## Request

Founder: synchronize the public GitHub vault mirror to the Mac vault state.
Direction confirmed as the standing one-way rule: Mac vault is the source of
truth; only the website mirror is updated.

## What ran

`scripts/repo_tools/sync_vault_to_github_mirror.py sync --confirm-mac-sot`
with report `analysis/vault_github_sync/latest_sync.json`.

Source of truth:
`/Users/danski2017/Desktop/Atlas_Solver_Project/Relational_Labs/Relational_Labs/`

Mirror target:
`/Users/danski2017/Desktop/danski2017.github.io/lab-vault/`

## Delta published

- 355 source files, 7,935,993 bytes.
- 16 additions, 15 changes, 0 deletions, 324 unchanged.
- Additions: Temporal Pilot I receipts (ET archive, curvature extension, Psi4
  time ladder); SXS receipts (horizon dynamics bridge, event-centered coherence
  audit); `ATLAS Diagnostic Contract — eigen_gap_full` and its receipt; three
  public-clone receipts; `RL_PUBLIC_CLONE_SKILL`; `RL_PUBLICATION_PROTOCOL`;
  the Strategic Direction sheet; `10 Vault GitHub Mirror Sync`.
- Changes: orientation docs 00-08, Evolution Log, Archive README, Atlas Platform
  Dashboard, Lab Goals and Milestones, Parking Lot and Experiment Queue, Live
  Experiment Dashboard, Next Simulation Queue, `.obsidian/workspace.json`.
- Pre-publication scan returned no findings. No private key, service-token
  pattern, credential filename, symlink, or oversized file was detected.

## Deviation from the runbook — direct push blocked

The runbook's step 10 (`git push` to `main`) FAILED. GitHub returned
`GH013: Repository rule violations` — `main` requires that changes arrive
through a pull request. This is a repository rule, not a tool defect, and the
runbook as written on 2026-07-22 could not complete.

Resolution taken, consistent with the PR #57 precedent:

1. The sync commit `1ea808b` was pushed on branch `vault-sync-2026-07-22`.
2. PR #58 was opened against `main`.
3. PR #58 was merged as `252b4d3` at 2026-07-22T05:48:15Z; branch deleted.
4. Local `main` fast-forwarded to `252b4d3`; local and remote agree.

Nothing about the one-way direction changed. No GitHub vault content entered
the Mac source at any point, including during the failed-push recovery.

## Verification

Post-merge preview reports 0 added, 0 changed, 0 deleted, 355 unchanged, and no
pre-publication findings. The public mirror is byte-for-byte identical to the
Mac vault for all eligible files.

## Owed follow-ups

- `10 Vault GitHub Mirror Sync` updated in this same session to document the
  pull-request path as the real step 10.
- `.obsidian/workspace.json` is local Obsidian UI state (pane layout, window
  geometry), carries no lab content, and will churn on every sync. Recommended
  for the configuration exclusion list beside `.DS_Store` and
  `.claude/settings.local.json`. NOT changed in this session — awaiting founder
  approval, since it alters what the public mirror contains.
- This receipt, its Evolution Log entry, and the runbook correction are
  themselves a new unpublished vault delta requiring a subsequent sync.
