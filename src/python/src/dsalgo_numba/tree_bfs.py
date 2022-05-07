import typing

import numba as nb
import numpy as np


@nb.njit
def tree_bfs(
    g: np.ndarray,
    edge_idx: np.ndarray,
    root: int,
) -> tuple[(np.ndarray,) * 2]:
    n = g[:, :2].max() + 1
    parent = np.full(n, -1, np.int64)
    depth = np.zeros(n, np.int64)
    fifo_que = [root]
    for u in fifo_que:
        for v in g[edge_idx[u] : edge_idx[u + 1], 1]:
            if v == parent[u]:
                continue
            parent[v] = u
            depth[v] = depth[u] + 1
            fifo_que.append(v)
    return parent, depth
