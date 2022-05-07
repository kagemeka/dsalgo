from __future__ import annotations

import typing

import dsalgo.doubly_linked_list
from dsalgo.type import T


class CircularBuffer(typing.Generic[T]):
    __data: list[T | None]
    __left: int
    __right: int
    __size: int

    def __init__(self, buffer_size: int) -> None:
        assert buffer_size >= 1
        self.__data = [None] * buffer_size
        self.__left = self.__right = 0  # data is stored in [left, right).
        self.__size = 0

    def __len__(self) -> int:
        return self.__size

    @property
    def buffer_size(self) -> int:
        return len(self.__data)

    def __bool__(self) -> bool:
        return not self.is_empty()

    def is_empty(self) -> bool:
        return len(self) == 0

    def is_full(self) -> bool:
        return len(self) == self.buffer_size

    def append_right(self, v: T) -> None:
        if self.is_full():
            raise Exception("buffer is already full")
        assert self.__data[self.__right] is None
        self.__data[self.__right] = v
        self.__size += 1
        self.__right += 1
        if self.__right == self.buffer_size:
            self.__right = 0

    def append_left(self, v: T) -> None:
        if self.is_full():
            raise Exception("buffer is already full")
        if self.__left == 0:
            self.__left = self.buffer_size
        self.__left -= 1
        assert self.__data[self.__left] is None
        self.__data[self.__left] = v
        self.__size += 1

    def pop_right(self) -> T:
        if self.is_empty():
            raise Exception("cannot pop from empty deque.")
        if self.__right == 0:
            self.__right = self.buffer_size
        self.__right -= 1
        v, self.__data[self.__right] = self.__data[self.__right], None
        self.__size -= 1
        assert v is not None
        return v

    def pop_left(self) -> T:
        if self.is_empty():
            raise Exception("cannot pop from empty deque.")
        v, self.__data[self.__left] = self.__data[self.__left], None
        self.__left += 1
        if self.__left == self.buffer_size:
            self.__left = 0
        self.__size -= 1
        assert v is not None
        return v


class MiddleIndexed:
    ...


class DoublyLinkedList(typing.Generic[T]):

    __first: dsalgo.doubly_linked_list.Node[T] | None
    __last: dsalgo.doubly_linked_list.Node[T] | None
    __size: int

    def __init__(self) -> None:
        self.__first = None
        self.__last = None
        self.__size = 0

    def __len__(self) -> int:
        return self.__size

    def __bool__(self) -> bool:
        return self.__first is not None

    def append_right(self, v: T) -> None:
        self.__last = dsalgo.doubly_linked_list.add_right(
            self.__last,
            dsalgo.doubly_linked_list.Node(value=v),
        )
        if self.__first is None:
            self.__first = self.__last
        self.__size += 1

    def append_left(self, v: T) -> None:
        self.__first = dsalgo.doubly_linked_list.add_left(
            self.__first,
            dsalgo.doubly_linked_list.Node(value=v),
        )
        if self.__last is None:
            self.__last = self.__first
        self.__size += 1

    def pop_right(self) -> T:
        if self.__last is None:
            raise Exception("cannot pop from empty deque.")
        popped, self.__last = dsalgo.doubly_linked_list.pop_right(self.__last)
        if self.__last is None:
            self.__first = None
        self.__size -= 1
        return popped.value

    def pop_left(self) -> T:
        if self.__first is None:
            raise Exception("cannot pop from empty deque.")
        popped, self.__first = dsalgo.doubly_linked_list.pop_left(self.__first)
        if self.__first is None:
            self.__last = None
        self.__size -= 1
        return popped.value


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
