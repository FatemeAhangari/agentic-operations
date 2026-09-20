from typing import Any

from llm_provider import LocalProvider


def compare_provider(
    cases: list[dict[str, Any]],
    provider: Any | None = None,
) -> dict[str, Any]:
    provider = provider or LocalProvider()

    expected = {case["case_id"]: case.get("type", "unknown") for case in cases}
    rows = []

    for case in cases:
        result = provider.interpret(case)
        target = expected[case["case_id"]]
        rows.append({
            "case_id": case["case_id"],
            "expected": target,
            "predicted": result.intent,
            "confidence": result.confidence,
            "correct": result.intent == target,
        })

    accuracy = (
        sum(row["correct"] for row in rows) / len(rows)
        if rows else 0.0
    )

    return {
        "provider": provider.__class__.__name__,
        "cases": len(rows),
        "accuracy": accuracy,
        "results": rows,
    }
