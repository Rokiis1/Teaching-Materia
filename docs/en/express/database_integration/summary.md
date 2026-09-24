# Summary

This summary brings together the most important concepts from the **Database Integration** module. It provides a quick reference for reviewing how an Express application connects to PostgreSQL, executes database queries, works with query results, and retrieves related data.

## Table of Contents: Database Integration

- [Level 1](#level-1)

## Level 1

Level 1 establishes the foundations of **PostgreSQL integration with Express, database connections, connection pooling, CRUD queries, parameterized queries, query results, and related data**. The main goal is to understand how an Express application communicates with PostgreSQL and uses stored data when handling HTTP requests.

A **database** provides persistent storage outside the running Node.js process. In this project, PostgreSQL stores account and profile data in the `users` and `profiles` tables. The `profiles.user_id` column references `users.id`, creating the relationship between a user and a profile.

The Node.js application communicates with PostgreSQL through the **node-postgres** database driver provided by the `pg` package. A shared `Pool` manages reusable database connections so application modules can use the same pool instead of creating a new connection for every request.

```js
import { Pool } from "pg";

const pool = new Pool({
    host: process.env.PGHOST,
    port: Number(process.env.PGPORT) || 5432,
    database: process.env.PGDATABASE,
    user: process.env.PGUSER,
    password: process.env.PGPASSWORD,
});

export default pool;
```

Database connection values are supplied through environment variables rather than being written directly into the source code. The Express application can use separate **liveness** and **readiness** routes to distinguish between the Node.js application running and the application being able to communicate successfully with PostgreSQL.

Express routes execute SQL through `pool.query()`. The common **CRUD** operations connect HTTP methods with SQL statements.

| Operation | HTTP Method      | SQL Statement |
|-----------|------------------|---------------|
| Create    | `POST`           | `INSERT`      |
| Read      | `GET`            | `SELECT`      |
| Update    | `PUT` or `PATCH` | `UPDATE`      |
| Delete    | `DELETE`         | `DELETE`      |

The `pool.query()` method returns a query result. Returned database records are available through `result.rows`. When a query returns a collection, the application can use the complete array. When one row is expected, it can use `result.rows[0]`.

```js
const result = await pool.query(
    `
        SELECT id, email
        FROM users
        WHERE id = $1
    `,
    [id],
);

res.json(result.rows[0]);
```

Queries that use values from `req.body` or `req.params` should use **parameterized queries**. Placeholders such as `$1` and `$2` remain in the SQL text, while the corresponding JavaScript values are passed separately in an array.

!!! warning "Pass Request Values as Query Parameters"

    Do not insert request values directly into SQL strings. Keep the SQL text separate from request values by using placeholders and the values array provided to `pool.query()`.

PostgreSQL's `RETURNING` clause can return rows affected by `INSERT`, `UPDATE`, or `DELETE`. This allows the application to use the created, modified, or removed row without executing a separate query.

Related information stored in different tables can be retrieved with a SQL **join**. A **join condition** compares values from columns in the participating tables. In this project, `profiles.user_id = users.id` compares the profile's user identifier with the user's identifier. Equal values form a **match** between those rows.

An `INNER JOIN` returns only rows for which a match exists. A `LEFT JOIN` keeps every row from the table on the left and fills selected columns from the right table with `null` when no matching row exists.

```sql
SELECT
    users.id,
    users.email,
    profiles.name AS profile_name
FROM users
LEFT JOIN profiles
    ON profiles.user_id = users.id;
```

The `AS` keyword creates a **column alias** in the query result. For example, `profiles.name AS profile_name` makes the value available as `profile_name` without changing the actual `name` column in the database.

!!! abstract "Database Integration Flow"

    **Express receives an HTTP request, the route executes SQL through the shared PostgreSQL pool, PostgreSQL processes the query and returns a result, and the route uses that result to create the HTTP response.**

!!! info "Error Handling"

    Database error handling and responses for missing resources are introduced in **Database Integration Level 2**.

After reviewing Level 1, you should be able to explain **how Express communicates with PostgreSQL through node-postgres**, describe the purpose of a shared **connection pool**, configure database access with environment variables, connect **CRUD operations** to SQL statements, work with **query results**, use **parameterized queries** and `RETURNING`, explain how **join conditions** identify matching rows, distinguish `INNER JOIN` from `LEFT JOIN`, and use **column aliases** when retrieving related data.
