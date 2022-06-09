import typing

from dsalgo.semiring_protocol import Semiring

T = typing.TypeVar("T")


class Ring(Semiring[T], typing.Protocol[T]):
    @classmethod
    def add_inv(cls, element: T) -> T:
        ...
