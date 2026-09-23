# Temporary Release Flags

Use this playbook when a new behavior is intentionally deployed behind a temporary release flag.

1. Create the flag disabled by default in each environment and make missing, unknown, or unavailable
   flag evaluations resolve to the safe disabled behavior.
2. Keep the disabled path equivalent to the previous public contract and relevant side effects;
   new-path side effects must not run while the flag is disabled.
3. Verify the relevant behavior with the flag disabled and enabled, including a provider failure
   case when the integration exposes one.
4. Record the cleanup path. After the released behavior is stable, remove the temporary flag and
   obsolete disabled path, then update affected tests.

The release is ready when both states and failure fallback are verified, and the temporary flag has
an explicit removal path. Long-lived operational or permission flags require their own lifecycle.
