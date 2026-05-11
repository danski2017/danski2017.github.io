---
layout: default
title: Lab Notebook
permalink: /lab-notes/
description: Working notes, ideas, links, and to-dos for the Relational Labs research program.
---

<style>
.nb-topbar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 12px;
  margin-bottom: 28px;
}
.nb-subtitle {
  font-size: 0.88rem;
  color: #888;
}
.nb-lockbar {
  display: inline-flex;
  align-items: center;
  gap: 7px;
  font-size: 0.78rem;
  color: #999;
  background: #f7f7f7;
  border: 1px solid #e8e8e8;
  border-radius: 20px;
  padding: 5px 14px 5px 11px;
  cursor: pointer;
  transition: all 0.2s;
  user-select: none;
  white-space: nowrap;
}
.nb-lockbar:hover { border-color: #ccc; color: #555; }
.nb-lockbar.unlocked { color: #2a7a2a; border-color: #b8ddb8; background: #f3faf3; }

.nb-pw-row {
  display: none;
  align-items: center;
  gap: 0;
  margin-bottom: 24px;
}
.nb-pw-row.visible { display: flex; }
.nb-pw-row input {
  font-size: 0.85rem;
  border: 1px solid #ddd;
  border-radius: 6px 0 0 6px;
  padding: 7px 12px;
  outline: none;
  width: 180px;
  font-family: inherit;
}
.nb-pw-row input:focus { border-color: #aaa; }
.nb-pw-row button {
  font-size: 0.8rem;
  padding: 7px 14px;
  border: 1px solid #ddd;
  border-left: none;
  border-radius: 0 6px 6px 0;
  background: #f5f5f5;
  cursor: pointer;
  font-family: inherit;
}
.nb-pw-row button:hover { background: #eee; }
.nb-pw-err {
  font-size: 0.75rem;
  color: #c0392b;
  margin-left: 12px;
  display: none;
}
.nb-pw-err.visible { display: inline; }

.nb-feed { max-width: 780px; }

.nb-entry {
  display: flex;
  gap: 18px;
  padding: 16px 0;
  border-bottom: 1px solid #f0f0f0;
}
.nb-entry:last-child { border-bottom: none; }
.nb-entry.nb-private { display: none; }
.nb-entry.nb-private.visible { display: flex; }

.nb-left {
  flex-shrink: 0;
  width: 96px;
}
.nb-date {
  font-size: 0.7rem;
  color: #c0c0c0;
  display: block;
  margin-bottom: 6px;
  letter-spacing: 0.02em;
}
.nb-tag {
  font-size: 0.62rem;
  font-weight: bold;
  letter-spacing: 0.07em;
  text-transform: uppercase;
  padding: 2px 8px;
  border-radius: 10px;
  display: inline-block;
}
.nb-concept    { background: #e8f0fe; color: #2c5faa; }
.nb-link       { background: #e6f4ea; color: #276c2c; }
.nb-todo       { background: #fef3e2; color: #8a5000; }
.nb-connection { background: #f3e8fd; color: #6b28a8; }
.nb-idea       { background: #e0f5f5; color: #1a6b6b; }

.nb-body {
  flex: 1;
  min-width: 0;
  font-size: 0.875rem;
  line-height: 1.65;
  color: #333;
}
.nb-body p { margin: 0 0 5px; }
.nb-body p:last-child { margin-bottom: 0; }
.nb-body a { color: #3366cc; }
.nb-priv-dot {
  display: inline-block;
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: #ddd;
  margin-left: 6px;
  vertical-align: middle;
  position: relative;
  top: -1px;
}

@media (max-width: 600px) {
  .nb-entry { flex-direction: column; gap: 5px; }
  .nb-left { width: auto; display: flex; align-items: center; gap: 10px; }
  .nb-date { margin-bottom: 0; }
}
</style>

# Lab Notebook

<div class="nb-topbar">
  <span class="nb-subtitle"><em>Working notes, connections, and follow-up items. Newest first.</em></span>
  <div id="nb-lockbar" class="nb-lockbar" onclick="nbToggle()">
    <span id="nb-icon">🔒</span>
    <span id="nb-label">Private entries locked</span>
  </div>
</div>

<div class="nb-pw-row" id="nb-pw-row">
  <input type="password" id="nb-pw" placeholder="Passphrase" onkeydown="if(event.key==='Enter')nbCheck()">
  <button onclick="nbCheck()">Unlock</button>
  <span class="nb-pw-err" id="nb-err">Incorrect.</span>
</div>

<div class="nb-feed">

  <div class="nb-entry">
    <div class="nb-left">
      <span class="nb-date">2026-05-11</span>
      <span class="nb-tag nb-concept">Concept</span>
    </div>
    <div class="nb-body">
      Apollonius sphere as exact two-body GCS boundary — r₁/r₂ = m₁/m₂. Worth a dedicated diagram in Paper VII to make this explicit for readers coming from classical geometry.
    </div>
  </div>

  <div class="nb-entry">
    <div class="nb-left">
      <span class="nb-date">2026-05-11</span>
      <span class="nb-tag nb-link">Link</span>
    </div>
    <div class="nb-body">
      <a href="https://mathworld.wolfram.com/ApolloniusCircle.html" target="_blank" rel="noopener">Apollonius Circles &amp; Spheres — Wolfram MathWorld</a><br>
      Already in Resources. Cross-reference explicitly in Paper VII introduction alongside the Hill sphere comparison table.
    </div>
  </div>

  <div class="nb-entry">
    <div class="nb-left">
      <span class="nb-date">2026-05-10</span>
      <span class="nb-tag nb-todo">To-Do</span>
    </div>
    <div class="nb-body">
      Run Facebook Sharing Debugger on home page URL to force OG cache refresh after recent meta tag updates.
    </div>
  </div>

  <!-- ─── Private entry example ─── -->
  <div class="nb-entry nb-private">
    <div class="nb-left">
      <span class="nb-date">2026-05-11</span>
      <span class="nb-tag nb-idea">Idea</span>
      <span class="nb-priv-dot" title="Private"></span>
    </div>
    <div class="nb-body">
      Private entry — visible only after unlocking. Use this format for pre-publication ideas, speculative connections, and anything not ready to surface publicly.
    </div>
  </div>

</div>

<script>
// ── To change the passphrase: replace 'atlas2026' below with your new passphrase ──
const NB_KEY = btoa('atlas2026');

(function(){ if(sessionStorage.getItem('nb')===NB_KEY) nbUnlock(false); })();

function nbToggle(){
  if(sessionStorage.getItem('nb')===NB_KEY){ nbLock(); return; }
  const r=document.getElementById('nb-pw-row');
  r.classList.toggle('visible');
  if(r.classList.contains('visible')) document.getElementById('nb-pw').focus();
}

function nbCheck(){
  const val=document.getElementById('nb-pw').value;
  const err=document.getElementById('nb-err');
  if(btoa(val)===NB_KEY){
    err.classList.remove('visible');
    document.getElementById('nb-pw-row').classList.remove('visible');
    document.getElementById('nb-pw').value='';
    sessionStorage.setItem('nb',NB_KEY);
    nbUnlock(true);
  } else {
    err.classList.add('visible');
    document.getElementById('nb-pw').value='';
    document.getElementById('nb-pw').focus();
  }
}

function nbUnlock(animate){
  document.querySelectorAll('.nb-private').forEach(el=>el.classList.add('visible'));
  document.getElementById('nb-icon').textContent='🔓';
  document.getElementById('nb-label').textContent='Private visible — click to lock';
  document.getElementById('nb-lockbar').classList.add('unlocked');
}

function nbLock(){
  document.querySelectorAll('.nb-private').forEach(el=>el.classList.remove('visible'));
  document.getElementById('nb-icon').textContent='🔒';
  document.getElementById('nb-label').textContent='Private entries locked';
  document.getElementById('nb-lockbar').classList.remove('unlocked');
  document.getElementById('nb-pw-row').classList.remove('visible');
  sessionStorage.removeItem('nb');
}
</script>
