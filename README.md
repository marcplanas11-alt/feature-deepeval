# feature-deepeval
## Current Baselines

### AnswerRelevancy — Claims Triage

Initial baseline executed on 3 insurance claims triage scenarios.

Result:

- Tests: 3
- Passed: 3
- Failed: 0
- Pass rate: 100%

Purpose:

AnswerRelevancy checks whether the agent response is relevant to the claim scenario and operationally useful for triage.

### Faithfulness — Wording / Compliance Review

Initial baseline executed on 3 wording-style scenarios.

Result:

- Tests: 3
- Passed: 3
- Failed: 0
- Average score: 1.00
- Pass rate: 100%

Purpose:

Faithfulness checks whether the agent answer is grounded in the provided wording or clause, reducing hallucination risk in insurance and compliance workflows.

## Prompt Versioning

This repo includes basic prompt versioning for claims triage:

```text
prompts/claims_triage/v1.md
prompts/claims_triage/v2.md
prompts/changelog.md
