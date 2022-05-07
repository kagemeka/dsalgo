import unittest

import dsalgo.abstract_structure
import dsalgo.fenwick_tree


class TestFenwickTree2D(unittest.TestCase):
    def test(self) -> None:
        monoid = dsalgo.abstract_structure.Monoid[int](
            lambda x, y: x + y,
            lambda: 0,
        )
        fw = dsalgo.fenwick_tree.FenwickTree2D(monoid, (4, 5))
        fw.set(1, 2, 1)
        self.assertEqual(fw.get(2, 3), 1)
        fw.set(0, 3, -1)
        fw.set(2, 0, 3)
        self.assertEqual(fw.get(3, 3), 4)
        self.assertEqual(fw.get(2, 4), 0)


class TestFenwickTreeIntAdd2D(unittest.TestCase):
    def test(self) -> None:
        fw = dsalgo.fenwick_tree.FenwickTreeIntAdd2D((4, 5))
        fw.set(1, 2, 1)
        self.assertEqual(fw.get(2, 3), 1)
        fw.set(0, 3, -1)
        fw.set(2, 0, 3)
        self.assertEqual(fw.get(3, 3), 4)
        self.assertEqual(fw.get(2, 4), 0)


class TestDualFenwickTree(unittest.TestCase):
    def test(self) -> None:
        group = dsalgo.abstract_structure.Group[int](
            lambda x, y: x + y,
            lambda: 0,
            lambda x: -x,
        )
        fw = dsalgo.fenwick_tree.DualFenwickTree[int](group, list(range(5)))
        self.assertEqual(fw[4], 4)
        fw.set(1, 3, 2)
        self.assertEqual(fw[2], 4)


class TestDualFenwickTreeIntAdd(unittest.TestCase):
    def test(self) -> None:
        fw = dsalgo.fenwick_tree.DualFenwickTreeIntAdd(list(range(5)))
        self.assertEqual(fw[4], 4)
        fw.set(1, 3, 2)
        self.assertEqual(fw[2], 4)


if __name__ == "__main__":
    unittest.main()
