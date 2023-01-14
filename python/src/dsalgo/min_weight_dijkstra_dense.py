import typing


# similar to prim's mst algorithm
def min_weight_dijkstra_dense(
    g: typing.List[typing.List[typing.Optional[int]]],
    src: int,
) -> None:
    n = len(g)
    min_weight = [None] * n
    min_weight[src] = 0
    is_fixed = [False] * n
    for _ in range(n - 1):
        u, wu = None, None
        for i in range(n):
            if is_fixed[i] or min_weight[i] is None:
                continue
            if wu is None or min_weight[i] < wu:
                u, wu = i, min_weight[i]
        if u is None:
            break
        is_fixed[u] = True
        for v in range(n):
            wv = g[u][v]
            if is_fixed[v] or wv is None:
                continue
            if min_weight[v] is None or wv < min_weight[v]:
                min_weight[v] = wv
    return min_weight
