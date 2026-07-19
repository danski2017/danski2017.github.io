---
type: platform_change_receipt
status: sandbox_complete_repeat
created: 2026-07-18
tags: [atlas-platform, node0, geometric-delta, compactness, asymptotic-tail, receipt]
---

# 2026-07-18 Receipt — Node 0 Compactness-to-Tail Sweep

## Scope

Codex executed `RL_NODE0_DELTA_ACCOUNTING_003_COMPACTNESS`, the first controlled
compactness-to-tail correspondence sweep following experiments 001 and 002.
The packet contains two seven-rung spherical similarity families derived from
the unchanged ET-validated profile A:

- Family A: fixed transported matter radius, varying ADM mass.
- Family B: fixed ADM mass, varying transported matter radius.

The family transform preserves the parent conformal constraint grammar but is
not represented as a newly solved hydrostatic EOS/TOV family. No new solve,
time evolution, morphology change, rotation, two-source scene, viewer change,
or doctrine change occurred.

## Artifacts

- Packet: `analysis/node0_delta_accounting/RL_NODE0_DELTA_ACCOUNTING_003_COMPACTNESS/`
- Passport: packet `PASSPORT.txt`
- Return packet: packet `RETURN_PACKET.md`
- Gate assessment: packet `GATE_ASSESSMENT.json`
- Manifest: packet `MANIFEST.json`
- Config: `configs/node0_delta_accounting/RL_NODE0_DELTA_ACCOUNTING_003_COMPACTNESS.json`
- Runner: `scripts/node0_delta_accounting/run_node0_delta_accounting_003_compactness.py`
- Tests: `scripts/node0_delta_accounting/tests/test_node0_delta_accounting_003_compactness.py`

Recorded SHA-256 at closeout:

- Manifest: `b15543b85e9c082a01edf9e70d877765bb472ea8529a1910a70eac93c78a0b29`
- Return packet: `86c6fb0982797e88e9a72a483699d4f3854113cae67a632c521fdadb63d963f1`
- Runner: `8cef62862143aae5efd8684c273378c1f096ee5374a60bd799f1219b6b1a8485`
- Parent 001 manifest (unchanged): `2fef36e948651744148c17849908e2ab3412d1b4f3ee84f3106f07151e53b6ee`
- Parent 002 manifest (unchanged): `c0050f57dfed28ecaa1c5987398a6aa2b872a89883dcd12f9ff405fe03ad2639`

## Resource and execution boundary

The sequential fine grid was `61^3 = 226,981` nodes. The conservative peak
estimate was 519.5 MiB, 6.3% of the approved 8 GiB host. Each rung was serialized
before advancing. No matrix solve or evolution was launched.

## Measured result

- Eight of fourteen main rungs pass the predeclared support-interior Hamiltonian
  threshold of 5.467445%; four pass in each family. All failed rungs remain in
  the packet and are excluded from regressions.
- Gate A passes because at least five total rungs are numerically admitted.
  Gate C passes because the declared amplitudes/exponents are measured with
  uncertainties and fit quality.
- Representative cleanliness does not pass. The high-compactness fixed-mass
  rung has a mid-to-fine `B_W2` change of 7.032% against a 6% threshold and an
  independent integrated `B_W2` residual of 13.846% against a 10% threshold.
- Neither family has five admitted rungs, so the correlation matrix is retained
  but correctly marked insufficient for family-level inference.
- At `r=32`, Family B has only 0.251% relative spread in `r^3||E||/M`. No tested
  fixed-mass far-field difference exceeds the declared three-sigma resolution
  floor. This is a candidate information-drowning result for the declared
  spherical diagnostics.
- The largest-radius fixed-mass rung `B_C01` has 16.847% `A_E` spread across the
  four predeclared windows. Its canonical window begins only one length unit
  beyond the transported profile edge, allowing the angular interpolation
  stencil to reach the transition zone. The coefficient remains ledgered as a
  systematic caution and is not used to manufacture a retained-information
  signal.
- The raw cumulative Node 0 volume displacement remains a divergent diagnostic,
  not a finite global budget.

## Gate decision

- Gate A — at least five valid compactness rungs: **PASS**
- Gate B — representative numerical cleanliness: **FAIL**
- Gate C — tail amplitudes/exponents measured: **PASS**
- Gate D — claim-eligible reproducible compactness trend: **FAIL**
- Gate E — trend survives resolution/independent extraction: **FAIL**
- Gate F — five-rung mass-controlled interpretation: **FAIL**

Status remains **SANDBOX / Seed**. No universal source-to-tail map, exterior
information law, conservation statement, or curvature-conversion claim is made.

Required return recommendation: **REPEAT**.

## QA

Eight unit/packet tests passed. All 82 files listed in the final packet manifest
matched their SHA-256 records. Twenty required ledger-backed figures were
generated and visually inspected. Both parent packet manifest hashes remained
unchanged.
