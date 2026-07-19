---
type: dynamic_visual_audit
status: completed
created: 2026-05-26
topics:
  - atlas-dynamics
  - 1pn
  - visualization
  - shadow-lanes
---

# 1PN Interpretive Animation 2026-05-26

## Purpose

Render a human-auditable 3D animation of the context-excluded 1PN shadow lane against the Newtonian primary lane.

This is a visual audit object, not certification.

## Source Run

`/Users/danski2017/Desktop/Atlas_Solver_Project/codex_context/dynamic_evolution/skeleton_smoke_20260526/skeleton_long_smoke_20260526_12step`

## Renderer

`/Users/danski2017/Desktop/Atlas_Solver_Project/codex_context/dynamic_evolution/skeleton_smoke_20260526/render_1pn_interpretive_animation.py`

## Outputs

GIF:

`/Users/danski2017/Desktop/Atlas_Solver_Project/codex_context/dynamic_evolution/skeleton_smoke_20260526/skeleton_long_smoke_20260526_12step/figures/atlas_1pn_interpretive_animation.gif`

Final frame:

`/Users/danski2017/Desktop/Atlas_Solver_Project/codex_context/dynamic_evolution/skeleton_smoke_20260526/skeleton_long_smoke_20260526_12step/figures/atlas_1pn_interpretive_final_frame.png`

Summary:

`/Users/danski2017/Desktop/Atlas_Solver_Project/codex_context/dynamic_evolution/skeleton_smoke_20260526/skeleton_long_smoke_20260526_12step/figures/atlas_1pn_interpretive_animation_summary.json`

## How To Read

Left panel:

- solid colored track: Newtonian leapfrog primary
- dashed/outlined marker: context-excluded 1PN shadow lane
- faint red `x`: legacy self-included 1PN anomaly lane

Right panel:

- same source positions
- arrows show the context-excluded 1PN correction vector
- vectors are magnified by `350x` for visual audit

Node 0 remains an update index, not a physical clock.

## Delta Summary

Final context-excluded 1PN position deltas:

- Heavy: `0.000860`
- Medium: `0.004894`
- Light: `0.008168`
- Dwarf: `0.009345`

Final legacy self-included anomaly deltas:

- Heavy: `4.798344`
- Medium: `3.919475`
- Light: `1.921850`
- Dwarf: `1.029770`

## Read

The context-excluded 1PN lane remains visually close to the Newtonian primary on physical scene scale, which is why the correction-vector panel is necessary.

The legacy self-included lane visibly departs from the physical neighborhood, consistent with the earlier self-potential contamination diagnosis.

## Claim Ceiling

This animation shows the currently best 1PN shadow-lane behavior in the skeleton toy.

It does not certify an Atlas-native update law because the primary evolution is still Newtonian leapfrog.

## Next Move

Use the same renderer on a future Atlas-native candidate lane once one exists, then compare visual correction structure, conservation diagnostics, and EIH residuals side by side.
