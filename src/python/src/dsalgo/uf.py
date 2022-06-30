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


class Root(typing.Sized, typing.Protocol):
    def root(self, u: int) -> int:
        ...


def same(uf: Root, u: int, v: int) -> bool:
    return uf.root(u) == uf.root(v)


def labels(uf: Root) -> list[int]:
    n = len(uf)
    lb = [-1] * n  # label
    l = 0
    for i in range(n):
        r = uf.root(i)
        if lb[r] == -1:
            lb[r] = l
            l += 1
        lb[i] = lb[r]
    return lb


T = typing.TypeVar("T")


class PotentialUF(typing.Generic[T]):
    # potentialized union find

    _g: Group[T]  # abelian
    _a: typing.List[int]
    _rp: typing.List[T]  # root: identity, other: rel potential from parrent.

    def __init__(self, g: Group[T], n: int) -> None:
        self._g = g
        self._a = [-1] * n
        self._rp = [g.e() for _ in range(n)]

    def __len__(self) -> int:
        return len(self._a)

    def root(self, u: int) -> int:
        a = self._a
        if a[u] < 0:
            return u
        p = a[u]
        a[u] = self.root(p)
        rp = self._rp
        rp[u] = self._g.op(rp[u], rp[p])
        return a[u]

    # potential from root
    def h(self, u: int) -> T:
        self.root(u)
        return self._rp[u]

    def diff(self, u: int, v: int) -> T:
        assert self.root(u) == self.root(v)
        return self._g.op(self._g.inv(self.h(u)), self.h(v))

    def unite(self, u: int, v: int, d: T) -> None:
        # d := potential diff v from u
        g = self._g
        d = g.op(g.op(self.h(u), d), g.inv(self.h(v)))
        u, v = self.root(u), self.root(v)
        if u == v:
            assert d == g.e()
            return
        a = self._a
        if a[u] > a[v]:
            u, v = v, u
            d = g.inv(d)
        a[u] += a[v]
        a[v] = u
        self._rp[v] = d

    def size_of(self, u: int) -> int:
        return -self._a[self.root(u)]


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
