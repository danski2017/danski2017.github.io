---
type: platform_change_receipt
status: archived
created: 2026-07-22
tags: [atlas-platform, visualization, ablation, plates, tour, provenance, receipt]
---

# 2026-07-22 Receipt — Ablation Plates 001 + Instrument Tour 001

## Mode

DERIVED VISUALISATION, INTERNAL / EXPLORATORY. Founder-directed experiment in
presentation visuals. No solver run, no ET evolution, no re-bake, no viewer edit,
no dataset mutation, no claim promotion or demotion.

## Publication status

**INTERNAL / EXPLORATORY — NOT FOR PUBLICATION** (founder framing, 2026-07-22).

Artifacts are written to `analysis/et_tov3_scout/ABLATION_PLATES_001/`, which sits
in the repo and **outside the Obsidian vault**, so they are not in the vault
mirror's publication path. Every plate carries the not-for-publication banner in
its own header. This receipt is in the vault (the ledger remembers), but the
images and video deliberately are not.

## Deliverables

`analysis/et_tov3_scout/ABLATION_PLATES_001/`

| File | Content |
|---|---|
| `plate_I_loudest_ablation.png` | Family S, `- pair I (ember+ash)`: full / ablated / relative delta |
| `plate_II_five_conventions.png` | One ablation under all five declared witness-denominator conventions |
| `plate_III_identity_vs_amplitude.png` | Gaia LSN-66, `- van_maanen_star`: amplitude vs eigenframe vs allegiance |
| `plate_IV_gated_eigenframe.png` | `eigen_gap_full` as admissibility channel + gate-cost sweep |
| `plate_V_witness_bench.png` | Magnetic Weyl, magnetic fraction, super-Poynting, momentum residual, commons entropy, webbing + troughs |
| `plates_report.json` | Full ablation ranking and every number printed on the plates |
| `atlas_instrument_tour.mp4` / `.webm` | 143 s scripted screen recording of the live instrument |
| `tour_beats.json` | Beat list + captured console errors (0) |

Generators (new, committed to the repo):
`scripts/et_tov3_scout/render_ablation_plates_001.py`,
`scripts/et_tov3_scout/record_instrument_tour_001.py`.

## Method

Plates read the same frozen payloads the Atlas Platform serves
(`BL_FOAM_BAKED_001`, `MAGNETIC_WEYL_002`, `COMMONS_ATLAS_001`) — no re-derivation.

Scene selection was by **declared numeric criterion, not by eye**: all ablation
configs were ranked by the p99 of relative `|dFroTF|` against FULL SCENE. The
ranking is preserved in `plates_report.json`. Family S winner `- pair I
(ember+ash)` (p99 0.9983); strongest single-source Gaia removal
`- van_maanen_star` (p99 0.8924).

The tour drives the LIVE viewer at `127.0.0.1:8792` with Playwright and records
the real UI. The caption bar and synthetic cursor are injected into the page at
runtime only; no viewer file was touched (`index.html` SHA-256 unchanged at
`1b59e1e9…b95beb3e`, viewer tree byte-untouched).

## Environment change

`playwright` 1.61.0 (+ `greenlet`, `pyee`) and its Chromium were installed into
the existing lab venv at `/.venv`, per founder selection. Additive and contained;
nothing outside the venv changed. The tour harness is reusable as a standing
demo/QA capture path.

## Three corrections made during the work — the substantive part of this receipt

These were caught by checking generators and distributions before rendering. Each
would have produced a handsome and wrong picture.

### 1. The allegiance channel is not a quantity to difference

`bake_bl_foam.mjs` L282-288 defines

    allegiance = <dE, E_full>^2 / (||dE||^2 ||E_full||^2),   dE = E_full - E_ablated

a proper tensor inner product (off-diagonals weighted x2). It is **cos^2 of the
angle between the removed source's contribution and the total field**, and the
full-scene config is **hard-set to 1 by convention** (`ci===0?1:...`).

A first pass plotted `allegiance_ablated - allegiance_full`, which is structurally
guaranteed non-positive and rendered as a uniformly blue panel carrying no
information. Corrected to report the ablated value directly, never differenced,
with the definition printed on the plate.

Restated metric: for `- van_maanen_star` the removed contribution is more
tensorially ORTHOGONAL than aligned to the total field on **85.4%** of lattice
points (median allegiance 0.1477) — while median relative `|dFroTF|` is 5.9e-4.

### 2. `eigen_gap_full` is bounded above by 0.5, not 1.0

For a trace-free symmetric 3x3, `(|l0|-|l1|)/|l0|` cannot exceed **0.5**, attained
at the axisymmetric spectrum `lam ~ (2,-1,-1)`. Measured maxima agree (0.4990
Family S, 0.4999 Gaia); Family S median is 0.438 — near the ceiling.

A first pass scaled the colour map over [0,1], which renders a near-ceiling field
as a weak one. Corrected to [0, 0.5] with the bound stated.

The plate's original rhetoric was also wrong: at the declared 0.02 floor the gate
excludes only **0.83%** of the lattice (8.29% at a strict 0.20 floor), so "the
ungated picture would overclaim" was unsupported. Rewritten to the honest
finding — in this substrate the eigenframe witness is admissible almost
everywhere — plus a fourth panel showing the gate's cost at any floor.

### 3. The H>=0.85 backbone is not drawable from `COMMONS_ATLAS_001/webbing.f32`

Entropy in that payload tops out at **0.8455**, so the `>=0.85` set is empty. A
first pass drew an "H>=0.85 backbone" panel that was structurally blank.

The backbone was established on the 64^3 disputed-region lattice in
COMMONS_SURVEY_001 — a different object from the webbing subset. The panel now
shows webbing bands and the 9-trough roster, which this payload does support,
with the substrate limit stated.

**No instrument defect is implied.** The viewer's own commons note (index.html
L543) is precise: it renders the certified **H = 0.75** entropy surface and troughs
at entropy >= 0.75, and separately *cites* the 2026-07-18 H>=0.85 adjudication.
The conflation was introduced by the plate script and corrected there.

Also fixed: trough records live at `islands.troughs` keyed `x`; a first parser
looked for a non-existent `islands` key and silently drew zero troughs. Trough
**idx-7 at (0.809, 1.481, -7.843)** confirmed against the register and ringed as
the permanent canary.

## Claim discipline carried on every artifact

Substrate / witness / norm / denominator passports; analytic BL-conformal
substrates declared NOT ET-fused GR; frozen arrangements declared not time
evolution; eigenvectors declared interpretive and gated; surface integration
UNAUTHORIZED; commons results reported as Reproduced **within the declared roster
family** with the 0/20 percolation null never stated as a universal probability;
idx-7 canary preserved; the SXS event-centered audit's `C_STOP_REFRAME` negative
narrated in the tour; `Lambda_Pi` uncalibrated footer on every plate and the
closing card.

## Verification

- Tour: 20 beats, **0 console errors**, 143 s, 1600x900.
- WebGL confirmed genuinely rendering under SwiftShader by frame sampling — the
  recording is not a movie of blank canvases.
- Viewer `index.html` SHA-256 unchanged; `find` over the viewer tree shows no
  modified files.
- Datasets, manifests, generators of record, website, and public clone unchanged.

## Not done

- No vault sync; no publication of any kind.
- The plates were not promoted to figure-grade; they remain exploratory.
- Recovery Lab's cosmetic passport/overlay overlap (noted 2026-07-22) is still
  unfixed and is visible briefly in the tour.
