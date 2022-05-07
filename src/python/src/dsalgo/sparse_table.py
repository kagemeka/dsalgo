from __future__ import annotations

import copy
import typing

import dsalgo.abstract_structure
from dsalgo.type import S


def sparse_table(
    semigroup: dsalgo.abstract_structure.Semigroup[S],
    arr: list[S],
) -> typing.Callable[[int, int], S]:
    n = len(arr)
    assert n > 0
    data = [arr.copy()]
    for i in range((n - 1).bit_length() - 1):
        data.append(data[i].copy())
        for j in range(n - (1 << i)):
            data[i + 1][j] = semigroup.operation(
                data[i][j],
                data[i][j + (1 << i)],
            )

    def get(left: int, right: int) -> S:
        assert 0 <= left < right <= n
        if right - left == 1:
            return data[0][left]
        k = (right - 1 - left).bit_length() - 1
        return semigroup.operation(data[k][left], data[k][right - (1 << k)])

    return get


def sparse_table_2d(
    semigroup: dsalgo.abstract_structure.Semigroup[S],
    matrix: list[list[S]],
) -> typing.Callable[[int, int, int, int], S]:
    h = len(matrix)
    assert h > 0
    w = len(matrix[0])
    assert w > 0 and all(len(row) == w for row in matrix)
    data = [copy.deepcopy(matrix)]

    for log_dx in range((w - 1).bit_length() - 1):
        i = log_dx
        data.append(copy.deepcopy(data[i]))
        for y in range(h):
            for x in range(w - (1 << i)):
                data[i + 1][y][x] = semigroup.operation(
                    data[i][y][x],
                    data[i][y][x + (1 << i)],
                )
    width = len(data)
    assert len(data) == max(1, (w - 1).bit_length())
    for log_dy in range((h - 1).bit_length() - 1):
        for log_dx in range(max(1, (w - 1).bit_length())):
            i = log_dy * width + log_dx
            ni = i + width
            data.append(copy.deepcopy(data[i]))
            for y in range(h - (1 << log_dy)):
                for x in range(w - (1 << log_dx)):
                    data[ni][y][x] = semigroup.operation(
                        data[i][y][x],
                        data[i][y + (1 << log_dy)][x],
                    )

    def get(y0: int, x0: int, y1: int, x1: int) -> S:
        assert 0 <= y0 < y1 <= h and 0 <= x0 < x1 <= w
        log_dy = (y1 - y0 - 1).bit_length() - 1
        log_dx = (x1 - x0 - 1).bit_length() - 1
        if log_dy == log_dx == -1:
            return data[0][y0][x0]
        if log_dy == -1:
            return semigroup.operation(
                data[log_dx][y0][x0],
                data[log_dx][y0][x1 - (1 << log_dx)],
            )
        if log_dx == -1:
            return semigroup.operation(
                data[log_dy][y0][x0],
                data[log_dy][y1 - (1 << log_dy)][x0],
            )
        i = log_dy * width + log_dx
        res = semigroup.operation(
            data[i][y0][x0],
            data[i][y1 - (1 << log_dy)][x1 - (1 << log_dx)],
        )
        res = semigroup.operation(res, data[i][y0][x1 - (1 << log_dx)])
        return semigroup.operation(res, data[i][y1 - (1 << log_dy)][x0])

    return get


