# Agentic Operations

**An AI-assisted operations workflow designed around a simple principle: use AI where it adds value, keep critical decisions deterministic, and keep humans in the loop where risk requires judgment.**

This is an executable product/system prototype for operational case handling — not a chatbot demo.

## 1. The problem

Operations teams repeatedly handle cases that require:

- Understanding an unstructured customer or operational request
- Classifying the case
- Investigating context
- Deciding what can be automated
- Executing an operational action
- Escalating when automation is unsafe
- Measuring whether the workflow is actually improving

A naive approach is to put an LLM in the middle and let it decide.

This project takes a different approach:

> **AI interprets. Policy constrains. Tools execute. Humans handle risk. Evaluation closes the loop.**

## 2. Why AI — and where not to use it

AI is useful when the input is ambiguous, unstructured, or requires interpretation.

Deterministic logic is preferable when the rule is explicit and the consequences are predictable.

For example:

| Decision | Mechanism | Why |
|---|---|---|
| Understand a free-text case | AI / semantic interpretation | Language is ambiguous |
| Apply refund threshold | Deterministic policy | Explicit business rule |
| Execute a known operational action | Bounded tool | Predictable execution |
| Handle high-risk / ambiguous case | Human review | Requires judgment |

The goal is **not maximum AI usage**. The goal is the right mechanism for each part of the workflow.

## 3. Product architecture

**Case → AI Interpretation → Policy / Guardrails → Orchestrator → Tool / Human Review → Decision → Evaluation**

### System boundaries

1. **Interpretation**
   - Converts an operational case into structured intent and confidence.
   - Model-agnostic interface.

2. **Policy / Guardrails**
   - Applies deterministic business and risk rules.
   - Can override an AI interpretation when required.

3. **Orchestration**
   - Routes the case to the appropriate workflow.

4. **Bounded tools**
   - Execute predefined operational actions.
   - The model does not directly authorize sensitive actions.

5. **Human review**
   - Explicit workflow for cases requiring judgment.

6. **Evaluation**
   - Measures interpretation quality and automation safety.

## 4. Example decision flow

A refund-related case might follow:

```
Customer case
     ↓
AI interpretation
     ↓
Refund request + confidence
     ↓
Policy check
     ├── Low-risk → bounded workflow
     ├── High-value → human approval
     └── Uncertain → escalation
```

Current example policy:

- Refunds ≥ **50M Toman** → human approval
- Provider failures → provider operations
- Unknown intent → escalation
- Low-risk known workflow → bounded tool execution

These thresholds are illustrative portfolio assumptions, not production policies.

## 5. Safety boundary

**AI interprets → deterministic policy constrains → tools execute bounded actions → humans handle high-risk cases**

The LLM is intentionally **not** the final authority for sensitive operational decisions.

This separation makes the system easier to reason about, test, change, and govern.

## 6. Human-in-the-loop

Human review is treated as a product workflow rather than an exception.

The review queue contains:

- Priority
- Escalation reason
- Status
- Reviewer
- Resolution notes

This creates a measurable boundary between:

**automate → assist → escalate**

rather than treating automation as a binary decision.

## 7. Evaluation

Evaluation is part of the product design, not a post-launch add-on.

Current metrics include:

- Intent accuracy
- Automation rate
- Escalation rate
- High-risk automation rate
- False automation rate

### Key safety metric

**False automation** measures cases where the system automates despite an incorrect interpretation.

This is especially important because increasing automation rate alone can make a system appear successful while increasing operational risk.

## 8. Model strategy

The application uses a provider abstraction:

**Application → LLM Provider → Model / Gateway**

The repository includes an offline deterministic provider so the project can run without API keys.

An approved LLM gateway can be connected without changing the business policy or orchestration layer.

Credentials are never stored in the repository.

## 9. Repository structure

```text
src/
├── agent.py              # policy and risk decisions
├── orchestrator.py       # routing and tool selection
├── llm_adapter.py        # interpretation interface
├── llm_provider.py       # model/provider abstraction
├── tools.py              # bounded operational tools
├── review_queue.py       # human review workflow
├── evaluate.py           # evaluation
├── metrics.py            # operational metrics
└── run.py                # local execution

data/
├── synthetic_cases.json
└── evaluation_cases.json

dashboard/
└── app.py                # operational control dashboard

tests/
└── ...                   # automated tests
```

## 10. Demo

Run the prototype locally:

```bash
pip install -r requirements.txt
python src/run.py
pytest
```

Run the control dashboard:

```bash
pip install -r dashboard/requirements.txt
streamlit run dashboard/app.py
```

The dashboard provides visibility into:

- Case decisions
- Automation rate
- Escalation rate
- Risk distribution
- High-risk automation
- Decision traces

## 11. Product trade-offs

### Why not let the LLM decide everything?

Because interpretive flexibility and decision authority are different concerns.

An LLM can be useful for understanding a case while deterministic policy remains responsible for enforcing critical business constraints.

### Why keep a human in the loop?

Some cases have high financial impact, ambiguous context, or consequences that are difficult to reverse.

The right question is therefore not:

> "How do we eliminate human intervention?"

It is:

> "Which decisions should be automated, assisted, or reviewed by a human?"

### Why provider abstraction?

Model quality, latency, cost, availability, and governance requirements can change.

Separating the provider from product policy makes model changes less disruptive.

## 12. What I would improve next

A production version would require substantially more work, including:

- Real operational integrations
- Authentication and authorization
- Production-grade observability
- Structured audit logs
- More representative evaluation datasets
- Offline and online evaluation
- Model/prompt versioning
- Cost and latency monitoring
- Confidence calibration
- Policy configuration and governance
- A/B or controlled rollout strategy
- Feedback loops from human reviewers

## 13. Product questions this prototype explores

- Where should AI decide versus recommend?
- Which operational actions are safe to automate?
- How should confidence affect escalation?
- What level of human review is appropriate?
- How should automation quality be measured?
- When does AI complexity justify its value?
- How do we improve operations without optimizing only for automation rate?

## Data & scope

All examples use synthetic/generated data for portfolio purposes.

No company-confidential data, credentials, or internal workflows are included.

## Portfolio focus

**AI-native operations · Agentic workflows · Automation · Human-in-the-loop · Guardrails · Evaluation · Product/system design**

**Status:** Executable portfolio prototype
