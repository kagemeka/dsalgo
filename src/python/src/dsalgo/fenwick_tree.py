# TODO:
# abelian group fenwick tree, invert as method of normal fenwick tree.
# type assertion and cast of m with isinstance(), typing.cast()
# if failed, raise not implemented error

from __future__ import annotations
import unittest

import typing

from dsalgo.algebraic_structure import Monoid, Group
from dsalgo.type import S


class Fenwick(typing.Generic[S]):
    _g: Monoid[S]  # Commutative
    _d: typing.List[S]  # data

    def __init__(self, g: Monoid[S], a: list[S]) -> None:
        """Not from size because intial values might not be identity."""
        n = len(a)
        a = [g.e()] + a
        for i in range(1, n):
            j = i + (i & -i)
            if j <= n:
                a[j] = g.op(a[j], a[i])
        self._g, self._d = g, a

    def __len__(self) -> int:
        return len(self._d) - 1

    def __setitem__(self, i: int, v: S) -> None:
        """operate"""
        n = len(self)
        assert 0 <= i < n
        i += 1
        while i <= n:
            self._d[i] = self._g.op(self._d[i], v)
            i += i & -i

    def __getitem__(self, i: int) -> S:
        """reduce less than"""
        v = self._g.e()
        while i > 0:
            v = self._g.op(v, self._d[i])
            i -= i & -i
        return v

    def max_right(self, is_ok: typing.Callable[[S], bool]) -> int:
        n = len(self)
        leng = 1 << n.bit_length()
        v, r = self._g.e(), 0
        while True:
            leng >>= 1
            if leng == 0:
                return r
            if r + leng > n:
                continue
            nv = self._g.op(v, self._d[r + leng])
            if is_ok(nv):
                r += leng
                v = nv


class FwAbelian(Fenwick[S]):
    _g: Group[S]

    def __init__(self, g: Group[S], a: list[S]) -> None:
        super().__init__(g, a)

    def reduce(self, l: int, r: int) -> S:
        return self._g.op(self._g.inv(self[l]), self[r])


class FwIntAdd:
    """faster than abstract one"""

    _d: typing.List[int]

    def __init__(self, a: list[int]) -> None:
        n = len(a)
        a = [0] + a
        for i in range(n):
            j = i + (i & -i)
            if j <= n:
                a[j] += a[i]
        self._d = a

    def __len__(self) -> int:
        return len(self._d) - 1

    def __setitem__(self, i: int, x: int) -> None:
        assert 0 <= i < len(self)
        i += 1
        while i < len(self) + 1:
            self._d[i] += x
            i += i & -i

    def __getitem__(self, i: int) -> int:
        v = 0
        while i > 0:
            v += self._d[i]
            i -= i & -i
        return v

    def get_range(self, l: int, r: int) -> int:
        return self[r] - self[l]

    def max_right(self, is_ok: typing.Callable[[int], bool]) -> int:
        n = len(self)
        leng = 1 << n.bit_length()
        v, r = 0, 0
        while True:
            leng >>= 1
            if leng == 0:
                return r
            if r + leng > n:
                continue
            if is_ok(v + self._d[r + leng]):
                r += leng
                v += self._d[r]


class Fw2DAbelian(typing.Generic[S]):
    _g: Group[S]
    _d: typing.List[FwAbelian[S]]

    def __init__(self, g: Monoid[S], a: list[list[S]]) -> None:
        h, w = len(a), len(a[0])
        d = [FwAbelian(g, [g.e() for _ in range(w)])] + [
            FwAbelian(g, row) for row in a
        ]
        for i in range(1, h):
            ni = i + (i & -i)
            if ni > h:
                break
            ri = d[i]._d
            rni = d[ni]._d
            for j in range(1, w + 1):
                rni[j] = g.op(rni[j], ri[j])
        self._g, self._d = g, d

    @property
    def shape(self) -> tuple[int, int]:
        return (len(self._d) - 1, len(self._d[0]) - 1)

    def operate(self, i: int, j: int, v: S) -> None:
        """
        operate v on a[i][j].
        tuple indexing is slow.
        """
        h, w = self.shape
        assert 0 <= i < h and 0 <= j < w
        i += 1
        while i <= h:
            self._d[i][j] = v

            i += i & -i

    def reduce_lt(self, i: int, j: int) -> S:
        """reduce range [0, i) & [0, j)"""
        v = self._g.e()
        while i > 0:
            v = self._g.op(v, self._d[i][j])
            i -= i & -i

        return v

    def reduce(self, i0: int, i1: int, j0: int, j1: int) -> S:
        v = self.reduce_lt(i1, j1)
        v = self._g.op(v, self._g.inv(self.reduce_lt(i1, j0)))
        v = self._g.op(v, self._g.inv(self.reduce_lt(i0, j1)))
        return self._g.op(v, self.reduce_lt(i0, j0))


