# Foundations

The [manifesto](../README.md) states the product direction. This document explains its reasoning. The [core specification](../spec/core.md) defines requirements.

## A changed relation of use

A person can delegate the use of software to an agent. The agent interprets the task, chooses capabilities, connects operations, and responds to feedback. The application now serves an immediate user that works through descriptions, tools, context, and results.

This changes product design. Navigation that helps a person explore a screen can impose needless work on an agent. A business rule still matters when the screen disappears. Applications need to expose the useful operation and preserve the rule.

Existing tools already supply many of these conditions. A well-designed CLI can support delegated use better than a new application with a chat box. Conversely, adding a callable endpoint leaves gaps if the agent cannot find relevant objects, understand effects, or verify the outcome.

API-first design provides a programmatic boundary. Agent-native design also considers how an agent learns that boundary, selects a capability for a purpose, works with limited context, handles uncertainty, and returns results to human judgment.

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
| Interface profile | Requirements for exposing capabilities through a particular kind of interface |

"The user's agent" describes a representative role. It does not establish ownership, identity, or permission by itself. Authority comes from the applicable user grant and access policy.

The same agent can use an application and be invoked by another program. A product can offer its own agent as well as serve external agents. These roles can coexist without requiring a second copy of domain rules.

## Purpose develops through use

A person may begin with an incomplete idea. Discussion and practical results help clarify it. Good delegation requires enough direction to act responsibly, but it does not require a complete plan for every future condition.

An application should support changes in requirements while work proceeds. An agent may propose a change and explain the trade-off. A proposal becomes a decision only through the authority that can make it.

A passing check establishes the property that check examined. It does not establish that the whole product serves the person's purpose. Review must connect requirements, artifacts, and consequences in use. People need the means to question that connection, even when no system reports an error.

## Judgment and executable rules

Programs preserve rules within the operations they control. A publication operation can check that the caller has permission and that the approved revision is still current. An agent can judge which material is useful to publish within its delegated authority.

This boundary makes stable rules easier to test and frees attention for judgment. It does not make the entire activity predictable. External observations can change, rules can be wrong, and judgments can be inadequate.

Tool granularity follows responsibility. One conceptual action may require many internal steps. A tool can hide those steps while exposing the choices its caller needs. A workflow can itself be a capability when its behavior is useful and clear.

Compare two extremes:

- Raw storage operations can force every caller to reconstruct the same domain rules and join the same data.
- A single opaque "do everything" operation can conceal decisions, effects, and opportunities to correct the work.

Prefer the smallest set of meaningful capabilities that handles the intended work and remains useful in new combinations. Evaluate both routine and unexpected cases.

## The application serves a user's work

The person can remain in a preferred agent, editor, or conversation while using several applications. Useful access should not depend on adopting each application's own agent or navigating its home page.

A product still needs to be identifiable and understandable. Discovery includes its purpose, provider, limits, access conditions, and entry points. Search engines, directories, package registries, and explicit user links can all provide discovery. None is universally available.

A host controls which products it exposes and how it selects them. An application should provide inspectable descriptions that let people and hosts make informed choices. This project does not assume a neutral global directory or automatic discovery by every agent.

## Human interfaces remain part of the work

Graphs, editors, timelines, maps, and direct manipulation can express intent or reveal relationships more effectively than a conversation. People may participate because they value the activity itself.

A human interface can be a standalone application, a link to an artifact, or a view embedded in the host. Its actions should operate on the same domain facts as the agent's actions, subject to the appropriate authority. Relevant human changes must reach later agent work.

Interface parity means access to intended business outcomes. It does not require a tool for every click, pixel, or gesture. Personal authentication, consent, or a decision reserved to a person can remain human steps, with explicit handoffs.

## Improvement through experience

Applications and their use can improve through verified methods, better tools, clearer instructions, and new checks. The next task can benefit from earlier work without every task creating a memory or modifying software.

Retained context needs scope, provenance, a useful lifetime, and a way to correct it. A generated lesson is a candidate for verification. It must not silently become authority over future users or new tasks.

Automatic self-modification is optional. Stable programs and ordinary releases can support the same direction.

## What this project commits to

The manifesto describes a direction for applications. The specification makes selected obligations concrete. Neither requires the disappearance of graphical interfaces, universal autonomy, a particular model, or adoption of every new agent protocol.

The intended benefit is useful action with less unnecessary explanation and coordination, while preserving informed participation. Success depends on actual use and its consequences.
