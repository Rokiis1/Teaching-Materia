# Level 1

## Table of Contents: HTTP

- [Node.js and HTTP](#nodejs-and-http)
- [Creating an HTTP Server](#creating-an-http-server)
- [Request Object](#request-object)
- [Request URL](#request-url)
- [Response Object](#response-object)
- [Returning Responses](#returning-responses)

In **HTTP Level 1**, you apply the HTTP concepts you already know by creating a basic HTTP API with Node.js. You already know requests, responses, methods, headers covered in the headers module, URLs, and status codes. This level focuses on how those concepts appear in Node.js without adding more complex request handling that frameworks such as Express will simplify later.

## Node.js and HTTP

Node.js includes the built-in `http` module for creating an HTTP server, so no additional package is required.

```js
import http from "node:http";

const server = http.createServer((req, res) => {
  // Handle each incoming request
  res.end("Hello from the API");
});
```

`http.createServer()` creates the server, and its callback runs whenever the server receives a request. The `req` parameter represents the incoming request, while `res` represents the response sent back to the client. This code creates the server but does not start it yet, so the next section completes the server by making it listen for incoming connections.

## Creating an HTTP Server

A server must listen on a **port** before clients can connect to it. The `server.listen()` method starts the server on the specified port, so the previous code can be completed with one additional line.

```js
import http from "node:http";

const server = http.createServer((req, res) => {
  res.end("API is running");
});

// Start the server on port 3000
server.listen(3000);
```

Here, the server listens on port `3000`. After running the file with Node.js, the API is available locally at `http://localhost:3000`.

!!! info "The Server Keeps Running"

    The HTTP server continues listening after it starts so that it can receive more requests. The Node.js process remains active until the server is stopped or the process ends.

Now that the server can receive requests, the next section expands the same server to inspect information about each incoming request.

## Request Object

The **request object**, commonly named `req`, contains information about the incoming HTTP request. At this level, the two most useful properties are `req.method` and `req.url`.

```js
import http from "node:http";

const server = http.createServer((req, res) => {
  // Inspect the incoming request
  console.log(req.method);
  console.log(req.url);

  res.end("Request received");
});

server.listen(3000);
```

`req.method` contains the HTTP method, so a `GET` request gives `"GET"` and a `POST` request gives `"POST"`. `req.url` contains the URL requested by the client. The server can check `req.method` when it needs to respond to a particular type of request.

```js
const server = http.createServer((req, res) => {
  // Respond only to GET requests
  if (req.method === "GET") {
    res.end("GET request received");
    return;
  }

  res.end("Another request received");
});
```

The `return` stops the callback after the response is sent, which prevents the code below the condition from running and attempting to send another response. More complex request data, including reading request bodies manually, is intentionally left for later because the built-in `http` module requires additional event based code, while Express provides a simpler way to work with request bodies.

The method tells the API what kind of operation was requested. The next section uses the other important request property, `req.url`, to identify what the client requested.

## Request URL

`req.url` contains the requested URL as a string. This section assumes the basic URL concepts covered earlier in the URL module. For a request to `/users`, the value of `req.url` is `"/users"`. The method and URL can be checked together when the API needs to identify a particular request.

```js
import http from "node:http";

const server = http.createServer((req, res) => {
  // Handle GET /users
  if (req.method === "GET" && req.url === "/users") {
    res.end("Users");
    return;
  }

  // Handle other requests for now
  res.end("API");
});

server.listen(3000);
```

The condition identifies a `GET` request sent to `/users`. Checking `req.method` and `req.url` with conditions is a basic form of **manual routing**, but the purpose at this level is only to show how Node.js identifies requests. More advanced URL parsing, path parameters, query strings, and larger routing structures are intentionally left for later.

Once the API has identified a request, it needs to construct the response that will be sent back to the client.

## Response Object

The **response object**, commonly named `res`, represents the HTTP response sent back to the client. It can set the status code, set response headers, send data, and complete the response. The same server can apply these response features together.

```js
import http from "node:http";

const server = http.createServer((req, res) => {
  if (req.method === "GET" && req.url === "/users") {
    res.statusCode = 200;
    res.setHeader("Content-Type", "application/json");

    const users = [{ id: 1, name: "Example" }];

    res.end(JSON.stringify(users));
    return;
  }

  res.statusCode = 404;
  res.end("Not Found");
});

server.listen(3000);
```

`res.statusCode` sets the HTTP status code and `res.setHeader()` sets a response header. Here, `application/json` tells the client that the response contains JSON. The `users` variable is a JavaScript array, so `JSON.stringify(users)` converts it into JSON text before it is sent with `res.end()`.

If the array is passed directly to `res.end()` without `JSON.stringify()`, Node.js throws an error because a JavaScript array cannot be sent directly as the response body.

```js
// Incorrect
res.end(users);

// Correct
res.end(JSON.stringify(users));
```

The `res.end()` method sends the response data and completes the response. Every response path must eventually call `res.end()`. If it is not called, the client can continue waiting because the response has not finished.

!!! bug "A Response That Never Ends"

    Forgetting `res.end()` can leave the client waiting for the response to finish.

The response object now provides everything needed for the basic API in this level. The final section applies the same pattern to a few common response results.

## Returning Responses

A response combines the status code, any required headers, and the response body. The following example keeps these pieces together so their relationship is clear.

```js
import http from "node:http";

const server = http.createServer((req, res) => {
  if (req.method === "GET" && req.url === "/text") {
    // Return plain text
    res.statusCode = 200;
    res.setHeader("Content-Type", "text/plain");
    res.end("Hello from the API");
    return;
  }

  if (req.method === "GET" && req.url === "/html") {
    // Return HTML
    res.statusCode = 200;
    res.setHeader("Content-Type", "text/html");
    res.end("<h1>Hello from the API</h1>");
    return;
  }

  if (req.method === "GET" && req.url === "/users") {
    // Return JSON
    res.statusCode = 200;
    res.setHeader("Content-Type", "application/json");
    res.end(JSON.stringify([{ id: 1, name: "Example" }]));
    return;
  }

  // No known request matched
  res.statusCode = 404;
  res.setHeader("Content-Type", "text/plain");
  res.end("Not Found");
});

server.listen(3000);
```

`GET /text` returns plain text with `text/plain`, `GET /html` returns HTML with `text/html`, and `GET /users` returns JSON with `application/json`. JSON values such as objects and arrays must first be converted with `JSON.stringify()`, while text and HTML can be sent directly as strings. If no known request matches, the server returns `404 Not Found`.

The status code, `Content-Type` header, and response body work together to describe and return the response. As an API grows, repeatedly checking `req.method` and `req.url` becomes harder to organize. Express provides a clearer way to define routes and return different types of responses, which makes it the natural next step after this Node.js HTTP foundation.
