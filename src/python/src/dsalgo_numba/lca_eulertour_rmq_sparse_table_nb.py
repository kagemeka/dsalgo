import numba as nb
import numpy as np
from dsa.math.bit_length.table.jit import bit_length_table
from dsa.misc.sparse_table.normal.jit import (
    S,
    sparse_table_build,
    sparse_table_get,
)
from dsa.topology.euler_tour.edge.non_recursive.jit import euler_tour_edge

# TODO cut below


@nb.njit
def sparse_table_op(x: S, y: S) -> S:
    return x if x[0] <= y[0] else y


@nb.njit
def lca_preprocess(
    n: int,
    g: np.ndarray,
    edge_idx: np.ndarray,
    root: int,
) -> np.ndarray:
    tour, parent, depth = (g, edge_idx, root)
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
    bit_len = bit_length_table(n * 2)
    table = sparse_table_build(bit_len, sparse_table_op, a)
    return first_idx, table, bit_len


@nb.njit
def lca(
    first_idx: np.ndarray,
    sparse_table: np.ndarray,
    bit_len,
    u: int,
    v: int,
) -> int:
    l, r = first_idx[u], first_idx[v]
    if l > r:
        l, r = r, l
    return sparse_table_get(
        bit_len,
        sparse_table,
        sparse_table_op,
        l,
        r,
    )[1]
