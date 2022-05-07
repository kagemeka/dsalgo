from __future__ import annotations

import typing

import dsalgo.primality


def find_prime_numbers(max_size: int) -> list[int]:
    is_prime = dsalgo.primality.sieve_of_eratosthenes(max_size)
    return [i for i in range(max_size) if is_prime[i]]


def prime_factorize(n: int) -> list[tuple[int, int]]:
    primes: list[int] = []
    counts: list[int] = []
    i = 1
    while i * i < n:
        i += 1
        if n % i:
            continue
        primes.append(i)
        counts.append(0)
        while n % i == 0:
            n //= i
            counts[-1] += 1
    if n > 1:
        primes.append(n)
        counts.append(1)
    return list(zip(primes, counts))


def prime_factorize_lpf(
    max_size: int,
) -> typing.Callable[[int], list[tuple[int, int]]]:
    lpf = least_prime_factor(max_size)

    def prime_factorize(n: int) -> list[tuple[int, int]]:
        primes = [0]
        counts = [0]
        while n > 1:
            prime = lpf[n]
            n //= prime
            if prime == primes[-1]:
                counts[-1] += 1
            else:
                primes.append(prime)
                counts.append(1)
        return list(zip(primes[1:], counts[1:]))

    return prime_factorize


def least_prime_factor(max_value: int) -> list[int]:
    is_prime = dsalgo.primality.sieve_of_eratosthenes(max_value)
    lpf = list(range(max_value))
    for i in range(2, max_value):
        if i * i >= max_value:
            break
        if not is_prime[i]:
            continue
        for j in range(i * i, max_value, i):
            if lpf[j] == j:
                lpf[j] = i
    return lpf


def greatest_prime_factor(n: int) -> list[int]:
    lpf = least_prime_factor(n)
    gpf = list(range(n))
    for i in range(2, n):
        if lpf[i] == i:
            continue
        gpf[i] = gpf[i // lpf[i]]
    return gpf


def count_prime_factors(max_value: int) -> list[int]:
    count = [0] * max_value
    for p in find_prime_numbers(max_value):
        for i in range(p, max_value, p):
            count[i] += 1
    return count
