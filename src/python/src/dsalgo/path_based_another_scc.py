import typing


def path_based(
    g: typing.List[typing.List[int]],
) -> typing.List[typing.List[int]]:
    n = len(g)
    st = []
    st_low = []
    state = [0] * n
    scc = []
    st_dfs = list(range(n))[::-1]
    while st_dfs:
        u = st_dfs.pop()
        if u < 0:
            i = state[~u] - 1
            if st_low[-1] != i + 1:
                continue
            scc.append(st[i:])
            del st[i:]
            st_low.pop()
            for v in scc[-1]:
                state[v] = -1
        elif state[u] > 0:
            while st_low[-1] > state[u]:
                st_low.pop()
        elif state[u] == 0:
            st.append(u)
            st_low.append(len(st))
            state[u] = st_low[-1]
            st_dfs.append(~u)
            st_dfs.extend(g[u])
    return scc[::-1]
