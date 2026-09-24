# Reporting service example

English | [简体中文](../zh-CN/examples/reporting-service.md)

This design applies the [application model](../docs/application-model.md) and [core specification](../spec/core.md) to continuing work. It is **not implemented or evaluated**. Capability names are not prescribed commands or endpoints.

## User task and environment

A user asks their agent:

> Prepare a report of this week's customer problems. Give me a draft to review before publication.

The remote service reads authorized records, maintains drafts, and publishes approved revisions. It may use a deterministic builder or an internal research agent.

Publication requires the designated reviewer's personal decision. The reviewer may be the requester or another authorized user. Preparation or publication access does not supply that decision.

## Product discovery

Here, the agent can search an authorized directory of company applications. It searches from the user's reporting need; the request supplies no product name or service address. The service's entry describes editable drafts built from customer records, source references for checking them, supported sources, access conditions, and the review required before publication. It links to the product's entry point.

The agent can judge whether the service fits the request before using it. Incompatible sources or access conditions may be reasons to choose another product. The directory is an illustrative discovery route, not a required architecture.

## Capabilities and context

The entry point explains scope, provider, access paths, requirements, and charges. Authorized reads supply source records, work state, drafts, and decisions. Guidance links to operation contracts and gives a recommended path through source selection, drafting, review, and publication, with conditions and result checks.

| Capability | What the caller supplies | What the service owns |
| --- | --- | --- |
| Search customer records | Time range, account scope, relevant filters | Authorization, search limits, dated records and references |
| Create reporting work | Objective, scope, source selection, applicable limits | Accepted direction, work identity and revision, execution state |
| Read work | Work identity | Accepted direction and revision, execution facts, pending decisions, available artifacts |
| Revise reporting direction | Work identity, expected work revision, revised objective or source scope | Validated direction and revision; declared effects on remaining work and the draft |
| Read or revise a draft | Draft identity; expected revision for a write | Content, revision, provenance, conflict checks |
| Record a review decision | Subject revision and evidence from the declared review path | Verified reviewer, decision, subject, and scope |
| Publish a revision | Exact revision, required authority, repetition identifier if supported | Validation, external visibility, publication record |
| Retrieve or export a report | Report identity, revision, requested representation | Authorized content or artifact reference, source revision, publication state, declared export transformations |
| Request cancellation | Work identity | Whether work can stop and which effects remain |

The review path verifies the reviewer's identity, role, and decision through a confirmation the agent cannot perform with delegated access. Account access and caller-supplied actor fields are not proof. The declared review path can convey decision evidence, including through the agent, if its source and scope can be verified.

A direction change reports its effect on remaining work and the draft. It does not by itself rewrite content; that requires a revision-checked update.

## A complete path

1. After finding the service, the agent reads its capability contracts and obtains access to read records and prepare a draft. Preparation access does not imply publication authority.
2. It reads scoped, dated records. Explicit truncation leads it to narrow the query or retrieve further detail.
3. The service accepts work and returns an identity and status path, not a claim of completion.
4. The requester receives a draft with source references and coverage limits, available as a view or document.
5. The requester says, "Focus on paying customers," and saves an edit to one paragraph. The agent updates the accepted direction using the observed work revision, then reads the current draft before preparing an update. A write based on the old draft revision returns a conflict. The agent reconciles the new scope with the requester's saved edit before committing revised content.
6. The designated reviewer examines the revision, coverage, audience, and uncertainty, then approves or refuses through the review path. Changed subjects or conditions require re-evaluation. A verified decision remains reusable within its scope; general delegation cannot replace a review that never occurred.
7. After approval and authority checks, the agent requests publication. The service returns a durable reference showing what was published and where.
8. After a conversation change, an authorized agent retrieves the work identity, direction, decisions, and results without relying on private model reasoning.
9. The requester exports the report, then uses the access-management handoff to revoke delegated access and verify its status. The policy states retention and active-work disposition. Disconnection, revocation, and withdrawal of a report remain distinct.

## Failure and correction paths

**No personal decision.** Even with publication access and a ready draft, the agent cannot publish without the required decision. The service identifies the pending handoff. An authenticated user without the reviewer role cannot approve; absent, refused, or unverifiable approval blocks publication.

**Agent claims approval.** The service rejects the agent's assertion as decision evidence. Relayed evidence is accepted only when its source, subject, and conditions can be verified.

**Response lost after publication.** Check the publication record or repeat safely within the documented deduplication scope and retention. After that guarantee expires, do not assume repetition is safe.

**Source disappears.** Identify the coverage gap. Cite a retained snapshot only if lawfully retained and accessible; a source link alone does not guarantee lasting evidence.

**Partial external delivery.** Record each destination's known result. A failed destination does not erase a successful one; withdrawal is a separate operation with limits.

**User cancels during work.** Record the request, then whether it took effect. Retain drafts under the stated policy; cancellation does not undo publication.

**Access is revoked.** Later operations enforce the revised grant. The policy states whether active work stops, pauses, or finishes an already committed effect.

## Human views and continued use

Views show source coverage, draft differences, and decisions on the same revisions agents use. Unsaved edits remain distinct from committed changes.

The agent can request a compact state record or diff instead of the rendering payload. Exports identify their source revision and any material information loss for the next application.

## Requirement mapping and evidence

Use the [interface guides](../spec/interfaces.md) for the access paths and supporting behavior used in the task.

| Part of the case | Core requirements |
| --- | --- |
| Complete agent use path | [Scope and coverage](../spec/core.md#scope-and-coverage) |
| Product discovery and fit | AN-01 |
| Capabilities and source selection | AN-02, AN-03 |
| Authority, review, and publication | AN-04, AN-06, AN-09 |
| Accepted work, direction changes, and continuation | AN-05, AN-06, AN-07 |
| Lost responses and partial effects | AN-05, AN-06 |
| Drafts, exports, and human changes | AN-08, AN-09 |
| Versions, costs, and leaving | AN-01, AN-02, AN-04, AN-07, AN-08 |

Record implementation evidence using the [evaluation procedure](../spec/evaluation.md) and [assessment template](assessment-template.md). No passing results are claimed here.
