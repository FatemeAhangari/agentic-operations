# Agentic Operations

An executable prototype for redesigning operational case handling around AI-assisted interpretation, deterministic guardrails, bounded tool use, human review, and measurable outcomes.

## Product problem

Operations teams repeatedly handle cases that require classification, investigation, decision-making, communication, and follow-up.

The opportunity is not simply to add a chatbot. It is to redesign the workflow so AI can interpret ambiguous cases, deterministic policies constrain risk, tools perform bounded actions, and humans handle cases where automation should stop.

## Architecture

**Case → AI interpretation → Policy / Guardrails → Orchestrator → Tool / Human Review → Decision & Evaluation**

The prototype separates:

1. **Interpretation** — model-agnostic interface for understanding the case.
2. **Policy** — deterministic risk and approval rules.
3. **Execution** — bounded operational tools.
4. **Human review** — queue for cases requiring judgment.
5. **Evaluation** — metrics for quality and automation safety.
6. **Control dashboard** — operational view of decisions and risk.

### Current components

- `src/llm_adapter.py` — model-agnostic interpretation interface
- `src/agent.py` — policy and risk decisions
- `src/orchestrator.py` — routing and tool selection
- `src/tools.py` — simulated operational tools
- `src/review_queue.py` — human-in-the-loop review queue
- `src/evaluate.py` — interpretation evaluation
- `src/metrics.py` — automation and safety metrics
- `data/evaluation_cases.json` — evaluation dataset
- `dashboard/app.py` — operations control dashboard
- `tests/` — automated tests

## Control dashboard

The Streamlit dashboard surfaces:

- Automation rate
- Escalation rate
- High-risk automation rate
- Case-level decisions
- Risk distribution
- Decision traces and rationale

Run:

```bash
pip install -r dashboard/requirements.txt
streamlit run dashboard/app.py
```

## Model strategy

The system uses a provider abstraction:

**Application → LLMProvider → Model / Gateway**

The repository ships with an offline deterministic provider so it remains runnable without API keys. An optional provider interface can be connected to an approved LLM gateway without changing business policy or orchestration.

Credentials are never stored in the repository.

## Safety boundary

**AI interprets → deterministic policy constrains → tools execute bounded actions → humans handle high-risk cases**

Example policy:
- Refunds ≥ **50M Toman** → human approval
- Provider failures → provider operations
- Unknown intent → escalation
- Low-risk known workflow → bounded tool execution

The LLM does not directly authorize sensitive operational actions.

## Human-in-the-loop

Cases requiring human judgment enter a review queue with:

- Priority
- Reason for escalation
- Status
- Reviewer
- Resolution notes

This makes human review an explicit product workflow rather than an exception hidden inside the agent.

## Evaluation

The project treats evaluation as a product requirement.

Current metrics:
- Intent accuracy
- Automation rate
- Escalation rate
- High-risk automation rate
- False automation rate

The most important safety metric is **false automation**: cases where the system performs automated handling despite an incorrect interpretation.

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
- How much human review is optimal?
- How do we measure whether automation improves operations rather than simply reducing headcount?

## Data

All examples are synthetic and generated for portfolio purposes. No company-confidential data, credentials, or internal workflows are included.

## Portfolio focus

AI-native operations · Agentic workflows · Human-in-the-loop · Guardrails · Evaluation · Tool use · Automation · Product/system design

## Status

🚧 Executable prototype
