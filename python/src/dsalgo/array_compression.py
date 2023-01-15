from __future__ import annotations

import bisect
import typing
import unittest

T = typing.TypeVar("T")


class ArrayCompression(typing.Generic[T]):
    _v: typing.List[T]  # unique values

    def __init__(self, a: typing.Iterable[T]) -> None:
        self._v = sorted(set(a))

    def __call__(self, v: T) -> int:
        i = bisect.bisect_left(self._v, v)
        assert self._v[i] == v
        return i

    def __getitem__(self, i: int) -> T:
        return self._v[i]

    @staticmethod
    def once(a: typing.Iterable[T]) -> typing.List[int]:
        f = ArrayCompression(a)
        return [f(v) for v in a]


class TestCompress(unittest.TestCase):
    def test(self) -> None:
        a = [3, 10, -1, 5]
        f = ArrayCompression(a)
        res = [f(x) for x in a]
        assert res == [1, 3, 0, 2]
        rev = [f[x] for x in res]
        assert rev == [3, 10, -1, 5]
        assert ArrayCompression.once(a) == res


if __name__ == "__main__":
    import doctest

    unittest.main()

    doctest.testmod(verbose=True)
