# use with coordinates compression.
# values range is limited [0, n) because of Fenwick Tree.

# TODO cut below
import typing

import numba as nb
import numpy as np
from dsa.misc.online_update_query.set_point_get_range.abstract.segtree.jit import (
    build_seg,
    get_seg,
    max_right_seg,
    operate_seg,
)

S = typing.TypeVar("S")


@nb.njit
def seg_op(a: S, b: S) -> S:
    return a + b


@nb.njit
def seg_e() -> S:
    return 0


@nb.njit
def ms_build(n: int) -> np.ndarray:
    return build_seg(np.zeros(n, np.int64))


@nb.njit
def ms_size(ms: np.ndarray) -> int:
    return get_seg(ms, 0, len(ms) - 1)


@nb.njit
def ms_add(ms: np.ndarray, x: int) -> None:
    operate_seg(ms, x, 1)


@nb.njit
def ms_pop(ms: np.ndarray, x: int) -> None:
    assert get_seg(ms, x, x + 1) > 0
    operate_seg(ms, x, -1)


@nb.njit
def ms_get(ms: np.ndarray, ms_len: int, i: int) -> int:
    assert 0 <= i < get_seg(ms, 0, ms_len)

    def is_ok(v, x):
        return v < x

    return max_right_seg(ms, is_ok, i + 1, 0, ms_len)


@nb.njit
def ms_max(ms: np.ndarray, ms_len: int) -> int:
    return ms_get(ms, ms_len, ms_size(ms) - 1)


@nb.njit
def ms_min(ms: np.ndarray, ms_len: int) -> int:
    return ms_get(ms, ms_len, 0)


@nb.njit
def ms_lower_bound(ms: np.ndarray, x: int) -> int:
    return get_seg(ms, 0, x)


@nb.njit
def ms_upper_bound(ms: np.ndarray, x: int) -> int:
    return get_seg(ms, 0, x + 1)
