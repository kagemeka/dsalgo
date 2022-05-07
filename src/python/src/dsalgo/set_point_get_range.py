from __future__ import annotations

import typing

import dsalgo.abstract_structure
import dsalgo.fenwick_tree
import dsalgo.segment_tree
from dsalgo.type import S, T


class FenwickTree(typing.Generic[S]):
    def __init__(
        self,
        group: dsalgo.abstract_structure.Group[S],
        arr: list[S],
    ) -> None:
        self.__fw = dsalgo.fenwick_tree.FenwickTreeAbelianGroup(group, arr)

    def __setitem__(self, i: int, x: S) -> None:
        self.__fw[i] = x

    def get(self, left: int, right: int) -> S:
        return self.__fw.get_range(left, right)


class SegmentTree(typing.Generic[T]):
    def __init__(
        self,
        monoid: dsalgo.abstract_structure.Monoid[T],
        arr: list[T],
    ) -> None:
        self.__seg = dsalgo.segment_tree.SegmentTree(monoid, arr)
        self.__monoid = monoid

    def set_point(self, i: int, x: T) -> None:
        self.__seg[i] = x

    def operate_point(self, i: int, x: T) -> None:
        self.set_point(i, self.__monoid.operation(self.get_point(i), x))

    def get_point(self, i: int) -> T:
        return self.__seg[i]

    def get_range(self, left: int, right: int) -> T:
        return self.__seg.get(left, right)


class FenwickTreeAddSum:
    def __init__(self, arr: list[int]) -> None:
        self.__fw = dsalgo.fenwick_tree.FenwickTreeIntAdd(arr)

    def __setitem__(self, i: int, x: int) -> None:
        self.__fw[i] = x

    def get(self, left: int, right: int) -> int:
        return self.__fw[right] - self.__fw[left]
