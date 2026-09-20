import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parents[1] / "src"))

from metrics import operational_metrics, evaluation_metrics


def test_operational_metrics():
    results = [
        {"case_id": "1", "risk": "low", "requires_human": False, "intent": "booking_failure"},
        {"case_id": "2", "risk": "high", "requires_human": True, "intent": "refund_request"},
    ]
    metrics = operational_metrics(results)
    assert metrics["automation_rate"] == 0.5
    assert metrics["escalation_rate"] == 0.5
    assert metrics["high_risk_automation_rate"] == 0.0


def test_false_automation_metric():
    results = [
        {"case_id": "1", "requires_human": False, "intent": "booking_failure"},
        {"case_id": "2", "requires_human": False, "intent": "unknown"},
    ]
    expected = {"1": "booking_failure", "2": "refund_request"}
    metrics = evaluation_metrics(results, expected)
    assert metrics["false_automation_rate"] == 0.5
