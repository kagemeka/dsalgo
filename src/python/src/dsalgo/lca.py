from __future__ import annotations

import typing

import dsalgo.algebraic_structure
import dsalgo.euler_tour
import dsalgo.hld
import dsalgo.sparse_table
from dsalgo.tree_bfs import tree_bfs


def doubling(
    e: typing.List[typing.Tuple[int, int]],
) -> typing.Callable[[int, int], int]:
    # binary lifting
    n = len(e) + 1
    r = 0  # root
    p, dep = tree_bfs(e, r)
    k = max(1, max(dep).bit_length())
    a = [[n] * n for _ in range(k)]
    a[0] = p
    a[0][r] = r
    for i in range(k - 1):
        for j in range(n):
            a[i + 1][j] = a[i][a[i][j]]

    def get(u: int, v: int) -> int:
        if dep[u] > dep[v]:
            u, v = v, u
        d = dep[v] - dep[u]
        for i in range(d.bit_length()):
            if d >> i & 1:
                v = a[i][v]
        if v == u:
            return u
        for f in a[::-1]:
            nu, nv = f[u], f[v]
            if nu != nv:
                u, v = nu, nv
        return p[u]

    return get


# tarjan's offline algorithm
def tarjan(
    e: list[tuple[int, int]],
    r: int,
    qs: list[tuple[int, int]],  # queries
) -> list[int]:
    import dsalgo.uf

    n = len(e) + 1
    g = [[] for _ in range(n)]
    for u, v in e:
        g[u].append(v)
        g[v].append(u)
    q = [[] for _ in range(n)]
    for i, (u, v) in enumerate(qs):
        q[u].append((v, i))
        q[v].append((u, i))
    vis = [False] * n
    uf = dsalgo.uf.UnionFind(n)
    a = [n] * n  # anc
    lca = [n] * len(qs)

    def dfs(u: int) -> None:
        vis[u] = True
        a[u] = u
        for v in g[u]:
            if vis[v]:
                continue
            dfs(v)
            uf.unite(u, v)
            a[uf.find_root(u)] = u

        for v, i in q[u]:
            if vis[v]:
                lca[i] = a[uf.find_root(v)]

    dfs(r)
    return lca


# with euler touer and rmq
# rmq constructor as parameter.
def et_rmq(
    e: list[tuple[int, int]],
    r: int,
) -> typing.Callable[[int, int], int]:
    to = dsalgo.euler_tour.euler_tour(e, r)
    dep = dsalgo.euler_tour.compute_depth(to)
    to = dsalgo.euler_tour.to_nodes(to)
    first_idx = dsalgo.euler_tour.compute_first_index(to)
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
        [(dep[i], i) for i in to],
    )

    def get(u: int, v: int) -> int:
        l, r = first_idx[u], first_idx[v]
        if l > r:
            l, r = r, l
        return get_min(l, r + 1)[1]

    return get


def with_hld(
    tree_edges: list[tuple[int, int]],
    root: int,
) -> typing.Callable[[int, int], int]:
    parent, depth = dsalgo.tree_bfs.tree_bfs(tree_edges, root)
    labels = dsalgo.hld.heavy_light_decompose(
        tree_edges,
        root,
    )
    roots = dsalgo.hld.compute_roots(
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


class TestHLD:
    # edges = [
    #     (0, 1),
    #     (0, 6),
    #     (0, 10),
    #     (1, 2),
    #     (1, 5),
    #     (2, 3),
    #     (2, 4),
    #     (6, 7),
    #     (7, 8),
    #     (7, 9),
    #     (10, 11),
    # ]
    # root = 0

    # get_lca = lca_hld(edges, root)

    # print(get_lca(3, 5))
    ...
