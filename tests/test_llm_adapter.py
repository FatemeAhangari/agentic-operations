import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parents[1] / "src"))

from llm_adapter import interpret_case


def test_booking_language_is_interpreted():
    result = interpret_case({
        "description": "Payment succeeded but booking confirmation failed."
    })
    assert result.intent == "booking_failure"
    assert result.confidence > 0.5


def test_unknown_language_has_low_confidence():
    result = interpret_case({
        "description": "Customer has an unusual request outside our workflows."
    })
    assert result.intent == "unknown"
    assert result.confidence < 0.5
