---
type: platform_receipt
status: complete
created: 2026-07-21
run_id: EIGEN_GAP_FULL_DIAGNOSTIC_CONTRACT_001
---

# 2026-07-21 `eigen_gap_full` Diagnostic Contract Receipt

## Change

Harvested the Claude-wing note *eigen_gap_full: Definition, Identity, and
Petrov Reading* into the canonical local contract
[[../ATLAS Diagnostic Contract — eigen_gap_full]] and expanded the
[[../05 Dataset and Model Registry#`eigen_gap_full` Diagnostic Contract|Dataset and Model Registry]]
native scalar record.

## Source recovery

The exact generator chain was recovered without modifying it:

- `atlas_eij_extract.py::sorted_eigh` orders eigenvalues by descending
  absolute magnitude;
- `run_pinch_eigenfield_ledger_001.py::geometry_fields_complete` computes
  `(|lambda0| - |lambda1|) / (|lambda0| + 1e-30)` in that native order;
- the Gaia runner reuses the function;
- the Gaia exporter writes it as `eigen_gap_full`.

This closes the former exact-expression and approximately 3% residual debts.
The Claude approximation is retained as an observed reconstruction and is not
promoted as the exact formula.

## Verification

Float32 payload channels were upcast to float64 for read-only checks. Verified:

- `35,937 = 33^3` samples;
- trace-free ratio median `1.49e-8`, maximum `5.76e-8`;
- exact trace-free magnitude identity maximum relative deviation `5.76e-8`;
- candidate approximation correlation `0.997153`, median residual `0.0315`,
  maximum residual `0.0359`;
- footprint counts `267` raw high-angle, `89` low-gap exclusions, `178`
  survivors;
- diagnostic-bin counts `2,240 / 19,344 / 14,353`;
- smoke correlations reproduce at the reported precision.

The detailed machine-readable record is
`analysis/documentation_harvest/EIGEN_GAP_FULL_DIAGNOSTIC_CONTRACT_001/VERIFICATION_LEDGER.json`.

## Adjudicated corrections

1. The payload `lambda0..2` ordering is descending absolute magnitude, not
   algebraic ascending. The contract now uses separate payload and proof
   notation.
2. The underlying full-grid spacing is `3.0`; the stride-2 exported `33^3`
   payload spacing is `6.0` solver units. The local manifest does not license
   labeling those units as pc.
3. `F32-UNDERFLOW-001` was retained as the source-note protocol label, but no
   canonical local record was found and no link was fabricated.

## Claim boundary

Document status remains **Observed / Definitional**. Petrov language is limited
to the declared time-symmetric, purely electric slice. Diagnostic bins are not
universal classification thresholds. Low-gap points are directionally
ambiguous under the selection convention, not automatically numerical noise.
No GCS, parity, gravitational-identity, invariant-footprint, or universal
26-target claim was promoted. The G001P negative stands.

## Safety and preservation

No solver ran. No physical data were generated. No generator, viewer, website,
public clone, or unrelated doctrine was modified. No file was deleted. The
source scripts are currently untracked, so content hashes in the harvest packet
are used instead of falsely attributing them to repository HEAD.

