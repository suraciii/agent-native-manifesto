# Assessment template

Use this blank template with the [evaluation procedure](../spec/evaluation.md). Replace placeholders with observed evidence before publishing.

## Scope

| Field | Value |
| --- | --- |
| Application and version | Not supplied |
| Specification commit | Not supplied |
| Assessed business outcomes | Not supplied |
| Excluded outcomes and human handoffs | Not supplied |
| Required human decisions, responsible roles, and verification paths | Not supplied |
| Capability access paths and supporting material | Not supplied |
| Product discovery paths and access conditions | Not supplied |
| Hosts, models, versions, and configuration | Not supplied |
| Environment, identity, and authority | Not supplied |
| Data, limits, and outcome criteria | Not supplied |

## Deterministic checks

For each case: starting state, action or fault, expected and actual results, evidence. Choose relevant cases from the interface guides, including failure boundaries. For required human decisions: source and scope verification, invalid or absent decisions, and valid relayed evidence where supported.

No checks recorded.

## Agent task trials

For each task, record:

- Trial type: product discovery or known-product use; request, input form, starting context, discovery channels or supplied entry point, host and model, and outcome criteria.
- Trial count, observed path, results, evidence, and limits. For discovery, record whether the product was encountered and whether the stated reasons for using or rejecting it match its capabilities and conditions.
- Guidance gaps, irrelevant material, repeated lookups, wrong product or operation choices, and their causes: application, agent, or host.
- Chosen participation, required human decisions, and defect repair, counted separately.
- Calls, model-context volume, latency, and relevant cost.

For comparisons, also record setup, authentication, caches, first and repeated use, automatic pagination, and actual retry attempts. Measure artifact and UI transfer separately from model context. Remove secrets and private data.

No trials recorded.

## Human review

Record whether users could inspect results, understand consequences and uncertainty, and change the work. For required decisions, record whether the responsible user could decide, decline, or revise the proposal through the declared path. State criteria and judgment limits for subjective outputs.

No review recorded.

## Conclusion

**Not evaluated.** A completed report states the tasks tested, results, failures, untested cases, and remaining uncertainty.
