<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>ATLAS · Three-Body Jurisdiction</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Space+Mono:ital,wght@0,400;0,700;1,400&display=swap" rel="stylesheet">
<style>
* { margin: 0; padding: 0; box-sizing: border-box; }

body {
  background: #020509;
  overflow: hidden;
  font-family: 'Space Mono', monospace;
}

canvas { display: block; }

/* ---- LOADING SCREEN ---- */
#loading {
  position: fixed; inset: 0;
  background: #020509;
  display: flex; flex-direction: column;
  align-items: center; justify-content: center;
  gap: 20px; z-index: 200;
}
.ld-wordmark {
  font-size: 9px; letter-spacing: 0.35em;
  color: #2A4066; text-transform: uppercase;
  margin-bottom: 4px;
}
.ld-title {
  font-size: 12px; letter-spacing: 0.18em;
  color: #4466AA; text-transform: uppercase;
}
.ld-bar-wrap { width: 200px; height: 1px; background: #0A1525; position: relative; }
.ld-bar-fill {
  position: absolute; top: 0; left: 0; height: 100%;
  background: linear-gradient(90deg, #1A4488, #4488CC);
  width: 0%; transition: width 0.5s ease;
}
.ld-stage {
  font-size: 8px; letter-spacing: 0.18em;
  color: #1C3050; text-transform: uppercase;
}

/* ---- PANEL TOGGLE (mobile) ---- */
#panel-toggle {
  display: none;
  position: fixed; top: 14px; left: 14px;
  width: 36px; height: 36px;
  background: rgba(3,8,22,0.92);
  border: 1px solid rgba(30,60,120,0.4);
  border-radius: 6px;
  z-index: 20;
  cursor: pointer;
  align-items: center; justify-content: center;
  backdrop-filter: blur(10px);
}
#panel-toggle svg { width: 16px; height: 16px; }

/* ---- LEFT PANEL ---- */
#panel {
  position: fixed; top: 0; left: 0;
  width: 230px; height: 100vh;
  background: linear-gradient(175deg, rgba(3,6,18,0.97) 0%, rgba(2,4,12,0.94) 100%);
  border-right: 1px solid rgba(25,50,100,0.22);
  padding: 26px 17px 20px;
  display: flex; flex-direction: column; gap: 22px;
  z-index: 10;
  backdrop-filter: blur(14px);
  transition: transform 0.22s ease;
}

@media (max-width: 640px) {
  #panel-toggle { display: flex; }
  #panel { transform: translateX(-105%); padding-top: 60px; width: 260px; }
  #panel.open { transform: translateX(0); }
  #corner { display: none; }
}

.panel-wordmark {
  font-size: 8px; letter-spacing: 0.28em;
  color: #1E3355; text-transform: uppercase;
}
.panel-scene-name {
  font-size: 14px; color: #7799CC; letter-spacing: 0.05em; line-height: 1.55;
  margin-top: 4px;
}
.panel-tag {
  font-size: 7.5px; letter-spacing: 0.12em;
  color: #152235; margin-top: 5px;
}

.section-label {
  font-size: 8px; letter-spacing: 0.22em;
  color: #1E3455; text-transform: uppercase; margin-bottom: 8px;
}

