# Governance

Guidance should encode evidenced constraints and preferences with the narrowest useful scope.
Human-facing rationale belongs in the handbook; agent runtime instructions should remain concise.

When revising a rule, distinguish product or security invariants from an agent's prescribed
procedure. Preserve the former; retain procedural instructions only when they solve an observed
problem that the normal workflow does not already handle. Evaluate changes on representative tasks
using completion, unnecessary interruptions, verification quality, and regressions rather than
instruction length alone. Account for other models and contributors that consume shared profiles.

An explicit request to implement an agreed guidance change authorizes that scope. Separate
approval remains necessary for additional protected actions outside it. Record behavioral changes
in `CHANGELOG.md`; keep source fragments, generated profiles, and authorized installations aligned.

## Reference

[OpenAI: Rethinking skills and prompts for GPT-6 Astra](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra),
published 2026-09-11, retrieved 2026-09-13. Practical takeaway: narrow skill triggers and document
routes, remove obsolete procedural scaffolding, and define authorization and completion clearly.
This is operational guidance, not evidence that removing constraints guarantees better results.
