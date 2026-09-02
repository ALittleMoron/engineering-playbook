# ADR 0002: Agent Tooling Runtime

## Context

Profile generation and installation must work on a developer machine without adding a project environment or downloading packages. Installation also needs reliable path validation, diffs, backups, and atomic file replacement.

## Decision

Implement repository automation in Python 3.11 or newer using only the standard library. Executable entry points live in `scripts/` without a `.py` suffix; shared implementation code may use `.py` modules in the same directory.

The global installer must:

- use dry-run behavior unless `--apply` is present;
- show the target diff before any write;
- refuse missing or stale generated input;
- back up a changed existing target before replacement;
- replace the target atomically;
- support an explicit Codex home directory for isolated verification;
- otherwise honor `CODEX_HOME` and fall back to `~/.codex`.

## Alternatives considered

- POSIX shell would minimize runtime assumptions but makes structured TOML validation and portable atomic replacement harder.
- A third-party CLI framework would improve ergonomics but add dependency management before the repository needs it.

## Consequences

- Python 3.11 or newer is the only runtime prerequisite.
- The tools can run in CI and temporary test directories without network access.
- New dependencies require a later decision record and an explicit maintenance rationale.
