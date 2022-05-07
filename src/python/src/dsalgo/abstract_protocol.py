"""
- algebra
- abstract data structure
"""

from __future__ import annotations

import typing

T = typing.TypeVar("T")


class Magma(typing.Protocol[T]):
    def op(self: T, rhs: T) -> T:
        ...


class Semigroup(Magma[T], typing.Protocol[T]):
    """Semigroup.

    It's binary operation needed to be associative
    in addition to being Magma itself.

    """

    ...


class Monoid(Semigroup[T], typing.Protocol[T]):
    @classmethod
    def identity(cls: T) -> T:
        ...


class Group(Monoid[T], typing.Protocol[T]):
    """Group

    Commutative Group is also callled Abelian-Group.

    """

    def invert(self: T) -> T:
        ...


class Semiring(typing.Protocol[T]):
    def __add__(self: T, rhs: T) -> T:
        ...

    def __mul__(self: T, rhs: T) -> T:
        ...

    @classmethod
    def add_e(cls) -> T:
        ...

    @classmethod
    def mul_e(cls) -> T:
        ...


class Ring(Semiring[T], typing.Protocol[T]):
    def add_invert(self: T) -> T:
        ...


"""
Examples
class MyInt(Monoid):
    def __init__(self, value: int) -> None:
        self.__value = value

    @property
    def value(self) -> int:
        return self.__value

    def op(self: MyInt, rhs: MyInt) -> MyInt:
        return MyInt(self.__value + rhs.value)

    @classmethod
    def identity(cls) -> MyInt:
        return MyInt(0)


m = MyInt(0)

"""
