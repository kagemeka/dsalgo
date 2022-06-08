import unittest


def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return abs(a)


class Tests(unittest.TestCase):
    def test(self) -> None:
        assert gcd(100, -3) == 1
        assert gcd(-1, 0) == 1
        assert gcd(0, 0) == 0


class TestGCD(unittest.TestCase):
    def test_gcd(self) -> None:
        self.assertEqual(dsalgo.euclidean_algorithm.greatest_common_divisor(5, 7), 1)
        self.assertEqual(dsalgo.euclidean_algorithm.greatest_common_divisor(5, 0), 5)
        self.assertEqual(dsalgo.euclidean_algorithm.greatest_common_divisor(4, 0), 4)
        self.assertEqual(
            dsalgo.euclidean_algorithm.greatest_common_divisor(4, 0),
            dsalgo.euclidean_algorithm.greatest_common_divisor(0, 4),
        )
        self.assertEqual(dsalgo.euclidean_algorithm.greatest_common_divisor(9, 6), 3)
        self.assertEqual(dsalgo.euclidean_algorithm.greatest_common_divisor(0, 0), 0)

    def test_array_gcd(self) -> None:
        self.assertEqual(
            dsalgo.euclidean_algorithm.array_gcd([15, 35, 21]),
            1,
        )


if __name__ == "__main__":
    import doctest

    unittest.main()

    doctest.testmod(verbose=True)
