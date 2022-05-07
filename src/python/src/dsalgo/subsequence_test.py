import unittest

import dsalgo.subsequence


class Test(unittest.TestCase):
    def test_count_common_subsequences(self) -> None:
        a = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        b = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        self.assertEqual(
            dsalgo.subsequence.count_common_subsequences(a, b, 10**9 + 7),
            846527861,
        )

    def test_longest_common_subsequence(self) -> None:
        s = "algorithm"
        t = "datastructure"
        self.assertEqual(
            dsalgo.subsequence.longest_common_subsequence(s, t),
            ["a", "r", "t"],
        )


if __name__ == "__main__":
    unittest.main()
