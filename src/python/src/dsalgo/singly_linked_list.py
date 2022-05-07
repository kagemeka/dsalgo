from __future__ import annotations

import dataclasses
import typing

from dsalgo.type import T


@dataclasses.dataclass
class Node(typing.Generic[T]):
    value: T
    next: Node[T] | None = None


def add_last(last: Node[T] | None, node: Node[T]) -> Node[T]:
    if last is None:
        return node
    last.next = node
    return node


def pop_front(first: Node[T]) -> tuple[Node[T], Node[T] | None]:
    popped, new_first = first, first.next
    popped.next is None
    return popped, new_first
