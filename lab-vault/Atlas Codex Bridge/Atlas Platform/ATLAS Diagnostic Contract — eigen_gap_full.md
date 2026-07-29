---
type: diagnostic_contract
source_wing: Claude
adjudicating_wing: GPT
status: Observed / Definitional
date: 2026-07-21
model: GAIA_LSN_PARENT_001
target: single_sun
topics:
  - electric-weyl
  - eigenframe
  - scalar-contract
  - diagnostic-stability
---

# ATLAS Diagnostic Contract — `eigen_gap_full`

## Contract in one sentence

`eigen_gap_full` reports how decisively the principal axis wins its own
selection.

It is a normalized principal-axis selection margin used to determine whether
the largest-magnitude principal eigenvector of the trace-free electric-Weyl
tensor is stable enough to interpret. It is a diagnostic witness, not a
physical source and not, by itself, a new physical observable.

## Provenance and source basis

This contract harvests the Claude-wing note *eigen_gap_full: Definition,
Identity, and Petrov Reading*, with GPT/Director adjudication and independent
local payload/source verification on 2026-07-21. No solver ran and no data were
generated.

- Model: `GAIA_LSN_PARENT_001`
- Target: `single_sun`
- Payload: `scalars.bin`, channel `eigen_gap_full`
- Sample count: `N = 35,937` on a `33 x 33 x 33` exported lattice
- Numeric handling for verification: float32 payload values upcast to float64
- Method in the source note: candidate-formula matching against the baked
  channel
