from __future__ import annotations

import typing

import dsalgo.abstract_structure
from dsalgo.type import T


class UnionFind:
    __data: list[int]

    def __init__(self, size: int) -> None:
        self.__data = [-1] * size

    def __len__(self) -> int:
        return len(self.__data)

    def find_root(self, node: int) -> int:
        assert 0 <= node < len(self)
        if self.__data[node] < 0:
            return node
        self.__data[node] = self.find_root(self.__data[node])
        return self.__data[node]

    def unite(self, node_u: int, node_v: int) -> None:
        assert 0 <= node_u < len(self) and 0 <= node_v < len(self)
        node_u, node_v = self.find_root(node_u), self.find_root(node_v)
        if node_u == node_v:
            return
        if self.__data[node_u] > self.__data[node_v]:
            node_u, node_v = node_v, node_u
        self.__data[node_u] += self.__data[node_v]
        self.__data[node_v] = node_u

    def size(self, node: int) -> int:
        assert 0 <= node < len(self)
        return -self.__data[self.find_root(node)]


def get_labels(uf: UnionFind) -> list[int]:
    n = len(uf)
    labels = [-1] * n
    label = 0
    for i in range(n):
        root = uf.find_root(i)
        if labels[root] == -1:
            labels[root] = label
            label += 1
        labels[i] = labels[root]
    return labels


class PotentialUnionFind(typing.Generic[T]):
    def __init__(
        self,
        group: dsalgo.abstract_structure.Group[T],
        size: int,
    ) -> None:
        self.__group = group  # abelian group
        self.__data = [-1] * size
        self.__delta = [group.identity() for _ in range(size)]

    def __len__(self) -> int:
        return len(self.__data)

    def find_root(self, node: int) -> int:
        assert 0 <= node < len(self)
        if self.__data[node] < 0:
            return node
        parent = self.__data[node]
        root = self.find_root(parent)
        self.__delta[node] = self.__group.operation(
            self.__delta[node],
            self.__delta[parent],
        )
        self.__data[node] = root
        return root

    def potential(self, node: int) -> T:
        self.find_root(node)
        return self.__group.invert(self.__delta[node])

    def unite(self, node_u: int, node_v: int, delta: T) -> None:
        delta = self.__group.operation(self.potential(node_u), delta)
        delta = self.__group.operation(
            delta,
            self.__group.invert(self.potential(node_v)),
        )
        node_u, node_v = self.find_root(node_u), self.find_root(node_v)
        if node_u == node_v:
            return
        delta = self.__group.invert(delta)
        if self.__data[node_u] > self.__data[node_v]:
            node_u, node_v = node_v, node_u
            delta = self.__group.invert(delta)
        self.__data[node_u] += self.__data[node_v]
        self.__data[node_v] = node_u
        self.__delta[node_v] = delta

    def size(self, node: int) -> int:
        assert 0 <= node < len(self)
        return -self.__data[self.find_root(node)]

    def delta(self, node_u: int, node_v: int) -> T | None:
        if self.find_root(node_u) != self.find_root(node_v):
            return None
        return self.__group.operation(
            self.__group.invert(self.potential(node_u)),
            self.potential(node_v),
        )


class PotentialUnionFindIntAdd:
    def __init__(self, size: int) -> None:
        self.__data = [-1] * size
        self.__delta = [0 for _ in range(size)]

    def __len__(self) -> int:
        return len(self.__data)

    def find_root(self, node: int) -> int:
        assert 0 <= node < len(self)
        if self.__data[node] < 0:
            return node
        parent = self.__data[node]
        root = self.find_root(parent)
        self.__delta[node] = self.__delta[node] + self.__delta[parent]
        self.__data[node] = root
        return root

    def potential(self, node: int) -> int:
        self.find_root(node)
        return -self.__delta[node]

    def unite(self, node_u: int, node_v: int, delta: int) -> None:
        delta = self.potential(node_u) + delta - self.potential(node_v)
        node_u, node_v = self.find_root(node_u), self.find_root(node_v)
        if node_u == node_v:
            return
        delta = -delta
        if self.__data[node_u] > self.__data[node_v]:
            node_u, node_v = node_v, node_u
            delta = -delta
        self.__data[node_u] += self.__data[node_v]
        self.__data[node_v] = node_u
        self.__delta[node_v] = delta

    def size(self, node: int) -> int:
        assert 0 <= node < len(self)
        return -self.__data[self.find_root(node)]

    def delta(self, node_u: int, node_v: int) -> int | None:
        if self.find_root(node_u) != self.find_root(node_v):
            return None
        return self.potential(node_v) - self.potential(node_u)


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
