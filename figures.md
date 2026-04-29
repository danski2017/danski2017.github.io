---
title: Figures & Visualizations
layout: default
---

## Featured Rendering

<div style="width: 100%; text-align: center; margin-bottom: 2rem;">
  <video width="50%" height="auto" controls autoplay loop muted style="border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.3);">
    <source src="images/mutual network rotate.mov" type="video/mp4">
    Your browser does not support the video tag.
  </video>
  <p><em>Primary Visualization: 12 star cluster</em></p>
</div>

---

## Technical Highlights

<div style="display: flex; gap: 15px; justify-content: space-between; margin-bottom: 3rem;">
  <div style="flex: 1; text-align: center;">
    <img src="images/ems_parent_support_slow_rotation_black.gif" alt="Focus A" style="width: 100%; border-radius: 4px;">
    <p><small><strong>Focus A:</strong> Localized Parity Surface</small></p>
  </div>
  
  <div style="flex: 1; text-align: center;">
    <img src="images/integrated_handoff_structure.png" alt="Focus B" style="width: 100%; border-radius: 4px;">
    <p><small><strong>Focus B:</strong> Integrated Handoff Mapping</small></p>
  </div>
  
  <div style="flex: 1; text-align: center;">
    <video id="focusC" width="100%" height="auto" autoplay loop muted playsinline style="border-radius: 4px; display: block;">
      <source src="images/binaryB_rotation.mov" type="video/mp4">
      Your browser does not support the video tag.
    </video>
    <p><small><strong>Focus C:</strong> High-Resolution Diagnostic</small></p>
  </div>
</div>

---

## Archive & Supplementary Data

<div style="display: grid; grid-template-columns: repeat(5, 1fr); gap: 10px;">
  <div style="text-align: center;">
    <img src="images/local_patch_extreme_ratio_anisotropy_pass_patch_frame_3d.png" style="width: 100%;">
    <p><small>Fig 01</small></p>
  </div>
  <div style="text-align: center;">
    <img src="images/frame_0000.png" style="width: 100%;">
    <p><small>Fig 02</small></p>
  </div>
  <div style="text-align: center;">
    <img src="images/frame_0001.png" style="width: 100%;">
    <p><small>Fig 03</small></p>
  </div>
  <div style="text-align: center;">
    <img src="images/frame_0002.png" style="width: 100%;">
    <p><small>Fig 04</small></p>
  </div>
  <div style="text-align: center;">
    <img src="images/frame_0003.png" style="width: 100%;">
    <p><small>Fig 05</small></p>
  </div>
</div>

<script>
  window.addEventListener('load', function() {
    var vC = document.getElementById('focusC');
    if (vC) {
      vC.playbackRate = 0.25; 
    }
  });
</script>

<div style="margin-top: 3rem; text-align: center;">
  [Back to Hub](/)
</div>
