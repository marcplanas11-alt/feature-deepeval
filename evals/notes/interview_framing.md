# DeepEval Interview Framing — Pensero

## Honest Positioning

In my insurance operations work, evaluation was closer to manual UAT: functional, scenario-based and business-user driven, but not systematic enough for LLM workflows.

This week I started applying DeepEval to my own agents to make that evaluation more structured.

## What I Tested First

I started with a small claims triage evaluation set:

- Water damage claim
- Theft / stolen equipment claim
- Travel cancellation claim with possible coverage issue

The objective was not to build a large benchmark immediately, but to create a baseline evaluation process.

## Metrics

Initial focus:

- AnswerRelevancy
- Faithfulness as next step for wording review / contract comparison

## Interview Message

I am not claiming long production experience with DeepEval. I started using it this week to close a specific gap: moving from manual UAT-style validation to systematic LLM evaluation.

The value for me is that it gives me a repeatable way to compare prompts, detect weak outputs and discuss quality beyond subjective review.

## Strong Answer

"Internally in insurance operations, UAT was manual and scenario-based. That works for business process validation, but LLM workflows need more systematic evaluation. This week I started applying DeepEval to my own agents using AnswerRelevancy and Faithfulness. I created a small baseline on claims triage and I am using it to compare prompt versions rather than relying only on manual judgement."

## What Not To Say

- Do not say I have used DeepEval for months.
- Do not say this is production-grade.
- Do not say it replaces human UAT.
- Do not overclaim Langfuse unless I have real traces.
