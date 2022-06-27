# mypy: ignore-errors


import typing
import unittest

from dsalgo.z_algorithm import z_algorithm

T = typing.TypeVar("T")
A = typing.Sequence[T]


def z_algorithm_findall(a: A, pattern: A) -> typing.List[int]:
    n = len(pattern)
    return [i for i, d in enumerate(z_algorithm(pattern + a)[n:]) if d >= n]


class Tests(unittest.TestCase):
    def test(self) -> None:
        s = "ababababc"
        pat = "aba"
        assert z_algorithm_findall(s, pat) == [0, 2, 4]


if __name__ == "__main__":
    import doctest

    unittest.main()

    doctest.testmod(verbose=True)
