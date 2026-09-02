# TODO

## Source inventory

- [ ] Create `references/agent-guidance-inventory.md` with an inventory of all 29 discovered `AGENTS.md` files from `design-system`, `engineering-playbook`, `knowledge-database`, `my-site`, `personal-workspace`, `rp`, and `start`, plus the global `~/.codex/AGENTS.md`.
  - Record the repository, scope, purpose, language, size, and source path for each file.
  - Identify exact duplicates, semantic overlap, conflicts, and rules coupled to a specific project.
- [ ] Create `references/source-projects.md` with a concise description of the reference material available from each source repository.
- [ ] Record the source Git commit for every imported example so later project changes cannot silently alter the reference meaning.
- [ ] Create a guidance migration table with `source`, `rule`, `scope`, `target`, `decision`, and `status` columns.
- [ ] Compare the related guidance sets in `my-site` and `personal-workspace` and separate shared practices from each project's domain-specific constraints.
- [ ] Inspect `design-system`, `knowledge-database`, `rp`, and `start` for guidance and examples absent from `my-site`, then add the unique sources to the inventory.

## Guidance lifecycle

- [ ] Write `governance/rule-lifecycle.md` with `proposed`, `active`, `deprecated`, and `archived` states and finite transitions between them.
- [ ] Write `governance/versioning.md` covering versioning for the handbook, agent profiles, and generated files.
- [ ] Write `governance/exceptions.md` and a finite exception template with scope, rationale, owner, and expiry condition.
- [ ] Create an ADR for the separation between `handbook`, `agents/fragments`, `agents/profiles`, and `agents/dist`, including the source of truth and manual-editing boundaries.
- [x] Create an ADR for the profile format and deterministic assembly of final `AGENTS.md` files.
- [x] Add distinct `CHANGELOG.md` entries for accepted behavioral changes, imported guidance, and profile releases.

## Agent guidance migration

- [x] Split the current `~/.codex/AGENTS.md` into minimal thematic fragments under `agents/fragments/core/` without expanding the original scope.
- [ ] Create a dedicated authority-boundaries fragment covering read-only inspection, ordinary local changes, actions requiring approval, and implicit scope expansion.
- [x] Create a dedicated guidance-maintenance fragment covering candidate collection, narrowest-scope placement, explicit approval, and duplicate prevention.
- [x] Create a dedicated fragment covering finite TODO items and placement of durable guidance in `AGENTS.md` or the handbook.
- [ ] Classify the root `my-site/AGENTS.md` into `core`, `processes`, `languages`, `stacks`, and `project-only`; do not move `project-only` rules into the global profile.
- [ ] Move reusable Python guidance from `my-site/backend/AGENTS.md` and `my-site/backend/src/core/AGENTS.md` into Python/backend fragments with source and applicability metadata.
- [ ] Move SQLAlchemy, PostgreSQL, and Alembic guidance from `my-site/backend/src/infra/postgresql/AGENTS.md` into dedicated stack fragments.
- [ ] Move the testing philosophy and structure from `my-site/backend/tests/AGENTS.md` into process fragments while separating universal ideas from pytest-, Litestar-, and PostgreSQL-specific guidance.
- [ ] Move Angular, frontend architecture, SSR, CSP, accessibility, and UI testing guidance from nested `my-site/frontend/**/AGENTS.md` files into specialized fragments.
- [ ] Move infrastructure and security boundaries from `my-site/infra/AGENTS.md` into an opt-in infrastructure profile rather than the global profile.
- [ ] Create a knowledge-base profile from `knowledge-database/AGENTS.md`, keeping Russian authorial style and Obsidian-specific guidance outside engineering profiles.
- [ ] Extract package-boundary and component-quality guidance from `design-system/AGENTS.md` into an opt-in design-system profile.
- [ ] Classify `start/**/AGENTS.md` and `rp/**/AGENTS.md` as references for legacy APIs, gateway/service boundaries, feature flags, DRAKON, and large service test suites.
- [ ] Resolve every semantic conflict between sources as one of: shared standard, separate profiles, documented exception, or rejected migration.
- [ ] Prepare a report of guidance intentionally retained only in source projects, with a concise rationale for each exception class.

