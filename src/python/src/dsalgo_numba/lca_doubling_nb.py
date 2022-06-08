import typing

import numba as nb
import numpy as np
from dsa.math.bit_length.naive.jit import bit_length
from dsa.topology.tree_bfs.jit import tree_bfs

# TODO cut below


@nb.njit
def tree_bfs(
    n: int,
    g: np.ndarray,
    edge_idx: np.ndarray,
    root: int,
) -> tuple[np.ndarray, np.ndarray]:
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


@nb.njit
def lca_preprocess(
    n: int,
    g: np.ndarray,
    edge_idx: np.ndarray,
    root: int,
) -> np.ndarray:
    parent, depth = tree_bfs(n, g, edge_idx, root)
    k = bit_length(depth.max())
    ancestors = np.empty((k, n), np.int64)
    ancestors[0] = parent.copy()
    ancestors[0, root] = root
    for i in range(k - 1):
        ancestors[i + 1] = ancestors[i][ancestors[i]]
    return depth, ancestors


@nb.njit
def lca(
    depth: np.ndarray,
    ancestors: np.ndarray,
    u: int,
    v: int,
) -> int:
    if depth[u] > depth[v]:
        u, v = v, u
    d = depth[v] - depth[u]
    for i in range(bit_length(d)):
        if d >> i & 1:
            v = ancestors[i, v]
    if v == u:
        return u
    for i in range(len(ancestors) - 1, -1, -1):
        nu, nv = ancestors[i, u], ancestors[i, v]
        if nu == nv:
            continue
        u, v = nu, nv
    return ancestors[0, u]
