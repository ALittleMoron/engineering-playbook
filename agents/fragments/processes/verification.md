# Verification

- Find the current project's supported checks in its local instructions, scripts, configuration,
  and CI. Use the relevant project commands for the change. Bypass a required project command only
  when the user explicitly instructs you to do so for the current task; do not infer permission from
  convenience, an environment failure, or a workflow skill. Do not present an ad hoc check or
  another project's toolchain as equivalent to a required check.
- Report only checks actually run, with their results. Name failed or blocked checks and the
  concrete reason; do not claim unrun checks passed.
- Before adding a command to an agent-trusted or automatically approved list, inspect the command
  and its delegated scripts for writes, destructive operations, network access, dependency changes,
  migrations, credential exposure, and long-running services.
