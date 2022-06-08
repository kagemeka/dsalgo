import unittest


def sieve_of_eratosthenes(sieve_size: int) -> list[int]:
    if sieve_size <= 2:
        return []
    primes = [2]
    is_prime = [True] * (sieve_size >> 1)
    for i in range(3, sieve_size, 2):
        if not is_prime[i >> 1]:
            continue
        primes.append(i)
        for j in range(i * i >> 1, sieve_size >> 1, i):
            is_prime[j] = False
    return primes


# TODO:
class Tests(unittest.TestCase):
    def test(self) -> None:
        ...


if __name__ == "__main__":
    import doctest

    unittest.main()

    doctest.testmod(verbose=True)
