import unittest

import numpy as np

from dsalgo.floor_sqrt import floor_sqrt


def fast(n: int) -> int:
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


# mypy: ignore-errors
def fast_opt(n: int) -> int:
    import numpy as np

    if n < 2:
        return 0
    if n == 2:
        return 1

    def half(i: int) -> int:
        return (i - 1) >> 1

    sqrt = floor_sqrt(n)
    size = (sqrt + 1) >> 1
    small = np.arange(size)
    large = half(n // (np.arange(size) << 1 | 1))
    unsieved_nums = np.arange(size) << 1 | 1
    checked_or_sieved = np.zeros(size, np.bool8)
    pi = 0
    for i in range(3, sqrt + 1, 2):
        half_i = half(i)
        if checked_or_sieved[half_i]:
            continue
        i2 = i * i
        if i2 * i2 > n:
            break
        checked_or_sieved[half_i] = True
        checked_or_sieved[half(np.arange(i2, sqrt + 1, i << 1))] = True
        k = np.arange(size)
        j = unsieved_nums[k]
        k = k[~checked_or_sieved[half(j)]]
        j = j[k]

        size = k.size
        border = j * i
        flg = border <= sqrt
        x = np.empty(size, np.int64)
        x[flg] = large[small[border[flg] >> 1] - pi]
        x[~flg] = small[half(n // border[~flg])]
        large[:size] = large[k] - x + pi
        unsieved_nums[:size] = j

        j = half(sqrt)
        for k in range(sqrt // i - 1 | 1, i - 1, -2):
            c = small[k >> 1] - pi
            e = k * i >> 1
            small[e : j + 1] -= c
            j = e - 1

        pi += 1

    large[0] += (size + ((pi - 1) << 1)) * (size - 1) >> 1
    large[0] -= large[1:size].sum()

    k = np.arange(1, size)
    q = unsieved_nums[k]
    n_q = n // q
    e = small[half(n_q // q)] - pi
    t = np.array(
        [
            np.sum(
                small[
                    half(
                        n_q[j] // unsieved_nums[np.arange(k[j] + 1, e[j] + 1)]
                    )
                ]
            )
            for j in range(size - 1)
            if e[j] >= k[j] + 1
        ]
    )
    s = t.size
    large[0] += np.sum(t - (e - k)[:s] * (pi + k - 1)[:s])
    return large[0] + 1


class Tests(unittest.TestCase):
    def test_fast_opt(self) -> None:
        from dsalgo.prime_pi import _test_fast_prime_pi

        _test_fast_prime_pi(fast_opt)

    def test_fast(self) -> None:
        from dsalgo.prime_pi import _test_fast_prime_pi

        _test_fast_prime_pi(fast)


if __name__ == "__main__":
    import doctest

    unittest.main()

    doctest.testmod(verbose=True)
