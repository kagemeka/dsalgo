import numba as nb
import numpy as np

from dsalgo.constant import INT_INF


@nb.njit
def maximum_flow_dinic_dense(g: np.ndarray, src: int, sink: int) -> int:
    n = len(g)
    g = g.copy()
    level = np.full(n, -1, np.int64)

    def update_level():
        level[:] = -1
        level[src] = 0
        fifo_que = [src]
        for u in fifo_que:
            for v in range(n):
                if level[v] != -1 or g[u, v] <= 0:
                    continue
                level[v] = level[u] + 1
                fifo_que.append(v)

    flow_in = np.zeros(n, np.int64)
    flow_out = np.zeros(n, np.int64)
    prev = np.full(n, -1, np.int64)

    def compute_flow():
        flow_in[:] = 0
        flow_in[src] = INT_INF
        flow_out[:] = 0
        prev[:] = -1
        st = [src]
        while st:
            u = st.pop()
            if u < 0:
                u = ~u
                if u == src:
                    return flow_out[src]
                p = prev[u]
                f = flow_out[u]
                flow_out[p] += f
                flow_in[p] -= f
                g[p, u] -= f
                g[u, p] += f
                flow_in[u] = flow_out[u] = 0
                continue
            st.append(~u)
            p = prev[u]
            if u != src:
                flow_in[u] = min(flow_in[p], g[p, u])
            if u == sink:
                flow_out[u] = flow_in[u]
                continue
            if flow_in[u] == 0:
                continue
            for v in range(n - 1, -1, -1):
                if g[u, v] == 0 or level[v] <= level[u]:
                    continue
                prev[v] = u
                st.append(v)

    flow = 0
    while 1:
        update_level()
        if level[sink] == -1:
            return flow
        flow += compute_flow()
