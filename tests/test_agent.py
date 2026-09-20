import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parents[1] / "src"))

from agent import process


def test_low_risk_case_can_be_automated():
    result = process({
        "case_id": "T-001",
        "type": "booking_failure",
        "customer_tier": "standard",
        "amount_toman": 0,
    })
    assert result["action"] == "execute_standard_workflow"
    assert result["requires_human"] is False


def test_high_value_refund_requires_human():
    result = process({
        "case_id": "T-002",
        "type": "refund_request",
        "customer_tier": "vip",
        "amount_toman": 60_000_000,
    })
    assert result["action"] == "request_human_approval"
    assert result["requires_human"] is True


def test_unknown_case_is_escalated():
    result = process({
        "case_id": "T-003",
        "type": "unknown",
        "customer_tier": "standard",
        "amount_toman": 0,
    })
    assert result["action"] == "escalate_unknown_case"
    assert result["requires_human"] is True
