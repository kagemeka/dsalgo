"""TODO
- search highly composite numbers
"""

import numba as nb
import numpy as np


@nb.njit
def find_divisors(n: int) -> np.ndarray:
    i = np.arange(int(n**0.5)) + 1
    i = i[n % i == 0]
    return np.unique(np.hstack((i, n // i)))
