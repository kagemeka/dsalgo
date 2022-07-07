import numpy as np


def find_divisors(n: int) -> np.ndarray:
    i = np.arange(int(n**0.5)) + 1
    i = i[n % i == 0]
    return np.unique(np.hstack((i, n // i)))
