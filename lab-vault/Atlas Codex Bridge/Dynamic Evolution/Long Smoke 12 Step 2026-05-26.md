---
type: dynamic_long_smoke
status: completed
created: 2026-05-26
topics:
  - atlas-dynamics
  - long-smoke
  - shadow-lanes
  - eih
---

# Long Smoke 12 Step 2026-05-26

## Purpose

Test whether the context-excluded 1PN acceleration lane remains the best EIH-aligned shadow candidate beyond the initial three-step smoke.

## Run

Run id:

`skeleton_long_smoke_20260526_12step`

Output:

`/Users/danski2017/Desktop/Atlas_Solver_Project/codex_context/dynamic_evolution/skeleton_smoke_20260526/skeleton_long_smoke_20260526_12step/`

Command shape:

`ATLAS_RUN_ID=skeleton_long_smoke_20260526_12step ATLAS_N_STEPS=12 ... atlas_skeleton_compute_local.py`

## Scale

- update steps: `12`
- crossing battery records: `10172`
- Tier 1 radial scalar trace records: `229080`
- shadow lane records: `132`
- EIH acceleration records: `192`
- output size: `102M`

## Crossing / Seam / Node Summary

Crossing counts:

- step 0: `[328, 383, 171, 275]`
- step 1: `[248, 250, 143, 182]`
- step 2: `[245, 250, 128, 205]`
- step 3: `[250, 234, 130, 195]`
- step 4: `[244, 245, 141, 203]`
- step 5: `[250, 249, 142, 174]`
- step 6: `[249, 250, 145, 193]`
- step 7: `[234, 243, 145, 184]`
- step 8: `[238, 249, 142, 183]`
- step 9: `[242, 250, 145, 176]`
- step 10: `[250, 247, 151, 178]`
- step 11: `[250, 250, 134, 179]`

Seams:

`[16, 2, 2, 5, 3, 1, 2, 4, 3, 4, 3, 2]`

Nodes:

`[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]`

## EIH Acceleration Comparison

Mean acceleration difference against EIH:

- Newtonian primary: `0.017185875`
- R4 geodesic: `0.0193821875`
- legacy self-included 1PN: `5.294725125`
- context-excluded 1PN: `0.002512`

Max acceleration difference against EIH:

- Newtonian primary: `0.022146`
- R4 geodesic: `0.025754`
- legacy self-included 1PN: `8.610959`
- context-excluded 1PN: `0.004005`

Figure:

`/Users/danski2017/Desktop/Atlas_Solver_Project/codex_context/dynamic_evolution/skeleton_smoke_20260526/skeleton_long_smoke_20260526_12step/figures/skeleton_smoke_eih_acceleration_comparison.png`

## Shadow Lane Drift

Mean position deviation from Newtonian primary:

- R4 geodesic: `0.003325`
- legacy self-included 1PN: `1.21158`
- context-excluded 1PN: `0.001825045`

Max position deviation from Newtonian primary:

- R4 geodesic: `0.008628`
- legacy self-included 1PN: `4.798344`
- context-excluded 1PN: `0.009345`

Figure:

`/Users/danski2017/Desktop/Atlas_Solver_Project/codex_context/dynamic_evolution/skeleton_smoke_20260526/skeleton_long_smoke_20260526_12step/figures/skeleton_smoke_shadow_lane_deviations.png`

## Read

The context-excluded 1PN acceleration lane remains the closest tested lane to the EIH-derived acceleration across all twelve update steps.

The legacy self-included lane continues to diverge and should remain a flagged negative control.

The context-excluded lane now earns "serious 1PN acceleration shadow candidate" status for further testing, not primary dynamics status.

## Claim Ceiling

This run does not certify GR compliance, Atlas-native dynamics, seam/node extraction, or a final action principle.

It only shows that the context-excluded 1PN acceleration shadow lane is much more consistent with the EIH-derived acceleration diagnostic than the self-included legacy lane.

## Next Move

Promote the context-excluded lane in diagnostics and run a modest c-toy sweep to test whether EIH agreement scales sensibly with PN strength.
