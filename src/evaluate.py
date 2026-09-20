from dataclasses import asdict
from typing import Any

from llm_adapter import interpret_case


def evaluate_cases(cases: list[dict[str, Any]]) -> dict[str, Any]:
    expected = {
        "booking_failure": "booking_failure",
        "refund_request": "refund_request",
        "provider_failure": "provider_failure",
    }

    results = []
    correct = 0

    for case in cases:
        interpretation = interpret_case(case)
        target = expected.get(case.get("type"), "unknown")
        is_correct = interpretation.intent == target
        correct += int(is_correct)

        results.append({
            "case_id": case.get("case_id"),
            "expected": target,
            "predicted": interpretation.intent,
            "confidence": interpretation.confidence,
            "correct": is_correct,
        })

    total = len(results)
    return {
        "cases": total,
        "correct": correct,
        "accuracy": correct / total if total else 0.0,
        "results": results,
    }
