import heapq

import numba as nb
import numpy as np

from dsalgo.constant import INT_INF
from dsalgo.numba.graph.csgraph_to_directed import csgraph_to_directed

# TODO cut below


@nb.njit
def mst_prim_dense(g: np.ndarray) -> np.ndarray:
    n = len(g)
    assert g.shape == (n, n)
    assert g.max() <= INT_INF
    g = dense_graph_to_undirected(g)
    mst = np.zeros((n, 3), np.int64)
    mst_idx = -1

    def add_edge(u, v, w):
        nonlocal mst, mst_idx
        mst[mst_idx] = (u, v, w)
        mst_idx += 1

    min_edge = np.full((n, 2), -1, np.int64)
    min_edge[:, 1] = INT_INF
    min_edge[0, 1] = 0
    visited = np.zeros(n, np.bool8)
    for _ in range(n):
        pre, u, wu = -1, -1, INT_INF
        for i in range(n):
            if visited[i]:
                continue
            p, w = min_edge[i]
            if w >= wu:
                continue
            pre, u, wu = p, i, w
        assert wu < INT_INF
        add_edge(pre, u, wu)
        visited[u] = True
        for v in range(n):
            if visited[v]:
                continue
            if g[u, v] < min_edge[v, 1]:
                min_edge[v] = (u, g[u, v])
    mst = mst[:mst_idx]
    assert mst[:, 2].sum() == min_edge[:, 1].sum()
    return mst


@nb.njit
def mst_prim_sparse(n: int, csgraph: np.ndarray) -> np.ndarray:
    m = len(csgraph)
    assert csgraph.shape == (m, 3)
    assert np.all(csgraph[:, 2] < INT_INF)
    csgraph = csgraph_to_directed(csgraph)
    m *= 2
    sort_idx = np.argsort(csgraph[:, 0], kind="mergesort")
    csgraph = csgraph[sort_idx]
    edge_idx = np.searchsorted(csgraph[:, 0], np.arange(n + 1))

    mst = np.zeros((m + 1, 3), np.int64)
    mst_idx = -1

    def add_edge(u, v, w):
        nonlocal mst, mst_idx
        mst[mst_idx] = (u, v, w)
        mst_idx += 1

    hq = [(0, -1, 0)]
    weight = np.full(n, INT_INF, np.int64)
    weight[0] = 0
    visited = np.zeros_like(weight, np.bool8)
    while hq:
        wu, pre, u = heapq.heappop(hq)
        if visited[u]:
            continue
        visited[u] = True
        add_edge(pre, u, wu)
        for i in range(edge_idx[u], edge_idx[u + 1]):
            _, v, wv = csgraph[i]
            if wv >= weight[v] or visited[v]:
                continue
            weight[v] = wv
            heapq.heappush(hq, (wv, u, v))
    mst = mst[:mst_idx]
    assert weight.sum() == mst[:, 2].sum()
    return mst
