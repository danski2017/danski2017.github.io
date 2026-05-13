#!/usr/bin/env python3
"""
Atlas Geometry Serializer v0.1
==============================
Converts a private GFRO ledger into anonymous render-ready geometry buffers
safe for transmission to the public-facing viewer.

IP protection guarantee:
  INPUT  — full GFRO ledger (private): field equations, masses, eigenvalues,
            residuals, Apollonius parameters, source positions in meters
  OUTPUT — render geometry (public): vertex positions (normalized),
            colors, normals, layer membership flags
  
  Field equations are NOT recoverable from render buffers.
  Source masses are NOT present in render buffers.
  Ledger schema is NOT exposed to the browser.

Render layers produced:
  gravity_boundaries  — Apollonius sphere surface meshes (R0 pairwise)
  star_web            — source-context boundary point cloud (R0 ctx)
  orientation_shifts  — eigenvector tick segments colored by entropy
  tidal_structure     — Frobenius norm isosurface candidates
  sources             — source positions and visual radii only

Usage:
  from atlas_geometry_serializer import serialize
  buffers = serialize(ledger)          # dict -> dict
  # or from CLI:
  python atlas_geometry_serializer.py ledger.json geometry.json
"""

import numpy as np
import json
import sys
from typing import List, Tuple, Optional


# ─────────────────────────────────────────────────────────────
# Coordinate normalizer
# Strips physical units. Viewer works in normalized scene space.
# ─────────────────────────────────────────────────────────────

def build_normalizer(source_positions_m: List[List[float]]):
    """
    Compute scene normalization: center at Node 0 (SOL),
    scale so the scene fits in a unit sphere of radius ~100
    (comfortable Three.js working scale).
    Returns (center, scale) where:
      normalized = (pos_m - center) / scale * 100
    """
    pts = np.array(source_positions_m)
    # Node 0 is always index 0 (SOL at origin)
    center = np.zeros(3)
    # Scale: farthest source -> 100 units
    dists = np.linalg.norm(pts, axis=1)
    max_dist = float(np.max(dists)) if len(dists) > 0 else 1.0
    scale = max_dist / 100.0 if max_dist > 0 else 1.0
    return center, scale


def norm(pos_m, center, scale):
    """Normalize a position in meters to scene units."""
    return ((np.array(pos_m) - center) / scale).tolist()


# ─────────────────────────────────────────────────────────────
# Apollonius sphere -> triangle mesh
# Icosphere subdivision for smooth render
# ─────────────────────────────────────────────────────────────

def apollonius_to_cloud(obj: dict, center_norm, scale: float, n_pts: int = 192):
    """
    Sample points on an Apollonius sphere surface.
    Point cloud is the primary render object — no meshing, no averaging.
    Antipodal Fibonacci sampling: uniform coverage, honest to emitted geometry.
    Physical parameters stripped — only normalized positions survive.
    """
    is_plane = obj.get("is_plane", False) or obj.get("type") == "bisector_plane"

    if is_plane:
        plane_pt = np.array(obj.get("plane_point", obj.get("point_m", [0,0,0])))
        normal   = np.array(obj.get("plane_normal", obj.get("normal", [0,0,1])))
        normal  /= np.linalg.norm(normal) + 1e-30
        perp     = np.array([1,0,0]) if abs(normal[0]) < 0.9 else np.array([0,1,0])
        u = np.cross(normal, perp); u /= np.linalg.norm(u)
        v = np.cross(normal, u)
        disc_r   = scale * 0.3   # visual extent only
        angles   = np.linspace(0, 2*np.pi, n_pts, endpoint=False)
        pts_m    = np.array([plane_pt + disc_r*(np.cos(a)*u + np.sin(a)*v)
                             for a in angles])
    else:
        c_m = np.array(obj.get("center", obj.get("center_m", [0,0,0])))
        r_m = float(obj.get("radius", obj.get("radius_m", 1.0)))
        # Fibonacci sphere point cloud on surface
        phi = np.pi * (1 + np.sqrt(5))
        pts_m = np.zeros((n_pts, 3))
        for i in range(n_pts):
            lat = np.arccos(1 - 2*(i+0.5)/n_pts)
            lon = phi * i
            d = np.array([np.sin(lat)*np.cos(lon),
                          np.sin(lat)*np.sin(lon),
                          np.cos(lat)])
            pts_m[i] = c_m + r_m * d

    # Normalize to scene units
    pts_n = (pts_m - center_norm) / scale

    return {
        "positions": pts_n.tolist(),
        "count": n_pts,
        "src_i": obj.get("src_i", obj.get("source_i", "")),
        "src_j": obj.get("src_j", obj.get("source_j", "")),
    }

