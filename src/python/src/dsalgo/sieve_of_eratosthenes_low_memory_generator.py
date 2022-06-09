import typing
import unittest

from dsalgo.floor_sqrt import floor_sqrt
from dsalgo.range_sieve_of_eratosthenes import range_sieve_of_eratosthenes


def sieve_of_eratosthenes_low_memory_generator(
    lo: int,
    hi: int,
) -> typing.Generator[int, None, None]:
    if lo < 2:
        lo = 2
    if hi < 2:
        hi = 2
    query = range_sieve_of_eratosthenes(hi)
    range_size = floor_sqrt(hi) << 3
    for i in range(lo, hi, range_size):
        yield from query(i, min(hi, i + range_size))


# TODO:
class Tests(unittest.TestCase):
    def test(self) -> None:
        ...


if __name__ == "__main__":
    import doctest

    unittest.main()

    doctest.testmod(verbose=True)
