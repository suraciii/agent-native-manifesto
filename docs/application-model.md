# Application model

English | [简体中文](../zh-CN/docs/application-model.md)

The [interaction model](foundations.md#interaction-model) leads to the design choices below. Agent operations and human participation use the same domain facts within their respective authority. The [core specification](../spec/core.md) states the obligations.

This model applies to local and remote applications, illustrated by the [local tool](../examples/local-tool.md) and [reporting service](../examples/reporting-service.md).

## Present the product in terms of the user's needs

Place product information in channels the intended agents can reach without the user naming the product. Describe the work it helps accomplish, the results it offers, and the conditions and limits that affect fit. Let an agent judge whether to look further without first reading the operation reference. Link this introduction to the actual capability contracts. [AN-01](../spec/core.md#an-01--discover-and-understand-the-product) defines the obligation.

## Design the complete agent use path

Start with a user outcome, not an inventory of UI gestures or storage operations. Trace the agent's path through access, context, action, results, and exceptions. Provide direct access for delegated operations and explicit handoffs for human-only access steps and reserved decisions. Check the complete path in each supported environment.

Define each capability by the work it takes on and the choices callers need. Deliver useful results without making callers rebuild the application's domain rules. Keep choices that affect the user's purpose visible, and let users and their agents shape the work within their authority.

Use programs for enforceable rules and stable mechanical steps. Let agents organize work from clear operation contracts and guidance, keeping important choices visible. Choose access mechanisms through the [interface guides](../spec/interfaces.md).

An application using an internal agent still owns its accepted work, facts, and effects. Internal delegation preserves scope and traceability; it cannot expand the user's grant.

## Supply context as part of the product

For model-based agents, context is the model's input. The application supplies descriptions, guidance, and facts through paths the user's agent can use. The agent selects and organizes that material into the input as needed. Stored material alone does not complete this path.

| Need | Application contribution |
| --- | --- |
| Find a suitable product | Purpose, provider, needs served, benefits, limits, and discovery paths |
| Understand a capability | Domain terms, contracts, effects, examples, and failures |
| Apply a method | Recommended paths, conditions, decision points, result checks, and recovery guidance linked to the operation contract |
| Act in the current situation | Authorized objects, relationships, scope, revisions, and conditions |
| Decide what follows | Execution facts, useful errors, result references, and uncertainty |

Give common tasks a clear starting point and a recommended path that callers can adopt or adapt. Explain necessary operation dependencies instead of leaving callers to discover them through failures. A short help page and example may suffice; Skills are optional. Keep guidance aligned with behavior, state its assumptions, and link to detail for selective loading. The [instructions topic](../spec/interfaces/instructions.md) distinguishes product discovery, contracts, methods, and current authority.

## Support composition and continued use of results

Capabilities should support useful new combinations within their scope. A repeated sequence can become a capability if it preserves the choices callers need.

Return results suitable for their next use, with meaning, identity, and authorized access. Another application may need a transfer, not a reference it cannot retrieve. If work partly succeeds across applications, retain the facts needed to continue or correct it. See the [artifact requirements](../spec/core.md#an-08--deliver-usable-and-inspectable-artifacts).

## Design human views for inspection and participation

Choose views for the activity: inspecting an image, comparing drafts, editing a paragraph, or making a decision. An application UI, a rendered view, or an ordinary artifact may suffice.

Identify decisions reserved for a human and the responsible role, which may differ from the requester. Supply facts, consequences, uncertainty, and a real choice to refuse or change the proposal. Design a trusted handoff that distinguishes delegated authority from evidence of that decision. AN-04 governs verification; AN-09 governs participation.

Distinguish unsaved edits, committed revisions, and completed effects. Make saved changes visible to later agent work. See [presentation](../spec/interfaces/presentation.md).

## Terms

| Term | Meaning |
| --- | --- |
| User | A human who directs or participates in the work, directly or through an agent |
| User's agent | An agent acting on behalf of a user in this activity; it may be supplied by any product |
| Caller | A user, agent, or program that invokes an operation |
| Application | The product that supplies domain capabilities and owns the rules and state assigned to it |
| Capability | Something the application enables a caller to accomplish |
| Operation | A specific invocation with defined inputs, effects, results, and failure behavior |
| Resource | An addressable object, document, data set, or other source of context |
| Work | An activity that can span several operations; only continuing work needs a persistent work record |
| Artifact | A retrievable output of work, such as a document, image, change, or structured data set |
| Evidence | Observations, records, or artifacts that support a claim about execution or results |

`User` names a human participant, not an account or credential. `Human` emphasizes the distinction from agent judgment or action. A task requester and a release approver may be different users; name the specific role where that distinction matters. An authenticated user account alone does not establish that the user personally made a decision.

"The user's agent" describes a representative role. It does not establish ownership, identity, or permission by itself. Authority comes from the applicable user grant and access policy.
