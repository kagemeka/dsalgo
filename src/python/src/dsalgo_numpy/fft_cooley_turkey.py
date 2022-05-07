import numpy as np


class FFT:
    def __butterfly(
        self,
    ) -> None:
        n = self.__n
        a = self.__a
        b = 1
        sign = -1 + 2 * self.__inv
        while b < n:
            j = np.arange(b)
            w = np.exp(sign * np.pi / b * j * 1j)
            k = np.arange(0, n, 2 * b)[:, None]
            s, t = a[k + j], a[k + j + b] * w
            a[k + j], a[k + j + b] = s + t, s - t
            b <<= 1

    def __call__(
        self,
        a: np.ndarray,
    ) -> np.ndarray:
        self.__a = a.astype(np.complex128)
        n = a.size
        h = n.bit_length() - 1
        assert 1 << h == n
        self.__n, self.__h = n, h
        self.__reverse_bits()
        self.__butterfly()
        a = self.__a
        if self.__inv:
            a /= n
        return a

    def __init__(
        self,
        inverse: bool = False,
    ) -> None:
        self.__inv = inverse

    def __reverse_bits(
        self,
    ) -> None:
        i = np.arange(self.__n)
        h = self.__h
        bits = i[:, None] >> np.arange(h) & 1
        j = (bits[:, ::-1] * (1 << np.arange(h))).sum(axis=1)
        self.__a = self.__a[j]
