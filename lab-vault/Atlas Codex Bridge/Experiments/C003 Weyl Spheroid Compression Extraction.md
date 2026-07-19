---
type: experiment_note
status: completed
created: 2026-05-13
experiment_id: C003_weyl_spheroid_compression_extraction
topics:
  - curvature-identity
  - weyl-spheroid
  - compression
  - multipole
  - website-payload
---

# C003 Weyl Spheroid Compression Extraction

## Status

Completed paper-result ledger extraction.

Package:

`codex_context/experiments/C003_weyl_spheroid_compression_extraction`

Script:

`codex_context/scripts/c003_weyl_spheroid_compression_extraction.py`

Source paper:

`papers/public/gcs_series/weyl_spheroid_final_v0_11.pdf`

Package size:

`0.008 MiB`

## Purpose

Replace the toy compression placeholder in the Curvature Identity Atlas with a paper-backed compression witness from the Weyl Spheroid paper.

## Model

Declared fiducial spheroid:

```text
a = 1
c = 0.5
rho0 = 1
G = 1
tolerance tau = 1e-3
```

Diagnostic:

```text
exterior potential multipole compression-faithful radius
```

## Ledgered Paper Values

From Weyl Spheroid v0.11, section 13.7:

| Lmax | r_tau / a | Reduction vs Lmax 2 |
|---:|---:|---:|
| 2 | 2.61 | 1.000 |
| 4 | 1.63 | 0.625 |
| 6 | 1.33 | 0.510 |
| 8 | 1.17 | 0.448 |
| 10 | 1.08 | 0.414 |

Read:

```text
Higher truncation order moves the compression-faithful radius inward.
```

## Website Patch

Payload patch:

`codex_context/experiments/C003_weyl_spheroid_compression_extraction/derived/curvature_identity_compression_patch_v0_1.json`

Public copy:

```text
For the fiducial oblate spheroid in the Weyl-electric attribution paper,
higher multipole truncation order moves the compression-faithful radius inward
at a declared tolerance of 1e-3.
```

Claim ceiling:

```text
Compression radii are approximation-validity scales, not physical boundaries
or parity surfaces.
```

## Claim Boundary

C003 ledgers paper-reported values. It does not recompute the original multipole expansion.

Non-claims:

- no physical boundary,
- no parity surface,
- no observable claim,
- no full GR compression theorem,
- no solved handoff mechanism.

## Next Gate

C004 should make jurisdiction ledger-backed by using GFRO/source-context examples rather than toy source/context mass ratios.

