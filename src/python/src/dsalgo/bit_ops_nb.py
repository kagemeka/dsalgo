import numba
import numpy as np
from numpy import typing as npt
import unittest
import dsalgo.bitset

bit_length = numba.njit(dsalgo.bitset.bit_length)


@numba.njit
def bit_length_table(n: int) -> npt.NDArray[np.uint8]:
    length: npt.NDArray[np.uint8] = np.zeros(n, np.uint8)
    for i in range(1, n):
        length[i] = length[i >> 1] + 1
    return length


popcount = numba.njit(dsalgo.bitset.popcount)


@numba.njit
def popcount_table(n: int) -> npt.NDArray[np.uint8]:
    count: npt.NDArray[np.uint8] = np.zeros(n, np.uint8)
    for i in range(n):
        count[i] = count[i >> 1] + (i & 1)
    return count


class Test(unittest.TestCase):
    def test(self) -> None:
        self.assertTrue(
            np.all(
                bit_length_table(10)
                == np.array([0, 1, 2, 2, 3, 3, 3, 3, 4, 4])
            ),
        )


if __name__ == "__main__":
    unittest.main()
