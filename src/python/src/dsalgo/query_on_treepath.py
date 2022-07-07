import typing

from python.src.dsalgo.algebraic_structure import Monoid

S = typing.TypeVar("S")


def query_on_path_binary_lifting(
    monoid: Monoid[S],
    tree_edges: list[tuple[int, int, S]],
) -> typing.Callable[[int, int], S]:
    # moniod operation must be commutative
    # focused on edges.
    root = 0
    n = len(tree_edges) + 1
    graph: list[list[tuple[int, S]]] = [[] for _ in range(n)]
    for u, v, value in tree_edges:
        graph[u].append((v, value))
        graph[v].append((u, value))
    que = [root]
    parent = [-1] * n
    depth = [0] * n
    value_to_parent = [monoid.identity() for _ in range(n)]
    for u in que:
        for v, value in graph[u]:
            if v == parent[u]:
                continue
            parent[v] = u
            depth[v] = depth[u] + 1
            value_to_parent[v] = value
            que.append(v)

    k = max(1, max(depth).bit_length())
    ancestor = [[n] * n for _ in range(k)]
    ancestor[0] = parent
    ancestor[0][root] = root
    value_to_ancestor = [value_to_parent]
    for i in range(k - 1):
        value_to_ancestor.append(value_to_ancestor[-1].copy())
        for j in range(n):
            ancestor[i + 1][j] = ancestor[i][ancestor[i][j]]
            value_to_ancestor[i + 1][j] = monoid.operation(
                value_to_ancestor[i][j],
                value_to_ancestor[i][ancestor[i][j]],
            )

    def get_value(u: int, v: int) -> S:
        value = monoid.identity()
        if depth[u] > depth[v]:
            u, v = v, u
        d = depth[v] - depth[u]
        for i in range(d.bit_length()):
            if d >> i & 1:
                value = monoid.operation(value, value_to_ancestor[i][v])
                v = ancestor[i][v]
        if v == u:
            return value
        for a, va in zip(ancestor[::-1], value_to_ancestor[::-1]):
            nu, nv = a[u], a[v]
            if nu == nv:
                continue
            value = monoid.operation(value, va[u])
            value = monoid.operation(value, va[v])
            u, v = nu, nv
        value = monoid.operation(value, value_to_parent[u])
        value = monoid.operation(value, value_to_parent[v])
        return value

    return get_value
