# Changelog

This file records notable changes to engineering guidance, agent profiles, templates, and the playbook structure.

## Unreleased

- Added a reusable task-estimation process fragment covering the 8–16 hour range, decomposition,
  testing, manual work, and estimates that do not assume AI assistance.

- Updated the global profile to `0.2.0`: authorized reversible local work no longer requires
  repeated workflow approval, while protected Git, publication, production, cost, and data
  boundaries remain explicit.
- Replaced the brainstorming-specific workaround with a general authorization rule and bounded
  completion guidance. Removed mandatory empty guidance reports and clarified that an approved
  audit authorizes its in-scope instruction changes.
- Made this repository the explicit source for subsequent global-profile updates and simplified
  repository maintenance guidance around contextual inspection and verification.

- Released the initial `global` profile as version `0.1.0`.
- Added deterministic profile generation, read-only generated-output verification, and safe dry-run-first global installation tooling.
- Adopted TOML profile manifests and dependency-free Python tooling through ADRs 0001 and 0002.
- Imported the current global Codex guidance into reusable core agent fragments.
- Created the initial repository structure.
- Added repository maintenance guidance in `AGENTS.md`.
