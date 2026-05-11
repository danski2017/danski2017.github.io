# New Session Brief — Atlas GCS Research Hub

## What this project is

You are continuing active research and web development for the **Atlas GCS Research Hub**
(`danski2017/danski2017.github.io`) — a Jekyll/GitHub Pages site publishing a program of
theoretical gravitational physics papers and interactive experiments. The framework is called
**Gravitational Coherence Surface (GCS)** theory — a weak-field general relativity framework
that defines precise geometric boundaries (parity surfaces) between gravitational source domains.

Working branch: `claude/explore-github-structure-qIhaA`
Site URL: https://danski2017.github.io

---

## Step 1: Orientate — read the papers

All seven GCS papers are in the repo root as PDFs. Read them before proposing or building anything.

```
/home/user/danski2017.github.io/The Gravitational Coherence Surface.pdf          ← GCS I (original)
/home/user/danski2017.github.io/Many Source Parity Networks_GCS_II_.pdf          ← GCS II
/home/user/danski2017.github.io/Mesoscale_Gravitational_Readability_GCS_III_final.pdf ← GCS III
/home/user/danski2017.github.io/Proof_of_Concept_Extraction_GCS_IV_final.pdf    ← GCS IV
/home/user/danski2017.github.io/Nesting_Domain_Handoff_GCS_V_.pdf               ← GCS V
/home/user/danski2017.github.io/Parity_Stack_and_Identity_Surface_GCS_VI_.pdf   ← GCS VI
/home/user/danski2017.github.io/Atlas_GCS_Information_Boundaries_v0_3.pdf       ← Information Boundaries
```

After reading, summarise the key ideas from each paper for the user before proposing next steps.
The user wants you to earn context the same way: read first, then think, then propose.

---

## Step 2: Review existing site and staging work

Key files to read:

- `experiments.md` — the live experiments page (Experiments I–IV active, V in staging)
- `staging.md` — the staging lab page; this is where pre-publication work lives
- `_config.yml` — site config and nav structure
- `atlas_entropy_field.html` — the Attribution Entropy Field interactive (Experiment V, staging)

---

## Step 3: What was accomplished in the previous session

### Experiment V — Attribution Entropy Field (COMPLETE, on staging)

Built a GPU-accelerated WebGL visualization (`atlas_entropy_field.html`) proving that the
attribution entropy ridge and the GCS parity surface are **algebraically identical** — not
approximately, but exactly. The connection:

- Attribution entropy: `S = −w ln w − (1−w) ln(1−w)`, where `w = Q_i / (Q_i + Q_Σ)`,
  `Q_i = M_i / r_i³`
- S is maximised at `w = 0.5`, which requires `Q_i = Q_Σ` — the exact GCS parity condition
- The entropy ridge *is* the parity surface, expressed in the language of information theory

Three modes: ATTR (per-source binary entropy), SCENE (global Shannon over all N sources,
arrangement sweep), ORBIT (two-body worldsheet animation). Full scientific report on staging page.

**What's novel:** The entropy framing gives parity surfaces a second definition — not "where
contributions are equal" but "where attribution is maximally uncertain." The SCENE mode makes
the full competition topology readable in one scalar field. Prior literature (Hosoya-Buchert-Morita
2004) applied Shannon entropy globally to matter distributions — not locally to tidal field
attribution. GCS fills that gap.

---

### Analysis I — HL Tau Disk Gap Prediction (COMPLETE, on staging)

Ran the GCS planet-planet parity surface framework against real ALMA protoplanetary disk data.
Using three planets inferred from HL Tau's major gaps (D1, D2, D5) via independent hydrodynamic
gap-width analysis:

- P1: a = 13.1 AU, M = 0.35 MJ
- P2: a = 33.0 AU, M = 0.17 MJ
- P3: a = 68.6 AU, M = 0.26 MJ (M★ = 0.55 M☉)

**Key formula — planet-planet parity radius (radial line):**
`r = (a_j + β·a_i) / (1 + β)`, where `β = (M_j / M_i)^(1/3)`

**Results (zero free parameters):**

