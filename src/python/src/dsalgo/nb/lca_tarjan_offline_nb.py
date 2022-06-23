import numba as nb
import numpy as np
from dsa.topology.euler_tour.edge.non_recursive.jit import euler_tour_edge
from dsa.topology.graph.jit.sort_csgraph import sort_csgraph
from dsa.topology.union_find.parent_size_at_same.jit import (
    uf_build,
    uf_find,
    uf_unite,
)

# TODO cut below


@nb.njit
def lca(
    g: np.ndarray,
    edge_idx: np.ndarray,
    vu: np.ndarray,
) -> np.ndarray:
    m = len(vu)
    tour, parent, _ = euler_tour_edge(g, edge_idx, 0)
    n = len(tour) >> 1
    first_idx = np.full(n, -1, np.int64)
    for i in range(len(tour)):
        u = tour[i]
        if u < 0:
            continue
        first_idx[u] = i

    for i in range(m):
        v, u = vu[i]
        if first_idx[v] < first_idx[u]:
            vu[i] = vu[i, ::-1]
    vu, query_idx, original_idx = sort_csgraph(n, vu)

    _lca = np.empty(m, np.int64)
    uf = uf_build(n)
    ancestor = np.arange(n)
    for v in tour[:-1]:
        if v >= 0:
            continue
        v = ~v
        for j in range(query_idx[v], query_idx[v + 1]):
            u = vu[j, 1]
            _lca[original_idx[j]] = ancestor[uf_find(uf, u)]
        p = parent[v]
        uf_unite(uf, v, p)
        ancestor[uf_find(uf, p)] = p
    return _lca
