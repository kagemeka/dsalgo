from __future__ import annotations
import unittest

import typing

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


# tarjan's lowlink algorithm
def tarjan(g: G) -> L:
    n = len(g)
    s = []
    order = [n] * n
    o = 0
    lo = [n] * n
    lb = [n] * n
    l = 0

    def labeling(u: int) -> None:
        nonlocal o, l
        order[u] = lo[u] = o
        o += 1
        s.append(u)
        for v in g[u]:
            if order[v] == n:
                labeling(v)
                lo[u] = min(lo[u], lo[v])
            elif lb[v] == n:
                lo[u] = min(lo[u], order[v])

        if lo[u] < order[u]:
            return
        while True:
            v = s.pop()
            lb[v] = l
            if v == u:
                break
        l += 1

    for i in range(n):
        if order[i] == n:
            labeling(i)
    return _toposort(lb)


# variant of tarjan
def path_based(g: G) -> L:
    n = len(g)
    s = []
    sl = []
    order = [n] * n
    o = 0
    lb = [n] * n
    l = 0

    def labeling(u: int) -> None:
        nonlocal o, l
        order[u] = o
        o += 1
        s.append(u)
        sl.append(u)
        for v in g[u]:
            if order[v] == n:
                labeling(v)
            elif lb[v] == n:
                while order[sl[-1]] > order[v]:
                    sl.pop()

        if sl[-1] != u:
            return
        while True:
            v = s.pop()
            lb[v] = l
            if v == u:
                break
        l += 1
        sl.pop()

    for i in range(n):
        if order[i] == n:
            labeling(i)
    return _toposort(lb)


class Tests(unittest.TestCase):
    def test(self) -> None:
        g: G = [[1, 3], [2], [3], []]
        ans = [0, 1, 2, 3]
        labels = kosaraju(g)
        assert labels == ans
        labels = tarjan(g)
        assert labels == ans
        labels = path_based(g)
        assert labels == ans


if __name__ == "__main__":
    unittest.main()
