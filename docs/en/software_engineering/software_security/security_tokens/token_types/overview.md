# Overview

**Token types** classify security tokens according to their intended purpose within authentication, authorization, and session management systems. Each type has a specific role, determining how it should be used, which systems are expected to receive it, and what requirements apply when processing it.

Common types include **access tokens**, **ID tokens**, **refresh tokens**, and **session tokens**. Access tokens are presented when requesting access to protected resources, while ID tokens communicate information about an authentication event and the authenticated user to an intended client application. Refresh tokens allow clients to obtain new access tokens, subject to applicable protocol and security requirements. Session tokens identify or represent established sessions, allowing applications to maintain continuity across requests.

These token types may be used together within the same software system, but their intended recipients, usage constraints, validity requirements, and security considerations differ. Their relationships depend on the authentication, authorization, and session management mechanisms involved. **Tokens intended for different purposes are not interchangeable.**

This topic is organized into two levels. [Level 1](1_level/1_token_types.md) examines when tokens are issued, which systems receive and process them, and how they support common application workflows through practical examples. [Level 2](2_level/2_token_types.md) explores their relationships, lifecycle differences, usage constraints, and security considerations in greater depth.
