---
type: configs_schemas_map
status: active
created: 2026-05-13
topics:
  - configs
  - schemas
  - reproducibility
---

# Configs and Schemas Map

## Configs

Path: `configs`

Status: Active / Historical mixed.

Useful lanes:

- `configs/engine_v2`: engine v2 three-body and extreme-ratio configs
- `configs/nodal/canonical`: canonical nodal configs
- `configs/nodal/sweeps`: historical/source sweep configs
- `configs/nodal/weakfield_variants`: weak-field variant configs
- `configs/ems_*`: EMS parent/context configs

## Schemas

Path: `schemas`

Status: Active.

Files:

- `atlas_retention_candidate_feature_schema_v0_1.json`
- `node_schema.json`
- `probe_schema.json`
- `run_config_schema.json`

## Use Rule

Configs and schemas are reproduction contracts. Link them to runs before interpretation. If a config has no matching report, treat it as setup material rather than evidence.

