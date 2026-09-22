# Core specification

This is a working draft. The key words **MUST**, **MUST NOT**, **SHOULD**, and **MAY** express this project's requirement levels, following [BCP 14](https://www.rfc-editor.org/rfc/rfc8174.html). They apply only where written in uppercase.

A MUST is required within its stated scope. A SHOULD is a recommendation; a departure needs a documented reason and evidence of its consequences. A MAY is optional. Conditional requirements do not require an application to add the condition they describe.

## Scope of an assessment

An assessment MUST identify the application and version, the specification commit, the business outcomes being assessed, the actual capability access paths, the applicable [interface profiles](interfaces.md), and the target host environments. It MUST include the read, action, result, and exception paths needed for those outcomes.

A claim about a subset of a product MUST name that subset. It MUST NOT imply whole-product coverage. A human-only decision or access step MUST be disclosed as a handoff. Intended outcomes, rather than individual UI gestures or internal CRUD endpoints, define coverage.

Passing a schema or repository check alone is not conformance. Use the [evaluation procedure](evaluation.md) to record evidence for every applicable requirement and selected profile.

## AN-01 — Discover and understand the product

**Applies to every application.**

The application MUST make its capabilities usable through a documented access path supported in its intended environment. This requirement does not prescribe a protocol, network endpoint, or server architecture.

The application MUST provide a stable, referenceable entry point available to its intended callers. This can be installed command help, function documentation, a service descriptor, or a protocol endpoint.

The entry point MUST identify the product, supported work, relevant environment or access requirements, and how to find capability contracts. It MUST state the version or provide a way to obtain it. Authentication requirements for further detail MUST be discoverable without performing a business mutation.

The application SHOULD offer a concise overview with links or commands for further detail. It MUST NOT claim automatic discovery in hosts it has not verified.

## AN-02 — Describe meaningful capabilities

**Applies to every exposed operation.**

Each operation MUST describe its purpose, input, result, preconditions, effects, and expected failures. Descriptions MUST define relevant domain terms, identifiers, units, time zones, defaults, and scope. They MUST distinguish unknown, missing, and empty values where these meanings differ.

Inputs MUST have a defined, programmatically validated structure. Results consumed by later operations MUST have a documented structure or native media format. Large or complex structured interfaces SHOULD expose machine-readable schemas as well as semantic descriptions.

Descriptions MUST explain consequential behavior such as publishing, overwriting, charging, or notifying when the operation has that behavior. Examples SHOULD include both ordinary use and a significant failure or boundary case.

## AN-03 — Make relevant context accessible

**Applies when operation choice or correctness depends on application context.**

The application MUST provide an authorized way to obtain the objects, relationships, constraints, and current state needed for the assessed work. It MUST NOT require the caller to infer domain facts from inaccessible UI state.

Context MUST identify its relevant scope and freshness, through a revision, timestamp, snapshot, or documented consistency rule. The application MUST explain the limits of searches and partial results. Truncation MUST be explicit and provide a path to retrieve or narrow the omitted detail when available.

Collections SHOULD support suitable search, filtering, pagination, or ranges. Output SHOULD preserve the identifiers needed to continue without forcing an unrelated second lookup.

## AN-04 — Enforce rules and authority at the operation boundary

**Applies to every operation; identity requirements apply where access is restricted.**

The application MUST validate inputs and enforce its domain invariants where effects occur. Instructions to an agent MUST NOT substitute for those checks.

For restricted access, the application MUST authenticate the applicable principal and authorize the actual operation and resource. A caller-supplied claim such as an actor name, a tool annotation, or an instruction document MUST NOT grant authority by itself. Account and service authentication credentials MUST use the interface's protected credential mechanism and MUST NOT be required in ordinary task prose or result content. Narrowly scoped artifact access links follow AN-08; they do not justify exposing reusable account credentials.

Required human decisions MUST identify the action and subject being decided. Where a decision approves specific content or conditions, execution MUST validate that those conditions still hold. Revisions or equivalent checks can bind that decision.

Previously granted authority SHOULD be reusable within its scope. An application SHOULD request another decision only when required by policy or a material change. Retrieved content and instructions from other parties MUST NOT silently expand authority.

## AN-05 — Make outcomes observable

**Applies to every operation.**

The application MUST distinguish request acceptance from work completion. Results MUST represent actual execution facts and MUST expose failure, partial effects, or an unknown outcome when applicable. These are semantic distinctions, not required state names.

Results MUST provide the relevant output, state, or reference needed to check what happened. Assertions about changes MUST be tied to the affected object or operation. An application MUST NOT present an agent's unsupported statement as proof of an external effect.

