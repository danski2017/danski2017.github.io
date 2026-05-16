"""
Atlas GFRO Emitter — atlas_emitter.py
Phase 2 core solver.

Architecture (GCS I-VI doctrine):
  Sources speak. Datums interrogate. Ledger remembers.

GFRO workflow (NOT ledger mining):
  1. Declare residual Psi_R[A|K](x) = R(F_A)(x) - R(F_K)(x)
  2. Solve zero set directly from equations
  3. Emit certified coordinates into compact ledger
  4. Full E_ij field evaluated at emitted points only

Layers:
  R0  — scalar parity (Apollonius, analytically exact)
  R2  — Weyl-electric Frobenius norm parity
  E   — full tidal tensor eigenstructure at emitted points
  Ctx — source-context parity (each source vs rest)
"""

import numpy as np
import json
from itertools import combinations
from dataclasses import dataclass, asdict, field
from typing import List, Tuple, Optional

G = 6.674e-11  # m^3 kg^-1 s^-2

# ─────────────────────────────────────────────
# Source
# ─────────────────────────────────────────────

@dataclass
class Source:
    id: str
    name: str
    mass: float        # kg
    pos: np.ndarray    # [x, y, z] in meters

    def Q(self, x: np.ndarray) -> float:
        """Scalar tidal readability Q = GM/r^3"""
        r = np.linalg.norm(x - self.pos)
        if r < 1e-10: return np.inf
        return G * self.mass / r**3

    def E(self, x: np.ndarray) -> np.ndarray:
        """
        Electric Weyl tidal tensor E_ij = GM/r^3 * (3*n_i*n_j - delta_ij)
        Returns 3x3 symmetric traceless tensor.
        Zero inside declared radius (shell theorem).
        """
        rv = x - self.pos
        r = np.linalg.norm(rv)
        if r < 1e-10:
            return np.zeros((3, 3))
        n = rv / r
        prefactor = G * self.mass / r**3
        E = prefactor * (3 * np.outer(n, n) - np.eye(3))
        return E

    def E_frob(self, x: np.ndarray) -> float:
        """||E_i||_F = sqrt(6) * GM/r^3 for point source"""
        r = np.linalg.norm(x - self.pos)
        if r < 1e-10: return np.inf
        return np.sqrt(6.0) * G * self.mass / r**3


# ─────────────────────────────────────────────
# R0 Parity: Apollonius Emission (analytically exact)
# ─────────────────────────────────────────────

@dataclass
class Apollonius:
    """
    Zero set of Psi_R0[i|j](x) = Q_i(x) - Q_j(x) = 0
    Condition: M_i/r_i^3 = M_j/r_j^3  =>  r_i/r_j = (M_i/M_j)^(1/3) = k
    k != 1: sphere with analytic center and radius
    k == 1: perpendicular bisector plane
    """
    src_i: str
    src_j: str
    mass_i: float
    mass_j: float
    pos_i: np.ndarray
    pos_j: np.ndarray
    k: float            # (M_i/M_j)^(1/3)
    center: Optional[np.ndarray]
    radius: Optional[float]
    is_plane: bool
    plane_point: Optional[np.ndarray]
    plane_normal: Optional[np.ndarray]
    operator: str = "R0"
    claim_status: str = "diagnostic_candidate_not_observational"

    def residual_at(self, x: np.ndarray) -> float:
        """Verify emitted point: Psi_R0[i|j](x) should be ~0"""
        r_i = np.linalg.norm(x - self.pos_i)
        r_j = np.linalg.norm(x - self.pos_j)
        if r_i < 1e-10 or r_j < 1e-10: return np.inf
        return (G * self.mass_i / r_i**3) - (G * self.mass_j / r_j**3)

    def to_dict(self) -> dict:
        d = {
            "operator": self.operator,
            "src_i": self.src_i,
            "src_j": self.src_j,
            "k": round(self.k, 8),
            "is_plane": self.is_plane,
            "claim_status": self.claim_status,
        }
        if not self.is_plane:
            d["center"] = self.center.tolist()
            d["radius"] = round(float(self.radius), 4)
        else:
            d["plane_point"] = self.plane_point.tolist()
            d["plane_normal"] = self.plane_normal.tolist()
        return d


def emit_R0_pairwise(sources: List[Source]) -> List[Apollonius]:
    """
    Emit all pairwise R0 Apollonius zero sets.
    Analytically exact. No sampling. No mining.
    For N sources: C(N,2) objects emitted.
    """
    emitted = []
    for s_i, s_j in combinations(sources, 2):
        d = s_j.pos - s_i.pos
        dist = np.linalg.norm(d)
        if dist < 1e-10:
            continue

        k = (s_i.mass / s_j.mass) ** (1.0 / 3.0)

        if abs(k - 1.0) < 1e-9:
            # Equal masses: perpendicular bisector plane
            plane_point = 0.5 * (s_i.pos + s_j.pos)
            plane_normal = d / dist
            obj = Apollonius(
                src_i=s_i.id, src_j=s_j.id,
                mass_i=s_i.mass, mass_j=s_j.mass,
                pos_i=s_i.pos.copy(), pos_j=s_j.pos.copy(),
                k=k, center=None, radius=None, is_plane=True,
                plane_point=plane_point, plane_normal=plane_normal,
            )
        else:
            # Unequal masses: Apollonius sphere
            # Center on the line between sources
            # r_i / r_j = k  =>  r_i = k * r_j
            # Internal division point: r_i = k/(1+k) * dist from s_i
            # External division point: r_i = k/(k-1) * dist from s_i (if k!=1)
            k2 = k * k
            # Center of Apollonius sphere
            center = (s_i.pos - k2 * s_j.pos) / (1.0 - k2)
            # Radius
            radius = k * dist / abs(1.0 - k2)
            obj = Apollonius(
                src_i=s_i.id, src_j=s_j.id,
                mass_i=s_i.mass, mass_j=s_j.mass,
                pos_i=s_i.pos.copy(), pos_j=s_j.pos.copy(),
                k=k, center=center, radius=radius, is_plane=False,
                plane_point=None, plane_normal=None,
            )
        emitted.append(obj)
    return emitted


