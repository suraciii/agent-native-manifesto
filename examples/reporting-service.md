# Reporting service example

This illustrative design applies the [application model](../docs/application-model.md) to continuing work and maps it to the [core specification](../spec/core.md). It is not a running or evaluated service. Capability names describe domain responsibilities, not mandatory commands or endpoints.

## User task and environment

A person asks their agent:

> Prepare a report of this week's customer problems. Give me a draft to review before publication.

The agent uses a remote service that can read authorized customer records, maintain report drafts, and publish a specific revision. The service may offer a deterministic report builder or its own research agent. Both must expose the same relevant work and result facts.

## Capabilities and context

The entry point explains the reporting scope, provider, supported interfaces, access requirements, and any charges. It links to an HTTP description or an MCP connection guide where those paths are supported. An optional Skill explains a research and review method without duplicating every parameter definition.

The agent can learn the difference between customer records, draft revisions, review decisions, and published reports. Authorized reads supply current source records, work status, and draft revisions. The agent can retrieve the information relevant to its next action without inspecting the service's database or navigating a dashboard.

| Capability | What the caller supplies | What the service owns |
| --- | --- | --- |
| Search customer records | Time range, account scope, relevant filters | Authorization, search limits, dated records and references |
| Create reporting work | Objective, scope, source selection, applicable limits | Accepted direction, work identity and revision, execution state |
| Read work | Work identity | Accepted direction and revision, execution facts, pending decisions, available artifacts |
| Revise reporting direction | Work identity, expected work revision, revised objective or source scope | Validated direction and revision; declared effects on remaining work and the draft |
| Read or revise a draft | Draft identity; expected revision for a write | Content, revision, provenance, conflict checks |
| Record a review decision | Decision, subject revision, authorized actor context | A decision bound to its subject and scope |
| Publish a revision | Exact revision, required authority, repetition identifier if supported | Validation, external visibility, publication record |
| Retrieve or export a report | Report identity, revision, requested representation | Authorized content or artifact reference, source revision, publication state, declared export transformations |
| Request cancellation | Work identity | Whether work can stop and which effects remain |

A caller's actor field is descriptive data. The actual decision authority is checked using authenticated context and policy.

A direction change reports its effect on remaining work and any existing draft. Draft content changes through a revision-checked update; changing the objective alone is not reported as rewriting an existing result.

## A complete path

1. The agent discovers the relevant capabilities and obtains the access required to read the selected records and prepare a draft. A publication grant is not inferred from permission to prepare.
2. The service returns records with their scope and freshness. Search truncation is explicit. The agent narrows the query or retrieves more records when needed.
3. Reporting work is accepted. Its response identifies the work and provides a status path; acceptance is not reported as report completion.
4. A draft becomes available with source references and its known coverage limits. The person can open a view or retrieve the document directly.
5. The person says, "Focus on paying customers," and saves an edit to one paragraph. The agent updates the accepted direction using the observed work revision, then reads the current draft before preparing an update. A write based on the old draft revision returns a conflict. The agent reconciles the new scope with the person's saved edit before committing revised content.
6. Review concerns a specific revision. If that revision changes before publication, the service requires the applicable decision to be re-evaluated. A prior grant that still covers the same action and conditions need not prompt again.
7. Publication returns a durable reference to the published revision. The person and agent can inspect what was made visible and where.
8. If the conversation or host changes, a later authorized agent retrieves the work identity, accepted direction, relevant decisions, and results through the service. The work remains inspectable without relying on the earlier agent's private reasoning.
9. The person retrieves or exports the report, then uses the documented access-management handoff to revoke delegated access and verify its status. The service's retention and revocation policy explains what remains accessible and what happens to active work. Disconnection, revocation, and withdrawal of a published report remain distinct actions.

## Failure and correction paths

**Response lost after publication.** Publication may have succeeded. The agent checks the publication record or safely repeats the request under the documented deduplication contract. The service states the key's scope and retention. After that guarantee expires, the caller must not assume a repeat is safe.

**Source disappears.** The draft identifies the missing source and coverage gap. It can cite a lawfully retained snapshot if one exists and is accessible. A source link alone does not guarantee permanent evidence.

**Partial external delivery.** If publication includes several destinations, the record identifies each known result. One failed destination does not erase a successful one. Correction or withdrawal is a separate operation with its own limits.

**User cancels during work.** The service records the request and later reports whether execution stopped. Existing drafts remain according to retention policy. Publication that already occurred is not described as undone.

**Connection or host changes.** An authorized caller can retrieve the work identity, accepted direction, decisions, state, and artifacts. Raw conversation history or private model reasoning is not the only continuation mechanism.

**Access is revoked.** Later operations enforce the revised grant at the stated boundaries. The service explains whether active work stops, pauses, or can finish an already committed effect.

## Human views and continued use

A report view presents source coverage, draft content, differences, and decisions. Editing and review operate on the same report revisions that the agent reads and updates. An unsaved edit remains visibly separate until it is committed or handed off through a supported path.

An MCP host may embed that view. A CLI client may return the artifact reference and a concise state record. An HTTP client may retrieve the same revision directly. The selected supported paths use consistent domain facts and access rules.

The agent can receive a compact description and request a diff when needed, without loading the entire rendering payload. An authorized export can also become input to another application, with the source revision and any lost information made clear.

## Requirement mapping and evidence

Assess all core requirements whose conditions apply. Select [HTTP](../spec/interfaces/http-api.md), [MCP](../spec/interfaces/mcp.md), or [CLI](../spec/interfaces/cli.md) profiles for access paths that use them. Select supporting [instructions](../spec/interfaces/instructions.md), [presentation](../spec/interfaces/presentation.md), and [files and artifacts](../spec/interfaces/files-and-artifacts.md) profiles where those behaviors are part of the actual product claim. An interface mentioned in this example does not become required.

| Part of the case | Core requirements | Evidence required from an implementation |
| --- | --- | --- |
| Task, product entry, and source selection | AN-01, AN-02, AN-03 | An agent can find the reporting capabilities and retrieve relevant current records through the declared path |
| Authority, review, and publication | AN-04, AN-06 | Scope is enforced; a decision is checked against the actual subject revision; stale approval cannot publish changed content |
| Accepted work, revised direction, and handoff | AN-05, AN-06, AN-07 | Acceptance is distinguished from completion; direction updates check the observed work revision; retained direction and results remain accessible after reconnection |
| Failure after an effect | AN-05, AN-06 | Lost responses, partial delivery, and outcome uncertainty follow the stated lookup and repetition contracts |
| Drafts, exports, and human changes | AN-08, AN-09 | The person can inspect and edit the relevant revision; later agent actions use the changed facts; authorized artifacts can be retrieved and reused |
| Versions, costs, and leaving | AN-10 | Descriptions match behavior; charges and limits are available before commitment; retention, export, and revocation follow the declared policy |

These are proposed checks, not observed passing results. Use the [evaluation procedure](../spec/evaluation.md) and [assessment template](assessment-template.md) to record evidence for every applicable core and profile requirement. Application behavior and agent task trials remain **not evaluated** in this design example.
