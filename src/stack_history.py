from __future__ import annotations

from typing import Generic, List, Optional, TypeVar

T = TypeVar("T")


class Stack(Generic[T]):
    def __init__(self) -> None:
        self._items: List[T] = []

    def push(self, item: T) -> None:
        self._items.append(item)

    def pop(self) -> Optional[T]:
        if not self._items:
            return None
        return self._items.pop()

    def peek(self) -> Optional[T]:
        if not self._items:
            return None
        return self._items[-1]

    def is_empty(self) -> bool:
        return not self._items

    def __len__(self) -> int:
        return len(self._items)

    def to_list(self) -> List[T]:
        return list(reversed(self._items))
