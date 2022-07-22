import math
import typing
import unittest


def gcd_reduce(iter: typing.Iterable[int]) -> int:
    import functools

    return functools.reduce(math.gcd, iter, 0)


class Tests(unittest.TestCase):
    def test(self) -> None:
        assert gcd_reduce([]) == 0
        assert gcd_reduce([-1, 2]) == 1
        assert gcd_reduce([15, 35, 21]) == 1


if __name__ == "__main__":
    import doctest

    unittest.main()

    doctest.testmod(verbose=True)
