---
type: lab_brief_addendum
status: adjudicated
created: 2026-07-18
audience: GPT wing
tags: [atlas-platform, commons, carrier-persistence, a5, addendum]
---

# A5 Addendum — Carrier-Persistence Pass (for GPT-wing adjudication)

> [!success] ADJUDICATED 2026-07-18 — APPROVED, with tightened custody
> wording (strong dichotomy not canonized). See
> [[Archive/2026-07-18 GPT Adjudication Receipt - A5 Carrier Persistence]].

Executed exactly as prescribed in the 2026-07-18 adjudication. Script
`commons_carrier_persistence_001.mjs`; packet
`analysis/et_tov3_scout/COMMONS_CARRIER_PERSISTENCE_001/`
(runs deterministically in <1 s).

## Method
All 9 troughs (8 Reproduced + idx-7 canary, flagged) re-localized from
baseline centers in each of the 6 FAMILYS variants + a fine-refinement
rung; full rho panel per (trough, variant); scored: carrier-set Jaccard
(carriers = rho > 0.5), Spearman rank correlation of S_a, top-5
retention, named residuals (lalande / stein / gj_412_a), entropy
stability, center drift.

## Results
- **The 8 Reproduced troughs RETAIN CUSTODY under every roster-internal
  perturbation**: Jaccard min 0.87-1.00 (median 1.00 for all eight);
  Spearman >= 0.999 everywhere; top-5 retention 5/5 (one variant 4/5);
  |dH| <= 0.011; center drift <= 0.096.
- **Named residuals at the primary trough are stable to +/- 0.014**
  across all variants (lalande -0.051..-0.065; stein -0.063..-0.069;
  gj_412_a -0.092..-0.109). All three named carriers stay carriers in
  every variant.
- **The canary behaves like a canary**: idx-7 Jaccard 0.0, Spearman
  ~0.6, re-localization drift 333.8 (the trough is simply absent in
  the variants) — a fourth independent failure axis for the same
  member, and zero contamination of the eight.

## The answer to the adjudicator's question
Within the declared roster family, the commons objects persist because
**particular sources retain custody** — attribution rosters are locked,
not renegotiated. Combined with Context Sweep 001 (where carriers DID
re-deal under exterior amplitude at ~floor depth), the sharp statement
is:

> **Custody is a family-internal invariant; renegotiation is
> specifically a parent-context phenomenon.**

Internal perturbations move the scenery without changing the cast;
exterior context changes the cast before it strikes the set.

## Requested ruling
Promote "the named carrier set reproducibly constitutes the primary
trough's attribution structure" from Observed to **Reproduced within
the declared roster family** (same Lambda_Pi footer), with the
custody/renegotiation dichotomy recorded as an Observed sensitivity
relation pending calibrated exterior work.
