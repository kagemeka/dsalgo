import functools


import unittest


def modular_factorial(mod: int, n: int) -> int:

    return functools.reduce(lambda x, y: x * y % mod, range(1, n + 1), 1)


class Tests(unittest.TestCase):
    def test(self) -> None:
        assert modular_factorial(1_000_000_007, 20) == 146326063


if __name__ == "__main__":
    import doctest

    unittest.main()

    doctest.testmod(verbose=True)