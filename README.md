# Agentic Operations

An executable prototype for redesigning operational case handling around AI-assisted decisions, deterministic guardrails, tool use, and human-in-the-loop escalation.

## Product problem

Operations teams repeatedly handle cases that require classification, investigation, decision-making, communication, and follow-up.

The opportunity is not simply to add a chatbot. It is to redesign the workflow so that AI can propose decisions, deterministic rules constrain risk, tools retrieve or change operational state, and humans approve cases that need judgment.

## Prototype architecture

**Case → Classifier → Policy / Guardrails → Orchestrator → Tool / Human Review → Decision Log**

The current prototype includes:

- Intent classification
- Risk-based guardrails
- Tool selection
- Synthetic operational tools
- Human-review routing
- Auditable decision rationale
- Automated tests

### Supported scenarios

| Case | Risk | Action |
|---|---|---|
| Booking failure | Low | Retrieve booking context |
| Standard refund | Low | Execute standard workflow |
| High-value refund | High | Human approval |
| Provider failure | Medium | Provider-ops escalation |
| Unknown case | High | Human escalation |

Example guardrail: refunds above **50M Toman** require human approval.

## Run locally

```bash
pip install -r requirements.txt
python src/run.py
pytest
```

## Design principles

1. **AI proposes; rules constrain.**
2. **Risk determines the level of automation.**
3. **Tools perform bounded actions rather than unrestricted side effects.**
4. **Uncertainty triggers escalation.**
5. **Every decision leaves an auditable rationale.**
6. **Human review is concentrated where it adds decision value.**

## Why this matters as a product

The interesting product question is not "How do we add an AI agent?"

It is:

> **Which operational decisions should be automated, which should be assisted, and which should remain human-controlled?**

This prototype makes that boundary explicit and testable.

## Data

All examples are synthetic and generated for portfolio purposes. No company-confidential data, credentials, or internal workflows are included.

## Next steps

- Add an LLM adapter for ambiguous case interpretation
- Add retrieval/context tools
- Add tool permission scopes
- Add confidence calibration and evaluation datasets
- Add a human-review queue
- Measure automation rate, escalation rate, decision quality, latency, and cost

## Portfolio focus

AI-native operations · Agentic workflows · Human-in-the-loop · Guardrails · Tool use · Evaluation · Automation · Product/system design

## Status

🚧 Executable prototype
