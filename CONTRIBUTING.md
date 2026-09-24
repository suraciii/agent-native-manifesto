# Contributing

English | [简体中文](zh-CN/CONTRIBUTING.md)

Bring a concrete task, counterexample, or evidence from use. Explain the current difficulty and the result a change should enable.

## Where changes belong

- `README.md`: manifesto, definition, and reading path.
- `docs/foundations.md`: argument and the single interaction diagram.
- `docs/application-model.md`: design choices and terms.
- `docs/references.md`: sources and their limits.
- `spec/core.md`: shared obligations.
- `spec/interfaces.md`: interface selection and composition. Individual guides explain design choices, examples, sources, and checks that apply the core requirements.
- `spec/evaluation.md`: task evaluation and evidence.
- `examples/`: complete use paths, requirement mappings, and the assessment template.

Use simple English or concise, natural Chinese, with consistent terms. Keep each explanation in its owning document and link to it elsewhere. Retain examples that show a distinct choice or boundary rather than repeat a rule.

Connect application design choices to concrete tasks before turning them into requirements. Separate obligations, rationale, illustrations, and outside standards. Make requirements observable and their conditions explicit.

For a requirement change, explain the scenario, simpler alternatives, interface consequences, and evaluation method. Update affected examples and checks. Preserve identifiers unless the obligation changes; never reuse one for an unrelated meaning. Assessments remain tied to a specification commit.

A new format or convention needs an interoperability problem that existing standards do not solve.

## Translations

English is the content baseline. Simplified Chinese reader documents mirror the same paths under `zh-CN/`, including this guide. Share the root licenses, repository instructions, and scripts.

Update corresponding translations in the same change as the original. If translation reveals a problem in the original, correct both versions. Keep scope, negation, requirement levels, and evidence limits aligned; fluent wording must preserve the meaning.

Use the existing Terms section for terminology, with English terms alongside Chinese translations. Preserve Agent Native, Agent, requirement identifiers, uppercase requirement words, code examples, protocol fields, and source URLs. Translate explanations and diagram labels without changing their meaning or structure.

Put the language switch below each title and link to the corresponding page. Internal document links stay within the selected language; update anchors when headings change. Chinese pages link to the shared licenses at the repository root.

## Check a change

Run from the repository root:

```sh
python3 scripts/test_check_docs.py
python3 scripts/check_docs.py
```

The checker validates local links, structure, requirement definitions and evaluation coverage in each language, matching requirement identifiers across languages, document pairs, language switches, and JSON syntax. It does not check translation meaning, external links, protocol schemas, or application behavior. Review translations against the original as well.

Also review meaning: follow a complete use path, include failure after an effect but before its response, and check that local tools and in-process functions do not acquire unnecessary servers, SDK packages, or task systems. File inputs and outputs are supporting contracts; file-triggered behavior needs an explicit contract only when offered.

Keep transient research and progress in issues or pull requests. Remove credentials and private data from published evidence.

## Rights

Contribute only material you have the right to share. Prose uses [CC BY 4.0](LICENSE); code uses [MIT](LICENSE-CODE). Credit external ideas and respect their sources' licenses.
