# TODO:
# abelian group fenwick tree, invert as method of normal fenwick tree.
# type assertion and cast of m with isinstance(), typing.cast()
# if failed, raise not implemented error

from __future__ import annotations

import typing

import dsalgo.abstract_structure
from dsalgo.type import S


class FenwickTree(typing.Generic[S]):
    """
    Example:
        >>> monoid = Monoid(op=lambda x, y: x + y, e=lambda: 0)
        >>> arr = [0, 1, 2, 3, 4]
        >>> fw = FenwickTree(monoid, arr)
        >>> fw[3]
        3
        >>> fw[2] = 2
        >>> fw[3]
        5
    """

    def __init__(
        self,
        monoid: dsalgo.abstract_structure.Monoid[S],
        arr: list[S],
    ) -> None:
        n = len(arr)
        data: list[S] = [monoid.identity() for _ in range(n + 1)]
        data[1:] = arr.copy()
        for i in range(1, n + 1):
            j = i + (i & -i)
            if j < n + 1:
                data[j] = monoid.operation(data[j], data[i])
        self.__monoid, self.__data = monoid, data

    def __len__(self) -> int:
        """Size of original array."""
        return len(self.__data) - 1

    def __setitem__(self, i: int, x: S) -> None:
        assert 0 <= i < len(self)
        i += 1
        while i < len(self) + 1:
            self.__data[i] = self.__monoid.operation(self.__data[i], x)
            i += i & -i

    def __getitem__(self, i: int) -> S:
        assert 0 <= i <= len(self)
        v = self.__monoid.identity()
        while i > 0:
            v = self.__monoid.operation(v, self.__data[i])
            i -= i & -i
        return v

    def max_right(self, is_ok: typing.Callable[[S], bool]) -> int:
        n = len(self) + 1
        length = 1
        while length << 1 < n:
            length <<= 1
        v, i = self.__monoid.identity(), 0
        while length:
            if i + length < n and is_ok(
                self.__monoid.operation(v, self.__data[i + length])
            ):
                i += length
                v = self.__monoid.operation(v, self.__data[i])
            length >>= 1
        return i


def build_fenwick_tree_with_size(
    monoid: dsalgo.abstract_structure.Monoid[S],
    size: int,
) -> FenwickTree[S]:
    return FenwickTree[S](monoid, [monoid.identity() for _ in range(size)])


class FenwickTreeAbelianGroup(FenwickTree[S]):
    def __init__(
        self,
        group: dsalgo.abstract_structure.Group[S],
        arr: list[S],
    ) -> None:
        super().__init__(group, arr)
        self.__group = group

    def get_range(self, left: int, right: int) -> S:
        return self.__group.operation(
            self.__group.invert(self[left]),
            self[right],
        )


def build_fenwick_tree_ablian_group_with_size(
    group: dsalgo.abstract_structure.Group[S],
    size: int,
) -> FenwickTreeAbelianGroup[S]:
    return FenwickTreeAbelianGroup[S](
        group,
        [group.identity() for _ in range(size)],
    )


class FenwickTreeIntAdd:
    def __init__(self, arr: list[int]) -> None:
        n = len(arr)
        data = [0] * (n + 1)
        data[1:] = arr.copy()
        for i in range(n):
            j = i + (i & -i)
            if j > n:
                continue
            data[j] += data[i]
        self.__data = data

    def __len__(self) -> int:
        return len(self.__data) - 1

    def __setitem__(self, i: int, x: int) -> None:
        assert 0 <= i < len(self)
        i += 1
        while i < len(self) + 1:
            self.__data[i] += x
            i += i & -i

    def __getitem__(self, i: int) -> int:
        assert 0 <= i <= len(self)
        v = 0
        while i > 0:
            v += self.__data[i]
            i -= i & -i
        return v

    def get_range(self, left: int, right: int) -> int:

        return self[right] - self[left]

    def max_right(self, is_ok: typing.Callable[[int], bool]) -> int:
        n = len(self) + 1
        length = 1
        while length << 1 < n:
            length <<= 1
        v, i = 0, 0
        while length:
            if i + length < n and is_ok(v + self.__data[i + length]):
                i += length
                v += self.__data[i]
            length >>= 1
        return i


class FenwickTreeIntMax:
    def __init__(self, arr: list[int]) -> None:
        n = len(arr)
        data = [0] * (n + 1)
        data[1:] = arr.copy()
        for i in range(n):
            j = i + (i & -i)
            if j > n:
                continue
            data[j] = max(data[j], data[i])
        self.__data = data

    def __len__(self) -> int:
        return len(self.__data) - 1

    def __setitem__(self, i: int, x: int) -> None:
        assert 0 <= i < len(self)
        i += 1
        while i < len(self) + 1:
            self.__data[i] = max(self.__data[i], x)
            i += i & -i

    def __getitem__(self, i: int) -> int:
        assert 0 <= i <= len(self)
        v = 0
        while i > 0:
            v = max(v, self.__data[i])
            i -= i & -i
        return v


