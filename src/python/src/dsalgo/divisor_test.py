import unittest

import dsalgo.divisor


class TestCountDivisors(unittest.TestCase):
    def test(self) -> None:
        self.assertEqual(
            dsalgo.divisor.count_divisors_zeta_transform(20),
            [0, 1, 2, 2, 3, 2, 4, 2, 4, 3, 4, 2, 6, 2, 4, 4, 5, 2, 6, 2],
        )


class TestFindDivisors(unittest.TestCase):
    def test(self) -> None:
        self.assertEqual(
            dsalgo.divisor.find_divisors(100),
            [1, 2, 4, 5, 10, 20, 25, 50, 100],
        )


if __name__ == "__main__":
    unittest.main()