/* Source roster */
.roster { display: flex; flex-direction: column; gap: 7px; }
.src-row {
  display: flex; align-items: center; gap: 9px;
  font-size: 10px; color: #5577AA;
}
.src-dot { width: 6px; height: 6px; border-radius: 50%; flex-shrink: 0; }
.src-mass { margin-left: auto; color: #273A55; font-size: 9px; }

/* Layer toggles */
.layers { display: flex; flex-direction: column; gap: 3px; }
.tog {
  display: flex; align-items: center; gap: 8px;
  padding: 6px 9px;
  border: 1px solid rgba(25,50,90,0.25);
  border-radius: 3px;
  cursor: pointer;
  font-size: 9.5px; color: #44607A;
  background: rgba(8,16,34,0.4);
  user-select: none;
  transition: all 0.12s;
}
.tog:hover { border-color: rgba(45,85,160,0.4); color: #7799BB; }
.tog.on  { border-color: rgba(55,100,190,0.38); color: #88AACC; background: rgba(12,24,50,0.5); }
.tog .pip {
  width: 5px; height: 5px; border-radius: 50%;
  background: #122030; flex-shrink: 0;
  transition: background 0.12s;
}
.tog.on .pip { background: currentColor; }

/* Legend */
.legend { display: flex; flex-direction: column; gap: 5px; }
.leg-row { display: flex; align-items: center; gap: 8px; font-size: 8.5px; color: #334455; }
.leg-line { width: 16px; height: 2px; border-radius: 1px; flex-shrink: 0; }

/* Status */
.status {
  margin-top: auto;
  font-size: 8px; color: #1E2D40; line-height: 2.1; letter-spacing: 0.07em;
}
.status-ok { color: #1F4430 !important; }

/* ---- CORNER INFO ---- */
#corner {
  position: fixed; bottom: 16px; right: 16px;
  font-family: 'Space Mono', monospace;
  font-size: 7.5px; color: #162230;
  text-align: right; letter-spacing: 0.12em; line-height: 2;
  z-index: 10; pointer-events: none;
  text-transform: uppercase;
}
</style>
</head>
<body>

<!-- LOADING SCREEN -->
<div id="loading">
  <div class="ld-wordmark">Atlas Solver · Sandbox</div>
  <div class="ld-title">Computing Field Structure</div>
  <div class="ld-bar-wrap"><div class="ld-bar-fill" id="ld-fill"></div></div>
  <div class="ld-stage" id="ld-stage">initializing scene passport</div>
</div>

<!-- PANEL TOGGLE BUTTON (mobile) -->
<button id="panel-toggle" aria-label="Toggle panel">
  <svg viewBox="0 0 16 16" fill="none" stroke="#4466AA" stroke-width="1.5" stroke-linecap="round">
    <line x1="2" y1="4" x2="14" y2="4"/>
    <line x1="2" y1="8" x2="14" y2="8"/>
    <line x1="2" y1="12" x2="14" y2="12"/>
  </svg>
</button>

<!-- LEFT PANEL -->
<div id="panel">
  <div>
    <div class="panel-wordmark">Atlas Solver · Sandbox Mode</div>
    <div class="panel-scene-name">Three-Body<br>Jurisdiction<br>Geometry</div>
    <div class="panel-tag">three_body_jurisdiction_v0_1</div>
  </div>

  <div>
    <div class="section-label">Source Roster · Node 2+</div>
    <div class="roster">
      <div class="src-row">
        <div class="src-dot" style="background:#FF9000"></div>
        S₁ · Node 2
        <span class="src-mass">M = 9</span>
      </div>
      <div class="src-row">
        <div class="src-dot" style="background:#00DDB8"></div>
        S₂ · Node 3
        <span class="src-mass">M = 3</span>
      </div>
      <div class="src-row">
        <div class="src-dot" style="background:#CC77FF"></div>
        S₃ · Node 4
        <span class="src-mass">M = 1</span>
      </div>
    </div>
  </div>

  <div>
    <div class="section-label">Layer Control</div>
    <div class="layers" id="layer-ui">
      <div class="tog on" data-layer="domain">   <span class="pip"></span> Domain Cloud    </div>
      <div class="tog on" data-layer="membrane"> <span class="pip"></span> Parity Membranes</div>
      <div class="tog on" data-layer="tidalRays"><span class="pip"></span> Datum Rays      </div>
      <div class="tog on" data-layer="tidal">    <span class="pip"></span> Tidal E_ij       </div>
      <div class="tog on" data-layer="equi">     <span class="pip"></span> Equipotentials   </div>
      <div class="tog on" data-layer="nodeA">    <span class="pip"></span> Node A Zone      </div>
      <div class="tog on" data-layer="gcs">      <span class="pip"></span> GCS Parity Faces </div>
      <div class="tog on" data-layer="srcs">     <span class="pip"></span> Sources          </div>
      <div class="tog on" data-layer="node1">    <span class="pip"></span> Node 1 Boundary  </div>
    </div>
  </div>

  <div>
    <div class="section-label">Tidal Legend</div>
    <div class="legend">
      <div class="leg-row"><div class="leg-line" style="background:#334466"></div>Datum interrogation rays</div>
      <div class="leg-row"><div class="leg-line" style="background:#FF5533"></div>Tidal stretch (geodesic dev.)</div>
      <div class="leg-row"><div class="leg-line" style="background:#3355CC"></div>Tidal squeeze (transverse)</div>
      <div class="leg-row"><div class="leg-line" style="background:linear-gradient(90deg,#FF9000,#00DDB8)"></div>GCS parity face (blended)</div>
      <div class="leg-row"><div class="leg-line" style="background:linear-gradient(90deg,#FFD700,#FFF)"></div>Node A — contested zone</div>
      <div class="leg-row"><div class="leg-line" style="background:#0D2240; border:1px solid #1A3A60"></div>Node 1 — null exterior</div>
    </div>
  </div>

  <div class="status">
    <div>REGIME · WEAK-FIELD STATIC SLICE</div>
    <div>FIELD · E_ij ELECTRIC WEYL TENSOR</div>
    <div>UNITS · G = c = 1</div>
    <div>GRID · 36³ MAIN · OMNI-RADIAL TIDAL</div>
    <div>DATUMS · NODE 0 + D_SRC × 3 · 96 RAYS · 10 STEPS</div>
    <div>NODE 0 · BARYCENTER (ORIGIN)</div>
    <div>NODE 1 · NULL EXTERIOR — DECLARED ✓</div>
    <div id="status-txt" style="margin-top:5px">STATUS · COMPUTING</div>
  </div>
</div>

<!-- CORNER LABELS -->
<div id="corner">
  DRAG · ROTATE &nbsp;·&nbsp; SCROLL · ZOOM<br>
  RED = TIDAL STRETCH &nbsp;·&nbsp; BLUE = TIDAL SQUEEZE<br>
  WHITE GLOW = NODE A ZONE (CONTESTED JURISDICTION)<br>
  Q CAN POINT &nbsp;·&nbsp; GR MUST DECIDE
</div>

<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
<script>
// ================================================================
//  ATLAS · THREE-BODY JURISDICTION GEOMETRY
//  Scene passport:
//    Name:        three_body_jurisdiction_v0_1
//    Mode:        sandbox / internal seed
//    Regime:      weak-field static slice, declared Newtonian metric
//                 perturbation h_mu_nu in Newtonian gauge
//    Units:       G = 1, c = 1, dimensionless masses
//    Coordinates: Cartesian, approximately barycenter-centered
//    Domain:      [-4.5, 4.5]^3
//    Grid:        48^3 main, 16^3 tidal sublattice
//    Softening:   eps = 0.25
//    Node -1:     relational ledger (computed in-memory)
//    Node 0:      barycenter datum (origin)
//    Node 1:      null exterior / asymptotic flatness
//    Node 2:      S1, mass = 9
//    Node 3:      S2, mass = 3
//    Node 4:      S3, mass = 1
//    Field plan:  Phi_i -> H_ab = d_a d_b Phi -> E_ab = H_ab - (1/3)delta_ab tr(H)
//    Extraction:  domain coloring, parity membranes, E_ij eigenstructure,
//                 equipotentials, Node A zone
//    Claim status: sandbox / internal seed
//
//  LAYER LAW: Rendering communicates. Rendering does not decide.
//  Q can point. GR must decide.
// ================================================================

// ---- SCENE PASSPORT · SOURCE DECLARATIONS ----

const SOURCES = [
  { id: 0, mass: 9, pos: [-0.70,  0.20, -0.10], name: 'S₁', rgb: [1.000, 0.565, 0.000] },
  { id: 1, mass: 3, pos: [ 1.00, -0.50,  0.30], name: 'S₂', rgb: [0.000, 0.867, 0.722] },
  { id: 2, mass: 1, pos: [ 2.00,  0.10, -0.35], name: 'S₃', rgb: [0.800, 0.467, 1.000] },
];

const P = {
  eps:          0.25,
  N_main:       36,
  N_tidal:      12,
  L:            4.5,
  nodeA_thresh: 0.15,
  phi_levels:   [{ lv: -3, tol: 0.22 }, { lv: -8, tol: 0.55 }, { lv: -20, tol: 1.4 }],
};

// ================================================================
//  FIELD MATHEMATICS
// ================================================================

// Q_i: legacy Atlas scalar (tidal proxy)
function qField(x, y, z, src) {
  const dx = x - src.pos[0], dy = y - src.pos[1], dz = z - src.pos[2];
  const r2 = dx*dx + dy*dy + dz*dz + P.eps*P.eps;
  return src.mass / (r2 * Math.sqrt(r2));
}

// Gravitational potential Phi = -sum_i M_i / r_{i,eps}
function phiField(x, y, z) {
  let phi = 0;
  for (const s of SOURCES) {
    const dx = x-s.pos[0], dy = y-s.pos[1], dz = z-s.pos[2];
    phi -= s.mass / Math.sqrt(dx*dx + dy*dy + dz*dz + P.eps*P.eps);
  }
  return phi;
}

// Hessian H_ab = d_a d_b Phi = sum_i M_i [delta_ab/r^3 - 3*d_a*d_b/r^5]
// Returns Float64Array[9], row-major
function hessian(x, y, z) {
  const H = new Float64Array(9);
  const e2 = P.eps * P.eps;
  for (const s of SOURCES) {
    const d = [x - s.pos[0], y - s.pos[1], z - s.pos[2]];
    const r2 = d[0]*d[0] + d[1]*d[1] + d[2]*d[2] + e2;
    const r  = Math.sqrt(r2);
    const r3i = 1.0 / (r2 * r);
    const r5i = r3i / r2;
    const M = s.mass;
    for (let a = 0; a < 3; a++)
      for (let b = 0; b < 3; b++)
        H[a*3+b] += M * ((a===b ? r3i : 0.0) - 3.0*d[a]*d[b]*r5i);
  }
  return H;
}

// Electric Weyl E_ab = H_ab - (1/3) delta_ab tr(H)
// Traceless tidal tensor on the spatial slice
function electricWeyl(H) {
  const E = new Float64Array(H);
  const tr = H[0] + H[4] + H[8];
  E[0] -= tr/3; E[4] -= tr/3; E[8] -= tr/3;
  return E;
}

// ================================================================
//  EIGENDECOMPOSITION: real symmetric 3x3 (Kopp analytical method)
// ================================================================

function cross3(a, b) {
  return [a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0]];
}
function mag3(v) { return Math.sqrt(v[0]*v[0]+v[1]*v[1]+v[2]*v[2]); }
function norm3(v) { const m = mag3(v); return m > 1e-13 ? [v[0]/m,v[1]/m,v[2]/m] : [1,0,0]; }

function eigenvecFor(E9, lam) {
  const M = [
    [E9[0]-lam, E9[1],     E9[2]    ],
    [E9[3],     E9[4]-lam, E9[5]    ],
    [E9[6],     E9[7],     E9[8]-lam]
  ];
  const c = [cross3(M[0],M[1]), cross3(M[0],M[2]), cross3(M[1],M[2])];
  let best = c[0], bm = mag3(c[0]);
  for (let i = 1; i < 3; i++) { const m = mag3(c[i]); if (m > bm) { best = c[i]; bm = m; } }
  return norm3(best);
}

// Returns { vals:[l1,l2,l3] sorted descending, vecs:[[v1],[v2],[v3]] }
function eigensolve3(E9) {
  const a=E9[0], b=E9[1], c=E9[2], d=E9[4], e=E9[5], f=E9[8];
  const p1 = b*b + c*c + e*e;
  let vals;

  if (p1 < 1e-20) {
    vals = [a, d, f];
  } else {
    const q  = (a+d+f) / 3.0;
    const p2 = (a-q)*(a-q) + (d-q)*(d-q) + (f-q)*(f-q) + 2.0*p1;
    const p  = Math.sqrt(p2 / 6.0);
    const ip = 1.0 / p;
    const B  = [
      (a-q)*ip, b*ip, c*ip,
       b*ip,  (d-q)*ip, e*ip,
       c*ip,   e*ip, (f-q)*ip
    ];
    let r = (B[0]*(B[4]*B[8]-B[5]*B[7]) - B[1]*(B[3]*B[8]-B[5]*B[6]) + B[2]*(B[3]*B[7]-B[4]*B[6])) * 0.5;
    r = Math.max(-1.0, Math.min(1.0, r));
    const phi = Math.acos(r) / 3.0;
    const PI23 = 2.0*Math.PI/3.0;
    const l1 = q + 2.0*p*Math.cos(phi);
    const l3 = q + 2.0*p*Math.cos(phi + PI23);
    vals = [l1, 3.0*q - l1 - l3, l3];
  }

  vals.sort((x, y) => y - x); // descending
  // vals[0] = max (transverse squeeze), vals[2] = min (radial stretch)
  return { vals, vecs: vals.map(lam => eigenvecFor(E9, lam)) };
}

// ================================================================
//  THREE.JS RENDERER SETUP
// ================================================================

const renderer = new THREE.WebGLRenderer({ antialias: true });
renderer.setPixelRatio(Math.min(devicePixelRatio, 2));
renderer.setSize(window.innerWidth, window.innerHeight);
renderer.setClearColor(0x020509);
document.body.appendChild(renderer.domElement);

const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(46, window.innerWidth/window.innerHeight, 0.01, 200);

// ---- CAMERA CONTROLLER ----
const CAM = { theta: 0.55, phi: 1.05, r: 10.5 };
function camSync() {
  const { theta, phi, r } = CAM;
  camera.position.set(r*Math.sin(phi)*Math.sin(theta), r*Math.cos(phi), r*Math.sin(phi)*Math.cos(theta));
  camera.lookAt(0, 0, 0);
}
camSync();

let drag = false, lastMouse = { x: 0, y: 0 };
renderer.domElement.addEventListener('mousedown', e => { drag = true; lastMouse = { x: e.clientX, y: e.clientY }; });
window.addEventListener('mouseup',   () => drag = false);
window.addEventListener('mousemove', e => {
  if (!drag) return;
  CAM.theta -= (e.clientX - lastMouse.x) * 0.008;
  CAM.phi    = Math.max(0.05, Math.min(Math.PI-0.05, CAM.phi + (e.clientY - lastMouse.y) * 0.008));
  lastMouse  = { x: e.clientX, y: e.clientY };
  camSync();
});
renderer.domElement.addEventListener('wheel', e => {
  CAM.r = Math.max(3, Math.min(28, CAM.r + e.deltaY * 0.015));
  camSync();
  e.preventDefault();
}, { passive: false });

// Touch support
let lastTouch = null, lastPinchDist = null;
renderer.domElement.addEventListener('touchstart', e => {
  if (e.touches.length === 1) { drag = true; lastMouse = { x: e.touches[0].clientX, y: e.touches[0].clientY }; }
  if (e.touches.length === 2) { lastPinchDist = Math.hypot(e.touches[0].clientX-e.touches[1].clientX, e.touches[0].clientY-e.touches[1].clientY); }
  e.preventDefault();
}, { passive: false });
renderer.domElement.addEventListener('touchend', () => { drag = false; lastPinchDist = null; });
renderer.domElement.addEventListener('touchmove', e => {
  if (e.touches.length === 1 && drag) {
    CAM.theta -= (e.touches[0].clientX - lastMouse.x) * 0.008;
    CAM.phi    = Math.max(0.05, Math.min(Math.PI-0.05, CAM.phi + (e.touches[0].clientY - lastMouse.y) * 0.008));
    lastMouse  = { x: e.touches[0].clientX, y: e.touches[0].clientY };
    camSync();
  }
  if (e.touches.length === 2 && lastPinchDist !== null) {
    const d = Math.hypot(e.touches[0].clientX-e.touches[1].clientX, e.touches[0].clientY-e.touches[1].clientY);
    CAM.r = Math.max(3, Math.min(28, CAM.r * (lastPinchDist / d)));
    lastPinchDist = d;
    camSync();
  }
  e.preventDefault();
}, { passive: false });

window.addEventListener('resize', () => {
  camera.aspect = window.innerWidth / window.innerHeight;
  camera.updateProjectionMatrix();
  renderer.setSize(window.innerWidth, window.innerHeight);
});

// ---- LIGHTING ----
scene.add(new THREE.AmbientLight(0x0D1A33, 3.0));
const sunLight = new THREE.DirectionalLight(0xffffff, 1.4);
sunLight.position.set(5, 10, 6);
scene.add(sunLight);
const fillLight = new THREE.DirectionalLight(0x334466, 0.5);
fillLight.position.set(-4, -3, -5);
scene.add(fillLight);

// ================================================================
//  LAYER REGISTRY
// ================================================================

const OBJ = {};
const VIS = { domain: true, membrane: true, tidalRays: true, tidal: true, equi: true, nodeA: true, gcs: true, srcs: true, node1: true };

// Panel toggle (mobile)
document.getElementById('panel-toggle').addEventListener('click', () => {
  document.getElementById('panel').classList.toggle('open');
});
// Tap canvas → close panel on mobile
renderer.domElement.addEventListener('touchstart', () => {
  document.getElementById('panel').classList.remove('open');
}, { passive: true });

document.getElementById('layer-ui').querySelectorAll('.tog').forEach(el => {
  el.addEventListener('click', () => {
    const k = el.dataset.layer;
    VIS[k] = !VIS[k];
    el.classList.toggle('on', VIS[k]);
    if (OBJ[k]) OBJ[k].visible = VIS[k];
  });
});

// ================================================================
//  PROGRESS
// ================================================================

function progress(pct, stage) {
  document.getElementById('ld-fill').style.width = pct + '%';
  document.getElementById('ld-stage').textContent = stage;
}

function wait(ms) { return new Promise(r => setTimeout(r, ms)); }

// ================================================================
//  STARFIELD
// ================================================================

function buildStars() {
  const N = 3500;
  const pos = new Float32Array(N * 3);
  for (let i = 0; i < N; i++) {
    const r = 45 + Math.random() * 25;
    const th = Math.random() * Math.PI * 2;
    const ph = Math.acos(2 * Math.random() - 1);
    pos[i*3]   = r * Math.sin(ph) * Math.cos(th);
    pos[i*3+1] = r * Math.sin(ph) * Math.sin(th);
    pos[i*3+2] = r * Math.cos(ph);
  }
  const geo = new THREE.BufferGeometry();
  geo.setAttribute('position', new THREE.Float32BufferAttribute(pos, 3));
  scene.add(new THREE.Points(geo, new THREE.PointsMaterial({
    color: 0xAABBDD, size: 0.1, transparent: true, opacity: 0.35, sizeAttenuation: true,
  })));
}

// ================================================================
//  MAIN COMPUTATION
// ================================================================

async function run() {
  try {
    await wait(80);
    progress(3, 'scene passport declared — allocating arrays');
    await wait(25);

    const { N_main: N, N_tidal: Nt, L, nodeA_thresh, phi_levels } = P;
    const step = 2 * L / N;
    const N3   = N * N * N;

    // ---- ALLOCATE ----
    const domLabel  = new Uint8Array(N3);
    const dom2Label = new Uint8Array(N3);
    const marginArr = new Float32Array(N3);
    const phiArr    = new Float32Array(N3);

    progress(8, 'computing Q-field dominance and gravitational potential');

    // ---- MAIN GRID PASS (chunked — yield every 4 z-slices) ----
    for (let iz = 0; iz < N; iz++) {
      if (iz % 4 === 0) {
        progress(8 + (iz/N)*20, 'computing Q-field and potential — slice ' + iz + '/' + N);
        await wait(0);
      }
      for (let iy = 0; iy < N; iy++) {
        for (let ix = 0; ix < N; ix++) {
          const x   = -L + (ix + 0.5) * step;
          const y   = -L + (iy + 0.5) * step;
          const z   = -L + (iz + 0.5) * step;
          const idx = iz*N*N + iy*N + ix;

          let qMax = -1, q2nd = -1, dom = 0, dom2 = 0;
          for (let s = 0; s < SOURCES.length; s++) {
            const q = qField(x, y, z, SOURCES[s]);
            if (q > qMax) { q2nd = qMax; dom2 = dom; qMax = q; dom = s; }
            else if (q > q2nd) { q2nd = q; dom2 = s; }
          }
          domLabel[idx]  = dom;
          dom2Label[idx] = dom2;
          marginArr[idx] = qMax > 0 ? (qMax - q2nd) / qMax : 1.0;
          phiArr[idx]    = phiField(x, y, z);
        }
      }
    }

    progress(30, 'detecting parity membrane boundaries');
    await wait(25);

    // ---- MEMBRANE DETECTION ----
    const isMem = new Uint8Array(N3);
    for (let iz = 0; iz < N; iz++) {
      for (let iy = 0; iy < N; iy++) {
        for (let ix = 0; ix < N; ix++) {
          const i  = iz*N*N + iy*N + ix;
          const L0 = domLabel[i];
          if (
            (ix > 0   && domLabel[i-1]   !== L0) ||
            (ix < N-1 && domLabel[i+1]   !== L0) ||
            (iy > 0   && domLabel[i-N]   !== L0) ||
            (iy < N-1 && domLabel[i+N]   !== L0) ||
            (iz > 0   && domLabel[i-N*N] !== L0) ||
            (iz < N-1 && domLabel[i+N*N] !== L0)
          ) isMem[i] = 1;
        }
      }
    }

    progress(48, 'omni-radial datum interrogation — E_ij electric Weyl');
    await wait(25);

    // ---- OMNI-RADIAL DATUM INTERROGATION ----
    // Atlas doctrine: Node 0 + source-associated interrogation datums
    // Each datum launches antipodal Fibonacci rays outward.
    // E_ij is evaluated at each radial ladder step along each ray.
    // The ledger records: sample position, E_ij eigenvalues, eigenvectors, launching datum.
    //
    // Datums declared:
    //   D_0     — Node 0, barycenter (origin)
    //   D_src_i — source-associated datum at each source position (3 total)
    //
    // Sources speak. Datums listen. The ledger remembers.

    const N_RAYS   = 96;  // antipodal Fibonacci pairs — must be even
    const N_LADDER = 10;  // radial steps per ray
    const SRC_EXCL = 0.20 * 0.20;  // exclusion radius^2 near any source

    // Antipodal Fibonacci direction set
    function fibAntipodal(n) {
      const dirs = [], half = n >> 1;
      const ga = Math.PI * (3 - Math.sqrt(5)); // golden angle
      for (let i = 0; i < half; i++) {
        const th = ga * i;
        const cp = 1 - (2*i + 1) / n;
        const sp = Math.sqrt(Math.max(0, 1 - cp*cp));
        const d  = [sp*Math.cos(th), cp, sp*Math.sin(th)];
        dirs.push(d, [-d[0], -d[1], -d[2]]);
      }
      return dirs;
    }

    // Log-linear radial ladder
    function logLadder(rMin, rMax, n) {
      const steps = [];
      for (let i = 0; i < n; i++) {
        const t = n > 1 ? i / (n - 1) : 0;
        steps.push(rMin * Math.pow(rMax / rMin, t));
      }
      return steps;
    }

    const DIRS = fibAntipodal(N_RAYS);

    // Datum declarations (Node 0 + one per source)
    const DATUMS = [
      { label: 'D_0',     pos: [0,0,0],         rMin: 0.40, rMax: L-0.55, col: [0.28, 0.48, 0.80] },
      { label: 'D_src_1', pos: SOURCES[0].pos,   rMin: 0.22, rMax: 2.20,  col: SOURCES[0].rgb },
      { label: 'D_src_2', pos: SOURCES[1].pos,   rMin: 0.22, rMax: 2.20,  col: SOURCES[1].rgb },
      { label: 'D_src_3', pos: SOURCES[2].pos,   rMin: 0.22, rMax: 2.20,  col: SOURCES[2].rgb },
    ];

    const tidalSamples = []; // ledgered: { x,y,z, vals, vecs, dir, col }
    const raySegs      = []; // { ax,ay,az, bx,by,bz, col }

    const domCutR2 = (L - 0.50) * (L - 0.50);

    for (const datum of DATUMS) {
      const [ox, oy, oz] = datum.pos;
      const ladder = logLadder(datum.rMin, datum.rMax, N_LADDER);

      for (const dir of DIRS) {
        // Record ray segment (rMin → rMax along dir)
        const r0 = ladder[0], r1 = ladder[N_LADDER-1];
        raySegs.push({
          ax: ox+dir[0]*r0, ay: oy+dir[1]*r0, az: oz+dir[2]*r0,
          bx: ox+dir[0]*r1, by: oy+dir[1]*r1, bz: oz+dir[2]*r1,
          col: datum.col,
        });

        // Walk radial ladder — evaluate E_ij at each step
        for (const r of ladder) {
          const x = ox + dir[0]*r;
          const y = oy + dir[1]*r;
          const z = oz + dir[2]*r;

          if (x*x+y*y+z*z > domCutR2) continue;

          // Source exclusion zone (softening artefact region)
          let skip = false;
          for (const s of SOURCES) {
            const dx=x-s.pos[0], dy=y-s.pos[1], dz=z-s.pos[2];
            if (dx*dx+dy*dy+dz*dz < SRC_EXCL) { skip = true; break; }
          }
          if (skip) continue;

          // Field evaluation: Hessian → electric Weyl → eigendecompose
          const H = hessian(x, y, z);
          const E = electricWeyl(H);
          const { vals, vecs } = eigensolve3(E);

          // Ledger entry
          tidalSamples.push({ x, y, z, vals, vecs, dir, col: datum.col });
        }
      }
    }

    progress(65, 'assembling Three.js geometry layers');
    await wait(25);

  // ---- UTILITY: index -> world coords ----
  function xyz(i) {
    const ix = i % N;
    const iy = Math.floor(i / N) % N;
    const iz = Math.floor(i / (N*N));
    return [-L+(ix+0.5)*step, -L+(iy+0.5)*step, -L+(iz+0.5)*step];
  }

  const domainCutR2 = (L - 0.48) * (L - 0.48);

  // ===== 1. DOMAIN CLOUD =====
  // Volume colored by dominant source — the jurisdiction territories
  {
    const pts = [], cols = [];
    const sk = 2; // stride: sample every 2nd voxel per axis
    for (let iz = 0; iz < N; iz += sk) {
      for (let iy = 0; iy < N; iy += sk) {
        for (let ix = 0; ix < N; ix += sk) {
          const i = iz*N*N + iy*N + ix;
          const [x, y, z] = xyz(i);
          if (x*x+y*y+z*z > domainCutR2) continue;
          const c = SOURCES[domLabel[i]].rgb;
          pts.push(x, y, z);
          cols.push(c[0], c[1], c[2]);
        }
      }
    }
    const geo = new THREE.BufferGeometry();
    geo.setAttribute('position', new THREE.Float32BufferAttribute(pts, 3));
    geo.setAttribute('color',    new THREE.Float32BufferAttribute(cols, 3));
    OBJ.domain = new THREE.Points(geo, new THREE.PointsMaterial({
      vertexColors: true, size: 0.048,
      transparent: true, opacity: 0.052,
      depthWrite: false, sizeAttenuation: true,
    }));
    scene.add(OBJ.domain);
  }

  // ===== 2. PARITY MEMBRANES =====
  // Jurisdiction boundaries — the geometry of belonging
  {
    const pts = [], cols = [];
    for (let i = 0; i < N3; i++) {
      if (!isMem[i]) continue;
      const [x, y, z] = xyz(i);
      if (x*x+y*y+z*z > domainCutR2) continue;
      const c = SOURCES[domLabel[i]].rgb;
      pts.push(x, y, z);
      // Brighten membrane points vs domain cloud
      cols.push(Math.min(1, c[0]*1.5+0.12), Math.min(1, c[1]*1.5+0.12), Math.min(1, c[2]*1.5+0.12));
    }
    const geo = new THREE.BufferGeometry();
    geo.setAttribute('position', new THREE.Float32BufferAttribute(pts, 3));
    geo.setAttribute('color',    new THREE.Float32BufferAttribute(cols, 3));
    OBJ.membrane = new THREE.Points(geo, new THREE.PointsMaterial({
      vertexColors: true, size: 0.062,
      transparent: true, opacity: 0.80,
      depthWrite: false, sizeAttenuation: true,
    }));
    scene.add(OBJ.membrane);
  }

  // ===== 3. OMNI-RADIAL TIDAL INTERROGATION =====
  // Datum rays show the lawful interrogation geometry.
  // Eigenvector whiskers at each ladder-step sample show E_ij field.
  // RED   = stretch axis (min eigenvalue) = geodesic deviation direction
  // BLUE  = squeeze axis (max eigenvalue) = transverse compression
  // Orientation of stretch: flipped to align with the launching ray direction (outward from datum)

  // --- 3a. Datum ray lines ---
  {
    const pts = [], cols = [];
    for (const seg of raySegs) {
      const c = seg.col;
      pts.push(seg.ax, seg.ay, seg.az, seg.bx, seg.by, seg.bz);
      cols.push(c[0]*0.30, c[1]*0.30, c[2]*0.30, c[0]*0.30, c[1]*0.30, c[2]*0.30);
    }
    const geo = new THREE.BufferGeometry();
    geo.setAttribute('position', new THREE.Float32BufferAttribute(pts, 3));
    geo.setAttribute('color',    new THREE.Float32BufferAttribute(cols, 3));
    OBJ.tidalRays = new THREE.LineSegments(geo, new THREE.LineBasicMaterial({
      vertexColors: true, transparent: true, opacity: 0.18, depthWrite: false,
    }));
    scene.add(OBJ.tidalRays);
  }

  // --- 3b. E_ij eigenvector whiskers at each sample ---
  {
    let maxAbs = 0;
    for (const s of tidalSamples)
      maxAbs = Math.max(maxAbs, Math.abs(s.vals[0]), Math.abs(s.vals[2]));
    const lScale = 0.36 / (Math.pow(maxAbs, 0.4) + 1e-7);

    const stretchPts = [], squeezePts = [], tipPts = [];

    for (const { x, y, z, vals, vecs, dir } of tidalSamples) {
      // Stretch eigenvector: orient along the interrogation ray direction
      const vs   = vecs[2];
      const sign = (vs[0]*dir[0] + vs[1]*dir[1] + vs[2]*dir[2]) >= 0 ? 1 : -1;
      const ls   = Math.pow(Math.abs(vals[2]), 0.4) * lScale;
      const vsx  = vs[0]*sign, vsy = vs[1]*sign, vsz = vs[2]*sign;

      // Single-headed: short tail, tip at +v
      stretchPts.push(
        x - vsx*ls*0.25, y - vsy*ls*0.25, z - vsz*ls*0.25,
        x + vsx*ls,      y + vsy*ls,      z + vsz*ls
      );
      tipPts.push(x + vsx*ls, y + vsy*ls, z + vsz*ls);

      // Squeeze axis (bidirectional, secondary, dim)
      const lq = Math.pow(Math.abs(vals[0]), 0.4) * lScale * 0.42;
      const vq = vecs[0];
      squeezePts.push(
        x - vq[0]*lq, y - vq[1]*lq, z - vq[2]*lq,
        x + vq[0]*lq, y + vq[1]*lq, z + vq[2]*lq
      );
    }

    const gStr = new THREE.BufferGeometry();
    gStr.setAttribute('position', new THREE.Float32BufferAttribute(stretchPts, 3));
    const gSq  = new THREE.BufferGeometry();
    gSq.setAttribute('position',  new THREE.Float32BufferAttribute(squeezePts, 3));
    const gTip = new THREE.BufferGeometry();
    gTip.setAttribute('position', new THREE.Float32BufferAttribute(tipPts, 3));

    const tGroup = new THREE.Group();
    tGroup.add(new THREE.LineSegments(gStr,
      new THREE.LineBasicMaterial({ color: 0xFF5533, transparent: true, opacity: 0.80 })));
    tGroup.add(new THREE.LineSegments(gSq,
      new THREE.LineBasicMaterial({ color: 0x3355CC, transparent: true, opacity: 0.22 })));
    tGroup.add(new THREE.Points(gTip, new THREE.PointsMaterial({
      color: 0xFF8866, size: 0.055, transparent: true, opacity: 0.85,
      depthWrite: false, sizeAttenuation: true,
    })));
    OBJ.tidal = tGroup;
    scene.add(tGroup);
  }

  // ===== 4. EQUIPOTENTIALS =====
  // Iso-surfaces of the gravitational potential — the "pinch" geometry
  {
    const pts = [], cols = [];
    for (let i = 0; i < N3; i++) {
      const phi = phiArr[i];
      let hit = false;
      for (const { lv, tol } of phi_levels) { if (Math.abs(phi - lv) < tol) { hit = true; break; } }
      if (!hit) continue;
      const [x, y, z] = xyz(i);
      if (x*x+y*y+z*z > domainCutR2) continue;
      pts.push(x, y, z);
      cols.push(0.92, 0.88, 0.65);
    }
    const geo = new THREE.BufferGeometry();
    geo.setAttribute('position', new THREE.Float32BufferAttribute(pts, 3));
    geo.setAttribute('color',    new THREE.Float32BufferAttribute(cols, 3));
    OBJ.equi = new THREE.Points(geo, new THREE.PointsMaterial({
      vertexColors: true, size: 0.05,
      transparent: true, opacity: 0.28,
      depthWrite: false, sizeAttenuation: true,
    }));
    scene.add(OBJ.equi);
  }

  // ===== 5. NODE A ZONE =====
  // Contested jurisdiction: where the dominant source has < 15% margin over the runner-up
  // Brightness encodes degree of contestation (most contested = most intense)
  {
    const pts = [], cols = [];
    for (let i = 0; i < N3; i++) {
      const mg = marginArr[i];
      if (mg > nodeA_thresh) continue;
      const [x, y, z] = xyz(i);
      if (x*x+y*y+z*z > domainCutR2) continue;
      const t = 1.0 - mg / nodeA_thresh; // 0 at threshold edge, 1 at membrane
      pts.push(x, y, z);
      // Gold-white gradient from edge (dim gold) to centre (bright white)
      cols.push(1.0, 0.80 + t*0.20, 0.10 + t*0.60);
    }
    const geo = new THREE.BufferGeometry();
    geo.setAttribute('position', new THREE.Float32BufferAttribute(pts, 3));
    geo.setAttribute('color',    new THREE.Float32BufferAttribute(cols, 3));
    OBJ.nodeA = new THREE.Points(geo, new THREE.PointsMaterial({
      vertexColors: true, size: 0.08,
      transparent: true, opacity: 0.88,
      depthWrite: false, sizeAttenuation: true,
      blending: THREE.AdditiveBlending,
    }));
    scene.add(OBJ.nodeA);
  }

  // ===== 5b. GCS PARITY NETWORK — RETAINED PAIRWISE FACES =====
  // For each pair (i,j): the retained face is voxels where i and j are the top-2 sources
  // AND their Q values are within tolerance (margin < gcs_tol).
  // This is the soap-bubble parity network from GCS II.
  // Each face colored as a blend of its two source colors.
  // Legacy Q readability branch — declared as scaffold, not GR result.
  {
    const GCS_TOL = 0.10; // parity face tolerance — tighter than Node A threshold

    // Pre-compute blended colors for each pair
    const pairColors = {};
    for (let a = 0; a < SOURCES.length; a++) {
      for (let b = a+1; b < SOURCES.length; b++) {
        const ca = SOURCES[a].rgb, cb = SOURCES[b].rgb;
        pairColors[`${a}_${b}`] = [
          (ca[0] + cb[0]) * 0.5,
          (ca[1] + cb[1]) * 0.5,
          (ca[2] + cb[2]) * 0.5,
        ];
      }
    }

    const pts = [], cols = [];
    for (let i = 0; i < N3; i++) {
      if (marginArr[i] > GCS_TOL) continue;
      const [x, y, z] = xyz(i);
      if (x*x+y*y+z*z > domainCutR2) continue;
      const a = domLabel[i], b = dom2Label[i];
      const key = a < b ? `${a}_${b}` : `${b}_${a}`;
      const c = pairColors[key];
      if (!c) continue;
      // Brightness: brightest at parity surface (margin=0), dims outward
      const t = 1.0 - marginArr[i] / GCS_TOL;
      pts.push(x, y, z);
      cols.push(
        Math.min(1, c[0] * (0.7 + t*0.6)),
        Math.min(1, c[1] * (0.7 + t*0.6)),
        Math.min(1, c[2] * (0.7 + t*0.6))
      );
    }
    const geo = new THREE.BufferGeometry();
    geo.setAttribute('position', new THREE.Float32BufferAttribute(pts, 3));
    geo.setAttribute('color',    new THREE.Float32BufferAttribute(cols, 3));
    OBJ.gcs = new THREE.Points(geo, new THREE.PointsMaterial({
      vertexColors: true, size: 0.07,
      transparent: true, opacity: 0.92,
      depthWrite: false, sizeAttenuation: true,
      blending: THREE.AdditiveBlending,
    }));
    scene.add(OBJ.gcs);
  }

  // ===== 6. SOURCE SPHERES =====
  {
    const grp = new THREE.Group();
    for (const s of SOURCES) {
      const R   = Math.pow(s.mass / 9, 1/3) * 0.30;
      const col = new THREE.Color(s.rgb[0], s.rgb[1], s.rgb[2]);
      const [sx, sy, sz] = s.pos;

      // Solid core
      const core = new THREE.Mesh(
        new THREE.SphereGeometry(R, 32, 32),
        new THREE.MeshPhongMaterial({ color: col, emissive: col.clone().multiplyScalar(0.4), shininess: 90 })
      );
      core.position.set(sx, sy, sz);
      grp.add(core);

      // Inner glow halo
      const halo1 = new THREE.Mesh(
        new THREE.SphereGeometry(R * 2.6, 16, 16),
        new THREE.MeshBasicMaterial({ color: col, transparent: true, opacity: 0.055,
          side: THREE.BackSide, depthWrite: false, blending: THREE.AdditiveBlending })
      );
      halo1.position.set(sx, sy, sz);
      grp.add(halo1);

      // Outer diffuse glow
      const halo2 = new THREE.Mesh(
        new THREE.SphereGeometry(R * 5.0, 12, 12),
        new THREE.MeshBasicMaterial({ color: col, transparent: true, opacity: 0.018,
          side: THREE.BackSide, depthWrite: false, blending: THREE.AdditiveBlending })
      );
      halo2.position.set(sx, sy, sz);
      grp.add(halo2);

      // Equatorial ring
      const ring = new THREE.Mesh(
        new THREE.TorusGeometry(R * 1.5, 0.008, 6, 36),
        new THREE.MeshBasicMaterial({ color: col, transparent: true, opacity: 0.30 })
      );
      ring.position.set(sx, sy, sz);
      ring.rotation.x = Math.PI / 2;
      grp.add(ring);
    }

    // Node 0: barycenter marker at origin
    const n0 = new THREE.Mesh(
      new THREE.SphereGeometry(0.04, 12, 12),
      new THREE.MeshBasicMaterial({ color: 0x336699, transparent: true, opacity: 0.6 })
    );
    grp.add(n0); // position defaults to origin

    OBJ.srcs = grp;
    scene.add(grp);
  }

  // ===== AMBIENT GEOMETRY =====
  {
    const L0  = 0.5;
    const ax  = [-L0,0,0, L0,0,0, 0,-L0,0, 0,L0,0, 0,0,-L0, 0,0,L0];
    const geo = new THREE.BufferGeometry();
    geo.setAttribute('position', new THREE.Float32BufferAttribute(ax, 3));
    scene.add(new THREE.LineSegments(geo,
      new THREE.LineBasicMaterial({ color: 0x0A1A30, transparent: true, opacity: 0.7 })));

    // NODE 1: declared parent context — null exterior / asymptotic flatness
    // Rendered as a faint wireframe box at the domain boundary
    const node1Geo = new THREE.EdgesGeometry(new THREE.BoxGeometry(L*2*0.92, L*2*0.92, L*2*0.92));
    OBJ.node1 = new THREE.LineSegments(node1Geo,
      new THREE.LineBasicMaterial({ color: 0x0D2240, transparent: true, opacity: 0.45, depthWrite: false }));
    VIS.node1 = true;
    scene.add(OBJ.node1);
  }

  buildStars();

  // ===== DONE =====
  progress(100, 'complete — ledger built, geometry ready');
  await wait(350);

  document.getElementById('loading').style.display = 'none';
  const st = document.getElementById('status-txt');
  st.textContent = 'STATUS · READY';
  st.className = 'status-ok';

  } catch (err) {
    // Surface any error rather than leaving the loading screen stuck
    document.getElementById('ld-stage').textContent = 'ERROR: ' + err.message;
    document.getElementById('ld-fill').style.background = '#882222';
    console.error('Atlas run() error:', err);
  }
}

// ================================================================
//  ANIMATION LOOP
// ================================================================

let clock = 0;
function animate() {
  requestAnimationFrame(animate);
  clock += 0.013;

  // Pulse Node A zone — contested jurisdiction breathes
  if (OBJ.nodeA && OBJ.nodeA.visible && OBJ.nodeA.material)
    OBJ.nodeA.material.opacity = 0.62 + 0.26 * Math.sin(clock * 2.3);

  renderer.render(scene, camera);
}

animate();
run();
</script>
</body>
</html>