class FenwickTree2D(typing.Generic[S]):
    def __init__(
        self,
        monoid: dsalgo.abstract_structure.Monoid[S],
        shape: tuple[int, int],
    ) -> None:
        self.__monoid = monoid
        height, width = shape
        self.__data = [
            [monoid.identity() for _ in range(width + 1)]
            for _ in range(height + 1)
        ]

    @property
    def shape(self) -> tuple[int, int]:
        return (len(self.__data) - 1, len(self.__data[0]) - 1)

    def set(self, i: int, j: int, x: S) -> None:
        n, m = self.shape
        assert 0 <= i < n and 0 <= j < m
        i += 1
        j0 = j + 1
        while i <= n:
            j = j0
            while j <= m:
                self.__data[i][j] = self.__monoid.operation(
                    self.__data[i][j],
                    x,
                )
                j += j & -j
            i += i & -i

    def get(self, i: int, j: int) -> S:
        n, m = self.shape
        assert 0 <= i <= n and 0 <= j <= m
        j0 = j
        v = self.__monoid.identity()
        while i > 0:
            j = j0
            while j > 0:
                v = self.__monoid.operation(v, self.__data[i][j])
                j -= j & -j
            i -= i & -i
        return v


class FenwickTreeIntAdd2D:
    def __init__(self, shape: tuple[int, int]) -> None:
        n, m = shape
        self.__data = [[0] * (m + 1) for _ in range(n + 1)]

    @property
    def shape(self) -> tuple[int, int]:
        return (len(self.__data) - 1, len(self.__data[0]) - 1)

    def set(self, i: int, j: int, x: int) -> None:
        n, m = self.shape
        assert 0 <= i < n and 0 <= j < m
        i += 1
        j0 = j + 1
        while i <= n:
            j = j0
            while j <= m:
                self.__data[i][j] += x
                j += j & -j
            i += i & -i

    def get(self, i: int, j: int) -> int:
        n, m = self.shape
        assert 0 <= i <= n and 0 <= j <= m
        j0 = j
        v = 0
        while i > 0:
            j = j0
            while j > 0:
                v += self.__data[i][j]
                j -= j & -j
            i -= i & -i
        return v

    def get_range(self, i0: int, j0: int, i1: int, j1: int) -> int:
        v = self.get(i1, j1)
        v -= self.get(i1, j0)
        v -= self.get(i0, j1)
        v += self.get(i0, j0)
        return v


class DualFenwickTree(typing.Generic[S]):
    """
    Examples:
        >>> a = [0, 1, 2, 3, 4]
        >>> g = Group[int](lambda x, y: x + y, lambda: 0, lambda x: -x)
        >>> fw = DualFenwickTree(g, a)
        >>> fw.set(1, 5, 2)
        >>> fw[3]
        5
        >>> fw[0]
        0
    """

    def __init__(
        self,
        group: dsalgo.abstract_structure.Group[S],
        arr: list[S],
    ) -> None:
        """
        group: Abelian Group.
        """
        n = len(arr)
        assert n > 0
        delta = [arr[0]]
        for i in range(n - 1):
            delta.append(group.operation(group.invert(arr[i]), arr[i + 1]))
        self.__fw = FenwickTree[S](group, delta)
        self.__group = group

    def set(self, left: int, right: int, x: S) -> None:
        n = len(self.__fw)
        assert 0 <= left < right <= n
        self.__fw[left] = x
        if right < n:
            self.__fw[right] = self.__group.invert(x)

    def __getitem__(self, i: int) -> S:
        assert 0 <= i < len(self.__fw)
        return self.__fw[i + 1]


class DualFenwickTreeIntAdd:
    def __init__(self, arr: list[int]) -> None:
        n = len(arr)
        assert n > 0
        delta = [arr[0]]
        for i in range(n - 1):
            delta.append(arr[i + 1] - arr[i])
        self.__fw = FenwickTreeIntAdd(delta)

    def set(self, left: int, right: int, x: int) -> None:
        n = len(self.__fw)
        assert 0 <= left < right <= n
        self.__fw[left] = x
        if right < n:
            self.__fw[right] = -x

    def __getitem__(self, i: int) -> int:
        assert 0 <= i < len(self.__fw)
        return self.__fw[i + 1]


class FwLazyIntAdd:
    """
    Examples:
        >>> a = [0, 1, 2, 3, 4]
        >>> fw = FenwickTreeAddSum(a)
        >>> fw.set(0, 3, 2)
        >>> fw.get(2, 5)
        11
    """

    def __init__(self, arr: list[int]) -> None:
        n = len(arr)
        self.__fw_0 = dsalgo.fenwick_tree.FenwickTreeIntAdd(arr)
        self.__fw_1 = dsalgo.fenwick_tree.FenwickTreeIntAdd([0] * n)

    def __len__(self) -> int:
        return len(self.__fw_0)

    def set(self, left: int, right: int, x: int) -> None:
        assert 0 <= left < right <= len(self)
        self.__fw_0[left] = -x * left
        self.__fw_1[left] = x
        if right < len(self):
            self.__fw_0[right] = x * right
            self.__fw_1[right] = -x

    def get(self, left: int, right: int) -> int:
        assert 0 <= left <= right <= len(self)
        fw0, fw1 = self.__fw_0, self.__fw_1
        return fw0[right] + fw1[right] * right - fw0[left] - fw1[left] * left

if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
