# Level 2

## Table of Contents: Middleware

- [Router-Level Middleware](#router-level-middleware)
- [Third-Party Middleware](#third-party-middleware)
- [Error-Handling Middleware](#error-handling-middleware)

**Middleware Level 2** expands the middleware model established in Level 1. It introduces middleware attached to `express.Router()` instances, middleware supplied by third-party packages, and the separate middleware flow used when errors occur. The regular middleware concepts from Level 1 still apply, including matching, registration order, `req`, `res`, and control flow through `next()`.

This module targets **Express 5.x**. Router-level middleware builds on the `express.Router()` foundation introduced in **Routing Level 1**, while the error-handling section introduces error handling from the middleware perspective before the **Error Handling** module develops that subject in greater detail.

## Router-Level Middleware

**Router-level middleware** is middleware attached to an `express.Router()` instance rather than directly to the Express application. It follows the same middleware model introduced in Level 1, but its scope is associated with the router on which it is registered.

```js
import express from "express";

const router = express.Router();

router.use((req, res, next) => {
  console.log("Router middleware");
  next();
});

router.get("/", (req, res) => {
  res.send("Users");
});

export default router;
```

In this example, the middleware is registered through `router.use()`. When a request reaches this router and matches the middleware, the middleware runs before the matching route handler and calls `next()` to continue processing.

The distinction between application-level and router-level middleware depends on where the middleware is attached. Middleware registered through methods such as `app.use()` and `app.get()` is application-level middleware, while middleware registered through methods such as `router.use()` and `router.get()` is router-level middleware.

Router-level middleware can also be limited by a path. The following middleware runs for requests that reach this router and match `/admin` or paths beneath it.

```js
router.use("/admin", (req, res, next) => {
  console.log("Router admin middleware");
  next();
});
```

A router can also use middleware for a specific route. In the following example, `logUserRequest` runs before the final route callback when `GET /users` matches within the router.

```js
function logUserRequest(req, res, next) {
  console.log("Users route requested");
  next();
}

router.get("/users", logUserRequest, (req, res) => {
  res.json([]);
});
```

Router-level middleware therefore does not introduce a different middleware execution model. It applies the same matching, registration-order, and control-flow concepts within an `express.Router()` instance. The routing material covers router organization and mounting in greater detail, including the `next("route")` behavior used to skip the remaining callbacks for the current route and continue to the next matching route. With router-level middleware connected to the Level 1 middleware model, the next section changes focus from where middleware is attached to where middleware comes from.

## Third-Party Middleware

**Third-party middleware** is middleware provided by an external package rather than written directly in the application or supplied as built-in Express middleware. It allows an application to add request-processing behavior without implementing every middleware function from scratch. Third-party middleware is typically added to the project through the package manager used by that project. After installation, the package is imported according to its documentation, configured when necessary, and registered with the Express application or a router.

```js
import middlewarePackage from "<package>";

app.use(middlewarePackage());
```

The exact installation command, import syntax, configuration options, and middleware behavior depend on the package. Some third-party middleware applies broadly to request processing, while other packages address a particular concern such as validation, logging, security, sessions, file uploads, or other application requirements. Registration order follows the same rules as other Express middleware, so if later middleware or route handlers depend on work performed by a third-party middleware package, that middleware must be registered before the code that needs its results.

Third-party middleware can be registered at the application level with `app.use()` or, when its behavior should be limited to a router, at the router level with `router.use()`.

```js
router.use(middlewarePackage());
```

The important distinction is where the middleware comes from and where it is registered. **Custom middleware** is written as part of the application, **built-in middleware** is supplied by Express, and **third-party middleware** is supplied by an external package. The package manager or operating system used to install that dependency does not change its role as third-party middleware in Express. Because third-party packages have their own APIs and configuration requirements, their documentation should be used to determine installation, setup, compatibility, and placement in the middleware chain. Specific packages can then be introduced where the functionality they provide is needed, rather than treating one package as the model for all third-party middleware.

With the source and placement of third-party middleware established, the next section moves from the regular middleware flow to the separate flow Express uses when errors occur.

## Error-Handling Middleware

**Error-handling middleware** handles errors passed through Express request processing. Unlike regular middleware, which uses the parameters `req`, `res`, and `next`, an error-handling middleware function has four parameters: `err`, `req`, `res`, and `next`.

```js
function errorHandler(err, req, res, next) {
  console.error(err);

  res.status(500).send("Something went wrong");
}
```

Express identifies error-handling middleware by its four-argument signature. The `next` parameter must remain even when the function does not use it directly.

A regular middleware function can enter the error-handling flow by passing an error to `next()`.

```js
app.use((req, res, next) => {
  const error = new Error("Something went wrong");

  next(error);
});
```

The named error handler can then be registered after the middleware and routes whose errors it should handle.

```js
app.get("/example", (req, res, next) => {
  next(new Error("Example error"));
});

app.use(errorHandler);
```

The key distinction is that **`next()` continues regular request processing, while `next(err)` passes control into the error-handling flow**. Registration order still matters because Express searches forward through the middleware stack for matching error-handling middleware.

For example, placing a custom error handler before a route does not make that handler catch errors produced later by the route.

```js
app.use(errorHandler);

app.get("/example", (req, res, next) => {
  next(new Error("Example error"));
});
```

The error handler has already been passed in the middleware stack when the route produces the error. Custom error-handling middleware is therefore normally registered after the middleware and routes whose errors it should handle.

Errors can also reach the error-handling flow when code throws. Errors thrown synchronously inside Express route handlers or middleware are caught by Express and processed as errors.

```js
app.get("/sync-error", (req, res) => {
  throw new Error("Synchronous error");
});
```

This is different from middleware that simply does nothing: middleware that neither sends a response, calls `next()`, nor throws leaves request processing without a way to continue. Synchronous throws therefore provide one path into error handling; asynchronous code introduces another.

Express 5 also forwards rejected promises from middleware and route handlers into error handling. An `async` route handler therefore does not need to call `next(err)` manually when an awaited operation rejects or the handler throws an error.

```js
app.get("/users", async (req, res) => {
  const users = await loadUsers();

  res.json(users);
});
```

If `loadUsers()` rejects, Express 5 forwards the failure into the error-handling flow automatically.

Automatic forwarding handles many Express 5 promise-based errors, but there are still situations where code needs to respond to an error at the point where it occurs. A `try...catch` block is useful when the application needs to perform work there. For example, the handler might add context, perform cleanup, or deliberately pass the caught error to Express.

```js
app.get("/users/:id", async (req, res, next) => {
  try {
    const user = await loadUser(req.params.id);

    res.json(user);
  } catch (err) {
    console.error("Failed to load user");
    next(err);
  }
});
```

In Express 5, `try...catch` is not required merely to forward errors from an awaited promise. Without the `try...catch` in this example, a rejection from `loadUser()` would still be forwarded automatically. When `try...catch` is used, calling `next(err)` passes the caught error into Express's error-handling flow. Promise-based asynchronous code therefore benefits from Express 5's automatic forwarding, but not every asynchronous API uses promises.

Some asynchronous APIs do not return promises and execute code later in callbacks. Errors thrown inside those callbacks are outside the synchronous Express handler, so they must be caught and passed to `next(err)` when necessary.

```js
app.get("/delayed", (req, res, next) => {
  setTimeout(() => {
    try {
      throw new Error("Delayed error");
    } catch (err) {
      next(err);
    }
  }, 100);
});
```

This section establishes error handling as a middleware category and shows the main ways control can reach it. Multiple error handlers, forwarding errors between handlers, response-state concerns, and broader application error strategy are developed in the **Error Handling** module.

This completes **Middleware Level 2**. Middleware can now be applied at the application and router levels, supplied by Express or third-party packages, and used in the separate error-handling flow.
