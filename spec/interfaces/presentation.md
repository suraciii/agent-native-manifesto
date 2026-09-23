# Presentation and human participation

English | [简体中文](../../zh-CN/spec/interfaces/presentation.md)

This guide covers views for inspection, editing, comparison, and decisions. It applies the [core requirements](../core.md); application actions still need an [execution path](../interfaces.md).

## Role and fit

Charts, images, and direct editing can communicate more than another instruction. Standalone views can support richer work; embedded views retain conversational context but depend on host support. Choose for the activity.

## Design choices

### Separate facts, interpretation, and rendering

| Part | Example | Responsibility |
| --- | --- | --- |
| Domain fact | Draft revision, publication status, source record | The application that owns the fact |
| Interpretation | Summary, comparison, proposed next action | A user, agent, or program, with a stated basis |
| Rendering | Table, chart, diff, editor | The selected view and host |

Generated views still need sources for business claims. A screenshot does not prove a draft was committed or published.

Separate concise agent context from large rendering payloads. Measure whether the host actually keeps those payloads outside model input.

### Coordinate edits and decisions

Identify the work and revision in the view. Show drafts, saved revisions, and publication as distinct states. Hand off unsaved changes explicitly; use refreshed reads, revision conflicts, or events to expose committed edits to the agent.

Decisions bind to their subject and conditions, checked again at execution. Closing a view does not itself cancel work or revoke authority.

A browser click cannot prove personal participation if an agent can perform it through the same session. Use the verified decision path under AN-04 and decision context under AN-09.

### Standalone and embedded delivery

[MCP Apps](https://apps.extensions.modelcontextprotocol.io/api/documents/overview.html) links tools to UI resources with host-mediated communication and sandboxed rendering. It also describes use in hosts without UI support.

Host display policy and application authority checks still apply. State host support, access conditions, and any link expiry. Where embedding is unavailable, a standalone handoff needs working authentication and a path back to the shared work.

### Make human participation usable

Use clear language and focused controls, with keyboard and nonvisual access. The [WAI-ARIA dialog pattern](https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/) explains focus placement, keyboard behavior, and focus return. A role label alone does not implement them. Prefer suitable native controls to unnecessary custom interaction.

## Example

In the illustrative [reporting service](../../examples/reporting-service.md), saving a paragraph creates a draft revision, not a publication. The agent rereads it before proposing publication.

The designated reviewer, possibly another user, sees the revision, audience, source coverage, and uncertainty. Their decision uses the verified path; a later edit triggers the revision and decision checks.

Without embedding, an authorized standalone page supports the same review. The agent retrieves the resulting state through the work reference.

## Verification

| Focus | Cases to try |
| --- | --- |
| Shared facts and human actions | Stale display; unsaved edits; human-agent concurrent changes; changed approval subject; agent-operated confirmation; responsible reviewer; keyboard and assistive interaction |
| Delivery and access | Unsupported embed; expired or private link; closed view during work; sandbox boundary; resumption after standalone editing |

Ask users to inspect a consequence, correct a mistake, and continue the work under the [evaluation procedure](../evaluation.md).

## Sources and related topics

- [MCP Apps overview](https://apps.extensions.modelcontextprotocol.io/api/documents/overview.html): UI resources, host communication, and progressive enhancement. Assess the specific extension and host versions in use.
- [WAI-ARIA modal dialog pattern](https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/): an established example of accessible interaction behavior.
- Related topics: [MCP](mcp.md), [HTTP](http-api.md), and [files and artifacts](files-and-artifacts.md).
