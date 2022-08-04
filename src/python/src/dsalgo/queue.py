from __future__ import annotations

import typing

import dsalgo.singly_linked_list
from dsalgo.type import T


class SinglyLinkedList(typing.Generic[T]):
    __first: dsalgo.singly_linked_list.Node[T] | None
    __last: dsalgo.singly_linked_list.Node[T] | None
    __size: int

    def __init__(self) -> None:
        self.__first = None
        self.__last = None
        self.__size = 0

    def __bool__(self) -> bool:
        return not self.is_empty()

    def __len__(self) -> int:
        return self.__size

    def is_empty(self) -> bool:
        return self.__first is None

    def append(self, v: T) -> None:
        self.__last = dsalgo.singly_linked_list.add_last(
            self.__last, dsalgo.singly_linked_list.Node(value=v)
        )
        if self.__first is None:
            self.__first = self.__last
        self.__size += 1

    def pop(self) -> T:
        if self.__first is None:
            raise Exception("cannot pop from empty queue.")
        popped, self.__first = dsalgo.singly_linked_list.pop_front(
            self.__first
        )
        if self.__first is None:
            self.__last = None
        self.__size -= 1
        return popped.value



if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
