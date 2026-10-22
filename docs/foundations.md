# Foundations

English | [简体中文](../zh-CN/docs/foundations.md)

Users increasingly interact with applications through agents. A user can state a need in natural language without choosing the software that will meet it. The agent may find suitable applications, interpret their capabilities, organize operations, and return results. The user addresses the agent; the agent finds and uses applications on the user's behalf.

In direct use, a user connects a purpose to a product's concepts, operations, and current state. Delegation can transfer part of this work to an agent. The application continues to serve the user's purposes through that agent's judgment and action. The [Agent Native Manifesto](../README.md) begins from this changed relation.

## A design lineage: from the shell to the agent

Agent Native continues the Unix composition stance: small capabilities that each do one thing well, a common way to connect them, and composition that produces uses no single part was designed for. In Unix, the shell composes, and the person at the shell answers for the result. Agent Native gives the shell's seat to the user's agent: it holds the user's purpose, finds applications, and composes their operations and results at runtime. That composition requires connections that carry meaning without owning it, and applications that describe themselves and answer for their effects.

## The conditions of delegated use

The principles in this document rest on one question: what must be true for an application to serve a user who acts through an agent?

Three premises and one observation answer it. The argument begins with a relation: the agent is the proximate caller; its standing comes from the user's authorization, not from a claim of its own.

**Purpose.** For work, an application is a means. Its value comes from the user's purpose, not from its own boundary. A means that cannot be reached is not a means.

**Knowledge.** Action requires knowledge of the means and of the situation. An operation that cannot be understood, or whose current state cannot be known, is callable but not usable. Contract knowledge and current facts are different objects; neither substitutes for the other.

**Responsibility.** Delegation transfers execution and bounded decision rights, not responsibility for the purpose. A system can execute a decision; it cannot answer for the purpose. Responsibility requires a subject that can bear it. The person who authorizes the work remains answerable for the purpose and for the decisions reserved to them.

**Work.** Work is not necessarily bounded by application boundaries. Application boundaries are administrative; the user's purpose is not. When work continues elsewhere, the result must carry its meaning, origin, scope, and authorized access with it.

These give four conditions of delegated use:

| Condition | What it requires | Scope |
| --- | --- | --- |
| Reachable | The agent can find the application and reach the operation through a supported path. | Every delegated use |
| Intelligible | The application makes the operation's meaning, effects, and current state available under warrant, with its conditions and limits. | Every delegated use |
| Continuable | A result can enter the next step without the next application reconstructing its meaning, origin, scope, or authorized access. | When work continues elsewhere |
| Accountable | The action is attributable to an authorized principal, reserved decisions are verified, and effects can be inspected and, where possible, corrected. | When an action has effects or a decision is reserved |

The first two conditions are unconditional within delegated use. The last two are conditional: not every task continues elsewhere, and not every task reserves a decision. Stating the condition is part of the claim, not a qualification added later. The four are necessary conditions, not sufficient ones: an application can satisfy all four and still be slow, unsafe, or wrong.

The four principles below develop these conditions. "Make the product discoverable by the user's agent" elaborates reachability. "Make the operation legible, not just callable" elaborates intelligibility. "Preserve meaning, origin, and authorized access across boundaries" elaborates continuability. "Delegate action; keep judgment effective" elaborates accountability.

An application can be reachable and intelligible without being continuable. It cannot be used without the first two.

### What the argument does and does not establish

The argument establishes three things:

- An application that cannot be reached or understood cannot serve delegated work, whatever its internal quality.
- A result that loses its meaning, origin, scope, or authorized access at the boundary shifts reconstruction cost to the next application and to the user.
- Responsibility for a reserved decision cannot be transferred to an agent's assertion.

It does not establish:

- that agents should outrank human users in design conflicts;
- how much discovery, interoperability, or approval an application should provide;
- which decisions a product reserves for a human;
- that every task needs a human in the loop.

Those are product and policy choices. They need product and policy reasons, not philosophical necessity.

### Boundaries

The argument concerns work delegated to an agent, not every use of software. Direct use, play, art, and exploration need not satisfy these conditions in the same way.

Reachability does not require a public registry. Intelligibility does not require every detail in one document. Continuability does not require every result to be portable. Accountability does not require approval of every step; it requires that reserved decisions are identified, verified, and correctable.

A local tool that ends when its process ends is reachable, intelligible, and accountable, but not continuable, because no work continues. An application that refuses an action until a required decision is made is accountable, not broken.

### Open questions

- Is the unit of design the application or the work? The application is the design object; the use relation is the evaluation object.
- Does human judgment mean setting the purpose, approving reserved decisions, or bearing final responsibility? The argument supports the first and third; the second is a product choice.
- Is trust a fifth condition, or a consequence of intelligibility and accountability? This document leaves the question open.

## Make the product discoverable by the user's agent

