# Evaluation

English | [简体中文](../zh-CN/spec/evaluation.md)

Evaluate the [application model](../docs/application-model.md) through deterministic contract checks and agent task trials. Contract tests establish specific behavior; trials establish use in a named environment. Neither settles the value of the result.

## Declare the assessment

Before testing, record:

- Application name, build or version, and specification commit.
- Supported business outcomes and explicit exclusions.
- Actual capability access paths and any supporting files, instructions, or human views.
- Claimed product discovery paths and the conditions needed to reach them.
- Agent, access environment, model and version, configuration, instructions, and available tools.
- Required installation, connectivity, identity, authority, and any reserved human decisions with their responsible roles.
- Data sets, outcome criteria, execution limits, and relevant resource costs.

State which facts are fixed and which can vary.

Choose tasks and checks for the outcomes in scope. Record results and evidence, and state what was not tested.

Use the [interface guides](interfaces.md#choose-access-paths) to plan checks for those paths.

## Deterministic contract checks

Test the application's own boundaries without relying on the model to choose the correct behavior. Include these scenarios where applicable:

| Scenario | What to establish | Core requirements |
| --- | --- | --- |
| Product discovery | Claimed discovery paths expose product information under the stated access conditions; descriptions of purpose, supported needs, benefits, and limits match the product | AN-01 |
| Use paths and contracts | Documented paths expose the operations, context, and guidance needed to select and use capabilities for each assessed outcome, including necessary operation dependencies and explicit human handoffs; versions, scope, examples, and descriptions match behavior | [Scope and coverage](core.md#scope-and-coverage), AN-01, AN-02 |
| Context access | Relevant objects are retrievable; where only part of a collection is needed, check whether it can be retrieved without reading the whole collection; scope, freshness, search limits, and truncation are clear | AN-03 |
| Invalid or unauthorized action | Input structure is checked programmatically; invalid inputs and out-of-scope access are rejected before effects; content cannot grant authority | AN-04 |
| Required human decision | The decision comes from an authorized user in the responsible role; account access and agent assertions alone cannot supply it; absent, refused, or unverifiable decisions block the dependent action | AN-04, AN-09 |
| Information for a human decision | The responsible user can inspect relevant facts, consequences, and uncertainty and can decline; pending and completed decisions are distinct | AN-09 |
| Decision handoff and reuse | Valid decision evidence can be relayed by an agent; existing decisions and ordinary delegated authority remain usable within their respective scope and conditions | AN-04, AN-09 |
| Accepted and completed work | Acceptance, progress, waiting, completion, partial effects, and uncertainty are represented correctly | AN-05, AN-07 |
| Diagnostic recovery | An authorized diagnostic path exposes bounded facts for a failure, partial effect, or unknown outcome; it identifies the relevant operation, work, or object, distinguishes observations from hypotheses and unknowns, and states scope, freshness, and the next supported check | AN-03, AN-05, AN-06, AN-07 |
| Lost response and repetition | A completed write followed by a lost response does not invite unsafe blind repetition; retention and key scope behave as stated | AN-05, AN-06 |
| Concurrent or revised work | A human edit or a change after approval follows the declared conflict and decision policy | AN-04, AN-06, AN-09 |
| Interruption and updates | Process termination, disconnection, cancellation, and missed updates preserve the declared work facts | AN-06, AN-07 |
| Artifact use | Results can be retrieved, inspected, and transferred through authorized paths; expiry, private access, and sensitive capability links are respected | AN-08, AN-09 |
| Limits and leaving | Budget boundaries, input and output retention, export, deletion limits, revocation, and active-work disposition match their contracts | AN-01, AN-02, AN-04, AN-07, AN-08 |

Check retention and revocation even when the application accepts no continuing work. Include retained input that is not returned as an artifact and delegated access that outlives synchronous calls.

Where separate requester and reviewer roles are supported, test different users in those roles. For a required human decision, test an authenticated user without the required authority and an agent with delegated access. If the application accepts decision evidence relayed by an agent, test that supported path. Also test work that needs no personal decision: do not introduce a gate where the declared contract permits delegated execution.

Inject failures at meaningful boundaries. In particular, test failure after an effect but before its response, not just rejection before execution. Use controlled data and fakes for external effects in automated tests. Separate authorized live integration checks from deterministic tests and record their limits.

## Interface checks

Use the guides for the interfaces and supporting material involved in each task.

| Guide | Checks to consider |
| --- | --- |
| [CLI](interfaces/cli.md#verification) | Non-interactive use, output channels, interruption |
| [HTTP](interfaces/http-api.md#verification) | Access, response meaning, conflicts, continuing work |
| [MCP](interfaces/mcp.md#verification) | Environment support, resource retrieval, authorization |
| [SDK](interfaces/sdk.md#verification) | Local and remote work, retries, bounded iteration |
| [Files and artifacts](interfaces/files-and-artifacts.md#verification) | Imports, conflicts, publication, retrieval |
| [Instructions](interfaces/instructions.md#verification) | Contract agreement, selective loading, dependencies |
| [Presentation](interfaces/presentation.md#verification) | Shared state, human edits, decisions, environment support |

## Agent task evaluations

In each claimed environment, give the agent a natural-language request and legitimate starting context. Do not supply hidden endpoints, implementation details, or a prewritten solution outside the claimed experience. Include other input forms where supported.

Product discovery trials start with a need, its constraints, and the normal discovery environment. Do not name the target product in the request or supply its entry point as a hint. Record the discovery channels, access conditions, and initial context. Known-product use trials may instead supply the normal product entry point. They do not, by themselves, establish product discovery.

Distinguish missing application capabilities or context from agent mistakes and unsupported environment behavior. A reasoned decision not to use the product is not itself a discovery failure.

Use realistic tasks with inspectable outcomes:

1. **Product discovery:** encounter the product through a claimed path and identify how it could help, its conditions, and its limits. Include a need outside the product's scope. Check accurate understanding and fit, not whether the agent always chooses it.
2. **Known-product first use:** start with a task expressed in ordinary language. Use normal product guidance to select operations, understand necessary dependencies, perform work within the available authority, and check the result. For common tasks, check whether a recommended path is available and usable without extra explanation. A valid call alone does not establish this.
3. **Composition:** complete a reasonable new combination of existing capabilities. Include artifact transfer across interfaces or products if that is part of the claim.
4. **Recoverable problem:** encounter a stale revision, invalid input, expired reference, or another realistic failure and continue using the documented feedback.
5. **Interruption:** resume or accurately report the limits of continuing work after a lost connection or a different conversation.
6. **Human change:** incorporate a user's correction or direct edit; seek a decision when the change exceeds existing authority.
7. **Required human decision:** where the application requires one, complete permitted preparation, present the relevant facts to the responsible user, and obtain their decision through the declared handoff. Include refusal as well as approval.
8. **Result judgment:** present enough evidence for a user to assess the output, including partial completion and known uncertainty.
9. **Diagnostic recovery:** encounter a failure, dependency fault, partial effect, or unknown outcome and use the application's normal diagnostic path to identify the known facts, limits, and supported next action. Include delayed, sampled, or incomplete diagnostic data where the application declares such conditions.

Define outcome checks before running the tasks. Several action sequences may be valid. Assess the result and the declared constraints instead of requiring a single tool-call trace. Hold out some task variants when tuning descriptions or tools.

For creative or judgment-heavy work, identify the human criteria and reviewers. A program can verify that an artifact exists and that stated checks ran. It cannot establish all of the artifact's usefulness or truth.

## Measures

Record task outcome, material errors, unplanned human repair, explanation and coordination effort, latency, calls, context volume, and monetary or resource cost where relevant. Record whether a user could find the evidence and change the work when needed.

Assess context quality through use: whether the agent could find and follow relevant guidance, obtain current facts, recognize effects and limits, and choose a supported next action. Record unclear or missing instructions, unnecessary trial and error, irrelevant material, repeated lookups, wrong product or operation choices, and extra explanation beyond normal product guidance. Distinguish inadequate guidance from an agent failing to follow guidance it received.

For diagnostic recovery, record whether the agent could locate the diagnostic path, associate facts with the relevant operation or work, distinguish observations from hypotheses and unknowns, identify the effects already known, and choose the next supported check or recovery action. Record diagnostic calls, returned volume, delay or sampling, repeated attempts, unresolved uncertainty, and human intervention.

For continuing work, record whether waiting requires repeated model involvement and whether missed updates can be recovered through authoritative state.

Distinguish chosen human participation, participation required by the application's contract or policy, and corrective intervention caused by a defect. Correctly waiting for a required decision or refusing an action without it is not, by itself, an application or agent failure. Record the actual task outcome separately. A higher autonomous completion rate is not always a better experience.

Report trial counts and variability for probabilistic evaluations. A single successful demonstration is useful evidence, but cannot establish a success rate. Do not set universal thresholds without reference to a task's stakes and intended use.

## Comparing interfaces

When comparing CLI, HTTP, MCP, or an SDK, use equivalent business tasks, data, authority, and outcome criteria. Record the full supported path, including instructions, installation, connection, artifact access, and human handoffs. Report both first-use and repeated-use conditions, including caches and reused connections.

Count actual I/O and attempts, including SDK retries and automatic pagination. Measure data entering model context separately from bytes sent to an application or UI. A small tool-call payload can still trigger substantial work; a large artifact need not enter the model context.

Retain failures and recovery costs. For maintenance comparisons, record contract drift, adapters, supported versions, and environment-specific work. Do not generalize beyond the tested environments, models, versions, and tasks.

## Report and claims

Use the [assessment template](../examples/assessment-template.md). Evidence references should identify a reproducible case, a result, or a reviewed artifact. Remove credentials and private user data before sharing reports.

Report the tested tasks, results, failures, untested cases, and limits. Keep claims within the observed evidence.

The [repository checks](../CONTRIBUTING.md#check-a-change) do not establish application behavior.
