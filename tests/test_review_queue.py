import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parents[1] / "src"))

from review_queue import ReviewQueue


def test_human_case_enters_queue():
    queue = ReviewQueue()
    queue.add({
        "case_id": "Q-1",
        "risk": "high",
        "requires_human": True,
        "rationale": ["High-value refund"],
    })
    assert len(queue.pending()) == 1
    assert queue.pending()[0].priority == "high"


def test_queue_item_can_be_resolved():
    queue = ReviewQueue()
    queue.add({
        "case_id": "Q-2",
        "risk": "high",
        "requires_human": True,
        "rationale": ["Unknown intent"],
    })
    queue.resolve("Q-2", reviewer="ops-1", notes="Approved after verification")
    assert len(queue.pending()) == 0
