import typing
from dsalgo.monoid_protocol import Monoid


T = typing.TypeVar("T")


class Group(Monoid[T], typing.Protocol[T]):
    @classmethod
    def invert(cls, element: T) -> T:
        ...
