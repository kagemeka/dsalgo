from __future__ import annotations

import typing

from python.src.dsalgo.algebraic_structure import Monoid

T = typing.TypeVar("T")
S = typing.TypeVar("S")
F = typing.TypeVar("F")


class Segtree(typing.Generic[S]):
    _g: Monoid[S]
    _d: list[S]  # data
    _sz: int  # size

    def __init__(self, g: Monoid[S], a: list[S]) -> None:
        sz = len(a)
        n = 1 << (sz - 1).bit_length()
        d = [g.e() for _ in range(n << 1)]
        d[n : n + sz] = a
        self._g, self._sz, self._d = g, sz, d
        for i in range(n - 1, 0, -1):
            self._update(i)

    @property
    def size(self) -> int:
        return self._sz

    def _n(self) -> int:
        return len(self._d) >> 1

    def _update(self, i: int) -> None:
        self._d[i] = self._g.op(self._d[i << 1], self._d[i << 1 | 1])

    def __setitem__(self, i: int, v: S) -> None:
        assert 0 <= i < self.size
        i += self._n()
        self._d[i] = v
        while i > 1:
            i >>= 1
            self._update(i)

    def __getitem__(self, i: int) -> S:
        assert 0 <= i < self.size
        return self._d[i + self._n()]

    def reduce(self, l: int, r: int) -> S:
        assert 0 <= l <= r <= self.size
        n = self._n()
        l += n
        r += n
        vl = self._g.e()
        vr = self._g.e()
        while l < r:
            if l & 1:
                vl = self._g.op(vl, self._d[l])
                l += 1
            if r & 1:
                r -= 1
                vr = self._g.op(self._d[r], vr)
            l >>= 1
            r >>= 1
        return self._g.op(vl, vr)

    def max_right(self, is_ok: typing.Callable[[S], bool], l: int) -> int:
        assert 0 <= l <= self.size
        if l == self.size:
            return self.size
        n = len(self._data) >> 1
        v, i = self._g.identity(), n + left
        while True:
            i //= i & -i
            if not is_ok(self._g.operation(v, self._data[i])):
                break
            v = self._g.operation(v, self._data[i])
            i += 1
            if i & -i == i:
                return self.size
        while i < n:
            i <<= 1
            if not is_ok(self._g.operation(v, self._data[i])):
                continue
            v = self._g.operation(v, self._data[i])
            i += 1
        return i - n

    def min_left(self, is_ok: typing.Callable[[S], bool], right: int) -> int:
        if not 0 <= right <= self.size:
            raise IndexError
        if right == 0:
            return 0
        n = len(self._data) >> 1
        v, i = self._g.identity(), n + right
        while True:
            i //= i & -i
            if not is_ok(self._g.operation(self._data[i - 1], v)):
                break
            i -= 1
            v = self._g.operation(self._data[i], v)
            if i & -i == i:
                return 0
        while i < n:
            i <<= 1
            if not is_ok(self._g.operation(self._data[i - 1], v)):
                continue
            i -= 1
            v = self._g.operation(self._data[i], v)
        return i - n


class SegmentTreeDFS(SegmentTree[S]):
    def get(self, left: int, right: int) -> S:
        if not 0 <= left <= right <= self.size:
            raise IndexError
        return self.__get(left, right, 0, len(self._data) >> 1, 1)

    def __get(
        self,
        left: int,
        right: int,
        current_left: int,
        current_right: int,
        node_index: int,
    ) -> S:
        if current_right <= left or right <= current_left:
            return self._g.identity()
        if left <= current_left and current_right <= right:
            return self._data[node_index]
        center = (current_left + current_right) >> 1
        return self._g.operation(
            self.__get(left, right, current_left, center, node_index << 1),
            self.__get(
                left, right, center, current_right, node_index << 1 | 1
            ),
        )


class SegmentTreeDual:
    ...


class SegmentTreeBeats:
    ...


