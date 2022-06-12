import unittest

from dsalgo.floor_sqrt import floor_sqrt


def prime_pi_fast_optimized(n: int) -> int:
    if n < 2:
        return 0
    if n == 2:
        return 1

    def half(i: int) -> int:
        return (i - 1) >> 1

    sqrt = floor_sqrt(n)
    size = (sqrt + 1) >> 1
    small = list(range(size))
    large = [half(n // (i << 1 | 1)) for i in range(size)]
    unsieved_nums = [i << 1 | 1 for i in range(size)]
    checked_or_sieved = [False] * size
    pi = 0
    for i in range(3, sqrt + 1, 2):
        if checked_or_sieved[half(i)]:
            continue
        i2 = i * i
        if i2 * i2 > n:
            break
        checked_or_sieved[half(i)] = True
        for j in range(i2, sqrt + 1, i << 1):
            checked_or_sieved[half(j)] = True
        ptr = 0
        for k in range(size):
            j = unsieved_nums[k]
            if checked_or_sieved[half(j)]:
                continue
            border = j * i
            large[ptr] = large[k] + pi
            large[ptr] -= (
                large[small[border >> 1] - pi]
                if border <= sqrt
                else small[half(n // border)]
            )
            unsieved_nums[ptr] = j
            ptr += 1
        size = ptr
        j = half(sqrt)
        k = sqrt // i - 1 | 1
        while k >= i:
            c = small[k >> 1] - pi
            e = k * i >> 1
            while j >= e:
                small[j] -= c
                j -= 1
            k -= 2
        pi += 1

    large[0] += (size + ((pi - 1) << 1)) * (size - 1) >> 1
    large[0] -= sum(large[1:size])
    for k in range(1, size):
        q = unsieved_nums[k]
        n_q = n // q
        e = small[half(n_q // q)] - pi
        if e < k + 1:
            break
        t = sum(small[half(n_q // unsieved_nums[l + 1])] for l in range(k, e))
        large[0] += t - (e - k) * (pi + k - 1)

    return large[0] + 1


class Tests(unittest.TestCase):
    def test(self) -> None:
        from dsalgo._test_fast_prime_pi import test_fast_prime_counting

        test_fast_prime_counting(prime_pi_fast_optimized)


if __name__ == "__main__":
    import doctest

    unittest.main()

    doctest.testmod(verbose=True)
