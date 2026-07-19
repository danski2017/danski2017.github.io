---
type: experiment_note
experiment_id: B015_galaxy_observational_anchor
status: completed
created: 2026-05-13
topics:
  - galaxy-averaging
  - observational-anchor
  - electric-weyl
  - coarse-graining
  - tensor-scalar
---

# B015 Galaxy Observational Anchor

## Purpose

B015 moves the galaxy averaging lane closer to an observation-shaped reduction.

Instead of only comparing retained sources against generic coarse averages, B015 adds declared observing protocols:

- inclination,
- position angle,
- beam smearing,
- line-of-sight velocity map,
- tilted-ring recovery,
- beam-smoothed surface-density reconstruction.

## Scene

- 12,000-source Milky-Way-like synthetic disc,
- 4,096 retained witness points,
- one rotating snapshot,
- four observing protocols:
  - baseline inclination 62 degrees, beam 1.45 pixels,
  - low inclination 35 degrees, beam 1.00 pixels,
  - high inclination 75 degrees, beam 2.20 pixels,
  - rotated position angle 65 degrees, beam 1.45 pixels.

## Outputs

Run package:

`codex_context/experiments/B015_galaxy_observational_anchor`

Summary:

`codex_context/experiments/B015_galaxy_observational_anchor/derived/B015_SUMMARY.json`

Method table:

`codex_context/experiments/B015_galaxy_observational_anchor/derived/B015_METHOD_SUMMARY.csv`

Report:

`codex_context/experiments/B015_galaxy_observational_anchor/reports/B015_REPORT.txt`

## Headline Result

The observation-shaped reductions do not erase the tensor/scalar split.

Best observational scalar preservation:

| Protocol | Method | p90 vc2 delta | p90 E-Fro delta | p90 eigenframe disagreement | E/vc2 ratio |
|---|---|---:|---:|---:|---:|
| low_inc35_beam100 | obs_beam_surface_density_grid | 0.223 | 0.798 | 0.936 | 3.583 |

The low-inclination beam-smoothed surface-density reconstruction preserved the scalar rotation proxy best, but still carried much larger electric-Weyl and eigenframe disagreement.

## Observation Branch Read

| Protocol | Method | p90 vc2 | p90 E-Fro | p90 eigenframe | E/vc2 |
|---|---|---:|---:|---:|---:|
| baseline_inc62_beam145 | tilted ring | 0.852 | 0.953 | 0.979 | 1.118 |
| baseline_inc62_beam145 | surface density grid | 0.282 | 0.797 | 0.947 | 2.827 |
| low_inc35_beam100 | tilted ring | 0.798 | 0.949 | 0.978 | 1.189 |
| low_inc35_beam100 | surface density grid | 0.223 | 0.798 | 0.936 | 3.583 |
| high_inc75_beam220 | tilted ring | 0.990 | 0.961 | 0.975 | 0.970 |
| high_inc75_beam220 | surface density grid | 0.489 | 0.851 | 0.951 | 1.740 |
| rotated_pa65_beam145 | tilted ring | 0.902 | 0.950 | 0.978 | 1.053 |
| rotated_pa65_beam145 | surface density grid | 0.284 | 0.812 | 0.943 | 2.862 |

## Atlas Read

B015 makes the galaxy story harder to dismiss as a toy averaging artifact.

The scalar branch is observation-sensitive. Some protocols preserve useful scalar rotation information much better than others.

But the tensor branch still reports large electric-Weyl and eigenframe disagreement.

Atlas sentence:

```text
Observation-shaped scalar recovery does not guarantee tensorial curvature identity recovery.
```

## Claim Boundary

B015 is a synthetic internal benchmark. It is not real survey data, not a dark-matter claim, not a GR replacement, and not a public result.

## Next

B016 should deliberately seek failure modes where the tensor/scalar split weakens or vanishes:

- nearly spherical source distribution,
- smooth axisymmetric disc,
- over-resolved grid,
- far-halo witness panel.
