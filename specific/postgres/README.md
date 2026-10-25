<!-- rule-prefix: PG -->
# PostgreSQL

Scope: designing and running PostgreSQL databases for applications, on the major versions the PostgreSQL project currently supports. Architecture-level data rules, such as data ownership, consistency between services, the transactional outbox and versioned migrations, are in [general/data.md](../../general/data.md); this file covers how to apply them in PostgreSQL. For secrets, see [general/security.md](../../general/security.md), and for connecting from serverless functions, see [Serverless and edge hosting](../web-hosting/README.md).

> Entries are sorted by score from 1 to 10 ([criteria](../../RANKING.md)): 9–10 start here or strongly recommended, 6–8 recommended, 1–5 further reading or conditional.

## Adopted references

- `10` [PostgreSQL Documentation](https://www.postgresql.org/docs/current/) (PostgreSQL Global Development Group): **the baseline.** Read the manual for the version you run; the chapters on data definition, indexes, concurrency control, performance tips, routine maintenance, backup and restore, client authentication and database roles matter most for application work.
- `8` [Backup and Restore](https://www.postgresql.org/docs/current/backup.html) (PostgreSQL docs): SQL dumps, file system backups and continuous archiving with point-in-time recovery, and the trade-offs between them.
- `7` [Don't Do This](https://wiki.postgresql.org/wiki/Don%27t_Do_This) (PostgreSQL wiki): a short list of common mistakes in data types, SQL constructs, tools and authentication, with the rare cases where each is still the right choice.
- `7` [Versioning Policy](https://www.postgresql.org/support/versioning/) (PostgreSQL): how long each major version is supported, what minor releases contain, and the end-of-life date of every release.
- `7` [Performance Tips](https://www.postgresql.org/docs/current/performance-tips.html) (PostgreSQL docs): reading query plans with `EXPLAIN`, planner statistics, and populating a database efficiently.
- `7` [PgBouncer features](https://www.pgbouncer.org/features.html) (PgBouncer): the session, transaction and statement pooling modes and which PostgreSQL features each one supports.

## Key rules

### Schema and data types

- `8` `PG-1` **Declare integrity rules as constraints in the database: a primary key on every table, `NOT NULL` on most columns, and foreign key, unique and check constraints where the data needs them.** PostgreSQL then rejects every write that would break them, whichever code path makes it. ([PostgreSQL, Constraints](https://www.postgresql.org/docs/current/ddl-constraints.html))
- `7` `PG-2` **Store points in time as `timestamptz`, not `timestamp`.** `timestamptz` records an instant and converts input with a time zone to UTC; `timestamp` silently ignores the time zone, so arithmetic across zones or daylight saving changes can be wrong. ([PostgreSQL wiki, Don't use timestamp (without time zone)](https://wiki.postgresql.org/wiki/Don%27t_Do_This#Don.27t_use_timestamp_.28without_time_zone.29), [PostgreSQL, Date/Time Types: Time Stamps](https://www.postgresql.org/docs/current/datatype-datetime.html#DATATYPE-DATETIME-INPUT-TIME-STAMPS))
- `6` `PG-3` **Generate keys with identity columns, such as `id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY`, instead of `serial`.** `serial` makes schema, dependency and permission management cumbersome. An identity column doesn't guarantee uniqueness by itself, so also make it the primary key. ([PostgreSQL wiki, Don't use serial](https://wiki.postgresql.org/wiki/Don%27t_Do_This#Don.27t_use_serial), [PostgreSQL, Identity Columns](https://www.postgresql.org/docs/current/ddl-identity-columns.html))
- `6` `PG-4` **Use `text` for strings, rather than `char(n)` or a `varchar(n)` with an arbitrary limit.** The types perform the same, `char(n)` pads values with spaces, and an arbitrary limit rejects real data later. ([PostgreSQL, Character Types](https://www.postgresql.org/docs/current/datatype-character.html), [PostgreSQL wiki, Don't use char(n)](https://wiki.postgresql.org/wiki/Don%27t_Do_This#Don.27t_use_char.28n.29), [Don't use varchar(n) by default](https://wiki.postgresql.org/wiki/Don%27t_Do_This#Don.27t_use_varchar.28n.29_by_default))

### Indexes and queries

- `7` `PG-5` **Add indexes for the queries the application actually runs: find the costly ones with `pg_stat_statements`, check their plans with `EXPLAIN ANALYZE` on realistic data, and drop indexes that are never used.** Every index slows down writes. PostgreSQL doesn't index the referencing columns of a foreign key, so index them yourself when you join on them or delete referenced rows. ([PostgreSQL, Examining Index Usage](https://www.postgresql.org/docs/current/indexes-examine.html), [Indexes: Introduction](https://www.postgresql.org/docs/current/indexes-intro.html), [pg_stat_statements](https://www.postgresql.org/docs/current/pgstatstatements.html), [Foreign Keys](https://www.postgresql.org/docs/current/ddl-constraints.html#DDL-CONSTRAINTS-FK))

### Schema migrations

- `8` `PG-6` **Create and drop indexes on tables in use with `CREATE INDEX CONCURRENTLY` and `DROP INDEX CONCURRENTLY`.** A plain `CREATE INDEX` blocks writes to the table until it finishes. The concurrent forms can't run inside a transaction block. A failed concurrent build leaves an `INVALID` index behind: drop it and try again. ([PostgreSQL, CREATE INDEX: Building Indexes Concurrently](https://www.postgresql.org/docs/current/sql-createindex.html#SQL-CREATEINDEX-CONCURRENTLY), [DROP INDEX](https://www.postgresql.org/docs/current/sql-dropindex.html))
- `7` `PG-7` **Set a short `lock_timeout` at the start of each migration, and retry the migration when it times out.** Many `ALTER TABLE` forms need an `ACCESS EXCLUSIVE` lock; while the statement waits behind a long-running transaction, all later reads and writes on the table wait behind it. ([PostgreSQL, lock_timeout](https://www.postgresql.org/docs/current/runtime-config-client.html#GUC-LOCK-TIMEOUT), [Table-Level Locks](https://www.postgresql.org/docs/current/explicit-locking.html#LOCKING-TABLES), [Squawk, Applying migrations safely](https://squawkhq.com/docs/safe_migrations))
- `7` `PG-8` **Add foreign key and check constraints to existing tables as `NOT VALID`, then run `VALIDATE CONSTRAINT` in a separate transaction.** Adding the constraint then skips the table scan, and validation takes a lock that lets writes continue. PostgreSQL 18 also allows this for not-null constraints. ([PostgreSQL, ALTER TABLE: Notes](https://www.postgresql.org/docs/current/sql-altertable.html#SQL-ALTERTABLE-NOTES))

### Connections and transactions

- `7` `PG-9` **Put a connection pooler such as PgBouncer between the database and large numbers of clients, such as many app instances or serverless functions, instead of raising `max_connections`.** In transaction pooling mode, don't use session state such as `SET`, `LISTEN`, SQL `PREPARE` or session-level advisory locks. ([PostgreSQL wiki, Number Of Database Connections](https://wiki.postgresql.org/wiki/Number_Of_Database_Connections), [PgBouncer, SQL feature map for pooling modes](https://www.pgbouncer.org/features.html#sql-feature-map-for-pooling-modes), [PostgreSQL, max_connections](https://www.postgresql.org/docs/current/runtime-config-connection.html#GUC-MAX-CONNECTIONS))
- `7` `PG-10` **Keep transactions short, set `idle_in_transaction_session_timeout` to end abandoned ones, and leave autovacuum on.** An open transaction keeps its locks and stops vacuum from removing dead rows, which bloats tables. ([PostgreSQL, idle_in_transaction_session_timeout](https://www.postgresql.org/docs/current/runtime-config-client.html#GUC-IDLE-IN-TRANSACTION-SESSION-TIMEOUT), [Deadlocks](https://www.postgresql.org/docs/current/explicit-locking.html#LOCKING-DEADLOCKS), [Recovering Disk Space](https://www.postgresql.org/docs/current/routine-vacuuming.html#VACUUM-FOR-SPACE-RECOVERY))

### Backup and recovery

- `9` `PG-11` **Test restores regularly, and check that the restored database works and contains the correct data.** `pg_verifybackup` checks a base backup against its manifest, but the PostgreSQL docs say it doesn't replace a test restore. ([PostgreSQL, pg_verifybackup](https://www.postgresql.org/docs/current/app-pgverifybackup.html), [Backup and Restore](https://www.postgresql.org/docs/current/backup.html))
- `8` `PG-12` **Back up production databases with continuous archiving, base backups plus archived WAL, so that you can restore to any point in time, not only to the last dump.** Set up and test WAL archiving before you take the first base backup. ([PostgreSQL, Continuous Archiving and Point-in-Time Recovery](https://www.postgresql.org/docs/current/continuous-archiving.html))

### Security

- `8` `PG-13` **Connect the application as a role that isn't a superuser and doesn't own the tables, and grant it only the privileges it needs; run migrations as a separate owner role.** Owners can alter or drop their objects, a right that can't be revoked, and normally bypass row security. ([PostgreSQL, Role Attributes](https://www.postgresql.org/docs/current/role-attributes.html), [Privileges](https://www.postgresql.org/docs/current/ddl-priv.html), [Row Security Policies](https://www.postgresql.org/docs/current/ddl-rowsecurity.html))
- `7` `PG-14` **Use `scram-sha-256` password authentication over TLS, and have clients verify the server with `sslmode=verify-full`.** MD5 passwords are deprecated, and `trust` authentication over TCP/IP lets clients connect as any user without a password. ([PostgreSQL, Password Authentication](https://www.postgresql.org/docs/current/auth-password.html), [libpq SSL Support](https://www.postgresql.org/docs/current/libpq-ssl.html), [PostgreSQL wiki, Don't use trust authentication over TCP/IP](https://wiki.postgresql.org/wiki/Don%27t_Do_This#Don.27t_use_trust_authentication_over_TCP.2FIP_.28host.2C_hostssl.29))
- `5` `PG-15` **When tenants share tables, isolate their rows with row security policies, and make sure the application role isn't the table owner or use `FORCE ROW LEVEL SECURITY`.** Superusers, roles with `BYPASSRLS` and, by default, table owners bypass the policies. ([PostgreSQL, Row Security Policies](https://www.postgresql.org/docs/current/ddl-rowsecurity.html))

### Versions

- `9` `PG-16` **Run a supported major version, apply each minor release soon after it ships, and upgrade to a newer major version before the current one reaches end of life.** Each major version is supported for five years, and the project recommends always running the current minor release. Major upgrades need `pg_upgrade` or a dump and restore. ([PostgreSQL, Versioning Policy](https://www.postgresql.org/support/versioning/), [pg_upgrade](https://www.postgresql.org/docs/current/pgupgrade.html))

## How to enforce

Tools that check the key rules above automatically, in CI, the IDE or a commit hook. "Partly" means the tool covers only some of what the rule asks.

- `7` [pg_verifybackup](https://www.postgresql.org/docs/current/app-pgverifybackup.html): built into PostgreSQL; checks a base backup taken with `pg_basebackup` against its manifest, and can be run after every backup. Partly checks `PG-11`.
- `6` [Squawk](https://squawkhq.com/docs/rules): a linter for PostgreSQL migration files that runs in CI and in editors, and can comment on GitHub pull requests. [`require-concurrent-index-creation`](https://squawkhq.com/docs/require-concurrent-index-creation), [`require-concurrent-index-deletion`](https://squawkhq.com/docs/require-concurrent-index-deletion) and [`ban-concurrent-index-creation-in-transaction`](https://squawkhq.com/docs/ban-concurrent-index-creation-in-transaction) cover index changes, [`constraint-missing-not-valid`](https://squawkhq.com/docs/constraint-missing-not-valid) flags constraints added without `NOT VALID` or validated in the same transaction, [`require-lock-timeout`](https://squawkhq.com/docs/require-lock-timeout) flags migrations without a `lock_timeout`, and [`prefer-timestamptz`](https://squawkhq.com/docs/prefer-timestamptz), [`prefer-identity`](https://squawkhq.com/docs/prefer-identity), [`prefer-text-field`](https://squawkhq.com/docs/prefer-text-field) and [`ban-char-field`](https://squawkhq.com/docs/ban-char-field) flag the column types. Checks `PG-2`, `PG-4`, `PG-6` and `PG-8`, and partly `PG-3` and `PG-7`.
- `5` [pgBackRest `check`](https://pgbackrest.org/command.html#command-check): validates that WAL archiving and backups are configured correctly, and detects archiving problems that would leave backups incomplete; [`verify`](https://pgbackrest.org/command.html#command-verify) checks that the backups and archived WAL in a repository are valid. Partly checks `PG-11` and `PG-12`.

## Tutorials and further reading

- `7` [Tutorial](https://www.postgresql.org/docs/current/tutorial.html) (PostgreSQL docs): the official introduction to PostgreSQL, relational concepts and SQL.
- `7` [Use The Index, Luke](https://use-the-index-luke.com/) (Markus Winand): a free online book on SQL indexing and query tuning for developers, with notes for PostgreSQL.
- `5` [PostgreSQL 14 Internals](https://postgrespro.com/community/books/internals) (Egor Rogov, Postgres Professional): a free book on MVCC, vacuum, the buffer cache, WAL, locks, query execution and index types.
