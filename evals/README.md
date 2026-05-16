# LLM Evaluation Sprint — DeepEval

## Purpose

This folder contains a compressed evaluation sprint for applying DeepEval to insurance-focused LLM agents.

The goal is to move from manual UAT-style validation to a more systematic evaluation process using small but realistic test cases.

## Context

The initial use case is claims triage. The evaluation set contains three insurance claim scenarios and compares the agent output against an expected business outcome.

## Initial Metrics

Planned metrics:

- AnswerRelevancy
- Faithfulness
- G-Eval / LLM-as-judge for compliance-style review

## Folder Structure

```text
evals/
├── README.md
├── test_cases/
│   └── claims_triage_cases.json
├── notes/
│   └── interview_framing.md
├── results/
│   └── answer_relevancy_baseline_example.json
└── run_answer_relevancy.py
