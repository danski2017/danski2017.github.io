---
type: ruling
status: adjudicated_with_revisions
created: 2026-05-15
topics:
  - hyperfoam
  - moving-binary
  - connection-witness
  - parity-node
  - gpt-wing
---

# HF-Gamma-001 GPT Wing Ruling

Canonical ruling:

- `codex_context/proposals/HF_Gamma_001_GPT_Wing_Ruling.md`

## Decision

HF-Gamma-001 is approved as a promising hypothesis lane, but not approved for execution exactly as written.

Proceed only after revision to `HF-Gamma-001 v0_2`.

## Core Correction

The scene should first earn the analytic parity-zero worldline object. It should not begin by claiming node drift as a connection witness.

Correct first object:

> analytic parity-zero worldline certification

Deferred object:

> connection witness

## Required Fixes

1. Correct Apollonius/on-axis node geometry.
2. Generate Keplerian source separation from `r(t)`, with periastron distance `a(1-e)`.
3. Keep barycenter fixed at origin for isolated binary.
4. Do not compare node velocity directly to `Gamma^i_00`.
5. Use implicit zero-set velocity as the primary v0_2 diagnostic.

## Gate Answers

- Analytic node formula is sufficient for identity certification only after correction and with provenance.
- Raw `Gamma^i_00` is not the primary drift comparator.
- No connection-alignment claim should be allowed in v0_1.
- C5-B2 / `E x B` companion should wait until the zero-set identity object is certified.

## One-Line Ruling

HF-Gamma-001 is a strong proposed lane, but v0_1 should be revised from "node drift as connection witness" to "analytic parity-zero worldline certification"; only after that object is earned should connection or curvature-update comparison be attempted.
