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

# Fibonacci sphere positions for sources without RA/Dec
def fibonacci_positions(sources_data: list) -> dict:
    """
    Assign 3D positions using Fibonacci sphere at correct distances.
    SOL always at origin.
    Flagged as schematic — real Gaia coordinates are Phase 2 v0.2.
    """
    n = len(sources_data)
    phi = np.pi * (1 + np.sqrt(5))
    positions = {}
    fib_idx = 0

    for s in sources_data:
        if s['id'] == 'SOL':
            positions[s['id']] = np.zeros(3)
            continue

        # Distance in meters
        if 'dist_pc' in s:
            dist_m = s['dist_pc'] * PC_TO_M
        elif 'dist_au' in s:
            dist_m = s['dist_au'] * AU_TO_M
        else:
            dist_m = 1e15

        # Fibonacci direction
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
    "PROXIMA_CEN":    {"name":"Proxima Centauri",   "mass_msun":0.1221,   "dist_pc":1.295},
    "ALPHA_CEN_A":    {"name":"Alpha Centauri A",   "mass_msun":1.100,    "dist_pc":1.338},
    "ALPHA_CEN_B":    {"name":"Alpha Centauri B",   "mass_msun":0.907,    "dist_pc":1.338},
    "BARNARDS":       {"name":"Barnard's Star",      "mass_msun":0.144,    "dist_pc":1.828},
    "LUHMAN16A":      {"name":"Luhman 16 A",         "mass_msun":0.032,    "dist_pc":1.998},
    "LUHMAN16B":      {"name":"Luhman 16 B",         "mass_msun":0.027,    "dist_pc":1.998},
    "WISE0855":       {"name":"WISE 0855-0714",       "mass_msun":0.008,    "dist_pc":2.231},
    "WOLF359":        {"name":"Wolf 359",             "mass_msun":0.090,    "dist_pc":2.394},
    "LALANDE21185":   {"name":"Lalande 21185",        "mass_msun":0.386,    "dist_pc":2.547},
    "SIRIUS_A":       {"name":"Sirius A",             "mass_msun":2.063,    "dist_pc":2.637},
    "SIRIUS_B":       {"name":"Sirius B",             "mass_msun":1.018,    "dist_pc":2.637},
    "BL_CETI":        {"name":"BL Ceti",              "mass_msun":0.102,    "dist_pc":2.680},
    "UV_CETI":        {"name":"UV Ceti",              "mass_msun":0.100,    "dist_pc":2.680},
    "ROSS154":        {"name":"Ross 154",             "mass_msun":0.170,    "dist_pc":2.976},
    "ROSS248":        {"name":"Ross 248",             "mass_msun":0.136,    "dist_pc":3.162},
    "EPS_ERI":        {"name":"Epsilon Eridani",      "mass_msun":0.832,    "dist_pc":3.218},
    "LACAILLE9352":   {"name":"Lacaille 9352",        "mass_msun":0.503,    "dist_pc":3.289},
    "ROSS128":        {"name":"Ross 128",             "mass_msun":0.168,    "dist_pc":3.374},
    "EZ_AQR_A":       {"name":"EZ Aquarii A",         "mass_msun":0.110,    "dist_pc":3.452},
    "61CYGNI_A":      {"name":"61 Cygni A",           "mass_msun":0.708,    "dist_pc":3.497},
    "61CYGNI_B":      {"name":"61 Cygni B",           "mass_msun":0.630,    "dist_pc":3.497},
    "STRUVE2398A":    {"name":"Struve 2398 A",        "mass_msun":0.342,    "dist_pc":3.517},
    "STRUVE2398B":    {"name":"Struve 2398 B",        "mass_msun":0.248,    "dist_pc":3.517},
    "GROOMBRIDGE34A": {"name":"Groombridge 34 A",     "mass_msun":0.380,    "dist_pc":3.561},
    "GROOMBRIDGE34B": {"name":"Groombridge 34 B",     "mass_msun":0.158,    "dist_pc":3.561},
    "DX_CANCRI":      {"name":"DX Cancri",            "mass_msun":0.090,    "dist_pc":3.582},
    "EPS_INDI_A":     {"name":"Epsilon Indi A",       "mass_msun":0.762,    "dist_pc":3.622},
    "EPS_INDI_BA":    {"name":"Epsilon Indi Ba",      "mass_msun":0.065,    "dist_pc":3.622},
    "EPS_INDI_BB":    {"name":"Epsilon Indi Bb",      "mass_msun":0.053,    "dist_pc":3.622},
    "TAU_CETI":       {"name":"Tau Ceti",             "mass_msun":0.783,    "dist_pc":3.650},
    "GJ1061":         {"name":"GJ 1061",              "mass_msun":0.113,    "dist_pc":3.674},
    "YZ_CETI":        {"name":"YZ Ceti",              "mass_msun":0.130,    "dist_pc":3.722},
    "LUYTEN_STAR":    {"name":"Luyten's Star",        "mass_msun":0.260,    "dist_pc":3.785},
    "TEEGARDEN":      {"name":"Teegarden's Star",     "mass_msun":0.089,    "dist_pc":3.831},
    "SCR1845":        {"name":"SCR 1845-6357 A",      "mass_msun":0.092,    "dist_pc":3.876},
    "KAPTEYN":        {"name":"Kapteyn's Star",       "mass_msun":0.274,    "dist_pc":3.934},
    "LACAILLE8760":   {"name":"Lacaille 8760",        "mass_msun":0.601,    "dist_pc":3.969},
    "KRUGER60A":      {"name":"Kruger 60 A",          "mass_msun":0.271,    "dist_pc":4.010},
    "KRUGER60B":      {"name":"Kruger 60 B",          "mass_msun":0.176,    "dist_pc":4.010},
    "ROSS614A":       {"name":"Ross 614 A",           "mass_msun":0.222,    "dist_pc":4.130},
    "VAN_MAANEN":     {"name":"Van Maanen's Star",    "mass_msun":0.670,    "dist_pc":4.334},
    "GLIESE1":        {"name":"Gliese 1",             "mass_msun":0.380,    "dist_pc":4.345},
    "WOLF424A":       {"name":"Wolf 424 A",           "mass_msun":0.140,    "dist_pc":4.392},
    "TZ_ARIETIS":     {"name":"TZ Arietis",           "mass_msun":0.150,    "dist_pc":4.461},
    "GJ687":          {"name":"GJ 687",               "mass_msun":0.413,    "dist_pc":4.530},
    "GJ674":          {"name":"GJ 674",               "mass_msun":0.350,    "dist_pc":4.547},
    "GJ440":          {"name":"GJ 440",               "mass_msun":0.550,    "dist_pc":4.626},
    "GJ1002":         {"name":"GJ 1002",              "mass_msun":0.117,    "dist_pc":4.844},
    "GJ412A":         {"name":"GJ 412 A",             "mass_msun":0.396,    "dist_pc":4.854},
}


