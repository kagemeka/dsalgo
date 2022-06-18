from __future__ import annotations

import typing
import unittest

import dsalgo.algebraic_structure
import dsalgo.segment_tree


class Test(unittest.TestCase):
    def test_segment_tree(self) -> None:
        monoid = dsalgo.algebraic_structure.Monoid[int](
            operation=lambda a, b: a + b,
            identity=lambda: 0,
        )
        n = 10
        arr = list(range(n))
        Classes = [
            dsalgo.segment_tree.SegmentTree[int],
            dsalgo.segment_tree.SegmentTreeDFS[int],
        ]

        for Class in Classes:
            seg = Class(monoid, arr)
            self.assertEqual(seg.get(0, n), sum(arr))
            seg[0] = 1
            self.assertEqual(seg.get(0, n), sum(arr) + 1)
            seg[0] = 0
            self.assertEqual(seg.get(0, n), sum(arr))
            self.assertEqual(seg.size, 10)
            self.assertEqual(seg[5], 5)
            seg[5] = 10
            self.assertEqual(seg.get(0, 10), 50)
            self.assertEqual(seg.max_right(lambda s: s < 10, 0), 4)
            self.assertEqual(seg.max_right(lambda s: s < 10, 5), 5)
            self.assertEqual(seg.min_left(lambda s: s < 10, 7), 6)
            self.assertEqual(seg.min_left(lambda s: s < 10, 6), 6)
            self.assertEqual(seg.min_left(lambda s: s < 10, 5), 2)
            self.assertEqual(seg.min_left(lambda s: s < 10, 4), 0)

    def test_segment_tree_lazy(self) -> None:
        monoid_s = dsalgo.algebraic_structure.Monoid[typing.Tuple[int, int]](
            operation=lambda a, b: (a[0] + b[0], a[1] + b[1]),
            identity=lambda: (0, 0),
        )
        monoid_f = dsalgo.algebraic_structure.Monoid[int](
            operation=lambda f, g: f + g,
            identity=lambda: 0,
        )

        def map_(f: int, x: tuple[int, int]) -> tuple[int, int]:
            return (x[0] + f * x[1], x[1])

        arr = [(i, 1) for i in range(10)]

        Classes = [
            dsalgo.segment_tree.LazySegmentTree,
            dsalgo.segment_tree.LazySegmentTreeDFS,
        ]
        for Class in Classes:
            seg = Class(monoid_s, monoid_f, map_, arr)
            self.assertEqual(seg.get(0, 10), (45, 10))
            self.assertEqual(seg.get(0, 1), (0, 1))
            self.assertEqual(len(seg), 32)
            self.assertEqual(seg.size, 10)
            seg.update(5, (10, 1))
            self.assertEqual(seg.get(0, 10), (50, 10))
            seg.set(2, 6, 3)
            self.assertEqual(seg.get(3, 10), (56, 7))


if __name__ == "__main__":
    unittest.main()
