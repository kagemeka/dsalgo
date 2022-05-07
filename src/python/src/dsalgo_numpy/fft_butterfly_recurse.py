import numpy as np


class FFT:
    def __call__(
        self,
        a: np.ndarray,
        inverse: bool = False,
    ) -> np.ndarray:
        n = a.size
        if n == 1:
            return a
        b = a[::2]
        c = a[1::2]
        self(b, inverse)
        self(c, inverse)
        sign = -1 + 2 * inverse
        zeta = np.exp(sign * 2j * np.pi / n * np.arange(n))
        a[: n // 2], a[n // 2 :] = (
            b + zeta[: n // 2] * c,
            b + zeta[n // 2 :] * c,
        )

    def inv(
        self,
        a: np.ndarray,
    ) -> np.ndarray:
        self(a, inverse=1)
        a /= a.size
