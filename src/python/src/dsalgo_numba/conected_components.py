import numba as nb
import numpy as np
from dsa.topology.graph.jit.csgraph_to_directed import csgraph_to_directed
from dsa.topology.graph.jit.sort_csgraph import sort_csgraph

# TODO cut below


# DFS
@nb.njit
def connected_components_dfs(n: int, g: np.ndarray):
    g = csgraph_to_directed(g)
    g, edge_idx, _ = sort_csgraph(n, g)
    label = np.full(n, -1, np.int64)
    l = 0
    for i in range(n):
        if label[i] != -1:
            continue
        label[i] = l
        st = [i]
        while st:
            u = st.pop()
            for v in g[edge_idx[u] : edge_idx[u + 1], 1]:
                if label[v] != -1:
                    continue
                label[v] = l
                st.append(v)
        l += 1
    return label


# BFS
@nb.njit
def connected_components_bfs(n: int, g: np.ndarray):
    g = csgraph_to_directed(g)
    g, edge_idx, _ = sort_csgraph(n, g)
    label = np.full(n, -1, np.int64)
    l = 0
    for i in range(n):
        if label[i] != -1:
            continue
        label[i] = l
        que = [i]
        for u in que:
            for v in g[edge_idx[u] : edge_idx[u + 1], 1]:
                if label[v] != -1:
                    continue
                label[v] = l
                que.append(v)
        l += 1
    return label


# with union find
