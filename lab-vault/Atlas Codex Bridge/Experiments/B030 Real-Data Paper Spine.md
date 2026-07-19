---
type: experiment_note
status: completed
created: 2026-05-14
program:
  - mesoscale-curvature
  - sparc
  - paper-spine
claim_level: internal_paper_spine
---

# B030 Real-Data Paper Spine

## Purpose

B030 is deliberately not another broad simulation push. It consolidates B021-B028 and asks whether the lab should keep running, draft, or run only targeted threats to the current claim.

## Source Package

- Experiment package: `codex_context/experiments/B030_real_data_paper_spine`
- Script: `codex_context/scripts/b030_real_data_paper_spine.py`
- Paper spine: `reports/B030_REAL_DATA_PAPER_SPINE.md`
- JSON spine: `derived/B030_PAPER_SPINE.json`

## Working Title

Scalar Rotation Preservation and Electric-Weyl Transfer Under Galaxy Coarse-Graining

## Central Claim

The real-data lane supports a transfer-function claim: scalar rotation-like information and electric-Weyl/eigenframe information do not pass through the same coarse representation with one universal fidelity.

Public-safe version:

> Across local SPARC/HALOGAS source-proxy scenes, sector-style coarse branches can preserve scalar rotation-like summaries more tightly than local electric-Weyl/eigenframe structure.

## Evidence Blocks

### HI-Only Four-Target Ledger

B026 consolidated NGC2403, NGC1003, NGC0891, and NGC5055.

HI-only `E/vc2` values:

- B021 NGC2403: `1.369`
- B022 NGC1003: `4.902`
- B024 NGC0891: `4.595`
- B025 NGC5055: `1.514`

Caution: `n=4`, heterogeneous geometry, not a monotonic SPARC-discrepancy law.

### First Total-Baryon Augmentation

B027 added local SPARC stellar disk/bulge annular source proxies.

Total-baryon `E/vc2` values:

- NGC2403: `12.11`
- NGC1003: `11.76`
- NGC0891: `14.49`
- NGC5055: `5.878`

Caution: annular source-proxy construction, not full photometric decomposition.

### Baryonic Stability Hardening

B028 stress-tested the B027 construction across local `M/L` and resolution variants.

- variants: `52`
- global `E/vc2` floor: `3.538`
- global median: `11.54`
- fraction above `E/vc2 = 1`: `1.0`

## Interpretation

The current result is not that SPARC discrepancy predicts tensor loss. B026 argues against that simple story.

The cleaner result is a transfer-function claim: scalar rotation-like summaries and electric-Weyl/eigenframe structure do not pass through coarse galaxy representations with one universal fidelity.

## Non-Claims

- Not a dark-matter explanation.
- Not a MOND test.
- Not a challenge to GR or SR.
- Not a full survey result.
- Not a full photometric decomposition.
- Not evidence for a monotonic SPARC-discrepancy law.

## Decision

Stop broad simulation expansion for now.

The next valuable work is either:

- targeted B029 observation-shaped nuisances that directly threaten the claim, or
- internal paper drafting with a Methods section, figure bundle, and claim-boundary box.
