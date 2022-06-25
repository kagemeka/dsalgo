import typing
from dsalgo.scc_topological_sort import toposort


def path_based(g: typing.List[typing.List[int]]) -> typing.List[int]:
    n = len(g)
    order = [n] * n
    labels = [n] * n
    o = l = 0
    st = []
    st_low = []
    st_dfs = list(range(n))[::-1]
    while st_dfs:
        u = st_dfs.pop()
        if u < 0:
            u = ~u
            if st_low[-1] != u:
                continue
            while True:
                v = st.pop()
                labels[v] = l
                if v == u:
                    break
            l += 1
            st_low.pop()
            continue
        if order[u] != n:
            continue

        st_dfs.append(~u)
        order[u] = o
        o += 1
        st.append(u)
        st_low.append(u)
        for v in g[u]:
            if order[v] == n:
                st_dfs.append(v)
            elif labels[v] == n:
                while order[st_low[-1]] > order[v]:
                    st_low.pop()
    return toposort(labels)
