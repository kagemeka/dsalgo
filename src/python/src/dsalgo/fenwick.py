# TODO:
# abelian group fenwick tree, invert as method of normal fenwick tree.
# type assertion and cast of m with isinstance(), typing.cast()
# if failed, raise not implemented error

from __future__ import annotations

import typing
import unittest

from dsalgo.algstr import Group, Monoid

S = typing.TypeVar("S")


class Fw(typing.Generic[S]):
    _g: Monoid[S]  # Commutative
    _d: typing.List[S]  # data

    def __init__(self, g: Monoid[S], a: typing.List[S]) -> None:
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
        """a[i] = op(a[i], v)"""
        n = len(self)
        assert 0 <= i < n
        i += 1
        while i <= n:
            self._d[i] = self._g.op(self._d[i], v)
            i += i & -i

    def __getitem__(self, i: int) -> S:
        """\prod_{j=0}^{i-1} a[j]"""
        v = self._g.e()
        while i > 0:
            v = self._g.op(v, self._d[i])
            i -= i & -i
        return v

    def _max(self, f: typing.Callable[[S], bool], l: int, v: S) -> int:
        n = len(self)
        d = 1 << n.bit_length()
        i = 0
        while True:
            d >>= 1
            if d == 0:
                assert l <= i and i <= n
                return i
            if i + d > n:
                continue
            nv = self._g.op(v, self._d[i + d])
            if i + d <= l or f(nv):
                i += d
                v = nv

    def max(self, f: typing.Callable[[S], bool]) -> int:
        # max i such that is_ok(fw[i]) is true.
        return self._max(f, 0, self._g.e())


class Abel(Fw[S]):
    _g: Group[S]  # abelian

    def __init__(self, g: Group[S], a: typing.List[S]) -> None:
        super().__init__(g, a)

    def get(self, l: int, r: int) -> S:
        # reduce [l, r)
        return self._g.op(self._g.inv(self[l]), self[r])

    def max_from(self, f: typing.Callable[[S], bool], l: int) -> int:
        return self._max(f, l, self._g.inv(self[l]))

    def min_from(self, f: typing.Callabel[[S], bool], r: int) -> int:
        n = len(self)
        assert 0 <= r <= n
        if r == 0:
            return 0
        d = 1 << n.bit_length()
        v = self[r]
        if f(v):
            return 0
        i = 1
        while True:
            d >>= 1
            if d == 0:
                assert 0 <= i and i <= r
                return i
            if i + d > r:
                continue
            nv = self._g.op(self._g.inv(self[i + d - 1]), v)
            if not f(nv):
                i += d
                v = nv


class TestAbel(unittest.TestCase):
    def test(self) -> None:
        import operator

        g = Group[int](op=operator.add, e=lambda: 0, inv=lambda x: -x)
        a = [0, 1, 2, 3, 4]
        fw = Abel(g, a)
        assert fw[3] == 3
        fw[2] = 2
        fw[3] == 5
        assert fw.get(1, 4) == 8


class Abel2D(typing.Generic[S]):
    # 2D fenwick tree for abelian group
    _g: Group[S]
    _d: typing.List[Abel[S]]

    def __init__(self, g: Group[S], a: typing.List[typing.List[S]]) -> None:
        h, w = len(a), len(a[0])
        d = [Abel(g, [g.e() for _ in range(w)])] + [Abel(g, row) for row in a]
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
    def shape(self) -> typing.Tuple[int, int]:
        return (len(self._d) - 1, len(self._d[0]) - 1)

    def __setitem__(self, ij: typing.Tuple[int, int], v: S) -> None:
        """
        operate v on a[i][j].
        """
        i, j = ij
        h, w = self.shape
        assert 0 <= i < h and 0 <= j < w
        i += 1
        while i <= h:
            self._d[i][j] = v
            i += i & -i

    def __getitem__(self, ij: typing.Tuple[int, int]) -> S:
        """reduce range [0, i) & [0, j)"""
        i, j = ij
        v = self._g.e()
        while i > 0:
            v = self._g.op(v, self._d[i][j])
            i -= i & -i
        return v

    def get(self, i0: int, i1: int, j0: int, j1: int) -> S:
        # reduce [i0, i1) & [j0, j1)
        v = self[i1, j1]
        v = self._g.op(v, self._g.inv(self[i1, j0]))
        v = self._g.op(v, self._g.inv(self[i0, j1]))
        return self._g.op(v, self[i0, j0])


class Dual(typing.Generic[S]):
    _g: Group[S]  # Abelian
    _fw: Fw[S]

    def __init__(self, g: Group[S], a: typing.List[S]) -> None:
        n = len(a)
        assert n > 0
        for i in range(n - 1, 0, -1):
            a[i] = g.op(g.inv(a[i - 1]), a[i])
        self._g, self._fw = g, Fw[S](g, a)

    def __setitem__(self, lr: typing.Tuple[int, int], x: S) -> None:
        n = len(self._fw)
        l, r = lr
        assert 0 <= lr <= n
        self.__fw[left] = x
        if right < n:
            self.__fw[right] = self._g.invert(x)

    def __getitem__(self, i: int) -> S:
        # return a[i]
        assert 0 <= i < len(self.__fw)
        return self.__fw[i + 1]


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


