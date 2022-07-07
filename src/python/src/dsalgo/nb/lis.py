import numba as nb
import numpy as np

from dsalgo.constant import INT_INF


@nb.njit
def longest_increasing_sequence(a: np.ndarray) -> np.ndarray:
    assert INT_INF > a.max()
    lis = np.full(len(a), INT_INF, np.int64)
    for x in a:
        lis[np.searchsorted(lis, x)] = x
    return lis[: np.searchsorted(lis, INT_INF)]
