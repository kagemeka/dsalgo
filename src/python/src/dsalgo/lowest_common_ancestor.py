from __future__ import annotations

import typing

import dsalgo.algebraic_structure
import dsalgo.euler_tour
import dsalgo.heavy_light_decomposition
import dsalgo.sparse_table
import dsalgo.tree_bfs


def binary_lifting(
    tree_edges: list[tuple[int, int]],
    root: int,
) -> typing.Callable[[int, int], int]:
    n = len(tree_edges) + 1
    parent, depth = dsalgo.tree_bfs.tree_bfs(tree_edges, root)
    k = max(1, max(depth).bit_length())
    ancestor = [[n] * n for _ in range(k)]
    ancestor[0] = parent
    ancestor[0][root] = root
    for i in range(k - 1):
        for j in range(n):
            ancestor[i + 1][j] = ancestor[i][ancestor[i][j]]

    def get_lca(u: int, v: int) -> int:
        if depth[u] > depth[v]:
            u, v = v, u
        d = depth[v] - depth[u]
        for i in range(d.bit_length()):
            if d >> i & 1:
                v = ancestor[i][v]
        if v == u:
            return u
        for a in ancestor[::-1]:
            nu, nv = a[u], a[v]
            if nu != nv:
                u, v = nu, nv
        return parent[u]

    return get_lca


def tarjan_offline(
    tree_edges: list[tuple[int, int]],
    root: int,
    query_pairs: list[tuple[int, int]],
) -> list[int]:
    import dsalgo.union_find

    n = len(tree_edges) + 1
    graph: list[list[int]] = [[] for _ in range(n)]
    for u, v in tree_edges:
        graph[u].append(v)
        graph[v].append(u)
    queries: list[list[tuple[int, int]]] = [[] for _ in range(n)]
    for i, (u, v) in enumerate(query_pairs):
        queries[u].append((v, i))
        queries[v].append((u, i))
    visited = [False] * n
    uf = dsalgo.union_find.UnionFind(n)
    ancestor = [n] * n
    lca = [n] * len(query_pairs)

    def dfs(u: int) -> None:
        visited[u] = True
        ancestor[u] = u
        for v in graph[u]:
            if visited[v]:
                continue
            dfs(v)
            uf.unite(u, v)
            ancestor[uf.find_root(u)] = u

        for v, query_id in queries[u]:
            if visited[v]:
                lca[query_id] = ancestor[uf.find_root(v)]

    dfs(root)
    return lca


def euler_tour_rmq(
    tree_edges: list[tuple[int, int]],
    root: int,
) -> typing.Callable[[int, int], int]:
    tour = dsalgo.euler_tour.euler_tour(tree_edges, root)
    depth = dsalgo.euler_tour.compute_depth(tour)
    tour = dsalgo.euler_tour.to_nodes(tour)
    first_idx = dsalgo.euler_tour.compute_first_index(tour)
    semigroup = dsalgo.algebraic_structure.Semigroup[typing.Tuple[int, int]](
        operation=min
    )
    """
    TODO: pass rmq constructor interface instead of define for each rmq method.
    - sparse table
    - sqrt decomposition
    - segment tree
    """
    get_min = dsalgo.sparse_table.sparse_table(
        semigroup,
        [(depth[i], i) for i in tour],
    )

    def get_lca(u: int, v: int) -> int:
        left, right = first_idx[u], first_idx[v]
        if left > right:
            left, right = right, left
        return get_min(left, right + 1)[1]

    return get_lca


def heavy_light_decomposition(
    tree_edges: list[tuple[int, int]],
    root: int,
) -> typing.Callable[[int, int], int]:
    parent, depth = dsalgo.tree_bfs.tree_bfs(tree_edges, root)
    labels = dsalgo.heavy_light_decomposition.heavy_light_decompose(
        tree_edges,
        root,
    )
    roots = dsalgo.heavy_light_decomposition.compute_roots(
        tree_edges,
        root,
        labels,
    )
    roots = [roots[label] for label in labels]

    def get_lca(u: int, v: int) -> int:
        while True:
            if roots[u] == roots[v]:
                return u if depth[u] <= depth[v] else v
            if depth[roots[u]] > depth[roots[v]]:
                u, v = v, u
            v = parent[roots[v]]

    return get_lca


def lca_farach_colton_bender() -> None:
    ...
