# mypy: ignore-errors

import numpy as np


def suffix_array(a: np.array) -> np.array:
    n = a.size
    d = 1
    while True:
        a <<= 30
        a[:-d] |= 1 + (a[d:] >> 30)
        sa = a.argsort()
        d <<= 1
        if d >= n:
            return sa
        a[sa[0]], a[sa[1:]] = 0, np.cumsum(a[sa[1:]] != a[sa[:-1]])
