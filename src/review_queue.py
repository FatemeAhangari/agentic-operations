from dataclasses import dataclass, field
from typing import Any


@dataclass
class ReviewItem:
    case_id: str
    priority: str
    reason: str
    status: str = "pending"
    reviewer: str | None = None
    notes: str = ""


@dataclass
class ReviewQueue:
    items: list[ReviewItem] = field(default_factory=list)

    def add(self, result: dict[str, Any]) -> None:
        if not result.get("requires_human"):
            return

        priority = "high" if result.get("risk") == "high" else "normal"
        self.items.append(
            ReviewItem(
                case_id=result["case_id"],
                priority=priority,
                reason="; ".join(result.get("rationale", [])),
            )
        )

    def pending(self) -> list[ReviewItem]:
        return [item for item in self.items if item.status == "pending"]

    def resolve(self, case_id: str, reviewer: str, notes: str = "") -> None:
        for item in self.items:
            if item.case_id == case_id and item.status == "pending":
                item.status = "resolved"
                item.reviewer = reviewer
                item.notes = notes
                return
        raise ValueError(f"No pending review found for {case_id}")
