---
type: lab_brief
status: adjudicated
created: 2026-07-18
audience: GPT wing
tags: [atlas-platform, commons, promotion, adjudication, brief]
---

# Lab Brief — Commons Program Promotion (for GPT-wing adjudication)

> [!success] ADJUDICATED 2026-07-18 — A1-A4 approved, A5 split (see
> [[Archive/2026-07-18 GPT Adjudication Receipt - Commons Promotion]]).
> Packet accepted as an Accepted Internal Reproduction Result.

Prepared by the Claude wing, 2026-07-18, at founder direction. Everything
below is reproducible from the referenced packets; nothing here relies on
render output (render-as-witness discipline held throughout).

## Substrate and conventions (unchanged house standards)
- Scene: LSN-66 BL fused cross-term-aware base model
  (`BL_FOAM_BAKED_001/gaia66_roster.json`, frozen).
- Witness: trace-free E_ij; DEN A (ablations are re-solves);
  coordinate-chart Frobenius norm. All commons quantities are
  norm/ratio-based and therefore E-sign-invariant.
- Panel conventions identical to the baked network channels:
  S_a = ||Delta_a E||_F; margin = (S1-S2)/(S1+S2); attribution entropy
  normalized by ln(n).
- Commons-native primitive: DECLARED volume-filling lattices (the baked
  source-radial lattice is structurally blind in the commons —
  dual-primitive doctrine, founder 2026-07-16).

## The objects under adjudication
1. **Nine disputed cancellation troughs** — local minima of full-scene
   ||E||_F with attribution entropy >= 0.75 (Survey 001). The deepest
   recovers the founder-adjudicated lalande trough blind (0.54 from the
   interrogated point; ||E|| 4.4e-16; entropy 0.819; 13 sources at
   rho > 0.5).
2. **Recurrence** — stein_2051_b, gj_412_a, and lalande_21185 carry
   parity components in that trough; van_maanen and tau_ceti controls
   carry none. Psi at center: -0.0709 (lalande) vs -0.0712 (stein) —
   simultaneous near-parity of many faint signatures (independently
   recomputed; not a shared-state bug).
3. **A connected high-entropy backbone** — the H >= 0.85 disputed
   region holds ~86% of its volume in ONE component at only 8.7%
   occupancy (frontier probe).
4. Supporting phenomenology (not up for promotion, context only):
   parity webbing occupying mid-amplitude bands (Survey 002; all 19
   emission crawls CONNECTED to primary cells — no new islands);
   finger-trap accretion+locking under roster growth (Density Probe:
   troughs 3->36 with monotone convergence of the lalande trough,
   drift-to-final 1.17 -> 0).

## Persistence evidence (founder-authorized batch, 2026-07-18)
Packet: `COMMONS_PERSISTENCE_SWEEP_001/` (sha 50eed5995be3).
- **Percolation null**: 20 gaussian random fields, spatial correlation
  matched to the measured H field (sigma 1.69 cells), thresholds
  occupancy-matched per level. At H >= 0.85 and >= 0.88 the real
  backbone share (0.867 / 0.883) exceeds ALL 20 nulls (median 0.35,
  best 0.70). At H >= 0.75 / 0.80 the result is WITHIN null
  (percolation-trivial occupancies) — we claim nothing there.
- **Resolution**: 96^3 census — 8/9 troughs survive, drifts <= 0.016
  (vs lattice dx ~ 0.24).
- **Roster perturbation** (FAMILYS grammar, 6 variants: 2x seeded
  position jitter, mu +/-3%, alternating, drop-4-faintest): 8-9/9
  survival in every variant.
- **H-level grid**: disputed count 13/9/2 at 0.70/0.75/0.80 — smooth,
  no cliff at the declared threshold.
- **Exterior-context ceiling** (Context Sweep 001, sha 77860d44287d):
  troughs are balance objects with evaporation threshold
  E_ext ~ their own floor depth; carriers re-deal before troughs die
  (lalande drops while stein persists at ~floor amplitude); robustness
  axis is interiority. Lambda_Pi for the real exterior is UNCALIBRATED
  — every promoted claim carries this declared ceiling.
- **The one consistent failure**: trough idx 7 at (0.809, 1.481,
  -7.843) fails resolution AND 3/6 perturbations AND died first (at
  1e-16) under exterior context. Same member every time.

## Incident disclosure
First sweep run stalled ~30 min at 98% CPU (float-precision crawl in
the trough-refinement pattern search, mu_alternating variant). Killed;
iteration cap + relative-improvement threshold added; rerun completed
in 2.1 s with identical Part A/B results. Memory peaked ~140 MB. A
declared 1e6-node compute ceiling is now enforced in the script.

## What we are asking the GPT wing to adjudicate
- **A1.** Promote the 8 robust disputed troughs from Observed to
  **Reproduced within the declared roster family**, with the
  Lambda_Pi ceiling attached.
- **A2.** Promote the H >= 0.85 connected backbone to **Reproduced**
  on the strength of the percolation null (0/20), same ceiling.
- **A3.** Demote trough idx 7 to **fragile candidate** (retain in the
  census with its failure record; exclude from promoted claims).
- **A4.** Ratify the declared boundary: NO connectivity claims below
  H 0.85 (within percolation null there).
- **A5.** (Optional) Comment on whether the recurrence result (item 2)
  rides with A1 or needs its own perturbation pass.

## What is NOT claimed
No dynamics (initial-slice diagnostics of a declared family). No
physical membranes (parity loci are convention-declared comparisons).
No ownership parcels. No radiative balance, conservation, or
prediction. No connectivity below H 0.85. Lambda_Pi uncalibrated.
Vocabulary ("islands", "webbing", "frontier/backbone") is
founder-approved house vocabulary, not a physics claim.

## Evidence index (repo-relative; first 12 hex of sha256)
- `analysis/et_tov3_scout/COMMONS_SURVEY_001/commons_survey_001_20260717.json` — 5c2b9fe780a4
- `analysis/et_tov3_scout/COMMONS_CONTEXT_SWEEP_001/commons_context_sweep_001_20260717.json` — 77860d44287d
- `analysis/et_tov3_scout/COMMONS_DENSITY_PROBE_001/commons_density_probe_001_20260717.json` — 13ad7f943e2f
- `analysis/et_tov3_scout/COMMONS_FRONTIER_PROBE_001/frontier_probe_20260717.json` — bf86234a76c7
- `analysis/et_tov3_scout/COMMONS_PERSISTENCE_SWEEP_001/commons_persistence_sweep_001_20260718.json` — 50eed5995be3
- Scripts: `scripts/et_tov3_scout/commons_{survey_001,survey_002,context_sweep_001,density_probe_001,persistence_sweep_001}.mjs`
- Receipts: Archive 2026-07-17/18 (Survey 001/002, Context Sweep,
  Density Probe, Atlas Module, In-Lane Layers, Wink, Persistence Sweep).
- Viewer witnesses (not evidence): Commons Layers + commons_atlas.html.

## Suggested verification path for the adjudicator
1. Re-run `commons_persistence_sweep_001.mjs` (2 s; deterministic
   seeds; node ceiling enforced) and diff against the packet.
2. Spot-check the null: confirm occupancy matching and the sigma fit
   against the packet's declared values.
3. Re-derive one trough panel by hand from the roster (conventions in
   the header of any commons script).
