import cmath


class FFT:
    def __butterfly(
        self,
    ) -> None:
        n = self.__n
        a = self.__a
        b = 1
        sign = -1 + 2 * self.__inv
        while b < n:
            for j in range(b):
                w = cmath.rect(1.0, sign * cmath.pi / b * j)
                k = 0
                while k < n:
                    s, t = a[k + j], a[k + j + b] * w
                    a[k + j], a[k + j + b] = s + t, s - t
                    k += 2 * b
            b <<= 1

    def __call__(
        self,
        a: list[complex],
    ) -> list[complex]:
        n = len(a)
        h = n.bit_length() - 1
        assert 1 << h == n
        self.__a = a
        self.__n, self.__h = n, h
        self.__reverse_bits()
        self.__butterfly()
        a = self.__a
        if self.__inv:
            for i in range(n):
                a[i] /= n
        return a

    def __init__(
        self,
        inverse: bool = False,
    ) -> None:
        self.__inv = inverse

    def __reverse_bits(
        self,
    ) -> None:
        a = self.__a
        n, h = self.__n, self.__h
        idx = [-1] * n
        for i in range(n):
            j = 0
            for k in range(h):
                j |= (i >> k & 1) << (h - 1 - k)
            idx[i] = j
        self.__a = [a[i] for i in idx]
