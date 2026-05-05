---
layout: default
title: Research Program
---

<style>
.research-grid {
  display: flex;
  gap: 60px;
  align-items: flex-start;
  line-height: 1.7;
}
.research-main {
  flex: 1;
  min-width: 0;
}
.research-sidebar {
  flex: 1;
  min-width: 0;
  border-left: 1px solid #eee;
  padding-left: 40px;
}
.research-explainer {
  max-width: 860px;
  line-height: 1.8;
}
.research-explainer .table-scroll {
  overflow-x: auto;
  -webkit-overflow-scrolling: touch;
}
@media (max-width: 780px) {
  .research-grid {
    flex-direction: column;
    gap: 0;
  }
  .research-sidebar {
    border-left: none;
    padding-left: 0;
    border-top: 1px solid #eee;
    padding-top: 40px;
    margin-top: 40px;
  }
  .research-explainer table {
    font-size: 0.82em;
  }
  .research-explainer table th,
  .research-explainer table td {
    padding: 0.45rem 0.55rem;
  }
}
</style>

<div class="research-grid" markdown="1">

<div class="research-main" markdown="1">

# Research Program

## Overview
The Atlas Research Program is an independent research effort focused on geometric methods in General Relativity, curvature structure in multi-body gravitational systems, and the development of numerical simulation tools that preserve geometric structure rather than relying on traditional point-mass approximations.

The program investigates how curvature behaves in relativistic n-body systems, where interacting sources generate structure that cannot be captured by simple superposition or two-body approximations. This includes the study of geodesic behavior, curvature coherence, and emergent geometric features in weak-field gravitational environments such as star systems, galaxies, and lensing configurations.

## Research Applications
* **Multi-Source Environments:** High-resolution evaluation of overlapping gravitational fields.
* **Structural Fidelity:** Consistent handling of extended systems within a unified geometric framework.
* **Trajectory Diagnostics:** Using geodesic deviations to map underlying mass-energy distributions.

<br>

<img
  src="/images/psUk3n_lsyb_tsP5YHe0IBhxS7m3MPA2nvQjuD6rhhcieaRHM66D9g8OyxsIDEQt6KM2iI_Du3UG_pKpRDMUuUnfjVbf62-G_jupxx8OYqfr0PEpb_-2FrdOnffqjs64pSQLs0QN1wlkIFsICP-HDTIWPSRgknESPSUo2St7cpg.jpeg"
  alt="Geodesic curvature structure in multi-body general relativity"
  style="max-width: 100%; height: auto;"
/>

</div>

<div class="research-sidebar" markdown="1">

# Active Research Papers

## Gravitational Coherence Surfaces as Information Boundaries of Source Attribution
*Parity, Entropy, and Stress-Energy Bookkeeping in Nested Gravitational Scenes*

[Read Paper](Atlas_GCS_Information_Boundaries_v0_3.pdf)

<br>

</div>

</div>

<hr style="border: 0; border-top: 1px solid #eee; margin: 60px 0 50px;">

<div class="research-explainer" markdown="1">

## What Is the GCS, and How Does It Relate to Classical Gravitational Boundaries?

A gravitational coherence surface (GCS) is a *parity horizon of gravitational identity*: the surface where a declared gravitational contribution reaches equality with its derived gravitational context.

To a reader familiar with celestial mechanics, the natural first question is: how is this different from a Hill sphere, a Roche lobe, or a sphere of influence? The short answer is that they answer different questions. The longer answer is worth unpacking — and Paper I works through it explicitly.

### The Classical Boundaries and What They Answer

The field already has well-tested tools for defining regions of gravitational influence:

- **The Hill sphere** (Hill, 1878) marks where satellite orbits can remain dynamically stable in the circular restricted three-body approximation. It answers: *where can a moon survive?*
- **The Roche lobe** marks the region of gravitational dominance in binary systems, relevant to mass transfer. It answers: *where is material gravitationally bound to which body?*
- **The Laplace sphere of influence** defines where patched-conic trajectory stitching should switch reference frames. It answers: *where should a spacecraft trajectory calculation change dominant body?*

