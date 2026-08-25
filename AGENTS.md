# Engineering Playbook Repository Guidance

## Purpose

- Treat this repository as the canonical source for reusable engineering guidance, workflows, templates, references, and agent instructions.
- Keep explanatory material for humans separate from concise runtime instructions for agents.
- Treat this root `AGENTS.md` as guidance for maintaining this repository, not as a distributable global agent profile.

## Repository map

- `governance/` defines how guidance is proposed, reviewed, versioned, deprecated, and excepted.
- `handbook/principles/` explains durable engineering values and the reasoning behind them.
- `handbook/standards/` contains normative engineering rules organized by general concern, language, or stack.
- `handbook/playbooks/` contains finite, repeatable operational procedures.
- `handbook/decisions/` records why consequential repository and guidance decisions were made.
- `agents/fragments/` contains reusable source fragments for agent instructions.
- `agents/profiles/` declares which fragments compose each agent profile.
- `agents/dist/` contains generated, self-contained distributable instructions.
- `templates/` contains content intended to be copied and adapted.
- `references/` contains curated examples and external-source notes, not normative rules.
- `evals/` contains behavior cases and expected outcomes for agent guidance.
- `scripts/` contains repository automation.

## Placement and scope

- Put each rule in the narrowest location whose full scope it governs.
- Do not promote a repository-, language-, framework-, toolchain-, or task-specific rule into a global profile merely because it recurs.
- Prefer updating or linking to one canonical statement over duplicating the same rule.
- Keep rationale, background, and extended examples in the handbook. Keep agent instructions concise, imperative, and self-contained.
- Do not use `TODO` files for durable principles, architecture, process, or working agreements. Put durable guidance in the applicable `AGENTS.md` or handbook section.
- Keep a short `README.md` in organizational directories so their purpose and content boundary remain discoverable.

## Agent guidance lifecycle

- Treat `agents/fragments/` as the source of truth for reusable agent instructions.
- Treat `agents/profiles/` as composition metadata, not duplicated instruction text.
- Once generation tooling exists, do not manually edit generated files in `agents/dist/`; update the source fragment or profile and regenerate.
- A distributable `AGENTS.md` must be understandable without relying on undocumented include behavior.
- Before adding, editing, relocating, or removing durable agent guidance, present the proposed wording, target file, and rationale to the user and obtain explicit approval.
- Record temporary exceptions with a clear scope, owner, reason, and expiry condition rather than weakening the canonical rule.

## Documentation quality

- State the problem or intent before prescribing a rule.
- For normative guidance, make the scope, exceptions, and verification method explicit when they are not obvious.
- Use concrete examples when they prevent ambiguity; avoid examples that merely repeat the prose.
- Keep documents focused and link related material rather than building large catch-all pages.
- Record the source, retrieval date, and practical takeaway for external references. Avoid vendoring third-party content unless its license and maintenance plan are clear.
- Do not add speculative sections, empty placeholders, or open-ended task lists.

## Change workflow

- Inspect related guidance and decision records before proposing a change.
- Keep changes small enough that one rule or concept can be reviewed independently.
- Distinguish editorial clarification from a behavioral change; document behavioral changes in `CHANGELOG.md`.
- Add or update a decision record when a change establishes a durable repository-wide convention or resolves a meaningful trade-off.
- Preserve existing user changes and unrelated work in the worktree.

## Verification

- Run the narrowest relevant repository checks after changes.
- At minimum, run `git diff --check`, inspect the final diff, and verify that new organizational directories contain a concise `README.md`.
- If generation or evaluation tooling exists for the changed area, run it and report the exact commands and results.
- Do not claim completion without fresh verification evidence.
