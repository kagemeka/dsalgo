import collections
import heapq
import typing
import unittest

from dsalgo._option import unwrap


class MinMaxPriorityQueueInt:
    __min_q: typing.List[int]
    __max_q: typing.List[int]
    __cnt: collections.Counter[int]
    # __cnt: collections.Counter # for old python version
    __size: int

    def __init__(self) -> None:
        self.__cnt = collections.Counter()
        self.__size = 0
        self.__min_q = []
        self.__max_q = []

    def insert(self, x: int, count: int = 1) -> None:
        assert count > 0
        if self.__cnt[x] == 0:  # constant time optimization
            heapq.heappush(self.__min_q, x)
            heapq.heappush(self.__max_q, -x)
        self.__cnt[x] += count
        self.__size += count

    def count(self, x: int) -> int:
        return self.__cnt[x]

    def __contains__(self, x: int) -> bool:
        return self.count(x) != 0

    def remove(self, x: int, count: int = 1) -> None:
        assert self.count(x) >= count > 0
        self.__cnt[x] -= count
        self.__size -= count

    @property
    def size(self) -> int:
        return self.__size

    def __lazy_discard_false_min(self) -> None:
        while self.__min_q and self.__cnt[self.__min_q[0]] == 0:
            heapq.heappop(self.__min_q)

    def __lazy_discard_false_max(self) -> None:
        while self.__max_q and self.__cnt[-self.__max_q[0]] == 0:
            heapq.heappop(self.__max_q)

    def min(self) -> typing.Optional[int]:
        self.__lazy_discard_false_min()
        return None if not self.size else self.__min_q[0]

    def pop_min(self) -> int:
        mn = unwrap(self.min())
        assert self.__cnt[mn] > 0
        self.__cnt[mn] -= 1
        self.__size -= 1
        if self.__cnt[mn] == 0:
            heapq.heappop(self.__min_q)
        return mn

    def max(self) -> typing.Optional[int]:
        self.__lazy_discard_false_max()
        return None if not self.size else -self.__max_q[0]

    def pop_max(self) -> int:
        mx = unwrap(self.max())
        assert self.__cnt[mx] > 0
        self.__cnt[mx] -= 1
        self.__size -= 1
        if self.__cnt[mx] == 0:
            heapq.heappop(self.__max_q)
        return mx


# TODO:
class Test(unittest.TestCase):
    def test(self) -> None:
        ...


if __name__ == "__main__":
    unittest.main()
