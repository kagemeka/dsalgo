from __future__ import annotations

import typing
import unittest

G = typing.List[typing.List[int]]
L = typing.List[int]


def _trans(g: G) -> G:
    n = len(g)
    t: G = [[] for _ in range(n)]
    for u in range(n):
        for v in g[u]:
            t[v].append(u)
    return t


def kosaraju(g: G) -> L:
    n = len(g)
    vis = [False] * n
    q = []

    def dfs(u: int) -> None:
        vis[u] = True
        for v in g[u]:
            if not vis[v]:
                dfs(v)
        q.append(u)

    for u in range(n):
        if not vis[u]:
            dfs(u)

    g = _trans(g)
    label = [-1] * n

    def rdfs(u: int, l: int) -> None:
        label[u] = l
        for v in g[u]:
            if label[v] == -1:
                rdfs(v, l)

    l = 0
    for u in q[::-1]:
        if label[u] == -1:
            rdfs(u, l)
            l += 1
    return label


def _toposort(lb: L) -> L:
    k = max(lb)
    return [k - l for l in lb]


class Tests(unittest.TestCase):
    def test(self) -> None:
        g: G = [[1, 3], [2], [3], []]
        ans = [0, 1, 2, 3]
        labels = kosaraju(g)
        assert labels == ans


if __name__ == "__main__":
    unittest.main()
