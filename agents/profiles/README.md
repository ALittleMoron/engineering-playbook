# Agent Profiles

Composition definitions for distributable profiles such as global, Python backend, or TypeScript frontend. A profile selects fragments and must not copy their content manually.

Profiles use TOML and contain the following fields:

- `schema_version`: manifest schema version, currently `1`;
- `name`: lowercase profile name matching the manifest filename;
- `version`: release version embedded in generated output;
- `description`: concise profile purpose;
- `use_cases`: non-empty list of supported uses;
- `fragments`: ordered, duplicate-free Markdown paths relative to `agents/fragments/`.

Build a named profile with `scripts/build-agents <name>` or build every profile with `scripts/build-agents`.
