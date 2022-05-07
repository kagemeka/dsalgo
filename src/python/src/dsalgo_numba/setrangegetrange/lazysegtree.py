import numba as nb
import numpy as np

from dsalgo.type import F, S


# set range add, get range mininum.
# @nb.njit
def seg_op_s(a: S, b: S) -> S:
    return min(a, b)


@nb.njit
def seg_e_s() -> S:
    return 1 << 60


@nb.njit
def seg_op_f(f: F, g: F) -> F:
    return f + g


@nb.njit
def seg_e_f() -> F:
    return 0


@nb.njit
def seg_map(f: F, x: S) -> S:
    return x + f


# set range xor, get range xor
@nb.njit
def seg_op_s(a: S, b: S) -> S:
    return a ^ b


@nb.njit
def seg_e_s() -> S:
    return 0


@nb.njit
def seg_op_f(f: F, g: F) -> F:
    return g ^ f


@nb.njit
def seg_e_f() -> F:
    return 0


@nb.njit
def seg_map(f: F, x: S) -> S:
    return x ^ f


# set range update, get range maximum
@nb.njit
def seg_op_s(a: S, b: S) -> S:
    return max(a, b)


@nb.njit
def seg_e_s() -> S:
    return -(1 << 60)


@nb.njit
def seg_op_f(f: F, g: F) -> F:
    return g if f == seg_e_f() else f


@nb.njit
def seg_e_f() -> F:
    return -1


@nb.njit
def seg_map(f: F, x: S) -> S:
    return x if f == seg_e_f() else f


# set range add, get range sum
@nb.njit
def seg_op_s(a: S, b: S) -> S:
    return a + b


@nb.njit
def seg_e_s() -> S:
    return np.zeros(2, np.int64)


@nb.njit
def seg_op_f(f: F, g: F) -> F:
    return f + g


@nb.njit
def seg_e_f() -> F:
    return 0


@nb.njit
def seg_map(f: F, x: S) -> S:
    return np.array([x[0] + f * x[1], x[1]])
