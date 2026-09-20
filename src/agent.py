from dataclasses import dataclass
from typing import Any


@dataclass
class Decision:
    case_id: str
    intent: str
    risk: str
    confidence: float
    action: str
    requires_human: bool
    rationale: list[str]


HIGH_VALUE_THRESHOLD = 50_000_000


def classify(case: dict[str, Any]) -> tuple[str, float]:
    case_type = case["type"]
    mapping = {
        "booking_failure": ("booking_failure", 0.96),
        "refund_request": ("refund_request", 0.98),
        "provider_failure": ("provider_failure", 0.91),
    }
    return mapping.get(case_type, ("unknown", 0.35))


def decide(case: dict[str, Any]) -> Decision:
    intent, confidence = classify(case)
    amount = case.get("amount_toman", 0)

    if intent == "unknown":
        return Decision(
            case["case_id"], intent, "high", confidence,
            "escalate_unknown_case", True,
            ["Intent is outside the supported workflow catalog."]
        )

    if intent == "refund_request" and amount >= HIGH_VALUE_THRESHOLD:
        return Decision(
            case["case_id"], intent, "high", confidence,
            "request_human_approval", True,
            ["Refund exceeds the automated approval threshold."]
        )

    if intent == "provider_failure":
        return Decision(
            case["case_id"], intent, "medium", confidence,
            "escalate_to_provider_ops", True,
            ["Provider error requires investigation before customer-facing action."]
        )

    return Decision(
        case["case_id"], intent, "low", confidence,
        "execute_standard_workflow", False,
        ["Case matches a known low-risk operational workflow."]
    )


def process(case: dict[str, Any]) -> dict[str, Any]:
    decision = decide(case)
    return {
        "case_id": decision.case_id,
        "intent": decision.intent,
        "risk": decision.risk,
        "confidence": decision.confidence,
        "action": decision.action,
        "requires_human": decision.requires_human,
        "rationale": decision.rationale,
    }
