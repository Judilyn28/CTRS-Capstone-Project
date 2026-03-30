from __future__ import annotations

from dataclasses import dataclass
from typing import Generator, Optional

from models import Cat


@dataclass
class Node:
    key: tuple[int, str]
    value: Cat
    height: int = 1
    left: Optional["Node"] = None
    right: Optional["Node"] = None


class AVLTree:
    def __init__(self) -> None:
        self.root: Optional[Node] = None

    def insert(self, key: tuple[int, str], value: Cat) -> None:
        self.root = self._insert(self.root, key, value)

    def _insert(self, node: Optional[Node], key: tuple[int, str], value: Cat) -> Node:
        if node is None:
            return Node(key=key, value=value)
        if key < node.key:
            node.left = self._insert(node.left, key, value)
        elif key > node.key:
            node.right = self._insert(node.right, key, value)
        else:
            node.value = value
            return node
        self._update_height(node)
        return self._rebalance(node)

    def inorder(self) -> Generator[Cat, None, None]:
        yield from self._inorder(self.root)

    def _inorder(self, node: Optional[Node]) -> Generator[Cat, None, None]:
        if node:
            yield from self._inorder(node.left)
            yield node.value
            yield from self._inorder(node.right)

    def _height(self, node: Optional[Node]) -> int:
        return node.height if node else 0

    def _update_height(self, node: Node) -> None:
        node.height = 1 + max(self._height(node.left), self._height(node.right))

    def _balance_factor(self, node: Optional[Node]) -> int:
        if node is None:
            return 0
        return self._height(node.left) - self._height(node.right)

    def _rebalance(self, node: Node) -> Node:
        balance = self._balance_factor(node)
        if balance > 1:
            if self._balance_factor(node.left) < 0:
                node.left = self._rotate_left(node.left)
            return self._rotate_right(node)
        if balance < -1:
            if self._balance_factor(node.right) > 0:
                node.right = self._rotate_right(node.right)
            return self._rotate_left(node)
        return node

    def _rotate_left(self, z: Node) -> Node:
        y = z.right
        assert y is not None
        t2 = y.left
        y.left = z
        z.right = t2
        self._update_height(z)
        self._update_height(y)
        return y

    def _rotate_right(self, z: Node) -> Node:
        y = z.left
        assert y is not None
        t3 = y.right
        y.right = z
        z.left = t3
        self._update_height(z)
        self._update_height(y)
        return y
