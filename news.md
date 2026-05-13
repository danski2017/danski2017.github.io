---
layout: default
title: Headlines
permalink: /news/
description: Research headlines, lab notes, and results from Relational Labs.
---

<style>
.news-section-head {
  font-size: 0.72rem;
  font-weight: bold;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: #aaa;
  margin-bottom: 28px;
  padding-bottom: 8px;
  border-bottom: 1px solid #eee;
}
.news-entry {
  display: flex;
  gap: 20px;
  align-items: flex-start;
  padding: 22px 0;
  border-bottom: 1px solid #eee;
}
.news-entry:last-child {
  border-bottom: none;
}
.news-date {
  flex: 0 0 80px;
  font-size: 0.72rem;
  color: #bbb;
  padding-top: 2px;
  white-space: nowrap;
}
.news-body {
  flex: 1;
  min-width: 0;
}
.news-badge {
  display: inline-block;
  font-size: 0.60rem;
  font-weight: bold;
  letter-spacing: 0.07em;
  text-transform: uppercase;
  padding: 2px 6px;
  border-radius: 4px;
  margin-bottom: 6px;
}
.news-badge-paper    { background: #f0faf0; color: #2a6a2a; border: 1px solid #b8ddb8; }
.news-badge-labnote  { background: #eef2ff; color: #334eaa; border: 1px solid #c8d4f8; }
.news-badge-result   { background: #fff4cc; color: #8a6d00; border: 1px solid #e6c84a; }
.news-title {
  font-size: 1.00rem;
  font-weight: bold;
  color: #222;
  line-height: 1.35;
  margin-bottom: 5px;
}
.news-title a {
  color: #222;
  text-decoration: none;
}
.news-title a:hover {
  color: #3366cc;
  text-decoration: underline;
}
.news-desc {
  font-size: 0.85rem;
  color: #555;
  line-height: 1.58;
  margin-bottom: 8px;
}
.news-link {
  font-size: 0.78rem;
  font-weight: bold;
  color: #3366cc;
  text-decoration: none;
}
.news-link:hover { text-decoration: underline; }
@media (max-width: 600px) {
  .news-entry { flex-direction: column; gap: 4px; }
  .news-date { flex: none; }
}
</style>

# Headlines

<div class="news-section-head">May 2026</div>

<div class="news-entry">
  <div class="news-date">May 13</div>
  <div class="news-body">
    <span class="news-badge news-badge-labnote">Lab Note</span>
    <div class="news-title"><a href="/galaxy-averages-curvature-structure.html">When Galaxy Averages Hide Curvature Structure</a></div>
    <div class="news-desc">Atlas ran a controlled sequence of toy-galaxy simulations (B006–B013) testing what survives common coarse-graining methods. Scalar rotation summaries can remain well-behaved while local electric-Weyl structure and eigenframe orientation changes several times more strongly. B013 extends the probe to a cosmic-web proxy scene.</div>
    <a class="news-link" href="/galaxy-averages-curvature-structure.html">Read lab note &rarr;</a>
  </div>
</div>

<div class="news-entry">
  <div class="news-date">May 13</div>
  <div class="news-body">
    <span class="news-badge news-badge-paper">Paper</span>
    <div class="news-title"><a href="/Three_Measures_of_Gravitational_Identity_GCS_VII.pdf">Paper VII — Three Measures of Gravitational Identity</a></div>
    <div class="news-desc">Budget, jurisdiction, and compression separated as three independent diagnostics of gravitational identity in the weak-field limit. The budget peaks at the neutron star boundary and inverts for black holes. Pre-circulation draft.</div>
    <a class="news-link" href="/Three_Measures_of_Gravitational_Identity_GCS_VII.pdf">Read paper &rarr;</a>
  </div>
</div>

<div class="news-entry">
  <div class="news-date">May 2026</div>
  <div class="news-body">
    <span class="news-badge news-badge-paper">Paper</span>
    <div class="news-title"><a href="/Gravitational_Field_Relation_Operator_public_GCS%20VI.pdf">Paper VI — The Gravitational Field-Relation Operator</a></div>
    <div class="news-desc">Direct construction of gravitational parity networks from source-context residuals. First full Riemann run completed with encouraging results.</div>
    <a class="news-link" href="/Gravitational_Field_Relation_Operator_public_GCS%20VI.pdf">Read paper &rarr;</a>
  </div>
</div>

<div class="news-entry">
  <div class="news-date">May 2026</div>
  <div class="news-body">
    <span class="news-badge news-badge-result">Result</span>
    <div class="news-title"><a href="/staging/">HL Tau Disk Gap Prediction</a></div>
    <div class="news-desc">Six of seven ALMA gaps in HL Tau match GCS parity surface predictions with zero free parameters, including D3 and D4 which have no agreed explanation in standard literature. Cross-system sweep across 7 DSHARP systems completed.</div>
    <a class="news-link" href="/staging/">View staging analysis &rarr;</a>
  </div>
</div>