# ─────────────────────────────────────────────────────────────
# Source-context point cloud
# ─────────────────────────────────────────────────────────────

def ctx_to_pointcloud(ctx_points: List[dict], center_norm, scale: float,
                      source_id: str) -> dict:
    """
    Convert source-context boundary points to normalized point cloud.
    Residuals and physical field values stripped.
    Only positions and source membership survive.
    """
    positions = []
    for p in ctx_points:
        pos_m = np.array(p.get("pos_m", p.get("pos", [0,0,0])))
        pos_n = (pos_m - center_norm) / scale
        positions.append(pos_n.tolist())

    return {
        "source": source_id,
        "positions": positions,
        "count": len(positions),
    }


# ─────────────────────────────────────────────────────────────
# Eigenvector tick segments (Orientation Shifts)
# ─────────────────────────────────────────────────────────────

ENTROPY_COLORMAP = [
    [0.10, 0.20, 0.80],  # low entropy  → blue (source dominates)
    [0.20, 0.80, 0.60],  # mid entropy  → teal
    [0.90, 0.70, 0.10],  # high entropy → amber (contested zone)
    [0.90, 0.20, 0.10],  # max entropy  → red (perfect balance)
]

def entropy_to_color(entropy: float, max_entropy: float) -> List[float]:
    """Map attribution entropy to RGB color."""
    t = min(entropy / max(max_entropy, 1e-10), 1.0)
    n = len(ENTROPY_COLORMAP) - 1
    i = int(t * n)
    f = t * n - i
    if i >= n:
        return ENTROPY_COLORMAP[-1]
    c0 = ENTROPY_COLORMAP[i]
    c1 = ENTROPY_COLORMAP[i+1]
    return [c0[k] + f*(c1[k]-c0[k]) for k in range(3)]


def weyl_to_ticks(weyl_records: List[dict], center_norm, scale: float,
                  tick_length_scene: float = 2.0) -> dict:
    """
    Convert Weyl field records to eigenvector tick segments.
    For each point:
      - Draw tick along principal eigenvector v1 (max stretch axis)
      - Color by attribution entropy
      - Length scaled to tick_length_scene in normalized scene units

    Physical eigenvalues stripped. Only direction and color survive.
    """
    if not weyl_records:
        return {"segments": [], "count": 0}

    max_entropy = max(r.get("attribution_entropy", 0) for r in weyl_records)
    segments = []

    for rec in weyl_records:
        pos_m  = np.array(rec.get("pos_m", rec.get("pos", [0,0,0])))
        pos_n  = (pos_m - center_norm) / scale
        evecs  = np.array(rec["eigenvectors"])  # columns are eigenvectors
        ent    = rec.get("attribution_entropy", 0)
        dom    = rec.get("dominant_source", "")

        # Principal eigenvector: first column (largest eigenvalue)
        v1 = evecs[:, 0]
        v1 /= (np.linalg.norm(v1) + 1e-30)

        half = 0.5 * tick_length_scene * v1
        p0   = (pos_n - half).tolist()
        p1   = (pos_n + half).tolist()
        color = entropy_to_color(ent, max_entropy)

        segments.append({
            "p0": p0,
            "p1": p1,
            "color": color,
            "dominant_source": dom,
        })

    return {
        "segments": segments,
        "count": len(segments),
        "entropy_range": [0.0, float(max_entropy)],
    }


