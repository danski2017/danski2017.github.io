---
type: platform_change_receipt
status: archived
created: 2026-07-19
tags: [atlas-platform, publication, github-pages, receipt]
---

# 2026-07-19 Receipt — Vault + Instrument Published to GitHub Pages

## Change (founder-directed publication)
The Obsidian vault and the complete ATLAS Field Metric Viewer cloned to
the public site (danski2017/danski2017.github.io) via merged PR #57.
New public paths (nothing existing touched except a scoped _config.yml
append):
- **https://danski2017.github.io/lab/** — landing page.
- **/lab-vault/** — full vault as browsable pages (8.2 MB; Liquid
  disabled for the path so Obsidian placeholders cannot break the
  Jekyll build; wikilinks render as plain text; claim-ladder labels
  and Lambda_Pi ceilings ship with the content).
- **/atlas-instrument/** — complete viewer + frozen payloads (339 MB;
  fully client-side; includes commons_atlas.html and
  lalande_island_showcase.html).

## Pre-publication checks
- Size: no file > 50 MB (100 MB cap clear); site total within Pages
  limits.
- Secrets/PII scan: clean (two benign false positives inspected and
  recorded in the PR).
- Liquid-hazard scan: one template placeholder; neutralized via
  render_with_liquid: false scope.

## Verification (live)
- Pages build: status "built", no error.
- HTTP 200 on: /lab/, instrument index, commons_atlas.html, commons +
  roster payload manifests, Mission Statement, Findings Digest.
- Functional: Commons Atlas rendered its full payload live from the
  public origin with zero console errors.

## Notes
- The site's existing navigation was NOT modified; /lab/ is reachable
  by URL. Adding it to header_pages/index is Gemini-wing (website)
  territory, flagged as a follow-up.
- The public clone is a SNAPSHOT of 2026-07-19. It does not auto-sync;
  future material vault/instrument changes need a re-publish step
  (owed: decide cadence or automation — Parking Lot).

## Rollback
Revert merge commit of PR #57 on danski2017.github.io (single revert
restores the prior site exactly).
