import typing

from dsalgo.scc_topological_sort import toposort


def tarjan(g: typing.List[typing.List[int]]) -> typing.List[int]:
    n = len(g)
    order = [n] * n
    labels = [n] * n
    o = l = 0

    st = []
    low_ord = [n] * n
    st_dfs = list(range(n))[::-1]
    parent = [n] * n
    while st_dfs:
        u = st_dfs.pop()
        if u < 0:
            u = ~u
            if low_ord[u] == order[u]:
                while True:
                    v = st.pop()
                    labels[v] = l
                    if v == u:
                        break
                l += 1
            p = parent[u]
            if p != n:
                low_ord[p] = min(low_ord[p], low_ord[u])
            continue
        if order[u] != n:
            continue
        st_dfs.append(~u)
        order[u] = low_ord[u] = o
        o += 1
        st.append(u)
        for v in g[u]:
            if order[v] == n:
                parent[v] = u
                st_dfs.append(v)
            elif labels[v] == n:
                low_ord[u] = min(low_ord[u], order[v])

    return toposort(labels)
