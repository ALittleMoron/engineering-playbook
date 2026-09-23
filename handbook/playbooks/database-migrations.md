# Testing Database Migrations

Use this playbook when a migration changes existing persisted data or schema used by populated
tables.

1. Start from the revision immediately before the migration and insert representative rows into
   the affected tables.
2. Apply the migration and check the resulting data and schema. Where downgrade is supported,
   exercise it and check the resulting state as well.
3. Describe historical tables in the test independently of the current application ORM models;
   those models may change after the migration was written.

The migration is verified when the relevant upgrade and supported downgrade behavior work on
representative existing data without relying on today's ORM shape.
