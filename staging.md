---
layout: default
title: Staging Lab
description: Pre-publication experiment results from Atlas GCS Research — preliminary, not peer reviewed.
---

<style>
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
.stg-banner strong {
  color: #3a3000;
}
.stg-header {
  font-size: 0.72rem;
  font-weight: bold;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: #aaa;
  margin-bottom: 20px;
  padding-bottom: 8px;
  border-bottom: 1px solid #eee;
}
.stg-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 22px;
  margin-top: 0;
}
.stg-card {
  border: 1px solid #e4e4e4;
  border-radius: 10px;
  overflow: hidden;
  background: #fff;
  transition: border-color 0.2s, box-shadow 0.2s;
}
.stg-card:hover {
  border-color: #bbb;
  box-shadow: 0 3px 16px rgba(0,0,0,0.10);
}
.stg-card-thumb {
  width: 100%;
  height: 120px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.65rem;
  letter-spacing: 0.18em;
  text-transform: uppercase;
}
.stg-thumb-entropy {
  background: linear-gradient(135deg, #000011 0%, #1a0040 40%, #7a0066 75%, #ff8800 95%);
  color: rgba(255,215,0,0.6);
}
.stg-card-body {
  padding: 14px 16px 16px;
}
.stg-card-meta {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-bottom: 7px;
  flex-wrap: wrap;
}
.stg-card-num {
  font-size: 0.67rem;
  color: #bbb;
  text-transform: uppercase;
  letter-spacing: 0.08em;
}
.stg-badge {
  font-size: 0.63rem;
  font-weight: bold;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  padding: 2px 7px;
  border-radius: 4px;
}
.stg-badge-staging {
  background: #fff4cc;
  color: #8a6d00;
  border: 1px solid #e6c84a;
}
.stg-card-title {
  font-size: 0.94rem;
  font-weight: bold;
  color: #222;
  margin-bottom: 6px;
}
.stg-card-desc {
  font-size: 0.80rem;
  color: #555;
  line-height: 1.5;
  margin-bottom: 12px;
}
.stg-card-date {
  font-size: 0.72rem;
  color: #bbb;
  margin-bottom: 10px;
}
.stg-card-link {
  display: inline-block;
  font-size: 0.80rem;
  font-weight: bold;
  color: #3366cc;
  text-decoration: none;
}
.stg-card-link:hover { text-decoration: underline; }
.stg-modes {
  margin-top: 10px;
  padding-top: 10px;
  border-top: 1px solid #f0f0f0;
}
.stg-modes-label {
  font-size: 0.67rem;
  color: #bbb;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  margin-bottom: 5px;
}
.stg-mode-list {
  font-size: 0.77rem;
  color: #666;
  line-height: 1.55;
}
@media (max-width: 600px) {
  .stg-grid { grid-template-columns: 1fr; }
}
</style>

# Staging Lab

<div class="stg-banner">
  <strong>Pre-publication notice.</strong> Experiments on this page are preliminary results from active Atlas research. They have not undergone formal peer review and may change substantially before publication. Links are provided so collaborators and interested readers can inspect the work directly. Interpret conservatively.
</div>

<div class="stg-header">Staging — {{ site.time | date: "%B %Y" }}</div>

<div class="stg-grid">

<div class="stg-card">
  <div class="stg-card-thumb stg-thumb-entropy">entropy ridge · GCS</div>
  <div class="stg-card-body">
    <div class="stg-card-meta">
      <span class="stg-card-num">Experiment V</span>
      <span class="stg-badge stg-badge-staging">Staging</span>
    </div>
    <div class="stg-card-title">Attribution Entropy Field</div>
    <div class="stg-card-date">Posted May 2026</div>
    <div class="stg-card-desc">GPU shader visualization of the GCS parity readability structure via attribution entropy. The bright ridges in the field are the exact GCS parity surfaces — not approximations — derived from S&nbsp;=&nbsp;−w&thinsp;ln&thinsp;w&nbsp;−&nbsp;(1−w)&thinsp;ln(1−w), maximized where source and context contributions are equal.</div>
    <div class="stg-modes">
      <div class="stg-modes-label">Modes</div>
      <div class="stg-mode-list">
        <strong>ATTR</strong> — per-source binary entropy; select focal source, drag to reshape.<br>
        <strong>SCENE</strong> — global Shannon entropy; full parity network + arrangement sweep.<br>
        <strong>ORBIT</strong> — two-source orbit; entropy ridge sweeps out the GCS worldsheet.
      </div>
    </div>
    <br>
    <a class="stg-card-link" href="/atlas_entropy_field.html" target="_blank" rel="noopener">Open Experiment &nearr;</a>
  </div>
</div>

</div>

<br>

---

*Staging experiments use the same four-source benchmark masses (M₁=1.00, M₂=0.72, M₃=0.33, M₄=0.11) established in the Atlas proof-of-concept paper (Paper IV). Results are interpreted within standard weak-field general relativity. No modification of gravity is proposed.*

[← Back to Experiments](/experiments/)
