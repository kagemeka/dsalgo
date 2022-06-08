import unittest


def gcd_recurse(a: int, b: int) -> int:
    return gcd_recurse(b, a % b) if b else abs(a)


class Tests(unittest.TestCase):
    def test(self) -> None:
        assert gcd_recurse(100, -3) == 1
        assert gcd_recurse(-1, 0) == 1
        assert gcd_recurse(0, 0) == 0


if __name__ == "__main__":
    import doctest

    unittest.main()

    doctest.testmod(verbose=True)
