import typing

from dsalgo.monoid_protocol import Monoid

T = typing.TypeVar("T", covariant=True)


class CommutativeMonoind(Monoid[T], typing.Protocol[T]):
    """
    Binary operation is commutative.
    """

    ...
