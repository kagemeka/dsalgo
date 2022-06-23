from __future__ import annotations

import typing

import dsalgo.algstr
import dsalgo.euler_tour
import dsalgo.hld
import dsalgo.sparse_table
from dsalgo.tree_bfs import tree_bfs


def _ue_to_g(n: int, e: typing.List[E]) -> typing.List[typing.List[int]]:
    # undirected edges to adj list
    g = [[] for _ in range(n)]
    for u, v in e:
        g[u].append(v)
        g[v].append(u)
    return g


T = typing.TypeVar("T")
ED = typing.Tuple[int, int, T]


def _ued_to_g(
    n: int,  # vertex size
    e: typing.List[ED],
) -> typing.List[typing.List[typing.Tuple[int, T]]]:
    # undirected edges with data to adj list
    g = [[] for _ in range(n)]
    for u, v, d in e:
        g[u].append((v, d))
        g[v].append((u, d))
    return g


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
def tarjan_recurse(
    g: typing.List[typing.List[int]],
    qs: typing.List[typing.Tuple[int, int]],  # queries
) -> typing.List[int]:
    # tarjan's offline algorithm
    n = len(g)
    q = _ued_to_g(n, [(u, v, i) for i, (u, v) in enumerate(qs)])
    uf = UF(n)
    a = [-1] * n  # current ancestor
    lca = [n] * len(qs)

    def dfs(u: int) -> None:
        a[u] = u
        for v in g[u]:
            if a[v] != -1:  # visited
                continue
            dfs(v)
            uf.unite(u, v)
            a[uf.root(u)] = u

        for v, i in q[u]:
            if a[v] != -1:
                lca[i] = a[uf.root(v)]

    dfs(0)
    return lca


def tarjan(
    g: typing.List[typing.List[int]],  # undirected tree adj list
    qs: typing.List[typing.Tuple[int, int]],  # queries
) -> typing.List[int]:
    # non recurse for performance.
    n = len(g)
    q = _ued_to_g(n, [(u, v, i) for i, (u, v) in enumerate(qs)])
    uf = UF(n)
    a = [-1] * n
    lca = [n] * len(qs)
    s = [0]
    p = [-1] * n
    while s:
        u = s.pop()
        if u >= 0:
            s.append(~u)
            a[u] = u
            for v in g[u]:
                if a[v] != -1:
                    continue
                p[v] = u
                s.append(v)
            continue
        u = ~u
        for v, i in q[u]:
            if a[v] != -1:
                lca[i] = a[uf.root(v)]
        v = p[u]
        if v != -1:
            uf.unite(v, u)
            a[uf.root(v)] = v

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
    semigroup = dsalgo.algstr.Semigroup[typing.Tuple[int, int]](operation=min)
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
