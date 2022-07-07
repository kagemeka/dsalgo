import unittest


def modular_inverse_fermat(p: int, x: int) -> int:
    return pow(x, p - 2, p)


class Tests(unittest.TestCase):
    def test(self) -> None:
        mod = 1_000_000_007
        assert modular_inverse_fermat(mod, 2) == (mod + 1) >> 1


if __name__ == "__main__":
    import doctest

    unittest.main()

    doctest.testmod(verbose=True)
