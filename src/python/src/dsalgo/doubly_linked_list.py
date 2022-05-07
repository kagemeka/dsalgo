from __future__ import annotations

import dataclasses
import typing

T = typing.TypeVar("T")


@dataclasses.dataclass
class Node(typing.Generic[T]):
    value: T
    left: typing.Optional[Node[T]] = None
    right: typing.Optional[Node[T]] = None


def add_right(
    right: typing.Optional[Node[T]],
    node: Node[T],
) -> Node[T]:
    if right is None:
        return node
    right.right, node.left = node, right
    return node


def add_left(
    left: typing.Optional[Node[T]],
    node: Node[T],
) -> Node[T]:
    if left is None:
        return node
    left.left, node.right = node, left
    return node


def pop_right(
    right: Node[T],
) -> tuple[Node[T], typing.Optional[Node[T]]]:
    popped, new_right = right, right.left
    popped.left is None
    if new_right is not None:
        new_right.right = None
    return popped, new_right


def pop_left(
    left: Node[T],
) -> tuple[Node[T], typing.Optional[Node[T]]]:
    popped, new_left = left, left.right
    popped.right is None
    if new_left is not None:
        new_left.left = None
    return popped, new_left
