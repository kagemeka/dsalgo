import unittest

from dsalgo.sieve_of_eratosthenes import sieve_of_eratosthenes


def prime_pi_table(size: int) -> list[int]:
    pi = [0] * size
    for p in sieve_of_eratosthenes(size):
        pi[p] = 1
    for i in range(size - 1):
        pi[i + 1] += pi[i]
    return pi


# TODO:
class Tests(unittest.TestCase):
    def test(self) -> None:
        ...


if __name__ == "__main__":
    import doctest

    unittest.main()

    doctest.testmod(verbose=True)
