"""Generación de representación Graphviz para el árbol."""

from __future__ import annotations
from typing import Optional
from abb import Node


def export_to_dot(root: Optional[Node], output_dot: str = 'avl_tree.dot') -> None:
    """Exporta el árbol a un archivo .dot."""
    lines = [
        'digraph AVL {',
        '    node [shape=circle, style=filled, fillcolor=lightblue, fontname="Arial"];',
        '    rankdir=TB;'
    ]

    if root is None:
        lines.append('    empty [label="Árbol vacío", shape=box, fillcolor=lightgray];')
    else:
        _build_dot(root, lines)

    lines.append('}')

    with open(output_dot, 'w', encoding='utf-8') as file:
        file.write('\n'.join(lines))


def _build_dot(node: Optional[Node], lines: list[str]) -> None:
    if node is None:
        return

    node_id = f'node_{id(node)}'
    lines.append(f'    {node_id} [label="{node.key}\nH={node.height}"];')

    if node.left:
        left_id = f'node_{id(node.left)}'
        lines.append(f'    {node_id} -> {left_id};')
        _build_dot(node.left, lines)
    else:
        null_left = f'null_left_{id(node)}'
        lines.append(f'    {null_left} [shape=point];')
        lines.append(f'    {node_id} -> {null_left};')

    if node.right:
        right_id = f'node_{id(node.right)}'
        lines.append(f'    {node_id} -> {right_id};')
        _build_dot(node.right, lines)
    else:
        null_right = f'null_right_{id(node)}'
        lines.append(f'    {null_right} [shape=point];')
        lines.append(f'    {node_id} -> {null_right};')
