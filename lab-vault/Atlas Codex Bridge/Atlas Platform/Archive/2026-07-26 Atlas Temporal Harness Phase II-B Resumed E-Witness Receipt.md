# Atlas Temporal Harness Phase II-B Resumed E-Witness Receipt

Date: 2026-07-26  
Work order: `ATLAS_TEMPORAL_HARNESS_PHASE_IIB_RESUME_EWITNESS_001`  
Result: **PASS — bounded canonical real electric-Weyl A/B engineering witness earned**

## Authorized scope

This work resumed only the previously stopped Phase-II-B canonical real
electric-Weyl extraction. It operated offline on the immutable Phase-II-A
Segment A and exact-child Segment B checkpoints. It did not launch Einstein
Toolkit, evolve a new state, implement magnetic Weyl curvature, construct a
complex Weyl operator, or promote a physical interpretation.

## Source and lineage closure

The raw HDF5, executable, and parameter identities matched the pre-computation
passport exactly. A is checkpoint `checkpoint_caa4034f09c15db8c3b0` at
iteration 2/time 0.5; B is its declared child
`checkpoint_c8a1abf27075fddcfba0` at iteration 4/time 1.0. Both contain 420
datasets on the same 29^3 level-0 grid, with three serialized ghost zones and
12,167 active cells.

The implemented evolved-slice v1 path ingests all six physical `gamma_ij`, six
`K_ij`, and six lower spatial `TMUNUBASE::T_ij` components at timelevel 0.
`S_ij=T_ij` was independently reconstructed from GRHydro primitives; the
maximum relative disagreement is below `1.1e-20`.

## Extraction and validation

The extractor computes coordinate-basis three-Ricci curvature with centered
second-order differences, canonical
`E_ij=C_{i alpha j beta}n^alpha n^beta` under
`atlas-3plus1-curvature-v1.0`, physical metric trace removal, metric-aware
norms, and generalized symmetric eigenpairs. Ghost cells and insufficient
stencils are masked.

The continuum Levi-Civita Ricci tensor is symmetric. The implementation retains
the raw finite-difference antisymmetric part as a diagnostic before applying
that exact mathematical identity. Its maximum relative size is 2.7206169% for
A and 2.7207110% for B against peak `||E||`, below the declared 5% extraction
bound. Emitted `E_ij` symmetry residual is zero. Maximum relative trace
residuals are `4.61e-15` (A) and `3.60e-15` (B). Every active value is finite.

Production-path validations pass: isotropic Schwarzschild sign and magnitude
(2.106% finite-difference magnitude error), static reduction, matter-term
inclusion, metric-norm cross-check, flat-space Ricci, schemas, source hashes,
lineage, segment gates, and A-to-B continuity. Harness tests pass 64/64 and
Temporal Pilot regressions pass 20/20.

## Witness summary

- A `||E||`: maximum `0.003794834906`, mean `0.001904031898`, RMS
  `0.002154824243`.
- B `||E||`: maximum `0.003793936769`, mean `0.001904129588`, RMS
  `0.002154798201`.
- A-to-B absolute norm difference: maximum `3.84422e-6`, mean `5.83827e-7`.
- Peak extraction RSS: 132,677,632 bytes. Observed swap was unchanged at
  215.44 MiB; no swap was created by the extraction.

The A-to-B difference is an engineering measurement only. Constraint H/M
summaries are numerical-health witnesses only. No source attribution,
convergence rate, uncertainty envelope, or physical-change claim is attached.

## Claim boundary and next gate

Earned claim: **canonical real electric-Weyl A/B engineering witness for the
two named immutable Phase-II-A checkpoints**.

Still held: general `B_ij`, complex Weyl, `weyl_gap` certification,
cross-resolution convergence, independent implementation agreement, production
envelope, causal attribution, and physical interpretation.

Recommended next action is a new, separately authorized Phase-II-B robustness
and independent/cross-resolution validation work order. It must not start
automatically and is not Phase II-C authorization.
