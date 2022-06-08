from __future__ import annotations

import dataclasses
import typing

import dsalgo.protocol
import dsalgo._util

K = typing.TypeVar("K", bound=dsalgo.protocol.Order)
V = typing.TypeVar("V")


@dataclasses.dataclass
class Node(typing.Generic[K, V]):
    key: K
    value: typing.Optional[V] = None
    left: typing.Optional[Node[K, V]] = None
    right: typing.Optional[Node[K, V]] = None
    height: int = 1
    size: int = 1


def _get_height(root: typing.Optional[Node[K, V]]) -> int:
    if root is None:
        return 0
    return root.height


def _get_size(root: typing.Optional[Node[K, V]]) -> int:
    if root is None:
        return 0
    return root.size


def _get_balance(root: typing.Optional[Node[K, V]]) -> int:
    if root is None:
        return 0
    return _get_height(root.right) - _get_height(root.left)


def _update(root: Node[K, V]) -> None:
    root.height = max(_get_height(root.left), _get_height(root.right)) + 1
    root.size = _get_size(root.left) + _get_size(root.right) + 1


def _left_rotate(root: Node[K, V]) -> Node[K, V]:
    u = dsalgo._util.unwrap(root.right)
    u.left, root.right = root, u.left
    _update(root)
    _update(u)
    return u


def _right_rotate(root: Node[K, V]) -> Node[K, V]:
    u = dsalgo._util.unwrap(root.left)
    u.right, root.left = root, u.right
    _update(root)
    _update(u)
    return u


def _balance_tree(root: Node[K, V]) -> Node[K, V]:
    _update(root)
    balance = _get_balance(root)
    if balance < -1:  # lean to left direction
        if _get_balance(root.left) > 0:
            root.left = _left_rotate(dsalgo._util.unwrap(root.left))
        return _right_rotate(root)
    elif balance > 1:
        if _get_balance(root.right) < 0:
            root.right = _right_rotate(dsalgo._util.unwrap(root.right))
        return _left_rotate(root)
    else:
        return root


def _pop_max_node(
    root: Node[K, V],
) -> tuple[Node[K, V], typing.Optional[Node[K, V]]]:
    if root.right is None:
        new_root, root.left = root.left, None
        return root, new_root
    max_node, root.right = _pop_max_node(root.right)
    return max_node, _balance_tree(root)


def insert(root: typing.Optional[Node[K, V]], node: Node[K, V]) -> Node[K, V]:
    if root is None:
        return node
    if node.key <= root.key:
        root.left = insert(root.left, node)
    else:
        root.right = insert(root.right, node)
    return _balance_tree(root)


def remove(
    root: typing.Optional[Node[K, V]],
    key: K,
) -> typing.Optional[Node[K, V]]:
    if root is None:
        return None
    if key < root.key:
        root.left = remove(root.left, key)
    elif key > root.key:
        root.right = remove(root.right, key)
    else:
        if root.left is None:
            return root.right
        max_node, root.left = _pop_max_node(root.left)
        root.key, root.value = max_node.key, max_node.value
    return _balance_tree(root)


def get_kth_node(root: Node[K, V], k: int) -> typing.Optional[Node[K, V]]:
    assert k >= 0
    i = _get_size(root.left)
    if k == i:
        return root
    if k < i:
        return get_kth_node(dsalgo._util.unwrap(root.left), k)
    if root.right is None:
        return None
    return get_kth_node(root.right, k - i - 1)


def lower_bound(root: typing.Optional[Node[K, V]], key: K) -> int:
    if root is None:
        return 0
    if root.key < key:
        return _get_size(root.left) + 1 + lower_bound(root.right, key)
    return lower_bound(root.left, key)


def upper_bound(root: typing.Optional[Node[K, V]], key: K) -> int:
    if root is None:
        return 0
    if root.key <= key:
        return _get_size(root.left) + 1 + upper_bound(root.right, key)
    return upper_bound(root.left, key)


def find(
    root: typing.Optional[Node[K, V]],
    key: K,
) -> typing.Optional[Node[K, V]]:
    if root is None:
        return None
    if key == root.key:
        return root
    elif key < root.key:
        return find(root.left, key)
    else:
        return find(root.right, key)


def iterate(root: typing.Optional[Node[K, V]]) -> typing.Iterator[Node[K, V]]:
    def dfs(root: typing.Optional[Node[K, V]]) -> typing.Iterator[Node[K, V]]:
        if root is None:
            return
        for node in dfs(root.left):
            yield node
        yield root
        for node in dfs(root.right):
            yield node

    return dfs(root)


__all__ = [
    "insert",
    "remove",
    "lower_bound",
    "upper_bound",
    "find",
    "get_kth_node",
    "Node",
    "iterate",
]
