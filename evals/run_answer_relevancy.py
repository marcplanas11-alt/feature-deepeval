import json
from pathlib import Path

from deepeval import evaluate
from deepeval.metrics import AnswerRelevancyMetric
from deepeval.test_case import LLMTestCase


TEST_CASES_PATH = Path("evals/test_cases/claims_triage_cases.json")
RESULTS_PATH = Path("evals/results/answer_relevancy_baseline.json")


def load_test_cases(path: Path) -> list[dict]:
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def build_deepeval_cases(raw_cases: list[dict]) -> list[LLMTestCase]:
    test_cases = []

    for case in raw_cases:
        test_cases.append(
            LLMTestCase(
                input=case["input"],
                actual_output=case["actual_output"],
                expected_output=case["expected_output"],
            )
        )

    return test_cases


def main() -> None:
    raw_cases = load_test_cases(TEST_CASES_PATH)
    test_cases = build_deepeval_cases(raw_cases)

    metric = AnswerRelevancyMetric(threshold=0.7)

    evaluation_result = evaluate(
        test_cases=test_cases,
        metrics=[metric],
    )

    RESULTS_PATH.parent.mkdir(parents=True, exist_ok=True)

    summary = {
        "metric": "AnswerRelevancy",
        "threshold": 0.7,
        "test_cases": len(test_cases),
        "note": "Run completed using DeepEval. See terminal output for detailed metric results.",
        "raw_result_string": str(evaluation_result),
    }

    with RESULTS_PATH.open("w", encoding="utf-8") as file:
        json.dump(summary, file, indent=2)

    print(f"Evaluation completed. Results written to {RESULTS_PATH}")


if __name__ == "__main__":
    main()
