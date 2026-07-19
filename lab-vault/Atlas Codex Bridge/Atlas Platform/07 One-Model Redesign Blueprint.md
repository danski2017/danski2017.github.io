---
type: design_blueprint
status: active
created: 2026-07-15
updated: 2026-07-15
tags:
  - atlas-platform
  - redesign
  - one-model
---

# One-Model Redesign Blueprint

Founder directives, 2026-07-15 session (Claude wing recording). This blueprint
governs the refinement arc; every phase ships with a backup, a receipt, and a
revert path. **We always step forward safely.**

## Founder Directives (recorded)

1. **Safe stepping.** Every change revertible: pre-change backup + receipt +
   isolated/toggleable implementation. If something breaks, we roll back.
2. **One model.** The instrument renders ONE canonical model; all panels
   interface that one model rather than owning parallel worlds.
   - **Founder clarification (2026-07-15, corrects an earlier typo):** Atlas
     Native and imported third-party tools STAY DISTINCT at the interface
     level — we must always know which modeling tools we built and which we
     didn't. However, all outputs (native and imported alike) become
     composable LAYERS on the one model: any combination may be overlaid
     freely, including messy ones, because valuable observation combinations
     cannot be known without seeing them overlaid. Provenance distinction is
     visual and organizational (grouping, tagging, badge), never a barrier to
     composition.
3. **Modeling standards aligned.** Omni-radial-from-sources sampling is the
   house standard. Founder rationale: chaotic crossing dots track visually
   better than cartesian grids, whose alignment causes visual "feedback"
   (aliasing/moire). Cartesian remains available, not default.
4. **GPT-wing work is outstanding but unfinished in places.** Audit every
   control; fix, finish, or fold. Controls that don't earn their keep get
   folded into presets rather than deleted (history preserved).
5. **Intuitive first.** Easy toggling and cycling through ablation scenes and
   delta scenes. The wink feature is a crown jewel — refine it until it
   shines, and generalize it as the universal A/B scrubber grammar.
6. **Base model: the LSN-66 BL cross-term-aware scene** (founder refinement,
   2026-07-15 evening). The BL-method timeslice is the gold standard for this
   instrument. Canonical workflow: solve the fused BL cross-term-aware full
   scene once; solve every ablation iteration as its own re-solve (DEN A
   discipline — ablations are never subtractions of a cached field, they are
   re-solved scenes); freeze all of it; then every tool in the instrument
   toggles as a layer onto that one base. StageB and Family S remain
   selectable substrates, but LSN-66 BL is the base model across all viewers.
   Consequence for the roadmap: native eigen-tools (eigenvectors, eigen-gap,
   orientation deltas, footprints) should eventually be baked FROM the BL
   substrate so the same solve feeds every layer.
7. **Freeze-in-time.** All model arrangements render once, then are frozen:
   no compute waits while driving knobs/sliders/toggles. Precompute or bake;
   live compute only where continuous sliders demand it (interior shell lab).
8. **Earns-its-keep rule.** Be deliberate about what loads by default. Every
   default preload and every visible knob must justify its cost — either it
   appears in a filed lab note within a sprint or it folds into a preset.

9. **Paper-integration doctrine (founder, 2026-07-16).** The revised GCS/GFRO/
   Nesting papers (July 2026) are integrated as ADDITIVE capability. Nothing
   is removed — the eigen-vector ablation studies continue. GFRO
   direct-emission is a shortcut that trades the richness of a fully solved
   field for the parity network alone; therefore **dense fully-solved fields
   remain the law and GFRO-style emission is a setting, never the default.**
   Preferred imports: dominance cells / margins / parity faces / attribution
   entropy over registered per-source amplitudes (GFRO Eq. 16-18, Nesting
   Eq. 10); continuous tensor-allegiance witnesses alongside (not instead of)
   gap-gated eigen displays (GFRO Principle 1, Nesting Principle 2);
   GFRO Table-3 ledger fields in payload manifests; Nesting Appendix-B scene
   passport (parent context Pi and uncertainty Lambda_Pi declared).

## Target Architecture

```
bake pipeline (scripts/, offline, versioned)
   -> frozen arrangement payloads (manifest + typed arrays, like existing datasets)
      -> ONE scene registry in the viewer (canonical model + arrangements)
         -> ONE render world + camera
            -> panels = views/lenses on the model:
               fields / ablation / parity foam / recovery / advisory (imported)
```

- **Scene registry:** every "arrangement" (full scene, each ablation, each
  denominator/witness variant) is a named, versioned, precomputed state.
  Cycling arrangements is a buffer swap, never a solve.
- **Bake pipeline:** BL foam extractions and eigen-footprint layers get
  generated offline into dataset payloads (certified march, all configs).
  The browser fetches and renders; it does not compute by default.
- **Live-compute island:** the interior parity shell lab keeps real-time
  kernels (continuous D/mu_n sliders; ~80 ms/update is acceptable).
- **Passport ribbon:** persistent strip declaring substrate, witness, norm,
  march quality, and claim ceiling for whatever the one model currently shows.
- **Universal A/B scrubber:** one wink component drives full<->removed,
  DEN A<->DEN B, baseline<->realization, lambda-continuation. One interaction
  grammar everywhere.

## Phases (each independently shippable + revertible)

- **Phase 0 — Knob audit.** Exercise every control in every lane; catalog
  works / broken / unfinished / unclear. No code changes. Output: audit table
  in this folder + fix list.
- **Phase 1 — Standards alignment.** Omni-radial default sampling; wink
  polish (cycle buttons for ablation/delta scenes, keyboard arrows); dead or
  duplicate knobs folded into presets. Small receipts each.
- **Phase 2 — Freeze-in-time.** Bake pipeline for LSN-66 arrangements
  (foam + eigen layers, certified march); scene registry; instant cycling.
- **Phase 3 — One-model shell.** Single world/camera; panels become lenses;
  a unified LAYER STACK where every native and imported output is an
  independently toggleable layer on the one model — grouped and badged by
  provenance (Atlas Native / Imported-Advisory), freely composable in any
  combination; passport ribbon reflects the composed stack.
- **Phase 4 — Convention tier.** ||.||_gamma-ref norm toggle and A2 comparison
  bundle surfaced in-instrument.
- **Phase 5 — GFRO emission lane (galaxy readiness).** Prototype a
  continuation/Newton zero-set extractor (E_ij parity residual on the BL
  fused cross-term-aware scene) and CERTIFY it against the baked dense-march
  ground truth (coverage, missed components, pinch behavior, closure census).
  Emission remains a setting, never the default (directive 9); its purpose is
  scales where dense marching is unaffordable (galaxy-class scenes, group
  ablation per the Nesting paper). Trust is earned on LSN-66 first.

## Revert Contract

Every phase: `backups/atlas_platform/index_pre_<phase>_<date>.html` (or module
directory copy once split), receipt in Archive, Evolution Log entry, and a
one-command rollback documented in the receipt.
