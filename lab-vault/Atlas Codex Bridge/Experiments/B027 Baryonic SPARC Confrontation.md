---
type: experiment_note
status: completed
created: 2026-05-14
program:
  - mesoscale-curvature
  - sparc
  - halogas
  - baryonic-augmentation
claim_level: internal_source_proxy_confrontation
---

# B027 Baryonic SPARC Confrontation

## Purpose

B027 uses no new downloaded data. It asks whether the HI-only transfer-function story from B026 survives when local SPARC stellar disk and bulge surface-brightness rows are added as declared baryonic source proxies.

This is not a dark-matter test. It is a source-proxy confrontation between an HI-only ledger and a first total-baryon proxy ledger.

## Source Package

- Experiment package: `codex_context/experiments/B027_baryonic_sparc_confrontation`
- Script: `codex_context/scripts/b027_baryonic_sparc_confrontation.py`
- Comparison table: `derived/B027_HI_VS_TOTAL_BARYON_COMPARISON.csv`
- Summary: `derived/B027_SUMMARY.json`

## Inputs

- HI source-proxy scenes from B020, B022, B024, and B025.
- Local SPARC `MassModels_Lelli2016c.mrt` rows.
- Declared mass-to-light choices:
  - disk `M/L_3.6 = 0.5`
  - bulge `M/L_3.6 = 0.7`

SPARC surface-brightness rows were converted into annular stellar disk/bulge source proxies using annular area and declared `M/L`.

## HI-Only vs Total-Baryon Ledger

| Galaxy | HI E/vc2 | Total E/vc2 | Total p90 vc2 | Total p90 E | Stellar/HI Proxy |
|---|---:|---:|---:|---:|---:|
| NGC2403 | 1.3686 | 12.1103 | 0.02730 | 0.3306 | 1.5719 |
| NGC1003 | 4.9015 | 11.7608 | 0.02889 | 0.3398 | 0.5580 |
| NGC0891 | 4.5946 | 14.4942 | 0.03703 | 0.5367 | 15.0641 |
| NGC5055 | 1.5143 | 5.8782 | 0.11825 | 0.6951 | 6.3643 |

## Read

Adding declared stellar disk/bulge annular source proxies changes the transfer ledger substantially.

The strongest change is that the sector-annular scalar proxy becomes very tightly preserved in the total-baryon scenes, while electric-Weyl/eigenframe deltas remain materially larger. This increases the `E/vc2` ratio across all four targets, but the mechanism is not a dark-matter signal. It is a transfer-function result under a declared baryonic source-proxy construction.

B027 therefore strengthens one boundary and one opportunity:

- Boundary: do not collapse HI-only and total-baryon language.
- Opportunity: the baryonic source ledger may make the tensor/scalar transfer-function paper sharper than the HI-only version.

## Claim Boundary

- No dark-matter claim.
- No MOND test.
- Not a full photometric decomposition.
- Stellar components are SPARC surface-brightness annular proxies.
- HI-only and total-baryon ledgers must remain separate.

## Next Gate

The next useful run is not more data. It is a nuisance and model-stability pass on B027:

- vary disk and bulge `M/L`,
- vary annular proxy resolution,
- compare sector-annular against observation-shaped branches from B015,
- keep NGC0891 edge-on geometry flagged.
