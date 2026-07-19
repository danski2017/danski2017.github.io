---
type: evidence_register
status: active
created: 2026-05-13
topics:
  - wireframe
  - lumen-lattice
  - gfro
  - seam
  - scaffold
---

# Wireframe Building Evidence Register

This register tracks Atlas artifacts related to wireframe building, lattice release, seam persistence, truss/rib scaffolds, and bone extraction. The claim ladder matters: a wireframe candidate is not a certified physical wireframe.

## Current Claim Ladder

```text
visual datum demonstration
candidate scaffold
matched witness signal
resolution/persistence witness
multi-witness convergence
retention-certified scaffold
public-facing claim
```

Atlas has several strong candidate lanes, but no note here upgrades them into a physical lattice or final invariant.

## Released Lattice Lane

### Dynamic Released-Coordinate Lattice

Path:

`Relational_Labs/morse_smale_tidal_wireframe_v0_3_20260510T201236Z`

Status:

- sandbox milestone achieved,
- dynamic visual datum,
- lattice recomputed live from moving source positions,
- communicates volumetric datum response,
- not canonical wireframe.

Next gates:

- 128^3 stability,
- bias check,
- GFRO field-sieve baseline,
- separatrix/skeleton correspondence reports.

### EMS Lumen Lattice v0.1

Path:

`analysis/sandbox/lumen_lattice_benchmark_v0_1`

Status:

- first interactive EMS Lumen Lattice viewer opened successfully,
- Released Coherence Lattice object declared,
- Sun/Earth/Moon source roster visible,
- GFRO overlays included from the EMS source-context emitter,
- viewer controls and claim ceiling present.

Metrics:

| Metric | Value |
|---|---:|
| sources | 3 |
| lattice nodes | 729 |
| lattice edges | 1944 |
| GFRO overlay families | 10 |
| GFRO overlay points | 3088 |

Recommended v0.2:

- source labels,
- lattice density / edge stride toggle,
- GFRO family legend,
- local/global view presets,
- dimmer default lattice opacity.

### EMS-in-LSN Full-Riemann GFRO Lumen Microscope

Path:

`analysis/sandbox/ems_in_lsn_full_riemann_gfro_lumen_v0_1`

Status:

- sandbox microscope lane,
- Sun parent-bath closure scout passed,
- 24-source local stellar parent context declared,
- Lumen studied against GFRO taxonomy and tensor/eigen/Weyl witnesses.

GFRO taxonomy to preserve:

- zero sets,
- faces,
- seams,
- junctions,
- pockets,
- handoff supports,
- parent-context supports,
- low-margin regions,
- tensor/eigenframe handoff witnesses,
- wireframe scaffold candidates,
- beams/trusses/ribs,
- topology-change candidates.

## Source-Source Bone Lane

### Persistent SS Wireframe Bone Extraction v0.1

Path:

`codex_context/experiments/persistent_ss_wireframe_bone_extraction_v0_1_20260506T031513Z`

Status:

- strong SS bone signal,
- source-source K-family supports only,
- no source-context coupling used,
- toy scratch diagnostic,
- no visual/physical wireframe claim.

Metrics:

| Metric | Value |
|---|---:|
| candidate bones | 2054 |
| graph nodes | 4108 |
| graph continuity edges | 1452 |
| same-source-pair continuity edges | 1340 |
| corridor-like bones | 224 |
| patch/node-like bones | 819 |
| junction-like bones | 1011 |

Interpretation:

Persistent source-source K-family support can produce a graph-like scaffold. That scaffold is an extraction candidate, not an ontology claim.

### SS Bone Eigenstructure Witness Alignment v0.1

Path:

`codex_context/experiments/ss_bone_eigenstructure_witness_alignment_v0_1_20260506T033820Z`

Status:

- weak / artifact-likely signal against broad random-domain baseline.

Important correction:

This run was useful because it showed that naive random baselines are not enough. It motivated matched baselines instead of killing the whole lane.

### SS Bone Matched-Baseline Eigenstructure Witness v0.2

Path:

`codex_context/experiments/ss_bone_matched_baseline_eigenstructure_witness_v0_2_20260506T034432Z`

Status:

- strong matched eigenstructure witness signal.

Key result:

- source-pair-family matched nonbone SS baseline showed median span lift near `0.98483`,
- matched comparisons preserved stronger organization than broad random controls.

Interpretation:

The bone candidates appear to carry eigenstructure organization beyond several matched baseline conditions. This is meaningful for further wireframe work, but still below certification.

### SS Bone Resolution Stability Audit v0.1

Path:

`codex_context/experiments/ss_bone_resolution_stability_audit_v0_1_20260506T035116Z`

Status:

- partial resolution stability signal.

Resolution ladder:

| grid | bones | edges | same-pair edge fraction |
|---:|---:|---:|---:|
| 48 | 1558 | 1125 | 0.933333 |
| 56 | 2054 | 1452 | 0.922865 approx |
| 64 | 2440 | 1611 | 0.922408 |

Interpretation:

Counts grow with grid density, but the same-pair graph organization remains materially present. This supports continued testing.

## GFRO Seam / Scaffold Lane

### GFRO Arm32 Seam Persistence Audit v0.1

Path:

`codex_context/experiments/gfro_arm32_seam_persistence_audit_v0_1_20260510`

Status:

- geometry persistence witness only,
- not topology certification.

Headline:

| Comparison | Seam Capture | Seam p90 Nearest | Seam-Knot Capture | Seam-Knot p90 Nearest |
|---|---:|---:|---:|---:|
| grid 48 to 60 | 0.996 | 0.0927 | 1.000 | 0.1148 |
| grid 54 to 60 | 0.995 | 0.0927 | 0.957 | 0.1688 |

Interpretation:

Seam geometry persists under refinement by nearest-candidate capture even though raw counts change. Knot nodes are less stable, as expected for binned convergence witnesses.

## Doctrine

The wireframe lane should be built by convergence, not by taste:

```text
GFRO emits a scaffold candidate.
Node -1 records the registry.
Tensor/eigen/Weyl witnesses inspect it.
Lumen shows released datum response around it.
Resolution and matched baselines test persistence.
Retention decides whether it survives.
```

The lab should avoid calling any candidate a physical wireframe until it survives multi-witness retention.