These are genuine, useful, well-tested constructs. The GCS program cites them directly and does not claim to replace them.

### The Different Question

None of these tools ask the question the GCS asks:

> *Where does a declared gravitational contribution remain readable as itself within the context of the scene in which it is embedded?*

The shift is precise but significant. Hill spheres, Roche lobes, and spheres of influence were developed to solve specific problems — orbital stability, mass transfer, trajectory design. In each case, the geometry was a means to an end. GCS treats the parity geometry as the *subject*: a structure worth studying in its own right, across arbitrary source counts, scales, and readability rules.

Three elements must be declared to define a GCS: the scene (which sources are in play), the contribution (whose readability is being tested), and the readability rule (the comparison metric). The context is then *derived* from the rest of the scene — it is not assumed or freely chosen. This three-declaration structure makes every GCS a reproducible mathematical object rather than an intuitive approximation.

### The Quantitative Relationship to the Hill Sphere

For a source of mass *M* at distance *D* from a dominant neighbor of mass *M′*, the two scales are:

<div class="table-scroll">

| Boundary | Formula | Primary question |
|---|---|---|
| Hill radius | r_H = D (M / 3M′)^(1/3) | Where can satellite orbits remain stable? |
| GCS monopole radius | r_0 = D (M / M′)^(1/2) | Where does the declared contribution reach parity with derived context? |

</div>

The ratio between them is r_0 / r_H = 3^(1/3) (M / M′)^(1/6). The 1/6 exponent is the structural fact worth pausing on. Across four orders of magnitude in planetary mass ratio — from Mercury to Jupiter — this ratio varies by less than a factor of five, sitting at roughly 10–70% of the Hill radius. For Earth in the solar context, the simplified monopole GCS lies at approximately 17% of Earth's Hill radius.

The two surfaces are not competing. They coexist at different radii and answer different questions. Neither is a force cutoff.

### The Earth–Moon–Sun Lesson

The Earth–Moon system is the cleanest introductory example. The Moon is dynamically Earth-bound — this is not in dispute. But the Sun's absolute gravitational acceleration at the Moon exceeds Earth's. A simplified Earth-monopole parity estimate places Earth's monopole readability radius in the solar context at approximately 261,000 km, while the Moon orbits at approximately 384,000 km.

This is not a contradiction. It separates three things that gravitational intuition tends to conflate:

1. **Dynamical membership** — whether the Moon remains in Earth's orbital system
2. **Contribution-context parity** — where Earth's declared monopole reaches equality with the derived solar context
3. **Full nested-scene structure** — how the Earth–Moon system is read inside the larger solar scene

The GCS separates these layers with precision. Ordinary influence language tends to collapse them into one.

### Why Environmental Dependence Is a Feature, Not a Problem

A GCS is not a fixed property of a source. It is a property of a *source-in-a-scene*. Change the scene and the parity surface moves.

A 10⁶ solar-mass globular cluster has a monopole parity boundary of roughly 36 parsecs inside a dense galactic-disk context. In a sparse, void-like context, the same cluster's parity boundary expands to roughly 16 kiloparsecs — a factor of 442. Same mass, same source, different scene, different GCS.

This sensitivity is not a weakness. It is the observational lever. Catalog the same object in two different environments and the parity geometry reports two different surfaces. That makes the GCS an empirically estimable diagnostic rather than an intrinsic constant attached to a source.

### What This Unlocks

The single-source GCS is the entry point. In many-source scenes, pairwise comparisons between each source's contribution assemble into a **parity network** — a structured geometry of faces, seams, and junctions encoding the full relational topology of the gravitational scene.

The result is a lawful, renderable weak-field wireframe of the gravitational scene — not an artistic approximation, but a geometry derived directly from declared sources under honest accounting. That structure has not been produced by prior influence-boundary methods, because those methods were designed to answer specific dynamical questions, not to render the full relational geometry of a scene.

</div>
