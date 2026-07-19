---
type: dynamic_parameter_sweep
status: completed
created: 2026-05-26
topics:
  - atlas-dynamics
  - c-toy
  - eih
  - shadow-lanes
---

# C Toy Sweep 6 Step 2026-05-26

## Purpose

Test whether the context-excluded 1PN acceleration lane remains best aligned with the EIH-derived acceleration as PN strength changes.

## Sweep

Six-step runs:

- `c_toy = 4`
- `c_toy = 5`
- `c_toy = 8`
- `c_toy = 12`

Summary artifacts:

`/Users/danski2017/Desktop/Atlas_Solver_Project/codex_context/dynamic_evolution/skeleton_smoke_20260526/ctoy_sweep_summary_20260526/ctoy_sweep_summary.json`

`/Users/danski2017/Desktop/Atlas_Solver_Project/codex_context/dynamic_evolution/skeleton_smoke_20260526/ctoy_sweep_summary_20260526/ctoy_sweep_summary.png`

Run folders:

- `/Users/danski2017/Desktop/Atlas_Solver_Project/codex_context/dynamic_evolution/skeleton_smoke_20260526/skeleton_ctoy_sweep_c4_6step/`
- `/Users/danski2017/Desktop/Atlas_Solver_Project/codex_context/dynamic_evolution/skeleton_smoke_20260526/skeleton_ctoy_sweep_c5_6step/`
- `/Users/danski2017/Desktop/Atlas_Solver_Project/codex_context/dynamic_evolution/skeleton_smoke_20260526/skeleton_ctoy_sweep_c8_6step/`
- `/Users/danski2017/Desktop/Atlas_Solver_Project/codex_context/dynamic_evolution/skeleton_smoke_20260526/skeleton_ctoy_sweep_c12_6step/`

Output sizes:

- c4: `49M`
- c5: `48M`
- c8: `48M`
- c12: `43M`

## EIH Alignment

Mean acceleration difference against EIH:

| c_toy | Newtonian | R4 | legacy self-included 1PN | context-excluded 1PN |
|---:|---:|---:|---:|---:|
| 4 | `0.024327875` | `0.027756667` | `8.265211833` | `0.004257708` |
| 5 | `0.017156375` | `0.019350667` | `5.288153792` | `0.002494875` |
| 8 | `0.007534292` | `0.008391375` | `2.064855` | `0.001357542` |
| 12 | `0.003503542` | `0.003884417` | `0.91755875` | `0.000729375` |

Max acceleration difference against EIH:

| c_toy | Newtonian | R4 | legacy self-included 1PN | context-excluded 1PN |
|---:|---:|---:|---:|---:|
| 4 | `0.031133` | `0.036746` | `13.403111` | `0.006957` |
| 5 | `0.021930` | `0.025522` | `8.577054` | `0.003981` |
| 8 | `0.009615` | `0.011018` | `3.349919` | `0.002048` |
| 12 | `0.004469` | `0.005092` | `1.488761` | `0.001002` |

Read:

The context-excluded 1PN lane is the closest tested acceleration lane to EIH at every tested `c_toy`.

The legacy self-included lane improves as `c_toy` rises, but it remains orders of magnitude worse than the context-excluded lane. This is consistent with self-potential contamination being suppressed by larger `c_toy`, not eliminated by lawful treatment.

## Geometry Sensitivity

Seam totals across six steps:

- c4: `11`
- c5: `29`
- c8: `141`
- c12: `380`

Node totals across six steps:

- c4: `0`
- c5: `0`
- c8: `0`
- c12: `2`

Crossing battery records:

- c4: `5931`
- c5: `5265`
- c8: `4675`
- c12: `3588`

Tier 1 radial scalar traces:

- c4: `117840`
- c5: `117940`
- c8: `120420`
- c12: `113540`

Read:

As `c_toy` rises and PN corrections weaken, crossing counts fall but seam counts rise sharply under the current fixed seam threshold. This may be a real geometry sensitivity or a threshold/radius scaling artifact. It should not be promoted until tested with threshold scaling and ray-density checks.

## Claim Ceiling

This sweep supports the context-excluded 1PN lane as the serious acceleration shadow candidate.

It does not certify GR compliance, Atlas-native dynamics, seam/node robustness, or a final action principle.

## Next Move

Run a seam-threshold sensitivity check at `c_toy = 8` and `c_toy = 12` before interpreting the seam rise physically.

## Follow-Up

Completed:

`/Users/danski2017/Desktop/Atlas_Solver_Project/Relational_Labs/Relational_Labs/Atlas Codex Bridge/Dynamic Evolution/Seam Threshold Sweep 2026-05-26.md`

Read:

The seam rise is strongly threshold-sensitive and should not be interpreted physically until a scale-normalized seam criterion exists.
