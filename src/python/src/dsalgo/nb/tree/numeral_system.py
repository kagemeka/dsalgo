import numba as nb
import numpy as np


@nb.njit
def int_from_nary(nums: np.ndarray, base: int) -> int:
    assert abs(base) >= 2
    n, d = 0, 1
    for x in nums:
        n += d * x
        d *= base
    return n


@nb.njit
def int_to_nary(n: int, base: int) -> np.ndarray:
    assert abs(base) >= 2
    nums, ptr = np.empty(64, np.int64), 0
    while True:
        n, r = divmod(n, base)
        if r < 0:
            n += 1
            r -= base
        nums[ptr] = r
        ptr += 1
        if n == 0:
            break
    return nums[:ptr]
