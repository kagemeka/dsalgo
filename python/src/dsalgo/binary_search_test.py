import unittest

import dsalgo.binary_search


class Test(unittest.TestCase):
    def test_binary_search(self) -> None:
        def is_ok(bl: bool) -> bool:
            return bl

        a = [False, True, True]
        self.assertEqual(dsalgo.binary_search.binary_search(is_ok, a), 1)
        self.assertEqual(
            dsalgo.binary_search.binary_search(is_ok, a, hi=0),
            0,
        )
        self.assertEqual(
            dsalgo.binary_search.binary_search(is_ok, a, lo=2),
            2,
        )
        with self.assertRaises(AssertionError):
            dsalgo.binary_search.binary_search(is_ok, a, lo=2, hi=1)
        self.assertEqual(dsalgo.binary_search.binary_search(is_ok, []), 0)
        self.assertEqual(dsalgo.binary_search.binary_search(is_ok, [False]), 1)
        self.assertEqual(dsalgo.binary_search.binary_search(is_ok, [True]), 0)


if __name__ == "__main__":
    unittest.main()
