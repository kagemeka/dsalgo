import typing

import numba as nb
import numpy as np

S = typing.TypeVar("S")


@nb.njit
def fw_build(op: typing.Callable[[S, S], S], a: np.ndarray) -> np.ndarray:
    r"""Build new fenwick tree."""
    n = len(a)
    fw = np.empty((n + 1,) + a.shape[1:], np.int64)
    fw[1:] = a.copy()
    for i in range(1, n + 1):
        j = i + (i & -i)
        if j < n + 1:
            fw[j] = op(fw[j], fw[i])
    return fw


@nb.njit
def fw_set(
    op: typing.Callable[[S, S], S],
    fw: np.ndarray,
    i: int,
    x: S,
) -> None:
    r"""Set.

    a_i := op(a_i, x)
    """
    assert 0 <= i < len(fw) - 1
    i += 1
    while i < len(fw):
        fw[i] = op(fw[i], x)
        i += i & -i


@nb.njit
def fw_get(
    op: typing.Callable[[S, S], S],
    e: typing.Callable[[], S],
    fw: np.ndarray,
    i: int,
) -> S:
    r"""Get.

    return \prod_{j=0}^{i-1}{a_j}
    """
    assert 0 <= i < len(fw)
    v = e()
    while i > 0:
        v = op(v, fw[i])
        i -= i & -i
    return v


@nb.njit
def fw_max_right(
    op: typing.Callable[[S, S], S],
    e: typing.Callable[[], S],
    fw: np.ndarray,
    is_ok: typing.Callable[[S, S], bool],
    x: S,
) -> int:
    r"""Max right.

    return maximum index i such that is_ok(\prod_{j=0}^{j=i-1}{a_j}, x).
        here, interface is is_ok(v, x) but is_ok(v)
        so that you should pass x explicitly as an argument,
        because closure is not supported on numba v0.53.1 (on AtCoder).
    """
    n = len(fw)
    l = 1
    while l << 1 < n:
        l <<= 1
    v, i = e(), 0
    while l:
        if i + l < n and is_ok(op(v, fw[i + l]), x):
            i += l
            v = op(v, fw[i])
        l >>= 1
    return i


# Fenwick Tree interfaces
S = typing.TypeVar("S")


@nb.njit
def build_fw(a: np.ndarray) -> np.ndarray:
    r"""Build interface."""
    return fw_build(fw_op, a)


@nb.njit
def set_fw(fw: np.ndarray, i: int, x: S) -> None:
    r"""Set interface."""
    fw_set(fw_op, fw, i, x)


@nb.njit
def get_fw(fw: np.ndarray, i: int) -> S:
    r"""Get interface."""
    return fw_get(fw_op, fw_e, fw, i)


@nb.njit
def get_range_fw(fw: np.ndarray, l: int, r: int) -> S:
    r"""Get Range interface.

    return \prod_{j=l}^{r-1}{a_j}.
    target is needed to be Abelian Group but just Commutative Monoid, that is (S, op, e, inv).
    """
    return fw_op(
        fw_inverse(fw_get(fw_op, fw_e, fw, l)),
        fw_get(fw_op, fw_e, fw, r),
    )


@nb.njit
def max_right_fw(
    fw: np.ndarray, is_ok: typing.Callable[[S, S], bool], x: S
) -> int:
    r"""Max right interface."""
    return fw_max_right(fw_op, fw_e, fw, is_ok, x)


@nb.njit
def fw_op(a: S, b: S) -> S:
    return ...


@nb.njit
def fw_e() -> S:
    return ...


@nb.njit
def fw_inverse(a: S) -> S:
    return ...


# 2d fenwick tree (set point add, get range sum)
@nb.njit
def fw2d_build(a: np.ndarray) -> np.ndarray:
    n, m = a.shape[:2]
    fw = np.empty((n + 1, m + 1) + a.shape[2:], np.int64)
    fw[1:, 1:] = a.copy()
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            k = j + (j & -j)
            if k < m + 1:
                fw[i, k] += fw[i, j]
    for j in range(1, m + 1):
        for i in range(1, n + 1):
            k = i + (i & -i)
            if k < n + 1:
                fw[k, j] += fw[i, j]
    return fw


@nb.njit
def fw2d_set(
    fw: np.ndarray,
    i: int,
    j: int,
    x: int,
) -> None:
    n, m = fw.shape
    j0 = j
    while i < n:
        j = j0
        while j < m:
            fw[i, j] += x
            j += j & -j
        i += i & -i


@nb.njit
def fw2d_get(fw: np.ndarray, i: int, j: int) -> int:
    v = 0
    i, j = i + 1, j + 1
    j0 = j
    while i > 0:
        j = j0
        while j > 0:
            v += fw[i, j]
            j -= j & -j
        i -= i & -i
    return v
