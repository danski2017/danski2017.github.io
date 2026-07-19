---
type: experiment_note
status: completed
created: 2026-05-13
experiment_id: C002_curvature_identity_website_payload
topics:
  - curvature-identity
  - website-payload
  - public-tool
---

# C002 Curvature Identity Website Payload

## Status

Completed website-payload draft.

Package:

`codex_context/experiments/C002_curvature_identity_website_payload`

Script:

`codex_context/scripts/c002_curvature_identity_website_payload.py`

Source:

`C001_curvature_identity_atlas_prototype`

Package size:

`0.017 MiB`

## Payload

Primary payload:

`codex_context/experiments/C002_curvature_identity_website_payload/derived/curvature_identity_atlas_payload_v0_1.json`

Contents:

- 12 object cards,
- 12 budget chart rows,
- 3 jurisdiction examples,
- 12 compression examples,
- public intro copy,
- claim-ceiling copy,
- paper links,
- non-claim list.

## Use

This is ready to hand to the website build lane as:

- a static JSON data file,
- a JavaScript calculator seed,
- a chart source for the Curvature Identity Atlas page.

## Public Tool Copy

Tool name:

```text
Curvature Identity Atlas
```

Dek:

```text
Inspect what a finite source carries, where it matters, and when its detail fades.
```

Claim ceiling:

```text
Weak-field curvature bookkeeping inside declared source models; not a new field equation,
force, observable boundary, or solved dynamical handoff.
```

## Claim Boundary

C002 adds no new evidence beyond C001. It only repackages C001 for website use.

## Next Gate

Website implementation can now use the JSON payload directly. If the website lane asks for a smaller file, derive a minified copy from the same payload without changing values.

