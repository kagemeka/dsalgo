import numba as nb
import numpy as np


@nb.njit((nb.i8[:], nb.i8[:]), cache=True)
def lcs(
    a: np.ndarray,
    b: np.ndarray,
) -> np.ndarray:
    n, m = a.size, b.size

    def _compute_lcs_len():
        length = np.zeros((n + 1, m + 1), np.int64)
        for i in range(n):
            for j in range(m):
                length[i + 1][j + 1] = max(
                    length[i][j + 1],
                    length[i + 1][j],
                    length[i][j] + (a[i] == b[j]),
                )
        return length

    def _retrieve_lcs(length):
        k = length[n][m]
        lcs = np.empty(k, np.int64)
        i, j = n - 1, m - 1
        while i >= 0 and j >= 0:
            x = length[i + 1][j + 1]
            if length[i + 1][j] == x:
                j -= 1
            elif length[i][j + 1] == x:
                i -= 1
            else:
                k -= 1
                lcs[k] = a[i]
                i -= 1
                j -= 1
        return lcs

    l = _compute_lcs_len()
    return _retrieve_lcs(l)
