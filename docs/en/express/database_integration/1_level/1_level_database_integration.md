# Level 1

## Table of Contents: Database Integration

- [Database Integration in Express](#database-integration-in-express)
- [Preparing PostgreSQL with pgAdmin](#preparing-postgresql-with-pgadmin)
- [Structuring Your Database Code](#structuring-your-database-code)
- [Installing and Configuring the Database Driver](#installing-and-configuring-the-database-driver)
- [Executing Database Queries in Routes](#executing-database-queries-in-routes)
- [Working with Related Data](#working-with-related-data)

**Database Integration Level 1** introduces how an Express application works with a PostgreSQL database. You will learn how the application connects to the database, executes SQL queries, works with query results, uses database data in routes, passes values safely to queries, and retrieves related data from multiple tables.

PostgreSQL is the database management system used throughout this module. **pgAdmin** provides a graphical interface for creating, inspecting, and managing PostgreSQL databases during development.

!!! info "Prerequisites"

    Before starting, you should be familiar with creating an Express application, defining routes, using `async` functions and `await`, and writing basic SQL statements. PostgreSQL and pgAdmin should already be installed.

With the required tools in place, you can begin by looking at how database integration fits into an Express application.

## Database Integration in Express

An Express application often needs to store and retrieve information that should remain available after the server stops and starts again. Examples include users, products, tasks, orders, and messages. A **database** provides persistent storage for this information outside the running Node.js process. Database integration allows Express to work with that stored data as part of handling HTTP requests and responses.

```mermaid
flowchart LR
    A["Client"] -->|"HTTP request"| B["Express application"]
    B -->|"Database query"| C["PostgreSQL"]
    C -->|"Query result"| B
    B -->|"HTTP response"| A
```

When a client sends an HTTP request that requires stored data, Express sends the necessary query to PostgreSQL. PostgreSQL processes the query and returns the result to the application, which uses that result to create the HTTP response. Before this flow can be implemented, the PostgreSQL database and the data used by the application need to be prepared.

## Preparing PostgreSQL with pgAdmin

Before Express can work with application data, PostgreSQL needs a database and the tables that will store that data. The project begins with `users` and `profiles`, which provide the initial structure for account and profile information. Open pgAdmin and connect to your PostgreSQL server. Create a database named `account_management`, then open the Query Tool for that database and create the initial project tables.

```sql
-- Account information
CREATE TABLE users (
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    password_hash VARCHAR(255),
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- Profile information
CREATE TABLE profiles (
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    user_id INTEGER NOT NULL UNIQUE REFERENCES users(id) ON DELETE CASCADE,
    name VARCHAR(100),
    phone VARCHAR(30),
    address VARCHAR(255)
);
```

The `users` table stores the main account information. The `id` column provides a unique identifier for each user, while `email` must contain a unique value. The `created_at` and `updated_at` columns record when the account was created and when its data was last updated. The `profiles` table stores additional information separately from the account, with each profile connected to one user through `user_id`. This structure keeps account and profile data separate as the application grows.

!!! warning "Password Storage"

    The `password_hash` column is reserved for authentication data. Passwords must never be stored as plain text. Password hashing and the logic for storing password hashes will be introduced when authentication is implemented. For now, `password_hash` can remain empty while the examples focus on connecting Express to PostgreSQL and working with application data.

!!! info "Simplified Database Structure"

    This is the initial version of the project database. As the project develops, the schema can be improved with **constraints** for stronger data rules, **indexes** for frequently searched data, **views** for reusable and controlled representations of stored data, and **functions and triggers** for database behavior that should run automatically. These features are intentionally not added yet so the first implementation can remain focused on database integration.

Add a small amount of sample data for the first database queries.

```sql
-- Create sample accounts
INSERT INTO users (email)
VALUES
    ('vardenis@example.com'),
    ('pavardenis@example.com');

-- Create profiles for the sample accounts
INSERT INTO profiles (user_id, name, phone, address)
VALUES
    (1, 'Vardenis', '+37060000001', 'Vilnius'),
    (2, 'Pavardenis', '+37060000002', 'Kaunas');
```

Confirm that the sample data was created by querying both tables.

```sql
SELECT *
FROM users
ORDER BY id;

SELECT *
FROM profiles
ORDER BY id;
```

!!! success "Database Ready"

    If both queries return the inserted rows, the `account_management` database is ready to be used by the Express application.

The initial database now provides enough structure for the application to begin working with account and profile data. It will continue to evolve as later requirements introduce authentication, authorization, additional data rules, and more advanced PostgreSQL features. With the database prepared, the next step is to install the database driver that allows the Node.js application to communicate with PostgreSQL.

## Structuring Your Database Code

The project will use a small database module so the PostgreSQL connection setup has one clear location. For now, keep the structure simple and place the application files inside the existing `app/` directory.

```text
project/
├── app/
│   ├── app.js
│   └── db.js
├── package.json
├── package-lock.json
└── .env
```

The `app/db.js` file will contain the PostgreSQL connection setup, while `app/app.js` remains the main Express application file. The `.env` file stores the environment-specific values used by the application.

!!! tip "Keep Database Configuration in One Place"

    Create one shared `Pool` for the application and export it from `db.js`. Other application files should import this pool instead of repeating the PostgreSQL connection configuration or creating a new pool for each request.

!!! info "Project Structure"

    This is a simplified project structure for database integration. The application structure will be expanded and reorganized later in the **Software Architecture** module. For now, only the files required for the current database integration are shown.

With the location for the database code established, the application can now add the PostgreSQL driver and configure its connection.

## Installing and Configuring the Database Driver

Node.js needs a **database driver** to communicate with PostgreSQL. This project uses node-postgres, which provides the `pg` module. Follow the installation instructions in the [node-postgres documentation](https://node-postgres.com/).

node-postgres provides both [`pg.Client`](https://node-postgres.com/apis/client) and [`pg.Pool`](https://node-postgres.com/apis/pool), but they manage connections differently. A `Client` represents one database connection that the application connects and closes explicitly, while a `Pool` manages reusable client connections and provides them when they are needed. Because an Express application can handle multiple requests over time, this project uses one shared `Pool`.

``` mermaid
flowchart TB
    subgraph ClientApproach["pg.Client"]
        A["Application"] --> B["One Client"]
        B --> C["PostgreSQL"]
    end

    subgraph PoolApproach["pg.Pool"]
        D["Express application"] --> E["Connection Pool"]
        E --> F["Client connection"]
        E --> G["Client connection"]
        E --> H["Client connection"]
        F --> I["PostgreSQL"]
        G --> I
        H --> I
    end
```

As introduced in **Node Environment Level 2**, this project uses dotenv to load environment variables from a `.env` file. The environment configuration is loaded once in the application's entry point and is then available through `process.env` throughout the Node.js process. The database module therefore only needs to read the values from `process.env` and does not need to load dotenv again.

Store the PostgreSQL connection values in the project's `.env` file.

```env
PGHOST=localhost
PGPORT=5432
PGDATABASE=account_management
PGUSER=postgres
PGPASSWORD=your_password
```

`PGHOST` identifies the PostgreSQL server, `PGPORT` identifies its port, `PGDATABASE` specifies the database, `PGUSER` specifies the PostgreSQL user, and `PGPASSWORD` contains that user's password. Replace the example credentials with the values configured on your development machine.

!!! warning "Keep Credentials Outside Source Code"

    Keep database connection values in `.env` rather than writing credentials directly in application source code. pgAdmin can be used to create, inspect, and manage the database during development, but the Express application connects directly to PostgreSQL through `pg`.

Configure one shared pool in `app/db.js`. Because the environment has already been loaded by the application entry point, `db.js` can read the PostgreSQL connection values directly from `process.env`.

```js
import { Pool } from "pg";

const pool = new Pool({
    host: process.env.PGHOST,
    port: Number(process.env.PGPORT) || 5432,
    database: process.env.PGDATABASE,
    user: process.env.PGUSER,
    password: process.env.PGPASSWORD,
});

pool.on("error", (err) => {
    console.error("Unexpected PostgreSQL pool error:", err);
});

export default pool;
```

The pool creates database clients when they are needed and reuses available connections instead of creating a new connection for every request. The `error` listener handles unexpected errors from clients that are already connected but currently idle in the pool.

!!! info "Connection URI"

    The same connection information can also be represented by one connection URI such as `DATABASE_URL=postgresql://postgres:your_password@localhost:5432/account_management` and passed with `new Pool({ connectionString: process.env.DATABASE_URL })`. This project uses separate environment variables so each connection value remains explicit.

The default pool settings are sufficient for the current examples. Applications can customize connection limits, timeouts, connection lifetime, and other pool behavior when needed. See the [node-postgres pool documentation](https://node-postgres.com/apis/pool) for the available configuration options.

Import the shared pool into `app/app.js`. dotenv is loaded once at the beginning of this entry point, before the application uses environment variables. After that initialization, imported application modules such as `db.js` can access the same values through `process.env`.

```js
import "dotenv/config";
import express from "express";
import pool from "./db.js";

const app = express();
const PORT = process.env.PORT || 3000;

app.use(express.json());

// Liveness: Is the Node.js application running?
app.get("/health/live", (req, res) => {
    res.status(200).json({
        status: "ok",
    });
});

// Readiness: Can the application actually serve requests?
app.get("/health/ready", async (req, res) => {
    try {
        await pool.query("SELECT 1");

        res.status(200).json({
            status: "ready",
        });
    } catch (err) {
        console.error("Database readiness check failed:", err);

        res.status(503).json({
            status: "not_ready",
        });
    }
});

app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```

The liveness check does not depend on PostgreSQL, so it can still report that the Node.js application is running when the database is unavailable. The readiness check uses `pool.query("SELECT 1")` to verify that the pool can establish or reuse a PostgreSQL connection and successfully execute a minimal query. A successful check returns HTTP `200` with `status: "ready"`, while a database failure returns HTTP `503` with `status: "not_ready"`.

This keeps environment initialization in one place. `app.js` loads the `.env` configuration with dotenv, `db.js` reads the already available values from `process.env` and configures the shared PostgreSQL pool, and the rest of the application imports that pool when database access is required. Application database queries are introduced in the next section.

## Executing Database Queries in Routes

Express routes can use the shared `pool` to execute SQL and work directly with data stored in PostgreSQL. This connects the HTTP methods used by the API with the four common database operations known as **CRUD**. `POST` creates data with `INSERT`, `GET` reads data with `SELECT`, `PUT` and `PATCH` update data with `UPDATE`, and `DELETE` removes data with `DELETE`. The `pool.query()` method sends SQL to PostgreSQL and returns a promise, so an asynchronous route handler can use `await` to wait for the database result before sending the HTTP response.

```mermaid
flowchart LR
    A["POST"] -->|"Create"| E["INSERT"]
    B["GET"] -->|"Read"| F["SELECT"]
    C["PUT / PATCH"] -->|"Update"| G["UPDATE"]
    D["DELETE"] -->|"Delete"| H["DELETE"]

    E --> I["PostgreSQL"]
    F --> I
    G --> I
    H --> I
```

The first CRUD operation is **Create**. A `POST` route receives data from the request body and uses `INSERT` to create a new row in the `users` table. The email from `req.body` is passed as a query value, while PostgreSQL's `RETURNING` clause returns the newly created row so it can be included in the HTTP response.

``` js
app.post("/users", async (req, res) => {
    const { email } = req.body;

    const result = await pool.query(
        `
            INSERT INTO users (email)
            VALUES ($1)
            RETURNING id, email, created_at
        `,
        [email],
    );

    res.status(201).json(result.rows[0]);
});
```

In this query, `$1` represents the first value in the values array, which is `email`. The created row is available through `result.rows[0]` and is returned to the client with HTTP status `201`.

After creating data, **Read** operations use `GET` routes with `SELECT`. The following route retrieves all users from PostgreSQL and sends the returned rows to the client.

```js
app.get("/users", async (req, res) => {
    const result = await pool.query(
        `
            SELECT id, email, created_at
            FROM users
            ORDER BY id
        `,
    );

    res.json(result.rows);
});
```

For a `SELECT` query, `result.rows` contains an array of the rows returned by PostgreSQL. Because this route retrieves a collection of users, the complete array is sent as the JSON response. A `GET` route can also retrieve one user by using a route parameter as a query value.

```js
app.get("/users/:id", async (req, res) => {
    const { id } = req.params;

    const result = await pool.query(
        `
            SELECT id, email, created_at
            FROM users
            WHERE id = $1
        `,
        [id],
    );

    res.json(result.rows[0]);
});
```

Here, `$1` represents the `id` value from `req.params`. Because only one row is expected, the route returns `result.rows[0]` instead of the complete `result.rows` array.

Existing data can be changed with either `PUT` or `PATCH`, but the two HTTP methods communicate different intentions. `PUT` is generally used when the client sends a complete replacement representation of a resource, while `PATCH` is used when only part of the resource should change. Because the following **Update** operation changes only the user's email, it uses `PATCH`.

```js
app.patch("/users/:id", async (req, res) => {
    const { id } = req.params;
    const { email } = req.body;

    const result = await pool.query(
        `
            UPDATE users
            SET email = $1,
                updated_at = CURRENT_TIMESTAMP
            WHERE id = $2
            RETURNING id, email, created_at, updated_at
        `,
        [email, id],
    );

    res.json(result.rows[0]);
});
```

The `UPDATE` statement uses two placeholders. `$1` receives the new `email` value and `$2` receives the user's `id`. The query also sets `updated_at` to the current time and uses `RETURNING` to make the updated row available through `result.rows[0]`.

!!! info "PUT and PATCH"

    Both methods update an existing resource, but they express different intentions. `PUT` represents replacing the complete resource representation, while `PATCH` represents applying a partial change. The account example uses `PATCH` because only the email field is being changed.

The final CRUD operation is **Delete**. A `DELETE` route receives the user's identifier from the route parameter and uses it to remove the matching row from PostgreSQL.

```js
app.delete("/users/:id", async (req, res) => {
    const { id } = req.params;

    const result = await pool.query(
        `
            DELETE FROM users
            WHERE id = $1
            RETURNING id, email
        `,
        [id],
    );

    res.json(result.rows[0]);
});
```

`RETURNING` makes the deleted row available through `result.rows[0]`. If no row matches the supplied `id`, `result.rows` is empty. Handling cases where a requested resource does not exist will be covered together with database and route errors.

The examples that use values from `req.body` or `req.params` use **parameterized queries**. node-postgres keeps the SQL text separate from the values by using placeholders such as `$1`, `$2`, and `$3` and passing the corresponding JavaScript values in an array.

!!! tip "Working with Query Results"

    Use `await` with `pool.query()` when the route needs the query result before it can continue. Returned records are available in `result.rows`. Use `result.rows[0]` when a query is expected to return one row.

!!! warning "Pass Request Values as Query Parameters"

    When a query uses values from the request, use placeholders such as `$1` and `$2` in the SQL and pass the actual values separately to `pool.query()`. For example, `$1` represents the first value in the array, which is `id` in this query.

    ```js
    const { id } = req.params;

    const result = await pool.query(
        "SELECT id, email FROM users WHERE id = $1",
        [id],
    );
    ```

    Do not insert request values directly into the SQL string. Keeping the SQL and its values separate makes the query safer and follows the same parameterized query pattern used throughout the application.

The CRUD examples follow the same application flow. Express receives an HTTP request and the route extracts any required values before calling `pool.query()`. The pool obtains an available database client, executes the query through that connection, and makes the client available to the pool again when the query finishes. The query result is returned to the route handler, which uses it to create the HTTP response.

```mermaid
sequenceDiagram
    participant C as Client
    participant E as Express Route
    participant P as pg Pool
    participant PC as Database Client
    participant D as PostgreSQL

    C->>E: HTTP request
    E->>P: pool.query(SQL, values)
    P->>PC: Acquire available client
    PC->>D: Execute SQL query
    D-->>PC: Query result
    PC-->>P: Return result
    P->>P: Release client back to pool
    P-->>E: result
    E-->>C: HTTP response
```

With the main CRUD operations connected to Express routes, the application can create, retrieve, modify, and remove PostgreSQL data through the API. The next section builds on these queries by retrieving related data from `users` and `profiles`.

## Working with Related Data

The application stores account information in `users` and additional user information in `profiles`. These tables are related through `profiles.user_id`, which references `users.id`. Because `user_id` is also `UNIQUE`, each user can have at most one profile. A SQL **join** allows PostgreSQL to combine columns from these related tables in one query instead of requiring the application to retrieve each table separately.

Joins are especially useful when reading related data with `SELECT`. In an API, this commonly happens in `GET` routes because those routes retrieve information for the client. For the current project, joins will be used with `SELECT` queries so the focus remains on retrieving related account and profile data.

For the current database structure, the important difference is whether users without profiles should appear in the result. An `INNER JOIN` keeps only users that have a matching profile, while a `LEFT JOIN` keeps every user and includes profile data only when a matching profile exists.

```mermaid
flowchart TB
    subgraph Inner["INNER JOIN"]
        IU["users"]
        IP["profiles"]
        IR["Only users with matching profiles"]
        IU --> IR
        IP --> IR
    end

    subgraph Left["LEFT JOIN"]
        LU["users"]
        LP["profiles"]
        LR["All users"]
        LM["Missing profile fields become null"]
        LU --> LR
        LP --> LR
        LR --> LM
    end
```

Use an `INNER JOIN` when the route should return only complete user and profile pairs. The `ON` condition tells PostgreSQL how the rows are related by matching `profiles.user_id` with `users.id`.

```js
app.get("/users/profiles", async (req, res) => {
    const result = await pool.query(`
        SELECT
            users.id,
            users.email,
            profiles.name,
            profiles.phone,
            profiles.address
        FROM users
        INNER JOIN profiles
            ON profiles.user_id = users.id
        ORDER BY users.id
    `);

    res.json(result.rows);
});
```

A user can exist before a profile is created because the `users` table does not require a corresponding row in `profiles`. If the application needs to return every user, including those without profiles, use a `LEFT JOIN`. Users without a matching profile remain in the result, while `name`, `phone`, and `address` contain `null`.

```sql
app.get("/users", async (req, res) => {
    const result = await pool.query(`
        SELECT
            users.id,
            users.email,
            profiles.name,
            profiles.phone,
            profiles.address
        FROM users
        LEFT JOIN profiles
            ON profiles.user_id = users.id
        ORDER BY users.id
    `);

    res.json(result.rows);
});
```

!!! info "Common Join Types"

    PostgreSQL also provides `RIGHT JOIN`, `FULL JOIN`, and `CROSS JOIN`. A `RIGHT JOIN` keeps every row from the table on the right even when no matching row exists on the left. A `FULL JOIN` keeps unmatched rows from both tables. A `CROSS JOIN` produces every possible combination of rows from the joined tables. These join types are useful in specific situations, but the current project does not require them. `INNER JOIN` and `LEFT JOIN` are enough for the account and profile examples in **Database Integration Level 1**.

The same join can be combined with a parameterized query when the application needs related data for one user. A `LEFT JOIN` is useful here because the account can still be returned even when its profile has not been created.

```js
app.get("/users/:id/profile", async (req, res) => {
    const { id } = req.params;

    const result = await pool.query(
        `
            SELECT
                users.id,
                users.email,
                profiles.name,
                profiles.phone,
                profiles.address
            FROM users
            LEFT JOIN profiles
                ON profiles.user_id = users.id
            WHERE users.id = $1
        `,
        [id],
    );

    res.json(result.rows[0]);
});
```

The join combines the related tables, while `WHERE users.id = $1` limits the result to the requested user. In this project, joins will mainly appear in read operations when the API needs information stored across multiple tables.

At this point, the Express application can connect to PostgreSQL, reuse a connection pool, execute CRUD queries, use returned rows in routes, pass values with parameterized queries, and retrieve related data with joins. **Database Integration Level 2** can build on this foundation with database error handling, transactions, migrations, stronger data access structure, and advanced query workflows.
