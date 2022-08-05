import unittest


def extgcd_recurse(a: int, b: int) -> tuple[int, int, int]:
    if not b:
        return (a, 1, 0) if a >= 0 else (-a, -1, 0)
    g, s, t = extgcd_recurse(b, a % b)
    return g, t, s - a // b * t


# TODO:
class Tests(unittest.TestCase):
    def test(self) -> None:
        assert extgcd_recurse(-30, 111) == (3, 11, 3)
        assert extgcd_recurse(111, 30) == (3, 3, -11)
        assert extgcd_recurse(0, 0) == (0, 1, 0)


if __name__ == "__main__":
    import doctest

    unittest.main()

    doctest.testmod(verbose=True)
