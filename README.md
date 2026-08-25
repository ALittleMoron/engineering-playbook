# Engineering Playbook

An evolving source of engineering principles, standards, workflows, templates, and AI agent instructions.

The repository separates detailed human-facing material from concise, executable agent instructions. Reusable knowledge lives in the handbook, while distributable `AGENTS.md` profiles are assembled from focused fragments.

## Structure

- [`governance/`](governance/) — rules for evolving the playbook itself.
- [`handbook/`](handbook/) — principles, standards, workflows, and decision history.
- [`agents/`](agents/) — source fragments, profiles, and assembled agent instructions.
- [`templates/`](templates/) — templates for new projects and engineering documents.
- [`references/`](references/) — curated examples, sources, and architecture references.
- [`evals/`](evals/) — agent behavior scenarios and expected results.
- [`scripts/`](scripts/) — automation for building, validating, and installing artifacts.

## Evolution model

A new practice starts as an observation or local decision. Once its value is supported by evidence, it may become a playbook, standard, or agent instruction. A rule's strictness should match the strength of its evidence, and material changes should remain visible in Git history and [`CHANGELOG.md`](CHANGELOG.md).

The finite backlog for populating and automating the repository lives in [`TODO.md`](TODO.md).

The root [`AGENTS.md`](AGENTS.md) defines how to maintain this repository. It is not a global template for other projects.
