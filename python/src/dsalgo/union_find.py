from __future__ import annotations

import typing

from python.src.dsalgo.algebraic_structure import Group


class UF:
    # Union Find
    _a: typing.List[int]  # root: neg-size, other: parent

    def __init__(self, n: int) -> None:
        self._a = [-1] * n

    def __len__(self) -> int:
        return len(self._a)

    def root(self, u: int) -> int:
        if self._a[u] < 0:
            return u
        self._a[u] = self.root(self._a[u])
        return self._a[u]

    def unite(self, u: int, v: int) -> None:
        u, v = self.root(u), self.root(v)
        if u == v:
            return
        if self._a[u] > self._a[v]:
            u, v = v, u
        self._a[u] += self._a[v]
        self._a[v] = u

    def size_of(self, u: int) -> int:
        return -self._a[self.root(u)]

    def same(self, u: int, v: int) -> bool:
        return self.root(u) == self.root(v)

    def labels(self) -> list[int]:
        n = len(self)
        lb = [-1] * n  # label
        l = 0
        for i in range(n):
            r = self.root(i)
            if lb[r] == -1:
                lb[r] = l
                l += 1
            lb[i] = lb[r]
        return lb


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
