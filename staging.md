---
layout: default
title: Staging Lab
description: Pre-publication experiment results from Atlas GCS Research — preliminary, not peer reviewed.
---

<style>
/* ── banner ── */
.stg-banner {
  background: #fffbe6;
  border: 1px solid #e6c84a;
  border-radius: 8px;
  padding: 14px 18px;
  margin-bottom: 32px;
  font-size: 0.84rem;
  color: #5a4a00;
  line-height: 1.55;
}
.stg-banner strong { color: #3a3000; }

/* ── section heading ── */
.stg-section-head {
  font-size: 0.72rem;
  font-weight: bold;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: #aaa;
  margin-bottom: 28px;
  padding-bottom: 8px;
  border-bottom: 1px solid #eee;
}

/* ── entry block ── */
.stg-entry {
  display: flex;
  gap: 32px;
  align-items: flex-start;
  margin-bottom: 56px;
  padding-bottom: 56px;
  border-bottom: 1px solid #eee;
}
.stg-entry:last-child {
  border-bottom: none;
  margin-bottom: 0;
  padding-bottom: 0;
}

/* ── left: card column ── */
.stg-card-col {
  flex: 0 0 260px;
  width: 260px;
}
.stg-card {
  border: 1px solid #e4e4e4;
  border-radius: 10px;
  overflow: hidden;
  background: #fff;
}
.stg-card-thumb {
  width: 100%;
  height: 130px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.60rem;
  letter-spacing: 0.18em;
  text-transform: uppercase;
}
.stg-thumb-entropy {
  background: linear-gradient(135deg, #000011 0%, #1a0040 38%, #7a0066 72%, #ff8800 92%);
  color: rgba(255,215,0,0.55);
}
.stg-card-body { padding: 13px 15px 15px; }
.stg-card-meta {
  display: flex;
  align-items: center;
  gap: 7px;
  margin-bottom: 6px;
  flex-wrap: wrap;
}
.stg-card-num {
  font-size: 0.65rem;
  color: #bbb;
  text-transform: uppercase;
  letter-spacing: 0.08em;
}
.stg-badge {
  font-size: 0.60rem;
  font-weight: bold;
  letter-spacing: 0.07em;
  text-transform: uppercase;
  padding: 2px 6px;
  border-radius: 4px;
}
.stg-badge-staging {
  background: #fff4cc;
  color: #8a6d00;
  border: 1px solid #e6c84a;
}
.stg-card-title {
  font-size: 0.88rem;
  font-weight: bold;
  color: #222;
  margin-bottom: 4px;
  line-height: 1.3;
}
.stg-card-date {
  font-size: 0.68rem;
  color: #ccc;
  margin-bottom: 10px;
}
.stg-card-open {
  display: inline-block;
  font-size: 0.76rem;
  font-weight: bold;
  color: #3366cc;
  text-decoration: none;
  margin-bottom: 12px;
}
.stg-card-open:hover { text-decoration: underline; }
.stg-modes {
  padding-top: 10px;
  border-top: 1px solid #f2f2f2;
}
.stg-modes-label {
  font-size: 0.63rem;
  color: #ccc;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  margin-bottom: 5px;
}
.stg-mode-list {
  font-size: 0.74rem;
  color: #777;
  line-height: 1.6;
}

/* ── right: report column ── */
.stg-report-col {
  flex: 1;
  min-width: 0;
}
.stg-outcome {
  font-size: 1.02rem;
  font-weight: bold;
  color: #111;
  line-height: 1.45;
  margin-bottom: 22px;
  padding-bottom: 18px;
  border-bottom: 1px solid #f0f0f0;
}
.stg-report-section {
  margin-bottom: 18px;
}
.stg-report-label {
  font-size: 0.66rem;
  font-weight: bold;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: #bbb;
  margin-bottom: 6px;
}
.stg-report-body {
  font-size: 0.87rem;
  color: #444;
  line-height: 1.62;
}
.stg-report-body p { margin: 0 0 10px; }
.stg-report-body p:last-child { margin-bottom: 0; }
.stg-report-body strong { color: #222; }
.stg-report-body em { color: #666; }

/* ── limits notice ── */
.stg-limits {
  margin-top: 20px;
  padding: 11px 14px;
  background: #fafafa;
  border-left: 3px solid #e0e0e0;
  border-radius: 0 6px 6px 0;
  font-size: 0.80rem;
  color: #888;
  line-height: 1.55;
}
.stg-limits strong { color: #666; }

/* ── footer note ── */
.stg-footer-note {
  font-size: 0.80rem;
  color: #aaa;
  line-height: 1.6;
  margin-top: 40px;
  padding-top: 20px;
  border-top: 1px solid #eee;
}

/* ── responsive ── */
@media (max-width: 700px) {
  .stg-entry { flex-direction: column; gap: 24px; }
  .stg-card-col { flex: none; width: 100%; }
}
</style>

# Staging Lab

<div class="stg-banner">
  <strong>Pre-publication notice.</strong> Experiments on this page are preliminary results from active Atlas research. They have not undergone formal peer review and may change substantially before publication. Links are provided so collaborators and interested readers can inspect the work directly. Interpret conservatively.
</div>

<div class="stg-section-head">Staging — {{ site.time | date: "%B %Y" }}</div>

<!-- ═══════════════════════════════════════════════════
     ENTRY: Attribution Entropy Field
════════════════════════════════════════════════════ -->
<div class="stg-entry">

<div class="stg-card-col">
  <div class="stg-card">
    <div class="stg-card-thumb stg-thumb-entropy">entropy ridge · GCS</div>
    <div class="stg-card-body">
      <div class="stg-card-meta">
        <span class="stg-card-num">Experiment V</span>
        <span class="stg-badge stg-badge-staging">Staging</span>
      </div>
      <div class="stg-card-title">Attribution Entropy Field</div>
      <div class="stg-card-date">Posted May 2026</div>
      <a class="stg-card-open" href="/atlas_entropy_field.html" target="_blank" rel="noopener">Open Experiment &nearr;</a>
      <div class="stg-modes">
        <div class="stg-modes-label">Modes</div>
        <div class="stg-mode-list">
          <strong>ATTR</strong> — per-source binary entropy; select focal source, drag to reshape.<br>
          <strong>SCENE</strong> — global Shannon entropy; full parity network + arrangement sweep.<br>
          <strong>ORBIT</strong> — two-source orbit; ridge sweeps out GCS worldsheet.
        </div>
      </div>
    </div>
  </div>
</div>

<div class="stg-report-col">

  <div class="stg-outcome">The bright ridge in the entropy field and the GCS parity surface are the same object — not approximately, but algebraically identical — and we can now render that identity in real time.</div>

  <div class="stg-report-section">
    <div class="stg-report-label">Why it works mathematically</div>
    <div class="stg-report-body">
      <p>Attribution entropy is S&nbsp;=&nbsp;−w&thinsp;ln&thinsp;w&nbsp;−&nbsp;(1−w)&thinsp;ln(1−w), where w&nbsp;=&nbsp;Q<sub>i</sub>/(Q<sub>i</sub>&nbsp;+&nbsp;Q<sub>Σ</sub>) is the fraction of tidal contribution from the focal source, and Q<sub>i</sub>&nbsp;=&nbsp;M<sub>i</sub>/r<sub>i</sub>³. Binary entropy is maximized exactly at w&nbsp;=&nbsp;0.5 — which is exactly the condition Q<sub>i</sub>&nbsp;=&nbsp;Q<sub>Σ</sub> — which is exactly the GCS parity condition. The ridge of the entropy field <em>is</em> the parity surface, expressed in a different mathematical language.</p>
      <p>This matters beyond the surface itself. The entropy field is smooth and continuous everywhere in space. Its gradient points toward the parity surface from any point in the scene. In SCENE mode, a single Shannon entropy field over all N sources encodes the full parity network simultaneously — every ridge is a pairwise parity surface, and the competition topology of the whole scene becomes readable in one scalar function.</p>
    </div>
  </div>

  <div class="stg-report-section">
    <div class="stg-report-label">What is novel</div>
    <div class="stg-report-body">
      <p>The GCS papers defined the parity surface as the zero-set of a comparison field Ψ&nbsp;=&nbsp;Q<sub>i</sub>&nbsp;−&nbsp;Q<sub>Σ</sub> — a geometric condition, find where the difference is zero. The entropy framing replaces that with a maximization problem on a smooth scalar field that exists everywhere, not just on the surface. The gradient structure gives a continuous measure of "distance from parity" without explicitly solving for the zero-set.</p>
      <p>The SCENE mode arrangement sweep is also new as an operational result. Paper IV demonstrated matched-budget morphology sensitivity at three discrete configurations. The ARRANGEMENT slider makes this continuous across the full interpolation from symmetric square to benchmark lopsided configuration, converting a proof-of-concept into a parameter-space result.</p>
    </div>
  </div>

  <div class="stg-report-section">
    <div class="stg-report-label">What is not novel</div>
    <div class="stg-report-body">
      <p>Shannon entropy applied to weight distributions is 1948. Voronoi-like competition zones in multi-source fields are standard in computational geometry. The Apollonius sphere (the two-body parity surface under the R0 branch) is ancient. Tidal field hierarchy analysis appears in cosmological large-scale structure classification methods — T-web, V-web, and related frameworks. None of these are being displaced.</p>
    </div>
  </div>

  <div class="stg-report-section">
    <div class="stg-report-label">Why the community might care</div>
    <div class="stg-report-body">
      <p><strong>For the GCS program:</strong> The entropy framing gives the parity surface a second definition — not "where contributions are equal" but "where attribution is maximally uncertain." Those are the same locus, but they say different things. A surface of geometric balance is also a surface of maximal epistemic ambiguity about which source owns the point. The Information Boundaries paper develops this philosophically; this experiment makes it visually literal.</p>
      <p><strong>For gravitational physics:</strong> Methods for identifying mesoscale structure in N-body simulations rely on density thresholds, Voronoi tessellation, or velocity-field topology — none tied to actual pairwise tidal contributions. The scene entropy field produces mesoscale boundary structure from the physics directly, without imposed tessellation. Whether it adds diagnostic value beyond existing methods is an open question, but it is a structurally different kind of object.</p>
    </div>
  </div>

  <div class="stg-limits">
    <strong>Scope limits.</strong> This experiment operates within the declared R0 weak-field branch (Q&nbsp;=&nbsp;M/r³), a scalar tidal proxy. Structures are branch-dependent — a different readable operator may produce different geometry. The visualization is a 2D slice of a 3D field. No physical observables are claimed. The value is demonstrating the entropy–parity identity concretely and showing it responds continuously to source arrangement. The case for broader relevance must be earned through the benchmark hardening work described in Paper IV.
  </div>

</div>
</div>

<div class="stg-footer-note">
  Staging experiments use the four-source benchmark masses M₁=1.00, M₂=0.72, M₃=0.33, M₄=0.11 established in the Atlas proof-of-concept paper (Paper IV). Results are interpreted within standard weak-field general relativity. No modification of gravity is proposed.<br><br>
  <a href="/experiments/">← Back to Experiments</a>
</div>
