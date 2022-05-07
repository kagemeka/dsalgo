import typing

import dsalgo.prime_number


def naive(n: int) -> int:
    count = n
    for p, _ in dsalgo.prime_number.prime_factorize(n):
        count = count // p * (p - 1)
    return count


def lpf(max_value: int) -> typing.Callable[[int], int]:
    prime_factorize = dsalgo.prime_number.prime_factorize_lpf(max_value)

    def euler_totient(n: int) -> int:
        count = n
        for p, _ in prime_factorize(n):
            count = count // p * (p - 1)
        return count

    return euler_totient
