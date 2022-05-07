from __future__ import annotations


def _left_pivot(pivot: int) -> int:
    return pivot - (pivot & -pivot) // 2


def _right_pivot(pivot: int) -> int:
    return pivot + (pivot & -pivot) // 2


class PivotTreeArray:
    __data: list[int | None]
    __size: list[int]
    __max_height: int

    def __init__(self, max_height: int) -> None:
        assert max_height >= 1
        n = 1 << max_height
        self.__data = [None] * n
        self.__max_height = max_height
        self.__size = [0] * n

    @property
    def __root_pivot(self) -> int:
        return 1 << self.__max_height - 1

    @property
    def max_size(self) -> int:
        return (1 << self.__max_height) - 1

    def __len__(self) -> int:
        return self.__size[self.__root_pivot]

    def __update(self, pivot: int) -> None:
        if self.__data[pivot] is None:
            self.__size[pivot] = 0
            return
        left_size = self.__size[_left_pivot(pivot)]
        right_size = self.__size[_right_pivot(pivot)]
        self.__size[pivot] = left_size + right_size + 1

    def insert(self, key: int) -> None:
        assert 0 <= key < self.max_size
        self.__insert(self.__root_pivot, key + 1)

    def __insert(self, pivot: int, key: int) -> None:
        root_key = self.__data[pivot]
        if root_key is None:
            self.__data[pivot] = key
            self.__size[pivot] = 1
            return
        if root_key == key:
            return
        lsb = pivot & -pivot
        if not pivot - (lsb - 1) <= key <= pivot + (lsb - 1):
            raise Exception("the given key is out of bounds")
        lo_key, hi_key = (key, root_key) if key < root_key else (root_key, key)
        if lo_key < pivot:
            self.__data[pivot] = hi_key
            self.__insert(pivot - lsb // 2, lo_key)
        else:
            self.__data[pivot] = lo_key
            self.__insert(pivot + lsb // 2, hi_key)
        self.__update(pivot)

    def __contains__(self, key: int) -> bool:
        assert 0 <= key < self.max_size
        return self.__find(self.__root_pivot, key + 1)

    def __find(self, pivot: int, key: int) -> bool:
        root_key = self.__data[pivot]
        if root_key is None or pivot & 1:
            return False
        if root_key == key:
            return True
        elif key < root_key:
            return self.__find(_left_pivot(pivot), key)
        else:
            return self.__find(_right_pivot(pivot), key)

    def remove(self, key: int) -> None:
        assert 0 <= key < self.max_size
        self.__remove(self.__root_pivot, key + 1)

    def __get_min(self, pivot: int) -> int:
        left_pivot = _left_pivot(pivot)
        root_key = self.__data[pivot]
        assert root_key is not None
        if pivot & 1 or self.__data[left_pivot] is None:
            return root_key
        return self.__get_min(left_pivot)

    def __get_max(self, pivot: int) -> int:
        right_pivot = _right_pivot(pivot)
        root_key = self.__data[pivot]
        assert root_key is not None
        if pivot & 1 or self.__data[right_pivot] is None:
            return root_key
        return self.__get_min(right_pivot)

    def __remove(self, pivot: int, key: int) -> int | None:
        root_key = self.__data[pivot]
        if root_key is None:
            return None
        left_pivot, right_pivot = _left_pivot(pivot), _right_pivot(pivot)
        if key < root_key:
            self.__remove(left_pivot, key)
        elif key > root_key:
            self.__remove(right_pivot, key)
        else:
            left_key = self.__data[left_pivot]
            right_key = self.__data[right_pivot]
            if pivot & 1 or left_key is None and right_key is None:
                self.__data[pivot] = None
            elif right_key is not None:
                root_key = self.__get_min(right_pivot)
                self.__data[pivot] = root_key
                self.__remove(right_pivot, root_key)
            elif left_key is not None:
                root_key = self.__get_max(left_pivot)
                self.__data[pivot] = root_key
                self.__remove(left_pivot, root_key)
        self.__update(pivot)
        return self.__data[pivot]

    def __getitem__(self, i: int) -> int:
        assert 0 <= i < len(self)
        return self.__get_kth_key(self.__root_pivot, i) - 1

    def __get_kth_key(self, pivot: int, k: int) -> int:
        left_pivot = _left_pivot(pivot)
        i = 0 if pivot & 1 else self.__size[left_pivot]
        if k == i:
            key = self.__data[pivot]
            assert key is not None
            return key
        if k < i:
            return self.__get_kth_key(left_pivot, k)
        return self.__get_kth_key(_right_pivot(pivot), k - i - 1)

    def lower_bound(self, key: int) -> int:
        return self.__lower_bound(self.__root_pivot, key + 1)

    def __lower_bound(self, pivot: int, key: int) -> int:
        root_key = self.__data[pivot]
        if root_key is None:
            return 0
        left_pivot = _left_pivot(pivot)
        if root_key < key:
            i = 0 if pivot & 1 else self.__size[left_pivot]
            i += 1
            if pivot & 1 == 0:
                i += self.__lower_bound(_right_pivot(pivot), key)
            return i
        return 0 if pivot & 1 else self.__lower_bound(left_pivot, key)

    def upper_bound(self, key: int) -> int:
        return self.__upper_bound(self.__root_pivot, key + 1)

    def __upper_bound(self, pivot: int, key: int) -> int:
        root_key = self.__data[pivot]
        if root_key is None:
            return 0
        left_pivot = _left_pivot(pivot)
        if root_key <= key:
            i = 0 if pivot & 1 else self.__size[left_pivot]
            i += 1
            if pivot & 1:
                return i
            else:
                return i + self.__upper_bound(_right_pivot(pivot), key)
        return 0 if pivot & 1 else self.__upper_bound(left_pivot, key)

    def min(self) -> int | None:
        return None if len(self) == 0 else self[0]

    def max(self) -> int | None:
        return None if len(self) == 0 else self[len(self) - 1]
