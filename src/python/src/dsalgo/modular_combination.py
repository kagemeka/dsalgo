from dsalgo.combination import combination
import typing

import unittest


def modular_combination(p: int, size: int) -> typing.Callable[[int, int], int]:
    return combination(
        lambda a, b: a * b % p,
        lambda a: pow(a, p - 2, p),
        size,
    )


class Tests(unittest.TestCase):
    def test(self) -> None:
        mod = 1_000_000_007
        f = modular_combination(mod, 100)
        assert f(10, 2) == 45


if __name__ == "__main__":
    import doctest

    unittest.main()

    doctest.testmod(verbose=True)
