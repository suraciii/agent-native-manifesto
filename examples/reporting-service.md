# Reporting service example

This is an illustrative product design. It is not a running service or a protocol definition. Capability names below describe domain responsibilities, not mandatory command names or endpoints.

## Intended work

A person asks their agent: "Prepare a report of this week's customer problems. Give me a draft to review before publication."

The agent uses a remote service that can read authorized customer records, maintain report drafts, and publish a specific revision. The service may offer a deterministic report builder or its own research agent. Both must expose the same relevant work and result facts.

## Product entry

The entry point explains the reporting scope, provider, supported interfaces, access requirements, and any charges. It links to an HTTP description and an MCP connection guide if both are supported. A Skill explains a typical research and review method without duplicating every parameter definition.

The agent can learn the difference between customer records, draft revisions, review decisions, and published reports. It does not need to inspect the service's database or navigate a dashboard to find these facts.

## Capabilities

| Capability | What the caller supplies | What the service owns |
| --- | --- | --- |
| Search customer records | Time range, account scope, relevant filters | Authorization, search limits, dated records and references |
| Create reporting work | Objective, scope, source selection, applicable limits | Accepted direction, work identity, execution state |
| Read work | Work identity | Current facts, pending decisions, available artifacts |
| Read or revise a draft | Draft identity; expected revision for a write | Content, revision, provenance, conflict checks |
| Record a review decision | Decision, subject revision, authorized actor context | A decision bound to its subject and scope |
| Publish a revision | Exact revision, required authority, repetition identifier if supported | Validation, external visibility, publication record |
| Request cancellation | Work identity | Whether work can stop and which effects remain |

A caller's actor field is descriptive data. The actual decision authority is checked using authenticated context and policy.

## A complete path

1. The agent discovers the relevant capabilities and obtains the access required to read the selected records and prepare a draft. A publication grant is not inferred from permission to prepare.
2. The service returns records with their scope and freshness. Search truncation is explicit. The agent narrows the query or retrieves more records when needed.
3. Reporting work is accepted. Its response identifies the work and provides a status path; acceptance is not reported as report completion.
4. A draft becomes available with source references and its known coverage limits. The person can open a view or retrieve the document directly.
5. The person says, "Focus on paying customers," and edits one paragraph. The new direction and edit become part of the work. A later write based on the old draft revision returns a conflict, allowing the agent to reread and prepare a revised update.
6. Review concerns a specific revision. If that revision changes before publication, the service requires the applicable decision to be re-evaluated. A prior grant that still covers the same action and conditions need not prompt again.
7. Publication returns a durable reference to the published revision. The person and agent can inspect what was made visible and where.

## Failure and correction paths

**Response lost after publication.** Publication may have succeeded. The agent checks the publication record or safely repeats the request under the documented deduplication contract. The service states the key's scope and retention. After that guarantee expires, the caller must not assume a repeat is safe.

**Source disappears.** The draft identifies the missing source and coverage gap. It can cite a lawfully retained snapshot if one exists and is accessible. A source link alone does not guarantee permanent evidence.

**Partial external delivery.** If publication includes several destinations, the record identifies each known result. One failed destination does not erase a successful one. Correction or withdrawal is a separate operation with its own limits.

**User cancels during work.** The service records the request and later reports whether execution stopped. Existing drafts remain according to retention policy. Publication that already occurred is not described as undone.

**Connection or host changes.** An authorized caller can retrieve the work identity, accepted direction, decisions, state, and artifacts. Raw conversation history or private model reasoning is not the only continuation mechanism.

**Access is revoked.** Later operations enforce the revised grant at the stated boundaries. The service explains whether active work stops, pauses, or can finish an already committed effect.

## Results in several environments

An MCP host may embed a report view. A CLI client may return the artifact reference and a concise state record. An HTTP client may retrieve the same revision directly. The selected supported paths use consistent domain facts and access rules.

A view can help the person compare draft revisions. The agent can receive a compact description and request a diff when needed, without loading the entire rendering payload.

## What to evaluate

Assess all core requirements whose conditions apply. Select HTTP, MCP, instructions, and presentation profiles only if those interfaces are part of the actual product claim. Optional interfaces do not become required because they appear in this example.

Evaluate the complete path, stale approvals, lost responses, private artifact access, human edits, budget limits, and disconnection. Record untested behavior as not evaluated. Use the [assessment template](assessment-template.md); this example does not supply implementation evidence.
