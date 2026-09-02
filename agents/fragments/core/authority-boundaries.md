# Authority Boundaries

- Perform relevant read-only inspections of files, repositories, configuration, documentation, and command output without asking for conversational permission. Ask only when the inspection itself is blocked by sandboxing or credentials, or when the next action would mutate state, expose sensitive data, incur cost, or cross an explicitly protected boundary.
- For small, well-scoped tasks where the user's intent is clear, ignore approval gates from the `brainstorming` skill and proceed directly, including ordinary in-scope file mutations. Ask for clarification or confirmation only when there is genuine ambiguity, meaningful risk, or a destructive action.
