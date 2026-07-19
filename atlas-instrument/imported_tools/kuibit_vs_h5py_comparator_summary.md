# Atlas ET HDF5 Comparator

Read-only audit comparing Atlas' h5py inventory path with the kuibit adapter availability envelope.

## Result

- ET HDF5 files: 10
- Observed ET variables: 26
- Iterations: [0]
- Refinement levels: [0]
- Dataset shapes: [[55, 105, 105]]
- Expected Atlas fields present: 26/26
- Expected Atlas fields missing: 0

## Recommendation

Promote kuibit to cross-check reader first, not primary reader yet. The current pass proves availability and pairs it with a full h5py field/stat inventory; the next gate is kuibit-native series extraction against the same fields.

## Carpet Risk

Carpet HDF5 dataset arrays are read as z,y,x by the existing Atlas reader; coordinate attrs often describe x,y,z. Treat origin/delta comparison as a required gate.

## Missing Expected Fields

- none

## Claim Boundary

read-only inventory; no Atlas ingestion behavior changed
