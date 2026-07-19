---
type: experiment_note
status: completed
created: 2026-05-15
topics:
  - gaia
  - gfro
  - local-stellar-ledger
  - tensor-scalar-transfer
  - certification
---

> SUPERSESSION NOTICE — 2026-05-16
>
> This note belongs to the GFRO-era doctrine layer.
> GFRO full-context field-emission framing has been demoted from default engine doctrine to historical candidate lineage.
> Current active internal candidate branch: BCW — Barycentric Compression Witnessing.
> Current bootloader: docs/bootloaders/ATLAS_BCW_ENGINE_BOOTLOADER_v0_1.txt
>
> Corrected rule:
> Pairwise parity drafts seams.
> BCW tests group-context compressibility.
> Datum Bible governs witness discipline.
> Ledger and validation decide retention.
>
> Preserve this note as historical lineage unless explicitly rewritten under BCW doctrine.

# G001H GFRO-Hardened Gaia Local Ledger

G001H rebuilds the Gaia 25 pc first-contact result under Atlas/GFRO discipline.

It uses the existing Gaia cache only. It declares every retained source, evaluates retained-vs-coarse relation maps over multi-resolution witness panels, audits softening and mass policy, emits a Node -1 diagnostic registry, and records retention certification.

## Package

- Experiment package: `codex_context/experiments/G001H_gfro_gaia_local_hardening`
- Report: `reports/G001H_REPORT.md`
- Source declaration ledger: `node_minus1/G001H_SOURCE_DECLARATION_LEDGER.csv`
- Emitted registry: `node_minus1/G001H_EMITTED_REGISTRY.csv`
- GFRO relation map summary: `derived/G001H_GFRO_RELATION_MAP_SUMMARY.csv`
- Audit aggregate: `derived/G001H_AUDIT_AGGREGATE.csv`
- Convergence audit: `derived/G001H_CONVERGENCE_AUDIT.csv`
- Certification: `certification/G001H_CERTIFICATION_DECISION.txt`

## Source Declaration

- Retained Gaia source proxies: `3894`
- Rejections: `{"missing_required": 6}`
- Location policy: Gaia DR3 cache astrometry after quality cuts.
- Mass policy: photometric proxy plus unit-mass and luminosity-weight controls; no official mass claim.
- Output size: about `2.4 MB`, below the `100 MB` cap.

## GFRO Audit Shape

| Audit Axis | Values |
|---|---|
| Witness panels | coarse, field_standard, field_fine |
| Mass policies | photometric_mass_proxy, unit_mass_control, g_luminosity_weight_proxy |
| Softening | 0.025 pc, 0.05 pc, 0.10 pc |
| Branch families | radial_shell_5pc, octant_radial_5pc, sky_sector_radial_5pc, local_cell_4pc |
| Relation-map rows | 108 |
| Emitted Node -1 rows | 96 |

## Result

- Positive `E/scalar > 1` rows: `81/108`
- High `E/scalar > 3` rows: `54/108`
- Baseline best split: `field_fine` + `local_cell_4pc`
- Baseline best p90 scalar delta: `0.511363`
- Baseline best p90 E delta: `4.10621`
- Baseline best p90 eigenframe disagreement: `0.843221`
- Baseline best p90 `E/scalar`: `8.02995`

## Independent Check

G001I independently reproduced the corrected G001H baseline comparison.

- [[G001I Independent Gaia Check]]
- Rows passing tolerance: `12/12`
- Tolerance: 2 percent relative p90 `E/scalar` plus sign match.

The independent check caught and corrected an important scalar-channel issue before the run was promoted: scalar acceleration must be vector-summed before taking the norm. The corrected result is more conservative and is now the authoritative G001H result.

## Atlas Read

The Gaia local signal survives the GFRO hardening audit as an internal control. Across the audited relation-map rows, electric-Weyl/eigenframe structure degrades more strongly than scalar field summaries under coarse source branches.

The sign of the tensor/scalar split is stable across the audit, but exact amplitudes remain branch- and witness-panel-sensitive. That is not a failure. It is the point of the lawful audit: scalar-only adequacy is not enough, and curvature-sensitive sampling must be declared.

## Certification Boundary

G001H is GFRO-hardened as an internal control.

It is not:

- public-certified,
- official Gaia mass-certified,
- a full Milky Way model,
- a dark-matter test,
- a public claim expansion.

## Next Lawful Gate

Do not jump to a bigger fast run.

Next acceptable step:

- approved Gaia DR3 mass-bearing local query with declared storage cap, official mass-quality flags, and selection-function ledger.