## Engineering standards and project references

- [ ] Write `handbook/standards/general/testing.md` from real `my-site/backend/tests/` examples covering unit, HTTP contract, database integration, full-stack integration, and migration tests.
- [ ] Add a reference for test helpers and factories based on `my-site/backend/tests/helpers/`, `test_cases.py`, and `unit/mocks/providers/`, including boundaries between shared helpers and scenario-local setup.
- [ ] Add a reference for parallel PostgreSQL tests based on `backend/scripts/pytest_parallel.py`, `pytest_databases.py`, and `backend/tests/integration/conftest.py`.
- [ ] Add a migration-testing reference based on `my-site/backend/tests/migrations/` with upgrade, downgrade, and data-verification examples that do not import current ORM models.
- [ ] Add an architecture-testing reference based on `my-site/backend/tests/unit/test_architecture/`, separating useful boundary checks from tests of implementation trivia.
- [ ] Write `handbook/standards/general/api-design.md` from `my-site/backend/src/entrypoints/litestar/api/`, covering handlers, schemas, parameters, validation, error contracts, guards, and public/admin/internal contours.
- [ ] Add a paired backend/frontend API error-handling reference based on Litestar exception handlers and Angular `core/http` and interceptors.
- [ ] Write a backend architecture reference for `core`, `infra`, `entrypoints`, and `ioc` boundaries using `my-site` and `personal-workspace` as two independent examples.
- [ ] Write a persistence reference for SQLAlchemy models, storage contracts, Alembic migrations, native enums, UTC datetimes, and query-plan regression checks.
- [ ] Write a frontend architecture reference for Angular `core`, `features`, `shared`, and `testing`, including import boundaries, DTO-to-UI mapping, and feature ownership.
- [ ] Add a frontend testing reference for observable behavior, SSR/browser boundaries, accessibility, CSP, and JSDOM limitations based on `my-site/frontend/src/**/*.spec.ts`.
- [ ] Write a build-and-check reference for thin Make targets, delegated scripts, and reusable CI workflows from `my-site/Makefile`, `backend/scripts/`, `frontend/scripts/`, `infra/scripts/`, and `.github/workflows/`.
- [ ] Add an infrastructure-security reference for private networks, the nginx edge, secrets, container restrictions, and verifiable pre-deploy invariants from `my-site/infra/`.
- [ ] Add a performance reference for query-plan baselines, Lighthouse, and their Make and CI entry points in `my-site`.
- [ ] Add a design-system reference for package topology, public entry points, distribution, and independence from consumer-specific contracts.
- [ ] Add a legacy-service reference from `start` and `rp` covering gateway boundaries, API contract evolution, feature flags, test data factories, and test-suite scaling.
- [ ] Add a DRAKON reference from `start` covering diagram purpose, JSON validation, real rendering checks, and applicability boundaries; keep DRAKON out of default profiles.
- [ ] Add the source path, commit, context, useful property, and applicability limits to every imported code example.

## Profiles and templates

- [x] Define and document the profile manifest schema: name, description, fragment list, assembly order, and supported use cases.
- [x] Create a minimal `global` profile containing only genuinely user-wide guidance.
- [ ] Create opt-in `python-backend`, `angular-frontend`, `full-stack-web`, `infrastructure`, and `knowledge-base` profiles.
- [ ] Create `templates/AGENTS.repo.md` for project commands, structure, checks, and local constraints.
- [ ] Create `templates/AGENTS.service.md` for service- or bounded-context-specific guidance.
- [ ] Create `templates/AGENTS.override.md` for temporary local overrides with an explicit rationale and removal condition.
- [ ] Create ADR, RFC, pull request, and postmortem templates with minimal required sections.
- [ ] Create Python backend and Angular frontend project-bootstrap examples without files for unused stacks.

## Scripts and automation

