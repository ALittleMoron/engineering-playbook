# Scripts

Automation for building agent profiles, checking structure, validating links, running evals, and installing generated files. Scripts should be safe by default and support previewing changes.

## Requirements

The implemented tools require Python 3.11 or newer and use only the standard library.

## Profile generation

Run `scripts/build-agents` to build every manifest in `agents/profiles/`, or pass one or more profile names explicitly:

```sh
scripts/build-agents global
```

Generated output is written to `agents/dist/<profile>/AGENTS.md`. Repeated builds leave identical files untouched.

## Generated-output verification

Run `scripts/check-generated` to compare every generated profile with a fresh in-memory build, or pass one or more profile names explicitly:

```sh
scripts/check-generated
scripts/check-generated global
```

The command does not modify files. It reports missing or stale output, prints a diff for stale files, and exits with a non-zero status when regeneration is required.

## Global installation

Run `scripts/install-global` to compare the generated global profile with the active Codex file. The command is a dry run unless `--apply` is passed:

```sh
scripts/install-global
scripts/install-global --apply
```

The installer refuses missing or stale generated output. Before replacing a changed target, it prints a diff and creates a timestamped backup. It honors `CODEX_HOME`, defaults to `~/.codex`, and accepts `--codex-home PATH` for isolated verification.
