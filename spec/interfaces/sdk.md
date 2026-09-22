# Software development kits

An SDK exposes capabilities as functions, types, and objects in a programming environment. An agent can write a program that uses it, or a host can use it behind a tool, CLI, or integration.

This is an execution profile governed by the [core specification](../core.md). An SDK does not require the application to run locally; it may be a client of a remote service. See the [interface overview](../interfaces.md).

## Role and fit

SDKs are useful for substantial programmatic composition: paging through records, transforming data, applying bounded batches, and retaining large intermediate results outside model context. The host needs a supported runtime and a way to execute code with appropriate access.

A short operation in a restricted host may be easier through [MCP](mcp.md) or an existing [CLI](cli.md). Installing a language environment and package for one call can add more effort than it removes. Compare setup cost as well as repeated execution.

## Design choices

### Generated bindings and domain helpers

Generated bindings can keep function parameters and data types aligned with an API description. They provide a broad, predictable mapping. Domain helpers can hide repeated sequences and expose a useful business responsibility. The choice depends on whether the abstraction removes caller knowledge or merely renames the same inputs.

A helper that silently creates several remote effects needs to make those effects clear. A typed method should not turn publishing, charging, or retries into an implementation detail that the caller cannot discover.

Types can distinguish absent input, explicit null, and a value. Language defaults should preserve the server's intended distinctions. Runtime checks remain necessary because untyped callers, stale generated code, and external input can bypass compile-time guarantees.

### Retry ownership

The [Stripe Python SDK](https://github.com/stripe/stripe-python) documents configurable network retries and idempotency support. This is useful evidence that retries are part of the client contract, not merely server behavior. Defaults and error categories depend on the SDK and version; do not copy one library's settings into every application.

Suppose an SDK makes up to three attempts and an agent repeats the SDK call three times. The service can receive up to nine attempts. If each new SDK call receives a new deduplication key, those calls may represent three logical operations even if each internal retry is safe.

Choose the layer that owns the retry policy for each logical operation. Preserve its identity across the attempts that belong to it. Make the attempt limit, delay, timeout, and final uncertainty visible enough for the surrounding workflow to remain within its budget.

### Lazy work, batching, and cancellation

An iterator that fetches pages lazily can hide many network calls behind a short loop. A helper that collects everything can exceed memory, context, or rate limits. Document when I/O happens, how to bound it, and what remains after interruption.

Batch operations need item-level results unless they really are atomic. A client-side timeout usually means the caller stopped waiting; it does not prove the server stopped. Cancellation tokens and context managers need defined meanings for both local resources and remote work.

Scoped clients are often easier to reason about than process-global mutable credentials or default accounts. This matters when an agent handles more than one workspace in the same process.

## Requirements

### SDK-01 — Callable contract

The SDK MUST document supported languages, runtimes, versions, initialization, and access requirements. Public operations MUST have documented parameters, effects, results, and errors. Types SHOULD describe these contracts where the language supports them.

Runtime validation MUST enforce the relevant rules even if callers bypass type checking. The SDK MUST document which work runs locally and which invokes a service. Host code-execution support MUST be stated as an environment requirement.

Where omission, null, or a default changes the domain operation, the SDK MUST preserve and document that distinction. Lazy operations MUST identify when they perform I/O and how the caller can bound their work.

### SDK-02 — Effects and lifecycle

The SDK MUST preserve the underlying service's authority, retry, and conflict contracts. Automatic retries MUST be limited to operations and conditions for which they are safe, with a bounded policy. Cancellation, timeouts, streaming, and cleanup MUST have documented meanings where offered.

Retry and timeout configuration MUST be discoverable for operations that use them. A retrying helper MUST preserve the logical operation identity required by the service's repetition contract. A fresh outer invocation MUST NOT be described as a continuation of an earlier invocation unless that identity is preserved.

## Example

This is a design example for the [reporting service](../../examples/reporting-service.md), not executable SDK code.

An agent program reads bounded pages of customer records, computes a summary locally, and submits reporting work. It retains the submission's logical operation identity and the returned work reference. If submission loses its response, the program follows the service's outcome lookup or safe repetition contract.

The program returns a compact summary and the relevant artifact references to the agent. The model need not read every record. If the person edits the draft, the next write still checks its revision; using an SDK does not change the concurrency rule.

Useful public methods hide transport details while leaving scope, revision conditions, bounds, and consequential effects explicit. An all-in-one helper that also publishes needs separate documented authority and review behavior.

## Verification

| Requirement | Important cases |
| --- | --- |
| SDK-01 | Supported installation; untyped input; omission versus null; two scoped clients; bounded lazy iteration |
| SDK-02 | SDK retries combined with caller retries; identity across attempts; failure after a remote effect; timeout and cleanup; partial batch results |

Measure both the program's result and its actual I/O. A small amount of generated code does not necessarily mean few requests. Follow the [evaluation procedure](../evaluation.md).

## Sources and related topics

- [Stripe Python SDK](https://github.com/stripe/stripe-python): client behavior, request options, and automatic retries.
- [Stripe idempotency contract](https://docs.stripe.com/api/idempotent_requests): the service guarantees on which safe client retries depend.
- [OpenAPI](https://spec.openapis.org/oas/latest.html): an existing source for generated HTTP bindings, with domain semantics still required.
- Related profiles: [HTTP APIs](http-api.md), [CLI](cli.md), and [files](files.md).
