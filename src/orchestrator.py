from typing import Any

from agent import decide
from tools import (
    create_provider_ticket,
    execute_standard_action,
    request_human_review,
    lookup_booking,
)


def run_case(case: dict[str, Any]) -> dict[str, Any]:
    decision = decide(case)
    tool_result = None

    if decision.action == "execute_standard_workflow":
        if decision.intent == "booking_failure":
            tool_result = lookup_booking(case)
        else:
            tool_result = execute_standard_action(case)

    elif decision.action == "request_human_approval":
        tool_result = request_human_review(case)

    elif decision.action == "escalate_to_provider_ops":
        tool_result = create_provider_ticket(case)

    return {
        "case_id": decision.case_id,
        "intent": decision.intent,
        "risk": decision.risk,
        "confidence": decision.confidence,
        "action": decision.action,
        "requires_human": decision.requires_human,
        "rationale": decision.rationale,
        "tool": (
            {
                "name": tool_result.tool,
                "success": tool_result.success,
                "message": tool_result.message,
                "data": tool_result.data,
            }
            if tool_result
            else None
        ),
    }
