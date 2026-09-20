# Agentic Operations

A small executable prototype for redesigning operational case handling around AI-assisted decisions, deterministic guardrails, and human-in-the-loop escalation.

## Product problem

Operations teams repeatedly handle cases that require classification, investigation, decision-making, communication, and follow-up.

The opportunity is not simply to add a chatbot. It is to redesign the workflow so that AI can propose decisions, deterministic rules constrain risk, and humans approve the cases that need judgment.

## Prototype

The current prototype processes synthetic operational cases through:

**Case → Intent classification → Risk rules → Action / Escalation → Audit-ready decision**

Supported scenarios:
- Booking failure
- Refund request
- Provider failure
- Unknown cases

Example guardrail:
- Refunds above **50M Toman** require human approval.
- Provider failures are escalated to provider operations.
- Unknown intents are never auto-executed.

## Architecture

```
Case
 ↓
Classifier
 ↓
Policy / Guardrails
 ↓
Risk & confidence
 ↓
┌──────────────────────┐
│ Low risk             │ → Execute
│ High risk / unknown  │ → Human approval
│ Provider issue       │ → Operations escalation
└──────────────────────┘
 ↓
Decision + rationale
```

## Run locally

```bash
pip install -r requirements.txt
python src/run.py
pytest
```

## Product design principles

1. **AI proposes; rules constrain.**
2. **Risk determines the level of automation.**
3. **Uncertainty should trigger escalation, not silent failure.**
4. **Every automated decision should leave an auditable rationale.**
5. **Human review should be concentrated where it adds the most value.**

## Data

All examples are synthetic and generated for portfolio purposes. No company-confidential data, credentials, or internal workflows are included.

## Next steps

- Add retrieval of case context
- Add tool/action simulation
- Add confidence calibration and evaluation datasets
- Add human-review queue
- Add decision-quality and automation-rate metrics
- Add an LLM adapter behind the deterministic guardrails

## Portfolio focus

AI-native operations · Agentic workflows · Human-in-the-loop · Guardrails · Evaluation · Automation · Product/system design

## Status

🚧 Executable prototype
