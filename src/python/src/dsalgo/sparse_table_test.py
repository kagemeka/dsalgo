import operator
import unittest

import dsalgo.algstr
import dsalgo.sparse_table


class TestSparseTable(unittest.TestCase):
    def test_min(self) -> None:
        a = [3, 1, 2, 10, -1]
        semigroup = dsalgo.algstr.Semigroup[int](min)
        get_min = dsalgo.sparse_table.sparse_table(semigroup, a)
        self.assertEqual(get_min(0, 5), -1)
        self.assertEqual(get_min(0, 1), 3)
        self.assertEqual(get_min(0, 3), 1)


class TestDisjointSparseTable(unittest.TestCase):
    def test_min(self) -> None:
        a = [3, 1, 2, 10, -1]
        semigroup = dsalgo.algstr.Semigroup[int](min)
        get_min = dsalgo.sparse_table.disjoint_sparse_table(semigroup, a)
        self.assertEqual(get_min(0, 5), -1)
        self.assertEqual(get_min(0, 1), 3)
        self.assertEqual(get_min(0, 3), 1)

    def test_sum(self) -> None:
        a = [3, 1, 2, 10, -1]
        semigroup = dsalgo.algstr.Semigroup[int](operator.add)
        get_sum = dsalgo.sparse_table.disjoint_sparse_table(semigroup, a)
        self.assertEqual(get_sum(0, 5), 15)
        self.assertEqual(get_sum(0, 1), 3)
        self.assertEqual(get_sum(0, 3), 6)

    def test_xor(self) -> None:
        a = [3, 1, 2, 10, 0]
        semigroup = dsalgo.algstr.Semigroup[int](operator.xor)
        get_xor = dsalgo.sparse_table.disjoint_sparse_table(semigroup, a)
        self.assertEqual(get_xor(0, 5), 10)
        self.assertEqual(get_xor(0, 1), 3)
        self.assertEqual(get_xor(0, 3), 0)


class TestDisjointSparseTableIntXor(unittest.TestCase):
    def test(self) -> None:
        a = [3, 1, 2, 10, 0]
        get_xor = dsalgo.sparse_table.disjoint_sparse_table_int_xor(a)
        self.assertEqual(get_xor(0, 5), 10)
        self.assertEqual(get_xor(0, 1), 3)
        self.assertEqual(get_xor(0, 3), 0)


class TestDisjointSparseTableIntSum(unittest.TestCase):
    def test(self) -> None:
        a = [3, 1, 2, 10, -1]
        get_sum = dsalgo.sparse_table.disjoint_sparse_table_int_sum(a)
        self.assertEqual(get_sum(0, 5), 15)
        self.assertEqual(get_sum(0, 1), 3)
        self.assertEqual(get_sum(0, 3), 6)


class TestSparseTable2D(unittest.TestCase):
    def test(self) -> None:
        a = [
            [0, 1, 2, 3],
            [4, 5, 6, 7],
            [-1, 4, 0, 1],
        ]
        semigroup = dsalgo.algstr.Semigroup[int](min)
        get_min = dsalgo.sparse_table.sparse_table_2d(semigroup, a)
        self.assertEqual(get_min(0, 0, 3, 4), -1)
        self.assertEqual(get_min(0, 1, 3, 4), 0)
        self.assertEqual(get_min(1, 3, 2, 4), 7)
        self.assertEqual(get_min(1, 1, 2, 3), 5)
        self.assertEqual(get_min(0, 2, 2, 3), 2)


class TestSparseTable2DFixedShape(unittest.TestCase):
    def test(self) -> None:
        a = [
            [0, 1, 2, 3],
            [4, 5, 6, 7],
            [-1, 4, 0, 1],
        ]
        semigroup = dsalgo.algstr.Semigroup[int](min)
        get_min = dsalgo.sparse_table.sparse_table_2d_fixed_window(
            semigroup,
            a,
            (2, 2),
        )
        self.assertEqual(get_min(0, 0), 0)
        self.assertEqual(get_min(1, 0), -1)
        self.assertEqual(get_min(0, 2), 2)
        with self.assertRaises(IndexError):
            get_min(0, 3)


if __name__ == "__main__":
    unittest.main()
