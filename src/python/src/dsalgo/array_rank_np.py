import numpy as np


def rank(a: np.ndarray) -> np.ndarray:
    rank = np.empty(a.size, dtype=np.int32)
    rank[np.argsort(a)] = np.arange(a.size)
    return rank


def rank_perm(a: np.ndarray) -> np.ndarray:
    rank = np.empty(a.size, dtype=np.int32)
    rank[a] = np.arange(a.size)
    return rank
