# Application model

The [foundations](foundations.md) explain why applications should be designed first for agents acting for people. This document turns that position into product design priorities. The [core specification](../spec/core.md) defines the obligations. The [local tool](../examples/local-tool.md) and [reporting service](../examples/reporting-service.md) show complete use paths.

The [interaction model](foundations.md#interaction-model) is the common starting point. Agent use and direct human participation work with the same relevant domain facts, within their respective authority. This describes product behavior without prescribing an internal service architecture.

## Organize capabilities for agent use

Start with the outcomes the application supports and the operations an agent needs to reach them. Expose useful domain responsibilities with clear inputs, effects, and results. A capability can carry substantial internal work; callers should not have to rebuild domain rules from storage primitives or UI gestures.

A person can begin with a natural-language task. The agent needs a documented route to the required operations and context in its actual host. Include installation or connection, access, result inspection, and exception paths. Decisions or access steps reserved for a person need explicit handoffs. Assess this resulting use path; implementation order alone does not establish that agents can use the product.

Use programs for rules they can enforce and agents where interpretation helps. Tool granularity follows useful choices and composition needs. A local function may be enough; a remote service may need several operations. The [interface profiles](../spec/interfaces.md) describe supported access mechanisms and how to choose among them.

## Supply context as part of the product

Make product knowledge and current facts available alongside the operations that use them. A caller needs to learn what the product does, find a relevant capability, and determine whether it applies to the current object and authority.

| Need | Application contribution |
| --- | --- |
| Find a suitable product | Purpose, provider, supported work, limits, and entry points |
| Understand a capability | Domain terms, input and result contracts, effects, examples, and failures |
| Apply a method | Task guidance, decision points, and optional Skills that refer to the operation contract |
| Act in the current situation | Authorized objects, relationships, scope, revisions, and applicable conditions |
| Decide what follows | Execution facts, useful errors, result references, and any remaining uncertainty |

Offer a short overview and paths to task-relevant detail. A small CLI can carry much of this in help and output. A larger product may provide references and optional methods separately. Instructions need to match the supported behavior and make their assumptions clear.

Product discovery depends on an actual path such as an installed package, registry, search result, or user link. A known catalog describes available capabilities; it cannot establish that the current caller may perform an operation on a particular object. The [instructions topic](../spec/interfaces/instructions.md) covers discovery and progressive disclosure.

## Support composition and continued use of results

An agent may use an application for one part of a larger task. Capabilities should work in reasonable new combinations within their declared scope. A repeated, useful sequence can itself become a capability while retaining the choices that matter to its callers.

Return results in a form suitable for their next intended use. Supply enough meaning, identity, and access guidance for another operation or a person to use them. Native text, images, files, and structured data may all fit. Ordinary file inputs and outputs support the access path; explicit file-triggered behavior needs its own declared contract.

The next application may need an authorized transfer rather than a reference it cannot retrieve. Cross-application work can also partially succeed. Preserve the facts needed to continue or correct the work. The [artifact requirements](../spec/core.md#an-08--deliver-usable-and-inspectable-artifacts) govern these promises.

## Design human views for inspection and participation

With agent use as the primary execution path, human views focus on presenting work, enabling review, and supporting direct edits and decisions. A person can choose direct interaction because it is useful or valuable to them. An application may provide its own UI, a host may render a view, or a person may inspect an ordinary artifact.

Human actions and agent operations use the same relevant domain facts and rules. A saved edit needs to become visible to later agent work. A view should distinguish an unsaved draft, a committed revision, and an already completed effect. Richer presentation can help judgment without making routine agent access depend on a renderer.

Return concise state and relevant references to the agent, and enough detail for the person to inspect the actual result. The [presentation topic](../spec/interfaces/presentation.md) develops these responsibilities. View design follows the activity rather than requiring an agent counterpart for every UI gesture.

## Product forms

| Form | What the product supplies | Typical access | State and responsibility |
| --- | --- | --- | --- |
| Local tool | A capability installed in a working environment | CLI, in-process functions, host tool bindings, SDK, local MCP | Local computation, files, and declared effects |
| Remote service | A shared or hosted domain capability | HTTP, remote MCP, a CLI or SDK client | Domain records, access controls, remote effects |
| Delegated work | A service that carries out continuing work | Work creation, input, status, and artifact operations | Execution ownership, decisions, interruption, delivery |
| Interactive application | Objects people inspect, edit, and decide on | Operations plus standalone or embedded views | Shared domain facts and human-agent handoffs |

These forms can overlap. They are not maturity levels. A local image converter can satisfy the applicable requirements without accounts, a server, or a task queue. A host plugin can return an image directly without an output file. A service that publishes reports may combine several forms.

An application may internally use an agent. It still owns the execution it accepts and the relevant work and result facts. Internal delegation preserves the scope and traceability of that work. It cannot expand a user's grant merely by passing the task onward.

## The full use cycle

| Stage | The caller's question | Application contribution | Core requirements |
| --- | --- | --- | --- |
| Discover | Can this product help? | Identity, purpose, scope, entry points | AN-01 |
| Understand | What does this capability mean? | Terms, contracts, examples, limits | AN-02, AN-10 |
| Connect | Can I use it in this environment? | Installation or connection guidance, versions, access requirements | AN-01, AN-04, AN-10 |
| Read context | What exists and what is current? | Relevant objects, relationships, constraints, revisions | AN-03 |
| Act | What input is needed and what will change? | Validated operations with declared effects | AN-02, AN-04, AN-06 |
| Follow | Was it accepted, completed, or blocked? | Results or continuing work state and updates | AN-05, AN-07 |
| Examine | What changed and how can I check? | Artifacts, evidence, uncertainty, views | AN-05, AN-08, AN-09 |
| Correct | What can change now? | Edits, decisions, cancellation, recovery, takeover | AN-06, AN-07, AN-09 |
| Leave | What happens when I disconnect? | Retention, exports, access revocation, disposition of active work | AN-07, AN-10 |

Stages can repeat or overlap. A synchronous calculation can complete several in one call. Continuing-work requirements apply only when work accepted by the application outlives a call, connection, process, or conversation. The exact conditions live in the core specification; this table does not require every application to implement every mechanism.

The [evaluation procedure](../spec/evaluation.md) checks both application guarantees and agent use from a natural-language task. The [local tool example](../examples/local-tool.md) and [reporting service example](../examples/reporting-service.md) follow this cycle and connect their design choices to requirements.

## Terms

| Term | Meaning |
| --- | --- |
| Person | The human who directs or participates in the work |
| User's agent | An agent acting for that person in this activity; it may be supplied by any product |
| Host | The environment that runs or connects the user's agent and provides its tools and interaction surfaces |
| Application | The product that supplies domain capabilities and owns the rules and state assigned to it |
| Capability | Something the application enables a caller to accomplish |
| Operation | A specific invocation with defined inputs, effects, results, and failure behavior |
| Resource | An addressable object, document, data set, or other source of context |
| Work | An activity that can span several operations; only continuing work needs a persistent work record |
| Artifact | A retrievable output of work, such as a document, image, change, or structured data set |
| Evidence | Observations, records, or artifacts that support a claim about execution or results |
| Interface profile | Requirements for a specific access mechanism or supporting part of the use path, applied where relevant |

"The user's agent" describes a representative role. It does not establish ownership, identity, or permission by itself. Authority comes from the applicable user grant and access policy. The same agent can use an application and be invoked by another program; these roles do not require separate copies of domain rules.
