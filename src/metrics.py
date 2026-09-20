from typing import Any


def operational_metrics(results: list[dict[str, Any]]) -> dict[str, float]:
    total = len(results)
    if total == 0:
        return {
            "automation_rate": 0.0,
            "escalation_rate": 0.0,
            "high_risk_automation_rate": 0.0,
        }

    automated = [r for r in results if not r.get("requires_human")]
    escalated = [r for r in results if r.get("requires_human")]
    high_risk = [r for r in results if r.get("risk") == "high"]
    high_risk_automated = [
        r for r in high_risk if not r.get("requires_human")
    ]

    return {
        "automation_rate": len(automated) / total,
        "escalation_rate": len(escalated) / total,
        "high_risk_automation_rate": (
            len(high_risk_automated) / len(high_risk)
            if high_risk else 0.0
        ),
    }


def evaluation_metrics(
    results: list[dict[str, Any]],
    expected_intents: dict[str, str],
) -> dict[str, float]:
    if not results:
        return {"intent_accuracy": 0.0, "false_automation_rate": 0.0}

    correct = 0
    automated_errors = 0
    automated = 0

    for result in results:
        case_id = result["case_id"]
        expected = expected_intents.get(case_id, "unknown")
        is_correct = result["intent"] == expected
        correct += int(is_correct)

        if not result.get("requires_human"):
            automated += 1
            automated_errors += int(not is_correct)

    return {
        "intent_accuracy": correct / len(results),
        "false_automation_rate": (
            automated_errors / automated if automated else 0.0
        ),
    }
