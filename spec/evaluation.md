# Evaluation

Evaluate both the interface contract and actual use through an agent. Deterministic checks establish specific behavior. Task evaluations establish how well a particular agent and host can use it. Neither replaces judgment about the value of the result.

## Declare the assessment

Before testing, record:

- Application name, build or version, and specification commit.
- Supported business outcomes and explicit exclusions.
- Entry points, selected execution profiles, and supporting profiles.
- Host, model and version, configuration, instructions, and available tools.
- Required installation, connectivity, identity, and authority.
- Data sets, outcome criteria, execution limits, and relevant resource costs.

State which facts are fixed for the evaluation and which can vary. A claim about one task or host must name that scope. It must not imply universal usability.

Create a requirement matrix containing every AN requirement and every requirement in the selected profiles. Mark each **pass**, **fail**, **not evaluated**, or **not applicable**, with an evidence reference. A not-applicable decision must explain why the condition is absent from the assessed work. It cannot hide a missing capability needed for that work.

## Deterministic contract checks

Test the application's own boundaries without relying on the model to choose the correct behavior. Include these scenarios where applicable:

| Scenario | What to establish | Core requirements |
| --- | --- | --- |
| Entry and contracts | Entry points resolve; versions, scope, examples, and descriptions match behavior | AN-01, AN-02, AN-10 |
| Context access | Relevant objects are retrievable; scope, freshness, search limits, and truncation are clear | AN-03 |
| Invalid or unauthorized action | Invalid inputs and out-of-scope access are rejected before effects; content cannot grant authority | AN-02, AN-04 |
| Accepted and completed work | Acceptance, progress, waiting, completion, partial effects, and uncertainty are represented correctly | AN-05, AN-07 |
| Lost response and repetition | A completed write followed by a lost response does not invite unsafe blind repetition; retention and key scope behave as stated | AN-05, AN-06 |
| Concurrent or revised work | A human edit or a change after approval follows the declared conflict and decision policy | AN-04, AN-06, AN-09 |
| Interruption and updates | Process termination, disconnection, cancellation, and missed updates preserve the declared work facts | AN-06, AN-07 |
| Artifact use | Results can be retrieved, inspected, and transferred through authorized paths; expiry and private access are respected | AN-08, AN-09 |
| Limits and leaving | Budget boundaries, retention, export, revocation, and active-work disposition match their contracts | AN-07, AN-10 |
| Retained experience | Stored preferences have a source and scope and can be corrected without silently creating authority | AN-04, AN-10 |

Inject failures at meaningful boundaries. In particular, test failure after an effect but before its response, not just rejection before execution. Use controlled data and fakes for external effects in automated tests. Separate authorized live integration checks from deterministic tests and record their limits.

## Profile checks

Include every requirement from each selected profile in the assessment matrix. The checks below guide evidence collection; each identifier still needs a verdict.

| Profile | Required evidence |
| --- | --- |
| CLI | CLI-01: root and subcommand help, version and environment. CLI-02: non-interactive inputs and human handoff. CLI-03: parseable result and error channels, exit status, acceptance semantics. CLI-04: interruption, composition, and bulk behavior. |
| HTTP | HTTP-01: description and credential flow. HTTP-02: schemas, status codes, failures, collections, and references. HTTP-03: repetition, conflicts, asynchronous status, and offered update mechanisms. |
| MCP | MCP-01: negotiated protocol and capability contracts. MCP-02: domain scope and authority. MCP-03: usable catalogs, resources, and handoffs in each claimed host. |
| SDK | SDK-01: installation, types, runtime validation, and remote boundaries. SDK-02: actual retry, timeout, cancellation, and cleanup behavior. |
| Files | FILE-01: formats, validation, and when edits take effect. FILE-02: partial writes, conflicts, access, and transfer. |
| Instructions | DOC-01: discovery, contract alignment, and checked executable examples. DOC-02: Skill format and dependencies where offered; truthful entry-point claims. |
| Presentation | UI-01: accurate facts and consistent human actions. UI-02: access, expiry, host coverage, and protocol isolation where relevant. |

## Agent task evaluations

Give an agent the declared user request, legitimate starting context, and the product's normal entry point. Do not provide hidden endpoint names, internal implementation details, or a prewritten solution unless these are part of the claimed user experience.

Use realistic tasks with inspectable outcomes:

1. **First use:** discover the relevant capability, connect within the available authority, perform work, and inspect the result.
2. **Composition:** complete a reasonable new combination of existing capabilities. Include artifact transfer across interfaces or products if that is part of the claim.
3. **Recoverable problem:** encounter a stale revision, invalid input, expired reference, or another realistic failure and continue using the documented feedback.
4. **Interruption:** resume or accurately report the limits of continuing work after a lost connection or a different conversation.
5. **Human change:** incorporate a person's correction or direct edit; seek a decision when the change exceeds existing authority.
6. **Result judgment:** present enough evidence for a person to assess the output, including partial completion and known uncertainty.

Define outcome checks before running the tasks. Several action sequences may be valid. Assess the result and the declared constraints instead of requiring a single tool-call trace. Hold out some task variants when tuning descriptions or tools.

For creative or judgment-heavy work, identify the human criteria and reviewers. A program can verify that an artifact exists and that stated checks ran. It cannot establish all of the artifact's usefulness or truth.

## Measures

Record task outcome, material errors, unplanned human repair, explanation and coordination effort, latency, calls, context volume, and monetary or resource cost where relevant. Record whether a person could find the evidence and change the work when needed.

Distinguish chosen human participation from corrective intervention caused by a defect. A higher autonomous completion rate is not always a better experience.

Report trial counts and variability for probabilistic evaluations. A single successful demonstration is useful evidence, but cannot establish a success rate. Do not set universal thresholds without reference to a task's stakes and intended use.

## Report and claims

Use the [assessment template](../examples/assessment-template.md). Evidence references should identify a reproducible case, a result, or a reviewed artifact. Remove credentials and private user data before sharing reports.

A claim of conformance to a named revision requires:

- Every applicable MUST in the core, selected profiles, and assessment scope is satisfied by evidence.
- Each unmet SHOULD has a documented reason and assessment of consequences.
- All required paths for the claimed outcomes and hosts have been evaluated.
- Limitations and excluded scope are stated alongside the claim.

A fail or not-evaluated result on an applicable MUST prevents that conformance claim. Publish a scoped evaluation with its gaps instead. The project does not operate a certification program, and its examples are not certified implementations.

The repository's document checker validates local links, basic structure, and requirement references. It does not validate external links, protocol compliance, application behavior, agent performance, or the truth of a conformance report.
