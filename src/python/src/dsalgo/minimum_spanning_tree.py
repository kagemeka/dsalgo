from __future__ import annotations


def randomized_linear() -> None:
    ...


def reverse_delete() -> None:
    ...


def boruvka(
    n: int,
    edges: list[tuple[int, int, int]],
) -> list[tuple[int, int, int]]:
    from dsalgo.connected_components import union_find

    # O(E\log{V})
    m = len(edges)
    is_added = [False] * m
    mst_edges: list[tuple[int, int, int]] = []
    while True:  # O(\log{N}) times loop.
        label = union_find(n, [(u, v) for u, v, _ in mst_edges])
        k = max(label) + 1
        if k == 1:
            break
        min_edge = [-1] * k  # for each component.
        for i, (u, v, weight) in enumerate(edges):
            u, v = label[u], label[v]
            if u == v:
                continue
            if min_edge[u] == -1 or weight < edges[min_edge[u]][2]:
                min_edge[u] = i
            if min_edge[v] == -1 or weight < edges[min_edge[v]][2]:
                min_edge[v] = i

        for i in min_edge:
            if is_added[i]:
                continue
            mst_edges.append(edges[i])
            is_added[i] = True
    return mst_edges


def kruskal_unionfind(
    n: int,
    edges: list[tuple[int, int, int]],
) -> list[tuple[int, int, int]]:
    from dsalgo.union_find import UnionFind

    edges = sorted(edges, key=lambda e: e[2])
    uf = UnionFind(n)
    mst_edges: list[tuple[int, int, int]] = []
    for u, v, weight in edges:
        if uf.find_root(u) == uf.find_root(v):
            continue
        mst_edges.append((u, v, weight))
        uf.unite(u, v)
    return mst_edges


# O(V^2)
def mst_prime_dense(
    graph: list[list[int]],
) -> list[tuple[int, int, int]]:
    from dsalgo.constant import INT_INF

    n = len(graph)
    for u in range(1, n):
        for v in range(u):
            assert graph[u][v] == graph[v][u]
    mst_edges: list[tuple[int, int, int]] = []
    min_edge = [(-1, INT_INF)] * n  # (previous node, weight)
    min_edge[0] = (-1, 0)
    visited = [False] * n
    for _ in range(n):
        pre = -1
        u = -1
        weight_to_u = INT_INF
        for i in range(n):
            if visited[i] or min_edge[i][1] >= weight_to_u:
                continue
            u = i
            pre, weight_to_u = min_edge[i]
        assert weight_to_u < INT_INF
        visited[u] = True
        if pre != -1:
            mst_edges.append((pre, u, weight_to_u))
        for v in range(n):
            if visited[v] or graph[u][v] >= min_edge[v][1]:
                continue
            min_edge[v] = (u, graph[u][v])
    assert len(mst_edges) == n - 1
    return mst_edges


def __to_directed(
    n: int,
    edges: list[tuple[int, int, int]],
) -> list[list[tuple[int, ...]]]:
    graph: list[list[tuple[int, ...]]] = [[] for _ in range(n)]
    for e in edges:
        u, v = e[:2]
        graph[u].append((v, *e[2:]))
        graph[v].append((u, *e[2:]))
    return graph


# O((E + V)\log{E})
def mst_prim_sparse(
    n: int,
    edges: list[tuple[int, int, int]],
) -> list[tuple[int, int, int]]:
    from dsalgo.constant import INT_INF

    graph = __to_directed(n, edges)
    mst_edges: list[tuple[int, int, int]] = []
    import heapq

    hq = [(0, -1, 0)]
    weight = [INT_INF] * n
    visited = [False] * n
    while hq:
        weight_to_u, pre, u = heapq.heappop(hq)
        if visited[u]:
            continue
        visited[u] = True
        if pre != -1:
            mst_edges.append((pre, u, weight_to_u))
        for v, weight_to_v in graph[u]:
            if visited[v] or weight_to_v >= weight[v]:
                continue
            weight[v] = weight_to_v
            heapq.heappush(hq, (weight_to_v, u, v))

    return mst_edges
