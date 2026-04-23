# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project context

This repository is part of the **Deep Gravity** project — the broader research effort being developed in Claude. Work done here (site updates, new pages, papers, figures) should be understood as the public-facing output of that project.

## What this site is

GitHub Pages site (https://danski2017.github.io) — the public research hub for the Atlas Solver project, a weak-field multi-source GR computational geometry platform. Built with Jekyll + Minima theme, deployed automatically on push to the default branch.

## Local development

No Gemfile is committed. To serve locally, install Jekyll and the required plugins:

```bash
gem install jekyll jekyll-seo-tag minima
bundle exec jekyll serve --livereload
# or without bundler:
jekyll serve --livereload
```

The site builds automatically on GitHub Pages; local preview is optional.

## Architecture

All content pages are Markdown files at the repo root with YAML front matter. Jekyll renders them through the Minima theme.

**Layouts:**
- `layout: default` — standard Minima page, no comments widget (used by most pages)
- `layout: page` — custom layout in `_layouts/page.html` that wraps content and appends a [Giscus](https://giscus.app) comments widget (linked to `danski2017/danski2017.github.io`, category "General")

**Navigation:** Controlled by `header_pages` in `_config.yml`. Pages listed there appear in the header nav. Two nav entries (`papers.md`, `hypotheses.md`) are referenced but not yet created.

**Styling:** `assets/main.scss` imports Minima then adds all custom styles. Key utility classes:
- `.home-grid` / `.home-card` — two-column card grid for the home page
- `.figures-page`, `.figures-showcase-primary`, `.figures-showcase-secondary`, `.figures-gallery` — multi-tier figures layout (primary banner → 3-col secondary → 5-col gallery)
- `.responsive-video` — 16:9 aspect-ratio wrapper for embedded iframes or `<video>` elements

**Media:** Images and videos live in `/images/`. PDFs are placed at the repo root and linked directly (e.g., `/Gravitational_Coherence_Surface.pdf`).

**Config quirk:** `author` and `email` in `_config.yml` are set to `" "` and `""` intentionally — this suppresses Minima's default behavior of repeating the site title in the footer.

## Content conventions

- All pages use `layout: default` unless Giscus comments are wanted, in which case use `layout: page`.
- Inline HTML is used on content-heavy pages (figures, home) where Markdown's layout primitives are insufficient — this is intentional, not a mistake.
- The `sitemap.xml` is manually maintained; update `<lastmod>` dates when pages change significantly.
- `figures.md` currently contains placeholder image paths (`path/to/sub1.png`, `https://via.placeholder.com/150`) that are not yet replaced with real assets.
