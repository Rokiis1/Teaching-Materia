# Summary

This summary brings together the key concepts from the **Token Types** topic, providing a reference for reviewing the purposes, usage, and relationships of common security tokens. It covers the foundations introduced in **Level 1**, alongside the lifecycle management, usage constraints, and security considerations explored in **Level 2**.

## Table of Contents: Token Types Summary

- [Token Types Level 1](#token-types-level-1)
- [Knowledge Check](#knowledge-check)

## Token Types Level 1

**Access tokens**, **session tokens**, **refresh tokens**, and **ID tokens** support different aspects of authentication, authorization, and session management. Although each serves a distinct purpose, several may be used together within the same application.

For example, a website may receive and validate an ID token during an OpenID Connect authentication process, then establish its own application session to recognize the user across subsequent requests. The application may also use access tokens to request protected API resources and, if a refresh token is issued, request replacement access tokens when needed. The following diagram illustrates this possible arrangement.

```mermaid
flowchart TB
    U["User"]
    I["Identity Provider / Authorization Server"]
    C["Client Application"]
    S["Application Session"]
    B["Browser"]
    API["Protected API"]
    D["Access Decision"]

    U -->|"Completes sign-in process"| I
    I -->|"ID token through OIDC process"| C
    I -->|"Access token"| C
    I -.->|"Refresh token, if issued"| C

    C -->|"Creates session, if used"| S
    C -->|"Sets session cookie"| B
    B -->|"Session cookie on later requests"| C
    C -->|"Checks application session"| S

    C -->|"Access token"| API
    API -->|"Validates token and checks permissions"| D

    C -.->|"Refresh token for renewal"| I
    I -.->|"Replacement access token, if approved"| C
```

This example demonstrates how the token types can complement one another without being interchangeable. **ID tokens** communicate authentication information, **session tokens** represent established application sessions, **access tokens** support requests to protected resources, and **refresh tokens** support access-token renewal. Not every application requires all four, and each token must be processed according to its intended purpose and the system's security requirements.

## Knowledge Check

Test your understanding of the key concepts covered in the Token Types topic. Select one answer for each question to receive feedback and an explanation.

<div class="knowledge-check">

  <div class="knowledge-question" data-answer="B" data-explanation="An access token allows a client application to request protected resources. The resource server must validate the token and determine whether the requested operation is permitted.">
    <p><strong>Access Tokens</strong></p>
    <p>How is an access token used when accessing a protected API?</p>
    <div class="quiz-options">
      <button type="button" data-option="A">A. It automatically grants access to every operation supported by the API</button>
      <button type="button" data-option="B">B. It is presented to the API, which validates it and checks whether the requested access is permitted</button>
      <button type="button" data-option="C">C. It is exchanged directly with the browser to establish a server-managed session</button>
      <button type="button" data-option="D">D. It replaces the need for the API to perform authorization checks</button>
    </div>
    <p class="quiz-feedback" role="status" aria-live="polite"></p>
  </div>

  <div class="knowledge-question" data-answer="C" data-explanation="A session token identifies or represents an established application session. In a server-managed session, a session identifier commonly allows the application to locate and validate session information stored on the server.">
    <p><strong>Session Tokens</strong></p>
    <p>What is the role of a session token in a server-managed application session?</p>
    <div class="quiz-options">
      <button type="button" data-option="A">A. It authorizes access to any protected API without further checks</button>
      <button type="button" data-option="B">B. It obtains replacement access tokens from an authorization server</button>
      <button type="button" data-option="C">C. It allows the application to recognize and validate an established session across requests</button>
      <button type="button" data-option="D">D. It communicates an OpenID Connect authentication result to the client application</button>
    </div>
    <p class="quiz-feedback" role="status" aria-live="polite"></p>
  </div>

  <div class="knowledge-question" data-answer="A" data-explanation="A refresh token is presented to an authorization server to request a replacement access token. The authorization server evaluates the renewal request and may approve or reject it.">
    <p><strong>Refresh Tokens</strong></p>
    <p>What happens when a client application uses a refresh token?</p>
    <div class="quiz-options">
      <button type="button" data-option="A">A. It requests a replacement access token from the authorization server, subject to approval</button>
      <button type="button" data-option="B">B. It gains direct access to protected resources without an access token</button>
      <button type="button" data-option="C">C. It automatically receives a new access token regardless of the refresh token's validity</button>
      <button type="button" data-option="D">D. It establishes an application session on the resource server</button>
    </div>
    <p class="quiz-feedback" role="status" aria-live="polite"></p>
  </div>

  <div class="knowledge-question" data-answer="D" data-explanation="An OpenID Connect ID token communicates information about an authenticated user and the authentication event to its intended client application. The client must validate the token before trusting its claims.">
    <p><strong>ID Tokens</strong></p>
    <p>Which statement correctly describes the purpose of an ID token?</p>
    <div class="quiz-options">
      <button type="button" data-option="A">A. It grants the client permission to perform any operation on a protected API</button>
      <button type="button" data-option="B">B. It allows a resource server to renew expired access tokens</button>
      <button type="button" data-option="C">C. It replaces application session management in every authentication system</button>
      <button type="button" data-option="D">D. It communicates authentication information to the intended client application, which must validate it</button>
    </div>
    <p class="quiz-feedback" role="status" aria-live="polite"></p>
  </div>

  <div class="knowledge-question" data-answer="B" data-explanation="Token types have distinct purposes and are not interchangeable. An application may use several token types together, but the combination depends on its architecture and security requirements.">
    <p><strong>Token Types and Their Relationships</strong></p>
    <p>Which statement correctly describes how different token types may be used within an application?</p>
    <div class="quiz-options">
      <button type="button" data-option="A">A. Every application must use all four token types to support authentication</button>
      <button type="button" data-option="B">B. Different token types may work together, but each must be processed according to its intended purpose</button>
      <button type="button" data-option="C">C. Access tokens and session tokens are interchangeable because both can be used across multiple requests</button>
      <button type="button" data-option="D">D. A valid ID token can always replace an access token when requesting protected API resources</button>
    </div>
    <p class="quiz-feedback" role="status" aria-live="polite"></p>
  </div>

</div>
