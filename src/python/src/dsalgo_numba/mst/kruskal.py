import numba as nb
import numpy as np

from ....union_find.parent_size_at_same.jit import uf_build, uf_find, uf_unite

# TODO cut below


@nb.njit
def mst_kruskal_naive(n: int, csgraph: np.ndarray) -> np.ndarray:
    m = len(csgraph)
    assert csgraph.shape == (m, 3)
    sort_idx = np.argsort(csgraph[:, 2], kind="mergesort")
    csgraph = csgraph[sort_idx]

    edge_indices = np.zeros(m, np.int64)
    j = 0

    def add_edge(i):
        nonlocal edge_indices, j
        edge_indices[j] = i
        j += 1

    group = np.arange(n)
    for i in range(m):
        u, v, _ = csgraph[i]
        if group[u] == group[v]:
            continue
        add_edge(i)
        k = group[v]
        for v in range(n):
            if group[v] != k:
                continue
            group[v] = group[u]

    return csgraph[edge_indices[:j]]


@nb.njit
def mst_kruskal_uf(n: int, csgraph: np.ndarray) -> np.ndarray:
    m = len(csgraph)
    assert csgraph.shape == (m, 3)
    sort_idx = np.argsort(csgraph[:, 2], kind="mergesort")
    csgraph = csgraph[sort_idx]
    uf = uf_build(n)

    added_edge_indices = np.zeros(m, np.int64)
    idx_to_add = 0

    def add_edge(i):
        nonlocal idx_to_add
        added_edge_indices[idx_to_add] = i
        idx_to_add += 1

    for i in range(m):
        u, v, _ = csgraph[i]
        if uf_find(uf, u) == uf_find(uf, v):
            continue
        uf_unite(uf, u, v)
        add_edge(i)

    return csgraph[added_edge_indices[:idx_to_add]]
