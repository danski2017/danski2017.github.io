---
type: experiment_note
status: completed
created: 2026-05-14
program:
  - mesoscale-curvature
  - sparc
  - draft-bundle
claim_level: internal_draft_bundle
---

# B031 Internal Draft Bundle

## Purpose

B031 turns the B030 paper spine into a lab-review draft bundle. This is a writing architecture pass, not a new simulation.

## Source Package

- Experiment package: `codex_context/experiments/B031_internal_draft_bundle`
- Script: `codex_context/scripts/b031_internal_draft_bundle.py`
- Draft bundle: `reports/B031_INTERNAL_DRAFT_BUNDLE.md`
- JSON bundle: `derived/B031_INTERNAL_DRAFT_BUNDLE.json`

## Draft Status

- Draft now: `true`
- Public now: `false`
- B029 required for public: `true`, unless the lab explicitly chooses a tightly bounded internal-methods note.

## Working Title

Scalar Rotation Preservation and Electric-Weyl Transfer Under Galaxy Coarse-Graining

## Abstract Draft

We test how common coarse representations of galaxy source structure transfer scalar rotation-like information compared with local electric-Weyl/eigenframe structure. Using local SPARC/HALOGAS source-proxy scenes and declared baryonic augmentations, we find that sector-style coarse branches can preserve scalar summaries more tightly than tensor/eigenframe structure. The result is a transfer-function methods claim inside weak-field GR-compatible language, not a dark-matter explanation or a survey-level law.

## Methods Outline

### Source Data

- SPARC public rotation and mass-model rows already mirrored in the repo.
- HALOGAS HI moment products already mirrored in the repo for NGC2403, NGC1003, NGC0891, and NGC5055.
- No new data were downloaded for B027-B031.

### HI Source Proxies

- Use existing HALOGAS-derived HI source-proxy scenes from B020, B022, B024, and B025.
- Normalize selected HI support proxies to SPARC HI mass.
- Keep NGC0891 flagged as edge-on sky-plane control.

### Baryonic Source Proxies

- Convert SPARC 3.6um disk/bulge surface-brightness rows into annular source proxies.
- Use declared baseline `M/L` values: disk `0.5`, bulge `0.7`.
- Treat this as a source-proxy construction, not a full photometric decomposition.

### Witness Protocol

- Evaluate retained source scene against sector/radial/low-order coarse branches.
- Track scalar rotation-like proxy, electric-Weyl Frobenius delta, and eigenframe disagreement.
- Use `E/vc2` only as a relative transfer diagnostic, not as an energy or dark-matter observable.

## Results Outline

### HI-Only Ledger

- B021 NGC2403: `E/vc2 = 1.369`
- B022 NGC1003: `E/vc2 = 4.902`
- B024 NGC0891: `E/vc2 = 4.595`
- B025 NGC5055: `E/vc2 = 1.514`

### Total-Baryon Ledger

- NGC2403: `E/vc2 = 12.11`
- NGC1003: `E/vc2 = 11.76`
- NGC0891: `E/vc2 = 14.49`
- NGC5055: `E/vc2 = 5.878`

### Stability Ledger

- B028 global `E/vc2` floor: `3.538`
- B028 global median: `11.54`
- Fraction above `E/vc2 = 1`: `1.0`

## Figure Plan

- Figure 1: HI-only transfer ledger.
- Figure 2: HI-only vs total-baryon transfer.
- Figure 3: Baryonic stability floor.
- Figure 4: Claim ladder from toy controls to real-data stability.

## Claim Boundary Box

- Not a dark-matter explanation.
- Not a MOND test.
- Not a challenge to GR or SR.
- Not a full survey result.
- Not a full photometric decomposition.
- Not evidence for a monotonic SPARC-discrepancy law.

## Reviewer-Risk Checklist

| Risk | Severity | Mitigation |
|---|---|---|
| NGC0891 edge-on geometry | high | Mark as edge-on sky-plane control; do not compare directly to deprojected disc witnesses. |
| Annular stellar proxy is not full photometric decomposition | high | State proxy construction plainly; avoid total-baryon galaxy claim beyond declared source proxies. |
| Small real-data sample | high | No survey-level correlation; frame as four-target methods study. |
| `E/vc2` ratio can inflate when scalar error is very small | medium | Always show p90 E and p90 vc2 alongside the ratio. |
| Dark-matter-adjacent misreading | high | Place non-claims before implications; avoid explanatory language about missing mass. |

## Decision

The spine is strong enough for internal drafting. Public release should wait for targeted observation-shaped nuisance tests or an explicit lab decision to publish as a bounded methods note.
