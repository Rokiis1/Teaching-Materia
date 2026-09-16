# Overview

**Node.js HTTP** introduces the built-in tools Node.js provides for creating an HTTP server and working directly with HTTP requests and responses. It applies previously learned HTTP concepts such as methods, URLs, headers, status codes, and response bodies in a Node.js application.

The module begins by establishing how the built-in `http` module creates a server and how `server.listen()` allows that server to receive incoming connections. It introduces the request and response objects provided to the server callback and shows how they represent the two main parts of HTTP communication in Node.js.

**Level 1** introduces the **request object** and shows how `req.method` and `req.url` can be used to identify incoming requests. It then introduces the **response object** and shows how to set status codes and headers, send response data, and complete a response with `res.end()`. The level also demonstrates returning common response formats such as plain text, HTML, and JSON while using the appropriate `Content-Type`.

Together, these concepts establish the foundation for handling HTTP directly with Node.js and show how requests are received, inspected, and answered. This foundation prepares for Express, which provides a simpler and more structured way to define routes and handle common HTTP operations as an API grows.
