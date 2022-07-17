import itertools

import numpy as np


def combinations(n: int, k: int) -> np.ndarray:
    return np.array((*itertools.combinations(range(n), k),))


def permutations(n: int, k: int) -> np.ndarray:
    return np.array((*itertools.permutations(range(n), k),))
