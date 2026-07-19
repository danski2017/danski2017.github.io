---
type: experiment
series: P
id: P001
status: active
created: 2026-05-21
updated: 2026-05-22
owner: codex
tags:
  - periodic-parity
  - tier-2-5
  - Q-field
  - atoms
  - molecules
---

# P001 Atomic Periodic Parity

## Purpose

Build a periodic table of Q-field parity networks. Each tile is a deterministic point-cloud visualization showing where parity surfaces (Q_i = Q_j) form around declared classical atomic and molecular rosters.

## Tier

**2.5** — nucleons (protons + neutrons) and electrons as classical point sources. No quantum orbitals, no EM, no nuclear forces.

## Field

Q_i(x) = G × M_i / (r² + ε²)^(3/2), with softening ε = 0.001 × min source separation.

## Pipeline (5 steps)

1. **Roster** — declare sources on shell-pack nuclear geometry, electrons at atomic orbital radii
2. **Passport** — scene metadata, domain radius, validation gates
3. **Extraction** — three-stage omni-radial sampling (2048 Node 0 rays + 512 electron datum rays per electron + 256 nucleon datum rays per nucleon), bisection refinement
4. **Render** — self-contained HTML/Three.js WebGL with full control panel
5. **Manifest** — hashes, counts, validation status

## Workspace

`/Users/danski2017/Desktop/Claude/atomic_periodic_parity/`

```
atomic_periodic_parity/
├── scripts/
│   ├── generate_roster.py      # Source roster + molecule roster
│   ├── generate_passport.py    # Scene passport
│   ├── run_extraction.py       # Two-stage Q-field parity extraction
│   ├── run_render.py           # WebGL render generator v0.2
│   ├── run_full_tile.py        # Atomic tile orchestrator
│   ├── run_molecule_tile.py    # Molecule tile orchestrator
│   └── run_sensitivity.py     # Nuclear/electron radius perturbation
├── configs/
│   └── pipeline_config_v0_1.json
└── analysis/
    ├── rosters/    # Source roster JSONs
    ├── passports/  # Scene passport JSONs
    ├── ledgers/    # Certified crossing ledger CSVs
    ├── renders/    # Self-contained HTML tiles
    └── manifests/  # Run manifest JSONs
```

## Tile Inventory (2026-05-25, three-stage extraction)

**50 tiles total**, all gates PASS, all three-stage extraction + v0.3 render.

### Row 1–2 Atomic (Z=1–10, 12 tiles)

| Tile | Sources | Parity points | Nuclear geometry |
|------|---------|--------------|-----------------|
| H-1 | 3 | 520 | shell_pack |
| He-4 | 6 | 3,361 | shell_pack |
| Li-7 | 10 | 8,281 | shell_pack |
| Be-9 | 13 | 12,612 | shell_pack |
| B-11 | 16 | 15,345 | shell_pack |
| C-12 (α) | 18 | 14,524 | alpha_cluster |
| C-12 (sp) | 18 | 18,088 | shell_pack |
| N-14 | 21 | 18,961 | shell_pack |
| O-16 (α) | 24 | 22,406 | alpha_cluster |
| O-16 (sp) | 24 | 22,767 | shell_pack |
| F-19 | 28 | 27,109 | shell_pack |
| Ne-20 | 30 | 30,419 | shell_pack |

### Row 3 Atomic (Z=11–18, 8 tiles)

| Tile | Sources | Parity points | Nuclear geometry |
|------|---------|--------------|-----------------|
| Na-23 | 34 | 34,230 | shell_pack |
| Mg-24 | 36 | 36,877 | shell_pack |
| Al-27 | 40 | 41,478 | shell_pack |
| Si-28 | 42 | 45,435 | shell_pack |
| P-31 | 46 | 51,214 | shell_pack |
| S-32 | 48 | 53,726 | shell_pack |
| Cl-35 | 52 | 60,239 | shell_pack |
| Ar-40 | 58 | 70,694 | shell_pack |

### Row 4 Atomic (Z=19–36, 18 tiles)

| Tile | Sources | Parity points | Nuclear geometry |
|------|---------|--------------|-----------------|
| K-39 | 58 | 71,122 | shell_pack |
| Ca-40 | 60 | 73,685 | shell_pack |
| Sc-45 | 66 | 84,178 | shell_pack |
| Ti-48 | 70 | 91,279 | shell_pack |
| V-51 | 74 | 99,140 | shell_pack |
| Cr-52 | 76 | 103,168 | shell_pack |
| Mn-55 | 80 | 112,173 | shell_pack |
| Fe-56 | 82 | 115,129 | shell_pack |
| Co-59 | 86 | 122,608 | shell_pack |
| Ni-58 | 86 | 122,994 | shell_pack |
| Cu-63 | 92 | 135,392 | shell_pack |
| Zn-64 | 94 | 138,913 | shell_pack |
| Ga-69 | 100 | 150,676 | shell_pack |
| Ge-74 | 106 | 163,460 | shell_pack |
| As-75 | 108 | 168,259 | shell_pack |
| Se-80 | 114 | 182,353 | shell_pack |
| Br-79 | 114 | 182,313 | shell_pack |
| Kr-84 | 120 | 198,034 | shell_pack |

