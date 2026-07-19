
> [!success] RESOLVED DOWNSTREAM (2026-07-17/18)
> The structural candidate below was CONFIRMED EXACT at O(v) and
> kappa = -2 LOCKED by numeric linearized-Riemann derivation:
> [[OBS_042_C5B2_Numeric_Convention_Lock_Crosscheck_Receipt]].
> E-sign adjudicated and founder-ratified:
> [[C5-B2 E-Sign Adjudication Candidate v0.1]]. The uncertified-sign
> language below is the historical state at drafting time.
# C5-B2 Convention Lock Derivation Table

## Claim Status
Convention-lock table / magnetic-Weyl formula provisional / no calculation certified.

This note is not certified evidence, not a completed derivation, not a repo calculation, not ordinary-energy accounting, not radiative balance, not conservation, and not a prediction.

Surface integration remains unauthorized.

The OBS_037 B_ij candidate remains structurally supported but sign/factor uncertified.

## Purpose
Assemble the convention-lock table required before any final B_ij formula, lobe sign, sample-point sign, or P_normal sign-map calculation.

This note does not derive B_ij. It organizes the convention dependencies that must be resolved.

## Source Links
- [[C5-B2 Literature Convention Extraction v0.1]]
- [[C5-B2 Magnetic Weyl Literature Convention Crosscheck]]
- [[C5-B2 B_ij Structural Derivation Candidate v0.1]]
- [[C5-B2 Linearized Metric B_ij Derivation Passport]]
- [[C5-B2 Explicit Weak Field EB Tensor Model Passport]]
- [[../Frontier Evidence Rule|Frontier Evidence Rule]]
- [[../../Best Practices/Claim Boundary Checklist|Claim Boundary Checklist]]

## Current Candidate

OBS_037 structural candidate:

B_ij^(s) = kappa/c * epsilon_{kl(i} v_s^k E_{j)}^{(s)l}

Expanded:

B_ij^(s)
=
kappa/(2c) [
  epsilon_{kli} v_s^k E_j^{(s)l}
  +
  epsilon_{klj} v_s^k E_i^{(s)l}
]

Current ruling from OBS_039:
Classification B. Candidate survives structurally but needs sign/factor convention calibration.

## Convention Table

| Convention Item | Atlas Current Declaration | Literature / External Target | Decision Needed | Status |
|---|---|---|---|---|
| Metric signature | Pending explicit lock | Costa/Herdeiro and selected PN source may differ | Choose one and propagate signs | unresolved |
| Scalar potential Phi | Phi = -GM/r used schematically | PN conventions may use U = +GM/r | Decide Phi/U sign and E_ij consequence | unresolved |
| g_00 convention | g_00 = -(1 + 2Phi/c^2) schematic | depends on Phi sign | Verify consistency with declared E_ij | unresolved |
| g_0i convention | candidate g_0i = -4 A_i/c^3 | PN/linearized references vary | Lock sign and factor | unresolved |
| Vector potential A_i | A_i = sum GM v_i/r schematic | PN sources may define with c factors or sign | Lock dimensional convention | unresolved |
| Electric Weyl E_ij | E_ij = GM(3n_i n_j - delta_ij)/r^3 | Costa/Herdeiro E(U)_alpha_beta, PN tidal tensor | Confirm sign relative to Weyl definition | unresolved |
| Magnetic Weyl B_ij | OBS_037 candidate | Costa/Herdeiro H(U)_alpha_beta or equivalent | Confirm formula and sign | unresolved |
| B_ij definition | B_ij = 1/2 epsilon_i^{kl} C_klj0 candidate | literature may use dual sign/factor differences | Lock definition | unresolved |
| Levi-Civita orientation | epsilon_xyz = +1 presumed | must match coordinate handedness | Lock orientation | unresolved |
| Observer | Eulerian/static barycentric | observer-dependent E/B split | Confirm compatibility | provisionally declared |
| Tetrad | weak-field barycentric orthonormal | literature may use coordinate/tetrad split | Declare mapping | unresolved |
| Source velocities | A: -y, B: +y | internal Atlas convention | Verify angular momentum +z or correct | unresolved |
| B source construction | B_s from source-local E_s, then sum | must be checked | Decide if source-local construction survives | unresolved |
| Super-Poynting P_BR | P_BR^i ~ epsilon^i_jk E^j_l B^kl | Wylleman / Bel-Robinson convention | Lock sign/factor separately from B_ij | unresolved |
| P_normal sign | positive = outward on F_mid | Atlas local pattern convention | Keep local only, no flux claim | provisionally declared |
| c-factors | B ~ (v/c)E required | linearized metric decides factors | Lock exact c placement | unresolved |

## Decision Matrix

### Decision 1: E sign
Options:
A. Keep Atlas E_ij = GM(3nn - delta)/r^3.
B. Flip sign to match a selected Weyl convention.
C. Keep Atlas sign for diagnostics but record conversion map.

Preferred:
A or C, unless literature mapping forces correction.

### Decision 2: B definition
Options:
A. B_ij = +1/2 epsilon_i^{kl} C_klj0.
B. B_ij = -1/2 epsilon_i^{kl} C_klj0.
C. Literature source uses H_ij with different dual convention; create translation map.

Preferred:
Do not decide until OBS_041 derivation/cross-check.

### Decision 3: kappa
Options:
A. kappa = +2 under chosen convention.
B. kappa = -2 under chosen convention.
C. different factor due to g_0i / B definition normalization.
D. kappa remains symbolic.

Preferred:
D until derivation or formula map locks signs.

### Decision 4: source-local B_s
Options:
A. B_s built from each source's own E_s and v_s, then summed.
B. B from total E and an effective velocity field.
C. derive from potentials directly, avoiding premature source-local assumption.

Preferred:
C for certification; A remains structural intuition until checked.

### Decision 5: P_BR convention
Options:
A. P_BR^i = epsilon^i_jk E^j_l B^kl.
B. P_BR^i = -epsilon^i_jk E^j_l B^kl.
C. factor variant from Bel-Robinson normalization.

Preferred:
keep schematic until Wylleman/Bel-Robinson convention map is locked.

## Required Lock Order
Before any sign-map calculation:

1. Lock metric signature and potential sign.
2. Lock E_ij sign convention.
3. Lock g_0i / A_i convention.
4. Derive or import B_ij.
5. Verify B_ij symmetry and trace-free character.
6. Lock kappa/sign/c-factors.
7. Lock P_BR sign/factor convention.
8. Only then evaluate P_normal sign patterns.

## Current Ruling
The branch is not ready for sign maps.

The correct next step is a convention-lock derivation attempt or explicit formula map, using this table as the checklist.

## Allowed Future Work
Allowed after GPT-wing adjudication:
- hand derivation of B_ij with the table as checklist,
- literature formula comparison row-by-row,
- provisional convention-lock recommendation.

Not allowed:
- lobe sign claims,
- sample-point sign claims,
- surface integration,
- ordinary-energy comparison,
- radiative flux interpretation,
- conservation claim,
- prediction claim,
- repo execution.

## Next Gate
OBS_041:
C5-B2 convention-lock derivation attempt.

Purpose:
Use the OBS_040 table to attempt a sign/factor/c-factor lock for B_ij, or explicitly classify which convention remains unresolved.
