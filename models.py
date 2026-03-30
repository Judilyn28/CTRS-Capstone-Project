from __future__ import annotations

from dataclasses import dataclass, field
from typing import List


@dataclass
class Cat:
    cat_id: str
    name: str
    age_months: int
    temperament_score: int
    medical_priority: int
    center: str
    adopted: bool = False
    vaccines_due: bool = False
    notes: List[str] = field(default_factory=list)

    @property
    def priority_score(self) -> int:
        # Higher means more urgent, so the heap uses negative values.
        return self.medical_priority * 10 + self.temperament_score


@dataclass
class FosterRequest:
    foster_name: str
    capacity: int
    kitten_experience: str
    spicy_cat_experience: str
    urgency: int


@dataclass
class RouteResult:
    distance: float
    path: List[str]
