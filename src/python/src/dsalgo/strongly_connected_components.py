from __future__ import annotations

import typing

G = typing.List[typing.List[int]]
L = typing.List[int]


def _transpose(g: G) -> G:
    n = len(g)
    g2: G = [[] for _ in range(n)]
    for u in range(n):
        for v in g[u]:
            g2[v].append(u)
    return g2


def kosaraju(g: G) -> L:
    n = len(g)
    vis = [False] * n
    q: list[int] = []

    def dfs(u: int) -> None:
        vis[u] = True
        for v in g[u]:
            if not vis[v]:
                dfs(v)
        q.append(u)

    g = _transpose(g)
    label = [-1] * n
    l = 0

    def rdfs(u: int, l: int) -> None:
        label[u] = l
        for v in g[u]:
            if label[v] == -1:
                rdfs(v, l)

    for u in range(n):
        if not vis[u]:
            dfs(u)
    for u in q[::-1]:
        if label[u] == -1:
            rdfs(u, l)
            l += 1
    return label


def path_based(g: G) -> L:
    n = len(g)
    order = [-1] * n
    labels = [-1] * n
    stack_0: list[int] = []
    stack_1: list[int] = []
    ord = 0
    label = 0

    def dfs(u: int) -> None:
        nonlocal ord, label
        order[u] = ord
        ord += 1
        stack_0.append(u)
        stack_1.append(u)
        for v in g[u]:
            if order[v] == -1:
                dfs(v)
            elif labels[v] == -1:
                # v is start of a scc.
                while order[stack_0[-1]] > order[v]:
                    stack_0.pop()

        if stack_0[-1] != u:
            return
        while True:
            v = stack_1.pop()
            labels[v] = label
            print(u, v)
            if v == u:
                break
        label += 1
        stack_0.pop()

    for i in range(n):
        if order[i] == -1:
            dfs(i)

    return labels


def tarjan_lowlink(g: G) -> list[int]:
    n = len(g)
    stack: list[int] = []
    on_stack = [False] * n
    order = [-1] * n
    lowlink = [-1] * n
    ord = 0
    labels = [-1] * n
    label = 0

    def dfs(u: int) -> None:
        nonlocal ord, label
        order[u] = lowlink[u] = ord
        ord += 1
        stack.append(u)
        on_stack[u] = True
        for v in g[u]:
            if order[v] == -1:
                dfs(v)
                lowlink[u] = min(lowlink[u], lowlink[v])
            elif on_stack[v] and order[v] < lowlink[u]:
                lowlink[u] = order[v]

        if lowlink[u] != order[u]:
            return
        while True:
            v = stack.pop()
            on_stack[v] = False
            labels[v] = label
            if v == u:
                break
        label += 1

    for i in range(n):
        if order[i] == -1:
            dfs(i)
    return labels


import unittest


class Tests(unittest.TestCase):
    def test_kosaraju(self) -> None:
        g: G = [[1, 3], [2], [3], []]
        labels = dsalgo.strongly_connected_components.kosaraju(g)
        self.assertEqual(
            labels,
            [0, 1, 2, 3],
        )

    def test_path_based(self) -> None:
        g: G = [[1, 3], [2], [3], []]
        labels = dsalgo.strongly_connected_components.path_based(g)
        self.assertEqual(
            labels,
            [3, 2, 1, 0],
        )

    def test_tarjan_lowlink(self) -> None:
        g: G = [[1, 3], [2], [3], []]
        labels = dsalgo.strongly_connected_components.tarjan_lowlink(g)
        self.assertEqual(
            labels,
            [3, 2, 1, 0],
        )


if __name__ == "__main__":
    unittest.main()
