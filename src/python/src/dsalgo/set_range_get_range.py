import dsalgo.fenwick_tree


class FenwickTreeAddSum:
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


class LazySegmentTreeAddSum:
    ...

    # # set range add, get range sum
    # def solve() -> None:
    #     s_op = lambda a, b: (a[0] + b[0], a[1] + b[1])
    #     s_e = lambda: (0, 0)
    #     f_op = lambda f, g: f + g
    #     f_e = lambda: 0
    #     ms = Monoid(s_op, s_e, False)
    #     mf = Monoid(f_op, f_e, False)
    #     map_ = lambda f, x: (x[0] + f * x[1], x[1])
