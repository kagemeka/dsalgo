import numpy as np


class BitwiseMatUtil:
    def __init__(
        self,
        dtype: np.dtype = np.uint32,
    ):
        self.dtype = dtype

    @property
    def mask(self):
        return np.iinfo(
            self.dtype,
        ).max

    @property
    def mul_identity(
        self,
    ):
        e = np.identity(
            self.n,
            dtype=self.dtype,
        )
        np.fill_diagonal(
            e,
            self.mask,
        )
        return e

    @staticmethod
    def dot(
        a: np.ndarray,
        b: np.ndarray,
    ) -> np.ndarray:
        c = np.bitwise_xor.reduce(
            a[:, None, :] & b.T[None, ...],
            axis=-1,
        )
        return c

    def pow(
        self,
        a: np.ndarray,
        n: int,
    ) -> np.ndarray:
        if n == 0:
            self.n = a.shape[0]
            return self.mul_identity
        x = self.pow(a, n >> 1)
        x = self.dot(x, x)
        if n & 1:
            x = self.dot(x, a)
        return x
