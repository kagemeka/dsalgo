import unittest

import dsalgo.euclidean


class TestLCM(unittest.TestCase):
    def test_lcm(self) -> None:
        self.assertEqual(dsalgo.euclidean.least_common_multiple(0, 0), 0)
        self.assertEqual(dsalgo.euclidean.least_common_multiple(0, 10), 0)
        self.assertEqual(dsalgo.euclidean.least_common_multiple(10, 0), 0)
        self.assertEqual(dsalgo.euclidean.least_common_multiple(9, 6), 18)


class TestGCD(unittest.TestCase):
    def test_gcd(self) -> None:
        self.assertEqual(dsalgo.euclidean.greatest_common_divisor(5, 7), 1)
        self.assertEqual(dsalgo.euclidean.greatest_common_divisor(5, 0), 5)
        self.assertEqual(dsalgo.euclidean.greatest_common_divisor(4, 0), 4)
        self.assertEqual(
            dsalgo.euclidean.greatest_common_divisor(4, 0),
            dsalgo.euclidean.greatest_common_divisor(0, 4),
        )
        self.assertEqual(dsalgo.euclidean.greatest_common_divisor(9, 6), 3)
        self.assertEqual(dsalgo.euclidean.greatest_common_divisor(0, 0), 0)

    def test_array_gcd(self) -> None:
        self.assertEqual(
            dsalgo.euclidean.array_gcd([15, 35, 21]),
            1,
        )


class TestExtendedEuclidean(unittest.TestCase):
    def test_recurse(self) -> None:
        self.assertEqual(
            dsalgo.euclidean.extended_euclidean_recurse(111, 30),
            (3, 3, -11),
        )

    def test(self) -> None:
        self.assertEqual(
            dsalgo.euclidean.extended_euclidean(111, 30),
            (3, 3, -11),
        )


if __name__ == "__main__":
    unittest.main()
