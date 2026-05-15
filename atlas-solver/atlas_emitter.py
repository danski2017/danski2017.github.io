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
    "SOL": {"name":"Sun", "cls":"star_G2", "mass_msun":1.0, "dist_au":0, "x_pc":0.0, "y_pc":0.0, "z_pc":0.0},
    "N1_10PC_STRICT_0001": {"name":"Proxima Cen", "cls":"M-dwarf", "mass_msun":0.1875, "dist_pc":1.3020, "x_pc":-0.47482, "y_pc":-0.36292, "z_pc":-1.15670},
    "N1_10PC_STRICT_0002": {"name":"Rigil Kentaurus", "cls":"star", "mass_msun":1.0, "dist_pc":1.3459, "x_pc":-0.50318, "y_pc":-0.42075, "z_pc":-1.17525},
    "N1_10PC_STRICT_0003": {"name":"Toliman", "cls":"star", "mass_msun":0.7, "dist_pc":1.3459, "x_pc":-0.50316, "y_pc":-0.42065, "z_pc":-1.17529},
    "N1_10PC_STRICT_0004": {"name":"Barnard's Star", "cls":"M-dwarf", "mass_msun":0.3374999999999999, "dist_pc":1.8282, "x_pc":-0.01754, "y_pc":-1.82190, "z_pc":0.15106},
    "N1_10PC_STRICT_0005": {"name":"Luhman 16", "cls":"brown_dwarf", "mass_msun":0.05, "dist_pc":1.9938, "x_pc":-1.13471, "y_pc":0.36194, "z_pc":-1.59895},
    "N1_10PC_STRICT_0006": {"name":"Luhman 16", "cls":"brown_dwarf", "mass_msun":0.05, "dist_pc":1.9938, "x_pc":-1.13470, "y_pc":0.36195, "z_pc":-1.59895},
    "N1_10PC_STRICT_0007": {"name":"WISEA J085510.74-071442.5", "cls":"brown_dwarf", "mass_msun":0.05, "dist_pc":2.2779, "x_pc":-1.56351, "y_pc":1.63150, "z_pc":-0.28723},
    "N1_10PC_STRICT_0008": {"name":"CN Leo", "cls":"M-dwarf", "mass_msun":0.15, "dist_pc":2.4086, "x_pc":-2.29920, "y_pc":0.65481, "z_pc":0.29365},
    "N1_10PC_STRICT_0009": {"name":"Lalande 21185", "cls":"M-dwarf", "mass_msun":0.4875, "dist_pc":2.5461, "x_pc":-1.99850, "y_pc":0.50455, "z_pc":1.49473},
    "N1_10PC_STRICT_0010": {"name":"Sirius A", "cls":"star", "mass_msun":2.0, "dist_pc":2.6371, "x_pc":-0.49433, "y_pc":2.47677, "z_pc":-0.75850},
    "N1_10PC_STRICT_0011": {"name":"Sirius B", "cls":"white_dwarf", "mass_msun":0.6, "dist_pc":2.6703, "x_pc":-0.50053, "y_pc":2.50794, "z_pc":-0.76827},
    "N1_10PC_STRICT_0012": {"name":"BL Cet", "cls":"M-dwarf", "mass_msun":0.2249999999999999, "dist_pc":2.7195, "x_pc":2.34912, "y_pc":1.08403, "z_pc":-0.83804},
    "N1_10PC_STRICT_0013": {"name":"UV Cet", "cls":"M-dwarf", "mass_msun":0.15, "dist_pc":2.6749, "x_pc":2.31059, "y_pc":1.06626, "z_pc":-0.82427},
    "N1_10PC_STRICT_0014": {"name":"Ross 154", "cls":"M-dwarf", "mass_msun":0.3374999999999999, "dist_pc":2.9760, "x_pc":0.58726, "y_pc":-2.65800, "z_pc":-1.20270},
    "N1_10PC_STRICT_0015": {"name":"HH And", "cls":"M-dwarf", "mass_msun":0.2249999999999999, "dist_pc":3.1597, "x_pc":2.25935, "y_pc":-0.17861, "z_pc":2.20169},
    "N1_10PC_STRICT_0016": {"name":"Ran", "cls":"star", "mass_msun":0.7, "dist_pc":3.2198, "x_pc":1.90127, "y_pc":2.54409, "z_pc":-0.52910},
    "N1_10PC_STRICT_0017": {"name":"Lacaille 9352", "cls":"M-dwarf", "mass_msun":0.4499999999999999, "dist_pc":3.2880, "x_pc":2.59160, "y_pc":-0.62200, "z_pc":-1.92554},
    "N1_10PC_STRICT_0018": {"name":"FI Vir", "cls":"M-dwarf", "mass_msun":0.3, "dist_pc":3.3749, "x_pc":-3.36975, "y_pc":0.18028, "z_pc":0.04707},
    "N1_10PC_STRICT_0019": {"name":"EZ Aqr A", "cls":"M-dwarf", "mass_msun":0.2249999999999999, "dist_pc":3.4060, "x_pc":3.08040, "y_pc":-1.14249, "z_pc":-0.89816},
    "N1_10PC_STRICT_0020": {"name":"EZ Aqr B", "cls":"M-dwarf", "mass_msun":0.2, "dist_pc":3.4060, "x_pc":3.08040, "y_pc":-1.14249, "z_pc":-0.89816},
    "N1_10PC_STRICT_0021": {"name":"EZ Aqr C", "cls":"M-dwarf", "mass_msun":0.2, "dist_pc":3.4060, "x_pc":3.08040, "y_pc":-1.14249, "z_pc":-0.89816},
    "N1_10PC_STRICT_0022": {"name":"61 Cyg A", "cls":"star", "mass_msun":0.7, "dist_pc":3.4966, "x_pc":1.98577, "y_pc":-1.86813, "z_pc":2.18924},
    "N1_10PC_STRICT_0023": {"name":"61 Cyg B", "cls":"star", "mass_msun":0.7, "dist_pc":3.4964, "x_pc":1.98609, "y_pc":-1.86808, "z_pc":2.18879},
    "N1_10PC_STRICT_0024": {"name":"Procyon A", "cls":"star", "mass_msun":1.3, "dist_pc":3.5142, "x_pc":-1.46933, "y_pc":3.17620, "z_pc":0.32003},
    "N1_10PC_STRICT_0025": {"name":"Procyon B", "cls":"white_dwarf", "mass_msun":0.6, "dist_pc":3.5142, "x_pc":-1.46927, "y_pc":3.17623, "z_pc":0.31997},
    "N1_10PC_STRICT_0026": {"name":"HD 173739", "cls":"M-dwarf", "mass_msun":0.375, "dist_pc":3.5231, "x_pc":0.33011, "y_pc":-1.74991, "z_pc":3.03992},
    "N1_10PC_STRICT_0027": {"name":"HD 173740", "cls":"M-dwarf", "mass_msun":0.3374999999999999, "dist_pc":3.5231, "x_pc":0.33015, "y_pc":-1.75009, "z_pc":3.03985},
    "N1_10PC_STRICT_0028": {"name":"GX And", "cls":"M-dwarf", "mass_msun":0.525, "dist_pc":3.5624, "x_pc":2.55323, "y_pc":0.20602, "z_pc":2.47578},
    "N1_10PC_STRICT_0029": {"name":"GQ And", "cls":"M-dwarf", "mass_msun":0.3374999999999999, "dist_pc":3.5626, "x_pc":2.55313, "y_pc":0.20655, "z_pc":2.47607},
    "N1_10PC_STRICT_0030": {"name":"DX Cnc", "cls":"M-dwarf", "mass_msun":0.1124999999999999, "dist_pc":3.5810, "x_pc":-1.94408, "y_pc":2.53814, "z_pc":1.61311},
    "N1_10PC_STRICT_0031": {"name":"eps Ind A", "cls":"star", "mass_msun":0.7, "dist_pc":3.6384, "x_pc":1.74046, "y_pc":-0.96982, "z_pc":-3.04442},
    "N1_10PC_STRICT_0032": {"name":"eps Ind Ba", "cls":"brown_dwarf", "mass_msun":0.05, "dist_pc":3.6947, "x_pc":1.77103, "y_pc":-0.97861, "z_pc":-3.09137},
    "N1_10PC_STRICT_0033": {"name":"eps Ind Bb", "cls":"brown_dwarf", "mass_msun":0.05, "dist_pc":3.6947, "x_pc":1.77103, "y_pc":-0.97861, "z_pc":-3.09137},
    "N1_10PC_STRICT_0034": {"name":"tau Cet", "cls":"star", "mass_msun":1.0, "dist_pc":3.6522, "x_pc":3.15619, "y_pc":1.53999, "z_pc":-1.00261},
    "N1_10PC_STRICT_0035": {"name":"GJ 1061", "cls":"M-dwarf", "mass_msun":0.1875, "dist_pc":3.6743, "x_pc":1.53990, "y_pc":2.11975, "z_pc":-2.57600},
    "N1_10PC_STRICT_0036": {"name":"YZ Cet", "cls":"M-dwarf", "mass_msun":0.3, "dist_pc":3.7167, "x_pc":3.37783, "y_pc":1.10621, "z_pc":-1.08641},
    "N1_10PC_STRICT_0037": {"name":"Luyten's Star", "cls":"M-dwarf", "mass_msun":0.3374999999999999, "dist_pc":3.7861, "x_pc":-1.40355, "y_pc":3.49945, "z_pc":0.34376},
    "N1_10PC_STRICT_0038": {"name":"Teegarden's Star", "cls":"M-dwarf", "mass_msun":0.15, "dist_pc":3.8316, "x_pc":2.66993, "y_pc":2.51335, "z_pc":1.11157},
    "N1_10PC_STRICT_0039": {"name":"Kapteyn's Star", "cls":"M-dwarf", "mass_msun":0.2, "dist_pc":3.9339, "x_pc":0.57981, "y_pc":2.71844, "z_pc":-2.78384},
    "N1_10PC_STRICT_0040": {"name":"Lacaille 8760", "cls":"M-dwarf", "mass_msun":0.525, "dist_pc":3.9696, "x_pc":2.34287, "y_pc":-2.01554, "z_pc":-2.49130},
    "N1_10PC_STRICT_0041": {"name":"Kruger 60 A", "cls":"M-dwarf", "mass_msun":0.375, "dist_pc":4.0097, "x_pc":1.97250, "y_pc":-0.83760, "z_pc":3.38906},
    "N1_10PC_STRICT_0042": {"name":"DO Cep", "cls":"M-dwarf", "mass_msun":0.3, "dist_pc":4.0005, "x_pc":1.96795, "y_pc":-0.83570, "z_pc":3.38128},
    "N1_10PC_STRICT_0043": {"name":"SCR J1845-6357 A", "cls":"M-dwarf", "mass_msun":0.08, "dist_pc":4.0054, "x_pc":0.34448, "y_pc":-1.72424, "z_pc":-3.59879},
    "N1_10PC_STRICT_0044": {"name":"SCR J1845-6357 B", "cls":"brown_dwarf", "mass_msun":0.05, "dist_pc":4.0054, "x_pc":0.34393, "y_pc":-1.72426, "z_pc":-3.59883},
    "N1_10PC_STRICT_0045": {"name":"DENIS J104814.6-395606", "cls":"M-dwarf", "mass_msun":0.08, "dist_pc":4.0451, "x_pc":-2.95053, "y_pc":0.95562, "z_pc":-2.59684},
    "N1_10PC_STRICT_0046": {"name":"V577 Mon A", "cls":"M-dwarf", "mass_msun":0.2625, "dist_pc":4.1158, "x_pc":-0.52596, "y_pc":4.07704, "z_pc":-0.20229},
    "N1_10PC_STRICT_0047": {"name":"V577 Mon B", "cls":"M-dwarf", "mass_msun":0.1875, "dist_pc":4.1158, "x_pc":-0.52596, "y_pc":4.07704, "z_pc":-0.20229},
    "N1_10PC_STRICT_0048": {"name":"UGPS J072227.51-054031.2", "cls":"brown_dwarf", "mass_msun":0.05, "dist_pc":4.1186, "x_pc":-1.44298, "y_pc":3.83600, "z_pc":-0.40730},
    "N1_10PC_STRICT_0049": {"name":"Wolf 1061", "cls":"M-dwarf", "mass_msun":0.375, "dist_pc":4.3078, "x_pc":-1.60331, "y_pc":-3.88507, "z_pc":-0.94469},
    "N1_10PC_STRICT_0050": {"name":"van Maanen's Star", "cls":"white_dwarf", "mass_msun":0.6, "dist_pc":4.3144, "x_pc":4.19691, "y_pc":0.91482, "z_pc":0.40427},
    "N1_10PC_STRICT_0051": {"name":"FL Vir A", "cls":"M-dwarf", "mass_msun":0.1875, "dist_pc":4.3268, "x_pc":-4.22834, "y_pc":-0.61794, "z_pc":0.67851},
    "N1_10PC_STRICT_0052": {"name":"FL Vir B", "cls":"M-dwarf", "mass_msun":0.08, "dist_pc":4.4747, "x_pc":-4.37291, "y_pc":-0.63908, "z_pc":0.70168},
    "N1_10PC_STRICT_0053": {"name":"HD 225213", "cls":"M-dwarf", "mass_msun":0.4499999999999999, "dist_pc":4.3460, "x_pc":3.45300, "y_pc":0.08338, "z_pc":-2.63771},
    "N1_10PC_STRICT_0054": {"name":"GJ 9066", "cls":"M-dwarf", "mass_msun":0.2625, "dist_pc":4.4696, "x_pc":3.76869, "y_pc":2.18103, "z_pc":1.00880},
    "N1_10PC_STRICT_0055": {"name":"GJ 687", "cls":"M-dwarf", "mass_msun":0.375, "dist_pc":4.5498, "x_pc":-0.17255, "y_pc":-1.67092, "z_pc":4.22835},
    "N1_10PC_STRICT_0056": {"name":"GJ 674", "cls":"M-dwarf", "mass_msun":0.4499999999999999, "dist_pc":4.5528, "x_pc":-0.42379, "y_pc":-3.08184, "z_pc":-3.32422},
    "N1_10PC_STRICT_0057": {"name":"WISE J163940.83-684738.6", "cls":"brown_dwarf", "mass_msun":0.05, "dist_pc":4.5537, "x_pc":-0.56534, "y_pc":-1.54675, "z_pc":-4.24552},
    "N1_10PC_STRICT_0058": {"name":"LP 731-58", "cls":"M-dwarf", "mass_msun":0.1124999999999999, "dist_pc":4.5593, "x_pc":-4.25282, "y_pc":1.37730, "z_pc":-0.89672},
    "N1_10PC_STRICT_0059": {"name":"LAWD 37", "cls":"white_dwarf", "mass_msun":0.6, "dist_pc":4.6366, "x_pc":-1.96725, "y_pc":0.12182, "z_pc":-4.19680},
    "N1_10PC_STRICT_0060": {"name":"GJ 1245 A", "cls":"M-dwarf", "mass_msun":0.1875, "dist_pc":4.6919, "x_pc":1.59817, "y_pc":-2.94595, "z_pc":3.28348},
    "N1_10PC_STRICT_0061": {"name":"GJ 1245 C", "cls":"M-dwarf", "mass_msun":0.08, "dist_pc":4.6919, "x_pc":1.59817, "y_pc":-2.94595, "z_pc":3.28348},
    "N1_10PC_STRICT_0062": {"name":"GJ 1245 B", "cls":"M-dwarf", "mass_msun":0.1875, "dist_pc":4.6604, "x_pc":1.58753, "y_pc":-2.92607, "z_pc":3.26145},
    "N1_10PC_STRICT_0063": {"name":"WISEP J174124.25+255319.5", "cls":"brown_dwarf", "mass_msun":0.05, "dist_pc":4.6664, "x_pc":-0.34013, "y_pc":-4.18411, "z_pc":2.03775},
    "N1_10PC_STRICT_0064": {"name":"IL Aqr", "cls":"M-dwarf", "mass_msun":0.3, "dist_pc":4.6775, "x_pc":4.34263, "y_pc":-1.30086, "z_pc":-1.15271},
    "N1_10PC_STRICT_0065": {"name":"L 143-23", "cls":"M-dwarf", "mass_msun":0.1875, "dist_pc":4.8316, "x_pc":-2.20178, "y_pc":0.75447, "z_pc":-4.23409},
    "N1_10PC_STRICT_0066": {"name":"G 158-27", "cls":"M-dwarf", "mass_msun":0.1875, "dist_pc":4.8461, "x_pc":4.80210, "y_pc":0.14054, "z_pc":-0.63644},
    "N1_10PC_STRICT_0067": {"name":"DENIS 0255-4700", "cls":"brown_dwarf", "mass_msun":0.05, "dist_pc":4.8680, "x_pc":2.39657, "y_pc":2.29598, "z_pc":-3.56117},
    "N1_10PC_STRICT_0068": {"name":"HD 88230", "cls":"star", "mass_msun":0.7, "dist_pc":4.8706, "x_pc":-2.81698, "y_pc":1.44568, "z_pc":3.70096},
    "N1_10PC_STRICT_0069": {"name":"BD+44 2051 A", "cls":"M-dwarf", "mass_msun":0.525, "dist_pc":4.9047, "x_pc":-3.45534, "y_pc":0.83963, "z_pc":3.37807},
    "N1_10PC_STRICT_0070": {"name":"WX UMa", "cls":"M-dwarf", "mass_msun":0.1875, "dist_pc":4.9060, "x_pc":-3.45671, "y_pc":0.83933, "z_pc":3.37867},
    "N1_10PC_STRICT_0071": {"name":"AD Leo", "cls":"M-dwarf", "mass_msun":0.375, "dist_pc":4.9651, "x_pc":-4.22851, "y_pc":1.98089, "z_pc":1.68755},
    "N1_10PC_STRICT_0072": {"name":"GJ 832", "cls":"M-dwarf", "mass_msun":0.4875, "dist_pc":4.9671, "x_pc":2.61518, "y_pc":-1.94283, "z_pc":-3.74943},
    "N1_10PC_STRICT_0073": {"name":"GJ 682", "cls":"M-dwarf", "mass_msun":0.2249999999999999, "dist_pc":5.0077, "x_pc":-0.35825, "y_pc":-3.56456, "z_pc":-3.49888},
    "N1_10PC_STRICT_0074": {"name":"Keid", "cls":"star", "mass_msun":0.7, "dist_pc":5.0098, "x_pc":2.19147, "y_pc":4.45521, "z_pc":-0.66848},
    "N1_10PC_STRICT_0075": {"name":"GJ 166 B", "cls":"white_dwarf", "mass_msun":0.6, "dist_pc":5.0077, "x_pc":2.18876, "y_pc":4.45418, "z_pc":-0.66862},
    "N1_10PC_STRICT_0076": {"name":"DY Eri", "cls":"M-dwarf", "mass_msun":0.2625, "dist_pc":5.0137, "x_pc":2.19148, "y_pc":4.45950, "z_pc":-0.66925},
    "N1_10PC_STRICT_0077": {"name":"EV Lac", "cls":"M-dwarf", "mass_msun":0.3, "dist_pc":5.0516, "x_pc":3.43073, "y_pc":-1.13442, "z_pc":3.53013},
    "N1_10PC_STRICT_0078": {"name":"EI Cnc A", "cls":"M-dwarf", "mass_msun":0.08, "dist_pc":5.1508, "x_pc":-3.40117, "y_pc":3.45391, "z_pc":1.74164},
    "N1_10PC_STRICT_0079": {"name":"EI Cnc B", "cls":"M-dwarf", "mass_msun":0.08, "dist_pc":5.0952, "x_pc":-3.36445, "y_pc":3.41669, "z_pc":1.72282},
    "N1_10PC_STRICT_0080": {"name":"70 Oph A", "cls":"star", "mass_msun":0.7, "dist_pc":5.1133, "x_pc":0.12164, "y_pc":-5.10703, "z_pc":0.22261},
    "N1_10PC_STRICT_0081": {"name":"70 Oph B", "cls":"star", "mass_msun":0.7, "dist_pc":5.1058, "x_pc":0.12159, "y_pc":-5.09950, "z_pc":0.22219},
    "N1_10PC_STRICT_0082": {"name":"Altair", "cls":"star", "mass_msun":2.0, "dist_pc":5.1295, "x_pc":2.35558, "y_pc":-4.48752, "z_pc":0.79079},
    "N1_10PC_STRICT_0083": {"name":"2MASS J15065257+7027247", "cls":"brown_dwarf", "mass_msun":0.05, "dist_pc":5.1562, "x_pc":-1.18259, "y_pc":-1.25505, "z_pc":4.85930},
    "N1_10PC_STRICT_0084": {"name":"G 99-49", "cls":"M-dwarf", "mass_msun":0.3374999999999999, "dist_pc":5.2080, "x_pc":-0.00145, "y_pc":5.20216, "z_pc":0.24591},
    "N1_10PC_STRICT_0085": {"name":"2MASS J08173001-6155158", "cls":"brown_dwarf", "mass_msun":0.05, "dist_pc":5.2128, "x_pc":-1.38549, "y_pc":2.02546, "z_pc":-4.59902},
    "N1_10PC_STRICT_0086": {"name":"G 254-29", "cls":"M-dwarf", "mass_msun":0.3, "dist_pc":5.2542, "x_pc":-1.02867, "y_pc":0.05500, "z_pc":5.15219},
    "N1_10PC_STRICT_0087": {"name":"WISEA J154045.67-510139.3", "cls":"M-dwarf", "mass_msun":0.1124999999999999, "dist_pc":5.3268, "x_pc":-1.91227, "y_pc":-2.75089, "z_pc":-4.14137},
    "N1_10PC_STRICT_0088": {"name":"2MASS J09393548-2448279", "cls":"brown_dwarf", "mass_msun":0.05, "dist_pc":5.3390, "x_pc":-3.96493, "y_pc":2.78682, "z_pc":-2.24012},
    "N1_10PC_STRICT_0089": {"name":"GJ 3323", "cls":"M-dwarf", "mass_msun":0.3, "dist_pc":5.3750, "x_pc":1.33710, "y_pc":5.16526, "z_pc":-0.65026},
    "N1_10PC_STRICT_0090": {"name":"HD 119850", "cls":"M-dwarf", "mass_msun":0.4875, "dist_pc":5.4349, "x_pc":-4.70309, "y_pc":-2.33878, "z_pc":1.39612},
    "N1_10PC_STRICT_0091": {"name":"Stein 2051 A", "cls":"M-dwarf", "mass_msun":0.3, "dist_pc":5.5174, "x_pc":1.07428, "y_pc":2.63365, "z_pc":4.72777},
    "N1_10PC_STRICT_0092": {"name":"Stein 2051 B", "cls":"white_dwarf", "mass_msun":0.6, "dist_pc":5.5165, "x_pc":1.07385, "y_pc":2.63320, "z_pc":4.72708},
    "N1_10PC_STRICT_0093": {"name":"2MASS J11145133-2618235", "cls":"brown_dwarf", "mass_msun":0.05, "dist_pc":5.5804, "x_pc":-4.90570, "y_pc":0.97902, "z_pc":-2.47307},
    "N1_10PC_STRICT_0094": {"name":"Wolf 294", "cls":"M-dwarf", "mass_msun":0.375, "dist_pc":5.5846, "x_pc":-1.10592, "y_pc":4.53662, "z_pc":3.06335},
    "N1_10PC_STRICT_0095": {"name":"LP 816-60", "cls":"M-dwarf", "mass_msun":0.3, "dist_pc":5.6201, "x_pc":3.67528, "y_pc":-3.92253, "z_pc":-1.64079},
    "N1_10PC_STRICT_0096": {"name":"WISE J035000.32-565830.2", "cls":"brown_dwarf", "mass_msun":0.05, "dist_pc":5.6689, "x_pc":1.65996, "y_pc":2.60571, "z_pc":-4.75307},
    "N1_10PC_STRICT_0097": {"name":"2MASSI J1835379+325954", "cls":"M-dwarf", "mass_msun":0.08, "dist_pc":5.6885, "x_pc":0.73875, "y_pc":-4.71353, "z_pc":3.09775},
    "N1_10PC_STRICT_0098": {"name":"HD 36395", "cls":"M-dwarf", "mass_msun":0.4875, "dist_pc":5.7041, "x_pc":0.70677, "y_pc":5.64823, "z_pc":-0.36676},
    "N1_10PC_STRICT_0099": {"name":"2MASSI J0415195-093506", "cls":"brown_dwarf", "mass_msun":0.05, "dist_pc":5.7078, "x_pc":2.48206, "y_pc":5.05120, "z_pc":-0.95042},
    "N1_10PC_STRICT_0100": {"name":"GJ 229 A", "cls":"M-dwarf", "mass_msun":0.525, "dist_pc":5.7612, "x_pc":-0.24660, "y_pc":5.34100, "z_pc":-2.14587},
    "N1_10PC_STRICT_0101": {"name":"GJ 229 B", "cls":"brown_dwarf", "mass_msun":0.05, "dist_pc":5.7740, "x_pc":-0.24729, "y_pc":5.35287, "z_pc":-2.15052},
    "N1_10PC_STRICT_0102": {"name":"Alsafi", "cls":"star", "mass_msun":1.0, "dist_pc":5.7639, "x_pc":0.78620, "y_pc":-1.84344, "z_pc":5.40426},
    "N1_10PC_STRICT_0103": {"name":"V1352 Ori", "cls":"M-dwarf", "mass_msun":0.3, "dist_pc":5.7912, "x_pc":0.43894, "y_pc":5.63723, "z_pc":1.25170},
    "N1_10PC_STRICT_0104": {"name":"KX Lib", "cls":"star", "mass_msun":0.7, "dist_pc":5.8864, "x_pc":-3.91697, "y_pc":-3.83198, "z_pc":-2.15001},
    "N1_10PC_STRICT_0105": {"name":"GJ 570 B", "cls":"M-dwarf", "mass_msun":0.525, "dist_pc":5.9252, "x_pc":-3.94336, "y_pc":-3.85697, "z_pc":-2.16379},
    "N1_10PC_STRICT_0106": {"name":"GJ 570 C", "cls":"M-dwarf", "mass_msun":0.2, "dist_pc":5.9252, "x_pc":-3.94336, "y_pc":-3.85697, "z_pc":-2.16379},
    "N1_10PC_STRICT_0107": {"name":"GJ 570 D", "cls":"brown_dwarf", "mass_msun":0.05, "dist_pc":5.9067, "x_pc":-3.93607, "y_pc":-3.84271, "z_pc":-2.15168},
    "N1_10PC_STRICT_0108": {"name":"L 205-128", "cls":"M-dwarf", "mass_msun":0.3, "dist_pc":5.8891, "x_pc":-0.18670, "y_pc":-3.17389, "z_pc":-4.95716},
    "N1_10PC_STRICT_0109": {"name":"L 347-14", "cls":"M-dwarf", "mass_msun":0.2625, "dist_pc":5.9089, "x_pc":1.42857, "y_pc":-3.88188, "z_pc":-4.21969},
    "N1_10PC_STRICT_0110": {"name":"BR Psc", "cls":"M-dwarf", "mass_msun":0.525, "dist_pc":5.9096, "x_pc":5.89790, "y_pc":-0.27746, "z_pc":0.24715},
    "N1_10PC_STRICT_0111": {"name":"V1428 Aql", "cls":"M-dwarf", "mass_msun":0.375, "dist_pc":5.9150, "x_pc":1.94004, "y_pc":-5.56239, "z_pc":0.53229},
    "N1_10PC_STRICT_0112": {"name":"vB 10", "cls":"M-dwarf", "mass_msun":0.08, "dist_pc":5.9188, "x_pc":1.94228, "y_pc":-5.56578, "z_pc":0.53071},
    "N1_10PC_STRICT_0113": {"name":"CD-40 9712", "cls":"M-dwarf", "mass_msun":0.4125, "dist_pc":5.9173, "x_pc":-2.67324, "y_pc":-3.55356, "z_pc":-3.90388},
    "N1_10PC_STRICT_0114": {"name":"Achird", "cls":"star", "mass_msun":1.3, "dist_pc":5.9230, "x_pc":3.08288, "y_pc":0.67134, "z_pc":5.01274},
    "N1_10PC_STRICT_0115": {"name":"eta Cas B", "cls":"star", "mass_msun":0.7, "dist_pc":5.9270, "x_pc":3.08475, "y_pc":0.67152, "z_pc":5.01628},
    "N1_10PC_STRICT_0116": {"name":"Guniibuu", "cls":"star", "mass_msun":0.7, "dist_pc":5.9478, "x_pc":-1.02971, "y_pc":-5.21721, "z_pc":-2.66390},
    "N1_10PC_STRICT_0117": {"name":"36 Oph B", "cls":"star", "mass_msun":0.7, "dist_pc":5.9523, "x_pc":-1.03059, "y_pc":-5.22119, "z_pc":-2.66582},
    "N1_10PC_STRICT_0118": {"name":"36 Oph C", "cls":"star", "mass_msun":0.7, "dist_pc":5.9537, "x_pc":-1.01135, "y_pc":-5.22892, "z_pc":-2.66130},
    "N1_10PC_STRICT_0119": {"name":"Furuhjelm 46 A", "cls":"M-dwarf", "mass_msun":0.375, "dist_pc":5.9776, "x_pc":-0.86620, "y_pc":-4.08715, "z_pc":4.27517},
    "N1_10PC_STRICT_0120": {"name":"Furuhjelm 46 B", "cls":"M-dwarf", "mass_msun":0.2, "dist_pc":5.9776, "x_pc":-0.86620, "y_pc":-4.08715, "z_pc":4.27517},
    "N1_10PC_STRICT_0121": {"name":"YZ CMi", "cls":"M-dwarf", "mass_msun":0.3, "dist_pc":5.9889, "x_pc":-2.63584, "y_pc":5.36481, "z_pc":0.37088},
    "N1_10PC_STRICT_0122": {"name":"WISE J154151.65-225024.9", "cls":"brown_dwarf", "mass_msun":0.05, "dist_pc":5.9916, "x_pc":-3.13047, "y_pc":-4.54868, "z_pc":-2.32575},
    "N1_10PC_STRICT_0123": {"name":"G 158-50 A", "cls":"M-dwarf", "mass_msun":0.3, "dist_pc":6.0024, "x_pc":5.75277, "y_pc":0.38915, "z_pc":-1.66823},
    "N1_10PC_STRICT_0124": {"name":"G 158-50 B", "cls":"M-dwarf", "mass_msun":0.3, "dist_pc":6.0024, "x_pc":5.75277, "y_pc":0.38915, "z_pc":-1.66823},
    "N1_10PC_STRICT_0125": {"name":"GJ 783 A", "cls":"star", "mass_msun":0.7, "dist_pc":6.0122, "x_pc":2.63141, "y_pc":-4.08280, "z_pc":-3.54309},
    "N1_10PC_STRICT_0126": {"name":"GJ 783 B", "cls":"M-dwarf", "mass_msun":0.3374999999999999, "dist_pc":6.0122, "x_pc":2.63141, "y_pc":-4.08280, "z_pc":-3.54309},
    "N1_10PC_STRICT_0127": {"name":"HD 20794", "cls":"star", "mass_msun":1.0, "dist_pc":6.0414, "x_pc":2.83700, "y_pc":3.38105, "z_pc":-4.12536},
    "N1_10PC_STRICT_0128": {"name":"QY Aur A", "cls":"M-dwarf", "mass_msun":0.2249999999999999, "dist_pc":6.0527, "x_pc":-1.42432, "y_pc":4.51596, "z_pc":3.77000},
    "N1_10PC_STRICT_0129": {"name":"QY Aur B", "cls":"M-dwarf", "mass_msun":0.2249999999999999, "dist_pc":6.0527, "x_pc":-1.42432, "y_pc":4.51596, "z_pc":3.77000},
    "N1_10PC_STRICT_0130": {"name":"del Pav", "cls":"star", "mass_msun":1.0, "dist_pc":6.0993, "x_pc":1.31207, "y_pc":-2.08393, "z_pc":-5.58002},
    "N1_10PC_STRICT_0131": {"name":"SIMP J013656.5+093347.3", "cls":"brown_dwarf", "mass_msun":0.05, "dist_pc":6.1182, "x_pc":5.50116, "y_pc":2.47708, "z_pc":1.01643},
    "N1_10PC_STRICT_0132": {"name":"2MASSI J0937347+293142", "cls":"brown_dwarf", "mass_msun":0.05, "dist_pc":6.1406, "x_pc":-4.34418, "y_pc":3.11066, "z_pc":3.02640},
    "N1_10PC_STRICT_0133": {"name":"HD 191849", "cls":"M-dwarf", "mass_msun":0.6, "dist_pc":6.1646, "x_pc":2.39754, "y_pc":-3.62540, "z_pc":-4.37153},
    "N1_10PC_STRICT_0134": {"name":"WISE J220905.73+271143.9", "cls":"brown_dwarf", "mass_msun":0.05, "dist_pc":6.1843, "x_pc":4.86923, "y_pc":-2.55902, "z_pc":2.82622},
    "N1_10PC_STRICT_0135": {"name":"EGGR 372", "cls":"white_dwarf", "mass_msun":0.6, "dist_pc":6.2114, "x_pc":-0.10590, "y_pc":-2.03160, "z_pc":5.86877},
    "N1_10PC_STRICT_0136": {"name":"HN Lib", "cls":"M-dwarf", "mass_msun":0.3374999999999999, "dist_pc":6.2530, "x_pc":-4.77282, "y_pc":-3.80578, "z_pc":-1.35521},
    "N1_10PC_STRICT_0137": {"name":"EQ Peg A", "cls":"M-dwarf", "mass_msun":0.3374999999999999, "dist_pc":6.2632, "x_pc":5.84355, "y_pc":-0.72059, "z_pc":2.13566},
    "N1_10PC_STRICT_0138": {"name":"EQ Peg B", "cls":"M-dwarf", "mass_msun":0.3, "dist_pc":6.2536, "x_pc":5.83460, "y_pc":-0.71933, "z_pc":2.13242},
    "N1_10PC_STRICT_0139": {"name":"HO Lib", "cls":"M-dwarf", "mass_msun":0.375, "dist_pc":6.3005, "x_pc":-4.02512, "y_pc":-4.77259, "z_pc":-0.84665},
    "N1_10PC_STRICT_0140": {"name":"WISE J140518.39+553421.3", "cls":"brown_dwarf", "mass_msun":0.05, "dist_pc":6.3211, "x_pc":-3.05290, "y_pc":-1.85770, "z_pc":5.21395},
    "N1_10PC_STRICT_0141": {"name":"GJ 338 A", "cls":"M-dwarf", "mass_msun":0.6, "dist_pc":6.3336, "x_pc":-2.87932, "y_pc":2.53993, "z_pc":5.03715},
    "N1_10PC_STRICT_0142": {"name":"GJ 338 B", "cls":"M-dwarf", "mass_msun":0.6, "dist_pc":6.3338, "x_pc":-2.87980, "y_pc":2.53966, "z_pc":5.03728},
    "N1_10PC_STRICT_0143": {"name":"LP 368-128", "cls":"M-dwarf", "mass_msun":0.1124999999999999, "dist_pc":6.3585, "x_pc":-4.18066, "y_pc":4.16673, "z_pc":2.36466},
    "N1_10PC_STRICT_0144": {"name":"2MASS J15031961+2525196", "cls":"brown_dwarf", "mass_msun":0.05, "dist_pc":6.4195, "x_pc":-4.03966, "y_pc":-4.15874, "z_pc":2.75604},
    "N1_10PC_STRICT_0145": {"name":"LP 944-20", "cls":"M-dwarf", "mass_msun":0.08, "dist_pc":6.4268, "x_pc":3.01134, "y_pc":4.28447, "z_pc":-3.72545},
    "N1_10PC_STRICT_0146": {"name":"HL 4", "cls":"white_dwarf", "mass_msun":0.6, "dist_pc":6.4417, "x_pc":0.13543, "y_pc":6.42319, "z_pc":-0.46942},
    "N1_10PC_STRICT_0147": {"name":"GL Vir", "cls":"M-dwarf", "mass_msun":0.2625, "dist_pc":6.4641, "x_pc":-6.32091, "y_pc":-0.52431, "z_pc":1.24747},
    "N1_10PC_STRICT_0148": {"name":"GJ 625", "cls":"M-dwarf", "mass_msun":0.4875, "dist_pc":6.4788, "x_pc":-1.51612, "y_pc":-3.46298, "z_pc":5.26152},
    "N1_10PC_STRICT_0149": {"name":"V1054 Oph", "cls":"M-dwarf", "mass_msun":0.375, "dist_pc":6.4949, "x_pc":-1.78256, "y_pc":-6.17308, "z_pc":-0.94864},
    "N1_10PC_STRICT_0150": {"name":"GJ 644 Ba", "cls":"M-dwarf", "mass_msun":0.2, "dist_pc":6.4949, "x_pc":-1.78256, "y_pc":-6.17308, "z_pc":-0.94864},
    "N1_10PC_STRICT_0151": {"name":"GJ 644 Bb", "cls":"M-dwarf", "mass_msun":0.2, "dist_pc":6.4949, "x_pc":-1.78256, "y_pc":-6.17308, "z_pc":-0.94864},
    "N1_10PC_STRICT_0152": {"name":"VB 8", "cls":"M-dwarf", "mass_msun":0.08, "dist_pc":6.4949, "x_pc":-1.78256, "y_pc":-6.17308, "z_pc":-0.94864},
    "N1_10PC_STRICT_0153": {"name":"GJ 643", "cls":"M-dwarf", "mass_msun":0.3374999999999999, "dist_pc":6.4988, "x_pc":-1.78844, "y_pc":-6.17655, "z_pc":-0.94112},
    "N1_10PC_STRICT_0154": {"name":"L 100-115", "cls":"M-dwarf", "mass_msun":0.3, "dist_pc":6.5037, "x_pc":-1.93571, "y_pc":1.32084, "z_pc":-6.06680},
    "N1_10PC_STRICT_0155": {"name":"HD 219134", "cls":"star", "mass_msun":0.7, "dist_pc":6.5418, "x_pc":3.47342, "y_pc":-0.71693, "z_pc":5.49691},
    "N1_10PC_STRICT_0156": {"name":"WISEA J082507.37+280548.2", "cls":"brown_dwarf", "mass_msun":0.05, "dist_pc":6.5531, "x_pc":-3.42075, "y_pc":4.66010, "z_pc":3.08622},
    "N1_10PC_STRICT_0157": {"name":"WISE J041022.71+150248.4", "cls":"brown_dwarf", "mass_msun":0.05, "dist_pc":6.6094, "x_pc":2.93777, "y_pc":5.66661, "z_pc":1.71551},
    "N1_10PC_STRICT_0158": {"name":"2MASS J05212615+1025328", "cls":"brown_dwarf", "mass_msun":0.05, "dist_pc":6.6578, "x_pc":1.09649, "y_pc":6.45545, "z_pc":1.20458},
    "N1_10PC_STRICT_0159": {"name":"L 471-42", "cls":"M-dwarf", "mass_msun":0.3, "dist_pc":6.6632, "x_pc":-5.14813, "y_pc":-0.88006, "z_pc":-4.13768},
    "N1_10PC_STRICT_0160": {"name":"Ross 104", "cls":"M-dwarf", "mass_msun":0.4125, "dist_pc":6.7477, "x_pc":-6.00754, "y_pc":1.60795, "z_pc":2.61828},
    "N1_10PC_STRICT_0161": {"name":"ksi Boo A", "cls":"star", "mass_msun":1.0, "dist_pc":6.7536, "x_pc":-4.67887, "y_pc":-4.33997, "z_pc":2.20992},
    "N1_10PC_STRICT_0162": {"name":"ksi Boo B", "cls":"star", "mass_msun":0.7, "dist_pc":6.7486, "x_pc":-4.67548, "y_pc":-4.33662, "z_pc":2.20838},
    "N1_10PC_STRICT_0163": {"name":"Ross 619", "cls":"M-dwarf", "mass_msun":0.2625, "dist_pc":6.7695, "x_pc":-3.64349, "y_pc":5.61162, "z_pc":1.02984},
    "N1_10PC_STRICT_0164": {"name":"G 41-14 A", "cls":"M-dwarf", "mass_msun":0.3, "dist_pc":6.7723, "x_pc":-4.71464, "y_pc":4.75823, "z_pc":0.99779},
    "N1_10PC_STRICT_0165": {"name":"G 41-14 B", "cls":"M-dwarf", "mass_msun":0.2, "dist_pc":6.7723, "x_pc":-4.71465, "y_pc":4.75822, "z_pc":0.99779},
    "N1_10PC_STRICT_0166": {"name":"G 41-14 C", "cls":"M-dwarf", "mass_msun":0.2, "dist_pc":6.7723, "x_pc":-4.71464, "y_pc":4.75823, "z_pc":0.99779},
    "N1_10PC_STRICT_0167": {"name":"Ross 775 A", "cls":"M-dwarf", "mass_msun":0.375, "dist_pc":6.7799, "x_pc":5.11945, "y_pc":-3.94135, "z_pc":2.05510},
    "N1_10PC_STRICT_0168": {"name":"Ross 775 B", "cls":"M-dwarf", "mass_msun":0.2, "dist_pc":6.7799, "x_pc":5.11945, "y_pc":-3.94135, "z_pc":2.05510},
    "N1_10PC_STRICT_0169": {"name":"Scholz's Star A", "cls":"M-dwarf", "mass_msun":0.08, "dist_pc":6.7981, "x_pc":-2.29931, "y_pc":6.31271, "z_pc":-1.03779},
    "N1_10PC_STRICT_0170": {"name":"Scholz's Star B", "cls":"brown_dwarf", "mass_msun":0.05, "dist_pc":6.7981, "x_pc":-2.29931, "y_pc":6.31271, "z_pc":-1.03779},
    "N1_10PC_STRICT_0171": {"name":"2MASS J19284155+2356016", "cls":"brown_dwarf", "mass_msun":0.05, "dist_pc":6.8303, "x_pc":2.35598, "y_pc":-5.78130, "z_pc":2.77105},
    "N1_10PC_STRICT_0172": {"name":"WISEPA J025409.45+022359.1", "cls":"brown_dwarf", "mass_msun":0.05, "dist_pc":6.8446, "x_pc":4.95787, "y_pc":4.71025, "z_pc":0.28650},
    "N1_10PC_STRICT_0173": {"name":"BD-17 588 A", "cls":"M-dwarf", "mass_msun":0.375, "dist_pc":6.8638, "x_pc":4.61359, "y_pc":4.68867, "z_pc":-1.96028},
    "N1_10PC_STRICT_0174": {"name":"BD-17 588 B", "cls":"M-dwarf", "mass_msun":0.4125, "dist_pc":6.8638, "x_pc":4.61359, "y_pc":4.68867, "z_pc":-1.96028},
    "N1_10PC_STRICT_0175": {"name":"BD-17 588 C", "cls":"M-dwarf", "mass_msun":0.2, "dist_pc":6.8638, "x_pc":4.61359, "y_pc":4.68867, "z_pc":-1.96028},
    "N1_10PC_STRICT_0176": {"name":"HD 216899", "cls":"M-dwarf", "mass_msun":0.4875, "dist_pc":6.8670, "x_pc":6.33189, "y_pc":-1.79888, "z_pc":1.95634},
    "N1_10PC_STRICT_0177": {"name":"CWISE J105512.11+544328.3", "cls":"brown_dwarf", "mass_msun":0.05, "dist_pc":6.8966, "x_pc":-3.82466, "y_pc":1.11120, "z_pc":5.63024},
    "N1_10PC_STRICT_0178": {"name":"EE Leo", "cls":"M-dwarf", "mass_msun":0.3, "dist_pc":6.9667, "x_pc":-6.60519, "y_pc":2.05565, "z_pc":0.82543},
    "N1_10PC_STRICT_0179": {"name":"BD+01 2447", "cls":"M-dwarf", "mass_msun":0.4499999999999999, "dist_pc":7.0375, "x_pc":-6.48832, "y_pc":2.72361, "z_pc":0.10290},
    "N1_10PC_STRICT_0180": {"name":"HD 199305", "cls":"M-dwarf", "mass_msun":0.525, "dist_pc":7.0396, "x_pc":2.25666, "y_pc":-2.39199, "z_pc":6.22425},
    "N1_10PC_STRICT_0181": {"name":"UCAC4 642-113039", "cls":"M-dwarf", "mass_msun":0.3, "dist_pc":7.0475, "x_pc":4.62216, "y_pc":-3.04858, "z_pc":4.35992},
    "N1_10PC_STRICT_0182": {"name":"LP 914-54", "cls":"M-dwarf", "mass_msun":0.08, "dist_pc":7.0527, "x_pc":-4.46064, "y_pc":-4.33127, "z_pc":-3.32922},
    "N1_10PC_STRICT_0183": {"name":"WISE J205628.91+145953.2", "cls":"brown_dwarf", "mass_msun":0.05, "dist_pc":7.1023, "x_pc":4.77603, "y_pc":-4.92477, "z_pc":1.83807},
    "N1_10PC_STRICT_0184": {"name":"L 230-188", "cls":"M-dwarf", "mass_msun":0.2625, "dist_pc":7.1075, "x_pc":1.93969, "y_pc":3.74379, "z_pc":-5.72175},
    "N1_10PC_STRICT_0185": {"name":"WISE J004945.61+215120.0", "cls":"brown_dwarf", "mass_msun":0.05, "dist_pc":7.1225, "x_pc":6.45540, "y_pc":1.42398, "z_pc":2.65146},
    "N1_10PC_STRICT_0186": {"name":"G 157-77", "cls":"M-dwarf", "mass_msun":0.1875, "dist_pc":7.1767, "x_pc":7.12851, "y_pc":-0.77477, "z_pc":-0.29963},
    "N1_10PC_STRICT_0187": {"name":"GJ 105 A", "cls":"star", "mass_msun":0.7, "dist_pc":7.2286, "x_pc":5.57481, "y_pc":4.51896, "z_pc":0.86758},
    "N1_10PC_STRICT_0188": {"name":"BX Cet", "cls":"M-dwarf", "mass_msun":0.3, "dist_pc":7.2235, "x_pc":5.56766, "y_pc":4.52015, "z_pc":0.86507},
    "N1_10PC_STRICT_0189": {"name":"GJ 105 C", "cls":"M-dwarf", "mass_msun":0.08, "dist_pc":7.2286, "x_pc":5.57481, "y_pc":4.51896, "z_pc":0.86758},
    "N1_10PC_STRICT_0190": {"name":"2MASS J08354256-0819237", "cls":"brown_dwarf", "mass_msun":0.05, "dist_pc":7.2299, "x_pc":-4.49471, "y_pc":5.56542, "z_pc":-1.04640},
    "N1_10PC_STRICT_0191": {"name":"L 788-34", "cls":"M-dwarf", "mass_msun":0.2625, "dist_pc":7.2344, "x_pc":6.28846, "y_pc":-2.82871, "z_pc":-2.18874},
    "N1_10PC_STRICT_0192": {"name":"GJ 667 A", "cls":"star", "mass_msun":0.7, "dist_pc":7.2429, "x_pc":-1.05565, "y_pc":-5.83853, "z_pc":-4.15413},
    "N1_10PC_STRICT_0193": {"name":"GJ 667 B", "cls":"star", "mass_msun":0.7, "dist_pc":7.2429, "x_pc":-1.05565, "y_pc":-5.83853, "z_pc":-4.15413},
    "N1_10PC_STRICT_0194": {"name":"GJ 667 C", "cls":"M-dwarf", "mass_msun":0.4875, "dist_pc":7.2429, "x_pc":-1.05565, "y_pc":-5.83853, "z_pc":-4.15413},
    "N1_10PC_STRICT_0195": {"name":"2MASS J06073908+2429574", "cls":"brown_dwarf", "mass_msun":0.05, "dist_pc":7.2431, "x_pc":-0.21971, "y_pc":6.58744, "z_pc":3.00342},
    "N1_10PC_STRICT_0196": {"name":"WISEP J031325.96+780744.2", "cls":"brown_dwarf", "mass_msun":0.05, "dist_pc":7.3746, "x_pc":1.00800, "y_pc":1.13370, "z_pc":7.21691},
    "N1_10PC_STRICT_0197": {"name":"2MASSW J1507476-162738", "cls":"brown_dwarf", "mass_msun":0.05, "dist_pc":7.4103, "x_pc":-4.85128, "y_pc":-5.19290, "z_pc":-2.10031},
    "N1_10PC_STRICT_0198": {"name":"HD 4628", "cls":"star", "mass_msun":0.7, "dist_pc":7.4352, "x_pc":7.23927, "y_pc":1.55185, "z_pc":0.68364},
    "N1_10PC_STRICT_0199": {"name":"bet Hyi", "cls":"star", "mass_msun":1.0, "dist_pc":7.4783, "x_pc":1.63955, "y_pc":0.18630, "z_pc":-7.29403},
    "N1_10PC_STRICT_0200": {"name":"WISE J200050.19+362950.1", "cls":"brown_dwarf", "mass_msun":0.05, "dist_pc":7.4963, "x_pc":3.03207, "y_pc":-5.20771, "z_pc":4.45871},
    "N1_10PC_STRICT_0201": {"name":"G 203-47 A", "cls":"M-dwarf", "mass_msun":0.3374999999999999, "dist_pc":7.5988, "x_pc":-1.20036, "y_pc":-5.36281, "z_pc":5.24797},
    "N1_10PC_STRICT_0202": {"name":"G 203-47 B", "cls":"white_dwarf", "mass_msun":0.6, "dist_pc":7.5988, "x_pc":-1.20036, "y_pc":-5.36281, "z_pc":5.24797},
    "N1_10PC_STRICT_0203": {"name":"Fomalhaut A", "cls":"star", "mass_msun":2.0, "dist_pc":7.7036, "x_pc":6.45044, "y_pc":-1.79946, "z_pc":-3.80771},
    "N1_10PC_STRICT_0204": {"name":"Fomalhaut B", "cls":"star", "mass_msun":0.7, "dist_pc":7.6015, "x_pc":6.22904, "y_pc":-1.77416, "z_pc":-3.97928},
    "N1_10PC_STRICT_0205": {"name":"Fomalhaut C", "cls":"M-dwarf", "mass_msun":0.3, "dist_pc":7.6763, "x_pc":6.65092, "y_pc":-2.15840, "z_pc":-3.16742},
    "N1_10PC_STRICT_0206": {"name":"GJ 53 A", "cls":"star", "mass_msun":1.0, "dist_pc":7.6753, "x_pc":4.21697, "y_pc":1.29689, "z_pc":6.28056},
    "N1_10PC_STRICT_0207": {"name":"GJ 53 B", "cls":"M-dwarf", "mass_msun":0.3, "dist_pc":7.6753, "x_pc":4.21697, "y_pc":1.29689, "z_pc":6.28056},
    "N1_10PC_STRICT_0208": {"name":"VX Ari", "cls":"M-dwarf", "mass_msun":0.375, "dist_pc":7.6807, "x_pc":5.22563, "y_pc":4.55361, "z_pc":3.30928},
    "N1_10PC_STRICT_0209": {"name":"G 141-36", "cls":"M-dwarf", "mass_msun":0.2249999999999999, "dist_pc":7.6174, "x_pc":1.57913, "y_pc":-7.38184, "z_pc":1.01935},
    "N1_10PC_STRICT_0210": {"name":"BD+11 2576", "cls":"M-dwarf", "mass_msun":0.525, "dist_pc":7.6277, "x_pc":-6.93169, "y_pc":-2.87180, "z_pc":1.37333},
    "N1_10PC_STRICT_0211": {"name":"WISE J173835.53+273259.0", "cls":"brown_dwarf", "mass_msun":0.05, "dist_pc":7.6394, "x_pc":-0.63170, "y_pc":-6.74369, "z_pc":3.53331},
    "N1_10PC_STRICT_0212": {"name":"G 258-33", "cls":"M-dwarf", "mass_msun":0.2625, "dist_pc":7.6422, "x_pc":0.25511, "y_pc":-3.07454, "z_pc":6.99176},
    "N1_10PC_STRICT_0213": {"name":"107 Psc", "cls":"star", "mass_msun":0.7, "dist_pc":7.6439, "x_pc":6.46557, "y_pc":3.10091, "z_pc":2.64762},
    "N1_10PC_STRICT_0214": {"name":"WISEA J235402.79+024014.1", "cls":"brown_dwarf", "mass_msun":0.05, "dist_pc":7.6570, "x_pc":7.64608, "y_pc":-0.19855, "z_pc":0.35667},
    "N1_10PC_STRICT_0215": {"name":"L 499-56", "cls":"M-dwarf", "mass_msun":0.375, "dist_pc":7.6676, "x_pc":5.33065, "y_pc":-3.00037, "z_pc":-4.62324},
    "N1_10PC_STRICT_0216": {"name":"Vega", "cls":"star", "mass_msun":2.0, "dist_pc":7.6787, "x_pc":0.96058, "y_pc":-5.90811, "z_pc":4.80981},
    "N1_10PC_STRICT_0217": {"name":"AN Sex", "cls":"M-dwarf", "mass_msun":0.4875, "dist_pc":7.7069, "x_pc":-6.85663, "y_pc":3.48264, "z_pc":-0.50362},
    "N1_10PC_STRICT_0218": {"name":"HD 157881", "cls":"star", "mass_msun":0.7, "dist_pc":7.7133, "x_pc":-1.14786, "y_pc":-7.62216, "z_pc":0.28347},
    "N1_10PC_STRICT_0219": {"name":"SIPS J1259-4336", "cls":"M-dwarf", "mass_msun":0.08, "dist_pc":7.7263, "x_pc":-5.40938, "y_pc":-1.42686, "z_pc":-5.32895},
    "N1_10PC_STRICT_0220": {"name":"LP 881-64 A", "cls":"M-dwarf", "mass_msun":0.1875, "dist_pc":7.7330, "x_pc":6.84164, "y_pc":0.74126, "z_pc":-3.52718},
    "N1_10PC_STRICT_0221": {"name":"LP 881-64 B", "cls":"M-dwarf", "mass_msun":0.08, "dist_pc":7.7330, "x_pc":6.84164, "y_pc":0.74126, "z_pc":-3.52718},
    "N1_10PC_STRICT_0222": {"name":"LP 881-64 C", "cls":"M-dwarf", "mass_msun":0.2, "dist_pc":7.7330, "x_pc":6.84164, "y_pc":0.74126, "z_pc":-3.52718},
    "N1_10PC_STRICT_0223": {"name":"G 192-13", "cls":"M-dwarf", "mass_msun":0.3, "dist_pc":7.7339, "x_pc":-0.02016, "y_pc":3.91435, "z_pc":6.67009},
    "N1_10PC_STRICT_0224": {"name":"HD 165222", "cls":"M-dwarf", "mass_msun":0.6, "dist_pc":7.7388, "x_pc":0.17319, "y_pc":-7.72605, "z_pc":-0.40944},
    "N1_10PC_STRICT_0225": {"name":"G 109-35", "cls":"M-dwarf", "mass_msun":0.2249999999999999, "dist_pc":7.7527, "x_pc":-1.87777, "y_pc":7.06992, "z_pc":2.56812},
    "N1_10PC_STRICT_0226": {"name":"G 227-22", "cls":"M-dwarf", "mass_msun":0.2249999999999999, "dist_pc":7.7939, "x_pc":0.03374, "y_pc":-3.38455, "z_pc":7.02057},
    "N1_10PC_STRICT_0227": {"name":"WISEP J180026.60+013453.1", "cls":"brown_dwarf", "mass_msun":0.05, "dist_pc":7.8092, "x_pc":0.01514, "y_pc":-7.80618, "z_pc":0.21542},
    "N1_10PC_STRICT_0228": {"name":"GJ 623 A", "cls":"M-dwarf", "mass_msun":0.375, "dist_pc":7.8445, "x_pc":-2.11652, "y_pc":-4.76419, "z_pc":5.86160},
    "N1_10PC_STRICT_0229": {"name":"GJ 623 B", "cls":"M-dwarf", "mass_msun":0.2, "dist_pc":7.8445, "x_pc":-2.11652, "y_pc":-4.76419, "z_pc":5.86160},
    "N1_10PC_STRICT_0230": {"name":"CD-68 47 A", "cls":"M-dwarf", "mass_msun":0.4125, "dist_pc":7.8802, "x_pc":2.88145, "y_pc":0.91404, "z_pc":-7.27734},
    "N1_10PC_STRICT_0231": {"name":"CD-68 47 B", "cls":"M-dwarf", "mass_msun":0.2, "dist_pc":7.8802, "x_pc":2.88145, "y_pc":0.91404, "z_pc":-7.27734},
    "N1_10PC_STRICT_0232": {"name":"WISE J000517.48+373720.5", "cls":"brown_dwarf", "mass_msun":0.05, "dist_pc":7.8802, "x_pc":6.23991, "y_pc":0.14429, "z_pc":4.81047},
    "N1_10PC_STRICT_0233": {"name":"2MASS J07290002-3954043", "cls":"brown_dwarf", "mass_msun":0.05, "dist_pc":7.9177, "x_pc":-2.29994, "y_pc":5.62177, "z_pc":-5.07891},
    "N1_10PC_STRICT_0234": {"name":"G 154-44", "cls":"M-dwarf", "mass_msun":0.3, "dist_pc":7.9712, "x_pc":0.25195, "y_pc":-7.65967, "z_pc":-2.19244},
    "N1_10PC_STRICT_0235": {"name":"SCR J0740-4257", "cls":"M-dwarf", "mass_msun":0.2625, "dist_pc":7.9807, "x_pc":-2.47261, "y_pc":5.29137, "z_pc":-5.43862},
    "N1_10PC_STRICT_0236": {"name":"BB Cap A", "cls":"M-dwarf", "mass_msun":0.2625, "dist_pc":7.9808, "x_pc":6.26713, "y_pc":-4.75133, "z_pc":-1.35718},
    "N1_10PC_STRICT_0237": {"name":"BB Cap B", "cls":"M-dwarf", "mass_msun":0.2, "dist_pc":7.9808, "x_pc":6.26713, "y_pc":-4.75133, "z_pc":-1.35718},
    "N1_10PC_STRICT_0238": {"name":"Tabit", "cls":"star", "mass_msun":1.3, "dist_pc":8.0244, "x_pc":2.40022, "y_pc":7.59501, "z_pc":0.97255},
    "N1_10PC_STRICT_0239": {"name":"CD-44 3045 A", "cls":"M-dwarf", "mass_msun":0.375, "dist_pc":8.0276, "x_pc":-1.43264, "y_pc":5.56471, "z_pc":-5.60577},
    "N1_10PC_STRICT_0240": {"name":"CD-44 3045 B", "cls":"M-dwarf", "mass_msun":0.375, "dist_pc":8.0414, "x_pc":-1.43500, "y_pc":5.57422, "z_pc":-5.61538},
    "N1_10PC_STRICT_0241": {"name":"GJ 1151", "cls":"M-dwarf", "mass_msun":0.2625, "dist_pc":8.0426, "x_pc":-5.33833, "y_pc":0.21159, "z_pc":6.01174},
    "N1_10PC_STRICT_0242": {"name":"L 399-68", "cls":"M-dwarf", "mass_msun":0.375, "dist_pc":8.0525, "x_pc":-5.74294, "y_pc":-1.03208, "z_pc":-5.54942},
    "N1_10PC_STRICT_0243": {"name":"chi Dra A", "cls":"star", "mass_msun":1.3, "dist_pc":8.0574, "x_pc":0.21977, "y_pc":-2.38174, "z_pc":7.69417},
    "N1_10PC_STRICT_0244": {"name":"chi Dra B", "cls":"star", "mass_msun":0.7, "dist_pc":8.0574, "x_pc":0.21977, "y_pc":-2.38174, "z_pc":7.69417},
    "N1_10PC_STRICT_0245": {"name":"GJ 486", "cls":"M-dwarf", "mass_msun":0.3374999999999999, "dist_pc":8.0791, "x_pc":-7.78899, "y_pc":-1.65296, "z_pc":1.36811},
    "N1_10PC_STRICT_0246": {"name":"2MASSW J2148162+400359", "cls":"brown_dwarf", "mass_msun":0.05, "dist_pc":8.0857, "x_pc":5.19376, "y_pc":-3.36355, "z_pc":5.20479},
    "N1_10PC_STRICT_0247": {"name":"G 262-15", "cls":"M-dwarf", "mass_msun":0.4125, "dist_pc":8.0870, "x_pc":2.05184, "y_pc":-2.66069, "z_pc":7.35601},
    "N1_10PC_STRICT_0248": {"name":"G 13-22", "cls":"M-dwarf", "mass_msun":0.2625, "dist_pc":8.0878, "x_pc":-8.07168, "y_pc":-0.50284, "z_pc":0.08790},
    "N1_10PC_STRICT_0249": {"name":"L 674-15", "cls":"M-dwarf", "mass_msun":0.3374999999999999, "dist_pc":8.1167, "x_pc":-4.13031, "y_pc":6.31889, "z_pc":-2.98202},
    "N1_10PC_STRICT_0250": {"name":"EGGR 290", "cls":"white_dwarf", "mass_msun":0.6, "dist_pc":8.1170, "x_pc":0.12636, "y_pc":8.08049, "z_pc":0.75814},
    "N1_10PC_STRICT_0251": {"name":"IRAS 21500+5903", "cls":"M-dwarf", "mass_msun":0.4499999999999999, "dist_pc":8.1263, "x_pc":3.51549, "y_pc":-2.20450, "z_pc":6.98704},
    "N1_10PC_STRICT_0252": {"name":"UCAC4 747-070768", "cls":"white_dwarf", "mass_msun":0.6, "dist_pc":8.4634, "x_pc":3.66179, "y_pc":-2.29558, "z_pc":7.27678},
    "N1_10PC_STRICT_0253": {"name":"GJ 686", "cls":"M-dwarf", "mass_msun":0.4875, "dist_pc":8.1596, "x_pc":-0.74437, "y_pc":-7.69771, "z_pc":2.60206},
    "N1_10PC_STRICT_0254": {"name":"LAWD 26", "cls":"white_dwarf", "mass_msun":0.6, "dist_pc":8.1691, "x_pc":-1.46346, "y_pc":2.71781, "z_pc":-7.56343},
    "N1_10PC_STRICT_0255": {"name":"UGPS J052127.27+364048.6", "cls":"brown_dwarf", "mass_msun":0.05, "dist_pc":8.1833, "x_pc":1.09859, "y_pc":6.47027, "z_pc":4.88828},
    "N1_10PC_STRICT_0256": {"name":"GJ 66 A", "cls":"star", "mass_msun":0.7, "dist_pc":8.1965, "x_pc":4.13451, "y_pc":1.92362, "z_pc":-6.81087},
    "N1_10PC_STRICT_0257": {"name":"GJ 66 B", "cls":"star", "mass_msun":0.7, "dist_pc":8.1894, "x_pc":4.13126, "y_pc":1.92217, "z_pc":-6.80474},
    "N1_10PC_STRICT_0258": {"name":"L 173-19", "cls":"M-dwarf", "mass_msun":0.4499999999999999, "dist_pc":8.2164, "x_pc":3.97579, "y_pc":2.31029, "z_pc":-6.80912},
    "N1_10PC_STRICT_0259": {"name":"HD 217357", "cls":"star", "mass_msun":0.7, "dist_pc":8.2323, "x_pc":7.34739, "y_pc":-1.96009, "z_pc":-3.15357},
    "N1_10PC_STRICT_0260": {"name":"Ross 318", "cls":"M-dwarf", "mass_msun":0.375, "dist_pc":8.2332, "x_pc":2.49208, "y_pc":0.69857, "z_pc":7.81580},
    "N1_10PC_STRICT_0261": {"name":"WISE J115013.85+630241.5", "cls":"brown_dwarf", "mass_msun":0.05, "dist_pc":8.2372, "x_pc":-3.73059, "y_pc":0.15903, "z_pc":7.34230},
    "N1_10PC_STRICT_0262": {"name":"LAWD 96", "cls":"white_dwarf", "mass_msun":0.6, "dist_pc":8.3323, "x_pc":6.07688, "y_pc":0.05817, "z_pc":-5.70053},
    "N1_10PC_STRICT_0263": {"name":"mu. Her Aa", "cls":"star", "mass_msun":1.0, "dist_pc":8.3386, "x_pc":-0.43608, "y_pc":-7.36884, "z_pc":3.87834},
    "N1_10PC_STRICT_0264": {"name":"mu. Her Ab", "cls":"M-dwarf", "mass_msun":0.3, "dist_pc":8.3058, "x_pc":-0.43573, "y_pc":-7.34004, "z_pc":3.86265},
    "N1_10PC_STRICT_0265": {"name":"mu. Her B", "cls":"M-dwarf", "mass_msun":0.3374999999999999, "dist_pc":8.3412, "x_pc":-0.43757, "y_pc":-7.37133, "z_pc":3.87910},
    "N1_10PC_STRICT_0266": {"name":"mu. Her C", "cls":"M-dwarf", "mass_msun":0.2, "dist_pc":8.3412, "x_pc":-0.43757, "y_pc":-7.37133, "z_pc":3.87910},
    "N1_10PC_STRICT_0267": {"name":"GJ 747 A", "cls":"M-dwarf", "mass_msun":0.3374999999999999, "dist_pc":8.3195, "x_pc":2.04277, "y_pc":-6.70856, "z_pc":4.47614},
    "N1_10PC_STRICT_0268": {"name":"GJ 747 B", "cls":"M-dwarf", "mass_msun":0.2, "dist_pc":8.3195, "x_pc":2.04277, "y_pc":-6.70856, "z_pc":4.47614},
    "N1_10PC_STRICT_0269": {"name":"2MASS J03480772-6022270", "cls":"brown_dwarf", "mass_msun":0.05, "dist_pc":8.3264, "x_pc":2.23975, "y_pc":3.45293, "z_pc":-7.23807},
    "N1_10PC_STRICT_0270": {"name":"Wolf 489", "cls":"white_dwarf", "mass_msun":0.6, "dist_pc":8.3503, "x_pc":-7.60579, "y_pc":-3.40479, "z_pc":0.53515},
    "N1_10PC_STRICT_0271": {"name":"G 227-29", "cls":"M-dwarf", "mass_msun":0.3, "dist_pc":8.3506, "x_pc":0.38226, "y_pc":-3.89587, "z_pc":7.37622},
    "N1_10PC_STRICT_0272": {"name":"G 130-4", "cls":"M-dwarf", "mass_msun":0.3, "dist_pc":8.3626, "x_pc":6.70101, "y_pc":-0.49427, "z_pc":4.97855},
    "N1_10PC_STRICT_0273": {"name":"SCR J1546-5534 A", "cls":"M-dwarf", "mass_msun":0.08, "dist_pc":8.3966, "x_pc":-2.60767, "y_pc":-3.96553, "z_pc":-6.92655},
    "N1_10PC_STRICT_0274": {"name":"SCR J1546-5534 B", "cls":"brown_dwarf", "mass_msun":0.05, "dist_pc":8.3966, "x_pc":-2.60767, "y_pc":-3.96553, "z_pc":-6.92655},
    "N1_10PC_STRICT_0275": {"name":"HD 32450 A", "cls":"M-dwarf", "mass_msun":0.6, "dist_pc":8.3630, "x_pc":1.93594, "y_pc":7.54974, "z_pc":-3.03216},
    "N1_10PC_STRICT_0276": {"name":"HD 32450 B", "cls":"M-dwarf", "mass_msun":0.2, "dist_pc":8.4157, "x_pc":1.94815, "y_pc":7.59733, "z_pc":-3.05123},
    "N1_10PC_STRICT_0277": {"name":"2MASS J00345157+0523050", "cls":"brown_dwarf", "mass_msun":0.05, "dist_pc":8.4175, "x_pc":8.28353, "y_pc":1.27017, "z_pc":0.79003},
    "N1_10PC_STRICT_0278": {"name":"SCR J1138-7721", "cls":"M-dwarf", "mass_msun":0.2249999999999999, "dist_pc":8.3793, "x_pc":-1.82513, "y_pc":0.17484, "z_pc":-8.17623},
    "N1_10PC_STRICT_0279": {"name":"Chara", "cls":"star", "mass_msun":1.0, "dist_pc":8.4727, "x_pc":-6.29074, "y_pc":-0.93246, "z_pc":5.59850},
    "N1_10PC_STRICT_0280": {"name":"Ross 64", "cls":"M-dwarf", "mass_msun":0.3, "dist_pc":8.4943, "x_pc":-0.83831, "y_pc":7.74864, "z_pc":3.37767},
    "N1_10PC_STRICT_0281": {"name":"CD-37 10765 A", "cls":"M-dwarf", "mass_msun":0.375, "dist_pc":8.5127, "x_pc":-2.85213, "y_pc":-6.11932, "z_pc":-5.18510},
    "N1_10PC_STRICT_0282": {"name":"CD-37 10765 B", "cls":"M-dwarf", "mass_msun":0.2249999999999999, "dist_pc":8.4977, "x_pc":-2.84718, "y_pc":-6.10841, "z_pc":-5.17605},
    "N1_10PC_STRICT_0283": {"name":"CD-32 5613", "cls":"white_dwarf", "mass_msun":0.6, "dist_pc":8.5182, "x_pc":-4.63151, "y_pc":5.44595, "z_pc":-4.63141},
    "N1_10PC_STRICT_0284": {"name":"61 Vir", "cls":"star", "mass_msun":1.0, "dist_pc":8.5344, "x_pc":-7.63277, "y_pc":-2.71735, "z_pc":-2.68199},
    "N1_10PC_STRICT_0285": {"name":"EGGR 453", "cls":"white_dwarf", "mass_msun":0.6, "dist_pc":8.5369, "x_pc":8.12731, "y_pc":-2.40996, "z_pc":-1.00856},
    "N1_10PC_STRICT_0286": {"name":"FN Vir", "cls":"M-dwarf", "mass_msun":0.2625, "dist_pc":8.5446, "x_pc":-8.20763, "y_pc":-2.22004, "z_pc":0.84666},
    "N1_10PC_STRICT_0287": {"name":"G 89-32 A", "cls":"M-dwarf", "mass_msun":0.2625, "dist_pc":8.5763, "x_pc":-3.47607, "y_pc":7.76877, "z_pc":1.05667},
    "N1_10PC_STRICT_0288": {"name":"G 89-32 B", "cls":"M-dwarf", "mass_msun":0.2249999999999999, "dist_pc":8.5763, "x_pc":-3.47607, "y_pc":7.76877, "z_pc":1.05667},
    "N1_10PC_STRICT_0289": {"name":"CWISEP J040235.55-265145.4", "cls":"brown_dwarf", "mass_msun":0.05, "dist_pc":8.5911, "x_pc":3.75655, "y_pc":6.68019, "z_pc":-3.88199},
    "N1_10PC_STRICT_0290": {"name":"L 49-19", "cls":"M-dwarf", "mass_msun":0.375, "dist_pc":8.5975, "x_pc":2.07354, "y_pc":-0.59765, "z_pc":-8.32224},
    "N1_10PC_STRICT_0291": {"name":"CD Cet", "cls":"M-dwarf", "mass_msun":0.2625, "dist_pc":8.6008, "x_pc":5.69572, "y_pc":6.40472, "z_pc":0.71599},
    "N1_10PC_STRICT_0292": {"name":"zet Tuc", "cls":"star", "mass_msun":1.3, "dist_pc":8.6071, "x_pc":3.64117, "y_pc":0.32084, "z_pc":-7.79242},
    "N1_10PC_STRICT_0293": {"name":"NLTT 40406", "cls":"M-dwarf", "mass_msun":0.1875, "dist_pc":8.6175, "x_pc":-5.16027, "y_pc":-6.75560, "z_pc":1.41259},
    "N1_10PC_STRICT_0294": {"name":"LP 666-9", "cls":"M-dwarf", "mass_msun":0.08, "dist_pc":8.6589, "x_pc":-5.93822, "y_pc":6.27985, "z_pc":-0.52758},
    "N1_10PC_STRICT_0295": {"name":"AP Col", "cls":"M-dwarf", "mass_msun":0.2249999999999999, "dist_pc":8.6656, "x_pc":-0.15163, "y_pc":7.13497, "z_pc":-4.91556},
    "N1_10PC_STRICT_0296": {"name":"PM J11413-3624", "cls":"M-dwarf", "mass_msun":0.2249999999999999, "dist_pc":8.6893, "x_pc":-6.97017, "y_pc":0.56787, "z_pc":-5.15742},
    "N1_10PC_STRICT_0297": {"name":"chi01 Ori A", "cls":"star", "mass_msun":1.0, "dist_pc":8.6995, "x_pc":0.20011, "y_pc":8.15794, "z_pc":3.01471},
    "N1_10PC_STRICT_0298": {"name":"chi01 Ori B", "cls":"M-dwarf", "mass_msun":0.2, "dist_pc":8.6995, "x_pc":0.20011, "y_pc":8.15794, "z_pc":3.01471},
    "N1_10PC_STRICT_0299": {"name":"G 19-7", "cls":"M-dwarf", "mass_msun":0.3, "dist_pc":8.7020, "x_pc":-2.35148, "y_pc":-8.35224, "z_pc":-0.66014},
    "N1_10PC_STRICT_0300": {"name":"LP 991-84", "cls":"M-dwarf", "mass_msun":0.2625, "dist_pc":8.7257, "x_pc":6.10088, "y_pc":2.82435, "z_pc":-5.56238},
    "N1_10PC_STRICT_0301": {"name":"Alula Australis", "cls":"star", "mass_msun":1.3, "dist_pc":8.7346, "x_pc":-7.32175, "y_pc":1.35127, "z_pc":4.56727},
    "N1_10PC_STRICT_0302": {"name":"ksi UMa Ab", "cls":"M-dwarf", "mass_msun":0.375, "dist_pc":8.7346, "x_pc":-7.32175, "y_pc":1.35127, "z_pc":4.56727},
    "N1_10PC_STRICT_0303": {"name":"ksi UMa Ba", "cls":"star", "mass_msun":1.0, "dist_pc":8.7346, "x_pc":-7.32175, "y_pc":1.35127, "z_pc":4.56727},
    "N1_10PC_STRICT_0304": {"name":"ksi UMa Bb", "cls":"star", "mass_msun":0.7, "dist_pc":8.7346, "x_pc":-7.32175, "y_pc":1.35127, "z_pc":4.56727},
    "N1_10PC_STRICT_0305": {"name":"WISE J111838.70+312537.9", "cls":"brown_dwarf", "mass_msun":0.05, "dist_pc":8.7346, "x_pc":-7.32175, "y_pc":1.35127, "z_pc":4.56727},
    "N1_10PC_STRICT_0306": {"name":"LSPM J0036+1821", "cls":"brown_dwarf", "mass_msun":0.05, "dist_pc":8.7356, "x_pc":8.18759, "y_pc":1.30724, "z_pc":2.75066},
    "N1_10PC_STRICT_0307": {"name":"HD 50281 A", "cls":"star", "mass_msun":0.7, "dist_pc":8.7447, "x_pc":-1.96990, "y_pc":8.48338, "z_pc":-0.78856},
    "N1_10PC_STRICT_0308": {"name":"HD 50281 Ba", "cls":"M-dwarf", "mass_msun":0.4499999999999999, "dist_pc":8.7496, "x_pc":-1.97092, "y_pc":8.48789, "z_pc":-0.79149},
    "N1_10PC_STRICT_0309": {"name":"HD 50281 Bb", "cls":"M-dwarf", "mass_msun":0.2, "dist_pc":8.7496, "x_pc":-1.97092, "y_pc":8.48789, "z_pc":-0.79149},
    "N1_10PC_STRICT_0310": {"name":"MCC 135", "cls":"M-dwarf", "mass_msun":0.4875, "dist_pc":8.7654, "x_pc":-7.15074, "y_pc":0.27732, "z_pc":5.06178},
    "N1_10PC_STRICT_0311": {"name":"WISENF J193656.08+040801.2", "cls":"brown_dwarf", "mass_msun":0.05, "dist_pc":8.7796, "x_pc":3.59415, "y_pc":-7.98523, "z_pc":0.63254},
    "N1_10PC_STRICT_0312": {"name":"41 Ara A", "cls":"star", "mass_msun":1.0, "dist_pc":8.7911, "x_pc":-1.07177, "y_pc":-5.94036, "z_pc":-6.39116},
    "N1_10PC_STRICT_0313": {"name":"41 Ara Ba", "cls":"M-dwarf", "mass_msun":0.6, "dist_pc":8.7831, "x_pc":-1.07120, "y_pc":-5.93480, "z_pc":-6.38539},
    "N1_10PC_STRICT_0314": {"name":"41 Ara Bb", "cls":"M-dwarf", "mass_msun":0.2, "dist_pc":8.7831, "x_pc":-1.07120, "y_pc":-5.93480, "z_pc":-6.38539},
    "N1_10PC_STRICT_0315": {"name":"HU Del A", "cls":"M-dwarf", "mass_msun":0.2625, "dist_pc":8.8183, "x_pc":5.28619, "y_pc":-6.90047, "z_pc":1.48420},
    "N1_10PC_STRICT_0316": {"name":"HU Del B", "cls":"M-dwarf", "mass_msun":0.2, "dist_pc":8.8183, "x_pc":5.28619, "y_pc":-6.90047, "z_pc":1.48420},
    "N1_10PC_STRICT_0317": {"name":"HD 192310", "cls":"star", "mass_msun":0.7, "dist_pc":8.8116, "x_pc":4.36952, "y_pc":-6.52005, "z_pc":-4.00500},
    "N1_10PC_STRICT_0318": {"name":"GJ 849", "cls":"M-dwarf", "mass_msun":0.3374999999999999, "dist_pc":8.8149, "x_pc":7.78780, "y_pc":-4.06736, "z_pc":-0.71320},
    "N1_10PC_STRICT_0319": {"name":"Ross 730", "cls":"M-dwarf", "mass_msun":0.4499999999999999, "dist_pc":8.8299, "x_pc":2.38040, "y_pc":-7.89874, "z_pc":3.14800},
    "N1_10PC_STRICT_0320": {"name":"GJ 745 B", "cls":"M-dwarf", "mass_msun":0.4499999999999999, "dist_pc":8.8321, "x_pc":2.38557, "y_pc":-7.90004, "z_pc":3.14724},
    "N1_10PC_STRICT_0321": {"name":"L 32-8", "cls":"M-dwarf", "mass_msun":0.375, "dist_pc":8.8392, "x_pc":-0.32208, "y_pc":2.17091, "z_pc":-8.56246},
    "N1_10PC_STRICT_0322": {"name":"L 32-9", "cls":"M-dwarf", "mass_msun":0.4499999999999999, "dist_pc":8.8394, "x_pc":-0.32145, "y_pc":2.17029, "z_pc":-8.56275},
    "N1_10PC_STRICT_0323": {"name":"HD 32147", "cls":"star", "mass_msun":0.7, "dist_pc":8.8440, "x_pc":2.24677, "y_pc":8.50766, "z_pc":-0.88738},
    "N1_10PC_STRICT_0324": {"name":"G 111-47", "cls":"M-dwarf", "mass_msun":0.3374999999999999, "dist_pc":8.8501, "x_pc":-3.27946, "y_pc":5.78365, "z_pc":5.84118},
    "N1_10PC_STRICT_0325": {"name":"Ross 695", "cls":"M-dwarf", "mass_msun":0.4499999999999999, "dist_pc":8.8752, "x_pc":-8.37893, "y_pc":-0.91378, "z_pc":-2.77976},
    "N1_10PC_STRICT_0326": {"name":"LEHPM 3396", "cls":"M-dwarf", "mass_msun":0.08, "dist_pc":8.8802, "x_pc":3.39766, "y_pc":4.60296, "z_pc":-6.79167},
    "N1_10PC_STRICT_0327": {"name":"SCR J0630-7643 A", "cls":"M-dwarf", "mass_msun":0.2, "dist_pc":8.8764, "x_pc":-0.27301, "y_pc":2.02109, "z_pc":-8.63892},
    "N1_10PC_STRICT_0328": {"name":"SCR J0630-7643 B", "cls":"M-dwarf", "mass_msun":0.2, "dist_pc":8.8811, "x_pc":-0.27321, "y_pc":2.02217, "z_pc":-8.64349},
    "N1_10PC_STRICT_0329": {"name":"2MASSI J0727182+171001", "cls":"brown_dwarf", "mass_msun":0.05, "dist_pc":8.8889, "x_pc":-3.15756, "y_pc":7.88408, "z_pc":2.62363},
    "N1_10PC_STRICT_0330": {"name":"CWISEP J181006.00-101001.1", "cls":"brown_dwarf", "mass_msun":0.05, "dist_pc":8.8889, "x_pc":0.38557, "y_pc":-8.74082, "z_pc":-1.56902},
    "N1_10PC_STRICT_0331": {"name":"GJ 216 A", "cls":"star", "mass_msun":1.3, "dist_pc":8.9050, "x_pc":0.55771, "y_pc":8.21123, "z_pc":-3.40063},
    "N1_10PC_STRICT_0332": {"name":"AK Lep", "cls":"star", "mass_msun":0.7, "dist_pc":8.8916, "x_pc":0.55773, "y_pc":8.20034, "z_pc":-3.39167},
    "N1_10PC_STRICT_0333": {"name":"GJ 867 A", "cls":"M-dwarf", "mass_msun":0.4499999999999999, "dist_pc":8.9258, "x_pc":7.83466, "y_pc":-2.89937, "z_pc":-3.14361},
    "N1_10PC_STRICT_0334": {"name":"GJ 867 B", "cls":"M-dwarf", "mass_msun":0.3374999999999999, "dist_pc":8.8506, "x_pc":7.76890, "y_pc":-2.87524, "z_pc":-3.11613},
    "N1_10PC_STRICT_0335": {"name":"GJ 867 C", "cls":"M-dwarf", "mass_msun":0.2, "dist_pc":8.9258, "x_pc":7.83466, "y_pc":-2.89937, "z_pc":-3.14361},
    "N1_10PC_STRICT_0336": {"name":"GJ 867 D", "cls":"brown_dwarf", "mass_msun":0.05, "dist_pc":8.8506, "x_pc":7.76890, "y_pc":-2.87524, "z_pc":-3.11613},
    "N1_10PC_STRICT_0337": {"name":"G 113-20", "cls":"M-dwarf", "mass_msun":0.4499999999999999, "dist_pc":8.9390, "x_pc":-5.00140, "y_pc":7.40607, "z_pc":0.20324},
    "N1_10PC_STRICT_0338": {"name":"G 193-27 A", "cls":"M-dwarf", "mass_msun":0.2249999999999999, "dist_pc":9.0231, "x_pc":-1.50606, "y_pc":5.25670, "z_pc":7.17744},
    "N1_10PC_STRICT_0339": {"name":"G 193-27 B", "cls":"M-dwarf", "mass_msun":0.2, "dist_pc":9.0231, "x_pc":-1.50606, "y_pc":5.25670, "z_pc":7.17744},
    "N1_10PC_STRICT_0340": {"name":"SZ UMa", "cls":"M-dwarf", "mass_msun":0.525, "dist_pc":9.0719, "x_pc":-3.65542, "y_pc":0.64533, "z_pc":8.27773},
    "N1_10PC_STRICT_0341": {"name":"GJ 433", "cls":"M-dwarf", "mass_msun":0.4499999999999999, "dist_pc":9.0768, "x_pc":-7.60770, "y_pc":0.81814, "z_pc":-4.88280},
    "N1_10PC_STRICT_0342": {"name":"Rana", "cls":"star", "mass_msun":0.7, "dist_pc":9.0888, "x_pc":5.03322, "y_pc":7.40940, "z_pc":-1.54076},
    "N1_10PC_STRICT_0343": {"name":"HD 115953 Aa", "cls":"M-dwarf", "mass_msun":0.4499999999999999, "dist_pc":9.0923, "x_pc":-5.74371, "y_pc":-2.08387, "z_pc":6.73323},
    "N1_10PC_STRICT_0344": {"name":"HD 115953 Ab", "cls":"M-dwarf", "mass_msun":0.2, "dist_pc":9.0923, "x_pc":-5.74371, "y_pc":-2.08387, "z_pc":6.73323},
    "N1_10PC_STRICT_0345": {"name":"HD 115953 B", "cls":"M-dwarf", "mass_msun":0.2, "dist_pc":9.0923, "x_pc":-5.74371, "y_pc":-2.08387, "z_pc":6.73323},
    "N1_10PC_STRICT_0346": {"name":"LP 469-206", "cls":"M-dwarf", "mass_msun":0.2249999999999999, "dist_pc":9.0950, "x_pc":7.31823, "y_pc":4.95979, "z_pc":2.13631},
    "N1_10PC_STRICT_0347": {"name":"EGGR 246", "cls":"white_dwarf", "mass_msun":0.6, "dist_pc":9.0969, "x_pc":8.27632, "y_pc":1.51245, "z_pc":-3.45956},
    "N1_10PC_STRICT_0348": {"name":"V374 Peg", "cls":"M-dwarf", "mass_msun":0.3374999999999999, "dist_pc":9.1029, "x_pc":6.96200, "y_pc":-3.97000, "z_pc":4.31659},
    "N1_10PC_STRICT_0349": {"name":"2MASS J06523073+4710348", "cls":"brown_dwarf", "mass_msun":0.05, "dist_pc":9.1104, "x_pc":-1.40644, "y_pc":6.03082, "z_pc":6.68206},
    "N1_10PC_STRICT_0350": {"name":"WT 460 A", "cls":"M-dwarf", "mass_msun":0.1875, "dist_pc":9.1131, "x_pc":-5.72096, "y_pc":-3.71458, "z_pc":-6.04324},
    "N1_10PC_STRICT_0351": {"name":"WT 460 B", "cls":"M-dwarf", "mass_msun":0.2, "dist_pc":9.1131, "x_pc":-5.72096, "y_pc":-3.71458, "z_pc":-6.04324},
    "N1_10PC_STRICT_0352": {"name":"ULAS J141623.94+134836.3", "cls":"brown_dwarf", "mass_msun":0.05, "dist_pc":9.1158, "x_pc":-7.33022, "y_pc":-4.96289, "z_pc":2.17597},
    "N1_10PC_STRICT_0353": {"name":"2MASS J14162408+1348263", "cls":"brown_dwarf", "mass_msun":0.05, "dist_pc":9.2818, "x_pc":-7.46373, "y_pc":-5.05346, "z_pc":2.21526},
    "N1_10PC_STRICT_0354": {"name":"GJ 283 A", "cls":"white_dwarf", "mass_msun":0.6, "dist_pc":9.1455, "x_pc":-3.70053, "y_pc":7.90269, "z_pc":-2.73731},
    "N1_10PC_STRICT_0355": {"name":"GJ 283 B", "cls":"M-dwarf", "mass_msun":0.1124999999999999, "dist_pc":9.1529, "x_pc":-3.70278, "y_pc":7.90958, "z_pc":-2.73941},
    "N1_10PC_STRICT_0356": {"name":"WISE J071322.55-291751.9", "cls":"brown_dwarf", "mass_msun":0.05, "dist_pc":9.1491, "x_pc":-2.51118, "y_pc":7.57333, "z_pc":-4.47720},
    "N1_10PC_STRICT_0357": {"name":"2MASS J03552337+1133437", "cls":"brown_dwarf", "mass_msun":0.05, "dist_pc":9.1627, "x_pc":4.64377, "y_pc":7.68241, "z_pc":1.83605},
    "N1_10PC_STRICT_0358": {"name":"WISEP J213456.73-713743.6", "cls":"brown_dwarf", "mass_msun":0.05, "dist_pc":9.1659, "x_pc":2.32925, "y_pc":-1.70873, "z_pc":-8.69877},
    "N1_10PC_STRICT_0359": {"name":"CF UMa", "cls":"star", "mass_msun":0.7, "dist_pc":9.1718, "x_pc":-7.25434, "y_pc":0.21944, "z_pc":5.60791},
    "N1_10PC_STRICT_0360": {"name":"Ross 1015", "cls":"M-dwarf", "mass_msun":0.3374999999999999, "dist_pc":9.1920, "x_pc":-6.92495, "y_pc":-3.32973, "z_pc":5.04486},
    "N1_10PC_STRICT_0361": {"name":"bet Com", "cls":"star", "mass_msun":1.0, "dist_pc":9.1975, "x_pc":-7.73346, "y_pc":-2.50742, "z_pc":4.30125},
    "N1_10PC_STRICT_0362": {"name":"2MASS J17502484-0016151 A", "cls":"brown_dwarf", "mass_msun":0.05, "dist_pc":9.2097, "x_pc":-0.38540, "y_pc":-9.20155, "z_pc":-0.04339},
    "N1_10PC_STRICT_0363": {"name":"2MASS J17502484-0016151 B", "cls":"brown_dwarf", "mass_msun":0.05, "dist_pc":9.2097, "x_pc":-0.38540, "y_pc":-9.20155, "z_pc":-0.04339},
    "N1_10PC_STRICT_0364": {"name":"WISEP J232519.54-410534.9", "cls":"brown_dwarf", "mass_msun":0.05, "dist_pc":9.2251, "x_pc":6.87301, "y_pc":-1.04786, "z_pc":-6.06351},
    "N1_10PC_STRICT_0365": {"name":"L 737-9 A", "cls":"M-dwarf", "mass_msun":0.3374999999999999, "dist_pc":9.2314, "x_pc":1.95084, "y_pc":8.55099, "z_pc":-2.87998},
    "N1_10PC_STRICT_0366": {"name":"L 737-9 B", "cls":"M-dwarf", "mass_msun":0.2, "dist_pc":9.2314, "x_pc":1.95084, "y_pc":8.55099, "z_pc":-2.87998},
    "N1_10PC_STRICT_0367": {"name":"LP 776-46", "cls":"M-dwarf", "mass_msun":0.375, "dist_pc":9.2359, "x_pc":2.15738, "y_pc":8.54635, "z_pc":-2.75814},
    "N1_10PC_STRICT_0368": {"name":"LP 469-67", "cls":"M-dwarf", "mass_msun":0.1875, "dist_pc":9.2372, "x_pc":7.82465, "y_pc":4.62097, "z_pc":1.65733},
    "N1_10PC_STRICT_0369": {"name":"gam Pav", "cls":"star", "mass_msun":1.3, "dist_pc":9.2584, "x_pc":3.02521, "y_pc":-2.39675, "z_pc":-8.41554},
    "N1_10PC_STRICT_0370": {"name":"G 112-50", "cls":"M-dwarf", "mass_msun":0.2625, "dist_pc":9.2722, "x_pc":-4.35005, "y_pc":8.18850, "z_pc":-0.00110},
    "N1_10PC_STRICT_0371": {"name":"kap01 Cet", "cls":"star", "mass_msun":1.0, "dist_pc":9.2762, "x_pc":5.97192, "y_pc":7.07723, "z_pc":0.54539},
    "N1_10PC_STRICT_0372": {"name":"HD 102365 A", "cls":"star", "mass_msun":1.0, "dist_pc":9.3195, "x_pc":-7.07440, "y_pc":0.41775, "z_pc":-6.05232},
    "N1_10PC_STRICT_0373": {"name":"HD 102365 B", "cls":"M-dwarf", "mass_msun":0.3, "dist_pc":9.3089, "x_pc":-7.06685, "y_pc":0.41648, "z_pc":-6.04503},
    "N1_10PC_STRICT_0374": {"name":"WISE J121756.90+162640.8 A", "cls":"brown_dwarf", "mass_msun":0.05, "dist_pc":9.3110, "x_pc":-8.90284, "y_pc":-0.69890, "z_pc":2.63543},
    "N1_10PC_STRICT_0375": {"name":"WISE J121756.90+162640.8 B", "cls":"brown_dwarf", "mass_msun":0.05, "dist_pc":9.3110, "x_pc":-8.90284, "y_pc":-0.69890, "z_pc":2.63543},
    "N1_10PC_STRICT_0376": {"name":"2MASS J00113182+5908400", "cls":"M-dwarf", "mass_msun":0.1875, "dist_pc":9.3121, "x_pc":4.77066, "y_pc":0.23956, "z_pc":7.99365},
    "N1_10PC_STRICT_0377": {"name":"BD-18 359 A", "cls":"M-dwarf", "mass_msun":0.375, "dist_pc":9.3199, "x_pc":7.59197, "y_pc":4.61169, "z_pc":-2.82045},
    "N1_10PC_STRICT_0378": {"name":"BD-18 359 B", "cls":"M-dwarf", "mass_msun":0.2, "dist_pc":9.3199, "x_pc":7.59197, "y_pc":4.61169, "z_pc":-2.82045},
    "N1_10PC_STRICT_0379": {"name":"2MASS J18212815+1414010", "cls":"brown_dwarf", "mass_msun":0.05, "dist_pc":9.3428, "x_pc":0.84727, "y_pc":-9.01634, "z_pc":2.29700},
    "N1_10PC_STRICT_0380": {"name":"2MASSI J0340094-672405", "cls":"brown_dwarf", "mass_msun":0.05, "dist_pc":9.3580, "x_pc":2.06100, "y_pc":2.94726, "z_pc":-8.63936},
    "N1_10PC_STRICT_0381": {"name":"Ross 837", "cls":"M-dwarf", "mass_msun":0.3374999999999999, "dist_pc":9.3598, "x_pc":-7.94624, "y_pc":-4.50612, "z_pc":2.03891},
    "N1_10PC_STRICT_0382": {"name":"WISEPA J045853.89+643452.9 A", "cls":"brown_dwarf", "mass_msun":0.05, "dist_pc":9.3721, "x_pc":1.05976, "y_pc":3.88060, "z_pc":8.46484},
    "N1_10PC_STRICT_0383": {"name":"WISEPA J045853.89+643452.9 B", "cls":"brown_dwarf", "mass_msun":0.05, "dist_pc":9.3721, "x_pc":1.05976, "y_pc":3.88060, "z_pc":8.46484},
    "N1_10PC_STRICT_0384": {"name":"CD-30 731", "cls":"M-dwarf", "mass_msun":0.4125, "dist_pc":9.3800, "x_pc":6.91768, "y_pc":4.23079, "z_pc":-4.71497},
    "N1_10PC_STRICT_0385": {"name":"EGGR 41", "cls":"white_dwarf", "mass_msun":0.6, "dist_pc":9.4039, "x_pc":3.26212, "y_pc":8.70112, "z_pc":-1.44296},
    "N1_10PC_STRICT_0386": {"name":"WISEA J193054.55-205949.4", "cls":"brown_dwarf", "mass_msun":0.05, "dist_pc":9.4073, "x_pc":3.39275, "y_pc":-8.10075, "z_pc":-3.37121},
    "N1_10PC_STRICT_0387": {"name":"CD-45 5378", "cls":"M-dwarf", "mass_msun":0.525, "dist_pc":9.4186, "x_pc":-5.45355, "y_pc":3.66168, "z_pc":-6.74991},
    "N1_10PC_STRICT_0388": {"name":"GJ 357", "cls":"M-dwarf", "mass_msun":0.4125, "dist_pc":9.4358, "x_pc":-7.09516, "y_pc":5.15352, "z_pc":-3.48355},
    "N1_10PC_STRICT_0389": {"name":"1RXS J115928.5-524717", "cls":"M-dwarf", "mass_msun":0.08, "dist_pc":9.4603, "x_pc":-5.72108, "y_pc":0.01436, "z_pc":-7.53431},
    "N1_10PC_STRICT_0390": {"name":"G 222-11", "cls":"M-dwarf", "mass_msun":0.4499999999999999, "dist_pc":9.4616, "x_pc":-0.05863, "y_pc":1.29899, "z_pc":9.37182},
    "N1_10PC_STRICT_0391": {"name":"UCAC4 379-100760", "cls":"M-dwarf", "mass_msun":0.1875, "dist_pc":9.4766, "x_pc":0.22980, "y_pc":-9.17690, "z_pc":-2.35327},
    "N1_10PC_STRICT_0392": {"name":"GJ 176", "cls":"M-dwarf", "mass_msun":0.4499999999999999, "dist_pc":9.4852, "x_pc":2.95978, "y_pc":8.46862, "z_pc":3.08075},
    "N1_10PC_STRICT_0393": {"name":"CD-51 6859", "cls":"M-dwarf", "mass_msun":0.375, "dist_pc":9.4925, "x_pc":-5.76450, "y_pc":-0.96052, "z_pc":-7.48031},
    "N1_10PC_STRICT_0394": {"name":"GJ 3512", "cls":"M-dwarf", "mass_msun":0.1875, "dist_pc":9.4973, "x_pc":-3.12047, "y_pc":3.67542, "z_pc":8.18242},
    "N1_10PC_STRICT_0395": {"name":"BPS CS 22879-0089 A", "cls":"M-dwarf", "mass_msun":0.2, "dist_pc":9.5097, "x_pc":4.88746, "y_pc":-5.37293, "z_pc":-6.13834},
    "N1_10PC_STRICT_0396": {"name":"BPS CS 22879-0089 B", "cls":"M-dwarf", "mass_msun":0.2, "dist_pc":9.5097, "x_pc":4.88746, "y_pc":-5.37293, "z_pc":-6.13834},
    "N1_10PC_STRICT_0397": {"name":"L 35-12", "cls":"M-dwarf", "mass_msun":0.2625, "dist_pc":9.5208, "x_pc":-1.52172, "y_pc":1.30955, "z_pc":-9.30668},
    "N1_10PC_STRICT_0398": {"name":"G 192-15", "cls":"M-dwarf", "mass_msun":0.2249999999999999, "dist_pc":9.5275, "x_pc":-0.06668, "y_pc":6.14140, "z_pc":7.28372},
    "N1_10PC_STRICT_0399": {"name":"G 144-25", "cls":"M-dwarf", "mass_msun":0.2625, "dist_pc":9.5312, "x_pc":5.92167, "y_pc":-7.02047, "z_pc":2.54751},
    "N1_10PC_STRICT_0400": {"name":"BD+43 2796", "cls":"M-dwarf", "mass_msun":0.4125, "dist_pc":9.5315, "x_pc":-0.48530, "y_pc":-6.91111, "z_pc":6.54610},
    "N1_10PC_STRICT_0401": {"name":"G 42-24", "cls":"M-dwarf", "mass_msun":0.3, "dist_pc":9.5453, "x_pc":-7.59899, "y_pc":4.66064, "z_pc":3.41264},
    "N1_10PC_STRICT_0402": {"name":"HD 100623 A", "cls":"star", "mass_msun":0.7, "dist_pc":9.5590, "x_pc":-7.98273, "y_pc":0.89268, "z_pc":-5.18208},
    "N1_10PC_STRICT_0403": {"name":"HD 100623 B", "cls":"white_dwarf", "mass_msun":0.6, "dist_pc":9.5550, "x_pc":-7.97922, "y_pc":0.89173, "z_pc":-5.18028},
    "N1_10PC_STRICT_0404": {"name":"Wolf 1069", "cls":"M-dwarf", "mass_msun":0.2249999999999999, "dist_pc":9.5747, "x_pc":2.97108, "y_pc":-4.01163, "z_pc":8.17038},
    "N1_10PC_STRICT_0405": {"name":"61 UMa", "cls":"star", "mass_msun":1.0, "dist_pc":9.5762, "x_pc":-7.89326, "y_pc":0.65415, "z_pc":5.38263},
    "N1_10PC_STRICT_0406": {"name":"PM J20502-3424", "cls":"M-dwarf", "mass_msun":0.2249999999999999, "dist_pc":9.6033, "x_pc":5.35945, "y_pc":-5.83466, "z_pc":-5.42736},
    "N1_10PC_STRICT_0407": {"name":"CD-40 5404", "cls":"M-dwarf", "mass_msun":0.375, "dist_pc":9.6065, "x_pc":-5.92868, "y_pc":4.16055, "z_pc":-6.31080},
    "N1_10PC_STRICT_0408": {"name":"WISE J114156.71-332635.8", "cls":"brown_dwarf", "mass_msun":0.05, "dist_pc":9.6154, "x_pc":-7.99847, "y_pc":0.63172, "z_pc":-5.29915},
    "N1_10PC_STRICT_0409": {"name":"Wolf 227 A", "cls":"M-dwarf", "mass_msun":0.2249999999999999, "dist_pc":9.6265, "x_pc":4.85400, "y_pc":7.82138, "z_pc":2.81693},
    "N1_10PC_STRICT_0410": {"name":"Wolf 227 B", "cls":"brown_dwarf", "mass_msun":0.05, "dist_pc":9.6265, "x_pc":4.85400, "y_pc":7.82138, "z_pc":2.81693},
    "N1_10PC_STRICT_0411": {"name":"2MASS J14053729+8350248", "cls":"brown_dwarf", "mass_msun":0.05, "dist_pc":9.6667, "x_pc":-0.88519, "y_pc":-0.53988, "z_pc":9.61098},
    "N1_10PC_STRICT_0412": {"name":"G 161-7 A", "cls":"M-dwarf", "mass_msun":0.2249999999999999, "dist_pc":9.6777, "x_pc":-7.16838, "y_pc":6.25341, "z_pc":-1.77978},
    "N1_10PC_STRICT_0413": {"name":"G 161-7 B", "cls":"M-dwarf", "mass_msun":0.2249999999999999, "dist_pc":9.6777, "x_pc":-7.16838, "y_pc":6.25341, "z_pc":-1.77978},
    "N1_10PC_STRICT_0414": {"name":"CD-48 11837 A", "cls":"M-dwarf", "mass_msun":0.375, "dist_pc":9.6798, "x_pc":-0.68946, "y_pc":-6.35407, "z_pc":-7.26971},
    "N1_10PC_STRICT_0415": {"name":"CD-48 11837 B", "cls":"M-dwarf", "mass_msun":0.2, "dist_pc":9.6897, "x_pc":-0.69032, "y_pc":-6.36067, "z_pc":-7.27702},
    "N1_10PC_STRICT_0416": {"name":"CFBDS J005910-011401", "cls":"brown_dwarf", "mass_msun":0.05, "dist_pc":9.6899, "x_pc":9.36655, "y_pc":2.47363, "z_pc":-0.20859},
    "N1_10PC_STRICT_0417": {"name":"L 768-119 A", "cls":"M-dwarf", "mass_msun":0.375, "dist_pc":9.6918, "x_pc":-5.17306, "y_pc":-7.53185, "z_pc":-3.23143},
    "N1_10PC_STRICT_0418": {"name":"L 768-119 B", "cls":"brown_dwarf", "mass_msun":0.05, "dist_pc":9.6918, "x_pc":-5.17306, "y_pc":-7.53185, "z_pc":-3.23143},
    "N1_10PC_STRICT_0419": {"name":"AT Mic A", "cls":"M-dwarf", "mass_msun":0.2625, "dist_pc":9.9214, "x_pc":5.43418, "y_pc":-6.37063, "z_pc":-5.32157},
    "N1_10PC_STRICT_0420": {"name":"AT Mic B", "cls":"M-dwarf", "mass_msun":0.3, "dist_pc":9.8066, "x_pc":5.37130, "y_pc":-6.29683, "z_pc":-5.26005},
    "N1_10PC_STRICT_0421": {"name":"AU Mic", "cls":"M-dwarf", "mass_msun":0.5625, "dist_pc":9.7141, "x_pc":5.47478, "y_pc":-6.23374, "z_pc":-5.05281},
    "N1_10PC_STRICT_0422": {"name":"L 88-59", "cls":"white_dwarf", "mass_msun":0.6, "dist_pc":9.7206, "x_pc":3.37690, "y_pc":1.62885, "z_pc":-8.96848},
    "N1_10PC_STRICT_0423": {"name":"WISE J223617.59+510551.9", "cls":"brown_dwarf", "mass_msun":0.05, "dist_pc":9.7276, "x_pc":5.70592, "y_pc":-2.18201, "z_pc":7.57021},
    "N1_10PC_STRICT_0424": {"name":"2MASS J20304235+0749358", "cls":"brown_dwarf", "mass_msun":0.05, "dist_pc":9.7280, "x_pc":5.89075, "y_pc":-7.62742, "z_pc":1.32463},
    "N1_10PC_STRICT_0425": {"name":"G 119-36 A", "cls":"M-dwarf", "mass_msun":0.2249999999999999, "dist_pc":9.7322, "x_pc":-7.54971, "y_pc":2.38965, "z_pc":5.65742},
    "N1_10PC_STRICT_0426": {"name":"G 119-36 B", "cls":"M-dwarf", "mass_msun":0.2, "dist_pc":9.7322, "x_pc":-7.54971, "y_pc":2.38965, "z_pc":5.65742},
    "N1_10PC_STRICT_0427": {"name":"2MASS J02572581-3105523", "cls":"brown_dwarf", "mass_msun":0.05, "dist_pc":9.7372, "x_pc":5.96121, "y_pc":5.82968, "z_pc":-5.02903},
    "N1_10PC_STRICT_0428": {"name":"WISE J111239.24-385700.7", "cls":"brown_dwarf", "mass_msun":0.05, "dist_pc":9.7466, "x_pc":-7.41884, "y_pc":1.55461, "z_pc":-6.12699},
    "N1_10PC_STRICT_0429": {"name":"LP 655-48", "cls":"M-dwarf", "mass_msun":0.15, "dist_pc":9.7471, "x_pc":3.30269, "y_pc":9.12281, "z_pc":-0.93451},
    "N1_10PC_STRICT_0430": {"name":"GJ 436", "cls":"M-dwarf", "mass_msun":0.4125, "dist_pc":9.7750, "x_pc":-8.70620, "y_pc":0.67745, "z_pc":4.39256},
    "N1_10PC_STRICT_0431": {"name":"G 268-110", "cls":"M-dwarf", "mass_msun":0.2249999999999999, "dist_pc":9.7768, "x_pc":8.92152, "y_pc":2.59704, "z_pc":-3.04107},
    "N1_10PC_STRICT_0432": {"name":"2MASSW J1515008+484742", "cls":"brown_dwarf", "mass_msun":0.05, "dist_pc":9.8073, "x_pc":-4.25949, "y_pc":-4.85654, "z_pc":7.37933},
    "N1_10PC_STRICT_0433": {"name":"CWISEP J225628.97+400227.3", "cls":"brown_dwarf", "mass_msun":0.05, "dist_pc":9.8232, "x_pc":7.23354, "y_pc":-2.05758, "z_pc":6.31959},
    "N1_10PC_STRICT_0434": {"name":"HD 151288", "cls":"star", "mass_msun":0.7, "dist_pc":9.8463, "x_pc":-2.63533, "y_pc":-7.77514, "z_pc":5.43608},
    "N1_10PC_STRICT_0435": {"name":"Wolf 46", "cls":"M-dwarf", "mass_msun":0.4875, "dist_pc":9.8596, "x_pc":4.40618, "y_pc":1.23594, "z_pc":8.73328},
    "N1_10PC_STRICT_0436": {"name":"V388 Cas", "cls":"M-dwarf", "mass_msun":0.2249999999999999, "dist_pc":9.8646, "x_pc":4.40171, "y_pc":1.24885, "z_pc":8.73934},
    "N1_10PC_STRICT_0437": {"name":"V547 Cas", "cls":"M-dwarf", "mass_msun":0.4499999999999999, "dist_pc":9.8925, "x_pc":3.78945, "y_pc":0.54222, "z_pc":9.12185},
    "N1_10PC_STRICT_0438": {"name":"GJ 22 B", "cls":"M-dwarf", "mass_msun":0.375, "dist_pc":9.9605, "x_pc":3.81565, "y_pc":0.54596, "z_pc":9.18445},
    "N1_10PC_STRICT_0439": {"name":"GJ 22 C", "cls":"M-dwarf", "mass_msun":0.3, "dist_pc":9.8925, "x_pc":3.78945, "y_pc":0.54222, "z_pc":9.12185},
    "N1_10PC_STRICT_0440": {"name":"12 Oph", "cls":"star", "mass_msun":0.7, "dist_pc":9.8939, "x_pc":-3.52803, "y_pc":-9.23483, "z_pc":-0.40154},
    "N1_10PC_STRICT_0441": {"name":"UPM J0815-2344", "cls":"M-dwarf", "mass_msun":0.2, "dist_pc":9.8970, "x_pc":-5.03951, "y_pc":7.52872, "z_pc":-3.98399},
    "N1_10PC_STRICT_0442": {"name":"G 203-42", "cls":"M-dwarf", "mass_msun":0.2249999999999999, "dist_pc":9.9081, "x_pc":-1.51079, "y_pc":-5.99274, "z_pc":7.74437},
    "N1_10PC_STRICT_0443": {"name":"HD 232979", "cls":"M-dwarf", "mass_msun":0.6, "dist_pc":9.9092, "x_pc":2.10126, "y_pc":5.59706, "z_pc":7.90255},
    "N1_10PC_STRICT_0444": {"name":"G 48-20", "cls":"M-dwarf", "mass_msun":0.3374999999999999, "dist_pc":9.9105, "x_pc":-7.88165, "y_pc":6.00785, "z_pc":0.05539},
    "N1_10PC_STRICT_0445": {"name":"G 160-28", "cls":"M-dwarf", "mass_msun":0.3374999999999999, "dist_pc":9.9275, "x_pc":5.27730, "y_pc":8.34224, "z_pc":-1.05511},
    "N1_10PC_STRICT_0446": {"name":"GJ 1230 A", "cls":"M-dwarf", "mass_msun":0.2249999999999999, "dist_pc":9.9320, "x_pc":1.61118, "y_pc":-8.87179, "z_pc":4.16405},
    "N1_10PC_STRICT_0447": {"name":"GJ 1230 B", "cls":"M-dwarf", "mass_msun":0.2625, "dist_pc":9.9448, "x_pc":1.61326, "y_pc":-8.88314, "z_pc":4.16963},
    "N1_10PC_STRICT_0448": {"name":"GJ 1230 C", "cls":"M-dwarf", "mass_msun":0.2, "dist_pc":9.9320, "x_pc":1.61118, "y_pc":-8.87179, "z_pc":4.16405},
    "N1_10PC_STRICT_0449": {"name":"CE Boo", "cls":"M-dwarf", "mass_msun":0.525, "dist_pc":9.9478, "x_pc":-6.91873, "y_pc":-6.59394, "z_pc":2.75877},
    "N1_10PC_STRICT_0450": {"name":"BD+16 2708 Ba", "cls":"M-dwarf", "mass_msun":0.08, "dist_pc":9.9478, "x_pc":-6.91859, "y_pc":-6.59402, "z_pc":2.75894},
    "N1_10PC_STRICT_0451": {"name":"BD+16 2708 Bb", "cls":"brown_dwarf", "mass_msun":0.05, "dist_pc":9.9478, "x_pc":-6.91859, "y_pc":-6.59402, "z_pc":2.75894},
    "N1_10PC_STRICT_0452": {"name":"L 403-31", "cls":"M-dwarf", "mass_msun":0.2249999999999999, "dist_pc":9.9401, "x_pc":-6.26425, "y_pc":-3.75836, "z_pc":-6.74090},
    "N1_10PC_STRICT_0453": {"name":"LP 98-79", "cls":"M-dwarf", "mass_msun":0.1124999999999999, "dist_pc":9.9690, "x_pc":-3.97934, "y_pc":-3.07008, "z_pc":8.60932},
    "N1_10PC_STRICT_0454": {"name":"WISE J182831.08+265037.7", "cls":"brown_dwarf", "mass_msun":0.05, "dist_pc":9.9701, "x_pc":1.10431, "y_pc":-8.82689, "z_pc":4.50213},
    "N1_10PC_STRICT_0455": {"name":"G 36-24", "cls":"M-dwarf", "mass_msun":0.3374999999999999, "dist_pc":9.9854, "x_pc":7.09615, "y_pc":5.62538, "z_pc":4.20801},
    "N1_10PC_STRICT_0456": {"name":"HD 260655", "cls":"M-dwarf", "mass_msun":0.6, "dist_pc":9.9977, "x_pc":-1.53892, "y_pc":9.40642, "z_pc":3.01739},
    "N1_10PC_STRICT_0457": {"name":"Gaia EDR3 6305165514134625024", "cls":"brown_dwarf", "mass_msun":0.05, "dist_pc":5.7463, "x_pc":-3.85399, "y_pc":-3.85085, "z_pc":-1.82692},
    "N1_10PC_STRICT_0458": {"name":"CWISE J061741.79+194512.8 A", "cls":"brown_dwarf", "mass_msun":0.05, "dist_pc":7.5188, "x_pc":-0.54586, "y_pc":7.05527, "z_pc":2.54117},
    "N1_10PC_STRICT_0459": {"name":"CWISE J061741.79+194512.8 B", "cls":"brown_dwarf", "mass_msun":0.05, "dist_pc":7.5188, "x_pc":-0.54586, "y_pc":7.05527, "z_pc":2.54117},
}


