---
layout: default
title: Headlines
permalink: /news/
description: Research headlines, lab notes, and results from Relational Labs.
---

<style>
.news-feed {
  max-width: 740px;
}
.news-feed-heading {
  font-size: 0.72rem;
  font-weight: bold;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: #aaa;
  margin-bottom: 28px;
  padding-bottom: 8px;
  border-bottom: 1px solid #eee;
}
.news-item {
  display: flex;
  gap: 24px;
  align-items: flex-start;
  padding: 24px 0;
  border-bottom: 1px solid #eee;
}
.news-item:last-child {
  border-bottom: none;
}
.news-date {
  flex: 0 0 90px;
  font-size: 0.76rem;
  color: #bbb;
  padding-top: 3px;
  font-variant-numeric: tabular-nums;
  white-space: nowrap;
}
.news-body {
  flex: 1;
  min-width: 0;
}
.news-tag {
  display: inline-block;
  font-size: 0.60rem;
  font-weight: bold;
  letter-spacing: 0.09em;
  text-transform: uppercase;
  padding: 2px 7px;
  border-radius: 4px;
  margin-bottom: 6px;
}
.news-tag-lab-note  { background: #eef2ff; color: #3355bb; border: 1px solid #c8d4f8; }
.news-tag-paper     { background: #f0faf0; color: #2a6a2a; border: 1px solid #b8ddb8; }
.news-tag-result    { background: #fff8ee; color: #885500; border: 1px solid #f0d090; }
.news-title {
  font-size: 1.02rem;
  font-weight: bold;
  color: #111;
  line-height: 1.35;
  margin-bottom: 6px;
}
.news-title a {
  color: inherit;
  text-decoration: none;
}
.news-title a:hover {
  color: #3366cc;
  text-decoration: underline;
}
.news-desc {
  font-size: 0.87rem;
  color: #555;
  line-height: 1.58;
  margin-bottom: 8px;
}
.news-link {
  font-size: 0.80rem;
  font-weight: bold;
  color: #3366cc;
  text-decoration: none;
}
.news-link:hover { text-decoration: underline; }
@media (max-width: 600px) {
  .news-item { flex-direction: column; gap: 6px; }
  .news-date { flex: none; }
}
</style>

# **Headlines**

*Research updates, lab notes, and results from Relational Labs.*

<br>

<div class="news-feed">

<div class="news-feed-heading">May 2026</div>

<div class="news-item">
  <div class="news-date">May 13, 2026</div>
  <div class="news-body">
    <span class="news-tag news-tag-lab-note">Lab Note</span>
    <div class="news-title"><a href="/galaxy-averages-curvature-structure.html">When Galaxy Averages Hide Curvature Structure</a></div>
    <div class="news-desc">Atlas ran a controlled sequence of toy-galaxy simulations (B006–B012) testing what survives common coarse-graining methods. Early result: scalar rotation summaries can remain well-behaved while the local electric-Weyl structure and eigenframe orientation seen by relational witnesses changes several times more strongly.</div>
    <a class="news-link" href="/galaxy-averages-curvature-structure.html">Read lab note &rarr;</a>
  </div>
</div>

<div class="news-item">
  <div class="news-date">May 13, 2026</div>
  <div class="news-body">
    <span class="news-tag news-tag-paper">Paper</span>
    <div class="news-title"><a href="/Three_Measures_of_Gravitational_Identity_GCS_VII.pdf">Paper VII — Three Measures of Gravitational Identity</a></div>
    <div class="news-desc">Budget, jurisdiction, and compression separated as three independent diagnostics of gravitational identity in the weak-field limit. The budget peaks at the neutron star boundary and inverts for black holes. Pre-circulation draft.</div>
    <a class="news-link" href="/Three_Measures_of_Gravitational_Identity_GCS_VII.pdf">Read paper &rarr;</a>
  </div>
</div>

<div class="news-item">
  <div class="news-date">May 2026</div>
  <div class="news-body">
    <span class="news-tag news-tag-paper">Paper</span>
    <div class="news-title"><a href="/Gravitational_Field_Relation_Operator_public_GCS%20VI.pdf">Paper VI — The Gravitational Field-Relation Operator</a></div>
    <div class="news-desc">Direct construction of gravitational parity networks from source-context residuals. First full Riemann run completed with encouraging results.</div>
    <a class="news-link" href="/Gravitational_Field_Relation_Operator_public_GCS%20VI.pdf">Read paper &rarr;</a>
  </div>
</div>

<div class="news-item">
  <div class="news-date">May 2026</div>
  <div class="news-body">
    <span class="news-tag news-tag-result">Result</span>
    <div class="news-title"><a href="/staging/">HL Tau Disk Gap Prediction — Staging</a></div>
    <div class="news-desc">Six of seven ALMA gaps in HL Tau match GCS parity surface predictions with zero free parameters, including the two minor gaps (D3, D4) with no agreed explanation in standard literature. Cross-system sweep across 7 DSHARP systems completed — HL Tau result does not replicate broadly.</div>
    <a class="news-link" href="/staging/">View staging analysis &rarr;</a>
  </div>
</div>

</div>
