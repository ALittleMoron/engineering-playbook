# Testing

- Choose whether and how to test from the change's risk, durable contracts, and regression value.
  Do not default to strict TDD or add an automated test for every code change.
- Prefer tests of externally observable behavior. Add a focused regression test for a fixed defect
  when reproducing the failure protects against a credible recurrence.
- Choose the test boundary that can prove the behavior: isolate self-contained logic, but use real
  database, middleware, or integration boundaries when the contract depends on queries,
  transactions, concurrency, or request processing. Avoid repeating isolated cases through the
  full stack without a distinct regression risk.
- When intentionally removing a feature that is no longer required, remove or update its obsolete
  tests and verify the change directly. Do not add a permanent test merely to prove that the old
  behavior stays absent unless that absence is itself a durable requirement with meaningful
  regression risk.
- Do not use behavioral tests to assert incidental source text, file or directory layout, or the
  presence or absence of particular imports. Use a one-time inspection for a one-time change; when
  a static invariant must remain enforced, prefer an appropriate linter, type checker, dependency
  rule, or architecture check.
- Keep an automated check only when its long-term protection justifies its maintenance cost and
  the same confidence cannot be obtained more directly.
