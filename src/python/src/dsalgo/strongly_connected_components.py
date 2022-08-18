# mypy: ignore-errors

from __future__ import annotations

import typing
import unittest


def transpose(
    g: typing.List[typing.List[int]],
) -> typing.List[typing.List[int]]:
    n = len(g)
    t = [[] for _ in range(n)]
    for u in range(n):
        for v in g[u]:
            t[v].append(u)
    return t


def scc(g: typing.List[typing.List[int]]) -> typing.List[int]:
    def dfs(u: int) -> None:
        state[u] = n
        for v in g[u]:
            if not state[v]:
                dfs(v)
        post_order.append(u)

    def rdfs(u: int) -> None:
        state[u] = label
        for v in g[u]:
            if state[v] == n:
                rdfs(v)

    n = len(g)
    post_order = []
    state = [0] * n

    for u in range(n):
        if not state[u]:
            dfs(u)

    g = transpose(g)
    label = 0

    for u in post_order[::-1]:
        if state[u] == n:
            rdfs(u)
            label += 1
    return state


class Tests(unittest.TestCase):
    def test(self) -> None:
        g = [[1, 3], [2], [3], []]
        ans = [0, 1, 2, 3]
        labels = scc(g)
        assert labels == ans


if __name__ == "__main__":
    unittest.main()
