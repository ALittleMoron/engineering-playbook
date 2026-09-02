# ADR 0001: Agent Profile Format

## Context

Reusable agent instructions need a small composition format that preserves fragment ownership, produces reviewable output, and does not duplicate instruction text in profile definitions.

## Decision

Store profiles as TOML files in `agents/profiles/`. A profile declares:

- `schema_version`, initially `1`;
- a filename-matching `name`;
- a release `version`;
- a concise `description`;
- one or more `use_cases`;
- an ordered, duplicate-free list of fragment paths relative to `agents/fragments/`.

Build each profile into `agents/dist/<name>/AGENTS.md`. The generated file contains profile metadata and a digest followed by the selected fragments in declared order, separated by one blank line. Fragment content is not otherwise transformed.

Profile names and paths must remain within their designated repository directories. Missing, empty, duplicated, or escaping fragment paths are invalid.

## Alternatives considered

- YAML would be familiar but would introduce a parser dependency.
- JSON would avoid dependencies but is less comfortable for hand-maintained ordered manifests.
- Markdown includes would be concise but are not a portable Codex instruction-loading mechanism.

## Consequences

- Profiles remain readable and dependency-free to parse on supported Python versions.
- Generated files are self-contained and may contain more than one top-level Markdown heading.
- Reordering fragments is an explicit behavioral change visible in the manifest and generated diff.
