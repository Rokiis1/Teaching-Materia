# Overview

Defined by [RFC 7519](https://www.rfc-editor.org/rfc/rfc7519), **JSON Web Tokens (JWTs)** follow standardized rules for representing and processing claims. JWTs can be digitally signed or protected using a message authentication code to support integrity verification and authentication of their origin. They can also be encrypted to protect the confidentiality of their contents. The protection mechanism determines how a receiving system processes and validates the token.

A JWT defines a **token format**, not a particular security purpose. For example, an OAuth 2.0 access token may use the JWT format, while an OpenID Connect ID token uses JWT to communicate authentication information to a client application. Although these tokens share a representation, they have different intended recipients, processing rules, and validation requirements. A JWT must therefore be evaluated according to the protocol and security context in which it is used.

This topic is organized into two levels. [Level 1](./1_level/1_level_jwt.md) introduces JWT structure, claims, protection, validation basics, and common security considerations through practical examples. [Level 2](./2_level/2_jwt.md) provides a more detailed examination of encoding, construction, claim processing, cryptographic mechanisms, and validation requirements.