| Gap  | Observed (AU) | GCS prediction (AU) | Δ (AU) | Status      |
|------|---------------|---------------------|--------|-------------|
| D3   | 42.3          | 42.22 (P1–P3)       | −0.08  | ★ Novel hit |
| D4   | 50.3          | 49.54 (P2–P3)       | −0.76  | ★ Novel hit |
| P1–P2 parity | — | 24.22             | —      | No gap found|

D3 and D4 are the two minor gaps with no agreed explanation in the standard literature.

**Hardening completed (six tests):**

1. Precision: ALMA Partnership 2015 Table 1 gives D3 = 42.3, D4 = 50.3 — tightens D3 to 0.08 AU
2. Mass uncertainty: 9/11 configurations within 4 AU — result robust
3. Azimuthal averaging: P2–P3 stable (+1.0 AU); P1–P3 shifts +6.3 AU — **primary open concern**
   — counter-argument: disk gap formation is resonance-driven (L1 Lagrange point analog),
   not time-averaged-field-driven; the radial-line formula may be the physically correct model;
   needs hydrodynamic disk simulation to adjudicate
4. Hill sphere clearance: P1–P2 locus has +7.2 AU clearance — Hill overlap hypothesis falsified;
   cause of P1–P2 non-match still unknown
5. HD 163296: P2–P3 parity at 63.7 AU vs ring at 67 AU (Δ = 3.3 AU); conditionally positive, weaker
6. DSHARP cross-system sweep (7 systems, 11 parity surfaces, 12 novel gaps): **only HL Tau produces
   hits**; no replication in AS 209, TW Hya, IM Lup, or HD 163296 within 3 AU; null model P(hit) ≈
   0.18 per system; pattern not yet established as systematic

**Honest status:** HL Tau is a compelling single-system result, not yet a confirmed pattern.
The most productive next target is AS 209, which has six observed substructures but an incomplete
planet census — better planet identification there could change the sweep result.

---

## Step 4: What is NOT yet done

The experiments page sidebar lists **"Experiment V — Recursive Domain Handoff"** as *forthcoming*
(nested parity domain geometry). This has not been built. It is the most natural next interactive
experiment based on GCS V (Nesting/Domain Handoff paper).

There is no Experiment VII or beyond yet. The previous session focused on entropy (ideas 6–8
from the paper survey). Ideas 1–5 are already live as Experiments I–IV.

---

## Step 5: What to do next

1. **Read all seven papers** (Step 1 above). Summarise each for the user.
2. **Propose the next experiment(s)** based on your reading. Prioritise ideas that:
   - Are not already covered by Experiments I–V
   - Are visually demonstrable as interactive WebGL/Three.js experiments
   - Have strong conceptual grounding in the papers
   - Connect to either the entropy thread (Experiment V) or the domain handoff thread (GCS V)
3. **Get user approval** before building anything.
4. When building, follow the existing code style: Three.js r128, ShaderMaterial for GPU compute,
   dark background, control panel overlay, standalone HTML files in the repo root or images/ folder.
5. Post completed work to `staging.md` with a full scientific report (see existing entries for format).

---

## Key GCS formulas for reference

```
Tidal proxy (R0 branch):     Q_i = M_i / r_i³
Parity condition:             Q_i = Q_Σ  (tidal attribution balanced)
Star-planet parity:           r_in  = a / (1 + q^(1/3))
                              r_out = a / (1 − q^(1/3))
  where q = M_planet / M_star
Planet-planet parity:         r = (a_j + β·a_i) / (1 + β)
  where β = (M_j / M_i)^(1/3)
Attribution entropy:          S = −w ln w − (1−w) ln(1−w)
  where w = Q_i / (Q_i + Q_Σ)
Scene entropy:                S_global = −Σ W_i ln W_i / ln N
  where W_i = Q_i / Σ Q_k
GCS half-width / Hill ratio:  3^(1/3) ≈ 1.442  (confirmed empirically at 1.45×)
```

---

## Site and branch notes

- **Do not push to main** — work on `claude/explore-github-structure-qIhaA`
- Jekyll/GitHub Pages; theme: minima; markdown: kramdown with MathJax
- Navigation defined in `_config.yml` under `header_pages`
- Staging page is at `/staging/` (file: `staging.md`) — always post new pre-publication work here
  with a full scientific report before it goes to the live experiments page
- The staging page links from the experiments page sidebar (amber notice box)
