# /mypy: ignore-errors

from __future__ import annotations

import typing
import unittest

import bisect

T = typing.TypeVar("T")


class Compress(typing.Generic[T]):
    _v: typing.List[int]  # unique values

    def __init__(self, a: typing.Iterable[T]) -> None:
        self._v = sorted(set(a))

    def __call__(self, v: T) -> int:
        i = bisect.bisect_left(self._v, v)
        assert self._v[i] == v
        return i

    def inv(self, i: int) -> T:
        # retrieve
        return self._v[i]

    @staticmethod
    def once(a: typing.Iterable[T]) -> typing.List[int]:
        f = Compress(a)
        return [f(v) for v in a]


class TestCompress(unittest.TestCase):
    def test(self) -> None:
        a = [3, 10, -1, 5]
        f = Compress(a)
        res = [f(x) for x in a]
        assert res == [1, 3, 0, 2]
        rev = [f.inv(x) for x in res]
        assert rev == [3, 10, -1, 5]
        assert Compress.once(a) == res


def argmax(a: typing.Sequence[T]) -> int:
    # comparable list
    i, mx = 0, a[0]
    for j, x in enumerate(a):
        if x > mx:
            i, mx = j, x
    return i


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


def flatnonzero(arr: typing.List[bool]) -> typing.List[int]:
    return [i for i, x in enumerate(arr) if x]


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
