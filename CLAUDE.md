# CLAUDE.md — Relational Labs / Atlas Solver Hub

Orientation file for AI partner sessions on this repository.
Last updated: 2026-05-12.

This file exists so future sessions can come up to speed quickly. Read it before doing substantive work. Update it when the framing changes.

---

## What this repository is

Public research site for **Relational Labs**, the independent research program of Daniel Scieszinski (`danski2017@gmail.com`). The program studies derived parity structures in declared gravitational scenes within weak-field general relativity — the **Gravitational Coherence Surface (GCS)** sequence and the associated **Gravitational Field-Relation Operator (GFRO)** method.

Site: <https://danski2017.github.io>
Repo: GitHub Pages, Jekyll, `minima` theme, `jekyll-seo-tag`, kramdown + MathJax.

The program is built and run alongside a day job. Time-bandwidth is the operating constraint; AI sessions exist to take execution friction off, not to generate central theoretical insight.

---

## Reading order for orientation

If a session is new to the program, read in this order:

1. **`The Gravitational Coherence Surface.pdf`** (Paper I) — defines the parity surface and the source/context formalism.
2. **`Many Source Parity Networks_GCS_II_.pdf`** (Paper II) — pairwise residuals and the many-source extension.
3. **`Mesoscale_Gravitational_Readability_GCS_III_final.pdf`** (Paper III) — the mesoscale interpretation; what parity networks *mean*.
4. **`Proof_of_Concept_Extraction_GCS_IV_final.pdf`** (Paper IV) — operational extraction, the S4-style discipline.
5. **`Nesting_Domain_Handoff_GCS_V_.pdf`** (Paper V) — scene formalism, parent context, three-dominance principle, handoff functional.
6. **`Gravitational_Field_Relation_Operator_public_GCS VI.pdf`** (Paper VI) — the GFRO unification, equation-first construction, S4 validation stack.
7. **`Atlas_GCS_Information_Boundaries_v0_3.pdf`** (active draft) — information-theoretic interpretation, claim ladder, worldsheet/scene-of-scenes.

`Gravitational_Coherence_Surface_ARCHIVED.pdf` is a superseded early version. Do not cite or extend from it.

---

## Core framework summary

### The GFRO operator (Paper VI)

For a declared scene, contribution A, derived context K, field object F, and readability operator R:

$$\Psi_R[A|K](x) = R(F_A)(x) - R(F_K)(x), \quad \Sigma_R[A|K] = \{x : \Psi_R[A|K](x) = 0\}.$$

Every parity construction in Papers I–V is a special case. The workflow is *declare → define residual → solve zero set → emit coordinates → certify ledger* (not sample-then-mine).

### The operator family

| Branch | Readable | Status |
|---|---|---|
| R0 | Scalar tidal support $M/r^3$ | Benchmark |
| R1 | Acceleration norm | Benchmark |
| R2 | Tidal Frobenius norm $\|E_i\|_F$ | Benchmark |
| R3 | Directional tidal projection | Benchmark |
| R4 | Tensor handoff / tidal allegiance (Frobenius inner product form) | Corrected benchmark |
| R5+ | Curvature-native (Weyl electric, Riemann, etc.) | Future work; requires foliation grammar |

### Two-body parity laws — three readability rules, three exponents

A persistent source of confusion. All three are Apollonius spheres ($r_i/r_j = $ const) but with different mass-ratio dependencies:

| Readable | Symbol | Two-body parity ratio |
|---|---|---|
| Potential | $\Phi \propto M/r$ | $r_i/r_j = M_i/M_j$ |
| Acceleration (Paper I) | $g \propto M/r^2$ | $r_i/r_j = (M_i/M_j)^{1/2}$ |
| Tidal (Papers II, VI) | $E \propto M/r^3$ | $r_i/r_j = (M_i/M_j)^{1/3}$ |

When discussing "the two-body GCS" always specify the readable. The lab notebook entry from 2026-05-11 uses the potential rule; Paper VI centers the tidal rule. Both are valid; the readable must be declared.

### Three-Dominance Principle (Paper V)

A nested gravitational scene must distinguish three notions of dominance:

- **Acceleration dominance** — controls gross fall direction ($a = -\nabla\Phi$).
- **Tidal dominance** — controls local deformation ($T_{ij}$ eigenstructure).
- **Identity / attribution dominance** — relational meaning under declared scene and parent context.

