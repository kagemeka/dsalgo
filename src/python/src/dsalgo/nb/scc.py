import numba as nb

# TODO cut below
import numpy as np
from dsa.topology.graph.jit.sort_csgraph import sort_csgraph


@nb.njit
def scc(n: int, g: np.ndarray) -> np.ndarray:
    def scc_dfs(n, g):
        g, edge_idx, _ = sort_csgraph(n, g)
        que = np.empty(n, np.int64)
        ptr = -1
        visited = np.zeros(n, np.bool8)
        for i in range(n):
            if visited[i]:
                continue
            st = [i]
            while st:
                u = st.pop()
                if u < 0:
                    que[ptr] = ~u
                    ptr -= 1
                    continue
                if visited[u]:
                    continue
                visited[u] = True
                st.append(~u)
                for v in g[edge_idx[u] : edge_idx[u + 1], 1][::-1]:
                    if not visited[v]:
                        st.append(v)
        return que

    def scc_reverse_dfs(n, g, que):
        g[:, :2] = g[:, 1::-1]
        g, edge_idx, _ = sort_csgraph(n, g)
        label = np.full(n, -1, np.int64)
        l = 0
        for i in que:
            if label[i] != -1:
                continue
            st = [i]
            label[i] = l
            while st:
                u = st.pop()
                for v in g[edge_idx[u] : edge_idx[u + 1], 1][::-1]:
                    if label[v] != -1:
                        continue
                    label[v] = l
                    st.append(v)
            l += 1
        return label

    g = g.copy()
    que = scc_dfs(n, g)
    return scc_reverse_dfs(n, g, que)


@nb.njit
def __scc_dfs(n, g, edge_idx, que, visited, u):
    if visited[u]:
        return
    visited[u] = True
    for v in g[edge_idx[u] : edge_idx[u + 1], 1][::-1]:
        __scc_dfs(n, g, edge_idx, que, visited, v)
    que.append(u)


@nb.njit
def __scc_reverse_dfs(n, g, edge_idx, label, l, u):
    if label[u] != -1:
        return
    label[u] = l
    for v in g[edge_idx[u] : edge_idx[u + 1], 1][::-1]:
        __scc_reverse_dfs(n, g, edge_idx, label, l, v)


def acc_recurse(
    n: int,
    g: np.ndarray,
) -> np.ndarray:
    g = g.copy()
    g, edge_idx, _ = sort_csgraph(n, g)
    visited = np.zeros(n, np.bool8)
    que = [0] * 0
    for i in range(n):
        __scc_dfs(n, g, edge_idx, que, visited, 0)
    g[:, :2] = g[:, 1::-1]
    g, edge_idx, _ = sort_csgraph(n, g)
    label = np.full(n, -1, np.int64)
    l = 0
    for i in que[::-1]:
        if label[i] != -1:
            continue
        __scc_reverse_dfs(n, g, edge_idx, label, l, i)
        l += 1
    return label
