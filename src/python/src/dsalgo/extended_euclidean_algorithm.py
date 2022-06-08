import unittest


def extgcd(a: int, b: int) -> tuple[int, int, int]:
    x00, x01, x10, x11 = 1, 0, 0, 1  # matrix identity element.
    while b:
        q = a // b
        x00, x01 = x01, x00 - q * x01
        x10, x11 = x11, x10 - q * x11
        a, b = b, a % b
    if a < 0:
        a *= -1
        x00 *= -1
        x10 *= -1
    return a, x00, x10


class Tests(unittest.TestCase):
    def test(self) -> None:
        assert extgcd(-30, 111) == (3, 11, 3)
        assert extgcd(111, 30) == (3, 3, -11)
        assert extgcd(0, 0) == (0, 1, 0)


if __name__ == "__main__":
    import doctest

    unittest.main()

    doctest.testmod(verbose=True)