def load_scene(passport):
    """
    Split ROSTER into active (full GFRO) and Node 1 (context-only) source lists,
    per passport doctrine (GCS V).
    """
    active_ids = passport.get("active_sources", [])
    node1_mode = passport.get("node1_mode", "none")  # "all" or "none"

    active_sources = []
    node1_sources = []

    for sid, r in ROSTER.items():
        if sid not in ROSTER:
            continue
        # Determine position
        if "x_pc" in r and sid != "SOL":
            pos = np.array([r["x_pc"], r["y_pc"], r["z_pc"]]) * PC_TO_M
        elif "dist_au" in r:
            # Solar system body - use schematic position for now
            continue  # skip solar system in LSN scene
        else:
            pos = np.zeros(3)

        mass_kg = r["mass_msun"] * MSUN_KG
        src = Source(id=sid, name=r["name"], mass=mass_kg, pos=pos)

        if sid in active_ids:
            active_sources.append(src)
        elif node1_mode == "all":
            node1_sources.append(src)

    return active_sources, node1_sources


# ─────────────────────────────────────────────
# Main solver: passport → emitted ledger
# ─────────────────────────────────────────────

def run(passport: dict, n_rays: int = 192, n_radial: int = 96) -> dict:
    """
    GFRO solver. Passport in. Emitted ledger out.

    Workflow:
    1. Load scene from passport
    2. Emit R0 pairwise Apollonius spheres (analytically exact)
    3. Emit R0 source-context zero sets (targeted root-finding)
    4. Evaluate full E_ij Weyl field at all emitted points
    5. Return compact certified ledger bundle

    The ledger is NOT a field sample. It is a certified geometric record
    of emitted zero sets with full tidal architecture at those locations.
    """
    print(f"Atlas GFRO Emitter — scene: {passport.get('scene_id','unnamed')}")

    # 1. Load scene
    active_sources, node1_sources = load_scene(passport)
    sources = active_sources  # active sources drive R0 pairwise + Weyl evaluation
    print(f"  Active sources: {len(active_sources)}")
    print(f"  Node 1 context sources: {len(node1_sources)}")

    # 2. R0 pairwise Apollonius emission (exact, active only)
    print(f"  Emitting R0 pairwise ({len(active_sources)*(len(active_sources)-1)//2} pairs)...")
    r0_pairwise = emit_R0_pairwise(active_sources)
    print(f"    Emitted {len(r0_pairwise)} Apollonius objects")

    # 3. R0 source-context emission (active source vs all-context including Node 1)
    all_context = active_sources + node1_sources
    print(f"  Emitting R0 source-context ({len(active_sources)} sources, "
          f"{len(all_context)-1} context each)...")
    r0_ctx_all = []
    for i, src in enumerate(active_sources):
        ctx = [s for s in all_context if s.id != src.id]
        pts = emit_R0_source_context(src, ctx, n_rays, n_radial)
        r0_ctx_all.extend(pts)
        if (i+1) % 5 == 0:
            print(f"    {i+1}/{len(active_sources)} done, {len(r0_ctx_all)} points emitted")
    print(f"    Total source-context emitted points: {len(r0_ctx_all)}")

    # 4. Full E_ij evaluation at emitted source-context points (active sources only)
    print(f"  Evaluating full Weyl field at {len(r0_ctx_all)} emitted points...")
    emitted_pos = [np.array(p["pos"]) for p in r0_ctx_all]
    weyl_records = evaluate_weyl_at(emitted_pos, active_sources)
    print(f"  Weyl evaluation complete.")

    # 5. Assemble compact ledger
    ledger = {
        "scene_id": passport.get("scene_id", "unnamed"),
        "regime": passport.get("regime", "weak_field_gr_approximation"),
        "epoch": passport.get("epoch", "J2000"),
        "position_convention": "real_gaia_icrs_coordinates_pc",
        "position_note": "Real Gaia ICRS Cartesian coordinates from EMS_Node1_LocalStellarContext_10pc_STRICT_v0_2.csv. Source: GPT wing Atlas repo. Epoch J2000. 47/48 stellar sources have real coordinates. SOL at origin.",
        "n_sources": len(sources),
        "source_roster": [
            {"id": s.id, "name": s.name, "mass_kg": s.mass, "pos_m": s.pos.tolist()}
            for s in sources
        ],
        "R0_pairwise": {
            "method": "apollonius_analytic_exact",
            "n_objects": len(r0_pairwise),
            "objects": [obj.to_dict() for obj in r0_pairwise],
            "claim_status": "diagnostic_candidate_not_observational",
        },
        "R0_source_context": {
            "method": "gfro_targeted_bisection",
            "n_rays": n_rays,
            "n_radial": n_radial,
            "n_emitted": len(r0_ctx_all),
            "points": r0_ctx_all,
            "claim_status": "diagnostic_candidate_not_observational",
        },
        "weyl_field": {
            "method": "full_E_ij_at_emitted_points",
            "n_points": len(weyl_records),
            "records": weyl_records,
            "note": "Full tidal tensor eigenstructure at GFRO-emitted locations. This is the primary lumen lattice substrate.",
            "claim_status": "diagnostic_candidate_not_observational",
        },
        "node1": {
            "mode": "full_gaia_10pc_volume",
            "n_sources": len(node1_sources),
            "description": "Gaia 10pc volume — EMS_Node1_LocalStellarContext_10pc_STRICT_v0_2.csv",
            "claim_status": "diagnostic_candidate_not_observational"
        },
        "certification": {
            "r0_pairwise_exact": True,
            "r0_ctx_bisection_depth": 52,
            "weyl_evaluated_at_emitted_only": True,
            "claim_status": "diagnostic_candidate_not_observational",
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
