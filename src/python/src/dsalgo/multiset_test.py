import unittest

import dsalgo.multiset


class Test(unittest.TestCase):
    def test(self) -> None:
        ms = dsalgo.multiset.FenwickTree(max_value=1 << 10)
        self.assertIsNone(ms.min())
        self.assertIsNone(ms.max())
        ms.insert(5)
        self.assertEqual(len(ms), 1)
        ms.insert(1000)
        self.assertEqual(len(ms), 2)
        ms.insert(5)
        self.assertEqual(len(ms), 3)
        self.assertEqual(ms.max(), 1000)
        self.assertEqual(ms.min(), 5)
        with self.assertRaises(AssertionError):
            ms.insert(1 << 10)
        self.assertEqual(ms.lower_bound(5), 0)
        self.assertEqual(ms.upper_bound(5), 2)
        self.assertEqual(ms.lower_bound(6), 2)
        self.assertEqual(ms.upper_bound(4), 0)
        ms.remove(1000)
        with self.assertRaises(KeyError):
            ms.remove(1000)
        self.assertEqual(len(ms), 2)
        ms.remove_all(5)
        self.assertTrue(ms.is_empty())


if __name__ == "__main__":
    unittest.main()