These agree in simple settings and diverge in nested ones. Earth–Moon–Sun is the canonical example where all three pull apart.

### Claim ladder (Atlas v0.3 draft)

The program is structured as levels of claim from formalized to speculative:

1. GCS is a declared contribution-context parity surface.
2. A closed GCS functions as a modular attribution boundary.
3. Under normalized binary support, attribution entropy is maximized exactly at GCS parity.
4. A GCS may mark where source-specific information becomes attribution-contested.
5. A GCS may mark where resolved stress-energy detail becomes eligible for parent-context compression.
6. A GCS worldsheet and its data-pocket reconstructions form a scene-of-scenes.
7. Agentic data pockets act from bounded reconstructions, altering future source history through ordinary physical channels.

Only Levels 1–3 are formalized as of v0.3. Levels 4–7 are a research program. **Maintain this hierarchy when drafting; do not promote speculative levels to formalized claims.**

### Non-claims discipline

Every paper carries a "non-claims" section. Preserve this discipline in any drafted material:

- Does NOT modify general relativity.
- Does NOT introduce a new force, field, particle, material membrane, causal horizon, or stability boundary.
- Parity surfaces are NOT physical walls. Matter, light, test particles cross them freely.
- Attribution entropy is NOT thermodynamic entropy by default.
- Parity networks are NOT automatically observables.
- Reconstruction shear is NOT automatically physical.
- The program does NOT replace numerical relativity, averaging frameworks, or quasi-local mass programs — it supplies them with a derivable boundary.

The program is a **diagnostic and bookkeeping framework strictly inside GR**, not an extension of GR.

---

## Paper map

