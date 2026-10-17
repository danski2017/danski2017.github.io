---
layout: default
title: Resources
permalink: /resources/
---

## Computational Toolkits & Libraries
* [The Einstein Toolkit](https://einsteintoolkit.org/) – An open-source community framework for numerical relativity and multi-physics simulations in astrophysics.
* [Living Reviews in Computational Astrophysics](https://link.springer.com/journal/41115) – Peer-reviewed, technical deep dives into N-body and relativistic simulation algorithms.

## Community & Literature
* [Hyperspace@Uni-Frankfurt](https://hyperspace.uni-frankfurt.de/grg-links/) – A comprehensive directory of General Relativity and Gravitation (GRG) resources and academic links.
* [arXiv: gr-qc](https://arxiv.org/list/gr-qc/recent) – Recent submissions in General Relativity and Quantum Cosmology for staying current with daily research.

## Theoretical Foundations & Backreaction
* [On Average Properties of Inhomogeneous Fluids in General Relativity](https://arxiv.org/abs/gr-qc/9906059) – *Thomas Buchert (1999)*. The foundational paper deriving the scalar averaging equations (Buchert Equations) and establishing the framework for how inhomogeneities affect global evolution.
* [Backreaction in Late-Time Cosmology](https://arxiv.org/abs/1112.5335) – *Thomas Buchert and Syksy Räsänen (2012)*. A definitive review of the "Averaging Problem" and its impact on cosmic expansion.

## Observational Data & Rotation Curves
* [SPARC Database](https://astroweb.case.edu/SPARC/) – Spitzer Photometry and Accurate Rotation Curves for 175 galaxies; a high-precision benchmark for testing gravitational potential models.
* [Sloan Digital Sky Survey (SDSS)](https://skyserver.sdss.org/dr18/SearchTools/) – A comprehensive 3D map of the universe for large-scale structure analysis.
* [Gaia ESA Archive](https://archives.esac.esa.int/gaia) – High-precision astrometric data for mapping the Milky Way's gravitational structure and light bending.
* [NASA HEASARC](https://heasarc.gsfc.nasa.gov/) – The primary archive for high-energy missions and relativistic source data (X-ray/Gamma-ray).

## Research Societies & Specialized Institutes
* [International Society on GRG (ISGRG)](http://www.isgrg.org/) – The primary global learned society for promoting research in gravitation and general relativity.
* [Institute of Cosmology and Gravitation (ICG)](https://www.port.ac.uk/research/institute-of-cosmology-and-gravitation) – An international center of excellence focusing on testing gravity and large-scale structure.
* [Gravity Research Foundation (GRF)](https://www.gravityresearchfoundation.org/) – A historic organization promoting new ideas in gravitation through its famous annual essay competition.
* [Max Planck Institute for Gravitational Physics](https://www.aei.mpg.de/) – The Albert Einstein Institute; a premier global center for fundamental research in gravitation.

## Technical Discussion & Forums
* [Physics Forums (Relativity)](https://www.physicsforums.com/forums/special-and-general-relativity.70/) – A leading technical community for discussing complex problems in special and general relativity.

## Simulation Projects & Numerical Data
* [SXS (Simulating eXtreme Spacetimes)](https://www.black-holes.org/) – The premier source for high-precision numerical relativity simulations, particularly for binary black hole mergers.
* [SXS Visualization Gallery](https://www.black-holes.org/gallery/visualizations) – High-quality movies and images of merging black holes and exotic spacetimes.
* [Spectral Einstein Code (SpEC) Documentation](https://www.black-holes.org/code/SpEC.html) – Technical information on the core code used for landmark relativistic simulations.
* [SpECTRE Gallery (GitHub)](https://github.com/sxs-collaboration/spectre) – Next-generation code previews for handling complex fluid dynamics and extreme mass ratios.

## Gravitational Wave Multimedia Archives
* [LIGO Lab Image Gallery](https://www.ligo.caltech.edu/gallery) – The official archive for scientific charts, simulation stills, and gravitational wave event posters.
* [LIGO Video Gallery](https://www.ligo.caltech.edu/video) – Featuring educational journeys and simulations of warped space-time around colliding black holes.
* [LIGO Northwestern Multimedia](https://ciera.northwestern.edu/gallery/) – Organized collections focusing on binary neutron star mergers and "death spirals."
* [Virgo Collaboration Gallery](https://www.virgo-gw.eu/gallery/) – The European counterpart resource for localized sky maps and detector-specific visualizations.

## Geometric Methods & Spatial Partitioning
* [Voronoi Diagram](https://mathworld.wolfram.com/VoronoiDiagram.html) – *Wolfram MathWorld.* The classical framework for partitioning space into regions of nearest-source dominance — the conceptual precursor to Atlas parity surfaces. The key distinction: Voronoi cells are bounded by equal Euclidean distance; GCS jurisdiction cells are bounded by equal gravitational potential, which curves boundaries toward lighter sources and expands them around heavier ones.
* [Power Diagram](https://en.wikipedia.org/wiki/Power_diagram) – *Wikipedia.* The weighted generalization of the Voronoi diagram, and the closest classical analog to the Atlas parity surface framework. By assigning a scalar weight to each seed (analogous to source mass), Power diagram boundaries curve in ways that qualitatively mirror GCS jurisdiction boundaries — though the Atlas framework operates in three dimensions with potential fields governed by the inverse-square law rather than algebraic weights.
* [Apollonius Circles & Spheres](https://mathworld.wolfram.com/ApolloniusCircle.html) – *Wolfram MathWorld.* The locus of points whose distances to two fixed points are in a constant ratio. For two gravitational sources of masses m₁ and m₂, the parity surface is exactly the Apollonius sphere defined by r₁/r₂ = m₁/m₂ — making this the precise classical geometric description of a two-body GCS boundary.
* [Multiplicatively Weighted Voronoi Diagram](https://en.wikipedia.org/wiki/Weighted_Voronoi_diagram) – *Wikipedia.* A variant of the Voronoi diagram where each seed carries a scalar weight and regions are defined by minimizing the ratio of distance to weight. When weights correspond to source masses, this produces jurisdiction-like cells whose boundaries follow the same mass-ratio geometry as GCS parity surfaces — a direct algebraic parallel to the potential-equality condition.
* [Level Set Methods](https://en.wikipedia.org/wiki/Level-set_method) – *Wikipedia.* Numerical techniques for representing and evolving surfaces implicitly as the zero contour of a higher-dimensional scalar function. Parity surfaces are naturally expressed as the zero set of Φ₁(r) − Φ₂(r); level set methods provide the computational machinery to track, deform, and analyze them as source configurations change.

## Topology of Field Structure
* [Morse Theory](https://en.wikipedia.org/wiki/Morse_theory) – *Wikipedia.* A branch of differential topology studying how the connectivity and shape of level sets change as a function's value passes through critical points. In the Atlas framework, parity surfaces are level sets whose topology changes when source configurations pass through Morse-critical configurations — the precise mathematical language for how jurisdiction cells merge, split, or invert.
* [Persistent Homology & Topological Data Analysis](https://en.wikipedia.org/wiki/Persistent_homology) – *Wikipedia.* A framework for measuring topological features — connected components, loops, enclosed voids — across a continuous range of scales, and identifying which features are structurally robust versus transient. Directly relevant to the nested scene structure of the GCS framework, where topological significance must be evaluated across multiple tiers of source resolution.
* [Basin of Attraction](https://en.wikipedia.org/wiki/Attractor) – *Wikipedia.* In dynamical systems theory, the basin of attraction of an attractor is the set of initial conditions whose trajectories converge to it under the governing flow. Under gradient flow of the gravitational potential, each source is an attractor and its jurisdiction cell is precisely its basin of attraction — a dynamical systems interpretation of the GCS partition that connects jurisdiction geometry to classical stability analysis.

## Mathematical Foundations
* [Classical Potential Theory](https://en.wikipedia.org/wiki/Potential_theory) – *Wikipedia.* The mathematical study of harmonic and superharmonic functions, including the Newtonian gravitational potential, Green's functions, and solutions to the Poisson equation (∇²Φ = 4πGρ). The entire Atlas framework rests on the structure of superposed Newtonian potentials; potential theory provides the rigorous analytic foundation for their behavior, boundary conditions, and decomposition.
* [Multipole Expansion](https://en.wikipedia.org/wiki/Multipole_expansion) – *Wikipedia.* A systematic decomposition of a gravitational potential into contributions at increasing angular resolution: monopole (total mass), dipole (mass offset), quadrupole (mass distribution shape), and higher moments. As the declared resolution of a GCS scene coarsens, internal source structure is progressively folded into higher multipole terms — the formal mathematical description of how geometric detail is lost when crossing scale boundaries.

## Initial Data, Parameter Spaces & Curvature Response
* [Interaction Energy in Geometrostatics](https://inspirehep.net/literature/45090) – *D. R. Brill and R. W. Lindquist, Phys. Rev. 131, 471 (1963).* The founding paper on time-symmetric multi-black-hole initial data. It defines a bare mass for each Einstein–Rosen bridge and shows that the total mass falls short of their sum by a negative interaction energy. Atlas Scene Studio uses this construction as its exact static lane.
* [On Superposition of Relativistic Point Sources](https://arxiv.org/pdf/2002.12281) – A modern treatment of Brill–Lindquist-type superposition, including the bare mass and the effective (total) mass of each source.
* [Improved Initial Data for Black Hole Collisions](https://arxiv.org/pdf/gr-qc/9708022) – Work in the initial-data tradition that treats families of solved slices, varied in a parameter, as objects of study. It is a precedent for the parameterised slice sequences used in Atlas.
* [Parameter Space Metric for 3.5PN Compact-Binary Inspirals](https://ar5iv.arxiv.org/html/1305.5381) – An example of the gravitational-wave template-bank metric, which builds a metric on source-parameter space from derivatives of the signal (the Fisher information matrix). It is structurally analogous to the source-space metric explored in Atlas delta-webbing work.
* [Template-Space Metric for Searches for Gravitational Waves](https://ar5iv.arxiv.org/html/1501.04418) – A careful treatment of parameter-space metrics, including projection of extrinsic parameters, a technique relevant to making response metrics independent of registration choices.
* [A Linear Response Relation in General Relativity](https://arxiv.org/pdf/2507.19922) – Curvature perturbations treated as a linear response to source perturbations, a kernel viewpoint on how a geometry responds when a source is varied.
* [Properties of Quasi-Local Mass in Binary Black Hole Mergers](https://arxiv.org/pdf/2308.10906) – Applies the Wang–Yau quasi-local mass to Brill–Lindquist head-on data. A useful contrast to attribution by registered response: it assigns mass by enclosing surface.

## Superspace & Curvature Energy
* [What Is the Geometry of Superspace?](https://arxiv.org/pdf/gr-qc/9311017) – On DeWitt's metric on the space of three-geometries, including why the pure conformal (scale) direction is its negative direction.
* [Overview of the Geometries of Shape Spaces and Diffeomorphism Groups](https://arxiv.org/pdf/1305.1150) – A mathematical survey that includes the Ebin (DeWitt-type) L² metric on the space of Riemannian metrics.
* [Dynamical Laws of Superenergy in General Relativity](https://arxiv.org/pdf/0707.1475) – The Bel–Robinson superenergy, built from the electric and magnetic Weyl tensors, and its conservation laws. A possible route toward the dynamical handoff problem.
* [On the Energy Content of Electromagnetic and Gravitational Plane Waves Through Super-Energy Tensors](https://arxiv.org/pdf/1809.05305) – Superenergy density expressed through E·E + B·B, the same quadratic structure as tidal-budget integrals.

## Visualizing the Weyl Tensor
* [Frame-Dragging Vortexes and Tidal Tendexes Attached to Colliding Black Holes](https://arxiv.org/pdf/1012.4869) – *Owen et al. (2011).* Visualises the electric (tidal) and magnetic (frame-drag) parts of the Weyl tensor through eigenvector field lines. The closest professional relative of the Atlas tensor-witness renders.
* [Visualizing Spacetime Curvature via Frame-Drag Vortexes and Tidal Tendexes](https://ar5iv.arxiv.org/html/1208.3038) – The general theory paper of the tendex/vortex programme.

## Spectral Methods for Collective Structure
* [Spectral Clustering](https://en.wikipedia.org/wiki/Spectral_clustering) – *Wikipedia.* Grouping elements using the eigenvectors of a similarity matrix. Relevant to reading collective source groups from the eigenmodes of a source-space response metric.
* [Spectral Analysis of the Gram Matrix of Mixture Models](https://arxiv.org/pdf/1510.03463) – Theory of how Gram-matrix spectra reveal class structure, a statistical foundation for eigenmode-based group detection.
