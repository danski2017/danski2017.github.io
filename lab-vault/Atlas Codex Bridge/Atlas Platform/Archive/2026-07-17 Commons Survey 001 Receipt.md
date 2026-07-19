---
type: platform_change_receipt
status: archived
created: 2026-07-17
tags: [atlas-platform, commons, gfro-emission, trough-census, receipt]
---

# 2026-07-17 Receipt — Commons Survey 001 (first commons-native survey)

## Change
- New script `scripts/et_tov3_scout/commons_survey_001.mjs` (additive; no
  viewer edits, no dataset overwrites). Evidence packet at
  `analysis/et_tov3_scout/COMMONS_SURVEY_001/commons_survey_001_20260717.json`.
- Implements the dual-primitive doctrine (founder, 2026-07-16): a DECLARED
  volume-filling lattice (48^3 over the roster bounding box + 2.0 pad,
  dx ~ 0.485) replaces source-radial rays for commons objects. Panel
  conventions identical to the baked network channels (S_a = ||Delta_a E||_F
  over DEN-A single-ablation re-solves; margin = (S1-S2)/(S1+S2); attribution
  entropy normalized by ln n; TF witness; delta-chart norm).

## Part 1 — Trough census
- 37 strict 26-neighbor lattice minima of full-scene ||E||_F, refined by
  pattern search and deduped to **36 troughs**; **9 are disputed commons
  candidates (entropy >= 0.75)**.
- The lalande adjudication trough is RECOVERED by the blind census: nearest
  trough at (-1.356, 1.662, 8.669), 0.54 from the interrogated point;
  ||E|| = 4.4e-16 (deepest trough in the census), entropy 0.819, margin
  0.205, dominant source stein_2051_b, **13 sources at rho > 0.5**.
- Eight further disputed troughs cataloged (ross_154 basin x2, lacaille_9352/
  luyten region with 15 sources above rho 0.5, wolf_424_ab, stein_2051_b far
  side, van_maanen/ez_aqr, epsilon_ind/gj_1061, lalande near-side).

## Part 2 — Recurrence test (commons prediction)
- Prediction from the 2026-07-16 adjudication: neighboring sources' parity
  sets should carry components in the lalande trough.
- Ball test (r = 1.5, ~257 samples) + Newton zero landing:
  **lalande_21185 CARRIES, stein_2051_b CARRIES (75/182 sign split — the
  largest share), gj_412_a CARRIES**; controls van_maanen_star and tau_ceti
  carry NO component (Psi ~ -0.74 throughout). Psi at the trough center is
  -0.0709 (lalande) vs -0.0712 (stein): many faint signatures at
  simultaneous near-parity — the commons signature itself.
- **The commons reading's prediction is CONFIRMED at Observed rung.**

## Part 3 — GFRO emission on a declared commons residual
- Residual: normalized attribution entropy level set H(x) = 0.75 (declared),
  crawled by continuation from a trough-anchored seed, radius cap 3.0.
- 640 surface points, uncapped; resubstitution |G| median 6e-4-ish (see
  packet); certified against a dense local lattice truth (26^3, 895 edge
  crossings): **cover median 0.069, p95 0.102, max 0.125 < 1.5h = 0.30 —
  CERTIFIED.** The census trough inside the cap sits on the high-entropy
  side of the surface, as required.
- Emission needed no source to march from — consistent with the doctrine
  that it may be the native first-class method in the commons. It remains a
  setting, never the default (directive 9).

## Validation
- `node --check` pass; run completes in < 1 s on the Mac mini (pointwise
  closed-form kernels only — compute-safety compliant).
- Independent recomputation of Psi at the trough center (separate one-off
  script) reproduced -0.0709 / -0.0712 / -0.1123 for lalande/stein/gj_412_a,
  ruling out a shared-state bug behind the near-identical values.
- Part 3 first ran with radius cap 6.0 and hit the 4,000-pt budget
  (cover max 3.85, capacity failure not accuracy failure); re-scoped to
  cap 3.0 / 15,000 budget and certified cleanly. Both runs recorded here.

## Boundary
- Claim ceiling: **Observed**. Persistence sweeps owed before promotion:
  lattice resolution (48 -> 64/96), refinement tolerance, roster
  perturbation (reuse FAMILYS_PERTURB grammar), and H-level sensitivity
  (0.70/0.75/0.80). Initial-slice diagnostic of the declared roster family;
  not dynamics. Dominance cells are not ownership parcels. Vocabulary
  candidate, not decision.

## Rollback
Delete `scripts/et_tov3_scout/commons_survey_001.mjs` and
`analysis/et_tov3_scout/COMMONS_SURVEY_001/` (founder permission required
for deletions); no other file was touched.
