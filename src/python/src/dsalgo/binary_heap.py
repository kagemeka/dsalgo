from __future__ import annotations

import typing

import dsalgo.order

T = typing.TypeVar("T", bound=dsalgo.order.Order)


class BinaryMinHeap(typing.Generic[T]):
    __data: list[T]

    def __init__(self) -> None:
        self.__data = []

    def __len__(self) -> int:
        return len(self.__data)

    def __repr__(self) -> str:
        return str(self.__data)

    def __iter__(self) -> typing.Iterator[T]:
        for x in self.__data:
            yield x

    def __bool__(self) -> bool:
        return bool(self.__data)

    def __swap(self, i: int, j: int) -> None:
        d = self.__data
        d[i], d[j] = d[j], d[i]

    def push(self, x: T) -> None:
        i = len(self)
        self.__data.append(x)
        while i > 0:
            j = (i - 1) >> 1
            if self.__data[i] >= self.__data[j]:
                break
            self.__swap(i, j)
            i = j

    def pop(self) -> T:
        self.__swap(0, -1)
        x = self.__data.pop()
        i = 0
        while True:
            j = (i << 1) + 1
            if j >= len(self):
                break
            j += j < len(self) - 1 and self.__data[j + 1] < self.__data[j]
            if self.__data[i] <= self.__data[j]:
                break
            self.__swap(i, j)
            i = j
        return x
