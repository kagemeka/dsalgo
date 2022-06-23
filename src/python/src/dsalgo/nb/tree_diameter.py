import numba as nb
import numpy as np
from dsa.topology.tree_bfs.jit import tree_bfs

# TODO cut below


@nb.njit
def tree_diameter_path(
    g: np.ndarray,
    edge_idx: np.ndarray,
) -> np.ndarray:
    _, depth = tree_bfs(g, edge_idx, 0)
    parent, depth = tree_bfs(g, edge_idx, np.argmax(depth))
    u = np.argmax(depth)
    d = depth[u]
    path = np.empty(d + 1, np.int64)
    for i in range(d + 1):
        path[i] = u
        u = parent[u]
    return path
