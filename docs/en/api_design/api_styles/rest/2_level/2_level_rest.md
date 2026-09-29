# Level 2

## Table of Contents: REST

- [Designing Responses and Errors](#designing-responses-and-errors)
- [Idempotent and Safe Operations](#idempotent-and-safe-operations)
- [Designing Collection Operations: Pagination, Filtering, and Sorting](#designing-collection-operations-pagination-filtering-and-sorting)
- [Versioning and Evolving an API](#versioning-and-evolving-an-api)

**REST Level 2** builds on the resource-oriented design introduced in **REST Level 1**, focusing on the parts of the API contract that determine how consumers interpret results, retry operations, work with large collections, and adapt when the API changes over time.

## Designing Responses and Errors

HTTP status codes provide the general outcome of a response and were introduced earlier in Web Development. This section builds on that HTTP knowledge rather than repeating the individual status codes. The focus here is on how a REST API designs the rest of the response contract, including the structure of successful representations and consistent error representations.

!!! info "HTTP response references"

    For the definitions and semantics of individual status codes, see the [MDN HTTP response status codes documentation](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status). For the standardized HTTP semantics behind status codes and methods, see [RFC 9110](https://www.rfc-editor.org/rfc/rfc9110.html). These references complement the HTTP material introduced in Web Development, while this section focuses on REST response design.

A successful response should return the information appropriate for the operation. When a representation is returned, its structure should be consistent and expose the fields consumers need without revealing unnecessary implementation details. The names, types, and meanings of those fields form part of the API contract, so consumers should be able to rely on the same conventions across related resources.

```json
{
  "id": 42,
  "name": "Wireless Mouse",
  "price": 29.99,
  "available": true
}
```

For example, if `price` is defined as a number representing the product price, that meaning should remain consistent wherever the field appears. Some successful operations do not need to return a representation. In those cases, the response can communicate success without an unnecessary body. The important design principle is that consumers should be able to predict the response structure and meaning for each operation.

Errors require the same consistency. A status code communicates the broad category of the result, while an **error representation** provides the information consumers need to understand and handle the specific problem. A consistent structure can include a machine-readable error code for consumer logic and a human-readable message explaining the problem.

```json
{
  "error": {
    "code": "INVALID_PRODUCT_PRICE",
    "message": "The product price must be greater than zero."
  }
}
```

When more context is needed, the same error structure can include additional details. Validation errors, for example, can identify which input caused each problem without changing the overall error format.

```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "The request contains invalid data.",
    "details": [
      {
        "field": "price",
        "message": "The price must be greater than zero."
      }
    ]
  }
}
```

The API should keep the meaning and structure of fields such as `code`, `message`, and `details` consistent across operations. This lets consumers handle errors predictably instead of implementing a different interpretation for every operation.

!!! info "Standardized error details"

    For APIs that want a standardized HTTP error format, [RFC 9457](https://www.rfc-editor.org/rfc/rfc9457.html) defines **Problem Details for HTTP APIs**. An API can use a standard format or define its own consistent error representation according to its requirements.

!!! info "Responses are part of the contract"

    Consumers can depend on response fields, data types, error codes, and error structures. Changing or removing these elements can therefore affect existing consumers even when the resource identifier and HTTP method remain unchanged.

Public responses should contain information that is useful to consumers without exposing unnecessary implementation details. In particular, database errors, stack traces, internal file paths, and similar diagnostics should remain internal. When a public error needs to be connected to provider logs for troubleshooting, the API can return a request or correlation identifier instead of exposing those diagnostics directly.

A well-designed response contract therefore gives consumers predictable information in both successful and unsuccessful interactions. Once those outcomes are defined consistently, the next design question concerns how operations behave when requests are repeated, especially when a failure leaves the consumer uncertain about whether an operation completed.

## Idempotent and Safe Operations

When a consumer sends a request, the request may sometimes need to be repeated because a connection fails, a response is lost, or the consumer times out before knowing whether the provider completed the operation. HTTP method semantics help the consumer understand what repeating that request can do.

Consider `DELETE /products/{productId}`. The first successful request removes the product. If the same request is sent again, there is no additional product to remove. A later request may return `404 Not Found`, but the intended resource state remains the same because the product is absent after the first successful deletion and remains absent after repeated requests. An operation with the same intended effect on resource state when repeated is **idempotent**.

A typical `POST /products` behaves differently. One request can create one product, while repeating the same creation request can create another product. Because repeating the operation can cause an additional state change, a typical resource-creation `POST` is **not idempotent**. Idempotency therefore concerns the effect of repeating an operation on resource state, not whether repeated requests return identical responses.

A **safe operation** is intended to retrieve information without requesting a change to resource state. For example, `GET /products/{productId}` retrieves a product, and repeating it requests the information again without asking the provider to change the product. Safe operations are therefore also idempotent. An idempotent operation does not have to be safe. `DELETE` is not safe because it changes resource state, but it is idempotent because repeating the same deletion is still intended to leave the resource absent.

| HTTP method | Safe | Idempotent     | Typical REST use                                                   |
|-------------|------|----------------|--------------------------------------------------------------------|
| `GET`       | Yes  | Yes            | Retrieve a resource or collection                                  |
| `POST`      | No   | No             | Create a resource or perform another non-idempotent operation      |
| `PUT`       | No   | Yes            | Replace or update a resource according to the API contract         |
| `PATCH`     | No   | Not guaranteed | Partially update a resource                                        |
| `DELETE`    | No   | Yes            | Remove a resource                                                  |

These properties are especially important when requests need to be retried. If the consumer loses the response to an idempotent operation such as `DELETE /products/{productId}`, repeating the request is intended to leave the resource in the same state. If the response to a typical `POST /products` is lost, repeating the request can create another product because the consumer may not know whether the first request already succeeded.

!!! warning "Retries require operation semantics"

    A failed response or interrupted connection does not always mean that the operation failed. The provider may have completed the operation before the connection was lost. Consumers should therefore consider whether an operation is idempotent before automatically repeating it.

Safe and idempotent semantics describe how individual operations behave when they are performed or repeated. Collections introduce another concern because consumers may need to work with many resources without retrieving the entire collection at once.

## Designing Collection Operations: Pagination, Filtering, and Sorting

Collection operations let consumers work with large groups of resources without retrieving the entire collection in one response. **Pagination** controls how much of the collection is returned, **filtering** determines which resources belong in the result set, and **sorting** determines the order of those resources. These controls are commonly expressed through query parameters because they change how a collection is returned without changing the identity of the collection.

**Pagination** divides a collection into smaller result sets. The appropriate approach depends on how consumers navigate the collection, its size, and how frequently its contents change.

| Method           | Example                | Commonly used when                              | Main trade-off                                                                      |
|------------------|------------------------|-------------------------------------------------|-------------------------------------------------------------------------------------|
| Offset and limit | `?offset=20&limit=10`  | APIs need simple sequential data retrieval      | Large offsets can become inefficient, and changing data can shift results           |
| Page based       | `?page=2&per_page=10`  | User interfaces display numbered pages          | Results can shift between requests when the collection changes                      |
| Cursor based     | `?cursor=abcdef123456` | Large or frequently changing collections        | More complex to implement and does not naturally support jumping to arbitrary pages |

Offset and limit pagination is useful when consumers need simple control over how many resources are skipped and returned, such as `GET /products?offset=20&limit=10`. Page-based pagination is useful for interfaces with numbered pages, where `GET /products?page=2&per_page=10` requests the second page containing up to 10 products. Cursor-based pagination is useful for large or frequently changing collections, where a request such as `GET /products?cursor=abcdef123456` continues from a position identified by the provider. Unlike offset and page-based approaches, cursor pagination does not depend on a numerical position that can shift as resources are added or removed.

Pagination responses should provide enough information for consumers to understand the current result and continue navigating the collection. Depending on the approach, this can include a next cursor, navigation links, the current page, page size, or total number of resources.

```json
{
  "items": [
    {
      "id": 42,
      "name": "Wireless Mouse"
    }
  ],
  "pagination": {
    "page": 2,
    "perPage": 10,
    "total": 47
  }
}
```

Here, `page` tells the consumer which page was returned, `perPage` describes the page size, and `total` tells the consumer how many resources exist in the collection. The consumer can use this information to determine whether more results remain, calculate how many pages are available, build page navigation, and request the next or previous set of resources. Pagination information can also be provided through response headers, such as a `Link` header containing links to other pages or `X-Total-Count` containing the total number of resources. Whether this information appears in the response body or headers, it gives the consumer the information needed to navigate through the collection.

**Filtering** narrows a collection to resources that match specified conditions. For example, `GET /products?category=electronics` returns products from one category, while `GET /products?category=electronics&available=true` combines multiple conditions. The API contract should define the available filter names, accepted values, and how multiple filters are interpreted.

**Sorting** controls the order of the resources in the result set. An API can use `GET /products?sort=price` for ascending price and `GET /products?sort=-price` for descending price, or use separate parameters such as `GET /products?sort=price&order=desc`. Whichever convention is chosen should be applied consistently across collections.

Filtering, sorting, and pagination can work together in a request such as `GET /products?category=electronics&sort=price&page=2&per_page=10`. Here, `category=electronics` determines which products belong in the result set, `sort=price` determines their order, and `page=2&per_page=10` determines which portion of that ordered result set is returned. Together, these parameters form part of the collection's public contract and should have predictable names, accepted values, and behavior.

As consumers depend on collection parameters alongside other parts of the API contract, changing them can affect existing integrations. The next design concern is how an API can evolve while managing what existing consumers already depend on.

## Versioning and Evolving an API

An API evolves as requirements change, but existing consumers may continue to depend on its current contract. The main concern is whether a change allows those consumers to continue using the API without changing their integrations. A change that preserves existing behavior is generally compatible, while a **breaking change** changes or removes something that consumers may already depend on.

| Change                                      | Typical compatibility concern                                        |
| ------------------------------------------- | -------------------------------------------------------------------- |
| Add an optional response field              | Usually compatible when consumers can ignore unknown fields          |
| Remove or rename a response field           | Can break consumers that depend on the field                         |
| Change the meaning of an existing field     | Can break consumer assumptions even if the field name remains        |
| Remove a supported filter or sort parameter | Can break collection requests that use it                            |
| Change operation semantics                  | Can affect retry behavior and consumer workflows                     |
| Add a new resource or operation             | Usually compatible when existing behavior remains unchanged          |

For example, adding an optional `description` field to a product representation usually does not require existing consumers to change if they can ignore fields they do not use. Removing an existing `price` field can break consumers that depend on it, just as removing the `category` filter can break requests such as `GET /products?category=electronics`. When a breaking change cannot be introduced while preserving the existing contract, the provider can introduce a new version. A path-based approach such as `/v1/products` and `/v2/products` allows existing consumers to continue using the old contract while they migrate to the new one.

A new version is not necessary for every change. Compatible additions can usually remain within the existing version, while unnecessary versions increase the number of contracts that providers and consumers must maintain. When an older version will eventually be retired, consumers should be told what changed, what they need to update, and when support for the older version will end so they have enough time to migrate.

!!! tip "Prefer evolution when compatibility can be preserved"

    Introduce a new version when the required change cannot remain compatible with the contract that existing consumers depend on.

Together, these concepts establish how a REST API can maintain a predictable contract as it evolves. **REST Level 3** builds on this foundation by examining more advanced REST design concerns, including advanced resource modeling, long-running and asynchronous operations, content negotiation, hypermedia and HATEOAS, and the Richardson Maturity Model.
