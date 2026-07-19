# C5-B2 Magnetic Weyl Literature Convention Crosscheck

## Claim Status
Literature/convention cross-check scaffold / magnetic-Weyl formula provisional / no calculation certified.

This note is not certified evidence, not a completed derivation, not a repo calculation, not ordinary-energy accounting, not radiative balance, not conservation, and not a prediction.

Surface integration remains unauthorized.

The sign and numerical factor in the OBS_037 B_ij structural candidate remain uncertified.

## Purpose
Map the OBS_037 structural magnetic-Weyl candidate against literature/convention targets before any sign-map, lobe-pattern, or sample-point calculation.

The goal is to calibrate the magnetic-Weyl compass:
- kappa,
- sign,
- c-factors,
- B_ij definition,
- Levi-Civita convention,
- observer/tetrad compatibility.

## Source Links
- [[C5-B2 B_ij Structural Derivation Candidate v0.1]]
- [[C5-B2 Linearized Metric B_ij Derivation Passport]]
- [[C5-B2 Magnetic Weyl Formula Selection Gate]]
- [[C5-B2 Explicit Weak Field EB Tensor Model Passport]]
- [[C5-B2 F_mid Sign Pattern Estimate v0.1]]
- [[../Frontier Evidence Rule|Frontier Evidence Rule]]
- [[../../Best Practices/Claim Boundary Checklist|Claim Boundary Checklist]]

## Literature Targets

### Target 1: Costa and Herdeiro tidal-tensor gravitoelectromagnetic analogy
Use as the primary convention target for gravitational electric/magnetic tidal tensors.

Reason:
This literature directly frames gravitoelectric and gravitomagnetic tidal tensors and their analogy to electromagnetism.

Items to extract:
- definition of electric tidal tensor,
- definition of magnetic tidal tensor,
- sign convention,
- Levi-Civita convention if stated,
- relation to Riemann/Weyl components,
- weak-field or linearized limit,
- whether B_ij is symmetric / trace-free in the relevant vacuum setting.

Citation target:
Costa & Herdeiro, “A gravito-electromagnetic analogy based on tidal tensors.”

### Target 2: Bel-Robinson / super-Poynting literature
Use to check the super-Poynting vector definition and claim boundaries.

Items to extract:
- superenergy density convention,
- super-Poynting vector convention,
- relation to E_ij and B_ij,
- dimensional caveats,
- observer dependence,
- warning against ordinary-energy interpretation.

Citation target:
Wylleman et al., “Poynting vector, super-Poynting vector, and principal observers…”

### Target 3: linearized-gravity / PN gravitomagnetic source formula
Use to check the moving-point-mass B_ij formula.

Items to extract:
- weak-field metric convention,
- g_0i convention,
- vector potential convention,
- leading B_ij expression for slow-moving source,
- c-factors,
- sign relative to chosen E_ij.

## OBS_037 Structural Candidate
Candidate preserved from OBS_037:

B_ij^(s) = kappa/c * epsilon_{kl(i} v_s^k E_{j)}^{(s)l}

Expanded:

B_ij^(s)
=
kappa/(2c) [
  epsilon_{kli} v_s^k E_j^{(s)l}
  +
  epsilon_{klj} v_s^k E_i^{(s)l}
]

Status:
tensor shape provisional;
kappa/sign/factor uncertified.

## What Must Be Checked

1. Is the literature B_ij definition compatible with:
   B_ij = 1/2 epsilon_i^{kl} C_klj0
   or does it use a sign-flipped convention?

2. Does the literature expression support the velocity-rotated-E structure:
   B_ij ~ epsilon v E symmetrized?

3. What is the correct kappa under the chosen convention?

4. Are factors of c consistent with:
   B ~ (v/c) E?

5. Is the source-local construction correct:
   B_ij^(s) from each source's own E_ij^(s),
   then B_total = sum_s B_ij^(s)?

6. Does total E_total pair with total B_total in:
   P_BR^i ~ epsilon^i_jk E^j_l B^kl?

7. Is the sign of epsilon_ijk consistent with the OBS_032 orbital-handedness convention?

8. Does the super-Poynting convention use:
   P_i ~ epsilon_ijk E^j_l B^{kl}
   or a sign/factor variant?

## Preliminary Literature-Aware Boundary
Bel-Robinson / super-Poynting quantities are curvature-square / superenergy-like objects, not ordinary local gravitational energy.

Therefore:
even after convention calibration, C5-B2 remains a Weyl-superenergy directionality witness, not a gravitational-wave luminosity or Bondi mass-loss claim.

## Allowed Future Work
Allowed after GPT-wing adjudication:
- web-assisted or paper-assisted convention extraction,
- formula comparison table,
- provisional kappa/sign recommendation,
- decision whether OBS_037 candidate survives, needs sign flip, needs factor correction, or must be replaced.

Not allowed:
- sign-map calculation,
- lobe certification,
- surface integration,
- ordinary-energy comparison,
- radiative flux interpretation,
- conservation claim,
- prediction claim,
- repo execution.

## Output Classification Options

A. Candidate survives with kappa/sign/factor locked provisionally.
B. Candidate survives structurally but needs sign/factor patch.
C. Candidate is only a parity proxy and cannot support sign maps.
D. Candidate is wrong and must be replaced.
E. Literature remains ambiguous; derive from linearized metric before proceeding.

## Current Ruling
C5-B2 must perform literature/convention calibration before any explicit sign-map calculation.

The OBS_037 B_ij shape is promising but not certified.

## Next Gate
OBS_039:
C5-B2 literature-assisted convention extraction or formula comparison table.
