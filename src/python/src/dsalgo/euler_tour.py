from __future__ import annotations

import dataclasses
import typing

import dsalgo.graph


@typing.final
@dataclasses.dataclass
class EulerTourResult:
    tour: list[int]
    parent: list[int]
    depth: list[int]


def euler_tour_recurse(
    tree_edges: list[tuple[int, int]],
    root: int,
) -> list[int]:
    """
    Examples:
        >>> edges = [(0, 1), (0, 3), (1, 4), (1, 2)]
        >>> euler_tour(edges, 0)
        [0, 1, 4, -5, 2, -3, -2, 3, -4, -1]
    """
    n = len(tree_edges) + 1
    graph = dsalgo.graph.edges_to_graph(n, tree_edges)
    parent: list[typing.Optional[int]] = [None] * n
    tour: list[int] = []

    def dfs(u: int) -> None:
        tour.append(u)
        for v in graph[u]:
            if v == parent[u]:
                continue
            parent[v] = u
            dfs(v)
        tour.append(~u)

    dfs(root)
    return tour


def euler_tour(
    tree_edges: list[tuple[int, int]],
    root: int,
) -> list[int]:
    """
    Examples:
        >>> edges = [(0, 1), (0, 3), (1, 4), (1, 2)]
        >>> euler_tour(edges, 0)
        [0, 1, 4, -5, 2, -3, -2, 3, -4, -1]
    """
    n = len(tree_edges) + 1
    graph = dsalgo.graph.edges_to_graph(n, tree_edges)
    parent: list[typing.Optional[int]] = [None] * n
    tour = [-1] * (n << 1)

    st = [root]
    for i in range(n << 1):
        u = st.pop()
        tour[i] = u
        if u < 0:
            continue
        st.append(~u)
        for v in graph[u][::-1]:
            if v == parent[u]:
                continue
            parent[v] = u
            st.append(v)
    return tour


def to_nodes(tour_edges: list[int]) -> list[int]:
    """Convert Euler-tour-on-edges to Euler-tour-on-nodes.

    Args:
        tour_edges (list[int]): euler tour on edges.

    Returns:
        list[int]: euler tour on nodes.

    Examples:
        >>> tour_edges = [0, 1, 4, -5, 2, -3, -2, 3, -4, -1]
        >>> to_nodes(tour_edges)
        [0, 1, 4, 1, 2, 1, 0, 3, 0]
    """
    parent = compute_parent(tour_edges)
    tour_nodes: list[int] = []
    for u in tour_edges[:-1]:
        if u >= 0:
            tour_nodes.append(u)
        else:
            p = parent[~u]
            assert p is not None
            tour_nodes.append(p)
    return tour_nodes


def compute_parent(
    tour_edges: list[int],
) -> list[typing.Optional[int]]:
    """Compute parent from Euler-tour-on-edges.

    Args:
        tour_edges (list[int]): euler tour on edges.

    Returns:
        list[typing.Optional[int]]:
            parent list.
            the tour root's parent is None.

    Examples:
        >>> tour_edges = [0, 1, 4, -5, 2, -3, -2, 3, -4, -1]
        >>> compute_parent(tour_edges)
        [None, 0, 1, 0, 1]
    """
    n = len(tour_edges) >> 1
    parent: list[typing.Optional[int]] = [None] * n
    st = [tour_edges[0]]
    for u in tour_edges[1:]:
        if u < 0:
            st.pop()
            continue
        parent[u] = st[-1]
        st.append(u)

    return parent


def compute_depth(tour_edges: list[int]) -> list[int]:
    """Compute depth from Euler-tour-on-edges.

    Args:
        tour_edges (list[int]): euler tour on edges.

    Returns:
        list[int]: depth list.

    Examples:
        >>> tour_edges = [0, 1, 4, -5, 2, -3, -2, 3, -4, -1]
        >>> compute_depth(tour_edges)
        [0, 1, 2, 1, 2]

    """
    n = len(tour_edges) >> 1
    parent = compute_parent(tour_edges)
    depth = [0] * n
    for u in tour_edges[1:]:
        if u < 0:
            continue
        p = parent[u]
        assert p is not None
        depth[u] = depth[p] + 1
    return depth


def compute_first_index(tour_nodes: list[int]) -> list[int]:
    """Compute first index in euler tour from euler tour on nodes.

    Args:
        tour_nodes (list[int]): euler tour on nodes.

    Returns:
        list[int]: first indices.

    Examples:
        >>> tour_nodes = [0, 1, 4, 1, 2, 1, 0, 3, 0]
        >>> compute_first_index(tour_nodes)
        [0, 1, 4, 7, 2]
    """
    n = len(tour_nodes) + 1 >> 1
    first_idx = [-1] * n
    for i, u in enumerate(tour_nodes):
        if first_idx[u] == -1:
            first_idx[u] = i
    return first_idx


def compute_last_index(tour_nodes: list[int]) -> list[int]:
    """Compute last index in euler tour from euler tour on nodes.

    Args:
        tour_nodes (list[int]): euler tour on nodes.

    Returns:
        list[int]: last indices.

    Examples:
        >>> tour_nodes = [0, 1, 4, 1, 2, 1, 0, 3, 0]
        >>> compute_last_index(tour_nodes)
        [8, 5, 4, 7, 2]
    """

    n = len(tour_nodes) + 1 >> 1
    last_idx = [-1] * n
    for i, u in enumerate(tour_nodes):
        last_idx[u] = i
    return last_idx


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