- Canonical model record: [[05 Dataset and Model Registry#Gaia LSN Parent 001]]

### Adjudicated spacing correction

The Claude note declared “33³, spacing 3 pc.” The local artifact separates two
different spacings: the underlying full solve grid is `65^3` with `dx = 3.0`,
while the exported payload uses stride 2 and therefore has sample spacing
`6.0`. `positions.bin` confirms spacing `6.0` on every exported axis. The
manifest describes normalized solver coordinates, not parsecs, so this
contract does not relabel them as pc. The original declaration is retained
here as provenance; the verified artifact values govern the contract.

`F32-UNDERFLOW-001` is the protocol label cited by the source note for the
float32-to-float64 verification handling. No canonical local vault or repo
record with that name was located during this harvest, so no dangling vault
link is asserted.

## Ordering conventions

Convention note (2026-07-26): the trace-free R3 substrate is canonical
`electric_weyl_ij` under `atlas-3plus1-curvature-v1.0`. The stretch-positive
tidal acceleration operator is `-E_ij`. Because this contract orders by
absolute eigenvalue magnitude, a global `E -> -E` negates each value without
changing its payload slot; eigenvectors remain the same up to their arbitrary
vector sign and `eigen_gap_full` is unchanged. Signed physical labels are not
therefore inherited from the gap. See [[13 Curvature Convention Registry]].

The payload channel names `lambda0_full`, `lambda1_full`, and `lambda2_full` do
**not** use algebraic ascending order. The recovered generator applies
`np.linalg.eigh` and then reorders by descending absolute magnitude. To avoid
conflating conventions, this contract uses:

- payload/source notation: `mu_0, mu_1, mu_2`, with
  `|mu_0| >= |mu_1| >= |mu_2|`;
- proof notation: `lambda_min <= lambda_mid <= lambda_max`.

The reported principal eigenvector is the eigenvector associated with `mu_0`,
the largest-absolute-magnitude eigenvalue.

## Recovered exact generator contract

The exact source expression is recovered from
`scripts/et_tov3_scout/run_pinch_eigenfield_ledger_001.py`, function
`geometry_fields_complete`:

```python
abs_vals = np.abs(vals)
eigen_gap = (abs_vals[..., 0] - abs_vals[..., 1]) / (abs_vals[..., 0] + 1e-30)
```

Here `vals` has already been sorted by descending absolute magnitude in
`scripts/et_tov3_scout/atlas_eij_extract.py`, function `sorted_eigh`. The Gaia
runner reuses `geometry_fields_complete`, and
`scripts/et_tov3_scout/export_gaia_lsn_parent_viewer_001.py` serializes
`full_geom["eigen_gap"]` as `eigen_gap_full`.

Therefore, in payload notation,

`eigen_gap_full = (|mu_0| - |mu_1|) / (|mu_0| + 1e-30)`.

The `1e-30` term is a denominator guard. Recomputing from separately quantized
float32 eigenvalue channels differs from the separately quantized baked gap by
at most `1.06e-7`; that serialization-level difference is not evidence of a
different generator transform.

## Trace-free and purely electric lane

Payload verification gives:

- median `|tr E| / spread = 1.49e-8`;
- maximum `|tr E| / spread = 5.76e-8`.

Within the declared time-symmetric, purely electric slice, `B_ij = 0` and
algebraic speciality is characterized by the eigenvalue degeneracy structure
of `E_ij`. The baked `E_ij` eigenvalues therefore contain the information
required for Petrov-type discrimination in this lane, without constructing an
additional invariant channel.

This statement is restricted to the declared slice. It does not generalize to
nonzero `B_ij`, different observers, different foliations, or dynamical lanes
without separate verification.

## Exact trace-free identity

For a real symmetric trace-free `3 x 3` tensor in algebraic order,

`lambda_min + lambda_mid + lambda_max = 0`, and

`abs(abs(lambda_max) - abs(lambda_min)) = abs(lambda_mid)`.

Compact proof:

- If `lambda_mid >= 0`, then
  `|lambda_min| = lambda_mid + lambda_max`, hence
  `|lambda_min| - |lambda_max| = lambda_mid`.
- If `lambda_mid <= 0`, then
  `lambda_max = |lambda_min| + |lambda_mid|`, hence
  `|lambda_max| - |lambda_min| = |lambda_mid|`.

Taking the outer absolute value covers both cases. The payload maximum relative
deviation from this identity is `5.76e-8`.

In this trace-free lane, the dominant and runner-up absolute magnitudes are the
two algebraic extremes, so—apart from the explicit denominator guard—the exact
formula may also be written

`eigen_gap_full = |lambda_mid| / max(|lambda_min|, |lambda_max|)`.

## Claude-wing observed approximation

The original candidate reconstruction used algebraic ordering and found:

`eigen_gap_full ~= 1.5 |lambda_mid| / (lambda_max - lambda_min)`.

This remains an **OBSERVED APPROXIMATION**, not the generator formula.

- Correlation: `0.997153`
- Median absolute residual: `3.15e-2`
- Maximum absolute residual: `3.59e-2`
- Observed channel range: `[0.0001, 0.5000]` when rounded to four decimals

The recovered source closes the approximately 3% interior residual: the exact
channel normalizes by the dominant absolute eigenvalue, while the approximation
normalizes by `2/3` of the algebraic spread. They agree at the dead-heat and
twofold-degenerate endpoints but differ systematically in the interior. No
clipping or undocumented transform is required to explain the residual.

## Operational Interpretation

The two competitors for largest absolute magnitude are the eigenvectors of
`lambda_min` and `lambda_max`. For a trace-free tensor, their magnitude margin
is controlled by `|lambda_mid|`.

- Large gap: the selected principal direction is more robust against small
  perturbations.
- Small gap: the two candidate directions are nearly tied; the reported
  principal eigenvector can swing strongly under small numerical,
  registration, counterfactual, or observer changes.

The channel is a confidence/stability witness for principal-axis
interpretation. It does not establish that a high-gap direction is invariant
or that a low-gap signal is numerical noise.

## Footprint gate

The manifest definition is:

```text
eigen_gap_full >= 0.02
AND
eigenvector_delta_angle >= 0.05
```

For `single_sun`:

- raw points with `eigenvector_delta_angle >= 0.05`: `267`;
- raw high-angle points below the `0.02` gap floor: `89`;
- discarded fraction: `33.3%`;
- surviving footprint: `178` points;
- surviving grid fraction: `0.50%`.

On this target, one third of the raw high-angle points occur in a
low-selection-margin regime and are therefore excluded from directional
interpretation by the declared stability gate. The gate removes likely
frame-swing contamination; it does not prove the discarded signal is wholly
numerical.

The standing registry rule remains in force: eigenvector angle is
sign-invariant and must be conditioned on eigen-gap stability for
interpretation.

## Purely electric Petrov reading

The upper-endpoint payload exemplar is

```text
(-9.70232668e-06, 4.85116334e-06, 4.85116334e-06)
eigen_gap_full = 0.500000
```

This has the form `(-2a, a, a)`. Within this purely electric slice, the upper
endpoint `eigen_gap_full = 0.5` coincides with the canonical twofold-degenerate
`E_ij` eigenvalue structure associated with Petrov type D. This is not an
unrestricted biconditional for arbitrary spacetimes or observer
decompositions.

At the lower endpoint, `eigen_gap_full -> 0` implies
`lambda_mid -> 0` and `|lambda_max| -> |lambda_min|`: the principal-axis
dead-heat limit.

The following are diagnostic bins used in the source note, not universal
Petrov classification thresholds:

| Bin | Count | Fraction |
|---|---:|---:|
| Near type D, gap `>= 0.45` | 2,240 | 6.23% |
| Mid, gap `0.30–0.45` | 19,344 | 53.83% |
| Far from D, gap `< 0.30` | 14,353 | 39.94% |

## Exploratory Smoke-Pass Correlations

Single-target global linear correlations:

- `delta_angle x eigen_gap_full = -0.180`;
- `delta_angle x delta_absWeyl = +0.199`;
- `delta_angle x 1/r = -0.000`.

These are orientation-only smoke-pass values from one target. Field structure
may be local or nonlinear. The absence of a global linear `1/r` correlation on
this target argues against a simple proximity-only explanation at this level
of analysis; it does not prove independence from source proximity.

## Claim status and boundaries

Document ceiling: **Observed / Definitional**.

Licensed:

- the existence of the baked channel as an implemented registry fact;
- the payload formula match as Observed;
- the trace-free identity as established mathematically under its assumptions;
- the selection-margin interpretation as established under the declared
  trace-free selection convention;
- the single-target counts and correlations;
- the type-D endpoint reading within the declared purely electric lane.

Not licensed:

- a GCS, parity, or gravitational-identity claim;
- an invariant-footprint or physical-eigenvector-rotation claim;
- a claim that every discarded point is numerical artifact;
- treating the Claude approximation as the exact generator formula;
- an assertion that all 26 targets behave identically;
- extending the Petrov reading beyond the purely electric lane without audit.

**Diagnostics are witnesses, not sources.**

## Prior negative: G001P stands

[[../Experiments/G001P Gaia Parity-Delta Overlay]] tested a different
3,894-source, 25 pc scene and a different acceleration/top-two-contribution
parity proxy against Hill-style and Voronoi-like positional structures. Its
logged result was `boundary_sensitive_not_parity_specific`, with median
enrichments parity `0.870`, Hill-style `1.566`, and Voronoi `0.897`. It belongs
to a superseded GFRO-era formulation.

The G001P negative stands. This contract concerns a different scene,
diagnostic channel, and algebraic question; it neither overturns nor weakens
G001P.

## GA2 connection and sharpened forward question

Under [[../../Atlas Strategic Direction - External Tether and Grounding#GA2 — Observer / Foliation Bundle Audit|GA2 — Observer / Foliation Bundle Audit]],
`eigen_gap_full` is a natural conditioning channel. Apparent eigenframe motion
should be interpreted jointly with principal-axis stability so that
directional evolution is not confused with axis-selection ambiguity. The
channel itself is not asserted to be observer invariant; GA2 must test observer
choice, foliation, smooth transformation of the margin, and persistence of
high-gap directional features.

Falsifiable follow-on question:

> Does the counterfactual reorientation signal live preferentially at
> particular Petrov-algebraic structure, near type D or far from it, beyond
> what the existing stability gate already explains?

This can begin from baked channels without new solver work, as an extension of
the existing null-audit lane—not a rerun of G001P and not evidence that the
answer will be positive. First-pass comparisons may include footprint
enrichment by gap bin, gap-matched and amplitude-matched controls, conditional
angle distributions, and target-by-target reproduction across the 26-target
catalog.

## Owed work after source recovery

Source recovery has closed the former exact-expression, writer-path, and
interior-residual debts. Remaining owed items are:

1. confirm the trace-free identity and endpoint behavior across all 26 targets;
2. test regions/targets where numerical trace-free quality degrades;
3. run the separately passported baked-channel Petrov-structure null audit if
   adjudicated;
4. test observer and foliation dependence under GA2.