- [x] Create an ADR selecting the tooling runtime and dependency policy before implementing the remaining scripts.
- [ ] Implement `scripts/inventory-agents`, accepting a set of roots and producing a stable machine-readable inventory without reading secret files.
- [x] Implement `scripts/build-agents` to assemble profiles from fragments into `agents/dist/` deterministically and include the source version.
- [x] Implement `scripts/check-generated` to fail when `agents/dist/` differs from a fresh build.
- [ ] Implement `scripts/check-structure` to validate required directories, README files in organizational directories, and the absence of empty placeholder files.
- [ ] Implement `scripts/check-links` to validate local Markdown links and report unavailable external sources separately.
- [ ] Implement `scripts/check-agents` to detect empty instructions, unknown fragments, profile cycles, repeated inclusions, and configured size-limit violations.
- [ ] Implement `scripts/diff-installed` to compare an assembled profile with a target `AGENTS.md` without modifying files.
- [x] Implement a safe `scripts/install-global` with dry-run by default, explicit `--apply`, a pre-write diff, and a backup of the replaced `~/.codex/AGENTS.md`.
- [ ] Implement a safe `scripts/apply-profile` for target repositories with dry-run by default, an explicit destination path, and refusal to overwrite unknown manual changes.
- [ ] Implement `scripts/run-evals` for deterministic structural evals and optional model-based cases enabled only by an explicit flag.
- [ ] Implement `scripts/check` as the single entry point for structure, links, generated output, agent validation, and deterministic evals.
- [ ] Add a thin root `Makefile` with `build`, `check`, `evals`, `diff-global`, `install-global`, and `apply-profile` targets delegating to scripts.
- [ ] Add a CI workflow that runs `make check` on pull requests without installing profiles or writing to external locations.
- [ ] Add tests for every script covering success, invalid input, dry-run, destination conflicts, and reproducible output.

## Evals

- [ ] Define an eval-case format with input context, active instruction chain, expected behavior, forbidden behavior, and rubric.
- [ ] Create deterministic evals for global/repository/nested precedence and `AGENTS.override.md` behavior.
- [ ] Create authority-boundary evals for read-only inspection, ordinary workspace writes, destructive actions, and scope expansion.
- [ ] Create scope-selection evals for global, repository, language, stack, and task-domain guidance, including rejection of recurring project-specific rules from the global profile.
- [ ] Create guidance-maintenance evals for proposed wording, target, rationale, explicit approval, and duplicate prevention.
- [ ] Create TODO evals for finite actions, absence of durable rules, and correct completion updates.
- [ ] Create API and testing cases from real `my-site` scenarios after removing project-private and unstable data.
- [ ] Create cross-profile conflict cases from differences among `my-site`, `knowledge-database`, `design-system`, `start`, and `rp`.
- [ ] Add an eval report containing case, failure, and skipped model-based-case counts plus the tested profile version.

## Documentation, rollout, and first release

- [ ] Write a playbook for migrating an existing `AGENTS.md`: inventory, classification, deduplication, profile selection, dry-run, review, and rollout.
- [ ] Write a guide for creating new guidance and choosing among a principle, standard, playbook, reference, template, and agent fragment.
- [ ] Write a guide for installing the global profile and applying a project profile, including dry-run and rollback commands.
- [x] Assemble the first `agents/dist/global/AGENTS.md` and compare it with the current `~/.codex/AGENTS.md` without writing to it.
- [ ] Show the first global-profile diff to the user and obtain separate explicit approval before installation.
- [ ] Prepare a pilot diff for `my-site` while preserving its project-specific and nested guidance; do not modify the source project without separate approval.
- [ ] Prepare a second pilot diff for a different repository type: `knowledge-database` or `design-system`.
- [ ] Verify a fresh-clone workflow covering build, `make check`, installation dry-run, and profile application to a temporary fixture repository.
- [ ] Update the root `README.md` with real commands after tooling exists and add a concise map of available profiles.
- [ ] Release `v0.1.0` after CI, deterministic evals, two pilot reviews, and reproducible-build verification pass.
