import unittest


def euler_totient(n: int) -> int:
    c, i = n, 1
    for i in range(2, n + 1):
        if i * i > n:
            break
        if n % i:
            continue
        c -= c // i
        while n % i == 0:
            n //= i
    if n > 1:
        c -= c // n
    return c


class Tests(unittest.TestCase):
    def test(self) -> None:
        ans = [
            1,
            1,
            2,
            2,
            4,
            2,
            6,
            4,
            6,
            4,
            10,
            4,
            12,
            6,
            8,
            8,
            16,
            6,
            18,
            8,
            12,
            10,
            22,
            8,
            20,
            12,
            18,
            12,
            28,
            8,
            30,
            16,
            20,
            16,
            24,
            12,
            36,
            18,
            24,
            16,
            40,
            12,
            42,
            20,
            24,
            22,
            46,
            16,
            42,
            20,
            32,
            24,
            52,
            18,
            40,
            24,
            36,
            28,
            58,
            16,
            60,
            30,
            36,
            32,
            48,
            20,
            66,
            32,
            44,
        ]
        for i, a in enumerate(ans):
            assert euler_totient(i + 1) == a


if __name__ == "__main__":
    import doctest

    unittest.main()

    doctest.testmod(verbose=True)