Feedback SHOULD arrive soon enough to guide the next action and SHOULD identify a useful cause. Where the application cannot verify an effect, it MUST state that limit. Verification of execution does not establish the value or truth of all generated content.

## AN-06 — Define interruption, repetition, and conflict behavior

**Applies to operations that change state or may be interrupted.**

The application MUST document what repetition, interruption, and retry mean for the operation. Where duplicate effects are possible, it MUST provide a way to determine the outcome or explicitly report that safe automatic retry is unavailable.

If a deduplication key or equivalent mechanism is offered, its scope, lifetime, and behavior for different inputs MUST be documented. A transport failure MUST NOT be treated as proof that no effect occurred.

For shared mutable objects, the application MUST declare and enforce a conflict policy. It SHOULD detect stale updates and require an explicit conflict resolution rather than silently overwrite work. Operations that span external systems MUST preserve known partial effects and uncertainty. Compensation MUST be described separately from rollback or cancellation.

## AN-07 — Preserve continuing work

**Applies when work can outlive a call, connection, process, or conversation.**

The application MUST provide a durable work identity and an authorized means to retrieve status, pending input or decisions, and available results. It MUST state what survives disconnection or worker interruption and what cannot resume.

The record MUST contain enough accepted direction, relevant decisions, and execution facts for the supported continuation. Private model reasoning is not required. The application MUST distinguish waiting for input from failure and completion when those conditions occur.

Cancellation MUST report whether it was requested, took effect, or was too late. The application MUST state the fate of completed effects. If cancellation or resumption is unavailable, it MUST disclose that limit before accepting work for which it is relevant.

Updates SHOULD use a suitable event, notification, or bounded waiting mechanism where supported, to avoid repeated unproductive agent calls. If updates can be missed, their delivery contract MUST define how a caller refreshes authoritative state. Declared work budgets MUST be enforced by the executing system, including work it delegates.

## AN-08 — Deliver usable and inspectable artifacts

**Applies when an operation produces resources or artifacts.**

Outputs MUST be accessible to the authorized caller in a form suitable for the next intended use. References MUST identify sufficient origin and scope, the relevant version, and any access or expiry conditions. Native text, images, files, and structured data are all valid output forms.

A summary MUST provide access to supporting detail needed for the assessed work. An export or transfer operation MUST preserve the facts its contract promises and state material losses or transformations.

An application MUST NOT require private output to be made public merely to expose it to an agent. If possession of an artifact link grants access, its scope and lifetime MUST be documented and the application MUST treat it as sensitive access material rather than an ordinary public citation. Such a link MUST NOT grant broader authority than the artifact operation requires. The application SHOULD separate concise context for reasoning from large artifacts and presentation data.

## AN-09 — Support human participation and correction

**Applies to the human participation and correction paths relevant to the assessed work.**

People MUST have an accessible way to inspect relevant results and consequences. This can be text, a file, a host view, or an application UI.

For mutable or continuing work, the application MUST expose the supported ways to edit, revise direction, stop, or take over, and state their limits. Direct human operations and agent operations MUST respect the same domain invariants, while their authorities may differ.

Relevant human changes MUST become visible to subsequent agent operations through refreshed state, revisions, events, or an equivalent contract. The application MUST NOT report that a change affected already completed work unless it did. Reserved human decisions MUST have a clear handoff and a way to determine whether they are resolved.

## AN-10 — Keep access, cost, and contracts understandable over time

**Applies to all applications, with conditional obligations below.**

The application MUST identify its supported interface versions. Documentation and behavior MUST agree for the assessed version. An unsupported version MUST produce a clear failure or an explicitly negotiated supported contract.

Where an operation incurs material charges or consumes limited resources, the application MUST disclose the relevant pricing or estimation basis, significant limits, and any supported budget controls before commitment. It MUST distinguish estimates from guaranteed bounds.

Where the application retains user work or delegated access, it MUST explain retention, retrieval or export, deletion limits, access revocation, and what disconnection or revocation means for active work. Revocation MUST take effect at the documented execution boundaries; it does not imply reversal of completed effects.

If the application retains lessons or preferences for future work, it MUST scope them to the appropriate user or activity, preserve their source, and provide a way to correct or remove them. Generated lessons MUST NOT silently become new user decisions or access grants.

## Supporting practices

Keep authoritative contracts close to their implementation. Generate reference material from schemas or command definitions where useful, and test examples against the implementation they describe. Generation does not replace semantic review.

Use deterministic programs for rules they can enforce. Use agents where interpretation and adaptation help the work. Choose tool boundaries through task evaluation, including novel combinations and exceptions. A capability can remain useful after its internal implementation becomes more deterministic.
