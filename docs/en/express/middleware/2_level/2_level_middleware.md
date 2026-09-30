# Level 2

## Table of Contents: Middleware

- [Router-Level Middleware](#router-level-middleware)
- [Third-Party Middleware](#third-party-middleware)
- [Error-Handling Middleware](#error-handling-middleware)

**Middleware Level 2** expands the middleware model established in **Middleware Level 1** with middleware attached to `express.Router()` instances, the separate middleware flow used when errors occur, and middleware supplied by third-party packages. The same core concepts still apply, including matching, registration order, `req`, `res`, and control flow through `next()`.

This module targets **Express 5.x**. Router-level middleware builds on **Routing Level 1**, while error-handling middleware is introduced here from the middleware perspective before the **Error Handling** module develops error-handling behavior in greater detail.

## Router-Level Middleware

**Router-level middleware** is middleware attached to an `express.Router()` instance rather than directly to the Express application. It follows the same execution model as application-level middleware, but its scope is associated with the router on which it is registered.

```js
import express from "express";

const router = express.Router();

router.use((req, res, next) => {
  console.log("Router middleware");
  next();
});

function logUserRequest(req, res, next) {
  console.log("Users route requested");
  next();
}

router.get("/users", logUserRequest, (req, res) => {
  res.send("Users");
});
```

In this example, `router.use()` registers router-level middleware that can run before matching routes. The `GET /users` route also places `logUserRequest` directly between the route path and the final route handler. When that route matches, `logUserRequest` runs first and calls `next()`, allowing Express to continue to the final callback that sends the response. Both forms are router-level middleware because they are registered through the router.

The distinction between application-level and router-level middleware therefore depends on where the middleware is attached: methods such as `app.use()` and `app.get()` attach middleware to the application, while `router.use()` and `router.get()` attach it to a router. Router-level middleware can apply more broadly through `router.use()`, be limited by a path, or run only for a specific route by placing it between the route path and the final handler. Router organization, mounting, and `next("route")` behavior belong to the routing material. With middleware now established at both the application and router levels, the next section follows what happens when normal request processing encounters an error.

## Error-Handling Middleware

**Error-handling middleware** handles errors passed through Express request processing. Unlike regular middleware, which receives `req`, `res`, and `next`, error-handling middleware has four parameters: `err`, `req`, `res`, and `next`. Express uses this four-argument signature to identify an error handler, so `next` must remain even when the function does not use it directly.

```js
function errorHandler(err, req, res, next) {
  console.error(err);
  res.status(500).send("Something went wrong");
}

app.get("/example", (req, res, next) => {
  next(new Error("Example error"));
});

app.use(errorHandler);
```

Calling `next()` continues regular request processing, while `next(err)` passes control into the error-handling flow. Registration order also matters because Express searches forward through the middleware stack for an error handler, so custom error-handling middleware is normally registered after the middleware and routes whose errors it should handle.

Errors can reach the same error-handling flow in other ways. Express catches errors thrown synchronously inside middleware and route handlers, while Express 5 automatically forwards rejected promises and errors thrown from `async` middleware and route handlers. Because promise-based errors are forwarded automatically, `try...catch` is not required merely to pass them to error-handling middleware. It is useful when the application needs to perform additional work, such as logging or cleanup, before calling `next(err)`.

```js
app.get("/users", async (req, res, next) => {
  try {
    throw new Error("Could not load users");
  } catch (err) {
    console.error("Failed to load users");
    next(err);
  }
});
```

The same automatic forwarding does not apply to errors thrown later inside callback-based asynchronous code. In those cases, the error must be caught and passed to `next(err)` so Express can continue through the error-handling flow. This distinction is developed further in the **Error Handling** module.

With the main error-handling middleware flow established, the final section returns to regular middleware and considers middleware supplied outside the application and Express itself.

## Third-Party Middleware

**Third-party middleware** is middleware provided by an external package rather than written as part of the application or supplied by Express. It adds functionality such as validation, logging, security, sessions, or file uploads without requiring the application to implement that behavior from scratch.

After a package is installed, it is imported, configured as required, and registered with the application or a router according to the package's documentation.

```js
import middlewarePackage from "<package>";

app.use(middlewarePackage());
```

Third-party middleware follows the same Express middleware principles established earlier, including matching, registration order, and placement in the request processing chain. Its installation, configuration, and behavior depend on the package, so its documentation should be used when integrating it into an application.

This completes **Middleware Level 2**. Middleware can now be attached to applications and routers, participate in regular and error-handling flows, and be provided by application code, Express, or third-party packages.
