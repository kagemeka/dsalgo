import numpy as np


def convolve(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    k = len(a) + len(b) - 1
    n = 1 << (k.bit_length() + 1)
    return np.rint(
        np.fft.irfft(np.fft.rfft(a, n) * np.fft.rfft(b, n), n),
    ).astype(np.int64)[:k]
