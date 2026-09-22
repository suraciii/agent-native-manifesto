# Presentation and human participation

Presentation lets users inspect, edit, compare, and decide within delegated work. A useful view may be a document, a graph, an editor, a standalone application page, or an interactive surface in the agent's host.

This is a supporting profile governed by the [core specification](../core.md). It needs an appropriate [execution path](../interfaces.md) for application actions. Human control depends on usable interaction and actual domain effects, not on the presence of a confirmation button alone.

## Role and fit

Direct interaction is useful when spatial relationships, visual detail, comparison, or repeated edits matter. A chart can reveal a pattern more clearly than a verbal description. Editing one paragraph can express a correction more precisely than explaining it to an agent.

A standalone view can support richer work and more clients. An embedded view can preserve conversational context and reduce navigation. It also depends on the host's rendering, access, and interaction support. Either can fit an Agent Native application.

## Design choices

### Separate facts, interpretation, and rendering

| Part | Example | Responsibility |
| --- | --- | --- |
| Domain fact | Draft revision, publication status, source record | The application that owns the fact |
| Interpretation | Summary, comparison, proposed next action | A user, agent, or program, with a stated basis |
| Rendering | Table, chart, diff, editor | The selected view and host |

An agent-generated view can be useful. Its claims about prices, permissions, revisions, and effects still need a source. A screenshot of an edited draft does not establish that the change was committed or published.

Send concise state and relevant references to the agent. Large rendering payloads can go to the view through a suitable path. This can reduce context use, but only if the actual host keeps those payloads out of the model's input; do not assume protocol fields alone guarantee that behavior.

### Coordinate edits and decisions

Show whether content is a local draft, a saved revision, or a published result. A user's unsaved edits do not automatically exist in the application's committed state. A later agent operation needs the committed revision or an explicit handoff of pending changes.

A review action should identify the object, revision, and consequences being approved. If the subject changes before execution, the operation boundary rechecks the applicable conditions. Closing a view does not necessarily cancel ongoing work, and navigation does not revoke authority by itself.

A browser click alone does not prove personal participation if an agent can perform it through the same session. Required human decisions use the verified path defined under AN-04 and the decision context required by AN-09. Displaying a confirmation button does not establish that path.

An agent can learn about a human edit through a refreshed read, revision conflict, or event. Choose a mechanism that fits the work; a single shared conversation is not the only synchronization mechanism.

### Standalone and embedded delivery

[MCP Apps](https://apps.extensions.modelcontextprotocol.io/api/documents/overview.html) provides a concrete model of tools linked to UI resources, host-mediated communication, and sandboxed rendering in supporting hosts. It also describes progressive enhancement for hosts without UI support.

The host remains responsible for its own display and integration policy. The application still checks authority on operations initiated from the view. A rendered button or a view's request to open a URL does not bypass the host or server boundary.

Document which hosts support the required views and what happens elsewhere. A link to a standalone editor can be a useful handoff if the user can authenticate and return the result to the work. An inaccessible link is not a substitute for a usable result.

### Make human participation usable

A decision needs understandable language, a clear subject, and an available way to decline or change direction. Keyboard access, meaningful labels, focus handling, and nonvisual representations matter for users of assistive technology.

The [WAI-ARIA dialog pattern](https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/) illustrates how a modal interaction needs focus placement, keyboard behavior, and focus return. Merely labeling a view as a dialog does not implement those behaviors. These established practices apply inside agent hosts as well as ordinary web applications.

Use native controls and semantics where they fit. Prefer a focused participation surface to forcing every user through an entire product navigation flow.

## Requirements

### UI-01 — Shared facts and human actions

Views MUST identify the relevant work, object, or revision. Displayed claims about business facts MUST be grounded in the application's data. Human actions MUST enforce the appropriate authority and domain rules and make relevant changes available to later agent work.

A view MUST distinguish a proposed action from one already executed. A decision affecting a specific result MUST bind to that result or revision as required by AN-04. Unsaved edits, committed changes, and publication MUST be distinguishable when the view supports those states.

Participation surfaces SHOULD provide accessible labels, keyboard interaction, appropriate focus behavior, and suitable nonvisual access. An assessment SHOULD include the intended users and supported assistive interaction paths.

### UI-02 — Delivery and access

Views MAY be standalone, linked, or embedded. The application MUST state host requirements, access conditions, and any expiry. A host-specific rendering feature MUST NOT silently remove the assessed core outcome on another host claimed as supported; provide a documented handoff or narrow the supported-host claim.

An application using MCP Apps or another UI protocol MUST follow its sandbox and communication requirements for the supported version. Credentials and application authority MUST remain protected at the operation boundary.

Closing or navigating away from a view MUST NOT be presented as cancellation or revocation unless the corresponding application operation took effect. Sensitive artifact links MUST follow AN-08.

## Example

This is an illustrative interaction for the [reporting service](../../examples/reporting-service.md).

The agent presents a draft summary and opens a review view. The view identifies the draft revision and source coverage. The user edits a paragraph locally, then saves. Save commits a new revision; it does not publish the report.

The agent rereads the saved revision before proposing publication. The designated reviewer, who may be a different user, sees the target audience, exact content revision, and known uncertainty. The reviewer's decision follows the service's verified human decision path; the view's presence alone does not prove that the reviewer decided. If another edit occurs before publication, the service enforces the revision and decision contract. The reviewer can inspect the conflict and decide how to proceed.

On a host without embedded views, the reviewer uses an authorized standalone page with the same decision contract. The agent still receives the work reference and can retrieve the resulting state. No display is counted as evidence of a domain effect without that state.

## Verification

| Requirement | Important cases |
| --- | --- |
| UI-01 | Stale display; unsaved edits; human-agent concurrent changes; changed approval subject; agent-operated confirmation; responsible reviewer; keyboard and assistive interaction |
| UI-02 | Unsupported embed; expired or private link; closed view during work; sandbox boundary; resumption after standalone editing |

Ask reviewers to inspect a consequence, correct a mistake, and continue the work. Distinguish chosen participation, required human decisions, and manual repair of an integration failure. Follow the [evaluation procedure](../evaluation.md).

## Sources and related topics

- [MCP Apps overview](https://apps.extensions.modelcontextprotocol.io/api/documents/overview.html): UI resources, host communication, and progressive enhancement. Assess the specific extension and host versions in use.
- [WAI-ARIA modal dialog pattern](https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/): an established example of accessible interaction behavior.
- Related topics: [MCP](mcp.md), [HTTP](http-api.md), and [files and artifacts](files-and-artifacts.md).