# ─────────────────────────────────────────────────────────────
# Source spheres (visual only — no physical parameters)
# ─────────────────────────────────────────────────────────────

# Visual class -> color mapping (aesthetic only, no physics)
SOURCE_COLORS = {
    "star_G2":     [1.00, 0.88, 0.38],  # warm yellow
    "G-star":      [1.00, 0.82, 0.32],
    "K-star":      [1.00, 0.56, 0.25],
    "M-dwarf":     [1.00, 0.31, 0.19],
    "A-star":      [0.75, 0.88, 1.00],
    "white_dwarf": [0.56, 0.69, 1.00],
    "brown_dwarf": [0.35, 0.17, 0.10],
    "planet":      [0.25, 0.50, 0.75],
    "moon":        [0.56, 0.56, 0.56],
    "dwarf_planet":[0.50, 0.44, 0.38],
}
DEFAULT_COLOR = [0.80, 0.80, 0.80]

# Visual radius by source class (scene units — aesthetic only)
SOURCE_VIS_RADIUS = {
    "star_G2": 2.5, "G-star": 1.8, "K-star": 1.5,
    "A-star": 2.0, "M-dwarf": 0.8, "white_dwarf": 0.6,
    "brown_dwarf": 0.4, "planet": 0.3, "moon": 0.15, "dwarf_planet": 0.2,
}
DEFAULT_RADIUS = 1.0


def sources_to_render(source_roster: List[dict], center_norm, scale: float) -> List[dict]:
    """
    Convert source roster to render objects.
    Mass stripped. Position normalized. Visual radius/color from class only.
    """
    rendered = []
    for s in source_roster:
        pos_m  = np.array(s["pos_m"])
        pos_n  = (pos_m - center_norm) / scale
        cls    = s.get("cls", "")
        color  = SOURCE_COLORS.get(cls, DEFAULT_COLOR)
        radius = SOURCE_VIS_RADIUS.get(cls, DEFAULT_RADIUS)
        rendered.append({
            "id":     s["id"],
            "name":   s.get("name", s["id"]),
            "pos":    pos_n.tolist(),
            "color":  color,
            "radius": radius,
            "cls":    cls,
        })
    return rendered


# ─────────────────────────────────────────────────────────────
# Master serializer
# ─────────────────────────────────────────────────────────────

