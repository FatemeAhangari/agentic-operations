# Agentic Operations

An executable prototype for redesigning operational case handling around AI-assisted interpretation, deterministic guardrails, tool use, and human-in-the-loop escalation.

## Product problem

Operations teams repeatedly handle cases that require classification, investigation, decision-making, communication, and follow-up.

The opportunity is not simply to add a chatbot. It is to redesign the workflow so AI can interpret ambiguous cases, deterministic policies constrain risk, tools perform bounded actions, and humans approve cases that need judgment.

## Architecture

**Case → AI interpretation → Policy / Guardrails → Orchestrator → Tool / Human Review → Decision Log**

The prototype separates four concerns:

1. **Interpretation** — model-agnostic interface for understanding the case.
2. **Policy** — deterministic risk and approval rules.
3. **Execution** — bounded operational tools.
4. **Evaluation** — explicit measurement of interpretation quality.

### Current components

- `src/llm_adapter.py` — model-agnostic interpretation interface with a deterministic stand-in
- `src/agent.py` — policy and risk decisions
- `src/orchestrator.py` — routing and tool selection
- `src/tools.py` — simulated operational tools
- `src/evaluate.py` — evaluation metrics
- `tests/` — automated tests
- `data/synthetic_cases.json` — synthetic operational cases

The deterministic stand-in is intentional: a real LLM can later replace the adapter without changing the policy or orchestration layers.

## Safety boundary

The core design decision is:

**LLM interprets → deterministic policy constrains → tools execute bounded actions → humans handle high-risk cases**

An LLM therefore does not directly authorize high-value refunds or other sensitive operational actions.

Example:
- Refunds ≥ **50M Toman** → human approval
- Provider failures → provider operations
- Unknown intent → escalation
- Low-risk known workflow → bounded tool execution

## Evaluation

The project treats evaluation as a product requirement, not an afterthought.

Current metrics:
- Intent accuracy
- Per-case prediction
- Model confidence

Next evaluation dimensions:
- False automation rate
- Escalation precision
- Tool-selection accuracy
- Decision quality
- Latency
- Cost

## Run locally

```bash
pip install -r requirements.txt
python src/run.py
pytest
```

## Product questions

- Where should AI be allowed to decide versus recommend?
- How should confidence affect escalation?
- Which operational actions are safe to automate?
- How do we measure whether automation actually improves operations?

## Data

All examples are synthetic and generated for portfolio purposes. No company-confidential data, credentials, or internal workflows are included.

## Portfolio focus

AI-native operations · Agentic workflows · Human-in-the-loop · Guardrails · Evaluation · Tool use · Automation · Product/system design

## Status

🚧 Executable prototype