### Row 5 Atomic (Z=37–54, 10 of 18 tiles — halted at Z=46)

| Tile | Sources | Parity points | Nuclear geometry |
|------|---------|--------------|-----------------|
| Rb-85 | 124 | — | shell_pack |
| Sr-88 | 126 | — | shell_pack |
| Y-89 | 128 | — | shell_pack |
| Zr-90 | 132 | — | shell_pack |
| Nb-93 | 134 | — | shell_pack |
| Mo-98 | 140 | — | shell_pack |
| Tc-99 | — | — | pending |
| Ru-102 | 146 | — | shell_pack |
| Rh-103 | 148 | — | shell_pack |
| Pd–Xe | — | — | pending (resume Z=46) |

### Molecules (3 proof tiles)

| Tile | Sources | Parity points |
|------|---------|--------------|
| H₂ | 4 | 1,769 |
| H₂O | 28 | 28,192 |
| O₂ | 48 | 54,970 |

All completed tiles: full three-stage extraction (Node 0 + electron datums + nucleon datums), all gates PASS.

## Key Discoveries

1. **Electron datum rays (Stage 2)** resolve inter-electron parity pockets that Node 0 alone cannot see. Density boost ranges from 1.8× (Li) to 3.8× (F).

2. **Nucleon datum rays (Stage 3)** resolve inter-nucleon parity structure invisible from atom-scale origins. Boost ranges from 55% (Be) to 122% (O-16 alpha cluster). Alpha-cluster geometries benefit most — the separated nucleon clusters create rich internal parity networks.

## Validation Gates

- **Gate 1** (H only): analytical r_p/r_e ratio < 0.1% error
- **Gate 2** (He only): mass-ratio distance-ratio bisector check + sphericity ≥ 0.95
- **Gate 3** (all): Z protons + (A−Z) neutrons + Z electrons = total sources

## Render Controls (v0.3)

Electrons toggle, Parity points toggle, Color by source toggle (PP=red, NN/PN=grey, NE/EE=blue), Orbit rings toggle (ON by default), Opacity slider, Dot size slider (0.5–3px), Density (Full/Light), Pair-type filter (N–N / N–E / E–E), Auto-rotate (~30s/rev), GIF export (1280×960, 72 frames @ 8fps), Zoom to Nucleus, Individual nucleons toggle, collapsible info panel.

## Effects Lab (experimental, Si-28 sandbox)

File: `analysis/renders/atlas_parity_Si_28_experimental.html`

Kept effects (promoting to production TBD):
- **Bloom / Glow** — post-processing UnrealBloomPass, intensity/radius/threshold sliders
- **Slicing plane** — clip plane cross-sections, position slider + X/Y/Z axis cycle
- **Shell isolation** — show only parity points near a specific orbital shell, width slider
- **Jurisdiction volumes** — transparent spheres at each orbital radius + nuclear zone, opacity slider
- **Distance coloring** — heatmap by distance from nucleus, thermal/ocean/plasma palettes
- **Opacity falloff** — inner bright → outer faded, falloff power slider

Cut effects (no value): fog, size attenuation, reference grid.

## Claim Block (mandatory)

> Atlas Periodic Parity tiles are deterministic Q-readability diagnostics over declared classical point-source atomic rosters. They are not quantum orbital reconstructions, electromagnetic atomic models, nuclear force models, observables, or GR-native tidal claims.

## Open Threads

- [x] Three-stage nucleon datum re-extraction of all 15 tiles (2026-05-22)
- [x] Color by source toggle — PP red, NN/PN grey, NE/EE blue (2026-05-25)
- [x] Row 3 elements Na–Ar with 3s/3p orbital shells (2026-05-25)
- [ ] Website periodic table UI — clickable grid, loads self-contained HTML renders
- [ ] Phase 4 remaining molecules: CO₂, N₂, CH₄, NH₃, C₂H₅OH, caffeine
- [ ] Phase 5: Oxygen environment sensitivity plates (O₂, H₂O, CO₂, O₃)
- [x] Row 4 elements K–Kr (Z=19–36, 3d/4s/4p orbitals) (2026-05-25)
- [ ] Row 5 elements Rb–Xe (Z=37–54, resume from Z=46)
- [ ] Rows 6–7 elements Cs–Og (Z=55–118)
- [ ] Clip extraction at max orbital radius — reject void crossings beyond outermost shell
- [ ] Gravity bath — surround atom with copies at lattice spacing for inter-atomic parity context
- [ ] Effects Lab → production render promotion
- [ ] Future: Weyl tensor eigenfield rendering at atomic scale (parked)

## Related

- [[Architecture/Atlas Node Taxonomy for Simulations|Atlas Node Taxonomy]]
- [[Synthesis/Claim Boundaries|Claim Boundaries]]
