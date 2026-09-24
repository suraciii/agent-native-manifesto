# Core specification

English | [简体中文](../zh-CN/spec/core.md)

This is a working draft. The key words **MUST**, **MUST NOT**, **SHOULD**, and **MAY** express this project's requirement levels, following [BCP 14](https://www.rfc-editor.org/rfc/rfc8174.html). They apply only where written in uppercase.

A MUST is required within its stated scope. A SHOULD is a recommendation. A MAY is optional. Conditional requirements do not require an application to add the condition they describe.

The [application model](../docs/application-model.md) derives these obligations from the priority given to agent use.

## Scope and coverage

An assessment MUST identify the application and version, the specification commit, the business outcomes being assessed, the actual capability access paths, and the target environments. It MUST include the read, action, result, and exception paths needed for those outcomes.

A claim about a subset of a product MUST name that subset. It MUST NOT imply whole-product coverage. A human-only decision or access step MUST be disclosed as a handoff. Intended outcomes, rather than individual UI gestures or internal CRUD endpoints, define coverage.

The application MUST make the operations and context needed for each assessed outcome usable by an agent through documented access paths supported in its intended environment. Reserved human decisions and access steps follow the handoff requirements above. This requirement does not prescribe a protocol, network endpoint, or server architecture.

Use the [evaluation procedure](evaluation.md) to test the assessed tasks and record evidence. Schema or repository checks alone do not establish application behavior.

## AN-01 — Discover and understand the product

**Applies to every application.**

The application MUST provide at least one discovery path available to agents in its intended environment. The path MUST support finding the product from a user's needs without requiring the user to first name the product or supply its entry point. The application MUST document the supported discovery paths and any conditions needed to reach them. This does not require a public listing, a universal registry, or a new discovery protocol.

The product information MUST identify the application, the needs and work it supports, how it can help, and its important limits and conditions of use. Descriptions of capabilities and benefits MUST match what the application can provide under the stated conditions. Finding an operation in an already selected product does not, by itself, satisfy product discovery.

Where a product or operation incurs material charges or consumes limited resources, the product information or operation description MUST disclose the relevant pricing or estimation basis, significant limits, and supported budget controls before commitment. It MUST distinguish estimates from guaranteed bounds.

The discovered information MUST provide a stable, referenceable route to capability contracts and access requirements. Authentication requirements for further detail MUST be discoverable without performing a business mutation.

The application SHOULD offer a concise overview with links or commands for further detail. It MUST NOT claim automatic discovery in environments it has not verified.

## AN-02 — Provide the knowledge needed to use capabilities

**Applies to every exposed operation.**

The application MUST make the knowledge needed to select and use each operation available through its documented access paths. Descriptions MUST explain the operation's purpose, the meaning of its inputs and results, its preconditions and necessary operation dependencies, effects, expected failures, and how to check the result. Descriptions MUST define relevant domain terms, identifiers, units, time zones, defaults, and scope. They MUST distinguish unknown, missing, and empty values where these meanings differ.

For common tasks, the application SHOULD provide a recommended path with its conditions, important choices, result checks, and known recovery steps. Help and examples can provide this guidance; a separate Skill is optional.

