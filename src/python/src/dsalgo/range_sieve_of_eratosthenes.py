import unittest
import typing
from dsalgo.floor_sqrt import floor_sqrt
from dsalgo.sieve_of_eratosthenes import sieve_of_eratosthenes


def range_sieve_of_eratosthenes(
    less_than: int,
) -> typing.Callable[[int, int], typing.List[int]]:
    primes = sieve_of_eratosthenes(floor_sqrt(less_than) + 1)

    def query(lo: int, hi: int) -> typing.List[int]:
        assert lo <= hi <= less_than
        res: typing.List[int] = []
        if hi <= 2:
            return res
        if lo < 2:
            lo = 2
        if lo & 1 == 0:
            if lo == 2:
                res.append(2)
            lo += 1
        if lo == hi:
            return res
        size = (hi - lo + 1) >> 1
        if_prime = [True] * size
        for i in primes[1:]:
            mn = i * i
            if mn >= hi:
                break
            mn = max(mn, (lo + i - 1) // i * i)
            if mn & 1 == 0:
                mn += i
            for j in range((mn - lo) >> 1, size, i):
                if_prime[j] = False
        for i in range(size):
            if if_prime[i]:
                res.append(lo + (i << 1))
        return res

    return query


class Tests(unittest.TestCase):
    def test(self) -> None:
        range_sieve = range_sieve_of_eratosthenes(1 << 40)
        assert len(range_sieve(999999990000, 1000000000000)) == 337


if __name__ == "__main__":
    import doctest

    unittest.main()

    doctest.testmod(verbose=True)
