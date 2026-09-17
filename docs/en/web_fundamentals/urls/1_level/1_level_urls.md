# Level 1

## Table of Contents: URLs

- [What Is a URL](#what-is-a-url)
- [URL Structure](#url-structure)
- [Paths and Parameters](#paths-and-parameters)

**URLs Level 1** introduces the structure of web addresses and explains how URLs identify destinations and resources. The focus is on the main parts of a URL, how paths identify resources, and when path parameters and query parameters are used.

## What Is a URL

A **URL (Uniform Resource Locator)** is an address used to identify and access a resource on the web. In the previous module, DNS was introduced as the system that helps a client locate a destination from its domain name. A URL builds on that idea by describing where a resource is located and which resource the client wants to access. For example, `https://example.com/users/42?view=profile` contains several parts that contribute to the complete address.

Understanding those parts makes it easier to see how a client identifies both a destination and a resource. The next section examines the structure that gives each part of a URL its role.

## URL Structure

A web URL can contain a **scheme**, **domain**, **port**, **path**, **query string**, and **fragment**. These components follow a general structure written as `{scheme}://{domain}:{port}/{path}?{query}#{fragment}`, where each value in braces represents a placeholder for the corresponding part of the URL. For example, in `https://example.com:443/users/42?view=profile#details`, `https` is the scheme, `example.com` is the domain, `443` is the port, `/users/42` is the path, `view=profile` is the query string, and `details` is the fragment. A **fragment** is the part that begins after `#` and identifies a specific location or section within the resource for the client, such as a heading on a web page.

The **scheme** indicates how the resource is accessed. Web URLs commonly use `http` or `https`. The **domain** identifies the named destination that DNS can resolve to an IP address, while the **port** identifies a communication endpoint on that destination. HTTP uses port `80` by default and HTTPS uses port `443` by default, so these port numbers are normally omitted. For example, `https://example.com` normally uses port `443` without displaying `:443`.

The **path** identifies a resource or location within the application, while the **query string** can provide additional values for the request. The **fragment** identifies a location within the resource for the client, such as a section of a web page. Unlike the other parts used to request the resource, the fragment is not sent to the server as part of the HTTP request. Instead, the browser handles it on the client.

Not every URL contains all of these components. Ports are commonly omitted because default values are available, while paths, query strings, and fragments can take different forms or be absent from the visible address. URLs can also contain encoded characters such as `%20`. This is known as **URL encoding** and is explored in **URLs Level 2**.

The structure shows how the individual parts of a URL work together to identify a destination and resource. The next section focuses on paths and parameters, including how applications use them to identify resources and provide additional request options.

## Paths and Parameters

The **path** appears after the domain and optional port and identifies a resource or location within a website or application. In `https://example.com/users/42/posts`, the path is `/users/42/posts`, which contains the segments `users`, `42`, and `posts` separated by `/`. When a URL such as `https://example.com` does not show a path, it targets the site's **root path**, written as `/`. Paths do not have to represent physical folders or files because an application can interpret them through its routing and application logic.

A path can be fixed, such as `/about`, or contain a variable value that identifies a particular resource. Frameworks commonly represent these variable parts as **path parameters**. For example, Express can define `/users/:id`, where `:id` is a placeholder for a user identifier. A request to `/users/42` supplies `42` as the value. The `:id` notation is a framework convention rather than URL syntax itself, and other frameworks may use forms such as `{id}`. The actual URL contains the real value rather than the placeholder.

**Query parameters** are used when additional values provide options rather than forming part of the resource path. They appear in the **query string**, which begins after `?`, and commonly follow a `key=value` form. In `https://example.com/products?category=books`, `category=books` could be used to filter the requested products. Multiple query parameters are separated by `&`, so `https://example.com/products?category=books&sort=price` could filter products by category and sort the results by price. The application determines the meaning and behavior of each parameter.

A useful distinction is that **path parameters commonly identify a resource**, while **query parameters commonly modify or narrow a request**. In `/users/42/posts?sort=newest`, `42` helps identify whose posts are requested, while `sort=newest` controls how those posts are ordered. This distinction provides a practical foundation for reading URLs without introducing framework-specific routing details too early.

With paths and parameters established, the main parts of a URL are complete. The next module examines **HTTP**, which defines how clients and servers exchange requests and responses.
