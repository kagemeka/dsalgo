from __future__ import annotations


def count_divisors_zeta_transform(n: int) -> list[int]:
    cnt = [1] * n
    cnt[0] = 0
    for i in range(2, n):
        for j in range(i, n, i):
            cnt[j] += 1
    return cnt


def find_divisors(n: int) -> list[int]:
    divisors = []
    for i in range(1, n + 1):
        if i * i > n:
            break
        if n % i:
            continue
        divisors.append(i)
        if i * i != n:
            divisors.append(n // i)
    return sorted(divisors)


def highly_composite_numbers() -> list[int]:
    ...


import unittest


class TestCountDivisors(unittest.TestCase):
    def test(self) -> None:
        self.assertEqual(
            count_divisors_zeta_transform(20),
            [0, 1, 2, 2, 3, 2, 4, 2, 4, 3, 4, 2, 6, 2, 4, 4, 5, 2, 6, 2],
        )


class TestFindDivisors(unittest.TestCase):
    def test(self) -> None:
        self.assertEqual(
            find_divisors(100),
            [1, 2, 4, 5, 10, 20, 25, 50, 100],
        )


if __name__ == "__main__":
    unittest.main()
