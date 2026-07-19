---
type: experiment_note
experiment_id: B016_galaxy_null_failure_scenes
status: completed
created: 2026-05-13
topics:
  - galaxy-averaging
  - failure-modes
  - null-scenes
  - tensor-scalar
  - electric-weyl
---

# B016 Galaxy Null Failure Scenes

## Purpose

B016 tries to weaken or collapse the galaxy tensor/scalar split.

This is the skeptical companion to B015. If the claim is real, it should have limiting cases and failure modes. If it is only a numerical artifact, the split should disappear under smooth, symmetric, far-field, or over-resolved conditions.

## Scenes

- smooth axisymmetric disc, midplane witness panel,
- spherical cloud, far-halo witness panel,
- Milky-Way-like disc, far-halo witness panel,
- Milky-Way-like disc, over-resolved grid control.

Each scene uses 12,000 sources and five coarse methods.

## Outputs

Run package:

`codex_context/experiments/B016_galaxy_null_failure_scenes`

Summary:

`codex_context/experiments/B016_galaxy_null_failure_scenes/derived/B016_SUMMARY.json`

Method table:

`codex_context/experiments/B016_galaxy_null_failure_scenes/derived/B016_METHOD_SUMMARY.csv`

Report:

`codex_context/experiments/B016_galaxy_null_failure_scenes/reports/B016_REPORT.txt`

## Result

| Scene | Weak/collapsed methods | Best E/vc2 ratio | Best method | Best scalar E/vc2 |
|---|---:|---:|---|---:|
| MW-like far halo panel | 0/5 | 2.008 | axisymmetric annular | 2.227 |
| MW-like overresolved grid | 0/5 | 2.811 | low order multipole | 5.038 |
| smooth axisymmetric disc midplane | 0/5 | 3.520 | CIC mesh fine | 9.738 |
| spherical cloud halo panel | 0/5 | 1.906 | CIC mesh fine | 2.813 |

## Atlas Read

B016 did not find a clean collapse of the tensor/scalar split.

It did find limiting behavior:

- far-halo and spherical scenes reduce absolute disagreements,
- CIC and multipole controls can make eigenframe disagreement tiny in spherical/far-field panels,
- the E/vc2 ratio still stays above roughly 1.9 in the best null case.

Atlas sentence:

```text
The split weakens in smoother or farther-field scenes, but it does not vanish under these first null controls.
```

## Claim Boundary

B016 is an internal failure-mode benchmark. It is not a real-survey result, not a dark-matter claim, not a GR replacement, and not a public result.

## Next

The galaxy lane now has positive anchors and first failure-mode bounds. The next useful move is a synthesis pass: B017 should consolidate B006-B016 into a paper-grade internal claim ledger and decide what additional run, if any, is needed before public writing.