def sparse_table_2d_fixed_window(
    semigroup: dsalgo.abstract_structure.Semigroup[S],
    matrix: list[list[S]],
    window_shape: tuple[int, int],
) -> typing.Callable[[int, int], S]:
    assert len(matrix) > 0
    assert len(matrix[0]) > 0 and all(
        len(row) == len(matrix[0]) for row in matrix
    )
    h, w = window_shape
    assert 0 < h <= len(matrix) and 0 < w <= len(matrix[0])
    data = copy.deepcopy(matrix)
    for log_dx in range((w - 1).bit_length() - 1):
        for y in range(len(matrix)):
            for x in range(len(matrix[0]) - (1 << log_dx)):
                data[y][x] = semigroup.operation(
                    data[y][x],
                    data[y][x + (1 << log_dx)],
                )
            data[y] = data[y][: len(matrix[0]) - (1 << log_dx)]

    for log_dy in range((h - 1).bit_length() - 1):
        for y in range(len(matrix) - (1 << log_dy)):
            for x in range(len(data[0])):
                data[y][x] = semigroup.operation(
                    data[y][x],
                    data[y + (1 << log_dy)][x],
                )
        data = data[: len(matrix) - (1 << log_dy)]

    log_dy = (h - 1).bit_length() - 1
    log_dx = (w - 1).bit_length() - 1
    if log_dx != -1:
        for y in range(len(data)):
            for x in range(len(matrix[0]) - w + 1):
                data[y][x] = semigroup.operation(
                    data[y][x],
                    data[y][x + w - (1 << log_dx)],
                )
            data[y] = data[y][: len(matrix[0]) - w + 1]
    if log_dy != -1:
        for y in range(len(matrix) - h + 1):
            for x in range(len(data[0])):
                data[y][x] = semigroup.operation(
                    data[y][x],
                    data[y + h - (1 << log_dy)][x],
                )
        data = data[: len(matrix) - h + 1]

    def get(y0: int, x0: int) -> S:
        return data[y0][x0]

    return get


def disjoint_sparse_table(
    semigroup: dsalgo.abstract_structure.Semigroup[S],
    arr: list[S],
) -> typing.Callable[[int, int], S]:
    n = len(arr)
    assert n > 0
    k = max(1, (n - 1).bit_length())
    data = [arr.copy()]
    for i in range(1, k):
        data.append(arr.copy())
        for j in range(1 << i, n + 1, 2 << i):
            for k in range(1, 1 << i):
                data[i][j - k - 1] = semigroup.operation(
                    data[i][j - k - 1],
                    data[i][j - k],
                )
            for k in range((1 << i) - 1):
                if j + k + 1 >= n:
                    break
                data[i][j + k + 1] = semigroup.operation(
                    data[i][j + k],
                    data[i][j + k + 1],
                )

    def get(left: int, right: int) -> S:
        assert 0 <= left < right <= n
        if right - left == 1:
            return data[0][left]
        k = (left ^ (right - 1)).bit_length() - 1
        return semigroup.operation(data[k][left], data[k][right - 1])

    return get


def disjoint_sparse_table_int_xor(
    arr: list[int],
) -> typing.Callable[[int, int], int]:
    n = len(arr)
    assert n > 0
    k = max(1, (n - 1).bit_length())
    data = [arr.copy()]
    for i in range(1, k):
        data.append(arr.copy())
        for j in range(1 << i, n + 1, 2 << i):
            for k in range(1, 1 << i):
                data[i][j - k - 1] ^= data[i][j - k]
            for k in range((1 << i) - 1):
                if j + k + 1 >= n:
                    break
                data[i][j + k + 1] ^= data[i][j + k]

    def get(left: int, right: int) -> int:
        assert 0 <= left < right <= n
        if right - left == 1:
            return data[0][left]
        k = (left ^ (right - 1)).bit_length() - 1
        return data[k][left] ^ data[k][right - 1]

    return get


def disjoint_sparse_table_int_sum(
    arr: list[int],
) -> typing.Callable[[int, int], int]:
    n = len(arr)
    assert n > 0
    bit_length = dsalgo.bitset.bit_length_table(n << 1)
    k = max(1, bit_length[n - 1])
    data = [arr.copy()]
    for i in range(1, k):
        data.append(arr.copy())
        for j in range(1 << i, n + 1, 2 << i):
            for k in range(1, 1 << i):
                data[i][j - k - 1] += data[i][j - k]
            for k in range((1 << i) - 1):
                if j + k + 1 >= n:
                    break
                data[i][j + k + 1] += data[i][j + k]

    def get(left: int, right: int) -> int:
        assert 0 <= left < right <= n
        if right - left == 1:
            return data[0][left]
        k = bit_length[left ^ (right - 1)] - 1
        return data[k][left] + data[k][right - 1]

    return get


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
