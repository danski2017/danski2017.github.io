---
type: platform_change_receipt
status: archived
created: 2026-07-17
tags: [atlas-platform, commons, layer-stack, viewer, receipt]
---

# 2026-07-17 Receipt — Commons Layers Wired Into the BL Layer Stack

## Change
The Commons Module block in `index.html` was upgraded from a link-only
annex to three first-class Layer Stack members rendered inside the one
BL world (`blWorld`), following the existing network-layer grammar:
- **parity webbing** — banded near-parity nodes from the frozen
  COMMONS_ATLAS_001 payload, colored by ||E|| decile (VIR lut), with a
  strict-rung filter checkbox (nearC@|Psi|<0.2 >= 3);
- **trough islands** — the 9 disputed troughs as octahedron markers
  (lalande trough red);
- **commons frontier patch** — the H=0.75 surface points (labeled a
  local patch; see Frontier Probe receipt).
Implementation: `commonsLayersUpdate(sceneKey)` + `clearCom()` +
lazy `comData()` loader; called alongside eigen/network updates;
onchange wiring; included in the all-layers-off sweep; passport stack
declares commons-webbing / commons-islands / commons-frontier. Layers
render ONLY on the gaia66 base model (payload provenance); passport
entries are gated on the same condition so the declared stack always
matches what is on screen. Edge case handled: empty point sets cannot
steal a network layer object from the shared cloud builder.
Backup: `backups/atlas_platform/index_pre_commons_layers_20260717.html`.

## Validation (in-browser, HTTP-served)
- gaia66 + all three layers: renders in the one world with the foam;
  passport reads "stack foam + commons-webbing + commons-islands +
  commons-frontier"; zero console errors.
- Scene switch to Family S: commons geometry clears AND passport drops
  the commons entries ("stack foam") — declared stack matches screen.
- all-layers-off: unchecks the commons boxes, geometry clears, passport
  reverts. Zero console errors throughout.

## Boundary
Render is a witness; payload provenance and claim ceilings unchanged
(Observed; candidate vocabulary). Owed still: wink-grammar A/B between
commons layers and network layers; walked-path connectivity; resolution
sweep; percolation null for the frontier backbone.

## Rollback
`cp backups/atlas_platform/index_pre_commons_layers_20260717.html analysis/et_tov3_scout/pinch_lab_viewer/index.html`
