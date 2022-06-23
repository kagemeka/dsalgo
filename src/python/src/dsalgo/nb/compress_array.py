import numba as nb
import numpy as np


@nb.njit
def compress_array(a: np.ndarray) -> tuple[(np.ndarray,) * 2]:
    v = np.unique(a)
    return np.searchsorted(v, a), v
