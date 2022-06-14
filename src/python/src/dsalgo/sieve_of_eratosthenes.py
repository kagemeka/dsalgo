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


class Tests(unittest.TestCase):
    def test(self) -> None:
        assert sieve_of_eratosthenes(2) == []
        assert sieve_of_eratosthenes(100) == [
            2,
            3,
            5,
            7,
            11,
            13,
            17,
            19,
            23,
            29,
            31,
            37,
            41,
            43,
            47,
            53,
            59,
            61,
            67,
            71,
            73,
            79,
            83,
            89,
            97,
        ]


if __name__ == "__main__":
    import doctest

    unittest.main()

    doctest.testmod(verbose=True)