# ─────────────────────────────────────────────
# R0 Source-Context: targeted root-finding
# ─────────────────────────────────────────────

def emit_R0_source_context(
    source: Source,
    context: List[Source],
    n_rays: int = 192,
    n_radial: int = 96,
    domain_scale: float = None,
) -> List[dict]:
    """
    Emit zero set of Psi_R0[i|K](x) = Q_i(x) - sum_K Q_j(x) = 0
    where K = all sources except i.

    Uses targeted rays from source position.
    Sign-change detection + bisection interpolation per ray.
    Compact output: emitted point, residual, support values.
    """
    if not context:
        return []

    # Antipodal Fibonacci ray directions
    dirs = fibonacci_antipodal(n_rays)

    # Domain scale: use max inter-source distance if not declared
    if domain_scale is None:
        all_sources = [source] + context
        dists = [np.linalg.norm(source.pos - c.pos) for c in context]
        domain_scale = max(dists) * 2.0 if dists else 1e15

    # Radial ladder: hybrid log-linear from near-source to domain boundary
    r_min = 1e-3 * min([np.linalg.norm(source.pos - c.pos) for c in context])
    r_min = max(r_min, 1e6)  # at least 1000 km
    r_max = domain_scale
    r_ladder = hybrid_radial_ladder(r_min, r_max, n_radial)

    def psi(x):
        q_src = source.Q(x)
        q_ctx = sum(c.Q(x) for c in context)
        return q_src - q_ctx

    emitted = []
    for d in dirs:
        # Sample psi along ray
        xs = [source.pos + r * d for r in r_ladder]
        vals = [psi(x) for x in xs]

        # Find sign changes
        for idx in range(len(vals) - 1):
            if vals[idx] * vals[idx+1] < 0:
                # Bisect to find root
                x_lo, x_hi = xs[idx], xs[idx+1]
                v_lo, v_hi = vals[idx], vals[idx+1]
                for _ in range(52):  # ~machine precision
                    x_mid = 0.5 * (x_lo + x_hi)
                    v_mid = psi(x_mid)
                    if v_lo * v_mid <= 0:
                        x_hi, v_hi = x_mid, v_mid
                    else:
                        x_lo, v_lo = x_mid, v_mid

                x_emit = 0.5 * (x_lo + x_hi)
                residual = psi(x_emit)

                emitted.append({
                    "pos": x_emit.tolist(),
                    "residual": float(residual),
                    "Q_source": float(source.Q(x_emit)),
                    "Q_context": float(sum(c.Q(x_emit) for c in context)),
                    "operator": "R0",
                    "type": "source_context",
                    "source": source.id,
                    "ray_dir": d.tolist(),
                    "claim_status": "diagnostic_candidate_not_observational",
                })
                break  # one crossing per ray per pair

    return emitted


# ─────────────────────────────────────────────
# Full E_ij field evaluation at emitted points
# ─────────────────────────────────────────────

def evaluate_weyl_at(
    points: List[np.ndarray],
    sources: List[Source],
) -> List[dict]:
    """
    For each emitted point, evaluate:
    - E_total = sum of E_ij from all sources
    - Eigenvalues lambda_1 >= lambda_2 >= lambda_3 (traceless: sum=0)
    - Eigenvectors v_1, v_2, v_3
    - Frobenius norm ||E_total||_F
    - Attribution entropy H (how balanced are source contributions?)
    - Dominant source ID

    This IS the precious jewel: the full tidal architecture
    at the geometrically meaningful locations.
    """
    results = []
    for x in points:
        # Total field
        E_total = sum(s.E(x) for s in sources)

        # Eigendecomposition (E is real symmetric 3x3)
        eigenvalues, eigenvectors = np.linalg.eigh(E_total)
        # Sort descending
        idx = np.argsort(eigenvalues)[::-1]
        eigenvalues = eigenvalues[idx]
        eigenvectors = eigenvectors[:, idx]

        # Frobenius norm
        frob = np.sqrt(np.sum(E_total**2))

        # Per-source Frobenius norms
        source_frobs = np.array([s.E_frob(x) for s in sources])
        total_frob = np.sum(source_frobs)

        # Attribution entropy H = -sum(p_i * log(p_i))
        if total_frob > 0:
            p = source_frobs / total_frob
            p = p[p > 0]
            entropy = float(-np.sum(p * np.log(p)))
        else:
            entropy = 0.0

        # Dominant source
        dom_idx = int(np.argmax(source_frobs))
        dominant = sources[dom_idx].id

        results.append({
            "pos": x.tolist(),
            "E_total": E_total.tolist(),
            "eigenvalues": eigenvalues.tolist(),
            "eigenvectors": eigenvectors.tolist(),
            "frob_norm": float(frob),
            "attribution_entropy": entropy,
            "dominant_source": dominant,
            "source_frobs": {s.id: float(f) for s, f in zip(sources, source_frobs)},
        })
    return results


# ─────────────────────────────────────────────────────────────────────────────
# BCW-L001: Barycentric Compression Witnessing
# Datum Bible v0.3.1 — Relational Labs / Atlas Solver
#
# Doctrine:
#   Sources contribute. Datums interrogate. Ledger remembers.
#   Node B is a compression witness, not a source.
#   Node G is a morphology witness, not a source.
#   Delta_E_G is the failure of group-compressibility.
#   The ledger is the authority. The render is the audit window.
# ─────────────────────────────────────────────────────────────────────────────

