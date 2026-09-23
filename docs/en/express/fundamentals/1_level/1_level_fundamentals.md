# Level 1

## Table of Contents: Fundamentals

- [From Node HTTP to Express](#from-node-http-to-express)
- [Setting Up the Express Project](#setting-up-the-express-project)
- [Creating and Running the Application](#creating-and-running-the-application)
- [Defining Routes](#defining-routes)
- [Sending Responses](#sending-responses)
- [Reading Request Data](#reading-request-data)
- [Development Workflow](#development-workflow)

**Fundamentals Level 1** begins with the transition from working directly with Node.js HTTP to building the same request and response flow with Express. The focus is on the essential pieces needed to create, run, and interact with a basic Express application before those pieces are explored in greater depth in later topics.

## From Node HTTP to Express

The built-in Node.js `http` module can create HTTP servers directly. As introduced previously, a server can inspect properties such as `req.method` and `req.url`, determine how to handle a request, prepare the response, and finish it with `res.end()`.

```js
import http from "node:http";

const server = http.createServer((req, res) => {
  if (req.method === "GET" && req.url === "/users") {
    res.statusCode = 200;
    res.setHeader("Content-Type", "application/json");
    res.end(JSON.stringify([{ id: 1, name: "Mantas" }]));
    return;
  }

  res.statusCode = 404;
  res.end("Not Found");
});

server.listen(3000);
```

This approach is valid, but method checks, path checks, response headers, serialization, and response completion become increasingly repetitive as an application gains more endpoints. Express provides higher level APIs for organizing the same HTTP work.

```js
// `app` is created in the next section
app.get("/users", (req, res) => {
  res.json([{ id: 1, name: "Mantas" }]);
});
```

The Express version associates `GET /users` directly with a handler, while `res.json()` prepares and sends the JSON response without requiring manual serialization and content type setup. The underlying HTTP concepts remain the same, but Express provides more convenient APIs for working with them.

With the relationship between Node HTTP and Express established, the next step is to set up the Express project.

## Setting Up the Express Project

Express is distributed as a package for Node.js projects. Follow the [official Express installation guide](https://expressjs.com/en/starter/installing.html) for the current installation instructions and use the command appropriate for your chosen package manager. Create and initialize a project named `users_management`, then install Express as a project dependency.

Create an `app` directory in the project root and add `app.js` as the application entry file.

```text
users_management/
├── app/
│   └── app.js
├── package.json
└── node_modules/
```

The examples use ECMAScript modules, which were introduced previously in **Node Modules Level 2**, so `"type": "module"` must be defined in `package.json`.

```json
{
  "name": "users_management",
  "version": "1.0.0",
  "type": "module"
}
```

With Express installed and the entry file prepared, the application can now be created and started.

## Creating and Running the Application

An Express application begins with three pieces. Express is imported, an application object is created, and the application starts listening for requests. The [official Express Hello World guide](https://expressjs.com/en/starter/hello-world.html) demonstrates the same basic structure.

```js
import express from "express";

// Create the Express application
const app = express();

// Register a health check route
app.get("/health", (req, res) => {
  res.send("OK");
});

// Start the server
app.listen(3000, () => {
  console.log("Server is running on http://localhost:3000");
});
```

Calling `express()` creates the **Express application object**, conventionally stored in `app`. This central object is used to register request handling behavior and start the server with `app.listen()`. In this example, `app.listen(3000, callback)` makes the application listen on port `3000`, while the callback runs after the server begins listening and prints a startup message.

The `app.get()` call registers a route and tells Express which handler should run for a matching request. When a browser visits `http://localhost:3000/health`, it sends a `GET` request to `/health`. Express finds the matching route, executes its handler, and sends `OK` back to the browser.

Start the application with `node app/app.js`, then open `http://localhost:3000/health` in a browser. If the browser displays `OK`, the application is running and responding to requests. **Development Workflow** later introduces a convenient watch-mode command for restarting the application automatically as files change. The server continues listening until its process is stopped. Press `Ctrl+C` in the terminal to stop it.

!!! info "Port Already in Use"

    If the application fails to start with an `EADDRINUSE` error, another process is already using the requested port. Stop the process using that port or run the application on a different available port.

!!! success "First Express Request"

    Reaching `/health` successfully confirms the complete basic flow from starting the Express application to matching a route and sending a response.

With the basic application running, the next step is to examine how Express defines routes for different HTTP methods.

## Defining Routes

A route associates an **HTTP method**, a **path**, and a **handler**. Express provides application methods that correspond to HTTP methods, including `app.get()`, `app.post()`, `app.put()`, `app.patch()`, and `app.delete()`. The [official Express routing guide](https://expressjs.com/en/guide/routing.html) documents routing in greater depth.

The common form is `app.METHOD(path, handler)`. `METHOD` represents the HTTP method, `path` identifies where the route is available, and `handler` is the function Express executes when an incoming request matches that method and path. The following routes show the main methods together.

```js
// Retrieve users
app.get("/users", (req, res) => {
  res.send("Users");
});

// Create a user
app.post("/users", (req, res) => {
  res.send("Create user");
});

// Replace or update a user
app.put("/users/1", (req, res) => {
  res.send("Update user");
});

// Partially update a user
app.patch("/users/1", (req, res) => {
  res.send("Update part of user");
});

// Delete a user
app.delete("/users/1", (req, res) => {
  res.send("Delete user");
});
```

`GET` commonly retrieves data, `POST` commonly creates a resource, and `DELETE` commonly removes one. `PUT` and `PATCH` are both used for updates, and the exact behavior depends on how the API is designed. A common convention treats `PUT` as replacing the complete resource representation and `PATCH` as applying a partial modification. In practice, APIs do not always follow that distinction strictly, so the contract defined by the API determines how each method behaves.

These application methods determine which requests can reach a route, while the **route handler** contains the application logic that runs after a match and receives `req` and `res` for working with the incoming request and outgoing response.

!!! info "Method and Path Must Match"

    Express matches a route using both the HTTP method and the path. `GET /users` and `POST /users` can therefore use the same path while handling different operations.

!!! warning "Examples Are Independent"

    Examples in different sections demonstrate specific concepts and are not intended to be pasted into one application unchanged. If the same HTTP method and path are registered more than once and an earlier matching handler completes the response, later matching handlers do not get an opportunity to send another response.

If no registered route handles a request, Express eventually reaches its default 404 handling. During development, requesting an unmatched path may therefore produce a response such as `Cannot GET /path`. Custom not found handling is introduced later in the **Error Handling Level 1**.

For now, it is enough to understand the common route form, the purpose of the main HTTP method specific application methods, and the role of the handler. **Routing Level 1** later expands on routing with route matching, route organization, and `Router` instances.

Once Express selects a route, its handler determines how the application responds.

## Sending Responses

The route handler uses the `res` object to build and send a response. The [official Express response API](https://expressjs.com/en/5x/api.html#res) provides many response methods. At this stage, the most useful ones to recognize are `res.send()`, `res.json()`, `res.status()`, `res.sendFile()`, `res.download()`, and `res.redirect()`.

`res.send()` sends general response content and can be used for simple text, while `res.json()` is intended specifically for JSON data. `res.status()` sets the HTTP status code and is commonly chained with a method that sends the response.

```js
// Send a text response
app.get("/health", (req, res) => {
  res.send("OK");
});

// Send JSON data
app.get("/users", (req, res) => {
  res.json([
    { id: 1, name: "Mantas" },
  ]);
});

// Set a status code and send a response body
app.get("/missing", (req, res) => {
  res.status(404).send("Not Found");
});
```

Express uses `200 OK` by default for a successful response when another status has not been set. HTTP status codes were covered in **Web Fundamentals HTTP Level 1**, and the [HTTP response status code reference](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status) provides the complete categorized list. Here, the focus is only on how Express sets a status with `res.status()`.

Express can also respond with files or direct the client to another location. `res.sendFile()` sends a file, `res.download()` sends a file as an attachment for download, and `res.redirect()` sends a redirect response that tells the client to request another location.

```js
// Send a file to the client
app.get("/document", (req, res) => {
  res.sendFile("/absolute/path/to/document.pdf");
});

// Send a file as a download
app.get("/report", (req, res) => {
  res.download("/absolute/path/to/report.pdf");
});

// Redirect the client to another route
app.get("/home", (req, res) => {
  res.redirect("/users");
});
```

The file paths above are placeholders that demonstrate the response methods. Real applications should construct paths appropriate to their project structure.

!!! info "Setting a Status Does Not Send the Response"

    `res.status()` changes the HTTP status code but does not send the response by itself. A method such as `res.send()` or `res.json()` is still needed to complete the response.

These methods cover several common response forms without requiring every response detail to be configured manually. The next section examines the incoming request and the data available through `req`.

## Reading Request Data

Express exposes incoming request information through the `req` object, and the [official Express request API](https://expressjs.com/en/5x/api.html#req) documents the complete API. At this stage, the main request data sources to recognize are route parameters, query strings, and request bodies.

A **route parameter** captures a value from a variable part of the route path. A parameter is written with `:` in the path and its captured value is available through `req.params`. A **query string** supplies additional values after `?` in the URL and Express exposes those values through `req.query`.

```js
// Read a route parameter
// /users/42 makes req.params.id contain "42"
app.get("/users/:id", (req, res) => {
  const userId = Number(req.params.id);

  res.send(`User ID: ${userId}`);
});

// Read a query string value
// /users?search=Mantas makes req.query.search contain "Mantas"
app.get("/users", (req, res) => {
  res.send(`Search: ${req.query.search}`);
});
```

Values captured from a URL should not be assumed to have the application type they appear to represent. The `42` in `/users/42`, for example, is available through `req.params.id` as the string `"42"`. If the application needs a number, it must convert the value with an operation such as `Number(req.params.id)`. Real applications should also validate values before relying on them.

Clients can also send data in the **request body**. As introduced in **Node.js HTTP Level 1**, JSON sent through HTTP is text-based data and must be parsed before JavaScript can work with it as structured data. Express provides the built-in `express.json()` middleware for this purpose.

```js
// Parse JSON request bodies before the routes handle them
app.use(express.json());

app.post("/users", (req, res) => {
  res.json(req.body);
});
```

Passing `express.json()` to `app.use()` registers it as application-level middleware for routes registered after it. When a supported JSON request body arrives, Express parses it and makes the resulting JavaScript value available through `req.body`.

!!! info "Without JSON Parsing"

    Without `express.json()` or another appropriate parser, `req.body` is typically `undefined` for an incoming JSON body. Trying to access a property such as `req.body.name` can then cause a `TypeError`.

A browser address bar is convenient for trying simple `GET` requests, but methods such as `POST` and requests with JSON bodies require an HTTP client. [`curl`](https://curl.se/docs/manpage.html) is a command-line tool that can send HTTP requests directly from the terminal. For example, the `POST /users` route above can be tested by sending a JSON request body.

```bash
curl -X POST http://localhost:3000/users \
  -H "Content-Type: application/json" \
  -d '{"name":"Mantas"}'
```

In this command, `-X` specifies the HTTP method, `-H` adds a request header, and `-d` supplies data for the request body.

The line-ending `\` characters split the command across multiple lines in shells that support this syntax. In Windows Command Prompt, write the same command on a single line instead.

```bat
curl -X POST http://localhost:3000/users -H "Content-Type: application/json" -d "{\"name\":\"Mantas\"}"
```

This example is enough to use `curl` for a simple request. Additional commands and options can be explored later when working with command-line tooling. **Middleware Level 1** explores `app.use()`, application-level middleware, execution order, and the middleware request flow in greater depth.

!!! info "Without JSON Parsing"

    Without `express.json()` or another appropriate parser, `req.body` is typically `undefined` for an incoming JSON body. Trying to access a property such as `req.body.name` can then cause a `TypeError`.

With the basic request and response flow established, the application has the essential pieces needed to handle simple HTTP requests. The final step is to make the development workflow more convenient while the application is being changed and tested.

## Development Workflow

During development, source files change frequently, so restarting the application manually after every change quickly becomes inconvenient. Node.js provides a built-in [watch](https://nodejs.org/api/cli.html#--watch) mode that monitors the entry point and its dependencies and restarts the application when relevant files change. [nodemon](https://www.npmjs.com/package/nodemon) provides a similar workflow with additional control over file watching and restart behavior. For this project, Node’s built-in `--watch` mode is sufficient because it requires no additional package or watch configuration.

The server port should also remain configurable rather than being fixed directly in the source code. Since `process.env` was introduced previously, the application can read a supplied port while keeping `3000` as a development fallback.

```js
const PORT = Number(process.env.PORT) || 3000;

app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});
```

A development script in `package.json` provides a short and consistent way to start the application in watch mode.

```json
{
  "scripts": {
    "dev": "node --watch app/app.js"
  }
}
```

The name `dev` is a project convention rather than a special script name required by Node.js. Teams may choose `dev`, `develop`, or another name that fits their conventions, but the chosen name should be clear and used consistently. This project uses `dev` for running the application during development.

!!! info “Related Topics Are Covered Separately”

    This section focuses on the development workflow for an Express application. Environment variables, configuration files, credentials, environment-specific settings, and production startup concerns are covered in **Environment and Configuration Level 1**.

At this point, the application has the foundation needed for further Express work. You can create and run an Express application, associate HTTP methods and paths with handlers, send common responses, read basic request data, and use a convenient development workflow. The next Express topic, **Routing Level 1**, builds on this foundation by exploring route matching, route parameters, route organization, and `Router` instances in greater depth.
