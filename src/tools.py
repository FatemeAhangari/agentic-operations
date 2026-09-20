from dataclasses import dataclass
from typing import Any


@dataclass
class ToolResult:
    tool: str
    success: bool
    message: str
    data: dict[str, Any]


def lookup_booking(case: dict[str, Any]) -> ToolResult:
    """Simulate retrieving reservation context."""
    return ToolResult(
        tool="lookup_booking",
        success=True,
        message="Booking context retrieved.",
        data={
            "booking_status": "payment_captured_confirmation_pending",
            "provider": "synthetic-provider",
            "attempts": 1,
        },
    )


def create_provider_ticket(case: dict[str, Any]) -> ToolResult:
    """Simulate an operations escalation."""
    return ToolResult(
        tool="create_provider_ticket",
        success=True,
        message="Provider operations ticket created.",
        data={"ticket_id": f"PO-{case['case_id']}"},
    )


def request_human_review(case: dict[str, Any]) -> ToolResult:
    """Simulate routing a case to a human reviewer."""
    return ToolResult(
        tool="request_human_review",
        success=True,
        message="Case routed to human review.",
        data={"queue": "operations-review"},
    )


def execute_standard_action(case: dict[str, Any]) -> ToolResult:
    """Simulate a safe low-risk operational action."""
    return ToolResult(
        tool="execute_standard_action",
        success=True,
        message="Standard workflow executed.",
        data={"workflow": case["type"]},
    )
