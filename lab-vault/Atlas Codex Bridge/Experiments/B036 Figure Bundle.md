---
type: experiment_note
status: completed
created: 2026-05-15
topics:
  - galaxy-rotation
  - sparc
  - halogas
  - figure-bundle
  - mechanism-audit
---

# B036 Figure Bundle

B036 packages the B027-B034 real-data lane into an internal lab-review figure bundle. It adds no new public data, no new simulation run, and no website write. The purpose is to make the current mechanism story reviewable as figures, tables, captions, and claim boundaries.

## Package

- Experiment package: `codex_context/experiments/B036_figure_bundle`
- Report: `reports/B036_FIGURE_BUNDLE.md`
- Summary: `derived/B036_SUMMARY.json`
- Scene passport: `docs/B036_SCENE_PASSPORT.txt`

## Figure Spine

| Figure | File | Atlas role |
|---|---|---|
| Fig. 1 | `figures/B036_FIG01_transfer_split.svg` | HI-only and total-baryon ledgers separate in the `E/vc2` transfer hierarchy. |
| Fig. 2 | `figures/B036_FIG02_residual_closure.svg` | Absolute electric-Weyl loss does not close the residual loop; relative `E/vc2` is residual-adjacent in primary targets. |
| Fig. 3 | `figures/B036_FIG03_denominator_audit.svg` | Denominator-risk filtering strengthens residual-vs-`E/vc2` alignment across all primary targets. |
| Fig. 4 | `figures/B036_FIG04_observation_stability.svg` | B034 perturbation variants preserve positive filtered correlations across the primary targets. |

## Core Read

The lab-review story is now figure-shaped:

- B027 shows that HI-only and total-baryon source-proxy ledgers must stay separate.
- B032 blocks the simple absolute-`E` closure story.
- B033 keeps a bounded relative tensor/scalar mechanism alive after denominator audit.
- B034 keeps that mechanism positive under first observation-shaped ledger perturbations.

## Claim Ladder

| Rung | Status | Claim |
|---|---|---|
| 1 | supported | Coarse source ledgers can preserve scalar rotation-like information while changing electric-Weyl/eigenframe information by a different transfer function. |
| 2 | supported in local tested ledgers | After denominator audit, residual-adjacent radial structure appears in the relative tensor/scalar hierarchy for the primary SPARC/HALOGAS targets. |
| 3 | not yet established | A survey-level astrophysical law connecting curvature-transfer hierarchy to SPARC discrepancy. |
| 4 | explicitly blocked | Dark matter is unnecessary or ruled out by these tests. |

## Boundary

This is an internal figure bundle. Public methods-note language is possible only after lab review, and public dark-matter language remains no.

## Next Work

B037 should be a lab-review manuscript draft assembled from B031/B035 prose plus B036 figures, with the claim ladder and reviewer-risk box kept prominent.
