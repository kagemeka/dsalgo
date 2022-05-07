"""
Graph Theory
"""

# TODO cut below
import typing


def traveling_salesperson(
    graph: list[list[typing.Optional[int]]],
    src: int,
) -> typing.Optional[int]:
    n = len(graph)
    assert all(len(edges) == n for edges in graph)
    assert 0 <= src < n
    dist: list[list[typing.Optional[int]]] = [
        [None] * n for _ in range(1 << n)
    ]
    dist[1 << src][src] = 0
    for s in range(1 << n):
        for i in range(n):
            if ~s >> i & 1:
                continue
            t = s & ~(1 << i)
            for j in range(n):
                if ~t >> j & 1 or dist[t][j] is None or graph[j][i] is None:
                    continue
                d = dist[t][j] + graph[j][i]
                if dist[s][i] is None or d < dist[s][i]:
                    dist[s][i] = d

    mn: typing.Optional[int] = None
    for i in range(n):
        if i == src or dist[-1][i] is None or graph[i][src] is None:
            continue
        d = dist[-1][i] + graph[i][src]
        if mn is None or d < mn:
            mn = d
    return mn
