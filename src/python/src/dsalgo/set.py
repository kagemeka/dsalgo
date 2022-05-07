from __future__ import annotations

import typing

import dsalgo.avl_tree_recurse
import dsalgo.pivot_tree_array_recurse
from dsalgo.avl_tree_recurse import K


class FenwickTree:
    ...


class SegmentTree:
    ...


class PivotTree:
    import dsalgo.pivot_tree_recurse

    __root: dsalgo.pivot_tree_recurse.Node[None] | None
    __max_height: int

    def __init__(self, max_height: int) -> None:
        self.__root = None
        self.__max_height = max_height

    @property
    def max_size(self) -> int:
        return (1 << self.__max_height) - 1

    def __len__(self) -> int:
        return 0 if self.__root is None else self.__root.size

    def __contains__(self, key: int) -> bool:
        assert 0 <= key < self.max_size
        return dsalgo.pivot_tree_recurse.find(self.__root, key + 1) is not None

    def __getitem__(self, i: int) -> int:
        assert 0 <= i < len(self)
        assert self.__root is not None
        node = dsalgo.pivot_tree_recurse.get_kth_node(self.__root, i)
        assert node is not None
        return node.key - 1

    def insert(self, key: int) -> None:
        assert 0 <= key < self.max_size
        if key in self:
            return
        key += 1
        if self.__root is None:
            self.__root = dsalgo.pivot_tree_recurse.new_tree_root(
                self.__max_height, key, None
            )
        else:
            dsalgo.pivot_tree_recurse.insert(self.__root, key, None)

    def remove(self, key: int) -> None:
        assert 0 <= key < self.max_size
        self.__root = dsalgo.pivot_tree_recurse.remove(self.__root, key + 1)

    def lower_bound(self, key: int) -> int:
        return dsalgo.pivot_tree_recurse.lower_bound(self.__root, key + 1)

    def upper_bound(self, key: int) -> int:
        return dsalgo.pivot_tree_recurse.upper_bound(self.__root, key + 1)

    def min(self) -> int | None:
        return None if self.__root is None else self[0]

    def max(self) -> int | None:
        return None if self.__root is None else self[len(self) - 1]


class PivotTreeArray(dsalgo.pivot_tree_array_recurse.PivotTreeArray):
    ...


class AVLTree(typing.Generic[K]):
    __root: dsalgo.avl_tree_recurse.Node[K, None] | None

    def __init__(self) -> None:
        self.__root = None

    def __len__(self) -> int:
        return 0 if self.__root is None else self.__root.size

    def __iter__(self) -> typing.Iterator[K]:
        for node in dsalgo.avl_tree_recurse.iterate(self.__root):
            yield node.key

    def __contains__(self, key: K) -> bool:
        return dsalgo.avl_tree_recurse.find(self.__root, key) is not None

    def insert(self, key: K) -> None:
        if key not in self:
            self.__root = dsalgo.avl_tree_recurse.insert(
                self.__root,
                dsalgo.avl_tree_recurse.Node(key),
            )

    def remove(self, key: K) -> None:
        if key in self:
            self.__root = dsalgo.avl_tree_recurse.remove(self.__root, key)

    def __getitem__(self, k: int) -> K | None:
        assert 0 <= k < len(self), "index ouf of range."
        assert self.__root is not None
        node = dsalgo.avl_tree_recurse.get_kth_node(self.__root, k)
        return None if node is None else node.key

    def max(self) -> K | None:
        return None if self.__root is None else self[len(self) - 1]

    def min(self) -> K | None:
        return None if self.__root is None else self[0]

    def lower_bound(self, key: K) -> int:
        return dsalgo.avl_tree_recurse.lower_bound(self.__root, key)

    def upper_bound(self, key: K) -> int:
        return dsalgo.avl_tree_recurse.upper_bound(self.__root, key)
