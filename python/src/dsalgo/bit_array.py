# mypy: ignore-errors

import typing

from dsalgo.popcount import popcount

Self = typing.TypeVar("Self")


class BitArray:
    N: int = 63
    _d: typing.List[int]

    def __init__(self, size: int) -> None:
        self._d = [0] * ((size + self.N - 1) // self.N)

    def __getitem__(self, i: int) -> int:
        return self._d[i // self.N] >> (i % self.N) & 1

    def __setitem__(self, i: int, value: int) -> None:
        if self[i] != value:
            self.flip(i)

    def flip(self, i: int) -> None:
        self._d[i // self.N] ^= 1 << i % self.N

    def __and__(self, rhs: Self) -> Self:
        res = BitArray(0)
        res._d = self._d.copy()
        for i in range(min(len(self._d), len(rhs._d))):
            res._d[i] &= rhs._d[i]
        return res

    def and_count(self, rhs: Self) -> int:
        s = 0
        for x, y in zip(self._d, rhs._d):
            s += popcount(x & y)
        return s

    def popcount(self) -> int:
        # sum() is slow with pypy.
        s = 0
        for x in self._d:
            s += popcount(x)
        return s