# class FwDual(typing.Generic[S]):
#     _g: Group[S]  # Abelian

#     def __init__(self, g: Group[S], a: list[S]) -> None:
#         """
#         group: Abelian Group.
#         """
#         n = len(arr)
#         assert n > 0
#         delta = [arr[0]]
#         for i in range(n - 1):
#             delta.append(group.op(group.invert(arr[i]), arr[i + 1]))
#         self.__fw = FenwickTree[S](group, delta)
#         self._g = group

#     def set(self, left: int, right: int, x: S) -> None:
#         n = len(self.__fw)
#         assert 0 <= left < right <= n
#         self.__fw[left] = x
#         if right < n:
#             self.__fw[right] = self._g.invert(x)

#     def __getitem__(self, i: int) -> S:
#         assert 0 <= i < len(self.__fw)
#         return self.__fw[i + 1]


# class FwDualIntAdd:
#     def __init__(self, arr: list[int]) -> None:
#         n = len(arr)
#         assert n > 0
#         delta = [arr[0]]
#         for i in range(n - 1):
#             delta.append(arr[i + 1] - arr[i])
#         self.__fw = FenwickTreeIntAdd(delta)

#     def set(self, left: int, right: int, x: int) -> None:
#         n = len(self.__fw)
#         assert 0 <= left < right <= n
#         self.__fw[left] = x
#         if right < n:
#             self.__fw[right] = -x

#     def __getitem__(self, i: int) -> int:
#         assert 0 <= i < len(self.__fw)
#         return self.__fw[i + 1]


# class FwLazyIntAdd:
#     """
#     Examples:
#         >>> a = [0, 1, 2, 3, 4]
#         >>> fw = FenwickTreeAddSum(a)
#         >>> fw.set(0, 3, 2)
#         >>> fw.get(2, 5)
#         11
#     """

#     def __init__(self, arr: list[int]) -> None:
#         n = len(arr)
#         self.__fw_0 = dsalgo.fenwick_tree.FenwickTreeIntAdd(arr)
#         self.__fw_1 = dsalgo.fenwick_tree.FenwickTreeIntAdd([0] * n)

#     def __len__(self) -> int:
#         return len(self.__fw_0)

#     def set(self, left: int, right: int, x: int) -> None:
#         assert 0 <= left < right <= len(self)
#         self.__fw_0[left] = -x * left
#         self.__fw_1[left] = x
#         if right < len(self):
#             self.__fw_0[right] = x * right
#             self.__fw_1[right] = -x

#     def get(self, left: int, right: int) -> int:
#         assert 0 <= left <= right <= len(self)
#         fw0, fw1 = self.__fw_0, self.__fw_1
#         return fw0[right] + fw1[right] * right - fw0[left] - fw1[left] * left


# mypy: ignore-errors


class Tests(unittest.TestCase):
    def test_fenwick(self) -> None:
        import operator

        g = Group(op=operator.add, e=lambda: 0, inv=lambda x: -x)
        a = [0, 1, 2, 3, 4]
        fw = FwAbelian(g, a)
        assert fw[3] == 3
        fw[2] = 2
        fw[3] == 5

    def test_dual(self) -> None:
        a = [0, 1, 2, 3, 4]
        # g = Group[int](lambda x, y: x + y, lambda: 0, lambda x: -x)
        # fw = FwDual(g, a)
        # fw.set(1, 5, 2)
        # assert fw[3] == 5
        # assert fw[0] == 0

    def test_2d(self) -> None:
        import operator

        g = Group(op=operator.add, e=lambda: 0, inv=lambda x: -x)

        h, w = 3, 3
        a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        fw = Fw2DAbelian(g, a)

        def assert_sum() -> None:
            for i0 in range(h + 1):
                for i1 in range(i0, h + 1):
                    for j0 in range(w + 1):
                        for j1 in range(j0, w + 1):
                            assert fw.reduce(i0, i1, j0, j1) == sum(
                                a[i][j]
                                for i in range(i0, i1)
                                for j in range(j0, j1)
                            )

        assert_sum()
        fw.operate(1, 1, -1)
        a[1][1] -= 1
        assert_sum()


if __name__ == "__main__":
    import doctest

    unittest.main()

    doctest.testmod(verbose=True)
