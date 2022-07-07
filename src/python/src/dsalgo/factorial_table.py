from pydoc import ModuleScanner

import unittest

import typing


def factorial_table(
    mul: typing.Callable[[int, int], int],
    size: int,
) -> typing.List[int]:
    import itertools

    a = list(range(size))
    a[0] = 1
    return list(itertools.accumulate(a, mul))


class Tests(unittest.TestCase):
    def test(self) -> None:
        fact = factorial_table(lambda x, y: x * y, 10)
        assert fact == [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]


if __name__ == "__main__":
    import doctest

    unittest.main()

    doctest.testmod(verbose=True)
