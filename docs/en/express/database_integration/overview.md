# Overview

Database integration allows an Express application to work with persistent data stored outside the running Node.js process. By connecting Express to PostgreSQL, application routes can store, retrieve, modify, and remove data as part of handling HTTP requests and responses.

The **Database Integration** module develops from establishing a connection between an Express application and PostgreSQL to using the database as part of the application's data workflows. It introduces the tools and patterns required to configure database access, execute SQL through the application, work with query results, and retrieve data across related tables.

**Level 1** introduces the foundations of database integration. It covers preparing PostgreSQL for the project, structuring and configuring database access with **node-postgres**, using a shared connection pool, and connecting common database operations to Express routes. It also introduces **parameterized queries** for passing values to SQL and **joins** for retrieving related data from multiple tables.

Together, these topics establish the foundation for building an Express API backed by PostgreSQL. **Database Integration Level 2** can build on this foundation with database error handling, transactions, migrations, stronger data access structure, and more advanced query workflows.
