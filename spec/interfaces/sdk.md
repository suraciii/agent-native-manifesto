# Software development kits

English | [简体中文](../../zh-CN/spec/interfaces/sdk.md)

An SDK exposes local or remote capabilities as functions, types, and objects. This guide applies the [core requirements](../core.md). Direct host functions need no SDK package; see the [interface overview](../interfaces.md).

## Role and fit

SDKs support composition, bounded batches, and intermediate processing outside model context. The host needs a compatible runtime and code-execution access. Provide setup guidance for supported runtimes and access methods. For one short operation, an existing CLI or MCP connection may cost less to set up.

## Design choices

### Generated bindings and domain helpers

Generated bindings align parameters and types with an API description. Domain helpers can remove repeated caller work, but should not hide publishing, charging, or retries. Show which calls run locally and which invoke a service.

Preserve distinctions between omission, null, and values across language defaults. Runtime validation still matters: untyped input and stale generated code can bypass compile-time checks.

### Retry ownership

The [Stripe Python SDK](https://github.com/stripe/stripe-python) documents configurable retries and idempotency support. Defaults depend on the library and version.

Three outer calls to an SDK that makes three attempts can produce nine requests. Fresh keys on each outer call can also create three logical operations, despite safe internal retries.

Choose one retry owner per logical operation and preserve its identity. Expose attempt limits, delays, timeouts, and uncertainty so the surrounding workflow can stay within budget.

### Lazy work, batching, and cancellation

Lazy iterators can hide many requests; collect-all helpers can exceed memory or rate limits. Explain when I/O occurs and how to bound it.

Use item-level batch results unless the batch is atomic. Define cleanup and cancellation for local resources and remote work: a client timeout does not prove server cancellation.

Scoped clients avoid changing process-global credentials or accounts when one program handles several workspaces.

## Example

In this illustrative [reporting service](../../examples/reporting-service.md) program, the agent reads bounded pages, summarizes them locally, and submits work. It retains the logical operation identity and work reference for lost-response recovery.

The program returns a summary and artifact references instead of every source record. Later writes still check draft revisions. A helper that also publishes needs an explicit publication and review contract. No executable SDK is supplied.

## Verification

| Focus | Cases to try |
| --- | --- |
| Callable contract | Supported installation; untyped input; omission versus null; two scoped clients; bounded lazy iteration |
| Effects and lifecycle | SDK retries combined with caller retries; identity across attempts; failure after a remote effect; timeout and cleanup; partial batch results |

Measure results and actual I/O, not code length, under the [evaluation procedure](../evaluation.md).

## Sources and related topics

- [Stripe Python SDK](https://github.com/stripe/stripe-python): client behavior, request options, and automatic retries.
- [Stripe idempotency contract](https://docs.stripe.com/api/idempotent_requests): the service guarantees on which safe client retries depend.
- [OpenAPI](https://spec.openapis.org/oas/latest.html): an existing source for generated HTTP bindings, with domain semantics still required.
- Related topics: [HTTP APIs](http-api.md), [CLI](cli.md), and [files and artifacts](files-and-artifacts.md).
