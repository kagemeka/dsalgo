from __future__ import annotations

import dataclasses
import typing

import dsalgo.order

K = typing.TypeVar("K", bound=dsalgo.order.Order)
V = typing.TypeVar("V")


@dataclasses.dataclass
class Node(typing.Generic[K, V]):
    key: K
    value: typing.Optional[V] = None
    left: typing.Optional[Node[K, V]] = None
    right: typing.Optional[Node[K, V]] = None
    height: int = 1
    size: int = 1


def __get_height(root: typing.Optional[Node[K, V]]) -> int:
    if root is None:
        return 0
    return root.height


def __get_size(root: typing.Optional[Node[K, V]]) -> int:
    if root is None:
        return 0
    return root.size


def __update(root: Node[K, V]) -> None:
    root.height = max(__get_height(root.left), __get_height(root.right)) + 1
    root.size = __get_size(root.left) + __get_size(root.right) + 1


def __pop_max_node(
    root: Node[K, V],
) -> tuple[Node[K, V], typing.Optional[Node[K, V]]]:
    if root.right is None:
        new_root, root.left = root.left, None
        return root, new_root
    max_node, root.right = __pop_max_node(root.right)
    __update(root)
    return max_node, root


def insert(root: typing.Optional[Node[K, V]], node: Node[K, V]) -> Node[K, V]:
    if root is None:
        return node
    if node.key <= root.key:
        root.left = insert(root.left, node)
    else:
        root.right = insert(root.right, node)
    __update(root)
    return root


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
        max_node, root.left = __pop_max_node(root.left)
        root.key, root.value = max_node.key, max_node.value
    __update(root)
    return root


def get_kth_node(root: Node[K, V], k: int) -> typing.Optional[Node[K, V]]:
    assert k >= 0
    i = __get_size(root.left)
    if k == i:
        return root
    if k < i:
        assert root.left is not None
        return get_kth_node(root.left, k)
    if root.right is None:
        return None
    return get_kth_node(root.right, k - i - 1)


def lower_bound(root: typing.Optional[Node[K, V]], key: K) -> int:
    if root is None:
        return 0
    if root.key < key:
        return __get_size(root.left) + 1 + lower_bound(root.right, key)
    return lower_bound(root.left, key)


def upper_bound(root: typing.Optional[Node[K, V]], key: K) -> int:
    if root is None:
        return 0
    if root.key <= key:
        return __get_size(root.left) + 1 + upper_bound(root.right, key)
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