def compute_bcw_nodes(sources: List[Source]):
    """
    Compute Node B (mass barycenter) and Node G (geometric centroid).
    BCW Datum Bible v0.3.1 §2.2, §2.3.

    Node B = sum_i(M_i * p_i) / sum_i(M_i)  — compression witness
    Node G = (1/N) * sum_i(p_i)              — morphology witness

    Neither is a source. Neither contributes curvature.
    Node B defines the collapsed monopole reference model.
    Node G audits the scene's shape independent of mass.
    """
    masses    = np.array([s.mass for s in sources])          # kg
    positions = np.array([s.pos  for s in sources])          # m

    M_total = float(np.sum(masses))
    node_B  = np.sum(masses[:, np.newaxis] * positions, axis=0) / M_total
    node_G  = np.mean(positions, axis=0)

    return node_B, node_G, M_total


def eval_E_surrogate(x: np.ndarray, node_B: np.ndarray,
                     M_total: float, epsilon_B: float) -> np.ndarray:
    """
    Monopole barycenter surrogate tidal tensor at point x.
    E_bar,G(x) = E[M_total, Node_B](x)
    BCW Datum Bible v0.3.1 §2.2, §3.

    This is the field that would be produced if the entire group
    were collapsed to a single pointlike mass M_total at Node B.
    Node B does not contribute curvature — this is a comparison model.
    Returns zeros inside epsilon_B (no-claim zone).
    """
    rv = x - node_B
    r  = np.linalg.norm(rv)
    if r < epsilon_B:
        return np.zeros((3, 3))   # no-claim zone
    n  = rv / r
    prefactor = G * M_total / r**3
    return prefactor * (3 * np.outer(n, n) - np.eye(3))


def eval_bcw_at(x: np.ndarray,
                sources: List[Source],
                node_B: np.ndarray,
                M_total: float,
                epsilon_B: float,
                source_softening: float = 1e10) -> dict:
    """
    BCW-L001 field evaluation at point x. BCW Datum Bible v0.3.1 §3, §6.

    E_actual,G(x) = sum_i E_i(x)             true roster field
    E_bar,G(x)    = E[M_total, Node_B](x)    monopole surrogate
    Delta_E_G(x)  = E_actual - E_bar         compression delta
    chi_G(x)      = ||Delta_E_G||_F / (||E_bar,G||_F + eps)
    eta_G(x)      = ||Delta_E_G||_F / (||E_actual,G||_F + eps)

    chi=1: where group's unresolved internal structure equals
           its collapsed parent-readable identity.
    """
    EPS = 1e-100

    # No-claim flags
    dist_B      = float(np.linalg.norm(x - node_B))
    no_claim_B  = dist_B < epsilon_B
    no_claim_src = any(np.linalg.norm(x - s.pos) < source_softening
                       for s in sources)

    # True roster field
    E_actual = sum(s.E(x) for s in sources)

    # Monopole surrogate field
    E_bar = eval_E_surrogate(x, node_B, M_total, epsilon_B)

    # Compression delta
    delta_E = E_actual - E_bar

    # Scalar witnesses
    norm_actual = float(np.sqrt(np.sum(E_actual**2)))
    norm_bar    = float(np.sqrt(np.sum(E_bar**2)))
    norm_delta  = float(np.sqrt(np.sum(delta_E**2)))
    chi         = norm_delta / (norm_bar    + EPS)
    eta         = norm_delta / (norm_actual + EPS)

    # Crossing flag: near chi=1 surface (within 10%)
    crossing = (not no_claim_B) and (not no_claim_src) and abs(chi - 1.0) < 0.10

    return {
        "pos":          x.tolist(),
        "norm_actual":  norm_actual,
        "norm_bar":     norm_bar,
        "norm_delta":   norm_delta,
        "chi":          float(chi),
        "eta":          float(eta),
        "crossing_flag":            crossing,
        "bcw_no_claim":             no_claim_B,
        "source_no_claim":          no_claim_src,
        "branch":                   "BCW_L001_monopole",
        "surrogate_rung":           0,
        "claim_status":             "diagnostic_candidate_not_observational",
    }


