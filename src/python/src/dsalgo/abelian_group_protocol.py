import typing

from dsalgo.group_protocol import Group

T = typing.TypeVar("T")


class AbelianGroup(Group[T], typing.Protocol[T]):
    """
    Binary operation is implicit commutative.
    """

    ...
