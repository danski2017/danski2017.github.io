---
layout: default
title: Experiments
description: Interactive simulations and numerical visualizations of GCS parity networks.
---

<style>
.exp-layout {
  display: flex;
  gap: 36px;
  align-items: flex-start;
}
.exp-showcase {
  flex: 3;
  min-width: 0;
}
.exp-sidebar {
  flex: 1;
  min-width: 240px;
  position: sticky;
  top: 20px;
}
.exp-showcase-item {
  margin-bottom: 48px;
}
.exp-showcase-item:last-child {
  margin-bottom: 0;
}
.exp-showcase-meta {
  font-size: 0.72rem;
  font-weight: bold;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: #999;
  margin-bottom: 5px;
}
.exp-showcase-title {
  font-size: 1.05rem;
  font-weight: bold;
  margin-bottom: 5px;
}
.exp-showcase-desc {
  font-size: 0.87rem;
  color: #555;
  margin-bottom: 12px;
  line-height: 1.55;
}
.exp-frame {
  width: 100%;
  border-radius: 8px;
  overflow: hidden;
  border: 1px solid rgba(25,50,100,0.3);
  box-shadow: 0 4px 20px rgba(0,0,0,0.4);
}
.exp-frame iframe {
  border: none;
  display: block;
  width: 100%;
}
.exp-sidebar-heading {
  font-size: 0.72rem;
  font-weight: bold;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: #aaa;
  margin-bottom: 16px;
  padding-bottom: 8px;
  border-bottom: 1px solid #eee;
}
.exp-card {
  border: 1px solid #e4e4e4;
  border-radius: 8px;
  overflow: hidden;
  margin-bottom: 14px;
  background: #fff;
  transition: border-color 0.2s, box-shadow 0.2s;
}
.exp-card:hover {
  border-color: #bbb;
  box-shadow: 0 2px 12px rgba(0,0,0,0.09);
}
.exp-card-thumb {
  width: 100%;
  height: 100px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.65rem;
  letter-spacing: 0.18em;
  text-transform: uppercase;
}
.exp-card-thumb-ii  { background: linear-gradient(135deg, #020b18 0%, #061c36 100%); color: rgba(80,140,255,0.45); }
.exp-card-thumb-iii { background: linear-gradient(135deg, #070412 0%, #180828 100%); color: rgba(180,100,255,0.45); }
.exp-card-body {
  padding: 11px 13px 13px;
}
.exp-card-num {
  font-size: 0.67rem;
  color: #bbb;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  margin-bottom: 3px;
}
.exp-card-title {
  font-size: 0.88rem;
  font-weight: bold;
  color: #222;
  margin-bottom: 5px;
}
.exp-card-desc {
  font-size: 0.78rem;
  color: #666;
  line-height: 1.45;
  margin-bottom: 10px;
}
.exp-card-link {
  display: inline-block;
  font-size: 0.78rem;
  font-weight: bold;
  color: #3366cc;
  text-decoration: none;
}
.exp-card-link:hover { text-decoration: underline; }
.exp-open-links {
  margin-top: 7px;
  font-size: 0.78rem;
}
.exp-open-links a {
  color: #888;
  text-decoration: none;
}
.exp-open-links a:hover { color: #333; text-decoration: underline; }
.exp-card-forthcoming {
  border-style: dashed;
  opacity: 0.55;
}
@media (max-width: 820px) {
  .exp-layout {
    flex-direction: column;
    gap: 0;
  }
  .exp-sidebar {
    position: static;
    width: 100%;
    min-width: 0;
    border-top: 1px solid #eee;
    padding-top: 32px;
    margin-top: 40px;
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 14px;
  }
  .exp-sidebar-heading {
    grid-column: 1 / -1;
  }
  .exp-card { margin-bottom: 0; }
}
@media (max-width: 500px) {
  .exp-sidebar { grid-template-columns: 1fr; }
}
</style>

# **Interactive Field Simulations**

*Real-time gravitational field renderings built on the Atlas platform. The two primary experiments are embedded below. All experiments open as full standalone viewers.*

<br>

<div class="exp-layout">

<div class="exp-showcase">

<div class="exp-showcase-item">
<div class="exp-showcase-meta">Experiment IV &nbsp;&middot;&nbsp; Active</div>
<div class="exp-showcase-title">Dynamic Sponge Lattice</div>
<div class="exp-showcase-desc">Four gravitational sources orbit a common centroid while the surrounding three-dimensional lattice deforms in real-time. Use the controls to pause, engage flythrough camera, and tune displacement strength, orbit speed, and opacity.</div>
<div class="exp-frame" style="background:#000;">
  <iframe src="atlas_dynamic_sponge_lattice.html" height="640px" loading="lazy"></iframe>
</div>
<div class="exp-open-links">
  <a href="atlas_dynamic_sponge_lattice.html" target="_blank" rel="noopener">Open full screen &nearr;</a>
</div>
</div>

<div class="exp-showcase-item">
<div class="exp-showcase-meta">Experiment I &nbsp;&middot;&nbsp; Active</div>
<div class="exp-showcase-title">Local Stellar Neighborhood — N Parity Stack</div>
<div class="exp-showcase-desc">57 local stellar sources rendered as a full parity stack matrix. Source–source parity networks and source–context parity surfaces emerge across three tiers of support, shaped by gradients of acceleration.</div>
<div class="exp-frame" style="background:#020509;">
  <iframe src="images/atlas_lsn_v1.html" height="700px" loading="lazy"></iframe>
</div>
<div class="exp-open-links">
  <a href="images/atlas_lsn_v1.html" target="_blank" rel="noopener">Open full screen &nearr;</a>
</div>
</div>

</div>

<div class="exp-sidebar">

<div class="exp-sidebar-heading">All Experiments</div>

<div class="exp-card">
  <div class="exp-card-thumb exp-card-thumb-ii">3-body parity</div>
  <div class="exp-card-body">
    <div class="exp-card-num">Experiment II</div>
    <div class="exp-card-title">Three-Body Jurisdiction</div>
    <div class="exp-card-desc">Parity surfaces between three sources assemble into faces, seams, and contested nodes — the simplest case where the full GCS topology becomes visible.</div>
    <a class="exp-card-link" href="images/three_body_jurisdiction_v0_1.html" target="_blank" rel="noopener">Open Experiment &rarr;</a>
  </div>
</div>

<div class="exp-card">
  <div class="exp-card-thumb exp-card-thumb-iii">EM field geometry</div>
  <div class="exp-card-body">
    <div class="exp-card-num">Experiment III</div>
    <div class="exp-card-title">Lawful 3D Electromagnetic Field</div>
    <div class="exp-card-desc">GCS readability applied to electromagnetic field structure. Demonstrates that parity and jurisdiction geometry generalize across field types beyond gravity.</div>
    <a class="exp-card-link" href="images/lawful_3d_em.html" target="_blank" rel="noopener">Open Experiment &rarr;</a>
  </div>
</div>

<div class="exp-card exp-card-forthcoming">
  <div class="exp-card-body" style="padding-top:16px;">
    <div class="exp-card-num">Experiment V &nbsp;&middot;&nbsp; Forthcoming</div>
    <div class="exp-card-title">Recursive Domain Handoff</div>
    <div class="exp-card-desc">Modular scene handoff geometry across nested parity domains.</div>
  </div>
</div>

</div>

</div>
