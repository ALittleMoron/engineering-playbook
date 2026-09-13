# Engineering Playbook Repository Guidance

## Ownership and placement

- This repository is the canonical source for reusable engineering guidance. This root AGENTS.md
  governs repository maintenance; it is not the distributable global profile.
- Keep concise runtime instructions in `agents/fragments/`, composition metadata in
  `agents/profiles/`, and generated self-contained output in `agents/dist/`. Edit sources and
  regenerate output; do not rely on undocumented Markdown includes.
- Keep explanations and examples in `handbook/` and `references/`, reusable copied material in
  `templates/`, and finite work in `TODO.md`. Use the root README for the directory map.
- Place each rule at its narrowest valid scope. Recurrence across projects does not make a
  framework, language, repository, or workflow rule global.

## Guidance changes

- Inspect the related source fragments and decision records for the changed concept. Keep one
  canonical statement; remove duplicates and obsolete procedures rather than accumulating rules.
- Prefer outcomes, domain invariants, and concrete authorization boundaries to prescribed reasoning
  steps. Link optional detail where it is relevant; do not require blanket documentation reads,
  approval ceremonies, test repetitions, or agent delegation for every task.
- Present wording, target, and rationale before changing durable guidance unless the user has
  already authorized the proposal or audit implementation. Do not ask again within that scope.
- Record behavioral changes in `CHANGELOG.md` and version changed distributable profiles. Add an
  ADR when a new repository-wide convention or meaningful trade-off needs a lasting explanation.
- Keep temporary exceptions scoped with an owner, reason, and expiry condition. Preserve unrelated
  user changes. Do not create placeholder documentation or open-ended TODO items.
- For external references, record the source, retrieval date, and practical takeaway. Keep copied
  content within its license and maintenance constraints.

## Verification and installation

- For profile changes, run `scripts/build-agents`, `scripts/check-generated`, and the existing
  tooling tests using Python 3.11+; commands and installation semantics live in `scripts/README.md`.
- Review the diff and run `git diff --check`. Check links and directory READMEs only where changed.
- Preview a global installation with `scripts/install-global`; use `--apply` when installation is
  authorized. The installer backs up the old file and replaces it atomically.
