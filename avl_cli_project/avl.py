"""Implementación de un Árbol AVL que extiende ABB."""

from __future__ import annotations
from typing import Optional
from abb import ABB, Node


class AVL(ABB):
    """Árbol AVL con inserción y eliminación balanceadas."""

    def _get_height(self, node: Optional[Node]) -> int:
        return node.height if node else 0

    def _update_height(self, node: Node) -> None:
        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))

    def _get_balance(self, node: Optional[Node]) -> int:
        if node is None:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)

    def _rotate_right(self, y: Node) -> Node:
        x = y.left
        if x is None:
            return y
        t2 = x.right

        x.right = y
        y.left = t2

        self._update_height(y)
        self._update_height(x)
        return x

    def _rotate_left(self, x: Node) -> Node:
        y = x.right
        if y is None:
            return x
        t2 = y.left

        y.left = x
        x.right = t2

        self._update_height(x)
        self._update_height(y)
        return y

    def _insert(self, node: Optional[Node], key: int) -> Node:
        if node is None:
            return Node(key)

        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        else:
            return node  # evita duplicados

        self._update_height(node)
        balance = self._get_balance(node)

        # Caso Izquierda-Izquierda
        if balance > 1 and node.left and key < node.left.key:
            return self._rotate_right(node)

        # Caso Derecha-Derecha
        if balance < -1 and node.right and key > node.right.key:
            return self._rotate_left(node)

        # Caso Izquierda-Derecha
        if balance > 1 and node.left and key > node.left.key:
            node.left = self._rotate_left(node.left)
            return self._rotate_right(node)

        # Caso Derecha-Izquierda
        if balance < -1 and node.right and key < node.right.key:
            node.right = self._rotate_right(node.right)
            return self._rotate_left(node)

        return node

    def _delete(self, node: Optional[Node], key: int) -> Optional[Node]:
        if node is None:
            return None

        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left

            successor = self._min_value_node(node.right)
            node.key = successor.key
            node.right = self._delete(node.right, successor.key)

        self._update_height(node)
        balance = self._get_balance(node)

        # Izquierda-Izquierda
        if balance > 1 and self._get_balance(node.left) >= 0:
            return self._rotate_right(node)

        # Izquierda-Derecha
        if balance > 1 and self._get_balance(node.left) < 0:
            if node.left:
                node.left = self._rotate_left(node.left)
            return self._rotate_right(node)

        # Derecha-Derecha
        if balance < -1 and self._get_balance(node.right) <= 0:
            return self._rotate_left(node)

        # Derecha-Izquierda
        if balance < -1 and self._get_balance(node.right) > 0:
            if node.right:
                node.right = self._rotate_right(node.right)
            return self._rotate_left(node)

        return node
