import typing

import numba as nb
import numpy as np

try:
    from numba.experimental import jitclass
except ImportError:
    from numba import jitclass


# @nb.njit((nb.int64), )
# def uf_build(n: int) -> np.ndarray:
#     return np.full(n, -1, np.int64)


# @nb.njit
# def uf_find(uf: np.ndarray, u: int) -> int:
#     if uf[u] < 0:
#         return u
#     uf[u] = uf_find(uf, uf[u])
#     return uf[u]


# @nb.njit
# def uf_unite(uf: np.ndarray, u: int, v: int) -> None:
#     u, v = uf_find(uf, u), uf_find(uf, v)
#     if u == v:
#         return
#     if uf[u] > uf[v]:
#         u, v = v, u
#     uf[u] += uf[v]
#     uf[v] = u


@jitclass(
    [
        ("__data", nb.int64[:]),
    ],
    nopython=True,
)
class UnionFind:
    """UnionFind DataStructure."""

    def __init__(self, size: int) -> None:
        """Initialize with size.

        Args:
            size (int): count of nodes in UnionFind Forest.
        """
        self.__data = np.full(size, -1, np.int64)

    @property
    def size(self) -> int:
        """Length of data.

        Returns:
            int: equal to the size of nodes.
        """
        return len(self.__data)

    def find_root(self, node: int) -> int:
        """Find root node of the component in which given node contained.

        Args:
            node (int): target node.

        Returns:
            int: root node.
        """
        assert 0 <= node < self.size
        st = []
        while self.__data[node] >= 0:
            st.append(node)
            node = self.__data[node]
        root = node
        while st:
            self.__data[st.pop()] = root
        return root

    def unite(self, node_u: int, node_v: int) -> None:
        """Unite two components.

        Args:
            node_u (int): a node.
            node_v (int): another node.

        Note:
            If node_u and node_v are contained in the same components,
            do nothing and return early.
        """
        assert 0 <= node_u < self.size and 0 <= node_v < self.size
        node_u, node_v = self.find_root(node_u), self.find_root(node_v)
        if node_u == node_v:
            return
        if self.__data[node_u] > self.__data[node_v]:
            node_u, node_v = node_v, node_u
        self.__data[node_u] += self.__data[node_v]
        self.__data[node_v] = node_u

    def size_of(self, node: int) -> int:
        """Size of the component of given node.

        Args:
            node (int): an arbitrary node.

        Returns:
            int: [description]
        """
        assert 0 <= node < self.size
        return -self.__data[self.find_root(node)]
