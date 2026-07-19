---
type: work_order
status: proposed
created: 2026-05-15
topics:
  - gaia
  - parity-network
  - averaging-delta
  - discriminating-null
  - future-work
---

# G001P Gaia Parity-Delta Overlay Work Order

Completion note:

- Completed run: [[../Experiments/G001P Gaia Parity-Delta Overlay]]
- Decision: boundary-sensitive, not parity-specific under first-pass proxy.
- Grammar correction: Hill-style is contextual, not a grammar-matched null. See [[G001P2 Grammar-Matched Parity Null Audit Work Order]].

This note records the Claude wing cross-wing inquiry and the accepted Codex hardening response.

Canonical proposal:

- `codex_context/proposals/G001P_Gaia_Parity_Delta_Overlay_Work_Order.md`

## Scientific Question

Do the high-delta regions in the Gaia 25 pc averaging comparison correlate spatially with parity network structure?

Specifically, are high-delta witnesses near parity-network boundaries, handoff surfaces, or triple-junction candidates, or are they distributed without apparent relation to parity geometry?

## Hypothesis

If the GCS/parity-network prediction is correct, averaging sensitivity should be highest where active handoff structure exists: where child/source domains are collapsed into parent/coarse contexts prematurely by averaging.

Short form:

> high delta = boundary crossing being erased.

## Required Discriminating Nulls

G001P must compare high-delta witnesses against:

1. Atlas parity/handoff boundary proxy.
2. Hill-style gravitational boundary proxy.
3. Voronoi tessellation boundary proxy.
4. Shuffled or rotated null controls.

The discriminating question:

Does the correlation require Atlas parity geometry, or would Hill-style or Voronoi boundaries predict the same high-delta clustering?

## Required Output Columns

Each enrichment row should include:

- `delta_metric`
- `top_delta_percentile`
- `boundary_predictor`
- `distance_or_margin_metric`
- `high_delta_near_boundary_fraction`
- `all_witness_near_boundary_fraction`
- `enrichment_ratio`
- `null_enrichment_median`
- `null_enrichment_p95`
- `p_value_or_rank_fraction`
- `comparative_rank`
- `claim_status`

Also produce a wide comparison with:

- `delta_metric`
- `top_delta_percentile`
- `parity_enrichment`
- `hill_enrichment`
- `voronoi_enrichment`
- `best_predictor`
- `comparative_ranking`
- `claim_status`

## Outcome Ladder

| Outcome | Meaning | Claim Status |
|---|---|---|
| Parity outperforms Hill/Voronoi | parity-local averaging sensitivity is supported | strong internal support |
| Hill/Voronoi comparable | high deltas are boundary-sensitive, but not parity-specific yet | useful but bounded |
| No boundary enrichment | tensor/scalar split is real but not tied to tested boundary metrics here | negative result, still valuable |

## Recommended Opening Prompt

```text
Proceed with G001P Gaia Parity-Delta Overlay from the work order. Use corrected G001H/G001I as the base. Build per-witness high-delta ledgers and compare spatial enrichment near Atlas parity/handoff, Hill-style, and Voronoi boundary proxies. Include shuffled/rotated null controls, comparative ranking, visuals, certification boundary, and Obsidian notes. No new data downloads and no website writes.
```
