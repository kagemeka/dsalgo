import typing

import numba as nb
import numpy as np

from dsalgo.constant import INT_INF


@nb.njit
def csgraph_from_dense(g: np.ndarray) -> np.ndarray:
    n = len(g)
    assert g.shape == (n, n)
    exist_edge = g != INT_INF
    m = exist_edge.sum()
    csgraph = np.zeros((m, 3), np.int64)
    k = 0

    def add_edge(u, v, w):
        nonlocal csgraph, k
        csgraph[k] = (u, v, w)
        k += 1

    for i in range(n):
        for j in range(n):
            if not exist_edge[i, j]:
                continue
            add_edge(i, j, g[i, j])
    return csgraph


@nb.njit
def csgraph_is_sorted(g: np.ndarray) -> bool:
    return np.all(g[:-1, 0] <= g[1:, 0])


@nb.njit
def csgraph_to_dense(n: int, g: np.ndarray, fill: int) -> np.ndarray:
    m = len(g)
    assert g.shape == (m, 3)
    t = np.full((n, n), fill, np.int64)
    for i in range(m):
        t[g[i, 0], g[i, 1]] = g[i, 2]
    return t


@nb.njit
def csgraph_to_directed(g: np.ndarray) -> np.ndarray:
    m = len(g)
    g = np.vstack((g, g))
    g[m:, :2] = g[m:, 1::-1]
    return g


@nb.njit
def sort_csgraph(n: int, g: np.ndarray) -> tuple[(np.ndarray,) * 3]:
    idx = g[:, 0] << 30 | g[:, 1]
    sort_idx = np.argsort(idx, kind="mergesort")
    g = g[sort_idx]
    original_idx = np.arange(len(g))[sort_idx]
    edge_idx = np.searchsorted(g[:, 0], np.arange(n + 1))
    return g, edge_idx, original_idx
