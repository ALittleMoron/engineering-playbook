# Sensitive Data in Engineering Artifacts

Keep real credentials, tokens, private keys, passwords, and production environment values out of
code, tests, documentation, and committed configuration.

Diagnostic logs and error reporting must not expose credentials or other sensitive request and
user data. Include only the context needed to distinguish failures, following the project's
redaction rules for identifiers and values.
