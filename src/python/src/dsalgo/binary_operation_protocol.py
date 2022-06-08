import typing

Lhs = typing.TypeVar("Lhs", contravariant=True)
Rhs = typing.TypeVar("Rhs", contravariant=True)
Codomain = typing.TypeVar("Codomain", covariant=True)


class BinaryOperation(typing.Protocol[Lhs, Rhs, Codomain]):
    @classmethod
    def map(cls, lhs: Lhs, rhs: Rhs) -> Codomain:
        ...
