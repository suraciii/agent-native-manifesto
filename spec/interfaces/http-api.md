# HTTP APIs

English | [简体中文](../../zh-CN/spec/interfaces/http-api.md)

This guide applies the [core requirements](../core.md) to HTTP access. Other access paths, including in-process APIs, are covered by the [interface overview](../interfaces.md).

## Role and fit

HTTP suits shared remote state and clients in different environments. The network boundary creates uncertainty: a disconnected client may not know whether a write completed.

HTTP defines request semantics; [OpenAPI](https://spec.openapis.org/oas/latest.html) describes operations and data. Domain guidance explains their use. Endpoints can expose resource updates or actions such as publication.

## Design choices

### Description and discovery

Link the product entry to its API address, supported version, description, and authentication guidance. [RFC 9727](https://www.rfc-editor.org/rfc/rfc9727.html) supports API catalogs, but clients still need discovery and authorization support.

Explain omission, null, empty, and redacted values; a schema alone cannot distinguish "unknown" from "not returned." Review generated OpenAPI tools for useful boundaries, names, response size, and authorization.

### Errors and current state

[Problem Details](https://www.rfc-editor.org/rfc/rfc9457.html) uses `type` to identify the problem and `detail` to explain the occurrence. Recover through defined fields, not prose parsing.

A failed `If-Match` normally produces 412; other business conflicts can use 409. A GET can return 200 while its work record reports failure: request success and work success differ.

A pagination cursor does not promise a snapshot during concurrent changes. State ordering and bounds so callers can traverse a changing collection. Field projection should retain the identifiers and revisions needed next.

### Repetition, conditions, and continuing work

Separate these concerns:

| Mechanism | What it addresses | Remaining question |
| --- | --- | --- |
| Idempotent method semantics | Repeating an intended effect | Did this particular attempt complete, and what response is now available? |
| Service-defined deduplication key | Repeated attempts of one logical operation | What are its scope, retention, and parameter rules? |
| Conditional write | Acting on a previously observed revision | How does the caller resolve a conflict? |
| Work identity | Tracking execution beyond a request | Which effects and pending decisions survive interruption? |

[Stripe](https://docs.stripe.com/api/idempotent_requests) can retain the first result, including an error, compare reused parameters, and prune keys after its retention period. These are provider-specific guarantees. A fresh key on each retry defeats recovery of one logical submission.

For asynchronous work, retain a status resource. Clients can obtain updates through notifications, bounded waits, or polling run by a program, without asking the model to decide each check. For streams and webhooks, define access, delivery, and refresh behavior, including ordering and duplicate handling where relevant. Request timeout does not cancel remote work unless the contract says so.

### Authentication and artifact delivery

Use the service's documented credential flow. Explain authentication and permission failures within its resource-concealment policy. Keep reusable account credentials out of resource URLs.

[S3 presigned URLs](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-presigned-url.html) grant scoped artifact access by possession, including reuse while valid. Underlying credential expiry can shorten that validity.

Treat these links as sensitive. For lasting references, use object identity with authorized retrieval. Supporting hosts can keep access material outside model context behind an opaque handle. Large artifacts can use separate retrieval paths to avoid repeating their content in every response.

## Example

This illustrative [reporting service](../../examples/reporting-service.md) interaction does not prescribe endpoint paths.

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

| Focus | Cases to try |
| --- | --- |
| Description and access | Fresh access, expired credentials, wrong audience or scope where applicable, protected descriptions, private artifact retrieval |
| Requests and responses | Omitted versus null values; typed failures; pagination during concurrent changes; bounded results |
| Effects and continuing work | Lost response after a committed write; reused keys with changed inputs; expired deduplication records; stale ETags; interrupted update delivery |

Use the [evaluation procedure](../evaluation.md) for application and task evidence.

## Sources and related topics

- [OpenAPI](https://spec.openapis.org/oas/latest.html), [RFC 9110 HTTP semantics](https://www.rfc-editor.org/rfc/rfc9110.html), and [RFC 9457 Problem Details](https://www.rfc-editor.org/rfc/rfc9457.html).
- [RFC 9727 API catalogs](https://www.rfc-editor.org/rfc/rfc9727.html).
- [Stripe idempotent requests](https://docs.stripe.com/api/idempotent_requests) and [S3 presigned URLs](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-presigned-url.html): provider-specific contracts, not universal defaults.
- Related topics: [CLI](cli.md), [MCP](mcp.md), [SDK](sdk.md), and [presentation](presentation.md).
