import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parents[1] / "src"))

from compare_models import compare_provider


def test_provider_comparison_returns_accuracy():
    result = compare_provider([
        {
            "case_id": "C-1",
            "type": "booking_failure",
            "description": "Payment succeeded but booking confirmation failed.",
        }
    ])
    assert result["provider"] == "LocalProvider"
    assert result["accuracy"] == 1.0
