# Summary

This summary brings together the most important concepts from the **Express Fundamentals** module. It is designed as a quick reference for reviewing the foundations introduced in Level 1, including the Express application structure, routes, responses, request data, and development workflow.

## Table of Contents

- [Level 1](#level-1)

## Level 1

Level 1 establishes the foundations of an **Express application** and connects them to the HTTP concepts introduced previously. Express provides higher level APIs for organizing request and response handling while preserving the same underlying HTTP model.

An Express application begins by importing Express, creating the application object with `express()`, and starting the server with `app.listen()`.

```js
import express from "express";

const app = express();

app.get("/health", (req, res) => {
  res.send("OK");
});

app.listen(3000, () => {
  console.log("Server is running on http://localhost:3000");
});
```

The application object, conventionally stored in `app`, is the central object used to register request handling behavior and start the server. A request such as `GET /health` is matched to a registered route, its handler runs, and the handler sends a response.

A **route** associates an HTTP method, a path, and a handler. Express provides methods such as `app.get()`, `app.post()`, `app.put()`, `app.patch()`, and `app.delete()` for registering routes that respond to different HTTP methods.

```js
app.get("/users", (req, res) => {
  res.send("Users");
});

app.post("/users", (req, res) => {
  res.send("Create user");
});
```

Express matches both the HTTP method and the path. `GET /users` and `POST /users` can therefore use the same path while representing different operations. The application method determines which request can reach the route, while the **route handler** contains the logic that runs after a match and receives `req` and `res`.

The `res` object provides methods for constructing and sending responses. `res.send()` sends general response content, `res.json()` sends JSON data, and `res.status()` sets the HTTP status code. Express also provides methods such as `res.sendFile()`, `res.download()`, and `res.redirect()` for other common response operations.

```js
app.get("/users", (req, res) => {
  res.json([{ id: 1, name: "Mantas" }]);
});

app.get("/missing", (req, res) => {
  res.status(404).send("Not Found");
});
```

`res.status()` only changes the response status and does not send the response by itself. A sending method such as `res.send()` or `res.json()` is still required to complete the response.

Incoming request data is available through the `req` object. **Route parameters** are captured from variable parts of a route path and are available through `req.params`. **Query string values** are available through `req.query`. Values captured from URLs should not be assumed to have the application type they appear to represent. For example, the `42` captured from `/users/42` is initially a string and can be converted with `Number()` when a numeric value is required.

```js
app.get("/users/:id", (req, res) => {
  const userId = Number(req.params.id);

  res.send(`User ID: ${userId}`);
});

app.get("/users", (req, res) => {
  res.send(`Search: ${req.query.search}`);
});
```

Request bodies provide another source of incoming data. JSON request bodies must be parsed before their contents are available as structured JavaScript data. Express provides the built in `express.json()` middleware for this purpose.

```js
app.use(express.json());

app.post("/users", (req, res) => {
  res.json(req.body);
});
```

When `express.json()` processes a supported JSON request body, the parsed value becomes available through `req.body`. Without an appropriate parser, `req.body` is typically `undefined` for an incoming JSON body. The role of `app.use()` and the middleware request flow are developed separately in **Middleware Level 1**.

Requests that are inconvenient to create through a browser address bar can be tested with an HTTP client such as `curl`. For example, a JSON body can be sent to the `POST /users` route from the command line.

```bash
curl -X POST http://localhost:3000/users \
  -H "Content-Type: application/json" \
  -d '{"name":"Mantas"}'
```

During development, Node.js `--watch` mode can restart the application when relevant source files change. A project can expose this workflow through a development script in `package.json`.

```json
{
  "scripts": {
    "dev": "node --watch app/app.js"
  }
}
```

The server port can also be read from `process.env.PORT` while retaining a local development fallback.

```js
const PORT = process.env.PORT || 3000;

app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});
```

After reviewing Level 1, the main concepts to know are **how an Express application is created and started**, **how HTTP methods and paths are associated with route handlers**, **how handlers use `req` and `res`**, **how common response methods send data and set status codes**, **how route parameters, query strings, and request bodies provide incoming data**, **why JSON request bodies require parsing**, **how `curl` can be used to test HTTP requests**, and **how watch mode, development scripts, and configurable ports support the development workflow**.
