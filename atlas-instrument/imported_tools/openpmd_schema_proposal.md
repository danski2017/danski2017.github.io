# Atlas openPMD Schema Proposal

Status: schema-only dry run. No Atlas ledger or viewer data is rewritten.

Series layout: one Atlas run per openPMD series; one iteration per slice/time

## Mesh Candidates

- `rho`
- `abs_weyl`
- `ricci_trace`
- `hamiltonian_residual`
- `eigenvector_delta_angle`
- `delta_absWeyl`

## Record Candidates

- `source_catalog`
- `node_minus1_manifest`
- `footprint_masks`

## Promotion Rule

Hold as optional exporter until an Atlas schema is explicitly approved. Keep JSON/NPZ/bin as the working Pinch Lab format.

## Claim Boundary

does not export scientific data until a schema is approved