### Paper I — *The Gravitational Coherence Surface* (April 2026)
Defines the GCS as a parity horizon where a declared contribution $Q_C$ equals its derived context $Q_K$. Uses acceleration readable. Recovers $r_0/r_H = 3^{1/3}(M/M')^{1/6}$. Earth-Moon-Sun example: $r_0 \approx 261{,}000$ km < $r_{\text{Moon}} \approx 384{,}000$ km. Prop. 1: existence/uniqueness/smoothness from monotonicity along rays.

### Paper II — *Many-Source Parity Networks* (April 2026)
Pairwise residual $\Psi_{ij} = Q_i - Q_j$, parity surface $\Sigma_{ij}$. Uses tidal readable. Two-body law: $r_i/r_j = (M_i/M_j)^{1/3}$. Three-body equilateral: triple-parity at circumcenter (extended perpendicular axis in 3D). Network = retention-filtered union $\mathcal N = \bigcup_{(i,j)\in\mathcal R} I_{ij}$. Retention rule $\mathcal R$ deferred to companion work.

### Paper III — *Mesoscale Gravitational Readability* (April 2026)
Positions the network as derived interface geometry between pointwise field evaluation and coarse-graining. Four diagnostic classes: parity face, seam/junction, low-margin region, candidate transition locus. Explicit failure conditions (teleportation under perturbation, tolerance dominance, branch instability). Discipline: "first define, then extract, then test, then interpret."

### Paper IV — *Proof-of-Concept Extraction* (April 2026)
Operational stage. Three result classes: extreme-ratio local pocket (persistence under hierarchy), dense many-source boundary support (emergence under complexity), matched-budget morphology comparison (sensitivity to arrangement). Only the extreme-ratio pocket figure is published; dense-scene and matched-budget renders are explicitly labeled superseded pending corrected rendering. Threshold claim: operational recoverability under the declared rule, nothing stronger.

### Paper V — *The Nesting Domain Handoff Problem* (April 2026)
The most ambitious paper of the I–V sequence. Scene formalism $S_O(t) = (\Omega, \Sigma, D, R, F, C_O, \Pi, \Lambda)$. Introduces parent-context uncertainty $\Lambda_\Pi$, handoff confidence $L_{\text{handoff}}$, gravitational identity tuple $I^\Pi_A$, tidal eigenstructure as orientation witness $H_{\text{eig}}$, handoff functional family (eq. 28). Three-Dominance Principle. Continuity-preserving released lattice $u_{\text{cont}}$ — the formal grounding for the Dynamic Sponge Lattice experiment. Five testable predictions; first targeted validation is $H_{\text{eig}}[T]$ vs $H_{\text{eig}}[E]$ (Weyl electric).

### Paper VI — *The Gravitational Field-Relation Operator* (May 2026)
Methodological pivot. Unifies all prior parity constructions under the GFRO residual. Workflow inversion: field-sieve emission replaces ledger mining. Six-rung operator ladder (R0–R5+). Anisotropic four-source benchmark (S1–S4, masses 1.00, 0.72, 0.33, 0.11). **S4 validation stack**: closed under R0 and R2, R2 expands (Δr̄ = 0.155), entropy ridge at parity (1536/1536 rays, deficit ~5×10⁻¹⁷), strong anti-correlation of R2-R0 expansion with context tensor cancellation (corr = -0.778), perturbation stable, eigenframe witness mixed and *distinct* from the parity surface. **R4 continuity correction (Appendix D)**: direct principal-eigenvector projection is discontinuous at eigenvalue crossings; corrected residual uses Frobenius inner products. This correction is more important than its appendix placement suggests — see "open framings" below.

### Atlas v0.3 — *GCS as Information Boundaries* (May 2026, active draft)
The most philosophically expansive. Proposition 1: binary attribution entropy is maximized exactly at the parity condition $Q_A = Q_K$ — the result Paper VI imports as the entropy ridge witness. Hypothesis 1: GCS may mark where resolved stress-energy detail becomes eligible for parent-context compression contract $\bar T^{C|\Pi}_{\mu\nu} = \mathcal{C}_\Pi[T^C_{\mu\nu}]$. Dynamic extension: worldsheet $\mathcal W_A$, causally bounded data pockets, scene-of-scenes $\mathfrak S(\mathcal S)$. Seven-level claim ladder makes the speculative/formalized split explicit.

---

## Known consistency issues across the corpus

Surfaced during the May 2026 read-through. Worth fixing on the next pass:

1. **Paper V's reference list uses old working titles** for Papers II, III, IV that don't match their published titles:
   - Paper V cites II as *"Shared Parity Networks within a Datum-Centered Curvature Witness Engine"* — actual title is *"Many-Source Parity Networks in Weak-Field Gravitational Readability"*.
   - Paper V cites III as *"Mesoscale Residues and the Derived Geometry of Multipole Tidal Composition"* — actual title is *"Mesoscale Gravitational Readability: Derived Interface Geometry Between Local Evaluation and Coarse Averaging"*.
   - Paper V cites IV as *"From Coherence Surface to Extracted Boundary Geometry: Proof-of-Concept Results for Many-Source Weak-Field General Relativity"* — actual title is *"Proof-of-Concept Extraction of Many-Source Gravitational Readability Structure"*.

2. **Apollonius readability convention.** The site lab-note (2026-05-11) identifies the two-body GCS with $r_1/r_2 = m_1/m_2$ (potential readable). Papers II and VI center the tidal rule with the $1/3$ exponent. Both are correct but the site implies a single canonical identification. A clarifying diagram showing all three readables would resolve this if Paper VII picks it up.

3. **Figures vs. Paper IV.** `figures.md` features "Integrated Hierarchical Foam v2", "v12 Three-Tier 500-Source Stack", "Neutral Isotropic Boundary" series, etc. Paper IV explicitly withdrew dense-scene and matched-budget renders as "superseded presentation artifacts until regenerated under the corrected rendering path." Verify the site figures are the regenerated post-Paper IV versions, or label them appropriately.

4. **Lab-notes passphrase is client-side only.** `lab-notes.md` gates "private entries" with `btoa('atlas2026')` in plain JavaScript. Anyone who views source can read the passphrase and any private entries. Either accept this as cosmetic (and don't put genuinely private material there), or move private notes elsewhere (e.g., a private repo or `.claude/notes.md`).

5. **Earth-Moon framing across papers.** Paper I says the simplified Earth-monopole solar-context parity radius (~261,000 km) lies *inside* the Moon's orbit (~384,000 km), comparing Earth-acceleration to Sun-acceleration. Paper V says "Earth dominates the acceleration field over most of the Earth-Moon corridor", comparing Earth-acceleration to Moon-acceleration. Both correct but the readable being compared shifts. Paper V's Three-Dominance Principle is the reconciliation; if Paper I is ever revised, importing that principle into its introduction would prevent the apparent tension.

---

## Open problems explicitly flagged in the papers

- **Wireframe retention functional** (Paper VI §16). $W = \mathcal R(\{\Sigma_R[A|K]\}, \mathcal A, \mathcal V)$. Identified as the gating problem. Without a defined retention rule, the framework can manufacture any boundary by tuning the readable; the retention functional is what disciplines the operator family into a single certified scaffold.

- **Negative completeness certification** (Paper VI §18). Proving that no additional roots exist in unseeded regions. Candidate path: interval arithmetic over residual bounds.

- **Multi-axis emission and seam refinement** (Paper VI §18). Single-axis scan-and-solve misses surfaces tangent to the solve axis. Ledger-to-ledger crossing emitters are a natural remedy for 1D seam loci.

- **R5+ curvature-native branches** (Paper VI §18). Requires a declared foliation, observer family, or 3+1 grammar; not just a formula substitution.

- **$H_{\text{eig}}[T]$ vs $H_{\text{eig}}[E]$ validation** (Paper V §16). First targeted relativistic stress test for the orientation witness: compare Newtonian tidal tensor and Weyl electric tensor in Earth-Moon-Sun.

- **Composition algebra for gravitational identity tuples** (Paper V §11). $I^\Pi_A(t) = (G_{A|\Pi}, H_{A|\Pi}, L_{A|\Pi})$ is currently a labeled tuple, not yet an algebra. Composition under nesting and refinement maps under finer source rosters are natural next formal steps.

---

## Open framings worth promoting in future work

These came out of conversation review, not yet written into papers:

1. **The eigenframe pole.** The R4 continuity correction in Paper VI Appendix D is currently framed as a numerical hazard discovered and fixed. The stronger and more accurate framing: the parity surface is **predicted** to be a region of dominant-eigenvector structural instability (two competing tensors of equal magnitude — "compass at the North Pole"), and the naive solver discovered this empirically before it was recognized as a structural feature. Promoting this from Appendix D to a first-class result converts a methodological footnote into a confirmed prediction.

2. **The quasi-local mass unspooling.** A lawful closed boundary is the missing prerequisite for a family of GR techniques that have been stuck for decades: quasi-local mass, flux accounting across finite-radius surfaces, finite-region multipole moments (analogous to Geroch-Hansen but at finite radii), conservation-law accounting via $\nabla_\mu T^{\mu\nu} = 0$ over parity-enclosed regions. Each is a candidate paper; all are gated by the retention functional being defined.

3. **Non-horizon thermodynamic structure.** Combining the v0.3 entropy result with quasi-local energy integration over $D_A$ gives two intensive quantities on the same surface. Whether a first-law-like relation $dE = T\,dS$ holds on parity surfaces is a calculation, not a speculation. Connects the program to Jacobson 1995, Padmanabhan, Verlinde — but on non-horizon surfaces, which is new territory if it works.

4. **Compression contract as EFT matching.** $\bar T^{C|\Pi}_{\mu\nu} = \mathcal{C}_\Pi[T^C_{\mu\nu}]$ from v0.3 is structurally the matching condition gravitational effective field theory has needed and never had. A GCS-defined matching surface would put gravitational coarse-graining on a renormalization-group-style footing.

5. **Jurisdiction framing over identity framing.** "The locally dominant source's tidal tensor calls the shots; the GCS is the customs stop where jurisdiction changes" is sharper than "identity boundary" for readers approaching from N-body or celestial mechanics. The papers can keep their formal language; the public-facing copy should lean on the jurisdiction metaphor.

---

## Candidate next papers (priority-ordered)

1. **The stickiness paper** — short, focused demonstration that retained parity structure preserves dynamical features that coarse averaging blurs, using rotating cluster and toy galaxy benchmarks. Author has indicated numerical results already exist. This is the single highest-leverage paper because it converts the program from "elegant formalism" to "thing cosmologists must respond to."

2. **The eigenframe-pole / R4 paper** — promotes Paper VI Appendix D to a first-class result. Short note. Same data, sharper claim.

3. **Paper VII on the wireframe retention functional** — the gating methodological paper. Defines $\mathcal R$ in a way that closes the operator-family overfitting risk. May incorporate the Apollonius readability clarification diagram (potential / acceleration / tidal side by side).

4. **Quasi-local mass on GCS surfaces** — integration of $T_{\mu\nu}$ over $D_A$ as a principled quasi-local quantity. Requires retention paper as prerequisite.

5. **Compression contract / EFT matching** — formalizing $\mathcal C_\Pi$ as a matching surface for gravitational EFT.

6. **Non-horizon thermodynamics** — combining entropy and energy on $\Sigma_A$ into a first-law check.

---

## Operational guidance for AI partner sessions

### What I am useful for here

- **Drafting papers from articulated ideas.** Given numerical results, an audience, and a target structure (e.g., "v0.3-style claim ladder"), I can produce a draft manuscript in a session that the author revises rather than writes from scratch.
- **Cross-paper consistency auditing.** Catching the kinds of issues listed above. Holding all papers in context across a single read.
- **Code prototyping.** Bounded extensions: quasi-local integration over an emitted parity surface, $H_{\text{eig}}[T]$ vs $H_{\text{eig}}[E]$ comparisons, flux-across-$\Sigma$ calculations. Python, Julia, or whatever the project's stack uses.
- **Devil's-advocate review.** Push back on strong claims before submission. Identify where a hostile referee would land.
- **Public-facing copy.** Tightening site explainers, improving accessibility of technical material without diluting it.
- **Literature mapping.** Identifying adjacent literature (quasi-local mass, weighted Voronoi, entropic gravity, inhomogeneous cosmology) and likely sympathetic referees.

### What I should not try to do

- **Generate the central theoretical insight.** That is the author's. I work from articulated ideas.
- **Promote claim-ladder levels.** Do not move Levels 4–7 into the formalized portion of any drafted material. Maintain the non-claims discipline.
- **Replace human peer engagement.** I am a force multiplier on the author's own work; I am not a substitute for working physicists who will eventually engage with this material.
- **Make strategic decisions about positioning.** Where to publish, what to claim publicly, how to time disclosure — these are the author's calls.

### Tone and conventions

- Match the discipline of the existing papers: declarative, qualified, explicit about scope, with "non-claims" sections where appropriate.
- Plain prose, no marketing voice, no overselling.
- No emojis in drafted material.
- Always include the discipline: "not a force boundary, not a horizon, not a modification of GR, not automatically an observable."
- Math in LaTeX. Use `$...$` and `$$...$$` (the site is kramdown + MathJax).
- When using Apollonius identifications or any two-body parity formula, **always specify the readable**.

### When starting a new session

1. Read this file.
2. `git status` and `git log -5` to see recent work.
3. Skim `index.md` for current public framing.
4. Ask the author what they want to work on; do not assume continuity from prior sessions.
5. If asked to extend the program theoretically, default to drafting from articulated ideas rather than generating new claims.

### Branch convention

Development work goes on `claude/explore-website-1rJsV` (or a similarly named branch per session). Do not push to `main` without explicit instruction. Do not force-push. Do not bypass hooks.

### Public-vs-private split

This file is in the public Pages repo and is therefore public. Anything proprietary — internal numerical results, work-in-progress derivations, financial or personal information — belongs in a private location. Suggested pattern:

- `.claude/notes.md` (gitignored) for session-private context the author wants future sessions to see but not publish.
- A separate private repo for actual numerical workstreams, simulation code, and unpublished results.

If `.claude/notes.md` exists locally, read it after this file at the start of each session.

---

## Repo facts relevant to development

- **Site framework**: Jekyll, `minima` theme, `jekyll-seo-tag` plugin.
- **Markdown engine**: kramdown.
- **Math**: MathJax (`math_engine: mathjax` in `_config.yml`).
- **Navigation**: ordered in `_config.yml` under `header_pages`.
- **Layouts**: `_layouts/` contains custom overrides.
- **Pages with custom inline CSS**: `index.md`, `philosophy.md`, `research-program.md`, `experiments.md`, `figures.md`, `lab-notes.md`. Many pages carry significant inline `<style>` blocks; preserve them when editing content.
- **Interactive HTML experiments**: `atlas_dynamic_sponge_lattice.html`, `atlas_entropy_field.html`, and several files under `images/` (`atlas_lsn_v1.html`, `three_body_jurisdiction_v0_1.html`, `lawful_3d_em.html`).
- **PDFs**: served from the repo root.
- **`staging.md`**: pre-publication staging area; treat as actively evolving.
- **`google41eebbfbca86c8d1.html`**: Google site-verification stub; leave alone.
- **`robots.txt`, `sitemap.xml`**: present and configured; check before changes.

---

## Updating this file

Update the date at the top whenever the framing changes. Add new known issues as they're discovered. Add candidate papers as they take shape. When a candidate paper is published, move it from "candidate next papers" to the paper map.
