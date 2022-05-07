import numpy as np


def least_prime_factor_np(n: int) -> np.ndarray:
    s = np.arange(n)
    s[:2] = -1
    i = 0
    while i * i < n - 1:
        i += 1
        if s[i] == i:
            np.minimum(s[i * i :: i], i, out=s[i * i :: i])
    return s


def sieve_of_eratosthenes_np(n: int) -> np.ndarray:
    return least_prime_factor_np(n) == np.arange(n)


def greatest_prime_factor_np(n: int) -> np.ndarray:
    s = np.arange(n)
    s[:2] = -1
    i = 0
    while i < n - 1:
        i += 1
        if s[i] == i:
            s[i::i] = i
    return s
