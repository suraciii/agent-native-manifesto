# HTTP APIs

An HTTP API exposes domain operations across a network boundary. A host, program, CLI, SDK, or MCP server can invoke it. The agent does not need to construct raw requests if an appropriate client already expresses the operations well.

This is an optional execution profile governed by the [core specification](../core.md). Its requirements apply only when an assessed access path uses HTTP. An Agent Native application does not need an HTTP API or a server architecture. "API" is a broader term than HTTP; it can also mean in-process functions. See the [interface overview](../interfaces.md) for other access paths.

## Role and fit

HTTP is useful for shared remote state and clients in different languages or environments. It separates the application from the caller's process. That also creates uncertainty: a disconnected client may not know whether a write completed.

HTTP defines request and response semantics. [OpenAPI](https://spec.openapis.org/oas/latest.html) describes operations, data, and security schemes. Product guidance supplies domain meaning. These are complementary responsibilities.

A domain operation may be a resource update or an explicit action such as publication. Neither one endpoint per database table nor one opaque natural-language endpoint is a universal design rule. Choose a boundary that owns the relevant invariants and exposes decisions the caller actually needs.

## Design choices

### Description and discovery

A product entry point can link to an API description and authentication instructions. [RFC 9727](https://www.rfc-editor.org/rfc/rfc9727.html) supplies an API catalog discovery mechanism. Catalog discovery does not imply that every host can turn OpenAPI into tools or complete the authorization flow.

A useful description includes input and output schemas, required authority, default scope, relevant units, and consequences. Document the meaning of omitted fields, explicit nulls, empty collections, and redacted or unrequested data. A shape alone cannot tell a caller whether a missing value means "unknown" or "not returned."

Generating tools from OpenAPI can reduce mechanical work. Review the resulting tools for useful domain boundaries, understandable names, bounded responses, and preserved authorization. Generation cannot decide the right granularity by itself.

### Errors and current state

[RFC 9457](https://www.rfc-editor.org/rfc/rfc9457.html) provides Problem Details for APIs that need a common error format. Its `type` identifies the problem; `detail` explains this occurrence. Programmatic recovery should use defined fields, not parse human prose.

Use HTTP semantics consistently. A failed `If-Match` precondition normally produces 412. A different business conflict can use 409. A successful GET of a work record can return 200 even when that record reports that the work failed. The HTTP request and the domain activity are different subjects.

Stable ordering and pagination need an explicit consistency policy. A cursor alone does not promise a snapshot when data changes between pages. Field projection may reduce output, but the result still needs identifiers and revision information required for the next step.

### Repetition, conditions, and continuing work

Separate these concerns:

| Mechanism | What it addresses | Remaining question |
| --- | --- | --- |
| Idempotent method semantics | Repeating an intended effect | Did this particular attempt complete, and what response is now available? |
| Service-defined deduplication key | Repeated attempts of one logical operation | What are its scope, retention, and parameter rules? |
| Conditional write | Acting on a previously observed revision | How does the caller resolve a conflict? |
| Work identity | Tracking execution beyond a request | Which effects and pending decisions survive interruption? |

[Stripe's documented idempotency behavior](https://docs.stripe.com/api/idempotent_requests) is a useful concrete example. It can retain the first result, including an error, compare parameters on reuse, and prune keys after the stated retention period. That contract is more precise than "requests are safe to retry." Other services may define different behavior.

A client-generated key retained across attempts can recover a lost submission response when the service supports it. Generating a new key at every retry defeats that purpose. Do not invent a universal idempotency header or retention period from one provider's implementation.

For work accepted asynchronously, a status resource is the durable basis. Streams and webhooks can reduce delay. Their delivery, ordering, authentication, and refresh behavior still need a contract. Request timeout is not an instruction to cancel the remote operation unless explicitly defined that way.

### Authentication and artifact delivery

Reusable account credentials belong in the documented protected authentication mechanism. A narrowly scoped signed artifact URL is a different access mechanism. [Amazon S3 presigned URLs](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-presigned-url.html) illustrate that possession can grant access, the URL can be reused within its validity, and underlying credential expiry can shorten that validity.

Treat such a URL as sensitive access material, not as a harmless public citation. Prefer durable object identity plus an authorized retrieval path when the caller needs a lasting reference. Hosts can hold access material outside model context and expose an opaque artifact handle when supported.

## Requirements

### HTTP-01 — Description and access

The service MUST publish an interface description for the assessed operations. It SHOULD use OpenAPI with semantic descriptions and examples. An alternative machine-readable description needs a documented reason and a usable client path.

The entry point MUST identify the API address, supported version, authentication requirements, and documentation. Access to protected details MAY require authorization. A public entry page need only explain the access process.

Supported clients MUST use the service's documented credential mechanism, and the service MUST enforce it. Authentication and authorization failures MUST be distinguishable to authorized clients, subject to the service's documented resource-concealment policy. Reusable account or service credentials MUST NOT be embedded in ordinary resource URLs. Scoped artifact access links MUST follow AN-08.

### HTTP-02 — Requests and responses

The API MUST validate inputs and document success and failure response structures. It MUST use HTTP status semantics consistently. Domain failures MUST provide enough structured or native-format detail for recovery without relying only on a status number.

Collections MUST document ordering, pagination or bounds, and consistency where these affect correct use. Resource references MUST have a defined scope. Large artifacts SHOULD have a separate retrieval path rather than require inclusion in every response.

For programmatic error recovery, the API MUST provide stable documented identifiers or fields instead of requiring parsing of localized explanations. Existing formats such as Problem Details SHOULD be used where suitable.

### HTTP-03 — Effects and continuing work

Mutating requests MUST satisfy AN-06. The service MUST NOT imply exactly-once execution merely because it accepts an idempotency key. It MUST specify the actual deduplication guarantee.

Asynchronous acceptance MUST provide a work or operation reference and a status path. If a stream or webhook is offered, the service MUST define authorization, delivery, reconnection or refresh, and ordering or deduplication where relevant. A broken stream MUST NOT silently determine the business outcome.

A resource revision or equivalent condition SHOULD protect writes based on previously read state. An approval of a specific revision MUST be checked at execution.

## Example

This is an illustrative interaction for the [reporting service](../../examples/reporting-service.md), not a running API or a prescribed path convention.

| Step | Interaction | Meaning |
| --- | --- | --- |
| Read | GET the draft and receive a strong ETag | The caller sees one identified revision |
| Revise | Submit an update with that value in `If-Match` | Apply only if the observed revision still matches |
| Conflict | Receive 412 and a documented problem | Reread and resolve; do not blindly retry the stale write |
| Submit work | Receive asynchronous acceptance and a status reference | The work exists; the result is not yet complete |
| Inspect | GET the status and artifact reference | Determine the domain outcome separately from HTTP success |

A possible Problem Details body for the conflict is shown below. `about:blank` uses the HTTP status meaning; an application needing a more specific problem can define and document its own type URI.

```json
{
  "type": "about:blank",
  "title": "Precondition Failed",
  "status": 412,
  "detail": "The draft changed after it was read. Retrieve the current revision before submitting an update."
}
```

A consumer uses the status and its conditional-write contract for recovery. It need not parse `detail`.

## Verification

| Requirement | Important cases |
| --- | --- |
| HTTP-01 | Fresh access, expired credentials, wrong audience or scope where applicable, protected descriptions, private artifact retrieval |
| HTTP-02 | Omitted versus null values; typed failures; pagination during concurrent changes; bounded results |
| HTTP-03 | Lost response after a committed write; reused keys with changed inputs; expired deduplication records; stale ETags; interrupted update delivery |

Use the [evaluation procedure](../evaluation.md). Live service behavior and example syntax need separate evidence; a valid OpenAPI document alone proves neither.

## Sources and related topics

- [OpenAPI](https://spec.openapis.org/oas/latest.html), [RFC 9110 HTTP semantics](https://www.rfc-editor.org/rfc/rfc9110.html), and [RFC 9457 Problem Details](https://www.rfc-editor.org/rfc/rfc9457.html).
- [RFC 9727 API catalogs](https://www.rfc-editor.org/rfc/rfc9727.html).
- [Stripe idempotent requests](https://docs.stripe.com/api/idempotent_requests) and [S3 presigned URLs](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-presigned-url.html): provider-specific contracts, not universal defaults.
- Related profiles: [CLI](cli.md), [MCP](mcp.md), [SDK](sdk.md), and [presentation](presentation.md).
