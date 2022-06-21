# algebraic structure protocol

import typing
import unittest

T = typing.TypeVar("T")


class Magma(typing.Protocol[T]):
    @classmethod
    def operate(cls, lhs: T, rhs: T) -> T:
        ...


class Semigroup(Magma[T], typing.Protocol[T]):
    ...


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


class Group(Monoid[T], typing.Protocol[T]):
    @classmethod
    def invert(cls, element: T) -> T:
        ...


class AbelianGroup(Group[T], typing.Protocol[T]):
    """
    Binary operation is implicit commutative.
    """

    ...


class Semiring(typing.Protocol[T]):
    @classmethod
    def add(cls, lhs: T, rhs: T) -> T:
        ...

    @classmethod
    def mul(cls, lhs: T, rhs: T) -> T:
        ...

    @classmethod
    def zero(cls) -> T:
        ...

    @classmethod
    def one(cls) -> T:
        ...


class Ring(Semiring[T], typing.Protocol[T]):
    @classmethod
    def add_inv(cls, element: T) -> T:
        ...
