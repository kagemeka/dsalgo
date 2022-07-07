import typing

import numba as nb
import numpy as np
from dsa.tree.misc.fenwick.one_indexed.jit import fw_build, fw_get, fw_set

# TODO cut below


@nb.njit
def build_fw(a: np.ndarray) -> np.ndarray:
    return fw_build(fw_op, a)


S = typing.TypeVar("S")


@nb.njit
def set_fw(
    fw: np.ndarray,
    l: int,
    r: int,
    x: S,
) -> None:
    fw_set(fw_op, fw, l, x)
    fw_set(fw_op, fw, r, fw_inverse(x))


@nb.njit
def get_fw(fw: np.ndarray, i: int) -> S:
    return fw_get(fw_op, fw_e, fw, i + 1)


@nb.njit
def fw_op(a: S, b: S) -> S:
    return ...


@nb.njit
def fw_e() -> S:
    return 0


@nb.njit
def fw_inverse(a: S) -> S:
    return ...
