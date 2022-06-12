import unittest

import numpy as np

from dsalgo.floor_sqrt import floor_sqrt


def prime_pi_fast(n: int) -> int:
    if n < 2:
        return 0
    sqrt = floor_sqrt(n)
    j = np.arange(sqrt) + 1
    small = np.zeros(sqrt + 1, np.int64)
    large = np.zeros(sqrt + 1, np.int64)
    small[1:] = j - 1
    large[1:] = n // j - 1
    for i in range(2, sqrt + 1):
        if small[i] == small[i - 1]:
            continue
        pi = small[i - 1]
        border = sqrt // i
        n_i = n // i
        d = min(sqrt, border)
        k = np.arange(1, d + 1)
        large[k] -= large[k * i] - pi
        k = np.arange(d + 1, min(sqrt, n_i // i) + 1)
        large[k] -= small[n_i // k] - pi
        j = np.arange(i * i, sqrt + 1)
        small[j] -= small[j // i] - pi
    return int(large[1])


class Tests(unittest.TestCase):
    def test(self) -> None:
        from dsalgo._test_fast_prime_pi import test_fast_prime_counting

        test_fast_prime_counting(prime_pi_fast)


if __name__ == "__main__":
    import doctest

    unittest.main()

    doctest.testmod(verbose=True)
