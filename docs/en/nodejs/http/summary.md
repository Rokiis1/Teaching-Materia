# Summary

This summary brings together the most important concepts from **Node.js HTTP**. It is designed as a quick reference for reviewing what should be understood from Level 1, including how to create an HTTP server, inspect incoming requests, construct responses, and return different types of response data.

## Table of Contents: HTTP

- [Level 1](#level-1)

## Level 1

Level 1 establishes the foundations of **Node.js HTTP servers, ports, request objects, request methods, request URLs, response objects, status codes, response headers, response bodies, and response completion**. The main goal is to understand how the HTTP concepts learned earlier appear when working directly with Node.js.

Node.js provides the built-in `http` module for creating an HTTP server. `http.createServer()` creates the server and receives a callback that runs for every incoming request. The callback receives two important objects. `req` represents the incoming request and `res` represents the response that will be returned to the client.

```js
import http from "node:http";

const server = http.createServer((req, res) => {
  res.end("Hello from the API");
});

server.listen(3000);
```

Creating the server does not make it available to clients by itself. `server.listen()` starts the server on a **port**. For example, `server.listen(3000)` allows the server to receive connections on port `3000`, making it available locally at `http://localhost:3000`. The server continues running and listening for requests until it is stopped or the Node.js process ends.

The **request object**, commonly named `req`, contains information about an incoming HTTP request. Two important properties at this level are `req.method` and `req.url`. `req.method` identifies the HTTP method, such as `"GET"` or `"POST"`, while `req.url` contains the requested URL as a string.

```js
if (req.method === "GET" && req.url === "/users") {
  res.end("Users");
  return;
}
```

Checking `req.method` and `req.url` together allows the server to identify a particular request. This is a basic form of **manual routing**. The `return` statement stops the callback after the response has been sent so that execution does not continue into code intended for another response.

The **response object**, commonly named `res`, is used to construct and return the HTTP response. `res.statusCode` sets the response status code, `res.setHeader()` sets a response header, and `res.end()` sends the final response data and completes the response.

```js
res.statusCode = 200;
res.setHeader("Content-Type", "application/json");
res.end(JSON.stringify([{ id: 1, name: "Example" }]));
```

The `Content-Type` header identifies the type of content being returned. Common examples at this level include `text/plain` for plain text, `text/html` for HTML, and `application/json` for JSON. Plain text and HTML can be sent as strings, while JavaScript objects and arrays must be converted to JSON text with `JSON.stringify()` before they are passed to `res.end()`.

```js
// Plain text
res.setHeader("Content-Type", "text/plain");
res.end("Hello from the API");

// HTML
res.setHeader("Content-Type", "text/html");
res.end("<h1>Hello from the API</h1>");

// JSON
res.setHeader("Content-Type", "application/json");
res.end(JSON.stringify({ message: "Hello from the API" }));
```

Passing a JavaScript object or array directly to `res.end()` without `JSON.stringify()` causes an error because it has not been converted into response data that can be sent as JSON.

```js
const users = [{ id: 1, name: "Example" }];

// Incorrect
res.end(users);

// Correct
res.end(JSON.stringify(users));
```

Every response must eventually be completed with `res.end()`. If the server sets a status code or headers but never completes the response, the client can continue waiting because Node.js has not finished sending the response.

Status codes describe the result of the request. In the examples from Level 1, `200` represents a successful response, `201` represents successful resource creation, and `404` indicates that no known request matched. The status code, response headers, and response body work together to form the response returned to the client.

A basic Node.js HTTP server therefore follows a simple flow. The server listens for a request, Node.js provides the request and response objects, the server inspects information such as `req.method` and `req.url`, the response is constructed with the appropriate status code and headers, and `res.end()` sends and completes the response.

After reviewing Level 1, the main concepts to know are **how the built-in `http` module creates an HTTP server**, **what `server.listen()` and a port do**, **the roles of `req` and `res`**, **how `req.method` and `req.url` identify requests**, **what basic manual routing means**, **why `return` is used after completing a response inside a condition**, **how `res.statusCode` and `res.setHeader()` construct response information**, **how `Content-Type` describes plain text, HTML, and JSON responses**, **why JavaScript objects and arrays need `JSON.stringify()` before being returned as JSON**, **why every response must be completed with `res.end()`**, and **how status codes such as `200`, `201`, and `404` describe common response results**.
