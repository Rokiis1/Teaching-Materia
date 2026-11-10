# Overview

**Token formats and representations** determine how security-related information is organized and made available to software systems. Some representations contain structured claims or statements that receiving systems can interpret directly, while others use opaque values whose meaning must be established through an associated system or service. These differences influence how security information is exchanged, processed, and validated.

Common examples include **opaque tokens**, **Security Assertion Markup Language (SAML) assertions**, and **JSON Web Tokens (JWTs)**. Opaque tokens contain values whose internal meaning is not intended to be interpreted by the receiving party. Their validation may involve consulting an authorization server or session store, depending on the system. SAML assertions use XML-based structures to communicate security statements, particularly between identity providers and applications participating in federated authentication. JWTs provide a compact, JSON-based representation of claims that can be cryptographically protected.

Although these representations may support similar authentication or authorization scenarios, they follow different processing models and security requirements. Their suitability depends on the protocols, trust relationships, and systems involved, and they are not necessarily interchangeable.

The following topics examine each representation in greater detail. [Opaque Tokens](./opaque_tokens/overview.md) explores opaque values and their validation. [SAML Assertions](./saml_assertions/overview.md) introduces XML-based security statements and their use in federated authentication. [JSON Web Tokens (JWTs)](./jwt/overview.md) examines JWT-specific standards, protection mechanisms, and validation requirements.
