---
title: Figures & Visualizations
layout: default
---

## Featured Rendering

<div style="width: 100%; text-align: center; margin-bottom: 2rem;">
  <video width="50%" height="auto" controls autoplay loop muted style="border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.3);">
    <source src="images/binaryB_rotation.mp4" type="video/mp4">
    Your browser does not support the video tag.
  </video>
  <p><em>Primary Visualization: 12 star cluster</em></p>
</div>

## Technical Highlights

<div style="display: flex; gap: 15px; justify-content: space-between; margin-bottom: 3rem;">
  <div style="flex: 1; text-align: center;">
    <img src="images/ems_parent_support_slow_rotation_black.gif" alt="Focus A" style="width: 100%; border-radius: 4px;">
    <p><small><strong>Focus A:</strong> Brief caption here.</small></p>
  </div>
  <div style="flex: 1; text-align: center;">
    <img src="images/integrated_handoff_structure.png" alt="Focus B" style="width: 100%; border-radius: 4px;">
    <p><small><strong>Focus B:</strong> Brief caption here.</small></p>
  </div>
  <div style="flex: 1; text-align: center;">
    <video id="focusC" width="100%" autoplay loop muted playsinline style="border-radius: 4px;">
      <source src="images/IMG_4424.mp4" type="video/mp4">
    </video>
    <p><small><strong>Focus C:</strong> Brief caption here.</small></p>
  </div>
</div>

---

## Archive & Supplementary Data

<div style="display: grid; grid-template-columns: repeat(5, 1fr); gap: 10px;">
  <div style="text-align: center;">
    <img src="images/local_patch_extreme_ratio_anisotropy_pass_patch_frame_3d.png" style="width: 100%;">
    <p><small>Fig 01: Caption</small></p>
  </div>
  </div>

<script>
  // Wait for the window to load to ensure the video element is ready
  window.addEventListener('load', function() {
    var vC = document.getElementById('focusC');
    if (vC) {
      vC.playbackRate = 0.25; 
    }
  });
</script>

<div style="margin-top: 2rem; text-align: center;">
  [Back to Hub](/)
</div>
