name: RL_PUBLICATION_PROTOCOL
version: 1.1
status: candidate canonical
owner: Relational Labs
last_updated: 2026-07-22
tags: [publication, vault, public-clone, governance, reproducibility]

Relational Labs Publication Protocol

Purpose

Define the controlled boundary between the private working laboratory and the public Relational Labs clone.

This protocol governs publication.

It does not govern scientific truth.

A result may be scientifically valid and remain unpublished.

A document may be publicly useful without representing the highest claim rung.

Publication changes visibility, not evidentiary status.

⸻

1. Public Architecture

The public Relational Labs environment currently consists of three primary surfaces:

Lab

The public entry point and orientation surface.

Vault

The published documentary record, including selected:

* findings
* receipts
* adjudications
* doctrine
* goals
* evolution records
* parking-lot items

Atlas Instrument

The public interactive and computational artifact surface, including selected:

* viewers
* scene payloads
* datasets
* frozen experimental outputs
* supporting code

The public clone is a snapshot of selected lab state, not an assumed live mirror.

⸻

2. Publication Boundary

Material crosses from private lab state into public state only through an intentional publication action.

No automatic assumption should be made that:

* everything local should become public
* everything in the vault is already public
* everything public is current
* public visibility implies scientific promotion

Publication and adjudication remain separate processes.

⸻

3. Eligibility

Material may be considered for publication when it has a clear public purpose.

Typical eligible material includes:

* accepted or clearly labeled research findings
* adjudications
* methodological documentation
* reproducibility artifacts
* public datasets
* frozen instrument payloads
* explanatory diagrams
* lab history
* explicitly bounded speculative material
* parking-lot concepts appropriate for public visibility

Material should retain its actual claim status.

Do not strip uncertainty labels merely to make public presentation cleaner.

⸻

4. Pre-Publication Scan

Before publication, perform a deliberate scan for:

* secrets
* API keys
* passwords
* credentials
* tokens
* private keys
* personal identifying information
* private contact information
* machine-specific sensitive paths
* unpublished third-party confidential material
* legally restricted content
* accidental internal-only commentary

False positives may be inspected and cleared.

True positives must be removed or the affected material withheld.

The scan is a permanent part of the publication path.

⸻

5. Scientific Boundary Check

Before publication, verify that the artifact communicates its epistemic status correctly.

Check for:

* claim-rung labels
* candidate versus established distinctions
* unresolved falsification conditions
* known limitations
* deprecated metrics
* superseded terminology
* legacy results that require qualification

Publication must not silently promote a claim.

The public record should preserve the laboratory’s actual uncertainty structure.

⸻

6. Reproducibility Check

For computational artifacts, preserve enough information to understand what was published.

Where practical, include or retain:

* source scene or roster
* method
* relevant parameters
* resolution
* scalarization choice
* ablation target
* artifact provenance
* script or code reference
* output identifier
* adjudication or receipt reference

Frozen public payloads should be treated as reproducibility anchors.

⸻

7. Public Snapshot Principle

Every publication should be understood as a dated snapshot.

The private laboratory may continue evolving immediately after publication.

Therefore:

* do not assume public equals latest
* do not overwrite historical meaning without reason
* preserve version or receipt information when useful
* explicitly identify major supersessions

The public clone should remain legible as a research history, not merely as a constantly rewritten present.

⸻

8. Sync Policy

The Mac vault at `~/Desktop/Atlas_Solver_Project/Relational_Labs/Relational_Labs/` is the authoritative source of truth for vault content.

The GitHub `lab-vault/` tree is a one-way public mirror. It is never a source for changes to the Mac vault. A requested sync must update that mirror to match the publication-eligible Mac vault, including propagation of local deletions. GitHub-only edits inside `lab-vault/` will be replaced at the next sync.

Sync remains manual and intentional, not unattended or continuous. The standard routine is [[../Atlas Platform/10 Vault GitHub Mirror Sync|Vault GitHub Mirror Sync]]. It fetches and fast-forwards the separate website checkout, scans the Mac source, previews the scoped delta, copies only into `lab-vault/`, verifies byte identity, then commits and pushes the mirror. It never copies in the reverse direction.

The website shell and `atlas-instrument/` are outside vault-sync scope and require their own publication actions. Local operational metadata such as `.DS_Store` and `.claude/settings.local.json` is not publication-eligible vault content.

Future automation may assist with:

* diff generation
* eligibility checks
* secret scanning
* broken-link checks
* payload validation
* build verification

Automation must implement the publication protocol, not replace it. A sync is not considered complete until the pushed Git commit is verified on the remote.

⸻

9. Publication Sequence

Preferred sequence:

1. Identify publication candidate.
2. Confirm source version.
3. Confirm claim status.
4. Run privacy and secret scan.
5. Check public-facing formatting hazards.
6. Verify artifact provenance.
7. Stage public copy.
8. Review diff.
9. Publish through version-controlled change.
10. Verify build.
11. Verify live surfaces.
12. File publication receipt.

For substantial releases, prefer a pull-request or similarly auditable change path.

⸻

10. Verification

After publication, verify the relevant public surfaces.

Depending on the release, this may include:

* lab landing page
* vault navigation
* specific document pages
* Atlas viewer
* payload fetches
* WebGL functionality
* static asset loading
* internal links

A successful repository merge alone does not prove a successful public release.

⸻

11. Rollback

Every substantial publication should have a clear rollback path.

Preferred rollback characteristics:

* version-controlled
* reversible with a single defined action where practical
* documented in the publication receipt

If a serious privacy or security issue is discovered after publication, rollback takes priority over preserving public continuity.

⸻

12. Publication Receipts

Significant publication actions should leave a receipt.

A publication receipt should record, when applicable:

* date
* source state
* destination
* major files or surfaces published
* scan result
* build result
* live verification result
* rollback path
* known exceptions
* follow-up actions

The receipt is part of the lab’s institutional memory.

⸻

13. Vault Rule

Because portions of the vault may be republished:

Vault does not mean private.
Vault means potentially publishable.

Writers should therefore distinguish between:

* vault-safe material
* explicitly private working notes
* sensitive operational records

Material requiring durable privacy should not rely solely on obscurity inside the vault.

⸻

14. Public Instrument Rule

The Atlas Instrument is not merely a display artifact.

Published instrument assets may serve as reproducible research inputs for future work.

Therefore public instrument releases should favor:

* stable payload paths
* understandable naming
* preserved provenance
* reproducible frozen baselines
* minimal unnecessary breakage between releases

Where practical, a future manifest should enumerate canonical public models, scenes, scripts, and baselines.

⸻

15. Separation of Powers

Publication does not adjudicate science.

Adjudication does not automatically authorize publication.

The lab should preserve these distinct questions:

Is this claim supported?

Is this artifact useful to publish?

Is this artifact safe to publish?

Is this the correct version to publish?

All four may have different answers.

⸻

16. Future Automation

A future publication tool may automate routine checks, but should preserve human-visible decisions.

Potential automation targets include:

* public/private diff
* secret scan
* PII scan
* broken-link scan
* oversized-file check
* Jekyll/Liquid hazard scan
* build-status verification
* public URL verification
* publication-receipt generation

No automation should silently publish material solely because it exists in the vault.

⸻

17. Governing Principle

The public clone should make Relational Labs more inspectable without making the laboratory less disciplined.

Publication should increase:

* transparency
* reproducibility
* traceability
* accessibility
* scientific legibility

without collapsing the boundary between:

* working thought
* evidence
* adjudication
* doctrine
* public record

The publication bridge is therefore part of the laboratory architecture.

It should remain deliberate, auditable, and reversible.
