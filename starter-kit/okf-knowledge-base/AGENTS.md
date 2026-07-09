# AGENTS.md - OKF Knowledge Base Governance

This file defines how agents should work inside this OKF knowledge base.

## Purpose

Use this knowledge base for durable notes, references, project knowledge, playbooks, prompts, and troubleshooting material.

This is not a scratchpad or a place for raw dumps.

## Before Writing

Before adding or changing files:

1. Read this `AGENTS.md`.
2. Read the root `index.md`.
3. Read the nearest folder `index.md`.
4. Check whether the information already exists.
5. Prefer updating an existing note over creating duplicates.
6. If placement is unclear, ask the human before reorganizing.

## Folder Rules

- `domains/` = broad knowledge areas.
- `playbooks/` = repeatable procedures.
- `references/` = reusable reference material.
- `projects/` = project notes and project knowledge.
- `prompts/` = AI prompts and agent instructions.
- `_templates/` = inert templates only.

Do not create new top-level folders unless the human approves.

## OKF Rules

- Use one Markdown file per concept, decision, procedure, reference, or project note.
- Use clear lowercase kebab-case filenames.
- Add YAML frontmatter with a non-empty `type` to non-reserved Markdown files.
- Use `index.md` for folder discovery.
- Use `log.md` for chronological change history.
- Prefer links between notes over copying the same information into multiple places.

## Privacy Rules

Do not copy secrets, credentials, private messages, account exports, customer data, or sensitive personal information into this knowledge base unless the human explicitly approves that exact action.

## Maintenance Rules

When making meaningful changes:

- update the nearest useful `index.md`
- add a short `log.md` entry
- validate the knowledge base when practical

When unsure, ask before making broad edits.
