import typing
import unittest

from dsalgo.semigroup_protocol import Semigroup

T = typing.TypeVar("T")


class Monoid(Semigroup[T], typing.Protocol[T]):
    @classmethod
    def identity(cls) -> T:
        ...


class Tests(unittest.TestCase):
    def test(self) -> None:
        def f(M: typing.Type[Monoid[T]], x: T) -> T:
            return M.operate(M.identity(), x)

        class IntAdd:
            @classmethod
            def identity(cls) -> int:
                return 0

            @classmethod
            def operate(cls, lhs: int, rhs: int) -> int:
                return lhs + rhs

        assert f(IntAdd, 1) == 1


if __name__ == "__main__":
    import doctest

    unittest.main()

    doctest.testmod(verbose=True)
