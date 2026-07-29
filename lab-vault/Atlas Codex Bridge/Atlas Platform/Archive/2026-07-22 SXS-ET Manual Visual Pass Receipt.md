---
type: platform_change_receipt
status: archived
created: 2026-07-22
tags: [atlas-platform, temporal-nr, sxs, qa, visual-pass, provenance, receipt]
---

# 2026-07-22 Receipt — SXS<->ET Manual Visual Pass Completed

## Mode

VERIFICATION ONLY. No source file, viewer file, dataset, manifest, generator,
script, claim, or doctrine was modified. No NR evolution, solver run, or heavy
local compute occurred. The only writes are this receipt, the Evolution Log
entry, and the goals-checkbox closure.

## Item closed

Work Order 2 (SXS Horizon Dynamics Bridge, 2026-07-21) left one outstanding
follow-up: "Complete the documented manual SXS<->ET browser visual pass." It was
deferred at the time because the in-app browser runtime was unavailable
in-session. That runtime was available on 2026-07-22 and the pass was performed.

## Environment

- Viewer served with `scripts/et_tov3_scout/atlas_viewer.sh start` on
  `http://127.0.0.1:8792/` (Python http.server bound to 127.0.0.1, PID 49675).
- Application under test: `analysis/et_tov3_scout/pinch_lab_viewer/index.html`,
  SHA-256 `1b59e1e9247b2a00965e0e15dab229f7b88997c15ad3b0867168af4ab95beb3e`
  (unchanged before and after the pass).
- Both temporal payloads present and served 200:
  `datasets/ATLAS_TEMPORAL_PILOT_I_ET_ARCHIVE_001/temporal_scene.json`,
  `datasets/SXS_HORIZON_DYNAMICS_001/temporal_scene.json`.

## Result: PASS

### Substrate separation holds (the central question)

The two Temporal NR substrates present visibly different instruments, and the
trajectory series is never dressed as a spatial field:

- **ET** (`FULL_SPATIAL_SLICE_ARCHIVE`): renders a 3D probe volume with two
  puncture markers. Passport reads `ML_BSSN::phi · BSSN_CONFORMAL_FIELD`, chart
  `Thornburg04 map 0 · rl=3 · +z bitant`, registration `IDW shared-coordinate ·
  max d=0.6841`, source DOI `10.5281/zenodo.155394`, 5,000 probes, Zenodo v1 ·
  CC BY 4.0.
- **SXS** (`HORIZON_TRAJECTORY_SERIES`): renders A/B inspiral trajectories and
  the C track. Passport reads substrate `A/B/C apparent-horizon history · Lev6`,
  chart `inertial coordinate centers · coordinate-dependent`, clock
  `horizons t/M; strain (t_corr-r*)/M · shift 0`, source
  `https://doi.org/10.26138/SXS:BBH:0305v3.0`, 11,934 epochs, SXS v3.0 ·
  CC BY 4.0.
- The SXS substrate exposes NO field selector, NO refinement-level selector, and
  NO 3D-region selector. Those controls are absent rather than disabled-and-
  misleading, which is the correct realization of the non-impersonation rule.
- Lane header states the doctrine on screen: "a trajectory series is never
  represented as a spatial field."

### Absence is displayed, not hidden

- ET field selector lists `E_ij · unavailable in published subset` and
  `constraints · unavailable in published subset` as visible, non-selectable
  entries.
- SXS availability block lists `unavailable: local fields · E_ij/B_ij ·
  constraints · proper separation · horizon shapes · Psi4 pilot`.

### Psi4 time ladder present

The ET TIME/COMPARISON selector offers all three common full-3D rungs
(`t=0`, `t=449.355956`, `t=898.711912`), both adjacent residuals (`t1-t0`,
`t2-t1`), and two cross-witness residual pairs. Radiative-witness selector
offers multipolar Psi4 `(2,±2)`, `(2,±1)`, `(2,0)` at seven extraction radii
(100-500), preserving the spatial-grid versus spin-weighted-multipole
distinction.

### In-instrument numbers reproduce the receipts exactly

| Quantity | In-instrument | Source receipt |
|---|---|---|
| Common horizon `T_CH` | `3685.496268 M` | `3685.496267868691 M` |
| Strain (2,2) peak | `3692.646900 M` | — |
| Peak minus common | `7.150632 M` | `+7.150632 M` |
| A / B / C samples | `7,376 / 7,376 / 5,464` | — |
| Alignment | `no hidden shift` | shift 0 |

### Independent payload check — coexistence window

Read directly from `SXS_HORIZON_DYNAMICS_001/temporal_scene.json`:

- A end `3687.500000 M`, B end `3687.500000 M`, C start `3685.496268 M`
  (identical to `metadata.common_horizon_time`).
- **A/B persist `2.003732 M` past C onset** — reproducing the audit receipt's
  `2.003732 M` exactly.

This independently confirms the endpoint-sensitivity reasoning behind the
`C_STOP_REFRAME` decision: the A/B overlap with C is about two `M` wide, so
apparent A/B orbital/mass/spin concentration near the event is an endpoint
artifact, not a signal.

### Timeline behavior

Driving the horizon timeline to its final epoch (index 11,933) advances
coordinate time to `4456.868781 M` and the header correctly reports
`common horizon present`. Substrate round-trip SXS -> ET -> SXS restores each
lane's full control set and passport without residue.

### Regression and responsiveness

- All five lanes exercised: Atlas Native, Imported Tools, Recovery Lab,
  Temporal NR, BL Foam. All render non-blank WebGL and load their payloads.
- BL Foam passport retains the Lambda_Pi footer ("parent Pi LSN roster complete
  to declared box; beyond-box structure undeclared (Lambda_Pi uncalibrated)").
- Imported Tools remains labeled read-only external advisory, not Atlas native
  ledgers.
- Console errors: **0**. Network failures: **0** (20/20 requests 200 OK).
- Desktop 1280x720 and mobile 375x812 both reflow without horizontal overflow;
  the combined source-context timeline chart and its common-horizon marker
  remain legible at mobile width.

## Minor cosmetic observation (not a defect gate)

In the Recovery Lab lane at 800x450 the passport ribbon text overlaps the scene
overlay chips, and a probe-density label clips at the left viewport edge. This is
cosmetic only, affects no numerical readout or claim wording, is confined to a
narrow intermediate viewport, and is recorded here rather than fixed, since this
pass was scoped as verification and changing the viewer would have exceeded it.

## Standing negative preserved

Nothing in this pass reopens `ATLAS_SXS_EVENT_CENTERED_COHERENCE_001`. The
coexistence, strain-ordering, and settling ledgers are the retained robust facts;
the point-centered multichannel coherence signature remains CLOSED NEGATIVE under
`C_STOP_REFRAME`, and no Ext-CCE rescue is implied or authorized by this
verification.

## Integrity

- Viewer SHA-256 unchanged: `1b59e1e9…b95beb3e`.
- Files modified in the viewer tree: 0. Datasets modified: 0. Deletions: 0.
- Website and public clone: untouched.
