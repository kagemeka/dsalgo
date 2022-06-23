import typing

import numba as nb
import numpy as np


@nb.njit
def euler_tour_edge(
    g: np.ndarray,
    edge_idx: np.ndarray,
    root: int,
) -> tuple[(np.ndarray,) * 3]:
    n = 1 if len(g) == 0 else g[:, :2].max() + 1
    parent = np.full(n, -1, np.int64)
    depth = np.zeros(n, np.int64)
    tour = np.empty(n << 1, np.int64)
    st = [root]
    for i in range(n << 1):
        u = st.pop()
        tour[i] = u
        if u < 0:
            continue
        st.append(~u)
        for v in g[edge_idx[u] : edge_idx[u + 1], 1][::-1]:
            if v == parent[u]:
                continue
            parent[v] = u
            depth[v] = depth[u] + 1
            st.append(v)
    return tour, parent, depth


@nb.njit
def euler_tour_node(
    g: np.ndarray,
    edge_idx: np.ndarray,
    root: int,
) -> tuple[(np.ndarray,) * 4]:
    tour, parent, depth = euler_tour_edge(g, edge_idx, root)
    n = len(tour) >> 1
    tour = tour[:-1]
    first_idx = np.full(n, -1, np.int64)
    for i in range(2 * n - 1):
        u = tour[i]
        if u < 0:
            tour[i] = parent[~u]
            continue
        first_idx[u] = i
    return tour, first_idx, parent, depth
