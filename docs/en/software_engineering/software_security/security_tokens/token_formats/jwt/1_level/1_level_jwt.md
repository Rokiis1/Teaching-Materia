# Level 1

## Table of Contents: JSON Web Tokens (JWT)

- [JWT Structure and Usage](#jwt-structure-and-usage)
- [JWT Claims](#jwt-claims)
- [JWT Protection and Validation Basics](#jwt-protection-and-validation-basics)
- [JWT Security Basics](#jwt-security-basics)

**JWT Level 1** focuses on the practical structure and usage of JSON Web Tokens. The following sections examine how JWTs are organized and exchanged between systems, how claims are interpreted, and how cryptographic protection and validation contribute to their secure use. Common security risks and considerations are also introduced.

## JWT Structure and Usage

JWTs can carry information directly within the token, allowing receiving systems to evaluate claims without necessarily retrieving them from a separate data source. For example, after a user successfully authenticates, an authentication service may issue a JWT to a client. The client can then present the token when requesting a protected resource from an API. The API validates the token, determines whether it is appropriate for the request, and applies its authorization rules. Depending on the application's requirements, additional checks or data lookups may still be necessary.

A typical **signed JWT** consists of three components separated by periods (`.`). These components are the **header**, **payload**, and **signature**, each serving a distinct purpose.

| Component     | Description                                                                                                                                      |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Header**    | Contains metadata describing the token, such as the algorithm used for cryptographic protection.                                                 |
| **Payload**   | Contains claims describing an entity or the token's intended use.                                                                                |
| **Signature** | Contains cryptographic data used to verify the integrity of the signed content and confirm that it was protected using the expected signing key. |

In its compact representation, a signed JWT follows the structure `encodedHeader.encodedPayload.encodedSignature`. The header and payload contain JSON data that is converted into a **Base64url-encoded representation** when constructing a signed JWT. This encoding represents the data using characters suitable for URLs and HTTP transmission. When a receiving application obtains the token, it can reverse the encoding to recover the original header and payload. This process is called **decoding**.

!!! warning "Encoding Is Not Encryption"

    Base64url encoding changes how information is represented but does not keep it secret. Anyone who obtains a signed, unencrypted JWT can decode its header and payload and read their contents. The signature helps detect unauthorized modifications but does not conceal the claims.

The **payload** contains the JWT's claims, which describe an entity, the token itself, or its intended use. Understanding these claims is essential because they provide the information that receiving applications evaluate when processing a token.

## JWT Claims

A **claim** is a JSON name-value pair contained in the JWT payload. Claims provide information about who issued the token, which user or entity it represents, which application or service should accept it, and how long it remains valid. The following table introduces four commonly used registered JWT claims.

| Claim | Name            | Description                                                                    |
|-------|-----------------|--------------------------------------------------------------------------------|
| `iss` | Issuer          | Identifies the entity that issued the JWT, such as an authentication service.  |
| `sub` | Subject         | Identifies the user or entity the token concerns.                              |
| `aud` | Audience        | Identifies the intended recipient, such as an API that manages documents.      |
| `exp` | Expiration time | Specifies the time at or after which the JWT must no longer be accepted.       |

The following example represents a JWT payload issued for a user accessing a document-management API. Alongside the registered claims, it includes a `role` claim to provide additional information about the user.

```json
{
  "iss": "https://auth.example.com",
  "sub": "user_123",
  "aud": "https://api.example.com",
  "exp": 1704070800,
  "role": "reader"
}
```

In this example, `iss` identifies the authentication service, `sub` identifies the user as `user_123`, and `aud` identifies the intended API. The `exp` claim specifies the expiration time using a numeric timestamp representing seconds since January 1, 1970, UTC. Its value, `1704070800`, corresponds to January 1, 2024, at 01:00:00 UTC and is included for illustration. The `role` claim indicates that the application has assigned the user a `"reader"` role.

Claims may also support authorization mechanisms such as **[Role-Based Access Control (RBAC)](../../../../authorization/rbac/rbac.md)**. For example, the document-management API might use the `"reader"` role when determining whether `user_123` can view a document. However, the presence of this role does not automatically grant access, since the application must validate the JWT and enforce its authorization policies. Before claims can be used in such decisions, the receiving system must establish that the token is trustworthy and intended for its use. This requires understanding how JWTs are protected and validated.

## JWT Protection and Validation Basics

JWTs can use **signing**, **encryption**, or both to protect their contents. Signing allows a receiving system to verify that the signed information has not been modified and was protected using a trusted key, while encryption prevents parties without the appropriate decryption key from reading the contents. These mechanisms serve different purposes. A signed JWT can be authentic without being confidential, and successfully decrypting an encrypted JWT does not necessarily establish who originally issued it.

Decoding a JWT only reveals its contents, but it does not establish whether those contents can be trusted. To determine whether a JWT can be trusted and accepted, the receiving application must **validate the token** according to its security requirements. For a signed JWT, this involves verifying its cryptographic signature and checking claims that establish its origin, intended recipient, and validity period.

The following table summarizes common validation checks performed when an API receives a signed JWT.

| Basic check                    | Purpose                                                                                                                                |
|------------------------------- |--------------------------------------------------------------------------------------------------------------------------------------- |
| **Cryptographic verification** | Checks that the JWT's signature is valid using a trusted key, such as a shared secret or public key, and an allowed signing algorithm. |
| **Issuer (`iss`)**             | Confirms that the token comes from an expected issuer.                                                                                 |
| **Audience (`aud`)**           | Confirms that the token is intended for the receiving API.                                                                             |
| **Expiration (`exp`)**         | Rejects the token when its expiration time has been reached.                                                                           |

A JWT must be rejected if any required validation check fails, even if the remaining checks succeed. It must also be appropriate for its intended purpose. For example, an ID token should not be accepted as an access token simply because both use the JWT format. Successful validation establishes that the token meets the receiving application's acceptance requirements, while authorization determines which operations the application permits.

## JWT Security Basics

Although JWTs provide a standardized format for exchanging claims, their security depends on how applications handle them. Signing and encryption provide important protections, but they do not eliminate risks involving token exposure, theft, expiration, or misuse. Applications should therefore avoid including unnecessary sensitive information in JWT payloads, especially passwords, credentials, or personal data that recipients do not need.

Another important risk is **token theft and reuse**. Many JWTs are used as bearer tokens, meaning anyone who possesses a valid token may be able to use it to access protected resources. Applications should protect tokens during transmission using HTTPS, handle them securely during storage, and avoid exposing them in URLs or logs. Short-lived tokens can also reduce the period during which a stolen token remains usable.

**Expiration** limits how long a JWT may be accepted, but it does not necessarily provide immediate invalidation. A self-contained signed JWT may continue to pass signature and expiration checks after a user signs out or their permissions change. Unless the application implements additional revocation or authorization checks, it may continue accepting the token until it expires.

JWTs must also be accepted only in the context for which they were issued. A token intended for one API or purpose should not automatically be accepted by another. **JWT security depends on correct validation and responsible token handling**, not simply on the presence of a signature or an expiration claim.

These concepts provide the foundation for more detailed JWT processing and security practices. [JWT Level 2](../2_level/2_jwt.md) examines JWT construction, cryptographic protection, detailed validation rules, and advanced security considerations.
