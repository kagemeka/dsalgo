import unittest

from dsalgo.floor_sqrt import floor_sqrt


# mypy: ignore-errors
def prime_pi_fast_optimized_np(n: int) -> int:
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
    def test(self) -> None:
        from dsalgo._test_fast_prime_pi import test_fast_prime_counting

        test_fast_prime_counting(prime_pi_fast_optimized_np)


if __name__ == "__main__":
    import doctest

    unittest.main()

    doctest.testmod(verbose=True)
