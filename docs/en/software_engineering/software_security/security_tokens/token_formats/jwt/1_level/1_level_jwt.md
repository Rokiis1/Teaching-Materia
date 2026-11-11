# Level 1

## Table of Contents: JSON Web Tokens (JWT)

- [JWT Structure and Usage](#jwt-structure-and-usage)
- [JWT Claims and Validation Basics](#jwt-claims-and-validation-basics)

**JWT Level 1** examines how JWTs are structured, interpreted, and validated in practice, including the security considerations involved in handling them. The following section introduces JWT structure and usage, explaining how tokens carry information and how applications use them in authentication and authorization workflows.

## JWT Structure and Usage

After a user successfully authenticates, an authentication service may issue a JWT to the client application. The client can then present the token when requesting access to a protected API, which validates the JWT and uses its claims when processing the request. Because the token carries this information directly, the API may not need to retrieve it from a database, although additional lookups may still be required for information that is missing or has changed since the token was issued.

A typical **signed JWT** consists of three components separated by dots (`.`), each serving a different purpose.

| Component     | Description                                                                            |
| ------------- |----------------------------------------------------------------------------------------|
| **Header**    | Contains metadata about the token, including the signing algorithm.                    |
| **Payload**   | Contains claims that describe the token, an entity, or its intended use.               |
| **Signature** | Contains the cryptographic signature associated with the signed header and payload.    |

In its compact representation, a signed JWT follows the structure `encodedHeader.encodedPayload.encodedSignature`. The header and payload contain JSON data converted into text using **Base64url encoding**, allowing them to form part of a compact token suitable for use in HTTP requests. A receiving application can reverse this encoding to read the original JSON data, a process known as **decoding**.

!!! warning "Encoding Is Not Encryption"

    **Base64url encoding does not protect information from being read.** Anyone who obtains a signed, unencrypted JWT can decode its header and payload. Although a signature helps detect unauthorized modifications, it does not hide the contents. Applications should therefore avoid including unnecessary sensitive information in JWT payloads, especially passwords, credentials, or personal information that recipients do not need.

Because the contents of an unencrypted JWT can be read by anyone who obtains it, applications should avoid including unnecessary sensitive information in its payload, particularly passwords, credentials, or personal information that recipients do not need. Beyond understanding how JWTs are structured and used, it is also important to understand the claims they contain and how applications validate those claims before trusting the token.

## JWT Claims and Validation Basics

The information carried in a JWT payload is organized into **claims**, represented as JSON name-value pairs. For example, a document-management API might receive a JWT containing claims that identify its issuer, the associated user, the intended API, and its expiration time, along with an application-specific role.

```json
{
  "iss": "https://auth.example.com",
  "sub": "user_123",
  "aud": "https://api.example.com",
  "exp": 1704070800,
  "role": "reader"
}
```

The following table explains the claims in this example and their significance when processing the token.

| Claim  | Name                       | Purpose                                                                                                         |
| ------ | -------------------------- | --------------------------------------------------------------------------------------------------------------- |
| `iss`  | Issuer                     | Identifies the entity that issued the JWT and allows the application to check whether it is an expected issuer. |
| `sub`  | Subject                    | Identifies the user or entity the token concerns.                                                               |
| `aud`  | Audience                   | Identifies the intended recipient, allowing the application to check whether the token was issued for it.       |
| `exp`  | Expiration time            | Specifies the time at or after which the token must no longer be accepted.                                      |
| `role` | Application-specific claim | Provides role information that may be considered during authorization decisions.                                |

In this example, the `role` value `"reader"` may help the document-management API determine whether `user_123` is permitted to view documents, potentially as part of [Role-Based Access Control (RBAC)](../../../../authorization/rbac/rbac.md). The expiration timestamp `1704070800` corresponds to January 1, 2024, at 01:00:00 UTC, using seconds since January 1, 1970, UTC. However, the presence of these claims does not establish that the JWT can be trusted, making proper cryptographic protection and validation essential.

JWTs can be **signed**, **encrypted**, or both, depending on their security requirements. Signing allows a receiving application to verify that the signed information has not been altered and was protected using the expected signing key, while encryption prevents unauthorized parties from reading the token's contents. These mechanisms serve different purposes and may be combined when both integrity and confidentiality are required.

For a signed JWT, **validation** involves verifying its signature using a trusted key and an allowed algorithm, then checking applicable claims such as `iss`, `aud`, and `exp`. The application must reject the token if any required check fails and ensure that it is being used for its intended purpose. For example, an ID token should not be accepted as an access token simply because both can use the JWT format. Even when validation succeeds, the application must still enforce its authorization rules before permitting the requested operation.

Beyond validation, applications must protect JWTs against **token theft and reuse**. Many JWTs are used as bearer tokens, meaning that someone who obtains a valid token may be able to use it to access protected resources. In web applications, JWTs may be stored in cookies and sent automatically with HTTP requests, or transmitted through an `Authorization` header. Regardless of how they are transmitted, applications should use HTTPS, protect tokens during storage, and avoid exposing them in URLs or logs. When JWTs are stored in cookies, attributes such as `Secure`, `HttpOnly`, and `SameSite` can provide additional protections, although appropriate defenses against cross-site request forgery (CSRF) may still be necessary.

Another important consideration is the lifetime of a JWT. Short-lived tokens reduce the period during which a stolen token can be used, but **expiration does not guarantee immediate invalidation**. Even after a user signs out or their permissions change, a self-contained signed JWT may continue to be accepted until its `exp` time is reached unless the application performs additional revocation or authorization checks. Secure JWT usage therefore requires appropriate validation, token protection, and lifecycle management rather than relying solely on signatures or expiration times.

Building on these fundamentals, [JWT Level 2](../2_level/2_jwt.md) explores JWT construction, cryptographic protection, detailed validation rules, and more advanced security practices.
