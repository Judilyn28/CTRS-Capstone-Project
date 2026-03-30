from __future__ import annotations

import heapq
from typing import List, Tuple

from models import FosterRequest, Cat


class FosterPriorityQueue:
    def __init__(self) -> None:
        self._heap: List[Tuple[int, str, FosterRequest]] = []

    def push(self, request: FosterRequest) -> None:
        # Min-heap, so negate urgency to simulate max-priority behavior.
        heapq.heappush(self._heap, (-request.urgency, request.foster_name, request))

    def pop(self) -> FosterRequest | None:
        if not self._heap:
            return None
        return heapq.heappop(self._heap)[2]

    def snapshot(self) -> List[FosterRequest]:
        return [item[2] for item in sorted(self._heap)]

    def __len__(self) -> int:
        return len(self._heap)


class MedicalPriorityQueue:
    def __init__(self) -> None:
        self._heap: List[Tuple[int, str, Cat]] = []

    def push(self, cat: Cat) -> None:
        heapq.heappush(self._heap, (-cat.priority_score, cat.cat_id, cat))

    def pop(self) -> Cat | None:
        if not self._heap:
            return None
        return heapq.heappop(self._heap)[2]

    def snapshot(self) -> List[Cat]:
        return [item[2] for item in sorted(self._heap)]