def load_scene(passport: dict) -> List[Source]:
    """
    Load declared sources from passport into Source objects.
    Assigns schematic Fibonacci positions at declared distances.
    SOL at origin.
    """
    active_ids = passport.get("active_sources", [])
    sources_data = []
    for sid in active_ids:
        if sid in ROSTER:
            r = ROSTER[sid]
            entry = {"id": sid, "name": r["name"], "mass_msun": r["mass_msun"]}
            if "dist_pc" in r:
                entry["dist_pc"] = r["dist_pc"]
            elif "dist_au" in r:
                entry["dist_au"] = r["dist_au"]
            sources_data.append(entry)

    positions = fibonacci_positions(sources_data)

    sources = []
    for sd in sources_data:
        pos = positions[sd["id"]]
        mass_kg = sd["mass_msun"] * MSUN_KG
        sources.append(Source(id=sd["id"], name=sd["name"], mass=mass_kg, pos=pos))

    return sources


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
    sources = load_scene(passport)
    print(f"  Sources loaded: {len(sources)}")

    # 2. R0 pairwise Apollonius emission (exact)
    print(f"  Emitting R0 pairwise ({len(sources)*(len(sources)-1)//2} pairs)...")
    r0_pairwise = emit_R0_pairwise(sources)
    print(f"    Emitted {len(r0_pairwise)} Apollonius objects")

    # 3. R0 source-context emission (targeted root-finding)
    print(f"  Emitting R0 source-context ({len(sources)} sources)...")
    r0_ctx_all = []
    for i, src in enumerate(sources):
        ctx = [s for s in sources if s.id != src.id]
        pts = emit_R0_source_context(src, ctx, n_rays, n_radial)
        r0_ctx_all.extend(pts)
        if (i+1) % 10 == 0:
            print(f"    {i+1}/{len(sources)} done, {len(r0_ctx_all)} points emitted")
    print(f"    Total source-context emitted points: {len(r0_ctx_all)}")

    # 4. Full E_ij evaluation at emitted source-context points
    print(f"  Evaluating full Weyl field at {len(r0_ctx_all)} emitted points...")
    emitted_pos = [np.array(p["pos"]) for p in r0_ctx_all]
    weyl_records = evaluate_weyl_at(emitted_pos, sources)
    print(f"  Weyl evaluation complete.")

    # 5. Assemble compact ledger
    ledger = {
        "scene_id": passport.get("scene_id", "unnamed"),
        "regime": passport.get("regime", "weak_field_gr_approximation"),
        "epoch": passport.get("epoch", "J2000"),
        "position_convention": "schematic_fibonacci_sphere_real_distances",
        "position_note": "Angular positions are schematic. Distances are declared values from passport. Real Gaia RA/Dec coordinates are Phase 2 v0.2.",
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
