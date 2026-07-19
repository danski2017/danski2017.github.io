---
type: experiment_note
experiment_id: B017_galaxy_evidence_synthesis
status: completed
created: 2026-05-13
topics:
  - galaxy-averaging
  - evidence-synthesis
  - paper-spine
  - claim-boundary
---

# B017 Galaxy Evidence Synthesis

## Purpose

B017 consolidates B006-B016 into a paper-grade internal claim ledger.

No new simulation was run. This is a synthesis pass.

## Outputs

Run package:

`codex_context/experiments/B017_galaxy_evidence_synthesis`

Evidence synthesis:

`codex_context/experiments/B017_galaxy_evidence_synthesis/derived/B017_GALAXY_EVIDENCE_SYNTHESIS.json`

Report:

`codex_context/experiments/B017_galaxy_evidence_synthesis/reports/B017_REPORT.txt`

Internal paper spine:

`codex_context/experiments/B017_galaxy_evidence_synthesis/reports/B017_INTERNAL_PAPER_SPINE.md`

## Core Headline

```text
Observation-shaped scalar recovery does not guarantee tensorial curvature identity recovery.
```

## Strongest Current Anchor

B015 low-inclination, clean-beam, surface-density reconstruction:

| Metric | Value |
|---|---:|
| p90 vc2 delta | 0.223 |
| p90 E-Frobenius delta | 0.798 |
| p90 eigenframe disagreement | 0.936 |
| E/vc2 ratio | 3.583 |

## Best Current Failure-Mode Bound

B016 spherical cloud halo panel:

| Metric | Value |
|---|---:|
| best E/vc2 ratio | 1.906 |
| weak/collapsed methods | 0/5 |

## Claim Ladder

Safe internal claim:

```text
In synthetic weak-field Milky-Way-like scenes, common coarse-graining and
observation-shaped reductions can preserve scalar rotation proxies more
effectively than local electric-Weyl/eigenframe witnesses.
```

Review-candidate public claim:

```text
Scalar recovery is not tensorial curvature identity recovery.
```

Do not claim:

- dark matter explanation,
- real galaxy survey result,
- GR replacement,
- new force,
- self-consistent N-body dynamics,
- universal law independent of witness and method.

## Recommendation

The galaxy lane is strong enough for an internal paper/web spine draft.

It is not yet ready for a real-survey claim, dark-matter-adjacent public claim, or broad cosmological claim.

## Next

Either:

- draft the internal paper/web spine from B017, or
- run B018 as a survey-forward-model hardening pass with noise, PSF, selection, inclination uncertainty, and velocity fit residuals.