class LazySegmentTree(typing.Generic[S, F]):
    _g_s: dsalgo.algebraic_structure.Monoid[S]
    _g_f: dsalgo.algebraic_structure.Monoid[F]
    _data: list[S]
    _lazy: list[F]
    _size: int

    def __init__(
        self,
        monoid_s: dsalgo.algebraic_structure.Monoid[S],
        monoid_f: dsalgo.algebraic_structure.Monoid[F],
        map_: typing.Callable[[F, S], S],
        arr: list[S],
    ) -> None:
        size = len(arr)
        n = 1 << (size - 1).bit_length()
        data = [monoid_s.identity() for _ in range(n << 1)]
        data[n : n + size] = arr.copy()
        lazy = [monoid_f.identity() for _ in range(n)]
        self._g_s, self._g_f, self.__map = monoid_s, monoid_f, map_
        self._size, self._data, self._lazy = size, data, lazy
        for i in range(n - 1, 0, -1):
            self._merge(i)

    def __len__(self) -> int:
        return len(self._data)

    @property
    def size(self) -> int:
        return self._size

    def _update(self, i: int) -> None:
        self._data[i] = self._g_s.operation(
            self._data[i << 1],
            self._data[i << 1 | 1],
        )

    def _apply(self, i: int, f: F) -> None:
        self._data[i] = self.__map(f, self._data[i])
        if i < len(self._lazy):
            self._lazy[i] = self._g_f.operation(f, self._lazy[i])

    def _propagate(self, i: int) -> None:
        self._apply(i << 1, self._lazy[i])
        self._apply(i << 1 | 1, self._lazy[i])
        self._lazy[i] = self._g_f.identity()

    def set(self, left: int, right: int, f: F) -> None:
        assert 0 <= left <= right <= self.size
        n = len(self) >> 1
        left += n
        right += n
        height = n.bit_length()

        for i in range(height, 0, -1):
            if (left >> i) << i != left:
                self._propagate(left >> i)
            if (right >> i) << i != right:
                self._propagate((right - 1) >> i)

        l0, r0 = left, right  # backup
        while left < right:
            if left & 1:
                self._apply(left, f)
                left += 1
            if right & 1:
                right -= 1
                self._apply(right, f)
            left, right = left >> 1, right >> 1

        left, right = l0, r0
        for i in range(1, height + 1):
            if (left >> i) << i != left:
                self._merge(left >> i)
            if (right >> i) << i != right:
                self._merge((right - 1) >> i)

    def get(self, left: int, right: int) -> S:
        assert 0 <= left <= right <= self.size
        n = len(self) >> 1
        left, right = n + left, n + right
        height = n.bit_length()

        for i in range(height, 0, -1):
            if (left >> i) << i != left:
                self._propagate(left >> i)
            if (right >> i) << i != right:
                self._propagate((right - 1) >> i)

        vl, vr = self._g_s.identity(), self._g_s.identity()
        while left < right:
            if left & 1:
                vl = self._g_s.operation(vl, self._data[left])
                left += 1
            if right & 1:
                right -= 1
                vr = self._g_s.operation(self._data[right], vr)
            left, right = left >> 1, right >> 1
        return self._g_s.operation(vl, vr)

    def update(self, i: int, x: S) -> None:
        assert 0 <= i < self.size
        n = len(self) >> 1
        i += n
        height = n.bit_length()
        for j in range(height, 0, -1):
            self._propagate(i >> j)
        self._data[i] = x
        for j in range(1, height + 1):
            self._merge(i >> j)


class LazySegmentTreeDFS(LazySegmentTree[S, F]):
    def set(self, left: int, right: int, f: F) -> None:
        assert 0 <= left <= right <= self.size
        self.__set(left, right, f, 0, len(self) >> 1, 1)

    def __set(
        self,
        left: int,
        right: int,
        f: F,
        current_left: int,
        current_right: int,
        i: int,
    ) -> None:
        n = len(self) >> 1
        if i < n:
            self._propagate(i)
        if current_right <= left or right <= current_left:
            return
        if left <= current_left and current_right <= right:
            self._apply(i, f)
            if i < n:
                self._propagate(i)
            return
        center = (current_left + current_right) >> 1
        self.__set(left, right, f, current_left, center, i << 1)
        self.__set(left, right, f, center, current_right, i << 1 | 1)
        self._merge(i)

    def get(self, left: int, right: int) -> S:
        assert 0 <= left <= right <= self.size
        return self.__get(left, right, 0, len(self) >> 1, 1)

    def __get(
        self,
        left: int,
        right: int,
        current_left: int,
        current_right: int,
        i: int,
    ) -> S:
        n = len(self) >> 1
        if i < n:
            self._propagate(i)
        if current_right <= left or right <= current_left:
            return self._g_s.identity()
        if left <= current_left and current_right <= right:
            if i < n:
                self._propagate(i)
            return self._data[i]
        center = (current_left + current_right) >> 1
        vl = self.__get(left, right, current_left, center, i << 1)
        vr = self.__get(left, right, center, current_right, i << 1 | 1)
        self._merge(i)
        return self._g_s.operation(vl, vr)

    def update(self, i: int, x: S) -> None:
        assert 0 <= i < self.size
        n = len(self) >> 1
        self.get(i, i + 1)
        self._data[n + i] = x
        self.get(i, i + 1)
