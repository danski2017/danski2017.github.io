---
type: thread_boot
status: canonical
created: 2026-07-15
updated: 2026-07-19
tags:
  - atlas-platform
  - handoff
---

# New Thread Orientation

## Mission

Orient to the existing Atlas Platform and continue it in place. The current
instrument is **ATLAS Field Metric Viewer**, implemented at:

`/Users/danski2017/Desktop/Atlas_Solver_Project/analysis/et_tov3_scout/pinch_lab_viewer/index.html`

Do not design from memory and do not begin by building a new viewer.

## Required Boot Sequence

0. Read the vault-root notes: [[../../Atlas Mission Statement|Atlas
   Mission Statement]], [[../../Atlas Platform Dashboard|Atlas Platform
   Dashboard]] (Current Focus section first), and
   [[../../Lab Goals and Milestones|Lab Goals and Milestones]]. The
   vault root is the program's single jump-off point.
1. Read [[00 Atlas Platform Home]].
2. Read [[02 Architecture and Data Flow]].
3. Read [[03 Repo ET and Artifact Location Map]].
4. Read [[05 Dataset and Model Registry]] closely enough to distinguish ET truth
   substrates from Atlas-native diagnostic and toy scenes.
5. Read the newest entries in [[Evolution Log]].
6. Inspect the actual current viewer source, manifests, relevant generator
   scripts, and `git status` before proposing changes.
7. Read [[07 One-Model Redesign Blueprint]] — the governing design record
   (founder directives 1-9, phase history, base-model doctrine).
8. Read [[09 Findings Digest 2026-07-18]] — one-document catch-up on the
   commons era and the adjudicated claim register.
9. Read [[../Best Practices/Compute Safety and Remote Execution Policy|Compute Safety and Remote Execution Policy]] before running any model job.

## First Inspection Commands

Run from `/Users/danski2017/Desktop/Atlas_Solver_Project`:

```bash
pwd
git status --short
shasum -a 256 analysis/et_tov3_scout/pinch_lab_viewer/index.html
find analysis/et_tov3_scout/pinch_lab_viewer -maxdepth 2 -type f | sort
find scripts/et_tov3_scout -maxdepth 2 -type f | sort
find configs/et_tov3_scout -maxdepth 1 -type f | sort
tail -120 logs/et_tov3_scout_lab_log.txt
```

Inspect the separate ET tree without modifying it:

```bash
find /Users/danski2017/Desktop/EinsteinToolkit/Cactus -maxdepth 2 -type d | sort
shasum -a 256 \
  /Users/danski2017/Desktop/EinsteinToolkit/Cactus/exe/cactus_ATLAS_TOV3_SCOUT \
  /Users/danski2017/Desktop/EinsteinToolkit/Cactus/exe/cactus_ATLAS_TOV3_EVOLVE
```

## Current Scientific Boundary

- The viewer can compare full and source-removed field datasets, eigenvalues,
  eigenframe changes, proper tensor-delta witnesses, topology, and recovery
  controls.
- Its Gaia and StageB scenes are valuable custom constrained/static diagnostic
  substrates, not full multi-source numerical-relativity solutions.
- `ATLAS_TOV3_DIAG` is real ET HDF5, but the three TOV sources were combined by
  `TOV_Combine_Method="maximum"`; it is an ingestion and constraint diagnostic,
  not jointly solved binary or N-body initial data.
- The FUKA unequal-mass BNS bridge has validated isolated components and produced
  a binary seed, but no coupled Newton step converged. It is not yet a fused BNS
  result.
- Pointwise nonzero tails do not establish a finite physical boundary. Candidate
  footprint surfaces are tolerance-, grid-, context-, and sampling-dependent.

## Development Contract

- Continue one instrument. Extend by modular controls, panels, adapters, and
  versioned datasets.
- Do not remove or silently alter existing controls while adding a feature.
- Do not overwrite source datasets, manifests, trackers, logs, or evidence.
- Preserve raw-to-derived provenance and explicit claim boundaries.
- Run syntax, manifest, dataset, and browser QA after UI changes.
- Use screenshots at desktop and mobile sizes for layout-sensitive changes.
- New ET substrate promotion order is matter, constraints, ADM/Hydro fields,
  derived curvature, then identity diagnostics. No parity or foam overlay before
  constraint residuals are visible.
- Never assume a sandbox is remote compute. Positively identify the host and RAM.

## Pasteable Goal Prefix

Use this at the beginning of future Atlas Platform goals:

> Work inside the existing Atlas Platform, whose canonical implementation is
> `analysis/et_tov3_scout/pinch_lab_viewer/index.html`. First read the complete
> Obsidian orientation under `Atlas Codex Bridge/Atlas Platform/`, beginning with
> `00 Atlas Platform Home.md`, then inspect the live repo and manifests. Continue
> the existing viewer in place; do not create a replacement. Preserve current
> behavior and add major functions through isolated, toggleable modules. Respect
> numerical provenance, append-only logs, the ET/Atlas split, and the compute
> safety policy. Do not touch `codex_context` unless explicitly instructed.

## Handoff Completion Test (updated 2026-07-19)

A newly oriented thread should be able to answer, before editing:

- Where is the viewer code and how is it served?
- Which FIVE panel lanes exist (Atlas Native, Imported Tools, Recovery
  Lab, BL Foam, Temporal NR), and which Layer Stack sections live in the BL lane
  (eigen, network, Commons Layers, Dynamic Witnesses)?
- Which datasets are selectable and what are their claim ceilings —
  including COMMONS_ATLAS_001, MAGNETIC_WEYL_001/002, and the archived
  `ATLAS_TEMPORAL_PILOT_I_ET_ARCHIVE_001` temporal substrate?
- Which scripts regenerate each payload, and why must claim-wording
  fixes land in the bake SCRIPT rather than the output manifest?
- What did the GPT-wing adjudications of 2026-07-18 promote, what did
  they demote, and what boundary applies below H = 0.85?
- Which trough is the canary, and why does its four-axis failure
  record strengthen the eight survivors?
- What does the Lambda_Pi footer on every promoted claim mean?
- What is kappa in the magnetic-Weyl lane, how was it locked, and
  which sign question remains for odd-in-E witnesses? (Answer: -2;
  OBS_042 numeric Riemann crosscheck; resolved by the ratified E-sign
  map — Atlas E = stretch-positive = -C_i0j0.)
- Where does Einstein Toolkit enter the pipeline?
- Which genuine evolved ET fields are present in Temporal Pilot I, which full
  Cauchy/constraint/curvature fields are absent, and why is the registered
  residual not gauge-free?
- What did the FUKA BNS resource stop prove and not prove?
- Which changes require evolution-log and archive receipts, and which
  orientation docs must be synchronized when behavior or paths change?

If any answer is unclear, orientation is not complete.
