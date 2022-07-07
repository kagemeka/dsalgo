import itertools

import numpy as np


def combinations(n: int, k: int) -> np.ndarray:
    """Combinations.

    Args:
        n (int): n of nCk
        k (int): k of nCk

    Returns:
        np.ndarray: combinations matrix.
    """
    return np.array((*itertools.combinations(range(n), k),))


def permutations(n: int, k: int) -> np.ndarray:
    """Permutations.

    Args:
        n (int): n of nPk
        k (int): k of nPk

    Returns:
        np.ndarray: permutations matrix.
    """

    return np.array((*itertools.permutations(range(n), k),))