Building a capability does not make it a means the agent will consider. The product may be ready to answer a call while giving the agent no reason to make one. Making a capability exist and making its usefulness recognizable are different parts of application design.

A user's agent seeking software brings the user's task and constraints. The application must meet it in reachable channels, with a clear account of the work it helps accomplish and the conditions that affect fit. The developer wants the product to be chosen; the user's agent seeks suitable means. The design connects these interests by delivering the help that attracted the agent.

Once chosen, the application needs a complete path through operations, current facts, results, and exceptions. Delegated work should not require the agent to navigate screens, infer meaning from layout, or imitate clicks. These demands make it reconstruct the application's use from a path designed for human operation.

Human-only access steps and reserved decisions remain valid handoffs. They identify who must act, what is needed, and how the caller learns the result. A missing operation cannot become a valid handoff merely by asking a user to perform it for the agent.

## Make the operation legible, not just callable

An operation can be delegated while the work of understanding it remains with the user. An application may offer a call but leave its conditions unexplained. It may hold state the user must read and repeat, or announce success without making the result available for examination. The operation is handed over; part of the work returns as explanation, checking, and repair.

For a model-based agent, application knowledge informs judgment through the model's input. Descriptions, schemas, Skills, current facts, and tool results become context when included in that input. Stored material needs a usable path into it. A callable operation that cannot be understood or selected from available input is technically present but practically absent from the agent's work.

The application supplies material that accurately describes its capabilities, state, conditions, effects, and limits. The agent selects and organizes it into model input as needed. It need not all be loaded at once. The application does not control the whole input or guarantee the model's judgment; it remains responsible for making its own material clear, current, and accessible. An application that also supplies the user's agent takes on that agent's responsibilities too.

The application already knows much of its own use. Clear guidance makes that knowledge directly usable: where to start, which conditions matter, how to check results, and how to recover from known failures. Agents can organize work on this basis without repeatedly guessing hidden rules. Stable mechanical steps can be performed by the application itself. Important choices remain available for judgment and adaptation to the user's purpose.

A method also carries judgments about what matters. A rule may select the sharpest photographs and exclude the only image of someone the album is meant to remember. It succeeds by its own measure while failing the purpose it was meant to serve. A criterion for choosing the means has begun to decide the end. Guidance must therefore make its assumptions available for judgment. It can offer a way of working; it cannot grant permission or settle the user's purpose. The application still enforces the rules and authority it controls.

## Preserve meaning, origin, and authorized access across boundaries

In a task that spans applications, an agent can arrange their capabilities around the user's purpose. An application's result can become material for further work.

Each application remains responsible for its own operations and effects. Its value in the wider activity depends on the capabilities and knowledge it contributes, and on whether its results can be used by the authorized caller. A complete workflow or a small operation can each serve the next intended step.

A result should carry its meaning, origin, scope, and authorized access, so the next application does not have to reconstruct them.

## Delegate action; keep judgment effective

Delegation changes the user's access to what happens. The agent selects facts, interprets results, and makes some decisions on their behalf. Human views make results and consequences available for inspection, editing, and judgment. They may be rich or complex when the work requires it. A changed paragraph or a selected photograph can express a purpose more precisely than another instruction.

A user may be consulted at every step and still lack the facts needed to judge it. A view may confirm that an edit was saved while the next agent operation receives an older version without notice. Control gains practical force when the user's judgment can alter what follows. Agent operations and human views must use the same domain state. The application makes committed changes available to later operations; the agent includes relevant changes in model input as needed.

The result can change the purpose that guided it. Successful execution does not settle the value of the result. That remains open to judgment in use. Effects already produced become conditions of further action. A new instruction can direct the next step; it cannot, by itself, undo what has already happened.

Delegation does not, by itself, release users from responsibility. An agent may prepare a production deployment correctly while the release approver has yet to decide whether it should happen. Where a decision is reserved for a human, the application must seek it from the responsible user. The agent can prepare the facts and carry out the decision; it cannot supply the user's answer.

Responsibility does not require approval of every step. Users can take responsibility for defined grants of authority and choose how much to delegate. Human approval does not release the application from responsibility for its own rules and effects.

## Interaction model

```mermaid
flowchart LR
    P[User] <-->|Intent, discussion, results| G[User's agent]
    P <-->|Inspect, edit, decide| V[Human views]
    G <-->|Operations and model input material| A[Application capabilities]
    V <-->|Facts, edits, and decisions| A
    A <--> S[Domain state and artifacts]
```

These are relationships within the same activity. The diagram leaves deployment and storage architecture open.

The user's agent can come from the application or another product. Language understanding can run in that agent.

## From this argument to application design

Agent Native treats these conditions as responsibilities of the people who design and operate the product. This includes clear guidance and the material needed for model input, direct paths for delegated work, results that carry work forward, and effective human participation. It does not require a particular protocol or the removal of human interfaces.

Existing tools and API-first products may already supply these conditions. The [application model](application-model.md) develops them into design choices.
