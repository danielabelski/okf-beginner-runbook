# Changelog

## v0.2.0 - 2026-08-10

- Updated the runbook, quick-start card, starter kit, examples, prompts, and validator to align with OKF spec v0.2.
- Replaced `timestamp` with `generated: { by, at }` as the recommended content-change field. `timestamp` is still accepted as a v0.1 fallback.
- Added optional v0.2 frontmatter fields: `sources`, `verified`, `status`, `stale_after`.
- Added a new runbook section: "Provenance, Trust, and Lifecycle (Optional v0.2 Fields)" with beginner-friendly explanations of `generated`, `verified`, `status`, `stale_after`, `sources`, the actor convention, the `references/` subdirectory convention, and `Attested Computation`.
- Added `Attested Computation` to the recommended concept types list.
- Updated the root `index.md` `okf_version` example from `"0.1"` to `"0.2"`.
- Updated the validation checklist and validator script to check v0.2 optional fields when present.
- Updated all sample files, templates, and prompts to use `generated` and mention v0.2 optional fields.
- Updated the starter kit root `index.md` to declare `okf_version: "0.2"`.
- Updated `AGENTS.md` to mention v0.2 optional fields.

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
