from __future__ import annotations

import typing

from dsalgo._util import unwrap
from dsalgo.floyd_warshall import *


class NegativeCycleError(Exception):
    pass


def bfs_sparse(graph: list[list[int]], src: int) -> list[int | None]:
    n = len(graph)
    dist: list[int | None] = [None] * n
    dist[src] = 0
    queue = [src]
    for u in queue:
        for v in graph[u]:
            dist_v = unwrap(dist[u]) + 1
            if dist[v] is not None and dist_v >= unwrap(dist[v]):
                continue
            dist[v] = dist_v
            queue.append(v)
    return dist


def zero_one_bfs_sparse(
    graph: list[list[tuple[int, int]]],
    src: int,
) -> list[int | None]:
    import collections

    n = len(graph)
    dist: list[int | None] = [None] * n
    dist[src] = 0
    deque = collections.deque([src])
    while deque:
        u = deque.popleft()
        for v, w in graph[u]:
            dist_v = unwrap(dist[u]) + w
            if dist[v] is not None and dist_v >= unwrap(dist[v]):
                continue
            dist[v] = dist_v
            if w >= 1:
                deque.append(v)
            else:
                deque.appendleft(v)
    return dist


def dijkstra_dense(
    dense_graph: list[list[int | None]],
    src: int,
) -> list[int | None]:
    n = len(dense_graph)
    assert 0 <= src < n
    for i in range(n):
        assert len(dense_graph[i]) == n
        for j in range(n):
            assert dense_graph[i][i] is None or unwrap(dense_graph[i][j]) >= 0
    dist: list[int | None] = [None] * n
    dist[src] = 0
    is_fixed = [False] * n
    for _ in range(n - 1):
        u: int | None = None
        dist_u: int | None = None
        for i in range(n):
            if is_fixed[i] or dist[i] is None:
                continue
            if dist_u is None or unwrap(dist[i]) < dist_u:
                u, dist_u = i, dist[i]
        if u is None:
            break
        is_fixed[u] = True
        for v in range(n):
            if dense_graph[u][v] is None:
                continue
            dist_v = unwrap(dist_u) + unwrap(dense_graph[u][v])
            if dist[v] is None or dist_v < unwrap(dist[v]):
                dist[v] = dist_v
    return dist


def count_dijkstra_sparse():
    ...


def dijkstra_sparse(
    graph: list[list[tuple[int, int]]],
    src: int,
) -> list[int | None]:
    import heapq

    n = len(graph)
    dist: list[int | None] = [None] * n
    dist[src] = 0
    hq = [(0, src)]
    while hq:
        dist_u, u = heapq.heappop(hq)
        if dist_u > unwrap(dist[u]):
            continue
        for v, w in graph[u]:
            dist_v = dist_u + w
            if dist[v] is not None and dist_v >= unwrap(dist[v]):
                continue
            dist[v] = dist_v
            heapq.heappush(hq, (dist_v, v))
    return dist


def bellman_ford_sparse(
    graph: list[list[tuple[int, int]]],
    src: int,
) -> list[int | None]:
    n = len(graph)
    dist: list[int | None] = [None] * n
    dist[src] = 0
    for _ in range(n - 1):
        for u in range(n):
            for v, w in graph[u]:
                if dist[u] is None:
                    continue
                dist_v = unwrap(dist[u]) + w
                if dist[v] is None or dist_v < unwrap(dist[v]):
                    dist[v] = dist_v
    for u in range(n):
        for v, w in graph[u]:
            if dist[u] is None:
                continue
            if dist[v] is None or unwrap(dist[u]) + w < unwrap(dist[v]):
                raise NegativeCycleError
    return dist


def johnson_sparse(
    graph: list[list[tuple[int, int]]]
) -> list[list[int | None]]:
    import copy

    n = len(graph)
    graph = copy.deepcopy(graph)
    potential = bellman_ford_sparse(
        graph + [[(i, 0) for i in range(n)]],
        n,
    )[:-1]
    for u in range(n):
        for i, (v, w) in enumerate(graph[u]):
            if w is None or potential[u] is None or potential[v] is None:
                continue
            graph[u][i] = (v, w + unwrap(potential[u]) - unwrap(potential[v]))
    dists: list[list[int | None]] = []
    for u in range(n):
        dist = dijkstra_sparse(graph, u)
        for v in range(n):
            if dist[v] is None or potential[u] is None or potential[v] is None:
                continue
            hu, hv = unwrap(potential[u]), unwrap(potential[v])
            dist[v] = unwrap(dist[v]) - hu + hv
        dists.append(dist)
    return dists