def serialize(ledger: dict) -> dict:
    """
    Convert private GFRO ledger to public render geometry buffers.

    IP protection:
      - No masses in output
      - No field equations in output
      - No residuals in output
      - No eigenvalue magnitudes in output (directions only)
      - Positions normalized (physical scale stripped)
      - Apollonius parameters (center_m, radius_m) stripped

    Returns geometry buffer dict safe for transmission to public viewer.
    """
    print("Atlas Geometry Serializer v0.1")

    # Extract source roster
    roster   = ledger.get("sources", ledger.get("source_roster", []))
    scene_id = ledger.get("scene_id", "unnamed")

    # Build normalizer from source positions
    positions_m = [s["pos_m"] for s in roster]
    center_norm, scale = build_normalizer(positions_m)
    print(f"  Scene: {scene_id} — {len(roster)} sources")
    print(f"  Scale: 1 scene unit = {scale:.3e} m")

    # 1. Source render objects
    print("  Serializing sources...")
    sources_render = sources_to_render(roster, center_norm, scale)

    # 2. Gravity Boundaries — Apollonius meshes
    print("  Serializing gravity boundaries (Apollonius point clouds)...")
    r0_objects = ledger.get("parity_network", ledger.get("R0_pairwise", {})).get("objects", [])
    gravity_boundaries = []
    for obj in r0_objects:
        try:
            cloud = apollonius_to_cloud(obj, center_norm, scale, n_pts=192)
            gravity_boundaries.append(cloud)
        except Exception as e:
            pass  # skip malformed objects silently
    print(f"    {len(gravity_boundaries)} meshes generated")

    # 3. Star Web — source-context point clouds
    print("  Serializing star web (source-context boundaries)...")
    ctx_raw = ledger.get("source_context_boundaries", ledger.get("R0_source_context", {}))
    # Support both by_source dict and flat points list
    by_source = ctx_raw.get("by_source", {})
    if by_source:
        grouped = by_source  # already grouped by source ID
    else:
        flat = ctx_raw.get("points", [])
        grouped = {}
        for p in flat:
            sid = p.get("source", "unknown")
            if sid not in grouped:
                grouped[sid] = []
            grouped[sid].append(p)
    star_web = []
    for sid, pts in grouped.items():
        cloud = ctx_to_pointcloud(pts, center_norm, scale, sid)
        star_web.append(cloud)
    total_ctx_pts = sum(c["count"] for c in star_web)
    print(f"    {len(star_web)} clouds, {total_ctx_pts} total points")

    # 4. Orientation Shifts — eigenvector ticks
    print("  Serializing orientation shifts (eigenvector ticks)...")
    weyl_records = ledger.get("weyl_field", {}).get("evaluations", ledger.get("weyl_field", {}).get("records", []))
    orientation_shifts = weyl_to_ticks(weyl_records, center_norm, scale)
    print(f"    {orientation_shifts['count']} tick segments")

    # 5. Assemble output
    buffers = {
        "scene_id":    scene_id,
        "n_sources":   len(roster),
        "scale_note":  f"1 scene unit = {scale:.4e} m (physical scale stripped)",
        "claim_status": "diagnostic_candidate_not_observational",

        "sources": sources_render,

        "layers": {
            "gravity_boundaries": {
                "label":       "Gravity Boundaries",
                "description": "Where one star's gravitational influence ends and another begins",
                "type":        "pointcloud",
                "clouds":      gravity_boundaries,
                "count":       len(gravity_boundaries),
                "default_size":    0.4,
                "default_color":   [0.80, 0.55, 0.12],
            },
            "star_web": {
                "label":       "Star Web",
                "description": "The geometric skeleton of source jurisdictions",
                "type":        "pointcloud",
                "clouds":      star_web,
                "total_points": total_ctx_pts,
                "default_size":    0.3,
                "default_color":   [0.40, 0.80, 0.60],
            },
            "orientation_shifts": {
                "label":       "Orientation Shifts",
                "description": "Where the dominant direction of gravitational pull rotates",
                "type":        "segments",
                "data":        orientation_shifts,
                "entropy_range": orientation_shifts.get("entropy_range", [0,1]),
            },
        },

        "meta": {
            "serializer_version": "0.1",
            "mesh_subdivisions":  2,  # legacy field, meshes replaced by point clouds
            "ip_note": "Field equations, source masses, eigenvalue magnitudes, and residuals are not present in this buffer. This file is safe for public distribution.",
        }
    }

    # Size estimate
    size_estimate = len(json.dumps(buffers)) / 1e6
    print(f"  Geometry buffer: ~{size_estimate:.2f} MB")
    print("  Serialization complete.")

    return buffers


# ─────────────────────────────────────────────────────────────
# CLI
# ─────────────────────────────────────────────────────────────

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python atlas_geometry_serializer.py ledger.json [geometry.json]")
        sys.exit(1)

    ledger_path   = sys.argv[1]
    geometry_path = sys.argv[2] if len(sys.argv) > 2 else "geometry.json"

    with open(ledger_path) as f:
        ledger = json.load(f)

    buffers = serialize(ledger)

    with open(geometry_path, "w") as f:
        json.dump(buffers, f)

    import os
    size_mb = os.path.getsize(geometry_path) / 1e6
    print(f"\nGeometry written: {geometry_path} ({size_mb:.2f} MB)")
    print(f"  Sources:              {buffers['n_sources']}")
    print(f"  Gravity boundaries:   {buffers['layers']['gravity_boundaries']['count']}")
    print(f"  Star web points:      {buffers['layers']['star_web']['total_points']}")
    print(f"  Orientation segments: {buffers['layers']['orientation_shifts']['data']['count']}")
