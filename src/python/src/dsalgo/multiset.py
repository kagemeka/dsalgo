from __future__ import annotations

import dsalgo.algebraic_structure
import dsalgo.fenwick_tree

# import typing

# from dsalgo.type import T


class FenwickTree:
    __max_value: int

    def __init__(self, max_value: int) -> None:
        """instance can contain values range of [0, max_value)."""
        self.__fw = dsalgo.fenwick_tree.FenwickTreeIntAdd([0] * max_value)

        self.__max_value = max_value

    @property
    def max_value(self) -> int:
        return self.__max_value

    def __len__(self) -> int:
        return self.__fw[self.max_value]

    def __contains__(self, x: int) -> bool:
        return self.count(x) >= 1

    def count(self, x: int) -> int:
        if x < 0 or self.max_value <= x:
            return 0
        return self.__fw.get_range(x, x + 1)

    def is_empty(self) -> bool:
        return len(self) == 0

    def __bool__(self) -> bool:
        return not self.is_empty()

    def insert(self, x: int) -> None:
        assert 0 <= x < self.max_value
        self.__fw[x] = 1

    def remove(self, x: int) -> None:
        if x not in self:
            raise KeyError(x)
        self.__fw[x] = -1

    def remove_all(self, x: int) -> None:
        assert 0 <= x < self.max_value
        self.__fw[x] = -self.count(x)

    def __getitem__(self, i: int) -> int | None:
        """Return i-th element."""
        if not 0 <= i < len(self):
            return None
        return self.__fw.max_right(lambda v: v < i + 1)

    def min(self) -> int | None:
        return None if len(self) == 0 else self[0]

    def max(self) -> int | None:
        return None if len(self) == 0 else self[len(self) - 1]

    def lower_bound(self, x: int) -> int:
        return self.__fw[x]

    def upper_bound(self, x: int) -> int:
        return self.__fw[x + 1]


class SegmentTree:
    ...


class RedBlackTree:
    ...


class AVLTree:
    ...


# import math
# import bisect


# class BucketMultiset(typing.Generic[T]):
#     BUCKET_RATIO = 50
#     REBUILD_RATIO = 170

#     def _build(self, a=None) -> None:
#         "Evenly divide `a` into buckets."
#         if a is None:
#             a = list(self)
#         size = self.size = len(a)
#         bucket_size = int(math.ceil(math.sqrt(size / self.BUCKET_RATIO)))
#         self.a = [
#             a[size * i // bucket_size : size * (i + 1) // bucket_size]
#             for i in range(bucket_size)
#         ]

#     def __init__(self, a: Iterable[T] = []) -> None:
#         """
#         Make a new SortedMultiset from iterable.
#         """
#         a = list(a)
#         if not all(a[i] <= a[i + 1] for i in range(len(a) - 1)):
#             a = sorted(a)
#         self._build(a)

#     def __iter__(self) -> Iterator[T]:
#         for i in self.a:
#             for j in i:
#                 yield j

#     def __reversed__(self) -> Iterator[T]:
#         for i in reversed(self.a):
#             for j in reversed(i):
#                 yield j

#     def __len__(self) -> int:
#         return self.size

#     def __repr__(self) -> str:
#         return "SortedMultiset" + str(self.a)

#     def __str__(self) -> str:
#         s = str(list(self))
#         return "{" + s[1 : len(s) - 1] + "}"

#     def _find_bucket(self, x: T) -> List[T]:
#         "Find the bucket which should contain x. self must not be empty."
#         for a in self.a:
#             if x <= a[-1]:
#                 return a
#         return a

#     def __contains__(self, x: T) -> bool:
#         if self.size == 0:
#             return False
#         a = self._find_bucket(x)
#         i = bisect_left(a, x)
#         return i != len(a) and a[i] == x

#     def count(self, x: T) -> int:
#         "Count the number of x."
#         return self.index_right(x) - self.index(x)

#     def add(self, x: T) -> None:
#         "Add an element. / O(√N)"
#         if self.size == 0:
#             self.a = [[x]]
#             self.size = 1
#             return
#         a = self._find_bucket(x)
#         insort(a, x)
#         self.size += 1
#         if len(a) > len(self.a) * self.REBUILD_RATIO:
#             self._build()

#     def discard(self, x: T) -> bool:
#         "Remove an element and return True if removed. / O(√N)"
#         if self.size == 0:
#             return False
#         a = self._find_bucket(x)
#         i = bisect_left(a, x)
#         if i == len(a) or a[i] != x:
#             return False
#         a.pop(i)
#         self.size -= 1
#         if len(a) == 0:
#             self._build()
#         return True

#     def lt(self, x: T) -> Union[T, None]:
#         "Find the largest element < x, or None if it doesn't exist."
#         for a in reversed(self.a):
#             if a[0] < x:
#                 return a[bisect_left(a, x) - 1]

#     def le(self, x: T) -> Union[T, None]:
#         "Find the largest element <= x, or None if it doesn't exist."
#         for a in reversed(self.a):
#             if a[0] <= x:
#                 return a[bisect_right(a, x) - 1]

#     def gt(self, x: T) -> Union[T, None]:
#         "Find the smallest element > x, or None if it doesn't exist."
#         for a in self.a:
#             if a[-1] > x:
#                 return a[bisect_right(a, x)]

#     def ge(self, x: T) -> Union[T, None]:
#         "Find the smallest element >= x, or None if it doesn't exist."
#         for a in self.a:
#             if a[-1] >= x:
#                 return a[bisect_left(a, x)]

#     def __getitem__(self, x: int) -> T:
#         "Return the x-th element, or IndexError if it doesn't exist."
#         if x < 0:
#             x += self.size
#         if x < 0:
#             raise IndexError
#         for a in self.a:
#             if x < len(a):
#                 return a[x]
#             x -= len(a)
#         raise IndexError

#     def index(self, x: T) -> int:
#         "Count the number of elements < x."
#         ans = 0
#         for a in self.a:
#             if a[-1] >= x:
#                 return ans + bisect_left(a, x)
#             ans += len(a)
#         return ans

#     def index_right(self, x: T) -> int:
#         "Count the number of elements <= x."
#         ans = 0
#         for a in self.a:
#             if a[-1] > x:
#                 return ans + bisect_right(a, x)
#             ans += len(a)
#         return ans


if __name__ == "__main__":
    import doctest

    doctest.testmod()
