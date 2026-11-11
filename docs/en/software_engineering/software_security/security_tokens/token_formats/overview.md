# Overview

**Token formats and representations** describe how security-related information is structured and exchanged between software systems. While token types describe the purpose a token serves, its format determines how the information is represented and how receiving systems can interpret or process it. Different formats may carry information directly or rely on another system to establish its meaning.

The choice of representation affects how tokens are handled, validated, and integrated into authentication and authorization workflows. However, a token's format does not independently determine its purpose or how it should be trusted. These considerations also depend on the protocols, applications, and security requirements involved.

This section introduces three common representations, including [Opaque Tokens](./opaque_tokens/overview.md), [SAML Assertions](./saml_assertions/overview.md), and [JSON Web Tokens (JWTs)](./jwt/overview.md). Each topic explores its respective structure, characteristics, and role in security systems.
