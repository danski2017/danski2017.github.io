---
type: experiment_note
status: completed
created: 2026-05-14
lane: galaxy-averaging
topics:
  - anti-bias
  - HALOGAS
  - SPARC
  - HI-cube
  - synthesis
---

# B023 Two-Galaxy Real-Data Witness Synthesis

Codex consolidated the first two real-data HI witnesses and made the selection
bias explicit.

Experiment package:

`/Users/danski2017/Desktop/Atlas_Solver_Project/codex_context/experiments/B023_two_galaxy_real_data_witness_synthesis`

Primary outputs:

- `derived/B023_TWO_GALAXY_WITNESS_TABLE.csv`
- `derived/B023_HALOGAS_CONTROL_CANDIDATES.csv`
- `derived/B023_SUMMARY.json`
- `reports/B023_REPORT.txt`

## Comparison

NGC2403:

- SPARC median discrepancy proxy: `2.277`
- best branch: `hi_sector_annular`
- p90 `vc2`: `0.3238`
- p90 electric-Weyl Frobenius delta: `0.4431`
- p90 `E/vc2`: `1.3686`

NGC1003:

- SPARC median discrepancy proxy: `5.023`
- best branch: `hi_sector_annular`
- p90 `vc2`: `0.03463`
- p90 electric-Weyl Frobenius delta: `0.16974`
- p90 `E/vc2`: `4.9015`

## Bias Audit

NGC1003 was intentionally selected as a stronger SPARC discrepancy target after
NGC2403. That is scientifically useful, but it is also selection pressure.

The next honest run should be a low-discrepancy control, not another exciting
high-ratio target.

Recommended control:

- NGC0891
- SPARC quality flag: `1`
- median discrepancy proxy: `1.3766`
- HR cube size: `752 MB`

Additional reasonable controls:

- NGC5055: median discrepancy proxy `1.6335`, HR cube `676 MB`
- NGC5585: median discrepancy proxy `2.7316`, HR cube `264 MB`

## Current Public-Safe Sentence

In two HALOGAS/SPARC HI-only source-proxy witnesses, scalar rotation-like
preservation and electric-Weyl/eigenframe preservation separate under declared
coarse branches.

## Do Not Claim

- dark-matter explanation
- total-baryon galaxy result
- survey-level correlation
- new physics
- public result before low-discrepancy controls and baryonic merge
