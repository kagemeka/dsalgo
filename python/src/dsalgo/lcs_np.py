# mypy: ignore-errors


import unittest

import numpy as np


def dp_np(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    n, m = a.size, b.size
    length = np.zeros((n + 1, m + 1), dtype=np.int64)
    for i in range(n):
        np.maximum(
            length[i, :-1] + (a[i] == b),
            length[i, 1:],
            out=length[i + 1, 1:],
        )
        np.maximum.accumulate(length[i + 1], out=length[i + 1])
    return length


# TODO:
class Test(unittest.TestCase):
    def test(self) -> None:
        ...


if __name__ == "__main__":
    import doctest

    unittest.main()

    doctest.testmod(verbose=True)
