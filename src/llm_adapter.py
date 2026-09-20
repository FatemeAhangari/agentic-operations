from dataclasses import dataclass
from typing import Any


@dataclass
class Interpretation:
    intent: str
    confidence: float
    rationale: str


SUPPORTED = {
    "booking_failure": ["payment", "reservation", "booking", "confirmation"],
    "refund_request": ["refund", "reimburse", "money back", "cancel"],
    "provider_failure": ["provider", "supplier", "timeout", "provider error"],
}


def interpret_case(case: dict[str, Any]) -> Interpretation:
    """Deterministic stand-in for an LLM adapter.

    The interface is intentionally model-agnostic: a real LLM can replace
    this function without changing the orchestration or policy layers.
    """
    text = str(case.get("description", "")).lower()

    for intent, keywords in SUPPORTED.items():
        if any(keyword in text for keyword in keywords):
            return Interpretation(
                intent=intent,
                confidence=0.86,
                rationale=f"Matched operational language for '{intent}'.",
            )

    return Interpretation(
        intent="unknown",
        confidence=0.30,
        rationale="No supported operational intent could be identified.",
    )
