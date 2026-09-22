# Contributing

Bring a concrete use case, a counterexample, or evidence from an application. Explain the work, the current difficulty, and the result a proposed change should enable.

## Where changes belong

- `README.md` contains the manifesto and its definition.
- `docs/` explains the reasoning, product forms, and sources.
- `spec/core.md` owns the shared requirements.
- `spec/interfaces.md` owns interface-specific requirements.
- `spec/evaluation.md` owns the evaluation procedure.
- `examples/` illustrates use and records no implied implementation claims.

Use simple English and one term for one meaning. Separate normative requirements from rationale, examples, and cited external standards. Keep requirements observable and give conditional requirements an explicit scope.

For a requirement change, explain the affected scenario, simpler alternatives, interface consequences, and how it can be evaluated. Update its evaluation coverage and relevant examples. A new wire format or convention needs a concrete interoperability problem that existing standards do not solve well.

Preserve requirement identifiers when their meaning is unchanged. Do not silently reuse an identifier for an unrelated obligation. Assessments identify the specification commit, so claims remain tied to the version actually examined.

## Check a change

Run from the repository root:

```sh
python3 scripts/check_docs.py
```

Review the semantics as well: follow a complete use path, consider failure after an effect but before a response, and check whether a small local application can still satisfy the applicable requirements without unnecessary infrastructure.

The document check does not run applications or validate external protocols. A claimed behavior needs separate evidence under the evaluation procedure.

Keep transient research, progress logs, and private environment information out of the specification. Use issues or pull requests for discussion and redact secrets and private data from evidence.

## Rights

Contribute only material you have the right to share. Contributions of prose use the repository's [CC BY 4.0 terms](LICENSE); code uses the [MIT License](LICENSE-CODE). Credit external ideas and link to source specifications. Do not copy third-party material under the assumption that this repository's license applies to it.
