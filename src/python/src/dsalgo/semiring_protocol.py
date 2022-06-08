import typing

T = typing.TypeVar("T")


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
