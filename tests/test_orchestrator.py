import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parents[1] / "src"))

from orchestrator import run_case


def test_booking_failure_uses_context_lookup():
    result = run_case({
        "case_id": "O-001",
        "type": "booking_failure",
        "amount_toman": 0,
    })
    assert result["tool"]["name"] == "lookup_booking"
    assert result["tool"]["success"] is True


def test_high_value_refund_routes_to_human():
    result = run_case({
        "case_id": "O-002",
        "type": "refund_request",
        "amount_toman": 80_000_000,
    })
    assert result["tool"]["name"] == "request_human_review"
    assert result["requires_human"] is True


def test_provider_failure_creates_ticket():
    result = run_case({
        "case_id": "O-003",
        "type": "provider_failure",
        "amount_toman": 0,
    })
    assert result["tool"]["name"] == "create_provider_ticket"
