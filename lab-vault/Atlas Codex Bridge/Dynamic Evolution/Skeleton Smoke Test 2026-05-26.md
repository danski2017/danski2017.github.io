---
type: dynamic_smoke_test
status: active
created: 2026-05-26
topics:
  - atlas-dynamics
  - skeleton
  - smoke-test
  - visuals
---

# Skeleton Smoke Test 2026-05-26

## Purpose

Run the dynamic handoff skeleton locally as a non-certifying smoke test and generate first machine-backed visual audit artifacts.

This test checks whether the handoff pieces can execute in the Atlas workspace and produce inspectable crossing, seam, node, clock, and grid-scale records.

## Source

Imported handoff script:

`/private/tmp/atlas_dynamic_session_20260524_handoff_inspect/atlas_skeleton_compute.py`

Local adapted copy:

`/Users/danski2017/Desktop/Atlas_Solver_Project/codex_context/dynamic_evolution/skeleton_smoke_20260526/atlas_skeleton_compute_local.py`

Renderer:

`/Users/danski2017/Desktop/Atlas_Solver_Project/codex_context/dynamic_evolution/skeleton_smoke_20260526/render_skeleton_smoke.py`

Output:

`/Users/danski2017/Desktop/Atlas_Solver_Project/codex_context/dynamic_evolution/skeleton_smoke_20260526/out/`

Battery ledger:

`/Users/danski2017/Desktop/Atlas_Solver_Project/codex_context/dynamic_evolution/skeleton_smoke_20260526/out/crossing_battery_records.jsonl`

Tier 1 radial scalar trace:

`/Users/danski2017/Desktop/Atlas_Solver_Project/codex_context/dynamic_evolution/skeleton_smoke_20260526/out/radial_scalar_traces.jsonl`

Shadow lane ledger:

`/Users/danski2017/Desktop/Atlas_Solver_Project/codex_context/dynamic_evolution/skeleton_smoke_20260526/out/shadow_lane_records.jsonl`

EIH-derived acceleration comparison:

`/Users/danski2017/Desktop/Atlas_Solver_Project/codex_context/dynamic_evolution/skeleton_smoke_20260526/out/eih_acceleration_records.jsonl`

Manifest:

`/Users/danski2017/Desktop/Atlas_Solver_Project/codex_context/dynamic_evolution/skeleton_smoke_20260526/out/manifest.json`

## Run Settings

- scene: 4-source tetrahedral
- masses: Heavy 10, Medium 5, Light 2, Dwarf 1
- steps: 3
- base rays: 300
- radial samples: 20
- `c_toy`: 5.0
- extraction: R5-native residual, `||E_self|| = ||E_ctx_1PN||`
- primary motion driver: Newtonian leapfrog
- shadow lanes: R4 geodesic correction and 1PN correction present in script
- L0 variational diagnostics: Newtonian `T - V` baseline only, not an Atlas-native action
- L1 variational diagnostics: EIH 1PN weak-field shadow diagnostic only, not an Atlas-native action

## Battery Ledger Refinement

The local skeleton now persists a crossing-level tensor battery ledger instead of discarding most computed quantities after crossing extraction.

Current battery scope: full records at accepted R5 crossings plus Tier 1 scalar traces for every sampled radial point. The run does not persist full tensor matrices at every radial sample along every ray.

Ledger size:

- crossing records: `2808`
- fields per crossing record: `34`
- battery JSONL size: `4.9M`
- radial scalar trace records: `61760`
- fields per radial scalar trace: `14`
- radial scalar trace JSONL size: `20M`
- full smoke output size after current figures: `27M`

Persisted crossing fields include source identity, source position, crossing position, ray direction, radius, R5 residual, R2 residual, R0 potential, R1 acceleration, R2 electric tensors, R3 lapse/spatial scale, R4 Christoffel spatial tensor, R5 1PN total/context tensors, R5 eigenvalues and principal eigenvector, self/context/cross correction branches, Kretschmann proxy, `K_self`, `K_context`, `K_total`, ADM scalar, and ADM Hamiltonian residual.

Persisted radial scalar fields include update step, source identity, source position, ray id, ray direction, radial index, radius, R5 residual, R2 residual, R5 cross fraction, `K_total`, and ADM Hamiltonian residual.

L0 Newtonian variational diagnostics are now emitted per update step:

- kinetic energy
- potential energy
- total energy
- ordinary Newtonian Lagrangian `T - V`
- discrete action increment `L * DT`
- linear momentum
- angular momentum

L1 EIH variational diagnostics are now emitted per update step:

