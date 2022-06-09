import math
import unittest


def lcm(a: int, b: int) -> int:
    return 0 if a == b == 0 else abs(a // math.gcd(a, b) * b)


class Tests(unittest.TestCase):
    def test(self) -> None:
        assert lcm(0, 0) == 0
        assert lcm(0, -1) == 0
        assert lcm(-1, 2) == 2
        assert lcm(6, 8) == 24


if __name__ == "__main__":
    import doctest

    unittest.main()

    doctest.testmod(verbose=True)
