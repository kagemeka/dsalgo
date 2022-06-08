import unittest

import typing

T = typing.TypeVar("T")


class Magma(typing.Protocol[T]):
    @classmethod
    def operate(cls, lhs: T, rhs: T) -> T:
        ...


# TODO:
class Tests(unittest.TestCase):
    def test(self) -> None:
        ...


if __name__ == "__main__":
    import doctest

    unittest.main()

    doctest.testmod(verbose=True)
