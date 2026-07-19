---
type: receipt
status: complete
created: 2026-05-15
packet: CODEX_PACKET_OBS_022_C5B1_SHELL_GEOMETRY_HARDENING
claim_status: shell geometry hardening gate / scratch theory / no calculation certified
repo_execution_authorized: false
---

# OBS_022 C5-B1 Shell Geometry Hardening Receipt

## Files Created

- [[C5-B1 Shell Geometry Hardening Gate]]
- [[OBS_022_C5B1_Shell_Geometry_Hardening_Receipt]]

## Files Modified

- None.

## Claim Status

Shell geometry hardening gate / scratch theory / no calculation certified.

The created gate is not certified evidence, not a calculation, not a conservation claim, not ordinary-energy accounting, not radiative balance, and not a prediction.

## Default Shell Declared

`S_mid`: mid-zone barycentric annular shell.

Declared features:

- center: barycenter
- exclude: balls of radius `R_excl` around each mass
- inner radial bound: `r_inner = a/4` from barycenter, unless it intersects exclusion balls
- outer radial bound: `r_outer = 3a/2`
- optional angular mask: none for first pass
- source exclusion condition: remove all points within `R_excl` of either mass
- required relation: `R_excl << a`

## Next Gate

OBS_023:
GPT-wing adjudication of shell geometry hardening and possible authorization of `S_mid` scaling/sensitivity estimate.

## Experiment Notes

No completed experiment notes were modified.

## Repo Code And codex_context

No repo code was touched.

No `codex_context` files were touched.

## Repo Execution Authorization

Repo execution remains unauthorized.
