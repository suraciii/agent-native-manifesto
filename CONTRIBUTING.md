# Contributing

Bring a concrete use case, a counterexample, or evidence from an application. Explain the work, the current difficulty, and the result a proposed change should enable.

## Where changes belong

- `README.md` states the manifesto, definition, and reading path.
- `docs/foundations.md` explains the philosophical position and owns the person–agent–application interaction model.
- `docs/application-model.md` derives product design priorities, product forms, and the full use cycle; it also defines terms.
- `docs/references.md` identifies sources and their limits.
- `spec/core.md` owns the shared requirements.
- `spec/interfaces.md` owns interface selection and composition; `spec/interfaces/*.md` own the individual profile requirements and their design analysis.
- `spec/evaluation.md` owns the evaluation procedure.
- `examples/` connects tasks, capabilities and context, agent use, human participation, and outcomes to requirements and evidence status.

Use simple English and one term for one meaning. Separate normative requirements from rationale, examples, and cited external standards. Keep requirements observable and give conditional requirements an explicit scope.

Connect philosophical claims to product design choices before turning them into requirements. Keep the philosophical argument focused on applications designed first for agent use. Place engineering detail in the specification and distinguish illustrative cases from verified implementation evidence.

For a requirement change, explain the affected scenario, simpler alternatives, interface consequences, and how it can be evaluated. Update its evaluation coverage and relevant examples. Keep shared domain rules in the core and link to them from topics. A topic should be independently useful, with its role, design choices, requirements, examples, verification cases, and primary sources. A new wire format or convention needs a concrete interoperability problem that existing standards do not solve well.

Preserve requirement identifiers when their meaning is unchanged. Do not silently reuse an identifier for an unrelated obligation. Assessments identify the specification commit, so claims remain tied to the version actually examined.

## Check a change

Run from the repository root:

```sh
python3 scripts/check_docs.py
```

Review the semantics as well: follow a complete use path, consider failure after an effect but before a response, and check whether a small local application can still satisfy the applicable requirements without unnecessary infrastructure. Assess a CLI-only tool and a host exposing functions directly; neither should need HTTP or SDK packaging. Treat file inputs and outputs as supporting contracts, and document file-driven behavior only when the application offers it.

The document check validates local links, requirement references across `spec/`, and JSON example syntax. It does not run applications, validate example payloads against external schemas, or verify external protocols. A claimed behavior needs separate evidence under the evaluation procedure.

Keep transient research, progress logs, and private environment information out of the specification. Use issues or pull requests for discussion and redact secrets and private data from evidence.

## Rights

Contribute only material you have the right to share. Contributions of prose use the repository's [CC BY 4.0 terms](LICENSE); code uses the [MIT License](LICENSE-CODE). Credit external ideas and link to source specifications. Do not copy third-party material under the assumption that this repository's license applies to it.
