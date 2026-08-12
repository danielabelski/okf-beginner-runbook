---
type: Guide
title: Getting Started
description: Basic instructions for using and maintaining this OKF knowledge base.
tags: [guide, maintenance]
generated:
  by: human:alex
  at: 2026-08-10T00:00:00Z
---

# Getting Started

Use `index.md` files to navigate the knowledge base. Add one concept per Markdown file. Update `log.md` after meaningful changes.

If this knowledge base is shared, operational, or maintained by AI agents, read `AGENTS.md` before editing. It defines governance rules, placement rules, privacy boundaries, and approval rules.

## How To Add A New Concept

1. Copy `_templates/concept-template.md.tmpl`.
2. Rename it with a lowercase, hyphenated file name.
3. Keep the YAML frontmatter at the top.
4. Set a useful non-empty `type`.
5. Optionally add `generated`, `sources`, `verified`, `status`, or `stale_after` when provenance, trust, or freshness tracking is useful.
6. Add links to related files.
7. Update the nearest `index.md` if the file is important.
8. Add a short entry to `log.md` for meaningful changes.
