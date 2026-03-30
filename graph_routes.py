from __future__ import annotations

import heapq
from collections import defaultdict
from pathlib import Path
from typing import DefaultDict, Dict, List, Tuple

from models import RouteResult


class WeightedGraph:
    def __init__(self) -> None:
        self.adj: DefaultDict[str, List[Tuple[str, float]]] = defaultdict(list)

    def add_edge(self, u: str, v: str, weight: float) -> None:
        self.adj[u].append((v, weight))
        self.adj[v].append((u, weight))

    def load_from_file(self, filepath: str) -> None:
        path = Path(filepath)
        for line in path.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            u, v, w = [part.strip() for part in line.split(",")]
            self.add_edge(u, v, float(w))

    def dijkstra(self, start: str, end: str) -> RouteResult:
        distances: Dict[str, float] = {node: float("inf") for node in self.adj}
        previous: Dict[str, str | None] = {node: None for node in self.adj}
        distances[start] = 0.0
        heap: List[Tuple[float, str]] = [(0.0, start)]

        while heap:
            current_dist, node = heapq.heappop(heap)
            if current_dist > distances[node]:
                continue
            if node == end:
                break
            for neighbor, weight in self.adj[node]:
                candidate = current_dist + weight
                if candidate < distances[neighbor]:
                    distances[neighbor] = candidate
                    previous[neighbor] = node
                    heapq.heappush(heap, (candidate, neighbor))

        if distances[end] == float("inf"):
            return RouteResult(distance=float("inf"), path=[])

        path: List[str] = []
        current: str | None = end
        while current is not None:
            path.append(current)
            current = previous[current]
        path.reverse()
        return RouteResult(distance=distances[end], path=path)
