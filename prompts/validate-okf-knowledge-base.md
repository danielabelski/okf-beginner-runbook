# Prompt: Validate An OKF Knowledge Base

```text
Validate this Open Knowledge Format knowledge base. Inspect only the folder I approve. Check that every non-reserved .md file has YAML frontmatter, that every non-reserved .md file has a non-empty root-level type field, that normal index.md files are discovery files, that log.md files are chronological history files, that AGENTS.md is used only as an optional governance file when present, that links are portable, that broken links are reported, that intentional missing targets are marked as planned, and that no private or sensitive folders were included by accident. If the root index.md declares okf_version, check that it is a recognized version. If generated is present, check that it has by and at sub-fields. If status is present, check that it is draft, stable, or deprecated. If verified is present, note whether a human reviewer is listed (advisory). Do not modify files unless I ask you to.
```
