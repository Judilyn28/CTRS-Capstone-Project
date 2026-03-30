from __future__ import annotations

from typing import Generic, Iterator, List, Optional, Tuple, TypeVar

K = TypeVar("K")
V = TypeVar("V")


class HashTable(Generic[K, V]):
    """Separate-chaining hash table used for cat registry lookups."""

    def __init__(self, capacity: int = 11) -> None:
        self.capacity = max(3, capacity)
        self.buckets: List[List[Tuple[K, V]]] = [[] for _ in range(self.capacity)]
        self.size = 0
        self.collisions = 0

    def _index(self, key: K) -> int:
        return hash(key) % self.capacity

    def put(self, key: K, value: V) -> None:
        idx = self._index(key)
        bucket = self.buckets[idx]
        for i, (existing_key, _) in enumerate(bucket):
            if existing_key == key:
                bucket[i] = (key, value)
                return
        if bucket:
            self.collisions += 1
        bucket.append((key, value))
        self.size += 1
        if self.load_factor() > 0.75:
            self._rehash()

    def get(self, key: K) -> Optional[V]:
        idx = self._index(key)
        for existing_key, value in self.buckets[idx]:
            if existing_key == key:
                return value
        return None

    def remove(self, key: K) -> Optional[V]:
        idx = self._index(key)
        bucket = self.buckets[idx]
        for i, (existing_key, value) in enumerate(bucket):
            if existing_key == key:
                del bucket[i]
                self.size -= 1
                return value
        return None

    def items(self) -> Iterator[Tuple[K, V]]:
        for bucket in self.buckets:
            for item in bucket:
                yield item

    def load_factor(self) -> float:
        return self.size / self.capacity

    def _rehash(self) -> None:
        old_items = list(self.items())
        self.capacity = self.capacity * 2 + 1
        self.buckets = [[] for _ in range(self.capacity)]
        self.size = 0
        self.collisions = 0
        for key, value in old_items:
            self.put(key, value)
