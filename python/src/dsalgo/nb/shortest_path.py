import heapq
import typing

import numba as nb
import numpy as np

from dsalgo.constant import INT_INF
from dsalgo.numba.graph_theory.graph import csgraph_is_sorted


@nb.njit
def bfs(
    n: int,
    g: np.ndarray,
    edge_idx: np.ndarray,
    src: int,
) -> tuple[(np.ndarray,) * 2]:
    assert g.shape == (len(g), 2)
    assert csgraph_is_sorted(g)
    predecessor = np.full(n, -1, np.int64)
    dist = np.full(n, INT_INF, np.int64)
    dist[src] = 0
    que = [0]
    for u in que:
        for i in range(edge_idx[u], edge_idx[u + 1]):
            v = g[i, 1]
            dv = dist[u] + 1
            if dv >= dist[v]:
                continue
            dist[v] = dv
            predecessor[v] = u
            que.append(v)
    return dist, predecessor


@nb.njit
def count_paths_bfs(
    n: int,
    g: np.ndarray,
    edge_idx: np.ndarray,
    src: int,
    mod: int,
) -> tuple[(np.ndarray,) * 2]:
    dist = np.full(n, INT_INF, np.int64)
    dist[src] = 0
    paths = np.zeros(n, np.int64)
    paths[src] = 1
    que = [src]
    for u in que:
        for v in g[edge_idx[u] : edge_idx[u + 1], 1]:
            dv = dist[u] + 1
            if dv > dist[v]:
                continue
            if dv == dist[v]:
                paths[v] += paths[u]
                paths[v] %= mod
                continue
            dist[v] = dv
            paths[v] = paths[u]
            que.append(v)
    return dist, paths


@nb.njit
def dijkstra_dense(g: np.ndarray, src: int) -> tuple[(np.ndarray,) * 2]:
    n = len(g)
    assert g.shape == (n, n)
    assert INT_INF >= g.max()
    predecessor = np.full(n, -1, np.int64)
    dist = np.full(n, INT_INF, np.int64)
    dist[src] = 0
    visited = np.zeros_like(dist, np.bool8)
    while True:
        u, du = -1, INT_INF
        for i in range(n):
            if not visited[i] and dist[i] < du:
                u, du = i, dist[i]
        if u == -1:
            break
        visited[u] = True
        for v in range(n):
            dv = du + g[u, v]
            if dv >= dist[v]:
                continue
            dist[v] = dv
            predecessor[v] = u
    return dist, predecessor


@nb.njit
def dijkstra_sparse(
    n: int, g: np.ndarray, src: int
) -> tuple[(np.ndarray,) * 2]:
    assert g.shape == (len(g), 3)
    assert INT_INF > g[:, 2].max() * n
    g = g[np.argsort(g[:, 0], kind="mergesort")]
    edge_idx = np.searchsorted(g[:, 0], np.arange(n + 1))
    predecessor = np.full(n, -1, np.int64)
    dist = np.full(n, INT_INF, np.int64)
    dist[src] = 0
    hq = [(0, src)]
    while hq:
        du, u = heapq.heappop(hq)
        if du > dist[u]:
            continue
        for i in range(edge_idx[u], edge_idx[u + 1]):
            _, v, w = g[i]
            dv = du + w
            if dv >= dist[v]:
                continue
            dist[v] = dv
            predecessor[v] = u
            heapq.heappush(hq, (dv, v))
    return dist, predecessor


@nb.njit
def count_paths_dijkstra_sparse(
    n: int,
    g: np.ndarray,
    src: int,
    mod: int,
) -> tuple[(np.ndarray,) * 2]:
    assert INT_INF > g[:, 2].max() * n
    g = g[np.argsort(g[:, 0], kind="mergesort")]
    edge_idx = np.searchsorted(g[:, 0], np.arange(n + 1))
    dist = np.full(n, INT_INF, np.int64)
    dist[src] = 0
    paths = np.zeros(n, np.int64)
    paths[src] = 1
    hq = [(0, src)]
    while hq:
        du, u = heapq.heappop(hq)
        if du > dist[u]:
            continue
        for i in range(edge_idx[u], edge_idx[u + 1]):
            _, v, w = g[i]
            dv = du + w
            if dv > dist[v]:
                continue
            if dv == dist[v]:
                paths[v] += paths[u]
                paths[v] %= mod
                continue
            dist[v] = dv
            paths[v] = paths[u]
            heapq.heappush(hq, (dv, v))
    return dist, paths


@nb.njit
def bellman_ford_sparse(
    n: int, g: np.ndarray, src: int
) -> tuple[(np.ndarray,) * 2]:
    m = len(g)
    assert g.shape == (m, 3)
    assert INT_INF > g[:, 2].max() * n
    predecessor = np.full(n, -1, np.int64)
    dist = np.full(n, INT_INF, np.int64)
    dist[src] = 0
    for _ in range(n - 1):
        for i in range(m):
            u, v, w = g[i]
            if dist[u] + w >= dist[v]:
                continue
            dist[v] = dist[u] + w
            predecessor[v] = u
    for i in range(m):
        u, v, w = g[i]
        if dist[u] + w < dist[v]:
            raise Exception("Negative cycle found.")
    return dist, predecessor


@nb.njit
def johnson_sparse(n: int, g: np.ndarray) -> np.ndarray:
    m = len(g)
    assert g.shape == (m, 3)
    new_edges = np.zeros((n, 3), np.int64)
    new_edges[:, 0] = n
    new_edges[:, 1] = np.arange(n)
    g = np.vstack((g, new_edges))
    h, _ = bellman_ford_sparse(n + 1, g, n)[:-1]
    g = g[:m]
    g[:, 2] += h[g[:, 0]] - h[g[:, 1]]
    dist = np.empty((n, n), np.int64)
    for i in range(n):
        d, _ = dijkstra_sparse(n, g, i)
        dist[i] = d - h[i] + h
    return dist


@nb.njit
def bfs01():
    ...
