import numpy as np


def longest_common_subsequence(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """Longest Common Subsequence.

    Args:
        a (np.ndarray): first array.
        b (np.ndarray): second array.

    Returns:
        np.ndarray: result.
    """
    n, m = a.size, b.size
    length = np.zeros((n + 1, m + 1), dtype=np.int64)
    for i in range(n):
        np.maximum(
            length[i, :-1] + (a[i] == b),
            length[i, 1:],
            out=length[i + 1, 1:],
        )
        np.maximum.accumulate(length[i + 1], out=length[i + 1])
    lcs = []
    i, j = n - 1, m - 1
    while i >= 0 and j >= 0:
        x = length[i + 1, j + 1]
        if length[i + 1, j] == x:
            j -= 1
            continue
        if length[i, j + 1] == x:
            i -= 1
            continue
        lcs.append(a[i])
        i -= 1
        j -= 1
    return np.array(lcs)[::-1]
