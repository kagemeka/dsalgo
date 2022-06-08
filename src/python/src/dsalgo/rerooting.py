"""
Graph Theory

"""

import typing

from dsalgo.abstract_structure import Monoid

S = typing.TypeVar("S")
F = typing.TypeVar("F")


# monoid operation must be commutative.
def tree_dp_for_all_roots(
    edges: list[tuple[int, int, F]],
    monoid: Monoid[S],
    map_: typing.Callable[[F, S], S],
) -> list[S]:
    n = len(edges) + 1
    graph: list[list[tuple[int, F]]] = [[] for _ in range(n)]
    for u, v, f in edges:
        graph[u].append((v, f))
        graph[v].append((u, f))

    dp_from_childs = [monoid.identity() for _ in range(n)]

    def tree_dp(u: int, parent: int) -> None:
        for v, f in graph[u]:
            if v == parent:
                continue
            tree_dp(v, u)
            dp_from_childs[u] = monoid.operation(
                dp_from_childs[u],
                map_(f, dp_from_childs[v]),
            )

    tree_dp(0, -1)
    dp_from_parent = [monoid.identity() for _ in range(n)]

    def reroot(u: int, parent: int) -> None:
        child_edges = [edge for edge in graph[u] if edge[0] != parent]
        deg = len(child_edges)
        dp_l = [monoid.identity() for _ in range(deg)]
        dp_r = [monoid.identity() for _ in range(deg)]
        for i, (v, f) in enumerate(child_edges[:-1]):
            dp_l[i + 1] = monoid.operation(dp_l[i], map_(f, dp_from_childs[v]))
        for i, (v, f) in reversed(list(enumerate(child_edges[1:]))):
            dp_r[i] = monoid.operation(dp_r[i + 1], map_(f, dp_from_childs[v]))
        for i, (v, f) in enumerate(child_edges):
            dp_from_parent[v] = map_(
                f,
                monoid.operation(
                    dp_from_parent[u], monoid.operation(dp_l[i], dp_r[i])
                ),
            )
            reroot(v, u)

    reroot(0, -1)
    return [
        monoid.operation(dp_from_childs[i], dp_from_parent[i])
        for i in range(n)
    ]
