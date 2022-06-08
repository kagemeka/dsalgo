import unittest
from dsalgo.magma_protocol import Magma
import typing

T = typing.TypeVar("T")


class Semigroup(Magma[T], typing.Protocol[T]):
    ...


class Tests(unittest.TestCase):
    def test(self) -> None:
        ...


if __name__ == "__main__":
    import doctest

    unittest.main()

    doctest.testmod(verbose=True)
