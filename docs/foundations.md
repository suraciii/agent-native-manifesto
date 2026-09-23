# Foundations

English | [简体中文](../zh-CN/docs/foundations.md)

Users increasingly interact with applications through agents. A user can state a need in natural language without choosing the software that will meet it. The agent may find suitable applications, interpret their capabilities, organize operations, and return results. The user addresses the agent; the agent finds and uses applications on the user's behalf.

In direct use, a user judges what a product offers and connects a purpose to its concepts, operations, and current state. Delegation can transfer part of this work to the agent, including the search for a suitable product. The application continues to serve the user's purposes through an agent's judgment and action.

In a model-based agent, this relation is mediated by the model's input. The model does not receive an application's internal capabilities directly. It judges an operation through what the application makes available in that input: interface descriptions, schemas, workflow Skills, current facts, tool results, and feedback. A callable operation that cannot be understood or selected from available input is technically present but practically absent from the agent's work.

An application does not control the whole input or guarantee a model's understanding. It is responsible for the part that describes its own capabilities, state, conditions, effects, and limits. That material may enter through initial instructions, retrieval, tool calls, or later results. It need not all be loaded at once, but it must be truthful, current, usable, and retrievable when needed.

The [Agent Native Manifesto](../README.md) begins from this changed relation: design applications first for agents acting on behalf of users.

## Applications must attract the attention of users' agents

Building a capability does not make it a means the agent will consider. The product may be ready to answer a call while giving the agent no reason to make one. Making a capability exist and making its usefulness recognizable are different parts of application design.

An agent seeking software on a user's behalf brings the user's task and constraints to that search. The application must meet it there: in the channels it can reach, with a clear account of the help the product can offer. It cannot present only its internal structure and leave the agent to infer why the product matters.

A reporting application can list its commands and protocols, or explain how it turns scattered customer feedback into a draft whose sources can be checked and whose contents can be revised. The first describes how the product is arranged; the second connects its capabilities to the user's work. Details of invocation remain necessary, but an agent should not have to read an interface manual before it can see why the product might help.

The developer wants the product to be chosen; the user's agent seeks suitable means for the task. The design must connect these interests: let the agent recognize the product when its help is relevant, and provide the help that attracted it.

## Applications deliver model context with capabilities

An operation can be delegated while the work of understanding it remains with the user. An application may offer a call but leave its conditions unexplained. It may hold state the user must read and repeat, or announce success without making the result available for examination. In each case, the user must keep interpreting the application for the agent. The operation is handed over; part of the work returns as explanation, checking, and repair.

The application already holds part of what the agent needs to know: what an operation means, under which conditions it can be used, what it changes, and what state the work is in. Providing the knowledge needed for use is part of providing the capability. For a model-based agent, that knowledge becomes effective only when it can enter the model's input. The application does not merely expose a callable interface; it provides the material by which that interface can enter the agent's judgment.

The application is not responsible for the whole prompt or for guaranteeing the model's choice. It is responsible for making its own usage conditions available in forms the host or agent can place in the input. The forms may be interface descriptions, workflow Skills, current state, or tool results; the responsibility is not tied to any one format.

Context has value through the judgment and action it supports. The agent selects and interprets it in relation to the user's task.

A method also carries judgments about what matters. A rule may select the sharpest photographs and exclude the only image of someone the album is meant to remember. It succeeds by its own measure while failing the purpose it was meant to serve. A criterion for choosing the means has begun to decide the end. Guidance must therefore make its assumptions available for judgment. It can offer a way of working; it cannot grant permission or settle the user's purpose. The application still enforces the rules and authority it controls.

## Applications contribute to work that extends beyond them

In a task that spans applications, an agent can arrange their capabilities around the user's purpose. An application's result can become material for further work.

Each application remains responsible for its own operations and effects. Its value in the wider activity depends on the capabilities and knowledge it contributes, and on whether its results can be used by the authorized caller. A complete workflow or a small operation can each serve the next intended step.

## Human interfaces must not gate agent use

Agent Native does not mean removing a human interface. It means that a human-oriented operation path must not be the condition for using the application's capabilities. If an agent must navigate screens, infer meaning from layout, or imitate clicks, the application is asking it to reproduce a human path rather than providing a direct Agent path. The translation work returns to the agent and, when it fails, to the user.

Human views have a different but necessary role. They show results and evidence, and let users inspect, edit, decide, redirect, or take over the same work. They may be rich or complex when the work requires visual judgment. Complexity is not the issue; making application navigation the only place where capabilities and state are available is. Agent operations and human views must meet at the same domain state, so committed human changes enter later model input and agent operations.

## Participation needs practical power

Delegation changes the user's access to what happens. The agent selects facts, interprets results, and makes some decisions on their behalf. The application must make the results and their consequences available for human judgment.

A user may be consulted at every step and still lack the facts needed to judge it. A view may confirm that an edit was saved while the next agent operation receives an older version without notice. Frequent consultation can coexist with little control. Control gains practical force when the user's judgment can alter what follows.

Human views let users see, shape, and decide the same work on which agents act. A changed paragraph or a selected photograph can express a purpose more precisely than another instruction. The application must make the committed change available to the agent as part of the current work.

The result can change the purpose that guided it. Successful execution does not settle the value of the result. That remains open to judgment in use. Effects already produced become conditions of further action. A new instruction can direct the next step; it cannot, by itself, undo what has already happened.

## Delegation does not erase responsibility

Delegation changes who performs the work. It does not, by itself, release users from responsibility. An agent may prepare a production deployment correctly while the release approver has yet to decide whether it should happen. Technical readiness does not make that decision.

Where a decision must be made by a human, the application must seek it from the user responsible for that decision. Participation here is a duty, not merely an opportunity to intervene. The agent can prepare the facts and carry out the decision; it cannot substitute its own choice for the user's answer.

Responsibility does not require approval of every step. Users can take responsibility for defined grants of authority. Human approval does not release the application from responsibility for its own rules and effects.

## Interaction model

```mermaid
flowchart LR
    P[User] <-->|Intent, discussion, results| H[Host and user's agent]
    P <-->|Inspect, edit, decide| V[Human views]
    H <-->|Operations and context| A[Application capabilities]
    V <-->|Operations and context| A
    A <--> S[Domain state and artifacts]
```

These are relationships within the same activity. The diagram leaves deployment and storage architecture open.

The user's agent can come from the application or another product. Language understanding can run in that agent or its host.

## From this argument to application design

An agent can sometimes use an application by adapting to a path built for human operation. Its success may show the agent's ability to adapt, rather than the application's support for this use. Agent Native makes the conditions for agent use a responsibility of the product itself. That includes the model input needed to understand and select capabilities; it does not require removing human interfaces or choosing a particular protocol.

Existing tools and API-first products may already supply these conditions. The [application model](application-model.md) develops them into design choices.
