import typing

T = typing.TypeVar("T")


def unwrap(x: typing.Optional[T]) -> T:
    assert x is not None
    return x