class FwMultiset:
    __max_value: int

    def __init__(self, max_value: int) -> None:
        """instance can contain values range of [0, max_value)."""
        self.__fw = FwIntAdd([0] * max_value)

        self.__max_value = max_value

    @property
    def max_value(self) -> int:
        return self.__max_value

    def __len__(self) -> int:
        return self.__fw[self.max_value]

    def __contains__(self, x: int) -> bool:
        return self.count(x) >= 1

    def count(self, x: int) -> int:
        if x < 0 or self.max_value <= x:
            return 0
        return self.__fw.get_range(x, x + 1)

    def is_empty(self) -> bool:
        return len(self) == 0

    def __bool__(self) -> bool:
        return not self.is_empty()

    def insert(self, x: int) -> None:
        assert 0 <= x < self.max_value
        self.__fw[x] = 1

    def remove(self, x: int) -> None:
        if x not in self:
            raise KeyError(x)
        self.__fw[x] = -1

    def remove_all(self, x: int) -> None:
        assert 0 <= x < self.max_value
        self.__fw[x] = -self.count(x)

    def __getitem__(self, i: int) -> int | None:
        """Return i-th element."""
        if not 0 <= i < len(self):
            return None
        return self.__fw.max_right(lambda v: v < i + 1)

    def min(self) -> int | None:
        return None if len(self) == 0 else self[0]

    def max(self) -> int | None:
        return None if len(self) == 0 else self[len(self) - 1]

    def lower_bound(self, x: int) -> int:
        return self.__fw[x]

    def upper_bound(self, x: int) -> int:
        return self.__fw[x + 1]


# class Tests(unittest.TestCase):
#     def test_dual(self) -> None:
#         a = [0, 1, 2, 3, 4]
#         # g = Group[int](lambda x, y: x + y, lambda: 0, lambda x: -x)
#         # fw = FwDual(g, a)
#         # fw.set(1, 5, 2)
#         # assert fw[3] == 5
#         # assert fw[0] == 0

#     def test_2d(self) -> None:
#         import operator

#         g = Group(op=operator.add, e=lambda: 0, inv=lambda x: -x)

#         h, w = 3, 3
#         a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#         fw = Fw2DAbel(g, a)

#         def assert_sum() -> None:
#             for i0 in range(h + 1):
#                 for i1 in range(i0, h + 1):
#                     for j0 in range(w + 1):
#                         for j1 in range(j0, w + 1):
#                             assert fw.reduce(i0, i1, j0, j1) == sum(
#                                 a[i][j]
#                                 for i in range(i0, i1)
#                                 for j in range(j0, j1)
#                             )

#         assert_sum()
#         fw.operate(1, 1, -1)
#         a[1][1] -= 1
#         assert_sum()

#     def test_fw_multiset(self) -> None:
#         ms = FwMultiset(max_value=1 << 10)
#         self.assertIsNone(ms.min())
#         self.assertIsNone(ms.max())
#         ms.insert(5)
#         self.assertEqual(len(ms), 1)
#         ms.insert(1000)
#         self.assertEqual(len(ms), 2)
#         ms.insert(5)
#         self.assertEqual(len(ms), 3)
#         self.assertEqual(ms.max(), 1000)
#         self.assertEqual(ms.min(), 5)
#         with self.assertRaises(AssertionError):
#             ms.insert(1 << 10)
#         self.assertEqual(ms.lower_bound(5), 0)
#         self.assertEqual(ms.upper_bound(5), 2)
#         self.assertEqual(ms.lower_bound(6), 2)
#         self.assertEqual(ms.upper_bound(4), 0)
#         ms.remove(1000)
#         with self.assertRaises(KeyError):
#             ms.remove(1000)
#         self.assertEqual(len(ms), 2)
#         ms.remove_all(5)
#         self.assertTrue(ms.is_empty())


# class TestFenwickTree2D(unittest.TestCase):
#     def test(self) -> None:
#         monoid = dsalgo.algebraic_structure.Monoid[int](
#             lambda x, y: x + y,
#             lambda: 0,
#         )
#         fw = dsalgo.fenwick_tree.FenwickTree2D(monoid, (4, 5))
#         fw.set(1, 2, 1)
#         self.assertEqual(fw.get(2, 3), 1)
#         fw.set(0, 3, -1)
#         fw.set(2, 0, 3)
#         self.assertEqual(fw.get(3, 3), 4)
#         self.assertEqual(fw.get(2, 4), 0)


# class TestFenwickTreeIntAdd2D(unittest.TestCase):
#     def test(self) -> None:
#         fw = dsalgo.fenwick_tree.FenwickTreeIntAdd2D((4, 5))
#         fw.set(1, 2, 1)
#         self.assertEqual(fw.get(2, 3), 1)
#         fw.set(0, 3, -1)
#         fw.set(2, 0, 3)
#         self.assertEqual(fw.get(3, 3), 4)
#         self.assertEqual(fw.get(2, 4), 0)


# class TestDualFenwickTree(unittest.TestCase):
#     def test(self) -> None:
#         group = dsalgo.algebraic_structure.Group[int](
#             lambda x, y: x + y,
#             lambda: 0,
#             lambda x: -x,
#         )
#         fw = dsalgo.fenwick_tree.DualFenwickTree[int](group, list(range(5)))
#         self.assertEqual(fw[4], 4)
#         fw.set(1, 3, 2)
#         self.assertEqual(fw[2], 4)


# class TestDualFenwickTreeIntAdd(unittest.TestCase):
#     def test(self) -> None:
#         fw = dsalgo.fenwick_tree.DualFenwickTreeIntAdd(list(range(5)))
#         self.assertEqual(fw[4], 4)
#         fw.set(1, 3, 2)
#         self.assertEqual(fw[2], 4)

if __name__ == "__main__":
    import doctest

    unittest.main()

    doctest.testmod(verbose=True)
