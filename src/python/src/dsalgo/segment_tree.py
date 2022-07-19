from __future__ import annotations

import typing


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
