import numpy as np


def convolve(a: np.ndarray, b: np.ndarray, n: int = 1 << 18) -> np.ndarray:
    return np.rint(
        np.fft.irfft(np.fft.rfft(a, n) * np.fft.rfft(b, n), n),
    ).astype(np.int64)
