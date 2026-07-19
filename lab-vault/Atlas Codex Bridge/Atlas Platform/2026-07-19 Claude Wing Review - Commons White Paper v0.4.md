---
type: cross_wing_review
status: filed
created: 2026-07-19
audience: founder + GPT wing
tags: [atlas-platform, commons, white-paper, review, claude-wing]
---

# Claude-Wing Review — Relational Commons Internal White Paper v0.4

Independent verification by the wing that generated the evidence
packets, against the frozen packets and canonical scripts. Scope:
numerical fidelity, freeze-checklist execution, and document defects.
The physics narrative and claim ladder are GPT/founder territory and
are not re-adjudicated here.

## 1. Numerical verification — ALL CHECKED VALUES MATCH

Every quantitative statement in the paper was checked against the
packet of origin. Confirmed exactly: 36 minima / 9 disputed; 3/1000
enrichment (null median 4, max 10); H 0.683 vs 0.608; scrambled
ensemble median 14, range 10-20, backbone share median 0.896, range
0.50-1.00; families 12/7 (N=24), 27/9 (N=48), 36/9 (N=66), 0 (N=5),
detection by N=16; 96^3 8/9 with drift <= 0.016 vs dx ~ 0.24; H-grid
13/9/2; sigma 1.69; null median ~0.35, max ~0.70, 0/20 at both levels;
B(0.85)=0.867, B(0.88)=0.883; carrier Jaccard min 0.87-1.00 (median
1.00 all eight), Spearman >= 0.999, top-5 5/5 (one 4/5), |dH| <=
0.011, drift <= 0.096; idx-7 J=0, Spearman ~0.6, drift 333.8; named
residual ranges; primary trough ||E|| 4.4e-16, H 0.819, 13 carriers,
0.54 recovery offset; 19/19 webbing crawls connected; finger-trap
3 -> 36 with drift-to-final 1.17 -> 0; incident narrative (30 min /
98% CPU / 2.1 s rerun / ~140 MB). No numerical discrepancies found.

## 2. Freeze-checklist items executed (Appendix B)

- **rho_s code definition**: `RHO = ||Delta_s E||_F / (||E^(-s)||_F +
  1e-300)` — additive 1e-300 regularization IS present; report it.
- **Carrier test**: strictly `rho_s > 0.5` (not >=). Confirmed.
- **Psi_s stored convention — IMPORTANT**: the canonical scripts store
  `Psi = log10(rho_s)` (the house parity log-ratio, consistent with
  the foam lane since inception). The paper's Section 4 offers
  "Psi_s = rho_s - 1" as an equivalent-zero-set alternative; the
  Section 14 numerical residuals are **log10 ratios, NOT rho-1**
  (e.g. Psi = -0.065 means rho = 0.861; rho-1 would be -0.139).
  Section 4 should declare log10 as the stored convention before any
  public edition. The freeze note in Section 14 was warranted and is
  hereby answered.
- **Entropy**: p_s = S_s / sum S_k and H = raw/ln N confirmed —
  with N = ACTIVE roster size (62 in the drop-four-faintest variant,
  66 elsewhere). Cross-variant entropy comparisons therefore compare
  ln(62)- vs ln(66)-normalized values (a ~1.6% normalization shift);
  harmless at the reported |dH| <= 0.011 level but must be declared.
- **Gaussian-null sigma estimator**: lag-1 x-direction autocorrelation
  of the measured H field; sigma^2 = -1/(4 ln c1). Occupancy is
  independently matched at every level via each field's own quantile
  threshold. Confirmed in code.
- **Full 20-null distributions**: were NOT in the packet (median/max
  only). The sweep script now exports `null_shares_full` per level;
  deterministic rerun reproduced every headline number identically.
  H>=0.85 full set: 0.153 ... 0.649 (real 0.867 above all).
  Checklist item CLOSED.

## 3. Document defects for v0.5

1. **Section numbering**: two sections numbered 23 (Stabilized gate;
   Claim register) and two numbered 25 (Remaining promotion gates;
   Failure conditions); no 24. Renumber.
2. **Stale conclusion paragraph**: the Conclusion still says the next
   promotion "will depend on ... whether the trough population defeats
   an occurrence null, whether the structure survives genuinely
   different scene families" — both DELIVERED in Section 23 and the
   basis of this very edition's Stabilized claim. Replace with the
   remaining real gates (broader null families, broader scene classes,
   Lambda_Pi calibration).
3. **Section 9.4 stale sentence**: "That promotion requires broader
   independent scene-family testing and a dedicated trough-occurrence
   null" — correct that the INSTANCES stay Reproduced, but the cited
   missing evidence now exists; rephrase to point at Section 23's
   class-level result.
4. **Psi convention** (Section 4 vs 14): see checklist item above.

## 4. Adjudication bookkeeping

This edition embeds the rulings requested in the 2026-07-18 Stabilized
Gate Brief: S1 answered (class claim Stabilized within the tested BL
many-source family), S2 answered (instances remain Reproduced; class
sits above), S3 answered (scrambling scope footnoted as
radial-profile-preserving; broader ensembles named as remaining null
work), S4 answered (observed onset interval recorded; NOT canonized as
a threshold — controlling variable unresolved). The brief is
accordingly marked adjudicated-via-paper.

## Verdict

The paper is numerically faithful to the packets in every checked
value, and its claim registers match the adjudicated ledger. With the
four v0.5 defects fixed and the Psi/entropy-N declarations added, the
Claude wing has no objection to this edition standing as the canonical
internal record of the Commons program.

The field is seamless. The quiet between the sources has an anatomy —
and now it has an audited one.
