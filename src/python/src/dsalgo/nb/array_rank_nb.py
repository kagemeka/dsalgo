import numba as nb
import numpy as np


@nb.njit
def compute_rank(a: np.ndarray) -> np.ndarray:
    return np.argsort(np.argsort(a))


@nb.njit
def compute_reversed_rank(a: np.ndarray) -> np.ndarray:
    return np.argsort(np.argsort(a)[::-1])
