# DeepEval Insurance Evaluation Sprint

Portfolio project for evaluating LLM outputs in insurance workflows using DeepEval.

> **Positioning:** this repo is an evaluation layer, not an application. It shows how to test answer relevancy and faithfulness for claims triage and wording/compliance style outputs.

---

## Executive Summary

Insurance AI workflows need evaluation before they can be trusted. A claims or compliance assistant can sound convincing while still being irrelevant, unsupported or inconsistent with the source text. This repo demonstrates a basic evaluation sprint using DeepEval metrics and synthetic insurance test cases.

The workflow is:

```text
Synthetic test cases
   ↓
DeepEval metric runner
   ↓
Answer relevancy / faithfulness scoring
   ↓
JSON baseline result
   ↓
Prompt/version comparison
```

---

## Main Files

| File / Folder | Purpose |
|---|---|
| `evals/run_answer_relevancy.py` | Runs AnswerRelevancy on claims triage cases |
| `evals/run_faithfulness.py` | Runs Faithfulness on wording/compliance cases |
| `evals/test_cases/` | Synthetic test case JSON files |
| `evals/results/` | Baseline result JSON outputs |
| `prompts/claims_triage/` | Prompt versions for claims triage |
| `prompts/changelog.md` | Prompt change history |
| `requirements.txt` | Python dependencies |

---

## Setup From Zero

### 1. Clone

```bash
git clone https://github.com/marcplanas11-alt/feature-deepeval.git
cd feature-deepeval
```

### 2. Create a virtual environment

Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

macOS / Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Important: the scripts import `deepeval`, so `deepeval` must be installed in the active environment.

---

## Run Evaluations

Answer relevancy:

```bash
python evals/run_answer_relevancy.py
```

Faithfulness:

```bash
python evals/run_faithfulness.py
```

Expected output files:

```text
evals/results/answer_relevancy_baseline.json
evals/results/faithfulness_baseline.json
```

---

## Complete Command Formula

### Windows CMD

```bash
git clone https://github.com/marcplanas11-alt/feature-deepeval.git
cd feature-deepeval
python -m venv .venv
.venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
python evals/run_answer_relevancy.py
python evals/run_faithfulness.py
```

### macOS / Linux

```bash
git clone https://github.com/marcplanas11-alt/feature-deepeval.git
cd feature-deepeval
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
python evals/run_answer_relevancy.py
python evals/run_faithfulness.py
```

---

## Troubleshooting

### `ModuleNotFoundError: No module named 'deepeval'`

Install the missing package:

```bash
pip install deepeval
```

Then rerun the script.

### Evaluation model credentials are missing

DeepEval metrics may require a model provider credential depending on configuration. Configure the credential locally in your environment before running the metric scripts.

### Running from the wrong folder

Run commands from the repository root:

```bash
cd feature-deepeval
python evals/run_answer_relevancy.py
```

---

## Cleanup Notes

- `requirements.txt` should include `deepeval`; otherwise the metric scripts cannot run in a clean clone.
- Evaluation result JSON files are useful as baselines, but should be regenerated when prompts or test cases change.
- Test cases are synthetic and should not include real claim or compliance data.

---

## Author

Built by Marc Planas Callico — Insurance Operations, Business Analysis and AI-enabled transformation.
