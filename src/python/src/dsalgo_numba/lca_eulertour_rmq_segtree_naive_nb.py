import numba as nb
import numpy as np
from dsa.misc.online_update_query.set_point_get_range.abstract.segtree.jit import (
    S,
    build_seg,
    get_range_seg,
)
from dsa.topology.euler_tour.edge.non_recursive.jit import euler_tour_edge

# TODO cut below


@nb.njit
def seg_op(a: S, b: S) -> S:
    return a if a[0] <= b[0] else b


@nb.njit
def seg_e() -> S:
    return np.array([1 << 60, -1])


@nb.njit
def lca_preprocess(
    n: int,
    g: np.ndarray,
    edge_idx: np.ndarray,
    root: int,
) -> np.ndarray:
    tour, parent, depth = euler_tour_edge(g, edge_idx, root)
    for i in range(n * 2):
        if tour[i] < 0:
            tour[i] = parent[~tour[i]]
    tour = tour[:-1]
    first_idx = np.full(n, -1, np.int64)
    for i in range(n * 2 - 1):
        u = tour[i]
        if first_idx[u] != -1:
            continue
        first_idx[u] = i
    a = np.empty((len(tour), 2), np.int64)
    a[:, 0], a[:, 1] = depth[tour], tour
    seg = build_seg(a)
    return first_idx, seg


@nb.njit
def lca(
    first_idx: np.ndarray,
    seg: np.ndarray,
    u: int,
    v: int,
) -> int:
    l, r = first_idx[u], first_idx[v]
    if l > r:
        l, r = r, l
    return get_range_seg(seg, l, r + 1)[1]
