"""
inspired by Rust's Result<T, E> type.
in python, Option[T] = Union[T, None] =: T | None
while Option<T> in Rust is enum {Some(T), None}

and because Result<T, E> is enum {Ok(T), Err(E)},
Result[T, E] = Union[T, Err[E]] is fine in Python.

we don't use any Exceptions
which are starndard error handling feature in Python.
instead, Result[T, E] is defactostandard in this package.
"""

import dataclasses
import typing
import unittest

from dsalgo._option import unwrap

T = typing.TypeVar("T", contravariant=True)
E = typing.TypeVar("E", contravariant=True)
U = typing.TypeVar("U", covariant=True)


@typing.final
@dataclasses.dataclass(frozen=True)
class Err(typing.Generic[E]):
    value: E


Result = typing.Union[T, Err[E]]


def is_ok(res: Result[T, E]) -> bool:
    return not is_err(res)


def is_err(x: Result[T, E]) -> bool:
    return isinstance(x, Err)


def ok(res: Result[T, E]) -> T | None:
    return typing.cast(T, res) if is_ok(res) else None


def err(res: Result[T, E]) -> E | None:
    return typing.cast(Err[E], res).value if is_err(res) else None


def unwrap_ok(res: Result[U, E]) -> U:
    return unwrap(ok(res))


def unwrap_err(res: Result[T, U]) -> U:
    return unwrap(err(res))


class Tests(unittest.TestCase):
    def test(self) -> None:
        def generate_error() -> Result[int, str]:
            return Err("nothing")

        a = Err(1)
        assert not is_ok(a)
        assert ok(a) is None
        assert err(a) == 1
        assert is_err(generate_error())
        assert unwrap_err(generate_error()) == "nothing"


if __name__ == "__main__":
    import doctest

    unittest.main()

    doctest.testmod(verbose=True)
