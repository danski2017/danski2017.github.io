---
type: experiment_note
status: completed
created: 2026-05-14
program:
  - mesoscale-curvature
  - sparc
  - baryonic-augmentation
  - stability-hardening
claim_level: internal_stability_hardening
---

# B028 Baryonic Stability Hardening

## Purpose

B028 tests whether the B027 baryonic transfer ledger survives local modeling choices or collapses as a first-pass annular proxy artifact.

No new data was downloaded. This run uses existing HI source-proxy scenes and local SPARC mass-model rows only.

## Source Package

- Experiment package: `codex_context/experiments/B028_baryonic_stability_hardening`
- Script: `codex_context/scripts/b028_baryonic_stability_hardening.py`
- Variant table: `derived/B028_VARIANT_ROWS.csv`
- Galaxy summary: `derived/B028_GALAXY_STABILITY_SUMMARY.csv`
- Summary: `derived/B028_SUMMARY.json`

## Variant Grid

Each galaxy was tested across `13` local variants:

- disk `M/L_3.6`: `0.35`, `0.50`, `0.65`
- bulge `M/L_3.6`: `0.50`, `0.70`, `0.90`
- stellar azimuthal proxy counts: `12`, `24`, `36`
- sector radial bins: `20`, `28`, `36`

Total rows: `52`.

## Stability Summary

| Galaxy | E/vc2 Min | E/vc2 Median | E/vc2 Max | p90 vc2 Median | p90 E Median |
|---|---:|---:|---:|---:|---:|
| NGC2403 | 4.4330 | 11.7194 | 13.0351 | 0.03346 | 0.3921 |
| NGC1003 | 6.1316 | 11.6111 | 11.6717 | 0.03087 | 0.3584 |
| NGC0891 | 8.5693 | 13.2313 | 13.8016 | 0.04305 | 0.5754 |
| NGC5055 | 3.5379 | 5.6241 | 6.2967 | 0.13102 | 0.7339 |

Global ratio floor: `3.5379`.

Fraction of rows above `E/vc2 = 1`: `1.0`.

Fraction of rows above `E/vc2 = 3`: `1.0`.

## Read

B028 hardens B027. Across declared `M/L` and resolution variants, the total-baryon sector transfer ratio remains above unity in every tested row.

That does not make it a dark-matter result. It does make the transfer-function claim harder to dismiss as one fragile parameter choice. The effect size varies by galaxy and model choice, so the right language is:

> The baryonic source-proxy ledger supports a robust but model-sensitive separation between scalar rotation-like preservation and electric-Weyl/eigenframe preservation under sector-style coarse transfer.

## Claim Boundary

- No dark-matter claim.
- No MOND test.
- Local stability hardening only.
- Stellar components remain SPARC surface-brightness annular proxies.
- Not a full survey result.

## Next Gate

The next useful move is observation-shaped hardening:

- beam/noise/inclination sweeps,
- explicit comparison to B015 observation-shaped branches,
- keep NGC0891 edge-on geometry flagged,
- decide whether the result is ready for internal paper drafting.