- EIH 1PN Lagrangian
- L0 reference Lagrangian
- 1PN correction term
- correction fraction
- discrete action increment

Shadow lane records are now emitted for matched update comparisons:

- R4 geodesic lane position and velocity
- legacy self-included R5/1PN geodesic lane position and velocity
- context-excluded R5/1PN geodesic lane position and velocity
- Newtonian primary position and velocity
- position/velocity deviation vectors and norms

EIH acceleration records are now emitted for smoke-grade Euler-Lagrange comparison:

- EIH-derived acceleration from the L1 Lagrangian
- lane acceleration
- acceleration difference vector
- acceleration difference norm

Mean source summaries across all three steps:

- Heavy: `821` records, mean R5 cross fraction `6.522450%`, mean R2 residual `10.532720`, mean Hamiltonian residual `0.014935719`, mean `K_total` `-0.003057775`
- Medium: `883` records, mean R5 cross fraction `11.436322%`, mean R2 residual `32.554551`, mean Hamiltonian residual `0.151307554`, mean `K_total` `0.001485855`
- Light: `442` records, mean R5 cross fraction `32.299176%`, mean R2 residual `-0.006048`, mean Hamiltonian residual `0.000001921`, mean `K_total` `-0.000310405`
- Dwarf: `662` records, mean R5 cross fraction `35.142982%`, mean R2 residual `-0.003855`, mean Hamiltonian residual `0.000000896`, mean `K_total` `-0.000014533`

Observed scalar ranges:

- R5 residual: `-0.000426` to `3.599752`
- R2 residual: `-0.046550` to `42.158257`
- R5 cross fraction: `5.669174%` to `42.009458%`
- `K_total`: `-0.967994` to `0.969255`
- ADM Hamiltonian residual: `-0.001991` to `0.624541`

Mean R5 correction norms:

- self A correction: `11.726984`
- self context correction: `0.003229`
- cross correction: `1.118394`

## Results

Step 0:
crossings `[328, 383, 171, 275]`, seams `16`, nodes `0`.

Step 1:
crossings `[248, 250, 143, 182]`, seams `2`, nodes `0`.

Step 2:
crossings `[245, 250, 128, 205]`, seams `2`, nodes `0`.

Subjective clocks desynchronized immediately. Heavy clock advanced fastest; Dwarf clock advanced slowest.

Grid scales were source-specific and stable over the tiny run: Heavy near `1.028`, Medium near `1.045`, Light near `1.055`, Dwarf near `1.058`.

Median GCS radii remained stable after the first adaptive update, with Heavy and Medium small and Light/Dwarf large under this extraction.

## Visual Artifacts

Panel:

`/Users/danski2017/Desktop/Atlas_Solver_Project/codex_context/dynamic_evolution/skeleton_smoke_20260526/out/figures/skeleton_smoke_steps_panel.png`

Animated GIF:

`/Users/danski2017/Desktop/Atlas_Solver_Project/codex_context/dynamic_evolution/skeleton_smoke_20260526/out/figures/skeleton_smoke_steps.gif`

Metrics:

`/Users/danski2017/Desktop/Atlas_Solver_Project/codex_context/dynamic_evolution/skeleton_smoke_20260526/out/figures/skeleton_smoke_metrics.png`

Tensor battery summary:

`/Users/danski2017/Desktop/Atlas_Solver_Project/codex_context/dynamic_evolution/skeleton_smoke_20260526/out/figures/skeleton_smoke_tensor_battery_summary.png`

R5 branch decomposition:

`/Users/danski2017/Desktop/Atlas_Solver_Project/codex_context/dynamic_evolution/skeleton_smoke_20260526/out/figures/skeleton_smoke_r5_branch_decomposition.png`

R5 eigenvalue anisotropy:

`/Users/danski2017/Desktop/Atlas_Solver_Project/codex_context/dynamic_evolution/skeleton_smoke_20260526/out/figures/skeleton_smoke_r5_eigen_anisotropy.png`

R5 principal eigenvector field:

`/Users/danski2017/Desktop/Atlas_Solver_Project/codex_context/dynamic_evolution/skeleton_smoke_20260526/out/figures/skeleton_smoke_r5_eigenvector_field.png`

Tier 1 radial residual profiles:

`/Users/danski2017/Desktop/Atlas_Solver_Project/codex_context/dynamic_evolution/skeleton_smoke_20260526/out/figures/skeleton_smoke_tier1_radial_residual_profiles.png`

L0 variational diagnostics:

`/Users/danski2017/Desktop/Atlas_Solver_Project/codex_context/dynamic_evolution/skeleton_smoke_20260526/out/figures/skeleton_smoke_l0_variational_diagnostics.png`

