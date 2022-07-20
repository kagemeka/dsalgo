import numpy as np


def array_rank(a: np.ndarray) -> np.ndarray:
    rank = np.empty(a.size, dtype=np.int32)
    rank[np.argsort(a)] = np.arange(a.size)
    return rank
