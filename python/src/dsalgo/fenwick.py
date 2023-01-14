# TODO:
# abelian group fenwick tree, invert as method of normal fenwick tree.
# type assertion and cast of m with isinstance(), typing.cast()
# if failed, raise not implemented error

from __future__ import annotations

import typing
import unittest

from python.src.dsalgo.algebraic_structure import Group, Monoid

S = typing.TypeVar("S")


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


# class Tests(unittest.TestCase):

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


if __name__ == "__main__":
    import doctest

    unittest.main()

    doctest.testmod(verbose=True)