L1 EIH variational diagnostics:

`/Users/danski2017/Desktop/Atlas_Solver_Project/codex_context/dynamic_evolution/skeleton_smoke_20260526/out/figures/skeleton_smoke_l1_eih_variational_diagnostics.png`

Shadow lane deviations:

`/Users/danski2017/Desktop/Atlas_Solver_Project/codex_context/dynamic_evolution/skeleton_smoke_20260526/out/figures/skeleton_smoke_shadow_lane_deviations.png`

EIH acceleration comparison:

`/Users/danski2017/Desktop/Atlas_Solver_Project/codex_context/dynamic_evolution/skeleton_smoke_20260526/out/figures/skeleton_smoke_eih_acceleration_comparison.png`

Per-step PNGs:

- `/Users/danski2017/Desktop/Atlas_Solver_Project/codex_context/dynamic_evolution/skeleton_smoke_20260526/out/figures/skeleton_smoke_step_000.png`
- `/Users/danski2017/Desktop/Atlas_Solver_Project/codex_context/dynamic_evolution/skeleton_smoke_20260526/out/figures/skeleton_smoke_step_001.png`
- `/Users/danski2017/Desktop/Atlas_Solver_Project/codex_context/dynamic_evolution/skeleton_smoke_20260526/out/figures/skeleton_smoke_step_002.png`

## Status Read

The skeleton executes locally and produces coherent first-pass machine data.

The crossing clouds are dense enough to visualize source jurisdictions.

The seam/node layer is not yet robust at this miniature setting. Seam count drops from 16 to 2 after step 0 and no nodes appear. This is not a failure; it means seam/node certification needs threshold, ray density, extraction cadence, and lineage hardening.

The current script remains a dynamic prototype, not an Atlas-native dynamics engine. Source motion is still driven by Newtonian leapfrog.

The L0 diagnostics show that the Newtonian baseline is numerically clean over the three-step smoke: total energy is stable to the shown precision, linear momentum remains zero, and angular momentum norm remains `56.028119`. This validates it as a baseline lane only.

The L1 EIH diagnostic reports a weak-field 1PN correction of about `2.289%` of the L0 Lagrangian across the three-step smoke. This makes the 1PN variational lane measurable, but it does not yet integrate an L1 trajectory and does not promote the dynamics to Atlas-native status.

The shadow-lane ledger shows R4 remains close to Newtonian while the legacy self-included R5/1PN acceleration lane diverges much more strongly. A context-excluded R5/1PN lane was added to test the suspected self-potential contamination.

Mean position deviation:

- R4: `0.00073025`
- legacy self-included R5/1PN: `0.10393525`
- context-excluded R5/1PN: `0.000357625`

Mean velocity deviation:

- R4: `0.000340125`
- legacy self-included R5/1PN: `0.782919125`
- context-excluded R5/1PN: `0.00246325`

Read: the anomaly collapses when source-motion 1PN correction excludes self-potential. The context-excluded lane is now the serious 1PN acceleration shadow candidate; the legacy self-included lane remains as a flagged negative control.

The EIH-derived acceleration diagnostic confirms the same result. Mean acceleration difference against EIH:

- Newtonian primary: `0.017150667`
- R4 geodesic: `0.019344667`
- legacy self-included R5/1PN: `5.286551`
- context-excluded R5/1PN: `0.002488083`

Read: context-excluded 1PN is the closest tested acceleration lane to the EIH-derived acceleration in this smoke run.

The tensor battery is now substantially richer on the ledger than in the renders. The ledger holds matrix-valued R2/R4/R5 objects, eigenstructure, correction branches, and ADM comparison scalars per crossing.

The render now shows crossing clouds, seams, source positions, clocks, grid scales, GCS radii, four scalar battery summaries, R5 branch decomposition, eigenvalue anisotropy, a sampled principal-eigenvector field, and Tier 1 radial residual profiles.

Remaining render gap: no per-ray radial profile browser yet, no full matrix glyphs, no seam/node-local tensor zoom, and no correction-branch decomposition at each individual crossing.

## Claim Ceiling

Local smoke reproduction only.

This run does not certify R5, `K_ij`, seam/node extraction, full GR compliance, or Atlas-native dynamics.

## Next Refinement

1. Preserve original imported script and local adapted script separately.
2. Add software environment details to the manifest.
3. Decide a lawful retention policy for sampled-point battery data before persisting every radial sample.
4. Run a ray-density / seam-threshold sweep.
5. Add render layers for eigenvectors, anisotropy, and R5 correction branch decomposition.
6. Promote only the output contract, not the scientific claim.
