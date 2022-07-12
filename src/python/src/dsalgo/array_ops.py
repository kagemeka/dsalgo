# /mypy: ignore-errors

from __future__ import annotations

import bisect
import typing
import unittest

T = typing.TypeVar("T")



def bincnt(a: typing.Sequence[int]) -> typing.List[int]:
    c = [0] * (max(a) + 1)
    for x in a:
        c[x] += 1
    return c


def inversion(a: typing.Sequence[T]) -> int:
    # inversion number of comparable list
    ...
    # TODO:
    # draft: use multiset with binary search functionality


# TODO: deprecate after implmenting general one.
def inversion_int(a: typing.List[int]) -> int:
    from dsalgo.fenwick import FwIntAdd

    a = Compress.once(a)
    fw = FwIntAdd([0] * len(a))
    c = 0
    for i, x in enumerate(a):
        c += i - fw[x]
        fw[x] = 1
    return c

def accumulate(
    identity_element: T,
) -> typing.Callable[
    [typing.Callable[[T, T], T]],
    typing.Callable[[typing.Iterable[T]], T],
]:
    def decorate(
        op: typing.Callable[[T, T], T],
    ) -> typing.Callable[[typing.Iterable[T]], T]:
        import functools

        def wrapped(arr: typing.Iterable[T]) -> T:
            return functools.reduce(op, arr, identity_element)

        return wrapped

    return decorate


# @accumulate(0)
# def xor(a: int, b: int) -> int:
#     return a ^ b


if __name__ == "__main__":
    unittest.main()
    import doctest

    doctest.testmod(verbose=True)
