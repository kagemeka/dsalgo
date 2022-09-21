import numpy as np


def popcount(k: int) -> np.ndarray:
    c = np.empty(1 << k, np.int64)
    c[0] = 0
    for i in range(k):
        c[1 << i : 1 << i + 1] = c[: 1 << i] + 1
    return c


print(popcount(4))
