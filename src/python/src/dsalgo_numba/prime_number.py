import typing

import numba as nb
import numpy as np


@nb.njit
def least_prime_factor(n: int) -> np.ndarray:
    s = np.arange(n)
    s[:2] = -1
    i = 0
    while i * i < n - 1:
        i += 1
        if s[i] != i:
            continue
        j = np.arange(i * i, n, i)
        s[j[s[j] == j]] = i
    return s


@nb.njit
def greatest_prime_factor(n: int) -> np.ndarray:
    s = np.arange(n)
    s[:2] = -1
    i = 0
    while i < n - 1:  # e.g. 51 = 3 * 17, 17 > \sqrt{51}
        i += 1
        if s[i] == i:
            s[i::i] = i
    return s


@nb.njit
def sieve_of_eratosthenes(n: int) -> np.ndarray:
    return least_prime_factor(n) == np.arange(n)


@nb.njit
def find_prime_numbers(n: int) -> np.ndarray:
    return np.flatnonzero(sieve_of_eratosthenes(n))


@nb.njit
def prime_factorize(n: int) -> np.ndarray:
    prime, cnt = [], []
    i = 1
    while i * i < n:
        i += 1
        if n % i:
            continue
        prime.append(i)
        cnt.append(0)
        while n % i == 0:
            n //= i
            cnt[-1] += 1
    if n > 1:
        prime.append(n)
        cnt.append(1)
    return np.vstack((np.array(prime), np.array(cnt))).T


@nb.njit
def prime_factorize_factorial(n: int) -> np.ndarray:
    prime, cnt = [], []
    idx = np.full(n + 1, -1, dtype=np.int64)
    for i in range(n + 1):
        for p, c in prime_factorize(i):
            if idx[p] != -1:
                cnt[idx[p]] += c
                continue
            idx[p] = len(prime)
            prime.append(p)
            cnt.append(c)
    return np.vstack((np.array(prime), np.array(cnt))).T


@nb.njit
def prime_factorize_lpf(n: int, lpf: np.ndarray) -> np.ndarray:
    prime, cnt = [-1], [-1]
    while n > 1:
        p = lpf[n]
        n //= p
        if prime[-1] == p:
            cnt[-1] += 1
            continue
        prime.append(p)
        cnt.append(1)
    return np.vstack((np.array(prime), np.array(cnt))).T[1:]


@nb.njit
def prime_factorize_factorial_lpf(n: int, lpf: np.ndarray) -> np.array:
    prime, cnt = [], []
    idx = np.full(n + 1, -1, dtype=np.int64)
    for i in range(n + 1):
        for p, c in prime_factorize(i, lpf):
            i = idx[p]
            if i != -1:
                cnt[i] += c
                continue
            idx[p] = len(prime)
            prime.append(p)
            cnt.append(c)
    return np.vstack((np.array(prime), np.array(cnt))).T


@nb.njit
def count_prime_factors(n: int) -> np.ndarray:
    cnt = np.zeros(n, np.int64)
    for p in find_prime_numbers(n):
        cnt[p::p] += 1
    return cnt


@nb.njit
def aks(n: int) -> bool:
    ...


@nb.njit
def miller_rabin(n: int) -> bool:
    ...


@nb.njit
def linear_sieve(n: int) -> list[bool]:
    ...


@nb.njit
def sieve_of_atkin(n: int) -> list[bool]:
    ...
