import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parents[1] / "src"))

from evaluate import evaluate_cases


def test_evaluation_returns_metrics():
    result = evaluate_cases([
        {"case_id": "E-1", "type": "booking_failure",
         "description": "Payment succeeded but booking confirmation failed."},
        {"case_id": "E-2", "type": "refund_request",
         "description": "Customer asks for a refund."},
    ])
    assert result["cases"] == 2
    assert result["accuracy"] == 1.0
