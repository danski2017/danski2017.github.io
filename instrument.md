---
layout: default
title: Atlas Instrument
permalink: /instrument/
description: Declare a gravitational scene, run the GFRO solver pipeline, and explore curvature structure — parity boundaries, source jurisdictions, and tidal orientation shifts — in an interactive 3D stage.
---

<style>
.instrument-intro {
  padding-bottom: 1.1rem;
  border-bottom: 1px solid #e8e8e8;
  margin-bottom: 0;
}
.instrument-intro h1 {
  margin-top: 0;
  margin-bottom: 0.3rem;
  font-size: 1.65rem;
}
.instrument-intro p {
  font-size: 0.96rem;
  color: #555;
  margin: 0;
  line-height: 1.6;
}
.instrument-panel-wrap {
  /* Break out of .wrapper max-width constraint */
  width: 100vw;
  position: relative;
  left: 50%;
  transform: translateX(-50%);
  overflow: hidden;
  /* Cancel .page-content bottom padding so no gap below panel */
  margin-bottom: -3rem;
}
#atlas-root {
  width: 100%;
  height: 100%;
  /* Custom properties for instrument font stack */
  --font-sans: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif;
  --font-mono: ui-monospace, 'Cascadia Code', 'Source Code Pro', Menlo, Consolas, monospace;
}
</style>

<div class="instrument-intro">
  <h1>Atlas Instrument</h1>
  <p>Declare a gravitational scene, run the GFRO solver pipeline, and explore curvature structure — parity boundaries, source jurisdictions, and tidal orientation shifts — in an interactive 3D stage.</p>
</div>

<div class="instrument-panel-wrap" id="instrument-wrap">
  <div id="atlas-root"></div>
</div>

<script src="https://unpkg.com/react@18/umd/react.production.min.js" crossorigin></script>
<script src="https://unpkg.com/react-dom@18/umd/react-dom.production.min.js" crossorigin></script>
<script src="https://unpkg.com/three@0.128.0/build/three.min.js"></script>
<script src="https://unpkg.com/@babel/standalone/babel.min.js"></script>
<script>
(function () {
  // Size the instrument panel to fill exactly the viewport below the intro
  function sizePanel() {
    var intro = document.querySelector('.instrument-intro');
    var wrap  = document.getElementById('instrument-wrap');
    if (!wrap) return;
    var usedPx = intro ? Math.round(intro.getBoundingClientRect().bottom) : 0;
    wrap.style.height = 'calc(100vh - ' + usedPx + 'px)';
  }
  sizePanel();
  window.addEventListener('resize', sizePanel);

  // Fetch, patch, transpile, and render the instrument JSX
  fetch('/atlas-solver/atlas_instrument_v0_2.jsx')
    .then(function (r) { return r.text(); })
    .then(function (code) {
      // Replace ES module imports with global references from CDN builds
      code = code
        .replace(
          /^import\s+\{\s*([^}]+)\s*\}\s+from\s+['"]react['"];?\s*$/gm,
          function (_, names) { return 'const { ' + names.trim() + ' } = React;'; }
        )
        .replace(/^import\s+\*\s+as\s+THREE\s+from\s+['"]three['"];?\s*$/gm, '')
        .replace(/^export\s+default\s+/gm, '');

      // Mount into the dedicated container
      code += '\nReactDOM.createRoot(document.getElementById("atlas-root")).render(React.createElement(AtlasInstrument));';

      var transpiled = Babel.transform(code, { presets: ['react'] }).code;
      var s = document.createElement('script');
      s.text = transpiled;
      document.body.appendChild(s);
    })
    .catch(function () {
      var root = document.getElementById('atlas-root');
      if (root) {
        root.innerHTML = '<p style="color:#888;padding:32px;font-family:system-ui,sans-serif;font-size:14px;">Atlas Instrument failed to load. Please refresh or try again.</p>';
      }
    });
})();
</script>