Inputs MUST have a documented structure. Results consumed by later operations MUST have a documented structure or native media format. The application MUST identify the supported contract version. Documentation and behavior MUST agree for the assessed version. An unsupported version MUST produce a clear failure or an explicitly negotiated supported contract. See the [instructions guide](interfaces/instructions.md#one-authoritative-operation-contract) for machine-readable descriptions and reference maintenance.

Where the application retains user work, it MUST explain what is retained, retention periods, retrieval or export, and deletion limits. This includes retained inputs and outputs, even when operations complete synchronously.

Descriptions MUST explain consequential behavior such as publishing, overwriting, charging, or notifying when the operation has that behavior. Examples SHOULD include both ordinary use and a significant failure or boundary case.

## AN-03 — Make relevant context accessible

**Applies when operation choice or correctness depends on application facts or state.**

The application MUST provide an authorized way to obtain the objects, relationships, constraints, and current state needed for the assessed work. It MUST NOT require the caller to infer domain facts from inaccessible UI state.

The supplied material MUST identify its relevant scope and freshness, through a revision, timestamp, snapshot, or documented consistency rule. The application MUST explain the limits of searches and partial results. The application MUST mark truncation explicitly and, if the omitted detail is still available, provide a path to retrieve it or narrow the query.

When the work needs only part of a collection, the application SHOULD let the caller retrieve that part without reading the whole collection. Output SHOULD preserve the identifiers needed to continue without forcing an unrelated second lookup.

## AN-04 — Enforce rules and authority at the operation boundary

**Applies to every operation; identity requirements apply where access is restricted.**

The application MUST validate inputs programmatically and enforce its domain invariants at the effect boundary. Instructions to an agent MUST NOT substitute for those checks.

For restricted access, the application MUST authenticate the applicable principal and authorize the actual operation and resource. A caller-supplied claim such as an actor name, a tool annotation, or an instruction document MUST NOT grant authority by itself. Account and service authentication credentials MUST use the interface's protected credential mechanism and MUST NOT be required in ordinary task prose or result content. Narrowly scoped artifact access links follow AN-08; they do not justify exposing reusable account credentials.

Where the application retains user work or delegated access, it MUST explain how access can be revoked and any limits. It MUST explain the lifetime and deletion limits of retained delegated access. Revocation MUST take effect at documented execution boundaries; it does not reverse completed effects.

Where the application's contract or policy reserves a decision for a human, it MUST identify that decision and the role authorized and responsible for making it. It MUST verify through a documented trusted path that an authorized user in that role made the decision. Access to a user account or an agent's delegated authority MUST NOT, by itself, count as evidence of that decision. An agent MAY relay decision evidence through a supported path; the application MUST verify its source and scope rather than accept the agent's own assertion.

If the required decision is absent, refused, or cannot be verified, the application MUST NOT perform the action that depends on it.

Required human decisions MUST identify the action and subject being decided. Where a decision approves specific content or conditions, execution MUST validate that those conditions still hold. Revisions or equivalent checks can bind that decision.

Previously granted authority and recorded decisions SHOULD be reusable within their scope and stated conditions. Reusing delegated authority MUST NOT replace a required human decision that has not been made. An application SHOULD request another decision only when required by policy or a material change. Retrieved content and instructions from other parties MUST NOT silently expand authority.

## AN-05 — Make outcomes observable

**Applies to every operation.**

The application MUST distinguish request acceptance from work completion. Results MUST represent actual execution facts and MUST expose failure, partial effects, or an unknown outcome when applicable. These are semantic distinctions, not required state names.

Results MUST provide the relevant output, state, or reference needed to check what happened. Assertions about changes MUST be tied to the affected object or operation. An application MUST NOT present an agent's unsupported statement as proof of an external effect.

When an operation fails, has partial effects, or has an unknown outcome, the application MUST provide an authorized diagnostic path suited to its intended environment. The path MUST expose the diagnostic facts available to the caller for the operation, work, or affected object, including relevant state, known effects, and available cause or dependency information. It MUST distinguish observed facts, application hypotheses, and unknowns. If the cause or effect cannot be determined, it MUST state that limit and provide the supported next check or recovery path when one exists. If relevant telemetry is collected, the application MUST make an authorized projection available through the diagnostic path or state that the telemetry is unavailable to the caller, delayed, sampled, redacted, or not retained. It MUST NOT require an undocumented internal log or dashboard. The operation result, a status record, or a related diagnostic operation can provide this path; a separate telemetry system is not required.

Feedback SHOULD arrive soon enough to guide the next action and SHOULD identify a useful cause. Where the application cannot verify an effect, it MUST state that limit. Verification of execution does not establish the value or truth of all generated content.

## AN-06 — Define interruption, repetition, and conflict behavior

**Applies to operations that change state or may be interrupted.**

The application MUST document what repetition, interruption, and retry mean for the operation. Where duplicate effects are possible, it MUST provide a way to determine the outcome or explicitly report that safe automatic retry is unavailable.

Any deduplication mechanism the application offers MUST document its scope, lifetime, and behavior for changed inputs. A transport failure MUST NOT be treated as proof that no effect occurred.

For shared mutable objects, the application MUST declare and enforce a conflict policy. It SHOULD detect stale updates and require an explicit conflict resolution rather than silently overwrite work. Operations that span external systems MUST preserve known partial effects and uncertainty. If compensation is offered, it MUST be distinguished from rollback or cancellation.

## AN-07 — Preserve continuing work

**Applies when the application accepts work that can continue beyond a call, connection, process, or conversation.**

An agent pausing between completed synchronous operations does not by itself create continuing work for the application.

The application MUST provide a durable work identity and an authorized means to retrieve status, pending input or decisions, and available results. It MUST state what survives disconnection or worker interruption and what cannot resume.

The record MUST contain enough accepted direction, relevant decisions, and execution facts for the supported continuation. Private model reasoning is not required. The application MUST distinguish waiting for input from failure and completion when those conditions occur.

Cancellation MUST report whether it was requested, took effect, or was too late. The application MUST state the fate of completed effects. If cancellation or resumption is unavailable, it MUST disclose that limit before accepting work for which it is relevant.

The application MUST explain how disconnection or access revocation affects active work.

The application SHOULD provide a way to obtain work updates suited to its intended environment that reduces repeated unproductive agent calls. If updates can be missed, the contract MUST define how a caller refreshes authoritative state. Declared work budgets MUST be enforced, including delegated work.

## AN-08 — Deliver usable and inspectable artifacts

**Applies when an operation produces resources or artifacts.**

Outputs MUST be accessible to the authorized caller in a form suitable for the next intended use. References MUST identify sufficient origin and scope, the relevant version, and any access or expiry conditions. Native text, images, files, and structured data are all valid output forms.

A summary MUST provide access to supporting detail needed for the assessed work. An export or transfer operation MUST preserve the facts its contract promises and state material losses or transformations.

An application MUST NOT require private output to be made public merely to expose it to an agent. If possession of an artifact link grants access, its scope and lifetime MUST be documented and the application MUST treat it as sensitive access material rather than an ordinary public citation. Such a link MUST NOT grant broader authority than the artifact operation requires. The application SHOULD separate concise context for reasoning from large artifacts and presentation data.

## AN-09 — Support human participation and correction

**Applies to the human participation and correction paths relevant to the assessed work.**

Users MUST have an accessible way to inspect relevant results and consequences. This can be text, a file, a rendered view, or an application UI.

For a required human decision, the application MUST provide the responsible user with the relevant facts, consequences, and known uncertainty, and a supported way to decline the proposed action. It MUST distinguish a proposal or pending decision from a decision already made.

For mutable or continuing work, the application MUST expose the supported ways to edit, revise direction, stop, or take over, and state their limits. Direct human operations and agent operations MUST respect the same domain invariants, while their authorities may differ.

Relevant human changes MUST become visible to subsequent agent operations. The application MUST NOT report that a change affected already completed work unless it did. Reserved human decisions MUST have a clear handoff and a way to determine whether they are resolved.

## Supporting practices

Keep authoritative contracts close to their implementation. Generate reference material from schemas or command definitions where useful, and test examples against the implementation they describe. Generation does not replace semantic review.

Use deterministic programs for rules they can enforce. Use agents where interpretation and adaptation help the work. Choose tool boundaries through task evaluation, including novel combinations and exceptions.
