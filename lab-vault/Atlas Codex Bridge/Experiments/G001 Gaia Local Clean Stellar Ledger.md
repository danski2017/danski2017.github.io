---
type: experiment_note
status: completed
created: 2026-05-15
topics:
  - gaia
  - local-stellar-ledger
  - tensor-scalar-transfer
  - future-experiments
---

# G001 Gaia Local Clean Stellar Ledger

G001 starts Gaia Lane 1 with a no-download pilot using the Gaia 25 pc cache already present in the repo.

This is a control ledger, not the full large Gaia Lane 1 result. It uses a declared photometric mass proxy from Gaia absolute G magnitude, not official Gaia FLAME masses.

Supersession note: G001 is now historical scouting only. G001H corrected the scalar-channel evaluation and is the authoritative Gaia 25 pc result.

## Package

- Experiment package: `codex_context/experiments/G001_gaia_local_clean_stellar_ledger`
- Report: `reports/G001_REPORT.md`
- Summary: `derived/G001_SUMMARY.json`
- Retained source proxy ledger: `derived/G001_RETAINED_SOURCE_PROXY_LEDGER.csv`
- Method summary: `derived/G001_METHOD_SUMMARY.csv`
- Scene passport: `docs/G001_SCENE_PASSPORT.txt`

## Source Cuts

- Input rows including header: `3901`
- Retained source proxies: `3894`
- Radius: `25 pc`
- Required: positive parallax, parallax/parallax_error >= 10, RUWE < 1.4, Gaia G magnitude present
- Rejections: `{"missing_required": 6}`

## Result

| Method | Retained | Coarse | Witnesses | p90 scalar | p90 E | p90 eigen | E/scalar |
|---|---:|---:|---:|---:|---:|---:|---:|
| radial_shell_5pc | 3894 | 5 | 576 | 8.22 | 16.57 | 0.8279 | 2.016 |
| octant_radial_5pc | 3894 | 40 | 576 | 0.9038 | 5.976 | 0.8728 | 6.612 |
| sky_sector_radial_5pc | 3894 | 209 | 576 | 0.6467 | 3.192 | 0.8296 | 4.936 |

## Atlas Read

The no-download Gaia pilot reproduces the broad Atlas pattern in a measured local stellar-source field: richer coarse branches reduce scalar disagreement faster than they reduce electric-Weyl/eigenframe disagreement.

The original scout split should not be cited. Use [[G001H GFRO-Hardened Gaia Local Ledger]] and [[G001I Independent Gaia Check]] instead.

## Boundary

Do not overread this run.

- Not a full Milky Way model.
- Not official Gaia FLAME mass-bearing analysis.
- Not a dark-matter test.
- Not the final Gaia Lane 1 result.

## Next Gate

To complete Lane 1 at meaningful scale, the lab should approve a Gaia DR3 query or bulk table acquisition for a larger local clean subset, preferably with official mass-bearing astrophysical-parameter joins where quality flags permit.
