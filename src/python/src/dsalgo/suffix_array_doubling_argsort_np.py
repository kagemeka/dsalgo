# mypy: ignore-errors

import numpy as np

# slower than argsort


def suffix_array(a: np.array) -> np.array:
    n = a.size
    d = 1
    while True:
        a <<= 30
        a[:-d] |= 1 + (a[d:] >> 30)
        a = np.searchsorted(np.unique(a), a)
        d <<= 1
        if d >= n:
            return a.argsort()
