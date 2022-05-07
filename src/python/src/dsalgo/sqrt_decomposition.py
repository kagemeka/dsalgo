from __future__ import annotations

import typing

from dsalgo.algebra.abstract.abstract_structure import Monoid
from dsalgo.number_theory.floor_sqrt import floor_sqrt

S = typing.TypeVar("S")


class SqrtDecomposition(typing.Generic[S]):
    def __init__(self, monoid: Monoid[S], arr: list[S]) -> None:
        n = len(arr)
        sqrt = floor_sqrt(n)
        num_buckets = (n + sqrt - 1) // sqrt
        buckets = [monoid.e() for _ in range(num_buckets)]
        data_size = sqrt * num_buckets
        data = [monoid.e() for _ in range(data_size)]
        data[:n] = arr.copy()
        for i in range(num_buckets):
            for j in range(sqrt * i, sqrt * (i + 1)):
                buckets[i] = monoid.op(buckets[i], data[j])
        self.__data = data
        self.__buckets = buckets
        self.__sqrt = sqrt
        self.__original_size = n
        self.__monoid = monoid

    def __len__(self) -> int:
        return self.__original_size

    def __setitem__(self, i: int, x: S) -> None:
        assert 0 <= i < len(self)
        self.__data[i] = x
        idx = i // self.__sqrt
        self.__buckets[idx] = self.__monoid.e()
        for j in range(self.__sqrt * idx, self.__sqrt * (idx + 1)):
            self.__buckets[idx] = self.__monoid.op(
                self.__buckets[idx],
                self.__data[j],
            )

    def __getitem__(self, i: int) -> S:
        assert 0 <= i < len(self)
        return self.__data[i]

    def get(self, left: int, right: int) -> S:
        assert 0 <= left <= right <= len(self)
        v = self.__monoid.e()
        for i in range(len(self.__buckets)):
            if left >= self.__sqrt * (i + 1):
                continue
            if right <= self.__sqrt * i:
                break
            if left <= self.__sqrt * i and self.__sqrt * (i + 1) <= right:
                v = self.__monoid.op(v, self.__buckets[i])
                continue
            for j in range(self.__sqrt * i, self.__sqrt * (i + 1)):
                if j < left:
                    continue
                if j >= right:
                    break
                v = self.__monoid.op(v, self.__data[j])
        return v


# a = list(range(10))
# m = Monoid[int](op=lambda x, y: x + y, e=lambda: 0)

# sd = SqrtDecomposition[int](m, a)
# print(sd.get(1, 10))