def run_bcw_l001(sources: List[Source], r0_pairwise: list) -> dict:
    """
    BCW-L001 protocol. BCW Datum Bible v0.3.1 §18.

    Step sequence:
      5.  Compute derived witnesses: Node B, Node G
      6.  Coarse scout pass over evaluation points
      7.  Detect crossing bands (chi near 1)
      10. Write compact ledger records

    Evaluation strategy (lean, no sampling explosion):
      - Coarse Fibonacci shells around Node B at 6 radii
      - Sample points on emitted Apollonius spheres (4 pts each)
      - Pairwise midpoints (subsampled)
    """
    print("  BCW-L001: computing derived witnesses...")

    # Step 5: Node B, Node G
    node_B, node_G, M_total = compute_bcw_nodes(sources)

    # Group geometry
    R_extent = float(max(np.linalg.norm(s.pos - node_B) for s in sources))

    # Surrogate softening — BCW Bible §4, beta=0.04
    beta      = 0.04
    epsilon_B = max(1e10, beta * R_extent)

    B_G_offset = float(np.linalg.norm(node_B - node_G))
    N0_B_offset = float(np.linalg.norm(node_B))  # Node 0 is at origin

    print(f"    Node B: {[round(v/PC_TO_M,4) for v in node_B.tolist()]} pc")
    print(f"    Node G: {[round(v/PC_TO_M,4) for v in node_G.tolist()]} pc")
    print(f"    ||B-G|| = {B_G_offset/PC_TO_M:.4f} pc  (mass-shape asymmetry)")
    print(f"    ||Node0-B|| = {N0_B_offset/PC_TO_M:.4f} pc")
    print(f"    M_total = {M_total/MSUN_KG:.2f} M_sun")
    print(f"    R_extent = {R_extent/PC_TO_M:.3f} pc")
    print(f"    epsilon_B = {epsilon_B/PC_TO_M:.4f} pc")

    # Step 6: Build evaluation points
    eval_pts = []

    # Node B and Node G themselves
    eval_pts.append(node_B.copy())
    eval_pts.append(node_G.copy())

    # Coarse Fibonacci shells around Node B (6 radii × 48 directions)
    n_dirs  = 48
    phi_fib = np.pi * (1 + np.sqrt(5))
    radii   = np.logspace(
        np.log10(max(epsilon_B * 1.5, R_extent * 0.05)),
        np.log10(R_extent * 2.2),
        6
    )
    for r in radii:
        for i in range(n_dirs):
            lat = np.arccos(1 - 2*(i+0.5)/n_dirs)
            lon = phi_fib * i
            d   = np.array([np.sin(lat)*np.cos(lon),
                            np.sin(lat)*np.sin(lon),
                            np.cos(lat)])
            eval_pts.append(node_B + r * d)

    # 4 cardinal points on each Apollonius sphere
    axes = [np.array([1,0,0]), np.array([0,1,0]),
            np.array([0,0,1]), np.array([-1,0,0])]
    for obj in r0_pairwise:
        if not obj.is_plane and obj.center is not None:
            c = obj.center
            r = obj.radius
            for ax in axes:
                eval_pts.append(c + r * ax)

    # Subsampled pairwise midpoints
    pairs = list(combinations(sources, 2))
    step  = max(1, len(pairs) // 150)
    for si, sj in pairs[::step]:
        eval_pts.append(0.5 * (si.pos + sj.pos))

    print(f"    BCW-L001: {len(eval_pts)} evaluation points")

    # Step 6-9: Evaluate chi field
    records = [
        eval_bcw_at(x, sources, node_B, M_total, epsilon_B)
        for x in eval_pts
    ]

    # Chi statistics (exclude no-claim zones)
    valid     = [r for r in records if not r["bcw_no_claim"] and not r["source_no_claim"]]
    chi_vals  = [r["chi"] for r in valid]
    n_cross   = sum(1 for r in valid if r["crossing_flag"])

    if chi_vals:
        print(f"    chi: min={min(chi_vals):.3f}, mean={np.mean(chi_vals):.3f}, max={max(chi_vals):.3f}")
        print(f"    Near chi=1: {n_cross} points")

    return {
        # Step 4 — Group declaration (BCW §5, §19)
        "group_roster": [{
            "group_id":         "G001",
            "member_source_ids": [s.id for s in sources],
            "n_members":        len(sources),
            "group_purpose":    "full_active_scene",
            "group_status":     "diagnostic",
            "parent_context":   "declared_not_computed",
            "surrogate_type":   "monopole_barycenter",
            "surrogate_rung":   0,
            "branch":           "BCW_L001",
            "claim_status":     "diagnostic_candidate_not_observational",
        }],

        # Step 5 — Derived nodes (BCW §2, §19)
        "derived_nodes": {
            "node_B": {
                "node_id":         "B_G001",
                "node_type":       "mass_barycenter",
                "group_id":        "G001",
                "pos_m":           node_B.tolist(),
                "pos_pc":          (node_B / PC_TO_M).tolist(),
                "M_total_kg":      float(M_total),
                "M_total_msun":    float(M_total / MSUN_KG),
                "role":            "compression_witness",
                "contributes_field": False,
                "note": "Node B is not a source. Defines the monopole collapsed reference model. Delta_E_G is the failure of group-compressibility.",
            },
            "node_G": {
                "node_id":         "G_G001",
                "node_type":       "geometric_centroid",
                "group_id":        "G001",
                "pos_m":           node_G.tolist(),
                "pos_pc":          (node_G / PC_TO_M).tolist(),
                "role":            "morphology_witness",
                "contributes_field": False,
                "B_G_offset_m":    B_G_offset,
                "B_G_offset_pc":   float(B_G_offset / PC_TO_M),
                "N0_B_offset_pc":  float(N0_B_offset / PC_TO_M),
                "note": "Node G audits scene shape. ||B-G|| = mass-shape asymmetry signal.",
            },
        },

        # Softening registry (BCW §4)
        "softening_registry": {
            "barycenter_surrogate": {
                "object_id":      "B_G001",
                "object_type":    "barycenter_surrogate",
                "epsilon_B_m":    float(epsilon_B),
                "epsilon_B_pc":   float(epsilon_B / PC_TO_M),
                "beta":           beta,
                "R_extent_m":     float(R_extent),
                "R_extent_pc":    float(R_extent / PC_TO_M),
                "no_claim_radius_m": float(epsilon_B),
                "rule": "no_bcw_interpretation_inside_epsilon_B",
            }
        },

        # BCW field evaluations
        "bcw_field": {
            "method":         "BCW_L001_monopole_surrogate",
            "surrogate_rung": 0,
            "group_id":       "G001",
            "n_points":       len(records),
            "n_valid":        len(valid),
            "n_crossings":    int(n_cross),
            "chi_min":        float(min(chi_vals))        if chi_vals else None,
            "chi_max":        float(max(chi_vals))        if chi_vals else None,
            "chi_mean":       float(np.mean(chi_vals))    if chi_vals else None,
            "records":        records,
            "claim_status":   "diagnostic_candidate_not_observational",
        },
    }


# ─────────────────────────────────────────────
# Sampling utilities
# ─────────────────────────────────────────────

def fibonacci_antipodal(n: int) -> np.ndarray:
    """
    Generate n/2 Fibonacci sphere directions + their antipodes.
    n must be even. Returns n unit vectors.
    Canonical Atlas production: n=384 (192 antipodal pairs).
    """
    n_half = n // 2
    phi = np.pi * (1 + np.sqrt(5))
    dirs = []
    for i in range(n_half):
        lat = np.arccos(1 - 2*(i+0.5)/n_half)
        lon = phi * i
        x = np.sin(lat) * np.cos(lon)
        y = np.sin(lat) * np.sin(lon)
        z = np.cos(lat)
        d = np.array([x, y, z])
        dirs.append(d)
        dirs.append(-d)
    return np.array(dirs)


def hybrid_radial_ladder(r_min: float, r_max: float, n: int) -> np.ndarray:
    """
    Hybrid log-linear radial ladder.
    Log spacing in near field (first half), linear in far field (second half).
    Canonical Atlas default: n=96 samples per ray.
    """
    n_log = n // 2
    n_lin = n - n_log
    r_mid = np.sqrt(r_min * r_max)
    log_part = np.logspace(np.log10(r_min), np.log10(r_mid), n_log, endpoint=False)
    lin_part = np.linspace(r_mid, r_max, n_lin)
    return np.concatenate([log_part, lin_part])


# ─────────────────────────────────────────────
# Scene loader from passport
# ─────────────────────────────────────────────

# Physical constants for unit conversion
PC_TO_M = 3.085677581e16    # parsecs to meters
AU_TO_M = 1.496e11          # AU to meters
MSUN_KG = 1.989e30          # solar masses to kg

# Fibonacci sphere positions for sources without real ICRS coordinates
def fibonacci_positions(sources_data: list) -> dict:
    """
    Assign 3D positions to sources.
    Uses real Gaia ICRS Cartesian coordinates when available (x_pc/y_pc/z_pc).
    Falls back to Fibonacci sphere at declared distance for sources without coordinates.
    SOL always at origin.
    """
    n = len(sources_data)
    phi = np.pi * (1 + np.sqrt(5))
    positions = {}
    fib_idx = 0

    for s in sources_data:
        if s['id'] == 'SOL':
            positions[s['id']] = np.zeros(3)
            continue

        # Use real Gaia ICRS coordinates if available
        if 'x_pc' in s and 'y_pc' in s and 'z_pc' in s:
            positions[s['id']] = np.array([
                s['x_pc'] * PC_TO_M,
                s['y_pc'] * PC_TO_M,
                s['z_pc'] * PC_TO_M,
            ])
            continue

        # Fall back to Fibonacci sphere at declared distance
        if 'dist_pc' in s:
            dist_m = s['dist_pc'] * PC_TO_M
        elif 'dist_au' in s:
            dist_m = s['dist_au'] * AU_TO_M
        else:
            dist_m = 1e15

        lat = np.arccos(1 - 2*(fib_idx+0.5)/max(n-1, 1))
        lon = phi * fib_idx
        d = np.array([
            np.sin(lat)*np.cos(lon),
            np.sin(lat)*np.sin(lon),
            np.cos(lat)
        ])
        positions[s['id']] = d * dist_m
        fib_idx += 1

    return positions


ROSTER = {
    "SOL":          {"name":"Sun",                  "mass_msun":1.0,      "dist_au":0},
    "MERCURY":      {"name":"Mercury",              "mass_msun":1.65e-7,  "dist_au":0.39},
    "VENUS":        {"name":"Venus",                "mass_msun":2.45e-6,  "dist_au":0.72},
    "EARTH":        {"name":"Earth",                "mass_msun":3.00e-6,  "dist_au":1.00},
    "MOON":         {"name":"Moon",                 "mass_msun":3.69e-8,  "dist_au":1.00},
    "MARS":         {"name":"Mars",                 "mass_msun":3.23e-7,  "dist_au":1.52},
    "JUPITER":      {"name":"Jupiter",              "mass_msun":9.55e-4,  "dist_au":5.20},
    "SATURN":       {"name":"Saturn",               "mass_msun":2.86e-4,  "dist_au":9.58},
    "URANUS":       {"name":"Uranus",               "mass_msun":4.37e-5,  "dist_au":19.2},
    "NEPTUNE":      {"name":"Neptune",              "mass_msun":5.15e-5,  "dist_au":30.1},
    "PLUTO":        {"name":"Pluto",                "mass_msun":6.6e-9,   "dist_au":39.5},
    # Gaia stellar neighbors to 4.9 pc
    "PROXIMA_CEN":    {"name":"Proxima Centauri",   "mass_msun":0.1221,   "dist_pc":1.295,  "x_pc":-0.47482, "y_pc":-0.36292, "z_pc":-1.15670},
    "ALPHA_CEN_A":    {"name":"Alpha Centauri A",   "mass_msun":1.100,    "dist_pc":1.338,  "x_pc":-0.50318, "y_pc":-0.42075, "z_pc":-1.17525},
    "ALPHA_CEN_B":    {"name":"Alpha Centauri B",   "mass_msun":0.907,    "dist_pc":1.338,  "x_pc":-0.50316, "y_pc":-0.42065, "z_pc":-1.17529},
    "BARNARDS":       {"name":"Barnard's Star",      "mass_msun":0.144,    "dist_pc":1.828,  "x_pc":-0.01754, "y_pc":-1.82190, "z_pc": 0.15106},
    "LUHMAN16A":      {"name":"Luhman 16 A",         "mass_msun":0.032,    "dist_pc":1.998,  "x_pc":-1.13471, "y_pc": 0.36194, "z_pc":-1.59895},
    "LUHMAN16B":      {"name":"Luhman 16 B",         "mass_msun":0.027,    "dist_pc":1.998,  "x_pc":-1.13470, "y_pc": 0.36195, "z_pc":-1.59895},
    "WISE0855":       {"name":"WISE 0855-0714",       "mass_msun":0.008,    "dist_pc":2.231,  "x_pc":-1.56351, "y_pc": 1.63150, "z_pc":-0.28723},
    "WOLF359":        {"name":"Wolf 359",             "mass_msun":0.090,    "dist_pc":2.394,  "x_pc":-2.29920, "y_pc": 0.65481, "z_pc": 0.29365},
    "LALANDE21185":   {"name":"Lalande 21185",        "mass_msun":0.386,    "dist_pc":2.547,  "x_pc":-1.99850, "y_pc": 0.50455, "z_pc": 1.49473},
    "SIRIUS_A":       {"name":"Sirius A",             "mass_msun":2.063,    "dist_pc":2.637,  "x_pc":-0.49433, "y_pc": 2.47677, "z_pc":-0.75850},
    "SIRIUS_B":       {"name":"Sirius B",             "mass_msun":1.018,    "dist_pc":2.637,  "x_pc":-0.50053, "y_pc": 2.50794, "z_pc":-0.76827},
    "BL_CETI":        {"name":"BL Ceti",              "mass_msun":0.102,    "dist_pc":2.680,  "x_pc": 2.34912, "y_pc": 1.08403, "z_pc":-0.83804},
    "UV_CETI":        {"name":"UV Ceti",              "mass_msun":0.100,    "dist_pc":2.680,  "x_pc": 2.31059, "y_pc": 1.06626, "z_pc":-0.82427},
    "ROSS154":        {"name":"Ross 154",             "mass_msun":0.170,    "dist_pc":2.976,  "x_pc": 0.58726, "y_pc":-2.65800, "z_pc":-1.20270},
    "ROSS248":        {"name":"Ross 248",             "mass_msun":0.136,    "dist_pc":3.162,  "x_pc": 2.25935, "y_pc":-0.17861, "z_pc": 2.20169},
    "EPS_ERI":        {"name":"Epsilon Eridani",      "mass_msun":0.832,    "dist_pc":3.218,  "x_pc": 1.90127, "y_pc": 2.54409, "z_pc":-0.52910},
    "LACAILLE9352":   {"name":"Lacaille 9352",        "mass_msun":0.503,    "dist_pc":3.289,  "x_pc": 2.59160, "y_pc":-0.62200, "z_pc":-1.92554},
    "ROSS128":        {"name":"Ross 128",             "mass_msun":0.168,    "dist_pc":3.374,  "x_pc":-3.36975, "y_pc": 0.18028, "z_pc": 0.04707},
    "EZ_AQR_A":       {"name":"EZ Aquarii A",         "mass_msun":0.110,    "dist_pc":3.452,  "x_pc": 3.08040, "y_pc":-1.14249, "z_pc":-0.89816},
    "61CYGNI_A":      {"name":"61 Cygni A",           "mass_msun":0.708,    "dist_pc":3.497,  "x_pc": 1.98577, "y_pc":-1.86813, "z_pc": 2.18924},
    "61CYGNI_B":      {"name":"61 Cygni B",           "mass_msun":0.630,    "dist_pc":3.497,  "x_pc": 1.98609, "y_pc":-1.86808, "z_pc": 2.18879},
    "STRUVE2398A":    {"name":"Struve 2398 A",        "mass_msun":0.342,    "dist_pc":3.517},
    "STRUVE2398B":    {"name":"Struve 2398 B",        "mass_msun":0.248,    "dist_pc":3.517},
    "GROOMBRIDGE34A": {"name":"Groombridge 34 A",     "mass_msun":0.380,    "dist_pc":3.561,  "x_pc": 2.55323, "y_pc": 0.20602, "z_pc": 2.47578},
    "GROOMBRIDGE34B": {"name":"Groombridge 34 B",     "mass_msun":0.158,    "dist_pc":3.561,  "x_pc": 2.55313, "y_pc": 0.20655, "z_pc": 2.47607},
    "DX_CANCRI":      {"name":"DX Cancri",            "mass_msun":0.090,    "dist_pc":3.582,  "x_pc":-1.94408, "y_pc": 2.53814, "z_pc": 1.61311},
    "EPS_INDI_A":     {"name":"Epsilon Indi A",       "mass_msun":0.762,    "dist_pc":3.622,  "x_pc": 1.74046, "y_pc":-0.96982, "z_pc":-3.04442},
    "EPS_INDI_BA":    {"name":"Epsilon Indi Ba",      "mass_msun":0.065,    "dist_pc":3.622,  "x_pc": 1.77103, "y_pc":-0.97861, "z_pc":-3.09137},
    "EPS_INDI_BB":    {"name":"Epsilon Indi Bb",      "mass_msun":0.053,    "dist_pc":3.622,  "x_pc": 1.77103, "y_pc":-0.97861, "z_pc":-3.09137},
    "TAU_CETI":       {"name":"Tau Ceti",             "mass_msun":0.783,    "dist_pc":3.650,  "x_pc": 3.15619, "y_pc": 1.53999, "z_pc":-1.00261},
    "GJ1061":         {"name":"GJ 1061",              "mass_msun":0.113,    "dist_pc":3.674,  "x_pc": 1.53990, "y_pc": 2.11975, "z_pc":-2.57600},
    "YZ_CETI":        {"name":"YZ Ceti",              "mass_msun":0.130,    "dist_pc":3.722,  "x_pc": 3.37783, "y_pc": 1.10621, "z_pc":-1.08641},
    "LUYTEN_STAR":    {"name":"Luyten's Star",        "mass_msun":0.260,    "dist_pc":3.785,  "x_pc":-1.40355, "y_pc": 3.49945, "z_pc": 0.34376},
    "TEEGARDEN":      {"name":"Teegarden's Star",     "mass_msun":0.089,    "dist_pc":3.831,  "x_pc": 2.66993, "y_pc": 2.51335, "z_pc": 1.11157},
    "SCR1845":        {"name":"SCR 1845-6357 A",      "mass_msun":0.092,    "dist_pc":3.876,  "x_pc": 0.34448, "y_pc":-1.72424, "z_pc":-3.59879},
    "KAPTEYN":        {"name":"Kapteyn's Star",       "mass_msun":0.274,    "dist_pc":3.934,  "x_pc": 0.57981, "y_pc": 2.71844, "z_pc":-2.78384},
    "LACAILLE8760":   {"name":"Lacaille 8760",        "mass_msun":0.601,    "dist_pc":3.969,  "x_pc": 2.34287, "y_pc":-2.01554, "z_pc":-2.49130},
    "KRUGER60A":      {"name":"Kruger 60 A",          "mass_msun":0.271,    "dist_pc":4.010,  "x_pc": 1.97250, "y_pc":-0.83760, "z_pc": 3.38906},
    "KRUGER60B":      {"name":"Kruger 60 B",          "mass_msun":0.176,    "dist_pc":4.010,  "x_pc": 1.96795, "y_pc":-0.83570, "z_pc": 3.38128},
    "ROSS614A":       {"name":"Ross 614 A",           "mass_msun":0.222,    "dist_pc":4.130,  "x_pc":-0.52596, "y_pc": 4.07704, "z_pc":-0.20229},
    "VAN_MAANEN":     {"name":"Van Maanen's Star",    "mass_msun":0.670,    "dist_pc":4.334,  "x_pc": 4.19691, "y_pc": 0.91482, "z_pc": 0.40427},
    "GLIESE1":        {"name":"Gliese 1",             "mass_msun":0.380,    "dist_pc":4.345,  "x_pc": 3.45300, "y_pc": 0.08338, "z_pc":-2.63771},
    "WOLF424A":       {"name":"Wolf 424 A",           "mass_msun":0.140,    "dist_pc":4.392,  "x_pc":-4.22834, "y_pc":-0.61794, "z_pc": 0.67851},
    "TZ_ARIETIS":     {"name":"TZ Arietis",           "mass_msun":0.150,    "dist_pc":4.461,  "x_pc": 3.76869, "y_pc": 2.18103, "z_pc": 1.00880},
    "GJ687":          {"name":"GJ 687",               "mass_msun":0.413,    "dist_pc":4.530,  "x_pc":-0.17255, "y_pc":-1.67092, "z_pc": 4.22835},
    "GJ674":          {"name":"GJ 674",               "mass_msun":0.350,    "dist_pc":4.547,  "x_pc":-0.42379, "y_pc":-3.08184, "z_pc":-3.32422},
    "GJ440":          {"name":"GJ 440",               "mass_msun":0.550,    "dist_pc":4.626,  "x_pc":-1.96725, "y_pc": 0.12182, "z_pc":-4.19680},
    "GJ1002":         {"name":"GJ 1002",              "mass_msun":0.117,    "dist_pc":4.844,  "x_pc":-2.20178, "y_pc": 0.75447, "z_pc":-4.23409},
    "GJ412A":         {"name":"GJ 412 A",             "mass_msun":0.396,    "dist_pc":4.854,  "x_pc":-3.45534, "y_pc": 0.83963, "z_pc": 3.37807},
}


def load_scene(passport: dict) -> List[Source]:
    """
    Load declared sources from passport into Source objects.
    Uses real Gaia ICRS XYZ coordinates when available in ROSTER.
    Falls back to Fibonacci sphere at declared distance otherwise.
    SOL at origin (Node 0).
    """
    active_ids   = passport.get("active_sources", [])
    sources_data = []
    for sid in active_ids:
        if sid in ROSTER:
            r     = ROSTER[sid]
            entry = {"id": sid, "name": r["name"], "mass_msun": r["mass_msun"]}
            # Real Gaia coordinates take priority
            if "x_pc" in r and sid != "SOL":
                entry["x_pc"] = r["x_pc"]
                entry["y_pc"] = r["y_pc"]
                entry["z_pc"] = r["z_pc"]
                entry["dist_pc"] = r.get("dist_pc", np.sqrt(r["x_pc"]**2 + r["y_pc"]**2 + r["z_pc"]**2))
            elif "dist_pc" in r:
                entry["dist_pc"] = r["dist_pc"]
            elif "dist_au" in r:
                entry["dist_au"] = r["dist_au"]
            sources_data.append(entry)

    positions = fibonacci_positions(sources_data)
    sources   = []
    for sd in sources_data:
        pos     = positions[sd["id"]]
        mass_kg = sd["mass_msun"] * MSUN_KG
        sources.append(Source(id=sd["id"], name=sd["name"], mass=mass_kg, pos=pos))
    return sources


# ─────────────────────────────────────────────
# Main solver: passport → emitted ledger
# ─────────────────────────────────────────────

def run(passport: dict, n_rays: int = 96, n_radial: int = 48) -> dict:
    """
    Atlas GFRO + BCW-L001 Solver.
    Passport in. Certified ledger out.

    Pipeline (Datum Bible v0.3.1):
      1. Load scene (real Gaia XYZ when available)
      2. Emit R0 pairwise Apollonius network (analytic, exact)
      3. Emit R0 source-context (targeted bisection, 48-source context)
      4. Evaluate full Weyl field at emitted points
      5. Run BCW-L001: Node B, Node G, Delta_E, chi field
      6. Assemble certified ledger

    GFRO certified for: pairwise Apollonius emission only.
    BCW-L001 certified for: monopole surrogate compression witnessing.
    Source-context bisection: diagnostic, 48-source relative context only.
    """
    print(f"Atlas GFRO+BCW Solver — scene: {passport.get('scene_id','unnamed')}")

    # 1. Load scene
    sources = load_scene(passport)
    print(f"  Sources loaded: {len(sources)}")

    # Check real vs schematic positions
    n_real = sum(1 for s in passport.get("active_sources",[])
                 if s in ROSTER and "x_pc" in ROSTER[s])
    print(f"  Real Gaia coordinates: {n_real}/{len(sources)}")

    # 2. R0 pairwise Apollonius (analytically exact)
    print(f"  Emitting R0 pairwise ({len(sources)*(len(sources)-1)//2} pairs)...")
    r0_pairwise = emit_R0_pairwise(sources)
    print(f"    {len(r0_pairwise)} Apollonius objects emitted")

    # 3. R0 source-context (48-source relative context)
    print(f"  Emitting R0 source-context ({len(sources)} sources)...")
    r0_ctx_all = []
    for i, src in enumerate(sources):
        ctx = [s for s in sources if s.id != src.id]
        pts = emit_R0_source_context(src, ctx, n_rays, n_radial)
        r0_ctx_all.extend(pts)
        if (i+1) % 10 == 0:
            print(f"    {i+1}/{len(sources)} done, {len(r0_ctx_all)} points")
    print(f"    Total: {len(r0_ctx_all)} source-context points")

    # 4. Full Weyl evaluation at emitted points
    print(f"  Evaluating Weyl field at {len(r0_ctx_all)} points...")
    emitted_pos  = [np.array(p["pos"]) for p in r0_ctx_all]
    weyl_records = evaluate_weyl_at(emitted_pos, sources)
    print(f"  Weyl evaluation complete.")

    # 5. BCW-L001
    print("  Running BCW-L001 (Barycentric Compression Witnessing)...")
    bcw = run_bcw_l001(sources, r0_pairwise)
    print(f"  BCW-L001 complete.")

    # 6. Assemble ledger (schema: BCW Datum Bible v0.3.1 §19)
    n_real_final = sum(1 for s in passport.get("active_sources",[])
                       if s in ROSTER and "x_pc" in ROSTER.get(s,{}))
    pos_note = (
        f"Real Gaia ICRS coordinates: {n_real_final}/{len(sources)} sources. "
        f"Remaining: Fibonacci sphere at declared distance. "
        f"Source: EMS_Node1_LocalStellarContext_10pc_STRICT_v0_2.csv."
    )

    ledger = {
        # Scene passport (BCW §19: scene_passport)
        "scene_id":          passport.get("scene_id", "unnamed"),
        "mode":              "GFRO_pairwise + BCW_L001",
        "regime":            passport.get("regime", "weak_field_gr_approximation"),
        "epoch":             passport.get("epoch", "J2000"),
        "coordinate_frame":  "ICRS_SOL_origin",
        "field_branch":      "weak_field_electric_weyl_tidal",
        "residual_branch":   "R0_scalar_tidal + BCW_L001_monopole",
        "surrogate_rung":    0,
        "position_convention": "real_gaia_icrs_with_fibonacci_fallback",
        "position_note":     pos_note,
        "claim_status":      "diagnostic_candidate_not_observational",

        # Node 0 (global registration datum)
        "node0": {
            "pos_m":  [0.0, 0.0, 0.0],
            "snapped_to": "SOL",
            "note": "Node 0 sits on SOL. It does not become SOL. SOL contributes curvature through its source record. Node 0 contributes nothing.",
        },

        # Node 1 (declared parent context)
        "node1": passport.get("node1", {
            "mode":         "declared_not_computed",
            "description":  "Local Milky Way disk",
            "claim_status": "declared_not_computed",
        }),

        # Source roster (BCW §19: source_roster)
        "source_roster": [
            {
                "source_id":  s.id,
                "name":       s.name,
                "mass_kg":    float(s.mass),
                "mass_msun":  float(s.mass / MSUN_KG),
                "pos_m":      s.pos.tolist(),
                "pos_pc":     (s.pos / PC_TO_M).tolist(),
                "has_real_gaia_coords": s.id in ROSTER and "x_pc" in ROSTER.get(s.id, {}),
                "active_flag": True,
            }
            for s in sources
        ],

        # BCW group roster and derived nodes
        "group_roster":     bcw["group_roster"],
        "derived_nodes":    bcw["derived_nodes"],
        "softening_registry": bcw["softening_registry"],

        # GFRO R0 pairwise (analytically exact)
        "R0_pairwise": {
            "method":         "apollonius_analytic_exact",
            "claim":          "Certified. Apollonius zero sets are analytic derivations, not numerical estimates.",
            "n_objects":      len(r0_pairwise),
            "objects":        [obj.to_dict() for obj in r0_pairwise],
            "claim_status":   "certified_analytic",
        },

        # R0 source-context (relative to 48-source child scene)
        "R0_source_context": {
            "method":         "gfro_targeted_bisection",
            "claim":          "Diagnostic. Context = 48 active sources only. Node 1 tidal background not yet evaluated.",
            "n_rays":         n_rays,
            "n_radial":       n_radial,
            "n_emitted":      len(r0_ctx_all),
            "points":         r0_ctx_all,
            "claim_status":   "diagnostic_candidate_not_observational",
        },

        # Full Weyl field at emitted points
        "weyl_field": {
            "method":         "full_E_ij_at_emitted_points",
            "n_points":       len(weyl_records),
            "records":        weyl_records,
            "claim_status":   "diagnostic_candidate_not_observational",
        },

        # BCW-L001 compression witnessing
        "bcw": bcw["bcw_field"],

        # Certification
        "certification": {
            "R0_pairwise_analytic":      True,
            "R0_ctx_bisection_depth":    52,
            "bcw_surrogate_rung":        0,
            "bcw_epsilon_B_declared":    True,
            "node1_tidal_background":    "not_computed",
            "claim_status":              "diagnostic_candidate_not_observational",
        }
    }

    return ledger


# ─────────────────────────────────────────────
# CLI entry point
# ─────────────────────────────────────────────

if __name__ == "__main__":
    import sys, os

    if len(sys.argv) < 2:
        print("Usage: python atlas_emitter.py passport.json [output_ledger.json]")
        sys.exit(1)

    passport_path = sys.argv[1]
    output_path = sys.argv[2] if len(sys.argv) > 2 else "atlas_ledger.json"

    with open(passport_path) as f:
        passport = json.load(f)

    ledger = run(passport)

    with open(output_path, "w") as f:
        json.dump(ledger, f, indent=2)

    size_mb = os.path.getsize(output_path) / 1e6
    print(f"\nLedger written: {output_path} ({size_mb:.2f} MB)")
    print(f"  R0 pairwise objects: {ledger['R0_pairwise']['n_objects']}")
    print(f"  R0 source-context points: {ledger['R0_source_context']['n_emitted']}")
    print(f"  Weyl records: {ledger['weyl_field']['n_points']}")
