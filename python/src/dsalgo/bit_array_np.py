import numpy as np

N = 63


def new(size: int) -> np.ndarray:
    return np.zeros((size + N - 1) // N, np.int64)


def get(a: np.ndarray, i: np.ndarray) -> np.ndarray:
    return a[i // N] >> (i % N) & 1


def set(a: np.ndarray, i: np.ndarray, value: np.ndarray) -> None:
    flip(a, i[get(a, i) != value])


def flip(a: np.ndarray, i: np.ndarray) -> None:
    np.bitwise_xor.at(a, i // N, 1 << i % N)
