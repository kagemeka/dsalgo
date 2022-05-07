from __future__ import annotations

import dataclasses
import typing

V = typing.TypeVar("V")


@dataclasses.dataclass
class Node(typing.Generic[V]):
    pivot: int
    key: int
    value: V
    left: typing.Optional[Node[V]] = None
    right: typing.Optional[Node[V]] = None
    size: int = 1


def _get_size(root: typing.Optional[Node[V]]) -> int:
    return 0 if root is None else root.size


def _update(root: Node[V]) -> None:
    root.size = _get_size(root.left) + _get_size(root.right) + 1


def new_tree_root(max_height: int, key: int, value: V) -> Node[V]:
    assert max_height >= 1
    assert 1 <= key < 1 << max_height
    return Node[V](1 << (max_height - 1), key, value)


def insert(root: Node[V], key: int, value: V) -> None:
    if key == root.key:
        raise Exception("you cannot insert the same key multiple times.")
    piv = root.pivot
    lsb = piv & -piv
    if not piv - (lsb - 1) <= key <= piv + (lsb - 1):
        raise Exception("the given key is out of bounds")
    if key < root.key:
        lo_key, lo_value = key, value
        hi_key, hi_value = root.key, root.value
    else:
        lo_key, lo_value = root.key, root.value
        hi_key, hi_value = key, value

    if lo_key < root.pivot:
        root.key, root.value = hi_key, hi_value
        if root.left is None:
            root.left = Node(piv - lsb // 2, lo_key, lo_value)
        else:
            insert(root.left, lo_key, lo_value)
    else:
        root.key, root.value = lo_key, lo_value
        if root.right is None:
            root.right = Node(piv + lsb // 2, hi_key, hi_value)
        else:
            insert(root.right, hi_key, hi_value)
    root.size += 1


def find(root: typing.Optional[Node[V]], key: int) -> typing.Optional[Node[V]]:
    if root is None:
        return None
    if key == root.key:
        return root
    elif key < root.key:
        return find(root.left, key)
    else:
        return find(root.right, key)


def _get_min(root: Node[V]) -> tuple[int, V]:
    if root.left is None:
        return (root.key, root.value)
    return _get_min(root.left)


def _get_max(root: Node[V]) -> tuple[int, V]:
    if root.right is None:
        return (root.key, root.value)
    return _get_max(root.right)


def remove(
    root: typing.Optional[Node[V]],
    key: int,
) -> typing.Optional[Node[V]]:
    if root is None:
        return None
    if key < root.key:
        root.left = remove(root.left, key)
    elif key > root.key:
        root.right = remove(root.right, key)
    else:
        if root.left is None and root.right is None:
            return None
        if root.right is not None:
            root.key, root.value = _get_min(root.right)
            root.right = remove(root.right, root.key)
        elif root.left is not None:
            root.key, root.value = _get_max(root.left)
            root.left = remove(root.left, root.key)
    _update(root)
    return root


def get_kth_node(root: Node[V], k: int) -> typing.Optional[Node[V]]:
    assert k >= 0
    i = _get_size(root.left)
    if k == i:
        return root
    if k < i:
        assert root.left is not None
        return get_kth_node(root.left, k)
    if root.right is None:
        return None
    return get_kth_node(root.right, k - i - 1)


def lower_bound(root: typing.Optional[Node[V]], key: int) -> int:
    if root is None:
        return 0
    if root.key < key:
        return _get_size(root.left) + 1 + lower_bound(root.right, key)
    return lower_bound(root.left, key)


def upper_bound(root: typing.Optional[Node[V]], key: int) -> int:
    if root is None:
        return 0
    if root.key <= key:
        return _get_size(root.left) + 1 + upper_bound(root.right, key)
    return upper_bound(root.left, key)
