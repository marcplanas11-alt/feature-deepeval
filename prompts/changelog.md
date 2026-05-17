# Prompt Versioning Changelog

## 2026-05-15 — Claims Triage Prompt

### v1

Initial simple claims triage prompt.

Focus:
- classify claim
- request information

Limitations:
- no explicit human review instruction
- no coverage confirmation guardrail
- no fraud or coverage concern flag

### v2

Improved operational prompt.

Changes:
- added human review requirement
- added instruction not to confirm coverage
- added documentation checklist
- added fraud / coverage concern flag
- improved alignment with insurance operations governance

### Evaluation Link

Initial DeepEval baseline:

- AnswerRelevancy: 3/3 passed, 100% pass rate
- Faithfulness: 3/3 passed, 100% pass rate

Next step:

- Run the same test cases against v1 and v2 outputs.
- Compare score changes.
- Document whether prompt v2 improves consistency and governance.
