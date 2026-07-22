---
type: implementation_receipt
status: complete
run_id: ATLAS_TEMPORAL_PILOT_I_ET_ARCHIVE_001
date: 2026-07-19
---

# Atlas Temporal Pilot I / ET Archive Receipt

Atlas now ingests two genuine archived Einstein Toolkit 3D conformal-field
slices from Zenodo DOI `10.5281/zenodo.155394` through the existing local
ET_2025_05 environment. The selected coordinate times are 0 and
898.711912089024. The existing Atlas Instrument gained an isolated Temporal NR
lane with time/residual, region, refinement, horizon, puncture, provenance,
fidelity, and availability controls.

The adapter uses bounded HDF5 hyperslabs; no evolution or heavy local solve ran.
Five unit tests and fourteen integration checks passed, deterministic payload
reproduction passed, and browser QA showed zero console errors. Raw archive
members remain in the external ET data cache and are not browser dependencies.

The published subset does not contain full `gamma_ij`, full `K_ij`, shift,
constraints, or `E_ij`; none were reconstructed or implied. The registered
scalar residual is coordinate-dependent, interpolation-dependent, non-
invariant, and not gauge-free.

Canonical packet:
`analysis/atlas_temporal_pilot/ATLAS_TEMPORAL_PILOT_I_ET_ARCHIVE_001/`

Full implementation receipt:
`ATLAS_TEMPORAL_PILOT_I_ET_ARCHIVE_RECEIPT.md`

