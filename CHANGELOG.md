# Changelog

## v0.2.0 - 2026-08-16

SimSuite test revisions. Five issues found through persona-based simulation testing:

- Quick-start card: replaced undefined jargon (Markdown, frontmatter, domain) with plain-language definitions and added a minimal one-domain tree example before the full structure.
- Quick-start card: added safety boundaries section (no secrets in OKF files, file-level exclusion guidance, clean staging folder recommendation).
- Runbook Section 6A: added explicit prohibition on placing passwords, API keys, credentials, or account numbers in any OKF artifact.
- Runbook Section 6B: added file-level exclusion guidance with allowlist/denylist and clean staging folder procedure for mixed-sensitivity folders.
- Runbook Section 16: documented validator output (PASS/WARN/FAIL), exit codes, what the script checks, and what it does not check (broken link targets, index quality, log chronology, governance quality, file size, duplicates, privacy).

## v0.1.2 - 2026-08-08

- Added the short video `How to Build an AI Brain in Five Minutes` under `videos/` and linked it from the README.
- Excluded Windows `Zone.Identifier` metadata from Git tracking.

## v0.1.1 - 2026-07-08

- Added guidance for root `AGENTS.md` governance files in shared or agent-maintained OKF knowledge bases.
- Added `AGENTS.md` to the starter OKF knowledge base as an optional governance layer.
- Updated prompts and quick-start guidance to mention governance files where appropriate.
- Updated `validate-okf.py` so `AGENTS.md` is treated as governance, not an OKF concept note requiring frontmatter.

## v0.1.0 - 2026-07-01

- Added a one-page quick-start card under `runbook/`.
- Added optional Obsidian viewing guidance to the runbook and README.
- Synced inline runbook prompts with their standalone prompt files.
- Added `validate-okf.py`, a dependency-free Python validator.
- Added a Reference-type example file under `examples/`.
- Updated README and starter-kit log notes for this release.

## 2026-06-27

- Created first distributable OKF Beginner Runbook package.
- Added full runbook under `runbook/`.
- Added starter OKF knowledge base under `starter-kit/`.
- Added copy-paste agent prompts.
- Added examples for concept, index, and log patterns.
- Added MIT License.
- Added About, Contact, and Privacy pages.
