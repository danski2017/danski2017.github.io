---
type: simulation_template
status: active
created: 2026-05-13
owner: codex
---

# Simulation Run Template

## Header

```python
#!/usr/bin/env python3
"""<RUN_ID> <short title>.

Purpose:
  <one or two lines>

Summary-only output unless explicitly justified.

Claim boundary:
  internal <kind> probe only; no public claim; no GR/SR challenge.
"""
```

## Standard Constants

```python
from atlas_simlib import DEFAULT_HARD_CAP_BYTES, experiment_paths, fresh_experiment

REPO_ROOT = Path(__file__).resolve().parents[2]
PATHS = experiment_paths(REPO_ROOT, "<RUN_ID_slug>")
SCENE_ID = "<RUN_ID_UPPER>"
HARD_CAP_BYTES = DEFAULT_HARD_CAP_BYTES
```

## Atlas Declaration Block

Every generated config or scene passport should declare:

```json
{
  "node_declaration": {
    "node_minus_1": "summary ledger",
    "node_0": "declared registration datum",
    "node_1": "declared parent/context boundary",
    "node_2_plus": "declared physical source roster",
    "node_psi": "not emitted | emitted diagnostic registry",
    "node_p": "not claimed | candidate",
    "node_a": "not claimed | earned candidate"
  },
  "gfro_emitter": {
    "relation_map": "declared source/context residual map",
    "field_sieve": "declared coordinate-emission rule",
    "emitted_ledger": "Node -1 summary ledger | full emitted diagnostic registry",
    "retention_status": "unranked | witness-ranked | retention-certified"
  },
  "source_datum_rule": "Sources contribute. Datums interrogate. Witnesses report.",
  "claim_ladder_status": "internal | benchmark | sensitivity-hardened | canonical candidate",
  "non_claims": []
}
```

## Standard Functions

Every script should include or import:

- `fresh_experiment`
- `enforce_cap`
- `write_csv`
- `write_json`
- `write_text`
- `write_manifest`
- `fit_asymptote`
- deterministic source builder
- deterministic witness builder
- branch/method builder
- evaluator
- summarizer
- report writer
- manifest writer

## GFRO Emitter Flow

```text
declare source/context relation map
evaluate residual/operator map
emit candidate coordinates or summary rows through declared field-sieve rule
write emitted registry to Node -1 ledger package
rank with witnesses / retention checks
interpret only after claim ladder check
```

## Standard Main Flow

```text
if EXP exists:
  remove old package for fresh run
ensure dirs
write config
write scene passport
build rows
write derived table
write fits/summaries
write report
write interpretation note
write run summary
write manifest with sha256
enforce cap
print completion JSON
```

## Post-Run Obsidian Flow

After successful run:

- create/update experiment note
- update Live Experiment Dashboard
- update Next Simulation Queue
- update Lab Goals if milestone-relevant
