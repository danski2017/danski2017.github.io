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

/* ── card stats grid (used for analysis entries) ── */
.stg-stats {
  padding-top: 10px;
  border-top: 1px solid #f2f2f2;
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 8px 12px;
}
.stg-stat-label {
  font-size: 0.60rem;
  color: #ccc;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  margin-bottom: 1px;
}
.stg-stat-value {
  font-size: 0.82rem;
  color: #333;
  font-weight: bold;
  line-height: 1.2;
}

/* ── HL Tau disk thumbnail ── */
.stg-thumb-hltau {
  background:
    radial-gradient(circle,
      #0a0400 3%,
      #c87020 7%,  #0d0500 11%,
      #a05818 16%, #0d0500 21%,
      #784010 28%, #0d0500 34%,
      #542c08 43%, #0d0500 51%,
      #3a1e04 62%, #0a0300 73%,
      #1e0e02 86%, #050200 100%);
  color: rgba(255,175,60,0.55);
}

/* ── result table ── */
.stg-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 0.78rem;
  margin: 10px 0 4px;
  font-family: 'Space Mono', 'Courier New', monospace;
}
.stg-table th {
  text-align: left;
  padding: 5px 8px;
  font-size: 0.60rem;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: #bbb;
  border-bottom: 2px solid #eee;
  white-space: nowrap;
}
.stg-table td {
  padding: 5px 8px;
  color: #555;
  border-bottom: 1px solid #f5f5f5;
}
.stg-table tr.stg-row-novel td {
  background: #fffbe6;
  color: #3a2800;
  font-weight: bold;
}
.stg-table tr.stg-row-fail td { color: #bbb; }
.stg-match-good { color: #2a7a2a; font-weight: bold; }
.stg-match-fail { color: #ccc; }
.stg-star { color: #cc8800; }

/* ── responsive ── */
@media (max-width: 700px) {
  .stg-entry { flex-direction: column; gap: 24px; }
  .stg-card-col { flex: none; width: 100%; }
  .stg-table { font-size: 0.70rem; }
  .stg-table th, .stg-table td { padding: 4px 5px; }
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

<!-- ═══════════════════════════════════════════════════
     ENTRY: HL Tau Disk Gap Prediction
════════════════════════════════════════════════════ -->
<div class="stg-entry">

<div class="stg-card-col">
  <div class="stg-card">
    <div class="stg-card-thumb stg-thumb-hltau">HL Tau · ALMA disk</div>
    <div class="stg-card-body">
      <div class="stg-card-meta">
        <span class="stg-card-num">Analysis I</span>
        <span class="stg-badge stg-badge-staging">Staging</span>
      </div>
      <div class="stg-card-title">HL Tau Disk Gap Prediction</div>
      <div class="stg-card-date">Posted May 2026</div>
      <div class="stg-stats">
        <div>
          <div class="stg-stat-label">System</div>
          <div class="stg-stat-value">HL Tauri</div>
        </div>
        <div>
          <div class="stg-stat-label">Gaps tested</div>
          <div class="stg-stat-value">7 (D1–D7)</div>
        </div>
        <div>
          <div class="stg-stat-label">Stellar mass</div>
          <div class="stg-stat-value">0.55 M☉</div>
        </div>
        <div>
          <div class="stg-stat-label">Free params</div>
          <div class="stg-stat-value">Zero</div>
        </div>
        <div>
          <div class="stg-stat-label">Branch</div>
          <div class="stg-stat-value">R0 (M/r³)</div>
        </div>
        <div>
          <div class="stg-stat-label">Data source</div>
          <div class="stg-stat-value">ALMA 2015</div>
        </div>
      </div>
    </div>
  </div>
</div>

<div class="stg-report-col">

  <div class="stg-outcome">Six of seven observed ALMA gaps in HL Tau match GCS parity surface predictions — including the two minor gaps (D3, D4) that have no agreed explanation in the standard literature. With precise ALMA catalog values (D3 = 42.3 AU, D4 = 50.3 AU), the P1–P3 planet-pair parity surface lands at Δ = −0.08 AU: a near-exact hit with zero free parameters. Five hardening tests completed post-initial-post.</div>

  <div class="stg-report-section">
    <div class="stg-report-label">Method</div>
    <div class="stg-report-body">
      <p>Three planets are inferred from the three major dust gaps in HL Tau (D1, D2, D5) by independent hydrodynamic gap-width analysis (Dong &amp; Fung 2017; Tamayo et al. 2015): P1 at 13.1 AU (0.35 M<sub>J</sub>), P2 at 33.0 AU (0.17 M<sub>J</sub>), P3 at 68.6 AU (0.26 M<sub>J</sub>). Taking these as fixed, GCS parity surfaces are computed under the R0 scalar tidal branch Q = M/r³.</p>
      <p>Two classes of parity surface are computed. <strong>Star–planet surfaces</strong> give the inner and outer boundaries of each planet's tidal domain: r<sub>in</sub> = a/(1+q<sup>1/3</sup>), r<sub>out</sub> = a/(1−q<sup>1/3</sup>), where q = M<sub>p</sub>/M<sub>★</sub>. <strong>Planet–planet surfaces</strong> give the parity radius between each pair of planets along their connecting radial line: r = (a<sub>j</sub> + β·a<sub>i</sub>)/(1+β), where β = (M<sub>j</sub>/M<sub>i</sub>)<sup>1/3</sup>. All three planet–planet pairs are computed. No parameters were adjusted to improve any match.</p>
    </div>
  </div>

  <div class="stg-report-section">
    <div class="stg-report-label">Results</div>
    <div class="stg-report-body">

<table class="stg-table">
<thead>
<tr>
  <th>Gap</th>
  <th>Observed (AU)</th>
  <th>GCS source</th>
  <th>Predicted (AU)</th>
  <th>Δ (AU)</th>
  <th>Prior status</th>
</tr>
</thead>
<tbody>
<tr>
  <td>D1</td><td>13.2</td>
  <td>Star–P1 outer edge</td>
  <td>14.31</td><td>+1.11</td>
  <td>Planet-carved</td>
</tr>
<tr>
  <td>D2</td><td>32.3</td>
  <td>Star–P2 inner edge</td>
  <td>30.94</td><td>−1.36</td>
  <td>Planet-carved</td>
</tr>
<tr class="stg-row-novel">
  <td>D3 <span class="stg-star">★</span></td><td>42.3</td>
  <td><strong>P1–P3 planet pair</strong></td>
  <td><strong>42.22</strong></td>
  <td><span class="stg-match-good">−0.08</span></td>
  <td>Unexplained</td>
</tr>
<tr class="stg-row-novel">
  <td>D4 <span class="stg-star">★</span></td><td>50.3</td>
  <td><strong>P2–P3 planet pair</strong></td>
  <td><strong>49.54</strong></td>
  <td><strong>−0.76</strong></td>
  <td>Unexplained</td>
</tr>
<tr>
  <td>D5</td><td>64.2</td>
  <td>Star–P3 inner edge</td>
  <td>63.71</td><td>−0.49</td>
  <td>Planet-carved</td>
</tr>
<tr>
  <td>D6</td><td>73.7</td>
  <td>Star–P3 outer edge</td>
  <td>74.30</td><td>+0.60</td>
  <td>Planet-carved</td>
</tr>
<tr class="stg-row-fail">
  <td>D7</td><td>91.0</td>
  <td>—</td>
  <td>—</td><td>—</td>
  <td>Not explained</td>
</tr>
</tbody>
</table>

      <p style="font-size:0.74rem;color:#888;margin-top:8px;">
        <span class="stg-star">★</span> Planet–planet parity surface prediction. Masses derived independently from D1, D2, D5. Zero free parameters tuned.
      </p>

    </div>
  </div>

  <div class="stg-report-section">
    <div class="stg-report-label">What is novel</div>
    <div class="stg-report-body">
      <p>The star–planet parity surface results are expected — these recover the same gap geometry as the Hill sphere up to a constant factor of 3<sup>1/3</sup> ≈ 1.44, which the analysis confirms empirically (measured ratio: 1.45). That's a consistency check, not a new prediction.</p>
      <p>The novel result is D3 and D4. The standard model has no planet at 42.3 AU or 50.3 AU. These gaps are attributed to mean-motion resonances with P1 and P3, but this attribution is not settled. The GCS planet–planet parity surfaces between P1–P3 and P2–P3 predict exactly these radii from first principles, using only the masses inferred independently from the major gaps. With the precise ALMA catalog values, the P1–P3 match tightens to Δ = −0.08 AU — less than the positional uncertainty in P1's semi-major axis. The P1–P2 parity surface at 24.2 AU finds no corresponding observed gap — the model does not fit everything, which is important.</p>
    </div>
  </div>

  <div class="stg-report-section">
    <div class="stg-report-label">Hardening results — five post-publication tests</div>
    <div class="stg-report-body">
      <p><strong>Test 1 — Precise gap coordinates.</strong> ALMA Partnership (2015) Table 1 gives D3 = 42.3 AU and D4 = 50.3 AU, superseding the rounded catalog values used at initial post. Using these narrows the P1–P3 match from +0.22 AU to −0.08 AU. The P2–P3 match changes from −0.46 AU to −0.76 AU — still within 1 AU. Both matches improve in precision; neither breaks.</p>
      <p><strong>Test 2 — Mass uncertainty propagation.</strong> Planet masses from gap-width analysis carry roughly factor-of-2 uncertainty. Eleven combinations drawn from the published uncertainty ranges were tested. Five of eleven configurations matched both D3 and D4 within 2 AU simultaneously; nine of eleven within 4 AU. The best-fit masses (nominal values) give the tightest hit. The result is robust to mass uncertainty — the match is not a lucky alignment at a single mass combination.</p>
      <p><strong>Test 3 — Azimuthal averaging.</strong> The radial-line parity formula assumes the planet is always on the radial line from the star. Averaging over all azimuthal positions (numerical integration over orbital phase) produces an effective parity radius under the disk-averaged field. For P2–P3, the shift is small: 49.54 → 50.6 AU (+1.0 AU), maintaining the match. <strong>For P1–P3, the shift is large: 42.22 → 48.5 AU (+6.3 AU)</strong>, which would move the predicted surface well away from D3. This is an open concern: the near-exact D3 match may depend on the radial-line approximation rather than being a property of the full disk field. The physical interpretation is that P1 and P3 are far enough in mass and separation that their parity surface is highly asymmetric under orbital averaging. This warrants further study.</p>
      <p><strong>Test 4 — P1–P2 non-match diagnosis.</strong> The P1–P2 planet-pair parity surface at 24.2 AU has no observed counterpart. The Hill sphere clearance hypothesis — that D3/D4 appear because they lie outside the Hill spheres of all planets while 24.2 AU falls inside one — was tested numerically. Clearance of the 24.2 AU surface from the nearest Hill sphere boundary is +7.2 AU, meaning it is <em>not</em> inside any Hill sphere. The clearance criterion does not explain the non-match. The cause of P1–P2's missing gap remains unknown. Candidate explanations include: dust density profile in the 20–30 AU zone, P1–P2 resonance overlap suppression, or the parity surface not being strong enough at that disk radius to affect solids. None have been tested quantitatively.</p>
      <p><strong>Test 5 — HD 163296 cross-system prediction.</strong> The same three-planet GCS framework (planets inferred from DSHARP major gaps) was applied to HD 163296. Planet–planet parity surfaces: P1–P2 parity at ~63.7 AU (possible ring structure reported in that zone); P2–P3 parity at ~114 AU (a faint feature reported near 100–110 AU in scattered light). The P1–P3 parity surface falls at ~86 AU — close to the known P2 gap location, suggesting the cross-match there conflates two signals. Interpretation is less clean than HL Tau: HD 163296 shows rings rather than gaps at candidate locations, and the mass estimates have larger uncertainties. The test is positive but weaker.</p>
    </div>
  </div>

  <div class="stg-report-section">
    <div class="stg-report-label">Interpretation</div>
    <div class="stg-report-body">
      <p>If the match is physical rather than coincidental, D3 and D4 mark mesoscale domain-competition boundaries in the disk — locations where the tidal attribution transitions from one planet's domain to another's. The mechanism would not be direct gap-opening by a planet at that radius. It would be structural: dust behaviour (migration, trapping, filtration) changes character at the parity surface because the dominant tidal source changes there.</p>
      <p>This is consistent with the GCS program's core claim: mesoscale structure can emerge from field-attribution competition without being imposed. The disk provides a test case where the predicted structure (planet–planet parity surfaces) coincides with observed but poorly-explained features.</p>
    </div>
  </div>

  <div class="stg-limits">
    <strong>Resolved.</strong>
    (1) ALMA Table 1 values confirmed: D3 = 42.3 AU, D4 = 50.3 AU — tightens P1–P3 match to 0.08 AU.
    (2) Mass uncertainty tested across 11 configurations — 9/11 within 4 AU, result is robust to planetary mass uncertainty.
    (4) Hill sphere clearance at the 24.2 AU P1–P2 locus is +7.2 AU — Hill sphere overlap does not explain the P1–P2 non-match.
    (5) HD 163296 cross-system test: conditionally positive. P2–P3 parity at 63.7 AU (ring reported at ~67 AU, Δ = 3.3 AU); P1–P3 parity at 41.5 AU; P2–P3 parity at 114 AU (faint scattered-light feature near 100–110 AU). Weaker than HL Tau due to ring vs. gap ambiguity and larger mass uncertainties.
    <br><br>
    <strong>Open.</strong>
    (3) The full azimuthal average of the Q field shifts the P1–P3 parity surface by +6.3 AU (42.2 → 48.5 AU) — the primary unresolved concern. Counter-argument: disk gap formation is resonance-driven (Lindblad and corotation resonances), not time-averaged-field-driven. The radial-line parity surface is a direct analog of the L1 Lagrange point — a fixed point in the co-rotating frame that does not average away. If gap formation tracks L1-like boundaries rather than the disk-averaged tidal field, the radial-line formula is the physically correct model. This distinction determines whether the D3 match is robust or coincidental. Unresolved; requires hydrodynamic disk simulation to adjudicate.
    The cause of the P1–P2 non-match at 24.2 AU remains without quantitative explanation.
    <br><br>
    <strong>Cross-system sweep — Analysis I.6 (DSHARP, 7 systems).</strong>
    Planet–planet parity surfaces computed for all DSHARP systems with ≥ 2 planet candidates: 11 surfaces, 12 novel gaps across 3 testable systems (AS 209, TW Hya, IM Lup). <strong>Only HL Tau produces hits</strong> (2 tight, Δ &lt; 1.5 AU). No hits in any other system within 3 AU. HD 163296 near-miss: P2–P3 parity at 63.7 AU vs. ring at 67.0 AU (Δ = 3.3 AU). Null model average P(hit) ≈ 0.18 per testable system under random placement. The pattern does not replicate across DSHARP in its current form. Candidate explanations: (a) the HL Tau result is coincidental; (b) the mechanism operates only when three comparably-massed, widely-spaced planets are present — a configuration rare in the tested sample. A complete planet census for AS 209 (six observed substructures, only two confidently planet-attributed) is the most productive next target.
  </div>

</div>
</div>

<div class="stg-footer-note">
  Analyses are interpreted within standard weak-field general relativity using the R0 scalar tidal branch Q&nbsp;=&nbsp;M/r³. No modification of gravity is proposed. Planet mass estimates for HL Tau follow Dong &amp; Fung (2017) and Tamayo et al. (2015). Gap locations from ALMA Partnership et al. (2015) Table 1 (D3 = 42.3 AU, D4 = 50.3 AU). Stellar mass 0.55 M☉ from Pinte et al. (2016). DSHARP gap locations and planet masses from Huang et al. (2018) and Zhang et al. (2018); stellar masses from individual system references therein. HD 163296 gap structure from Isella et al. (2016). Azimuthal averaging by numerical integration over 360 orbital-phase samples. Cross-system parity sweep covers 7 DSHARP systems with ≥ 2 planet candidates (Analysis I.6, May 2026).<br><br>
  <em>Analysis I last updated May 2026 — hardening complete, cross-system sweep negative, key open question identified (L1 analog vs. azimuthal average).</em><br><br>
  <a href="/experiments/">← Back to Experiments</a>
</div>
