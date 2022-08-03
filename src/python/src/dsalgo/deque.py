from __future__ import annotations

import typing

import dsalgo.doubly_linked_list
from dsalgo.type import T


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
